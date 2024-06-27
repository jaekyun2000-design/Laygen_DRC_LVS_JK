import copy

from generatorLib import StickDiagram
from generatorLib import DesignParameters
from generatorLib import DRC

from generatorLib import CoordinateCalc as CoordCalc


class SupplyRail(StickDiagram._StickDiagram):
    _ParametersForDesignCalculation = dict(NumPitch=None,   #
                                           UnitPitch=130,   #
                                           Met1YWidth=80,   #
                                           Met2YWidth=300,  #
                                           PpNpYWidth=180,  #
                                           isPbody=False,
                                           deleteViaAndMet1=False
                                           )

    def __init__(self, _DesignParameter=None, _Name=None):

        if _DesignParameter != None:
            self._DesignParameter = _DesignParameter
        else:
            self._DesignParameter = dict(
                _ODLayer=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['DIFF'][0],_Datatype=DesignParameters._LayerMapping['DIFF'][1], _XYCoordinates=[],_XWidth=400, _YWidth=400),
                _Met1Layer=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0],_Datatype=DesignParameters._LayerMapping['METAL1'][1], _XYCoordinates=[],_XWidth=400, _YWidth=400),
                _Met2Layer=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0],_Datatype=DesignParameters._LayerMapping['METAL2'][1], _XYCoordinates=[],_XWidth=400, _YWidth=400),
                _COLayer=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['CONT'][0], _Datatype=DesignParameters._LayerMapping['CONT'][1], _XYCoordinates=[], _XWidth=400, _YWidth=400),
                _Via1Layer=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['VIA12'][0], _Datatype=DesignParameters._LayerMapping['VIA12'][1], _XYCoordinates=[], _XWidth=400, _YWidth=400),
                _Name=self._NameDeclaration(_Name=_Name), _GDSFile=self._GDSObjDeclaration(_GDSFile=None),
            )
        if _Name != None:
            self._DesignParameter['_Name']['_Name'] = _Name


    def _CalculateDesignParameter(self,
                                  NumPitch=None, UnitPitch=130,
                                  Met1YWidth=80, Met2YWidth=300, PpNpYWidth=180,
                                  isPbody=False, deleteViaAndMet1=False
                                  ):
        """ Supply Rails for Onesemicon Style

        Generate Supply Rails(VSS/VDD) containing up to Metal2 Layer.
        Default Setting : {NumPitch=None, UnitPitch=130, Met1YWidth=80, Met2YWidth=300, PpNpYWidth=180}

        Args:
            NumPitch (int): the number of pitch(contact).
            UnitPitch (int | float): (center-to-center) distance between contacts.
            Met1YWidth (int | float):
            Met2YWidth (int | float):
            PpNpYWidth (int | float): PP(BP)/NP Layer YWidth
            isPbody (bool): If true, it contains PP(BP) Layer(VSS Rail). Or, VDD Rail.
            deleteViaAndMet1 (bool): If true, delete CO,Met1,Via1 Layers(For use with Z_PWR_CNT).
        """

        _DRCObj = DRC.DRC()
        _Name = self._DesignParameter['_Name']['_Name']
        _XYCoord = [[0, 0]]

        print('\n' + ''.center(105,'#'))
        print('     {} Calculation Start     '.format(_Name).center(105,'#'))
        print(''.center(105, '#') + '\n')

        ''' Calculate XWidth '''
        _XWidth = NumPitch * UnitPitch if (NumPitch is not None) and (UnitPitch is not None) else 0
        assert _XWidth != 0, "You should input 'XWidth' or {'NumPitch' & 'UnitPitch'} "

        _YWidth = Met1YWidth
        assert _YWidth >= _DRCObj._OdMinWidth

        ''' --------------------------------------   DIFF Layer Calculation   -------------------------------------- '''
        self._DesignParameter['_ODLayer']['_XWidth'] = _XWidth
        self._DesignParameter['_ODLayer']['_YWidth'] = _YWidth
        self._DesignParameter['_ODLayer']['_XYCoordinates'] = _XYCoord

        ''' -------------------------------------   Metal1 Layer Calculation   ------------------------------------- '''
        self._DesignParameter['_Met1Layer']['_XWidth'] = self.getXWidth('_ODLayer')
        self._DesignParameter['_Met1Layer']['_YWidth'] = self.getYWidth('_ODLayer')
        self._DesignParameter['_Met1Layer']['_XYCoordinates'] = self.getXY('_ODLayer')

        ''' -------------------------------------   Metal2 Layer Calculation   ------------------------------------- '''
        self._DesignParameter['_Met2Layer']['_XWidth'] = self.getXWidth('_ODLayer')
        self._DesignParameter['_Met2Layer']['_YWidth'] = Met2YWidth
        self._DesignParameter['_Met2Layer']['_XYCoordinates'] = self.getXY('_ODLayer')


        ''' -----------------------------------   NP/PP(BP) Layer Calculation   ------------------------------------ '''
        if isPbody:
            assert PpNpYWidth >= max(self.getYWidth('_ODLayer') + 2*_DRCObj._PpMinExtensiononPactive2, _DRCObj._PpMinWidth)
            self._DesignParameter['_PPLayer'] = self._BoundaryElementDeclaration(
                _Layer=DesignParameters._LayerMapping['PIMP'][0],
                _Datatype=DesignParameters._LayerMapping['PIMP'][1],
                _XWidth=max(self.getXWidth('_ODLayer') + 2*_DRCObj._PpMinExtensiononPactive2, _DRCObj._PpMinWidth),
                _YWidth=PpNpYWidth,
                _XYCoordinates=_XYCoord,
            )
        else:
            if DesignParameters._Technology != 'SS28nm':             # @ Samsung 28nm, There is No 'NPLayer(NIMP)'
                assert PpNpYWidth >= max(self.getYWidth('_ODLayer') + 2 * _DRCObj._NpMinExtensiononNactive2, _DRCObj._NpMinWidth)
                self._DesignParameter['_NPLayer'] = self._BoundaryElementDeclaration(
                    _Layer=DesignParameters._LayerMapping['NIMP'][0],
                    _Datatype=DesignParameters._LayerMapping['NIMP'][1],
                    _XWidth=max(self.getXWidth('_ODLayer') + 2*_DRCObj._NpMinExtensiononNactive2, _DRCObj._NpMinWidth),
                    _YWidth=PpNpYWidth,
                    _XYCoordinates=_XYCoord,
                )
            else:
                pass

        ''' -----------------------------------   CONT/Via1 Layer Calculation   ------------------------------------ '''
        tmpXYs = []
        for i in range(0, NumPitch):
            tmpXYs.append(CoordCalc.Add(_XYCoord[0], [-(NumPitch - 1) / 2 * UnitPitch + i * UnitPitch, 0]))

        self._DesignParameter['_COLayer']['_XWidth'] = _DRCObj._CoMinWidth
        self._DesignParameter['_COLayer']['_YWidth'] = _DRCObj._CoMinWidth
        self._DesignParameter['_COLayer']['_XYCoordinates'] = tmpXYs

        self._DesignParameter['_Via1Layer']['_XWidth'] = _DRCObj._VIAxMinWidth
        self._DesignParameter['_Via1Layer']['_YWidth'] = _DRCObj._VIAxMinWidth
        self._DesignParameter['_Via1Layer']['_XYCoordinates'] = tmpXYs

        if deleteViaAndMet1 == True:
            del self._DesignParameter['_COLayer'], self._DesignParameter['_Via1Layer'], self._DesignParameter['_Met1Layer']
        else:   # False | None
            pass



        print('\n' + ''.center(105, '#'))
        print('     {} Calculation End     '.format(_Name).center(105,'#'))
        print(''.center(105, '#') + '\n')


if __name__ == '__main__':
    from Private import MyInfo
    import DRCchecker
    My = MyInfo.USER(DesignParameters._Technology)

    libname = 'TEST_MOS'
    cellname = 'SupplyRail_1'
    _fileName = cellname + '.gds'

    ''' Generate Layout Object '''
    LayoutObj = SupplyRail(_Name=cellname)
    InputParams = copy.deepcopy(SupplyRail._ParametersForDesignCalculation)
    InputParams.update({
        'NumPitch':  3,
        'UnitPitch': 130,
        'XWidth':    None,
        'isPbody':   True
    })
    LayoutObj._CalculateDesignParameter(**InputParams)
    LayoutObj._UpdateDesignParameter2GDSStructure(_DesignParameterInDictionary=LayoutObj._DesignParameter)
    testStreamFile = open('./{}'.format(_fileName), 'wb')
    tmp = LayoutObj._CreateGDSStream(LayoutObj._DesignParameter['_GDSFile']['_GDSFile'])
    tmp.write_binary_gds_stream(testStreamFile)
    testStreamFile.close()

    print('#############################      Sending to FTP Server...      #############################')

    Checker = DRCchecker.DRCchecker(
        username=My.ID,
        password=My.PW,
        WorkDir=My.Dir_Work,
        DRCrunDir=My.Dir_DRCrun,
        libname=libname,
        cellname=cellname,
    )
    Checker.Upload2FTP()
    Checker.StreamIn(tech=DesignParameters._Technology)
    print('#############################      Finished      ################################')
