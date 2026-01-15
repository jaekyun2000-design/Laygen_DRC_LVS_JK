from Proj_RCDAC_ADC2024_V6_IJK_v2.KJH91_Projects.Project_ADC.Layoutgen_code.E00_Slicer.SthPack import CoordCalc
from Proj_RCDAC_ADC2024_V6_IJK_v2.KJH91_Projects.Project_ADC.Layoutgen_code.E00_Slicer import StickDiagram
from Proj_RCDAC_ADC2024_V6_IJK_v2.KJH91_Projects.Project_ADC.Layoutgen_code.E00_Slicer import DesignParameters
from Proj_RCDAC_ADC2024_V6_IJK_v2.KJH91_Projects.Project_ADC.Layoutgen_code.E00_Slicer import DRC

#
#from Private import MyInfo
# import DRCchecker


class _NMOS(StickDiagram._StickDiagram):
    _ParametersForDesignCalculation = dict(_NMOSNumberofGate=None, _NMOSChannelWidth=None, _NMOSChannellength=None,
                                           _NMOSDummy=False, _XVT=None, _DistanceBtwFinger=None)

    def __init__(self, _DesignParameter=None, _Name=None):

        if _DesignParameter != None:
            self._DesignParameter = _DesignParameter
        else:
            self._DesignParameter = dict(
                _ODLayer=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['DIFF'][0],
                                                          _Datatype=DesignParameters._LayerMapping['DIFF'][1],
                                                          _XYCoordinates=[], _XWidth=400, _YWidth=400),
                _ODLayerPINDrawing=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['RXPIN'][0],
                                                                    _Datatype=DesignParameters._LayerMapping['RXPIN'][1],
                                                                    _XYCoordinates=[], _XWidth=400, _YWidth=400),
                _POLayer=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0],
                                                          _Datatype=DesignParameters._LayerMapping['POLY'][1],
                                                          _XYCoordinates=[], _XWidth=400, _YWidth=400),
                _POLayerPINDrawing=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['PCPIN'][0],
                                                                    _Datatype=DesignParameters._LayerMapping['PCPIN'][1],
                                                                    _XYCoordinates=[], _XWidth=400, _YWidth=400),
                _Met1Layer=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0],
                                                            _Datatype=DesignParameters._LayerMapping['METAL1'][1],
                                                            _XYCoordinates=[], _XWidth=400, _YWidth=400),
                _METAL1PINDrawing=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['M1PIN'][0],
                                                                   _Datatype=DesignParameters._LayerMapping['M1PIN'][1],
                                                                   _XYCoordinates=[], _XWidth=400, _YWidth=400),
                _COLayer=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['CONT'][0],
                                                          _Datatype=DesignParameters._LayerMapping['CONT'][1],
                                                          _XYCoordinates=[], _XWidth=400, _YWidth=400),
                _Name=self._NameDeclaration(_Name=_Name), _GDSFile=self._GDSObjDeclaration(_GDSFile=None),
                _XYCoordinateNMOSSupplyRouting=dict(_DesignParametertype=7, _XYCoordinates=[]),
                _XYCoordinateNMOSOutputRouting=dict(_DesignParametertype=7, _XYCoordinates=[]),
                _XYCoordinateNMOSGateRouting=dict(_DesignParametertype=7, _XYCoordinates=[]),
                DistanceXBtwPoly=self._SizeInfoDeclaration(_DesignSizesInList=None),
                _XYcoordAsCent=dict(_XYcoordAsCent=1),
            )

        if _Name != None:
            self._DesignParameter['_Name']['_Name'] = _Name

    def _CalculateNMOSDesignParameter(self, _NMOSNumberofGate=None, _NMOSChannelWidth=None, _NMOSChannellength=None,
                                      _NMOSDummy=False, _XVT=None, _DistanceBtwFinger=None):

        _DRCObj = DRC.DRC()
        MinSnapSpacing = _DRCObj._MinSnapSpacing
        print ('#########################################################################################################')
        print ('                                    {}  NMOS Calculation Start                                    '.format(self._DesignParameter['_Name']['_Name']))
        print ('#########################################################################################################')

        flag_EvenChannelWidth = True if (_NMOSChannelWidth % 2 == 0) else False
        _XYCoordinateOfNMOS = [[0, 0]] if flag_EvenChannelWidth else [[0, MinSnapSpacing/2.0]]

        _LengthNMOSBtwCO = _DRCObj._CoMinSpace + _DRCObj._CoMinWidth

        if DesignParameters._Technology == '028nm':
            _LengthNMOSBtwPO = _DRCObj.DRCPolyMinSpace(_Width=_NMOSChannelWidth, _ParallelLength=_NMOSChannellength) + _NMOSChannellength
        else:
            _LengthNMOSBtwPO = _DRCObj.DRCPolygateMinSpace(_DRCObj._CoMinWidth + 2 * _DRCObj._PolygateMinSpace2Co) + _NMOSChannellength

        if _DistanceBtwFinger == None:
            pass
        elif _LengthNMOSBtwPO > _DistanceBtwFinger:
            raise Exception(f"Invalid Parameter '_DistanceBtwFinger(={_DistanceBtwFinger})'.\n"
                            f"Available Condition: 1) '_DistanceBtwFinger >= {_LengthNMOSBtwPO}'\n"
                            f"                     2) '_DistanceBtwFinger = None' for Minimum Value.")
        else:
            _LengthNMOSBtwPO = _DistanceBtwFinger


        print ('#############################     POLY (PO/PC) Layer Calculation    ##############################################')
        tmpXYs = []
        for i in range(0, _NMOSNumberofGate):
            tmpXYs.append([_XYCoordinateOfNMOS[0][0] - (_NMOSNumberofGate - 1) / 2.0 * _LengthNMOSBtwPO + i * _LengthNMOSBtwPO,
                           _XYCoordinateOfNMOS[0][1]])

        self._DesignParameter['_POLayer']['_XWidth'] = _NMOSChannellength
        self._DesignParameter['_POLayer']['_YWidth'] = _NMOSChannelWidth + 2 * _DRCObj.DRCPolygateMinExtensionOnOD(_NMOSChannellength)
        self._DesignParameter['_POLayer']['_XYCoordinates'] = tmpXYs


        if _NMOSDummy:
            print ('#############################     POLY Dummy Layer Calculation    ##############################################')
            self._DesignParameter['_PODummyLayer'] = self._BoundaryElementDeclaration(
                _Layer=DesignParameters._LayerMapping['POLY'][0],
                _Datatype=DesignParameters._LayerMapping['POLY'][1],
                _XWidth=_NMOSChannellength,
                _YWidth=_NMOSChannelWidth + 2 * _DRCObj._PolygateMinExtensionOnOD,
                _XYCoordinates=[
                    CoordCalc.Add(self._DesignParameter['_POLayer']['_XYCoordinates'][0], [-_LengthNMOSBtwPO, 0]),
                    CoordCalc.Add(self._DesignParameter['_POLayer']['_XYCoordinates'][-1], [_LengthNMOSBtwPO, 0])
                ])

            if float(self._DesignParameter['_PODummyLayer']['_XWidth']) * float(self._DesignParameter['_PODummyLayer']['_YWidth']) < _DRCObj._PODummyMinArea:  # Should check this DRC at TSMC
                self._DesignParameter['_PODummyLayer']['_YWidth'] = self.CeilMinSnapSpacing(float(_DRCObj._PODummyMinArea) / float(self._DesignParameter['_PODummyLayer']['_XWidth']), _DRCObj._MinSnapSpacing*2)
                # if DesignParameters._Technology != '028nm':  ## Need?
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
                    CoordCalc.Add(self._DesignParameter['_POLayer']['_XYCoordinates'][0], [-_LengthNMOSBtwPO, 0]),
                    CoordCalc.Add(self._DesignParameter['_POLayer']['_XYCoordinates'][-1], [_LengthNMOSBtwPO, 0])
                ])


        print ('#############################     DIFF (OD/RX) Layer Calculation    ##############################################')
        # if _NMOSDummy and DesignParameters._Technology != '028nm':
        #     XWidth_OD = self._DesignParameter['_PODummyLayer']['_XYCoordinates'][-1][0] - self._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][0] + _NMOSChannellength + 2 * _DRCObj._PolygateMinExtensionOnODX
        # else:
        XWidth_OD = _LengthNMOSBtwPO * _NMOSNumberofGate + _DRCObj._CoMinWidth + 2 * _DRCObj._CoMinEnclosureByOD
        self._DesignParameter['_ODLayer']['_XWidth'] = XWidth_OD
        self._DesignParameter['_ODLayer']['_YWidth'] = _NMOSChannelWidth
        self._DesignParameter['_ODLayer']['_XYCoordinates'] = _XYCoordinateOfNMOS


        print ('#############################     METAL1 Layer Calculation    ##############################################')
        # METAL1 Layer Coordinate Setting
        _LengthNMOSBtwMet1 = _LengthNMOSBtwPO
        self._DesignParameter['DistanceXBtwPoly']['_DesignSizesInList'] = _LengthNMOSBtwMet1

        tmpXYs = []
        for i in range(0, _NMOSNumberofGate + 1):
            tmpXYs.append([_XYCoordinateOfNMOS[0][0] - _NMOSNumberofGate / 2.0 * _LengthNMOSBtwMet1 + i * _LengthNMOSBtwMet1,
                           _XYCoordinateOfNMOS[0][1]])

        self._DesignParameter['_Met1Layer']['_XWidth'] = _DRCObj._CoMinWidth + 2 * _DRCObj._Metal1MinEnclosureCO
        self._DesignParameter['_Met1Layer']['_YWidth'] = self._DesignParameter['_ODLayer']['_YWidth']
        self._DesignParameter['_Met1Layer']['_XYCoordinates'] = tmpXYs

        if DesignParameters._Technology == '028nm':
            self._DesignParameter['_METAL1PINDrawing']['_XWidth'] = self._DesignParameter['_Met1Layer']['_XWidth']
            self._DesignParameter['_METAL1PINDrawing']['_YWidth'] = self._DesignParameter['_Met1Layer']['_YWidth']
            self._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'] = self._DesignParameter['_Met1Layer']['_XYCoordinates']


        print ('#############################     CONT Layer Calculation    ##############################################')
        # CONT XNum/YNum Calculation
        _XNumberOfCOInNMOS = _NMOSNumberofGate + 1
        _YNumberOfCOInNMOS = int(float(self._DesignParameter['_ODLayer']['_YWidth']
                                       - 2 * max([_DRCObj._CoMinEnclosureByODAtLeastTwoSide, _DRCObj._Metal1MinEnclosureCO2])
                                       + _DRCObj._CoMinSpace)
                                 / (_DRCObj._CoMinSpace + _DRCObj._CoMinWidth))

        # Check the number of CO On NMOS TR
        if _XNumberOfCOInNMOS == 0 or _YNumberOfCOInNMOS == 0:
            print ('************************* Error occurred in {} Design Parameter Calculation******************************'.format(self._DesignParameter['_Name']['_Name']))
            if DesignParameters._DebugMode == 0:
                return 0

        # CONT XY coordinates Calculation
        tmpXYs = []
        for i in range(0, _XNumberOfCOInNMOS):
            for j in range(0, _YNumberOfCOInNMOS):
                tmpXYs.append([_XYCoordinateOfNMOS[0][0] - (_XNumberOfCOInNMOS - 1) / 2.0 * _LengthNMOSBtwMet1 + i * _LengthNMOSBtwMet1,
                               _XYCoordinateOfNMOS[0][1] - (_YNumberOfCOInNMOS - 1) / 2.0 * _LengthNMOSBtwCO + j * _LengthNMOSBtwCO])

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
            _CoArrXWidth = (_XNumberOfCOInNMOS - 1) * _LengthNMOSBtwMet1 + self._DesignParameter['_COLayer']['_XWidth']
            _CoArrYWidth = (_YNumberOfCOInNMOS - 1) * _LengthNMOSBtwCO + self._DesignParameter['_COLayer']['_YWidth']
            if min(_CoArrXWidth, _CoArrYWidth) > _DRCObj._CoArrayMaxWidth:
                print('CA Array Maximum Width should be smaller than 1211n.')
                raise NotImplementedError
        else:
            pass

        self._DesignParameter['_NPLayer'] = self._BoundaryElementDeclaration(
                _Layer=DesignParameters._LayerMapping['NIMP'][0],
                _Datatype=DesignParameters._LayerMapping['NIMP'][1],
                _XWidth=0,
                _YWidth=0,
                _XYCoordinates=_XYCoordinateOfNMOS,)



        if DesignParameters._Technology != '028nm':  # There is no NIMP(NP) Layer at 28nm
            print ('#############################     NIMP (NP/-) Layer Calculation    ####################')
            if _NMOSDummy:
                XWidth_NP_byPO = self._DesignParameter['_PODummyLayer']['_XWidth'] \
                                 + (self._DesignParameter['_PODummyLayer']['_XYCoordinates'][1][0] - self._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][0]) \
                                 + 2 * _DRCObj._NpMinEnclosureOfPo
            else:
                XWidth_NP_byPO = 0
            XWidth_NP_byOD = self._DesignParameter['_ODLayer']['_XWidth'] + 2 * _DRCObj._NpMinExtensiononNactive

            self._DesignParameter['_NPLayer'] = self._BoundaryElementDeclaration(
                _Layer=DesignParameters._LayerMapping['NIMP'][0],
                _Datatype=DesignParameters._LayerMapping['NIMP'][1],
                _XWidth=max(XWidth_NP_byPO, XWidth_NP_byOD),
                _YWidth=max(self._DesignParameter['_POLayer']['_YWidth'], self._DesignParameter['_PODummyLayer']['_YWidth']) + 2 * _DRCObj._NpMinEnclosureOfPo,
                _XYCoordinates=_XYCoordinateOfNMOS,)


        ''' XVT Layer Calculation '''
        try:
            if (DesignParameters._Technology == '028nm') and _XVT in ('SLVT', 'LVT', 'RVT', 'HVT'):
                self._XVTLayer = '_' + _XVT + 'Layer'
                self._XVTLayerMappingName = _XVT
            elif (DesignParameters._Technology == '065nm') and _XVT in ('LVT', 'HVT'):
                self._XVTLayer = '_N' + _XVT + 'Layer'
                self._XVTLayerMappingName = 'N' + _XVT
            elif (DesignParameters._Technology == '065nm') and (_XVT == None):
                self._XVTLayer = None
                self._XVTLayerMappingName = None
            elif (DesignParameters._Technology == '045nm') and _XVT in ('LVT', 'HVT'):
                self._XVTLayer = '_N' + _XVT + 'Layer'
                self._XVTLayerMappingName = 'N' + _XVT
            elif (DesignParameters._Technology == '045nm') and (_XVT == None):
                self._XVTLayer = None
                self._XVTLayerMappingName = None
            elif (DesignParameters._Technology == '090nm') and _XVT in ('LVT', 'HVT'):
                self._XVTLayer = '_N' + _XVT + 'Layer'
                self._XVTLayerMappingName = 'N' + _XVT
            elif (DesignParameters._Technology == '090nm') and (_XVT == None):
                self._XVTLayer = None
                self._XVTLayerMappingName = None


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
                raise NotImplementedError("Not Yet Implemented in other technology : {}".format(DesignParameters._Technology))

            if self._XVTLayer != None:
                print ('#############################     {0} Layer Calculation    ##############################################'.format(self._XVTLayer))
                self._DesignParameter[self._XVTLayer] = self._BoundaryElementDeclaration(
                    _Layer=DesignParameters._LayerMapping[self._XVTLayerMappingName][0],
                    _Datatype=DesignParameters._LayerMapping[self._XVTLayerMappingName][1],
                    _XWidth=max(self._DesignParameter['_ODLayer']['_XWidth'] + 2 * _DRCObj._XvtMinEnclosureOfODX,
                                _LengthNMOSBtwPO * (_NMOSNumberofGate + 1)),
                    _YWidth=self._DesignParameter['_ODLayer']['_YWidth'] + 2 * _DRCObj._XvtMinEnclosureOfODY,
                    _XYCoordinates=self._DesignParameter['_ODLayer']['_XYCoordinates']
                )

        except Exception as e:
            print('Error Occurred', e)
            raise NotImplementedError

        if DesignParameters._Technology == '028nm':
            if self._DesignParameter['_POLayer']['_XWidth'] in (30, 34):
                self._DesignParameter['_PCCRITLayer'] = self._BoundaryElementDeclaration(
                    _Layer=DesignParameters._LayerMapping['PCCRIT'][0],
                    _Datatype=DesignParameters._LayerMapping['PCCRIT'][1],
                    _XWidth=_LengthNMOSBtwMet1 * _NMOSNumberofGate + _DRCObj._CoMinWidth + 2 * _DRCObj._CoMinEnclosureByOD + 2 * _DRCObj._PCCRITExtension,
                    _YWidth=self._DesignParameter['_ODLayer']['_YWidth'] + 2 * _DRCObj._PCCRITExtension,
                    _XYCoordinates=_XYCoordinateOfNMOS
                )
            else:
                pass
        else:
            pass

        if DesignParameters._Technology == '180nm':
            print ('#############################     WELLBODY Layer Calculation    #########################################')
            self._DesignParameter['_WELLBodyLayer'] = self._BoundaryElementDeclaration(
                _Layer=DesignParameters._LayerMapping['WELLBODY'][0],
                _Datatype=DesignParameters._LayerMapping['WELLBODY'][1],
                _XWidth=self._DesignParameter['_ODLayer']['_XWidth'],
                _YWidth=self._DesignParameter['_ODLayer']['_YWidth'],
                _XYCoordinates=_XYCoordinateOfNMOS
            )
        else:
            pass

        if DesignParameters._Technology == '065nm':
            print ('################################     PDK Layer Calculation    ############################################')
            self._DesignParameter['_PDKLayer'] = self._BoundaryElementDeclaration(
                _Layer=DesignParameters._LayerMapping['PDK'][0],
                _Datatype=DesignParameters._LayerMapping['PDK'][1],
                _XWidth=self._DesignParameter['_NPLayer']['_XWidth'],
                _YWidth=self._DesignParameter['_NPLayer']['_YWidth'],
                _XYCoordinates=_XYCoordinateOfNMOS
            )
        else:
            pass

        if DesignParameters._Technology == '045nm':
            print ('################################     PDK Layer Calculation    ############################################')
            self._DesignParameter['_PDKLayer'] = self._BoundaryElementDeclaration(
                _Layer=DesignParameters._LayerMapping['PDK'][0],
                _Datatype=DesignParameters._LayerMapping['PDK'][1],
                _XWidth=self._DesignParameter['_NPLayer']['_XWidth'],
                _YWidth=self._DesignParameter['_NPLayer']['_YWidth'],
                _XYCoordinates=_XYCoordinateOfNMOS
            )
        else:
            pass

        if DesignParameters._Technology == '090nm':
            print ('################################     PDK Layer Calculation    ############################################')
            self._DesignParameter['_PDKLayer'] = self._BoundaryElementDeclaration(
                _Layer=DesignParameters._LayerMapping['PDK'][0],
                _Datatype=DesignParameters._LayerMapping['PDK'][1],
                _XWidth=self._DesignParameter['_NPLayer']['_XWidth'],
                _YWidth=self._DesignParameter['_NPLayer']['_YWidth'],
                _XYCoordinates=_XYCoordinateOfNMOS
            )
        else:
            pass



        print ('#########################     Supply Routing Coordinates Calculation   ##################################')
        tmpXYs = []
        if (_NMOSNumberofGate % 2) == 0:
            for i in range(0, int(_NMOSNumberofGate / 2 + 1)):
                tmpXYs.append([_XYCoordinateOfNMOS[0][0] - _NMOSNumberofGate / 2 * _LengthNMOSBtwMet1 + i * 2 * _LengthNMOSBtwMet1,
                               _XYCoordinateOfNMOS[0][1]])
        else:
            for i in range(0, int((_NMOSNumberofGate + 1) / 2)):
                tmpXYs.append([_XYCoordinateOfNMOS[0][0] - _NMOSNumberofGate / 2 * _LengthNMOSBtwMet1 + i * 2 * _LengthNMOSBtwMet1,
                               _XYCoordinateOfNMOS[0][1]])
        self._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'] = tmpXYs


        print ('#########################     Output Routing Coordinates Calculation    ##################################')
        tmpXYs = []
        if (_NMOSNumberofGate % 2) == 0:
            for i in range(0, int(_NMOSNumberofGate / 2)):
                tmpXYs.append([_XYCoordinateOfNMOS[0][0] - _NMOSNumberofGate / 2 * _LengthNMOSBtwMet1 + (i * 2 + 1) * _LengthNMOSBtwMet1,
                               _XYCoordinateOfNMOS[0][1]])
        else:
            for i in range(0, int((_NMOSNumberofGate + 1) / 2)):
                tmpXYs.append([_XYCoordinateOfNMOS[0][0] - ((_NMOSNumberofGate + 1) / 2 - 0.5) * _LengthNMOSBtwMet1 + (i * 2 + 1) * _LengthNMOSBtwMet1,
                               _XYCoordinateOfNMOS[0][1]])
        self._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'] = tmpXYs


        print ('#########################     Gate Routing Coordinates Calculation   ##################################')
        tmpXYs = []
        for i in range(0, _NMOSNumberofGate):
            tmpXYs.append([_XYCoordinateOfNMOS[0][0] - (_NMOSNumberofGate - 1) / 2.0 * _LengthNMOSBtwMet1 + i * _LengthNMOSBtwMet1,
                           _XYCoordinateOfNMOS[0][1]])

        self._DesignParameter['_XYCoordinateNMOSGateRouting']['_XYCoordinates'] = tmpXYs

        if DesignParameters._Technology == '028nm':  # ?
            print ('##################################################### Diff Pin Generation & Coordinates ####################################################')
            self._DesignParameter['_ODLayerPINDrawing']['_XWidth'] = self._DesignParameter['_ODLayer']['_XWidth'] / 2 - (self._DesignParameter['_XYCoordinateNMOSGateRouting']['_XYCoordinates'][-1][0] + self._DesignParameter['_POLayer']['_XWidth'] / 2)
            self._DesignParameter['_ODLayerPINDrawing']['_YWidth'] = self._DesignParameter['_ODLayer']['_YWidth']
            self._DesignParameter['_ODLayerPINDrawing']['_XYCoordinates'] = [[(self._DesignParameter['_ODLayer']['_XWidth'] / 2 + (self._DesignParameter['_XYCoordinateNMOSGateRouting']['_XYCoordinates'][-1][0] + self._DesignParameter['_POLayer']['_XWidth'] / 2)) / 2, _XYCoordinateOfNMOS[0][1]],
                                                                             [0 - (self._DesignParameter['_ODLayer']['_XWidth'] / 2 + (self._DesignParameter['_XYCoordinateNMOSGateRouting']['_XYCoordinates'][-1][0] + self._DesignParameter['_POLayer']['_XWidth'] / 2)) / 2, _XYCoordinateOfNMOS[0][1]]]


            print ('##################################################### POLayer Pin Generation & Coordinates ####################################################')
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
        else:
            pass

        print ('#########################################################################################################')
        print ('                                    {}  NMOS Calculation End                                   '.format(self._DesignParameter['_Name']['_Name']))
        print ('#########################################################################################################')


if __name__ == '__main__':

    from Private import MyInfo
    import DRCchecker

    libname = 'TEST_MOS'
    cellname = 'NMOSWithDummy_iksu'
    _fileName = cellname + '.gds'

    ''' Input Parameters for Layout Object '''
    InputParams = dict(
        _NMOSNumberofGate=20,
        _NMOSChannelWidth=500,      # Minimum value : 200 (samsung) / 200 (65nm)
        _NMOSChannellength=30,      # Minimum value : 30 (samsung) / 60 (65nm)
        _NMOSDummy=True,
        _XVT='SLVT',                # @ 028nm, 'SLVT' 'LVT' 'RVT' 'HVT' / @ 065nm, 'LVT' 'HVT' or None
    )

    ''' Generate Layout Object '''
    LayoutObj = _NMOS(_DesignParameter=None, _Name=cellname)
    LayoutObj._CalculateNMOSDesignParameter(**InputParams)
    LayoutObj._UpdateDesignParameter2GDSStructure(_DesignParameterInDictionary=LayoutObj._DesignParameter)
    testStreamFile = open('./{}'.format(_fileName), 'wb')
    tmp = LayoutObj._CreateGDSStream(LayoutObj._DesignParameter['_GDSFile']['_GDSFile'])
    tmp.write_binary_gds_stream(testStreamFile)
    testStreamFile.close()

    # import ftplib
    # ftp = ftplib.FTP('141.223.22.156')
    # ftp.login('junung', 'chlwnsdnd1!')
    # #ftp.cwd('/mnt/sdc/junung/OPUS/Samsung28n')
    # #ftp.cwd('/mnt/sdc/junung/OPUS/TSMC65n')
    # ftp.cwd('/mnt/sdc/junung/OPUS/TSMC40n')
    # myfile = open('NMOSWithDummy_iksu.gds', 'rb')
    # ftp.storbinary('STOR NMOSWithDummy_iksu.gds', myfile)
    # myfile.close()
    # ftp.close()

    # print ('###############      Sending to FTP Server...      ##################')
    # My = MyInfo.USER(DesignParameters._Technology)
    # Checker = DRCchecker.DRCchecker(
    #     username=My.ID,
    #     password=My.PW,
    #     WorkDir=My.Dir_Work,
    #     DRCrunDir=My.Dir_DRCrun,
    #     libname=libname,
    #     cellname=cellname,
    #     GDSDir=My.Dir_GDS
    # )
    # Checker.Upload2FTP()
    # Checker.StreamIn(tech=DesignParameters._Technology)
    # import ftplib
    #
    # ftp = ftplib.FTP('141.223.22.156')
    # ftp.login('jicho0927', 'cho89140616!!')
    # ftp.cwd('/mnt/sdc/jicho0927/OPUS/tsmc65n')
    # myfile = open('NMOSWithDummy_iksu.gds', 'rb')
    # ftp.storbinary('STOR NMOSWithDummy_iksu.gds', myfile)
    # myfile.close()
    # ftp.close()
    print ('#############################      Finished      ################################')
    # end of 'main():' ---------------------------------------------------------------------------------------------
