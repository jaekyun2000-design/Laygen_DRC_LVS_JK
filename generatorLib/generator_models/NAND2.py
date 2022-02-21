from generatorLib import StickDiagram
from generatorLib import DesignParameters
import copy
import math
from generatorLib import DRC
from generatorLib import CoordinateCalc as CoordCalc
from generatorLib.generator_models import NMOSWithDummy
from generatorLib.generator_models import Z_PWR_CNT
from generatorLib.generator_models import PMOSWithDummy
from generatorLib.generator_models import SupplyRails
from generatorLib.generator_models import ViaPoly2Met1
from generatorLib.generator_models import ViaPoly2Met1_resize
from generatorLib.generator_models import CascodeNMOS


class NAND2(StickDiagram._StickDiagram):
    def __init__(self, _DesignParameter=None, _Name='NAND2'):
        if _DesignParameter != None:
            self._DesignParameter = _DesignParameter
        else:
            self._DesignParameter = dict(_Name=self._NameDeclaration(_Name=_Name), _GDSFile=self._GDSObjDeclaration(_GDSFile=None))
        self._DesignParameter['_Name']['Name'] = _Name

    def _CalculateDesignParameter(self,CellHeight=1800,ChannelLength=30,GateSpacing=100,XVT='SLVT',NMOSWidth=400,PMOSWidth=400,YCoordOfInputOutput=900,NumFinger=3,YCoordOfNM=350,YCoordOfPM=1400):

        drc = DRC.DRC()
        _Name = self._DesignParameter['_Name']['_Name']

        # YWidth_Met1HorizontalRouting = drc._Metal1MinWidth  # 50
        YWidth_Met1HorizontalRouting = 66

        self._DesignParameter['VSSRail'] = self._SrefElementDeclaration(_DesignObj=SupplyRails.SupplyRail(_Name='VSSRailIn{}'.format(_Name)))[0]
        self._DesignParameter['VSSRail']['_DesignObj']._CalculateDesignParameter(**dict(NumPitch=((NumFinger * 2) + 1), UnitPitch=130, Met1YWidth=80, Met2YWidth=300, PpNpYWidth=180, isPbody=True, deleteViaAndMet1=True))
        self._DesignParameter['VSSRail']['_XYCoordinates'] = [[0.0, 0.0]]
        self._DesignParameter['VDDRail'] = self._SrefElementDeclaration(_DesignObj=SupplyRails.SupplyRail(_Name='VDDRailIn{}'.format(_Name)))[0]
        self._DesignParameter['VDDRail']['_DesignObj']._CalculateDesignParameter(**dict(NumPitch=((NumFinger * 2) + 1), UnitPitch=130, Met1YWidth=80, Met2YWidth=300, PpNpYWidth=180, isPbody=False, deleteViaAndMet1=True))
        self._DesignParameter['VDDRail']['_XYCoordinates'] = [[0, CellHeight]]
        self._DesignParameter['NMOS'] = self._SrefElementDeclaration(_DesignObj=NMOSWithDummy._NMOS(_Name='NMOSIn{}'.format(_Name)))[0]
        self._DesignParameter['NMOS']['_DesignObj']._CalculateNMOSDesignParameter(**dict(_NMOSNumberofGate=(NumFinger * 2), _NMOSChannelWidth=NMOSWidth, _NMOSChannellength=ChannelLength, _NMOSDummy=True, _GateSpacing=GateSpacing, _SDWidth=66, _XVT=XVT))
        self._DesignParameter['NMOS']['_XYCoordinates'] = [[0, YCoordOfNM]]
        self._DesignParameter['PMOS'] = self._SrefElementDeclaration(_DesignObj=PMOSWithDummy._PMOS(_Name='PMOSIn{}'.format(_Name)))[0]
        self._DesignParameter['PMOS']['_DesignObj']._CalculatePMOSDesignParameter(**dict(_PMOSNumberofGate=(NumFinger * 2), _PMOSChannelWidth=PMOSWidth, _PMOSChannellength=ChannelLength, _PMOSDummy=True, _GateSpacing=GateSpacing, _SDWidth=66, _XVT=XVT))
        self._DesignParameter['PMOS']['_XYCoordinates'] = [[0, YCoordOfPM]]
        self._DesignParameter['ViaPoly_InputA'] = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1_resize._ViaPoly2Met1_resize(_Name='ViaPoly_InputAIn{}'.format(_Name)))[0]    # manually edited
        self._DesignParameter['ViaPoly_InputA']['_DesignObj']._CalculateDesignParameter(
            **dict(_ViaPoly2Met1NumberOfCOX=1, _ViaPoly2Met1NumberOfCOY=2,
                   Met1XWidth=66, Met1YWidth=200, POXWidth=50, POYWidth=200))  # manually edited
        self._DesignParameter['ViaPoly_InputA']['_XYCoordinates'] = [[(self._DesignParameter['NMOS']['_XYCoordinates'][0][0] + self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0]), YCoordOfInputOutput]]
        self._DesignParameter['ViaPoly_InputB'] = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1_resize._ViaPoly2Met1_resize(_Name='ViaPoly_InputBIn{}'.format(_Name)))[0]    # manually edited
        self._DesignParameter['ViaPoly_InputB']['_DesignObj']._CalculateDesignParameter(
            **dict(_ViaPoly2Met1NumberOfCOX=1, _ViaPoly2Met1NumberOfCOY=2,
                   Met1XWidth=66, Met1YWidth=200, POXWidth=50, POYWidth=200))  # manually edited
        self._DesignParameter['ViaPoly_InputB']['_XYCoordinates'] = [[(self._DesignParameter['NMOS']['_XYCoordinates'][0][0] + self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][(- 1)][0]), YCoordOfInputOutput]]
        XYList = []
        xy_offset = (0, ((- (self._DesignParameter['PMOS']['_XYCoordinates'][0][1] + self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1])) + CellHeight))
        for i in range(len(self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'])):
            if ((i % 2) == 0):
                xy = (self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i][0] if (type(self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i][0]) == list) else self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i])
                XYList.append([((x + y) + z) for (x, y, z) in zip([(0 + self._DesignParameter['PMOS']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['PMOS']['_XYCoordinates'][0][1])], xy, xy_offset)])
        self._DesignParameter['ViaForVDD'] = self._SrefElementDeclaration(_DesignObj=Z_PWR_CNT.Z_PWR_CNT(_Name='ViaForVDDIn{}'.format(_Name)))[0]
        self._DesignParameter['ViaForVDD']['_DesignObj']._CalculateDesignParameter(**dict(_Xnum=1, _Xdistance=0))
        self._DesignParameter['ViaForVDD']['_XYCoordinates'] = XYList
        path_list = []
        if (len(self._DesignParameter['ViaForVDD']['_XYCoordinates']) == 1):
            mode = 'vertical'
            _width = self._DesignParameter['ViaForVDD']['_DesignObj']._DesignParameter['METAL1_boundary_0']['_XWidth']
        elif (self._DesignParameter['ViaForVDD']['_XYCoordinates'][0][0] == self._DesignParameter['ViaForVDD']['_XYCoordinates'][(- 1)][0]):
            mode = 'horizontal'
            _width = self._DesignParameter['ViaForVDD']['_DesignObj']._DesignParameter['METAL1_boundary_0']['_XWidth']
        elif (self._DesignParameter['ViaForVDD']['_XYCoordinates'][0][1] == self._DesignParameter['ViaForVDD']['_XYCoordinates'][(- 1)][1]):
            mode = 'vertical'
            _width = self._DesignParameter['ViaForVDD']['_DesignObj']._DesignParameter['METAL1_boundary_0']['_XWidth']
        else:
            print('Invalid Target Input')
        if (mode == 'vertical'):
            xy_with_offset = []
            target_y_value = ((self._DesignParameter['PMOS']['_XYCoordinates'][0][1] + self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) + (self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2))
            for i in range(len(self._DesignParameter['ViaForVDD']['_XYCoordinates'])):
                xy_with_offset.append([(x + y) for (x, y) in zip([0, 0], self._DesignParameter['ViaForVDD']['_XYCoordinates'][i])])
            for i in range(len(xy_with_offset)):
                path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
        elif (mode == 'horizontal'):
            xy_with_offset = []
            target_x_value = (self._DesignParameter['PMOS']['_XYCoordinates'][0][0] + self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0])
            for i in range(len(self._DesignParameter['ViaForVDD']['_XYCoordinates'])):
                xy_with_offset.append([(x + y) for (x, y) in zip([0, 0], self._DesignParameter['ViaForVDD']['_XYCoordinates'][i])])
            for i in range(len(xy_with_offset)):
                path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
        self._DesignParameter['Met1RouteY_VDD'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=_width)
        self._DesignParameter['Met1RouteY_VDD']['_XYCoordinates'] = path_list
        path_list = []
        if (len(self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates']) == 1):
            mode = 'vertical'
            _width = self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
        elif (self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0] == self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]):
            mode = 'horizontal'
            _width = self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
        elif (self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1] == self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][1]):
            mode = 'vertical'
            _width = self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
        else:
            print('Invalid Target Input')
        if (mode == 'vertical'):
            xy_with_offset = []
            target_y_value = ((self._DesignParameter['ViaPoly_InputA']['_XYCoordinates'][0][1] + self._DesignParameter['ViaPoly_InputA']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1]) - (self._DesignParameter['ViaPoly_InputA']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2))
            for i in range(len(self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
                xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['NMOS']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['NMOS']['_XYCoordinates'][0][1])], self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i])])
            for i in range(len(xy_with_offset)):
                path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
        elif (mode == 'horizontal'):
            xy_with_offset = []
            target_x_value = (self._DesignParameter['ViaPoly_InputA']['_XYCoordinates'][0][0] + self._DesignParameter['ViaPoly_InputA']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0])
            for i in range(len(self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
                xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['NMOS']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['NMOS']['_XYCoordinates'][0][1])], self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i])])
            for i in range(len(xy_with_offset)):
                path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
        self._DesignParameter['PolyRouteY_NM'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _Width=_width)
        self._DesignParameter['PolyRouteY_NM']['_XYCoordinates'] = path_list
        path_list = []
        if (len(self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates']) == 1):
            mode = 'vertical'
            _width = self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
        elif (self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0] == self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]):
            mode = 'horizontal'
            _width = self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
        elif (self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1] == self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][1]):
            mode = 'vertical'
            _width = self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
        else:
            print('Invalid Target Input')
        if (mode == 'vertical'):
            xy_with_offset = []
            target_y_value = ((self._DesignParameter['ViaPoly_InputA']['_XYCoordinates'][0][1] + self._DesignParameter['ViaPoly_InputA']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1]) + (self._DesignParameter['ViaPoly_InputA']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2))
            for i in range(len(self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
                xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['PMOS']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['PMOS']['_XYCoordinates'][0][1])], self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i])])
            for i in range(len(xy_with_offset)):
                path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
        elif (mode == 'horizontal'):
            xy_with_offset = []
            target_x_value = (self._DesignParameter['ViaPoly_InputA']['_XYCoordinates'][0][0] + self._DesignParameter['ViaPoly_InputA']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0])
            for i in range(len(self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
                xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['PMOS']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['PMOS']['_XYCoordinates'][0][1])], self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i])])
            for i in range(len(xy_with_offset)):
                path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
        self._DesignParameter['PolyRouteY_PM'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _Width=_width)
        self._DesignParameter['PolyRouteY_PM']['_XYCoordinates'] = path_list
        XYList = []
        xy_offset = (0, (((- self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']) / 2) - ((drc._Metal1MinSpaceAtCorner + YWidth_Met1HorizontalRouting) / 2)))  # Manually Edited
        for i in range(len(self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'])):
            if ((i % 2) == 1):
                XYList.append([((x + y) + z) for (x, y, z) in zip([(0 + self._DesignParameter['PMOS']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['PMOS']['_XYCoordinates'][0][1])], self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i], xy_offset)])
        self._DesignParameter['Met1RouteY_PMOutput'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _XWidth=self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'], _YWidth=(drc._Metal1MinSpaceAtCorner + YWidth_Met1HorizontalRouting))  # Manually Edited
        self._DesignParameter['Met1RouteY_PMOutput']['_XYCoordinates'] = XYList
        self._DesignParameter['Met1RouteX_PMOutput'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _XWidth=((self._DesignParameter['Met1RouteY_PMOutput']['_XYCoordinates'][(- 1)][0] + (self._DesignParameter['Met1RouteY_PMOutput']['_XWidth'] / 2)) - (self._DesignParameter['Met1RouteY_PMOutput']['_XYCoordinates'][0][0] - (self._DesignParameter['Met1RouteY_PMOutput']['_XWidth'] / 2))), _YWidth=YWidth_Met1HorizontalRouting)  # Manually Edit
        self._DesignParameter['Met1RouteX_PMOutput']['_XYCoordinates'] = [[(((self._DesignParameter['Met1RouteY_PMOutput']['_XYCoordinates'][(- 1)][0] + (self._DesignParameter['Met1RouteY_PMOutput']['_XWidth'] / 2)) + (self._DesignParameter['Met1RouteY_PMOutput']['_XYCoordinates'][0][0] - (self._DesignParameter['Met1RouteY_PMOutput']['_XWidth'] / 2))) / 2), ((((self._DesignParameter['PMOS']['_XYCoordinates'][0][1] + self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) - (self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)) - drc._Metal1MinSpaceAtCorner) - (self._DesignParameter['Met1RouteX_PMOutput']['_YWidth'] / 2))]]
        self._DesignParameter['PolyRouteX_NMInputA'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _XWidth=(((self._DesignParameter['NMOS']['_XYCoordinates'][0][0] + self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(NumFinger - 1)][0]) + (self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)) - ((self._DesignParameter['ViaPoly_InputA']['_XYCoordinates'][0][0] + self._DesignParameter['ViaPoly_InputA']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['ViaPoly_InputA']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2))), _YWidth=50)
        self._DesignParameter['PolyRouteX_NMInputA']['_XYCoordinates'] = [[((((self._DesignParameter['NMOS']['_XYCoordinates'][0][0] + self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(NumFinger - 1)][0]) + (self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)) + ((self._DesignParameter['ViaPoly_InputA']['_XYCoordinates'][0][0] + self._DesignParameter['ViaPoly_InputA']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['ViaPoly_InputA']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2))) / 2), (((self._DesignParameter['ViaPoly_InputA']['_XYCoordinates'][0][1] + self._DesignParameter['ViaPoly_InputA']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1]) - (self._DesignParameter['ViaPoly_InputA']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2)) + (self._DesignParameter['PolyRouteX_NMInputA']['_YWidth'] / 2))]]
        self._DesignParameter['PolyRouteX_PMInputA'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _XWidth=self._DesignParameter['PolyRouteX_NMInputA']['_XWidth'], _YWidth=self._DesignParameter['PolyRouteX_NMInputA']['_YWidth'])
        self._DesignParameter['PolyRouteX_PMInputA']['_XYCoordinates'] = [[self._DesignParameter['PolyRouteX_NMInputA']['_XYCoordinates'][0][0], (((self._DesignParameter['ViaPoly_InputA']['_XYCoordinates'][0][1] + self._DesignParameter['ViaPoly_InputA']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1]) + (self._DesignParameter['ViaPoly_InputA']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2)) - (self._DesignParameter['PolyRouteX_PMInputA']['_YWidth'] / 2))]]
        self._DesignParameter['PolyRouteX_PMInputB'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _XWidth=self._DesignParameter['PolyRouteX_NMInputA']['_XWidth'], _YWidth=self._DesignParameter['PolyRouteX_NMInputA']['_YWidth'])
        self._DesignParameter['PolyRouteX_PMInputB']['_XYCoordinates'] = [[((((self._DesignParameter['ViaPoly_InputB']['_XYCoordinates'][0][0] + self._DesignParameter['ViaPoly_InputB']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) + (self._DesignParameter['ViaPoly_InputB']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)) + ((self._DesignParameter['PMOS']['_XYCoordinates'][0][0] + self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][NumFinger][0]) - (self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2))) / 2), self._DesignParameter['PolyRouteX_PMInputA']['_XYCoordinates'][0][1]]]
        self._DesignParameter['PolyRouteX_NMInputB'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _XWidth=self._DesignParameter['PolyRouteX_NMInputA']['_XWidth'], _YWidth=self._DesignParameter['PolyRouteX_NMInputA']['_YWidth'])
        self._DesignParameter['PolyRouteX_NMInputB']['_XYCoordinates'] = [[self._DesignParameter['PolyRouteX_PMInputB']['_XYCoordinates'][0][0], self._DesignParameter['PolyRouteX_NMInputA']['_XYCoordinates'][0][1]]]

        # nand2_8.bin finish


        ''' Code Generater '''

        # Met1Routing
        self._DesignParameter['Met1RouteY_NMOutput'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1'][0],
            _Datatype=DesignParameters._LayerMapping['METAL1'][1],
            _XWidth=self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'],
            _YWidth=(drc._Metal1MinSpaceAtCorner + YWidth_Met1HorizontalRouting)
        )
        self._DesignParameter['Met1RouteY_NMDown'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1'][0],
            _Datatype=DesignParameters._LayerMapping['METAL1'][1],
            _XWidth=self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'],
            _YWidth=(drc._Metal1MinSpaceAtCorner + YWidth_Met1HorizontalRouting)
        )

        tmpXYs_NMout = []
        tmpXYs_NMintermediate = []
        for i in range(0, NumFinger + 1):
            if i % 2 == 1:
                tmpXYs_NMout.append(
                    CoordCalc.Sum(self.getXY('NMOS', '_Met1Layer')[NumFinger - i],
                                  [0, self.getYWidth('NMOS', '_Met1Layer')/2],
                                  [0, self.getYWidth('Met1RouteY_NMOutput')/2])
                )
            else:
                tmpXYs_NMintermediate.append(
                    CoordCalc.Sum(self.getXY('NMOS', '_Met1Layer')[NumFinger - i],
                                  [0, -self.getYWidth('NMOS', '_Met1Layer')/2],
                                  [0, -self.getYWidth('Met1RouteY_NMDown')/2])
                )
        self._DesignParameter['Met1RouteY_NMOutput']['_XYCoordinates'] = tmpXYs_NMout
        self._DesignParameter['Met1RouteY_NMDown']['_XYCoordinates'] = tmpXYs_NMintermediate


        self._DesignParameter['Met1RouteX_NMOutput'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1'][0],
            _Datatype=DesignParameters._LayerMapping['METAL1'][1],
            _XWidth=CoordCalc.getXYCoords_MaxX(self.getXY('Met1RouteY_NMOutput'))[0][0] - CoordCalc.getXYCoords_MinX(self.getXY('Met1RouteY_NMOutput'))[0][0] + self.getXWidth('Met1RouteY_NMOutput'),
            _YWidth=YWidth_Met1HorizontalRouting
        )
        self._DesignParameter['Met1RouteX_NMOutput']['_XYCoordinates'] = [[
            (self.getXY('Met1RouteY_NMOutput')[0][0] + self.getXY('Met1RouteY_NMOutput')[-1][0]) / 2,
            self.getXY('Met1RouteY_NMOutput')[0][1] + self.getYWidth('Met1RouteY_NMOutput') / 2 - self.getYWidth('Met1RouteX_NMOutput') / 2
        ]]

        self._DesignParameter['Met1RouteX_NMDown'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1'][0],
            _Datatype=DesignParameters._LayerMapping['METAL1'][1],
            _XWidth=CoordCalc.getXYCoords_MaxX(self.getXY('Met1RouteY_NMDown'))[0][0] - CoordCalc.getXYCoords_MinX(self.getXY('Met1RouteY_NMDown'))[0][0] + self.getXWidth('Met1RouteY_NMDown'),
            _YWidth=YWidth_Met1HorizontalRouting
        )
        self._DesignParameter['Met1RouteX_NMDown']['_XYCoordinates'] = [[
            (self.getXY('Met1RouteY_NMDown')[0][0] + self.getXY('Met1RouteY_NMDown')[-1][0]) / 2,
            self.getXY('Met1RouteY_NMDown')[0][1] - self.getYWidth('Met1RouteY_NMDown')/2 + self.getYWidth('Met1RouteX_NMDown')/2
        ]]

        #
        self._DesignParameter['Met1RouteY_NMUp'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1'][0],
            _Datatype=DesignParameters._LayerMapping['METAL1'][1],
            _XWidth=self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'],
            _YWidth=(drc._Metal1MinSpaceAtCorner + YWidth_Met1HorizontalRouting)
        )
        self._DesignParameter['Met1RouteY_NM2VSS'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1'][0],
            _Datatype=DesignParameters._LayerMapping['METAL1'][1],
            _XWidth=self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'],
            _YWidth=self.getXY('NMOS', '_Met1Layer')[0][1] - self.getYWidth('NMOS', '_Met1Layer')/2
        )
        tmpXYs_NMup = []
        tmpXYs_NM2VSS = []
        for i in range(0, NumFinger + 1):
            if i % 2 == 0:
                tmpXYs_NMup.append(
                    CoordCalc.Sum(self.getXY('NMOS', '_Met1Layer')[NumFinger + i],
                                  [0, self.getYWidth('NMOS', '_Met1Layer') / 2],
                                  [0, self.getYWidth('Met1RouteY_NMUp') / 2])
                )
            else:
                tmpXYs_NM2VSS.append(
                    CoordCalc.Sum(self.getXY('NMOS', '_Met1Layer')[NumFinger + i],
                                  [0, -self.getYWidth('NMOS', '_Met1Layer') / 2],
                                  [0, -self.getYWidth('Met1RouteY_NM2VSS') / 2])
                )
        self._DesignParameter['Met1RouteY_NMUp']['_XYCoordinates'] = tmpXYs_NMup
        self._DesignParameter['Met1RouteY_NM2VSS']['_XYCoordinates'] = tmpXYs_NM2VSS

        self._DesignParameter['Met1RouteX_NMUp'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1'][0],
            _Datatype=DesignParameters._LayerMapping['METAL1'][1],
            _XWidth=CoordCalc.getXYCoords_MaxX(self.getXY('Met1RouteY_NMUp'))[0][0] - CoordCalc.getXYCoords_MinX(self.getXY('Met1RouteY_NMUp'))[0][0] + self.getXWidth('Met1RouteY_NMUp'),
            _YWidth=YWidth_Met1HorizontalRouting
        )
        self._DesignParameter['Met1RouteX_NMUp']['_XYCoordinates'] = [[
            (self.getXY('Met1RouteY_NMUp')[0][0] + self.getXY('Met1RouteY_NMUp')[-1][0]) / 2,
            self.getXY('Met1RouteY_NMUp')[0][1] + self.getYWidth('Met1RouteY_NMUp') / 2 - self.getYWidth('Met1RouteX_NMUp') / 2
        ]]

        # VSS Via
        tmpXYs = []
        for XYs in self.getXY('Met1RouteY_NM2VSS'):
            tmpXYs.append(CoordCalc.Sum(XYs, [0, -self.getYWidth('Met1RouteY_NM2VSS') / 2]))

        self._DesignParameter['ViaForVSS'] = self._SrefElementDeclaration(_DesignObj=Z_PWR_CNT.Z_PWR_CNT(_Name='ViaForVSSIn{}'.format(_Name)))[0]
        self._DesignParameter['ViaForVSS']['_DesignObj']._CalculateDesignParameter(**dict(_Xnum=1, _Xdistance=0))
        self._DesignParameter['ViaForVSS']['_XYCoordinates'] = tmpXYs

        # Nwell Layer
        YCoord_NwellTopBoundary = self.getXY('VDDRail', '_ODLayer')[0][1] + self.getYWidth('VDDRail', '_ODLayer') / 2 + drc._NwMinEnclosurePactive
        YCoord_NwellBotBoundary = self.getXY('PMOS', '_ODLayer')[0][1] - (self.getYWidth('PMOS', '_ODLayer') / 2 + drc._NwMinEnclosurePactive)
        self._DesignParameter['NwellLayer'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['NWELL'][0], _Datatype=DesignParameters._LayerMapping['NWELL'][1],
            _XWidth=self.getXWidth('PMOS', '_ODLayer') + 2 * drc._NwMinEnclosurePactive2,
            _YWidth=YCoord_NwellTopBoundary - YCoord_NwellBotBoundary,
            _XYCoordinates=[[0, (YCoord_NwellTopBoundary + YCoord_NwellBotBoundary)/2]]
        )

        self._DesignParameter['XVTLayer'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping[XVT][0], _Datatype=DesignParameters._LayerMapping[XVT][1],
            _XWidth=self.getXWidth('VSSRail', '_ODLayer'),
            _YWidth=CellHeight,
            _XYCoordinates=[[0, CellHeight / 2]]
        )

        # Met1YRouting NMout - PMout
        XWidth_Met1YRouting = self.getXWidth('Met1RouteY_NMUp')
        self._DesignParameter['Met1RouteY_NM2PM'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1'][0],
            _Datatype=DesignParameters._LayerMapping['METAL1'][1],
            _XWidth=XWidth_Met1YRouting,
            _YWidth=(self.getXY('Met1RouteX_PMOutput')[0][1] - self.getYWidth('Met1RouteX_PMOutput')/2) - (self.getXY('Met1RouteX_NMUp')[0][1] + self.getYWidth('Met1RouteX_NMUp')/2)
        )
        self._DesignParameter['Met1RouteY_NM2PM']['_XYCoordinates'] = [[
            self.getXY('NMOS', '_Met1Layer')[NumFinger-1][0] + self.getXWidth('NMOS', '_Met1Layer') / 2 - self.getXWidth('Met1RouteY_NM2PM') / 2,
            ((self.getXY('Met1RouteX_PMOutput')[0][1] - self.getYWidth('Met1RouteX_PMOutput') / 2) + (self.getXY('Met1RouteX_NMUp')[0][1] + self.getYWidth('Met1RouteX_NMUp') / 2)) / 2
        ]]

        if NumFinger == 1:
            del self._DesignParameter['NMOS']
            del self._DesignParameter['Met1RouteX_NMUp']
            del self._DesignParameter['Met1RouteY_NMUp']
            del self._DesignParameter['Met1RouteX_NMDown']
            del self._DesignParameter['Met1RouteY_NMDown']
            del self._DesignParameter['Met1RouteX_NMOutput']
            del self._DesignParameter['Met1RouteY_NMOutput']
            del self._DesignParameter['Met1RouteY_NM2PM']

            self._DesignParameter['NMOS'] = self._SrefElementDeclaration(_DesignObj=CascodeNMOS._CascodeNMOS(_Name='NMOSIn{}'.format(_Name)))[0]
            self._DesignParameter['NMOS']['_DesignObj']._CalculateDesignParameter(
                **dict(_NMOSChannelWidth=NMOSWidth, _NMOSChannellength=ChannelLength,
                       _NMOSDummy=True, _GateSpacing=GateSpacing, _SDWidth=66, _XVT=XVT))
            self._DesignParameter['NMOS']['_XYCoordinates'] = [[0, YCoordOfNM]]

            self._DesignParameter['Met1RouteX_NM2PM'] = self._BoundaryElementDeclaration(
                _Layer=DesignParameters._LayerMapping['METAL1'][0],
                _Datatype=DesignParameters._LayerMapping['METAL1'][1],
                _XWidth=(self.getXY('Met1RouteY_PMOutput')[0][0] + self.getXWidth('Met1RouteY_PMOutput')/2) - (self.getXY('NMOS', '_Met1Layer')[0][0] - self.getXWidth('NMOS', '_Met1Layer') / 2),
                _YWidth=self.getXWidth('NMOS', '_Met1Layer')
            )
            self._DesignParameter['Met1RouteX_NM2PM']['_XYCoordinates'] = [[
                ((self.getXY('Met1RouteY_PMOutput')[0][0] + self.getXWidth('Met1RouteY_PMOutput') / 2) + (self.getXY('NMOS', '_Met1Layer')[0][0] - self.getXWidth('NMOS', '_Met1Layer') / 2)) / 2,
                self.getXY('NMOS', '_Met1Layer')[0][1] + self.getYWidth('NMOS', '_Met1Layer') / 2 - self.getYWidth('Met1RouteX_NM2PM') / 2
            ]]

            self._DesignParameter['Met1RouteY_NM2PM'] = self._BoundaryElementDeclaration(
                _Layer=DesignParameters._LayerMapping['METAL1'][0],
                _Datatype=DesignParameters._LayerMapping['METAL1'][1],
                _XWidth=self.getXWidth('Met1RouteY_PMOutput'),
                _YWidth=(self.getXY('Met1RouteY_PMOutput')[0][1] - self.getYWidth('Met1RouteY_PMOutput')/2) - (self.getXY('Met1RouteX_NM2PM')[0][1] + self.getYWidth('Met1RouteX_NM2PM')/2)
            )
            self._DesignParameter['Met1RouteY_NM2PM']['_XYCoordinates'] = [[
                self.getXY('Met1RouteY_PMOutput')[0][0],
                ((self.getXY('Met1RouteY_PMOutput')[0][1] - self.getYWidth('Met1RouteY_PMOutput') / 2) + (self.getXY('Met1RouteX_NM2PM')[0][1] + self.getYWidth('Met1RouteX_NM2PM') / 2)) / 2
            ]]

        else:
            pass



        # ''' Pin(Label) '''
        # self._DesignParameter['PIN_VSS'] = self._TextElementDeclaration(
        #     _Layer=DesignParameters._LayerMapping['METAL2PIN'][0],
        #     _Datatype=DesignParameters._LayerMapping['METAL2PIN'][1],
        #     _Presentation=[0, 1, 1], _Reflect=[0, 0, 0], _Mag=0.04, _Angle=0, _TEXT='VSS',
        #     _XYCoordinates=[[0, 0]]
        # )
        # self._DesignParameter['PIN_VDD'] = self._TextElementDeclaration(
        #     _Layer=DesignParameters._LayerMapping['METAL2PIN'][0],
        #     _Datatype=DesignParameters._LayerMapping['METAL2PIN'][1],
        #     _Presentation=[0, 1, 1], _Reflect=[0, 0, 0], _Mag=0.04, _Angle=0, _TEXT='VDD',
        #     _XYCoordinates=[[0, CellHeight]]
        # )
        # self._DesignParameter['PIN_A'] = self._TextElementDeclaration(
        #     _Layer=DesignParameters._LayerMapping['METAL1PIN'][0],
        #     _Datatype=DesignParameters._LayerMapping['METAL1PIN'][1],
        #     _Presentation=[0, 1, 1], _Reflect=[0, 0, 0], _Mag=0.01, _Angle=0, _TEXT='A',
        #     _XYCoordinates=[self.getXY('ViaPoly_InputA')[0]],
        # )
        # self._DesignParameter['PIN_B'] = self._TextElementDeclaration(
        #     _Layer=DesignParameters._LayerMapping['METAL1PIN'][0],
        #     _Datatype=DesignParameters._LayerMapping['METAL1PIN'][1],
        #     _Presentation=[0, 1, 1], _Reflect=[0, 0, 0], _Mag=0.01, _Angle=0, _TEXT='B',
        #     _XYCoordinates=[self.getXY('ViaPoly_InputB')[0]],
        # )
        # self._DesignParameter['PIN_Y'] = self._TextElementDeclaration(
        #     _Layer=DesignParameters._LayerMapping['METAL1PIN'][0],
        #     _Datatype=DesignParameters._LayerMapping['METAL1PIN'][1],
        #     _Presentation=[0, 1, 1], _Reflect=[0, 0, 0], _Mag=0.01, _Angle=0, _TEXT='Y',
        #     _XYCoordinates=[[self.getXY('Met1RouteY_NM2PM')[0][0], YCoordOfInputOutput]]
        # )


    def _CalculateDesignParameter_v2(self,CellHeight=1800, YCoordOfNM=350, YCoordOfPM=1400, YCoordOfInputOutput=900,
                                     ChannelLength=30, GateSpacing=100, XVT='SLVT',
                                     NMOSWidth=400, PMOSWidth=400, NumFinger_NM=1, NumFinger_PM=2):

        drc = DRC.DRC()
        _Name = self._DesignParameter['_Name']['_Name']

        # YWidth_Met1HorizontalRouting = drc._Metal1MinWidth  # 50
        YWidth_Met1HorizontalRouting = 66

        ''' --------------------------------------- Supply Rails and MOSFET ---------------------------------------- '''
        self._DesignParameter['VSSRail'] = self._SrefElementDeclaration(_DesignObj=SupplyRails.SupplyRail(_Name='VSSRailIn{}'.format(_Name)))[0]
        self._DesignParameter['VSSRail']['_DesignObj']._CalculateDesignParameter(
            **dict(NumPitch=((max(NumFinger_NM, NumFinger_PM) * 2) + 1), UnitPitch=(GateSpacing + ChannelLength),
                   Met1YWidth=80, Met2YWidth=300, PpNpYWidth=180, isPbody=True, deleteViaAndMet1=False))
        self._DesignParameter['VSSRail']['_XYCoordinates'] = [[0.0, 0.0]]
        self._DesignParameter['VDDRail'] = self._SrefElementDeclaration(_DesignObj=SupplyRails.SupplyRail(_Name='VDDRailIn{}'.format(_Name)))[0]
        self._DesignParameter['VDDRail']['_DesignObj']._CalculateDesignParameter(
            **dict(NumPitch=((max(NumFinger_NM, NumFinger_PM) * 2) + 1), UnitPitch=(ChannelLength + GateSpacing),
                   Met1YWidth=80, Met2YWidth=300, PpNpYWidth=180, isPbody=False, deleteViaAndMet1=False))
        self._DesignParameter['VDDRail']['_XYCoordinates'] = [[0, CellHeight]]

        self._DesignParameter['NMOS'] = self._SrefElementDeclaration(_DesignObj=NMOSWithDummy._NMOS(_Name='NMOSIn{}'.format(_Name)))[0]
        self._DesignParameter['NMOS']['_DesignObj']._CalculateNMOSDesignParameter(
            **dict(_NMOSNumberofGate=(NumFinger_NM * 2), _NMOSChannelWidth=NMOSWidth, _NMOSChannellength=ChannelLength,
                   _NMOSDummy=True, _GateSpacing=GateSpacing, _SDWidth=66, _XVT=XVT))
        self._DesignParameter['NMOS']['_XYCoordinates'] = [[0, YCoordOfNM]]
        self._DesignParameter['PMOS'] = self._SrefElementDeclaration(_DesignObj=PMOSWithDummy._PMOS(_Name='PMOSIn{}'.format(_Name)))[0]
        self._DesignParameter['PMOS']['_DesignObj']._CalculatePMOSDesignParameter(
            **dict(_PMOSNumberofGate=(NumFinger_PM * 2), _PMOSChannelWidth=PMOSWidth, _PMOSChannellength=ChannelLength,
                   _PMOSDummy=True, _GateSpacing=GateSpacing, _SDWidth=66, _XVT=XVT))
        self._DesignParameter['PMOS']['_XYCoordinates'] = [[0, YCoordOfPM]]

        ''' ------------------------------------------ Nwell & XVT Layer ------------------------------------------- '''
        YCoord_NwellTopBoundary = self.getXY('VDDRail', '_ODLayer')[0][1] + self.getYWidth('VDDRail', '_ODLayer') / 2 + drc._NwMinEnclosurePactive
        YCoord_NwellBotBoundary = self.getXY('PMOS', '_ODLayer')[0][1] - (
                    self.getYWidth('PMOS', '_ODLayer') / 2 + drc._NwMinEnclosurePactive)
        self._DesignParameter['NwellLayer'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['NWELL'][0], _Datatype=DesignParameters._LayerMapping['NWELL'][1],
            _XWidth=self.getXWidth('PMOS', '_ODLayer') + 2 * drc._NwMinEnclosurePactive2,
            _YWidth=YCoord_NwellTopBoundary - YCoord_NwellBotBoundary,
            _XYCoordinates=[[0, (YCoord_NwellTopBoundary + YCoord_NwellBotBoundary) / 2]]
        )
        self._DesignParameter['XVTLayer'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping[XVT][0], _Datatype=DesignParameters._LayerMapping[XVT][1],
            _XWidth=self.getXWidth('VSSRail', '_ODLayer'),
            _YWidth=CellHeight,
            _XYCoordinates=[[0, CellHeight / 2]]
        )


        self._DesignParameter['Met1RouteY_VDD'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1'][0],
            _Datatype=DesignParameters._LayerMapping['METAL1'][1],
            _XWidth=self.getXWidth('PMOS', '_Met1Layer'),
            _YWidth=CellHeight - (self.getXY('PMOS', '_Met1Layer')[0][1] + self.getYWidth('PMOS', '_Met1Layer') / 2)
        )
        tmpXYs = []
        for i, XYs in enumerate(self.getXY('PMOS', '_Met1Layer')):
            if i % 2 == 0:
                tmpXYs.append([XYs[0], CellHeight - self.getYWidth('Met1RouteY_VDD') / 2])
        self._DesignParameter['Met1RouteY_VDD']['_XYCoordinates'] = tmpXYs


        ''' Optional '''
        # XYList = []
        # xy_offset = (0, ((- (self._DesignParameter['PMOS']['_XYCoordinates'][0][1] + self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1])) + CellHeight))
        # for i in range(len(self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'])):
        #     if ((i % 2) == 0):
        #         xy = (self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i][0] if (type(self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i][0]) == list) else self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i])
        #         XYList.append([((x + y) + z) for (x, y, z) in zip([(0 + self._DesignParameter['PMOS']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['PMOS']['_XYCoordinates'][0][1])], xy, xy_offset)])
        # self._DesignParameter['ViaForVDD'] = self._SrefElementDeclaration(_DesignObj=Z_PWR_CNT.Z_PWR_CNT(_Name='ViaForVDDIn{}'.format(_Name)))[0]
        # self._DesignParameter['ViaForVDD']['_DesignObj']._CalculateDesignParameter(**dict(_Xnum=1, _Xdistance=0))
        # self._DesignParameter['ViaForVDD']['_XYCoordinates'] = XYList


        XYList = []
        xy_offset = (0, (((- self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']) / 2) - ((drc._Metal1MinSpaceAtCorner + YWidth_Met1HorizontalRouting) / 2)))  # Manually Edited
        for i in range(len(self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'])):
            if (i % 2) == 1:
                XYList.append([((x + y) + z) for (x, y, z) in zip([(0 + self._DesignParameter['PMOS']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['PMOS']['_XYCoordinates'][0][1])], self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i], xy_offset)])

        self._DesignParameter['Met1RouteY_PMOutput'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _XWidth=self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'], _YWidth=(drc._Metal1MinSpaceAtCorner + YWidth_Met1HorizontalRouting))  # Manually Edited
        self._DesignParameter['Met1RouteY_PMOutput']['_XYCoordinates'] = XYList
        self._DesignParameter['Met1RouteX_PMOutput'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _XWidth=((self._DesignParameter['Met1RouteY_PMOutput']['_XYCoordinates'][(- 1)][0] + (self._DesignParameter['Met1RouteY_PMOutput']['_XWidth'] / 2)) - (self._DesignParameter['Met1RouteY_PMOutput']['_XYCoordinates'][0][0] - (self._DesignParameter['Met1RouteY_PMOutput']['_XWidth'] / 2))), _YWidth=YWidth_Met1HorizontalRouting)  # Manually Edit
        self._DesignParameter['Met1RouteX_PMOutput']['_XYCoordinates'] = [[(((self._DesignParameter['Met1RouteY_PMOutput']['_XYCoordinates'][(- 1)][0] + (self._DesignParameter['Met1RouteY_PMOutput']['_XWidth'] / 2)) + (self._DesignParameter['Met1RouteY_PMOutput']['_XYCoordinates'][0][0] - (self._DesignParameter['Met1RouteY_PMOutput']['_XWidth'] / 2))) / 2), ((((self._DesignParameter['PMOS']['_XYCoordinates'][0][1] + self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) - (self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)) - drc._Metal1MinSpaceAtCorner) - (self._DesignParameter['Met1RouteX_PMOutput']['_YWidth'] / 2))]]


        ''' NMOS Met1Routing '''
        self._DesignParameter['Met1RouteY_NMOutput'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1'][0],
            _Datatype=DesignParameters._LayerMapping['METAL1'][1],
            _XWidth=self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'],
            _YWidth=(drc._Metal1MinSpaceAtCorner + YWidth_Met1HorizontalRouting)
        )
        self._DesignParameter['Met1RouteY_NMDown'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1'][0],
            _Datatype=DesignParameters._LayerMapping['METAL1'][1],
            _XWidth=self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'],
            _YWidth=(drc._Metal1MinSpaceAtCorner + YWidth_Met1HorizontalRouting)
        )

        tmpXYs_NMout = []
        tmpXYs_NMintermediate = []
        for i in range(0, NumFinger_NM + 1):
            if i % 2 == 1:
                tmpXYs_NMout.append(
                    CoordCalc.Sum(self.getXY('NMOS', '_Met1Layer')[NumFinger_NM + i],
                                  [0, self.getYWidth('NMOS', '_Met1Layer')/2],
                                  [0, self.getYWidth('Met1RouteY_NMOutput')/2])
                )
            else:
                tmpXYs_NMintermediate.append(
                    CoordCalc.Sum(self.getXY('NMOS', '_Met1Layer')[NumFinger_NM + i],
                                  [0, -self.getYWidth('NMOS', '_Met1Layer')/2],
                                  [0, -self.getYWidth('Met1RouteY_NMDown')/2])
                )
        self._DesignParameter['Met1RouteY_NMOutput']['_XYCoordinates'] = tmpXYs_NMout
        self._DesignParameter['Met1RouteY_NMDown']['_XYCoordinates'] = tmpXYs_NMintermediate


        self._DesignParameter['Met1RouteX_NMOutput'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1'][0],
            _Datatype=DesignParameters._LayerMapping['METAL1'][1],
            _XWidth=CoordCalc.getXYCoords_MaxX(self.getXY('Met1RouteY_NMOutput'))[0][0] - CoordCalc.getXYCoords_MinX(self.getXY('Met1RouteY_NMOutput'))[0][0] + self.getXWidth('Met1RouteY_NMOutput'),
            _YWidth=YWidth_Met1HorizontalRouting
        )
        self._DesignParameter['Met1RouteX_NMOutput']['_XYCoordinates'] = [[
            (self.getXY('Met1RouteY_NMOutput')[0][0] + self.getXY('Met1RouteY_NMOutput')[-1][0]) / 2,
            self.getXY('Met1RouteY_NMOutput')[0][1] + self.getYWidth('Met1RouteY_NMOutput') / 2 - self.getYWidth('Met1RouteX_NMOutput') / 2
        ]]

        self._DesignParameter['Met1RouteX_NMDown'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1'][0],
            _Datatype=DesignParameters._LayerMapping['METAL1'][1],
            _XWidth=CoordCalc.getXYCoords_MaxX(self.getXY('Met1RouteY_NMDown'))[0][0] - CoordCalc.getXYCoords_MinX(self.getXY('Met1RouteY_NMDown'))[0][0] + self.getXWidth('Met1RouteY_NMDown'),
            _YWidth=YWidth_Met1HorizontalRouting
        )
        self._DesignParameter['Met1RouteX_NMDown']['_XYCoordinates'] = [[
            (self.getXY('Met1RouteY_NMDown')[0][0] + self.getXY('Met1RouteY_NMDown')[-1][0]) / 2,
            self.getXY('Met1RouteY_NMDown')[0][1] - self.getYWidth('Met1RouteY_NMDown')/2 + self.getYWidth('Met1RouteX_NMDown')/2
        ]]

        self._DesignParameter['Met1RouteY_NMUp'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1'][0],
            _Datatype=DesignParameters._LayerMapping['METAL1'][1],
            _XWidth=self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'],
            _YWidth=(drc._Metal1MinSpaceAtCorner + YWidth_Met1HorizontalRouting)
        )
        self._DesignParameter['Met1RouteY_NM2VSS'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1'][0],
            _Datatype=DesignParameters._LayerMapping['METAL1'][1],
            _XWidth=self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'],
            _YWidth=self.getXY('NMOS', '_Met1Layer')[0][1] - self.getYWidth('NMOS', '_Met1Layer')/2
        )
        tmpXYs_NMup = []
        tmpXYs_NM2VSS = []
        for i in range(0, NumFinger_NM + 1):
            if i % 2 == 0:
                tmpXYs_NMup.append(
                    CoordCalc.Sum(self.getXY('NMOS', '_Met1Layer')[NumFinger_NM - i],
                                  [0, self.getYWidth('NMOS', '_Met1Layer') / 2],
                                  [0, self.getYWidth('Met1RouteY_NMUp') / 2])
                )
            else:
                tmpXYs_NM2VSS.append(
                    CoordCalc.Sum(self.getXY('NMOS', '_Met1Layer')[NumFinger_NM - i],
                                  [0, -self.getYWidth('NMOS', '_Met1Layer') / 2],
                                  [0, -self.getYWidth('Met1RouteY_NM2VSS') / 2])
                )
        self._DesignParameter['Met1RouteY_NMUp']['_XYCoordinates'] = tmpXYs_NMup
        self._DesignParameter['Met1RouteY_NM2VSS']['_XYCoordinates'] = tmpXYs_NM2VSS

        self._DesignParameter['Met1RouteX_NMUp'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1'][0],
            _Datatype=DesignParameters._LayerMapping['METAL1'][1],
            _XWidth=CoordCalc.getXYCoords_MaxX(self.getXY('Met1RouteY_NMUp'))[0][0] - CoordCalc.getXYCoords_MinX(self.getXY('Met1RouteY_NMUp'))[0][0] + self.getXWidth('Met1RouteY_NMUp'),
            _YWidth=YWidth_Met1HorizontalRouting
        )
        self._DesignParameter['Met1RouteX_NMUp']['_XYCoordinates'] = [[
            (self.getXY('Met1RouteY_NMUp')[0][0] + self.getXY('Met1RouteY_NMUp')[-1][0]) / 2,
            self.getXY('Met1RouteY_NMUp')[0][1] + self.getYWidth('Met1RouteY_NMUp') / 2 - self.getYWidth('Met1RouteX_NMUp') / 2
        ]]

        ''' Optional '''
        # # VSS Via
        # tmpXYs = []
        # for XYs in self.getXY('Met1RouteY_NM2VSS'):
        #     tmpXYs.append(CoordCalc.Sum(XYs, [0, -self.getYWidth('Met1RouteY_NM2VSS') / 2]))
        #
        # self._DesignParameter['ViaForVSS'] = self._SrefElementDeclaration(_DesignObj=Z_PWR_CNT.Z_PWR_CNT(_Name='ViaForVSSIn{}'.format(_Name)))[0]
        # self._DesignParameter['ViaForVSS']['_DesignObj']._CalculateDesignParameter(**dict(_Xnum=1, _Xdistance=0))
        # self._DesignParameter['ViaForVSS']['_XYCoordinates'] = tmpXYs

        ''' Input Via Out Output Met1 '''
        self._DesignParameter['Met1RouteY_OutputPM2NM'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1'][0],
            _Datatype=DesignParameters._LayerMapping['METAL1'][1],
            _XWidth=self.getXWidth('Met1RouteY_PMOutput'),
            _YWidth=(self.getXY('Met1RouteX_PMOutput')[0][1] + self.getYWidth('Met1RouteX_PMOutput') / 2) - (self.getXY('Met1RouteX_NMOutput')[0][1] - self.getYWidth('Met1RouteX_NMOutput') / 2)
        )

        self._DesignParameter['ViaPoly_InputAB'] = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1_resize._ViaPoly2Met1_resize(_Name='ViaPoly_InputABIn{}'.format(_Name)))[0]
        self._DesignParameter['ViaPoly_InputAB']['_DesignObj']._CalculateDesignParameter(
            **dict(_ViaPoly2Met1NumberOfCOX=1, _ViaPoly2Met1NumberOfCOY=2,
                   Met1XWidth=66, Met1YWidth=200, POXWidth=50, POYWidth=200))


        if max(NumFinger_NM, NumFinger_PM) == 1:                    # (N,P) = (1,1)
            XCoord_OutputMet1Y = 0
            XCoord_InputA = self.getXY('PMOS', '_Met1Layer')[0][0]
            XCoord_InputB = self.getXY('PMOS', '_Met1Layer')[-1][0]
        elif NumFinger_NM == 1:                                     # (N,P) = (1,2), (1,3), ...  rare condition
            XCoord_OutputMet1Y = 0
            XCoord_InputA = - max(NumFinger_NM, NumFinger_PM) / 2 * (GateSpacing + ChannelLength)
            XCoord_InputB = + max(NumFinger_NM, NumFinger_PM) / 2 * (GateSpacing + ChannelLength)
        elif max(NumFinger_NM, NumFinger_PM) == 2:                  # (N,P) = (2,1), (2,2)
            XCoord_OutputMet1Y = self.getXY('PMOS', '_Met1Layer')[-1][0]
            XCoord_InputA = - max(NumFinger_NM, NumFinger_PM) / 2 * (GateSpacing + ChannelLength)
            XCoord_InputB = + max(NumFinger_NM, NumFinger_PM) / 2 * (GateSpacing + ChannelLength)
        else:
            XCoord_InputA = - max(NumFinger_NM, NumFinger_PM) / 2 * (GateSpacing + ChannelLength)
            XCoord_InputB = + max(NumFinger_NM, NumFinger_PM) // 2 * (GateSpacing + ChannelLength)
            XCoord_OutputMet1Y = XCoord_InputB + (GateSpacing + ChannelLength)


        self._DesignParameter['Met1RouteY_OutputPM2NM']['_XYCoordinates'] = [[
            XCoord_OutputMet1Y,
            ((self.getXY('Met1RouteX_PMOutput')[0][1] + self.getYWidth('Met1RouteX_PMOutput') / 2) + (self.getXY('Met1RouteX_NMOutput')[0][1] - self.getYWidth('Met1RouteX_NMOutput') / 2)) / 2
        ]]
        self._DesignParameter['ViaPoly_InputAB']['_XYCoordinates'] = [
            [XCoord_InputA, YCoordOfInputOutput],
            [XCoord_InputB, YCoordOfInputOutput]
        ]



        RightBoundary_Met1X_OutputPM2NM_NMside = max(
            self.getXY('Met1RouteY_OutputPM2NM')[0][0] + self.getXWidth('Met1RouteY_OutputPM2NM') / 2,
            self.getXY('Met1RouteX_NMOutput')[0][0] + self.getXWidth('Met1RouteX_NMOutput') / 2
        )
        LeftBoundary_Met1X_OutputPM2NM_NMside = min(
            self.getXY('Met1RouteY_OutputPM2NM')[0][0] - self.getXWidth('Met1RouteY_OutputPM2NM') / 2,
            self.getXY('Met1RouteX_NMOutput')[0][0] + self.getXWidth('Met1RouteX_NMOutput') / 2
        )
        self._DesignParameter['Met1RouteX_OutputPM2NM_NMside'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1'][0],
            _Datatype=DesignParameters._LayerMapping['METAL1'][1],
            _XWidth=RightBoundary_Met1X_OutputPM2NM_NMside - LeftBoundary_Met1X_OutputPM2NM_NMside,
            _YWidth=YWidth_Met1HorizontalRouting
        )
        self._DesignParameter['Met1RouteX_OutputPM2NM_NMside']['_XYCoordinates'] = [[
            (RightBoundary_Met1X_OutputPM2NM_NMside + LeftBoundary_Met1X_OutputPM2NM_NMside) / 2,
            self.getXY('Met1RouteX_NMOutput')[0][1]
        ]]

        self._DesignParameter['Met1RouteX_OutputPM2NM_PMside'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1'][0],
            _Datatype=DesignParameters._LayerMapping['METAL1'][1],
            _XWidth=(self.getXY('Met1RouteY_OutputPM2NM')[0][0] + self.getXWidth('Met1RouteY_OutputPM2NM') / 2) - (self.getXY('Met1RouteY_PMOutput')[0][0] - self.getXWidth('Met1RouteY_PMOutput') / 2),
            _YWidth=YWidth_Met1HorizontalRouting
        )
        self._DesignParameter['Met1RouteX_OutputPM2NM_PMside']['_XYCoordinates'] = [[
            ((self.getXY('Met1RouteY_OutputPM2NM')[0][0] + self.getXWidth('Met1RouteY_OutputPM2NM') / 2) + (self.getXY('Met1RouteY_PMOutput')[0][0] - self.getXWidth('Met1RouteY_PMOutput') / 2)) / 2,
            self.getXY('Met1RouteY_OutputPM2NM')[0][1] + self.getYWidth('Met1RouteY_OutputPM2NM') / 2 - self.getYWidth('Met1RouteX_OutputPM2NM_PMside') / 2
        ]]


        ''' PolyRouting For Input Gate '''
        self._DesignParameter['PolyRouteY_PMB'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['POLY'][0],
            _Datatype=DesignParameters._LayerMapping['POLY'][1],
            _XWidth=ChannelLength,
            _YWidth=(self.getXY('PMOS', '_POLayer')[0][1] - self.getYWidth('PMOS', '_POLayer') / 2) - (self.getXY('ViaPoly_InputAB', '_POLayer')[0][1] + self.getYWidth('ViaPoly_InputAB', '_POLayer') / 2)
        )
        tmpXYs = []
        for i, XYs in enumerate(self.getXY('PMOS', '_POLayer')):
            if i >= NumFinger_PM:
                tmpXYs.append([
                    XYs[0],
                    ((self.getXY('PMOS', '_POLayer')[0][1] - self.getYWidth('PMOS', '_POLayer') / 2) + (self.getXY('ViaPoly_InputAB', '_POLayer')[0][1] + self.getYWidth('ViaPoly_InputAB', '_POLayer') / 2)) / 2
                ])
        self._DesignParameter['PolyRouteY_PMB']['_XYCoordinates'] = tmpXYs

        self._DesignParameter['PolyRouteY_NMB'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['POLY'][0],
            _Datatype=DesignParameters._LayerMapping['POLY'][1],
            _XWidth=ChannelLength,
            _YWidth=(self.getXY('ViaPoly_InputAB', '_POLayer')[0][1] - self.getYWidth('ViaPoly_InputAB', '_POLayer') / 2) - (self.getXY('NMOS', '_POLayer')[0][1] + self.getYWidth('NMOS', '_POLayer') / 2)
        )
        tmpXYs = []
        for i, XYs in enumerate(self.getXY('NMOS', '_POLayer')):
            if i >= NumFinger_NM:
                tmpXYs.append([
                    XYs[0],
                    ((self.getXY('ViaPoly_InputAB', '_POLayer')[0][1] - self.getYWidth('ViaPoly_InputAB', '_POLayer') / 2) + (self.getXY('NMOS', '_POLayer')[0][1] + self.getYWidth('NMOS', '_POLayer') / 2)) / 2
                ])
        self._DesignParameter['PolyRouteY_NMB']['_XYCoordinates'] = tmpXYs

        RightBoundary_PMPolyB = max(
            self.getXY('ViaPoly_InputAB', '_POLayer')[1][0] + self.getXWidth('ViaPoly_InputAB', '_POLayer') / 2,
            self.getXY('PMOS', '_POLayer')[-1][0] + self.getXWidth('PMOS', '_POLayer') / 2)
        LeftBoundary_PMPolyB = min(
            self.getXY('ViaPoly_InputAB', '_POLayer')[1][0] - self.getXWidth('ViaPoly_InputAB', '_POLayer') / 2,
            self.getXY('PMOS', '_POLayer')[NumFinger_PM][0] - self.getXWidth('PMOS', '_POLayer') / 2)
        self._DesignParameter['PolyRouteX_PM_InputB'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['POLY'][0],
            _Datatype=DesignParameters._LayerMapping['POLY'][1],
            _XWidth=RightBoundary_PMPolyB - LeftBoundary_PMPolyB,
            _YWidth=50
        )
        self._DesignParameter['PolyRouteX_PM_InputB']['_XYCoordinates'] = [[
            (RightBoundary_PMPolyB + LeftBoundary_PMPolyB) / 2,
            self.getXY('PolyRouteY_PMB')[0][1] - self.getYWidth('PolyRouteY_PMB') / 2 - self.getYWidth('PolyRouteX_PM_InputB') / 2
        ]]
        RightBoundary_NMPolyB = max(
            self.getXY('ViaPoly_InputAB', '_POLayer')[1][0] + self.getXWidth('ViaPoly_InputAB', '_POLayer') / 2,
            self.getXY('NMOS', '_POLayer')[-1][0] + self.getXWidth('NMOS', '_POLayer') / 2)
        LeftBoundary_NMPolyB = min(
            self.getXY('ViaPoly_InputAB', '_POLayer')[1][0] - self.getXWidth('ViaPoly_InputAB', '_POLayer') / 2,
            self.getXY('NMOS', '_POLayer')[NumFinger_NM][0] - self.getXWidth('NMOS', '_POLayer') / 2)
        self._DesignParameter['PolyRouteX_NM_InputB'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['POLY'][0],
            _Datatype=DesignParameters._LayerMapping['POLY'][1],
            _XWidth=RightBoundary_NMPolyB - LeftBoundary_NMPolyB,
            _YWidth=self.getYWidth('PolyRouteX_PM_InputB')
        )
        self._DesignParameter['PolyRouteX_NM_InputB']['_XYCoordinates'] = [[
            (RightBoundary_NMPolyB + LeftBoundary_NMPolyB) / 2,
            self.getXY('PolyRouteY_NMB')[0][1] + self.getYWidth('PolyRouteY_NMB') / 2 + self.getYWidth('PolyRouteX_NM_InputB') / 2
        ]]

        RightBoundary_PMPolyA = max(
            self.getXY('ViaPoly_InputAB', '_POLayer')[0][0] + self.getXWidth('ViaPoly_InputAB', '_POLayer') / 2,
            self.getXY('PMOS', '_POLayer')[NumFinger_PM - 1][0] + self.getXWidth('PMOS', '_POLayer') / 2)
        LeftBoundary_PMPolyA = min(
            self.getXY('ViaPoly_InputAB', '_POLayer')[0][0] - self.getXWidth('ViaPoly_InputAB', '_POLayer') / 2,
            self.getXY('PMOS', '_POLayer')[0][0] - self.getXWidth('PMOS', '_POLayer') / 2)
        self._DesignParameter['PolyRouteX_PM_InputA'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['POLY'][0],
            _Datatype=DesignParameters._LayerMapping['POLY'][1],
            _XWidth=RightBoundary_PMPolyA - LeftBoundary_PMPolyA,
            _YWidth=self.getYWidth('PolyRouteX_PM_InputB')
        )
        self._DesignParameter['PolyRouteX_PM_InputA']['_XYCoordinates'] = [[
            (RightBoundary_PMPolyA + LeftBoundary_PMPolyA) / 2,
            self.getXY('ViaPoly_InputAB', '_POLayer')[0][1] + self.getYWidth('ViaPoly_InputAB', '_POLayer') / 2 - self.getYWidth( 'PolyRouteX_PM_InputA') / 2
        ]]

        RightBoundary_NMPolyA = max(
            self.getXY('ViaPoly_InputAB', '_POLayer')[0][0] + self.getXWidth('ViaPoly_InputAB', '_POLayer') / 2,
            self.getXY('NMOS', '_POLayer')[NumFinger_NM - 1][0] + self.getXWidth('NMOS', '_POLayer') / 2)
        LeftBoundary_NMPolyA = min(
            self.getXY('ViaPoly_InputAB', '_POLayer')[0][0] - self.getXWidth('ViaPoly_InputAB', '_POLayer') / 2,
            self.getXY('NMOS', '_POLayer')[0][0] - self.getXWidth('NMOS', '_POLayer') / 2)
        self._DesignParameter['PolyRouteX_NM_InputA'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['POLY'][0],
            _Datatype=DesignParameters._LayerMapping['POLY'][1],
            _XWidth=RightBoundary_NMPolyA - LeftBoundary_NMPolyA,
            _YWidth=self.getYWidth('PolyRouteX_PM_InputB')
        )
        self._DesignParameter['PolyRouteX_NM_InputA']['_XYCoordinates'] = [[
            (RightBoundary_NMPolyA + LeftBoundary_NMPolyA) / 2,
            self.getXY('ViaPoly_InputAB', '_POLayer')[0][1] - self.getYWidth('ViaPoly_InputAB', '_POLayer') / 2 + self.getYWidth('PolyRouteX_NM_InputA') / 2
        ]]

        self._DesignParameter['PolyRouteY_PMA'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['POLY'][0],
            _Datatype=DesignParameters._LayerMapping['POLY'][1],
            _XWidth=ChannelLength,
            _YWidth=((self.getXY('PMOS', '_POLayer')[0][1] - self.getYWidth('PMOS', '_POLayer') / 2) - (
                        self.getXY('PolyRouteX_PM_InputA')[0][1] + self.getYWidth('PolyRouteX_PM_InputA') / 2))
        )
        tmpXYs = []
        for i, XYs in enumerate(self.getXY('PMOS', '_POLayer')):
            if i < NumFinger_PM:
                tmpXYs.append([
                    XYs[0],
                    ((self.getXY('PMOS', '_POLayer')[0][1] - self.getYWidth('PMOS', '_POLayer') / 2) + (self.getXY('PolyRouteX_PM_InputA')[0][1] + self.getYWidth('PolyRouteX_PM_InputA') / 2)) / 2
                ])
        self._DesignParameter['PolyRouteY_PMA']['_XYCoordinates'] = tmpXYs

        self._DesignParameter['PolyRouteY_NMA'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['POLY'][0],
            _Datatype=DesignParameters._LayerMapping['POLY'][1],
            _XWidth=ChannelLength,
            _YWidth=((self.getXY('PolyRouteX_NM_InputA')[0][1] - self.getYWidth('PolyRouteX_NM_InputA') / 2) - (self.getXY('NMOS', '_POLayer')[0][1] + self.getYWidth('NMOS', '_POLayer') / 2))
        )
        tmpXYs = []
        for i, XYs in enumerate(self.getXY('NMOS', '_POLayer')):
            if i < NumFinger_NM:
                tmpXYs.append([
                    XYs[0],
                    ((self.getXY('PolyRouteX_NM_InputA')[0][1] - self.getYWidth('PolyRouteX_NM_InputA') / 2) + (self.getXY('NMOS', '_POLayer')[0][1] + self.getYWidth('NMOS', '_POLayer') / 2)) / 2
                ])
        self._DesignParameter['PolyRouteY_NMA']['_XYCoordinates'] = tmpXYs

        self._DesignParameter['PolyRouteY_PMNMA'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['POLY'][0],
            _Datatype=DesignParameters._LayerMapping['POLY'][1],
            _XWidth=self.getXWidth('ViaPoly_InputAB', '_POLayer'),
            _YWidth=((self.getXY('PolyRouteX_PM_InputA')[0][1] - self.getYWidth('PolyRouteX_PM_InputA') / 2) - (self.getXY('PolyRouteX_NM_InputA')[0][1] + self.getYWidth('PolyRouteX_NM_InputA') / 2)),
            _XYCoordinates=[[
                self.getXY('ViaPoly_InputAB')[0][0],
                ((self.getXY('PolyRouteX_PM_InputA')[0][1] - self.getYWidth('PolyRouteX_PM_InputA') / 2) + (self.getXY('PolyRouteX_NM_InputA')[0][1] + self.getYWidth('PolyRouteX_NM_InputA') / 2)) / 2
            ]]
        )


        if NumFinger_NM == 1:
            del self._DesignParameter['NMOS']
            del self._DesignParameter['Met1RouteX_NMUp']
            del self._DesignParameter['Met1RouteY_NMUp']
            del self._DesignParameter['Met1RouteX_NMDown']
            del self._DesignParameter['Met1RouteY_NMDown']
            del self._DesignParameter['Met1RouteX_NMOutput']
            del self._DesignParameter['Met1RouteY_NMOutput']

            self._DesignParameter['NMOS'] = self._SrefElementDeclaration(_DesignObj=CascodeNMOS._CascodeNMOS(_Name='NMOSIn{}'.format(_Name)))[0]
            self._DesignParameter['NMOS']['_DesignObj']._CalculateDesignParameter(
                **dict(_NMOSChannelWidth=NMOSWidth, _NMOSChannellength=ChannelLength,
                       _NMOSDummy=True, _GateSpacing=GateSpacing, _SDWidth=66, _XVT=XVT))
            self._DesignParameter['NMOS']['_XYCoordinates'] = [[0, YCoordOfNM]]

            self._DesignParameter['Met1RouteX_OutputPM2NM_NMside']['_XYCoordinates'] = [[
                self.getXY('Met1RouteX_OutputPM2NM_NMside')[0][0],
                self.getXY('NMOS', '_Met1Layer')[0][1] + self.getYWidth('NMOS', '_Met1Layer') / 2 - self.getYWidth('Met1RouteX_OutputPM2NM_NMside') / 2
            ]]

            TopBoundary_Met1RouteY_OutputPM2NM = self.getXY('Met1RouteX_OutputPM2NM_PMside')[0][1] + self.getYWidth('Met1RouteX_OutputPM2NM_PMside') / 2
            BotBoundary_Met1RouteY_OutputPM2NM = self.getXY('Met1RouteX_OutputPM2NM_NMside')[0][1] - self.getYWidth('Met1RouteX_OutputPM2NM_NMside') / 2

            self._DesignParameter['Met1RouteY_OutputPM2NM']['_YWidth'] = TopBoundary_Met1RouteY_OutputPM2NM - BotBoundary_Met1RouteY_OutputPM2NM
            self._DesignParameter['Met1RouteY_OutputPM2NM']['_XYCoordinates'] = [[
                0, (TopBoundary_Met1RouteY_OutputPM2NM + BotBoundary_Met1RouteY_OutputPM2NM) / 2
            ]]

        else:
            pass
