from generatorLib import StickDiagram
from generatorLib import DesignParameters
import copy
import math
from generatorLib import DRC
from generatorLib.generator_models import ViaPoly2Met1
from generatorLib.generator_models import PSubRing

class _NCap(StickDiagram._StickDiagram):
    _ParametersForDesignCalculation = dict(_XWidth=None, _YWidth=None, _NumofGates=None, NumOfCOX=None, NumOfCOY=None,
                                           Guardring=False, guardring_height=None, guardring_width=None, guardring_right=None, guardring_left=None, guardring_top=None, guardring_bot=None,
                                           _NumofOD=None, _ViaPoly2Met1NumberOfCOX=None, _ViaPoly2Met1NumberOfCOY=None) # Added
    def __init__(self, _DesignParameter=None, _Name='NCap'):
        if _DesignParameter != None:
            self._DesignParameter = _DesignParameter
        else:
            self._DesignParameter = dict(
                _POLayer=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0],
                                                          _Datatype=DesignParameters._LayerMapping['POLY'][1],
                                                          _XYCoordinates=[], _XWidth=400, _YWidth=400),
                _ODLayer=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['DIFF'][0],
                                                          _Datatype=DesignParameters._LayerMapping['DIFF'][1],
                                                          _XYCoordinates=[], _XWidth=400, _YWidth=400),
                _Met1Layer1=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0],
                                                             _Datatype=DesignParameters._LayerMapping['METAL1'][1],
                                                             _XYCoordinates=[], _XWidth=400, _YWidth=400),
                _Met1Layer2=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0],
                                                             _Datatype=DesignParameters._LayerMapping['METAL1'][1],
                                                             _XYCoordinates=[], _XWidth=400, _YWidth=400),
                _COLayer=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['CONT'][0],
                                                          _Datatype=DesignParameters._LayerMapping['CONT'][1],
                                                          _XYCoordinates=[], _XWidth=400, _YWidth=400),
                _Name=self._NameDeclaration(_Name=_Name), _GDSFile=self._GDSObjDeclaration(_GDSFile=None),
                _XYCoordinateM1inPO=dict(_DesignParametertype=7, _XYCoordinates=[]),
                _XYCoordinateM1inOD=dict(_DesignParametertype=7, _XYCoordinates=[]))

        if _Name != None:
            self._DesignParameter['_Name']['Name'] = _Name


    def _CalculateNCapDesignParameter(self, _XWidth=1000, _YWidth=1000, _NumofGates=3, NumOfCOX=None, NumOfCOY=None, Guardring=False, guardring_height=None, guardring_width=None, guardring_right=2, guardring_left=2, guardring_top=2, guardring_bot=2, _NumofOD=2, _ViaPoly2Met1NumberOfCOX=None, _ViaPoly2Met1NumberOfCOY=1):
        print('#########################################################################################################')
        print('                                    {}  ncap_b Calculation Start                                       '.format(self._DesignParameter['_Name']['_Name']))
        print('#########################################################################################################')

        _DRCObj = DRC.DRC()
        _Name = self._DesignParameter['_Name']['_Name']
        MinSnapSpacing = _DRCObj._MinSnapSpacing

        if _XWidth % 2 == 0 and _YWidth % 2 == 0 :
            _XYCoordinatesofNcap = [[0,0]]
        elif _XWidth % 2 == 0 and _YWidth % 2 == 1 :
            _XYCoordinatesofNcap = [[0, MinSnapSpacing/2.0]]
        elif _XWidth % 2 == 1 and _YWidth % 2 == 0 :
            _XYCoordinatesofNcap = [[MinSnapSpacing/2.0,0]]
        elif _XWidth % 2 == 1 and _YWidth % 2 == 1 :
            _XYCoordinatesofNcap = [[MinSnapSpacing/2.0,MinSnapSpacing/2.0]]

        print('#############################     POLY Layer Calculation    ##############################################')
        _DRCgatemaxarea = _DRCObj._PolygateMaxArea
        ODExtensionOnPO = (_DRCObj._OdMinSpace + _DRCObj._CoMinWidth + 2 * _DRCObj._CoMinEnclosureByPOAtLeastTwoSide) * 2 # (80 + 40 + 20) * 2

        self._DesignParameter['_POLayer']['_XWidth'] = _XWidth
        # min XWidth = 30nm
        if DesignParameters == 'SS28nm':
            if _XWidth < _DRCObj._PolygateMinWidth:
                raise NotImplementedError("Xwidth should be longer than 30nm")

        self._DesignParameter['_POLayer']['_YWidth'] = _YWidth + ODExtensionOnPO

        if DesignParameters == 'SS28nm':
            if _XWidth * _YWidth > _DRCgatemaxarea:
                raise NotImplementedError("poly max area should be less than 38.661um2")

        tmp = []
        if _NumofGates % 2 == 0 and _NumofOD % 2 == 0:
            for j in range(_NumofOD):
                for i in range(_NumofGates):
                    tmp.append([_XYCoordinatesofNcap[0][0] - ((_NumofGates - 1) // 2 + 0.5) * (self._DesignParameter['_POLayer']['_XWidth'] + ODExtensionOnPO // 2 + _DRCObj._PolygateMinSpace2OD) + i * (self._DesignParameter['_POLayer']['_XWidth'] + ODExtensionOnPO // 2 + _DRCObj._PolygateMinSpace2OD),
                                _XYCoordinatesofNcap[0][1] - ((_NumofOD - 1) // 2 + 0.5) * (_YWidth + _DRCObj._OdSpace_ncap) + j * (_YWidth + _DRCObj._OdSpace_ncap)])
        if _NumofGates % 2 == 0 and _NumofOD % 2 == 1:
            for j in range(_NumofOD):
                for i in range(_NumofGates):
                    tmp.append([_XYCoordinatesofNcap[0][0] - ((_NumofGates - 1) // 2 + 0.5) * (self._DesignParameter['_POLayer']['_XWidth'] + ODExtensionOnPO // 2 + _DRCObj._PolygateMinSpace2OD) + i * (self._DesignParameter['_POLayer']['_XWidth'] + ODExtensionOnPO // 2 + _DRCObj._PolygateMinSpace2OD),
                                _XYCoordinatesofNcap[0][1] - (_NumofOD - 1) // 2 * (_YWidth + _DRCObj._OdSpace_ncap) + j * (_YWidth + _DRCObj._OdSpace_ncap)])
        if _NumofGates % 2 == 1 and _NumofOD % 2 == 0:
            for j in range(_NumofOD):
                for i in range(_NumofGates):
                    tmp.append([_XYCoordinatesofNcap[0][0] - (_NumofGates - 1) // 2 * (self._DesignParameter['_POLayer']['_XWidth'] + ODExtensionOnPO // 2 + _DRCObj._PolygateMinSpace2OD) + i * (self._DesignParameter['_POLayer']['_XWidth'] + ODExtensionOnPO // 2 + _DRCObj._PolygateMinSpace2OD),
                                _XYCoordinatesofNcap[0][1] - ((_NumofOD - 1) // 2 + 0.5) * (_YWidth + _DRCObj._OdSpace_ncap) + j * (_YWidth + _DRCObj._OdSpace_ncap)])
        if _NumofGates % 2 == 1 and _NumofOD % 2 == 1:
            for j in range(_NumofOD):
                for i in range(_NumofGates):
                    tmp.append([_XYCoordinatesofNcap[0][0] - (_NumofGates - 1) // 2 * (self._DesignParameter['_POLayer']['_XWidth'] + ODExtensionOnPO // 2 + _DRCObj._PolygateMinSpace2OD) + i * (self._DesignParameter['_POLayer']['_XWidth'] + ODExtensionOnPO // 2 + _DRCObj._PolygateMinSpace2OD),
                                _XYCoordinatesofNcap[0][1] - (_NumofOD - 1) // 2 * (_YWidth + _DRCObj._OdSpace_ncap) + j * (_YWidth + _DRCObj._OdSpace_ncap)])

        self._DesignParameter['_POLayer']['_XYCoordinates'] = tmp
        del tmp


        print('#############################     OD Layer Calculation    ################################################')

        self._DesignParameter['_ODLayer']['_XWidth'] = _XWidth + ODExtensionOnPO
        self._DesignParameter['_ODLayer']['_YWidth'] = _YWidth
        # min YWidth = 80nm
        if DesignParameters._Technology == 'SS28nm':
            if _YWidth < _DRCObj._OdMinWidth:
                raise NotImplementedError("Ywidth should be longer than 80nm")

        self._DesignParameter['_ODLayer']['_XYCoordinates'] = self._DesignParameter['_POLayer']['_XYCoordinates']


        print('#############################     CONT Layer Calculation    ##############################################')

        self._DesignParameter['Viapoly2Met1H'] = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_Name='Viapoly2Met1HIn{}'.format(_Name)))[0]
        self._DesignParameter['Viapoly2Met1H']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(**dict(_ViaPoly2Met1NumberOfCOX=max(1, int(_DRCObj.DRCCOFillAtPoly2Met1(XWidth=_XWidth, YWidth=ODExtensionOnPO, NumOfCOX=NumOfCOX, NumOfCOY=NumOfCOY)[0])),
                                                                                                          _ViaPoly2Met1NumberOfCOY=_ViaPoly2Met1NumberOfCOY))

        self._DesignParameter['Viapoly2Met1H']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] = _DRCObj._Metal1MinWidth
        self._DesignParameter['Viapoly2Met1H']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] = _DRCObj._Metal1MinWidth

        self._DesignParameter['Viapoly2Met1V'] = self._SrefElementDeclaration(_Reflect = [1,0,0], _Angle=0, _DesignObj=ViaPoly2Met1._ViaPoly2Met1(_Name='Viapoly2Met1VIn{}'.format(_Name)))[0]
        self._DesignParameter['Viapoly2Met1V']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(**dict(_ViaPoly2Met1NumberOfCOX=_ViaPoly2Met1NumberOfCOY,
                                                                                                          _ViaPoly2Met1NumberOfCOY=max(1, int(_DRCObj.DRCCOFillAtOD2Met1(XWidth = ODExtensionOnPO,  YWidth = _YWidth, NumOfCOX = NumOfCOX, NumOfCOY=NumOfCOY)[1]))))

        self._DesignParameter['Viapoly2Met1V']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] = 0
        self._DesignParameter['Viapoly2Met1V']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] = 0

        tmp_m1poly = []
        for j in range(_NumofOD):
            for i in range(_NumofGates):
                tmp_m1poly.append([self._DesignParameter['_POLayer']['_XYCoordinates'][i][0],
                                   self._DesignParameter['_POLayer']['_XYCoordinates'][0][1] - self._DesignParameter['_POLayer']['_YWidth'] // 2 + _DRCObj._CoMinEnclosureByPOAtLeastTwoSide
                                   + 0.5 * _DRCObj._CoMinWidth + (_ViaPoly2Met1NumberOfCOY - 1) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2) // 2 + j * (_YWidth + _DRCObj._OdSpace_ncap)])
                tmp_m1poly.append([self._DesignParameter['_POLayer']['_XYCoordinates'][i][0],
                                   self._DesignParameter['_POLayer']['_XYCoordinates'][0][1] + self._DesignParameter['_POLayer']['_YWidth'] // 2 - _DRCObj._CoMinEnclosureByPOAtLeastTwoSide
                                   - 0.5 * _DRCObj._CoMinWidth - (_ViaPoly2Met1NumberOfCOY - 1) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2) // 2 + j * (_YWidth + _DRCObj._OdSpace_ncap)])

        self._DesignParameter['Viapoly2Met1H']['_XYCoordinates'] = tmp_m1poly
        del tmp_m1poly

        tmp_m1od = []
        for j in range(_NumofOD):
            for i in range(_NumofGates):
                tmp_m1od.append([self._DesignParameter['_POLayer']['_XYCoordinates'][i][0] - self._DesignParameter['_POLayer']['_XWidth'] // 2 - _DRCObj._CoMinSpace
                                 - 0.5 * _DRCObj._CoMinWidth - (_ViaPoly2Met1NumberOfCOY - 1) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace) // 2,
                                 self._DesignParameter['_POLayer']['_XYCoordinates'][0][1] + j * (_YWidth + _DRCObj._OdSpace_ncap)])
                tmp_m1od.append([self._DesignParameter['_POLayer']['_XYCoordinates'][i][0] + self._DesignParameter['_POLayer']['_XWidth'] // 2 + _DRCObj._CoMinSpace
                                 + 0.5 * _DRCObj._CoMinWidth - (_ViaPoly2Met1NumberOfCOY - 1) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace) // 2,
                                 self._DesignParameter['_POLayer']['_XYCoordinates'][0][1] + j * (_YWidth + _DRCObj._OdSpace_ncap)])

        # tmp_m1od = list(set(map(tuple, tmp_m1od)))
        self._DesignParameter['Viapoly2Met1V']['_XYCoordinates'] = tmp_m1od
        del tmp_m1od



        # LVS만 수정하면 됨
        self._DesignParameter['LVSLayer']=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['LVS_dr4'][0],
                                                                    _Datatype=DesignParameters._LayerMapping['LVS_dr4'][1],
                                                                    _XWidth=self._DesignParameter['_ODLayer']['_XYCoordinates'][-1][0] - self._DesignParameter['_ODLayer']['_XYCoordinates'][0][0] + self._DesignParameter['_ODLayer']['_XWidth'] + _DRCObj._CoMinEnclosureByPOAtLeastTwoSide * 2,
                                                                    _YWidth=self._DesignParameter['_POLayer']['_XYCoordinates'][-1][1] - self._DesignParameter['_POLayer']['_XYCoordinates'][0][1] + self._DesignParameter['_POLayer']['_YWidth'] + _DRCObj._CoMinEnclosureByPOAtLeastTwoSide * 2)
        self._DesignParameter['LVSLayer']['_XYCoordinates'] = _XYCoordinatesofNcap



        self._DesignParameter['NWELL']=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['NWELL'][0], _Datatype=DesignParameters._LayerMapping['NWELL'][1],
                                                                _XWidth=self._DesignParameter['_POLayer']['_XYCoordinates'][-1][0] - self._DesignParameter['_POLayer']['_XYCoordinates'][0][0] + self._DesignParameter['_POLayer']['_XWidth'] + 2 * _DRCObj._PolygateMinEnclosureByNcap,
                                                                _YWidth=self._DesignParameter['_POLayer']['_XYCoordinates'][-1][1] - self._DesignParameter['_POLayer']['_XYCoordinates'][0][1] + self._DesignParameter['_ODLayer']['_YWidth'] + 2 * _DRCObj._PolygateMinEnclosureByNcap)
        self._DesignParameter['NWELL']['_XYCoordinates'] = self._DesignParameter['LVSLayer']['_XYCoordinates']



        self._DesignParameter['NCAPLayer']=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['NCAP'][0], _Datatype=DesignParameters._LayerMapping['NCAP'][1],
                                                                    _XWidth=self._DesignParameter['NWELL']['_XWidth'], _YWidth=self._DesignParameter['NWELL']['_YWidth'])
        self._DesignParameter['NCAPLayer']['_XYCoordinates'] = self._DesignParameter['LVSLayer']['_XYCoordinates']



        if Guardring == True :
            self._DesignParameter['guardring']=self._SrefElementDeclaration(_DesignObj=PSubRing.PSubRing(_Name='PSubRingIn{}'.format(_Name)))[0]
            self._DesignParameter['guardring']['_DesignObj']._CalculateDesignParameter(**dict(height=5000, width=3000, contact_bottom=guardring_left, contact_top=guardring_top, contact_left=guardring_left, contact_right=guardring_right))

            if guardring_width == None :
                guardring_Xwidth=self._DesignParameter['NCAPLayer']['_XWidth']+self._DesignParameter['guardring']['_DesignObj']._DesignParameter['right']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth']/2+self._DesignParameter['guardring']['_DesignObj']._DesignParameter['left']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth']/2+2*_DRCObj._NwMinSpacetoRX

            elif guardring_width != None :
                guardring_Xwidth=guardring_width

            if guardring_height == None :
                guardring_Yheight=self._DesignParameter['NCAPLayer']['_YWidth']+self._DesignParameter['guardring']['_DesignObj']._DesignParameter['top']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth']/2+self._DesignParameter['guardring']['_DesignObj']._DesignParameter['bot']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth']/2+2*_DRCObj._NwMinSpacetoRX

            elif guardring_height != None :
                guardring_Yheight=guardring_height

            self._DesignParameter['guardring']['_DesignObj']._CalculateDesignParameter(**dict(height=guardring_Yheight, width=guardring_Xwidth, contact_bottom=guardring_bot, contact_top=guardring_top, contact_left=guardring_left, contact_right=guardring_right))
            self._DesignParameter['guardring']['_XYCoordinates']=self._DesignParameter['NCAPLayer']['_XYCoordinates']

            if guardring_Xwidth < self._DesignParameter['NWELL']['_XWidth']+self._DesignParameter['guardring']['_DesignObj']._DesignParameter['right']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth']/2+self._DesignParameter['guardring']['_DesignObj']._DesignParameter['left']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth']/2+2*_DRCObj._NwMinSpacetoRX :
                raise NotImplementedError
            if guardring_Yheight < self._DesignParameter['NWELL']['_YWidth']+self._DesignParameter['guardring']['_DesignObj']._DesignParameter['top']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth']/2+self._DesignParameter['guardring']['_DesignObj']._DesignParameter['bot']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth']/2+2*_DRCObj._NwMinSpacetoRX :
                raise NotImplementedError

if __name__ == '__main__':
    import random
    # for i in range(1):
    _XWidth=1000#random.randrange(40,2000, 2)
    _YWidth=1000#random.randrange(80,2000, 2)
    _NumofGates=3#random.randint(1,20)
    _NumofOD=3#random.randint(1,20)
    # print('num of drc=',i)
    # print('_XWidth=', _XWidth)
    # print('_YWidth=', _YWidth)
    # print('_NumofGates=', _NumofGates)
    # print('_NumofOD=', _NumofOD)

    NumOfCOX=None
    NumOfCOY=None
    Guardring=True
    guardring_height=None
    guardring_width=None
    guardring_right=2
    guardring_left=2
    guardring_top=2
    guardring_bot=2
    _ViaPoly2Met1NumberOfCOX = None
    _ViaPoly2Met1NumberOfCOY = 1

    DesignParameters._Technology = 'SS28nm'
    TopObj = _NCap(_DesignParameter=None, _Name='_NCap')
    TopObj._CalculateNCapDesignParameter(_XWidth=_XWidth, _YWidth=_YWidth, _NumofGates=_NumofGates, NumOfCOX=NumOfCOX, NumOfCOY=NumOfCOY,
                                         Guardring=Guardring, guardring_height=guardring_height, guardring_width=guardring_width, guardring_right=guardring_right, guardring_left=guardring_left, guardring_top=guardring_top, guardring_bot=guardring_bot,
                                         _NumofOD=_NumofOD, _ViaPoly2Met1NumberOfCOX=_ViaPoly2Met1NumberOfCOX, _ViaPoly2Met1NumberOfCOY=_ViaPoly2Met1NumberOfCOY)
    TopObj._UpdateDesignParameter2GDSStructure(_DesignParameterInDictionary=TopObj._DesignParameter)
    testStreamFile = open('./_NCap.gds', 'wb')
    tmp = TopObj._CreateGDSStream(TopObj._DesignParameter['_GDSFile']['_GDSFile'])
    tmp.write_binary_gds_stream(testStreamFile)
    testStreamFile.close()

    print('#############################      Sending to FTP Server...      ##############################')

    import ftplib

    ftp = ftplib.FTP('141.223.29.62')
    ftp.login('smlim96', 'min753531')
    ftp.cwd('/mnt/sdc/smlim96/OPUS/ss28')
    myfile = open('_NCap.gds', 'rb')
    ftp.storbinary('STOR _NCap.gds', myfile)
    myfile.close()

    import DRCchecker
    a = DRCchecker.DRCchecker('smlim96','min753531','/mnt/sdc/smlim96/OPUS/ss28','/mnt/sdc/smlim96/OPUS/ss28/DRC/run','_SummerBottom','_SummerBottom',None)
    a.DRCchecker()

    print ("DRC Clean!!!")