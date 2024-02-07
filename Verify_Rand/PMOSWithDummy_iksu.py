from SthPack import CoordCalc
import StickDiagram
import DesignParameters
import DRC

#
#from Private import MyInfo
# import DRCchecker


class _PMOS(StickDiagram._StickDiagram):
    _ParametersForDesignCalculation = dict(_PMOSNumberofGate=None, _PMOSChannelWidth=None, _PMOSChannellength=None,
                                           _PMOSDummy=False, _XVT=None, _DistanceBtwFinger=None)

    def __init__(self, _DesignParameter=None, _Name=None):

        if _DesignParameter != None:
            self._DesignParameter = _DesignParameter
        else:
            self._DesignParameter = dict(
                _ODLayer=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['DIFF'][0],
                                                          _Datatype=DesignParameters._LayerMapping['DIFF'][1],
                                                          _XYCoordinates=[],_XWidth=400, _YWidth=400),  # boundary type:1, #path type:2, #sref type: 3, #gds data type: 4, #Design Name data type: 5,  #other data type: ?
                _ODLayerPINDrawing=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['RXPIN'][0],
                                                                    _Datatype=DesignParameters._LayerMapping['RXPIN'][1],
                                                                    _XYCoordinates=[], _XWidth=400, _YWidth=400),
                _POLayer=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0],
                                                          _Datatype=DesignParameters._LayerMapping['POLY'][1],
                                                          _XYCoordinates=[],_XWidth=400, _YWidth=400),
                _POLayerPINDrawing=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['PCPIN'][0],
                                                                    _Datatype=DesignParameters._LayerMapping['PCPIN'][1],
                                                                    _XYCoordinates=[], _XWidth=400, _YWidth=400),
                _Met1Layer=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0],
                                                            _Datatype=DesignParameters._LayerMapping['METAL1'][1],
                                                            _XYCoordinates=[],_XWidth=400, _YWidth=400),
                _METAL1PINDrawing=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['M1PIN'][0],
                                                                   _Datatype=DesignParameters._LayerMapping['M1PIN'][1],
                                                                   _XYCoordinates=[], _XWidth=400, _YWidth=400),
                _PPLayer=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['PIMP'][0],
                                                          _Datatype=DesignParameters._LayerMapping['PIMP'][1],
                                                          _XYCoordinates=[],_XWidth=400, _YWidth=400),
                _COLayer=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['CONT'][0],
                                                          _Datatype=DesignParameters._LayerMapping['CONT'][1],
                                                          _XYCoordinates=[],_XWidth=400, _YWidth=400),
                _Name=self._NameDeclaration(_Name=_Name), _GDSFile=self._GDSObjDeclaration(_GDSFile=None),
                _XYCoordinatePMOSSupplyRouting=dict(_DesignParametertype=7,_XYCoordinates=[]),
                _XYCoordinatePMOSOutputRouting=dict(_DesignParametertype=7,_XYCoordinates=[]),
                _XYCoordinatePMOSGateRouting=dict(_DesignParametertype=7,_XYCoordinates=[]),
                DistanceXBtwPoly=self._SizeInfoDeclaration(_DesignSizesInList=None)
            )

        if _Name != None:
            self._DesignParameter['_Name']['_Name'] = _Name

    def _CalculatePMOSDesignParameter(self, _PMOSNumberofGate=None, _PMOSChannelWidth=None, _PMOSChannellength=None,
                                      _PMOSDummy=False, _XVT=None, _DistanceBtwFinger=None):

        _DRCObj = DRC.DRC()
        MinSnapSpacing = _DRCObj._MinSnapSpacing
        _Name = self._DesignParameter['_Name']['_Name']

        print(''.center(105,'#'))
        print(f'     {_Name} PMOS Calculation Start     '.center(105,'#'))
        print(''.center(105,'#'))

        flag_EvenChannelWidth = True if (_PMOSChannelWidth % 2 == 0) else False
        _XYCoordinateOfPMOS = [[0, 0]] if flag_EvenChannelWidth else [[0, MinSnapSpacing/2.0]]

        _LengthPMOSBtwCO = _DRCObj._CoMinSpace + _DRCObj._CoMinWidth

        if DesignParameters._Technology == '028nm':
            _LengthPMOSBtwPO = _DRCObj.DRCPolyMinSpace(_Width=_PMOSChannelWidth, _ParallelLength=_PMOSChannellength) + _PMOSChannellength
        else:
            _LengthPMOSBtwPO = _DRCObj.DRCPolygateMinSpace(_DRCObj._CoMinWidth + 2 * _DRCObj._PolygateMinSpace2Co) + _PMOSChannellength

        if _DistanceBtwFinger == None:
            pass
        elif _LengthPMOSBtwPO > _DistanceBtwFinger:
            raise Exception(f"Invalid Parameter '_DistanceBtwFinger(={_DistanceBtwFinger})' in {_Name}.\n"
                            f"Available Condition: 1) '_DistanceBtwFinger >= {_LengthPMOSBtwPO}'\n"
                            f"                     2) '_DistanceBtwFinger = None' for Minimum Value.")
        else:
            _LengthPMOSBtwPO = _DistanceBtwFinger


        print('     POLY (PO/PC) Layer Calculation     '.center(105,'#'))
        tmpXYs = []
        for i in range(0, _PMOSNumberofGate):
            tmpXYs.append([_XYCoordinateOfPMOS[0][0] - (_PMOSNumberofGate - 1) / 2.0 * _LengthPMOSBtwPO + i * _LengthPMOSBtwPO,
                           _XYCoordinateOfPMOS[0][1]])

        self._DesignParameter['_POLayer']['_XWidth'] = _PMOSChannellength
        self._DesignParameter['_POLayer']['_YWidth'] = _PMOSChannelWidth + 2 * _DRCObj.DRCPolygateMinExtensionOnOD(_PMOSChannellength)
        self._DesignParameter['_POLayer']['_XYCoordinates'] = tmpXYs


        if _PMOSDummy:
            print('     POLY Dummy Layer Calculation     '.center(105,'#'))
            self._DesignParameter['_PODummyLayer'] = self._BoundaryElementDeclaration(
                _Layer=DesignParameters._LayerMapping['POLY'][0],
                _Datatype=DesignParameters._LayerMapping['POLY'][1],
                _XWidth=_PMOSChannellength,
                _YWidth=_PMOSChannelWidth + 2 * _DRCObj._PolygateMinExtensionOnOD,
                _XYCoordinates=[
                    CoordCalc.Add(self._DesignParameter['_POLayer']['_XYCoordinates'][0], [-_LengthPMOSBtwPO, 0]),
                    CoordCalc.Add(self._DesignParameter['_POLayer']['_XYCoordinates'][-1], [_LengthPMOSBtwPO, 0])
                ])

            if float(self._DesignParameter['_PODummyLayer']['_XWidth']) * float(self._DesignParameter['_PODummyLayer']['_YWidth']) < _DRCObj._PODummyMinArea:  # Should check this DRC at TSMC
                self._DesignParameter['_PODummyLayer']['_YWidth'] = self.CeilMinSnapSpacing(float(_DRCObj._PODummyMinArea) / float(self._DesignParameter['_PODummyLayer']['_XWidth']), _DRCObj._MinSnapSpacing*2)
                # if DesignParameters._Technology != '028nm':
                #     self._DesignParameter['_POLayer']['_YWidth'] = self._DesignParameter['_PODummyLayer']['_YWidth']
            else:
                pass
        else:
            self._DesignParameter['_PODummyLayer'] = self._BoundaryElementDeclaration(
                _Layer=DesignParameters._LayerMapping['POLY'][0],
                _Datatype=DesignParameters._LayerMapping['POLY'][1],
                _XWidth=0,
                _YWidth=0,
                _XYCoordinates=[
                    CoordCalc.Add(self._DesignParameter['_POLayer']['_XYCoordinates'][0], [-_LengthPMOSBtwPO, 0]),
                    CoordCalc.Add(self._DesignParameter['_POLayer']['_XYCoordinates'][-1], [_LengthPMOSBtwPO, 0])
                ])


        print('     DIFF (OD/RX) Layer Calculation     '.center(105,'#'))
        # if _PMOSDummy and DesignParameters._Technology != '028nm':
        #     XWidth_OD = self._DesignParameter['_PODummyLayer']['_XYCoordinates'][-1][0] - self._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][0] + _PMOSChannellength + 2 * _DRCObj._PolygateMinExtensionOnODX
        # else:
        XWidth_OD = _LengthPMOSBtwPO * _PMOSNumberofGate + _DRCObj._CoMinWidth + 2 * _DRCObj._CoMinEnclosureByOD
        self._DesignParameter['_ODLayer']['_XWidth'] = XWidth_OD
        self._DesignParameter['_ODLayer']['_YWidth'] = _PMOSChannelWidth
        self._DesignParameter['_ODLayer']['_XYCoordinates'] = _XYCoordinateOfPMOS


        print('     METAL1 Layer Calculation     '.center(105,'#'))
        # METAL1 Layer Coordinate Setting
        _LengthPMOSBtwMet1 = _LengthPMOSBtwPO
        self._DesignParameter['DistanceXBtwPoly']['_DesignSizesInList'] = _LengthPMOSBtwMet1

        tmpXYs = []
        for i in range(0, _PMOSNumberofGate + 1):  # the number of the metal = the number of the gate + 1
            tmpXYs.append([_XYCoordinateOfPMOS[0][0] - _PMOSNumberofGate / 2.0 * _LengthPMOSBtwMet1 + i * _LengthPMOSBtwMet1,
                           _XYCoordinateOfPMOS[0][1]])

        self._DesignParameter['_Met1Layer']['_XWidth'] = _DRCObj._CoMinWidth + 2 * _DRCObj._Metal1MinEnclosureCO
        self._DesignParameter['_Met1Layer']['_YWidth'] = self._DesignParameter['_ODLayer']['_YWidth']
        self._DesignParameter['_Met1Layer']['_XYCoordinates'] = tmpXYs

        if DesignParameters._Technology == '028nm':
            self._DesignParameter['_METAL1PINDrawing']['_XWidth'] = self._DesignParameter['_Met1Layer']['_XWidth']
            self._DesignParameter['_METAL1PINDrawing']['_YWidth'] = self._DesignParameter['_Met1Layer']['_YWidth']
            self._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'] = self._DesignParameter['_Met1Layer']['_XYCoordinates']


        print('     CONT (Source/Drain) Layer Calculation     '.center(105,'#'))
        # CONT XNum/YNum Calculation
        _XNumberOfCOInPMOS = _PMOSNumberofGate + 1
        _YNumberOfCOInPMOS = int(float(self._DesignParameter['_ODLayer']['_YWidth']
                                       - 2 * max([_DRCObj._CoMinEnclosureByODAtLeastTwoSide, _DRCObj._Metal1MinEnclosureCO2])
                                       + _DRCObj._CoMinSpace)
                                 / (_DRCObj._CoMinSpace + _DRCObj._CoMinWidth))

        # Check the number of CO On PMOS TR
        if (_XNumberOfCOInPMOS == 0) or (_YNumberOfCOInPMOS == 0):
            print('************************* Error occurred in {} Design Parameter Calculation******************************'.format(self._DesignParameter['_Name']['_Name']))
            if DesignParameters._DebugMode == 0:
                return 0

        # CONT XY coordinates Calculation
        tmpXYs = []
        for i in range(0, _XNumberOfCOInPMOS):
            for j in range(0, _YNumberOfCOInPMOS):
                tmpXYs.append([_XYCoordinateOfPMOS[0][0] - (_XNumberOfCOInPMOS - 1) / 2.0 * _LengthPMOSBtwMet1 + i * _LengthPMOSBtwMet1,
                               _XYCoordinateOfPMOS[0][1] - (_YNumberOfCOInPMOS - 1) / 2.0 * _LengthPMOSBtwCO + j * _LengthPMOSBtwCO])

        self._DesignParameter['_COLayer']['_YWidth'] = _DRCObj._CoMinWidth
        self._DesignParameter['_COLayer']['_XWidth'] = _DRCObj._CoMinWidth
        self._DesignParameter['_COLayer']['_XYCoordinates'] = tmpXYs

        if flag_EvenChannelWidth:
            pass
        else:                # when finger width is odd number
            tmpXYs = []
            for XY in self._DesignParameter['_COLayer']['_XYCoordinates']:
                tmpXYs.append(CoordCalc.Add(XY, [0, MinSnapSpacing / 2.0]))
            self._DesignParameter['_COLayer']['_XYCoordinates'] = tmpXYs

        #
        if DesignParameters._Technology == '028nm':
            _CoArrXWidth = (_XNumberOfCOInPMOS - 1) * _LengthPMOSBtwMet1 + self._DesignParameter['_COLayer']['_XWidth']
            _CoArrYWidth = (_YNumberOfCOInPMOS - 1) * _LengthPMOSBtwCO + self._DesignParameter['_COLayer']['_YWidth']
            if min(_CoArrXWidth, _CoArrYWidth) > _DRCObj._CoArrayMaxWidth:
                print('CA Array Maximum Width should be smaller than 1211n.')
                raise NotImplementedError
        else:
            pass


        print('     PIMP (PP/BP) Layer Calculation     '.center(105,'#'))  # Need to check
        if (DesignParameters._Technology != '028nm') and (_PMOSDummy is True) :
            XWidth_PP_byPO = self._DesignParameter['_PODummyLayer']['_XWidth'] \
                             + (self._DesignParameter['_PODummyLayer']['_XYCoordinates'][1][0] -
                                self._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][0]) \
                             + 2 * _DRCObj._PpMinEnclosureOfPo
        else:
            XWidth_PP_byPO = 0

        XWidth_PP_byOD = self._DesignParameter['_ODLayer']['_XWidth'] + 2 * _DRCObj._PpMinExtensiononPactive

        self._DesignParameter['_PPLayer']['_XWidth'] = max(XWidth_PP_byPO, XWidth_PP_byOD)
        self._DesignParameter['_PPLayer']['_YWidth'] = max(self._DesignParameter['_POLayer']['_YWidth'], self._DesignParameter['_PODummyLayer']['_YWidth']) + 2 * _DRCObj._PpMinEnclosureOfPo
        self._DesignParameter['_PPLayer']['_XYCoordinates'] = _XYCoordinateOfPMOS

        # XVT Layer Calculation
        try:
            if (DesignParameters._Technology == '028nm') and _XVT in ('SLVT', 'LVT', 'RVT', 'HVT'):
                self._XVTLayer = '_' + _XVT + 'Layer'
                self._XVTLayerMappingName = _XVT
            elif (DesignParameters._Technology == '065nm') and _XVT in ('LVT', 'HVT'):
                self._XVTLayer = '_P' + _XVT + 'Layer'
                self._XVTLayerMappingName = 'P' + _XVT
            elif (DesignParameters._Technology == '065nm') and (_XVT == None):
                self._XVTLayer = None
            elif (DesignParameters._Technology == '045nm') and _XVT in ('LVT', 'HVT'):
                self._XVTLayer = '_P' + _XVT + 'Layer'
                self._XVTLayerMappingName = 'P' + _XVT
            elif (DesignParameters._Technology == '045nm') and (_XVT == None):
                self._XVTLayer = None
            elif (DesignParameters._Technology == '090nm') and _XVT in ('LVT', 'HVT'):
                self._XVTLayer = '_P' + _XVT + 'Layer'
                self._XVTLayerMappingName = 'P' + _XVT
            elif (DesignParameters._Technology == '090nm') and (_XVT == None):
                self._XVTLayer = None


            elif DesignParameters._Technology == '028nm':
                _XVT = _XVT if _XVT else "None"  # just for Error Message
                raise NotImplementedError("Invalid '_XVT' argument({}) for 028nm".format(_XVT))
            elif DesignParameters._Technology == '065nm':
                raise NotImplementedError("Invalid '_XVT' argument({}) for 065nm".format(_XVT))
            elif DesignParameters._Technology == '045nm':
                raise NotImplementedError("Invalid '_XVT' argument({}) for 045nm".format(_XVT))
            elif DesignParameters._Technology == '090nm':
                raise NotImplementedError("Invalid '_XVT' argument({}) for 090nm".format(_XVT))

            else:
                raise NotImplementedError("Not Implemented in other technology : {}".format(DesignParameters._Technology))

            if self._XVTLayer != None:
                print('#############################     {0} Layer Calculation    ##############################################'.format(self._XVTLayer))
                self._DesignParameter[self._XVTLayer] = self._BoundaryElementDeclaration(
                    _Layer=DesignParameters._LayerMapping[self._XVTLayerMappingName][0],
                    _Datatype=DesignParameters._LayerMapping[self._XVTLayerMappingName][1],
                    _XWidth=max(self._DesignParameter['_ODLayer']['_XWidth'] + 2 * _DRCObj._XvtMinEnclosureOfODX,
                                _LengthPMOSBtwPO * (_PMOSNumberofGate + 1)),
                    _YWidth=self._DesignParameter['_ODLayer']['_YWidth'] + 2 * _DRCObj._XvtMinEnclosureOfODY,
                    _XYCoordinates=self._DesignParameter['_ODLayer']['_XYCoordinates']
                )

        except Exception as e:
            print('Error Occurred', e)
            raise NotImplementedError


        if DesignParameters._Technology == '028nm':
            print('     PCCRIT Layer Calculation     '.center(105,'#'))
            if self._DesignParameter['_POLayer']['_XWidth'] in (30, 34):
                self._DesignParameter['_PCCRITLayer'] = self._BoundaryElementDeclaration(
                    _Layer=DesignParameters._LayerMapping['PCCRIT'][0],
                    _Datatype=DesignParameters._LayerMapping['PCCRIT'][1],
                    _XWidth=_PMOSNumberofGate * _LengthPMOSBtwMet1 + _DRCObj._CoMinWidth + 2 * _DRCObj._CoMinEnclosureByOD + 2 * _DRCObj._PCCRITExtension,
                    _YWidth=self._DesignParameter['_ODLayer']['_YWidth'] + 2 * _DRCObj._PCCRITExtension,
                    _XYCoordinates=_XYCoordinateOfPMOS
                )
            else:
                pass
        else:
            pass

        print('     Supply Routing Coordinates Calculation     '.center(105,'#'))
        tmpXYs = []
        if (_PMOSNumberofGate % 2) == 0:
            for i in range(0, _PMOSNumberofGate // 2 + 1):
                tmpXYs.append([_XYCoordinateOfPMOS[0][0] - _PMOSNumberofGate / 2 * _LengthPMOSBtwMet1 + i * 2 * _LengthPMOSBtwMet1,
                               _XYCoordinateOfPMOS[0][1]])
        else:
            for i in range(0, (_PMOSNumberofGate + 1) // 2):
                tmpXYs.append([_XYCoordinateOfPMOS[0][0] - ((_PMOSNumberofGate + 1) / 2 - 0.5) * _LengthPMOSBtwMet1 + i * 2 * _LengthPMOSBtwMet1,
                               _XYCoordinateOfPMOS[0][1]])
        self._DesignParameter['_XYCoordinatePMOSSupplyRouting']['_XYCoordinates'] = tmpXYs


        print('     Output Routing Coordinates Calculation     '.center(105,'#'))
        tmpXYs = []
        if (_PMOSNumberofGate % 2) == 0:
            for i in range(0, _PMOSNumberofGate // 2):
                tmpXYs.append([_XYCoordinateOfPMOS[0][0] - _PMOSNumberofGate / 2 * _LengthPMOSBtwMet1 + (i * 2 + 1) * _LengthPMOSBtwMet1,
                               _XYCoordinateOfPMOS[0][1]])
        else:
            for i in range(0, (_PMOSNumberofGate + 1) // 2):
                tmpXYs.append([_XYCoordinateOfPMOS[0][0] - ((_PMOSNumberofGate + 1) / 2 - 0.5) * _LengthPMOSBtwMet1 + (i * 2 + 1) * _LengthPMOSBtwMet1,
                               _XYCoordinateOfPMOS[0][1]])
        self._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'] = tmpXYs


        print('     Gate Routing Coordinates Calculation     '.center(105,'#'))
        tmpXYs = []
        for i in range(0, _PMOSNumberofGate):
            tmpXYs.append([_XYCoordinateOfPMOS[0][0] - (_PMOSNumberofGate - 1) / 2.0 * _LengthPMOSBtwMet1 + i * _LengthPMOSBtwMet1,
                           _XYCoordinateOfPMOS[0][1]])
        self._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'] = tmpXYs


        if DesignParameters._Technology == '028nm':  # ?
            print('     Diff Pin Generation & Coordinates     '.center(105,'#'))
            self._DesignParameter['_ODLayerPINDrawing']['_XWidth'] = self._DesignParameter['_ODLayer']['_XWidth'] / 2 - (self._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'][-1][0] + self._DesignParameter['_POLayer']['_XWidth'] / 2)
            self._DesignParameter['_ODLayerPINDrawing']['_YWidth'] = self._DesignParameter['_ODLayer']['_YWidth']

            self._DesignParameter['_ODLayerPINDrawing']['_XYCoordinates'] = [
                [(self._DesignParameter['_ODLayer']['_XWidth'] / 2 + (self._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'][-1][0] + self._DesignParameter['_POLayer']['_XWidth'] / 2)) / 2,
                  _XYCoordinateOfPMOS[0][1]],
                [0 - (self._DesignParameter['_ODLayer']['_XWidth'] / 2 + (self._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'][-1][0] + self._DesignParameter['_POLayer']['_XWidth'] / 2)) / 2,
                 _XYCoordinateOfPMOS[0][1]]
            ]


            print('     POLayer Pin Generation & Coordinates     '.center(105,'#'))
            self._DesignParameter['_POLayerPINDrawing']['_XWidth'] = self._DesignParameter['_POLayer']['_XWidth']
            self._DesignParameter['_POLayerPINDrawing']['_YWidth'] = (self._DesignParameter['_POLayer']['_YWidth'] - self._DesignParameter['_ODLayer']['_YWidth']) / 2
            tmp1 = []
            tmp2 = []
            for i in range(0, len(self._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'])):
                tmp1.append([self._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'][i][0], - (self._DesignParameter['_ODLayer']['_YWidth'] / 2 + self._DesignParameter['_POLayerPINDrawing']['_YWidth'] / 2)])
                tmp2.append([self._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'][i][0], (self._DesignParameter['_ODLayer']['_YWidth'] / 2 + self._DesignParameter['_POLayerPINDrawing']['_YWidth'] / 2)])

            if _PMOSNumberofGate == 1:
                self._DesignParameter['_POLayerPINDrawing']['_XYCoordinates'] = tmp1 + tmp2
            else:
                self._DesignParameter['_POLayerPINDrawing']['_XYCoordinates'] = tmp1
        else:
            pass

        print(''.center(105,'#'))
        print(f'     {_Name} PMOS Calculation End     '.center(105,'#'))
        print(''.center(105,'#'))


if __name__ == '__main__':

    from Private import MyInfo
    libname = 'TEST_MOS'
    cellname = 'PMOSWithDummy_iksu'
    _fileName = cellname + '.gds'

    ''' Input Parameters for Layout Object '''
    InputParams = dict(
        _PMOSNumberofGate=10,
        _PMOSChannelWidth=1000,
        _PMOSChannellength=30,          # Minimum value : 30 (samsung) / 60 (65nm)
        _PMOSDummy=False,
        _XVT=None,                    # @ 028nm, 'SLVT' 'LVT' 'RVT' 'HVT' / @ 065nm, 'LVT' 'HVT' or None
    )

    ''' Generate Layout Object '''
    LayoutObj = _PMOS(_DesignParameter=None, _Name=cellname)
    LayoutObj._CalculatePMOSDesignParameter(**InputParams)
    LayoutObj._UpdateDesignParameter2GDSStructure(_DesignParameterInDictionary=LayoutObj._DesignParameter)
    testStreamFile = open('./{}'.format(_fileName), 'wb')
    tmp = LayoutObj._CreateGDSStream(LayoutObj._DesignParameter['_GDSFile']['_GDSFile'])
    tmp.write_binary_gds_stream(testStreamFile)
    testStreamFile.close()

    print('#############################      Sending to FTP Server...      #############################')
    My = MyInfo.USER(DesignParameters._Technology)
    Checker = DRCchecker.DRCchecker(
        username=My.ID,
        password=My.PW,
        WorkDir=My.Dir_Work,
        DRCrunDir=My.Dir_DRCrun,
        libname=libname,
        cellname=cellname,
        GDSDir=My.Dir_GDS
    )
    Checker.Upload2FTP()
    Checker.StreamIn(tech=DesignParameters._Technology)
    print('#############################      Finished      ################################')
    # end of 'main():' ---------------------------------------------------------------------------------------------
