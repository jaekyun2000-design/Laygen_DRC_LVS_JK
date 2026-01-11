from generatorLib import StickDiagram
from generatorLib import DesignParameters
import copy
import math
from generatorLib import DRC

class vpnp(StickDiagram._StickDiagram):
    def __init__(self, _DesignParameter=None, _Name='vpnp'):
        if _DesignParameter != None:
            self._DesignParameter = _DesignParameter
        else:
            self._DesignParameter = dict(_Name=self._NameDeclaration(_Name=_Name), _GDSFile=self._GDSObjDeclaration(_GDSFile=None))
        self._DesignParameter['_Name']['Name'] = _Name

    def _CalculateDesignParameter(self,W=3200):

        drc = DRC.DRC()
        _Name = self._DesignParameter['_Name']['_Name']

        self._DesignParameter['DIFF_boundary_6'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['DIFF'][0], _Datatype=DesignParameters._LayerMapping['DIFF'][1], _XWidth=W, _YWidth=W)
        self._DesignParameter['DIFF_boundary_6']['_XYCoordinates'] = [[(0),0]]
        self._DesignParameter['NWELL_boundary_0'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['NWELL'][0], _Datatype=DesignParameters._LayerMapping['NWELL'][1], _XWidth=(W + 1504), _YWidth=(W + 1504))
        self._DesignParameter['NWELL_boundary_0']['_XYCoordinates'] = [[(+ self._DesignParameter['DIFF_boundary_6']['_XYCoordinates'][0][0]), (+ self._DesignParameter['DIFF_boundary_6']['_XYCoordinates'][0][1])]]
        self._DesignParameter['PIMP_boundary_3'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['PIMP'][0], _Datatype=DesignParameters._LayerMapping['PIMP'][1], _XWidth=(W + 140), _YWidth=(W + 140))
        self._DesignParameter['PIMP_boundary_3']['_XYCoordinates'] = [[(+ self._DesignParameter['DIFF_boundary_6']['_XYCoordinates'][0][0]), (+ self._DesignParameter['DIFF_boundary_6']['_XYCoordinates'][0][1])]]
        self._DesignParameter['BIPOLAR_boundary_0'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['BIPOLAR'][0], _Datatype=DesignParameters._LayerMapping['BIPOLAR'][1], _XWidth=(W + 1504), _YWidth=(W + 1504))
        self._DesignParameter['BIPOLAR_boundary_0']['_XYCoordinates'] = [[(+ self._DesignParameter['DIFF_boundary_6']['_XYCoordinates'][0][0]), (+ self._DesignParameter['DIFF_boundary_6']['_XYCoordinates'][0][1])]]
        self._DesignParameter['DIFF_boundary_0'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['DIFF'][0], _Datatype=DesignParameters._LayerMapping['DIFF'][1], _XWidth=340, _YWidth=(W + (356 * 2)))
        self._DesignParameter['DIFF_boundary_0']['_XYCoordinates'] = [[((self._DesignParameter['DIFF_boundary_6']['_XYCoordinates'][0][0] + (W / 2)) + 526), self._DesignParameter['DIFF_boundary_6']['_XYCoordinates'][0][1]]]
        self._DesignParameter['DIFF_boundary_4'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['DIFF'][0], _Datatype=DesignParameters._LayerMapping['DIFF'][1], _XWidth=340, _YWidth=(W + (356 * 2)))
        self._DesignParameter['DIFF_boundary_4']['_XYCoordinates'] = [[((self._DesignParameter['DIFF_boundary_6']['_XYCoordinates'][0][0] - (W / 2)) - 526), self._DesignParameter['DIFF_boundary_6']['_XYCoordinates'][0][1]]]
        self._DesignParameter['DIFF_boundary_7'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['DIFF'][0], _Datatype=DesignParameters._LayerMapping['DIFF'][1], _XWidth=(W + (696 * 2)), _YWidth=340)
        self._DesignParameter['DIFF_boundary_7']['_XYCoordinates'] = [[self._DesignParameter['DIFF_boundary_6']['_XYCoordinates'][0][0], ((self._DesignParameter['DIFF_boundary_6']['_XYCoordinates'][0][1] + (W / 2)) + 526)]]
        self._DesignParameter['DIFF_boundary_3'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['DIFF'][0], _Datatype=DesignParameters._LayerMapping['DIFF'][1], _XWidth=(W + (696 * 2)), _YWidth=340)
        self._DesignParameter['DIFF_boundary_3']['_XYCoordinates'] = [[self._DesignParameter['DIFF_boundary_6']['_XYCoordinates'][0][0], ((self._DesignParameter['DIFF_boundary_6']['_XYCoordinates'][0][1] - (W / 2)) - 526)]]
        self._DesignParameter['DIFF_boundary_1'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['DIFF'][0], _Datatype=DesignParameters._LayerMapping['DIFF'][1], _XWidth=480, _YWidth=(W + (1196 * 2)))
        self._DesignParameter['DIFF_boundary_1']['_XYCoordinates'] = [[((self._DesignParameter['DIFF_boundary_6']['_XYCoordinates'][0][0] + (W / 2)) + 1436), self._DesignParameter['DIFF_boundary_6']['_XYCoordinates'][0][1]]]
        self._DesignParameter['DIFF_boundary_2'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['DIFF'][0], _Datatype=DesignParameters._LayerMapping['DIFF'][1], _XWidth=480, _YWidth=(W + (1196 * 2)))
        self._DesignParameter['DIFF_boundary_2']['_XYCoordinates'] = [[((self._DesignParameter['DIFF_boundary_6']['_XYCoordinates'][0][0] - (W / 2)) - 1436), self._DesignParameter['DIFF_boundary_6']['_XYCoordinates'][0][1]]]
        self._DesignParameter['DIFF_boundary_8'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['DIFF'][0], _Datatype=DesignParameters._LayerMapping['DIFF'][1], _XWidth=(W + (1676 * 2)), _YWidth=480)
        self._DesignParameter['DIFF_boundary_8']['_XYCoordinates'] = [[self._DesignParameter['DIFF_boundary_6']['_XYCoordinates'][0][0], ((self._DesignParameter['DIFF_boundary_6']['_XYCoordinates'][0][1] + (W / 2)) + 1436)]]
        self._DesignParameter['DIFF_boundary_5'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['DIFF'][0], _Datatype=DesignParameters._LayerMapping['DIFF'][1], _XWidth=(W + (1676 * 2)), _YWidth=480)
        self._DesignParameter['DIFF_boundary_5']['_XYCoordinates'] = [[self._DesignParameter['DIFF_boundary_6']['_XYCoordinates'][0][0], ((self._DesignParameter['DIFF_boundary_6']['_XYCoordinates'][0][1] - (W / 2)) - 1436)]]
        self._DesignParameter['PIMP_boundary_1'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['PIMP'][0], _Datatype=DesignParameters._LayerMapping['PIMP'][1], _XWidth=522, _YWidth=(W + (1175 * 2)))
        self._DesignParameter['PIMP_boundary_1']['_XYCoordinates'] = [[((self._DesignParameter['DIFF_boundary_6']['_XYCoordinates'][0][0] + (W / 2)) + 1436), self._DesignParameter['DIFF_boundary_6']['_XYCoordinates'][0][1]]]
        self._DesignParameter['PIMP_boundary_0'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['PIMP'][0], _Datatype=DesignParameters._LayerMapping['PIMP'][1], _XWidth=522, _YWidth=(W + (1175 * 2)))
        self._DesignParameter['PIMP_boundary_0']['_XYCoordinates'] = [[((self._DesignParameter['DIFF_boundary_6']['_XYCoordinates'][0][0] - (W / 2)) - 1436), self._DesignParameter['DIFF_boundary_6']['_XYCoordinates'][0][1]]]
        self._DesignParameter['PIMP_boundary_4'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['PIMP'][0], _Datatype=DesignParameters._LayerMapping['PIMP'][1], _XWidth=(W + (1697 * 2)), _YWidth=522)
        self._DesignParameter['PIMP_boundary_4']['_XYCoordinates'] = [[self._DesignParameter['DIFF_boundary_6']['_XYCoordinates'][0][0], ((self._DesignParameter['DIFF_boundary_6']['_XYCoordinates'][0][1] + (W / 2)) + 1436)]]
        self._DesignParameter['PIMP_boundary_2'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['PIMP'][0], _Datatype=DesignParameters._LayerMapping['PIMP'][1], _XWidth=(W + (1697 * 2)), _YWidth=522)
        self._DesignParameter['PIMP_boundary_2']['_XYCoordinates'] = [[self._DesignParameter['DIFF_boundary_6']['_XYCoordinates'][0][0], ((self._DesignParameter['DIFF_boundary_6']['_XYCoordinates'][0][1] - (W / 2)) - 1436)]]
        self._DesignParameter['METAL1_boundary_5'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _XWidth=276, _YWidth=(W + (688 * 2)))
        self._DesignParameter['METAL1_boundary_5']['_XYCoordinates'] = [[((self._DesignParameter['DIFF_boundary_6']['_XYCoordinates'][0][0] - (W / 2)) - 526), self._DesignParameter['DIFF_boundary_6']['_XYCoordinates'][0][1]]]
        self._DesignParameter['METAL1_boundary_12'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1PINDrawing'][0], _Datatype=DesignParameters._LayerMapping['METAL1PINDrawing'][1], _XWidth=276, _YWidth=(W + (688 * 2)))
        self._DesignParameter['METAL1_boundary_12']['_XYCoordinates'] = [[((self._DesignParameter['DIFF_boundary_6']['_XYCoordinates'][0][0] - (W / 2)) - 526), self._DesignParameter['DIFF_boundary_6']['_XYCoordinates'][0][1]]]
        self._DesignParameter['METAL1_boundary_3'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _XWidth=276, _YWidth=(W + (688 * 2)))
        self._DesignParameter['METAL1_boundary_3']['_XYCoordinates'] = [[((self._DesignParameter['DIFF_boundary_6']['_XYCoordinates'][0][0] + (W / 2)) + 526), self._DesignParameter['DIFF_boundary_6']['_XYCoordinates'][0][1]]]
        self._DesignParameter['METAL1_boundary_11'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1PINDrawing'][0], _Datatype=DesignParameters._LayerMapping['METAL1PINDrawing'][1], _XWidth=276, _YWidth=(W + (688 * 2)))
        self._DesignParameter['METAL1_boundary_11']['_XYCoordinates'] = [[((self._DesignParameter['DIFF_boundary_6']['_XYCoordinates'][0][0] + (W / 2)) + 526), self._DesignParameter['DIFF_boundary_6']['_XYCoordinates'][0][1]]]
        self._DesignParameter['METAL1_boundary_4'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _XWidth=(W + (388 * 2)), _YWidth=300)
        self._DesignParameter['METAL1_boundary_4']['_XYCoordinates'] = [[self._DesignParameter['DIFF_boundary_6']['_XYCoordinates'][0][0], ((self._DesignParameter['DIFF_boundary_6']['_XYCoordinates'][0][1] + (W / 2)) + 538)]]
        self._DesignParameter['METAL1_boundary_10'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1PINDrawing'][0], _Datatype=DesignParameters._LayerMapping['METAL1PINDrawing'][1], _XWidth=(W + (288 * 2)), _YWidth=276)
        self._DesignParameter['METAL1_boundary_10']['_XYCoordinates'] = [[self._DesignParameter['DIFF_boundary_6']['_XYCoordinates'][0][0], ((self._DesignParameter['DIFF_boundary_6']['_XYCoordinates'][0][1] + (W / 2)) + 526)]]
        self._DesignParameter['METAL1_boundary_6'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _XWidth=(W + (1198 * 2)), _YWidth=476)
        self._DesignParameter['METAL1_boundary_6']['_XYCoordinates'] = [[self._DesignParameter['DIFF_boundary_6']['_XYCoordinates'][0][0], ((self._DesignParameter['DIFF_boundary_6']['_XYCoordinates'][0][1] + (W / 2)) + 1436)]]
        self._DesignParameter['METAL1_boundary_7'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1PINDrawing'][0], _Datatype=DesignParameters._LayerMapping['METAL1PINDrawing'][1], _XWidth=(W + (1138 * 2)), _YWidth=476)
        self._DesignParameter['METAL1_boundary_7']['_XYCoordinates'] = [[self._DesignParameter['DIFF_boundary_6']['_XYCoordinates'][0][0], ((self._DesignParameter['DIFF_boundary_6']['_XYCoordinates'][0][1] + (W / 2)) + 1436)]]
        self._DesignParameter['METAL1_boundary_1'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _XWidth=476, _YWidth=((W + 1674) + 1436))
        self._DesignParameter['METAL1_boundary_1']['_XYCoordinates'] = [[((self._DesignParameter['DIFF_boundary_6']['_XYCoordinates'][0][0] + (W / 2)) + 1436), (self._DesignParameter['DIFF_boundary_6']['_XYCoordinates'][0][1] + 119)]]
        self._DesignParameter['METAL1_boundary_8'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1PINDrawing'][0], _Datatype=DesignParameters._LayerMapping['METAL1PINDrawing'][1], _XWidth=476, _YWidth=((W + 1198) + 1138))
        self._DesignParameter['METAL1_boundary_8']['_XYCoordinates'] = [[((self._DesignParameter['DIFF_boundary_6']['_XYCoordinates'][0][0] + (W / 2)) + 1436), (self._DesignParameter['DIFF_boundary_6']['_XYCoordinates'][0][1] + 30)]]
        self._DesignParameter['METAL1_boundary_2'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _XWidth=476, _YWidth=((W + 1674) + 1436))
        self._DesignParameter['METAL1_boundary_2']['_XYCoordinates'] = [[((self._DesignParameter['DIFF_boundary_6']['_XYCoordinates'][0][0] - (W / 2)) - 1436), (self._DesignParameter['DIFF_boundary_6']['_XYCoordinates'][0][1] + 119)]]
        self._DesignParameter['METAL1_boundary_9'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1PINDrawing'][0], _Datatype=DesignParameters._LayerMapping['METAL1PINDrawing'][1], _XWidth=476, _YWidth=((W + 1198) + 1138))
        self._DesignParameter['METAL1_boundary_9']['_XYCoordinates'] = [[((self._DesignParameter['DIFF_boundary_6']['_XYCoordinates'][0][0] - (W / 2)) - 1436), (self._DesignParameter['DIFF_boundary_6']['_XYCoordinates'][0][1] + 30)]]
        self._DesignParameter['LVS_boundary_0'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['LVS1'][0], _Datatype=DesignParameters._LayerMapping['LVS1'][1], _XWidth=W, _YWidth=100)
        self._DesignParameter['LVS_boundary_0']['_XYCoordinates'] = [[self._DesignParameter['DIFF_boundary_6']['_XYCoordinates'][0][0], ((self._DesignParameter['DIFF_boundary_6']['_XYCoordinates'][0][1] - (W / 2)) + 50)]]
        self._DesignParameter['SBLK_boundary_3'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['SBLK'][0], _Datatype=DesignParameters._LayerMapping['SBLK'][1], _XWidth=(W + (181 * 2)), _YWidth=306)
        self._DesignParameter['SBLK_boundary_3']['_XYCoordinates'] = [[self._DesignParameter['DIFF_boundary_6']['_XYCoordinates'][0][0], ((self._DesignParameter['DIFF_boundary_6']['_XYCoordinates'][0][1] - (W / 2)) - 28)]]
        self._DesignParameter['SBLK_boundary_2'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['SBLK'][0], _Datatype=DesignParameters._LayerMapping['SBLK'][1], _XWidth=(W + (181 * 2)), _YWidth=306)
        self._DesignParameter['SBLK_boundary_2']['_XYCoordinates'] = [[self._DesignParameter['DIFF_boundary_6']['_XYCoordinates'][0][0], ((self._DesignParameter['DIFF_boundary_6']['_XYCoordinates'][0][1] + (W / 2)) + 28)]]
        self._DesignParameter['SBLK_boundary_0'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['SBLK'][0], _Datatype=DesignParameters._LayerMapping['SBLK'][1], _XWidth=306, _YWidth=(W - (125 * 2)))
        self._DesignParameter['SBLK_boundary_0']['_XYCoordinates'] = [[((self._DesignParameter['DIFF_boundary_6']['_XYCoordinates'][0][0] - (W / 2)) - 28), self._DesignParameter['DIFF_boundary_6']['_XYCoordinates'][0][1]]]
        self._DesignParameter['SBLK_boundary_1'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['SBLK'][0], _Datatype=DesignParameters._LayerMapping['SBLK'][1], _XWidth=306, _YWidth=(W - (125 * 2)))
        self._DesignParameter['SBLK_boundary_1']['_XYCoordinates'] = [[((self._DesignParameter['DIFF_boundary_6']['_XYCoordinates'][0][0] + (W / 2)) + 28), self._DesignParameter['DIFF_boundary_6']['_XYCoordinates'][0][1]]]
        self._DesignParameter['METAL1_boundary_13'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1PINDrawing'][0], _Datatype=DesignParameters._LayerMapping['METAL1PINDrawing'][1], _XWidth=(W - (312 * 2)), _YWidth=(W - (312 * 2)))
        self._DesignParameter['METAL1_boundary_13']['_XYCoordinates'] = [[(+ self._DesignParameter['DIFF_boundary_6']['_XYCoordinates'][0][0]), (+ self._DesignParameter['DIFF_boundary_6']['_XYCoordinates'][0][1])]]
        #LVS PIN LAYER
        self._DesignParameter['E'] = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1PIN'][0], _Datatype=DesignParameters._LayerMapping['METAL1PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0], _XYCoordinates=[[self._DesignParameter['DIFF_boundary_6']['_XYCoordinates'][0][0], (((self._DesignParameter['DIFF_boundary_6']['_XYCoordinates'][0][1] - (W / 2)) + 200) + 500)]],_Mag=0.1, _Angle=0, _TEXT='E')
        self._DesignParameter['B'] = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1PIN'][0], _Datatype=DesignParameters._LayerMapping['METAL1PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0], _XYCoordinates=[[self._DesignParameter['DIFF_boundary_6']['_XYCoordinates'][0][0] + (W/2) +526, self._DesignParameter['DIFF_boundary_6']['_XYCoordinates'][0][1]]],_Mag=0.1, _Angle=0, _TEXT='B')
        self._DesignParameter['C'] = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1PIN'][0], _Datatype=DesignParameters._LayerMapping['METAL1PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0], _XYCoordinates=[[self._DesignParameter['DIFF_boundary_6']['_XYCoordinates'][0][0] + (W/2) +1436, self._DesignParameter['DIFF_boundary_6']['_XYCoordinates'][0][1]]],_Mag=0.1, _Angle=0, _TEXT='C')
        ############################
        self._DesignParameter['ContArray1'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['CONT'][0], _Datatype=DesignParameters._LayerMapping['CONT'][1], _XWidth=40, _YWidth=40)
        self._DesignParameter['ContArray1']['_XYCoordinates'] = None
        
        XYList = []
        xy_base = [((self._DesignParameter['DIFF_boundary_6']['_XYCoordinates'][0][0] - (W / 2)) - 626), ((self._DesignParameter['DIFF_boundary_6']['_XYCoordinates'][0][1] - (W / 2)) - 650)]
        for i in range((int(((((W + (688 * 2)) - (18 * 2)) - 40) / 100)) + 1)):
            for j in range(3):
                x = (j * 100)
                y = (i * 100)
                XYList.append([(a + b) for (a, b) in zip(xy_base, [x, y])])
        self._DesignParameter['ContArray1']['_XYCoordinates'] = XYList
        self._DesignParameter['ContArray2'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['CONT'][0], _Datatype=DesignParameters._LayerMapping['CONT'][1], _XWidth=40, _YWidth=40)
        self._DesignParameter['ContArray2']['_XYCoordinates'] = None
        XYList = []
        xy_base = [(((self._DesignParameter['DIFF_boundary_6']['_XYCoordinates'][0][0] + (W / 2)) + 626) - (100 * 2)), ((self._DesignParameter['DIFF_boundary_6']['_XYCoordinates'][0][1] - (W / 2)) - 650)]
        for i in range((int(((((W + (688 * 2)) - (18 * 2)) - 40) / 100)) + 1)):
            for j in range(3):
                x = (j * 100)
                y = (i * 100)
                XYList.append([(a + b) for (a, b) in zip(xy_base, [x, y])])
        self._DesignParameter['ContArray2']['_XYCoordinates'] = XYList
        self._DesignParameter['ContArray3'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['CONT'][0], _Datatype=DesignParameters._LayerMapping['CONT'][1], _XWidth=40, _YWidth=40)
        self._DesignParameter['ContArray3']['_XYCoordinates'] = None
        XYList = []
        xy_base = [((self._DesignParameter['DIFF_boundary_6']['_XYCoordinates'][0][0] - (W / 2)) - 250), ((self._DesignParameter['DIFF_boundary_6']['_XYCoordinates'][0][1] + (W / 2)) + 426)]
        for i in range(3):
            for j in range((int(((((W + (288 * 2)) - (18 * 2)) - 40) / 100)) + 1)):
                x = (j * 100)
                y = (i * 100)
                XYList.append([(a + b) for (a, b) in zip(xy_base, [x, y])])
        self._DesignParameter['ContArray3']['_XYCoordinates'] = XYList
        self._DesignParameter['ContArray4'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['CONT'][0], _Datatype=DesignParameters._LayerMapping['CONT'][1], _XWidth=40, _YWidth=40)
        self._DesignParameter['ContArray4']['_XYCoordinates'] = None
        XYList = []
        xy_base = [((self._DesignParameter['DIFF_boundary_6']['_XYCoordinates'][0][0] - (W / 2)) - 1636), ((self._DesignParameter['DIFF_boundary_6']['_XYCoordinates'][0][1] - (W / 2)) - 1100)]
        for i in range((int(((((((W + 1138) + 1198) - 78) - 18) - 40) / 100)) + 1)):
            for j in range(5):
                x = (j * 100)
                y = (i * 100)
                XYList.append([(a + b) for (a, b) in zip(xy_base, [x, y])])
        self._DesignParameter['ContArray4']['_XYCoordinates'] = XYList
        self._DesignParameter['ContArray5'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['CONT'][0], _Datatype=DesignParameters._LayerMapping['CONT'][1], _XWidth=40, _YWidth=40)
        self._DesignParameter['ContArray5']['_XYCoordinates'] = None
        XYList = []
        xy_base = [(((self._DesignParameter['DIFF_boundary_6']['_XYCoordinates'][0][0] + (W / 2)) + 1636) - 400), ((self._DesignParameter['DIFF_boundary_6']['_XYCoordinates'][0][1] - (W / 2)) - 1100)]
        for i in range((int(((((((W + 1138) + 1198) - 78) - 18) - 40) / 100)) + 1)):
            for j in range(5):
                x = (j * 100)
                y = (i * 100)
                XYList.append([(a + b) for (a, b) in zip(xy_base, [x, y])])
        self._DesignParameter['ContArray5']['_XYCoordinates'] = XYList
        self._DesignParameter['ContArray6'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['CONT'][0], _Datatype=DesignParameters._LayerMapping['CONT'][1], _XWidth=40, _YWidth=40)
        self._DesignParameter['ContArray6']['_XYCoordinates'] = None
        XYList = []
        xy_base = [((self._DesignParameter['DIFF_boundary_6']['_XYCoordinates'][0][0] - (W / 2)) - 1100), ((self._DesignParameter['DIFF_boundary_6']['_XYCoordinates'][0][1] + (W / 2)) + 1236)]
        for i in range(5):
            for j in range((int(((((W + (1138 * 2)) - (18 * 2)) - 40) / 100)) + 1)):
                x = (j * 100)
                y = (i * 100)
                XYList.append([(a + b) for (a, b) in zip(xy_base, [x, y])])
        self._DesignParameter['ContArray6']['_XYCoordinates'] = XYList

        if (1100 <= self._DesignParameter['DIFF_boundary_6']['_XWidth'] < 5200):
            self._DesignParameter['METAL1_boundary_0'] = self._BoundaryElementDeclaration(
                _Layer=DesignParameters._LayerMapping['METAL1'][0],
                _Datatype=DesignParameters._LayerMapping['METAL1'][1], _XWidth=(W - (312 * 2)), _YWidth=(W - (312 * 2)))
            self._DesignParameter['METAL1_boundary_0']['_XYCoordinates'] = [
                [(+ self._DesignParameter['DIFF_boundary_6']['_XYCoordinates'][0][0]),
                 (+ self._DesignParameter['DIFF_boundary_6']['_XYCoordinates'][0][1])]]

            self._DesignParameter['ContArray7'] = self._BoundaryElementDeclaration(
                _Layer=DesignParameters._LayerMapping['CONT'][0], _Datatype=DesignParameters._LayerMapping['CONT'][1],
                _XWidth=40, _YWidth=40)
            self._DesignParameter['ContArray7']['_XYCoordinates'] = None

            XYList = []
            xy_base = [((self._DesignParameter['DIFF_boundary_6']['_XYCoordinates'][0][0] - (W / 2)) + 312 + 38),
                       ((self._DesignParameter['DIFF_boundary_6']['_XYCoordinates'][0][1] - (W / 2)) + 312 + 38)]
            for i in range((int(((((W - (312 * 2)) - (18 * 2)) - 40) / 100)) + 1)):
                offset = 0
                for j in range(int(((W - (312 * 2) - (18 * 2) - 40) / 100) + 1)):
                    if j % 7 == 0 and j != 0 :
                        offset += 252
                    x = (j * 100) + offset
                    y = (i * 100)
                    if (W - 312 * 2 - (18 + 20) * 2) < x :
                        break
                    XYList.append([(a + b) for (a, b) in zip(xy_base, [x, y])])
            self._DesignParameter['ContArray7']['_XYCoordinates'] = XYList


        elif (5200 <= self._DesignParameter['DIFF_boundary_6']['_XWidth'] < 9700):
            W_ = self._DesignParameter['DIFF_boundary_6']['_XWidth'] - 312 * 2
            h1_ = (W_ - 500) / 2
            h2_ = 500
            W1_ = (W_ - 500) / 2

            centerX = self._DesignParameter['DIFF_boundary_6']['_XYCoordinates'][0][0]
            centerY = self._DesignParameter['DIFF_boundary_6']['_XYCoordinates'][0][1]

            # M1_UP
            self._DesignParameter['M1_UP'] = self._BoundaryElementDeclaration(
                _Layer=DesignParameters._LayerMapping['METAL1'][0],
                _Datatype=DesignParameters._LayerMapping['METAL1'][1],
                _XWidth=W_,
                _YWidth=h1_)
            self._DesignParameter['M1_UP']['_XYCoordinates'] = [[
                centerX,
                centerY + W_ / 2 - h1_ / 2
            ]]

            # M1_DOWN
            self._DesignParameter['M1_DOWN'] = self._BoundaryElementDeclaration(
                _Layer=DesignParameters._LayerMapping['METAL1'][0],
                _Datatype=DesignParameters._LayerMapping['METAL1'][1],
                _XWidth=W_,
                _YWidth=h1_)
            self._DesignParameter['M1_DOWN']['_XYCoordinates'] = [[
                centerX,
                centerY - W_ / 2 + h1_ / 2
            ]]

            # M1_1
            self._DesignParameter['M1_1'] = self._BoundaryElementDeclaration(
                _Layer=DesignParameters._LayerMapping['METAL1'][0],
                _Datatype=DesignParameters._LayerMapping['METAL1'][1],
                _XWidth=W1_,
                _YWidth=h2_)
            self._DesignParameter['M1_1']['_XYCoordinates'] = [[
                centerX - W_ / 2 + W1_ / 2,
                centerY
            ]]

            # M1_2
            self._DesignParameter['M1_2'] = self._BoundaryElementDeclaration(
                _Layer=DesignParameters._LayerMapping['METAL1'][0],
                _Datatype=DesignParameters._LayerMapping['METAL1'][1],
                _XWidth=W1_,
                _YWidth=h2_)
            self._DesignParameter['M1_2']['_XYCoordinates'] = [[
                centerX + W_ / 2 - W1_ / 2,
                centerY
            ]]

            self._DesignParameter['ContArray7'] = self._BoundaryElementDeclaration(
                _Layer=DesignParameters._LayerMapping['CONT'][0], _Datatype=DesignParameters._LayerMapping['CONT'][1],
                _XWidth=40, _YWidth=40)
            self._DesignParameter['ContArray7']['_XYCoordinates'] = None

            XYList = []
            xy_base = [((self._DesignParameter['M1_1']['_XYCoordinates'][0][0] - (W1_ / 2)) + 38),
                       ((self._DesignParameter['M1_1']['_XYCoordinates'][0][1] - (W_ / 2)) + 38)]
            for i in range(int(((W_- (18 * 2) - 40) / 100) + 1)):
                offset = 0
                for j in range(int(((W1_- (18 * 2) - 40) / 100) + 1)):
                    if j % 6 == 0 and j != 0 :
                        offset += 252
                    x = (j * 100) + offset
                    y = (i * 100)
                    if (W1_ - (18 + 20) * 2 ) < x :
                        break
                    XYList.append([(a + b) for (a, b) in zip(xy_base, [x, y])])
            self._DesignParameter['ContArray7']['_XYCoordinates'] = XYList

            self._DesignParameter['ContArray8'] = self._BoundaryElementDeclaration(
                _Layer=DesignParameters._LayerMapping['CONT'][0], _Datatype=DesignParameters._LayerMapping['CONT'][1],
                _XWidth=40, _YWidth=40)
            self._DesignParameter['ContArray8']['_XYCoordinates'] = None

            XYList = []
            xy_base = [((self._DesignParameter['M1_2']['_XYCoordinates'][0][0] - (W1_ / 2)) + 38),
                       ((self._DesignParameter['M1_2']['_XYCoordinates'][0][1] - (W_ / 2)) + 38)]
            for i in range(int(((W_- (18 * 2) - 40) / 100) + 1)):
                offset = 0
                for j in range(int(((W1_- (18 * 2) - 40) / 100) + 1)):
                    if j % 6 == 0 and j != 0 :
                        offset += 252
                    x = (j * 100) + offset
                    y = (i * 100)
                    if (W1_ - (18 + 20) * 2 ) < x :
                        break
                    XYList.append([(a + b) for (a, b) in zip(xy_base, [x, y])])
            self._DesignParameter['ContArray8']['_XYCoordinates'] = XYList


        elif (9700 <= self._DesignParameter['DIFF_boundary_6']['_XWidth'] < 14200):
            W_ = self._DesignParameter['DIFF_boundary_6']['_XWidth'] - 312 * 2
            h1_ = 2000
            h2_ = W_ - h1_ * 2
            W1_ = int((W_ - 500 * 2) / 3)

            centerX = self._DesignParameter['DIFF_boundary_6']['_XYCoordinates'][0][0]
            centerY = self._DesignParameter['DIFF_boundary_6']['_XYCoordinates'][0][1]

            # M1_UP
            self._DesignParameter['M1_UP'] = self._BoundaryElementDeclaration(
                _Layer=DesignParameters._LayerMapping['METAL1'][0],
                _Datatype=DesignParameters._LayerMapping['METAL1'][1],
                _XWidth=W_,
                _YWidth=h1_)
            self._DesignParameter['M1_UP']['_XYCoordinates'] = [[
                centerX,
                centerY + W_ / 2 - h1_ / 2
            ]]

            # M1_DOWN
            self._DesignParameter['M1_DOWN'] = self._BoundaryElementDeclaration(
                _Layer=DesignParameters._LayerMapping['METAL1'][0],
                _Datatype=DesignParameters._LayerMapping['METAL1'][1],
                _XWidth=W_,
                _YWidth=h1_)
            self._DesignParameter['M1_DOWN']['_XYCoordinates'] = [[
                centerX,
                centerY - W_ / 2 + h1_ / 2
            ]]

            # M1_1 (Left)
            self._DesignParameter['M1_1'] = self._BoundaryElementDeclaration(
                _Layer=DesignParameters._LayerMapping['METAL1'][0],
                _Datatype=DesignParameters._LayerMapping['METAL1'][1],
                _XWidth=W1_,
                _YWidth=h2_)
            self._DesignParameter['M1_1']['_XYCoordinates'] = [[
                centerX - W_ / 2 + W1_ / 2,
                centerY
            ]]

            # M1_2 (Center)
            self._DesignParameter['M1_2'] = self._BoundaryElementDeclaration(
                _Layer=DesignParameters._LayerMapping['METAL1'][0],
                _Datatype=DesignParameters._LayerMapping['METAL1'][1],
                _XWidth=W1_,
                _YWidth=h2_)
            self._DesignParameter['M1_2']['_XYCoordinates'] = [[
                centerX,
                centerY
            ]]

            # M1_3 (Right)
            self._DesignParameter['M1_3'] = self._BoundaryElementDeclaration(
                _Layer=DesignParameters._LayerMapping['METAL1'][0],
                _Datatype=DesignParameters._LayerMapping['METAL1'][1],
                _XWidth=W1_,
                _YWidth=h2_)
            self._DesignParameter['M1_3']['_XYCoordinates'] = [[
                centerX + W_ / 2 - W1_ / 2,
                centerY
            ]]

            self._DesignParameter['ContArray7'] = self._BoundaryElementDeclaration(
                _Layer=DesignParameters._LayerMapping['CONT'][0], _Datatype=DesignParameters._LayerMapping['CONT'][1],
                _XWidth=40, _YWidth=40)
            self._DesignParameter['ContArray7']['_XYCoordinates'] = None

            XYList = []
            xy_base = [((self._DesignParameter['M1_1']['_XYCoordinates'][0][0] - (W1_ / 2)) + 38),
                       ((self._DesignParameter['M1_1']['_XYCoordinates'][0][1] - (W_ / 2)) + 38)]
            for i in range(int(((W_- (18 * 2) - 40) / 100) + 1)):
                offset = 0
                for j in range(int(((W1_- (18 * 2) - 40) / 100) + 1)):
                    if j % 6 == 0 and j != 0 :
                        offset += 252
                    x = (j * 100) + offset
                    y = (i * 100)
                    if (W1_ - (18 + 20) * 2 ) < x :
                        break
                    XYList.append([(a + b) for (a, b) in zip(xy_base, [x, y])])
            self._DesignParameter['ContArray7']['_XYCoordinates'] = XYList

            self._DesignParameter['ContArray8'] = self._BoundaryElementDeclaration(
                _Layer=DesignParameters._LayerMapping['CONT'][0], _Datatype=DesignParameters._LayerMapping['CONT'][1],
                _XWidth=40, _YWidth=40)
            self._DesignParameter['ContArray8']['_XYCoordinates'] = None

            XYList = []
            xy_base = [((self._DesignParameter['M1_2']['_XYCoordinates'][0][0] - (W1_ / 2)) + 38),
                       ((self._DesignParameter['M1_2']['_XYCoordinates'][0][1] - (W_ / 2)) + 38)]
            for i in range(int(((W_- (18 * 2) - 40) / 100) + 1)):
                offset = 0
                for j in range(int(((W1_- (18 * 2) - 40) / 100) + 1)):
                    if j % 6 == 0 and j != 0 :
                        offset += 252
                    x = (j * 100) + offset
                    y = (i * 100)
                    if (W1_ - (18 + 20) * 2 ) < x :
                        break
                    XYList.append([(a + b) for (a, b) in zip(xy_base, [x, y])])
            self._DesignParameter['ContArray8']['_XYCoordinates'] = XYList

            self._DesignParameter['ContArray9'] = self._BoundaryElementDeclaration(
                _Layer=DesignParameters._LayerMapping['CONT'][0], _Datatype=DesignParameters._LayerMapping['CONT'][1],
                _XWidth=40, _YWidth=40)
            self._DesignParameter['ContArray9']['_XYCoordinates'] = None

            XYList = []
            xy_base = [((self._DesignParameter['M1_3']['_XYCoordinates'][0][0] - (W1_ / 2)) + 38),
                       ((self._DesignParameter['M1_3']['_XYCoordinates'][0][1] - (W_ / 2)) + 38)]
            for i in range(int(((W_- (18 * 2) - 40) / 100) + 1)):
                offset = 0
                for j in range(int(((W1_- (18 * 2) - 40) / 100) + 1)):
                    if j % 6 == 0 and j != 0 :
                        offset += 252
                    x = (j * 100) + offset
                    y = (i * 100)
                    if (W1_ - (18 + 20) * 2 ) < x :
                        break
                    XYList.append([(a + b) for (a, b) in zip(xy_base, [x, y])])
            self._DesignParameter['ContArray9']['_XYCoordinates'] = XYList

        elif (14200 <= self._DesignParameter['DIFF_boundary_6']['_XWidth'] < 18700):
            W_ = self._DesignParameter['DIFF_boundary_6']['_XWidth'] - 312 * 2
            h1_ = 2000
            h2_ = W_ - h1_ * 2
            W1_ = int((W_ - 500 * 3) / 4)

            centerX = self._DesignParameter['DIFF_boundary_6']['_XYCoordinates'][0][0]
            centerY = self._DesignParameter['DIFF_boundary_6']['_XYCoordinates'][0][1]

            # M1_UP
            self._DesignParameter['M1_UP'] = self._BoundaryElementDeclaration(
                _Layer=DesignParameters._LayerMapping['METAL1'][0],
                _Datatype=DesignParameters._LayerMapping['METAL1'][1],
                _XWidth=W_,
                _YWidth=h1_)
            self._DesignParameter['M1_UP']['_XYCoordinates'] = [[
                centerX,
                centerY + W_ / 2 - h1_ / 2
            ]]

            # M1_DOWN
            self._DesignParameter['M1_DOWN'] = self._BoundaryElementDeclaration(
                _Layer=DesignParameters._LayerMapping['METAL1'][0],
                _Datatype=DesignParameters._LayerMapping['METAL1'][1],
                _XWidth=W_,
                _YWidth=h1_)
            self._DesignParameter['M1_DOWN']['_XYCoordinates'] = [[
                centerX,
                centerY - W_ / 2 + h1_ / 2
            ]]

            # M1_1 (Left)
            self._DesignParameter['M1_1'] = self._BoundaryElementDeclaration(
                _Layer=DesignParameters._LayerMapping['METAL1'][0],
                _Datatype=DesignParameters._LayerMapping['METAL1'][1],
                _XWidth=W1_,
                _YWidth=h2_)
            self._DesignParameter['M1_1']['_XYCoordinates'] = [[
                centerX - W_ / 2 + W1_ / 2,
                centerY
            ]]

            # M1_2 (Left-Center)
            self._DesignParameter['M1_2'] = self._BoundaryElementDeclaration(
                _Layer=DesignParameters._LayerMapping['METAL1'][0],
                _Datatype=DesignParameters._LayerMapping['METAL1'][1],
                _XWidth=W1_,
                _YWidth=h2_)
            self._DesignParameter['M1_2']['_XYCoordinates'] = [[
                centerX - 250 - W1_ / 2,
                centerY
            ]]

            # M1_3 (Right-Center)
            self._DesignParameter['M1_3'] = self._BoundaryElementDeclaration(
                _Layer=DesignParameters._LayerMapping['METAL1'][0],
                _Datatype=DesignParameters._LayerMapping['METAL1'][1],
                _XWidth=W1_,
                _YWidth=h2_)
            self._DesignParameter['M1_3']['_XYCoordinates'] = [[
                centerX + 250 + W1_ / 2,
                centerY
            ]]

            # M1_4 (Right)
            self._DesignParameter['M1_4'] = self._BoundaryElementDeclaration(
                _Layer=DesignParameters._LayerMapping['METAL1'][0],
                _Datatype=DesignParameters._LayerMapping['METAL1'][1],
                _XWidth=W1_,
                _YWidth=h2_)
            self._DesignParameter['M1_4']['_XYCoordinates'] = [[
                centerX + W_ / 2 - W1_ / 2,
                centerY
            ]]

            self._DesignParameter['ContArray7'] = self._BoundaryElementDeclaration(
                _Layer=DesignParameters._LayerMapping['CONT'][0], _Datatype=DesignParameters._LayerMapping['CONT'][1],
                _XWidth=40, _YWidth=40)
            self._DesignParameter['ContArray7']['_XYCoordinates'] = None

            XYList = []
            xy_base = [((self._DesignParameter['M1_1']['_XYCoordinates'][0][0] - (W1_ / 2)) + 38),
                       ((self._DesignParameter['M1_1']['_XYCoordinates'][0][1] - (W_ / 2)) + 38)]
            for i in range(int(((W_- (18 * 2) - 40) / 100) + 1)):
                offset = 0
                for j in range(int(((W1_- (18 * 2) - 40) / 100) + 1)):
                    if j % 6 == 0 and j != 0 :
                        offset += 252
                    x = (j * 100) + offset
                    y = (i * 100)
                    if (W1_ - (18 + 20) * 2 ) < x :
                        break
                    XYList.append([(a + b) for (a, b) in zip(xy_base, [x, y])])
            self._DesignParameter['ContArray7']['_XYCoordinates'] = XYList

            self._DesignParameter['ContArray8'] = self._BoundaryElementDeclaration(
                _Layer=DesignParameters._LayerMapping['CONT'][0], _Datatype=DesignParameters._LayerMapping['CONT'][1],
                _XWidth=40, _YWidth=40)
            self._DesignParameter['ContArray8']['_XYCoordinates'] = None

            XYList = []
            xy_base = [((self._DesignParameter['M1_2']['_XYCoordinates'][0][0] - (W1_ / 2)) + 38),
                       ((self._DesignParameter['M1_2']['_XYCoordinates'][0][1] - (W_ / 2)) + 38)]
            for i in range(int(((W_- (18 * 2) - 40) / 100) + 1)):
                offset = 0
                for j in range(int(((W1_- (18 * 2) - 40) / 100) + 1)):
                    if j % 6 == 0 and j != 0 :
                        offset += 252
                    x = (j * 100) + offset
                    y = (i * 100)
                    if (W1_ - (18 + 20) * 2 ) < x :
                        break
                    XYList.append([(a + b) for (a, b) in zip(xy_base, [x, y])])
            self._DesignParameter['ContArray8']['_XYCoordinates'] = XYList

            self._DesignParameter['ContArray9'] = self._BoundaryElementDeclaration(
                _Layer=DesignParameters._LayerMapping['CONT'][0], _Datatype=DesignParameters._LayerMapping['CONT'][1],
                _XWidth=40, _YWidth=40)
            self._DesignParameter['ContArray9']['_XYCoordinates'] = None

            XYList = []
            xy_base = [((self._DesignParameter['M1_3']['_XYCoordinates'][0][0] - (W1_ / 2)) + 38),
                       ((self._DesignParameter['M1_3']['_XYCoordinates'][0][1] - (W_ / 2)) + 38)]
            for i in range(int(((W_- (18 * 2) - 40) / 100) + 1)):
                offset = 0
                for j in range(int(((W1_- (18 * 2) - 40) / 100) + 1)):
                    if j % 6 == 0 and j != 0 :
                        offset += 252
                    x = (j * 100) + offset
                    y = (i * 100)
                    if (W1_ - (18 + 20) * 2 ) < x :
                        break
                    XYList.append([(a + b) for (a, b) in zip(xy_base, [x, y])])
            self._DesignParameter['ContArray9']['_XYCoordinates'] = XYList

            self._DesignParameter['ContArray10'] = self._BoundaryElementDeclaration(
                _Layer=DesignParameters._LayerMapping['CONT'][0], _Datatype=DesignParameters._LayerMapping['CONT'][1],
                _XWidth=40, _YWidth=40)
            self._DesignParameter['ContArray10']['_XYCoordinates'] = None

            XYList = []
            xy_base = [((self._DesignParameter['M1_4']['_XYCoordinates'][0][0] - (W1_ / 2)) + 38),
                       ((self._DesignParameter['M1_4']['_XYCoordinates'][0][1] - (W_ / 2)) + 38)]
            for i in range(int(((W_- (18 * 2) - 40) / 100) + 1)):
                offset = 0
                for j in range(int(((W1_- (18 * 2) - 40) / 100) + 1)):
                    if j % 6 == 0 and j != 0 :
                        offset += 252
                    x = (j * 100) + offset
                    y = (i * 100)
                    if (W1_ - (18 + 20) * 2 ) < x :
                        break
                    XYList.append([(a + b) for (a, b) in zip(xy_base, [x, y])])
            self._DesignParameter['ContArray10']['_XYCoordinates'] = XYList

        elif (18700 <= self._DesignParameter['DIFF_boundary_6']['_XWidth'] < 23200):
            W_ = self._DesignParameter['DIFF_boundary_6']['_XWidth'] - 312 * 2
            h1_ = 2000
            h2_ = W_ - h1_ * 2
            W1_ = int((W_ - 500 * 4) / 5)

            centerX = self._DesignParameter['DIFF_boundary_6']['_XYCoordinates'][0][0]
            centerY = self._DesignParameter['DIFF_boundary_6']['_XYCoordinates'][0][1]

            # M1_UP
            self._DesignParameter['M1_UP'] = self._BoundaryElementDeclaration(
                _Layer=DesignParameters._LayerMapping['METAL1'][0],
                _Datatype=DesignParameters._LayerMapping['METAL1'][1],
                _XWidth=W_,
                _YWidth=h1_)
            self._DesignParameter['M1_UP']['_XYCoordinates'] = [[
                centerX,
                centerY + W_ / 2 - h1_ / 2
            ]]

            # M1_DOWN
            self._DesignParameter['M1_DOWN'] = self._BoundaryElementDeclaration(
                _Layer=DesignParameters._LayerMapping['METAL1'][0],
                _Datatype=DesignParameters._LayerMapping['METAL1'][1],
                _XWidth=W_,
                _YWidth=h1_)
            self._DesignParameter['M1_DOWN']['_XYCoordinates'] = [[
                centerX,
                centerY - W_ / 2 + h1_ / 2
            ]]

            # M1_1 (Leftmost)
            self._DesignParameter['M1_1'] = self._BoundaryElementDeclaration(
                _Layer=DesignParameters._LayerMapping['METAL1'][0],
                _Datatype=DesignParameters._LayerMapping['METAL1'][1],
                _XWidth=W1_,
                _YWidth=h2_)
            self._DesignParameter['M1_1']['_XYCoordinates'] = [[
                centerX - W_ / 2 + W1_ / 2,
                centerY
            ]]

            # M1_2 (Left-Center)
            self._DesignParameter['M1_2'] = self._BoundaryElementDeclaration(
                _Layer=DesignParameters._LayerMapping['METAL1'][0],
                _Datatype=DesignParameters._LayerMapping['METAL1'][1],
                _XWidth=W1_,
                _YWidth=h2_)
            self._DesignParameter['M1_2']['_XYCoordinates'] = [[
                centerX - 500 - W1_,
                centerY
            ]]

            # M1_3 (Center)
            self._DesignParameter['M1_3'] = self._BoundaryElementDeclaration(
                _Layer=DesignParameters._LayerMapping['METAL1'][0],
                _Datatype=DesignParameters._LayerMapping['METAL1'][1],
                _XWidth=W1_,
                _YWidth=h2_)
            self._DesignParameter['M1_3']['_XYCoordinates'] = [[
                centerX,
                centerY
            ]]

            # M1_4 (Right-Center)
            self._DesignParameter['M1_4'] = self._BoundaryElementDeclaration(
                _Layer=DesignParameters._LayerMapping['METAL1'][0],
                _Datatype=DesignParameters._LayerMapping['METAL1'][1],
                _XWidth=W1_,
                _YWidth=h2_)
            self._DesignParameter['M1_4']['_XYCoordinates'] = [[
                centerX + 500 + W1_,
                centerY
            ]]

            # M1_5 (Rightmost)
            self._DesignParameter['M1_5'] = self._BoundaryElementDeclaration(
                _Layer=DesignParameters._LayerMapping['METAL1'][0],
                _Datatype=DesignParameters._LayerMapping['METAL1'][1],
                _XWidth=W1_,
                _YWidth=h2_)
            self._DesignParameter['M1_5']['_XYCoordinates'] = [[
                centerX + W_ / 2 - W1_ / 2,
                centerY
            ]]

            self._DesignParameter['ContArray7'] = self._BoundaryElementDeclaration(
                _Layer=DesignParameters._LayerMapping['CONT'][0], _Datatype=DesignParameters._LayerMapping['CONT'][1],
                _XWidth=40, _YWidth=40)
            self._DesignParameter['ContArray7']['_XYCoordinates'] = None

            XYList = []
            xy_base = [((self._DesignParameter['M1_1']['_XYCoordinates'][0][0] - (W1_ / 2)) + 38),
                       ((self._DesignParameter['M1_1']['_XYCoordinates'][0][1] - (W_ / 2)) + 38)]
            for i in range(int(((W_- (18 * 2) - 40) / 100) + 1)):
                offset = 0
                for j in range(int(((W1_- (18 * 2) - 40) / 100) + 1)):
                    if j % 6 == 0 and j != 0 :
                        offset += 252
                    x = (j * 100) + offset
                    y = (i * 100)
                    if (W1_ - (18 + 20) * 2 ) < x :
                        break
                    XYList.append([(a + b) for (a, b) in zip(xy_base, [x, y])])
            self._DesignParameter['ContArray7']['_XYCoordinates'] = XYList

            self._DesignParameter['ContArray8'] = self._BoundaryElementDeclaration(
                _Layer=DesignParameters._LayerMapping['CONT'][0], _Datatype=DesignParameters._LayerMapping['CONT'][1],
                _XWidth=40, _YWidth=40)
            self._DesignParameter['ContArray8']['_XYCoordinates'] = None

            XYList = []
            xy_base = [((self._DesignParameter['M1_2']['_XYCoordinates'][0][0] - (W1_ / 2)) + 38),
                       ((self._DesignParameter['M1_2']['_XYCoordinates'][0][1] - (W_ / 2)) + 38)]
            for i in range(int(((W_- (18 * 2) - 40) / 100) + 1)):
                offset = 0
                for j in range(int(((W1_- (18 * 2) - 40) / 100) + 1)):
                    if j % 6 == 0 and j != 0 :
                        offset += 252
                    x = (j * 100) + offset
                    y = (i * 100)
                    if (W1_ - (18 + 20) * 2 ) < x :
                        break
                    XYList.append([(a + b) for (a, b) in zip(xy_base, [x, y])])
            self._DesignParameter['ContArray8']['_XYCoordinates'] = XYList

            self._DesignParameter['ContArray9'] = self._BoundaryElementDeclaration(
                _Layer=DesignParameters._LayerMapping['CONT'][0], _Datatype=DesignParameters._LayerMapping['CONT'][1],
                _XWidth=40, _YWidth=40)
            self._DesignParameter['ContArray9']['_XYCoordinates'] = None

            XYList = []
            xy_base = [((self._DesignParameter['M1_3']['_XYCoordinates'][0][0] - (W1_ / 2)) + 38),
                       ((self._DesignParameter['M1_3']['_XYCoordinates'][0][1] - (W_ / 2)) + 38)]
            for i in range(int(((W_- (18 * 2) - 40) / 100) + 1)):
                offset = 0
                for j in range(int(((W1_- (18 * 2) - 40) / 100) + 1)):
                    if j % 6 == 0 and j != 0 :
                        offset += 252
                    x = (j * 100) + offset
                    y = (i * 100)
                    if (W1_ - (18 + 20) * 2 ) < x :
                        break
                    XYList.append([(a + b) for (a, b) in zip(xy_base, [x, y])])
            self._DesignParameter['ContArray9']['_XYCoordinates'] = XYList

            self._DesignParameter['ContArray10'] = self._BoundaryElementDeclaration(
                _Layer=DesignParameters._LayerMapping['CONT'][0], _Datatype=DesignParameters._LayerMapping['CONT'][1],
                _XWidth=40, _YWidth=40)
            self._DesignParameter['ContArray10']['_XYCoordinates'] = None

            XYList = []
            xy_base = [((self._DesignParameter['M1_4']['_XYCoordinates'][0][0] - (W1_ / 2)) + 38),
                       ((self._DesignParameter['M1_4']['_XYCoordinates'][0][1] - (W_ / 2)) + 38)]
            for i in range(int(((W_- (18 * 2) - 40) / 100) + 1)):
                offset = 0
                for j in range(int(((W1_- (18 * 2) - 40) / 100) + 1)):
                    if j % 6 == 0 and j != 0 :
                        offset += 252
                    x = (j * 100) + offset
                    y = (i * 100)
                    if (W1_ - (18 + 20) * 2) < x :
                        break
                    XYList.append([(a + b) for (a, b) in zip(xy_base, [x, y])])
            self._DesignParameter['ContArray10']['_XYCoordinates'] = XYList

            self._DesignParameter['ContArray11'] = self._BoundaryElementDeclaration(
                _Layer=DesignParameters._LayerMapping['CONT'][0], _Datatype=DesignParameters._LayerMapping['CONT'][1],
                _XWidth=40, _YWidth=40)
            self._DesignParameter['ContArray11']['_XYCoordinates'] = None

            XYList = []
            xy_base = [((self._DesignParameter['M1_5']['_XYCoordinates'][0][0] - (W1_ / 2)) + 38),
                       ((self._DesignParameter['M1_5']['_XYCoordinates'][0][1] - (W_ / 2)) + 38)]
            for i in range(int(((W_- (18 * 2) - 40) / 100) + 1)):
                offset = 0
                for j in range(int(((W1_- (18 * 2) - 40) / 100) + 1)):
                    if j % 6 == 0 and j != 0 :
                        offset += 252
                    x = (j * 100) + offset
                    y = (i * 100)
                    if (W1_ - (18 + 20) * 2 ) < x :
                        break
                    XYList.append([(a + b) for (a, b) in zip(xy_base, [x, y])])
            self._DesignParameter['ContArray11']['_XYCoordinates'] = XYList

# if __name__ == '__main__':
#     libname = 'vpnp_Gen'
#     cellname = 'vpnp'
#     _fileName = cellname + '.gds'
#
#     ''' Input Parameters for Layout Object '''
#
#     InputParams = dict(
#         # width=4174,
#         W=1100
#     )
#
#     Mode_DRCCheck = True  # True | False
#     Num_DRCCheck = 100
#
#     LayoutObj =vpnp(_Name=cellname)
#     LayoutObj._CalculateDesignParameter(**InputParams)
#     LayoutObj._UpdateDesignParameter2GDSStructure(_DesignParameterInDictionary=LayoutObj._DesignParameter)
#     with open(f'./{_fileName}', 'wb') as testStreamFile:
#         tmp = LayoutObj._CreateGDSStream(LayoutObj._DesignParameter['_GDSFile']['_GDSFile'])
#         tmp.write_binary_gds_stream(testStreamFile)
#
#     print('   Sending to FTP Server & StreamIn...   '.center(105, '#'))
#
#
#     print('      Finished       '.center(105, '#'))
