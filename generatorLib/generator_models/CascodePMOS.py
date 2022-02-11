from generatorLib.generator_models import PMOSWithDummy
from generatorLib import CoordinateCalc as CoordCalc


class _CascodePMOS(PMOSWithDummy._PMOS):
    _ParametersForDesignCalculation = dict(_PMOSChannelWidth=None, _PMOSChannellength=None,
                                           _PMOSDummy=False, _XVT=None, _GateSpacing=None)


    def _CalculateDesignParameter(self, _PMOSChannelWidth=200, _PMOSChannellength=30,
                                           _PMOSDummy=True, _XVT='SLVT', _GateSpacing=100):

        self._CalculatePMOSDesignParameter(
            _PMOSNumberofGate=2,
            _PMOSChannelWidth=_PMOSChannelWidth, _PMOSChannellength=_PMOSChannellength,
            _PMOSDummy=_PMOSDummy, _XVT=_XVT, _GateSpacing=_GateSpacing
        )

        # Delete middle metal1 layer and contact
        XYCoordOfPMOSDrain = CoordCalc.getXYCoords_MinX(self.getXY('_Met1Layer'))
        XYCoordOfPMOSSource = CoordCalc.getXYCoords_MaxX(self.getXY('_Met1Layer'))
        self._DesignParameter['_Met1Layer']['_XYCoordinates'] = XYCoordOfPMOSDrain + XYCoordOfPMOSSource
        self._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'] = XYCoordOfPMOSDrain + XYCoordOfPMOSSource
        self._DesignParameter['_COLayer']['_XYCoordinates'] = \
            CoordCalc.getXYCoords_MinX(self.getXY('_COLayer')) + CoordCalc.getXYCoords_MaxX(self.getXY('_COLayer'))

        self._DesignParameter['_XYCoordinatePMOSSupplyRouting']['_XYCoordinates'] = XYCoordOfPMOSSource
        self._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'] = XYCoordOfPMOSDrain
