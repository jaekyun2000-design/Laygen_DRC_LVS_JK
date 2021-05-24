from generatorLib import StickDiagram
from generatorLib import DesignParameters
# import user_define_exceptions


from generatorLib import DRC

import ftplib
from ftplib import FTP
import base64

import sys


class _NMOS(StickDiagram._StickDiagram):

    _ParametersForDesignCalculation= dict(_NMOSNumberofGate=None, _NMOSChannelWidth=None, _NMOSChannellength=None, _NMOSDummy=False )
    def __init__(self, _DesignParameter=None, _Name=None):

        if _DesignParameter!=None:
            self._DesignParameter=_DesignParameter
        else :
            self._DesignParameter = dict(
                                                    _ODLayer=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['DIFF'][0],_Datatype=DesignParameters._LayerMapping['DIFF'][1], _XYCoordinates=[],_XWidth=400, _YWidth=400), #boundary type:1, #path type:2, #sref type: 3, #gds data type: 4, #Design Name data type: 5,  #other data type: ?
                                                    _PODummyLayer=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0],_Datatype=DesignParameters._LayerMapping['POLY'][1], _XYCoordinates=[],_XWidth=400, _YWidth=400),
                                                    _POLayer=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0],_Datatype=DesignParameters._LayerMapping['POLY'][1], _XYCoordinates=[],_XWidth=400, _YWidth=400),
                                                    _PDKLayer=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['PDK'][0],_Datatype=DesignParameters._LayerMapping['PDK'][1], _XYCoordinates=[],_XWidth=400, _YWidth=400),
                                                    _Met1Layer=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0],_Datatype=DesignParameters._LayerMapping['METAL1'][1], _XYCoordinates=[],_XWidth=400, _YWidth=400),
                                                    _NPLayer=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['NIMP'][0],_Datatype=DesignParameters._LayerMapping['NIMP'][1], _XYCoordinates=[],_XWidth=400, _YWidth=400),
                                                    _COLayer=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['CONT'][0],_Datatype=DesignParameters._LayerMapping['CONT'][1], _XYCoordinates=[],_XWidth=400, _YWidth=400),
                                                    _WELLBodyLayer=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['WELLBODY'][0],_Datatype=DesignParameters._LayerMapping['WELLBODY'][1], _XYCoordinates=[],_XWidth=400, _YWidth=400),
                                                    _Name=self._NameDeclaration(_Name=_Name), _GDSFile=self._GDSObjDeclaration(_GDSFile=None),
                                                    _XYCoordinateNMOSSupplyRouting=dict(_DesignParametertype=7,_XYCoordinates=[]),_XYCoordinateNMOSOutputRouting=dict(_DesignParametertype=7,_XYCoordinates=[]),_XYCoordinateNMOSGateRouting=dict(_DesignParametertype=7,_XYCoordinates=[]),


                                                   )



        if _Name != None:
            self._DesignParameter['_Name']['_Name']=_Name






    def _CalculateNMOSDesignParameter(self, _NMOSNumberofGate=None, _NMOSChannelWidth=None, _NMOSChannellength=None, _NMOSDummy=False ):
        print('#########################################################################################################')
        print('                                    {}  NMOSContact Calculation Start                                    '.format(self._DesignParameter['_Name']['_Name']))
        print('#########################################################################################################')
        _DRCObj=DRC.DRC()

        _XYCoordinateOfNMOS = [[0,0]]

        print('#############################     POLY Layer Calculation    ##############################################')

        self._DesignParameter['_POLayer']['_XWidth']= _NMOSChannellength
        self._DesignParameter['_POLayer']['_YWidth']= _NMOSChannelWidth + 2 * _DRCObj._PolygateMinExtensionOnOD
        _LengthNMOSBtwPO = _DRCObj.DRCPolygateMinSpace(_DRCObj._CoMinWidth + 2 * _DRCObj._PolygateMinSpace2Co) + self._DesignParameter['_POLayer']['_XWidth']
        tmp=[]
        for i in range(0, _NMOSNumberofGate):
            if (_NMOSNumberofGate % 2) == 0:
                _xycoordinatetmp = [_XYCoordinateOfNMOS[0][0] - ( _NMOSNumberofGate / 2 - 0.5) \
                                 *  _LengthNMOSBtwPO + i *  _LengthNMOSBtwPO,  _XYCoordinateOfNMOS[0][1]]
            elif (_NMOSNumberofGate % 2) == 1:
                _xycoordinatetmp = [_XYCoordinateOfNMOS[0][0] - ( _NMOSNumberofGate - 1) / 2 \
                                 *  _LengthNMOSBtwPO + i *  _LengthNMOSBtwPO, _XYCoordinateOfNMOS[0][1]]
            tmp.append(_xycoordinatetmp)
        self._DesignParameter['_POLayer']['_XYCoordinates']=tmp
        print('#############################     DIFF Layer Calculation    ##############################################')
        _LengthNMOSBtwPO = _DRCObj.DRCPolygateMinSpace(_DRCObj._CoMinWidth + 2 * _DRCObj._PolygateMinSpace2Co) + self._DesignParameter['_POLayer']['_XWidth']
        self._DesignParameter['_ODLayer']['_XYCoordinates']=_XYCoordinateOfNMOS

        self._DesignParameter['_ODLayer']['_XWidth']=_LengthNMOSBtwPO*_NMOSNumberofGate +_DRCObj._CoMinWidth+ 2 * _DRCObj._CoMinEnclosureByOD
        self._DesignParameter['_ODLayer']['_YWidth']=_NMOSChannelWidth
        if _NMOSDummy == True:
            print('#############################     POLY Dummy Layer Calculation    ##############################################')

            self._DesignParameter['_PODummyLayer']['_XWidth']= _NMOSChannellength
            self._DesignParameter['_PODummyLayer']['_YWidth']= _NMOSChannelWidth + 2 * _DRCObj._PolygateMinExtensionOnOD

            _LengthNMOSBtwPO = _DRCObj.DRCPolygateMinSpace(_DRCObj._CoMinWidth + 2 * _DRCObj._PolygateMinSpace2Co) + self._DesignParameter['_POLayer']['_XWidth']

            #print 'testDisplay for debug', _DRCObj.DRCPolygateMinSpace(_DRCObj._CoMinWidth +  _DRCObj._PolygateMinSpace2Co + _DRCObj._CoMinEnclosureByOD + _DRCObj._PolygateMinSpace2OD + float(self._DesignParameter['_PODummyLayer']['_XWidth'])/2 + float(self._DesignParameter['_POLayer']['_XWidth'])/2), _DRCObj._CoMinWidth, _DRCObj._PolygateMinSpace2Co, _DRCObj._CoMinEnclosureByOD, _DRCObj._PolygateMinSpace2OD


            if (_NMOSNumberofGate % 2) == 0:
                _xycoordinatetmp = [
                                    [_XYCoordinateOfNMOS[0][0] - ( _NMOSNumberofGate / 2 - 0.5) *  _LengthNMOSBtwPO + 0 *  _LengthNMOSBtwPO - _DRCObj.DRCPolygateMinSpace(_DRCObj._CoMinWidth +  _DRCObj._PolygateMinSpace2Co + _DRCObj._CoMinEnclosureByOD + _DRCObj._PolygateMinSpace2OD ) - (float(self._DesignParameter['_PODummyLayer']['_XWidth'])/2 + float(self._DesignParameter['_POLayer']['_XWidth'])/2) ,  _XYCoordinateOfNMOS[0][1]],
                                    [_XYCoordinateOfNMOS[0][0] - ( _NMOSNumberofGate / 2 - 0.5) *  _LengthNMOSBtwPO + (_NMOSNumberofGate -1) *  _LengthNMOSBtwPO + _DRCObj.DRCPolygateMinSpace(_DRCObj._CoMinWidth +  _DRCObj._PolygateMinSpace2Co + _DRCObj._CoMinEnclosureByOD + _DRCObj._PolygateMinSpace2OD ) + float(self._DesignParameter['_PODummyLayer']['_XWidth'])/2 + float(self._DesignParameter['_POLayer']['_XWidth'])/2,  _XYCoordinateOfNMOS[0][1]],
                                    ]
            elif (_NMOSNumberofGate % 2) == 1:
                _xycoordinatetmp = [
                                    [_XYCoordinateOfNMOS[0][0] - ( _NMOSNumberofGate - 1) / 2 *  _LengthNMOSBtwPO + 0 *  _LengthNMOSBtwPO - _DRCObj.DRCPolygateMinSpace(_DRCObj._CoMinWidth +  _DRCObj._PolygateMinSpace2Co + _DRCObj._CoMinEnclosureByOD + _DRCObj._PolygateMinSpace2OD ) - (float(self._DesignParameter['_PODummyLayer']['_XWidth'])/2 + float(self._DesignParameter['_POLayer']['_XWidth'])/2), _XYCoordinateOfNMOS[0][1]],
                                    [_XYCoordinateOfNMOS[0][0] - ( _NMOSNumberofGate - 1) / 2 *  _LengthNMOSBtwPO + (_NMOSNumberofGate -1) *  _LengthNMOSBtwPO + _DRCObj.DRCPolygateMinSpace(_DRCObj._CoMinWidth +  _DRCObj._PolygateMinSpace2Co + _DRCObj._CoMinEnclosureByOD + _DRCObj._PolygateMinSpace2OD ) + (float(self._DesignParameter['_PODummyLayer']['_XWidth'])/2 + float(self._DesignParameter['_POLayer']['_XWidth'])/2), _XYCoordinateOfNMOS[0][1]],
                                    ]


            # _xycoordinatetmp = [
            #                     [self._DesignParameter['_ODLayer']['_XYCoordinates'][0][0] - float(self._DesignParameter['_ODLayer']['_XWidth'])/2 - _DRCObj._PolygateMinSpace2OD - float(self._DesignParameter['_PODummyLayer']['_XWidth'])/2,  _XYCoordinateOfNMOS[0][1]],
            #                     [self._DesignParameter['_ODLayer']['_XYCoordinates'][0][0] + float(self._DesignParameter['_ODLayer']['_XWidth'])/2 + _DRCObj._PolygateMinSpace2OD + float(self._DesignParameter['_PODummyLayer']['_XWidth'])/2,  _XYCoordinateOfNMOS[0][1]],
            #                     # [_XYCoordinateOfNMOS[0][0] - ( _NMOSNumberofGate / 2 - 0.5) *  _LengthNMOSBtwPO + 0 *  _LengthNMOSBtwPO,  _XYCoordinateOfNMOS[0][1]],
            #                     # [_XYCoordinateOfNMOS[0][0] - ( _NMOSNumberofGate / 2 - 0.5) *  _LengthNMOSBtwPO + (_NMOSNumberofGate -1) *  _LengthNMOSBtwPO,  _XYCoordinateOfNMOS[0][1]],
            #                     ]

            self._DesignParameter['_PODummyLayer']['_XYCoordinates']=_xycoordinatetmp
        else:
            self._DesignParameter['_PODummyLayer']['_XYCoordinates'] = []





        print('#############################     METAL1 Layer Calcuation    ##############################################')
        self._DesignParameter['_Met1Layer']['_XWidth'] = _DRCObj._CoMinWidth + 2*_DRCObj._Metal1MinEnclosureCO
        self._DesignParameter['_Met1Layer']['_YWidth'] = self._DesignParameter['_ODLayer']['_YWidth']
        _LengthNMOSBtwMet1 = _DRCObj.DRCPolygateMinSpace(_DRCObj._CoMinWidth + 2 * _DRCObj._PolygateMinSpace2Co) + self._DesignParameter['_POLayer']['_XWidth']

        tmp=[]


        for i in range(0, _NMOSNumberofGate + 1):
            if (_NMOSNumberofGate % 2) == 0:
                _xycoordinatetmp = [_XYCoordinateOfNMOS[0][0] - _NMOSNumberofGate / 2 *\
                                    _LengthNMOSBtwMet1 + i * _LengthNMOSBtwMet1,   _XYCoordinateOfNMOS[0][1]]
            elif (_NMOSNumberofGate % 2) == 1:
                _xycoordinatetmp = [_XYCoordinateOfNMOS[0][0] - ((_NMOSNumberofGate + 1) / 2 - 0.5) \
                                * _LengthNMOSBtwMet1 + i * _LengthNMOSBtwMet1, _XYCoordinateOfNMOS[0][1]]

            tmp.append(_xycoordinatetmp)

        self._DesignParameter['_Met1Layer']['_XYCoordinates']=tmp


        print('#############################     CONT Layer Calculation    ##############################################')
        _XNumberOfCOInNMOS=_NMOSNumberofGate+1
        _YNumberOfCOInNMOS=int(float(self._DesignParameter['_ODLayer']['_YWidth'] - 2 * max([_DRCObj._CoMinEnclosureByODAtLeastTwoSide , _DRCObj._Metal1MinEnclosureCO2 ] ) + _DRCObj._CoMinSpace) / ( _DRCObj._CoMinSpace + _DRCObj._CoMinWidth))
        self._DesignParameter['_COLayer']['_YWidth'] = _DRCObj._CoMinWidth
        self._DesignParameter['_COLayer']['_XWidth'] = _DRCObj._CoMinWidth

        _LengthNMOSBtwCO=_DRCObj._CoMinSpace + self._DesignParameter['_COLayer']['_YWidth']
        _LengthNMOSBtwMet1 = _DRCObj.DRCPolygateMinSpace(_DRCObj._CoMinWidth + 2 * _DRCObj._PolygateMinSpace2Co) + self._DesignParameter['_POLayer']['_XWidth']

        tmp=[]
###############################################Check the number of CO On NMOS TR##############################################################################################
        if _XNumberOfCOInNMOS ==0 or _YNumberOfCOInNMOS==0:
            print('************************* Error occured in {} Design Parameter Calculation******************************'.format(self._DesignParameter['_Name']['_Name']))
            if DesignParameters._DebugMode == 0:
                return 0
###############################################################################################################################################################################
        for i in range(0, _XNumberOfCOInNMOS):
            for j in range(0, _YNumberOfCOInNMOS):

                if (_XNumberOfCOInNMOS % 2) == 1 and (_YNumberOfCOInNMOS % 2) == 0:
                    _xycoordinatetmp = [_XYCoordinateOfNMOS[0][0] - (_XNumberOfCOInNMOS - 1 ) / 2 * _LengthNMOSBtwMet1 + i * _LengthNMOSBtwMet1,
                                        _XYCoordinateOfNMOS[0][1] -(_YNumberOfCOInNMOS / 2 - 0.5) * _LengthNMOSBtwCO + j * _LengthNMOSBtwCO]

                elif (_XNumberOfCOInNMOS % 2) == 1 and (_YNumberOfCOInNMOS% 2) == 1:
                    _xycoordinatetmp = [_XYCoordinateOfNMOS[0][0] - (_XNumberOfCOInNMOS - 1 ) / 2 * _LengthNMOSBtwMet1 + i * _LengthNMOSBtwMet1,
                                        _XYCoordinateOfNMOS[0][1] -(_YNumberOfCOInNMOS - 1) / 2 * _LengthNMOSBtwCO + j * _LengthNMOSBtwCO]

                elif (_XNumberOfCOInNMOS % 2)  == 0 and (_YNumberOfCOInNMOS % 2) == 0:
                    _xycoordinatetmp = [_XYCoordinateOfNMOS[0][0] - (_XNumberOfCOInNMOS / 2 - 0.5) * _LengthNMOSBtwMet1 + i * _LengthNMOSBtwMet1,
                                        _XYCoordinateOfNMOS[0][1] -(_YNumberOfCOInNMOS / 2 - 0.5) * _LengthNMOSBtwCO + j * _LengthNMOSBtwCO]

                elif (_XNumberOfCOInNMOS % 2)  == 0 and (_YNumberOfCOInNMOS % 2) == 1:
                    _xycoordinatetmp = [_XYCoordinateOfNMOS[0][0] - (_XNumberOfCOInNMOS / 2 - 0.5) * _LengthNMOSBtwMet1 + i * _LengthNMOSBtwMet1,
                                        _XYCoordinateOfNMOS[0][1] -(_YNumberOfCOInNMOS - 1) / 2 * _LengthNMOSBtwCO + j * _LengthNMOSBtwCO]
                tmp.append(_xycoordinatetmp)


        self._DesignParameter['_COLayer']['_XYCoordinates']=tmp
        print('#############################     NIMP Layer Calculation    ####################')
        self._DesignParameter['_NPLayer']['_XYCoordinates']=_XYCoordinateOfNMOS
        self._DesignParameter['_NPLayer']['_XWidth'] = self._DesignParameter['_ODLayer']['_XWidth'] + 2 * _DRCObj._NpMinExtensiononNactive if _NMOSDummy == False else \
            self._DesignParameter['_PODummyLayer']['_XWidth'] + abs(self._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][0] - self._DesignParameter['_PODummyLayer']['_XYCoordinates'][1][0]) + 2 * _DRCObj._NpMinEnclosureOfPo
        self._DesignParameter['_NPLayer']['_YWidth'] = self._DesignParameter['_POLayer']['_YWidth'] + 2 * _DRCObj._NpMinEnclosureOfPo


        # self._DesignParameter['_NLVTlayer'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['NLVT'][0],
        #                                             _Datatype=DesignParameters._LayerMapping['NLVT'][1],
        #                                             _XYCoordinates=[], _XWidth=400, _YWidth=400)
        # self._DesignParameter['_NLVTlayer']['_XYCoordinates'] = _XYCoordinateOfNMOS
        # self._DesignParameter['_NLVTlayer']['_XWidth'] = self._DesignParameter['_ODLayer']['_XWidth'] + 2 * _DRCObj._NpMinExtensiononNactive if _NMOSDummy == False else \
        #     self._DesignParameter['_NLVTlayer']['_XWidth'] + abs(self._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][0] -self._DesignParameter['_PODummyLayer']['_XYCoordinates'][1][0]) + 2 * _DRCObj._NpMinEnclosureOfPo
        # self._DesignParameter['_NLVTlayer']['_YWidth'] = self._DesignParameter['_POLayer'][
        #                                                    '_YWidth'] + 2 * _DRCObj._NpMinEnclosureOfPo

        if DesignParameters._Technology=='180nm':
            print('#############################     WELLBODY Layer Calculation    #########################################')
            self._DesignParameter['_WELLBodyLayer']['_XYCoordinates']=_XYCoordinateOfNMOS
            self._DesignParameter['_WELLBodyLayer']['_XWidth'] = self._DesignParameter['_ODLayer']['_XWidth']
            self._DesignParameter['_WELLBodyLayer']['_YWidth'] = self._DesignParameter['_ODLayer']['_YWidth']

        if DesignParameters._Technology=='065nm':
            print('################################     PDK Layer Calculation    ############################################')
            self._DesignParameter['_PDKLayer']['_XYCoordinates']=_XYCoordinateOfNMOS
            self._DesignParameter['_PDKLayer']['_XWidth'] = self._DesignParameter['_NPLayer']['_XWidth']
            self._DesignParameter['_PDKLayer']['_YWidth'] = self._DesignParameter['_NPLayer']['_YWidth']


        print('#########################     Supply Routing Coordinates Calculation   ##################################')
        tmp=[]
        _LengthNMOSBtwMet1 = _DRCObj.DRCPolygateMinSpace(_DRCObj._CoMinWidth + 2 * _DRCObj._PolygateMinSpace2Co) + self._DesignParameter['_POLayer']['_XWidth']
        if (_NMOSNumberofGate % 2)==0:
            for i in range(0, _NMOSNumberofGate / 2 + 1):
                #_XYCenter=[self._XYCoordinateNMOS[0] -  self._NumberOfNMOSGate / 2 * self._LengthBtwMet1 + i * self._LengthBtwMet1, self._XYCoordinateNMOS[1]]
                tmp.append([_XYCoordinateOfNMOS[0][0] -  _NMOSNumberofGate / 2 \
                                                                                       * _LengthNMOSBtwMet1 + i * 2 * _LengthNMOSBtwMet1, _XYCoordinateOfNMOS[0][1]])
        elif (_NMOSNumberofGate % 2)==1:
            for i in range(0,(_NMOSNumberofGate - 1) / 2 + 1 ):
                #_XYCenter=[self._XYCoordinateNMOS[0] - (  (self._NumberOfNMOSGate + 1) / 2 - 0.5) * self._LengthBtwMet1 + i * self._LengthBtwMet1, self._XYCoordinateNMOS[1]]
                tmp.append([_XYCoordinateOfNMOS[0][0] - (  (_NMOSNumberofGate + 1) / 2 - 0.5) \
                                                                                       * _LengthNMOSBtwMet1 + i * 2 * _LengthNMOSBtwMet1, _XYCoordinateOfNMOS[0][1]])

        self._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates']=tmp


        print('#########################     Output Routing Coordinates Calculation    ##################################')
        tmp=[]
        _LengthNMOSBtwMet1 = _DRCObj.DRCPolygateMinSpace(_DRCObj._CoMinWidth + 2 * _DRCObj._PolygateMinSpace2Co) + self._DesignParameter['_POLayer']['_XWidth']
        if (_NMOSNumberofGate % 2)==0:
            for i in range(0, _NMOSNumberofGate / 2 ):
                # _XYCenter=[self._XYCoordinateNMOS[0] -  self._NumberOfNMOSGate / 2 * self._LengthBtwMet1 + i * self._LengthBtwMet1, self._XYCoordinateNMOS[1]]
                tmp.append([_XYCoordinateOfNMOS[0][0] - _NMOSNumberofGate / 2 \
                                                                                       * _LengthNMOSBtwMet1 + ( i * 2 + 1) * _LengthNMOSBtwMet1, _XYCoordinateOfNMOS[0][1]])
        elif (_NMOSNumberofGate % 2)==1:
            for i in range(0, (_NMOSNumberofGate - 1) / 2 + 1):
                # _XYCenter=[self._XYCoordinateNMOS[0] - (  (self._NumberOfNMOSGate + 1) / 2 - 0.5) * self._LengthBtwMet1 + i * self._LengthBtwMet1, self._XYCoordinateNMOS[1]]
                tmp.append([_XYCoordinateOfNMOS[0][0] - ((_NMOSNumberofGate + 1) / 2 - 0.5)\
                                                                                       * _LengthNMOSBtwMet1 + ( i * 2 + 1 ) * _LengthNMOSBtwMet1, _XYCoordinateOfNMOS[0][1]])
        self._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates']=tmp



        print('#########################     Gate Routing Coordinates Calculation   ##################################')
        tmp=[]
        _LengthNMOSBtwMet1 = _DRCObj.DRCPolygateMinSpace(_DRCObj._CoMinWidth + 2 * _DRCObj._PolygateMinSpace2Co) + self._DesignParameter['_POLayer']['_XWidth']
        for i in range(0, _NMOSNumberofGate):
            if (_NMOSNumberofGate % 2) == 0:
                tmp.append([_XYCoordinateOfNMOS[0][0] - (_NMOSNumberofGate / 2 - 0.5) \
                                                                                    * _LengthNMOSBtwMet1 + i * _LengthNMOSBtwMet1, _XYCoordinateOfNMOS[0][1]])
                #_xycoordinatetmp = self.CenterCoordinateAndWidth2XYCoordinate(_XYCenter=[self._XYCoordinateNMOS[0] - (self._NumberOfNMOSGate / 2 - 0.5) * self._LengthBtwMet1 + i * self._LengthBtwMet1, self._XYCoordinateNMOS[1]], _WidthX=self._LengthNMOSPO, _WidthY=self._WidthNMOSPO)
            elif (_NMOSNumberofGate % 2) == 1:
                tmp.append([_XYCoordinateOfNMOS[0][0] - (_NMOSNumberofGate - 1) / 2 \
                                                                                    * _LengthNMOSBtwMet1 + i * _LengthNMOSBtwMet1,   _XYCoordinateOfNMOS[0][1]])

        self._DesignParameter['_XYCoordinateNMOSGateRouting']['_XYCoordinates']=tmp



        del _DRCObj
        print('#########################################################################################################')
        print('                                    {}  NMOSContact Calculation End                                   '.format(self._DesignParameter['_Name']['_Name']))
        print('#########################################################################################################')


if __name__=='__main__':
    # _NMOSFinger = 4
    # _NMOSWidth = 600
    # _NMOSChannelLength = 40
    # _NMOSDummy = True
    # # DesignParameters._Technology='045nm'
    # # print 'Technology Process', DesignParameters._Technology
    # NMOSObj=_NMOS(_DesignParameter=None, _Name='NMOS')
    # NMOSObj._CalculateNMOSDesignParameter(_NMOSNumberofGate=_NMOSFinger, _NMOSChannelWidth=_NMOSWidth, _NMOSChannellength=_NMOSChannelLength, _NMOSDummy=_NMOSDummy)
    # NMOSObj._UpdateDesignParameter2GDSStructure(_DesignParameterInDictionary=NMOSObj._DesignParameter)
    # testStreamFile=open('./testStreamFile.gds','wb')
    # tmp=NMOSObj._CreateGDSStream(NMOSObj._DesignParameter['_GDSFile']['_GDSFile'])
    # tmp.write_binary_gds_stream(testStreamFile)
    # testStreamFile.close()
    # print '###############open ftp connection & update gds file to cadence server###################'
    # ftp_cadence_server=ftplib.FTP('141.223.86.109')
    # ftp_cadence_server.login(base64.b64decode('YWxlY25ldzE='),base64.b64decode('NzNoazNhYWs='))
    # if DesignParameters._Technology =='065nm':
    #     ftp_cadence_server.cwd('/home/alecnew1/OPUS/design_automation')
    # elif DesignParameters._Technology =='180nm':
    #     ftp_cadence_server.cwd('/home/alecnew1/OPUS/DesignAutomationTSMC018')
    # elif DesignParameters._Technology =='045nm':
    #     ftp_cadence_server.cwd('/home/alecnew1/OPUS/DesignAutomationTSMC45')
    # print ftp_cadence_server.pwd()
    # testStreamFile=open('./testStreamFile.gds','rb')
    # ftp_cadence_server.storbinary('STOR testStreamFile.gds', testStreamFile)
    # print 'close ftp connection'
    # ftp_cadence_server.quit()
    # testStreamFile.close()
    #
    # print '##########################################################################################'
    # # print globals()
    # # tmp=globals()
    # # for var in tmp.keys():
    # #     print var
    # # all = [var for var in globals().keys() if var[1] != "_" ]
    # # print all
    # # for var in all:
    # #     del globals()[var]
    # #
    # # del globals()['all']
    # # del globals()['var']
    # # print globals()


    # _NMOSFinger = 3
    # _NMOSWidth = 600
    # _NMOSChannelLength = 60
    # _NMOSDummy = True
    # DesignParameters._Technology='065nm'
    # print 'Technology Process', DesignParameters._Technology
    # NMOSObj=_NMOS(_DesignParameter=None, _Name='NMOS')
    # NMOSObj._CalculateNMOSDesignParameter(_NMOSNumberofGate=_NMOSFinger, _NMOSChannelWidth=_NMOSWidth, _NMOSChannellength=_NMOSChannelLength, _NMOSDummy=_NMOSDummy)
    # NMOSObj._UpdateDesignParameter2GDSStructure(_DesignParameterInDictionary=NMOSObj._DesignParameter)
    # testStreamFile=open('./testStreamFile.gds','wb')
    # tmp=NMOSObj._CreateGDSStream(NMOSObj._DesignParameter['_GDSFile']['_GDSFile'])
    # tmp.write_binary_gds_stream(testStreamFile)
    # testStreamFile.close()
    # print '###############open ftp connection & update gds file to cadence server###################'
    # ftp_cadence_server=ftplib.FTP('141.223.86.109')
    # ftp_cadence_server.login(base64.b64decode('YWxlY25ldzE='),base64.b64decode('NzNoazNhYWs='))
    # if DesignParameters._Technology =='065nm':
    #     ftp_cadence_server.cwd('/home/alecnew1/OPUS/design_automation')
    # elif DesignParameters._Technology =='180nm':
    #     ftp_cadence_server.cwd('/home/alecnew1/OPUS/DesignAutomationTSMC018')
    # elif DesignParameters._Technology =='045nm':
    #     ftp_cadence_server.cwd('/home/alecnew1/OPUS/DesignAutomationTSMC45')
    # print ftp_cadence_server.pwd()
    # testStreamFile=open('./testStreamFile.gds','rb')
    # ftp_cadence_server.storbinary('STOR testStreamFile.gds', testStreamFile)
    # print 'close ftp connection'
    # ftp_cadence_server.quit()
    # testStreamFile.close()
    #
    # print '##########################################################################################'
    # # tmp=globals()
    # # for var in tmp.keys():
    # #     print var
    # # all = [var for var in globals().keys() if var[1] != "_" ]
    # # print all
    # # for var in all:
    # #     del globals()[var]
    # #
    # # del globals()['all']
    # # del globals()['var']
    # # print globals()

    _NMOSFinger = 3
    _NMOSWidth = 1000
    _NMOSChannelLength = 180
    _NMOSDummy = True
    DesignParameters._Technology='065nm'
    print('Technology Process', DesignParameters._Technology)
    NMOSObj=_NMOS(_DesignParameter=None, _Name='NMOS')
    NMOSObj._CalculateNMOSDesignParameter(_NMOSNumberofGate=_NMOSFinger, _NMOSChannelWidth=_NMOSWidth, _NMOSChannellength=_NMOSChannelLength, _NMOSDummy=_NMOSDummy)
    NMOSObj._UpdateDesignParameter2GDSStructure(_DesignParameterInDictionary=NMOSObj._DesignParameter)
    testStreamFile=open('./testStreamFile.gds','wb')
    tmp=NMOSObj._CreateGDSStream(NMOSObj._DesignParameter['_GDSFile']['_GDSFile'])
    tmp.write_binary_gds_stream(testStreamFile)
    testStreamFile.close()
   

    print('##########################################################################################')
