from generatorLib import StickDiagram
from generatorLib import DesignParameters
# import user_define_exceptions


from generatorLib import DRC
import ftplib
from ftplib import FTP
import base64

class _ViaPoly2Met1(StickDiagram._StickDiagram):
    _ParametersForDesignCalculation= dict(_ViaPoly2Met1NumberOfCOX=None, _ViaPoly2Met1NumberOfCOY=None )


    def __init__(self, _DesignParameter=None, _Name=None):

        if _DesignParameter!=None:
            self._DesignParameter=_DesignParameter
        else :
            self._DesignParameter = dict(
                                                    _POLayer=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0],_Datatype=DesignParameters._LayerMapping['POLY'][1], _XYCoordinates=[],_XWidth=400, _YWidth=400),
                                                    _Met1Layer=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0],_Datatype=DesignParameters._LayerMapping['METAL1'][1], _XYCoordinates=[],_XWidth=400, _YWidth=400),
                                                    _COLayer=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['CONT'][0],_Datatype=DesignParameters._LayerMapping['CONT'][1], _XYCoordinates=[],_XWidth=400, _YWidth=400),
                                                    _Name=self._NameDeclaration(_Name=_Name), _GDSFile=self._GDSObjDeclaration(_GDSFile=None)


                                                   )



        if _Name != None:
            self._DesignParameter['_Name']['_Name']=_Name



    def _CalculateViaPoly2Met1DesignParameter(self, _ViaPoly2Met1NumberOfCOX=None, _ViaPoly2Met1NumberOfCOY=None ):
        print('#########################################################################################################')
        print('                                    {}  ViaPoly2Met1 Calculation Start                                    '.format(self._DesignParameter['_Name']['_Name']))
        print('#########################################################################################################')

        ###############################################Check the number of CO On Via Contact###########################################################################################
        if _ViaPoly2Met1NumberOfCOX ==0 or _ViaPoly2Met1NumberOfCOY==0:
            print('************************* Error occured in {} Design Parameter Calculation******************************'.format(self._DesignParameter['_Name']['_Name']))
            if DesignParameters._DebugMode == 0:
                return 0
        ###############################################################################################################################################################################
        _DRCObj=DRC.DRC()
        _XYCoordinateOfViaPoly2Met1 = [[0,0]]


        print('#############################     POLY Layer Calculation   ##############################################')

        _LengthViaPoly2Met1BtwCO = _DRCObj._CoMinWidth + _DRCObj.DRCCOMinSpace(NumOfCOX=_ViaPoly2Met1NumberOfCOX,NumOfCOY=_ViaPoly2Met1NumberOfCOY )
        self._DesignParameter['_POLayer']['_XYCoordinates']=_XYCoordinateOfViaPoly2Met1
        self._DesignParameter['_POLayer']['_XWidth']= _DRCObj._CoMinWidth + (_ViaPoly2Met1NumberOfCOX - 1)* _LengthViaPoly2Met1BtwCO+ 2 * _DRCObj._CoMinEnclosureByPOAtLeastTwoSide
        self._DesignParameter['_POLayer']['_YWidth']= _DRCObj._CoMinWidth + (_ViaPoly2Met1NumberOfCOY - 1)* _LengthViaPoly2Met1BtwCO+ 2 * _DRCObj._CoMinEnclosureByPOAtLeastTwoSide


        print('#############################     Met1 Layer Calculation   ##############################################')
        _LengthViaPoly2Met1BtwCO = _DRCObj._CoMinWidth + _DRCObj.DRCCOMinSpace(NumOfCOX=_ViaPoly2Met1NumberOfCOX,NumOfCOY=_ViaPoly2Met1NumberOfCOY )
        self._DesignParameter['_Met1Layer']['_XYCoordinates']=_XYCoordinateOfViaPoly2Met1
        self._DesignParameter['_Met1Layer']['_XWidth']=_DRCObj._CoMinWidth + (_ViaPoly2Met1NumberOfCOX - 1)* _LengthViaPoly2Met1BtwCO+ 2 * _DRCObj._Metal1MinEnclosureCO2
        self._DesignParameter['_Met1Layer']['_YWidth']=_DRCObj._CoMinWidth + (_ViaPoly2Met1NumberOfCOY - 1)* _LengthViaPoly2Met1BtwCO+ 2 * _DRCObj._Metal1MinEnclosureCO2

        print('#############################     Cont Layer Calculation   ##############################################')

        tmp=[]
        self._DesignParameter['_COLayer']['_XWidth'] = _DRCObj._CoMinWidth
        self._DesignParameter['_COLayer']['_YWidth'] = _DRCObj._CoMinWidth
        _LengthViaPoly2Met1BtwCO = _DRCObj._CoMinWidth + _DRCObj.DRCCOMinSpace(NumOfCOX=_ViaPoly2Met1NumberOfCOX,NumOfCOY=_ViaPoly2Met1NumberOfCOY )
        for i in range(0, _ViaPoly2Met1NumberOfCOX):
            for j in range(0, _ViaPoly2Met1NumberOfCOY):

                if (_ViaPoly2Met1NumberOfCOX % 2) == 0 and (_ViaPoly2Met1NumberOfCOY % 2)==0:
                    _xycoordinatetmp = [_XYCoordinateOfViaPoly2Met1[0][0] - (_ViaPoly2Met1NumberOfCOX / 2 - 0.5) * _LengthViaPoly2Met1BtwCO + i * _LengthViaPoly2Met1BtwCO,
                                        _XYCoordinateOfViaPoly2Met1[0][1] - (_ViaPoly2Met1NumberOfCOY / 2 - 0.5 )*_LengthViaPoly2Met1BtwCO + j*_LengthViaPoly2Met1BtwCO]

                elif (_ViaPoly2Met1NumberOfCOX % 2) == 0 and (_ViaPoly2Met1NumberOfCOY % 2)==1:
                    _xycoordinatetmp = [_XYCoordinateOfViaPoly2Met1[0][0] - (_ViaPoly2Met1NumberOfCOX / 2 - 0.5) * _LengthViaPoly2Met1BtwCO + i * _LengthViaPoly2Met1BtwCO,
                                        _XYCoordinateOfViaPoly2Met1[0][1] - (_ViaPoly2Met1NumberOfCOY-1)/2  * _LengthViaPoly2Met1BtwCO +j*_LengthViaPoly2Met1BtwCO]

                elif (_ViaPoly2Met1NumberOfCOX % 2) == 1 and (_ViaPoly2Met1NumberOfCOY % 2)==0:
                    _xycoordinatetmp =[_XYCoordinateOfViaPoly2Met1[0][0] - (_ViaPoly2Met1NumberOfCOX -1) / 2  * _LengthViaPoly2Met1BtwCO + i * _LengthViaPoly2Met1BtwCO,
                                       _XYCoordinateOfViaPoly2Met1[0][1] - (_ViaPoly2Met1NumberOfCOY / 2 - 0.5 ) *_LengthViaPoly2Met1BtwCO + j*_LengthViaPoly2Met1BtwCO]

                elif (_ViaPoly2Met1NumberOfCOX % 2) == 1 and (_ViaPoly2Met1NumberOfCOY % 2)==1:
                    _xycoordinatetmp = [_XYCoordinateOfViaPoly2Met1[0][0] - (_ViaPoly2Met1NumberOfCOX -1) / 2 * _LengthViaPoly2Met1BtwCO + i * _LengthViaPoly2Met1BtwCO,
                                        _XYCoordinateOfViaPoly2Met1[0][1] - (_ViaPoly2Met1NumberOfCOY-1)/2 * _LengthViaPoly2Met1BtwCO +j*_LengthViaPoly2Met1BtwCO]
                tmp.append(_xycoordinatetmp)


        self._DesignParameter['_COLayer']['_XYCoordinates']=tmp




        del _DRCObj
        print('#########################################################################################################')
        print('                                    {}  ViaPoly2Met1 Calculation End                                    '.format(self._DesignParameter['_Name']['_Name']))
        print('#########################################################################################################')

if __name__=='__main__':
    ViaPoly2Met1Obj=_ViaPoly2Met1(_DesignParameter=None, _Name='ViaPoly2Met1')
    ViaPoly2Met1Obj._CalculateViaPoly2Met1DesignParameter(_ViaPoly2Met1NumberOfCOX=3, _ViaPoly2Met1NumberOfCOY=4 )
    ViaPoly2Met1Obj._UpdateDesignParameter2GDSStructure(_DesignParameterInDictionary=ViaPoly2Met1Obj._DesignParameter)
    testStreamFile=open('./testStreamFile.gds','wb')

    tmp=ViaPoly2Met1Obj._CreateGDSStream(ViaPoly2Met1Obj._DesignParameter['_GDSFile']['_GDSFile'])

    tmp.write_binary_gds_stream(testStreamFile)

    testStreamFile.close()
    

    print('##########################################################################################')