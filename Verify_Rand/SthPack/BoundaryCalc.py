from shapely.geometry import Polygon, box
import matplotlib.pyplot as plt


def getOverlappedBoundaryElement(BoundaryElement1, BoundaryElement2):
    """
    It is usually used for Via Calculation when two metals(BoundaryElements) are overlapped.
    It cannot support PathElement
      -> Later, It can support PathElementType when only limited condition (like simple straight lines, not complicated orthogonal line).

    Caution : Every Overlapped BoundaryElements should same XYWidths. Or AssertionError will occur.

    :param BoundaryElement1: <dict('_XWidth', '_YWidth', '_XYCoordinates')>
    :param BoundaryElement2: <dict('_XWidth', '_YWidth', '_XYCoordinates')>
    :return: <dict('_XWidth', '_YWidth', '_XYCoordinates')> Overlapped BoundaryElement
    """
    overlappedMinMaxXYList = _getOverlappedMinMaxXY(MinMaxXYObj1=_BoundaryElement2MinMaxXY(BoundaryElement1),
                                                    MinMaxXYObj2=_BoundaryElement2MinMaxXY(BoundaryElement2))

    return _MinMaxXY2BoundaryElement(overlappedMinMaxXYList)


def _BoundaryElement2MinMaxXY(BoundaryElementObj):
    MinMaxXYList = []
    for XYs in BoundaryElementObj['_XYCoordinates']:
        MinMaxXYList.append((XYs[0] - BoundaryElementObj['_XWidth'] / 2.,     # minX
                             XYs[1] - BoundaryElementObj['_YWidth'] / 2.,     # minY
                             XYs[0] + BoundaryElementObj['_XWidth'] / 2.,     # maxX
                             XYs[1] + BoundaryElementObj['_YWidth'] / 2.,     # maxY
                             ))
    return MinMaxXYList


def _getOverlappedMinMaxXY(MinMaxXYObj1, MinMaxXYObj2):
    overlappedMinMaxXYList = []
    for Obj1 in MinMaxXYObj1:
        for Obj2 in MinMaxXYObj2:
            minX = max(Obj1[0], Obj2[0])
            minY = max(Obj1[1], Obj2[1])
            maxX = min(Obj1[2], Obj2[2])
            maxY = min(Obj1[3], Obj2[3])

            if minX < maxX and minY < maxY:
                overlappedMinMaxXYList.append((minX, minY, maxX, maxY))
            else:
                pass
    return overlappedMinMaxXYList


def _MinMaxXY2BoundaryElement(MinMaxXYList):
    """
            Only for same XWidth and YWidth of ALL boundList's Obj
    """

    if len(MinMaxXYList) == 0:
        return None
    else:
        BoundaryElement = dict(_XWidth=(MinMaxXYList[0][2] - MinMaxXYList[0][0]),
                               _YWidth=(MinMaxXYList[0][3] - MinMaxXYList[0][1]),
                               _XYCoordinates=[])
        for Obj in MinMaxXYList:
            assert (Obj[2] - Obj[0]) == BoundaryElement['_XWidth']
            assert (Obj[3] - Obj[1]) == BoundaryElement['_YWidth']
            BoundaryElement['_XYCoordinates'].append(
                [(Obj[2] + Obj[0]) / 2.,
                 (Obj[3] + Obj[1]) / 2.])
        return BoundaryElement


if __name__ == '__main__':
    p1 = dict()
    p1['_XWidth'] = 1000
    p1['_YWidth'] = 60
    p1['_XYCoordinates'] = [[0,0]]

    p2 = dict()
    p2['_XWidth'] = 30
    p2['_YWidth'] = 60
    p2['_XYCoordinates'] = [[0,10], [20,10], [40,10], [60,10]]

    aa = getOverlappedBoundaryElement(p1, p2)

    print(aa)
