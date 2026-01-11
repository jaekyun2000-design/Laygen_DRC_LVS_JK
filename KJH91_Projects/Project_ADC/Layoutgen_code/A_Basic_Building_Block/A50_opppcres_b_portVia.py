from KJH91_Projects.Project_ADC.Library_and_Engine import StickDiagram_KJH1, DesignParameters
from KJH91_Projects.Project_ADC.Library_and_Engine import DRC_EGFET
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A02_ViaStack_KJH2_YCH

import numpy as np
import copy
import math

class _Opppcres_b(StickDiagram_KJH1._StickDiagram_KJH):

    _ParametersForDesignCalculation = dict(
        _ResWidth=None,
        _ResLength=None,
        _CONUMX=None,
        _CONUMY=None,
        _SeriesStripes=None,
        _ParallelStripes=None,
        _Port1Layer=None,
        _Port2Layer=None,
    )

    def __init__(self, _DesignParameter=None, _Name=None):
        if _DesignParameter != None:
            self._DesignParameter = _DesignParameter
        else:
            self._DesignParameter = dict(
                _Name=self._NameDeclaration(_Name=_Name),
                _GDSFile=self._GDSObjDeclaration(_GDSFile=None),
                _XYcoordAsCent=dict(_XYcoordAsCent=0),
                _XYCoordinatePort1Routing=dict(_DesignParametertype=7, _XYCoordinates=[]),
                _XYCoordinatePort2Routing=dict(_DesignParametertype=7, _XYCoordinates=[]),
            )

        ## ################################################################################################################################################ _CalculateDesignParameter
    def _CalculateDesignParameter(self,
                                    _ResWidth=None,
                                    _ResLength=None,
                                    _CONUMX=None,
                                    _CONUMY=None,
                                    _SeriesStripes=None,
                                    _ParallelStripes=None,
                                    _Port1Layer=None,
                                    _Port2Layer=None,
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

        MinSnapSpacing = _DRCObj._MinSnapSpacing

        _XYCoordinateOfOPRES_Center = []

        if _ResWidth % 2 == 0 and _ResLength % 2 == 0:
            _XYCoordinateOfOPRES = [[0, 0]]
        elif _ResWidth % 2 == 0 and _ResLength % 2 == 1:
            _XYCoordinateOfOPRES = [[0, MinSnapSpacing / 2.0]]
        elif _ResWidth % 2 == 1 and _ResLength % 2 == 0:
            _XYCoordinateOfOPRES = [[MinSnapSpacing / 2.0, 0]]
        elif _ResWidth % 2 == 1 and _ResLength % 2 == 1:
            _XYCoordinateOfOPRES = [[MinSnapSpacing / 2.0, MinSnapSpacing / 2.0]]

        if _ResWidth % (2 * MinSnapSpacing) != 0 or _ResLength % (2 * MinSnapSpacing) != 0:
            raise Exception("Only even number can be generated")

        if _SeriesStripes == None or _ParallelStripes == None:
            raise Exception("<_SeriesStripes> and <_ParallelStripes> should be at least 1")

        if _SeriesStripes > 1 and _ParallelStripes > 1:
            raise Exception("<_SeriesStripes> or <_ParallelStripes>, only one of the two options is possible.")
        elif _SeriesStripes > 1 or _ParallelStripes > 1:
            NumofPolyLayer = max(_SeriesStripes, _ParallelStripes)
            for i in range(0, NumofPolyLayer - 1):
                _XYCoordinateOfOPRES.append([_XYCoordinateOfOPRES[i][0] + _ResWidth + _DRCObj._PolygateMinSpace, _XYCoordinateOfOPRES[0][0]])

        else:
            NumofPolyLayer = 1
        for i in range(0, NumofPolyLayer):
            _XYCoordinateOfOPRES_Center.append([_XYCoordinateOfOPRES[i][0] + _ResWidth / 2,_XYCoordinateOfOPRES[i][1] + (_ResLength + _DRCObj._PolyoverOPlayer * 2) / 2])

        print('#############################     POLY Layer Calculation    ##############################################')
        # Define Boundary_element
        self._DesignParameter['_POLayer'] = self._BoundaryElementDeclaration(
                                                                                _Layer=DesignParameters._LayerMapping['POLY'][0],
                                                                                _Datatype=DesignParameters._LayerMapping['POLY'][1],
                                                                                _XWidth=None,
                                                                                _YWidth=None,
                                                                                _XYCoordinates=[],
        )
        self._DesignParameter['_POLayer']['_XWidth'] = _ResWidth
        self._DesignParameter['_POLayer']['_YWidth'] = _ResLength + _DRCObj._PolyoverOPlayer * 2
        self._DesignParameter['_POLayer']['_XYCoordinates'] = _XYCoordinateOfOPRES


        print('#############################     PRES Layer Calculation    ##############################################')
        self._DesignParameter['_PRESLayer'] = self._BoundaryElementDeclaration(
                                                                                _Layer=DesignParameters._LayerMapping['PRES'][0],
                                                                                _Datatype=DesignParameters._LayerMapping['PRES'][1],
                                                                                _XWidth=None,
                                                                                _YWidth=None,
                                                                                _XYCoordinates=[],
        )
        self._DesignParameter['_PRESLayer']['_XWidth'] = _ResWidth * NumofPolyLayer + _DRCObj._PolygateMinSpace * (NumofPolyLayer - 1) + _DRCObj._PRESlayeroverPoly * 2
        self._DesignParameter['_PRESLayer']['_YWidth'] = self._DesignParameter['_POLayer']['_YWidth'] + _DRCObj._PRESlayeroverPoly * 2
        self._DesignParameter['_PRESLayer']['_XYCoordinates'] = [[0,0]]

        tmpXY = []
        # Target_coord
        tmp1 = self.get_param_KJH4( '_POLayer')
        target_coordx = abs ((tmp1[-1][0]['_XY_right'][0]-tmp1[0][0]['_XY_left'][0])/2)
        target_coordy = abs ((tmp1[0][0]['_XY_up'][1]-tmp1[0][0]['_XY_down'][1])/2)
        target_coord = [target_coordx, target_coordy]
        # Approaching_coord
        tmp2 = self.get_param_KJH4('_PRESLayer')
        approaching_coord = tmp2[0][0]['_XY_cent']
        # Sref coord
        tmp3 = self.get_param_KJH4('_PRESLayer')
        Scoord = tmp3[0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)

        tmpXY.append(New_Scoord)
        # Define
        self._DesignParameter['_PRESLayer']['_XYCoordinates'] = tmpXY


        print('#############################     PIMP Layer Calculation    ##############################################')
        self._DesignParameter['_PPLayer'] = self._BoundaryElementDeclaration(
                                                                                    _Layer=DesignParameters._LayerMapping['PIMP'][0],
                                                                                    _Datatype=DesignParameters._LayerMapping['PIMP'][1],
                                                                                    _XWidth=None,
                                                                                    _YWidth=None,
                                                                                    _XYCoordinates=[],
        )
        self._DesignParameter['_PPLayer']['_XWidth'] = self._DesignParameter['_PRESLayer']['_XWidth']
        self._DesignParameter['_PPLayer']['_YWidth'] = self._DesignParameter['_PRESLayer']['_YWidth']
        self._DesignParameter['_PPLayer']['_XYCoordinates'] = self._DesignParameter['_PRESLayer']['_XYCoordinates']


        print('#############################     OP Layer Calculation    ################################################')
        self._DesignParameter['_OPLayer'] = self._BoundaryElementDeclaration(
                                                                                    _Layer=DesignParameters._LayerMapping['OP'][0],
                                                                                    _Datatype=DesignParameters._LayerMapping['OP'][1],
                                                                                    _XWidth=None,
                                                                                    _YWidth=None,
                                                                                    _XYCoordinates=[],
        )
        self._DesignParameter['_OPLayer']['_XWidth'] = _ResWidth * NumofPolyLayer + _DRCObj._PolygateMinSpace * (NumofPolyLayer - 1) + _DRCObj._OPlayeroverPoly * 2
        self._DesignParameter['_OPLayer']['_YWidth'] = _ResLength
        if _ResLength < _DRCObj._PolyoverOPlayer:
            raise NotImplementedError
        self._DesignParameter['_OPLayer']['_XYCoordinates'] = [[0,0]]

        tmpXY = []

        # Target_coord
        tmp1 = self.get_param_KJH4('_PRESLayer')
        target_coord = tmp1[0][0]['_XY_cent']
        # Approaching_coord
        tmp2 = self.get_param_KJH4('_OPLayer')
        approaching_coord = tmp2[0][0]['_XY_cent']
        # Sref coord
        tmp3 = self.get_param_KJH4('_OPLayer')
        Scoord = tmp3[0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)

        tmpXY.append(New_Scoord)
        # Define
        self._DesignParameter['_OPLayer']['_XYCoordinates'] = tmpXY


        print('#############################     CONT Layer Calculation    ##############################################')
        self._DesignParameter['_COLayer'] = self._BoundaryElementDeclaration(
                                                                                    _Layer=DesignParameters._LayerMapping['CONT'][0],
                                                                                    _Datatype=DesignParameters._LayerMapping['CONT'][1],
                                                                                    _XWidth=None,
                                                                                    _YWidth=None,
                                                                                    _XYCoordinates=[],
        )
        self._DesignParameter['_COLayer']['_XWidth'] = _DRCObj._CoMinWidth
        self._DesignParameter['_COLayer']['_YWidth'] = _DRCObj._CoMinWidth

        tmp = []
        _CONUMXmax = int((self._DesignParameter['_POLayer']['_XWidth'] - _DRCObj._CoMinEnclosureByPO2 * 2 - _DRCObj._CoMinWidth + 4) // (
                        _DRCObj._CoMinWidth + _DRCObj._CoMinSpace)) + 1
        _CONUMYmax = int((int((self._DesignParameter['_POLayer']['_YWidth'] - self._DesignParameter['_OPLayer'][
            '_YWidth'] - 2 * _DRCObj._CoMinSpace2OP - 2 * _DRCObj._CoMinEnclosureByPO2) // (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2)) + 1) // 2)

        if DesignParameters._Technology != '028nm':
            _CONUMYmax = 3

        if _CONUMX == None:
            _CONUMX = _CONUMXmax
        if _CONUMY == None:
            _CONUMY = _CONUMYmax
            if DesignParameters._Technology == '028nm': # 수정 부분
                _CONUMY = 1

        if _CONUMY > 1:
            _CONUMX = int((self._DesignParameter['_POLayer']['_XWidth'] - _DRCObj._CoMinEnclosureByPO2 * 2 - _DRCObj._CoMinWidth) // (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2)) + 1

        if _CONUMX > _CONUMXmax or _CONUMY > _CONUMYmax:
            raise NotImplementedError


        for k in range(0, NumofPolyLayer):
            if _CONUMY == 1:
                if _ResWidth % 2 == 0 and _ResLength % 2 == 0:
                    for i in range(0, _CONUMX):
                        for j in range(0, _CONUMY):
                            if (_CONUMX % 2 == 0):
                                tmp.append([_XYCoordinateOfOPRES_Center[k][0] - (_CONUMX // 2 - 0.5) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace) + i * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace)-_DRCObj._CoMinWidth/2,
                                            _XYCoordinateOfOPRES_Center[k][1] - (self._DesignParameter['_OPLayer']['_YWidth'] // 2 + _DRCObj._CoMinSpace2OP + 0.5 * _DRCObj._CoMinWidth) - j * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace)-_DRCObj._CoMinWidth/2])
                                tmp.append([_XYCoordinateOfOPRES_Center[k][0] - (_CONUMX // 2 - 0.5) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace) + i * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace)-_DRCObj._CoMinWidth/2,
                                            _XYCoordinateOfOPRES_Center[k][1] + (self._DesignParameter['_OPLayer']['_YWidth'] // 2 + _DRCObj._CoMinSpace2OP + 0.5 * _DRCObj._CoMinWidth) + j * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace)-_DRCObj._CoMinWidth/2])
                            else:
                                tmp.append([_XYCoordinateOfOPRES_Center[k][0] - (_CONUMX // 2) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace) + i * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace)-_DRCObj._CoMinWidth/2,
                                            _XYCoordinateOfOPRES_Center[k][1] - (self._DesignParameter['_OPLayer']['_YWidth'] // 2 + _DRCObj._CoMinSpace2OP + 0.5 * _DRCObj._CoMinWidth) - j * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace)-_DRCObj._CoMinWidth/2])
                                tmp.append([_XYCoordinateOfOPRES_Center[k][0] - (_CONUMX // 2) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace) + i * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace)-_DRCObj._CoMinWidth/2,
                                            _XYCoordinateOfOPRES_Center[k][1] + (self._DesignParameter['_OPLayer']['_YWidth'] // 2 + _DRCObj._CoMinSpace2OP + 0.5 * _DRCObj._CoMinWidth) + j * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace)-_DRCObj._CoMinWidth/2])

                elif _ResWidth % 2 == 0 and _ResLength % 2 == 1:
                    for i in range(0, _CONUMX):
                        for j in range(0, _CONUMY):
                            if (_CONUMX % 2 == 0):
                                tmp.append([_XYCoordinateOfOPRES_Center[k][0] - (_CONUMX // 2 - 0.5) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace) + i * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace)-_DRCObj._CoMinWidth/2,
                                            _XYCoordinateOfOPRES_Center[k][1] - MinSnapSpacing / 2.0 - (self._DesignParameter['_OPLayer']['_YWidth'] // 2 + _DRCObj._CoMinSpace2OP + 0.5 * _DRCObj._CoMinWidth) - j * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace)]-_DRCObj._CoMinWidth/2)
                                tmp.append([_XYCoordinateOfOPRES_Center[k][0] - (_CONUMX // 2 - 0.5) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace) + i * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace)-_DRCObj._CoMinWidth/2,
                                            _XYCoordinateOfOPRES_Center[k][1] + MinSnapSpacing / 2.0 + (self._DesignParameter['_OPLayer']['_YWidth'] // 2 + _DRCObj._CoMinSpace2OP + 0.5 * _DRCObj._CoMinWidth) + j * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace)-_DRCObj._CoMinWidth/2])
                            else:
                                tmp.append([_XYCoordinateOfOPRES_Center[k][0] - (_CONUMX // 2) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace) + i * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace)-_DRCObj._CoMinWidth/2,
                                            _XYCoordinateOfOPRES_Center[k][1] - MinSnapSpacing / 2.0 - (self._DesignParameter['_OPLayer']['_YWidth'] // 2 + _DRCObj._CoMinSpace2OP + 0.5 * _DRCObj._CoMinWidth) - j * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace)-_DRCObj._CoMinWidth/2])
                                tmp.append([_XYCoordinateOfOPRES_Center[k][0] - (_CONUMX // 2) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace) + i * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace)-_DRCObj._CoMinWidth/2,
                                            _XYCoordinateOfOPRES_Center[k][1] + MinSnapSpacing / 2.0 + (self._DesignParameter['_OPLayer']['_YWidth'] // 2 + _DRCObj._CoMinSpace2OP + 0.5 * _DRCObj._CoMinWidth) + j * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace)-_DRCObj._CoMinWidth/2])

                elif _ResWidth % 2 == 1 and _ResLength % 2 == 0:
                    for i in range(0, _CONUMX):
                        for j in range(0, _CONUMY):
                            if (_CONUMX % 2 == 0):
                                tmp.append([_XYCoordinateOfOPRES_Center[k][0] + MinSnapSpacing / 2.0 - (_CONUMX // 2 - 0.5) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace) + i * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace)-_DRCObj._CoMinWidth/2,
                                            _XYCoordinateOfOPRES_Center[k][1] - (self._DesignParameter['_OPLayer']['_YWidth'] // 2 + _DRCObj._CoMinSpace2OP + 0.5 * _DRCObj._CoMinWidth) - j * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace)-_DRCObj._CoMinWidth/2])
                                tmp.append([_XYCoordinateOfOPRES_Center[k][0] + MinSnapSpacing / 2.0 - (_CONUMX // 2 - 0.5) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace) + i * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace)-_DRCObj._CoMinWidth/2,
                                            _XYCoordinateOfOPRES_Center[k][1] + (self._DesignParameter['_OPLayer']['_YWidth'] // 2 + _DRCObj._CoMinSpace2OP + 0.5 * _DRCObj._CoMinWidth) + j * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace)-_DRCObj._CoMinWidth/2])
                            else:
                                tmp.append([_XYCoordinateOfOPRES_Center[k][0] + MinSnapSpacing / 2.0 - (_CONUMX // 2) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace) + i * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace)-_DRCObj._CoMinWidth/2,
                                            _XYCoordinateOfOPRES_Center[k][1] - (self._DesignParameter['_OPLayer']['_YWidth'] // 2 + _DRCObj._CoMinSpace2OP + 0.5 * _DRCObj._CoMinWidth) - j * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace)-_DRCObj._CoMinWidth/2])
                                tmp.append([_XYCoordinateOfOPRES_Center[k][0] + MinSnapSpacing / 2.0 - (_CONUMX // 2) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace) + i * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace)-_DRCObj._CoMinWidth/2,
                                            _XYCoordinateOfOPRES_Center[k][1] + (self._DesignParameter['_OPLayer']['_YWidth'] // 2 + _DRCObj._CoMinSpace2OP + 0.5 * _DRCObj._CoMinWidth) + j * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace)-_DRCObj._CoMinWidth/2])

                elif _ResWidth % 2 == 1 and _ResLength % 2 == 1:
                    for i in range(0, _CONUMX):
                        for j in range(0, _CONUMY):
                            if (_CONUMX % 2 == 0):
                                tmp.append([_XYCoordinateOfOPRES_Center[k][0] + MinSnapSpacing / 2.0 - (_CONUMX // 2 - 0.5) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace) + i * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace)-_DRCObj._CoMinWidth/2,
                                            _XYCoordinateOfOPRES_Center[k][1] - self.CeilMinSnapSpacing((self._DesignParameter['_OPLayer']['_YWidth'] / 2 + _DRCObj._CoMinSpace2OP + 0.5 * _DRCObj._CoMinWidth), MinSnapSpacing / 2) - j * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace)-_DRCObj._CoMinWidth/2])
                                tmp.append([_XYCoordinateOfOPRES_Center[k][0] + MinSnapSpacing / 2.0 - (_CONUMX // 2 - 0.5) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace) + i * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace)-_DRCObj._CoMinWidth/2,
                                            _XYCoordinateOfOPRES_Center[k][1] + self.CeilMinSnapSpacing((self._DesignParameter['_OPLayer']['_YWidth'] / 2 + _DRCObj._CoMinSpace2OP + 0.5 * _DRCObj._CoMinWidth), MinSnapSpacing / 2) + j * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace)-_DRCObj._CoMinWidth/2])
                            else:
                                tmp.append([_XYCoordinateOfOPRES_Center[k][0] + MinSnapSpacing / 2.0 - (_CONUMX // 2) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace) + i * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace)-_DRCObj._CoMinWidth/2,
                                            _XYCoordinateOfOPRES_Center[k][1] - self.CeilMinSnapSpacing((self._DesignParameter['_OPLayer']['_YWidth'] / 2 + _DRCObj._CoMinSpace2OP + 0.5 * _DRCObj._CoMinWidth),
                                                                                                 MinSnapSpacing / 2) - j * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace)-_DRCObj._CoMinWidth/2])
                                tmp.append([_XYCoordinateOfOPRES_Center[k][0] + MinSnapSpacing / 2.0 - (_CONUMX // 2) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace) + i * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace)-_DRCObj._CoMinWidth/2,
                                            _XYCoordinateOfOPRES_Center[k][1] + self.CeilMinSnapSpacing((self._DesignParameter['_OPLayer']['_YWidth'] / 2 + _DRCObj._CoMinSpace2OP + 0.5 * _DRCObj._CoMinWidth),
                                                                                                 MinSnapSpacing / 2) + j * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace)-_DRCObj._CoMinWidth/2])

            else:
                if _ResWidth % 2 == 0 and _ResLength % 2 == 0:
                    for i in range(0, _CONUMX):
                        for j in range(0, _CONUMY):
                            if (_CONUMX % 2 == 0):
                                tmp.append([_XYCoordinateOfOPRES_Center[k][0] - (_CONUMX // 2 - 0.5) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2) + i * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2)-_DRCObj._CoMinWidth/2,
                                            _XYCoordinateOfOPRES_Center[k][1] - (self._DesignParameter['_OPLayer']['_YWidth'] // 2 + _DRCObj._CoMinSpace2OP + 0.5 * _DRCObj._CoMinWidth) - j * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2)-_DRCObj._CoMinWidth/2])
                                tmp.append([_XYCoordinateOfOPRES_Center[k][0] - (_CONUMX // 2 - 0.5) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2) + i * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2)-_DRCObj._CoMinWidth/2,
                                            _XYCoordinateOfOPRES_Center[k][1] + (self._DesignParameter['_OPLayer']['_YWidth'] // 2 + _DRCObj._CoMinSpace2OP + 0.5 * _DRCObj._CoMinWidth) + j * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2)-_DRCObj._CoMinWidth/2])
                            else:
                                tmp.append([_XYCoordinateOfOPRES_Center[k][0] - (_CONUMX // 2) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2) + i * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2)-_DRCObj._CoMinWidth/2,
                                            _XYCoordinateOfOPRES_Center[k][1] - (self._DesignParameter['_OPLayer']['_YWidth'] // 2 + _DRCObj._CoMinSpace2OP + 0.5 * _DRCObj._CoMinWidth) - j * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2)-_DRCObj._CoMinWidth/2])
                                tmp.append([_XYCoordinateOfOPRES_Center[k][0] - (_CONUMX // 2) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2) + i * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2)-_DRCObj._CoMinWidth/2,
                                            _XYCoordinateOfOPRES_Center[k][1] + (self._DesignParameter['_OPLayer']['_YWidth'] // 2 + _DRCObj._CoMinSpace2OP + 0.5 * _DRCObj._CoMinWidth) + j * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2)-_DRCObj._CoMinWidth/2])

                elif _ResWidth % 2 == 0 and _ResLength % 2 == 1:
                    for i in range(0, _CONUMX):
                        for j in range(0, _CONUMY):
                            if (_CONUMX % 2 == 0):
                                tmp.append([_XYCoordinateOfOPRES_Center[k][0] - (_CONUMX // 2 - 0.5) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2) + i * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2)-_DRCObj._CoMinWidth/2,
                                            _XYCoordinateOfOPRES_Center[k][1] - 0.5 - (self._DesignParameter['_OPLayer']['_YWidth'] // 2 + _DRCObj._CoMinSpace2OP + 0.5 * _DRCObj._CoMinWidth) - j * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2)-_DRCObj._CoMinWidth/2])
                                tmp.append([_XYCoordinateOfOPRES_Center[k][0] - (_CONUMX // 2 - 0.5) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2) + i * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2)-_DRCObj._CoMinWidth/2,
                                            _XYCoordinateOfOPRES_Center[k][1] + 0.5 + (self._DesignParameter['_OPLayer']['_YWidth'] // 2 + _DRCObj._CoMinSpace2OP + 0.5 * _DRCObj._CoMinWidth) + j * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2)-_DRCObj._CoMinWidth/2])
                            else:
                                tmp.append([_XYCoordinateOfOPRES_Center[k][0] - (_CONUMX // 2) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2) + i * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2)-_DRCObj._CoMinWidth/2,
                                            _XYCoordinateOfOPRES_Center[k][1] - 0.5 - (self._DesignParameter['_OPLayer']['_YWidth'] // 2 + _DRCObj._CoMinSpace2OP + 0.5 * _DRCObj._CoMinWidth) - j * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2)-_DRCObj._CoMinWidth/2])
                                tmp.append([_XYCoordinateOfOPRES_Center[k][0] - (_CONUMX // 2) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2) + i * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2)-_DRCObj._CoMinWidth/2,
                                            _XYCoordinateOfOPRES_Center[k][1] + 0.5 + (self._DesignParameter['_OPLayer']['_YWidth'] // 2 + _DRCObj._CoMinSpace2OP + 0.5 * _DRCObj._CoMinWidth) + j * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2)-_DRCObj._CoMinWidth/2])

                elif _ResWidth % 2 == 1 and _ResLength % 2 == 0:
                    for i in range(0, _CONUMX):
                        for j in range(0, _CONUMY):
                            if (_CONUMX % 2 == 0):
                                tmp.append([_XYCoordinateOfOPRES_Center[k][0] + 0.5 - (_CONUMX // 2 - 0.5) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2) + i * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2)-_DRCObj._CoMinWidth/2,
                                            _XYCoordinateOfOPRES_Center[k][1] - (self._DesignParameter['_OPLayer']['_YWidth'] // 2 + _DRCObj._CoMinSpace2OP + 0.5 * _DRCObj._CoMinWidth) - j * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2)-_DRCObj._CoMinWidth/2])
                                tmp.append([_XYCoordinateOfOPRES_Center[k][0] + 0.5 - (_CONUMX // 2 - 0.5) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2) + i * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2)-_DRCObj._CoMinWidth/2,
                                            _XYCoordinateOfOPRES_Center[k][1] + (self._DesignParameter['_OPLayer']['_YWidth'] // 2 + _DRCObj._CoMinSpace2OP + 0.5 * _DRCObj._CoMinWidth) + j * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2)-_DRCObj._CoMinWidth/2])
                            else:
                                tmp.append([_XYCoordinateOfOPRES_Center[k][0] + 0.5 - (_CONUMX // 2) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2) + i * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2)-_DRCObj._CoMinWidth/2,
                                            _XYCoordinateOfOPRES_Center[k][1] - (self._DesignParameter['_OPLayer']['_YWidth'] // 2 + _DRCObj._CoMinSpace2OP + 0.5 * _DRCObj._CoMinWidth) - j * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2)-_DRCObj._CoMinWidth/2])
                                tmp.append([_XYCoordinateOfOPRES_Center[k][0] + 0.5 - (_CONUMX // 2) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2) + i * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2)-_DRCObj._CoMinWidth/2,
                                            _XYCoordinateOfOPRES_Center[k][1] + (self._DesignParameter['_OPLayer']['_YWidth'] // 2 + _DRCObj._CoMinSpace2OP + 0.5 * _DRCObj._CoMinWidth) + j * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2)-_DRCObj._CoMinWidth/2])

                elif _ResWidth % 2 == 1 and _ResLength % 2 == 1:
                    for i in range(0, _CONUMX):
                        for j in range(0, _CONUMY):
                            if (_CONUMX % 2 == 0):
                                tmp.append([_XYCoordinateOfOPRES_Center[k][0] + 0.5 - (_CONUMX // 2 - 0.5) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2) + i * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2)-_DRCObj._CoMinWidth/2,
                                            _XYCoordinateOfOPRES_Center[k][1] - 0.5 - (self._DesignParameter['_OPLayer']['_YWidth'] // 2 + _DRCObj._CoMinSpace2OP + 0.5 * _DRCObj._CoMinWidth) - j * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2)-_DRCObj._CoMinWidth/2])
                                tmp.append([_XYCoordinateOfOPRES_Center[k][0] + 0.5 - (_CONUMX // 2 - 0.5) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2) + i * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2)-_DRCObj._CoMinWidth/2,
                                            _XYCoordinateOfOPRES_Center[k][1] + 0.5 + (self._DesignParameter['_OPLayer']['_YWidth'] // 2 + _DRCObj._CoMinSpace2OP + 0.5 * _DRCObj._CoMinWidth) + j * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2)-_DRCObj._CoMinWidth/2])
                            else:
                                tmp.append([_XYCoordinateOfOPRES_Center[k][0] + 0.5 - (_CONUMX // 2) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2) + i * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2)-_DRCObj._CoMinWidth/2,
                                            _XYCoordinateOfOPRES_Center[k][1] - 0.5 - (self._DesignParameter['_OPLayer']['_YWidth'] // 2 + _DRCObj._CoMinSpace2OP + 0.5 * _DRCObj._CoMinWidth) - j * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2)-_DRCObj._CoMinWidth/2])
                                tmp.append([_XYCoordinateOfOPRES_Center[k][0] + 0.5 - (_CONUMX // 2) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2) + i * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2)-_DRCObj._CoMinWidth/2,
                                            _XYCoordinateOfOPRES_Center[k][1] + 0.5 + (self._DesignParameter['_OPLayer']['_YWidth'] // 2 + _DRCObj._CoMinSpace2OP + 0.5 * _DRCObj._CoMinWidth) + j * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2)-_DRCObj._CoMinWidth/2])

        self._DesignParameter['_COLayer']['_XYCoordinates'] = tmp



        print ('#########################     Port1 Routing Coordinates Calculation    ####################################')
        tmp = []
        for k in range(0, NumofPolyLayer):
            if _CONUMY == 1:
                if _ResWidth % 2 == 0 and _ResLength % 2 == 0:
                    tmp.append([_XYCoordinateOfOPRES_Center[k][0], _XYCoordinateOfOPRES_Center[k][1] - (
                                self._DesignParameter['_OPLayer']['_YWidth'] // 2 + _DRCObj._CoMinSpace2OP +
                                (_CONUMY - 1) * (
                                            _DRCObj._CoMinWidth + _DRCObj._CoMinSpace) // 2 + _DRCObj._CoMinWidth // 2)])

                if _ResWidth % 2 == 0 and _ResLength % 2 == 1:
                    tmp.append([_XYCoordinateOfOPRES_Center[k][0], _XYCoordinateOfOPRES_Center[k][1] - 0.5 - (
                                self._DesignParameter['_OPLayer']['_YWidth'] // 2 + _DRCObj._CoMinSpace2OP +
                                (_CONUMY - 1) * (
                                            _DRCObj._CoMinWidth + _DRCObj._CoMinSpace) // 2 + _DRCObj._CoMinWidth // 2)])

                if _ResWidth % 2 == 1 and _ResLength % 2 == 0:
                    tmp.append([_XYCoordinateOfOPRES_Center[k][0], _XYCoordinateOfOPRES_Center[k][1] - (
                                self._DesignParameter['_OPLayer']['_YWidth'] // 2 + _DRCObj._CoMinSpace2OP +
                                (_CONUMY - 1) * (
                                            _DRCObj._CoMinWidth + _DRCObj._CoMinSpace) // 2 + _DRCObj._CoMinWidth // 2)])

                if _ResWidth % 2 == 1 and _ResLength % 2 == 1:
                    tmp.append([_XYCoordinateOfOPRES_Center[k][0], _XYCoordinateOfOPRES_Center[k][1] - 0.5 - (
                                self._DesignParameter['_OPLayer']['_YWidth'] // 2 + _DRCObj._CoMinSpace2OP +
                                (_CONUMY - 1) * (
                                            _DRCObj._CoMinWidth + _DRCObj._CoMinSpace) // 2 + _DRCObj._CoMinWidth // 2)])

            else:
                if _ResWidth % 2 == 0 and _ResLength % 2 == 0:
                    tmp.append([_XYCoordinateOfOPRES_Center[k][0], _XYCoordinateOfOPRES_Center[k][1] - (
                                self._DesignParameter['_OPLayer']['_YWidth'] // 2 + _DRCObj._CoMinSpace2OP +
                                (_CONUMY - 1) * (
                                            _DRCObj._CoMinWidth + _DRCObj._CoMinSpace2) // 2 + _DRCObj._CoMinWidth // 2)])

                if _ResWidth % 2 == 0 and _ResLength % 2 == 1:
                    tmp.append([_XYCoordinateOfOPRES_Center[k][0], _XYCoordinateOfOPRES_Center[k][1] - 0.5 - (
                                self._DesignParameter['_OPLayer']['_YWidth'] // 2 + _DRCObj._CoMinSpace2OP +
                                (_CONUMY - 1) * (
                                            _DRCObj._CoMinWidth + _DRCObj._CoMinSpace2) // 2 + _DRCObj._CoMinWidth // 2)])

                if _ResWidth % 2 == 1 and _ResLength % 2 == 0:
                    tmp.append([_XYCoordinateOfOPRES_Center[k][0], _XYCoordinateOfOPRES_Center[k][1] - (
                                self._DesignParameter['_OPLayer']['_YWidth'] // 2 + _DRCObj._CoMinSpace2OP +
                                (_CONUMY - 1) * (
                                            _DRCObj._CoMinWidth + _DRCObj._CoMinSpace2) // 2 + _DRCObj._CoMinWidth // 2)])

                if _ResWidth % 2 == 1 and _ResLength % 2 == 1:
                    tmp.append([_XYCoordinateOfOPRES_Center[k][0], _XYCoordinateOfOPRES_Center[k][1] - 0.5 - (
                                self._DesignParameter['_OPLayer']['_YWidth'] // 2 + _DRCObj._CoMinSpace2OP +
                                (_CONUMY - 1) * (
                                            _DRCObj._CoMinWidth + _DRCObj._CoMinSpace2) // 2 + _DRCObj._CoMinWidth // 2)])

        self._DesignParameter['_XYCoordinatePort1Routing']['_XYCoordinates'] = tmp
        # del tmp


        print( '#########################     Port2 Routing Coordinates Calculation    ####################################')
        tmp = []
        for k in range(0, NumofPolyLayer):
            if _CONUMY == 1:
                if _ResWidth % 2 == 0 and _ResLength % 2 == 0:
                    tmp.append([_XYCoordinateOfOPRES_Center[k][0], _XYCoordinateOfOPRES_Center[k][1] + (
                                self._DesignParameter['_OPLayer']['_YWidth'] // 2 + _DRCObj._CoMinSpace2OP +
                                (_CONUMY - 1) * (
                                            _DRCObj._CoMinWidth + _DRCObj._CoMinSpace) // 2 + _DRCObj._CoMinWidth // 2)])

                if _ResWidth % 2 == 1 and _ResLength % 2 == 0:
                    tmp.append([_XYCoordinateOfOPRES_Center[k][0], _XYCoordinateOfOPRES_Center[k][1] + (
                                self._DesignParameter['_OPLayer']['_YWidth'] // 2 + _DRCObj._CoMinSpace2OP +
                                (_CONUMY - 1) * (
                                            _DRCObj._CoMinWidth + _DRCObj._CoMinSpace) // 2 + _DRCObj._CoMinWidth // 2)])

                if _ResWidth % 2 == 0 and _ResLength % 2 == 1:
                    tmp.append([_XYCoordinateOfOPRES_Center[k][0], _XYCoordinateOfOPRES_Center[k][1] + 0.5 + (
                                self._DesignParameter['_OPLayer']['_YWidth'] // 2 + _DRCObj._CoMinSpace2OP +
                                (_CONUMY - 1) * (
                                            _DRCObj._CoMinWidth + _DRCObj._CoMinSpace) // 2 + _DRCObj._CoMinWidth // 2)])

                if _ResWidth % 2 == 1 and _ResLength % 2 == 1:
                    tmp.append([_XYCoordinateOfOPRES_Center[k][0], _XYCoordinateOfOPRES_Center[k][1] + 0.5 + (
                                self._DesignParameter['_OPLayer']['_YWidth'] // 2 + _DRCObj._CoMinSpace2OP +
                                (_CONUMY - 1) * (
                                            _DRCObj._CoMinWidth + _DRCObj._CoMinSpace) // 2 + _DRCObj._CoMinWidth // 2)])

            else:
                if _ResWidth % 2 == 0 and _ResLength % 2 == 0:
                    tmp.append([_XYCoordinateOfOPRES_Center[k][0], _XYCoordinateOfOPRES_Center[k][1] + (
                                self._DesignParameter['_OPLayer']['_YWidth'] // 2 + _DRCObj._CoMinSpace2OP +
                                (_CONUMY - 1) * (
                                            _DRCObj._CoMinWidth + _DRCObj._CoMinSpace2) // 2 + _DRCObj._CoMinWidth // 2)])

                if _ResWidth % 2 == 1 and _ResLength % 2 == 0:
                    tmp.append([_XYCoordinateOfOPRES_Center[k][0], _XYCoordinateOfOPRES_Center[k][1] + (
                                self._DesignParameter['_OPLayer']['_YWidth'] // 2 + _DRCObj._CoMinSpace2OP +
                                (_CONUMY - 1) * (
                                            _DRCObj._CoMinWidth + _DRCObj._CoMinSpace2) // 2 + _DRCObj._CoMinWidth // 2)])

                if _ResWidth % 2 == 0 and _ResLength % 2 == 1:
                    tmp.append([_XYCoordinateOfOPRES_Center[k][0], _XYCoordinateOfOPRES_Center[k][1] + 0.5 + (
                                self._DesignParameter['_OPLayer']['_YWidth'] // 2 + _DRCObj._CoMinSpace2OP +
                                (_CONUMY - 1) * (
                                            _DRCObj._CoMinWidth + _DRCObj._CoMinSpace2) // 2 + _DRCObj._CoMinWidth // 2)])

                if _ResWidth % 2 == 1 and _ResLength % 2 == 1:
                    tmp.append([_XYCoordinateOfOPRES_Center[k][0], _XYCoordinateOfOPRES_Center[k][1] + 0.5 + (
                                self._DesignParameter['_OPLayer']['_YWidth'] // 2 + _DRCObj._CoMinSpace2OP +
                                (_CONUMY - 1) * (
                                            _DRCObj._CoMinWidth + _DRCObj._CoMinSpace2) // 2 + _DRCObj._CoMinWidth // 2)])

        self._DesignParameter['_XYCoordinatePort2Routing']['_XYCoordinates'] = tmp
        # del tmp


        print('#############################     Metal1 Layer Calculation    #############################################')
        self._DesignParameter['_Met1Layer'] = self._BoundaryElementDeclaration(
                                                                                _Layer=DesignParameters._LayerMapping['METAL1'][0],
                                                                                _Datatype=DesignParameters._LayerMapping['METAL1'][1],
                                                                                _XWidth=None,
                                                                                _YWidth=None,
                                                                                _XYCoordinates=[],
        )

        if _CONUMY == 1 :
            self._DesignParameter['_Met1Layer']['_XWidth'] = (_CONUMX - 1) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace) + _DRCObj._CoMinWidth + _DRCObj._Metal1MinEnclosureCO3 * 2
            self._DesignParameter['_Met1Layer']['_YWidth'] = (_CONUMY - 1) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace) + _DRCObj._CoMinWidth + _DRCObj._Metal1MinEnclosureCO3 * 2
            self._DesignParameter['_Met1Layer']['_XYCoordinates'] = self._DesignParameter['_XYCoordinatePort1Routing']['_XYCoordinates'] + self._DesignParameter['_XYCoordinatePort2Routing']['_XYCoordinates']

            tmpXY = []
            tmp_Met1Layer = self._DesignParameter['_Met1Layer']['_XYCoordinates']
            tmp1 = self.get_param_KJH4('_Met1Layer')
            for i in range(0, len(tmp1)):
                target_coordx = tmp1[i][0]['_Xwidth']
                target_coordy = tmp1[i][0]['_Ywidth']
                XY = [tmp_Met1Layer[i][0] - target_coordx / 2, tmp_Met1Layer[i][1] - target_coordy / 2]
                tmpXY.append(XY)
            self._DesignParameter['_Met1Layer']['_XYCoordinates'] = tmpXY

        else :
            self._DesignParameter['_Met1Layer']['_XWidth'] = (_CONUMX - 1) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2) + _DRCObj._CoMinWidth + _DRCObj._Metal1MinEnclosureCO3 * 2
            self._DesignParameter['_Met1Layer']['_YWidth'] = (_CONUMY - 1) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2) + _DRCObj._CoMinWidth + _DRCObj._Metal1MinEnclosureCO3 * 2
            self._DesignParameter['_Met1Layer']['_XYCoordinates'] = self._DesignParameter['_XYCoordinatePort1Routing']['_XYCoordinates'] + self._DesignParameter['_XYCoordinatePort2Routing']['_XYCoordinates']

            tmpXY = []
            tmp_Met1Layer = self._DesignParameter['_Met1Layer']['_XYCoordinates']
            tmp1 = self.get_param_KJH4('_Met1Layer')
            for i in range (0, len(tmp1)):
                target_coordx = tmp1[i][0]['_Xwidth']
                target_coordy = tmp1[i][0]['_Ywidth']
                XY = [tmp_Met1Layer[i][0]-target_coordx/2, tmp_Met1Layer[i][1]-target_coordy/2]
                tmpXY.append(XY)
            self._DesignParameter['_Met1Layer']['_XYCoordinates'] = tmpXY



        if DesignParameters._Technology != '028nm' :
            self._DesignParameter['_POLayer']['_YWidth'] += self._DesignParameter['_Met1Layer']['_YWidth'] * 2 + _DRCObj._CoMinEnclosureByPO * 2
            self._DesignParameter['_PPLayer']['_XWidth'] = self._DesignParameter['_POLayer']['_XWidth'] + 2 * _DRCObj._PpMinEnclosureOfPo
            self._DesignParameter['_PPLayer']['_YWidth'] = self._DesignParameter['_POLayer']['_YWidth'] + 2 * _DRCObj._PpMinEnclosureOfPo



        print('#############################     Metal1 Port Routing    #############################################')

        if _SeriesStripes > _ParallelStripes:
            self._DesignParameter['_Met1Routing'] = self._PathElementDeclaration(
                                                                                    _Layer=DesignParameters._LayerMapping['METAL1'][0],
                                                                                    _Datatype=DesignParameters._LayerMapping['METAL1'][1],
                                                                                    _Width=self._DesignParameter['_Met1Layer']['_YWidth'])
            tmp = []
            for i in range(0, _SeriesStripes // 2):
                tmp.append([[self.getXY('_XYCoordinatePort1Routing')[2*i][0] - self.getXWidth('_Met1Layer') / 2, self.getXY('_XYCoordinatePort1Routing')[2*i][1]],
                            [self.getXY('_XYCoordinatePort1Routing')[2*i+1][0] + self.getXWidth('_Met1Layer') / 2, self.getXY('_XYCoordinatePort1Routing')[2*i+1][1]]])

            for i in range(0, (_SeriesStripes - 1) // 2):
                tmp.append([[self.getXY('_XYCoordinatePort2Routing')[2*i+1][0] - self.getXWidth('_Met1Layer') / 2, self.getXY('_XYCoordinatePort2Routing')[2*i][1]],
                            [self.getXY('_XYCoordinatePort2Routing')[2*(i+1)][0] + self.getXWidth('_Met1Layer') / 2, self.getXY('_XYCoordinatePort2Routing')[2*i+1][1]]])
            self._DesignParameter['_Met1Routing']['_XYCoordinates'] = tmp
            # del tmp

        elif _ParallelStripes > _SeriesStripes:
            self._DesignParameter['_Met1Routing'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=self._DesignParameter['_Met1Layer']['_YWidth'])
            self._DesignParameter['_Met1Routing']['_XYCoordinates'] = [[[self.getXY('_XYCoordinatePort1Routing')[0][0] - self.getXWidth('_Met1Layer') / 2, self.getXY('_XYCoordinatePort1Routing')[0][1]],
                                                                        [self.getXY('_XYCoordinatePort1Routing')[-1][0] + self.getXWidth('_Met1Layer') / 2, self.getXY('_XYCoordinatePort1Routing')[-1][1]]],
                                                                       [[self.getXY('_XYCoordinatePort2Routing')[0][0] - self.getXWidth('_Met1Layer') / 2, self.getXY('_XYCoordinatePort2Routing')[0][1]],
                                                                        [self.getXY('_XYCoordinatePort2Routing')[-1][0] + self.getXWidth('_Met1Layer') / 2, self.getXY('_XYCoordinatePort2Routing')[-1][1]]]]
        else:
            pass

        print('##########################     Output Port1 Via Calculation    ##########################################')

        # Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH2_YCH._ViaStack_KJH2._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 1
        _Caculation_Parameters['_Layer2'] = _Port1Layer
        _Caculation_Parameters['_COX'] = None
        _Caculation_Parameters['_COY'] = None

        # Sref ViaX declaration
        self._DesignParameter['SRF_OutputPort1_Via'] = self._SrefElementDeclaration(
            _DesignObj=A02_ViaStack_KJH2_YCH._ViaStack_KJH2(_DesignParameter=None,
                                                            _Name='{}:SRF_OutputPort1_Via'.format(_Name)))[0]

        # Define Sref Relection
        self._DesignParameter['SRF_OutputPort1_Via']['_Reflect'] = [0, 0, 0]

        # Define Sref Angle
        self._DesignParameter['SRF_OutputPort1_Via']['_Angle'] = 0

        # Calcuate _COY
        _Caculation_Parameters['_COY'] = 4

        # Calcuate _COX
        tmp1 = self.get_param_KJH4('_Met1Layer')
        tmpWidth = tmp1[0][0]['_Xwidth']
        _Caculation_Parameters['_COX'] = max(2, int(
            (tmpWidth - 2 * _DRCObj._Metal1MinEnclosureVia3) / (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace2)
        ))

        # Generate Metal(x), Metal(x+1) and C0(Viax) layer
        self._DesignParameter['SRF_OutputPort1_Via']['_DesignObj']._CalculateDesignParameterXmin(
            **_Caculation_Parameters)  ## Option: Xmin, Ymin

        # Calculate Sref XYcoord
        tmpXY = []
        # initialized Sref coordinate
        self._DesignParameter['SRF_OutputPort1_Via']['_XYCoordinates'] = [[0, 0]]

        # Calculate
        # Target_coord
        target_coord = tmp1[_SeriesStripes][0]['_XY_cent']

        # Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_OutputPort1_Via','SRF_ViaM1M2','BND_Met1Layer')
        approaching_coord = tmp2[0][0][0][0]['_XY_cent']

        # Sref coord
        tmp3 = self.get_param_KJH4('SRF_OutputPort1_Via')
        Scoord = tmp3[0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        # Define
        self._DesignParameter['SRF_OutputPort1_Via']['_XYCoordinates'] = tmpXY

        ### Metal1 Overlap
            ## Boundary_element Generation
                ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_Met1_OutputPort1'] = self._BoundaryElementDeclaration(
        _Layer=DesignParameters._LayerMapping['METAL1'][0],
        _Datatype=DesignParameters._LayerMapping['METAL1'][1],
        _XWidth=None,
        _YWidth=None,
        _XYCoordinates=[],
        )

        tmp11 = self.get_param_KJH4('_Met1Layer')
        tmp12 = self.get_param_KJH4('SRF_OutputPort1_Via','SRF_ViaM1M2','BND_Met1Layer')

                ## Define Boundary_element _YWidth
        self._DesignParameter['BND_Met1_OutputPort1']['_YWidth'] = tmp12[0][0][0][0]['_Ywidth']

                ## Define Boundary_element _XWidth
        self._DesignParameter['BND_Met1_OutputPort1']['_XWidth'] = tmp11[0][0]['_Xwidth']

                ## Define Boundary_element _XYCoordinates
        tmpOriginx = tmp11[_SeriesStripes][0]['_XY_origin'][0]
        tmpOriginy = tmp12[0][0][0][0]['_XY_origin'][1]
        self._DesignParameter['BND_Met1_OutputPort1']['_XYCoordinates'] = [[tmpOriginx,tmpOriginy]]

        print('##########################     Output Port2 Via Calculation    ##########################################')

        # Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH2_YCH._ViaStack_KJH2._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 1
        _Caculation_Parameters['_Layer2'] = _Port2Layer
        _Caculation_Parameters['_COX'] = None
        _Caculation_Parameters['_COY'] = None

        # Sref ViaX declaration
        self._DesignParameter['SRF_OutputPort2_Via'] = self._SrefElementDeclaration(
            _DesignObj=A02_ViaStack_KJH2_YCH._ViaStack_KJH2(_DesignParameter=None,
                                                            _Name='{}:SRF_OutputPort2_Via'.format(_Name)))[0]

        # Define Sref Relection
        self._DesignParameter['SRF_OutputPort2_Via']['_Reflect'] = [0, 0, 0]

        # Define Sref Angle
        self._DesignParameter['SRF_OutputPort2_Via']['_Angle'] = 0

        # Calcuate _COY
        _Caculation_Parameters['_COY'] = 4

        # Calcuate _COX
        tmp1 = self.get_param_KJH4('_Met1Layer')
        tmpWidth = tmp1[0][0]['_Xwidth']
        _Caculation_Parameters['_COX'] = max(2, int(
            (tmpWidth - 2 * _DRCObj._Metal1MinEnclosureVia3) / (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace2)
        ))

        # Generate Metal(x), Metal(x+1) and C0(Viax) layer
        self._DesignParameter['SRF_OutputPort2_Via']['_DesignObj']._CalculateDesignParameterXmin(
            **_Caculation_Parameters)  ## Option: Xmin, Ymin

        # Calculate Sref XYcoord
        tmpXY = []
        # initialized Sref coordinate
        self._DesignParameter['SRF_OutputPort2_Via']['_XYCoordinates'] = [[0, 0]]

        # Calculate
        # Target_coord
        if(_SeriesStripes % 2 == 0):
            target_coord = tmp1[2 * _SeriesStripes - 1][0]['_XY_cent']
        else:
            target_coord = tmp1[_SeriesStripes - 1][0]['_XY_cent']

        # Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_OutputPort2_Via','SRF_ViaM1M2','BND_Met1Layer')
        approaching_coord = tmp2[0][0][0][0]['_XY_cent']

        # Sref coord
        tmp3 = self.get_param_KJH4('SRF_OutputPort2_Via')
        Scoord = tmp3[0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        # Define
        self._DesignParameter['SRF_OutputPort2_Via']['_XYCoordinates'] = tmpXY

        ### Metal1 Overlap
            ## Boundary_element Generation
                ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_Met1_OutputPort2'] = self._BoundaryElementDeclaration(
        _Layer=DesignParameters._LayerMapping['METAL1'][0],
        _Datatype=DesignParameters._LayerMapping['METAL1'][1],
        _XWidth=None,
        _YWidth=None,
        _XYCoordinates=[],
        )

        tmp11 = self.get_param_KJH4('_Met1Layer')
        tmp12 = self.get_param_KJH4('SRF_OutputPort2_Via','SRF_ViaM1M2','BND_Met1Layer')

                ## Define Boundary_element _YWidth
        self._DesignParameter['BND_Met1_OutputPort2']['_YWidth'] = tmp12[0][0][0][0]['_Ywidth']

                ## Define Boundary_element _XWidth
        self._DesignParameter['BND_Met1_OutputPort2']['_XWidth'] = tmp11[0][0]['_Xwidth']

                ## Define Boundary_element _XYCoordinates
        if(_SeriesStripes % 2 == 0):
            tmpOriginx = tmp11[2 * _SeriesStripes - 1][0]['_XY_origin'][0]
        else:
            tmpOriginx = tmp11[_SeriesStripes - 1][0]['_XY_origin'][0]
        tmpOriginy = tmp12[0][0][0][0]['_XY_origin'][1]
        self._DesignParameter['BND_Met1_OutputPort2']['_XYCoordinates'] = [[tmpOriginx,tmpOriginy]]

## ########################################################################################################################################################## Start_Main
if __name__ == '__main__':

    from KJH91_Projects.Project_ADC.Library_and_Engine.Private import MyInfo_AJH
    from KJH91_Projects.Project_ADC.Library_and_Engine import DRCchecker_KJH0

    libname = 'Proj_A50_opppcres_b_v15'
    cellname = 'A50_opppcres_b'
    _fileName = cellname + '.gds'

    ''' Input Parameters for Layout Object '''
    InputParams = dict(
        _ResWidth=160,
        _ResLength=1300,
        _CONUMX=None,
        _CONUMY=None,
        _SeriesStripes=50,
        _ParallelStripes=1,
        _Port1Layer = 4,
        _Port2Layer = 5,

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
    LayoutObj = _Opppcres_b(_DesignParameter=None, _Name=cellname)
    LayoutObj._CalculateDesignParameter(**InputParams)
    LayoutObj._UpdateDesignParameter2GDSStructure(_DesignParameterInDictionary=LayoutObj._DesignParameter)
    testStreamFile = open('./{}'.format(_fileName), 'wb')
    tmp = LayoutObj._CreateGDSStream(LayoutObj._DesignParameter['_GDSFile']['_GDSFile'])
    tmp.write_binary_gds_stream(testStreamFile)
    testStreamFile.close()

    print('###############      Sending to FTP Server...      ##################')
    My = MyInfo_AJH.USER(DesignParameters._Technology)
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