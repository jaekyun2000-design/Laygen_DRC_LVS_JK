from generatorLib import StickDiagram
from generatorLib import DesignParameters
from generatorLib import DRC


class _PbodyContact(StickDiagram._StickDiagram):
    _ParametersForDesignCalculation = dict(_InputModeArea=True, _NumberOfPbodyCOX=None, _NumberOfPbodyCOY=None, _Met1XWidth=None, _Met1YWidth=None, _COXpitch=None, _COYpitch=None, _PPEnclosure=None)

    '''
        _InputModeArea = True -> Generate PbodyContact by _Met1XWidth & _Met1YWidth
        _InputModeArea = False -> Generate PbodyContact by _NumberOfPbodyCOX & _NumberOfPbodyCOY
        
        _COXpitch & _COYpitch : Can define CONT layer's pitch by users
        _PPEnclosure : Can define gap between PIMP(BP) layer and Metal1 layer
    '''

    def __init__(self, _DesignParameter=None, _Name=None):

        if _DesignParameter != None:
            self._DesignParameter = _DesignParameter
        else:
            self._DesignParameter = dict(
                _ODLayer=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['DIFF'][0],
                                                          _Datatype=DesignParameters._LayerMapping['DIFF'][1],
                                                          _XYCoordinates=[], _XWidth=400, _YWidth=400),
                # boundary type:1, #path type:2, #sref type: 3, #gds data type: 4, #Design Name data type: 5,  #other data type: ?
                _Met1Layer=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0],
                                                            _Datatype=DesignParameters._LayerMapping['METAL1'][1],
                                                            _XYCoordinates=[], _XWidth=400, _YWidth=400),
                _PPLayer=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['PIMP'][0],
                                                          _Datatype=DesignParameters._LayerMapping['PIMP'][1],
                                                          _XYCoordinates=[], _XWidth=400, _YWidth=400),
                _COLayer=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['CONT'][0],
                                                          _Datatype=DesignParameters._LayerMapping['CONT'][1],
                                                          _XYCoordinates=[], _XWidth=400, _YWidth=400),
                # _PDKLayer=dict(_DesignParametertype=1,_Layer=DesignParameters._LayerMapping['PDK'][0], _Datatype=DesignParameters._LayerMapping['PDK'][1],_XYCoordinates=[],_XWidth=400, _YWidth=400),
                _Name=self._NameDeclaration(_Name=_Name), _GDSFile=self._GDSObjDeclaration(_GDSFile=None),

            )

        if _Name != None:
            self._DesignParameter['_Name']['_Name'] = _Name


    def _CalculatePbodyContactDesignParameter(self, _InputModeArea=True, _NumberOfPbodyCOX=None, _NumberOfPbodyCOY=None, _Met1XWidth=None, _Met1YWidth=None, _COXpitch=None, _COYpitch=None, _PPEnclosure=None):
        print('#########################################################################################################')
        print(('                                  {}  PbodyContact Calculation Start                                     '.format(self._DesignParameter['_Name']['_Name'])))
        print('#########################################################################################################')

        _DRCObj = DRC.DRC()
        MinSnapSpacing = _DRCObj._MinSnapSpacing
        _XYCoordinateOfPbodyContact = [[0,0]]

        if _COXpitch == None:
            _XpitchBtwCO = _DRCObj._CoMinWidth + _DRCObj.DRCCOMinSpace(NumOfCOX=_NumberOfPbodyCOX, NumOfCOY=_NumberOfPbodyCOY)
        else:
            _XpitchBtwCO = _COXpitch

        if _COYpitch == None:
            _YpitchBtwCO = _DRCObj._CoMinWidth + _DRCObj.DRCCOMinSpace(NumOfCOX=_NumberOfPbodyCOX, NumOfCOY=_NumberOfPbodyCOY)
        else:
            _YpitchBtwCO = _COYpitch

        if _InputModeArea == True:
            print('#############################     DIFF Layer Calculation    ##############################################')
            self._DesignParameter['_ODLayer']['_XYCoordinates'] = _XYCoordinateOfPbodyContact
            self._DesignParameter['_ODLayer']['_XWidth'] = _Met1XWidth
            self._DesignParameter['_ODLayer']['_YWidth'] = _Met1YWidth

            print('#############################     Met1 Layer Calculation    ##############################################')
            self._DesignParameter['_Met1Layer']['_XYCoordinates'] = _XYCoordinateOfPbodyContact
            self._DesignParameter['_Met1Layer']['_XWidth'] = _Met1XWidth
            self._DesignParameter['_Met1Layer']['_YWidth'] = _Met1YWidth

            print('#############################     PIMP Layer Calculation    ##############################################')
            self._DesignParameter['_PPLayer']['_XYCoordinates'] = _XYCoordinateOfPbodyContact
            if _PPEnclosure != None:
                self._DesignParameter['_PPLayer']['_XWidth'] = _Met1XWidth + _PPEnclosure * 2
                self._DesignParameter['_PPLayer']['_YWidth'] = _Met1YWidth + _PPEnclosure * 2

            else:
                if DesignParameters._Technology == 'SS28nm':
                    self._DesignParameter['_PPLayer']['_XWidth'] = self._DesignParameter['_ODLayer']['_XWidth'] + 2 * _DRCObj._PpMinExtensiononPactive2
                    self._DesignParameter['_PPLayer']['_YWidth'] = self._DesignParameter['_ODLayer']['_YWidth'] + 2 * _DRCObj._PpMinExtensiononPactive2

                    if self._DesignParameter['_PPLayer']['_YWidth'] < 170:
                        self._DesignParameter['_PPLayer']['_YWidth'] = self._DesignParameter['_ODLayer']['_YWidth'] + 2 * _DRCObj._PpMinExtensiononPactive2 + 28
                    if self._DesignParameter['_PPLayer']['_XWidth'] < 170:
                        self._DesignParameter['_PPLayer']['_XWidth'] = self._DesignParameter['_ODLayer']['_XWidth'] + 2 * _DRCObj._PpMinExtensiononPactive2 + 28

                else:
                    self._DesignParameter['_PPLayer']['_XWidth'] = self._DesignParameter['_ODLayer']['_XWidth'] + 2 * _DRCObj._PpMinExtensiononPactive
                    self._DesignParameter['_PPLayer']['_YWidth'] = self._DesignParameter['_ODLayer']['_YWidth'] + 2 * _DRCObj._PpMinExtensiononPactive

            print('#############################     CONT Layer Calculation    ##############################################')
            self._DesignParameter['_COLayer']['_XWidth'] = _DRCObj._CoMinWidth
            self._DesignParameter['_COLayer']['_YWidth'] = _DRCObj._CoMinWidth

            _NumofCOX = int((_Met1XWidth - 2 * _DRCObj._CoMinEnclosureByODAtLeastTwoSide - self._DesignParameter['_COLayer']['_XWidth']) // _XpitchBtwCO + 1)
            _NumofCOY = int((_Met1YWidth - 2 * _DRCObj._CoMinEnclosureByOD - self._DesignParameter['_COLayer']['_YWidth']) // _YpitchBtwCO + 1)

            print('_XpitchBtwCO =', _XpitchBtwCO)
            print('_YpitchBtwCO =', _YpitchBtwCO)
            print('_NumofCOX =', _NumofCOX)
            print('_NumofCOY =', _NumofCOY)

            tmp = []
            for i in range(0, _NumofCOX):
                for j in range(0, _NumofCOY):
                    if (_NumofCOX % 2) == 0 and (_NumofCOY % 2) == 0:
                        _xycoordinatetmp = [_XYCoordinateOfPbodyContact[0][0] - (_NumofCOX // 2 - 0.5) * _XpitchBtwCO + i * _XpitchBtwCO,
                                            _XYCoordinateOfPbodyContact[0][1] - (_NumofCOY // 2 - 0.5) * _YpitchBtwCO + j * _YpitchBtwCO]

                    elif (_NumofCOX % 2) == 0 and (_NumofCOY % 2) == 1:
                        _xycoordinatetmp = [_XYCoordinateOfPbodyContact[0][0] - (_NumofCOX // 2 - 0.5) * _XpitchBtwCO + i * _XpitchBtwCO,
                                            _XYCoordinateOfPbodyContact[0][1] - (_NumofCOY - 1) // 2 * _YpitchBtwCO + j * _YpitchBtwCO]

                    elif (_NumofCOX % 2) == 1 and (_NumofCOY % 2) == 0:
                        _xycoordinatetmp = [_XYCoordinateOfPbodyContact[0][0] - (_NumofCOX - 1) // 2 * _XpitchBtwCO + i * _XpitchBtwCO,
                                            _XYCoordinateOfPbodyContact[0][1] - (_NumofCOY // 2 - 0.5) * _YpitchBtwCO + j * _YpitchBtwCO]

                    elif (_NumofCOX % 2) == 1 and (_NumofCOY % 2) == 1:
                        _xycoordinatetmp = [_XYCoordinateOfPbodyContact[0][0] - (_NumofCOX - 1) // 2 * _XpitchBtwCO + i * _XpitchBtwCO,
                                            _XYCoordinateOfPbodyContact[0][1] - (_NumofCOY - 1) // 2 * _YpitchBtwCO + j * _YpitchBtwCO]
                    tmp.append(_xycoordinatetmp)

            self._DesignParameter['_COLayer']['_XYCoordinates'] = tmp
            del tmp



        else:
            print('#############################     DIFF Layer Calculation    ##############################################')
            self._DesignParameter['_ODLayer']['_XYCoordinates'] = _XYCoordinateOfPbodyContact
            if _Met1XWidth == None:
                self._DesignParameter['_ODLayer']['_XWidth'] = _DRCObj._CoMinWidth + (_NumberOfPbodyCOX - 1) * _XpitchBtwCO + 2 * _DRCObj._CoMinEnclosureByODAtLeastTwoSide
            else:
                self._DesignParameter['_ODLayer']['_XWidth'] = _Met1XWidth
            if _Met1YWidth == None:
                self._DesignParameter['_ODLayer']['_YWidth'] = _DRCObj._CoMinWidth + (_NumberOfPbodyCOY - 1) * _YpitchBtwCO + 2 * _DRCObj._CoMinEnclosureByODAtLeastTwoSide
            else:
                self._DesignParameter['_ODLayer']['_YWidth'] = _Met1YWidth

            print('#############################     Met1 Layer Calculation    ##############################################')
            self._DesignParameter['_Met1Layer']['_XYCoordinates'] = _XYCoordinateOfPbodyContact
            self._DesignParameter['_Met1Layer']['_XWidth'] = self._DesignParameter['_ODLayer']['_XWidth']
            self._DesignParameter['_Met1Layer']['_YWidth'] = self._DesignParameter['_ODLayer']['_YWidth']

            print('#############################     PIMP Layer Calculation    ##############################################')
            self._DesignParameter['_PPLayer']['_XYCoordinates'] = _XYCoordinateOfPbodyContact
            if _PPEnclosure != None:
                self._DesignParameter['_PPLayer']['_XWidth'] = self._DesignParameter['_ODLayer']['_XWidth'] + _PPEnclosure * 2
                self._DesignParameter['_PPLayer']['_YWidth'] = self._DesignParameter['_ODLayer']['_YWidth'] + _PPEnclosure * 2

            else:
                if DesignParameters._Technology == 'SS28nm':
                    self._DesignParameter['_PPLayer']['_XWidth'] = self._DesignParameter['_ODLayer']['_XWidth'] + 2 * _DRCObj._PpMinExtensiononPactive2
                    self._DesignParameter['_PPLayer']['_YWidth'] = self._DesignParameter['_ODLayer']['_YWidth'] + 2 * _DRCObj._PpMinExtensiononPactive2

                    if self._DesignParameter['_PPLayer']['_YWidth'] < 170:
                        self._DesignParameter['_PPLayer']['_YWidth'] = self._DesignParameter['_ODLayer']['_YWidth'] + 2 * _DRCObj._PpMinExtensiononPactive2 + 28
                    if self._DesignParameter['_PPLayer']['_XWidth'] < 170:
                        self._DesignParameter['_PPLayer']['_XWidth'] = self._DesignParameter['_ODLayer']['_XWidth'] + 2 * _DRCObj._PpMinExtensiononPactive2 + 28

                else:
                    self._DesignParameter['_PPLayer']['_XWidth'] = self._DesignParameter['_ODLayer']['_XWidth'] + 2 * _DRCObj._PpMinExtensiononPactive
                    self._DesignParameter['_PPLayer']['_YWidth'] = self._DesignParameter['_ODLayer']['_YWidth'] + 2 * _DRCObj._PpMinExtensiononPactive

            print('#############################     CONT Layer Calculation    ##############################################')
            self._DesignParameter['_COLayer']['_XWidth'] = _DRCObj._CoMinWidth
            self._DesignParameter['_COLayer']['_YWidth'] = _DRCObj._CoMinWidth

            _NumofCOX = _NumberOfPbodyCOX
            _NumofCOY = _NumberOfPbodyCOY

            tmp = []
            for i in range(0, _NumofCOX):
                for j in range(0, _NumofCOY):
                    if (_NumofCOX % 2) == 0 and (_NumofCOY % 2) == 0:
                        _xycoordinatetmp = [_XYCoordinateOfPbodyContact[0][0] - (_NumofCOX // 2 - 0.5) * _XpitchBtwCO + i * _XpitchBtwCO,
                                            _XYCoordinateOfPbodyContact[0][1] - (_NumofCOY // 2 - 0.5) * _YpitchBtwCO + j * _YpitchBtwCO]

                    elif (_NumofCOX % 2) == 0 and (_NumofCOY % 2) == 1:
                        _xycoordinatetmp = [_XYCoordinateOfPbodyContact[0][0] - (_NumofCOX // 2 - 0.5) * _XpitchBtwCO + i * _XpitchBtwCO,
                                            _XYCoordinateOfPbodyContact[0][1] - (_NumofCOY - 1) // 2 * _YpitchBtwCO + j * _YpitchBtwCO]

                    elif (_NumofCOX % 2) == 1 and (_NumofCOY % 2) == 0:
                        _xycoordinatetmp = [_XYCoordinateOfPbodyContact[0][0] - (_NumofCOX - 1) // 2 * _XpitchBtwCO + i * _XpitchBtwCO,
                                            _XYCoordinateOfPbodyContact[0][1] - (_NumofCOY // 2 - 0.5) * _YpitchBtwCO + j * _YpitchBtwCO]

                    elif (_NumofCOX % 2) == 1 and (_NumofCOY % 2) == 1:
                        _xycoordinatetmp = [_XYCoordinateOfPbodyContact[0][0] - (_NumofCOX - 1) // 2 * _XpitchBtwCO + i * _XpitchBtwCO,
                                            _XYCoordinateOfPbodyContact[0][1] - (_NumofCOY - 1) // 2 * _XpitchBtwCO + j * _XpitchBtwCO]
                    tmp.append(_xycoordinatetmp)

            self._DesignParameter['_COLayer']['_XYCoordinates'] = tmp
            del tmp

        print('#########################################################################################################')
        print(('                                  {}  PbodyContact Calculation End                                   '.format(self._DesignParameter['_Name']['_Name'])))
        print('#########################################################################################################')



if __name__ == '__main__':
    DesignParameters._Technology = 'SS28nm'
    PbodyContactObj = _PbodyContact(_DesignParameter=None, _Name='PbodyContact')
    PbodyContactObj._CalculatePbodyContactDesignParameter(_InputModeArea=True, _NumberOfPbodyCOX=3, _NumberOfPbodyCOY=58, _Met1XWidth=348, _Met1YWidth=8272, _COXpitch=142, _COYpitch=142, _PPEnclosure=56)
    PbodyContactObj._UpdateDesignParameter2GDSStructure(_DesignParameterInDictionary=PbodyContactObj._DesignParameter)
    _fileName = 'PbodyContact.gds'
    testStreamFile = open('./PbodyContact.gds', 'wb')
    tmp = PbodyContactObj._CreateGDSStream(PbodyContactObj._DesignParameter['_GDSFile']['_GDSFile'])
    tmp.write_binary_gds_stream(testStreamFile)
    testStreamFile.close()

    print('#############################      Sending to FTP Server...      ##############################')

    import ftplib

    ftp = ftplib.FTP('141.223.24.53')
    ftp.login('smlim96', 'min753531')
    ftp.cwd('/mnt/sdc/smlim96/OPUS/ss28')
    myfile = open('PbodyContact.gds', 'rb')
    ftp.storbinary('STOR PbodyContact.gds', myfile)
    myfile.close()