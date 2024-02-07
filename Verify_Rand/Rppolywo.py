import StickDiagram
import DesignParameters
import user_define_exceptions
import DRC
import copy
import ftplib
from ftplib import FTP
import base64

class _RPPOLYWOSegment(StickDiagram._StickDiagram):
    _ParametersForDesignCalculation=dict(_NumberOfCOY=None,  _ResXWidth=None, _ResYWidth=None)
    #_ParametersForDesignCalculation= dict(_NMOSNumberofGate=None, _NMOSChannelWidth=None, _NMOSChannellength=None )
    def __init__(self, _DesignParameter=None, _Name=None):

        if _DesignParameter!=None:
            self._DesignParameter=_DesignParameter
        else :
            self._DesignParameter = dict(
                                                    _POLayer=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0],_Datatype=DesignParameters._LayerMapping['POLY'][1], _XYCoordinates=[],_XWidth=400, _YWidth=400),
                                                    _Met1Layer=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0],_Datatype=DesignParameters._LayerMapping['METAL1'][1], _XYCoordinates=[],_XWidth=400, _YWidth=400),
                                                    _PPLayer=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['PIMP'][0],_Datatype=DesignParameters._LayerMapping['PIMP'][1], _XYCoordinates=[],_XWidth=400, _YWidth=400),
                                                    _COLayer=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['CONT'][0],_Datatype=DesignParameters._LayerMapping['CONT'][1], _XYCoordinates=[],_XWidth=400, _YWidth=400),
                                                    _RHLayer=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['RH'][0],_Datatype=DesignParameters._LayerMapping['RH'][1], _XYCoordinates=[],_XWidth=400, _YWidth=400),
                                                    _RPOLayer=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['RPO'][0],_Datatype=DesignParameters._LayerMapping['RPO'][1], _XYCoordinates=[],_XWidth=400, _YWidth=400),
                                                    _RPDMYLayer=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['RPDMY'][0],_Datatype=DesignParameters._LayerMapping['RPDMY'][1], _XYCoordinates=[],_XWidth=400, _YWidth=400),
                                                    _Name=dict(_DesignParametertype=5,_Name='RPPOLYWOSegment'), _GDSFile=dict(_DesignParametertype=4, _GDSFile=None),
                                                    _XYCoordinatePort1Routing=dict(_DesignParametertype=7,_XYCoordinates=[]),_XYCoordinatePort2Routing=dict(_DesignParametertype=7,_XYCoordinates=[]),


                                                   )



        if _Name != None:
            self._DesignParameter['_Name']['_Name']=_Name

    def _CalculateDesignParameter(self, _NumberOfCOY=None,  _ResXWidth=None, _ResYWidth=None):
        _DRCObj=DRC.DRC()
        _MinSnapSpacing = _DRCObj._MinSnapSpacing
        ###############################################Check the number of CO ###########################################################################################
        if _NumberOfCOY ==0 :
            print ('************************* Error occured in {} Design Parameter Calculation******************************'.format(self._DesignParameter['_Name']['_Name']))
            if DesignParameters._DebugMode == 0:
                return 0
        ###############################################################################################################################################################################
        ###############################################Check the Res size###########################################################################################
        if _ResXWidth==0 or _ResYWidth==0:
            print ('************************* Error occured in {} Design Parameter Calculation******************************'.format(self._DesignParameter['_Name']['_Name']))
            if DesignParameters._DebugMode == 0:
                return 0
        ###############################################################################################################################################################################
        if _ResXWidth % (2 * _MinSnapSpacing) != 0 or _ResYWidth % (2 * _MinSnapSpacing) != 0 :
            raise Exception ("Design Rule Error!!")
        _XYCoordinateOfTheDesign = [[0,0]]

        print ('#############################     Cont Layer Calculation   ##############################################')


        self._DesignParameter['_COLayer']['_XWidth'] = _DRCObj._CoMinWidth
        self._DesignParameter['_COLayer']['_YWidth'] = _DRCObj._CoMinWidth
        _NumberOfCOX = int(int(_ResXWidth - 2*_DRCObj._CoMinEnclosureByPOAtLeastTwoSide + _DRCObj._CoMinSpace)/(_DRCObj._CoMinWidth + _DRCObj._CoMinSpace))
        if (2 < _NumberOfCOX and 2 <=_NumberOfCOY) or (2 <=_NumberOfCOX and 2 <_NumberOfCOY):
            _NumberOfCOX = int(int(_ResXWidth - 2*_DRCObj._CoMinEnclosureByPOAtLeastTwoSide + _DRCObj._CoMinSpace2)/(_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2))

        ###############################################Check the number of CO ###########################################################################################
        if _NumberOfCOX ==0 :
            print ('************************* Error occured in {} Design Parameter Calculation******************************'.format(self._DesignParameter['_Name']['_Name']))
            if DesignParameters._DebugMode == 0:
                return 0
        ###############################################################################################################################################################################
        
        print ('#############################     POLY Layer Calculation    ##############################################')
        _LengthBtwCO = _DRCObj._CoMinWidth + _DRCObj.DRCCOMinSpace(NumOfCOX=_NumberOfCOY,NumOfCOY=_NumberOfCOX )
        tmp=[]
        _LengthBtwCO = _DRCObj._CoMinWidth + _DRCObj.DRCCOMinSpace(NumOfCOX=_NumberOfCOY,NumOfCOY=_NumberOfCOX )
        self._DesignParameter['_POLayer']['_XWidth']= _ResXWidth 
        self._DesignParameter['_POLayer']['_YWidth']= _ResYWidth + (_DRCObj._CoMinWidth + (_NumberOfCOY - 1)* _LengthBtwCO+ _DRCObj._CoMinEnclosureByPOAtLeastTwoSide + _DRCObj._RPOMinSpace2CO) * 2
        self._DesignParameter['_POLayer']['_XYCoordinates'] = [[_XYCoordinateOfTheDesign[0][0], _XYCoordinateOfTheDesign[0][1]]]

        ## CO layer coordinate settings
        #print 'testMonitor for debugging: '
        for i in range(0, _NumberOfCOY):
            #print 'testMonitor for debugging: ', i, _NumberOfCOX
            for j in range(0, _NumberOfCOX):
                if (_NumberOfCOX % 2) == 0:
                    #print 'testMonitor for debugging: ', i, j
                    _xycoordinatetmp = [_XYCoordinateOfTheDesign[0][0] - (_NumberOfCOX / 2 - 0.5 )*_LengthBtwCO + j*_LengthBtwCO,
                                            _XYCoordinateOfTheDesign[0][1] - _ResYWidth // 2 - _DRCObj._RPOMinSpace2CO - float(_DRCObj._CoMinWidth)/2 - i * _LengthBtwCO]

                    tmp.append(_xycoordinatetmp)
                    _xycoordinatetmp = [_XYCoordinateOfTheDesign[0][0] - (_NumberOfCOX / 2 - 0.5 )*_LengthBtwCO + j*_LengthBtwCO,
                                        _XYCoordinateOfTheDesign[0][1] + _ResYWidth // 2  + float(_DRCObj._CoMinWidth)/2  + \
                                         _DRCObj._RPOMinSpace2CO + i * _LengthBtwCO] 
                else:
                    _xycoordinatetmp = [_XYCoordinateOfTheDesign[0][0] - (_NumberOfCOX  - 1 )/2*_LengthBtwCO + j*_LengthBtwCO,
                                            _XYCoordinateOfTheDesign[0][1] - _ResYWidth // 2 -  _DRCObj._RPOMinSpace2CO - float(_DRCObj._CoMinWidth)/2 - i * _LengthBtwCO]

                    tmp.append(_xycoordinatetmp)
                    _xycoordinatetmp = [_XYCoordinateOfTheDesign[0][0] - (_NumberOfCOX - 1 )/2*_LengthBtwCO + j*_LengthBtwCO,
                                        _XYCoordinateOfTheDesign[0][1] + _ResYWidth // 2 + float(_DRCObj._CoMinWidth)/2 + \
                                        _DRCObj._RPOMinSpace2CO + i * _LengthBtwCO]

                tmp.append(_xycoordinatetmp)
        self._DesignParameter['_COLayer']['_XYCoordinates']=tmp


        
        print ('#############################     RPDMY Layer Calculation    ##############################################')
        self._DesignParameter['_RPDMYLayer']['_XWidth']= _ResXWidth
        self._DesignParameter['_RPDMYLayer']['_YWidth']= _ResYWidth
        self._DesignParameter['_RPDMYLayer']['_XYCoordinates'] = self._DesignParameter['_POLayer']['_XYCoordinates']

        print ('#############################     METAL1 Layer Calculation    ##############################################')
        _LengthBtwCO = _DRCObj._CoMinWidth + _DRCObj.DRCCOMinSpace(NumOfCOX=_NumberOfCOY,NumOfCOY=_NumberOfCOX )
        self._DesignParameter['_Met1Layer']['_XWidth']= _LengthBtwCO*(_NumberOfCOX - 1) + _DRCObj._CoMinWidth + _DRCObj._Metal1MinEnclosureCO2 * 2
        self._DesignParameter['_Met1Layer']['_YWidth']= _LengthBtwCO*(_NumberOfCOY - 1) + _DRCObj._CoMinWidth + _DRCObj._Metal1MinEnclosureCO2 * 2
        tmp1 = _XYCoordinateOfTheDesign[0][1] - _ResYWidth // 2 - _DRCObj._RPOMinSpace2CO - float(_DRCObj._CoMinWidth)/2
        tmp2 = _XYCoordinateOfTheDesign[0][1] + _ResYWidth // 2 + float(_DRCObj._CoMinWidth)/2 + _DRCObj._RPOMinSpace2CO
        tmp3 = _XYCoordinateOfTheDesign[0][1] - _ResYWidth // 2 - _DRCObj._RPOMinSpace2CO - float(_DRCObj._CoMinWidth)/2 - (_NumberOfCOY - 1) * _LengthBtwCO
        tmp4 = _XYCoordinateOfTheDesign[0][1] + _ResYWidth // 2 + float(_DRCObj._CoMinWidth)/2 + _DRCObj._RPOMinSpace2CO + (_NumberOfCOY - 1) * _LengthBtwCO
        
        self._DesignParameter['_Met1Layer']['_XYCoordinates'] = [[_XYCoordinateOfTheDesign[0][0],self.CeilMinSnapSpacing((tmp1 + tmp3)//2, 2*_MinSnapSpacing)],
                                                                 [_XYCoordinateOfTheDesign[0][0],self.CeilMinSnapSpacing((tmp2 + tmp4)//2, 2*_MinSnapSpacing)]]
        self._DesignParameter['_XYCoordinatePort1Routing']['_XYCoordinates'] = [self._DesignParameter['_Met1Layer']['_XYCoordinates'][0]]
        self._DesignParameter['_XYCoordinatePort2Routing']['_XYCoordinates'] = [self._DesignParameter['_Met1Layer']['_XYCoordinates'][1]]


        print ('#############################     RPO Layer Calculation    ##############################################')
        self._DesignParameter['_RPOLayer']['_XWidth']= _ResXWidth + 2* _DRCObj.DRCRPOMinExtensionOnPO(_Width= _ResYWidth)
        self._DesignParameter['_RPOLayer']['_YWidth']= _ResYWidth 
        self._DesignParameter['_RPOLayer']['_XYCoordinates'] = self._DesignParameter['_POLayer']['_XYCoordinates']

        print ('#############################     PPO Layer Calculation    ##############################################')
        self._DesignParameter['_PPLayer']['_XWidth']= self._DesignParameter['_POLayer']['_XWidth'] + 2 * _DRCObj._PpMinEnclosureOfPtypePoRes
        self._DesignParameter['_PPLayer']['_YWidth']= self._DesignParameter['_POLayer']['_YWidth'] + 2 * _DRCObj._PpMinEnclosureOfPo
        self._DesignParameter['_PPLayer']['_XYCoordinates'] = self._DesignParameter['_POLayer']['_XYCoordinates']

        if (DesignParameters._Technology != '045nm') :
            print ('#############################     RHO Layer Calculation    ##############################################')
            self._DesignParameter['_RHLayer']['_XWidth']= self._DesignParameter['_PPLayer']['_XWidth']
            self._DesignParameter['_RHLayer']['_YWidth']= self._DesignParameter['_PPLayer']['_YWidth']
            self._DesignParameter['_RHLayer']['_XYCoordinates'] = self._DesignParameter['_POLayer']['_XYCoordinates']

        else :
            print ('#############################     RHO Layer Calculation    ##############################################')
            self._DesignParameter['_RHLayer']['_XWidth']= self._DesignParameter['_POLayer']['_XWidth'] + _DRCObj._RHMinExtensionOnPO * 2
            self._DesignParameter['_RHLayer']['_YWidth']= self._DesignParameter['_POLayer']['_YWidth'] + _DRCObj._RHMinExtensionOnPO * 2
            self._DesignParameter['_RHLayer']['_XYCoordinates'] = self._DesignParameter['_POLayer']['_XYCoordinates']


if __name__=='__main__':
    polyres= _RPPOLYWOSegment(_DesignParameter=None, _Name='PolyResSegment')
    polyres._CalculateDesignParameter(_NumberOfCOY=1,  _ResXWidth=1800, _ResYWidth=2000)
    #NMOSObj=_NMOS(_NMOSDesignParameter=DesignParameters.NMOSDesignParamter, _NMOSName='NMOS2')
    #NMOSObj=_NMOS(_Technology=DesignParameters._Technology, _XYCoordinatePbody=[0,0], _NumberOfPbodyCO=2, _WidthXPbodyOD=890, _WidthYPbodyOD=420, _WidthXPbodyNP=1250, _WidthYPbodyNP=780, _WidthPbodyCO=220, _LengthPbodyBtwCO=470, _WidthXPbodyMet1=810, _WidthYPbodyMet1=340, _PbodyName='NMOS')
    polyres._UpdateDesignParameter2GDSStructure(_DesignParameterInDictionary=polyres._DesignParameter)
    testStreamFile=open('./testStreamFile.gds','wb')

    tmp=polyres._CreateGDSStream(polyres._DesignParameter['_GDSFile']['_GDSFile'])

    tmp.write_binary_gds_stream(testStreamFile)

    testStreamFile.close()

    print ('###############################    Transporting to FTP server    ########################################')
    ftp = ftplib.FTP('141.223.22.156')
    ftp.login('junung', 'chlwnsdnd1!')
    ftp.cwd('/mnt/sdc/junung/OPUS/TSMC65n')
    #ftp.cwd('/mnt/sdc/junung/OPUS/Samsung28n')
    myfile = open('testStreamFile.gds', 'rb')
    ftp.storbinary('STOR testStreamFile.gds', myfile)
    myfile.close()
    ftp.close()