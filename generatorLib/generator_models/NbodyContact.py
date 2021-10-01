from generatorLib import StickDiagram
from generatorLib import DesignParameters
from generatorLib import DRC

class _NbodyContact(StickDiagram._StickDiagram):
    _ParametersForDesignCalculation = dict(_NumberOfNbodyCOX=None, _NumberOfNbodyCOY=None,
                                           _Met1XWidth=None, _Met1YWidth=None)

    def __init__(self, _DesignParameter=None, _Name=None):

        if _DesignParameter != None:
            self._DesignParameter = _DesignParameter
        else:
            self._DesignParameter = dict(
                _Name=self._NameDeclaration(_Name=_Name), _GDSFile=self._GDSObjDeclaration(_GDSFile=None),
            )

        if _Name != None:
            self._DesignParameter['_Name']['_Name'] = _Name


    def _CalculateNbodyContactDesignParameter(self, _NumberOfNbodyCOX=None, _NumberOfNbodyCOY=None,  _Met1XWidth=None, _Met1YWidth=None):
        """

        :param _NumberOfNbodyCOX: (Essential)
        :param _NumberOfNbodyCOY: (Essential)
        :param _Met1XWidth: (Optional)
        :param _Met1YWidth: (Optional)
        :return:
        """

        print ('#########################################################################################################')
        print ('                                  {}  NbodyContact Calculation Start                                     '.format(self._DesignParameter['_Name']['_Name']))
        print ('#########################################################################################################')

        _DRCObj = DRC.DRC()
        _XYCoordinateOfNbodyContact = [[0, 0]]

        _LengthNbodyBtwCO = _DRCObj._CoMinWidth + _DRCObj.DRCCOMinSpace(NumOfCOX=_NumberOfNbodyCOX, NumOfCOY=_NumberOfNbodyCOY)


        print ('#############################     DIFF Layer Calculation    ##############################################')
        self._DesignParameter['_ODLayer'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['DIFF'][0],
                                                                             _Datatype=DesignParameters._LayerMapping['DIFF'][1],
                                                                             _XYCoordinates=[], _XWidth=400,
                                                                             _YWidth=400)  # boundary type:1, #path type:2, #sref type: 3, #gds data type: 4, #Design Name data type: 5,  #other data type: ?
        self._DesignParameter['_ODLayer']['_XWidth'] = _DRCObj._CoMinWidth + (_NumberOfNbodyCOX - 1) * _LengthNbodyBtwCO + 2 * _DRCObj._CoMinEnclosureByODAtLeastTwoSide
        self._DesignParameter['_ODLayer']['_YWidth'] = _DRCObj._CoMinWidth + (_NumberOfNbodyCOY - 1) * _LengthNbodyBtwCO + 2 * _DRCObj._CoMinEnclosureByODAtLeastTwoSide
        self._DesignParameter['_ODLayer']['_XYCoordinates'] = _XYCoordinateOfNbodyContact


        if DesignParameters._Technology != 'SS28nm':  # @ Samsung 28nm, There is No 'NPLayer(NIMP)'
            print ('#############################     NIMP  Layer Calculation    ##############################################')
            self._DesignParameter['_NPLayer'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['NIMP'][0],
                                                                                 _Datatype=DesignParameters._LayerMapping['NIMP'][1],
                                                                                 _XYCoordinates=[], _XWidth=400, _YWidth=400)
            self._DesignParameter['_NPLayer']['_XWidth'] = max(self._DesignParameter['_ODLayer']['_XWidth'] + 2 * _DRCObj._NpMinExtensiononNactive2, _DRCObj._NpMinWidth)
            self._DesignParameter['_NPLayer']['_YWidth'] = max(self._DesignParameter['_ODLayer']['_YWidth'] + 2 * _DRCObj._NpMinExtensiononNactive2, _DRCObj._NpMinWidth)
            self._DesignParameter['_NPLayer']['_XYCoordinates'] = _XYCoordinateOfNbodyContact


        print ('###########################     Metal1  Layer Calculation    ##############################################')
        Met1XWidth = 0 if (_Met1XWidth == None) else _Met1XWidth
        Met1YWidth = 0 if (_Met1YWidth == None) else _Met1YWidth
        self._DesignParameter['_Met1Layer'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0],
                                                                               _Datatype=DesignParameters._LayerMapping['METAL1'][1],
                                                                               _XYCoordinates=[], _XWidth=400, _YWidth=400)
        self._DesignParameter['_Met1Layer']['_XWidth'] = max(self._DesignParameter['_ODLayer']['_XWidth'], Met1XWidth)
        self._DesignParameter['_Met1Layer']['_YWidth'] = max(self._DesignParameter['_ODLayer']['_YWidth'], Met1YWidth)
        self._DesignParameter['_Met1Layer']['_XYCoordinates'] = _XYCoordinateOfNbodyContact


        print ('#############################     CONT Layer Caculation    ##############################################')
        tmpXYs = []
        for i in range(0, _NumberOfNbodyCOX):
            for j in range(0, _NumberOfNbodyCOY):

                if (_NumberOfNbodyCOX % 2) == 0 and (_NumberOfNbodyCOY % 2) == 0:
                    _xycoordinatetmp = [_XYCoordinateOfNbodyContact[0][0] - (_NumberOfNbodyCOX / 2 - 0.5) * _LengthNbodyBtwCO + i * _LengthNbodyBtwCO,
                                        _XYCoordinateOfNbodyContact[0][1] - (_NumberOfNbodyCOY / 2 - 0.5) * _LengthNbodyBtwCO + j * _LengthNbodyBtwCO]

                elif (_NumberOfNbodyCOX % 2) == 0 and (_NumberOfNbodyCOY % 2) == 1:
                    _xycoordinatetmp = [_XYCoordinateOfNbodyContact[0][0] - (_NumberOfNbodyCOX / 2 - 0.5) * _LengthNbodyBtwCO + i * _LengthNbodyBtwCO,
                                        _XYCoordinateOfNbodyContact[0][1] - (_NumberOfNbodyCOY - 1) / 2 * _LengthNbodyBtwCO + j * _LengthNbodyBtwCO]

                elif (_NumberOfNbodyCOX % 2) == 1 and (_NumberOfNbodyCOY % 2) == 0:
                    _xycoordinatetmp = [_XYCoordinateOfNbodyContact[0][0] - (_NumberOfNbodyCOX - 1) / 2 * _LengthNbodyBtwCO + i * _LengthNbodyBtwCO,
                                        _XYCoordinateOfNbodyContact[0][1] - (_NumberOfNbodyCOY / 2 - 0.5) * _LengthNbodyBtwCO + j * _LengthNbodyBtwCO]

                else:
                    _xycoordinatetmp = [_XYCoordinateOfNbodyContact[0][0] - (_NumberOfNbodyCOX - 1) / 2 * _LengthNbodyBtwCO + i * _LengthNbodyBtwCO,
                                        _XYCoordinateOfNbodyContact[0][1] - (_NumberOfNbodyCOY - 1) / 2 * _LengthNbodyBtwCO + j * _LengthNbodyBtwCO]

                tmpXYs.append(_xycoordinatetmp)
        self._DesignParameter['_COLayer'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['CONT'][0],
                                                                             _Datatype=DesignParameters._LayerMapping['CONT'][1],
                                                                             _XYCoordinates=[], _XWidth=400, _YWidth=400)

        self._DesignParameter['_COLayer']['_XWidth'] = _DRCObj._CoMinWidth
        self._DesignParameter['_COLayer']['_YWidth'] = _DRCObj._CoMinWidth
        self._DesignParameter['_COLayer']['_XYCoordinates'] = tmpXYs


        print ('#########################################################################################################')
        print ('                                  {}  NbodyContact Calculation End                                       '.format(self._DesignParameter['_Name']['_Name']))
        print ('#########################################################################################################')