from KJH91_Projects.Project_ADC.Layoutgen_code.E00_Slicer import StickDiagram
from KJH91_Projects.Project_ADC.Layoutgen_code.E00_Slicer import DesignParameters
from KJH91_Projects.Project_ADC.Layoutgen_code.E00_Slicer import user_define_exceptions


from KJH91_Projects.Project_ADC.Layoutgen_code.E00_Slicer import DRC

import ftplib
from ftplib import FTP
import base64


class _ViaMet62Met7(StickDiagram._StickDiagram):
    _ParametersForDesignCalculation= dict(_ViaMet62Met7NumberOfCOX=None, _ViaMet62Met7NumberOfCOY=None,
                                          _MetalType = dict(METAL1 = 'X', METAL2 = 'X', METAL3 = 'X', METAL4 = 'X', METAL5 = 'X', METAL6 = 'X', METAL7 = 'X', METAL8 = 'Z', METAL9 = 'Z'),
                                          )



    def __init__(self, _DesignParameter=None, _Name=None):

        if _DesignParameter!=None:
            self._DesignParameter=_DesignParameter
        else :
            self._DesignParameter = dict(
                                                    _Met7Layer=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL7'][0],_Datatype=DesignParameters._LayerMapping['METAL7'][1], _XYCoordinates=[],_XWidth=400, _YWidth=400),
                                                    _Met6Layer=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL6'][0],_Datatype=DesignParameters._LayerMapping['METAL6'][1], _XYCoordinates=[],_XWidth=400, _YWidth=400),
                                                    _COLayer=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['VIA67'][0],_Datatype=DesignParameters._LayerMapping['VIA67'][1], _XYCoordinates=[],_XWidth=400, _YWidth=400),
                                                    _Name=self._NameDeclaration(_Name=_Name), _GDSFile=self._GDSObjDeclaration(_GDSFile=None),
                                                    _XYcoordAsCent=dict(_XYcoordAsCent=1),
                                                   )

        if _Name != None:
            self._DesignParameter['_Name']['_Name']=_Name

    def _CalculateViaMet62Met7DesignParameter(self, _ViaMet62Met7NumberOfCOX=None, _ViaMet62Met7NumberOfCOY=None,
                                              _MetalType = dict(METAL1 = 'X', METAL2 = 'X', METAL3 = 'X', METAL4 = 'X', METAL5 = 'X', METAL6 = 'X', METAL7 = 'X', METAL8 = 'Z', METAL9 = 'Z'), ):
        print ('#########################################################################################################')
        print ('                                    {}  ViaMet62Met7 Calculation Start                                    '.format(self._DesignParameter['_Name']['_Name']))
        print ('#########################################################################################################')

        ###############################################Check the number of CO On Via Contact###########################################################################################
        if _ViaMet62Met7NumberOfCOX ==0 or _ViaMet62Met7NumberOfCOY==0:
            print ('************************* Error occured in {} Design Parameter Calculation******************************'.format(self._DesignParameter['_Name']['_Name']))
            if DesignParameters._DebugMode == 0:
                return 0
        ###############################################################################################################################################################################
        _DRCObj=DRC.DRC()
        _XYCoordinateOfViaMet62Met7 = [[0,0]]


        print ('#############################     Met5 Layer Calculation   ##############################################')
        if _MetalType['METAL7'] == 'X':
            _LengthViaMet62Met7BtwCO = _DRCObj._VIAxMinWidth + _DRCObj.DRCVIAxMinSpace(NumOfVIAxX=_ViaMet62Met7NumberOfCOX,NumOfVIAxY=_ViaMet62Met7NumberOfCOY )
        elif _MetalType['METAL7'] == 'Y':
            _LengthViaMet62Met7BtwCO = _DRCObj._VIAyMinWidth + _DRCObj.DRCVIAyMinSpace(NumOfVIAyX=_ViaMet62Met7NumberOfCOX,NumOfVIAyY=_ViaMet62Met7NumberOfCOY )
        elif _MetalType['METAL7'] == 'Z':
            _LengthViaMet62Met7BtwCO = _DRCObj._VIAzMinWidth + _DRCObj.DRCVIAzMinSpace(NumOfVIAzX=_ViaMet62Met7NumberOfCOX,NumOfVIAzY=_ViaMet62Met7NumberOfCOY )
        elif _MetalType['METAL7'] == 'R':
            _LengthViaMet62Met7BtwCO = _DRCObj._VIArMinWidth + _DRCObj.DRCVIArMinSpace(NumOfVIArX=_ViaMet62Met7NumberOfCOX,NumOfVIArY=_ViaMet62Met7NumberOfCOY )
        else:
            raise user_define_exceptions.IncorrectInputError('_MetalType should have a value among X Y Z R')

        if _MetalType['METAL7'] == 'X':
            self._DesignParameter['_Met6Layer']['_XYCoordinates']=_XYCoordinateOfViaMet62Met7
            self._DesignParameter['_Met6Layer']['_XWidth']=_DRCObj._VIAxMinWidth + (_ViaMet62Met7NumberOfCOX - 1)* _LengthViaMet62Met7BtwCO+ 2 * max([_DRCObj._Metal1MinEnclosureVia12,_DRCObj._MetalxMinEnclosureCO2])
            self._DesignParameter['_Met6Layer']['_YWidth']=_DRCObj._VIAxMinWidth + (_ViaMet62Met7NumberOfCOY - 1)* _LengthViaMet62Met7BtwCO+ 2 * max([_DRCObj._Metal1MinEnclosureVia12,_DRCObj._MetalxMinEnclosureCO2])
        elif _MetalType['METAL7'] == 'Y':
            self._DesignParameter['_Met6Layer']['_XYCoordinates']=_XYCoordinateOfViaMet62Met7
            self._DesignParameter['_Met6Layer']['_XWidth']=_DRCObj._VIAyMinWidth + (_ViaMet62Met7NumberOfCOX - 1)* _LengthViaMet62Met7BtwCO+ 2 * max([_DRCObj._Metal1MinEnclosureVia12,_DRCObj._MetalxMinEnclosureCO2, _DRCObj._MetalyMinEnclosureCO2])
            self._DesignParameter['_Met6Layer']['_YWidth']=_DRCObj._VIAyMinWidth + (_ViaMet62Met7NumberOfCOY - 1)* _LengthViaMet62Met7BtwCO+ 2 * max([_DRCObj._Metal1MinEnclosureVia12,_DRCObj._MetalxMinEnclosureCO2, _DRCObj._MetalyMinEnclosureCO2])
        elif _MetalType['METAL7'] == 'Z':
            self._DesignParameter['_Met6Layer']['_XYCoordinates']=_XYCoordinateOfViaMet62Met7
            self._DesignParameter['_Met6Layer']['_XWidth']=_DRCObj._VIAzMinWidth + (_ViaMet62Met7NumberOfCOX - 1)* _LengthViaMet62Met7BtwCO+ 2 * max([_DRCObj._Metal1MinEnclosureVia12,_DRCObj._MetalxMinEnclosureCO2, _DRCObj._MetalyMinEnclosureCO2, _DRCObj._MetalzMinEnclosureCO2])
            self._DesignParameter['_Met6Layer']['_YWidth']=_DRCObj._VIAzMinWidth + (_ViaMet62Met7NumberOfCOY - 1)* _LengthViaMet62Met7BtwCO+ 2 * max([_DRCObj._Metal1MinEnclosureVia12,_DRCObj._MetalxMinEnclosureCO2, _DRCObj._MetalyMinEnclosureCO2, _DRCObj._MetalzMinEnclosureCO2])
        elif _MetalType['METAL7'] == 'R':
            self._DesignParameter['_Met6Layer']['_XYCoordinates']=_XYCoordinateOfViaMet62Met7
            self._DesignParameter['_Met6Layer']['_XWidth']=_DRCObj._VIArMinWidth + (_ViaMet62Met7NumberOfCOX - 1)* _LengthViaMet62Met7BtwCO+ 2 * max([_DRCObj._Metal1MinEnclosureVia12,_DRCObj._MetalxMinEnclosureCO2, _DRCObj._MetalyMinEnclosureCO2, _DRCObj._MetalzMinEnclosureCO2, _DRCObj._MetalrMinEnclosureCO2])
            self._DesignParameter['_Met6Layer']['_YWidth']=_DRCObj._VIArMinWidth + (_ViaMet62Met7NumberOfCOY - 1)* _LengthViaMet62Met7BtwCO+ 2 * max([_DRCObj._Metal1MinEnclosureVia12,_DRCObj._MetalxMinEnclosureCO2, _DRCObj._MetalyMinEnclosureCO2, _DRCObj._MetalzMinEnclosureCO2, _DRCObj._MetalrMinEnclosureCO2])
        else:
            raise user_define_exceptions.IncorrectInputError('_MetalType should have a value among X Y Z R')


        print ('#############################     Met2 Layer Calculation   ##############################################')
        # _LengthViaMet62Met7BtwCO = _DRCObj._VIAxMinWidth + _DRCObj.DRCVIAxMinSpace(NumOfVIAxX=_ViaMet62Met7NumberOfCOX,NumOfVIAxY=_ViaMet62Met7NumberOfCOY )

        # self._DesignParameter['_Met7Layer']['_XYCoordinates']=_XYCoordinateOfViaMet62Met7
        # self._DesignParameter['_Met7Layer']['_XWidth'] = _DRCObj._VIAxMinWidth + (_ViaMet62Met7NumberOfCOX - 1)*  _LengthViaMet62Met7BtwCO+ 2 * max([_DRCObj._Metal1MinEnclosureVia12,_DRCObj._MetalxMinEnclosureCO2])
        # self._DesignParameter['_Met7Layer']['_YWidth'] = _DRCObj._VIAxMinWidth + (_ViaMet62Met7NumberOfCOY - 1)*  _LengthViaMet62Met7BtwCO+ 2 * max([_DRCObj._Metal1MinEnclosureVia12,_DRCObj._MetalxMinEnclosureCO2])
        if _MetalType['METAL7'] == 'X':
            self._DesignParameter['_Met7Layer']['_XYCoordinates']=_XYCoordinateOfViaMet62Met7
            self._DesignParameter['_Met7Layer']['_XWidth']=_DRCObj._VIAxMinWidth + (_ViaMet62Met7NumberOfCOX - 1)* _LengthViaMet62Met7BtwCO+ 2 * max([_DRCObj._Metal1MinEnclosureVia12,_DRCObj._MetalxMinEnclosureCO2])
            self._DesignParameter['_Met7Layer']['_YWidth']=_DRCObj._VIAxMinWidth + (_ViaMet62Met7NumberOfCOY - 1)* _LengthViaMet62Met7BtwCO+ 2 * max([_DRCObj._Metal1MinEnclosureVia12,_DRCObj._MetalxMinEnclosureCO2])
        elif _MetalType['METAL7'] == 'Y':
            self._DesignParameter['_Met7Layer']['_XYCoordinates']=_XYCoordinateOfViaMet62Met7
            self._DesignParameter['_Met7Layer']['_XWidth']=_DRCObj._VIAyMinWidth + (_ViaMet62Met7NumberOfCOX - 1)* _LengthViaMet62Met7BtwCO+ 2 * max([_DRCObj._Metal1MinEnclosureVia12,_DRCObj._MetalxMinEnclosureCO2, _DRCObj._MetalyMinEnclosureCO2])
            self._DesignParameter['_Met7Layer']['_YWidth']=_DRCObj._VIAyMinWidth + (_ViaMet62Met7NumberOfCOY - 1)* _LengthViaMet62Met7BtwCO+ 2 * max([_DRCObj._Metal1MinEnclosureVia12,_DRCObj._MetalxMinEnclosureCO2, _DRCObj._MetalyMinEnclosureCO2])
        elif _MetalType['METAL7'] == 'Z':
            self._DesignParameter['_Met7Layer']['_XYCoordinates']=_XYCoordinateOfViaMet62Met7
            self._DesignParameter['_Met7Layer']['_XWidth']=_DRCObj._VIAzMinWidth + (_ViaMet62Met7NumberOfCOX - 1)* _LengthViaMet62Met7BtwCO+ 2 * max([_DRCObj._Metal1MinEnclosureVia12,_DRCObj._MetalxMinEnclosureCO2, _DRCObj._MetalyMinEnclosureCO2, _DRCObj._MetalzMinEnclosureCO2])
            self._DesignParameter['_Met7Layer']['_YWidth']=_DRCObj._VIAzMinWidth + (_ViaMet62Met7NumberOfCOY - 1)* _LengthViaMet62Met7BtwCO+ 2 * max([_DRCObj._Metal1MinEnclosureVia12,_DRCObj._MetalxMinEnclosureCO2, _DRCObj._MetalyMinEnclosureCO2, _DRCObj._MetalzMinEnclosureCO2])
        elif _MetalType['METAL7'] == 'R':
            self._DesignParameter['_Met7Layer']['_XYCoordinates']=_XYCoordinateOfViaMet62Met7
            self._DesignParameter['_Met7Layer']['_XWidth']=_DRCObj._VIArMinWidth + (_ViaMet62Met7NumberOfCOX - 1)* _LengthViaMet62Met7BtwCO+ 2 * max([_DRCObj._Metal1MinEnclosureVia12,_DRCObj._MetalxMinEnclosureCO2, _DRCObj._MetalyMinEnclosureCO2, _DRCObj._MetalzMinEnclosureCO2, _DRCObj._MetalrMinEnclosureCO2])
            self._DesignParameter['_Met7Layer']['_YWidth']=_DRCObj._VIArMinWidth + (_ViaMet62Met7NumberOfCOY - 1)* _LengthViaMet62Met7BtwCO+ 2 * max([_DRCObj._Metal1MinEnclosureVia12,_DRCObj._MetalxMinEnclosureCO2, _DRCObj._MetalyMinEnclosureCO2, _DRCObj._MetalzMinEnclosureCO2, _DRCObj._MetalrMinEnclosureCO2])
        else:
            raise user_define_exceptions.IncorrectInputError('_MetalType should have a value among X Y Z R')
        print ('#############################     Cont Layer Calculation   ##############################################')

        tmp=[]
        if _MetalType['METAL7'] == 'X':
            self._DesignParameter['_COLayer']['_XWidth'] = _DRCObj._VIAxMinWidth
            self._DesignParameter['_COLayer']['_YWidth'] = _DRCObj._VIAxMinWidth
        elif _MetalType['METAL7'] == 'Y':
            self._DesignParameter['_COLayer']['_XWidth'] = _DRCObj._VIAyMinWidth
            self._DesignParameter['_COLayer']['_YWidth'] = _DRCObj._VIAyMinWidth
        elif _MetalType['METAL7'] == 'Z':
            self._DesignParameter['_COLayer']['_XWidth'] = _DRCObj._VIAzMinWidth
            self._DesignParameter['_COLayer']['_YWidth'] = _DRCObj._VIAzMinWidth
        elif _MetalType['METAL7'] == 'R':
            self._DesignParameter['_COLayer']['_XWidth'] = _DRCObj._VIArMinWidth
            self._DesignParameter['_COLayer']['_YWidth'] = _DRCObj._VIArMinWidth
        else:
            raise user_define_exceptions.IncorrectInputError('_MetalType should have a value among X Y Z R')

        # _LengthViaMet62Met7BtwCO = _DRCObj._VIAxMinWidth + _DRCObj.DRCVIAxMinSpace(NumOfVIAxX=_ViaMet62Met7NumberOfCOX,NumOfVIAxY=_ViaMet62Met7NumberOfCOY )
        for i in range(0, _ViaMet62Met7NumberOfCOX):
            for j in range(0, _ViaMet62Met7NumberOfCOY):

                if (_ViaMet62Met7NumberOfCOX % 2) == 0 and (_ViaMet62Met7NumberOfCOY % 2)==0:
                    _xycoordinatetmp = [_XYCoordinateOfViaMet62Met7[0][0] - (_ViaMet62Met7NumberOfCOX / 2 - 0.5) * _LengthViaMet62Met7BtwCO + i * _LengthViaMet62Met7BtwCO,
                                        _XYCoordinateOfViaMet62Met7[0][1] - (_ViaMet62Met7NumberOfCOY / 2 - 0.5 )*_LengthViaMet62Met7BtwCO + j*_LengthViaMet62Met7BtwCO]

                elif (_ViaMet62Met7NumberOfCOX % 2) == 0 and (_ViaMet62Met7NumberOfCOY % 2)==1:
                    _xycoordinatetmp = [_XYCoordinateOfViaMet62Met7[0][0] - (_ViaMet62Met7NumberOfCOX / 2 - 0.5) * _LengthViaMet62Met7BtwCO + i * _LengthViaMet62Met7BtwCO,
                                        _XYCoordinateOfViaMet62Met7[0][1] - (_ViaMet62Met7NumberOfCOY-1)/2 * _LengthViaMet62Met7BtwCO +j*_LengthViaMet62Met7BtwCO]

                elif (_ViaMet62Met7NumberOfCOX % 2) == 1 and (_ViaMet62Met7NumberOfCOY % 2)==0:
                    _xycoordinatetmp = [_XYCoordinateOfViaMet62Met7[0][0] - (_ViaMet62Met7NumberOfCOX -1) / 2  * _LengthViaMet62Met7BtwCO + i * _LengthViaMet62Met7BtwCO,
                                        _XYCoordinateOfViaMet62Met7[0][1] - (_ViaMet62Met7NumberOfCOY / 2 - 0.5 )*_LengthViaMet62Met7BtwCO + j*_LengthViaMet62Met7BtwCO]

                elif (_ViaMet62Met7NumberOfCOX % 2) == 1 and (_ViaMet62Met7NumberOfCOY % 2)==1:
                    _xycoordinatetmp = [_XYCoordinateOfViaMet62Met7[0][0] - (_ViaMet62Met7NumberOfCOX -1) / 2 * _LengthViaMet62Met7BtwCO + i * _LengthViaMet62Met7BtwCO,
                                        _XYCoordinateOfViaMet62Met7[0][1] - (_ViaMet62Met7NumberOfCOY-1)/2 * _LengthViaMet62Met7BtwCO +j*_LengthViaMet62Met7BtwCO]
                tmp.append(_xycoordinatetmp)


        self._DesignParameter['_COLayer']['_XYCoordinates']=tmp




        del _DRCObj
        print ('#########################################################################################################')
        print ('                                    {}  ViaMet62Met7 Calculation End                                    '.format(self._DesignParameter['_Name']['_Name']))
        print ('#########################################################################################################')


    def _CalculateViaMet62Met7DesignParameterMinimumEnclosureX(self, _ViaMet62Met7NumberOfCOX=None, _ViaMet62Met7NumberOfCOY=None,
                                                               _MetalType = dict(METAL1 = 'X', METAL2 = 'X', METAL3 = 'X', METAL4 = 'X', METAL5 = 'X', METAL6 = 'X', METAL7 = 'X', METAL8 = 'Z', METAL9 = 'Z'), ):

        print ('#########################################################################################################')
        print ('                                    {}  ViaMet62Met7 Calculation Start                                    '.format(self._DesignParameter['_Name']['_Name']))
        print ('#########################################################################################################')

        ###############################################Check the number of CO On Via Contact###########################################################################################
        if _ViaMet62Met7NumberOfCOX ==0 or _ViaMet62Met7NumberOfCOY==0:
            print ('************************* Error occured in {} Design Parameter Calculation******************************'.format(self._DesignParameter['_Name']['_Name']))
            if DesignParameters._DebugMode == 0:
                return 0
        ###############################################################################################################################################################################
        _DRCObj=DRC.DRC()
        _XYCoordinateOfViaMet62Met7 = [[0,0]]


        print ('#############################     Met5 Layer Calculation   ##############################################')
        if _MetalType['METAL7'] == 'X':
            _LengthViaMet62Met7BtwCO = _DRCObj._VIAxMinWidth + _DRCObj.DRCVIAxMinSpace(NumOfVIAxX=_ViaMet62Met7NumberOfCOX,NumOfVIAxY=_ViaMet62Met7NumberOfCOY )
        elif _MetalType['METAL7'] == 'Y':
            _LengthViaMet62Met7BtwCO = _DRCObj._VIAyMinWidth + _DRCObj.DRCVIAyMinSpace(NumOfVIAyX=_ViaMet62Met7NumberOfCOX,NumOfVIAyY=_ViaMet62Met7NumberOfCOY )
        elif _MetalType['METAL7'] == 'Z':
            _LengthViaMet62Met7BtwCO = _DRCObj._VIAzMinWidth + _DRCObj.DRCVIAzMinSpace(NumOfVIAzX=_ViaMet62Met7NumberOfCOX,NumOfVIAzY=_ViaMet62Met7NumberOfCOY )
        elif _MetalType['METAL7'] == 'R':
            _LengthViaMet62Met7BtwCO = _DRCObj._VIArMinWidth + _DRCObj.DRCVIArMinSpace(NumOfVIArX=_ViaMet62Met7NumberOfCOX,NumOfVIArY=_ViaMet62Met7NumberOfCOY )
        else:
            raise user_define_exceptions.IncorrectInputError('_MetalType should have a value among X Y Z R')
        # _LengthViaMet62Met7BtwCO = _DRCObj._VIAxMinWidth + _DRCObj.DRCVIAxMinSpace(NumOfVIAxX=_ViaMet62Met7NumberOfCOX,NumOfVIAxY=_ViaMet62Met7NumberOfCOY )
        # self._DesignParameter['_Met6Layer']['_XYCoordinates']=_XYCoordinateOfViaMet62Met7
        # self._DesignParameter['_Met6Layer']['_XWidth']=_DRCObj._VIAxMinWidth+ (_ViaMet62Met7NumberOfCOX - 1)* _LengthViaMet62Met7BtwCO+ 2 * max([_DRCObj._Metal1MinEnclosureVia1,_DRCObj._MetalxMinEnclosureCO])
        # self._DesignParameter['_Met6Layer']['_YWidth']=_DRCObj._VIAxMinWidth + (_ViaMet62Met7NumberOfCOY - 1)* _LengthViaMet62Met7BtwCO+ 2 * max([_DRCObj._Metal1MinEnclosureVia12,_DRCObj._MetalxMinEnclosureCO2])

        if _MetalType['METAL7'] == 'X':
            self._DesignParameter['_Met6Layer']['_XYCoordinates']=_XYCoordinateOfViaMet62Met7
            self._DesignParameter['_Met6Layer']['_XWidth']=_DRCObj._VIAxMinWidth + (_ViaMet62Met7NumberOfCOX - 1)* _LengthViaMet62Met7BtwCO+ 2 * max([_DRCObj._Metal1MinEnclosureVia1,_DRCObj._MetalxMinEnclosureCO])
            self._DesignParameter['_Met6Layer']['_YWidth']=_DRCObj._VIAxMinWidth + (_ViaMet62Met7NumberOfCOY - 1)* _LengthViaMet62Met7BtwCO+ 2 * max([_DRCObj._Metal1MinEnclosureVia12,_DRCObj._MetalxMinEnclosureCO2])
        elif _MetalType['METAL7'] == 'Y':
            self._DesignParameter['_Met6Layer']['_XYCoordinates']=_XYCoordinateOfViaMet62Met7
            self._DesignParameter['_Met6Layer']['_XWidth']=_DRCObj._VIAyMinWidth + (_ViaMet62Met7NumberOfCOX - 1)* _LengthViaMet62Met7BtwCO+ 2 * max([_DRCObj._Metal1MinEnclosureVia1,_DRCObj._MetalxMinEnclosureCO, _DRCObj._MetalyMinEnclosureCO])
            self._DesignParameter['_Met6Layer']['_YWidth']=_DRCObj._VIAyMinWidth + (_ViaMet62Met7NumberOfCOY - 1)* _LengthViaMet62Met7BtwCO+ 2 * max([_DRCObj._Metal1MinEnclosureVia12,_DRCObj._MetalxMinEnclosureCO2, _DRCObj._MetalyMinEnclosureCO2])
        elif _MetalType['METAL7'] == 'Z':
            self._DesignParameter['_Met6Layer']['_XYCoordinates']=_XYCoordinateOfViaMet62Met7
            self._DesignParameter['_Met6Layer']['_XWidth']=_DRCObj._VIAzMinWidth + (_ViaMet62Met7NumberOfCOX - 1)* _LengthViaMet62Met7BtwCO+ 2 * max([_DRCObj._Metal1MinEnclosureVia1,_DRCObj._MetalxMinEnclosureCO, _DRCObj._MetalyMinEnclosureCO, _DRCObj._MetalzMinEnclosureCO])
            self._DesignParameter['_Met6Layer']['_YWidth']=_DRCObj._VIAzMinWidth + (_ViaMet62Met7NumberOfCOY - 1)* _LengthViaMet62Met7BtwCO+ 2 * max([_DRCObj._Metal1MinEnclosureVia12,_DRCObj._MetalxMinEnclosureCO2, _DRCObj._MetalyMinEnclosureCO2, _DRCObj._MetalzMinEnclosureCO2])
        elif _MetalType['METAL7'] == 'R':
            self._DesignParameter['_Met6Layer']['_XYCoordinates']=_XYCoordinateOfViaMet62Met7
            self._DesignParameter['_Met6Layer']['_XWidth']=_DRCObj._VIArMinWidth + (_ViaMet62Met7NumberOfCOX - 1)* _LengthViaMet62Met7BtwCO+ 2 * max([_DRCObj._Metal1MinEnclosureVia1,_DRCObj._MetalxMinEnclosureCO, _DRCObj._MetalyMinEnclosureCO, _DRCObj._MetalzMinEnclosureCO, _DRCObj._MetalrMinEnclosureCO])
            self._DesignParameter['_Met6Layer']['_YWidth']=_DRCObj._VIArMinWidth + (_ViaMet62Met7NumberOfCOY - 1)* _LengthViaMet62Met7BtwCO+ 2 * max([_DRCObj._Metal1MinEnclosureVia12,_DRCObj._MetalxMinEnclosureCO2, _DRCObj._MetalyMinEnclosureCO2, _DRCObj._MetalzMinEnclosureCO2, _DRCObj._MetalrMinEnclosureCO2])
        else:
            raise user_define_exceptions.IncorrectInputError('_MetalType should have a value among X Y Z R')

        print ('#############################     Met2 Layer Calculation   ##############################################')
        # _LengthViaMet62Met7BtwCO = _DRCObj._VIAxMinWidth + _DRCObj.DRCVIAxMinSpace(NumOfVIAxX=_ViaMet62Met7NumberOfCOX,NumOfVIAxY=_ViaMet62Met7NumberOfCOY )

        # self._DesignParameter['_Met7Layer']['_XYCoordinates']=_XYCoordinateOfViaMet62Met7
        # self._DesignParameter['_Met7Layer']['_XWidth'] = _DRCObj._VIAxMinWidth + (_ViaMet62Met7NumberOfCOX - 1)*  _LengthViaMet62Met7BtwCO+ 2 * max([_DRCObj._Metal1MinEnclosureVia1,_DRCObj._MetalxMinEnclosureCO])
        #
        # self._DesignParameter['_Met7Layer']['_YWidth'] = _DRCObj._VIAxMinWidth + (_ViaMet62Met7NumberOfCOY - 1)*  _LengthViaMet62Met7BtwCO+ 2 * max([_DRCObj._Metal1MinEnclosureVia12,_DRCObj._MetalxMinEnclosureCO2])
        #
        if _MetalType['METAL7'] == 'X':
            self._DesignParameter['_Met7Layer']['_XYCoordinates']=_XYCoordinateOfViaMet62Met7
            self._DesignParameter['_Met7Layer']['_XWidth']=_DRCObj._VIAxMinWidth + (_ViaMet62Met7NumberOfCOX - 1)* _LengthViaMet62Met7BtwCO+ 2 * max([_DRCObj._Metal1MinEnclosureVia1,_DRCObj._MetalxMinEnclosureCO])
            self._DesignParameter['_Met7Layer']['_YWidth']=_DRCObj._VIAxMinWidth + (_ViaMet62Met7NumberOfCOY - 1)* _LengthViaMet62Met7BtwCO+ 2 * max([_DRCObj._Metal1MinEnclosureVia12,_DRCObj._MetalxMinEnclosureCO2])
        elif _MetalType['METAL7'] == 'Y':
            self._DesignParameter['_Met7Layer']['_XYCoordinates']=_XYCoordinateOfViaMet62Met7
            self._DesignParameter['_Met7Layer']['_XWidth']=_DRCObj._VIAyMinWidth + (_ViaMet62Met7NumberOfCOX - 1)* _LengthViaMet62Met7BtwCO+ 2 * max([_DRCObj._Metal1MinEnclosureVia1,_DRCObj._MetalxMinEnclosureCO, _DRCObj._MetalyMinEnclosureCO])
            self._DesignParameter['_Met7Layer']['_YWidth']=_DRCObj._VIAyMinWidth + (_ViaMet62Met7NumberOfCOY - 1)* _LengthViaMet62Met7BtwCO+ 2 * max([_DRCObj._Metal1MinEnclosureVia12,_DRCObj._MetalxMinEnclosureCO2, _DRCObj._MetalyMinEnclosureCO2])
        elif _MetalType['METAL7'] == 'Z':
            self._DesignParameter['_Met7Layer']['_XYCoordinates']=_XYCoordinateOfViaMet62Met7
            self._DesignParameter['_Met7Layer']['_XWidth']=_DRCObj._VIAzMinWidth + (_ViaMet62Met7NumberOfCOX - 1)* _LengthViaMet62Met7BtwCO+ 2 * max([_DRCObj._Metal1MinEnclosureVia1,_DRCObj._MetalxMinEnclosureCO, _DRCObj._MetalyMinEnclosureCO, _DRCObj._MetalzMinEnclosureCO])
            self._DesignParameter['_Met7Layer']['_YWidth']=_DRCObj._VIAzMinWidth + (_ViaMet62Met7NumberOfCOY - 1)* _LengthViaMet62Met7BtwCO+ 2 * max([_DRCObj._Metal1MinEnclosureVia12,_DRCObj._MetalxMinEnclosureCO2, _DRCObj._MetalyMinEnclosureCO2, _DRCObj._MetalzMinEnclosureCO2])
        elif _MetalType['METAL7'] == 'R':
            self._DesignParameter['_Met7Layer']['_XYCoordinates']=_XYCoordinateOfViaMet62Met7
            self._DesignParameter['_Met7Layer']['_XWidth']=_DRCObj._VIArMinWidth + (_ViaMet62Met7NumberOfCOX - 1)* _LengthViaMet62Met7BtwCO+ 2 * max([_DRCObj._Metal1MinEnclosureVia1,_DRCObj._MetalxMinEnclosureCO, _DRCObj._MetalyMinEnclosureCO, _DRCObj._MetalzMinEnclosureCO, _DRCObj._MetalrMinEnclosureCO])
            self._DesignParameter['_Met7Layer']['_YWidth']=_DRCObj._VIArMinWidth + (_ViaMet62Met7NumberOfCOY - 1)* _LengthViaMet62Met7BtwCO+ 2 * max([_DRCObj._Metal1MinEnclosureVia12,_DRCObj._MetalxMinEnclosureCO2, _DRCObj._MetalyMinEnclosureCO2, _DRCObj._MetalzMinEnclosureCO2, _DRCObj._MetalrMinEnclosureCO2])
        else:
            raise user_define_exceptions.IncorrectInputError('_MetalType should have a value among X Y Z R')


        print ('#############################     Cont Layer Calculation   ##############################################')

        tmp=[]
        if _MetalType['METAL7'] == 'X':
            self._DesignParameter['_COLayer']['_XWidth'] = _DRCObj._VIAxMinWidth
            self._DesignParameter['_COLayer']['_YWidth'] = _DRCObj._VIAxMinWidth
        elif _MetalType['METAL7'] == 'Y':
            self._DesignParameter['_COLayer']['_XWidth'] = _DRCObj._VIAyMinWidth
            self._DesignParameter['_COLayer']['_YWidth'] = _DRCObj._VIAyMinWidth
        elif _MetalType['METAL7'] == 'Z':
            self._DesignParameter['_COLayer']['_XWidth'] = _DRCObj._VIAzMinWidth
            self._DesignParameter['_COLayer']['_YWidth'] = _DRCObj._VIAzMinWidth
        elif _MetalType['METAL7'] == 'R':
            self._DesignParameter['_COLayer']['_XWidth'] = _DRCObj._VIArMinWidth
            self._DesignParameter['_COLayer']['_YWidth'] = _DRCObj._VIArMinWidth
        else:
            raise user_define_exceptions.IncorrectInputError('_MetalType should have a value among X Y Z R')
        # self._DesignParameter['_COLayer']['_XWidth'] = _DRCObj._VIAxMinWidth
        # self._DesignParameter['_COLayer']['_YWidth'] = _DRCObj._VIAxMinWidth
        # _LengthViaMet62Met7BtwCO = _DRCObj._VIAxMinWidth + _DRCObj.DRCVIAxMinSpace(NumOfVIAxX=_ViaMet62Met7NumberOfCOX,NumOfVIAxY=_ViaMet62Met7NumberOfCOY )
        for i in range(0, _ViaMet62Met7NumberOfCOX):
            for j in range(0, _ViaMet62Met7NumberOfCOY):

                if (_ViaMet62Met7NumberOfCOX % 2) == 0 and (_ViaMet62Met7NumberOfCOY % 2)==0:
                    _xycoordinatetmp = [_XYCoordinateOfViaMet62Met7[0][0] - (_ViaMet62Met7NumberOfCOX / 2 - 0.5) * _LengthViaMet62Met7BtwCO + i * _LengthViaMet62Met7BtwCO,
                                        _XYCoordinateOfViaMet62Met7[0][1] - (_ViaMet62Met7NumberOfCOY / 2 - 0.5 )*_LengthViaMet62Met7BtwCO + j*_LengthViaMet62Met7BtwCO]

                elif (_ViaMet62Met7NumberOfCOX % 2) == 0 and (_ViaMet62Met7NumberOfCOY % 2)==1:
                    _xycoordinatetmp = [_XYCoordinateOfViaMet62Met7[0][0] - (_ViaMet62Met7NumberOfCOX / 2 - 0.5) * _LengthViaMet62Met7BtwCO + i * _LengthViaMet62Met7BtwCO,
                                        _XYCoordinateOfViaMet62Met7[0][1] - (_ViaMet62Met7NumberOfCOY-1)/2 * _LengthViaMet62Met7BtwCO +j*_LengthViaMet62Met7BtwCO]

                elif (_ViaMet62Met7NumberOfCOX % 2) == 1 and (_ViaMet62Met7NumberOfCOY % 2)==0:
                    _xycoordinatetmp = [_XYCoordinateOfViaMet62Met7[0][0] - (_ViaMet62Met7NumberOfCOX -1) / 2  * _LengthViaMet62Met7BtwCO + i * _LengthViaMet62Met7BtwCO,
                                        _XYCoordinateOfViaMet62Met7[0][1] - (_ViaMet62Met7NumberOfCOY / 2 - 0.5 )*_LengthViaMet62Met7BtwCO + j*_LengthViaMet62Met7BtwCO]

                elif (_ViaMet62Met7NumberOfCOX % 2) == 1 and (_ViaMet62Met7NumberOfCOY % 2)==1:
                    _xycoordinatetmp = [_XYCoordinateOfViaMet62Met7[0][0] - (_ViaMet62Met7NumberOfCOX -1) / 2 * _LengthViaMet62Met7BtwCO + i * _LengthViaMet62Met7BtwCO,
                                        _XYCoordinateOfViaMet62Met7[0][1] - (_ViaMet62Met7NumberOfCOY-1)/2 * _LengthViaMet62Met7BtwCO +j*_LengthViaMet62Met7BtwCO]
                tmp.append(_xycoordinatetmp)


        self._DesignParameter['_COLayer']['_XYCoordinates']=tmp


        del _DRCObj
        print ('#########################################################################################################')
        print ('                                    {}  ViaMet62Met7 Calculation End                                    '.format(self._DesignParameter['_Name']['_Name']))
        print ('#########################################################################################################')

    def _CalculateViaMet62Met7DesignParameterMinimumEnclosureY(self, _ViaMet62Met7NumberOfCOX=None, _ViaMet62Met7NumberOfCOY=None,
                                                               _MetalType = dict(METAL1 = 'X', METAL2 = 'X', METAL3 = 'X', METAL4 = 'X', METAL5 = 'X', METAL6 = 'X', METAL7 = 'X', METAL8 = 'Z', METAL9 = 'Z'), ):

        print ('#########################################################################################################')
        print ('                                    {}  ViaMet62Met7 Calculation Start                                    '.format(self._DesignParameter['_Name']['_Name']))
        print ('#########################################################################################################')

        ###############################################Check the number of CO On Via Contact###########################################################################################
        if _ViaMet62Met7NumberOfCOX ==0 or _ViaMet62Met7NumberOfCOY==0:
            print ('************************* Error occured in {} Design Parameter Calculation******************************'.format(self._DesignParameter['_Name']['_Name']))
            if DesignParameters._DebugMode == 0:
                return 0
        ###############################################################################################################################################################################
        _DRCObj=DRC.DRC()
        _XYCoordinateOfViaMet62Met7 = [[0,0]]


        print ('#############################     Met5 Layer Calculation   ##############################################')
        # _LengthViaMet62Met7BtwCO = _DRCObj._VIAxMinWidth + _DRCObj.DRCVIAxMinSpace(NumOfVIAxX=_ViaMet62Met7NumberOfCOX,NumOfVIAxY=_ViaMet62Met7NumberOfCOY )
        if _MetalType['METAL7'] == 'X':
            _LengthViaMet62Met7BtwCO = _DRCObj._VIAxMinWidth + _DRCObj.DRCVIAxMinSpace(NumOfVIAxX=_ViaMet62Met7NumberOfCOX,NumOfVIAxY=_ViaMet62Met7NumberOfCOY )
        elif _MetalType['METAL7'] == 'Y':
            _LengthViaMet62Met7BtwCO = _DRCObj._VIAyMinWidth + _DRCObj.DRCVIAyMinSpace(NumOfVIAyX=_ViaMet62Met7NumberOfCOX,NumOfVIAyY=_ViaMet62Met7NumberOfCOY )
        elif _MetalType['METAL7'] == 'Z':
            _LengthViaMet62Met7BtwCO = _DRCObj._VIAzMinWidth + _DRCObj.DRCVIAzMinSpace(NumOfVIAzX=_ViaMet62Met7NumberOfCOX,NumOfVIAzY=_ViaMet62Met7NumberOfCOY )
        elif _MetalType['METAL7'] == 'R':
            _LengthViaMet62Met7BtwCO = _DRCObj._VIArMinWidth + _DRCObj.DRCVIArMinSpace(NumOfVIArX=_ViaMet62Met7NumberOfCOX,NumOfVIArY=_ViaMet62Met7NumberOfCOY )
        else:
            raise user_define_exceptions.IncorrectInputError('_MetalType should have a value among X Y Z R')
        # self._DesignParameter['_Met6Layer']['_XYCoordinates']=_XYCoordinateOfViaMet62Met7
        # self._DesignParameter['_Met6Layer']['_XWidth']=_DRCObj._VIAxMinWidth+ (_ViaMet62Met7NumberOfCOX - 1)* _LengthViaMet62Met7BtwCO+ 2 * max([_DRCObj._Metal1MinEnclosureVia12,_DRCObj._MetalxMinEnclosureCO2])
        # self._DesignParameter['_Met6Layer']['_YWidth']=_DRCObj._VIAxMinWidth + (_ViaMet62Met7NumberOfCOY - 1)* _LengthViaMet62Met7BtwCO+ 2 * max([_DRCObj._Metal1MinEnclosureVia1,_DRCObj._MetalxMinEnclosureCO])
        if _MetalType['METAL7'] == 'X':
            self._DesignParameter['_Met6Layer']['_XYCoordinates']=_XYCoordinateOfViaMet62Met7
            self._DesignParameter['_Met6Layer']['_XWidth']=_DRCObj._VIAxMinWidth + (_ViaMet62Met7NumberOfCOX - 1)* _LengthViaMet62Met7BtwCO+ 2 * max([_DRCObj._Metal1MinEnclosureVia12,_DRCObj._MetalxMinEnclosureCO2])
            self._DesignParameter['_Met6Layer']['_YWidth']=_DRCObj._VIAxMinWidth + (_ViaMet62Met7NumberOfCOY - 1)* _LengthViaMet62Met7BtwCO+ 2 * max([_DRCObj._Metal1MinEnclosureVia1,_DRCObj._MetalxMinEnclosureCO])
        elif _MetalType['METAL7'] == 'Y':
            self._DesignParameter['_Met6Layer']['_XYCoordinates']=_XYCoordinateOfViaMet62Met7
            self._DesignParameter['_Met6Layer']['_XWidth']=_DRCObj._VIAyMinWidth + (_ViaMet62Met7NumberOfCOX - 1)* _LengthViaMet62Met7BtwCO+ 2 * max([_DRCObj._Metal1MinEnclosureVia12,_DRCObj._MetalxMinEnclosureCO2, _DRCObj._MetalyMinEnclosureCO2])
            self._DesignParameter['_Met6Layer']['_YWidth']=_DRCObj._VIAyMinWidth + (_ViaMet62Met7NumberOfCOY - 1)* _LengthViaMet62Met7BtwCO+ 2 * max([_DRCObj._Metal1MinEnclosureVia1,_DRCObj._MetalxMinEnclosureCO, _DRCObj._MetalyMinEnclosureCO])
        elif _MetalType['METAL7'] == 'Z':
            self._DesignParameter['_Met6Layer']['_XYCoordinates']=_XYCoordinateOfViaMet62Met7
            self._DesignParameter['_Met6Layer']['_XWidth']=_DRCObj._VIAzMinWidth + (_ViaMet62Met7NumberOfCOX - 1)* _LengthViaMet62Met7BtwCO+ 2 * max([_DRCObj._Metal1MinEnclosureVia12,_DRCObj._MetalxMinEnclosureCO2, _DRCObj._MetalyMinEnclosureCO2, _DRCObj._MetalzMinEnclosureCO2])
            self._DesignParameter['_Met6Layer']['_YWidth']=_DRCObj._VIAzMinWidth + (_ViaMet62Met7NumberOfCOY - 1)* _LengthViaMet62Met7BtwCO+ 2 * max([_DRCObj._Metal1MinEnclosureVia1,_DRCObj._MetalxMinEnclosureCO, _DRCObj._MetalyMinEnclosureCO, _DRCObj._MetalzMinEnclosureCO])
        elif _MetalType['METAL7'] == 'R':
            self._DesignParameter['_Met6Layer']['_XYCoordinates']=_XYCoordinateOfViaMet62Met7
            self._DesignParameter['_Met6Layer']['_XWidth']=_DRCObj._VIArMinWidth + (_ViaMet62Met7NumberOfCOX - 1)* _LengthViaMet62Met7BtwCO+ 2 * max([_DRCObj._Metal1MinEnclosureVia12,_DRCObj._MetalxMinEnclosureCO2, _DRCObj._MetalyMinEnclosureCO2, _DRCObj._MetalzMinEnclosureCO2, _DRCObj._MetalrMinEnclosureCO2])
            self._DesignParameter['_Met6Layer']['_YWidth']=_DRCObj._VIArMinWidth + (_ViaMet62Met7NumberOfCOY - 1)* _LengthViaMet62Met7BtwCO+ 2 * max([_DRCObj._Metal1MinEnclosureVia1,_DRCObj._MetalxMinEnclosureCO, _DRCObj._MetalyMinEnclosureCO, _DRCObj._MetalzMinEnclosureCO, _DRCObj._MetalrMinEnclosureCO])
        else:
            raise user_define_exceptions.IncorrectInputError('_MetalType should have a value among X Y Z R')
        print ('#############################     Met2 Layer Calculation   ##############################################')
        # _LengthViaMet62Met7BtwCO = _DRCObj._VIAxMinWidth + _DRCObj.DRCVIAxMinSpace(NumOfVIAxX=_ViaMet62Met7NumberOfCOX,NumOfVIAxY=_ViaMet62Met7NumberOfCOY )

        # self._DesignParameter['_Met7Layer']['_XYCoordinates']=_XYCoordinateOfViaMet62Met7
        # self._DesignParameter['_Met7Layer']['_XWidth'] = _DRCObj._VIAxMinWidth + (_ViaMet62Met7NumberOfCOX - 1)*  _LengthViaMet62Met7BtwCO+ 2 * max([_DRCObj._Metal1MinEnclosureVia12,_DRCObj._MetalxMinEnclosureCO2])
        #
        # self._DesignParameter['_Met7Layer']['_YWidth'] = _DRCObj._VIAxMinWidth + (_ViaMet62Met7NumberOfCOY - 1)*  _LengthViaMet62Met7BtwCO+ 2 * max([_DRCObj._Metal1MinEnclosureVia1,_DRCObj._MetalxMinEnclosureCO])

        if _MetalType['METAL7'] == 'X':
            self._DesignParameter['_Met7Layer']['_XYCoordinates']=_XYCoordinateOfViaMet62Met7
            self._DesignParameter['_Met7Layer']['_XWidth']=_DRCObj._VIAxMinWidth + (_ViaMet62Met7NumberOfCOX - 1)* _LengthViaMet62Met7BtwCO+ 2 * max([_DRCObj._Metal1MinEnclosureVia12,_DRCObj._MetalxMinEnclosureCO2])
            self._DesignParameter['_Met7Layer']['_YWidth']=_DRCObj._VIAxMinWidth + (_ViaMet62Met7NumberOfCOY - 1)* _LengthViaMet62Met7BtwCO+ 2 * max([_DRCObj._Metal1MinEnclosureVia1,_DRCObj._MetalxMinEnclosureCO])
        elif _MetalType['METAL7'] == 'Y':
            self._DesignParameter['_Met7Layer']['_XYCoordinates']=_XYCoordinateOfViaMet62Met7
            self._DesignParameter['_Met7Layer']['_XWidth']=_DRCObj._VIAyMinWidth + (_ViaMet62Met7NumberOfCOX - 1)* _LengthViaMet62Met7BtwCO+ 2 * max([_DRCObj._Metal1MinEnclosureVia12,_DRCObj._MetalxMinEnclosureCO2, _DRCObj._MetalyMinEnclosureCO2])
            self._DesignParameter['_Met7Layer']['_YWidth']=_DRCObj._VIAyMinWidth + (_ViaMet62Met7NumberOfCOY - 1)* _LengthViaMet62Met7BtwCO+ 2 * max([_DRCObj._Metal1MinEnclosureVia1,_DRCObj._MetalxMinEnclosureCO, _DRCObj._MetalyMinEnclosureCO])
        elif _MetalType['METAL7'] == 'Z':
            self._DesignParameter['_Met7Layer']['_XYCoordinates']=_XYCoordinateOfViaMet62Met7
            self._DesignParameter['_Met7Layer']['_XWidth']=_DRCObj._VIAzMinWidth + (_ViaMet62Met7NumberOfCOX - 1)* _LengthViaMet62Met7BtwCO+ 2 * max([_DRCObj._Metal1MinEnclosureVia12,_DRCObj._MetalxMinEnclosureCO2, _DRCObj._MetalyMinEnclosureCO2, _DRCObj._MetalzMinEnclosureCO2])
            self._DesignParameter['_Met7Layer']['_YWidth']=_DRCObj._VIAzMinWidth + (_ViaMet62Met7NumberOfCOY - 1)* _LengthViaMet62Met7BtwCO+ 2 * max([_DRCObj._Metal1MinEnclosureVia1,_DRCObj._MetalxMinEnclosureCO, _DRCObj._MetalyMinEnclosureCO, _DRCObj._MetalzMinEnclosureCO])
        elif _MetalType['METAL7'] == 'R':
            self._DesignParameter['_Met7Layer']['_XYCoordinates']=_XYCoordinateOfViaMet62Met7
            self._DesignParameter['_Met7Layer']['_XWidth']=_DRCObj._VIArMinWidth + (_ViaMet62Met7NumberOfCOX - 1)* _LengthViaMet62Met7BtwCO+ 2 * max([_DRCObj._Metal1MinEnclosureVia12,_DRCObj._MetalxMinEnclosureCO2, _DRCObj._MetalyMinEnclosureCO2, _DRCObj._MetalzMinEnclosureCO2, _DRCObj._MetalrMinEnclosureCO2])
            self._DesignParameter['_Met7Layer']['_YWidth']=_DRCObj._VIArMinWidth + (_ViaMet62Met7NumberOfCOY - 1)* _LengthViaMet62Met7BtwCO+ 2 * max([_DRCObj._Metal1MinEnclosureVia1,_DRCObj._MetalxMinEnclosureCO, _DRCObj._MetalyMinEnclosureCO, _DRCObj._MetalzMinEnclosureCO, _DRCObj._MetalrMinEnclosureCO])
        else:
            raise user_define_exceptions.IncorrectInputError('_MetalType should have a value among X Y Z R')

        print ('#############################     Cont Layer Calculation   ##############################################')

        tmp=[]
        # self._DesignParameter['_COLayer']['_XWidth'] = _DRCObj._VIAxMinWidth
        # self._DesignParameter['_COLayer']['_YWidth'] = _DRCObj._VIAxMinWidth
        if _MetalType['METAL7'] == 'X':
            self._DesignParameter['_COLayer']['_XWidth'] = _DRCObj._VIAxMinWidth
            self._DesignParameter['_COLayer']['_YWidth'] = _DRCObj._VIAxMinWidth
        elif _MetalType['METAL7'] == 'Y':
            self._DesignParameter['_COLayer']['_XWidth'] = _DRCObj._VIAyMinWidth
            self._DesignParameter['_COLayer']['_YWidth'] = _DRCObj._VIAyMinWidth
        elif _MetalType['METAL7'] == 'Z':
            self._DesignParameter['_COLayer']['_XWidth'] = _DRCObj._VIAzMinWidth
            self._DesignParameter['_COLayer']['_YWidth'] = _DRCObj._VIAzMinWidth
        elif _MetalType['METAL7'] == 'R':
            self._DesignParameter['_COLayer']['_XWidth'] = _DRCObj._VIArMinWidth
            self._DesignParameter['_COLayer']['_YWidth'] = _DRCObj._VIArMinWidth
        else:
            raise user_define_exceptions.IncorrectInputError('_MetalType should have a value among X Y Z R')
        # _LengthViaMet62Met7BtwCO = _DRCObj._VIAxMinWidth + _DRCObj.DRCVIAxMinSpace(NumOfVIAxX=_ViaMet62Met7NumberOfCOX,NumOfVIAxY=_ViaMet62Met7NumberOfCOY )
        for i in range(0, _ViaMet62Met7NumberOfCOX):
            for j in range(0, _ViaMet62Met7NumberOfCOY):

                if (_ViaMet62Met7NumberOfCOX % 2) == 0 and (_ViaMet62Met7NumberOfCOY % 2)==0:
                    _xycoordinatetmp = [_XYCoordinateOfViaMet62Met7[0][0] - (_ViaMet62Met7NumberOfCOX / 2 - 0.5) * _LengthViaMet62Met7BtwCO + i * _LengthViaMet62Met7BtwCO,
                                        _XYCoordinateOfViaMet62Met7[0][1] - (_ViaMet62Met7NumberOfCOY / 2 - 0.5 )*_LengthViaMet62Met7BtwCO + j*_LengthViaMet62Met7BtwCO]

                elif (_ViaMet62Met7NumberOfCOX % 2) == 0 and (_ViaMet62Met7NumberOfCOY % 2)==1:
                    _xycoordinatetmp = [_XYCoordinateOfViaMet62Met7[0][0] - (_ViaMet62Met7NumberOfCOX / 2 - 0.5) * _LengthViaMet62Met7BtwCO + i * _LengthViaMet62Met7BtwCO,
                                        _XYCoordinateOfViaMet62Met7[0][1] - (_ViaMet62Met7NumberOfCOY-1)/2 * _LengthViaMet62Met7BtwCO +j*_LengthViaMet62Met7BtwCO]

                elif (_ViaMet62Met7NumberOfCOX % 2) == 1 and (_ViaMet62Met7NumberOfCOY % 2)==0:
                    _xycoordinatetmp = [_XYCoordinateOfViaMet62Met7[0][0] - (_ViaMet62Met7NumberOfCOX -1) / 2  * _LengthViaMet62Met7BtwCO + i * _LengthViaMet62Met7BtwCO,
                                        _XYCoordinateOfViaMet62Met7[0][1] - (_ViaMet62Met7NumberOfCOY / 2 - 0.5 )*_LengthViaMet62Met7BtwCO + j*_LengthViaMet62Met7BtwCO]

                elif (_ViaMet62Met7NumberOfCOX % 2) == 1 and (_ViaMet62Met7NumberOfCOY % 2)==1:
                    _xycoordinatetmp = [_XYCoordinateOfViaMet62Met7[0][0] - (_ViaMet62Met7NumberOfCOX -1) / 2 * _LengthViaMet62Met7BtwCO + i * _LengthViaMet62Met7BtwCO,
                                        _XYCoordinateOfViaMet62Met7[0][1] - (_ViaMet62Met7NumberOfCOY-1)/2 * _LengthViaMet62Met7BtwCO +j*_LengthViaMet62Met7BtwCO]
                tmp.append(_xycoordinatetmp)


        self._DesignParameter['_COLayer']['_XYCoordinates']=tmp
        del _DRCObj
        print ('#########################################################################################################')
        print ('                                    {}  ViaMet62Met7 Calculation End                                    '.format(self._DesignParameter['_Name']['_Name']))
        print ('#########################################################################################################')

if __name__=='__main__':
    pass