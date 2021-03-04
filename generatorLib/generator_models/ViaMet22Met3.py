from generatorLib import StickDiagram
from generatorLib import DesignParameters
# import user_define_exceptions


from generatorLib import DRC

import ftplib
from ftplib import FTP
import base64


class _ViaMet22Met3(StickDiagram._StickDiagram):

    _ParametersForDesignCalculation= dict(_ViaMet22Met3NumberOfCOX=None, _ViaMet22Met3NumberOfCOY=None )
    def __init__(self, _DesignParameter=None, _Name=None):

        if _DesignParameter!=None:
            self._DesignParameter=_DesignParameter
        else :
            self._DesignParameter = dict(
                                                    _Met2Layer=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0],_Datatype=DesignParameters._LayerMapping['METAL2'][1], _XYCoordinates=[],_XWidth=400, _YWidth=400),
                                                    _Met3Layer=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0],_Datatype=DesignParameters._LayerMapping['METAL3'][1], _XYCoordinates=[],_XWidth=400, _YWidth=400),
                                                    _COLayer=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['VIA23'][0],_Datatype=DesignParameters._LayerMapping['VIA23'][1], _XYCoordinates=[],_XWidth=400, _YWidth=400),
                                                    _Name=self._NameDeclaration(_Name=_Name), _GDSFile=self._GDSObjDeclaration(_GDSFile=None)


                                                   )



        if _Name != None:
            self._DesignParameter['_Name']['_Name']=_Name
    # def __init__(self, _ViaMet22Met3DesignParameter=None, _ViaMet22Met3Name=None):
    #
    #     if _ViaMet22Met3DesignParameter!=None:
    #         self._ViaMet22Met3DesignParameter=_ViaMet22Met3DesignParameter
    #     else:
    #         self._ViaMet22Met3DesignParameter=dict(_Technology=[0, None, '065nm'],
    #                                                _XYCoordinateOfViaMet22Met3=[1, None, [0,0]],
    #
    #
    #
    #                                                _XYCoordinateOfMet2=[1, None, [[0,0]]], _XWidthOfMet2=[2, DesignParameters._LayerMapping['METAL2'][0],60], _YWidthOfMet2=[2, DesignParameters._LayerMapping['METAL2'][0],400] ,
    #                                                _XYCoordinateOfCO=[1, None, [[0,0]]], _WidthOfCO=[2, DesignParameters._LayerMapping['VIA23'][0],60],
    #                                                _XYCoordinateOfMet3=[1, None, [[0,0]]], _XWidthOfMet3=[2, DesignParameters._LayerMapping['METAL3'][0],90], _YWidthOfMet3=[2, DesignParameters._LayerMapping['METAL3'][0],430],
    #
    #                                                _ViaMet22Met3Name=[0, None,'ViaMet22Met3'], _ViaMet22Met3GDSStructure=[4,None,[]],
    #                                                )
    #
    #
    #
    #
    #     if _ViaMet22Met3Name != None:
    #         self._ViaMet22Met3DesignParameter['_ViaMet22Met3Name'][2]=_ViaMet22Met3Name
            

    def _CalculateViaMet22Met3DesignParameter(self, _ViaMet22Met3NumberOfCOX=None, _ViaMet22Met3NumberOfCOY=None ):
        print('#########################################################################################################')
        print('                                    {}  ViaMet22Met3 Calculation Start                                    '.format(self._DesignParameter['_Name']['_Name']))
        print('#########################################################################################################')

        ###############################################Check the number of CO On Via Contact###########################################################################################
        if _ViaMet22Met3NumberOfCOX ==0 or _ViaMet22Met3NumberOfCOY==0:
            print('************************* Error occured in {} Design Parameter Calculation******************************'.format(self._DesignParameter['_Name']['_Name']))
            if DesignParameters._DebugMode == 0:
                return 0
        ###############################################################################################################################################################################
        _DRCObj=DRC.DRC()
        _XYCoordinateOfViaMet22Met3 = [[0,0]]


        print('#############################     Met3 Layer Calculation   ##############################################')
        _LengthViaMet22Met3BtwCO = _DRCObj._VIAxMinWidth + _DRCObj.DRCVIAxMinSpace(NumOfVIAxX=_ViaMet22Met3NumberOfCOX,NumOfVIAxY=_ViaMet22Met3NumberOfCOY )
        self._DesignParameter['_Met3Layer']['_XYCoordinates']=_XYCoordinateOfViaMet22Met3
        self._DesignParameter['_Met3Layer']['_XWidth']=_DRCObj._VIAxMinWidth + (_ViaMet22Met3NumberOfCOX - 1)* _LengthViaMet22Met3BtwCO+ 2 * max([_DRCObj._Metal1MinEnclosureVia12,_DRCObj._MetalxMinEnclosureCO2])
        self._DesignParameter['_Met3Layer']['_YWidth']=_DRCObj._VIAxMinWidth + (_ViaMet22Met3NumberOfCOY - 1)* _LengthViaMet22Met3BtwCO+ 2 * max([_DRCObj._Metal1MinEnclosureVia12,_DRCObj._MetalxMinEnclosureCO2])

        print('#############################     Met2 Layer Calculation   ##############################################')
        _LengthViaMet22Met3BtwCO = _DRCObj._VIAxMinWidth + _DRCObj.DRCVIAxMinSpace(NumOfVIAxX=_ViaMet22Met3NumberOfCOX,NumOfVIAxY=_ViaMet22Met3NumberOfCOY )

        self._DesignParameter['_Met2Layer']['_XYCoordinates']=_XYCoordinateOfViaMet22Met3
        self._DesignParameter['_Met2Layer']['_XWidth'] = _DRCObj._VIAxMinWidth + (_ViaMet22Met3NumberOfCOX - 1)*  _LengthViaMet22Met3BtwCO+ 2 * max([_DRCObj._Metal1MinEnclosureVia12,_DRCObj._MetalxMinEnclosureCO2])
        self._DesignParameter['_Met2Layer']['_YWidth'] = _DRCObj._VIAxMinWidth + (_ViaMet22Met3NumberOfCOY - 1)*  _LengthViaMet22Met3BtwCO+ 2 * max([_DRCObj._Metal1MinEnclosureVia12,_DRCObj._MetalxMinEnclosureCO2])

        print('#############################     Cont Layer Calculation   ##############################################')

        tmp=[]
        self._DesignParameter['_COLayer']['_XWidth'] = _DRCObj._VIAxMinWidth
        self._DesignParameter['_COLayer']['_YWidth'] = _DRCObj._VIAxMinWidth
        _LengthViaMet22Met3BtwCO = _DRCObj._VIAxMinWidth + _DRCObj.DRCVIAxMinSpace(NumOfVIAxX=_ViaMet22Met3NumberOfCOX,NumOfVIAxY=_ViaMet22Met3NumberOfCOY )
        for i in range(0, _ViaMet22Met3NumberOfCOX):
            for j in range(0, _ViaMet22Met3NumberOfCOY):

                if (_ViaMet22Met3NumberOfCOX % 2) == 0 and (_ViaMet22Met3NumberOfCOY % 2)==0:
                    _xycoordinatetmp = [_XYCoordinateOfViaMet22Met3[0][0] - (_ViaMet22Met3NumberOfCOX / 2 - 0.5) * _LengthViaMet22Met3BtwCO + i * _LengthViaMet22Met3BtwCO,
                                        _XYCoordinateOfViaMet22Met3[0][1] - (_ViaMet22Met3NumberOfCOY / 2 - 0.5 )*_LengthViaMet22Met3BtwCO + j*_LengthViaMet22Met3BtwCO]

                elif (_ViaMet22Met3NumberOfCOX % 2) == 0 and (_ViaMet22Met3NumberOfCOY % 2)==1:
                    _xycoordinatetmp = [_XYCoordinateOfViaMet22Met3[0][0] - (_ViaMet22Met3NumberOfCOX / 2 - 0.5) * _LengthViaMet22Met3BtwCO + i * _LengthViaMet22Met3BtwCO,
                                        _XYCoordinateOfViaMet22Met3[0][1] - (_ViaMet22Met3NumberOfCOY-1)/2 * _LengthViaMet22Met3BtwCO +j*_LengthViaMet22Met3BtwCO]

                elif (_ViaMet22Met3NumberOfCOX % 2) == 1 and (_ViaMet22Met3NumberOfCOY % 2)==0:
                    _xycoordinatetmp = [_XYCoordinateOfViaMet22Met3[0][0] - (_ViaMet22Met3NumberOfCOX -1) / 2  * _LengthViaMet22Met3BtwCO + i * _LengthViaMet22Met3BtwCO,
                                        _XYCoordinateOfViaMet22Met3[0][1] - (_ViaMet22Met3NumberOfCOY / 2 - 0.5 )*_LengthViaMet22Met3BtwCO + j*_LengthViaMet22Met3BtwCO]

                elif (_ViaMet22Met3NumberOfCOX % 2) == 1 and (_ViaMet22Met3NumberOfCOY % 2)==1:
                    _xycoordinatetmp = [_XYCoordinateOfViaMet22Met3[0][0] - (_ViaMet22Met3NumberOfCOX -1) / 2 * _LengthViaMet22Met3BtwCO + i * _LengthViaMet22Met3BtwCO,
                                        _XYCoordinateOfViaMet22Met3[0][1] - (_ViaMet22Met3NumberOfCOY-1)/2 * _LengthViaMet22Met3BtwCO +j*_LengthViaMet22Met3BtwCO]
                tmp.append(_xycoordinatetmp)


        self._DesignParameter['_COLayer']['_XYCoordinates']=tmp




        del _DRCObj
        print('#########################################################################################################')
        print('                                    {}  ViaMet22Met3 Calculation End                                    '.format(self._DesignParameter['_Name']['_Name']))
        print('#########################################################################################################')


    def _CalculateViaMet22Met3DesignParameterMinimumEnclosureX(self, _ViaMet22Met3NumberOfCOX=None, _ViaMet22Met3NumberOfCOY=None ):

        print('#########################################################################################################')
        print('                                    {}  ViaMet22Met3 Calculation Start                                    '.format(self._DesignParameter['_Name']['_Name']))
        print('#########################################################################################################')

        ###############################################Check the number of CO On Via Contact###########################################################################################
        if _ViaMet22Met3NumberOfCOX ==0 or _ViaMet22Met3NumberOfCOY==0:
            print('************************* Error occured in {} Design Parameter Calculation******************************'.format(self._DesignParameter['_Name']['_Name']))
            if DesignParameters._DebugMode == 0:
                return 0
        ###############################################################################################################################################################################
        _DRCObj=DRC.DRC()
        _XYCoordinateOfViaMet22Met3 = [[0,0]]


        print('#############################     Met3 Layer Calculation   ##############################################')
        _LengthViaMet22Met3BtwCO = _DRCObj._VIAxMinWidth + _DRCObj.DRCVIAxMinSpace(NumOfVIAxX=_ViaMet22Met3NumberOfCOX,NumOfVIAxY=_ViaMet22Met3NumberOfCOY )
        self._DesignParameter['_Met3Layer']['_XYCoordinates']=_XYCoordinateOfViaMet22Met3
        self._DesignParameter['_Met3Layer']['_XWidth']=_DRCObj._VIAxMinWidth+ (_ViaMet22Met3NumberOfCOX - 1)* _LengthViaMet22Met3BtwCO+ 2 * max([_DRCObj._Metal1MinEnclosureVia1,_DRCObj._MetalxMinEnclosureCO])
        self._DesignParameter['_Met3Layer']['_YWidth']=_DRCObj._VIAxMinWidth + (_ViaMet22Met3NumberOfCOY - 1)* _LengthViaMet22Met3BtwCO+ 2 * max([_DRCObj._Metal1MinEnclosureVia12,_DRCObj._MetalxMinEnclosureCO2])

        print('#############################     Met2 Layer Calculation   ##############################################')
        _LengthViaMet22Met3BtwCO = _DRCObj._VIAxMinWidth + _DRCObj.DRCVIAxMinSpace(NumOfVIAxX=_ViaMet22Met3NumberOfCOX,NumOfVIAxY=_ViaMet22Met3NumberOfCOY )

        self._DesignParameter['_Met2Layer']['_XYCoordinates']=_XYCoordinateOfViaMet22Met3
        self._DesignParameter['_Met2Layer']['_XWidth'] = _DRCObj._VIAxMinWidth + (_ViaMet22Met3NumberOfCOX - 1)*  _LengthViaMet22Met3BtwCO+ 2 * max([_DRCObj._Metal1MinEnclosureVia1,_DRCObj._MetalxMinEnclosureCO])

        self._DesignParameter['_Met2Layer']['_YWidth'] = _DRCObj._VIAxMinWidth + (_ViaMet22Met3NumberOfCOY - 1)*  _LengthViaMet22Met3BtwCO+ 2 * max([_DRCObj._Metal1MinEnclosureVia12,_DRCObj._MetalxMinEnclosureCO2])



        print('#############################     Cont Layer Calculation   ##############################################')

        tmp=[]
        self._DesignParameter['_COLayer']['_XWidth'] = _DRCObj._VIAxMinWidth
        self._DesignParameter['_COLayer']['_YWidth'] = _DRCObj._VIAxMinWidth
        _LengthViaMet22Met3BtwCO = _DRCObj._VIAxMinWidth + _DRCObj.DRCVIAxMinSpace(NumOfVIAxX=_ViaMet22Met3NumberOfCOX,NumOfVIAxY=_ViaMet22Met3NumberOfCOY )
        for i in range(0, _ViaMet22Met3NumberOfCOX):
            for j in range(0, _ViaMet22Met3NumberOfCOY):

                if (_ViaMet22Met3NumberOfCOX % 2) == 0 and (_ViaMet22Met3NumberOfCOY % 2)==0:
                    _xycoordinatetmp = [_XYCoordinateOfViaMet22Met3[0][0] - (_ViaMet22Met3NumberOfCOX / 2 - 0.5) * _LengthViaMet22Met3BtwCO + i * _LengthViaMet22Met3BtwCO,
                                        _XYCoordinateOfViaMet22Met3[0][1] - (_ViaMet22Met3NumberOfCOY / 2 - 0.5 )*_LengthViaMet22Met3BtwCO + j*_LengthViaMet22Met3BtwCO]

                elif (_ViaMet22Met3NumberOfCOX % 2) == 0 and (_ViaMet22Met3NumberOfCOY % 2)==1:
                    _xycoordinatetmp = [_XYCoordinateOfViaMet22Met3[0][0] - (_ViaMet22Met3NumberOfCOX / 2 - 0.5) * _LengthViaMet22Met3BtwCO + i * _LengthViaMet22Met3BtwCO,
                                        _XYCoordinateOfViaMet22Met3[0][1] - (_ViaMet22Met3NumberOfCOY-1)/2 * _LengthViaMet22Met3BtwCO +j*_LengthViaMet22Met3BtwCO]

                elif (_ViaMet22Met3NumberOfCOX % 2) == 1 and (_ViaMet22Met3NumberOfCOY % 2)==0:
                    _xycoordinatetmp = [_XYCoordinateOfViaMet22Met3[0][0] - (_ViaMet22Met3NumberOfCOX -1) / 2  * _LengthViaMet22Met3BtwCO + i * _LengthViaMet22Met3BtwCO,
                                        _XYCoordinateOfViaMet22Met3[0][1] - (_ViaMet22Met3NumberOfCOY / 2 - 0.5 )*_LengthViaMet22Met3BtwCO + j*_LengthViaMet22Met3BtwCO]

                elif (_ViaMet22Met3NumberOfCOX % 2) == 1 and (_ViaMet22Met3NumberOfCOY % 2)==1:
                    _xycoordinatetmp = [_XYCoordinateOfViaMet22Met3[0][0] - (_ViaMet22Met3NumberOfCOX -1) / 2 * _LengthViaMet22Met3BtwCO + i * _LengthViaMet22Met3BtwCO,
                                        _XYCoordinateOfViaMet22Met3[0][1] - (_ViaMet22Met3NumberOfCOY-1)/2 * _LengthViaMet22Met3BtwCO +j*_LengthViaMet22Met3BtwCO]
                tmp.append(_xycoordinatetmp)


        self._DesignParameter['_COLayer']['_XYCoordinates']=tmp


        del _DRCObj
        print('#########################################################################################################')
        print('                                    {}  ViaMet22Met3 Calculation End                                    '.format(self._DesignParameter['_Name']['_Name']))
        print('#########################################################################################################')

    def _CalculateViaMet22Met3DesignParameterMinimumEnclosureY(self, _ViaMet22Met3NumberOfCOX=None, _ViaMet22Met3NumberOfCOY=None ):

        print('#########################################################################################################')
        print('                                    {}  ViaMet22Met3 Calculation Start                                    '.format(self._DesignParameter['_Name']['_Name']))
        print('#########################################################################################################')

        ###############################################Check the number of CO On Via Contact###########################################################################################
        if _ViaMet22Met3NumberOfCOX ==0 or _ViaMet22Met3NumberOfCOY==0:
            print('************************* Error occured in {} Design Parameter Calculation******************************'.format(self._DesignParameter['_Name']['_Name']))
            if DesignParameters._DebugMode == 0:
                return 0
        ###############################################################################################################################################################################
        _DRCObj=DRC.DRC()
        _XYCoordinateOfViaMet22Met3 = [[0,0]]


        print('#############################     Met3 Layer Calculation   ##############################################')
        _LengthViaMet22Met3BtwCO = _DRCObj._VIAxMinWidth + _DRCObj.DRCVIAxMinSpace(NumOfVIAxX=_ViaMet22Met3NumberOfCOX,NumOfVIAxY=_ViaMet22Met3NumberOfCOY )
        self._DesignParameter['_Met3Layer']['_XYCoordinates']=_XYCoordinateOfViaMet22Met3
        self._DesignParameter['_Met3Layer']['_XWidth']=_DRCObj._VIAxMinWidth+ (_ViaMet22Met3NumberOfCOX - 1)* _LengthViaMet22Met3BtwCO+ 2 * max([_DRCObj._Metal1MinEnclosureVia12,_DRCObj._MetalxMinEnclosureCO2])
        self._DesignParameter['_Met3Layer']['_YWidth']=_DRCObj._VIAxMinWidth + (_ViaMet22Met3NumberOfCOY - 1)* _LengthViaMet22Met3BtwCO+ 2 * max([_DRCObj._Metal1MinEnclosureVia1,_DRCObj._MetalxMinEnclosureCO])

        print('#############################     Met2 Layer Calculation   ##############################################')
        _LengthViaMet22Met3BtwCO = _DRCObj._VIAxMinWidth + _DRCObj.DRCVIAxMinSpace(NumOfVIAxX=_ViaMet22Met3NumberOfCOX,NumOfVIAxY=_ViaMet22Met3NumberOfCOY )

        self._DesignParameter['_Met2Layer']['_XYCoordinates']=_XYCoordinateOfViaMet22Met3
        self._DesignParameter['_Met2Layer']['_XWidth'] = _DRCObj._VIAxMinWidth + (_ViaMet22Met3NumberOfCOX - 1)*  _LengthViaMet22Met3BtwCO+ 2 * max([_DRCObj._Metal1MinEnclosureVia12,_DRCObj._MetalxMinEnclosureCO2])

        self._DesignParameter['_Met2Layer']['_YWidth'] = _DRCObj._VIAxMinWidth + (_ViaMet22Met3NumberOfCOY - 1)*  _LengthViaMet22Met3BtwCO+ 2 * max([_DRCObj._Metal1MinEnclosureVia1,_DRCObj._MetalxMinEnclosureCO])



        print('#############################     Cont Layer Calculation   ##############################################')

        tmp=[]
        self._DesignParameter['_COLayer']['_XWidth'] = _DRCObj._VIAxMinWidth
        self._DesignParameter['_COLayer']['_YWidth'] = _DRCObj._VIAxMinWidth
        _LengthViaMet22Met3BtwCO = _DRCObj._VIAxMinWidth + _DRCObj.DRCVIAxMinSpace(NumOfVIAxX=_ViaMet22Met3NumberOfCOX,NumOfVIAxY=_ViaMet22Met3NumberOfCOY )
        for i in range(0, _ViaMet22Met3NumberOfCOX):
            for j in range(0, _ViaMet22Met3NumberOfCOY):

                if (_ViaMet22Met3NumberOfCOX % 2) == 0 and (_ViaMet22Met3NumberOfCOY % 2)==0:
                    _xycoordinatetmp = [_XYCoordinateOfViaMet22Met3[0][0] - (_ViaMet22Met3NumberOfCOX / 2 - 0.5) * _LengthViaMet22Met3BtwCO + i * _LengthViaMet22Met3BtwCO,
                                        _XYCoordinateOfViaMet22Met3[0][1] - (_ViaMet22Met3NumberOfCOY / 2 - 0.5 )*_LengthViaMet22Met3BtwCO + j*_LengthViaMet22Met3BtwCO]

                elif (_ViaMet22Met3NumberOfCOX % 2) == 0 and (_ViaMet22Met3NumberOfCOY % 2)==1:
                    _xycoordinatetmp = [_XYCoordinateOfViaMet22Met3[0][0] - (_ViaMet22Met3NumberOfCOX / 2 - 0.5) * _LengthViaMet22Met3BtwCO + i * _LengthViaMet22Met3BtwCO,
                                        _XYCoordinateOfViaMet22Met3[0][1] - (_ViaMet22Met3NumberOfCOY-1)/2 * _LengthViaMet22Met3BtwCO +j*_LengthViaMet22Met3BtwCO]

                elif (_ViaMet22Met3NumberOfCOX % 2) == 1 and (_ViaMet22Met3NumberOfCOY % 2)==0:
                    _xycoordinatetmp = [_XYCoordinateOfViaMet22Met3[0][0] - (_ViaMet22Met3NumberOfCOX -1) / 2  * _LengthViaMet22Met3BtwCO + i * _LengthViaMet22Met3BtwCO,
                                        _XYCoordinateOfViaMet22Met3[0][1] - (_ViaMet22Met3NumberOfCOY / 2 - 0.5 )*_LengthViaMet22Met3BtwCO + j*_LengthViaMet22Met3BtwCO]

                elif (_ViaMet22Met3NumberOfCOX % 2) == 1 and (_ViaMet22Met3NumberOfCOY % 2)==1:
                    _xycoordinatetmp = [_XYCoordinateOfViaMet22Met3[0][0] - (_ViaMet22Met3NumberOfCOX -1) / 2 * _LengthViaMet22Met3BtwCO + i * _LengthViaMet22Met3BtwCO,
                                        _XYCoordinateOfViaMet22Met3[0][1] - (_ViaMet22Met3NumberOfCOY-1)/2 * _LengthViaMet22Met3BtwCO +j*_LengthViaMet22Met3BtwCO]
                tmp.append(_xycoordinatetmp)


        self._DesignParameter['_COLayer']['_XYCoordinates']=tmp
        del _DRCObj
        print('#########################################################################################################')
        print('                                    {}  ViaMet22Met3 Calculation End                                    '.format(self._DesignParameter['_Name']['_Name']))
        print('#########################################################################################################')

if __name__=='__main__':
    ViaMet22Met3Obj1=_ViaMet22Met3(_DesignParameter=None, _Name='ViaMet22Met3test1')
    ViaMet22Met3Obj1._CalculateViaMet22Met3DesignParameter(_ViaMet22Met3NumberOfCOX=3, _ViaMet22Met3NumberOfCOY=4 )
    ViaMet22Met3Obj2=_ViaMet22Met3(_DesignParameter=None, _Name='ViaMet22Met3test2')
    ViaMet22Met3Obj2._CalculateViaMet22Met3DesignParameterMinimumEnclosureY(_ViaMet22Met3NumberOfCOX=3, _ViaMet22Met3NumberOfCOY=4 )
    ViaMet22Met3Obj3=_ViaMet22Met3(_DesignParameter=None, _Name='ViaMet22Met3test3')
    ViaMet22Met3Obj3._CalculateViaMet22Met3DesignParameterMinimumEnclosureX(_ViaMet22Met3NumberOfCOX=3, _ViaMet22Met3NumberOfCOY=4 )
    #ViaMet22Met3Obj=_ViaMet22Met3(_ViaMet22Met3DesignParameter=DesignParameters.ViaMet22Met3DesignParameter, _ViaMet22Met3Name='ViaMet22Met32test')
    #ViaMet22Met3Obj=_ViaMet22Met3(_Technology=DesignParameters._Technology, _XYCoordinatePbody=[0,0], _NumberOfPbodyCO=2, _WidthXPbodyOD=890, _WidthYPbodyOD=420, _WidthXPbodyNP=1250, _WidthYPbodyNP=780, _WidthPbodyCO=220, _LengthPbodyBtwCO=470, _WidthXPbodyMet3=810, _WidthYPbodyMet1=340, _PbodyName='ViaMet22Met3')
    ViaMet22Met3Obj1._UpdateDesignParameter2GDSStructure(_DesignParameterInDictionary=ViaMet22Met3Obj1._DesignParameter)
    ViaMet22Met3Obj2._UpdateDesignParameter2GDSStructure(_DesignParameterInDictionary=ViaMet22Met3Obj2._DesignParameter)
    ViaMet22Met3Obj3._UpdateDesignParameter2GDSStructure(_DesignParameterInDictionary=ViaMet22Met3Obj3._DesignParameter)

    testStreamFile=open('./testStreamFile1.gds','wb')

    tmp1=ViaMet22Met3Obj1._CreateGDSStream(ViaMet22Met3Obj1._DesignParameter['_GDSFile']['_GDSFile'])

    tmp1.write_binary_gds_stream(testStreamFile)
    testStreamFile=open('./testStreamFile2.gds','wb')

    tmp2=ViaMet22Met3Obj2._CreateGDSStream(ViaMet22Met3Obj2._DesignParameter['_GDSFile']['_GDSFile'])

    tmp2.write_binary_gds_stream(testStreamFile)

    testStreamFile=open('./testStreamFile3.gds','wb')

    tmp3=ViaMet22Met3Obj3._CreateGDSStream(ViaMet22Met3Obj3._DesignParameter['_GDSFile']['_GDSFile'])

    tmp3.write_binary_gds_stream(testStreamFile)

    testStreamFile.close()
    print('###############open ftp connection & update gds file to cadence server###################')
    ftp_cadence_server=ftplib.FTP('141.223.86.109')
    ftp_cadence_server.login(base64.b64decode('YWxlY25ldzE='),base64.b64decode('NzNoazNhYWs='))
    if DesignParameters._Technology =='065nm':
        ftp_cadence_server.cwd('/home/alecnew1/OPUS/design_automation')
    elif DesignParameters._Technology =='180nm':
        ftp_cadence_server.cwd('/home/alecnew1/OPUS/DesignAutomationTSMC018')
    elif DesignParameters._Technology =='045nm':
        ftp_cadence_server.cwd('/home/alecnew1/OPUS/DesignAutomationTSMC45')
    print(ftp_cadence_server.pwd())
    testStreamFile=open('./testStreamFile1.gds','rb')
    ftp_cadence_server.storbinary('STOR testStreamFile1.gds', testStreamFile)
    testStreamFile.close()
    testStreamFile=open('./testStreamFile2.gds','rb')
    ftp_cadence_server.storbinary('STOR testStreamFile2.gds', testStreamFile)
    testStreamFile.close()
    testStreamFile=open('./testStreamFile3.gds','rb')
    ftp_cadence_server.storbinary('STOR testStreamFile3.gds', testStreamFile)
    testStreamFile.close()
    print('close ftp connection')
    ftp_cadence_server.quit()
    testStreamFile.close()

    print('##########################################################################################')