from generatorLib import StickDiagram
from generatorLib import DesignParameters
from generatorLib import DRC
'''
This is for Opppcres_b including SeriesStripes.
Existing opppcres_b.py didn't have a serial connection.
'''

class _Opppcres(StickDiagram._StickDiagram) :

    _ParametersForDesignCalculation = dict(_ResWidth=None, _ResLength=None, _CONUMX=None,_CONUMY=None, _SeriesStripes=None, _ParallelStripes=None)

    def __init__(self, _DesignParameter=None, _Name=None):

        if _DesignParameter!=None:
            self._DesignParameter=_DesignParameter
        else :
            self._DesignParameter = dict(
                                                    _POLayer=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0],_Datatype=DesignParameters._LayerMapping['POLY'][1], _XYCoordinates=[],_XWidth=400, _YWidth=400),
                                                    _OPLayer = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['OP'][0],_Datatype=DesignParameters._LayerMapping['OP'][1], _XYCoordinates=[],_XWidth=400, _YWidth=400),
                                                    _PRESLayer = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['PRES'][0],_Datatype=DesignParameters._LayerMapping['PRES'][1], _XYCoordinates=[],_XWidth=400, _YWidth=400),
                                                    _PPLayer=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['PIMP'][0],_Datatype=DesignParameters._LayerMapping['PIMP'][1],_XYCoordinates=[], _XWidth=400, _YWidth=400),
                                                    _Met1Layer=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0],_Datatype=DesignParameters._LayerMapping['METAL1'][1], _XYCoordinates=[],_XWidth=400, _YWidth=400),
                                                    _COLayer=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['CONT'][0],_Datatype=DesignParameters._LayerMapping['CONT'][1], _XYCoordinates=[],_XWidth=400, _YWidth=400),
                                                    _Name=self._NameDeclaration(_Name=_Name), _GDSFile=self._GDSObjDeclaration(_GDSFile=None),
                                                    _XYCoordinatePort1Routing=dict(_DesignParametertype=7,_XYCoordinates=[]),
                                                    _XYCoordinatePort2Routing=dict(_DesignParametertype=7,_XYCoordinates=[]),
                                                   )

        if _Name != None:
            self._DesignParameter['_Name']['_Name']=_Name


    def _CalculateOpppcresDesignParameter(self, _ResWidth = None, _ResLength = None, _CONUMX = None, _CONUMY = None, _SeriesStripes=None, _ParallelStripes=None):
        print ('#########################################################################################################')
        print ('                                    {}  Opppcres Calculation Start                                       '.format(self._DesignParameter['_Name']['_Name']))
        print ('#########################################################################################################')

        _DRCObj = DRC.DRC()
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

        if DesignParameters._Technology != 'SS28nm' :
            _CONUMYmax = 3

        if _CONUMX == None :
            _CONUMX = _CONUMXmax
        if _CONUMY == None :
            _CONUMY = _CONUMYmax
            if DesignParameters._Technology != 'SS28nm' :
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
        del tmp


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
        del tmp


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
        del tmp


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

        if DesignParameters._Technology != 'SS28nm' :
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
            del tmp

        elif _ParallelStripes > _SeriesStripes:
            self._DesignParameter['_Met1Routing'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=self._DesignParameter['_Met1Layer']['_YWidth'])
            self._DesignParameter['_Met1Routing']['_XYCoordinates'] = [[[self.getXY('_XYCoordinatePort1Routing')[0][0] - self.getXWidth('_Met1Layer') / 2, self.getXY('_XYCoordinatePort1Routing')[0][1]],
                                                                        [self.getXY('_XYCoordinatePort1Routing')[-1][0] + self.getXWidth('_Met1Layer') / 2, self.getXY('_XYCoordinatePort1Routing')[-1][1]]],
                                                                       [[self.getXY('_XYCoordinatePort2Routing')[0][0] - self.getXWidth('_Met1Layer') / 2, self.getXY('_XYCoordinatePort2Routing')[0][1]],
                                                                        [self.getXY('_XYCoordinatePort2Routing')[-1][0] + self.getXWidth('_Met1Layer') / 2, self.getXY('_XYCoordinatePort2Routing')[-1][1]]]]
        else:
            pass


if __name__ == '__main__':
    _ResWidth = 1650
    _ResLength = 1500
    _CONUMX = None
    _CONUMY = 1
    _SeriesStripes = 4
    _ParallelStripes = 1


    DesignParameters._Technology = 'SS28nm'
    TopObj = _Opppcres(_DesignParameter=None, _Name='_Opppcres')
    TopObj._CalculateOpppcresDesignParameter(
        _ResWidth = _ResWidth,
        _ResLength = _ResLength,
        _CONUMX = _CONUMX,
        _CONUMY = _CONUMY,
        _SeriesStripes=_SeriesStripes,
        _ParallelStripes=_ParallelStripes
    )
    TopObj._UpdateDesignParameter2GDSStructure(_DesignParameterInDictionary=TopObj._DesignParameter)
    testStreamFile = open('./_Opppcres.gds', 'wb')
    tmp = TopObj._CreateGDSStream(TopObj._DesignParameter['_GDSFile']['_GDSFile'])
    tmp.write_binary_gds_stream(testStreamFile)
    testStreamFile.close()

    print('#############################      Sending to FTP Server...      ##############################')

    import ftplib

    ftp = ftplib.FTP('141.223.24.53')
    ftp.login('smlim96', 'min753531')
    ftp.cwd('/mnt/sdc/smlim96/OPUS/ss28')
    myfile = open('_Opppcres.gds', 'rb')
    ftp.storbinary('STOR _Opppcres.gds', myfile)
    myfile.close()
