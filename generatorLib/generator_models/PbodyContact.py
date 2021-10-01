from generatorLib import StickDiagram
from generatorLib import DesignParameters
from generatorLib import DRC

class _PbodyContact(StickDiagram._StickDiagram):
    _ParametersForDesignCalculation = dict(_NumberOfPbodyCOX=None, _NumberOfPbodyCOY=None,
                                           _Met1XWidth=None, _Met1YWidth=None)

    def __init__(self, _DesignParameter=None, _Name=None):

        if _DesignParameter != None:
            self._DesignParameter = _DesignParameter
        else:
            self._DesignParameter = dict(
                _Name=self._NameDeclaration(_Name=_Name), _GDSFile=self._GDSObjDeclaration(_GDSFile=None)
            )

        if _Name != None:
            self._DesignParameter['_Name']['_Name'] = _Name


    def _CalculatePbodyContactDesignParameter(self,  _NumberOfPbodyCOX=None, _NumberOfPbodyCOY=None,  _Met1XWidth=None, _Met1YWidth=None):
        """

        :param _NumberOfPbodyCOX: (Essential)
        :param _NumberOfPbodyCOY: (Essential)
        :param _Met1XWidth: (Optional)
        :param _Met1YWidth: (Optional)
        :return:
        """

        print ('#########################################################################################################')
        print ('                                  {}  PbodyContact Calculation Start                                     '.format(self._DesignParameter['_Name']['_Name']))
        print ('#########################################################################################################')

        _DRCObj = DRC.DRC()
        _XYCoordinateOfPbodyContact = [[0, 0]]

        _LengthPbodyBtwCO = _DRCObj._CoMinWidth + _DRCObj.DRCCOMinSpace(NumOfCOX=_NumberOfPbodyCOX, NumOfCOY=_NumberOfPbodyCOY)


        print ('#############################     DIFF Layer Calculation    ##############################################')
        self._DesignParameter['_ODLayer'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['DIFF'][0],
                                                                             _Datatype=DesignParameters._LayerMapping['DIFF'][1],
                                                                             _XYCoordinates=[], _XWidth=400,
                                                                             _YWidth=400)
        self._DesignParameter['_ODLayer']['_XWidth'] = _DRCObj._CoMinWidth + (_NumberOfPbodyCOX - 1) * _LengthPbodyBtwCO + 2 * _DRCObj._CoMinEnclosureByODAtLeastTwoSide
        self._DesignParameter['_ODLayer']['_YWidth'] = _DRCObj._CoMinWidth + (_NumberOfPbodyCOY - 1) * _LengthPbodyBtwCO + 2 * _DRCObj._CoMinEnclosureByODAtLeastTwoSide
        self._DesignParameter['_ODLayer']['_XYCoordinates'] = _XYCoordinateOfPbodyContact


        print ('#############################     PIMP  Layer Calculation    ##############################################')
        self._DesignParameter['_PPLayer'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['PIMP'][0],
                                                                             _Datatype=DesignParameters._LayerMapping['PIMP'][1],
                                                                             _XYCoordinates=[], _XWidth=400, _YWidth=400)
        self._DesignParameter['_PPLayer']['_XYCoordinates'] = _XYCoordinateOfPbodyContact
        self._DesignParameter['_PPLayer']['_XWidth'] = max(self._DesignParameter['_ODLayer']['_XWidth'] + 2 * _DRCObj._PpMinExtensiononPactive2, _DRCObj._PpMinWidth)
        self._DesignParameter['_PPLayer']['_YWidth'] = max(self._DesignParameter['_ODLayer']['_YWidth'] + 2 * _DRCObj._PpMinExtensiononPactive2, _DRCObj._PpMinWidth)


        print ('###########################     Metal1  Layer Calculation    ##############################################')
        Met1XWidth = 0 if (_Met1XWidth == None) else _Met1XWidth
        Met1YWidth = 0 if (_Met1YWidth == None) else _Met1YWidth
        self._DesignParameter['_Met1Layer'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0],
                                                                               _Datatype=DesignParameters._LayerMapping['METAL1'][1],
                                                                               _XYCoordinates=[], _XWidth=400, _YWidth=400)
        self._DesignParameter['_Met1Layer']['_XWidth'] = max(self._DesignParameter['_ODLayer']['_XWidth'], Met1XWidth)
        self._DesignParameter['_Met1Layer']['_YWidth'] = max(self._DesignParameter['_ODLayer']['_YWidth'], Met1YWidth)
        self._DesignParameter['_Met1Layer']['_XYCoordinates'] = _XYCoordinateOfPbodyContact


        print ('#############################     CONT Layer Caculation    ##############################################')
        tmpXYs = []
        for i in range(0, _NumberOfPbodyCOX):
            for j in range(0, _NumberOfPbodyCOY):

                if (_NumberOfPbodyCOX % 2) == 0 and (_NumberOfPbodyCOY % 2) == 0:
                    _xycoordinatetmp = [_XYCoordinateOfPbodyContact[0][0] - (_NumberOfPbodyCOX / 2 - 0.5) * _LengthPbodyBtwCO + i * _LengthPbodyBtwCO,
                                        _XYCoordinateOfPbodyContact[0][1] - (_NumberOfPbodyCOY / 2 - 0.5) * _LengthPbodyBtwCO + j * _LengthPbodyBtwCO]

                elif (_NumberOfPbodyCOX % 2) == 0 and (_NumberOfPbodyCOY % 2) == 1:
                    _xycoordinatetmp = [_XYCoordinateOfPbodyContact[0][0] - (_NumberOfPbodyCOX / 2 - 0.5) * _LengthPbodyBtwCO + i * _LengthPbodyBtwCO,
                                        _XYCoordinateOfPbodyContact[0][1] - (_NumberOfPbodyCOY - 1) / 2 * _LengthPbodyBtwCO + j * _LengthPbodyBtwCO]

                elif (_NumberOfPbodyCOX % 2) == 1 and (_NumberOfPbodyCOY % 2) == 0:
                    _xycoordinatetmp = [_XYCoordinateOfPbodyContact[0][0] - (_NumberOfPbodyCOX - 1) / 2 * _LengthPbodyBtwCO + i * _LengthPbodyBtwCO,
                                        _XYCoordinateOfPbodyContact[0][1] - (_NumberOfPbodyCOY / 2 - 0.5) * _LengthPbodyBtwCO + j * _LengthPbodyBtwCO]

                else:
                    _xycoordinatetmp = [_XYCoordinateOfPbodyContact[0][0] - (_NumberOfPbodyCOX - 1) / 2 * _LengthPbodyBtwCO + i * _LengthPbodyBtwCO,
                                        _XYCoordinateOfPbodyContact[0][1] - (_NumberOfPbodyCOY - 1) / 2 * _LengthPbodyBtwCO + j * _LengthPbodyBtwCO]

                tmpXYs.append(_xycoordinatetmp)

        self._DesignParameter['_COLayer'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['CONT'][0],
                                                                             _Datatype=DesignParameters._LayerMapping['CONT'][1],
                                                                             _XYCoordinates=[], _XWidth=400, _YWidth=400)
        self._DesignParameter['_COLayer']['_XWidth'] = _DRCObj._CoMinWidth
        self._DesignParameter['_COLayer']['_YWidth'] = _DRCObj._CoMinWidth
        self._DesignParameter['_COLayer']['_XYCoordinates'] = tmpXYs


        print ('#########################################################################################################')
        print ('                                  {}  PbodyContact Calculation End                                   '.format(self._DesignParameter['_Name']['_Name']))
        print ('#########################################################################################################')