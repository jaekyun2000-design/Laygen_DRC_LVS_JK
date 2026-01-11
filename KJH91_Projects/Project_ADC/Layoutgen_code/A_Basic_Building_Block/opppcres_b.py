from TIA_Proj_YCH.Library_and_Engine import StickDiagram_KJH1
from TIA_Proj_YCH.Library_and_Engine import DesignParameters
from TIA_Proj_YCH.Library_and_Engine import DRC_EGFET
'''
This is for Opppcres_b including SeriesStripes.
Existing opppcres_b.py didn't have a serial connection.
'''

class _Opppcres(StickDiagram_KJH1._StickDiagram_KJH) :

    _ParametersForDesignCalculation = dict(
        _ResWidth=None,
        _ResLength=None,
        _CONUMX=None,
        _CONUMY=None,
        _SeriesStripes=None,
        _ParallelStripes=None
    )

    ## Initially Generated _DesignParameter
    def __init__(self, _DesignParameter=None, _Name=None):

        if _DesignParameter != None:
            self._DesignParameter = _DesignParameter
        else:
            self._DesignParameter = dict(
                                                    _POLayer=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0],_Datatype=DesignParameters._LayerMapping['POLY'][1], _XYCoordinates=[],_XWidth=400, _YWidth=400),
                                                    _OPLayer = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['OP'][0],_Datatype=DesignParameters._LayerMapping['OP'][1], _XYCoordinates=[],_XWidth=400, _YWidth=400),
                                                    _PRESLayer = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['PRES'][0],_Datatype=DesignParameters._LayerMapping['PRES'][1], _XYCoordinates=[],_XWidth=400, _YWidth=400),
                                                    _PPLayer=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['PIMP'][0],_Datatype=DesignParameters._LayerMapping['PIMP'][1],_XYCoordinates=[], _XWidth=400, _YWidth=400),
                                                    _Met1Layer=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0],_Datatype=DesignParameters._LayerMapping['METAL1'][1], _XYCoordinates=[],_XWidth=400, _YWidth=400),
                                                    _COLayer=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['CONT'][0],_Datatype=DesignParameters._LayerMapping['CONT'][1], _XYCoordinates=[],_XWidth=400, _YWidth=400),
                                                    _Name=self._NameDeclaration(_Name=_Name),
                                                    _GDSFile=self._GDSObjDeclaration(_GDSFile=None),
                                                    _XYCoordinatePort1Routing=dict(_DesignParametertype=7,_XYCoordinates=[]),
                                                    _XYCoordinatePort2Routing=dict(_DesignParametertype=7,_XYCoordinates=[]),
            )




    def _CalculateDesignParameter(self,
                                          _ResWidth = None,
                                          _ResLength = None,
                                          _CONUMX = None,
                                          _CONUMY = None,
                                          _SeriesStripes=None,
                                          _ParallelStripes=None
                                          ):
        # Load DRC library
        _DRCObj = DRC_EGFET.DRC()

        # Define _name
        _Name = self._DesignParameter['_Name']['_Name']

        ## ################################################################################################################################# Calculation_Start
        print('##############################')
        print('##     Calculation_Start    ##')
        print('##############################')


        MinSnapSpacing = _DRCObj._MinSnapSpacing

        if _ResWidth % 2 == 0 and _ResLength % 2 == 0 :
            _XYCoordinateOfOPRES = [[0,0]]
        elif _ResWidth % 2 == 0 and _ResLength % 2 == 1 :
            _XYCoordinateOfOPRES = [[0, MinSnapSpacing/2.0]]
        elif _ResWidth % 2 == 1 and _ResLength % 2 == 0 :
            _XYCoordinateOfOPRES = [[MinSnapSpacing/2.0,0]]
        elif _ResWidth % 2 == 1 and _ResLength % 2 == 1 :
            _XYCoordinateOfOPRES = [[MinSnapSpacing/2.0,MinSnapSpacing/2.0]]

        if _ResWidth % (2 * MinSnapSpacing) != 0 or _ResLength % (2 * MinSnapSpacing) != 0 :
            raise Exception ("Only even number can be generated")

        if _SeriesStripes == None or _ParallelStripes == None:
            raise Exception("<_SeriesStripes> and <_ParallelStripes> should be at least 1")

        if _SeriesStripes > 1 and _ParallelStripes > 1:
            raise Exception("<_SeriesStripes> or <_ParallelStripes>, only one of the two options is possible.")
        elif _SeriesStripes > 1 or _ParallelStripes > 1:
            NumofPolyLayer = max(_SeriesStripes, _ParallelStripes)
            for i in range(0, NumofPolyLayer-1):
                _XYCoordinateOfOPRES.append([_XYCoordinateOfOPRES[i][0] + _ResWidth + _DRCObj._PolygateMinSpace2, _XYCoordinateOfOPRES[0][0]])
        else:
            NumofPolyLayer = 1


        print ('#############################     POLY Layer Calculation    ##############################################')
        self._DesignParameter['_POLayer']['_XWidth'] = _ResWidth
        self._DesignParameter['_POLayer']['_YWidth'] = _ResLength + _DRCObj._PolyoverOPlayer * 2
        self._DesignParameter['_POLayer']['_XYCoordinates'] = _XYCoordinateOfOPRES
        # print(self._DesignParameter['_POLayer']['_XWidth'])

        print ('#############################     PRES Layer Calculation    ##############################################') ## for ss28nm
        self._DesignParameter['_PRESLayer']['_XWidth'] = _ResWidth * NumofPolyLayer + _DRCObj._PolygateMinSpace2 * (NumofPolyLayer - 1) + _DRCObj._PRESlayeroverPoly * 2
        self._DesignParameter['_PRESLayer']['_YWidth'] = self._DesignParameter['_POLayer']['_YWidth'] + _DRCObj._PRESlayeroverPoly * 2
        self._DesignParameter['_PRESLayer']['_XYCoordinates'] = [[(_XYCoordinateOfOPRES[-1][0] - _XYCoordinateOfOPRES[0][0]) / 2, _XYCoordinateOfOPRES[0][1]]]


        print ('#############################     PIMP Layer Calculation    ##############################################')
        self._DesignParameter['_PPLayer']['_XWidth'] = self._DesignParameter['_PRESLayer']['_XWidth']
        self._DesignParameter['_PPLayer']['_YWidth'] = self._DesignParameter['_PRESLayer']['_YWidth']
        self._DesignParameter['_PPLayer']['_XYCoordinates'] = self._DesignParameter['_PRESLayer']['_XYCoordinates']


        print ('#############################     OP Layer Calculation    ################################################')
        self._DesignParameter['_OPLayer']['_XWidth'] = _ResWidth * NumofPolyLayer + _DRCObj._PolygateMinSpace2 * (NumofPolyLayer - 1) + _DRCObj._OPlayeroverPoly * 2
        self._DesignParameter['_OPLayer']['_YWidth'] = _ResLength
        if _ResLength < _DRCObj._PolyoverOPlayer :
            raise NotImplementedError
        self._DesignParameter['_OPLayer']['_XYCoordinates'] = self._DesignParameter['_PRESLayer']['_XYCoordinates']


        print ('#############################     CONT Layer Calculation    ##############################################')
        self._DesignParameter['_COLayer']['_XWidth'] = _DRCObj._CoMinWidth
        self._DesignParameter['_COLayer']['_YWidth'] = _DRCObj._CoMinWidth
        tmp = []
        _CONUMXmax = int((self._DesignParameter['_POLayer']['_XWidth'] - _DRCObj._CoMinEnclosureByPO2 * 2 - _DRCObj._CoMinWidth) // (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace)) + 1
        _CONUMYmax = int((int((self._DesignParameter['_POLayer']['_YWidth'] - self._DesignParameter['_OPLayer']['_YWidth'] - 2*_DRCObj._CoMinSpace2OP - 2*_DRCObj._CoMinEnclosureByPO2) // (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2)) + 1) // 2)

        if DesignParameters._Technology != '028nm' :
            _CONUMYmax = 3

        if _CONUMX == None :
            _CONUMX = _CONUMXmax
        if _CONUMY == None :
            _CONUMY = _CONUMYmax
            if DesignParameters._Technology != '028nm' :
                _CONUMY = 1

        if _CONUMY > 1 :
            _CONUMX = int((self._DesignParameter['_POLayer']['_XWidth'] - _DRCObj._CoMinEnclosureByPO2 * 2 - _DRCObj._CoMinWidth) // (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2)) + 1


        if _CONUMX > _CONUMXmax or _CONUMY > _CONUMYmax :
            raise NotImplementedError

        for k in range(0, NumofPolyLayer):
            if _CONUMY == 1 :
                if _ResWidth % 2 == 0 and _ResLength % 2 == 0 :
                    for i in range (0, _CONUMX) :
                        for j in range (0, _CONUMY) :
                            if (_CONUMX % 2 == 0) :
                                tmp.append([_XYCoordinateOfOPRES[k][0]- (_CONUMX//2 - 0.5) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace) + i * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace),
                                            _XYCoordinateOfOPRES[k][1]- (self._DesignParameter['_OPLayer']['_YWidth']//2 +_DRCObj._CoMinSpace2OP + 0.5 * _DRCObj._CoMinWidth) - j * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace)])
                                tmp.append([_XYCoordinateOfOPRES[k][0]- (_CONUMX // 2 - 0.5) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace) + i * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace),
                                            _XYCoordinateOfOPRES[k][1]+ (self._DesignParameter['_OPLayer']['_YWidth']//2 +_DRCObj._CoMinSpace2OP + 0.5 * _DRCObj._CoMinWidth) + j * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace)])
                            else :
                                tmp.append([_XYCoordinateOfOPRES[k][0] - (_CONUMX // 2) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace) + i * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace),
                                            _XYCoordinateOfOPRES[k][1] - (self._DesignParameter['_OPLayer']['_YWidth'] // 2 + _DRCObj._CoMinSpace2OP + 0.5 * _DRCObj._CoMinWidth) - j * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace)])
                                tmp.append([_XYCoordinateOfOPRES[k][0] - (_CONUMX // 2) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace) + i * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace),
                                            _XYCoordinateOfOPRES[k][1] + (self._DesignParameter['_OPLayer']['_YWidth'] // 2 + _DRCObj._CoMinSpace2OP + 0.5 * _DRCObj._CoMinWidth) + j * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace)])

                elif _ResWidth % 2 == 0 and _ResLength % 2 == 1 :
                    for i in range (0, _CONUMX) :
                        for j in range (0, _CONUMY) :
                            if (_CONUMX % 2 == 0) :
                                tmp.append([_XYCoordinateOfOPRES[k][0]-(_CONUMX//2 - 0.5) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace) + i * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace),
                                            _XYCoordinateOfOPRES[k][1] - MinSnapSpacing/2.0 -(self._DesignParameter['_OPLayer']['_YWidth']//2 +_DRCObj._CoMinSpace2OP + 0.5 * _DRCObj._CoMinWidth) - j * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace)])
                                tmp.append([_XYCoordinateOfOPRES[k][0]-(_CONUMX // 2 - 0.5) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace) + i * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace),
                                            _XYCoordinateOfOPRES[k][1] + MinSnapSpacing/2.0 +(self._DesignParameter['_OPLayer']['_YWidth']//2 +_DRCObj._CoMinSpace2OP + 0.5 * _DRCObj._CoMinWidth) + j * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace)])
                            else :
                                tmp.append([_XYCoordinateOfOPRES[k][0] - (_CONUMX // 2) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace) + i * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace),
                                            _XYCoordinateOfOPRES[k][1] - MinSnapSpacing/2.0 - (self._DesignParameter['_OPLayer']['_YWidth'] // 2 + _DRCObj._CoMinSpace2OP + 0.5 * _DRCObj._CoMinWidth) - j * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace)])
                                tmp.append([_XYCoordinateOfOPRES[k][0] - (_CONUMX // 2) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace) + i * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace),
                                            _XYCoordinateOfOPRES[k][1] + MinSnapSpacing/2.0 + (self._DesignParameter['_OPLayer']['_YWidth'] // 2 + _DRCObj._CoMinSpace2OP + 0.5 * _DRCObj._CoMinWidth) + j * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace)])

                elif _ResWidth % 2 == 1 and _ResLength % 2 == 0 :
                    for i in range (0, _CONUMX) :
                        for j in range (0, _CONUMY) :
                            if (_CONUMX % 2 == 0) :
                                tmp.append([_XYCoordinateOfOPRES[k][0] + MinSnapSpacing/2.0 -(_CONUMX//2 - 0.5) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace) + i * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace),
                                            _XYCoordinateOfOPRES[k][1]-(self._DesignParameter['_OPLayer']['_YWidth']//2 +_DRCObj._CoMinSpace2OP + 0.5 * _DRCObj._CoMinWidth) - j * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace)])
                                tmp.append([_XYCoordinateOfOPRES[k][0] + MinSnapSpacing/2.0 -(_CONUMX // 2 - 0.5) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace) + i * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace),
                                            _XYCoordinateOfOPRES[k][1]+(self._DesignParameter['_OPLayer']['_YWidth']//2 +_DRCObj._CoMinSpace2OP + 0.5 * _DRCObj._CoMinWidth) + j * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace)])
                            else :
                                tmp.append([_XYCoordinateOfOPRES[k][0] + MinSnapSpacing/2.0 - (_CONUMX // 2) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace) + i * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace),
                                            _XYCoordinateOfOPRES[k][1] - (self._DesignParameter['_OPLayer']['_YWidth'] // 2 + _DRCObj._CoMinSpace2OP + 0.5 * _DRCObj._CoMinWidth) - j * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace)])
                                tmp.append([_XYCoordinateOfOPRES[k][0] + MinSnapSpacing/2.0 - (_CONUMX // 2) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace) + i * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace),
                                            _XYCoordinateOfOPRES[k][1] + (self._DesignParameter['_OPLayer']['_YWidth'] // 2 + _DRCObj._CoMinSpace2OP + 0.5 * _DRCObj._CoMinWidth) + j * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace)])

                elif _ResWidth % 2 == 1 and _ResLength % 2 == 1 :
                    for i in range (0, _CONUMX) :
                        for j in range (0, _CONUMY) :
                            if (_CONUMX % 2 == 0) :
                                tmp.append([_XYCoordinateOfOPRES[k][0] + MinSnapSpacing/2.0 - (_CONUMX//2 - 0.5) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace) + i * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace),
                                            _XYCoordinateOfOPRES[k][1] - self.CeilMinSnapSpacing((self._DesignParameter['_OPLayer']['_YWidth']/2 +_DRCObj._CoMinSpace2OP + 0.5 * _DRCObj._CoMinWidth), MinSnapSpacing / 2) - j * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace)])
                                tmp.append([_XYCoordinateOfOPRES[k][0] + MinSnapSpacing/2.0 - (_CONUMX // 2 - 0.5) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace) + i * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace),
                                            _XYCoordinateOfOPRES[k][1] + self.CeilMinSnapSpacing((self._DesignParameter['_OPLayer']['_YWidth']/2 +_DRCObj._CoMinSpace2OP + 0.5 * _DRCObj._CoMinWidth), MinSnapSpacing / 2) + j * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace)])
                            else :
                                tmp.append([_XYCoordinateOfOPRES[k][0] + MinSnapSpacing/2.0 - (_CONUMX // 2) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace) + i * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace),
                                            _XYCoordinateOfOPRES[k][1] - self.CeilMinSnapSpacing((self._DesignParameter['_OPLayer']['_YWidth'] / 2 + _DRCObj._CoMinSpace2OP + 0.5 * _DRCObj._CoMinWidth), MinSnapSpacing / 2) - j * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace)])
                                tmp.append([_XYCoordinateOfOPRES[k][0] + MinSnapSpacing/2.0 - (_CONUMX // 2) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace) + i * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace),
                                            _XYCoordinateOfOPRES[k][1] + self.CeilMinSnapSpacing((self._DesignParameter['_OPLayer']['_YWidth'] / 2 + _DRCObj._CoMinSpace2OP + 0.5 * _DRCObj._CoMinWidth), MinSnapSpacing / 2) + j * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace)])

            else :
                if _ResWidth % 2 == 0 and _ResLength % 2 == 0 :
                    for i in range (0, _CONUMX) :
                        for j in range (0, _CONUMY) :
                            if (_CONUMX % 2 == 0) :
                                tmp.append([_XYCoordinateOfOPRES[k][0]-(_CONUMX//2 - 0.5) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2) + i * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2),
                                            _XYCoordinateOfOPRES[k][1]-(self._DesignParameter['_OPLayer']['_YWidth']//2 +_DRCObj._CoMinSpace2OP + 0.5 * _DRCObj._CoMinWidth) - j * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2)])
                                tmp.append([_XYCoordinateOfOPRES[k][0]-(_CONUMX // 2 - 0.5) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2) + i * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2),
                                            _XYCoordinateOfOPRES[k][1]+(self._DesignParameter['_OPLayer']['_YWidth']//2 +_DRCObj._CoMinSpace2OP + 0.5 * _DRCObj._CoMinWidth) + j * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2)])
                            else :
                                tmp.append([_XYCoordinateOfOPRES[k][0] - (_CONUMX // 2) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2) + i * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2),
                                            _XYCoordinateOfOPRES[k][1] - (self._DesignParameter['_OPLayer']['_YWidth'] // 2 + _DRCObj._CoMinSpace2OP + 0.5 * _DRCObj._CoMinWidth) - j * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2)])
                                tmp.append([_XYCoordinateOfOPRES[k][0] - (_CONUMX // 2) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2) + i * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2),
                                            _XYCoordinateOfOPRES[k][1] + (self._DesignParameter['_OPLayer']['_YWidth'] // 2 + _DRCObj._CoMinSpace2OP + 0.5 * _DRCObj._CoMinWidth) + j * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2)])

                elif _ResWidth % 2 == 0 and _ResLength % 2 == 1 :
                    for i in range (0, _CONUMX) :
                        for j in range (0, _CONUMY) :
                            if (_CONUMX % 2 == 0) :
                                tmp.append([_XYCoordinateOfOPRES[k][0] - (_CONUMX // 2 - 0.5) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2) + i * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2),
                                            _XYCoordinateOfOPRES[k][1] - 0.5 -(self._DesignParameter['_OPLayer']['_YWidth']//2 +_DRCObj._CoMinSpace2OP + 0.5 * _DRCObj._CoMinWidth) - j * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2)])
                                tmp.append([_XYCoordinateOfOPRES[k][0] - (_CONUMX // 2 - 0.5) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2) + i * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2),
                                            _XYCoordinateOfOPRES[k][1] + 0.5 +(self._DesignParameter['_OPLayer']['_YWidth']//2 +_DRCObj._CoMinSpace2OP + 0.5 * _DRCObj._CoMinWidth) + j * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2)])
                            else :
                                tmp.append([_XYCoordinateOfOPRES[k][0] - (_CONUMX // 2) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2) + i * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2),
                                            _XYCoordinateOfOPRES[k][1] - 0.5 - (self._DesignParameter['_OPLayer']['_YWidth'] // 2 + _DRCObj._CoMinSpace2OP + 0.5 * _DRCObj._CoMinWidth) - j * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2)])
                                tmp.append([_XYCoordinateOfOPRES[k][0] - (_CONUMX // 2) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2) + i * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2),
                                            _XYCoordinateOfOPRES[k][1] + 0.5 + (self._DesignParameter['_OPLayer']['_YWidth'] // 2 + _DRCObj._CoMinSpace2OP + 0.5 * _DRCObj._CoMinWidth) + j * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2)])

                elif _ResWidth % 2 == 1 and _ResLength % 2 == 0 :
                    for i in range (0, _CONUMX) :
                        for j in range (0, _CONUMY) :
                            if (_CONUMX % 2 == 0) :
                                tmp.append([_XYCoordinateOfOPRES[k][0] + 0.5 -(_CONUMX//2 - 0.5) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2) + i * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2),
                                            _XYCoordinateOfOPRES[k][1]-(self._DesignParameter['_OPLayer']['_YWidth']//2 +_DRCObj._CoMinSpace2OP + 0.5 * _DRCObj._CoMinWidth) - j * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2)])
                                tmp.append([_XYCoordinateOfOPRES[k][0] + 0.5-(_CONUMX // 2 - 0.5) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2) + i * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2),
                                            _XYCoordinateOfOPRES[k][1]+(self._DesignParameter['_OPLayer']['_YWidth']//2 +_DRCObj._CoMinSpace2OP + 0.5 * _DRCObj._CoMinWidth) + j * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2)])
                            else :
                                tmp.append([_XYCoordinateOfOPRES[k][0] + 0.5 - (_CONUMX // 2) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2) + i * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2),
                                            _XYCoordinateOfOPRES[k][1] - (self._DesignParameter['_OPLayer']['_YWidth'] // 2 + _DRCObj._CoMinSpace2OP + 0.5 * _DRCObj._CoMinWidth) - j * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2)])
                                tmp.append([_XYCoordinateOfOPRES[k][0] + 0.5 - (_CONUMX // 2) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2) + i * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2),
                                            _XYCoordinateOfOPRES[k][1] + (self._DesignParameter['_OPLayer']['_YWidth'] // 2 + _DRCObj._CoMinSpace2OP + 0.5 * _DRCObj._CoMinWidth) + j * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2)])

                elif _ResWidth % 2 == 1 and _ResLength % 2 == 1 :
                    for i in range (0, _CONUMX) :
                        for j in range (0, _CONUMY) :
                            if (_CONUMX % 2 == 0) :
                                tmp.append([_XYCoordinateOfOPRES[k][0] + 0.5-(_CONUMX//2 - 0.5) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2) + i * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2),
                                            _XYCoordinateOfOPRES[k][1] - 0.5 -(self._DesignParameter['_OPLayer']['_YWidth']//2 +_DRCObj._CoMinSpace2OP + 0.5 * _DRCObj._CoMinWidth) - j * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2)])
                                tmp.append([_XYCoordinateOfOPRES[k][0] + 0.5 -(_CONUMX // 2 - 0.5) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2) + i * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2),
                                            _XYCoordinateOfOPRES[k][1] + 0.5 +(self._DesignParameter['_OPLayer']['_YWidth']//2 +_DRCObj._CoMinSpace2OP + 0.5 * _DRCObj._CoMinWidth) + j * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2)])
                            else :
                                tmp.append([_XYCoordinateOfOPRES[k][0] + 0.5 - (_CONUMX // 2) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2) + i * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2),
                                            _XYCoordinateOfOPRES[k][1] - 0.5 - (self._DesignParameter['_OPLayer']['_YWidth'] // 2 + _DRCObj._CoMinSpace2OP + 0.5 * _DRCObj._CoMinWidth) - j * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2)])
                                tmp.append([_XYCoordinateOfOPRES[k][0] + 0.5 - (_CONUMX // 2) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2) + i * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2),
                                            _XYCoordinateOfOPRES[k][1] + 0.5 + (self._DesignParameter['_OPLayer']['_YWidth'] // 2 + _DRCObj._CoMinSpace2OP + 0.5 * _DRCObj._CoMinWidth) + j * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2)])

        self._DesignParameter['_COLayer']['_XYCoordinates'] = tmp
        # del tmp


        print ('#########################     Port1 Routing Coordinates Calculation    ####################################')
        tmp = []
        for k in range(0, NumofPolyLayer):
            if _CONUMY == 1 :
                if _ResWidth % 2 == 0 and _ResLength % 2 == 0 :
                    tmp.append([_XYCoordinateOfOPRES[k][0], _XYCoordinateOfOPRES[k][1] - (self._DesignParameter['_OPLayer']['_YWidth']//2 + _DRCObj._CoMinSpace2OP +
                                                                                    (_CONUMY - 1) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace)//2 + _DRCObj._CoMinWidth//2)])

                if _ResWidth % 2 == 0 and _ResLength % 2 == 1 :
                    tmp.append([_XYCoordinateOfOPRES[k][0], _XYCoordinateOfOPRES[k][1] - 0.5 - (self._DesignParameter['_OPLayer']['_YWidth']//2 + _DRCObj._CoMinSpace2OP +
                                                                                    (_CONUMY - 1) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace)//2 + _DRCObj._CoMinWidth//2)])

                if _ResWidth % 2 == 1 and _ResLength % 2 == 0 :
                    tmp.append([_XYCoordinateOfOPRES[k][0], _XYCoordinateOfOPRES[k][1] - (self._DesignParameter['_OPLayer']['_YWidth']//2 + _DRCObj._CoMinSpace2OP +
                                                                                    (_CONUMY - 1) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace)//2 + _DRCObj._CoMinWidth//2)])

                if _ResWidth % 2 == 1 and _ResLength % 2 == 1 :
                    tmp.append([_XYCoordinateOfOPRES[k][0], _XYCoordinateOfOPRES[k][1] - 0.5 - (self._DesignParameter['_OPLayer']['_YWidth']//2 + _DRCObj._CoMinSpace2OP +
                                                                                    (_CONUMY - 1) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace)//2 + _DRCObj._CoMinWidth//2)])

            else :
                if _ResWidth % 2 == 0 and _ResLength % 2 == 0 :
                    tmp.append([_XYCoordinateOfOPRES[k][0], _XYCoordinateOfOPRES[k][1] - (self._DesignParameter['_OPLayer']['_YWidth']//2 + _DRCObj._CoMinSpace2OP +
                                                                                  (_CONUMY - 1) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2)//2 + _DRCObj._CoMinWidth//2)])

                if _ResWidth % 2 == 0 and _ResLength % 2 == 1 :
                    tmp.append([_XYCoordinateOfOPRES[k][0], _XYCoordinateOfOPRES[k][1] - 0.5 - (self._DesignParameter['_OPLayer']['_YWidth']//2 + _DRCObj._CoMinSpace2OP +
                                                                                    (_CONUMY - 1) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2)//2 + _DRCObj._CoMinWidth//2)])

                if _ResWidth % 2 == 1 and _ResLength % 2 == 0 :
                    tmp.append([_XYCoordinateOfOPRES[k][0], _XYCoordinateOfOPRES[k][1] - (self._DesignParameter['_OPLayer']['_YWidth']//2 + _DRCObj._CoMinSpace2OP +
                                                                                    (_CONUMY - 1) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2)//2 + _DRCObj._CoMinWidth//2)])

                if _ResWidth % 2 == 1 and _ResLength % 2 == 1 :
                    tmp.append([_XYCoordinateOfOPRES[k][0], _XYCoordinateOfOPRES[k][1] - 0.5 - (self._DesignParameter['_OPLayer']['_YWidth']//2 + _DRCObj._CoMinSpace2OP +
                                                                                    (_CONUMY - 1) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2)//2 + _DRCObj._CoMinWidth//2)])


        self._DesignParameter['_XYCoordinatePort1Routing']['_XYCoordinates'] = tmp
        # del tmp


        print ('#########################     Port2 Routing Coordinates Calculation    ####################################')
        tmp = []
        for k in range(0, NumofPolyLayer):
            if _CONUMY == 1 :
                if _ResWidth % 2 == 0 and _ResLength % 2 == 0 :
                    tmp.append([_XYCoordinateOfOPRES[k][0], _XYCoordinateOfOPRES[k][1] + (self._DesignParameter['_OPLayer']['_YWidth'] // 2 + _DRCObj._CoMinSpace2OP +
                            (_CONUMY - 1) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace) // 2 + _DRCObj._CoMinWidth // 2)])

                if _ResWidth % 2 == 1 and _ResLength % 2 == 0 :
                    tmp.append([_XYCoordinateOfOPRES[k][0], _XYCoordinateOfOPRES[k][1] + (self._DesignParameter['_OPLayer']['_YWidth'] // 2 + _DRCObj._CoMinSpace2OP +
                            (_CONUMY - 1) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace) // 2 + _DRCObj._CoMinWidth // 2)])

                if _ResWidth % 2 == 0 and _ResLength % 2 == 1 :
                    tmp.append([_XYCoordinateOfOPRES[k][0], _XYCoordinateOfOPRES[k][1] + 0.5 + (self._DesignParameter['_OPLayer']['_YWidth'] // 2 + _DRCObj._CoMinSpace2OP +
                            (_CONUMY - 1) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace) // 2 + _DRCObj._CoMinWidth // 2)])

                if _ResWidth % 2 == 1 and _ResLength % 2 == 1 :
                    tmp.append([_XYCoordinateOfOPRES[k][0] , _XYCoordinateOfOPRES[k][1] + 0.5 + (self._DesignParameter['_OPLayer']['_YWidth'] // 2 + _DRCObj._CoMinSpace2OP +
                            (_CONUMY - 1) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace) // 2 + _DRCObj._CoMinWidth // 2)])

            else :
                if _ResWidth % 2 == 0 and _ResLength % 2 == 0 :
                    tmp.append([_XYCoordinateOfOPRES[k][0], _XYCoordinateOfOPRES[k][1] + (self._DesignParameter['_OPLayer']['_YWidth'] // 2 + _DRCObj._CoMinSpace2OP +
                            (_CONUMY - 1) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2) // 2 + _DRCObj._CoMinWidth // 2)])

                if _ResWidth % 2 == 1 and _ResLength % 2 == 0 :
                    tmp.append([_XYCoordinateOfOPRES[k][0], _XYCoordinateOfOPRES[k][1] + (self._DesignParameter['_OPLayer']['_YWidth'] // 2 + _DRCObj._CoMinSpace2OP +
                            (_CONUMY - 1) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2) // 2 + _DRCObj._CoMinWidth // 2)])

                if _ResWidth % 2 == 0 and _ResLength % 2 == 1 :
                    tmp.append([_XYCoordinateOfOPRES[k][0], _XYCoordinateOfOPRES[k][1] + 0.5 + (self._DesignParameter['_OPLayer']['_YWidth'] // 2 + _DRCObj._CoMinSpace2OP +
                            (_CONUMY - 1) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2) // 2 + _DRCObj._CoMinWidth // 2)])

                if _ResWidth % 2 == 1 and _ResLength % 2 == 1 :
                    tmp.append([_XYCoordinateOfOPRES[k][0] , _XYCoordinateOfOPRES[k][1] + 0.5 + (self._DesignParameter['_OPLayer']['_YWidth'] // 2 + _DRCObj._CoMinSpace2OP +
                            (_CONUMY - 1) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2) // 2 + _DRCObj._CoMinWidth // 2)])

        self._DesignParameter['_XYCoordinatePort2Routing']['_XYCoordinates'] = tmp
        # del tmp


        print ('#############################     Metal1 Layer Calculation    #############################################')
        if _CONUMY == 1 :
            self._DesignParameter['_Met1Layer']['_XWidth'] = (_CONUMX - 1) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace) + _DRCObj._CoMinWidth + _DRCObj._Metal1MinEnclosureCO3 * 2
            self._DesignParameter['_Met1Layer']['_YWidth'] = (_CONUMY - 1) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace) + _DRCObj._CoMinWidth + _DRCObj._Metal1MinEnclosureCO3 * 2
            self._DesignParameter['_Met1Layer']['_XYCoordinates'] = self._DesignParameter['_XYCoordinatePort1Routing']['_XYCoordinates'] + self._DesignParameter['_XYCoordinatePort2Routing']['_XYCoordinates']
            self._DesignParameter['_Met1Layer']['_XYCoordinates'].sort()

        else :
            self._DesignParameter['_Met1Layer']['_XWidth'] = (_CONUMX - 1) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2) + _DRCObj._CoMinWidth + _DRCObj._Metal1MinEnclosureCO3 * 2
            self._DesignParameter['_Met1Layer']['_YWidth'] = (_CONUMY - 1) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2) + _DRCObj._CoMinWidth + _DRCObj._Metal1MinEnclosureCO3 * 2
            self._DesignParameter['_Met1Layer']['_XYCoordinates'] = self._DesignParameter['_XYCoordinatePort1Routing']['_XYCoordinates'] + self._DesignParameter['_XYCoordinatePort2Routing']['_XYCoordinates']
            self._DesignParameter['_Met1Layer']['_XYCoordinates'].sort()

        if DesignParameters._Technology != '028nm' :
            self._DesignParameter['_POLayer']['_YWidth'] += self._DesignParameter['_Met1Layer']['_YWidth'] * 2 + _DRCObj._CoMinEnclosureByPO * 2
            self._DesignParameter['_PPLayer']['_XWidth'] = self._DesignParameter['_POLayer']['_XWidth'] + 2 * _DRCObj._PpMinEnclosureOfPo
            self._DesignParameter['_PPLayer']['_YWidth'] = self._DesignParameter['_POLayer']['_YWidth'] + 2 * _DRCObj._PpMinEnclosureOfPo


        print('#############################     Metal1 Port Routing    #############################################')
        if _SeriesStripes > _ParallelStripes:
            self._DesignParameter['_Met1Routing'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=self._DesignParameter['_Met1Layer']['_YWidth'])
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

        ## ################################################################################################################################# Calculation_End
        print('##############################')
        print('##     Calculation_End      ##')
        print('##############################')

if __name__ == '__main__':

    from TIA_Proj_YCH.Library_and_Engine.Private import MyInfo_YCH
    from TIA_Proj_YCH.Library_and_Engine import DRCchecker_KJH0

    libname = 'Proj_A50_opppcres_b_v12'
    cellname = 'A50_opppcres_b'
    _fileName = cellname + '.gds'

    ''' Input Parameters for Layout Object '''
    InputParams = dict(
        _ResWidth=356,
        _ResLength=400,
        _CONUMX=None,
        _CONUMY=None,
        _SeriesStripes=1,
        _ParallelStripes=1,

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
    LayoutObj = _Opppcres(_DesignParameter=None, _Name=cellname)
    LayoutObj._CalculateDesignParameter(**InputParams)
    LayoutObj._UpdateDesignParameter2GDSStructure(_DesignParameterInDictionary=LayoutObj._DesignParameter)
    testStreamFile = open('./{}'.format(_fileName), 'wb')
    tmp = LayoutObj._CreateGDSStream(LayoutObj._DesignParameter['_GDSFile']['_GDSFile'])
    tmp.write_binary_gds_stream(testStreamFile)
    testStreamFile.close()

    print('###############      Sending to FTP Server...      ##################')
    My = MyInfo_YCH.USER(DesignParameters._Technology)
    # print(DesignParameters._Technology)
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