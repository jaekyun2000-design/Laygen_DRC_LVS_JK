import warnings



def Add(Coordinate1, Coordinate2):
    x = Coordinate1[0] + Coordinate2[0]
    y = Coordinate1[1] + Coordinate2[1]

    return [x, y]


def Sum(*Coordinates):
    """ Add all XYCoordinates

    Args:
        Coordinates (list[int | float]): XYCoordinates. ex) [[-3,0], [-1,1], [1,2], [3,3]]
    Returns:
        list[int | float]: One XYCoordinate by obtained by adding all XYCoordinates
    Example:
        >>> Sum([-3,0], [-1,1], [1,2], [3,3])
        [0, 6]
    """
    x, y = 0, 0     # Initialize
    for XY in Coordinates:
        _isCoordinate(XY)
        x = x + XY[0]
        y = y + XY[1]

    return [x, y]


def CenterBtw2Coords(Coordinate1, Coordinate2):
    x = (Coordinate1[0] + Coordinate2[0]) / 2.
    y = (Coordinate1[1] + Coordinate2[1]) / 2.

    return [x, y]


def FlipX(Coordinate):
    return [-Coordinate[0], Coordinate[1]]


def FlipY(Coordinate):
    return [Coordinate[0], -Coordinate[1]]


def FlipXY(Coordinate):
    return [-Coordinate[0], -Coordinate[1]]


def FlipXs(Coordinates):
    tmpXYs = []
    for XY in Coordinates:
        tmpXYs.append([-XY[0], XY[1]])
    return tmpXYs


def FlipYs(Coordinates):
    tmpXYs = []
    for XY in Coordinates:
        tmpXYs.append([XY[0], -XY[1]])
    return tmpXYs


def FlipXYs(Coordinates):
    tmpXYs = []
    for XY in Coordinates:
        tmpXYs.append([-XY[0], -XY[1]])
    return tmpXYs


def MinMaxXY(Coordinates):
    x_list, y_list = [], []
    for XY in Coordinates:
        _isCoordinate(XY)
        x_list.append(XY[0])
        y_list.append(XY[1])

    return min(x_list), min(y_list), max(x_list), max(y_list)


def getXYCoords_MinY(Coordinates):
    XYList = []
    referenceMinY = None

    for XY in Coordinates:
        _isCoordinate(XY)
        if referenceMinY is None:         # initial
            referenceMinY = XY[1]
            XYList.append(XY)
        else:
            if XY[1] < referenceMinY:     # New MinimumY
                referenceMinY = XY[1]
                XYList = [XY]
            elif XY[1] == referenceMinY:  # Same with MinimumY
                XYList.append(XY)
            else:                         # bigger than MinimumY
                pass
    return XYList


def getXYCoords_MinX(Coordinates):
    XYList = []
    referenceMinX = None

    for XY in Coordinates:
        _isCoordinate(XY)
        if referenceMinX is None:         # initial
            referenceMinX = XY[0]
            XYList.append(XY)
        else:
            if XY[0] < referenceMinX:     # New MinimumX
                referenceMinX = XY[0]
                XYList = [XY]
            elif XY[0] == referenceMinX:  # Same with MinimumX
                XYList.append(XY)
            else:                         # bigger than MinimumX
                pass
    return XYList


def getXYCoords_MaxX(Coordinates):
    XYList = []
    referenceMaxX = None

    for XY in Coordinates:
        _isCoordinate(XY)
        if referenceMaxX is None:         # initial
            referenceMaxX = XY[0]
            XYList.append(XY)
        else:
            if XY[0] > referenceMaxX:     # New MaximumX
                referenceMaxX = XY[0]
                XYList = [XY]
            elif XY[0] == referenceMaxX:  # Same with MaximumX
                XYList.append(XY)
            else:                         # smaller than MaximumX
                pass
    return XYList


def getXYCoords_MaxY(Coordinates):
    XYList = []
    referenceMaxY = None

    for XY in Coordinates:
        _isCoordinate(XY)
        if referenceMaxY is None:         # initial
            referenceMaxY = XY[1]
            XYList.append(XY)
        else:
            if XY[1] > referenceMaxY:     # New MaximumY
                referenceMaxY = XY[1]
                XYList = [XY]
            elif XY[1] == referenceMaxY:  # Same with MaximumY
                XYList.append(XY)
            else:                         # smaller than MaximumY
                pass
    return XYList


def getSortedList_ascending(Coordinates):
    """ Return sorted set list of the each X and Y of XYCoordinates.\n
    The first tuple contains X coordinates in ascending order and no duplicates.
    The second tuple contains Y Coordinates in ascending order and no duplicates.\n
    It can be used to find the minimum or maximum values of the X or Y Coordinates without knowing how they are ordered.

    Args:
        Coordinates (list[list[int | float]]): XYCoordinates. ex) [[-3,0], [-1,0], [1,0], [3,0]]
    Returns:
        tuple[list[int | float], list[int | float]]: [X coordinates sorted in ascending order], [Y coordinates sorted in ascending order]
    Example:
        >>> getSortedList_ascending([[-3,0], [0,1], [3,-5], [3,1]])
        [-3, 0, 3], [-5, 0, 1]
    """
    xList, yList = [], []
    for XY in Coordinates:
        _isCoordinate(XY)
        xList.append(XY[0])
        yList.append(XY[1])

    return sorted(set(xList)), sorted(set(yList))


def getDistanceBtwMinMaxX(Coordinates):
    """ Calculate the distance between maxX and minX.

    Args:
        Coordinates (list[list[int | float]]): XYCoordinates. ex) [[-3,-3], [-1,-3], [1,3], [3,3]]
    Returns:
        [int | float]: Distance between Min-Max XCoordinates.
    Example:
        >>> getDistanceBtwMinMaxX([[-3,-3], [-1,-3], [1,3], [3,3]])
        6
    """
    xList, _ = getSortedList_ascending(Coordinates)
    Distance = xList[-1] - xList[0]

    if len(xList) == 1:
        warnings.warn("Only one XCoordinate is inputted.")
    elif Distance == 0:
        warnings.warn("The Distance between MaxX and MinX is calculated as 'zero'.")

    return Distance


def getDistanceBtwMinMaxY(Coordinates):
    """ Calculate the distance between maxY and minY.

    Args:
        Coordinates (list[list[int | float]]): XYCoordinates. ex) [[-3,-3], [-1,-3], [1,3], [3,3]]
    Returns:
        [int | float]: Distance between Min-Max YCoordinates.
    Example:
        >>> getDistanceBtwMinMaxY([[-3,-3], [-1,-3], [1,3], [3,3]])
        6
    """
    _, yList = getSortedList_ascending(Coordinates)
    Distance = yList[-1] - yList[0]

    if len(yList) == 1:
        warnings.warn("Only one YCoordinate is inputted.")
    elif Distance == 0:
        warnings.warn("The Distance between MaxY and MinY is calculated as 'zero'.")

    return Distance


def _isCoordinate(Coordinate):
    assert isinstance(Coordinate, list), 'Expected list. But {}'.format(type(Coordinate))
    assert len(Coordinate) == 2, 'Expected two element. But {}.'.format(len(Coordinate))
    for i in Coordinate:
        assert isinstance(i, (int, float)), 'Expected number. But {}.'.format(i)


# testbench
if __name__ == '__main__':

    # value1 = [1, 3]
    # value2 = [2, 5]
    #
    # results = Add(value1, value2)

    XYCoordinatesqq = [[3,5], [1,5], [-1,5], [4,5], [0,-1], [0,-1], [-3,-1]]
    results = Sum([3,5], [1,5], [-1,5])

    kk = getDistanceBtwMinMaxY([[0, 1]])
    type_ = type(kk)

    print(type_)
    print(kk)
