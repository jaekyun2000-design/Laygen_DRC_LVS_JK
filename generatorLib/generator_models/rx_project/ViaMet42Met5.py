from generatorLib import StickDiagram
from generatorLib import DesignParameters
from generatorLib import DRC

class _ViaMet42Met5(StickDiagram._StickDiagram):
    _ParametersForDesignCalculation= dict(_ViaMet42Met5NumberOfCOX=None, _ViaMet42Met5NumberOfCOY=None )


    def __init__(self, _DesignParameter=None, _Name=None):

        if _DesignParameter!=None:
            self._DesignParameter=_DesignParameter
        else :
            self._DesignParameter = dict(
                                                    _Met4Layer=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL4'][0],_Datatype=DesignParameters._LayerMapping['METAL4'][1], _XYCoordinates=[],_XWidth=400, _YWidth=400),
                                                    _Met5Layer=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL5'][0],_Datatype=DesignParameters._LayerMapping['METAL5'][1], _XYCoordinates=[],_XWidth=400, _YWidth=400),
                                                    _COLayer=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['VIA45'][0],_Datatype=DesignParameters._LayerMapping['VIA45'][1], _XYCoordinates=[],_XWidth=400, _YWidth=400),
                                                    _Name=self._NameDeclaration(_Name=_Name), _GDSFile=self._GDSObjDeclaration(_GDSFile=None)


                                                   )



        if _Name != None:
            self._DesignParameter['_Name']['_Name']=_Name
    # def __init__(self, _ViaMet42Met5DesignParameter=None, _ViaMet42Met5Name=None):
    #
    #     if _ViaMet42Met5DesignParameter!=None:
    #         self._ViaMet42Met5DesignParameter=_ViaMet42Met5DesignParameter
    #     else:
    #         self._ViaMet42Met5DesignParameter=dict(_Technology=[0, None, '065nm'],
    #                                                _XYCoordinateOfViaMet42Met5=[1, None, [0,0]],
    #
    #
    #
    #                                                _XYCoordinateOfMet2=[1, None, [[0,0]]], _XWidthOfMet2=[2, DesignParameters._LayerMapping['METAL2'][0],60], _YWidthOfMet2=[2, DesignParameters._LayerMapping['METAL2'][0],400] ,
    #                                                _XYCoordinateOfCO=[1, None, [[0,0]]], _WidthOfCO=[2, DesignParameters._LayerMapping['VIA23'][0],60],
    #                                                _XYCoordinateOfMet5=[1, None, [[0,0]]], _XWidthOfMet5=[2, DesignParameters._LayerMapping['METAL3'][0],90], _YWidthOfMet5=[2, DesignParameters._LayerMapping['METAL3'][0],430],
    #
    #                                                _ViaMet42Met5Name=[0, None,'ViaMet42Met5'], _ViaMet42Met5GDSStructure=[4,None,[]],
    #                                                )
    #
    #
    #
    #
    #     if _ViaMet42Met5Name != None:
    #         self._ViaMet42Met5DesignParameter['_ViaMet42Met5Name'][2]=_ViaMet42Met5Name
            

    def _CalculateViaMet42Met5DesignParameter(self, _ViaMet42Met5NumberOfCOX=None, _ViaMet42Met5NumberOfCOY=None ):
        print ('#########################################################################################################')
        print(('                                    {}  ViaMet42Met5 Calculation Start                                    '.format(self._DesignParameter['_Name']['_Name'])))
        print ('#########################################################################################################')

        ###############################################Check the number of CO On Via Contact###########################################################################################
        if _ViaMet42Met5NumberOfCOX ==0 or _ViaMet42Met5NumberOfCOY==0:
            print(('************************* Error occured in {} Design Parameter Calculation******************************'.format(self._DesignParameter['_Name']['_Name'])))
            if DesignParameters._DebugMode == 0:
                return 0
        ###############################################################################################################################################################################
        _DRCObj=DRC.DRC()
        _XYCoordinateOfViaMet42Met5 = [[0,0]]


        print ('#############################     Met5 Layer Calculation   ##############################################')
        _LengthViaMet42Met5BtwCO = _DRCObj._VIAxMinWidth + _DRCObj.DRCVIAxMinSpace(NumOfVIAxX=_ViaMet42Met5NumberOfCOX,NumOfVIAxY=_ViaMet42Met5NumberOfCOY )
        self._DesignParameter['_Met5Layer']['_XYCoordinates']=_XYCoordinateOfViaMet42Met5
        self._DesignParameter['_Met5Layer']['_XWidth']=_DRCObj._VIAxMinWidth + (_ViaMet42Met5NumberOfCOX - 1)* _LengthViaMet42Met5BtwCO+ 2 * max([_DRCObj._Metal1MinEnclosureVia12,_DRCObj._MetalxMinEnclosureCO2])
        self._DesignParameter['_Met5Layer']['_YWidth']=_DRCObj._VIAxMinWidth + (_ViaMet42Met5NumberOfCOY - 1)* _LengthViaMet42Met5BtwCO+ 2 * max([_DRCObj._Metal1MinEnclosureVia12,_DRCObj._MetalxMinEnclosureCO2])

        print ('#############################     Met2 Layer Calculation   ##############################################')
        _LengthViaMet42Met5BtwCO = _DRCObj._VIAxMinWidth + _DRCObj.DRCVIAxMinSpace(NumOfVIAxX=_ViaMet42Met5NumberOfCOX,NumOfVIAxY=_ViaMet42Met5NumberOfCOY )

        self._DesignParameter['_Met4Layer']['_XYCoordinates']=_XYCoordinateOfViaMet42Met5
        self._DesignParameter['_Met4Layer']['_XWidth'] = _DRCObj._VIAxMinWidth + (_ViaMet42Met5NumberOfCOX - 1)*  _LengthViaMet42Met5BtwCO+ 2 * max([_DRCObj._Metal1MinEnclosureVia12,_DRCObj._MetalxMinEnclosureCO2])
        self._DesignParameter['_Met4Layer']['_YWidth'] = _DRCObj._VIAxMinWidth + (_ViaMet42Met5NumberOfCOY - 1)*  _LengthViaMet42Met5BtwCO+ 2 * max([_DRCObj._Metal1MinEnclosureVia12,_DRCObj._MetalxMinEnclosureCO2])

        print ('#############################     Cont Layer Calculation   ##############################################')

        tmp=[]
        self._DesignParameter['_COLayer']['_XWidth'] = _DRCObj._VIAxMinWidth
        self._DesignParameter['_COLayer']['_YWidth'] = _DRCObj._VIAxMinWidth
        _LengthViaMet42Met5BtwCO = _DRCObj._VIAxMinWidth + _DRCObj.DRCVIAxMinSpace(NumOfVIAxX=_ViaMet42Met5NumberOfCOX,NumOfVIAxY=_ViaMet42Met5NumberOfCOY )
        for i in range(0, _ViaMet42Met5NumberOfCOX):
            for j in range(0, _ViaMet42Met5NumberOfCOY):

                if (_ViaMet42Met5NumberOfCOX % 2) == 0 and (_ViaMet42Met5NumberOfCOY % 2)==0:
                    _xycoordinatetmp = [_XYCoordinateOfViaMet42Met5[0][0] - (_ViaMet42Met5NumberOfCOX / 2 - 0.5) * _LengthViaMet42Met5BtwCO + i * _LengthViaMet42Met5BtwCO,
                                        _XYCoordinateOfViaMet42Met5[0][1] - (_ViaMet42Met5NumberOfCOY / 2 - 0.5 )*_LengthViaMet42Met5BtwCO + j*_LengthViaMet42Met5BtwCO]

                elif (_ViaMet42Met5NumberOfCOX % 2) == 0 and (_ViaMet42Met5NumberOfCOY % 2)==1:
                    _xycoordinatetmp = [_XYCoordinateOfViaMet42Met5[0][0] - (_ViaMet42Met5NumberOfCOX / 2 - 0.5) * _LengthViaMet42Met5BtwCO + i * _LengthViaMet42Met5BtwCO,
                                        _XYCoordinateOfViaMet42Met5[0][1] - (_ViaMet42Met5NumberOfCOY-1)/2 * _LengthViaMet42Met5BtwCO +j*_LengthViaMet42Met5BtwCO]

                elif (_ViaMet42Met5NumberOfCOX % 2) == 1 and (_ViaMet42Met5NumberOfCOY % 2)==0:
                    _xycoordinatetmp = [_XYCoordinateOfViaMet42Met5[0][0] - (_ViaMet42Met5NumberOfCOX -1) / 2  * _LengthViaMet42Met5BtwCO + i * _LengthViaMet42Met5BtwCO,
                                        _XYCoordinateOfViaMet42Met5[0][1] - (_ViaMet42Met5NumberOfCOY / 2 - 0.5 )*_LengthViaMet42Met5BtwCO + j*_LengthViaMet42Met5BtwCO]

                elif (_ViaMet42Met5NumberOfCOX % 2) == 1 and (_ViaMet42Met5NumberOfCOY % 2)==1:
                    _xycoordinatetmp = [_XYCoordinateOfViaMet42Met5[0][0] - (_ViaMet42Met5NumberOfCOX -1) / 2 * _LengthViaMet42Met5BtwCO + i * _LengthViaMet42Met5BtwCO,
                                        _XYCoordinateOfViaMet42Met5[0][1] - (_ViaMet42Met5NumberOfCOY-1)/2 * _LengthViaMet42Met5BtwCO +j*_LengthViaMet42Met5BtwCO]
                tmp.append(_xycoordinatetmp)


        self._DesignParameter['_COLayer']['_XYCoordinates']=tmp




        del _DRCObj
        print ('#########################################################################################################')
        print(('                                    {}  ViaMet42Met5 Calculation End                                    '.format(self._DesignParameter['_Name']['_Name'])))
        print ('#########################################################################################################')


    def _CalculateViaMet42Met5DesignParameterMinimumEnclosureX(self, _ViaMet42Met5NumberOfCOX=None, _ViaMet42Met5NumberOfCOY=None ):

        print ('#########################################################################################################')
        print(('                                    {}  ViaMet42Met5 Calculation Start                                    '.format(self._DesignParameter['_Name']['_Name'])))
        print ('#########################################################################################################')

        ###############################################Check the number of CO On Via Contact###########################################################################################
        if _ViaMet42Met5NumberOfCOX ==0 or _ViaMet42Met5NumberOfCOY==0:
            print(('************************* Error occured in {} Design Parameter Calculation******************************'.format(self._DesignParameter['_Name']['_Name'])))
            if DesignParameters._DebugMode == 0:
                return 0
        ###############################################################################################################################################################################
        _DRCObj=DRC.DRC()
        _XYCoordinateOfViaMet42Met5 = [[0,0]]


        print ('#############################     Met5 Layer Calculation   ##############################################')
        _LengthViaMet42Met5BtwCO = _DRCObj._VIAxMinWidth + _DRCObj.DRCVIAxMinSpace(NumOfVIAxX=_ViaMet42Met5NumberOfCOX,NumOfVIAxY=_ViaMet42Met5NumberOfCOY )
        self._DesignParameter['_Met5Layer']['_XYCoordinates']=_XYCoordinateOfViaMet42Met5
        self._DesignParameter['_Met5Layer']['_XWidth']=_DRCObj._VIAxMinWidth+ (_ViaMet42Met5NumberOfCOX - 1)* _LengthViaMet42Met5BtwCO+ 2 * max([_DRCObj._Metal1MinEnclosureVia1,_DRCObj._MetalxMinEnclosureCO])
        self._DesignParameter['_Met5Layer']['_YWidth']=_DRCObj._VIAxMinWidth + (_ViaMet42Met5NumberOfCOY - 1)* _LengthViaMet42Met5BtwCO+ 2 * max([_DRCObj._Metal1MinEnclosureVia12,_DRCObj._MetalxMinEnclosureCO2])

        print ('#############################     Met2 Layer Calculation   ##############################################')
        _LengthViaMet42Met5BtwCO = _DRCObj._VIAxMinWidth + _DRCObj.DRCVIAxMinSpace(NumOfVIAxX=_ViaMet42Met5NumberOfCOX,NumOfVIAxY=_ViaMet42Met5NumberOfCOY )

        self._DesignParameter['_Met4Layer']['_XYCoordinates']=_XYCoordinateOfViaMet42Met5
        self._DesignParameter['_Met4Layer']['_XWidth'] = _DRCObj._VIAxMinWidth + (_ViaMet42Met5NumberOfCOX - 1)*  _LengthViaMet42Met5BtwCO+ 2 * max([_DRCObj._Metal1MinEnclosureVia1,_DRCObj._MetalxMinEnclosureCO])

        self._DesignParameter['_Met4Layer']['_YWidth'] = _DRCObj._VIAxMinWidth + (_ViaMet42Met5NumberOfCOY - 1)*  _LengthViaMet42Met5BtwCO+ 2 * max([_DRCObj._Metal1MinEnclosureVia12,_DRCObj._MetalxMinEnclosureCO2])



        print ('#############################     Cont Layer Calculation   ##############################################')

        tmp=[]
        self._DesignParameter['_COLayer']['_XWidth'] = _DRCObj._VIAxMinWidth
        self._DesignParameter['_COLayer']['_YWidth'] = _DRCObj._VIAxMinWidth
        _LengthViaMet42Met5BtwCO = _DRCObj._VIAxMinWidth + _DRCObj.DRCVIAxMinSpace(NumOfVIAxX=_ViaMet42Met5NumberOfCOX,NumOfVIAxY=_ViaMet42Met5NumberOfCOY )
        for i in range(0, _ViaMet42Met5NumberOfCOX):
            for j in range(0, _ViaMet42Met5NumberOfCOY):

                if (_ViaMet42Met5NumberOfCOX % 2) == 0 and (_ViaMet42Met5NumberOfCOY % 2)==0:
                    _xycoordinatetmp = [_XYCoordinateOfViaMet42Met5[0][0] - (_ViaMet42Met5NumberOfCOX / 2 - 0.5) * _LengthViaMet42Met5BtwCO + i * _LengthViaMet42Met5BtwCO,
                                        _XYCoordinateOfViaMet42Met5[0][1] - (_ViaMet42Met5NumberOfCOY / 2 - 0.5 )*_LengthViaMet42Met5BtwCO + j*_LengthViaMet42Met5BtwCO]

                elif (_ViaMet42Met5NumberOfCOX % 2) == 0 and (_ViaMet42Met5NumberOfCOY % 2)==1:
                    _xycoordinatetmp = [_XYCoordinateOfViaMet42Met5[0][0] - (_ViaMet42Met5NumberOfCOX / 2 - 0.5) * _LengthViaMet42Met5BtwCO + i * _LengthViaMet42Met5BtwCO,
                                        _XYCoordinateOfViaMet42Met5[0][1] - (_ViaMet42Met5NumberOfCOY-1)/2 * _LengthViaMet42Met5BtwCO +j*_LengthViaMet42Met5BtwCO]

                elif (_ViaMet42Met5NumberOfCOX % 2) == 1 and (_ViaMet42Met5NumberOfCOY % 2)==0:
                    _xycoordinatetmp = [_XYCoordinateOfViaMet42Met5[0][0] - (_ViaMet42Met5NumberOfCOX -1) / 2  * _LengthViaMet42Met5BtwCO + i * _LengthViaMet42Met5BtwCO,
                                        _XYCoordinateOfViaMet42Met5[0][1] - (_ViaMet42Met5NumberOfCOY / 2 - 0.5 )*_LengthViaMet42Met5BtwCO + j*_LengthViaMet42Met5BtwCO]

                elif (_ViaMet42Met5NumberOfCOX % 2) == 1 and (_ViaMet42Met5NumberOfCOY % 2)==1:
                    _xycoordinatetmp = [_XYCoordinateOfViaMet42Met5[0][0] - (_ViaMet42Met5NumberOfCOX -1) / 2 * _LengthViaMet42Met5BtwCO + i * _LengthViaMet42Met5BtwCO,
                                        _XYCoordinateOfViaMet42Met5[0][1] - (_ViaMet42Met5NumberOfCOY-1)/2 * _LengthViaMet42Met5BtwCO +j*_LengthViaMet42Met5BtwCO]
                tmp.append(_xycoordinatetmp)


        self._DesignParameter['_COLayer']['_XYCoordinates']=tmp


        del _DRCObj
        print ('#########################################################################################################')
        print(('                                    {}  ViaMet42Met5 Calculation End                                    '.format(self._DesignParameter['_Name']['_Name'])))
        print ('#########################################################################################################')

    def _CalculateViaMet42Met5DesignParameterMinimumEnclosureY(self, _ViaMet42Met5NumberOfCOX=None, _ViaMet42Met5NumberOfCOY=None ):

        print ('#########################################################################################################')
        print(('                                    {}  ViaMet42Met5 Calculation Start                                    '.format(self._DesignParameter['_Name']['_Name'])))
        print ('#########################################################################################################')

        ###############################################Check the number of CO On Via Contact###########################################################################################
        if _ViaMet42Met5NumberOfCOX ==0 or _ViaMet42Met5NumberOfCOY==0:
            print(('************************* Error occured in {} Design Parameter Calculation******************************'.format(self._DesignParameter['_Name']['_Name'])))
            if DesignParameters._DebugMode == 0:
                return 0
        ###############################################################################################################################################################################
        _DRCObj=DRC.DRC()
        _XYCoordinateOfViaMet42Met5 = [[0,0]]


        print ('#############################     Met5 Layer Calculation   ##############################################')
        _LengthViaMet42Met5BtwCO = _DRCObj._VIAxMinWidth + _DRCObj.DRCVIAxMinSpace(NumOfVIAxX=_ViaMet42Met5NumberOfCOX,NumOfVIAxY=_ViaMet42Met5NumberOfCOY )
        self._DesignParameter['_Met5Layer']['_XYCoordinates']=_XYCoordinateOfViaMet42Met5
        self._DesignParameter['_Met5Layer']['_XWidth']=_DRCObj._VIAxMinWidth+ (_ViaMet42Met5NumberOfCOX - 1)* _LengthViaMet42Met5BtwCO+ 2 * max([_DRCObj._Metal1MinEnclosureVia12,_DRCObj._MetalxMinEnclosureCO2])
        self._DesignParameter['_Met5Layer']['_YWidth']=_DRCObj._VIAxMinWidth + (_ViaMet42Met5NumberOfCOY - 1)* _LengthViaMet42Met5BtwCO+ 2 * max([_DRCObj._Metal1MinEnclosureVia1,_DRCObj._MetalxMinEnclosureCO])

        print ('#############################     Met2 Layer Calculation   ##############################################')
        _LengthViaMet42Met5BtwCO = _DRCObj._VIAxMinWidth + _DRCObj.DRCVIAxMinSpace(NumOfVIAxX=_ViaMet42Met5NumberOfCOX,NumOfVIAxY=_ViaMet42Met5NumberOfCOY )

        self._DesignParameter['_Met4Layer']['_XYCoordinates']=_XYCoordinateOfViaMet42Met5
        self._DesignParameter['_Met4Layer']['_XWidth'] = _DRCObj._VIAxMinWidth + (_ViaMet42Met5NumberOfCOX - 1)*  _LengthViaMet42Met5BtwCO+ 2 * max([_DRCObj._Metal1MinEnclosureVia12,_DRCObj._MetalxMinEnclosureCO2])

        self._DesignParameter['_Met4Layer']['_YWidth'] = _DRCObj._VIAxMinWidth + (_ViaMet42Met5NumberOfCOY - 1)*  _LengthViaMet42Met5BtwCO+ 2 * max([_DRCObj._Metal1MinEnclosureVia1,_DRCObj._MetalxMinEnclosureCO])



        print ('#############################     Cont Layer Calculation   ##############################################')

        tmp=[]
        self._DesignParameter['_COLayer']['_XWidth'] = _DRCObj._VIAxMinWidth
        self._DesignParameter['_COLayer']['_YWidth'] = _DRCObj._VIAxMinWidth
        _LengthViaMet42Met5BtwCO = _DRCObj._VIAxMinWidth + _DRCObj.DRCVIAxMinSpace(NumOfVIAxX=_ViaMet42Met5NumberOfCOX,NumOfVIAxY=_ViaMet42Met5NumberOfCOY )
        for i in range(0, _ViaMet42Met5NumberOfCOX):
            for j in range(0, _ViaMet42Met5NumberOfCOY):

                if (_ViaMet42Met5NumberOfCOX % 2) == 0 and (_ViaMet42Met5NumberOfCOY % 2)==0:
                    _xycoordinatetmp = [_XYCoordinateOfViaMet42Met5[0][0] - (_ViaMet42Met5NumberOfCOX / 2 - 0.5) * _LengthViaMet42Met5BtwCO + i * _LengthViaMet42Met5BtwCO,
                                        _XYCoordinateOfViaMet42Met5[0][1] - (_ViaMet42Met5NumberOfCOY / 2 - 0.5 )*_LengthViaMet42Met5BtwCO + j*_LengthViaMet42Met5BtwCO]

                elif (_ViaMet42Met5NumberOfCOX % 2) == 0 and (_ViaMet42Met5NumberOfCOY % 2)==1:
                    _xycoordinatetmp = [_XYCoordinateOfViaMet42Met5[0][0] - (_ViaMet42Met5NumberOfCOX / 2 - 0.5) * _LengthViaMet42Met5BtwCO + i * _LengthViaMet42Met5BtwCO,
                                        _XYCoordinateOfViaMet42Met5[0][1] - (_ViaMet42Met5NumberOfCOY-1)/2 * _LengthViaMet42Met5BtwCO +j*_LengthViaMet42Met5BtwCO]

                elif (_ViaMet42Met5NumberOfCOX % 2) == 1 and (_ViaMet42Met5NumberOfCOY % 2)==0:
                    _xycoordinatetmp = [_XYCoordinateOfViaMet42Met5[0][0] - (_ViaMet42Met5NumberOfCOX -1) / 2  * _LengthViaMet42Met5BtwCO + i * _LengthViaMet42Met5BtwCO,
                                        _XYCoordinateOfViaMet42Met5[0][1] - (_ViaMet42Met5NumberOfCOY / 2 - 0.5 )*_LengthViaMet42Met5BtwCO + j*_LengthViaMet42Met5BtwCO]

                elif (_ViaMet42Met5NumberOfCOX % 2) == 1 and (_ViaMet42Met5NumberOfCOY % 2)==1:
                    _xycoordinatetmp = [_XYCoordinateOfViaMet42Met5[0][0] - (_ViaMet42Met5NumberOfCOX -1) / 2 * _LengthViaMet42Met5BtwCO + i * _LengthViaMet42Met5BtwCO,
                                        _XYCoordinateOfViaMet42Met5[0][1] - (_ViaMet42Met5NumberOfCOY-1)/2 * _LengthViaMet42Met5BtwCO +j*_LengthViaMet42Met5BtwCO]
                tmp.append(_xycoordinatetmp)


        self._DesignParameter['_COLayer']['_XYCoordinates']=tmp
        del _DRCObj
        print ('#########################################################################################################')
        print(('                                    {}  ViaMet42Met5 Calculation End                                    '.format(self._DesignParameter['_Name']['_Name'])))
        print ('#########################################################################################################')


    def _CalculateDesignParameterSameEnclosure(self, _ViaMet42Met5NumberOfCOX=None, _ViaMet42Met5NumberOfCOY=None):
        print ('#########################################################################################################')
        print(('                                    {}  ViaMet42Met5 Calculation Start                                    '.format(self._DesignParameter['_Name']['_Name'])))
        print ('#########################################################################################################')

        ###############################################Check the number of CO On Via Contact###########################################################################################
        if _ViaMet42Met5NumberOfCOX == 0 or _ViaMet42Met5NumberOfCOY == 0:
            print(('************************* Error occured in {} Design Parameter Calculation******************************'.format(self._DesignParameter['_Name']['_Name'])))
            if DesignParameters._DebugMode == 0:
                return 0
        ###############################################################################################################################################################################
        _DRCObj = DRC.DRC()
        _XYCoordinateOfViaMet42Met5 = [[0,0]]

        print ('#############################     Met5 Layer Calculation   ##############################################')
        _LengthViaMet42Met5BtwCO = _DRCObj._VIAxMinWidth + _DRCObj.DRCVIAxMinSpace(NumOfVIAxX=_ViaMet42Met5NumberOfCOX,NumOfVIAxY=_ViaMet42Met5NumberOfCOY)
        self._DesignParameter['_Met5Layer']['_XYCoordinates'] = _XYCoordinateOfViaMet42Met5
        self._DesignParameter['_Met5Layer']['_XWidth'] = _DRCObj._VIAxMinWidth + (_ViaMet42Met5NumberOfCOX - 1) * _LengthViaMet42Met5BtwCO + 2 * max([_DRCObj._Metal1MinEnclosureVia3,_DRCObj._MetalxMinEnclosureVia3])
        self._DesignParameter['_Met5Layer']['_YWidth'] = _DRCObj._VIAxMinWidth + (_ViaMet42Met5NumberOfCOY - 1) * _LengthViaMet42Met5BtwCO + 2 * max([_DRCObj._Metal1MinEnclosureVia3,_DRCObj._MetalxMinEnclosureVia3])

        print ('#############################     Met2 Layer Calculation   ##############################################')
        _LengthViaMet42Met5BtwCO = _DRCObj._VIAxMinWidth + _DRCObj.DRCVIAxMinSpace(NumOfVIAxX=_ViaMet42Met5NumberOfCOX,NumOfVIAxY=_ViaMet42Met5NumberOfCOY)
        self._DesignParameter['_Met4Layer']['_XYCoordinates'] = _XYCoordinateOfViaMet42Met5
        self._DesignParameter['_Met4Layer']['_XWidth'] = _DRCObj._VIAxMinWidth + (_ViaMet42Met5NumberOfCOX - 1) * _LengthViaMet42Met5BtwCO + 2 * max([_DRCObj._Metal1MinEnclosureVia3,_DRCObj._MetalxMinEnclosureVia3])
        self._DesignParameter['_Met4Layer']['_YWidth'] = _DRCObj._VIAxMinWidth + (_ViaMet42Met5NumberOfCOY - 1) * _LengthViaMet42Met5BtwCO + 2 * max([_DRCObj._Metal1MinEnclosureVia3,_DRCObj._MetalxMinEnclosureVia3])

        print ('#############################     Cont Layer Calculation   ##############################################')
        tmp = []
        self._DesignParameter['_COLayer']['_XWidth'] = _DRCObj._VIAxMinWidth
        self._DesignParameter['_COLayer']['_YWidth'] = _DRCObj._VIAxMinWidth
        _LengthViaMet42Met5BtwCO = _DRCObj._VIAxMinWidth + _DRCObj.DRCVIAxMinSpace(NumOfVIAxX=_ViaMet42Met5NumberOfCOX,NumOfVIAxY=_ViaMet42Met5NumberOfCOY)
        for i in range(0, _ViaMet42Met5NumberOfCOX):
            for j in range(0, _ViaMet42Met5NumberOfCOY):
                if (_ViaMet42Met5NumberOfCOX % 2) == 0 and (_ViaMet42Met5NumberOfCOY % 2)==0:
                    _xycoordinatetmp = [_XYCoordinateOfViaMet42Met5[0][0] - (_ViaMet42Met5NumberOfCOX / 2 - 0.5) * _LengthViaMet42Met5BtwCO + i * _LengthViaMet42Met5BtwCO,
                                        _XYCoordinateOfViaMet42Met5[0][1] - (_ViaMet42Met5NumberOfCOY / 2 - 0.5 )*_LengthViaMet42Met5BtwCO + j*_LengthViaMet42Met5BtwCO]
                elif (_ViaMet42Met5NumberOfCOX % 2) == 0 and (_ViaMet42Met5NumberOfCOY % 2)==1:
                    _xycoordinatetmp = [_XYCoordinateOfViaMet42Met5[0][0] - (_ViaMet42Met5NumberOfCOX / 2 - 0.5) * _LengthViaMet42Met5BtwCO + i * _LengthViaMet42Met5BtwCO,
                                        _XYCoordinateOfViaMet42Met5[0][1] - (_ViaMet42Met5NumberOfCOY-1)/2 * _LengthViaMet42Met5BtwCO +j*_LengthViaMet42Met5BtwCO]
                elif (_ViaMet42Met5NumberOfCOX % 2) == 1 and (_ViaMet42Met5NumberOfCOY % 2)==0:
                    _xycoordinatetmp = [_XYCoordinateOfViaMet42Met5[0][0] - (_ViaMet42Met5NumberOfCOX -1) / 2  * _LengthViaMet42Met5BtwCO + i * _LengthViaMet42Met5BtwCO,
                                        _XYCoordinateOfViaMet42Met5[0][1] - (_ViaMet42Met5NumberOfCOY / 2 - 0.5 )*_LengthViaMet42Met5BtwCO + j*_LengthViaMet42Met5BtwCO]
                elif (_ViaMet42Met5NumberOfCOX % 2) == 1 and (_ViaMet42Met5NumberOfCOY % 2)==1:
                    _xycoordinatetmp = [_XYCoordinateOfViaMet42Met5[0][0] - (_ViaMet42Met5NumberOfCOX -1) / 2 * _LengthViaMet42Met5BtwCO + i * _LengthViaMet42Met5BtwCO,
                                        _XYCoordinateOfViaMet42Met5[0][1] - (_ViaMet42Met5NumberOfCOY-1)/2 * _LengthViaMet42Met5BtwCO +j*_LengthViaMet42Met5BtwCO]
                tmp.append(_xycoordinatetmp)
        self._DesignParameter['_COLayer']['_XYCoordinates'] = tmp

        print ('#########################################################################################################')
        print(('                                    {}  ViaMet42Met5 Calculation End                                    '.format(self._DesignParameter['_Name']['_Name'])))
        print ('#########################################################################################################')



if __name__=='__main__':
    pass