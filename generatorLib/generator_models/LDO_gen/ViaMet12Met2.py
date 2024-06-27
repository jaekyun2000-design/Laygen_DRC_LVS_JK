from generatorLib import StickDiagram
from generatorLib import DesignParameters
from generatorLib import DRC


class _ViaMet12Met2(StickDiagram._StickDiagram):
    _ParametersForDesignCalculation= dict(_ViaMet12Met2NumberOfCOX=None, _ViaMet12Met2NumberOfCOY=None )
    def __init__(self, _DesignParameter=None, _Name=None):

        if _DesignParameter!=None:
            self._DesignParameter=_DesignParameter
        else :
            self._DesignParameter = dict(
                                                    _Met2Layer=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0],_Datatype=DesignParameters._LayerMapping['METAL2'][1], _XYCoordinates=[],_XWidth=400, _YWidth=400),
                                                    _Met1Layer=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0],_Datatype=DesignParameters._LayerMapping['METAL1'][1], _XYCoordinates=[],_XWidth=400, _YWidth=400),
                                                    _COLayer=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['VIA12'][0],_Datatype=DesignParameters._LayerMapping['VIA12'][1], _XYCoordinates=[],_XWidth=400, _YWidth=400),
                                                    _Name=self._NameDeclaration(_Name=_Name), _GDSFile=self._GDSObjDeclaration(_GDSFile=None)


                                                   )



        if _Name != None:
            self._DesignParameter['_Name']['_Name']=_Name


    def _CalculateViaMet12Met2DesignParameter(self, _ViaMet12Met2NumberOfCOX=None, _ViaMet12Met2NumberOfCOY=None ):
        """
            Via Spacing:
                - x,y-direction same spacing.
                - _DRCObj.DRCVIAxMinSpace(NumX, NumY)
            Enclosure:
                - opposite side min enclosure(~~Via12, ~~CO2)
                - Met1, Metx(Met2) 중 max enclosure value를 모든 metal에 적용.
                - max([_DRCObj._Metal1MinEnclosureVia12, _DRCObj._MetalxMinEnclosureCO2])

        """
        print ('#########################################################################################################')
        print(('                                    {}  ViaMet12Met2 Calculation Start                                    '.format(self._DesignParameter['_Name']['_Name'])))
        print ('#########################################################################################################')

        ###############################################Check the number of CO On Via Contact###########################################################################################
        if _ViaMet12Met2NumberOfCOX ==0 or _ViaMet12Met2NumberOfCOY==0:
            print(('************************* Error occured in {} Design Parameter Calculation******************************'.format(self._DesignParameter['_Name']['_Name'])))
            if DesignParameters._DebugMode == 0:
                return 0
        ###############################################################################################################################################################################
        _DRCObj=DRC.DRC()
        _XYCoordinateOfViaMet12Met2 = [[0,0]]


        print ('#############################     Met1 Layer Calculation   ##############################################')
        _LengthViaMet12Met2BtwCO = _DRCObj._VIAxMinWidth + _DRCObj.DRCVIAxMinSpace(NumOfVIAxX=_ViaMet12Met2NumberOfCOX,NumOfVIAxY=_ViaMet12Met2NumberOfCOY )
        self._DesignParameter['_Met1Layer']['_XYCoordinates']=_XYCoordinateOfViaMet12Met2
        self._DesignParameter['_Met1Layer']['_XWidth']=_DRCObj._VIAxMinWidth + (_ViaMet12Met2NumberOfCOX - 1)* _LengthViaMet12Met2BtwCO+ 2 * max([_DRCObj._Metal1MinEnclosureVia12,_DRCObj._MetalxMinEnclosureCO2])
        self._DesignParameter['_Met1Layer']['_YWidth']=_DRCObj._VIAxMinWidth + (_ViaMet12Met2NumberOfCOY - 1)* _LengthViaMet12Met2BtwCO+ 2 * max([_DRCObj._Metal1MinEnclosureVia12,_DRCObj._MetalxMinEnclosureCO2])

        print ('#############################     Met2 Layer Calculation   ##############################################')
        _LengthViaMet12Met2BtwCO = _DRCObj._VIAxMinWidth + _DRCObj.DRCVIAxMinSpace(NumOfVIAxX=_ViaMet12Met2NumberOfCOX,NumOfVIAxY=_ViaMet12Met2NumberOfCOY )

        self._DesignParameter['_Met2Layer']['_XYCoordinates']=_XYCoordinateOfViaMet12Met2
        self._DesignParameter['_Met2Layer']['_XWidth'] = _DRCObj._VIAxMinWidth + (_ViaMet12Met2NumberOfCOX - 1)*  _LengthViaMet12Met2BtwCO+ 2 * max([_DRCObj._Metal1MinEnclosureVia12,_DRCObj._MetalxMinEnclosureCO2])
        self._DesignParameter['_Met2Layer']['_YWidth'] = _DRCObj._VIAxMinWidth + (_ViaMet12Met2NumberOfCOY - 1)*  _LengthViaMet12Met2BtwCO+ 2 * max([_DRCObj._Metal1MinEnclosureVia12,_DRCObj._MetalxMinEnclosureCO2])

        print ('#############################     Cont Layer Calculation   ##############################################')
        tmp=[]
        self._DesignParameter['_COLayer']['_XWidth'] = _DRCObj._VIAxMinWidth
        self._DesignParameter['_COLayer']['_YWidth'] = _DRCObj._VIAxMinWidth
        _LengthViaMet12Met2BtwCO = _DRCObj._VIAxMinWidth + _DRCObj.DRCVIAxMinSpace(NumOfVIAxX=_ViaMet12Met2NumberOfCOX,NumOfVIAxY=_ViaMet12Met2NumberOfCOY )
        for i in range(0, _ViaMet12Met2NumberOfCOX):
            for j in range(0, _ViaMet12Met2NumberOfCOY):

                if (_ViaMet12Met2NumberOfCOX % 2) == 0 and (_ViaMet12Met2NumberOfCOY % 2)==0:
                    _xycoordinatetmp = [_XYCoordinateOfViaMet12Met2[0][0] - (_ViaMet12Met2NumberOfCOX / 2 - 0.5) * _LengthViaMet12Met2BtwCO + i * _LengthViaMet12Met2BtwCO,
                                        _XYCoordinateOfViaMet12Met2[0][1] - (_ViaMet12Met2NumberOfCOY / 2 - 0.5 )*_LengthViaMet12Met2BtwCO + j*_LengthViaMet12Met2BtwCO]

                elif (_ViaMet12Met2NumberOfCOX % 2) == 0 and (_ViaMet12Met2NumberOfCOY % 2)==1:
                    _xycoordinatetmp = [_XYCoordinateOfViaMet12Met2[0][0] - (_ViaMet12Met2NumberOfCOX / 2 - 0.5) * _LengthViaMet12Met2BtwCO + i * _LengthViaMet12Met2BtwCO,
                                        _XYCoordinateOfViaMet12Met2[0][1] - (_ViaMet12Met2NumberOfCOY-1)/2 * _LengthViaMet12Met2BtwCO +j*_LengthViaMet12Met2BtwCO]

                elif (_ViaMet12Met2NumberOfCOX % 2) == 1 and (_ViaMet12Met2NumberOfCOY % 2)==0:
                    _xycoordinatetmp = [_XYCoordinateOfViaMet12Met2[0][0] - (_ViaMet12Met2NumberOfCOX -1) / 2  * _LengthViaMet12Met2BtwCO + i * _LengthViaMet12Met2BtwCO,
                                        _XYCoordinateOfViaMet12Met2[0][1] - (_ViaMet12Met2NumberOfCOY / 2 - 0.5 )*_LengthViaMet12Met2BtwCO + j*_LengthViaMet12Met2BtwCO]

                elif (_ViaMet12Met2NumberOfCOX % 2) == 1 and (_ViaMet12Met2NumberOfCOY % 2)==1:
                    _xycoordinatetmp = [_XYCoordinateOfViaMet12Met2[0][0] - (_ViaMet12Met2NumberOfCOX -1) / 2 * _LengthViaMet12Met2BtwCO + i * _LengthViaMet12Met2BtwCO,
                                        _XYCoordinateOfViaMet12Met2[0][1] - (_ViaMet12Met2NumberOfCOY-1)/2 * _LengthViaMet12Met2BtwCO +j*_LengthViaMet12Met2BtwCO]
                tmp.append(_xycoordinatetmp)

        self._DesignParameter['_COLayer']['_XYCoordinates']=tmp




        del _DRCObj
        print ('#########################################################################################################')
        print(('                                    {}  ViaMet12Met2 Calculation End                                    '.format(self._DesignParameter['_Name']['_Name'])))
        print ('#########################################################################################################')


    def _CalculateViaMet12Met2DesignParameterMinimumEnclosureX(self, _ViaMet12Met2NumberOfCOX=None, _ViaMet12Met2NumberOfCOY=None ):
        """
            Via Spacing:
                - x,y-direction same spacing.
                - _DRCObj.DRCVIAxMinSpace(NumX, NumY)
            Enclosure:
                - x(horizontal): min enclosure(drc.~~Via1, drc.~~CO)
                - y(vertical): opposite side min enclosure(drc.~~Via12, drc.~~CO2)
                - 각 x,y direction에서 Met1, Metx(Met2) 중 max enclosure value를 모든 metal에 적용.

        """
        print ('#########################################################################################################')
        print(('                                    {}  ViaMet12Met2 Calculation Start                                    '.format(self._DesignParameter['_Name']['_Name'])))
        print ('#########################################################################################################')

        ###############################################Check the number of CO On Via Contact###########################################################################################
        if _ViaMet12Met2NumberOfCOX ==0 or _ViaMet12Met2NumberOfCOY==0:
            print(('************************* Error occured in {} Design Parameter Calculation******************************'.format(self._DesignParameter['_Name']['_Name'])))
            if DesignParameters._DebugMode == 0:
                return 0
        ###############################################################################################################################################################################
        _DRCObj=DRC.DRC()
        _XYCoordinateOfViaMet12Met2 = [[0,0]]


        print ('#############################     Met1 Layer Calculation   ##############################################')
        _LengthViaMet12Met2BtwCO = _DRCObj._VIAxMinWidth + _DRCObj.DRCVIAxMinSpace(NumOfVIAxX=_ViaMet12Met2NumberOfCOX,NumOfVIAxY=_ViaMet12Met2NumberOfCOY )
        self._DesignParameter['_Met1Layer']['_XYCoordinates']=_XYCoordinateOfViaMet12Met2
        self._DesignParameter['_Met1Layer']['_XWidth']=_DRCObj._VIAxMinWidth + (_ViaMet12Met2NumberOfCOX - 1)* _LengthViaMet12Met2BtwCO+ 2 * max([_DRCObj._Metal1MinEnclosureVia1,_DRCObj._MetalxMinEnclosureCO])
        self._DesignParameter['_Met1Layer']['_YWidth']=_DRCObj._VIAxMinWidth + (_ViaMet12Met2NumberOfCOY - 1)* _LengthViaMet12Met2BtwCO+ 2 * max([_DRCObj._Metal1MinEnclosureVia12,_DRCObj._MetalxMinEnclosureCO2])

        print ('#############################     Met2 Layer Calculation   ##############################################')
        _LengthViaMet12Met2BtwCO = _DRCObj._VIAxMinWidth + _DRCObj.DRCVIAxMinSpace(NumOfVIAxX=_ViaMet12Met2NumberOfCOX,NumOfVIAxY=_ViaMet12Met2NumberOfCOY )

        self._DesignParameter['_Met2Layer']['_XYCoordinates']=_XYCoordinateOfViaMet12Met2
        self._DesignParameter['_Met2Layer']['_XWidth'] = _DRCObj._VIAxMinWidth + (_ViaMet12Met2NumberOfCOX - 1)*  _LengthViaMet12Met2BtwCO+ 2 * max([_DRCObj._Metal1MinEnclosureVia1,_DRCObj._MetalxMinEnclosureCO])

        self._DesignParameter['_Met2Layer']['_YWidth'] = _DRCObj._VIAxMinWidth + (_ViaMet12Met2NumberOfCOY - 1)*  _LengthViaMet12Met2BtwCO+ 2 * max([_DRCObj._Metal1MinEnclosureVia12,_DRCObj._MetalxMinEnclosureCO2])



        print ('#############################     Cont Layer Calculation   ##############################################')

        tmp=[]
        self._DesignParameter['_COLayer']['_XWidth'] = _DRCObj._VIAxMinWidth
        self._DesignParameter['_COLayer']['_YWidth'] = _DRCObj._VIAxMinWidth
        _LengthViaMet12Met2BtwCO = _DRCObj._VIAxMinWidth + _DRCObj.DRCVIAxMinSpace(NumOfVIAxX=_ViaMet12Met2NumberOfCOX,NumOfVIAxY=_ViaMet12Met2NumberOfCOY )
        for i in range(0, _ViaMet12Met2NumberOfCOX):
            for j in range(0, _ViaMet12Met2NumberOfCOY):

                if (_ViaMet12Met2NumberOfCOX % 2) == 0 and (_ViaMet12Met2NumberOfCOY % 2)==0:
                    _xycoordinatetmp = [_XYCoordinateOfViaMet12Met2[0][0] - (_ViaMet12Met2NumberOfCOX / 2 - 0.5) * _LengthViaMet12Met2BtwCO + i * _LengthViaMet12Met2BtwCO,
                                        _XYCoordinateOfViaMet12Met2[0][1] - (_ViaMet12Met2NumberOfCOY / 2 - 0.5 )*_LengthViaMet12Met2BtwCO + j*_LengthViaMet12Met2BtwCO]

                elif (_ViaMet12Met2NumberOfCOX % 2) == 0 and (_ViaMet12Met2NumberOfCOY % 2)==1:
                    _xycoordinatetmp = [_XYCoordinateOfViaMet12Met2[0][0] - (_ViaMet12Met2NumberOfCOX / 2 - 0.5) * _LengthViaMet12Met2BtwCO + i * _LengthViaMet12Met2BtwCO,
                                        _XYCoordinateOfViaMet12Met2[0][1] - (_ViaMet12Met2NumberOfCOY-1)/2 * _LengthViaMet12Met2BtwCO +j*_LengthViaMet12Met2BtwCO]

                elif (_ViaMet12Met2NumberOfCOX % 2) == 1 and (_ViaMet12Met2NumberOfCOY % 2)==0:
                    _xycoordinatetmp = [_XYCoordinateOfViaMet12Met2[0][0] - (_ViaMet12Met2NumberOfCOX -1) / 2  * _LengthViaMet12Met2BtwCO + i * _LengthViaMet12Met2BtwCO,
                                        _XYCoordinateOfViaMet12Met2[0][1] - (_ViaMet12Met2NumberOfCOY / 2 - 0.5 )*_LengthViaMet12Met2BtwCO + j*_LengthViaMet12Met2BtwCO]

                elif (_ViaMet12Met2NumberOfCOX % 2) == 1 and (_ViaMet12Met2NumberOfCOY % 2)==1:
                    _xycoordinatetmp = [_XYCoordinateOfViaMet12Met2[0][0] - (_ViaMet12Met2NumberOfCOX -1) / 2 * _LengthViaMet12Met2BtwCO + i * _LengthViaMet12Met2BtwCO,
                                        _XYCoordinateOfViaMet12Met2[0][1] - (_ViaMet12Met2NumberOfCOY-1)/2 * _LengthViaMet12Met2BtwCO +j*_LengthViaMet12Met2BtwCO]
                tmp.append(_xycoordinatetmp)


        self._DesignParameter['_COLayer']['_XYCoordinates']=tmp


        del _DRCObj
        print ('#########################################################################################################')
        print(('                                    {}  ViaMet12Met2 Calculation End                                    '.format(self._DesignParameter['_Name']['_Name'])))
        print ('#########################################################################################################')

    def _CalculateViaMet12Met2DesignParameterMinimumEnclosureY(self, _ViaMet12Met2NumberOfCOX=None, _ViaMet12Met2NumberOfCOY=None ):
        """
            Via Spacing:
                - x,y-direction same spacing.
                - _DRCObj.DRCVIAxMinSpace(NumX, NumY)
            Enclosure:
                - x(horizontal): opposite side min enclosure(drc.~~Via12, drc.~~CO2)
                - y(vertical): min enclosure(drc.~~Via1, drc.~~CO)
                - 각 x,y direction에서 Met1, Metx(Met2) 중 max enclosure value를 모든 metal에 적용.

        """
        print ('#########################################################################################################')
        print(('                                    {}  ViaMet12Met2 Calculation Start                                    '.format(self._DesignParameter['_Name']['_Name'])))
        print ('#########################################################################################################')

        ###############################################Check the number of CO On Via Contact###########################################################################################
        if _ViaMet12Met2NumberOfCOX ==0 or _ViaMet12Met2NumberOfCOY==0:
            print(('************************* Error occured in {} Design Parameter Calculation******************************'.format(self._DesignParameter['_Name']['_Name'])))
            if DesignParameters._DebugMode == 0:
                return 0
        ###############################################################################################################################################################################
        _DRCObj=DRC.DRC()
        _XYCoordinateOfViaMet12Met2 = [[0,0]]


        print ('#############################     Met1 Layer Calculation   ##############################################')
        _LengthViaMet12Met2BtwCO = _DRCObj._VIAxMinWidth + _DRCObj.DRCVIAxMinSpace(NumOfVIAxX=_ViaMet12Met2NumberOfCOX,NumOfVIAxY=_ViaMet12Met2NumberOfCOY )
        self._DesignParameter['_Met1Layer']['_XYCoordinates']=_XYCoordinateOfViaMet12Met2
        self._DesignParameter['_Met1Layer']['_XWidth']=_DRCObj._VIAxMinWidth+ (_ViaMet12Met2NumberOfCOX - 1)* _LengthViaMet12Met2BtwCO+ 2 * max([_DRCObj._Metal1MinEnclosureVia12,_DRCObj._MetalxMinEnclosureCO2])
        self._DesignParameter['_Met1Layer']['_YWidth']=_DRCObj._VIAxMinWidth + (_ViaMet12Met2NumberOfCOY - 1)* _LengthViaMet12Met2BtwCO+ 2 * max([_DRCObj._Metal1MinEnclosureVia1,_DRCObj._MetalxMinEnclosureCO])

        print ('#############################     Met2 Layer Calculation   ##############################################')
        _LengthViaMet12Met2BtwCO = _DRCObj._VIAxMinWidth + _DRCObj.DRCVIAxMinSpace(NumOfVIAxX=_ViaMet12Met2NumberOfCOX,NumOfVIAxY=_ViaMet12Met2NumberOfCOY )

        self._DesignParameter['_Met2Layer']['_XYCoordinates']=_XYCoordinateOfViaMet12Met2
        self._DesignParameter['_Met2Layer']['_XWidth'] = _DRCObj._VIAxMinWidth + (_ViaMet12Met2NumberOfCOX - 1)*  _LengthViaMet12Met2BtwCO+ 2 * max([_DRCObj._Metal1MinEnclosureVia12,_DRCObj._MetalxMinEnclosureCO2])

        self._DesignParameter['_Met2Layer']['_YWidth'] = _DRCObj._VIAxMinWidth + (_ViaMet12Met2NumberOfCOY - 1)*  _LengthViaMet12Met2BtwCO+ 2 * max([_DRCObj._Metal1MinEnclosureVia1,_DRCObj._MetalxMinEnclosureCO])



        print ('#############################     Cont Layer Calculation   ##############################################')

        tmp=[]
        self._DesignParameter['_COLayer']['_XWidth'] = _DRCObj._VIAxMinWidth
        self._DesignParameter['_COLayer']['_YWidth'] = _DRCObj._VIAxMinWidth
        _LengthViaMet12Met2BtwCO = _DRCObj._VIAxMinWidth + _DRCObj.DRCVIAxMinSpace(NumOfVIAxX=_ViaMet12Met2NumberOfCOX,NumOfVIAxY=_ViaMet12Met2NumberOfCOY )
        for i in range(0, _ViaMet12Met2NumberOfCOX):
            for j in range(0, _ViaMet12Met2NumberOfCOY):

                if (_ViaMet12Met2NumberOfCOX % 2) == 0 and (_ViaMet12Met2NumberOfCOY % 2)==0:
                    _xycoordinatetmp = [_XYCoordinateOfViaMet12Met2[0][0] - (_ViaMet12Met2NumberOfCOX / 2 - 0.5) * _LengthViaMet12Met2BtwCO + i * _LengthViaMet12Met2BtwCO,
                                        _XYCoordinateOfViaMet12Met2[0][1] - (_ViaMet12Met2NumberOfCOY / 2 - 0.5 )*_LengthViaMet12Met2BtwCO + j*_LengthViaMet12Met2BtwCO]

                elif (_ViaMet12Met2NumberOfCOX % 2) == 0 and (_ViaMet12Met2NumberOfCOY % 2)==1:
                    _xycoordinatetmp = [_XYCoordinateOfViaMet12Met2[0][0] - (_ViaMet12Met2NumberOfCOX / 2 - 0.5) * _LengthViaMet12Met2BtwCO + i * _LengthViaMet12Met2BtwCO,
                                        _XYCoordinateOfViaMet12Met2[0][1] - (_ViaMet12Met2NumberOfCOY-1)/2 * _LengthViaMet12Met2BtwCO +j*_LengthViaMet12Met2BtwCO]

                elif (_ViaMet12Met2NumberOfCOX % 2) == 1 and (_ViaMet12Met2NumberOfCOY % 2)==0:
                    _xycoordinatetmp = [_XYCoordinateOfViaMet12Met2[0][0] - (_ViaMet12Met2NumberOfCOX -1) / 2  * _LengthViaMet12Met2BtwCO + i * _LengthViaMet12Met2BtwCO,
                                        _XYCoordinateOfViaMet12Met2[0][1] - (_ViaMet12Met2NumberOfCOY / 2 - 0.5 )*_LengthViaMet12Met2BtwCO + j*_LengthViaMet12Met2BtwCO]

                elif (_ViaMet12Met2NumberOfCOX % 2) == 1 and (_ViaMet12Met2NumberOfCOY % 2)==1:
                    _xycoordinatetmp = [_XYCoordinateOfViaMet12Met2[0][0] - (_ViaMet12Met2NumberOfCOX -1) / 2 * _LengthViaMet12Met2BtwCO + i * _LengthViaMet12Met2BtwCO,
                                        _XYCoordinateOfViaMet12Met2[0][1] - (_ViaMet12Met2NumberOfCOY-1)/2 * _LengthViaMet12Met2BtwCO +j*_LengthViaMet12Met2BtwCO]
                tmp.append(_xycoordinatetmp)


        self._DesignParameter['_COLayer']['_XYCoordinates']=tmp
        del _DRCObj
        print ('#########################################################################################################')
        print(('                                    {}  ViaMet12Met2 Calculation End                                    '.format(self._DesignParameter['_Name']['_Name'])))
        print ('#########################################################################################################')


    def _CalculateDesignParameterSameEnclosure(self, _ViaMet12Met2NumberOfCOX=None, _ViaMet12Met2NumberOfCOY=None):
        """
            Note:
                - SS28nm 에서만 적용된 rule 이용.
                - 나머지 공정에서는 _CalculateDesignParameter() 와 동일한 output.
            Via Spacing:
                - x,y-direction same spacing.
                - _DRCObj.DRCVIAxMinSpace(NumX, NumY)
            Enclosure:
                - x,y-direction 모두 same enclosure 적용 (drc.~~Via3)
                - max([_DRCObj._Metal1MinEnclosureVia3,_DRCObj._MetalxMinEnclosureVia3])
                - 각 x,y direction에서 Met1, Metx(Met2) 중 max enclosure value를 모든 metal에 적용.

        """
        print ('#########################################################################################################')
        print(('                                    {}  ViaMet12Met2 Calculation Start                                    '.format(self._DesignParameter['_Name']['_Name'])))
        print ('#########################################################################################################')

        ###############################################Check the number of CO On Via Contact###########################################################################################
        if _ViaMet12Met2NumberOfCOX == 0 or _ViaMet12Met2NumberOfCOY == 0:
            print(('************************* Error occured in {} Design Parameter Calculation******************************'.format(self._DesignParameter['_Name']['_Name'])))
            if DesignParameters._DebugMode == 0:
                return 0
        ###############################################################################################################################################################################
        _DRCObj = DRC.DRC()
        _XYCoordinateOfViaMet12Met2 = [[0,0]]

        print ('#############################     Met1 Layer Calculation   ##############################################')
        _LengthViaMet12Met2BtwCO = _DRCObj._VIAxMinWidth + _DRCObj.DRCVIAxMinSpace(NumOfVIAxX=_ViaMet12Met2NumberOfCOX,NumOfVIAxY=_ViaMet12Met2NumberOfCOY)
        self._DesignParameter['_Met1Layer']['_XYCoordinates'] = _XYCoordinateOfViaMet12Met2
        self._DesignParameter['_Met1Layer']['_XWidth'] = _DRCObj._VIAxMinWidth + (_ViaMet12Met2NumberOfCOX - 1) * _LengthViaMet12Met2BtwCO + 2 * max([_DRCObj._Metal1MinEnclosureVia3,_DRCObj._MetalxMinEnclosureVia3])
        self._DesignParameter['_Met1Layer']['_YWidth'] = _DRCObj._VIAxMinWidth + (_ViaMet12Met2NumberOfCOY - 1) * _LengthViaMet12Met2BtwCO + 2 * max([_DRCObj._Metal1MinEnclosureVia3,_DRCObj._MetalxMinEnclosureVia3])

        print ('#############################     Met2 Layer Calculation   ##############################################')
        _LengthViaMet12Met2BtwCO = _DRCObj._VIAxMinWidth + _DRCObj.DRCVIAxMinSpace(NumOfVIAxX=_ViaMet12Met2NumberOfCOX,NumOfVIAxY=_ViaMet12Met2NumberOfCOY)
        self._DesignParameter['_Met2Layer']['_XYCoordinates'] = _XYCoordinateOfViaMet12Met2
        self._DesignParameter['_Met2Layer']['_XWidth'] = _DRCObj._VIAxMinWidth + (_ViaMet12Met2NumberOfCOX - 1) * _LengthViaMet12Met2BtwCO + 2 * max([_DRCObj._Metal1MinEnclosureVia3,_DRCObj._MetalxMinEnclosureVia3])
        self._DesignParameter['_Met2Layer']['_YWidth'] = _DRCObj._VIAxMinWidth + (_ViaMet12Met2NumberOfCOY - 1) * _LengthViaMet12Met2BtwCO + 2 * max([_DRCObj._Metal1MinEnclosureVia3,_DRCObj._MetalxMinEnclosureVia3])

        print ('#############################     Cont Layer Calculation   ##############################################')
        self._DesignParameter['_COLayer']['_XWidth'] = _DRCObj._VIAxMinWidth
        self._DesignParameter['_COLayer']['_YWidth'] = _DRCObj._VIAxMinWidth
        _LengthViaMet12Met2BtwCO = _DRCObj._VIAxMinWidth + _DRCObj.DRCVIAxMinSpace(NumOfVIAxX=_ViaMet12Met2NumberOfCOX,NumOfVIAxY=_ViaMet12Met2NumberOfCOY)
        tmp = []
        for i in range(0, _ViaMet12Met2NumberOfCOX):
            for j in range(0, _ViaMet12Met2NumberOfCOY):
                if (_ViaMet12Met2NumberOfCOX % 2) == 0 and (_ViaMet12Met2NumberOfCOY % 2) == 0:
                    _xycoordinatetmp = [_XYCoordinateOfViaMet12Met2[0][0] - (_ViaMet12Met2NumberOfCOX / 2 - 0.5) * _LengthViaMet12Met2BtwCO + i * _LengthViaMet12Met2BtwCO,
                                        _XYCoordinateOfViaMet12Met2[0][1] - (_ViaMet12Met2NumberOfCOY / 2 - 0.5) * _LengthViaMet12Met2BtwCO + j * _LengthViaMet12Met2BtwCO]

                elif (_ViaMet12Met2NumberOfCOX % 2) == 0 and (_ViaMet12Met2NumberOfCOY % 2) == 1:
                    _xycoordinatetmp = [_XYCoordinateOfViaMet12Met2[0][0] - (_ViaMet12Met2NumberOfCOX / 2 - 0.5) * _LengthViaMet12Met2BtwCO + i * _LengthViaMet12Met2BtwCO,
                                        _XYCoordinateOfViaMet12Met2[0][1] - (_ViaMet12Met2NumberOfCOY - 1) / 2 * _LengthViaMet12Met2BtwCO + j * _LengthViaMet12Met2BtwCO]

                elif (_ViaMet12Met2NumberOfCOX % 2) == 1 and (_ViaMet12Met2NumberOfCOY % 2) == 0:
                    _xycoordinatetmp = [_XYCoordinateOfViaMet12Met2[0][0] - (_ViaMet12Met2NumberOfCOX - 1) / 2 * _LengthViaMet12Met2BtwCO + i * _LengthViaMet12Met2BtwCO,
                                        _XYCoordinateOfViaMet12Met2[0][1] - (_ViaMet12Met2NumberOfCOY / 2 - 0.5) * _LengthViaMet12Met2BtwCO + j * _LengthViaMet12Met2BtwCO]

                elif (_ViaMet12Met2NumberOfCOX % 2) == 1 and (_ViaMet12Met2NumberOfCOY % 2) == 1:
                    _xycoordinatetmp = [_XYCoordinateOfViaMet12Met2[0][0] - (_ViaMet12Met2NumberOfCOX - 1) / 2 * _LengthViaMet12Met2BtwCO + i * _LengthViaMet12Met2BtwCO,
                                        _XYCoordinateOfViaMet12Met2[0][1] - (_ViaMet12Met2NumberOfCOY - 1) / 2 * _LengthViaMet12Met2BtwCO + j * _LengthViaMet12Met2BtwCO]
                tmp.append(_xycoordinatetmp)

        self._DesignParameter['_COLayer']['_XYCoordinates'] = tmp

        print ('#########################################################################################################')
        print(('                                    {}  ViaMet12Met2 Calculation End                                    '.format(self._DesignParameter['_Name']['_Name'])))
        print ('#########################################################################################################')


    @classmethod
    def _CalculateNumViaByXYWidth(cls, XWidth=None, YWidth=None, Mode=None):
        """
        :param XWidth:
        :param YWidth:
        :param Mode:    None or 'MinEnclosureX' or 'MinEnclosureY'
        :return:
        """

        _DRCObj = DRC.DRC()

        LengthBtwVias_case1 = _DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace
        LengthBtwVias_case2 = _DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace2  # when exceeding 2x2 array (3x2 or 2x3, ...)

        if Mode == 'MinEnclosureX':
            MetMinEnclosureX = _DRCObj._Metal1MinEnclosureVia1
            MetMinEnclosureY = _DRCObj._Metal1MinEnclosureVia12
        elif Mode == 'MinEnclosureY':
            MetMinEnclosureX = _DRCObj._Metal1MinEnclosureVia12
            MetMinEnclosureY = _DRCObj._Metal1MinEnclosureVia1
        elif Mode == 'SameEnclosure':
            MetMinEnclosureX = _DRCObj._Metal1MinEnclosureVia3
            MetMinEnclosureY = _DRCObj._Metal1MinEnclosureVia3
        else:
            MetMinEnclosureX = _DRCObj._Metal1MinEnclosureVia12
            MetMinEnclosureY = _DRCObj._Metal1MinEnclosureVia12

        # MetMinEnclosureX = _DRCObj._Metal1MinEnclosureVia1 if (Mode is 'MinEnclosureX') else _DRCObj._Metal1MinEnclosureVia12
        # MetMinEnclosureY = _DRCObj._Metal1MinEnclosureVia1 if (Mode is 'MinEnclosureY') else _DRCObj._Metal1MinEnclosureVia12

        NumViaX_case1 = int((XWidth - 2*MetMinEnclosureX - _DRCObj._VIAxMinWidth) // LengthBtwVias_case1) + 1
        NumViaY_case1 = int((YWidth - 2*MetMinEnclosureY - _DRCObj._VIAxMinWidth) // LengthBtwVias_case1) + 1
        NumViaX_case2 = int((XWidth - 2*MetMinEnclosureX - _DRCObj._VIAxMinWidth) // LengthBtwVias_case2) + 1
        NumViaY_case2 = int((YWidth - 2*MetMinEnclosureY - _DRCObj._VIAxMinWidth) // LengthBtwVias_case2) + 1

        if (NumViaX_case1 > 2) and (NumViaY_case1 > 2):
            NumViaX = NumViaX_case2
            NumViaY = NumViaY_case2
        else:
            NumViaX = NumViaX_case1
            NumViaY = NumViaY_case1

        if (NumViaX < 1) or (NumViaY < 1):
            raise NotImplementedError

        # print('NumViaX_case1', NumViaX_case1, 'NumViaY_case1', NumViaY_case1, 'NumViaX_case2', NumViaX_case2, 'NumViaY_case2', NumViaY_case2)

        return NumViaX, NumViaY

    @classmethod
    def CalcNumVia(cls, XWidth=None, YWidth=None):
        return cls._CalculateNumViaByXYWidth(XWidth=XWidth, YWidth=YWidth, Mode=None)

    @classmethod
    def CalcNumViaMinEnclosureX(cls, XWidth=None, YWidth=None):
        return cls._CalculateNumViaByXYWidth(XWidth=XWidth, YWidth=YWidth, Mode='MinEnclosureX')

    @classmethod
    def CalcNumViaMinEnclosureY(cls, XWidth=None, YWidth=None):
        return cls._CalculateNumViaByXYWidth(XWidth=XWidth, YWidth=YWidth, Mode='MinEnclosureY')

    @classmethod
    def CalcNumViaSameEnclosure(cls, XWidth=None, YWidth=None):
        return cls._CalculateNumViaByXYWidth(XWidth=XWidth, YWidth=YWidth, Mode='SameEnclosure')




if __name__=='__main__':
    ViaMet12Met2Obj1=_ViaMet12Met2(_DesignParameter=None, _Name='ViaMet12Met2test1')
    ViaMet12Met2Obj1._CalculateViaMet12Met2DesignParameter(_ViaMet12Met2NumberOfCOX=3, _ViaMet12Met2NumberOfCOY=4 )
    ViaMet12Met2Obj2=_ViaMet12Met2(_DesignParameter=None, _Name='ViaMet12Met2test2')
    ViaMet12Met2Obj2._CalculateViaMet12Met2DesignParameterMinimumEnclosureY(_ViaMet12Met2NumberOfCOX=3, _ViaMet12Met2NumberOfCOY=4 )
    ViaMet12Met2Obj3=_ViaMet12Met2(_DesignParameter=None, _Name='ViaMet12Met2test3')
    ViaMet12Met2Obj3._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(_ViaMet12Met2NumberOfCOX=3, _ViaMet12Met2NumberOfCOY=4 )
    #ViaMet12Met2Obj=_ViaMet12Met2(_ViaMet12Met2DesignParameter=DesignParameters.ViaMet12Met2DesignParameter, _ViaMet12Met2Name='ViaMet12Met22test')
    #ViaMet12Met2Obj=_ViaMet12Met2(_Technology=DesignParameters._Technology, _XYCoordinatePbody=[0,0], _NumberOfPbodyCO=2, _WidthXPbodyOD=890, _WidthYPbodyOD=420, _WidthXPbodyNP=1250, _WidthYPbodyNP=780, _WidthPbodyCO=220, _LengthPbodyBtwCO=470, _WidthXPbodyMet1=810, _WidthYPbodyMet1=340, _PbodyName='ViaMet12Met2')
    ViaMet12Met2Obj1._UpdateDesignParameter2GDSStructure(_DesignParameterInDictionary= ViaMet12Met2Obj1._DesignParameter)
    ViaMet12Met2Obj2._UpdateDesignParameter2GDSStructure(_DesignParameterInDictionary= ViaMet12Met2Obj2._DesignParameter)
    ViaMet12Met2Obj3._UpdateDesignParameter2GDSStructure(_DesignParameterInDictionary= ViaMet12Met2Obj3._DesignParameter)

    testStreamFile=open('./testStreamFile1.gds','wb')

    tmp1=ViaMet12Met2Obj1._CreateGDSStream(ViaMet12Met2Obj1._DesignParameter['_GDSFile']['_GDSFile'])

    tmp1.write_binary_gds_stream(testStreamFile)
    testStreamFile=open('./testStreamFile2.gds','wb')

    tmp2=ViaMet12Met2Obj2._CreateGDSStream(ViaMet12Met2Obj2._DesignParameter['_GDSFile']['_GDSFile'])

    tmp2.write_binary_gds_stream(testStreamFile)

    testStreamFile=open('./testStreamFile3.gds','wb')

    tmp3=ViaMet12Met2Obj3._CreateGDSStream(ViaMet12Met2Obj3._DesignParameter['_GDSFile']['_GDSFile'])

    tmp3.write_binary_gds_stream(testStreamFile)

    testStreamFile.close()
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
    # testStreamFile=open('./testStreamFile1.gds','rb')
    # ftp_cadence_server.storbinary('STOR testStreamFile1.gds', testStreamFile)
    # testStreamFile.close()
    # testStreamFile=open('./testStreamFile2.gds','rb')
    # ftp_cadence_server.storbinary('STOR testStreamFile2.gds', testStreamFile)
    # testStreamFile.close()
    # testStreamFile=open('./testStreamFile3.gds','rb')
    # ftp_cadence_server.storbinary('STOR testStreamFile3.gds', testStreamFile)
    # testStreamFile.close()
    # print 'close ftp connection'
    # ftp_cadence_server.quit()
    # testStreamFile.close()
    #
    # print '##########################################################################################'