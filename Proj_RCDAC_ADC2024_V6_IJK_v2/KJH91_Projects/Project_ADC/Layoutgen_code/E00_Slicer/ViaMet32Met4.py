from Proj_RCDAC_ADC2024_V6_IJK_v2.KJH91_Projects.Project_ADC.Layoutgen_code.E00_Slicer import StickDiagram
from Proj_RCDAC_ADC2024_V6_IJK_v2.KJH91_Projects.Project_ADC.Layoutgen_code.E00_Slicer import DesignParameters
from Proj_RCDAC_ADC2024_V6_IJK_v2.KJH91_Projects.Project_ADC.Layoutgen_code.E00_Slicer import user_define_exceptions


from Proj_RCDAC_ADC2024_V6_IJK_v2.KJH91_Projects.Project_ADC.Layoutgen_code.E00_Slicer import DRC

import ftplib
from ftplib import FTP
import base64


class _ViaMet32Met4(StickDiagram._StickDiagram):
    _ParametersForDesignCalculation= dict(_ViaMet32Met4NumberOfCOX=None, _ViaMet32Met4NumberOfCOY=None )


    def __init__(self, _DesignParameter=None, _Name=None):

        if _DesignParameter!=None:
            self._DesignParameter=_DesignParameter
        else :
            self._DesignParameter = dict(
                                                    _Met4Layer=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL4'][0],_Datatype=DesignParameters._LayerMapping['METAL4'][1], _XYCoordinates=[],_XWidth=400, _YWidth=400),
                                                    _Met3Layer=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0],_Datatype=DesignParameters._LayerMapping['METAL3'][1], _XYCoordinates=[],_XWidth=400, _YWidth=400),
                                                    _COLayer=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['VIA34'][0],_Datatype=DesignParameters._LayerMapping['VIA34'][1], _XYCoordinates=[],_XWidth=400, _YWidth=400),
                                                    _Name=self._NameDeclaration(_Name=_Name), _GDSFile=self._GDSObjDeclaration(_GDSFile=None),
                                                    _XYcoordAsCent=dict(_XYcoordAsCent=1),


                                                   )



        if _Name != None:
            self._DesignParameter['_Name']['_Name']=_Name
    # def __init__(self, _ViaMet32Met4DesignParameter=None, _ViaMet32Met4Name=None):
    #
    #     if _ViaMet32Met4DesignParameter!=None:
    #         self._ViaMet32Met4DesignParameter=_ViaMet32Met4DesignParameter
    #     else:
    #         self._ViaMet32Met4DesignParameter=dict(_Technology=[0, None, '065nm'],
    #                                                _XYCoordinateOfViaMet32Met4=[1, None, [0,0]],
    #
    #
    #
    #                                                _XYCoordinateOfMet2=[1, None, [[0,0]]], _XWidthOfMet2=[2, DesignParameters._LayerMapping['METAL2'][0],60], _YWidthOfMet2=[2, DesignParameters._LayerMapping['METAL2'][0],400] ,
    #                                                _XYCoordinateOfCO=[1, None, [[0,0]]], _WidthOfCO=[2, DesignParameters._LayerMapping['VIA23'][0],60],
    #                                                _XYCoordinateOfMet3=[1, None, [[0,0]]], _XWidthOfMet3=[2, DesignParameters._LayerMapping['METAL3'][0],90], _YWidthOfMet3=[2, DesignParameters._LayerMapping['METAL3'][0],430],
    #
    #                                                _ViaMet32Met4Name=[0, None,'ViaMet32Met4'], _ViaMet32Met4GDSStructure=[4,None,[]],
    #                                                )
    #
    #
    #
    #
    #     if _ViaMet32Met4Name != None:
    #         self._ViaMet32Met4DesignParameter['_ViaMet32Met4Name'][2]=_ViaMet32Met4Name
            

    def _CalculateViaMet32Met4DesignParameter(self, _ViaMet32Met4NumberOfCOX=None, _ViaMet32Met4NumberOfCOY=None ):
        print ('#########################################################################################################')
        print ('                                    {}  ViaMet32Met4 Calculation Start                                    '.format(self._DesignParameter['_Name']['_Name']))
        print ('#########################################################################################################')

        ###############################################Check the number of CO On Via Contact###########################################################################################
        if _ViaMet32Met4NumberOfCOX ==0 or _ViaMet32Met4NumberOfCOY==0:
            print ('************************* Error occured in {} Design Parameter Calculation******************************'.format(self._DesignParameter['_Name']['_Name']))
            if DesignParameters._DebugMode == 0:
                return 0
        ###############################################################################################################################################################################
        _DRCObj=DRC.DRC()
        _XYCoordinateOfViaMet32Met4 = [[0,0]]


        print ('#############################     Met3 Layer Calculation   ##############################################')
        _LengthViaMet32Met4BtwCO = _DRCObj._VIAxMinWidth + _DRCObj.DRCVIAxMinSpace(NumOfVIAxX=_ViaMet32Met4NumberOfCOX,NumOfVIAxY=_ViaMet32Met4NumberOfCOY )
        self._DesignParameter['_Met3Layer']['_XYCoordinates']=_XYCoordinateOfViaMet32Met4
        self._DesignParameter['_Met3Layer']['_XWidth']=_DRCObj._VIAxMinWidth + (_ViaMet32Met4NumberOfCOX - 1)* _LengthViaMet32Met4BtwCO+ 2 * max([_DRCObj._Metal1MinEnclosureVia12,_DRCObj._MetalxMinEnclosureCO2])
        self._DesignParameter['_Met3Layer']['_YWidth']=_DRCObj._VIAxMinWidth + (_ViaMet32Met4NumberOfCOY - 1)* _LengthViaMet32Met4BtwCO+ 2 * max([_DRCObj._Metal1MinEnclosureVia12,_DRCObj._MetalxMinEnclosureCO2])

        print ('#############################     Met2 Layer Calculation   ##############################################')
        _LengthViaMet32Met4BtwCO = _DRCObj._VIAxMinWidth + _DRCObj.DRCVIAxMinSpace(NumOfVIAxX=_ViaMet32Met4NumberOfCOX,NumOfVIAxY=_ViaMet32Met4NumberOfCOY )

        self._DesignParameter['_Met4Layer']['_XYCoordinates']=_XYCoordinateOfViaMet32Met4
        self._DesignParameter['_Met4Layer']['_XWidth'] = _DRCObj._VIAxMinWidth + (_ViaMet32Met4NumberOfCOX - 1)*  _LengthViaMet32Met4BtwCO+ 2 * max([_DRCObj._Metal1MinEnclosureVia12,_DRCObj._MetalxMinEnclosureCO2])
        self._DesignParameter['_Met4Layer']['_YWidth'] = _DRCObj._VIAxMinWidth + (_ViaMet32Met4NumberOfCOY - 1)*  _LengthViaMet32Met4BtwCO+ 2 * max([_DRCObj._Metal1MinEnclosureVia12,_DRCObj._MetalxMinEnclosureCO2])

        print ('#############################     Cont Layer Calculation   ##############################################')

        tmp=[]
        self._DesignParameter['_COLayer']['_XWidth'] = _DRCObj._VIAxMinWidth
        self._DesignParameter['_COLayer']['_YWidth'] = _DRCObj._VIAxMinWidth
        _LengthViaMet32Met4BtwCO = _DRCObj._VIAxMinWidth + _DRCObj.DRCVIAxMinSpace(NumOfVIAxX=_ViaMet32Met4NumberOfCOX,NumOfVIAxY=_ViaMet32Met4NumberOfCOY )
        for i in range(0, _ViaMet32Met4NumberOfCOX):
            for j in range(0, _ViaMet32Met4NumberOfCOY):

                if (_ViaMet32Met4NumberOfCOX % 2) == 0 and (_ViaMet32Met4NumberOfCOY % 2)==0:
                    _xycoordinatetmp = [_XYCoordinateOfViaMet32Met4[0][0] - (_ViaMet32Met4NumberOfCOX / 2 - 0.5) * _LengthViaMet32Met4BtwCO + i * _LengthViaMet32Met4BtwCO,
                                        _XYCoordinateOfViaMet32Met4[0][1] - (_ViaMet32Met4NumberOfCOY / 2 - 0.5 )*_LengthViaMet32Met4BtwCO + j*_LengthViaMet32Met4BtwCO]

                elif (_ViaMet32Met4NumberOfCOX % 2) == 0 and (_ViaMet32Met4NumberOfCOY % 2)==1:
                    _xycoordinatetmp = [_XYCoordinateOfViaMet32Met4[0][0] - (_ViaMet32Met4NumberOfCOX / 2 - 0.5) * _LengthViaMet32Met4BtwCO + i * _LengthViaMet32Met4BtwCO,
                                        _XYCoordinateOfViaMet32Met4[0][1] - (_ViaMet32Met4NumberOfCOY-1)/2 * _LengthViaMet32Met4BtwCO +j*_LengthViaMet32Met4BtwCO]

                elif (_ViaMet32Met4NumberOfCOX % 2) == 1 and (_ViaMet32Met4NumberOfCOY % 2)==0:
                    _xycoordinatetmp = [_XYCoordinateOfViaMet32Met4[0][0] - (_ViaMet32Met4NumberOfCOX -1) / 2  * _LengthViaMet32Met4BtwCO + i * _LengthViaMet32Met4BtwCO,
                                        _XYCoordinateOfViaMet32Met4[0][1] - (_ViaMet32Met4NumberOfCOY / 2 - 0.5 )*_LengthViaMet32Met4BtwCO + j*_LengthViaMet32Met4BtwCO]

                elif (_ViaMet32Met4NumberOfCOX % 2) == 1 and (_ViaMet32Met4NumberOfCOY % 2)==1:
                    _xycoordinatetmp = [_XYCoordinateOfViaMet32Met4[0][0] - (_ViaMet32Met4NumberOfCOX -1) / 2 * _LengthViaMet32Met4BtwCO + i * _LengthViaMet32Met4BtwCO,
                                        _XYCoordinateOfViaMet32Met4[0][1] - (_ViaMet32Met4NumberOfCOY-1)/2 * _LengthViaMet32Met4BtwCO +j*_LengthViaMet32Met4BtwCO]
                tmp.append(_xycoordinatetmp)


        self._DesignParameter['_COLayer']['_XYCoordinates']=tmp




        del _DRCObj
        print ('#########################################################################################################')
        print ('                                    {}  ViaMet32Met4 Calculation End                                    '.format(self._DesignParameter['_Name']['_Name']))
        print ('#########################################################################################################')


    def _CalculateViaMet32Met4DesignParameterMinimumEnclosureX(self, _ViaMet32Met4NumberOfCOX=None, _ViaMet32Met4NumberOfCOY=None ):

        print ('#########################################################################################################')
        print ('                                    {}  ViaMet32Met4 Calculation Start                                    '.format(self._DesignParameter['_Name']['_Name']))
        print ('#########################################################################################################')

        ###############################################Check the number of CO On Via Contact###########################################################################################
        if _ViaMet32Met4NumberOfCOX ==0 or _ViaMet32Met4NumberOfCOY==0:
            print ('************************* Error occured in {} Design Parameter Calculation******************************'.format(self._DesignParameter['_Name']['_Name']))
            if DesignParameters._DebugMode == 0:
                return 0
        ###############################################################################################################################################################################
        _DRCObj=DRC.DRC()
        _XYCoordinateOfViaMet32Met4 = [[0,0]]


        print ('#############################     Met3 Layer Calculation   ##############################################')
        _LengthViaMet32Met4BtwCO = _DRCObj._VIAxMinWidth + _DRCObj.DRCVIAxMinSpace(NumOfVIAxX=_ViaMet32Met4NumberOfCOX,NumOfVIAxY=_ViaMet32Met4NumberOfCOY )
        self._DesignParameter['_Met3Layer']['_XYCoordinates']=_XYCoordinateOfViaMet32Met4
        self._DesignParameter['_Met3Layer']['_XWidth']=_DRCObj._VIAxMinWidth+ (_ViaMet32Met4NumberOfCOX - 1)* _LengthViaMet32Met4BtwCO+ 2 * max([_DRCObj._Metal1MinEnclosureVia1,_DRCObj._MetalxMinEnclosureCO])
        self._DesignParameter['_Met3Layer']['_YWidth']=_DRCObj._VIAxMinWidth + (_ViaMet32Met4NumberOfCOY - 1)* _LengthViaMet32Met4BtwCO+ 2 * max([_DRCObj._Metal1MinEnclosureVia12,_DRCObj._MetalxMinEnclosureCO2])

        print ('#############################     Met2 Layer Calculation   ##############################################')
        _LengthViaMet32Met4BtwCO = _DRCObj._VIAxMinWidth + _DRCObj.DRCVIAxMinSpace(NumOfVIAxX=_ViaMet32Met4NumberOfCOX,NumOfVIAxY=_ViaMet32Met4NumberOfCOY )

        self._DesignParameter['_Met4Layer']['_XYCoordinates']=_XYCoordinateOfViaMet32Met4
        self._DesignParameter['_Met4Layer']['_XWidth'] = _DRCObj._VIAxMinWidth + (_ViaMet32Met4NumberOfCOX - 1)*  _LengthViaMet32Met4BtwCO+ 2 * max([_DRCObj._Metal1MinEnclosureVia1,_DRCObj._MetalxMinEnclosureCO])

        self._DesignParameter['_Met4Layer']['_YWidth'] = _DRCObj._VIAxMinWidth + (_ViaMet32Met4NumberOfCOY - 1)*  _LengthViaMet32Met4BtwCO+ 2 * max([_DRCObj._Metal1MinEnclosureVia12,_DRCObj._MetalxMinEnclosureCO2])



        print ('#############################     Cont Layer Calculation   ##############################################')

        tmp=[]
        self._DesignParameter['_COLayer']['_XWidth'] = _DRCObj._VIAxMinWidth
        self._DesignParameter['_COLayer']['_YWidth'] = _DRCObj._VIAxMinWidth
        _LengthViaMet32Met4BtwCO = _DRCObj._VIAxMinWidth + _DRCObj.DRCVIAxMinSpace(NumOfVIAxX=_ViaMet32Met4NumberOfCOX,NumOfVIAxY=_ViaMet32Met4NumberOfCOY )
        for i in range(0, _ViaMet32Met4NumberOfCOX):
            for j in range(0, _ViaMet32Met4NumberOfCOY):

                if (_ViaMet32Met4NumberOfCOX % 2) == 0 and (_ViaMet32Met4NumberOfCOY % 2)==0:
                    _xycoordinatetmp = [_XYCoordinateOfViaMet32Met4[0][0] - (_ViaMet32Met4NumberOfCOX / 2 - 0.5) * _LengthViaMet32Met4BtwCO + i * _LengthViaMet32Met4BtwCO,
                                        _XYCoordinateOfViaMet32Met4[0][1] - (_ViaMet32Met4NumberOfCOY / 2 - 0.5 )*_LengthViaMet32Met4BtwCO + j*_LengthViaMet32Met4BtwCO]

                elif (_ViaMet32Met4NumberOfCOX % 2) == 0 and (_ViaMet32Met4NumberOfCOY % 2)==1:
                    _xycoordinatetmp = [_XYCoordinateOfViaMet32Met4[0][0] - (_ViaMet32Met4NumberOfCOX / 2 - 0.5) * _LengthViaMet32Met4BtwCO + i * _LengthViaMet32Met4BtwCO,
                                        _XYCoordinateOfViaMet32Met4[0][1] - (_ViaMet32Met4NumberOfCOY-1)/2 * _LengthViaMet32Met4BtwCO +j*_LengthViaMet32Met4BtwCO]

                elif (_ViaMet32Met4NumberOfCOX % 2) == 1 and (_ViaMet32Met4NumberOfCOY % 2)==0:
                    _xycoordinatetmp = [_XYCoordinateOfViaMet32Met4[0][0] - (_ViaMet32Met4NumberOfCOX -1) / 2  * _LengthViaMet32Met4BtwCO + i * _LengthViaMet32Met4BtwCO,
                                        _XYCoordinateOfViaMet32Met4[0][1] - (_ViaMet32Met4NumberOfCOY / 2 - 0.5 )*_LengthViaMet32Met4BtwCO + j*_LengthViaMet32Met4BtwCO]

                elif (_ViaMet32Met4NumberOfCOX % 2) == 1 and (_ViaMet32Met4NumberOfCOY % 2)==1:
                    _xycoordinatetmp = [_XYCoordinateOfViaMet32Met4[0][0] - (_ViaMet32Met4NumberOfCOX -1) / 2 * _LengthViaMet32Met4BtwCO + i * _LengthViaMet32Met4BtwCO,
                                        _XYCoordinateOfViaMet32Met4[0][1] - (_ViaMet32Met4NumberOfCOY-1)/2 * _LengthViaMet32Met4BtwCO +j*_LengthViaMet32Met4BtwCO]
                tmp.append(_xycoordinatetmp)


        self._DesignParameter['_COLayer']['_XYCoordinates']=tmp


        del _DRCObj
        print ('#########################################################################################################')
        print ('                                    {}  ViaMet32Met4 Calculation End                                    '.format(self._DesignParameter['_Name']['_Name']))
        print ('#########################################################################################################')

    def _CalculateViaMet32Met4DesignParameterMinimumEnclosureY(self, _ViaMet32Met4NumberOfCOX=None, _ViaMet32Met4NumberOfCOY=None ):

        print ('#########################################################################################################')
        print ('                                    {}  ViaMet32Met4 Calculation Start                                    '.format(self._DesignParameter['_Name']['_Name']))
        print ('#########################################################################################################')

        ###############################################Check the number of CO On Via Contact###########################################################################################
        if _ViaMet32Met4NumberOfCOX ==0 or _ViaMet32Met4NumberOfCOY==0:
            print ('************************* Error occured in {} Design Parameter Calculation******************************'.format(self._DesignParameter['_Name']['_Name']))
            if DesignParameters._DebugMode == 0:
                return 0
        ###############################################################################################################################################################################
        _DRCObj=DRC.DRC()
        _XYCoordinateOfViaMet32Met4 = [[0,0]]


        print ('#############################     Met3 Layer Calculation   ##############################################')
        _LengthViaMet32Met4BtwCO = _DRCObj._VIAxMinWidth + _DRCObj.DRCVIAxMinSpace(NumOfVIAxX=_ViaMet32Met4NumberOfCOX,NumOfVIAxY=_ViaMet32Met4NumberOfCOY )
        self._DesignParameter['_Met3Layer']['_XYCoordinates']=_XYCoordinateOfViaMet32Met4
        self._DesignParameter['_Met3Layer']['_XWidth']=_DRCObj._VIAxMinWidth+ (_ViaMet32Met4NumberOfCOX - 1)* _LengthViaMet32Met4BtwCO+ 2 * max([_DRCObj._Metal1MinEnclosureVia12,_DRCObj._MetalxMinEnclosureCO2])
        self._DesignParameter['_Met3Layer']['_YWidth']=_DRCObj._VIAxMinWidth + (_ViaMet32Met4NumberOfCOY - 1)* _LengthViaMet32Met4BtwCO+ 2 * max([_DRCObj._Metal1MinEnclosureVia1,_DRCObj._MetalxMinEnclosureCO])

        print ('#############################     Met2 Layer Calculation   ##############################################')
        _LengthViaMet32Met4BtwCO = _DRCObj._VIAxMinWidth + _DRCObj.DRCVIAxMinSpace(NumOfVIAxX=_ViaMet32Met4NumberOfCOX,NumOfVIAxY=_ViaMet32Met4NumberOfCOY )

        self._DesignParameter['_Met4Layer']['_XYCoordinates']=_XYCoordinateOfViaMet32Met4
        self._DesignParameter['_Met4Layer']['_XWidth'] = _DRCObj._VIAxMinWidth + (_ViaMet32Met4NumberOfCOX - 1)*  _LengthViaMet32Met4BtwCO+ 2 * max([_DRCObj._Metal1MinEnclosureVia12,_DRCObj._MetalxMinEnclosureCO2])

        self._DesignParameter['_Met4Layer']['_YWidth'] = _DRCObj._VIAxMinWidth + (_ViaMet32Met4NumberOfCOY - 1)*  _LengthViaMet32Met4BtwCO+ 2 * max([_DRCObj._Metal1MinEnclosureVia1,_DRCObj._MetalxMinEnclosureCO])



        print ('#############################     Cont Layer Calculation   ##############################################')

        tmp=[]
        self._DesignParameter['_COLayer']['_XWidth'] = _DRCObj._VIAxMinWidth
        self._DesignParameter['_COLayer']['_YWidth'] = _DRCObj._VIAxMinWidth
        _LengthViaMet32Met4BtwCO = _DRCObj._VIAxMinWidth + _DRCObj.DRCVIAxMinSpace(NumOfVIAxX=_ViaMet32Met4NumberOfCOX,NumOfVIAxY=_ViaMet32Met4NumberOfCOY )
        for i in range(0, _ViaMet32Met4NumberOfCOX):
            for j in range(0, _ViaMet32Met4NumberOfCOY):

                if (_ViaMet32Met4NumberOfCOX % 2) == 0 and (_ViaMet32Met4NumberOfCOY % 2)==0:
                    _xycoordinatetmp = [_XYCoordinateOfViaMet32Met4[0][0] - (_ViaMet32Met4NumberOfCOX / 2 - 0.5) * _LengthViaMet32Met4BtwCO + i * _LengthViaMet32Met4BtwCO,
                                        _XYCoordinateOfViaMet32Met4[0][1] - (_ViaMet32Met4NumberOfCOY / 2 - 0.5 )*_LengthViaMet32Met4BtwCO + j*_LengthViaMet32Met4BtwCO]

                elif (_ViaMet32Met4NumberOfCOX % 2) == 0 and (_ViaMet32Met4NumberOfCOY % 2)==1:
                    _xycoordinatetmp = [_XYCoordinateOfViaMet32Met4[0][0] - (_ViaMet32Met4NumberOfCOX / 2 - 0.5) * _LengthViaMet32Met4BtwCO + i * _LengthViaMet32Met4BtwCO,
                                        _XYCoordinateOfViaMet32Met4[0][1] - (_ViaMet32Met4NumberOfCOY-1)/2 * _LengthViaMet32Met4BtwCO +j*_LengthViaMet32Met4BtwCO]

                elif (_ViaMet32Met4NumberOfCOX % 2) == 1 and (_ViaMet32Met4NumberOfCOY % 2)==0:
                    _xycoordinatetmp = [_XYCoordinateOfViaMet32Met4[0][0] - (_ViaMet32Met4NumberOfCOX -1) / 2  * _LengthViaMet32Met4BtwCO + i * _LengthViaMet32Met4BtwCO,
                                        _XYCoordinateOfViaMet32Met4[0][1] - (_ViaMet32Met4NumberOfCOY / 2 - 0.5 )*_LengthViaMet32Met4BtwCO + j*_LengthViaMet32Met4BtwCO]

                elif (_ViaMet32Met4NumberOfCOX % 2) == 1 and (_ViaMet32Met4NumberOfCOY % 2)==1:
                    _xycoordinatetmp = [_XYCoordinateOfViaMet32Met4[0][0] - (_ViaMet32Met4NumberOfCOX -1) / 2 * _LengthViaMet32Met4BtwCO + i * _LengthViaMet32Met4BtwCO,
                                        _XYCoordinateOfViaMet32Met4[0][1] - (_ViaMet32Met4NumberOfCOY-1)/2 * _LengthViaMet32Met4BtwCO +j*_LengthViaMet32Met4BtwCO]
                tmp.append(_xycoordinatetmp)


        self._DesignParameter['_COLayer']['_XYCoordinates']=tmp
        del _DRCObj
        print ('#########################################################################################################')
        print ('                                    {}  ViaMet32Met4 Calculation End                                    '.format(self._DesignParameter['_Name']['_Name']))
        print ('#########################################################################################################')


    def _CalculateDesignParameterSameEnclosure(self, _ViaMet32Met4NumberOfCOX=None, _ViaMet32Met4NumberOfCOY=None):
        print ('#########################################################################################################')
        print ('                                    {}  ViaMet32Met4 Calculation Start                                    '.format(self._DesignParameter['_Name']['_Name']))
        print ('#########################################################################################################')

        ###############################################Check the number of CO On Via Contact###########################################################################################
        if _ViaMet32Met4NumberOfCOX == 0 or _ViaMet32Met4NumberOfCOY == 0:
            print ('************************* Error occured in {} Design Parameter Calculation******************************'.format(self._DesignParameter['_Name']['_Name']))
            if DesignParameters._DebugMode == 0:
                return 0
        ###############################################################################################################################################################################
        _DRCObj = DRC.DRC()
        _XYCoordinateOfViaMet32Met4 = [[0, 0]]

        print ('#############################     Met3 Layer Calculation   ##############################################')
        _LengthViaMet32Met4BtwCO = _DRCObj._VIAxMinWidth + _DRCObj.DRCVIAxMinSpace(NumOfVIAxX=_ViaMet32Met4NumberOfCOX, NumOfVIAxY=_ViaMet32Met4NumberOfCOY)
        self._DesignParameter['_Met3Layer']['_XYCoordinates'] = _XYCoordinateOfViaMet32Met4
        self._DesignParameter['_Met3Layer']['_XWidth'] = _DRCObj._VIAxMinWidth + (_ViaMet32Met4NumberOfCOX - 1) * _LengthViaMet32Met4BtwCO + 2 * max([_DRCObj._Metal1MinEnclosureVia3,_DRCObj._MetalxMinEnclosureVia3])
        self._DesignParameter['_Met3Layer']['_YWidth'] = _DRCObj._VIAxMinWidth + (_ViaMet32Met4NumberOfCOY - 1) * _LengthViaMet32Met4BtwCO + 2 * max([_DRCObj._Metal1MinEnclosureVia3,_DRCObj._MetalxMinEnclosureVia3])

        print ('#############################     Met2 Layer Calculation   ##############################################')
        _LengthViaMet32Met4BtwCO = _DRCObj._VIAxMinWidth + _DRCObj.DRCVIAxMinSpace(NumOfVIAxX=_ViaMet32Met4NumberOfCOX, NumOfVIAxY=_ViaMet32Met4NumberOfCOY)
        self._DesignParameter['_Met4Layer']['_XYCoordinates'] = _XYCoordinateOfViaMet32Met4
        self._DesignParameter['_Met4Layer']['_XWidth'] = _DRCObj._VIAxMinWidth + (_ViaMet32Met4NumberOfCOX - 1) * _LengthViaMet32Met4BtwCO + 2 * max([_DRCObj._Metal1MinEnclosureVia3,_DRCObj._MetalxMinEnclosureVia3])
        self._DesignParameter['_Met4Layer']['_YWidth'] = _DRCObj._VIAxMinWidth + (_ViaMet32Met4NumberOfCOY - 1) * _LengthViaMet32Met4BtwCO + 2 * max([_DRCObj._Metal1MinEnclosureVia3,_DRCObj._MetalxMinEnclosureVia3])

        print ('#############################     Cont Layer Calculation   ##############################################')
        tmp = []
        self._DesignParameter['_COLayer']['_XWidth'] = _DRCObj._VIAxMinWidth
        self._DesignParameter['_COLayer']['_YWidth'] = _DRCObj._VIAxMinWidth
        _LengthViaMet32Met4BtwCO = _DRCObj._VIAxMinWidth + _DRCObj.DRCVIAxMinSpace(NumOfVIAxX=_ViaMet32Met4NumberOfCOX, NumOfVIAxY=_ViaMet32Met4NumberOfCOY)
        for i in range(0, _ViaMet32Met4NumberOfCOX):
            for j in range(0, _ViaMet32Met4NumberOfCOY):
                if (_ViaMet32Met4NumberOfCOX % 2) == 0 and (_ViaMet32Met4NumberOfCOY % 2) == 0:
                    _xycoordinatetmp = [_XYCoordinateOfViaMet32Met4[0][0] - (_ViaMet32Met4NumberOfCOX / 2 - 0.5) * _LengthViaMet32Met4BtwCO + i * _LengthViaMet32Met4BtwCO,
                                        _XYCoordinateOfViaMet32Met4[0][1] - (_ViaMet32Met4NumberOfCOY / 2 - 0.5) * _LengthViaMet32Met4BtwCO + j * _LengthViaMet32Met4BtwCO]
                elif (_ViaMet32Met4NumberOfCOX % 2) == 0 and (_ViaMet32Met4NumberOfCOY % 2) == 1:
                    _xycoordinatetmp = [_XYCoordinateOfViaMet32Met4[0][0] - (_ViaMet32Met4NumberOfCOX / 2 - 0.5) * _LengthViaMet32Met4BtwCO + i * _LengthViaMet32Met4BtwCO,
                                        _XYCoordinateOfViaMet32Met4[0][1] - (_ViaMet32Met4NumberOfCOY - 1) / 2 * _LengthViaMet32Met4BtwCO + j * _LengthViaMet32Met4BtwCO]
                elif (_ViaMet32Met4NumberOfCOX % 2) == 1 and (_ViaMet32Met4NumberOfCOY % 2) == 0:
                    _xycoordinatetmp = [_XYCoordinateOfViaMet32Met4[0][0] - (_ViaMet32Met4NumberOfCOX - 1) / 2 * _LengthViaMet32Met4BtwCO + i * _LengthViaMet32Met4BtwCO,
                                        _XYCoordinateOfViaMet32Met4[0][1] - (_ViaMet32Met4NumberOfCOY / 2 - 0.5) * _LengthViaMet32Met4BtwCO + j * _LengthViaMet32Met4BtwCO]
                elif (_ViaMet32Met4NumberOfCOX % 2) == 1 and (_ViaMet32Met4NumberOfCOY % 2) == 1:
                    _xycoordinatetmp = [_XYCoordinateOfViaMet32Met4[0][0] - (_ViaMet32Met4NumberOfCOX - 1) / 2 * _LengthViaMet32Met4BtwCO + i * _LengthViaMet32Met4BtwCO,
                                        _XYCoordinateOfViaMet32Met4[0][1] - (_ViaMet32Met4NumberOfCOY - 1) / 2 * _LengthViaMet32Met4BtwCO + j * _LengthViaMet32Met4BtwCO]
                tmp.append(_xycoordinatetmp)
        self._DesignParameter['_COLayer']['_XYCoordinates'] = tmp

        print ('#########################################################################################################')
        print ('                                    {}  ViaMet32Met4 Calculation End                                    '.format(self._DesignParameter['_Name']['_Name']))
        print ('#########################################################################################################')


if __name__=='__main__':
    ViaMet32Met4Obj1=_ViaMet32Met4(_DesignParameter=None, _Name='ViaMet32Met4test1')
    ViaMet32Met4Obj1._CalculateViaMet32Met4DesignParameter(_ViaMet32Met4NumberOfCOX=3, _ViaMet32Met4NumberOfCOY=4 )
    ViaMet32Met4Obj2=_ViaMet32Met4(_DesignParameter=None, _Name='ViaMet32Met4test2')
    ViaMet32Met4Obj2._CalculateViaMet32Met4DesignParameterMinimumEnclosureY(_ViaMet32Met4NumberOfCOX=3, _ViaMet32Met4NumberOfCOY=4 )
    ViaMet32Met4Obj3=_ViaMet32Met4(_DesignParameter=None, _Name='ViaMet32Met4test3')
    ViaMet32Met4Obj3._CalculateViaMet32Met4DesignParameterMinimumEnclosureX(_ViaMet32Met4NumberOfCOX=3, _ViaMet32Met4NumberOfCOY=4 )
    #ViaMet32Met4Obj=_ViaMet32Met4(_ViaMet32Met4DesignParameter=DesignParameters.ViaMet32Met4DesignParameter, _ViaMet32Met4Name='ViaMet32Met42test')
    #ViaMet32Met4Obj=_ViaMet32Met4(_Technology=DesignParameters._Technology, _XYCoordinatePbody=[0,0], _NumberOfPbodyCO=2, _WidthXPbodyOD=890, _WidthYPbodyOD=420, _WidthXPbodyNP=1250, _WidthYPbodyNP=780, _WidthPbodyCO=220, _LengthPbodyBtwCO=470, _WidthXPbodyMet3=810, _WidthYPbodyMet1=340, _PbodyName='ViaMet32Met4')
    ViaMet32Met4Obj1._UpdateDesignParameter2GDSStructure(_DesignParameterInDictionary=ViaMet32Met4Obj1._DesignParameter)
    ViaMet32Met4Obj2._UpdateDesignParameter2GDSStructure(_DesignParameterInDictionary=ViaMet32Met4Obj2._DesignParameter)
    ViaMet32Met4Obj3._UpdateDesignParameter2GDSStructure(_DesignParameterInDictionary=ViaMet32Met4Obj3._DesignParameter)

    testStreamFile=open('./testStreamFile1.gds','wb')

    tmp1=ViaMet32Met4Obj1._CreateGDSStream(ViaMet32Met4Obj1._DesignParameter['_GDSFile']['_GDSFile'])

    tmp1.write_binary_gds_stream(testStreamFile)
    testStreamFile=open('./testStreamFile2.gds','wb')

    tmp2=ViaMet32Met4Obj2._CreateGDSStream(ViaMet32Met4Obj2._DesignParameter['_GDSFile']['_GDSFile'])

    tmp2.write_binary_gds_stream(testStreamFile)

    testStreamFile=open('./testStreamFile3.gds','wb')

    tmp3=ViaMet32Met4Obj3._CreateGDSStream(ViaMet32Met4Obj3._DesignParameter['_GDSFile']['_GDSFile'])

    tmp3.write_binary_gds_stream(testStreamFile)

    testStreamFile.close()
    print ('###############open ftp connection & update gds file to cadence server###################')
    ftp_cadence_server=ftplib.FTP('141.223.86.109')
    ftp_cadence_server.login(base64.b64decode('YWxlY25ldzE='),base64.b64decode('NzNoazNhYWs='))
    if DesignParameters._Technology =='065nm':
        ftp_cadence_server.cwd('/home/alecnew1/OPUS/design_automation')
    elif DesignParameters._Technology =='180nm':
        ftp_cadence_server.cwd('/home/alecnew1/OPUS/DesignAutomationTSMC018')
    elif DesignParameters._Technology =='045nm':
        ftp_cadence_server.cwd('/home/alecnew1/OPUS/DesignAutomationTSMC45')
    print (ftp_cadence_server.pwd())
    testStreamFile=open('./testStreamFile1.gds','rb')
    ftp_cadence_server.storbinary('STOR testStreamFile1.gds', testStreamFile)
    testStreamFile.close()
    testStreamFile=open('./testStreamFile2.gds','rb')
    ftp_cadence_server.storbinary('STOR testStreamFile2.gds', testStreamFile)
    testStreamFile.close()
    testStreamFile=open('./testStreamFile3.gds','rb')
    ftp_cadence_server.storbinary('STOR testStreamFile3.gds', testStreamFile)
    testStreamFile.close()
    print ('close ftp connection')
    ftp_cadence_server.quit()
    testStreamFile.close()

    print ('##########################################################################################')