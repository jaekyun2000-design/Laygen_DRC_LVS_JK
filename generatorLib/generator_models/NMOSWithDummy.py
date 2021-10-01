from generatorLib import CoordinateCalc
from generatorLib import StickDiagram
from generatorLib import DesignParameters
from generatorLib import DRC


class _NMOS(StickDiagram._StickDiagram):
    _ParametersForDesignCalculation = dict(_NMOSNumberofGate=None, _NMOSChannelWidth=None, _NMOSChannellength=None,
                                           _NMOSDummy=False, _XVT=None)

    def __init__(self, _DesignParameter=None, _Name=None):

        if _DesignParameter != None:
            self._DesignParameter = _DesignParameter
        else:
            self._DesignParameter = dict(
                _Name=self._NameDeclaration(_Name=_Name), _GDSFile=self._GDSObjDeclaration(_GDSFile=None),
                _XYCoordinateNMOSSupplyRouting=dict(_DesignParametertype=7, _XYCoordinates=[]),
                _XYCoordinateNMOSOutputRouting=dict(_DesignParametertype=7, _XYCoordinates=[]),
                _XYCoordinateNMOSGateRouting=dict(_DesignParametertype=7, _XYCoordinates=[]),
            )

        if _Name != None:
            self._DesignParameter['_Name']['_Name'] = _Name

    def _CalculateNMOSDesignParameter(self, _NMOSNumberofGate=None, _NMOSChannelWidth=None, _NMOSChannellength=None, _NMOSDummy=False, _XVT=None):
        """

        :param _NMOSNumberofGate:
        :param _NMOSChannelWidth:
        :param _NMOSChannellength:
        :param _NMOSDummy:
        :param _XVT:
        :return:
        """

        self._DesignParameter['_ODLayer'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['DIFF'][0],
                                                                             _Datatype=DesignParameters._LayerMapping['DIFF'][1],
                                                                             _XYCoordinates=[], _XWidth=400, _YWidth=400)
        self._DesignParameter['_ODLayerPINDrawing'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['RXPIN'][0],
                                                                                       _Datatype=DesignParameters._LayerMapping['RXPIN'][1],
                                                                                       _XYCoordinates=[], _XWidth=400, _YWidth=400)
        self._DesignParameter['_PODummyLayer'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0],
                                                                                  _Datatype=DesignParameters._LayerMapping['POLY'][1],
                                                                                  _XYCoordinates=[], _XWidth=400, _YWidth=400)
        self._DesignParameter['_SLVTLayer'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['SLVT'][0],
                                                                               _Datatype=DesignParameters._LayerMapping['SLVT'][1],
                                                                               _XYCoordinates=[], _XWidth=400, _YWidth=400)
        self._DesignParameter['_LVTLayer'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['LVT'][0],
                                                                              _Datatype=DesignParameters._LayerMapping['LVT'][1],
                                                                              _XYCoordinates=[], _XWidth=400, _YWidth=400)
        self._DesignParameter['_RVTLayer'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['RVT'][0],
                                                                              _Datatype=DesignParameters._LayerMapping['RVT'][1],
                                                                              _XYCoordinates=[], _XWidth=400, _YWidth=400)
        self._DesignParameter['_HVTLayer'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['HVT'][0],
                                                                              _Datatype=DesignParameters._LayerMapping['HVT'][1],
                                                                              _XYCoordinates=[], _XWidth=400, _YWidth=400)
        self._DesignParameter['_POLayer'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0],
                                                                             _Datatype=DesignParameters._LayerMapping['POLY'][1],
                                                                             _XYCoordinates=[], _XWidth=400, _YWidth=400)

        print ('#########################################################################################################')
        print ('                                    {}  NMOS Calculation Start                                    '.format(self._DesignParameter['_Name']['_Name']))
        print ('#########################################################################################################')
        _DRCObj = DRC.DRC()
        _XYCoordinateOfNMOS = [[0, 0]]

        _LengthNMOSBtwCO = _DRCObj._CoMinSpace + _DRCObj._CoMinWidth

        if DesignParameters._Technology == 'SS28nm':  # Need to Modify
            _LengthNMOSBtwPO = _DRCObj.DRCPolyMinSpace(_Width=_NMOSChannelWidth, _ParallelLength=_NMOSChannellength) + _NMOSChannellength
        else:
            _LengthNMOSBtwPO = _DRCObj.DRCPolygateMinSpace(_DRCObj._CoMinWidth + 2 * _DRCObj._PolygateMinSpace2Co) + _NMOSChannellength


        print ('#############################     POLY Layer Calculation    ##############################################')
        # POLY Layer Coordinate Calc
        tmpXY_PO = []
        for i in range(0, _NMOSNumberofGate):
            if (_NMOSNumberofGate % 2) == 0:
                _xycoordinatetmp = [_XYCoordinateOfNMOS[0][0] - (_NMOSNumberofGate / 2 - 0.5) * _LengthNMOSBtwPO + i * _LengthNMOSBtwPO,
                                    _XYCoordinateOfNMOS[0][1]]
            else:
                _xycoordinatetmp = [_XYCoordinateOfNMOS[0][0] - (_NMOSNumberofGate - 1) / 2 * _LengthNMOSBtwPO + i * _LengthNMOSBtwPO,
                                    _XYCoordinateOfNMOS[0][1]]
            tmpXY_PO.append(_xycoordinatetmp)

        self._DesignParameter['_POLayer']['_XWidth'] = _NMOSChannellength
        self._DesignParameter['_POLayer']['_YWidth'] = _NMOSChannelWidth + 2 * _DRCObj.DRCPolygateMinExtensionOnOD(_NMOSChannellength)
        self._DesignParameter['_POLayer']['_XYCoordinates'] = tmpXY_PO


        if _NMOSDummy:
            print ('#############################     POLY Dummy Layer Calculation    ##############################################')
            self._DesignParameter['_PODummyLayer']['_XWidth'] = _NMOSChannellength
            self._DesignParameter['_PODummyLayer']['_YWidth'] = _NMOSChannelWidth + 2 * _DRCObj._PolygateMinExtensionOnOD  # ??

            _tmpXY_Dummy = [
                CoordinateCalc.Add(self._DesignParameter['_POLayer']['_XYCoordinates'][0], [-_LengthNMOSBtwPO, 0]),
                CoordinateCalc.Add(self._DesignParameter['_POLayer']['_XYCoordinates'][-1], [_LengthNMOSBtwPO, 0]),
            ]
            self._DesignParameter['_PODummyLayer']['_XYCoordinates'] = _tmpXY_Dummy

            if float(self._DesignParameter['_PODummyLayer']['_XWidth']) * float(self._DesignParameter['_PODummyLayer']['_YWidth']) < _DRCObj._PODummyMinArea:
                self._DesignParameter['_PODummyLayer']['_YWidth'] = self.CeilMinSnapSpacing(float(_DRCObj._PODummyMinArea) / float(self._DesignParameter['_PODummyLayer']['_XWidth']), _DRCObj._MinSnapSpacing*2)
                if DesignParameters._Technology != 'SS28nm':
                    self._DesignParameter['_POLayer']['_YWidth'] = self._DesignParameter['_PODummyLayer']['_YWidth']
            else:
                pass
        else:
            del self._DesignParameter['_PODummyLayer']


        print ('#############################     DIFF (OD/RX) Layer Calculation    ##############################################')
        if _NMOSDummy and DesignParameters._Technology != 'SS28nm':
            XWidth_OD = self._DesignParameter['_PODummyLayer']['_XYCoordinates'][-1][0] - self._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][0] + _NMOSChannellength + 2 * _DRCObj._PolygateMinExtensionOnODX
        else:
            XWidth_OD = _LengthNMOSBtwPO * _NMOSNumberofGate + _DRCObj._CoMinWidth + 2 * _DRCObj._CoMinEnclosureByOD
        self._DesignParameter['_ODLayer']['_XWidth'] = XWidth_OD
        self._DesignParameter['_ODLayer']['_YWidth'] = _NMOSChannelWidth
        self._DesignParameter['_ODLayer']['_XYCoordinates'] = _XYCoordinateOfNMOS


        print ('#############################     METAL1 Layer Calculation    ##############################################')
        # METAL1 Layer Coordinate Setting
        _LengthNMOSBtwMet1 = _LengthNMOSBtwPO

        tmpXY_M1 = []
        for i in range(0, _NMOSNumberofGate + 1):
            if (_NMOSNumberofGate % 2) == 0:
                _xycoordinatetmp = [_XYCoordinateOfNMOS[0][0] - _NMOSNumberofGate / 2 * _LengthNMOSBtwMet1 + i * _LengthNMOSBtwMet1,
                                    _XYCoordinateOfNMOS[0][1]]
            else:
                _xycoordinatetmp = [_XYCoordinateOfNMOS[0][0] - ((_NMOSNumberofGate + 1) / 2 - 0.5) * _LengthNMOSBtwMet1 + i * _LengthNMOSBtwMet1,
                                    _XYCoordinateOfNMOS[0][1]]

            tmpXY_M1.append(_xycoordinatetmp)

        self._DesignParameter['_Met1Layer'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0],
                                                                               _Datatype=DesignParameters._LayerMapping['METAL1'][1],
                                                                               _XYCoordinates=[], _XWidth=400, _YWidth=400)
        self._DesignParameter['_Met1Layer']['_XWidth'] = _DRCObj._CoMinWidth + 2 * _DRCObj._Metal1MinEnclosureCO
        self._DesignParameter['_Met1Layer']['_YWidth'] = self._DesignParameter['_ODLayer']['_YWidth']
        self._DesignParameter['_Met1Layer']['_XYCoordinates'] = tmpXY_M1

        if DesignParameters._Technology == 'SS28nm':
            self._DesignParameter['_METAL1PINDrawing'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['M1PIN'][0],
                                                                                          _Datatype=DesignParameters._LayerMapping['M1PIN'][1],
                                                                                          _XYCoordinates=[], _XWidth=400, _YWidth=400)
            self._DesignParameter['_METAL1PINDrawing']['_XWidth'] = self._DesignParameter['_Met1Layer']['_XWidth']
            self._DesignParameter['_METAL1PINDrawing']['_YWidth'] = self._DesignParameter['_Met1Layer']['_YWidth']
            self._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'] = self._DesignParameter['_Met1Layer']['_XYCoordinates']

        #
        print ('#############################     CONT Layer Calculation    ##############################################')
        # CONT XNum/YNum Calculation
        _XNumberOfCOInNMOS = _NMOSNumberofGate + 1
        _YNumberOfCOInNMOS = int(float(self._DesignParameter['_ODLayer']['_YWidth']
                                       - 2 * max([_DRCObj._CoMinEnclosureByODAtLeastTwoSide, _DRCObj._Metal1MinEnclosureCO2])
                                       + _DRCObj._CoMinSpace)
                                 / (_DRCObj._CoMinSpace + _DRCObj._CoMinWidth))

        # Check the number of CO On NMOS TR
        if _XNumberOfCOInNMOS == 0 or _YNumberOfCOInNMOS == 0:
            print ('************************* Error occured in {} Design Parameter Calculation******************************'.format(self._DesignParameter['_Name']['_Name']))
            if DesignParameters._DebugMode == 0:
                return 0

        # CONT XY coordinates Calculation
        tmpXYs = []
        for i in range(0, _XNumberOfCOInNMOS):
            for j in range(0, _YNumberOfCOInNMOS):

                if (_XNumberOfCOInNMOS % 2) == 1 and (_YNumberOfCOInNMOS % 2) == 0:
                    _xycoordinatetmp = [_XYCoordinateOfNMOS[0][0] - (_XNumberOfCOInNMOS - 1) / 2 * _LengthNMOSBtwMet1 + i * _LengthNMOSBtwMet1,
                                        _XYCoordinateOfNMOS[0][1] - (_YNumberOfCOInNMOS / 2 - 0.5) * _LengthNMOSBtwCO + j * _LengthNMOSBtwCO]

                elif (_XNumberOfCOInNMOS % 2) == 1 and (_YNumberOfCOInNMOS % 2) == 1:
                    _xycoordinatetmp = [_XYCoordinateOfNMOS[0][0] - (_XNumberOfCOInNMOS - 1) / 2 * _LengthNMOSBtwMet1 + i * _LengthNMOSBtwMet1,
                                        _XYCoordinateOfNMOS[0][1] - (_YNumberOfCOInNMOS - 1) / 2 * _LengthNMOSBtwCO + j * _LengthNMOSBtwCO]

                elif (_XNumberOfCOInNMOS % 2) == 0 and (_YNumberOfCOInNMOS % 2) == 0:
                    _xycoordinatetmp = [_XYCoordinateOfNMOS[0][0] - (_XNumberOfCOInNMOS / 2 - 0.5) * _LengthNMOSBtwMet1 + i * _LengthNMOSBtwMet1,
                                        _XYCoordinateOfNMOS[0][1] - (_YNumberOfCOInNMOS / 2 - 0.5) * _LengthNMOSBtwCO + j * _LengthNMOSBtwCO]

                else:
                    _xycoordinatetmp = [_XYCoordinateOfNMOS[0][0] - (_XNumberOfCOInNMOS / 2 - 0.5) * _LengthNMOSBtwMet1 + i * _LengthNMOSBtwMet1,
                                        _XYCoordinateOfNMOS[0][1] - (_YNumberOfCOInNMOS - 1) / 2 * _LengthNMOSBtwCO + j * _LengthNMOSBtwCO]
                tmpXYs.append(_xycoordinatetmp)

        self._DesignParameter['_COLayer'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['CONT'][0],
                                                                             _Datatype=DesignParameters._LayerMapping['CONT'][1],
                                                                             _XYCoordinates=[], _XWidth=400, _YWidth=400)
        self._DesignParameter['_COLayer']['_YWidth'] = _DRCObj._CoMinWidth
        self._DesignParameter['_COLayer']['_XWidth'] = _DRCObj._CoMinWidth
        self._DesignParameter['_COLayer']['_XYCoordinates'] = tmpXYs


        if DesignParameters._Technology != 'SS28nm':  # There is no NIMP(NP) Layer at 28nm
            print ('#############################     NIMP (NP/-) Layer Calculation    ####################')
            if _NMOSDummy:
                XWidth_NP_byPO = self._DesignParameter['_PODummyLayer']['_XWidth'] \
                                 + (self._DesignParameter['_PODummyLayer']['_XYCoordinates'][1][0] - self._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][0]) \
                                 + 2 * _DRCObj._NpMinEnclosureOfPo
            else:
                XWidth_NP_byPO = 0

            XWidth_NP_byOD = self._DesignParameter['_ODLayer']['_XWidth'] + 2 * _DRCObj._NpMinExtensiononNactive

            self._DesignParameter['_NPLayer'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['NIMP'][0],
                                                                                 _Datatype=DesignParameters._LayerMapping['NIMP'][1],
                                                                                 _XYCoordinates=[], _XWidth=400, _YWidth=400)
            self._DesignParameter['_NPLayer']['_XWidth'] = max(XWidth_NP_byPO, XWidth_NP_byOD)
            self._DesignParameter['_NPLayer']['_YWidth'] = self._DesignParameter['_POLayer']['_YWidth'] + 2 * _DRCObj._NpMinEnclosureOfPo
            self._DesignParameter['_NPLayer']['_XYCoordinates'] = _XYCoordinateOfNMOS

        # XVT Layer Calculation
        try:
            if (DesignParameters._Technology == 'SS28nm') and _XVT in ('SLVT', 'LVT', 'RVT', 'HVT'):
                _XVTLayer = '_' + _XVT + 'Layer'
            elif (DesignParameters._Technology == 'TSMC65nm') and _XVT in ('LVT', 'HVT'):
                _XVTLayer = '_N' + _XVT + 'Layer'
            elif (DesignParameters._Technology == 'TSMC65nm') and (_XVT == None):
                _XVTLayer = None

            elif DesignParameters._Technology == 'SS28nm':
                _XVT = _XVT if _XVT else "None"
                raise NotImplementedError("Invalid '_XVT' argument({}) for SS28nm".format(_XVT))
            elif DesignParameters._Technology == 'TSMC65nm':
                raise NotImplementedError("Invalid '_XVT' argument({}) for TSMC65nm".format(_XVT))
            else:
                raise NotImplementedError("Not Yet Implemented in other technology : {}".format(DesignParameters._Technology))

            if _XVTLayer != None:
                print ('#############################     {0} Layer Calculation    ##############################################'.format(_XVTLayer))
                self._DesignParameter[_XVTLayer]['_XWidth'] = self._DesignParameter['_ODLayer']['_XWidth'] + 2 * _DRCObj._XvtMinEnclosureOfODX
                self._DesignParameter[_XVTLayer]['_YWidth'] = self._DesignParameter['_ODLayer']['_YWidth'] + 2 * _DRCObj._XvtMinEnclosureOfODY
                self._DesignParameter[_XVTLayer]['_XYCoordinates'] = self._DesignParameter['_ODLayer']['_XYCoordinates']

        except Exception as e:
            print('Error Occurred', e)
            # raise NotImplementedError

        # ?
        if DesignParameters._Technology == 'SS28nm':  # ?
            self._DesignParameter['_PCCRITLayer'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['PCCRIT'][0],
                                                                                     _Datatype=DesignParameters._LayerMapping['PCCRIT'][1],
                                                                                     _XYCoordinates=[], _XWidth=400, _YWidth=400)
            if self._DesignParameter['_POLayer']['_XWidth'] in (30, 34):
                self._DesignParameter['_PCCRITLayer']['_XWidth'] = _LengthNMOSBtwMet1 * _NMOSNumberofGate + _DRCObj._CoMinWidth + 2 * _DRCObj._CoMinEnclosureByOD + 2 * _DRCObj._PCCRITExtension
                self._DesignParameter['_PCCRITLayer']['_YWidth'] = self._DesignParameter['_ODLayer']['_YWidth'] + 2 * _DRCObj._PCCRITExtension
                self._DesignParameter['_PCCRITLayer']['_XYCoordinates'] = _XYCoordinateOfNMOS
            else:
                self._DesignParameter['_PCCRITLayer']['_XWidth'] = None
                self._DesignParameter['_PCCRITLayer']['_YWidth'] = None
                self._DesignParameter['_PCCRITLayer']['_XYCoordinates'] = []


        if DesignParameters._Technology == 'TSMC180nm':
            print ('#############################     WELLBODY Layer Calculation    #########################################')
            self._DesignParameter['_WELLBodyLayer'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['WELLBODY'][0],
                                                                                       _Datatype=DesignParameters._LayerMapping['WELLBODY'][1],
                                                                                       _XYCoordinates=[], _XWidth=400, _YWidth=400)
            self._DesignParameter['_WELLBodyLayer']['_XYCoordinates'] = _XYCoordinateOfNMOS
            self._DesignParameter['_WELLBodyLayer']['_XWidth'] = self._DesignParameter['_ODLayer']['_XWidth']
            self._DesignParameter['_WELLBodyLayer']['_YWidth'] = self._DesignParameter['_ODLayer']['_YWidth']


        if DesignParameters._Technology == 'TSMC65nm':
            print ('################################     PDK Layer Calculation    ############################################')
            self._DesignParameter['_PDKLayer'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['PDK'][0],
                                                                                  _Datatype=DesignParameters._LayerMapping['PDK'][1],
                                                                                  _XYCoordinates=[], _XWidth=400, _YWidth=400)
            self._DesignParameter['_PDKLayer']['_XYCoordinates'] = _XYCoordinateOfNMOS
            self._DesignParameter['_PDKLayer']['_XWidth'] = self._DesignParameter['_NPLayer']['_XWidth']
            self._DesignParameter['_PDKLayer']['_YWidth'] = self._DesignParameter['_NPLayer']['_YWidth']


        print ('#########################     Supply Routing Coordinates Calculation   ##################################')
        tmpXYs = []
        if (_NMOSNumberofGate % 2) == 0:
            for i in range(0, _NMOSNumberofGate // 2 + 1):
                tmpXYs.append([_XYCoordinateOfNMOS[0][0] - _NMOSNumberofGate / 2 * _LengthNMOSBtwMet1 + i * 2 * _LengthNMOSBtwMet1,
                               _XYCoordinateOfNMOS[0][1]])
        else:
            for i in range(0, (_NMOSNumberofGate - 1) // 2 + 1):
                tmpXYs.append([_XYCoordinateOfNMOS[0][0] - ((_NMOSNumberofGate + 1) / 2 - 0.5) * _LengthNMOSBtwMet1 + i * 2 * _LengthNMOSBtwMet1,
                               _XYCoordinateOfNMOS[0][1]])

        self._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'] = tmpXYs


        print ('#########################     Output Routing Coordinates Calculation    ##################################')
        tmpXYs = []
        if (_NMOSNumberofGate % 2) == 0:
            for i in range(0, _NMOSNumberofGate // 2):
                tmpXYs.append([_XYCoordinateOfNMOS[0][0] - _NMOSNumberofGate / 2 * _LengthNMOSBtwMet1 + (i * 2 + 1) * _LengthNMOSBtwMet1,
                               _XYCoordinateOfNMOS[0][1]])
        else:
            for i in range(0, (_NMOSNumberofGate - 1) // 2 + 1):
                tmpXYs.append([_XYCoordinateOfNMOS[0][0] - ((_NMOSNumberofGate + 1) / 2 - 0.5) * _LengthNMOSBtwMet1 + (i * 2 + 1) * _LengthNMOSBtwMet1,
                               _XYCoordinateOfNMOS[0][1]])

        self._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'] = tmpXYs


        print ('#########################     Gate Routing Coordinates Calculation   ##################################')
        tmpXYs = []
        for i in range(0, _NMOSNumberofGate):
            if (_NMOSNumberofGate % 2) == 0:
                tmpXYs.append([_XYCoordinateOfNMOS[0][0] - (_NMOSNumberofGate / 2 - 0.5) * _LengthNMOSBtwMet1 + i * _LengthNMOSBtwMet1,
                               _XYCoordinateOfNMOS[0][1]])
            else:
                tmpXYs.append([_XYCoordinateOfNMOS[0][0] - (_NMOSNumberofGate - 1) / 2 * _LengthNMOSBtwMet1 + i * _LengthNMOSBtwMet1,
                               _XYCoordinateOfNMOS[0][1]])

        self._DesignParameter['_XYCoordinateNMOSGateRouting']['_XYCoordinates'] = tmpXYs


        print ('##################################################### Diff Pin Generation & Coordinates ####################################################')

        self._DesignParameter['_ODLayerPINDrawing']['_XWidth'] = self._DesignParameter['_ODLayer']['_XWidth'] / 2 - (self._DesignParameter['_XYCoordinateNMOSGateRouting']['_XYCoordinates'][-1][0] + self._DesignParameter['_POLayer']['_XWidth'] / 2)
        self._DesignParameter['_ODLayerPINDrawing']['_YWidth'] = self._DesignParameter['_ODLayer']['_YWidth']
        self._DesignParameter['_ODLayerPINDrawing']['_XYCoordinates'] = [[(self._DesignParameter['_ODLayer']['_XWidth'] / 2 + (self._DesignParameter['_XYCoordinateNMOSGateRouting']['_XYCoordinates'][-1][0] + self._DesignParameter['_POLayer']['_XWidth'] / 2)) / 2, _XYCoordinateOfNMOS[0][1]],
                                                                         [0 - (self._DesignParameter['_ODLayer']['_XWidth'] / 2 + (self._DesignParameter['_XYCoordinateNMOSGateRouting']['_XYCoordinates'][-1][0] + self._DesignParameter['_POLayer']['_XWidth'] / 2)) / 2, _XYCoordinateOfNMOS[0][1]]]


        print ('##################################################### POLayer Pin Generation & Coordinates ####################################################')
        self._DesignParameter['_POLayerPINDrawing'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['PCPIN'][0],
                                                                                       _Datatype=DesignParameters._LayerMapping['PCPIN'][1],
                                                                                       _XYCoordinates=[], _XWidth=400, _YWidth=400)
        self._DesignParameter['_POLayerPINDrawing']['_XWidth'] = self._DesignParameter['_POLayer']['_XWidth']
        self._DesignParameter['_POLayerPINDrawing']['_YWidth'] = (self._DesignParameter['_POLayer']['_YWidth'] - self._DesignParameter['_ODLayer']['_YWidth']) / 2
        tmp1 = []
        tmp2 = []
        for i in range(0, len(self._DesignParameter['_XYCoordinateNMOSGateRouting']['_XYCoordinates'])):
            tmp1.append([self._DesignParameter['_XYCoordinateNMOSGateRouting']['_XYCoordinates'][i][0], - (self._DesignParameter['_ODLayer']['_YWidth'] / 2 + self._DesignParameter['_POLayerPINDrawing']['_YWidth'] / 2)])
            tmp2.append([self._DesignParameter['_XYCoordinateNMOSGateRouting']['_XYCoordinates'][i][0], (self._DesignParameter['_ODLayer']['_YWidth'] / 2 + self._DesignParameter['_POLayerPINDrawing']['_YWidth'] / 2)])

        if _NMOSNumberofGate == 1:
            self._DesignParameter['_POLayerPINDrawing']['_XYCoordinates'] = tmp1 + tmp2
        else:
            self._DesignParameter['_POLayerPINDrawing']['_XYCoordinates'] = tmp1


        del _DRCObj
        print ('#########################################################################################################')
        print ('                                    {}  NMOS Calculation End                                   '.format(self._DesignParameter['_Name']['_Name']))
        print ('#########################################################################################################')