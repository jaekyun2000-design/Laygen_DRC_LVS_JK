from generatorLib.generator_models import NMOSWithDummy
from generatorLib import CoordinateCalc as CoordCalc


class _CascodeNMOS(NMOSWithDummy._NMOS):
    _ParametersForDesignCalculation = dict(_NMOSChannelWidth=None, _NMOSChannellength=None,
                                           _NMOSDummy=False, _XVT=None, _GateSpacing=None)


    def _CalculateDesignParameter(self, _NMOSChannelWidth=200, _NMOSChannellength=30,
                                           _NMOSDummy=True, _XVT='SLVT', _GateSpacing=100):

        self._CalculateNMOSDesignParameter(
            _NMOSNumberofGate=2,
            _NMOSChannelWidth=_NMOSChannelWidth, _NMOSChannellength=_NMOSChannellength,
            _NMOSDummy=_NMOSDummy, _XVT=_XVT, _GateSpacing=_GateSpacing
        )

        # Delete middle metal1 layer and contact
        XYCoordOfNMOSDrain = CoordCalc.getXYCoords_MinX(self.getXY('_Met1Layer'))
        XYCoordOfNMOSSource = CoordCalc.getXYCoords_MaxX(self.getXY('_Met1Layer'))
        self._DesignParameter['_Met1Layer']['_XYCoordinates'] = XYCoordOfNMOSDrain + XYCoordOfNMOSSource
        self._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'] = XYCoordOfNMOSDrain + XYCoordOfNMOSSource
        self._DesignParameter['_COLayer']['_XYCoordinates'] = \
            CoordCalc.getXYCoords_MinX(self.getXY('_COLayer')) + CoordCalc.getXYCoords_MaxX(self.getXY('_COLayer'))

        self._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'] = XYCoordOfNMOSSource
        self._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'] = XYCoordOfNMOSDrain
