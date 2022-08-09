from generatorLib import StickDiagram
from generatorLib import DesignParameters
from generatorLib import DRC


class ViaX(StickDiagram._StickDiagram):
    def __init__(self, X=1, _DesignParameter=None, _Name='ViaX'):
        if X not in (1,2,3,4,5,6,7):
            raise NotImplementedError

        if _DesignParameter != None:
            self._DesignParameter = _DesignParameter
        else:
            self._DesignParameter = {
                f"_Met{X+1}Layer":self._BoundaryElementDeclaration(
                    _Layer=DesignParameters._LayerMapping[f'METAL{X+1}'][0],
                    _Datatype=DesignParameters._LayerMapping[f'METAL{X+1}'][1],
                    _XYCoordinates=[], _XWidth=400, _YWidth=400),
                f"_Met{X}Layer":self._BoundaryElementDeclaration(
                    _Layer=DesignParameters._LayerMapping[f'METAL{X}'][0],
                    _Datatype=DesignParameters._LayerMapping[f'METAL{X}'][1],
                    _XYCoordinates=[], _XWidth=400, _YWidth=400),
                "_COLayer":self._BoundaryElementDeclaration(
                    _Layer=DesignParameters._LayerMapping[f'VIA{X}{X+1}'][0],
                    _Datatype=DesignParameters._LayerMapping[f'VIA{X}{X+1}'][1],
                    _XYCoordinates=[], _XWidth=400, _YWidth=400),
                "_Name":self._NameDeclaration(_Name=_Name),
                "_GDSFile":self._GDSObjDeclaration(_GDSFile=None)}
        self._DesignParameter['_Name']['Name'] = _Name
        self.ViaLayer = X

    @classmethod
    def getMinEnclosureVia(cls, MetalLayer:int):
        drc = DRC.DRC()
        MetalType = drc.getMetalType(MetalLayer)

        if MetalType == '1':
            enclosure = drc._Metal1MinEnclosureVia1
        elif MetalType == 'x':
            enclosure = drc._MetalxMinEnclosureCO
        elif MetalType == 'y':
            enclosure = drc._MetalyMinEnclosureCO
        elif MetalType == 'z':
            enclosure = drc._MetalzMinEnclosureCO
        elif MetalType == 'r':
            enclosure = drc._MetalrMinEnclosureCO
        else:
            enclosure = drc._Metal1MinEnclosureVia1

        return enclosure

    @classmethod
    def getMinEnclosureViaOpposite(cls, MetalLayer:int):
        drc = DRC.DRC()
        MetalType = drc.getMetalType(MetalLayer)

        if MetalType == '1':
            enclosure = drc._Metal1MinEnclosureVia12
        elif MetalType == 'x':
            enclosure = drc._MetalxMinEnclosureCO2
        elif MetalType == 'y':
            enclosure = drc._MetalyMinEnclosureCO2
        elif MetalType == 'z':
            enclosure = drc._MetalzMinEnclosureCO2
        elif MetalType == 'r':
            enclosure = drc._MetalrMinEnclosureCO2
        else:
            enclosure = drc._Metal1MinEnclosureVia12

        return enclosure

    @classmethod
    def getMinEnclosureViaSame(cls, MetalLayer: int):
        drc = DRC.DRC()
        MetalType = drc.getMetalType(MetalLayer)

        if MetalType == '1':
            enclosure = drc._Metal1MinEnclosureVia3
        elif MetalType == 'x':
            enclosure = drc._MetalxMinEnclosureVia3
        elif MetalType == 'y':
            enclosure = drc._MetalyMinEnclosureVia3
        elif MetalType == 'z':
            enclosure = drc._MetalzMinEnclosureVia3
        elif MetalType == 'r':
            enclosure = drc._MetalrMinEnclosureVia3
        else:
            enclosure = drc._Metal1MinEnclosureVia3

        return enclosure


    def _CalculateDesignParameterbyMode(self, XNum:int, YNum:int, Mode):
        """
        Do not use this def directly.

        Layer1: lower layer
        Layer2: upper layer

        """
        # check input arguments
        if (XNum < 1) or (YNum < 1):
            raise NotImplementedError

        drc = DRC.DRC()
        _Name = self._DesignParameter['_Name']['_Name']
        ViaLayer = 1

        # Via size
        ViaXWidth = drc._VIAxMinWidth
        ViaYWidth = ViaXWidth

        # Calculate Via Spacing        : edge-to-edge distance (calc by func. in DRC.py)
        MetalType = drc.getMetalType(ViaLayer)
        if MetalType in ('1', 'x'):
            MinSpaceBtwVia, MinSpaceBtwViaOpposite = drc.DRCVIAxMinSpace_v2(XNum, YNum)
        elif MetalType == 'y':
            MinSpaceBtwVia, MinSpaceBtwViaOpposite = drc.DRCVIAyMinSpace_v2(XNum, YNum)
        elif MetalType == 'z':
            MinSpaceBtwVia, MinSpaceBtwViaOpposite = drc.DRCVIAzMinSpace_v2(XNum, YNum)
        elif MetalType == 'r':
            MinSpaceBtwVia, MinSpaceBtwViaOpposite = drc.DRCVIArMinSpace_v2(XNum, YNum)
        else:
            raise NotImplementedError

        # Calculate Enclosure
        '''
        there are 3 types.
        when default mode,
            ss28nm -> it has same enclosure rule
            other tech -> check Number of Vias 
        '''
        Layer1MinEnclosureVia1 = self.getMinEnclosureVia(ViaLayer)
        Layer1MinEnclosureVia12 = self.getMinEnclosureViaOpposite(ViaLayer)
        Layer1MinEnclosureVia3 = self.getMinEnclosureViaSame(ViaLayer)
        Layer2MinEnclosureVia1 = self.getMinEnclosureVia(ViaLayer + 1)
        Layer2MinEnclosureVia12 = self.getMinEnclosureViaOpposite(ViaLayer + 1)
        Layer2MinEnclosureVia3 = self.getMinEnclosureViaSame(ViaLayer + 1)

        if Mode is 'MinEnclosureX':
            XSpaceBtwVias = ViaXWidth + MinSpaceBtwVia
            YSpaceBtwVias = ViaYWidth + MinSpaceBtwViaOpposite
            XEnclosureLayer1 = Layer1MinEnclosureVia1
            YEnclosureLayer1 = Layer1MinEnclosureVia12
            XEnclosureLayer2 = Layer2MinEnclosureVia1
            YEnclosureLayer2 = Layer2MinEnclosureVia12
        elif Mode is 'MinEnclosureY':
            XSpaceBtwVias = ViaXWidth + MinSpaceBtwViaOpposite
            YSpaceBtwVias = ViaYWidth + MinSpaceBtwVia
            XEnclosureLayer1 = Layer1MinEnclosureVia12
            YEnclosureLayer1 = Layer1MinEnclosureVia1
            XEnclosureLayer2 = Layer2MinEnclosureVia12
            YEnclosureLayer2 = Layer2MinEnclosureVia1
        elif Mode is 'default':
            if DesignParameters._Technology == 'SS28nm':
                XSpaceBtwVias = ViaXWidth + MinSpaceBtwVia
                YSpaceBtwVias = ViaYWidth + MinSpaceBtwViaOpposite
                XEnclosureLayer1 = Layer1MinEnclosureVia3
                YEnclosureLayer1 = Layer1MinEnclosureVia3
                XEnclosureLayer2 = Layer2MinEnclosureVia3
                YEnclosureLayer2 = Layer2MinEnclosureVia3
            else:
                if XNum >= YNum:        # 'MinEnclosureY'
                    XSpaceBtwVias = ViaXWidth + MinSpaceBtwViaOpposite
                    YSpaceBtwVias = ViaYWidth + MinSpaceBtwVia
                    XEnclosureLayer1 = Layer1MinEnclosureVia12
                    YEnclosureLayer1 = Layer1MinEnclosureVia1
                    XEnclosureLayer2 = Layer2MinEnclosureVia12
                    YEnclosureLayer2 = Layer2MinEnclosureVia1
                else:                   # 'MinEnclosureX'
                    XSpaceBtwVias = ViaXWidth + MinSpaceBtwVia
                    YSpaceBtwVias = ViaYWidth + MinSpaceBtwViaOpposite
                    XEnclosureLayer1 = Layer1MinEnclosureVia1
                    YEnclosureLayer1 = Layer1MinEnclosureVia12
                    XEnclosureLayer2 = Layer2MinEnclosureVia1
                    YEnclosureLayer2 = Layer2MinEnclosureVia12
        else:
            raise NotImplementedError

        #
        self._DesignParameter[f'_Met{self.ViaLayer}Layer']['_XYCoordinates'] = [[0,0]]
        self._DesignParameter[f'_Met{self.ViaLayer}Layer']['_XWidth'] = ViaXWidth + (XNum - 1) * XSpaceBtwVias + 2 * XEnclosureLayer1
        self._DesignParameter[f'_Met{self.ViaLayer}Layer']['_YWidth'] = ViaYWidth + (YNum - 1) * YSpaceBtwVias + 2 * YEnclosureLayer1

        self._DesignParameter[f'_Met{self.ViaLayer+1}Layer']['_XYCoordinates'] = [[0, 0]]
        self._DesignParameter[f'_Met{self.ViaLayer+1}Layer']['_XWidth'] = ViaXWidth + (XNum - 1) * XSpaceBtwVias + 2 * XEnclosureLayer2
        self._DesignParameter[f'_Met{self.ViaLayer+1}Layer']['_YWidth'] = ViaYWidth + (YNum - 1) * YSpaceBtwVias + 2 * YEnclosureLayer2

        tmpXYs = []
        for i in range(0, XNum):
            for j in range(0, YNum):
                XY = [int(-(XNum - 1) / 2 * XSpaceBtwVias + i * XSpaceBtwVias),     # need MinSnapSpacing ?
                      int(-(YNum - 1) / 2 * YSpaceBtwVias + j * YSpaceBtwVias)]
                tmpXYs.append(XY)
        self._DesignParameter['_COLayer']['_XYCoordinates'] = tmpXYs
        self._DesignParameter['_COLayer']['_XWidth'] = ViaXWidth
        self._DesignParameter['_COLayer']['_YWidth'] = ViaYWidth

    def _CalculateDesignParameter(self, XNum:int, YNum:int):
        self._CalculateDesignParameterbyMode(XNum=XNum, YNum=YNum, Mode='default')

    def _CalculateDesignParameterMinEnclosureY(self, XNum: int, YNum: int):
        self._CalculateDesignParameterbyMode(XNum=XNum, YNum=YNum, Mode='MinEnclosureY')

    def _CalculateDesignParameterMinEnclosureX(self, XNum: int, YNum: int):
        self._CalculateDesignParameterbyMode(XNum=XNum, YNum=YNum, Mode='MinEnclosureX')
