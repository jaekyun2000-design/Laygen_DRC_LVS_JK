## ################################################################################################################### Pre-defined: Coordination
_XYCoordinateOfViaPoly2Met1 = [[0, 0]]

## ################################################################################################################### NotImplemented condition
if _ViaMet02Met1NumberOfCOX == 0 or _ViaMet02Met1NumberOfCOY == 0:
    print(('**** Error occured in {} Design Parameter Calculation****'.format(self._DesignParameter['_Name']['_Name'])))
    if DesignParameters._DebugMode == 0:
        return 0

    ## ################################################################################################################### POLY Layer
# Define Boundary_element
self._DesignParameter['BND_POLayer'] = self._BoundaryElementDeclaration(
    _Layer=DesignParameters._LayerMapping['POLY'][0],
    _Datatype=DesignParameters._LayerMapping['POLY'][1],
    _XWidth=None,
    _YWidth=None,
    _XYCoordinates=[],
)
# Define _LengthViaPoly2Met1BtwCO: Co center to center distance
_LengthViaPoly2Met1BtwCO = _DRCObj._CoMinWidth + _DRCObj.DRCCOMinSpace(NumOfCOX=_ViaMet02Met1NumberOfCOX,
                                                                       NumOfCOY=_ViaMet02Met1NumberOfCOY)

# Define Boundary_element _YWidth
self._DesignParameter['BND_POLayer']['_YWidth'] = _DRCObj._CoMinWidth + (
            _ViaMet02Met1NumberOfCOY - 1) * _LengthViaPoly2Met1BtwCO + 2 * _DRCObj._CoMinEnclosureByPOAtLeastTwoSide

# Define Boundary_element _XWidth
self._DesignParameter['BND_POLayer']['_XWidth'] = _DRCObj._CoMinWidth + (
            _ViaMet02Met1NumberOfCOX - 1) * _LengthViaPoly2Met1BtwCO + 2 * _DRCObj._CoMinEnclosureByPOAtLeastTwoSide

# Define Boundary_element Coordinates
self._DesignParameter['BND_POLayer']['_XYCoordinates'] = _XYCoordinateOfViaPoly2Met1

## ################################################################################################################### Metal1 Layer
# Define Boundary_element
self._DesignParameter['BND_Met1Layer'] = self._BoundaryElementDeclaration(
    _Layer=DesignParameters._LayerMapping['METAL1'][0],
    _Datatype=DesignParameters._LayerMapping['METAL1'][1],
    _XWidth=None,
    _YWidth=None,
    _XYCoordinates=[],
)
# Define _LengthViaPoly2Met1BtwCO
_LengthViaPoly2Met1BtwCO = _DRCObj._CoMinWidth + _DRCObj.DRCCOMinSpace(NumOfCOX=_ViaMet02Met1NumberOfCOX,
                                                                       NumOfCOY=_ViaMet02Met1NumberOfCOY)

# Define Boundary_element _YWidth
self._DesignParameter['BND_Met1Layer']['_YWidth'] = _DRCObj._CoMinWidth + (
            _ViaMet02Met1NumberOfCOY - 1) * _LengthViaPoly2Met1BtwCO + 2 * _DRCObj._Metal1MinEnclosureCO2

# Define Boundary_element _XWidth
self._DesignParameter['BND_Met1Layer']['_XWidth'] = _DRCObj._CoMinWidth + (
            _ViaMet02Met1NumberOfCOX - 1) * _LengthViaPoly2Met1BtwCO + 2 * _DRCObj._Metal1MinEnclosureCO2

# Define Boundary_element Coordinates
self._DesignParameter['BND_Met1Layer']['_XYCoordinates'] = _XYCoordinateOfViaPoly2Met1

## ################################################################################################################### Metal1Layer and POLYLayer placement: size of two layer could be different
# change xcoord
if self._DesignParameter['BND_Met1Layer']['_XWidth'] >= self._DesignParameter['BND_POLayer']['_XWidth']:
    _Xwidth_diff = abs(
        self._DesignParameter['BND_Met1Layer']['_XWidth'] - self._DesignParameter['BND_POLayer']['_XWidth'])
    _Xcoord = np.round(_Xwidth_diff / 2)
    self._DesignParameter['BND_POLayer']['_XYCoordinates'][0][0] = \
    self._DesignParameter['BND_POLayer']['_XYCoordinates'][0][0] + _Xcoord
else:
    _Xwidth_diff = abs(self._DesignParameter['BND_POLayer']['_XWidth']) - abs(
        self._DesignParameter['BND_Met1Layer']['_XWidth'])
    _Xcoord = np.round(_Xwidth_diff / 2)
    self._DesignParameter['BND_Met1Layer']['_XYCoordinates'][0][0] = \
    self._DesignParameter['BND_Met1Layer']['_XYCoordinates'][0][0] + _Xcoord

# change ycoord
if self._DesignParameter['BND_Met1Layer']['_YWidth'] >= self._DesignParameter['BND_POLayer']['_YWidth']:
    _Ywidth_diff = abs(
        self._DesignParameter['BND_Met1Layer']['_YWidth'] - self._DesignParameter['BND_POLayer']['_YWidth'])
    _Ycoord = np.round(_Ywidth_diff / 2)
    self._DesignParameter['BND_POLayer']['_XYCoordinates'][0][1] = \
    self._DesignParameter['BND_POLayer']['_XYCoordinates'][0][1] + _Ycoord
else:
    _Ywidth_diff = abs(self._DesignParameter['BND_POLayer']['_YWidth']) - abs(
        self._DesignParameter['BND_Met1Layer']['_YWidth'])
    _Ycoord = np.round(_Ywidth_diff / 2)
    self._DesignParameter['BND_Met1Layer']['_XYCoordinates'][0][1] = \
    self._DesignParameter['BND_Met1Layer']['_XYCoordinates'][0][1] + _Ycoord

    ## ################################################################################################################### CONT Layer
# Define Boundary_element
self._DesignParameter['BND_COLayer'] = self._BoundaryElementDeclaration(
    _Layer=DesignParameters._LayerMapping['CONT'][0],
    _Datatype=DesignParameters._LayerMapping['CONT'][1],
    _XWidth=None,
    _YWidth=None,
    _XYCoordinates=[],
)

# Define Boundary_element _YWidth
self._DesignParameter['BND_COLayer']['_YWidth'] = _DRCObj._CoMinWidth

# Define Boundary_element _XWidth
self._DesignParameter['BND_COLayer']['_XWidth'] = _DRCObj._CoMinWidth

# Define _LengthViaPoly2Met1BtwCO
_LengthViaPoly2Met1BtwCO = _DRCObj._CoMinWidth + _DRCObj.DRCCOMinSpace(NumOfCOX=_ViaMet02Met1NumberOfCOX,
                                                                       NumOfCOY=_ViaMet02Met1NumberOfCOY)

# Define Boundary_element Coordinates
# Calculate coordinates
tmp = []
for i in range(0, _ViaMet02Met1NumberOfCOX):
    for j in range(0, _ViaMet02Met1NumberOfCOY):

        if self._DesignParameter['BND_Met1Layer']['_XWidth'] >= self._DesignParameter['BND_POLayer']['_XWidth']:
            if self._DesignParameter['BND_Met1Layer']['_YWidth'] >= self._DesignParameter['BND_POLayer']['_YWidth']:
                _xycoordinatetmp = [_XYCoordinateOfViaPoly2Met1[0][0] +]
            else:

        else:
            if self._DesignParameter['BND_Met1Layer']['_YWidth'] >= self._DesignParameter['BND_POLayer'][
                '_YWidth']:

            else:

        tmp.append(_xycoordinatetmp)

    # Define coordinates
self._DesignParameter['BND_COLayer']['_XYCoordinates'] = tmp

del _DRCObj


