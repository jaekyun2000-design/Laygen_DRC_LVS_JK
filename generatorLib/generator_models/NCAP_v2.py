from generatorLib import StickDiagram
from generatorLib import DesignParameters
from generatorLib import DRC
from generatorLib.generator_models import ViaPoly2Met1
#from LayGenGUI.generatorLib.generator_models import PSubRing
from generatorLib.generator_models import SubRing

class _NCap(StickDiagram._StickDiagram):
    _ParametersForDesignCalculation = dict(_XWidth=None, _YWidth=None, _NumofGates=None, NumOfCOX=None, NumOfCOY=None,
                                           Guardring=False, guardring_height=None, guardring_width=None, _Thickness=None, _COpitch=None, _Enclosure=None,
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
                _Name=self._NameDeclaration(_Name=_Name), _GDSFile=self._GDSObjDeclaration(_GDSFile=None))

        if _Name != None:
            self._DesignParameter['_Name']['Name'] = _Name


    def _CalculateNCapDesignParameter(self, _XWidth=1000, _YWidth=1000, _NumofGates=3, NumOfCOX=None, NumOfCOY=None, Guardring=False, guardring_height=None, guardring_width=None, _Thickness=348, _COpitch=175, _Enclosure=None, _NumofOD=2, _ViaPoly2Met1NumberOfCOX=None, _ViaPoly2Met1NumberOfCOY=1):
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
                if _XWidth % 2 == 0 and _YWidth % 2 == 0:
                    tmp_m1poly.append([self._DesignParameter['_POLayer']['_XYCoordinates'][i][0],
                                       self._DesignParameter['_POLayer']['_XYCoordinates'][0][1] - self._DesignParameter['_POLayer']['_YWidth'] // 2 + _DRCObj._CoMinEnclosureByPOAtLeastTwoSide
                                       + 0.5 * _DRCObj._CoMinWidth + (_ViaPoly2Met1NumberOfCOY - 1) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2) // 2 + j * (_YWidth + _DRCObj._OdSpace_ncap)])
                    tmp_m1poly.append([self._DesignParameter['_POLayer']['_XYCoordinates'][i][0],
                                       self._DesignParameter['_POLayer']['_XYCoordinates'][0][1] + self._DesignParameter['_POLayer']['_YWidth'] // 2 - _DRCObj._CoMinEnclosureByPOAtLeastTwoSide
                                       - 0.5 * _DRCObj._CoMinWidth - (_ViaPoly2Met1NumberOfCOY - 1) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2) // 2 + j * (_YWidth + _DRCObj._OdSpace_ncap)])

                if _XWidth % 2 == 0 and _YWidth % 2 == 1:
                    tmp_m1poly.append([self._DesignParameter['_POLayer']['_XYCoordinates'][i][0],
                                       self._DesignParameter['_POLayer']['_XYCoordinates'][0][1] - MinSnapSpacing/2.0 - self._DesignParameter['_POLayer']['_YWidth'] // 2 + _DRCObj._CoMinEnclosureByPOAtLeastTwoSide
                                       + 0.5 * _DRCObj._CoMinWidth + (_ViaPoly2Met1NumberOfCOY - 1) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2) // 2 + j * (_YWidth + _DRCObj._OdSpace_ncap)])
                    tmp_m1poly.append([self._DesignParameter['_POLayer']['_XYCoordinates'][i][0],
                                       self._DesignParameter['_POLayer']['_XYCoordinates'][0][1] + MinSnapSpacing/2.0 + self._DesignParameter['_POLayer']['_YWidth'] // 2 - _DRCObj._CoMinEnclosureByPOAtLeastTwoSide
                                       - 0.5 * _DRCObj._CoMinWidth - (_ViaPoly2Met1NumberOfCOY - 1) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2) // 2 + j * (_YWidth + _DRCObj._OdSpace_ncap)])

                if _XWidth % 2 == 1 and _YWidth % 2 == 0:
                    tmp_m1poly.append([self._DesignParameter['_POLayer']['_XYCoordinates'][i][0] - MinSnapSpacing/2.0,
                                       self._DesignParameter['_POLayer']['_XYCoordinates'][0][1] - self._DesignParameter['_POLayer']['_YWidth'] // 2 + _DRCObj._CoMinEnclosureByPOAtLeastTwoSide
                                       + 0.5 * _DRCObj._CoMinWidth + (_ViaPoly2Met1NumberOfCOY - 1) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2) // 2 + j * (_YWidth + _DRCObj._OdSpace_ncap)])
                    tmp_m1poly.append([self._DesignParameter['_POLayer']['_XYCoordinates'][i][0] - MinSnapSpacing/2.0,
                                       self._DesignParameter['_POLayer']['_XYCoordinates'][0][1] + self._DesignParameter['_POLayer']['_YWidth'] // 2 - _DRCObj._CoMinEnclosureByPOAtLeastTwoSide
                                       - 0.5 * _DRCObj._CoMinWidth - (_ViaPoly2Met1NumberOfCOY - 1) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2) // 2 + j * (_YWidth + _DRCObj._OdSpace_ncap)])

                if _XWidth % 2 == 1 and _YWidth % 2 == 1:
                    tmp_m1poly.append([self._DesignParameter['_POLayer']['_XYCoordinates'][i][0] - MinSnapSpacing/2.0,
                                       self._DesignParameter['_POLayer']['_XYCoordinates'][0][1] - MinSnapSpacing/2.0 - self._DesignParameter['_POLayer']['_YWidth'] // 2 + _DRCObj._CoMinEnclosureByPOAtLeastTwoSide
                                       + 0.5 * _DRCObj._CoMinWidth + (_ViaPoly2Met1NumberOfCOY - 1) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2) // 2 + j * (_YWidth + _DRCObj._OdSpace_ncap)])
                    tmp_m1poly.append([self._DesignParameter['_POLayer']['_XYCoordinates'][i][0] - MinSnapSpacing/2.0,
                                       self._DesignParameter['_POLayer']['_XYCoordinates'][0][1] + MinSnapSpacing/2.0 + self._DesignParameter['_POLayer']['_YWidth'] // 2 - _DRCObj._CoMinEnclosureByPOAtLeastTwoSide
                                       - 0.5 * _DRCObj._CoMinWidth - (_ViaPoly2Met1NumberOfCOY - 1) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2) // 2 + j * (_YWidth + _DRCObj._OdSpace_ncap)])

        m1poly = []
        for i in tmp_m1poly:
            if i not in m1poly:
                m1poly.append(i)
        m1poly.sort()

        self._DesignParameter['Viapoly2Met1H']['_XYCoordinates'] = m1poly
        del tmp_m1poly


        tmp_m1od = []
        for j in range(_NumofOD):
            for i in range(_NumofGates):
                if _XWidth % 2 == 0 and _YWidth % 2 == 0:
                    tmp_m1od.append([self._DesignParameter['_POLayer']['_XYCoordinates'][i][0] - self._DesignParameter['_POLayer']['_XWidth'] // 2 - _DRCObj._CoMinSpace
                                     - 0.5 * _DRCObj._CoMinWidth - (_ViaPoly2Met1NumberOfCOY - 1) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace) // 2,
                                     self._DesignParameter['_POLayer']['_XYCoordinates'][0][1] + j * (_YWidth + _DRCObj._OdSpace_ncap)])
                    tmp_m1od.append([self._DesignParameter['_POLayer']['_XYCoordinates'][i][0] + self._DesignParameter['_POLayer']['_XWidth'] // 2 + _DRCObj._CoMinSpace
                                     + 0.5 * _DRCObj._CoMinWidth - (_ViaPoly2Met1NumberOfCOY - 1) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace) // 2,
                                     self._DesignParameter['_POLayer']['_XYCoordinates'][0][1] + j * (_YWidth + _DRCObj._OdSpace_ncap)])

                if _XWidth % 2 == 0 and _YWidth % 2 == 1:
                    tmp_m1od.append([self._DesignParameter['_POLayer']['_XYCoordinates'][i][0] - self._DesignParameter['_POLayer']['_XWidth'] // 2 - _DRCObj._CoMinSpace
                                     - 0.5 * _DRCObj._CoMinWidth - (_ViaPoly2Met1NumberOfCOY - 1) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace) // 2,
                                     self._DesignParameter['_POLayer']['_XYCoordinates'][0][1] - MinSnapSpacing/2.0 + j * (_YWidth + _DRCObj._OdSpace_ncap)])
                    tmp_m1od.append([self._DesignParameter['_POLayer']['_XYCoordinates'][i][0] + self._DesignParameter['_POLayer']['_XWidth'] // 2 + _DRCObj._CoMinSpace
                                     + 0.5 * _DRCObj._CoMinWidth - (_ViaPoly2Met1NumberOfCOY - 1) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace) // 2,
                                     self._DesignParameter['_POLayer']['_XYCoordinates'][0][1] - MinSnapSpacing/2.0 + j * (_YWidth + _DRCObj._OdSpace_ncap)])

                if _XWidth % 2 == 1 and _YWidth % 2 == 0:
                    tmp_m1od.append([self._DesignParameter['_POLayer']['_XYCoordinates'][i][0] - MinSnapSpacing/2.0 - self._DesignParameter['_POLayer']['_XWidth'] // 2 - _DRCObj._CoMinSpace
                                     - 0.5 * _DRCObj._CoMinWidth - (_ViaPoly2Met1NumberOfCOY - 1) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace) // 2,
                                     self._DesignParameter['_POLayer']['_XYCoordinates'][0][1] + j * (_YWidth + _DRCObj._OdSpace_ncap)])
                    tmp_m1od.append([self._DesignParameter['_POLayer']['_XYCoordinates'][i][0] + MinSnapSpacing/2.0 + self._DesignParameter['_POLayer']['_XWidth'] // 2 + _DRCObj._CoMinSpace
                                     + 0.5 * _DRCObj._CoMinWidth - (_ViaPoly2Met1NumberOfCOY - 1) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace) // 2,
                                     self._DesignParameter['_POLayer']['_XYCoordinates'][0][1] + j * (_YWidth + _DRCObj._OdSpace_ncap)])

                if _XWidth % 2 == 1 and _YWidth % 2 == 1:
                    tmp_m1od.append([self._DesignParameter['_POLayer']['_XYCoordinates'][i][0] - MinSnapSpacing/2.0 - self._DesignParameter['_POLayer']['_XWidth'] // 2 - _DRCObj._CoMinSpace
                                     - 0.5 * _DRCObj._CoMinWidth - (_ViaPoly2Met1NumberOfCOY - 1) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace) // 2,
                                     self._DesignParameter['_POLayer']['_XYCoordinates'][0][1] - MinSnapSpacing/2.0 + j * (_YWidth + _DRCObj._OdSpace_ncap)])
                    tmp_m1od.append([self._DesignParameter['_POLayer']['_XYCoordinates'][i][0] + MinSnapSpacing/2.0 + self._DesignParameter['_POLayer']['_XWidth'] // 2 + _DRCObj._CoMinSpace
                                     + 0.5 * _DRCObj._CoMinWidth - (_ViaPoly2Met1NumberOfCOY - 1) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace) // 2,
                                     self._DesignParameter['_POLayer']['_XYCoordinates'][0][1] - MinSnapSpacing/2.0 + j * (_YWidth + _DRCObj._OdSpace_ncap)])

        m1od = []
        for i in tmp_m1od:
            if i not in m1od:
                m1od.append(i)
        m1od.sort()

        self._DesignParameter['Viapoly2Met1V']['_XYCoordinates'] = m1od
        del tmp_m1od



        print('#############################     LVS Layer Calculation    ##############################################')
        self._DesignParameter['LVSLayer']=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['LVS_dr4'][0],
                                                                    _Datatype=DesignParameters._LayerMapping['LVS_dr4'][1],
                                                                    _XWidth=self._DesignParameter['_ODLayer']['_XYCoordinates'][-1][0] - self._DesignParameter['_ODLayer']['_XYCoordinates'][0][0] + self._DesignParameter['_ODLayer']['_XWidth'] + _DRCObj._CoMinEnclosureByPOAtLeastTwoSide * 2,
                                                                    _YWidth=self._DesignParameter['_POLayer']['_XYCoordinates'][-1][1] - self._DesignParameter['_POLayer']['_XYCoordinates'][0][1] + self._DesignParameter['_POLayer']['_YWidth'] + _DRCObj._CoMinEnclosureByPOAtLeastTwoSide * 2)
        self._DesignParameter['LVSLayer']['_XYCoordinates'] = _XYCoordinatesofNcap



        print('#############################     NWELL Layer Calculation    ##############################################')
        self._DesignParameter['NWELL']=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['NWELL'][0], _Datatype=DesignParameters._LayerMapping['NWELL'][1],
                                                                _XWidth=self._DesignParameter['_POLayer']['_XYCoordinates'][-1][0] - self._DesignParameter['_POLayer']['_XYCoordinates'][0][0] + self._DesignParameter['_POLayer']['_XWidth'] + 2 * _DRCObj._PolygateMinEnclosureByNcap,
                                                                _YWidth=self._DesignParameter['_POLayer']['_XYCoordinates'][-1][1] - self._DesignParameter['_POLayer']['_XYCoordinates'][0][1] + self._DesignParameter['_ODLayer']['_YWidth'] + 2 * _DRCObj._PolygateMinEnclosureByNcap)
        self._DesignParameter['NWELL']['_XYCoordinates'] = self._DesignParameter['LVSLayer']['_XYCoordinates']



        print('#############################     NCAP Layer Calculation    ##############################################')
        self._DesignParameter['NCAPLayer']=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['NCAP'][0], _Datatype=DesignParameters._LayerMapping['NCAP'][1],
                                                                    _XWidth=self._DesignParameter['NWELL']['_XWidth'], _YWidth=self._DesignParameter['NWELL']['_YWidth'])
        self._DesignParameter['NCAPLayer']['_XYCoordinates'] = self._DesignParameter['LVSLayer']['_XYCoordinates']



        print('#############################     Guardring Calculation    ##############################################')
        if Guardring == True :
            self._DesignParameter['guardring']=self._SrefElementDeclaration(_DesignObj=SubRing._SubRing(_Name='PSubRingIn{}'.format(_Name)))[0]
            self._DesignParameter['guardring']['_DesignObj']._CalculateDesignParameter(**dict(_Psubtype=True, _MetalOpen=None, _Height=5000, _Width=3000, _Thickness=_Thickness, _COpitch=_COpitch, _Enclosure=_Enclosure))

            if guardring_width == None :
                # guardring_Xwidth=self._DesignParameter['NCAPLayer']['_XWidth']+self._DesignParameter['guardring']['_DesignObj']._DesignParameter['right']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth']/2+self._DesignParameter['guardring']['_DesignObj']._DesignParameter['left']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth']/2+2*_DRCObj._NwMinSpacetoRX
                guardring_Xwidth=self._DesignParameter['NCAPLayer']['_XWidth']+2*_DRCObj._NwMinSpacetoRX

            elif guardring_width != None :
                guardring_Xwidth=guardring_width

            if guardring_height == None :
                # guardring_Yheight=self._DesignParameter['NCAPLayer']['_YWidth']+self._DesignParameter['guardring']['_DesignObj']._DesignParameter['top']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth']/2+self._DesignParameter['guardring']['_DesignObj']._DesignParameter['bot']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth']/2+2*_DRCObj._NwMinSpacetoRX
                guardring_Yheight=self._DesignParameter['NCAPLayer']['_YWidth']+2*_DRCObj._NwMinSpacetoRX

            elif guardring_height != None :
                guardring_Yheight=guardring_height

            self._DesignParameter['guardring']['_DesignObj']._CalculateDesignParameter(**dict(_Psubtype=True, _MetalOpen=None, _Height=guardring_Yheight, _Width=guardring_Xwidth, _Thickness=_Thickness, _COpitch=_COpitch, _Enclosure=_Enclosure))
            self._DesignParameter['guardring']['_XYCoordinates']=self._DesignParameter['NCAPLayer']['_XYCoordinates']

            # if guardring_Xwidth < self._DesignParameter['NWELL']['_XWidth']+self._DesignParameter['guardring']['_DesignObj']._DesignParameter['right']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth']/2+self._DesignParameter['guardring']['_DesignObj']._DesignParameter['left']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth']/2+2*_DRCObj._NwMinSpacetoRX :
            #     raise NotImplementedError
            # if guardring_Yheight < self._DesignParameter['NWELL']['_YWidth']+self._DesignParameter['guardring']['_DesignObj']._DesignParameter['top']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth']/2+self._DesignParameter['guardring']['_DesignObj']._DesignParameter['bot']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth']/2+2*_DRCObj._NwMinSpacetoRX :
            #     raise NotImplementedError
