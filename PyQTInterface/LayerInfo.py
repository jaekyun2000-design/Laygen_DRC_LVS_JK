import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

class _Layer():
    _LayerName = []
    _Layer = dict()
    _DataType = dict()

    _LayerName.append("M1")
    _LayerName.append("M2")
    _LayerName.append("M3")
    _LayerName.append("M4")

    i =1
    for keysName in _LayerName:
        _Layer[keysName] =i
        _DataType[keysName] =i
        i = i+1


    #_Layer[_LayerName] = 3
    #_DataType[_LayerName] = 10