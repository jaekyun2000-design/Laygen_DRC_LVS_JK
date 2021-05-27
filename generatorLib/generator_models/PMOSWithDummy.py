from generatorLib import StickDiagram
from generatorLib import DesignParameters
# import user_define_exceptions


from generatorLib import DRC

import ftplib
from ftplib import FTP
import base64

import sys


class _PMOS(StickDiagram._StickDiagram):

    _ParametersForDesignCalculation= dict(_PMOSNumberofGate=None, _PMOSChannelWidth=None, _PMOSChannellength=None, _PMOSDummy=False )
    def __init__(self, _DesignParameter=None, _Name=None):

        if _DesignParameter!=None:
            self._DesignParameter=_DesignParameter
        else :
            self._DesignParameter = dict(
                                                    _ODLayer=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['DIFF'][0],_Datatype=DesignParameters._LayerMapping['DIFF'][1], _XYCoordinates=[],_XWidth=400, _YWidth=400), #boundary type:1, #path type:2, #sref type: 3, #gds data type: 4, #Design Name data type: 5,  #other data type: ?
                                                    _PODummyLayer=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0],_Datatype=DesignParameters._LayerMapping['POLY'][1], _XYCoordinates=[],_XWidth=400, _YWidth=400),
                                                    _POLayer=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0],_Datatype=DesignParameters._LayerMapping['POLY'][1], _XYCoordinates=[],_XWidth=400, _YWidth=400),
                                                    _Met1Layer=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0],_Datatype=DesignParameters._LayerMapping['METAL1'][1], _XYCoordinates=[],_XWidth=400, _YWidth=400),
                                                    _PPLayer=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['PIMP'][0],_Datatype=DesignParameters._LayerMapping['PIMP'][1], _XYCoordinates=[],_XWidth=400, _YWidth=400),
                                                    _COLayer=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['CONT'][0],_Datatype=DesignParameters._LayerMapping['CONT'][1], _XYCoordinates=[],_XWidth=400, _YWidth=400),
                                                    _Name=self._NameDeclaration(_Name=_Name), _GDSFile=self._GDSObjDeclaration(_GDSFile=None),
                                                    _XYCoordinatePMOSSupplyRouting=dict(_DesignParametertype=7,_XYCoordinates=[]),_XYCoordinatePMOSOutputRouting=dict(_DesignParametertype=7,_XYCoordinates=[]),_XYCoordinatePMOSGateRouting=dict(_DesignParametertype=7,_XYCoordinates=[]),


                                                   )



        if _Name != None:
            self._DesignParameter['_Name']['_Name']=_Name

    def _CalculatePMOSDesignParameter(self, _PMOSNumberofGate=None, _PMOSChannelWidth=None, _PMOSChannellength=None, _PMOSDummy=False ):
        print('#########################################################################################################')
        print('                                    {}  PMOSContact Calculation Start                                    '.format(self._DesignParameter['_Name']['_Name']))
        print('#########################################################################################################')
        _DRCObj=DRC.DRC()

        _XYCoordinateOfPMOS = [[0,0]]

        print('#############################     POLY Layer Calculation    ##############################################')

        self._DesignParameter['_POLayer']['_XWidth']= _PMOSChannellength
        self._DesignParameter['_POLayer']['_YWidth']= _PMOSChannelWidth + 2 * _DRCObj._PolygateMinExtensionOnOD
        _LengthPMOSBtwPO = _DRCObj.DRCPolygateMinSpace(_DRCObj._CoMinWidth + 2 * _DRCObj._PolygateMinSpace2Co) + self._DesignParameter['_POLayer']['_XWidth']
        tmp=[]
        for i in range(0, _PMOSNumberofGate):
            if (_PMOSNumberofGate % 2) == 0:
                _xycoordinatetmp = [_XYCoordinateOfPMOS[0][0] - ( _PMOSNumberofGate / 2 - 0.5) \
                                 *  _LengthPMOSBtwPO + i *  _LengthPMOSBtwPO,  _XYCoordinateOfPMOS[0][1]]
            elif (_PMOSNumberofGate % 2) == 1:
                _xycoordinatetmp = [_XYCoordinateOfPMOS[0][0] - ( _PMOSNumberofGate - 1) / 2 \
                                 *  _LengthPMOSBtwPO + i *  _LengthPMOSBtwPO, _XYCoordinateOfPMOS[0][1]]
            tmp.append(_xycoordinatetmp)
        self._DesignParameter['_POLayer']['_XYCoordinates']=tmp
        print('#############################     DIFF Layer Calculation    ##############################################')
        _LengthPMOSBtwPO = _DRCObj.DRCPolygateMinSpace(_DRCObj._CoMinWidth + 2 * _DRCObj._PolygateMinSpace2Co) + self._DesignParameter['_POLayer']['_XWidth']
        self._DesignParameter['_ODLayer']['_XYCoordinates']=_XYCoordinateOfPMOS

        self._DesignParameter['_ODLayer']['_XWidth']=_LengthPMOSBtwPO*_PMOSNumberofGate +_DRCObj._CoMinWidth+ 2 * _DRCObj._CoMinEnclosureByOD
        self._DesignParameter['_ODLayer']['_YWidth']=_PMOSChannelWidth
        if _PMOSDummy == True:
            print('#############################     POLY Dummy Layer Calculation    ##############################################')

            self._DesignParameter['_PODummyLayer']['_XWidth']= _PMOSChannellength
            self._DesignParameter['_PODummyLayer']['_YWidth']= _PMOSChannelWidth + 2 * _DRCObj._PolygateMinExtensionOnOD

            _LengthPMOSBtwPO = _DRCObj.DRCPolygateMinSpace(_DRCObj._CoMinWidth + 2 * _DRCObj._PolygateMinSpace2Co) + self._DesignParameter['_POLayer']['_XWidth']

            #print 'testDisplay for debug', _DRCObj.DRCPolygateMinSpace(_DRCObj._CoMinWidth +  _DRCObj._PolygateMinSpace2Co + _DRCObj._CoMinEnclosureByOD + _DRCObj._PolygateMinSpace2OD + float(self._DesignParameter['_PODummyLayer']['_XWidth'])/2 + float(self._DesignParameter['_POLayer']['_XWidth'])/2), _DRCObj._CoMinWidth, _DRCObj._PolygateMinSpace2Co, _DRCObj._CoMinEnclosureByOD, _DRCObj._PolygateMinSpace2OD


            if (_PMOSNumberofGate % 2) == 0:
                _xycoordinatetmp = [
                                    [_XYCoordinateOfPMOS[0][0] - ( _PMOSNumberofGate / 2 - 0.5) *  _LengthPMOSBtwPO + 0 *  _LengthPMOSBtwPO - _DRCObj.DRCPolygateMinSpace(_DRCObj._CoMinWidth +  _DRCObj._PolygateMinSpace2Co + _DRCObj._CoMinEnclosureByOD + _DRCObj._PolygateMinSpace2OD ) - (float(self._DesignParameter['_PODummyLayer']['_XWidth'])/2 + float(self._DesignParameter['_POLayer']['_XWidth'])/2) ,  _XYCoordinateOfPMOS[0][1]],
                                    [_XYCoordinateOfPMOS[0][0] - ( _PMOSNumberofGate / 2 - 0.5) *  _LengthPMOSBtwPO + (_PMOSNumberofGate -1) *  _LengthPMOSBtwPO + _DRCObj.DRCPolygateMinSpace(_DRCObj._CoMinWidth +  _DRCObj._PolygateMinSpace2Co + _DRCObj._CoMinEnclosureByOD + _DRCObj._PolygateMinSpace2OD ) + float(self._DesignParameter['_PODummyLayer']['_XWidth'])/2 + float(self._DesignParameter['_POLayer']['_XWidth'])/2,  _XYCoordinateOfPMOS[0][1]],
                                    ]
            elif (_PMOSNumberofGate % 2) == 1:
                _xycoordinatetmp = [
                                    [_XYCoordinateOfPMOS[0][0] - ( _PMOSNumberofGate - 1) / 2 *  _LengthPMOSBtwPO + 0 *  _LengthPMOSBtwPO - _DRCObj.DRCPolygateMinSpace(_DRCObj._CoMinWidth +  _DRCObj._PolygateMinSpace2Co + _DRCObj._CoMinEnclosureByOD + _DRCObj._PolygateMinSpace2OD ) - (float(self._DesignParameter['_PODummyLayer']['_XWidth'])/2 + float(self._DesignParameter['_POLayer']['_XWidth'])/2), _XYCoordinateOfPMOS[0][1]],
                                    [_XYCoordinateOfPMOS[0][0] - ( _PMOSNumberofGate - 1) / 2 *  _LengthPMOSBtwPO + (_PMOSNumberofGate -1) *  _LengthPMOSBtwPO + _DRCObj.DRCPolygateMinSpace(_DRCObj._CoMinWidth +  _DRCObj._PolygateMinSpace2Co + _DRCObj._CoMinEnclosureByOD + _DRCObj._PolygateMinSpace2OD ) + (float(self._DesignParameter['_PODummyLayer']['_XWidth'])/2 + float(self._DesignParameter['_POLayer']['_XWidth'])/2), _XYCoordinateOfPMOS[0][1]],
                                    ]


            # _xycoordinatetmp = [
            #                     [self._DesignParameter['_ODLayer']['_XYCoordinates'][0][0] - float(self._DesignParameter['_ODLayer']['_XWidth'])/2 - _DRCObj._PolygateMinSpace2OD - float(self._DesignParameter['_PODummyLayer']['_XWidth'])/2,  _XYCoordinateOfPMOS[0][1]],
            #                     [self._DesignParameter['_ODLayer']['_XYCoordinates'][0][0] + float(self._DesignParameter['_ODLayer']['_XWidth'])/2 + _DRCObj._PolygateMinSpace2OD + float(self._DesignParameter['_PODummyLayer']['_XWidth'])/2,  _XYCoordinateOfPMOS[0][1]],
            #                     # [_XYCoordinateOfPMOS[0][0] - ( _PMOSNumberofGate / 2 - 0.5) *  _LengthPMOSBtwPO + 0 *  _LengthPMOSBtwPO,  _XYCoordinateOfPMOS[0][1]],
            #                     # [_XYCoordinateOfPMOS[0][0] - ( _PMOSNumberofGate / 2 - 0.5) *  _LengthPMOSBtwPO + (_PMOSNumberofGate -1) *  _LengthPMOSBtwPO,  _XYCoordinateOfPMOS[0][1]],
            #                     ]

            self._DesignParameter['_PODummyLayer']['_XYCoordinates']=_xycoordinatetmp
        else:
            self._DesignParameter['_PODummyLayer']['_XYCoordinates'] = []





        print('#############################     METAL1 Layer Calcuation    ##############################################')
        self._DesignParameter['_Met1Layer']['_XWidth'] = _DRCObj._CoMinWidth + 2*_DRCObj._Metal1MinEnclosureCO
        self._DesignParameter['_Met1Layer']['_YWidth'] = self._DesignParameter['_ODLayer']['_YWidth']
        _LengthPMOSBtwMet1 = _DRCObj.DRCPolygateMinSpace(_DRCObj._CoMinWidth + 2 * _DRCObj._PolygateMinSpace2Co) + self._DesignParameter['_POLayer']['_XWidth']

        tmp=[]


        for i in range(0, _PMOSNumberofGate + 1):
            if (_PMOSNumberofGate % 2) == 0:
                _xycoordinatetmp = [_XYCoordinateOfPMOS[0][0] - _PMOSNumberofGate / 2 *\
                                    _LengthPMOSBtwMet1 + i * _LengthPMOSBtwMet1,   _XYCoordinateOfPMOS[0][1]]
            elif (_PMOSNumberofGate % 2) == 1:
                _xycoordinatetmp = [_XYCoordinateOfPMOS[0][0] - ((_PMOSNumberofGate + 1) / 2 - 0.5) \
                                * _LengthPMOSBtwMet1 + i * _LengthPMOSBtwMet1, _XYCoordinateOfPMOS[0][1]]

            tmp.append(_xycoordinatetmp)

        self._DesignParameter['_Met1Layer']['_XYCoordinates']=tmp


        print('#############################     CONT Layer Calculation    ##############################################')
        _XNumberOfCOInPMOS=_PMOSNumberofGate+1
        _YNumberOfCOInPMOS=int(float(self._DesignParameter['_ODLayer']['_YWidth'] - 2 * max([_DRCObj._CoMinEnclosureByODAtLeastTwoSide , _DRCObj._Metal1MinEnclosureCO2 ] ) + _DRCObj._CoMinSpace) / ( _DRCObj._CoMinSpace + _DRCObj._CoMinWidth))
        self._DesignParameter['_COLayer']['_YWidth'] = _DRCObj._CoMinWidth
        self._DesignParameter['_COLayer']['_XWidth'] = _DRCObj._CoMinWidth

        _LengthPMOSBtwCO=_DRCObj._CoMinSpace + self._DesignParameter['_COLayer']['_YWidth']
        _LengthPMOSBtwMet1 = _DRCObj.DRCPolygateMinSpace(_DRCObj._CoMinWidth + 2 * _DRCObj._PolygateMinSpace2Co) + self._DesignParameter['_POLayer']['_XWidth']

        tmp=[]
###############################################Check the number of CO On PMOS TR##############################################################################################
        if _XNumberOfCOInPMOS ==0 or _YNumberOfCOInPMOS==0:
            print('************************* Error occured in {} Design Parameter Calculation******************************'.format(self._DesignParameter['_Name']['_Name']))
            if DesignParameters._DebugMode == 0:
                return 0
###############################################################################################################################################################################
        for i in range(0, _XNumberOfCOInPMOS):
            for j in range(0, _YNumberOfCOInPMOS):

                if (_XNumberOfCOInPMOS % 2) == 1 and (_YNumberOfCOInPMOS % 2) == 0:
                    _xycoordinatetmp = [_XYCoordinateOfPMOS[0][0] - (_XNumberOfCOInPMOS - 1 ) / 2 * _LengthPMOSBtwMet1 + i * _LengthPMOSBtwMet1,
                                        _XYCoordinateOfPMOS[0][1] -(_YNumberOfCOInPMOS / 2 - 0.5) * _LengthPMOSBtwCO + j * _LengthPMOSBtwCO]

                elif (_XNumberOfCOInPMOS % 2) == 1 and (_YNumberOfCOInPMOS% 2) == 1:
                    _xycoordinatetmp = [_XYCoordinateOfPMOS[0][0] - (_XNumberOfCOInPMOS - 1 ) / 2 * _LengthPMOSBtwMet1 + i * _LengthPMOSBtwMet1,
                                        _XYCoordinateOfPMOS[0][1] -(_YNumberOfCOInPMOS - 1) / 2 * _LengthPMOSBtwCO + j * _LengthPMOSBtwCO]

                elif (_XNumberOfCOInPMOS % 2)  == 0 and (_YNumberOfCOInPMOS % 2) == 0:
                    _xycoordinatetmp = [_XYCoordinateOfPMOS[0][0] - (_XNumberOfCOInPMOS / 2 - 0.5) * _LengthPMOSBtwMet1 + i * _LengthPMOSBtwMet1,
                                        _XYCoordinateOfPMOS[0][1] -(_YNumberOfCOInPMOS / 2 - 0.5) * _LengthPMOSBtwCO + j * _LengthPMOSBtwCO]

                elif (_XNumberOfCOInPMOS % 2)  == 0 and (_YNumberOfCOInPMOS % 2) == 1:
                    _xycoordinatetmp = [_XYCoordinateOfPMOS[0][0] - (_XNumberOfCOInPMOS / 2 - 0.5) * _LengthPMOSBtwMet1 + i * _LengthPMOSBtwMet1,
                                        _XYCoordinateOfPMOS[0][1] -(_YNumberOfCOInPMOS - 1) / 2 * _LengthPMOSBtwCO + j * _LengthPMOSBtwCO]
                tmp.append(_xycoordinatetmp)


        self._DesignParameter['_COLayer']['_XYCoordinates']=tmp
        print('#############################     PIMP Layer Calculation    ####################')
        self._DesignParameter['_PPLayer']['_XYCoordinates']=_XYCoordinateOfPMOS
        self._DesignParameter['_PPLayer']['_XWidth'] = self._DesignParameter['_ODLayer']['_XWidth'] + 2 * _DRCObj._PpMinExtensiononPactive if _PMOSDummy == False else \
            self._DesignParameter['_PODummyLayer']['_XWidth'] + abs(self._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][0] - self._DesignParameter['_PODummyLayer']['_XYCoordinates'][1][0]) + 2 * _DRCObj._PpMinEnclosureOfPo
        self._DesignParameter['_PPLayer']['_YWidth'] = self._DesignParameter['_POLayer']['_YWidth'] + 2 * _DRCObj._PpMinEnclosureOfPo





        print('#########################     Supply Routing Coordinates Calculation   ##################################')
        tmp=[]
        _LengthPMOSBtwMet1 = _DRCObj.DRCPolygateMinSpace(_DRCObj._CoMinWidth + 2 * _DRCObj._PolygateMinSpace2Co) + self._DesignParameter['_POLayer']['_XWidth']
        if (_PMOSNumberofGate % 2)==0:
            for i in range(0, _PMOSNumberofGate // 2 + 1):
                #_XYCenter=[self._XYCoordinatePMOS[0] -  self._NumberOfPMOSGate / 2 * self._LengthBtwMet1 + i * self._LengthBtwMet1, self._XYCoordinatePMOS[1]]
                tmp.append([_XYCoordinateOfPMOS[0][0] -  _PMOSNumberofGate / 2 \
                                                                                       * _LengthPMOSBtwMet1 + i * 2 * _LengthPMOSBtwMet1, _XYCoordinateOfPMOS[0][1]])
        elif (_PMOSNumberofGate % 2)==1:
            for i in range(0,(_PMOSNumberofGate - 1) // 2 + 1 ):
                #_XYCenter=[self._XYCoordinatePMOS[0] - (  (self._NumberOfPMOSGate + 1) / 2 - 0.5) * self._LengthBtwMet1 + i * self._LengthBtwMet1, self._XYCoordinatePMOS[1]]
                tmp.append([_XYCoordinateOfPMOS[0][0] - (  (_PMOSNumberofGate + 1) / 2 - 0.5) \
                                                                                       * _LengthPMOSBtwMet1 + i * 2 * _LengthPMOSBtwMet1, _XYCoordinateOfPMOS[0][1]])

        self._DesignParameter['_XYCoordinatePMOSSupplyRouting']['_XYCoordinates']=tmp


        print('#########################     Output Routing Coordinates Calculation    ##################################')
        tmp=[]
        _LengthPMOSBtwMet1 = _DRCObj.DRCPolygateMinSpace(_DRCObj._CoMinWidth + 2 * _DRCObj._PolygateMinSpace2Co) + self._DesignParameter['_POLayer']['_XWidth']
        if (_PMOSNumberofGate % 2)==0:
            for i in range(0, _PMOSNumberofGate // 2 ):
                # _XYCenter=[self._XYCoordinatePMOS[0] -  self._NumberOfPMOSGate / 2 * self._LengthBtwMet1 + i * self._LengthBtwMet1, self._XYCoordinatePMOS[1]]
                tmp.append([_XYCoordinateOfPMOS[0][0] - _PMOSNumberofGate / 2 \
                                                                                       * _LengthPMOSBtwMet1 + ( i * 2 + 1) * _LengthPMOSBtwMet1, _XYCoordinateOfPMOS[0][1]])
        elif (_PMOSNumberofGate % 2)==1:
            for i in range(0, (_PMOSNumberofGate - 1) // 2 + 1):
                # _XYCenter=[self._XYCoordinatePMOS[0] - (  (self._NumberOfPMOSGate + 1) / 2 - 0.5) * self._LengthBtwMet1 + i * self._LengthBtwMet1, self._XYCoordinatePMOS[1]]
                tmp.append([_XYCoordinateOfPMOS[0][0] - ((_PMOSNumberofGate + 1) / 2 - 0.5)\
                                                                                       * _LengthPMOSBtwMet1 + ( i * 2 + 1 ) * _LengthPMOSBtwMet1, _XYCoordinateOfPMOS[0][1]])
        self._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates']=tmp



        print('#########################     Gate Routing Coordinates Calculation   ##################################')
        tmp=[]
        _LengthPMOSBtwMet1 = _DRCObj.DRCPolygateMinSpace(_DRCObj._CoMinWidth + 2 * _DRCObj._PolygateMinSpace2Co) + self._DesignParameter['_POLayer']['_XWidth']
        for i in range(0, _PMOSNumberofGate):
            if (_PMOSNumberofGate % 2) == 0:
                tmp.append([_XYCoordinateOfPMOS[0][0] - (_PMOSNumberofGate / 2 - 0.5) \
                                                                                    * _LengthPMOSBtwMet1 + i * _LengthPMOSBtwMet1, _XYCoordinateOfPMOS[0][1]])
                #_xycoordinatetmp = self.CenterCoordinateAndWidth2XYCoordinate(_XYCenter=[self._XYCoordinatePMOS[0] - (self._NumberOfPMOSGate / 2 - 0.5) * self._LengthBtwMet1 + i * self._LengthBtwMet1, self._XYCoordinatePMOS[1]], _WidthX=self._LengthPMOSPO, _WidthY=self._WidthPMOSPO)
            elif (_PMOSNumberofGate % 2) == 1:
                tmp.append([_XYCoordinateOfPMOS[0][0] - (_PMOSNumberofGate - 1) / 2 \
                                                                                    * _LengthPMOSBtwMet1 + i * _LengthPMOSBtwMet1,   _XYCoordinateOfPMOS[0][1]])

        self._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates']=tmp



        del _DRCObj
        print('#########################################################################################################')
        print('                                    {}  PMOSContact Calculation End                                   '.format(self._DesignParameter['_Name']['_Name']))
        print('#########################################################################################################')


if __name__=='__main__':
    _PMOSFinger = 4
    _PMOSWidth = 600
    _PMOSChannelLength = 40
    _PMOSDummy = True
    # DesignParameters._Technology='045nm'
    # print 'Technology Process', DesignParameters._Technology
    PMOSObj=_PMOS(_DesignParameter=None, _Name='PMOS')
    PMOSObj._CalculatePMOSDesignParameter(_PMOSNumberofGate=_PMOSFinger, _PMOSChannelWidth=_PMOSWidth, _PMOSChannellength=_PMOSChannelLength, _PMOSDummy=_PMOSDummy)
    PMOSObj._UpdateDesignParameter2GDSStructure(_DesignParameterInDictionary=PMOSObj._DesignParameter)
    testStreamFile=open('./testStreamFile.gds','wb')
    tmp=PMOSObj._CreateGDSStream(PMOSObj._DesignParameter['_GDSFile']['_GDSFile'])
    tmp.write_binary_gds_stream(testStreamFile)
    testStreamFile.close()

    print('##########################################################################################')

