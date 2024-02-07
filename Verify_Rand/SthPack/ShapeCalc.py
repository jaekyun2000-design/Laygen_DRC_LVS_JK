from shapely.geometry import Polygon, box, MultiPolygon
import matplotlib.pyplot as plt
import shapely.ops as so
import math


def _Boundary2Polygon(Boundary):
    PolygonList = []
    for XYs in Boundary['_XYCoordinates']:
        PolygonList.append(
            box(XYs[0] - Boundary['_XWidth'] / 2,     # minX
                XYs[1] - Boundary['_YWidth'] / 2,     # minY
                XYs[0] + Boundary['_XWidth'] / 2,     # maxX
                XYs[1] + Boundary['_YWidth'] / 2)     # maxY
        )
    return MultiPolygon(PolygonList)


def _MultiPolygon2MultiBoundary(MultiPolygon):

    assert MultiPolygon.geom_type == 'MultiPolygon'

    MultiBoundaryElement = []
    for Polygon in multipolygon1.geoms:
        MultiBoundaryElement.append(_Polygon2Boundary(Polygon))

    return MultiBoundaryElement


def _Polygon2Boundary(Polygon):
    assert Polygon.geom_type == 'Polygon'
    assert _isRectangle(Polygon)

    (minx, miny, maxx, maxy) = Polygon.bounds
    Boundary = dict(_XWidth=maxx - minx,
                    _YWidth=maxy - miny,
                    _XYCoordinates=[(minx + maxx) / 2, (miny + maxy) / 2])

    return Boundary


def _isRectangle(poly):
    if math.isclose(poly.minimum_rotated_rectangle.area, poly.area):
        return True
    else:
        return False

if __name__ == '__main__':
    plt.rcParams["figure.figsize"] = [7.00, 3.50]
    plt.rcParams["figure.autolayout"] = True


    b1 = dict()
    b1['_XWidth'] = 1000
    b1['_YWidth'] = 60
    b1['_XYCoordinates'] = [[0,0]]

    b2 = dict()
    b2['_XWidth'] = 20
    b2['_YWidth'] = 80
    b2['_XYCoordinates'] = [[0,0], [100,0], [200,0], [300,0]]

    p1 = _Boundary2Polygon(b1)
    p2 = _Boundary2Polygon(b2)

    p3 = p1.difference(p2)


    multipolygon1 = p3

    print(multipolygon1)
    for Polygon1 in multipolygon1.geoms:
        print(Polygon1.bounds)

    kk = _MultiPolygon2MultiBoundary(multipolygon1)

    ''' plot '''
    fig, axs = plt.subplots()
    axs.set_aspect('equal', 'datalim')

    for geom in multipolygon1.geoms:
        xs, ys = geom.exterior.xy
        axs.fill(xs, ys, alpha=0.5, fc='r', ec='none')

    plt.show()