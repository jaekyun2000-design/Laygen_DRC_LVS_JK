from generatorLib import StickDiagram
from generatorLib import DesignParameters
import copy
import math
from generatorLib import DRC
from generatorLib.generator_models import SupplyRails
from generatorLib.generator_models import ViaMet12Met2
from generatorLib.generator_models import NMOSWithDummy
from generatorLib.generator_models import ViaPoly2Met1
from generatorLib.generator_models import PMOSWithDummy
from generatorLib.generator_models import ViaPoly2Met1_resize
from generatorLib.generator_models import CascodePMOS
from generatorLib.generator_models import CascodeNMOS


class TristateInverter(StickDiagram._StickDiagram):
    def __init__(self, _DesignParameter=None, _Name='TristateInverter'):
        if _DesignParameter != None:
            self._DesignParameter = _DesignParameter
        else:
            self._DesignParameter = dict(_Name=self._NameDeclaration(_Name=_Name), _GDSFile=self._GDSObjDeclaration(_GDSFile=None))
        self._DesignParameter['_Name']['Name'] = _Name


    def _CalculateDesignParameterFinger1(self,NMOSWidth=250,PMOSWidth=500,ChannelLength=30,XVT='SLVT',GateSpacing=100,CellHeight=1800,VDD2PMOS=400,VSS2NMOS=275):

        drc = DRC.DRC()
        _Name = self._DesignParameter['_Name']['_Name']

        self._DesignParameter['InputVia_EN'] = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1_resize._ViaPoly2Met1_resize(_Name='InputVia_ENIn{}'.format(_Name)))[0]
        self._DesignParameter['InputVia_EN']['_DesignObj']._CalculateDesignParameter(**dict(_ViaPoly2Met1NumberOfCOX=1, _ViaPoly2Met1NumberOfCOY=2, Met1XWidth=66, Met1YWidth=200, POXWidth=40, POYWidth=200))
        self._DesignParameter['InputVia_EN']['_XYCoordinates'] = [[(- 120.0), 650.0]]
        self._DesignParameter['InputVia_ENb'] = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1_resize._ViaPoly2Met1_resize(_Name='InputVia_ENbIn{}'.format(_Name)))[0]
        self._DesignParameter['InputVia_ENb']['_DesignObj']._CalculateDesignParameter(**dict(_ViaPoly2Met1NumberOfCOX=1, _ViaPoly2Met1NumberOfCOY=2, Met1XWidth=66, Met1YWidth=200, POXWidth=40, POYWidth=200))
        self._DesignParameter['InputVia_ENb']['_XYCoordinates'] = [[(- 120.0), 950.0]]
        self._DesignParameter['VSSRail'] = self._SrefElementDeclaration(_DesignObj=SupplyRails.SupplyRail(_Name='VSSRailIn{}'.format(_Name)))[0]
        self._DesignParameter['VSSRail']['_DesignObj']._CalculateDesignParameter(**dict(NumPitch=3, UnitPitch=(GateSpacing + ChannelLength), Met1YWidth=80, Met2YWidth=300, PpNpYWidth=180, isPbody=True))
        self._DesignParameter['VSSRail']['_XYCoordinates'] = [[0.0, 0.0]]
        self._DesignParameter['VDDRail'] = self._SrefElementDeclaration(_DesignObj=SupplyRails.SupplyRail(_Name='VDDRailIn{}'.format(_Name)))[0]
        self._DesignParameter['VDDRail']['_DesignObj']._CalculateDesignParameter(**dict(NumPitch=3, UnitPitch=(GateSpacing + ChannelLength), Met1YWidth=80, Met2YWidth=300, PpNpYWidth=180, isPbody=False))
        self._DesignParameter['VDDRail']['_XYCoordinates'] = [[0, CellHeight]]
        self._DesignParameter['CascodeNMOS'] = self._SrefElementDeclaration(_DesignObj=CascodeNMOS._CascodeNMOS(_Name='CascodeNMOSIn{}'.format(_Name)))[0]
        self._DesignParameter['CascodeNMOS']['_DesignObj']._CalculateDesignParameter(**dict(_NMOSChannelWidth=NMOSWidth, _NMOSChannellength=ChannelLength, _NMOSDummy=True, _XVT=XVT, _GateSpacing=GateSpacing))
        self._DesignParameter['CascodeNMOS']['_XYCoordinates'] = [[0, VSS2NMOS]]
        self._DesignParameter['CascodePMOS'] = self._SrefElementDeclaration(_DesignObj=CascodePMOS._CascodePMOS(_Name='CascodePMOSIn{}'.format(_Name)))[0]
        self._DesignParameter['CascodePMOS']['_DesignObj']._CalculateDesignParameter(**dict(_PMOSChannelWidth=PMOSWidth, _PMOSChannellength=ChannelLength, _PMOSDummy=True, _XVT=XVT, _GateSpacing=GateSpacing))
        self._DesignParameter['CascodePMOS']['_XYCoordinates'] = [[0, (CellHeight - VDD2PMOS)]]
        self._DesignParameter['VSSRouting'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _XWidth=self._DesignParameter['CascodeNMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'], _YWidth=(((self._DesignParameter['CascodeNMOS']['_XYCoordinates'][0][1] + self._DesignParameter['CascodeNMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) + (self._DesignParameter['CascodeNMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)) - ((self._DesignParameter['VSSRail']['_XYCoordinates'][0][1] + self._DesignParameter['VSSRail']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) - (self._DesignParameter['VSSRail']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2))))
        self._DesignParameter['VSSRouting']['_XYCoordinates'] = [[(self._DesignParameter['CascodeNMOS']['_XYCoordinates'][0][0] + self._DesignParameter['CascodeNMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][1][0]), ((((self._DesignParameter['CascodeNMOS']['_XYCoordinates'][0][1] + self._DesignParameter['CascodeNMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) + (self._DesignParameter['CascodeNMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)) + ((self._DesignParameter['VSSRail']['_XYCoordinates'][0][1] + self._DesignParameter['VSSRail']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) - (self._DesignParameter['VSSRail']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2))) / 2)]]
        self._DesignParameter['VDDRouting'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _XWidth=self._DesignParameter['CascodePMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'], _YWidth=(((self._DesignParameter['VDDRail']['_XYCoordinates'][0][1] + self._DesignParameter['VDDRail']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) + (self._DesignParameter['VDDRail']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)) - ((self._DesignParameter['CascodePMOS']['_XYCoordinates'][0][1] + self._DesignParameter['CascodePMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) - (self._DesignParameter['CascodePMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2))))
        self._DesignParameter['VDDRouting']['_XYCoordinates'] = [[(self._DesignParameter['CascodePMOS']['_XYCoordinates'][0][0] + self._DesignParameter['CascodePMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][1][0]), ((((self._DesignParameter['VDDRail']['_XYCoordinates'][0][1] + self._DesignParameter['VDDRail']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) + (self._DesignParameter['VDDRail']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)) + ((self._DesignParameter['CascodePMOS']['_XYCoordinates'][0][1] + self._DesignParameter['CascodePMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) - (self._DesignParameter['CascodePMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2))) / 2)]]
        self._DesignParameter['POLY_boundary_30'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _XWidth=ChannelLength, _YWidth=(((self._DesignParameter['InputVia_EN']['_XYCoordinates'][0][1] + self._DesignParameter['InputVia_EN']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1]) - (self._DesignParameter['InputVia_EN']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2)) - ((self._DesignParameter['CascodeNMOS']['_XYCoordinates'][0][1] + self._DesignParameter['CascodeNMOS']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1]) + (self._DesignParameter['CascodeNMOS']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2))))
        self._DesignParameter['POLY_boundary_30']['_XYCoordinates'] = [[(self._DesignParameter['CascodeNMOS']['_XYCoordinates'][0][0] + self._DesignParameter['CascodeNMOS']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]), ((((self._DesignParameter['InputVia_EN']['_XYCoordinates'][0][1] + self._DesignParameter['InputVia_EN']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1]) - (self._DesignParameter['InputVia_EN']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2)) + ((self._DesignParameter['CascodeNMOS']['_XYCoordinates'][0][1] + self._DesignParameter['CascodeNMOS']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1]) + (self._DesignParameter['CascodeNMOS']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2))) / 2)]]
        self._DesignParameter['POLY_boundary_29'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _XWidth=(((self._DesignParameter['CascodeNMOS']['_XYCoordinates'][0][0] + self._DesignParameter['CascodeNMOS']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) + (self._DesignParameter['CascodeNMOS']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)) - ((self._DesignParameter['InputVia_EN']['_XYCoordinates'][0][0] + self._DesignParameter['InputVia_EN']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) + (self._DesignParameter['InputVia_EN']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2))), _YWidth=((self._DesignParameter['InputVia_EN']['_XYCoordinates'][0][1] + self._DesignParameter['InputVia_EN']['_DesignObj']._DesignParameter['_COLayer']['_XYCoordinates'][0][1]) - ((self._DesignParameter['InputVia_EN']['_XYCoordinates'][0][1] + self._DesignParameter['InputVia_EN']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1]) - (self._DesignParameter['InputVia_EN']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2))))
        self._DesignParameter['POLY_boundary_29']['_XYCoordinates'] = [[((((self._DesignParameter['InputVia_EN']['_XYCoordinates'][0][0] + self._DesignParameter['InputVia_EN']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) + (self._DesignParameter['InputVia_EN']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)) + ((self._DesignParameter['CascodeNMOS']['_XYCoordinates'][0][0] + self._DesignParameter['CascodeNMOS']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) + (self._DesignParameter['CascodeNMOS']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2))) / 2), (((self._DesignParameter['InputVia_EN']['_XYCoordinates'][0][1] + self._DesignParameter['InputVia_EN']['_DesignObj']._DesignParameter['_COLayer']['_XYCoordinates'][0][1]) + ((self._DesignParameter['InputVia_EN']['_XYCoordinates'][0][1] + self._DesignParameter['InputVia_EN']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1]) - (self._DesignParameter['InputVia_EN']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2))) / 2)]]
        self._DesignParameter['POLY_boundary_24'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _XWidth=ChannelLength, _YWidth=(((self._DesignParameter['CascodePMOS']['_XYCoordinates'][0][1] + self._DesignParameter['CascodePMOS']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1]) - (self._DesignParameter['CascodePMOS']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2)) - ((self._DesignParameter['InputVia_ENb']['_XYCoordinates'][0][1] + self._DesignParameter['InputVia_ENb']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1]) + (self._DesignParameter['InputVia_ENb']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2))))
        self._DesignParameter['POLY_boundary_24']['_XYCoordinates'] = [[(self._DesignParameter['CascodePMOS']['_XYCoordinates'][0][0] + self._DesignParameter['CascodePMOS']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]), ((((self._DesignParameter['CascodePMOS']['_XYCoordinates'][0][1] + self._DesignParameter['CascodePMOS']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1]) - (self._DesignParameter['CascodePMOS']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2)) + ((self._DesignParameter['InputVia_ENb']['_XYCoordinates'][0][1] + self._DesignParameter['InputVia_ENb']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1]) + (self._DesignParameter['InputVia_ENb']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2))) / 2)]]
        self._DesignParameter['POLY_boundary_23'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _XWidth=(((self._DesignParameter['CascodePMOS']['_XYCoordinates'][0][0] + self._DesignParameter['CascodePMOS']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) + (self._DesignParameter['CascodePMOS']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)) - ((self._DesignParameter['InputVia_ENb']['_XYCoordinates'][0][0] + self._DesignParameter['InputVia_ENb']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) + (self._DesignParameter['InputVia_ENb']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2))), _YWidth=(((self._DesignParameter['InputVia_ENb']['_XYCoordinates'][0][1] + self._DesignParameter['InputVia_ENb']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1]) + (self._DesignParameter['InputVia_ENb']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2)) - (self._DesignParameter['InputVia_ENb']['_XYCoordinates'][0][1] + self._DesignParameter['InputVia_ENb']['_DesignObj']._DesignParameter['_COLayer']['_XYCoordinates'][1][1])))
        self._DesignParameter['POLY_boundary_23']['_XYCoordinates'] = [[((((self._DesignParameter['CascodePMOS']['_XYCoordinates'][0][0] + self._DesignParameter['CascodePMOS']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) + (self._DesignParameter['CascodePMOS']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)) + ((self._DesignParameter['InputVia_ENb']['_XYCoordinates'][0][0] + self._DesignParameter['InputVia_ENb']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) + (self._DesignParameter['InputVia_ENb']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2))) / 2), ((((self._DesignParameter['InputVia_ENb']['_XYCoordinates'][0][1] + self._DesignParameter['InputVia_ENb']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1]) + (self._DesignParameter['InputVia_ENb']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2)) + (self._DesignParameter['InputVia_ENb']['_XYCoordinates'][0][1] + self._DesignParameter['InputVia_ENb']['_DesignObj']._DesignParameter['_COLayer']['_XYCoordinates'][1][1])) / 2)]]
        self._DesignParameter['NWELL_boundary_2'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['NWELL'][0], _Datatype=DesignParameters._LayerMapping['NWELL'][1], _XWidth=max((self._DesignParameter['CascodePMOS']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth'] + (2 * drc._NwMinEnclosurePactive2)), (self._DesignParameter['VDDRail']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth'] + (2 * drc._NwMinEnclosurePactive))), _YWidth=((((self._DesignParameter['VDDRail']['_XYCoordinates'][0][1] + self._DesignParameter['VDDRail']['_DesignObj']._DesignParameter['_ODLayer']['_XYCoordinates'][0][1]) + (self._DesignParameter['VDDRail']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth'] / 2)) - ((self._DesignParameter['CascodePMOS']['_XYCoordinates'][0][1] + self._DesignParameter['CascodePMOS']['_DesignObj']._DesignParameter['_ODLayer']['_XYCoordinates'][0][1]) - (self._DesignParameter['CascodePMOS']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth'] / 2))) + (2 * drc._NwMinEnclosurePactive)))
        self._DesignParameter['NWELL_boundary_2']['_XYCoordinates'] = [[0, ((((self._DesignParameter['VDDRail']['_XYCoordinates'][0][1] + self._DesignParameter['VDDRail']['_DesignObj']._DesignParameter['_ODLayer']['_XYCoordinates'][0][1]) + (self._DesignParameter['VDDRail']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth'] / 2)) + ((self._DesignParameter['CascodePMOS']['_XYCoordinates'][0][1] + self._DesignParameter['CascodePMOS']['_DesignObj']._DesignParameter['_ODLayer']['_XYCoordinates'][0][1]) - (self._DesignParameter['CascodePMOS']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth'] / 2))) / 2)]]
        self._DesignParameter['OutputRouting'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=self._DesignParameter['CascodePMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'])
        self._DesignParameter['OutputRouting']['_XYCoordinates'] = [[[((self._DesignParameter['CascodePMOS']['_XYCoordinates'][0][0] + self._DesignParameter['CascodePMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0]) + (self._DesignParameter['CascodePMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] / 2)), (((self._DesignParameter['CascodePMOS']['_XYCoordinates'][0][1] + self._DesignParameter['CascodePMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) - (self._DesignParameter['CascodePMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)) + (self._DesignParameter['CascodePMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] / 2))], [(self._DesignParameter['CascodePMOS']['_XYCoordinates'][0][0] + self._DesignParameter['CascodePMOS']['_DesignObj']._DesignParameter['_PPLayer']['_XYCoordinates'][0][0]), (((self._DesignParameter['CascodePMOS']['_XYCoordinates'][0][1] + self._DesignParameter['CascodePMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) - (self._DesignParameter['CascodePMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)) + (self._DesignParameter['CascodePMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] / 2))], [(self._DesignParameter['CascodePMOS']['_XYCoordinates'][0][0] + self._DesignParameter['CascodePMOS']['_DesignObj']._DesignParameter['_PPLayer']['_XYCoordinates'][0][0]), (((self._DesignParameter['CascodeNMOS']['_XYCoordinates'][0][1] + self._DesignParameter['CascodeNMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) + (self._DesignParameter['CascodeNMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)) - (self._DesignParameter['CascodePMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] / 2))], [((self._DesignParameter['CascodeNMOS']['_XYCoordinates'][0][0] + self._DesignParameter['CascodeNMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0]) + (self._DesignParameter['CascodeNMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] / 2)), (((self._DesignParameter['CascodeNMOS']['_XYCoordinates'][0][1] + self._DesignParameter['CascodeNMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) + (self._DesignParameter['CascodeNMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)) - (self._DesignParameter['CascodePMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] / 2))]]]
        self._DesignParameter['InputVia_A'] = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1_resize._ViaPoly2Met1_resize(_Name='InputVia_AIn{}'.format(_Name)))[0]
        self._DesignParameter['InputVia_A']['_DesignObj']._CalculateDesignParameter(**dict(_ViaPoly2Met1NumberOfCOX=1, _ViaPoly2Met1NumberOfCOY=2, Met1XWidth=66, Met1YWidth=200, POXWidth=40, POYWidth=200))
        self._DesignParameter['InputVia_A']['_XYCoordinates'] = [[(self._DesignParameter['CascodeNMOS']['_XYCoordinates'][0][0] + self._DesignParameter['CascodeNMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][(- 1)][0]), ((self._DesignParameter['CascodeNMOS']['_XYCoordinates'][0][1] + self._DesignParameter['CascodePMOS']['_XYCoordinates'][0][1]) / 2)]]
        self._DesignParameter['POLY_boundary_21'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _XWidth=ChannelLength, _YWidth=(((self._DesignParameter['CascodePMOS']['_XYCoordinates'][0][1] + self._DesignParameter['CascodePMOS']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][1][1]) - (self._DesignParameter['CascodePMOS']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2)) - ((self._DesignParameter['InputVia_A']['_XYCoordinates'][0][1] + self._DesignParameter['InputVia_A']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1]) + (self._DesignParameter['InputVia_A']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2))))
        self._DesignParameter['POLY_boundary_21']['_XYCoordinates'] = [[(self._DesignParameter['CascodePMOS']['_XYCoordinates'][0][0] + self._DesignParameter['CascodePMOS']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][1][0]), ((((self._DesignParameter['CascodePMOS']['_XYCoordinates'][0][1] + self._DesignParameter['CascodePMOS']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][1][1]) - (self._DesignParameter['CascodePMOS']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2)) + ((self._DesignParameter['InputVia_A']['_XYCoordinates'][0][1] + self._DesignParameter['InputVia_A']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1]) + (self._DesignParameter['InputVia_A']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2))) / 2)]]
        self._DesignParameter['POLY_boundary_28'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _XWidth=ChannelLength, _YWidth=(((self._DesignParameter['InputVia_A']['_XYCoordinates'][0][1] + self._DesignParameter['InputVia_A']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1]) - (self._DesignParameter['InputVia_A']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2)) - ((self._DesignParameter['CascodeNMOS']['_XYCoordinates'][0][1] + self._DesignParameter['CascodeNMOS']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][1][1]) + (self._DesignParameter['CascodeNMOS']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2))))
        self._DesignParameter['POLY_boundary_28']['_XYCoordinates'] = [[(self._DesignParameter['CascodeNMOS']['_XYCoordinates'][0][0] + self._DesignParameter['CascodeNMOS']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][1][0]), ((((self._DesignParameter['InputVia_A']['_XYCoordinates'][0][1] + self._DesignParameter['InputVia_A']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1]) - (self._DesignParameter['InputVia_A']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2)) + ((self._DesignParameter['CascodeNMOS']['_XYCoordinates'][0][1] + self._DesignParameter['CascodeNMOS']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][1][1]) + (self._DesignParameter['CascodeNMOS']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2))) / 2)]]
        self._DesignParameter['POLY_boundary_25'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _XWidth=(((self._DesignParameter['InputVia_A']['_XYCoordinates'][0][0] + self._DesignParameter['InputVia_A']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['InputVia_A']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)) - ((self._DesignParameter['CascodePMOS']['_XYCoordinates'][0][0] + self._DesignParameter['CascodePMOS']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][1][0]) - (self._DesignParameter['CascodePMOS']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2))), _YWidth=(((self._DesignParameter['InputVia_A']['_XYCoordinates'][0][1] + self._DesignParameter['InputVia_A']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1]) + (self._DesignParameter['InputVia_A']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2)) - (self._DesignParameter['InputVia_A']['_XYCoordinates'][0][1] + self._DesignParameter['InputVia_A']['_DesignObj']._DesignParameter['_COLayer']['_XYCoordinates'][1][1])))
        self._DesignParameter['POLY_boundary_25']['_XYCoordinates'] = [[((((self._DesignParameter['InputVia_A']['_XYCoordinates'][0][0] + self._DesignParameter['InputVia_A']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['InputVia_A']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)) + ((self._DesignParameter['CascodePMOS']['_XYCoordinates'][0][0] + self._DesignParameter['CascodePMOS']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][1][0]) - (self._DesignParameter['CascodePMOS']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2))) / 2), ((((self._DesignParameter['InputVia_A']['_XYCoordinates'][0][1] + self._DesignParameter['InputVia_A']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1]) + (self._DesignParameter['InputVia_A']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2)) + (self._DesignParameter['InputVia_A']['_XYCoordinates'][0][1] + self._DesignParameter['InputVia_A']['_DesignObj']._DesignParameter['_COLayer']['_XYCoordinates'][1][1])) / 2)]]
        self._DesignParameter['POLY_boundary_27'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _XWidth=(((self._DesignParameter['InputVia_A']['_XYCoordinates'][0][0] + self._DesignParameter['InputVia_A']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['InputVia_A']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)) - ((self._DesignParameter['CascodeNMOS']['_XYCoordinates'][0][0] + self._DesignParameter['CascodeNMOS']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][1][0]) - (self._DesignParameter['CascodeNMOS']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2))), _YWidth=((self._DesignParameter['InputVia_A']['_XYCoordinates'][0][1] + self._DesignParameter['InputVia_A']['_DesignObj']._DesignParameter['_COLayer']['_XYCoordinates'][0][1]) - ((self._DesignParameter['InputVia_A']['_XYCoordinates'][0][1] + self._DesignParameter['InputVia_A']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1]) - (self._DesignParameter['InputVia_A']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2))))
        self._DesignParameter['POLY_boundary_27']['_XYCoordinates'] = [[((((self._DesignParameter['InputVia_A']['_XYCoordinates'][0][0] + self._DesignParameter['InputVia_A']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['InputVia_A']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)) + ((self._DesignParameter['CascodeNMOS']['_XYCoordinates'][0][0] + self._DesignParameter['CascodeNMOS']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][1][0]) - (self._DesignParameter['CascodeNMOS']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2))) / 2), (((self._DesignParameter['InputVia_A']['_XYCoordinates'][0][1] + self._DesignParameter['InputVia_A']['_DesignObj']._DesignParameter['_COLayer']['_XYCoordinates'][0][1]) + ((self._DesignParameter['InputVia_A']['_XYCoordinates'][0][1] + self._DesignParameter['InputVia_A']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1]) - (self._DesignParameter['InputVia_A']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2))) / 2)]]



    def _CalculateDesignParameterFinger2(self,NMOSWidth=200,PMOSWidth=400,ChannelLength=30,XVT='SLVT',GateSpacing=100,CellHeight=1800,VDD2PMOS=410,VSS2NMOS=310):

        drc = DRC.DRC()
        _Name = self._DesignParameter['_Name']['_Name']

        self._DesignParameter['VSSRail'] = self._SrefElementDeclaration(_DesignObj=SupplyRails.SupplyRail(_Name='VSSRailIn{}'.format(_Name)))[0]
        self._DesignParameter['VSSRail']['_DesignObj']._CalculateDesignParameter(**dict(NumPitch=5, UnitPitch=(GateSpacing + ChannelLength), Met1YWidth=80, Met2YWidth=300, PpNpYWidth=180, isPbody=True))
        self._DesignParameter['VSSRail']['_XYCoordinates'] = [[0.0, 0.0]]
        self._DesignParameter['VDDRail'] = self._SrefElementDeclaration(_DesignObj=SupplyRails.SupplyRail(_Name='VDDRailIn{}'.format(_Name)))[0]
        self._DesignParameter['VDDRail']['_DesignObj']._CalculateDesignParameter(**dict(NumPitch=5, UnitPitch=(GateSpacing + ChannelLength), Met1YWidth=80, Met2YWidth=300, PpNpYWidth=180, isPbody=False))
        self._DesignParameter['VDDRail']['_XYCoordinates'] = [[0, CellHeight]]
        self._DesignParameter['NMOS'] = self._SrefElementDeclaration(_DesignObj=NMOSWithDummy._NMOS(_Name='NMOSIn{}'.format(_Name)))[0]
        self._DesignParameter['NMOS']['_DesignObj']._CalculateNMOSDesignParameter(**dict(_NMOSNumberofGate=4, _NMOSChannelWidth=NMOSWidth, _NMOSChannellength=ChannelLength, _NMOSDummy=True, _GateSpacing=GateSpacing, _SDWidth=None, _XVT=XVT))
        self._DesignParameter['NMOS']['_XYCoordinates'] = [[0, VSS2NMOS]]
        self._DesignParameter['PMOS'] = self._SrefElementDeclaration(_DesignObj=PMOSWithDummy._PMOS(_Name='PMOSIn{}'.format(_Name)))[0]
        self._DesignParameter['PMOS']['_DesignObj']._CalculatePMOSDesignParameter(**dict(_PMOSNumberofGate=4, _PMOSChannelWidth=PMOSWidth, _PMOSChannellength=ChannelLength, _PMOSDummy=True, _GateSpacing=GateSpacing, _SDWidth=None, _XVT=XVT))
        self._DesignParameter['PMOS']['_XYCoordinates'] = [[0, (CellHeight - VDD2PMOS)]]
        self._DesignParameter['polygate1'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _XWidth=ChannelLength, _YWidth=(((self._DesignParameter['PMOS']['_XYCoordinates'][0][1] + self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1]) - (self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2)) - ((self._DesignParameter['NMOS']['_XYCoordinates'][0][1] + self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1]) + (self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2))))
        self._DesignParameter['polygate1']['_XYCoordinates'] = [[(self._DesignParameter['NMOS']['_XYCoordinates'][0][0] + self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]), ((((self._DesignParameter['PMOS']['_XYCoordinates'][0][1] + self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1]) - (self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2)) + ((self._DesignParameter['NMOS']['_XYCoordinates'][0][1] + self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1]) + (self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2))) / 2)]]
        self._DesignParameter['polygate2'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _XWidth=ChannelLength, _YWidth=(((self._DesignParameter['PMOS']['_XYCoordinates'][0][1] + self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][1]) - (self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2)) - ((self._DesignParameter['NMOS']['_XYCoordinates'][0][1] + self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][1]) + (self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2))))
        self._DesignParameter['polygate2']['_XYCoordinates'] = [[(self._DesignParameter['NMOS']['_XYCoordinates'][0][0] + self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]), ((((self._DesignParameter['PMOS']['_XYCoordinates'][0][1] + self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][1]) - (self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2)) + ((self._DesignParameter['NMOS']['_XYCoordinates'][0][1] + self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][1]) + (self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2))) / 2)]]
        self._DesignParameter['InputVia_A'] = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1_resize._ViaPoly2Met1_resize(_Name='InputVia_AIn{}'.format(_Name)))[0]
        self._DesignParameter['InputVia_A']['_DesignObj']._CalculateDesignParameter(**dict(_ViaPoly2Met1NumberOfCOX=1, _ViaPoly2Met1NumberOfCOY=2, Met1XWidth=66, Met1YWidth=200, POXWidth=40, POYWidth=200))
        self._DesignParameter['InputVia_A']['_XYCoordinates'] = [[(self._DesignParameter['NMOS']['_XYCoordinates'][0][0] + self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]), self._DesignParameter['polygate1']['_XYCoordinates'][0][1]]]
        self._DesignParameter['polygate3'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _XWidth=((self._DesignParameter['polygate2']['_XYCoordinates'][0][0] - (self._DesignParameter['polygate2']['_XWidth'] / 2)) - (self._DesignParameter['polygate1']['_XYCoordinates'][0][0] + (self._DesignParameter['polygate1']['_XWidth'] / 2))), _YWidth=50.0)
        self._DesignParameter['polygate3']['_XYCoordinates'] = [[(((self._DesignParameter['polygate1']['_XYCoordinates'][0][0] + (self._DesignParameter['polygate1']['_XWidth'] / 2)) + (self._DesignParameter['polygate2']['_XYCoordinates'][0][0] - (self._DesignParameter['polygate2']['_XWidth'] / 2))) / 2), self._DesignParameter['InputVia_A']['_XYCoordinates'][0][1]]]
        self._DesignParameter['VSSRouting1'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _XWidth=self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'], _YWidth=(((self._DesignParameter['NMOS']['_XYCoordinates'][0][1] + self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) + (self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)) - ((self._DesignParameter['VSSRail']['_XYCoordinates'][0][1] + self._DesignParameter['VSSRail']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) - (self._DesignParameter['VSSRail']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2))))
        self._DesignParameter['VSSRouting1']['_XYCoordinates'] = [[(self._DesignParameter['NMOS']['_XYCoordinates'][0][0] + self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0]), ((((self._DesignParameter['NMOS']['_XYCoordinates'][0][1] + self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) + (self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)) + ((self._DesignParameter['VSSRail']['_XYCoordinates'][0][1] + self._DesignParameter['VSSRail']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) - (self._DesignParameter['VSSRail']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2))) / 2)]]
        self._DesignParameter['VSSRouting2'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _XWidth=self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'], _YWidth=(((self._DesignParameter['NMOS']['_XYCoordinates'][0][1] + self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][(- 1)][1]) + (self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)) - ((self._DesignParameter['VSSRail']['_XYCoordinates'][0][1] + self._DesignParameter['VSSRail']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][(- 1)][1]) - (self._DesignParameter['VSSRail']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2))))
        self._DesignParameter['VSSRouting2']['_XYCoordinates'] = [[(self._DesignParameter['NMOS']['_XYCoordinates'][0][0] + self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][(- 1)][0]), ((((self._DesignParameter['NMOS']['_XYCoordinates'][0][1] + self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][(- 1)][1]) + (self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)) + ((self._DesignParameter['VSSRail']['_XYCoordinates'][0][1] + self._DesignParameter['VSSRail']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][(- 1)][1]) - (self._DesignParameter['VSSRail']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2))) / 2)]]
        self._DesignParameter['VDDRouting1'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _XWidth=self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'], _YWidth=(((self._DesignParameter['VDDRail']['_XYCoordinates'][0][1] + self._DesignParameter['VDDRail']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) + (self._DesignParameter['VDDRail']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)) - ((self._DesignParameter['PMOS']['_XYCoordinates'][0][1] + self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) - (self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2))))
        self._DesignParameter['VDDRouting1']['_XYCoordinates'] = [[(self._DesignParameter['PMOS']['_XYCoordinates'][0][0] + self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0]), ((((self._DesignParameter['VDDRail']['_XYCoordinates'][0][1] + self._DesignParameter['VDDRail']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) + (self._DesignParameter['VDDRail']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)) + ((self._DesignParameter['PMOS']['_XYCoordinates'][0][1] + self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) - (self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2))) / 2)]]
        self._DesignParameter['VDDRouting2'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _XWidth=self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'], _YWidth=(((self._DesignParameter['VDDRail']['_XYCoordinates'][0][1] + self._DesignParameter['VDDRail']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][(- 1)][1]) + (self._DesignParameter['VDDRail']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)) - ((self._DesignParameter['PMOS']['_XYCoordinates'][0][1] + self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][(- 1)][1]) - (self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2))))
        self._DesignParameter['VDDRouting2']['_XYCoordinates'] = [[(self._DesignParameter['PMOS']['_XYCoordinates'][0][0] + self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][(- 1)][0]), ((((self._DesignParameter['VDDRail']['_XYCoordinates'][0][1] + self._DesignParameter['VDDRail']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) + (self._DesignParameter['VDDRail']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)) + ((self._DesignParameter['PMOS']['_XYCoordinates'][0][1] + self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) - (self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2))) / 2)]]
        self._DesignParameter['NWELL_boundary_1'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['NWELL'][0], _Datatype=DesignParameters._LayerMapping['NWELL'][1], _XWidth=max((self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth'] + (2 * drc._NwMinEnclosurePactive2)), (self._DesignParameter['VDDRail']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth'] + (2 * drc._NwMinEnclosurePactive))), _YWidth=((((self._DesignParameter['VDDRail']['_XYCoordinates'][0][1] + self._DesignParameter['VDDRail']['_DesignObj']._DesignParameter['_ODLayer']['_XYCoordinates'][0][1]) + (self._DesignParameter['VDDRail']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth'] / 2)) - ((self._DesignParameter['PMOS']['_XYCoordinates'][0][1] + self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_ODLayer']['_XYCoordinates'][0][1]) - (self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth'] / 2))) + (2 * drc._NwMinEnclosurePactive)))
        self._DesignParameter['NWELL_boundary_1']['_XYCoordinates'] = [[0, ((((self._DesignParameter['VDDRail']['_XYCoordinates'][0][1] + self._DesignParameter['VDDRail']['_DesignObj']._DesignParameter['_ODLayer']['_XYCoordinates'][0][1]) + (self._DesignParameter['VDDRail']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth'] / 2)) + ((self._DesignParameter['PMOS']['_XYCoordinates'][0][1] + self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_ODLayer']['_XYCoordinates'][0][1]) - (self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth'] / 2))) / 2)]]
        self._DesignParameter['met1_pmos_1'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _XWidth=(((self._DesignParameter['PMOS']['_XYCoordinates'][0][0] + self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][3][0]) + (self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] / 2)) - ((self._DesignParameter['PMOS']['_XYCoordinates'][0][0] + self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][1][0]) - (self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] / 2))), _YWidth=drc._Metal1MinWidth)
        self._DesignParameter['met1_pmos_1']['_XYCoordinates'] = [[0, ((((self._DesignParameter['PMOS']['_XYCoordinates'][0][1] + self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) + (self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)) + drc._Metal1MinSpaceAtCorner) + (drc._Metal1MinWidth / 2))]]
        self._DesignParameter['met1_boundary_2'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _XWidth=self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'], _YWidth=((self._DesignParameter['met1_pmos_1']['_XYCoordinates'][0][1] + (self._DesignParameter['met1_pmos_1']['_YWidth'] / 2)) - ((self._DesignParameter['PMOS']['_XYCoordinates'][0][1] + self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) + (self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2))))
        self._DesignParameter['met1_boundary_2']['_XYCoordinates'] = [[(self._DesignParameter['PMOS']['_XYCoordinates'][0][0] + self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][1][0]), ((((self._DesignParameter['PMOS']['_XYCoordinates'][0][1] + self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][1][1]) + (self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)) + (self._DesignParameter['met1_pmos_1']['_XYCoordinates'][0][1] + (self._DesignParameter['met1_pmos_1']['_YWidth'] / 2))) / 2)]]
        self._DesignParameter['met1_pmos_2'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _XWidth=self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'], _YWidth=((self._DesignParameter['met1_pmos_1']['_XYCoordinates'][0][1] + (self._DesignParameter['met1_pmos_1']['_YWidth'] / 2)) - ((self._DesignParameter['PMOS']['_XYCoordinates'][0][1] + self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) + (self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2))))
        self._DesignParameter['met1_pmos_2']['_XYCoordinates'] = [[(self._DesignParameter['PMOS']['_XYCoordinates'][0][0] + self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][3][0]), ((((self._DesignParameter['PMOS']['_XYCoordinates'][0][1] + self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][1][1]) + (self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)) + (self._DesignParameter['met1_pmos_1']['_XYCoordinates'][0][1] + (self._DesignParameter['met1_pmos_1']['_YWidth'] / 2))) / 2)]]
        self._DesignParameter['met1_nmos_1'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _XWidth=(((self._DesignParameter['NMOS']['_XYCoordinates'][0][0] + self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][3][0]) + (self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] / 2)) - ((self._DesignParameter['NMOS']['_XYCoordinates'][0][0] + self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][1][0]) - (self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] / 2))), _YWidth=drc._Metal1MinWidth)
        self._DesignParameter['met1_nmos_1']['_XYCoordinates'] = [[0, ((((self._DesignParameter['NMOS']['_XYCoordinates'][0][1] + self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) - (self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)) - drc._Metal1MinSpaceAtCorner) - (drc._Metal1MinWidth / 2))]]
        self._DesignParameter['met1_nmos_2'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _XWidth=self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'], _YWidth=(((self._DesignParameter['NMOS']['_XYCoordinates'][0][1] + self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) - (self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)) - (self._DesignParameter['met1_nmos_1']['_XYCoordinates'][0][1] - (self._DesignParameter['met1_nmos_1']['_YWidth'] / 2))))
        self._DesignParameter['met1_nmos_2']['_XYCoordinates'] = [[(self._DesignParameter['NMOS']['_XYCoordinates'][0][0] + self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][1][0]), ((((self._DesignParameter['NMOS']['_XYCoordinates'][0][1] + self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) - (self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)) + (self._DesignParameter['met1_nmos_1']['_XYCoordinates'][0][1] - (self._DesignParameter['met1_nmos_1']['_YWidth'] / 2))) / 2)]]
        self._DesignParameter['met1_nmos3'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _XWidth=self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'], _YWidth=(((self._DesignParameter['NMOS']['_XYCoordinates'][0][1] + self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) - (self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)) - (self._DesignParameter['met1_nmos_1']['_XYCoordinates'][0][1] - (self._DesignParameter['met1_nmos_1']['_YWidth'] / 2))))
        self._DesignParameter['met1_nmos3']['_XYCoordinates'] = [[(self._DesignParameter['NMOS']['_XYCoordinates'][0][0] + self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][3][0]), ((((self._DesignParameter['NMOS']['_XYCoordinates'][0][1] + self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) - (self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)) + (self._DesignParameter['met1_nmos_1']['_XYCoordinates'][0][1] - (self._DesignParameter['met1_nmos_1']['_YWidth'] / 2))) / 2)]]
        self._DesignParameter['met1_output_1'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _XWidth=(((self._DesignParameter['NMOS']['_XYCoordinates'][0][0] + self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][(- 1)][0]) + (self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] / 2)) - ((self._DesignParameter['NMOS']['_XYCoordinates'][0][0] + self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][2][0]) - (self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] / 2))), _YWidth=drc._Metal1MinWidth)
        self._DesignParameter['met1_output_1']['_XYCoordinates'] = [[((((self._DesignParameter['NMOS']['_XYCoordinates'][0][0] + self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][(- 1)][0]) + (self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] / 2)) + ((self._DesignParameter['NMOS']['_XYCoordinates'][0][0] + self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][2][0]) - (self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] / 2))) / 2), ((((self._DesignParameter['NMOS']['_XYCoordinates'][0][1] + self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) + (self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)) + drc._Metal1MinSpaceAtCorner) + (drc._Metal1MinWidth / 2))]]
        self._DesignParameter['met1_output_2'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _XWidth=self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'], _YWidth=((self._DesignParameter['met1_output_1']['_XYCoordinates'][0][1] + (self._DesignParameter['met1_output_1']['_YWidth'] / 2)) - ((self._DesignParameter['NMOS']['_XYCoordinates'][0][1] + self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][2][1]) + (self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2))))
        self._DesignParameter['met1_output_2']['_XYCoordinates'] = [[(self._DesignParameter['NMOS']['_XYCoordinates'][0][0] + self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][2][0]), (((self._DesignParameter['met1_output_1']['_XYCoordinates'][0][1] + (self._DesignParameter['met1_output_1']['_YWidth'] / 2)) + ((self._DesignParameter['NMOS']['_XYCoordinates'][0][1] + self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) + (self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2))) / 2)]]
        self._DesignParameter['InputVia_EN'] = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_Name='InputVia_ENIn{}'.format(_Name)))[0]
        self._DesignParameter['InputVia_EN']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(**dict(_ViaPoly2Met1NumberOfCOX=2, _ViaPoly2Met1NumberOfCOY=1))
        self._DesignParameter['InputVia_EN']['_XYCoordinates'] = [[self._DesignParameter['NMOS']['_XYCoordinates'][0][0], (((self._DesignParameter['met1_output_1']['_XYCoordinates'][0][1] + (self._DesignParameter['met1_output_1']['_YWidth'] / 2)) + drc._Metal1MinSpaceAtCorner) + ((drc._CoMinWidth / 2) + drc._Metal1MinEnclosureCO2))]]
        self._DesignParameter['polygate_en_1'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _XWidth=ChannelLength, _YWidth=(((self._DesignParameter['InputVia_EN']['_XYCoordinates'][0][1] + self._DesignParameter['InputVia_EN']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1]) - (self._DesignParameter['InputVia_EN']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2)) - ((self._DesignParameter['NMOS']['_XYCoordinates'][0][1] + self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1]) + (self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2))))
        self._DesignParameter['polygate_en_1']['_XYCoordinates'] = [[(self._DesignParameter['NMOS']['_XYCoordinates'][0][0] + self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][1][0]), ((((self._DesignParameter['NMOS']['_XYCoordinates'][0][1] + self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1]) + (self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2)) + ((self._DesignParameter['InputVia_EN']['_XYCoordinates'][0][1] + self._DesignParameter['InputVia_EN']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1]) - (self._DesignParameter['InputVia_EN']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2))) / 2)]]
        self._DesignParameter['polygate_en_2'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _XWidth=ChannelLength, _YWidth=(((self._DesignParameter['InputVia_EN']['_XYCoordinates'][0][1] + self._DesignParameter['InputVia_EN']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1]) - (self._DesignParameter['InputVia_EN']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2)) - ((self._DesignParameter['NMOS']['_XYCoordinates'][0][1] + self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1]) + (self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2))))
        self._DesignParameter['polygate_en_2']['_XYCoordinates'] = [[(self._DesignParameter['NMOS']['_XYCoordinates'][0][0] + self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][2][0]), ((((self._DesignParameter['NMOS']['_XYCoordinates'][0][1] + self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1]) + (self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2)) + ((self._DesignParameter['InputVia_EN']['_XYCoordinates'][0][1] + self._DesignParameter['InputVia_EN']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1]) - (self._DesignParameter['InputVia_EN']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2))) / 2)]]
        self._DesignParameter['met1_output_3'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _XWidth=(((self._DesignParameter['PMOS']['_XYCoordinates'][0][0] + self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][(- 1)][0]) + (self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] / 2)) - ((self._DesignParameter['PMOS']['_XYCoordinates'][0][0] + self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][2][0]) - (self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] / 2))), _YWidth=drc._Metal1MinWidth)
        self._DesignParameter['met1_output_3']['_XYCoordinates'] = [[((((self._DesignParameter['PMOS']['_XYCoordinates'][0][0] + self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][(- 1)][0]) + (self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] / 2)) + ((self._DesignParameter['PMOS']['_XYCoordinates'][0][0] + self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][2][0]) - (self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] / 2))) / 2), ((((self._DesignParameter['PMOS']['_XYCoordinates'][0][1] + self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][2][1]) - (self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)) - drc._Metal1MinSpaceAtCorner) - (drc._Metal1MinWidth / 2))]]
        self._DesignParameter['met1_output_4'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _XWidth=self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'], _YWidth=(((self._DesignParameter['PMOS']['_XYCoordinates'][0][1] + self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][2][1]) - (self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)) - (self._DesignParameter['met1_output_3']['_XYCoordinates'][0][1] - (self._DesignParameter['met1_output_3']['_YWidth'] / 2))))
        self._DesignParameter['met1_output_4']['_XYCoordinates'] = [[(self._DesignParameter['PMOS']['_XYCoordinates'][0][0] + self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][2][0]), (((self._DesignParameter['met1_output_3']['_XYCoordinates'][0][1] - (self._DesignParameter['met1_output_3']['_YWidth'] / 2)) + ((self._DesignParameter['PMOS']['_XYCoordinates'][0][1] + self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) - (self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2))) / 2)]]
        self._DesignParameter['InputVia_ENb'] = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_Name='InputVia_ENbIn{}'.format(_Name)))[0]
        self._DesignParameter['InputVia_ENb']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(**dict(_ViaPoly2Met1NumberOfCOX=2, _ViaPoly2Met1NumberOfCOY=1))
        self._DesignParameter['InputVia_ENb']['_XYCoordinates'] = [[self._DesignParameter['PMOS']['_XYCoordinates'][0][0], (((self._DesignParameter['met1_output_3']['_XYCoordinates'][0][1] - (self._DesignParameter['met1_output_3']['_YWidth'] / 2)) - drc._Metal1MinSpaceAtCorner) - ((drc._CoMinWidth / 2) + drc._Metal1MinEnclosureCO2))]]
        self._DesignParameter['polygate_enb_1'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _XWidth=ChannelLength, _YWidth=(((self._DesignParameter['PMOS']['_XYCoordinates'][0][1] + self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1]) - (self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2)) - ((self._DesignParameter['InputVia_ENb']['_XYCoordinates'][0][1] + self._DesignParameter['InputVia_ENb']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1]) + (self._DesignParameter['InputVia_ENb']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2))))
        self._DesignParameter['polygate_enb_1']['_XYCoordinates'] = [[(self._DesignParameter['PMOS']['_XYCoordinates'][0][0] + self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][1][0]), ((((self._DesignParameter['PMOS']['_XYCoordinates'][0][1] + self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1]) - (self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2)) + ((self._DesignParameter['InputVia_ENb']['_XYCoordinates'][0][1] + self._DesignParameter['InputVia_ENb']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1]) + (self._DesignParameter['InputVia_ENb']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2))) / 2)]]
        self._DesignParameter['polygate_enb_2'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _XWidth=ChannelLength, _YWidth=(((self._DesignParameter['PMOS']['_XYCoordinates'][0][1] + self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1]) - (self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2)) - ((self._DesignParameter['InputVia_ENb']['_XYCoordinates'][0][1] + self._DesignParameter['InputVia_ENb']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1]) + (self._DesignParameter['InputVia_ENb']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2))))
        self._DesignParameter['polygate_enb_2']['_XYCoordinates'] = [[(self._DesignParameter['PMOS']['_XYCoordinates'][0][0] + self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][2][0]), ((((self._DesignParameter['PMOS']['_XYCoordinates'][0][1] + self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1]) - (self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2)) + ((self._DesignParameter['InputVia_ENb']['_XYCoordinates'][0][1] + self._DesignParameter['InputVia_ENb']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1]) + (self._DesignParameter['InputVia_ENb']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2))) / 2)]]
        self._DesignParameter['met1_output_5'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _XWidth=self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'], _YWidth=((self._DesignParameter['met1_output_3']['_XYCoordinates'][0][1] + (self._DesignParameter['met1_output_3']['_YWidth'] / 2)) - (self._DesignParameter['met1_output_1']['_XYCoordinates'][0][1] - (self._DesignParameter['met1_output_1']['_YWidth'] / 2))))
        self._DesignParameter['met1_output_5']['_XYCoordinates'] = [[(self._DesignParameter['NMOS']['_XYCoordinates'][0][0] + self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][(- 1)][0]), (((self._DesignParameter['met1_output_3']['_XYCoordinates'][0][1] + (self._DesignParameter['met1_output_3']['_YWidth'] / 2)) + (self._DesignParameter['met1_output_1']['_XYCoordinates'][0][1] - (self._DesignParameter['met1_output_1']['_YWidth'] / 2))) / 2)]]





    def _CalculateDesignParameterFinger3orMore(self, Width_NM1=300, Width_NM2=350, Width_PM1=600, Width_PM2=700, Length=30,
                                  GateSpacing=100, XVT='SLVT', NumFinger_NM1=5, NumFinger_NM2=7,
                                  Dummy=True, NumViaY_InputA=1, NumViaY_InputEN=1, CellHeight=1800,
                                  YCoord_InputA=700, YCoord_InputEN=550, YCoord_InputENb=900):

        drc = DRC.DRC()
        _Name = self._DesignParameter['_Name']['_Name']

        NumFinger_PM1 = NumFinger_NM1
        NumFinger_PM2 = NumFinger_NM2


        NumPitch_NM = ((NumFinger_NM1 + NumFinger_NM2) + 2)
        NumPitch_PM = ((NumFinger_PM1 + NumFinger_PM2) + 2)
        self._DesignParameter['VSSRail'] = \
        self._SrefElementDeclaration(_DesignObj=SupplyRails.SupplyRail(_Name='VSSRailIn{}'.format(_Name)))[0]
        self._DesignParameter['VSSRail']['_DesignObj']._CalculateDesignParameter(
            **dict(NumPitch=max(NumPitch_NM, NumPitch_PM), UnitPitch=(GateSpacing + Length), Met1YWidth=80,
                   Met2YWidth=300, PpNpYWidth=180, isPbody=True))
        self._DesignParameter['VSSRail']['_XYCoordinates'] = [[0.0, 0.0]]
        self._DesignParameter['VDDRail'] = \
        self._SrefElementDeclaration(_DesignObj=SupplyRails.SupplyRail(_Name='VDDRailIn{}'.format(_Name)))[0]
        self._DesignParameter['VDDRail']['_DesignObj']._CalculateDesignParameter(
            **dict(NumPitch=max(NumPitch_NM, NumPitch_PM), UnitPitch=130, Met1YWidth=80, Met2YWidth=300, PpNpYWidth=180,
                   isPbody=False))
        self._DesignParameter['VDDRail']['_XYCoordinates'] = [[0, CellHeight]]
        self._DesignParameter['NM1'] = \
        self._SrefElementDeclaration(_DesignObj=NMOSWithDummy._NMOS(_Name='NM1In{}'.format(_Name)))[0]
        self._DesignParameter['NM1']['_DesignObj']._CalculateNMOSDesignParameter(
            **dict(_NMOSNumberofGate=NumFinger_NM1, _NMOSChannelWidth=Width_NM1, _NMOSChannellength=Length,
                   _NMOSDummy=Dummy, _GateSpacing=GateSpacing, _SDWidth=66, _XVT=XVT))
        self._DesignParameter['NM1']['_XYCoordinates'] = [[(((- (NumFinger_NM2 + 1)) * (GateSpacing + Length)) / 2), (((
                                                                                                                                   (
                                                                                                                                               self._DesignParameter[
                                                                                                                                                   'VSSRail'][
                                                                                                                                                   '_XYCoordinates'][
                                                                                                                                                   0][
                                                                                                                                                   1] +
                                                                                                                                               self._DesignParameter[
                                                                                                                                                   'VSSRail'][
                                                                                                                                                   '_DesignObj']._DesignParameter[
                                                                                                                                                   '_PPLayer'][
                                                                                                                                                   '_XYCoordinates'][
                                                                                                                                                   0][
                                                                                                                                                   1]) + (
                                                                                                                                               self._DesignParameter[
                                                                                                                                                   'VSSRail'][
                                                                                                                                                   '_DesignObj']._DesignParameter[
                                                                                                                                                   '_PPLayer'][
                                                                                                                                                   '_YWidth'] / 2)) + (
                                                                                                                                   self._DesignParameter[
                                                                                                                                       'NM1'][
                                                                                                                                       '_DesignObj']._DesignParameter[
                                                                                                                                       '_ODLayer'][
                                                                                                                                       '_YWidth'] / 2)) + drc._OdMinSpace2Pp)]]
        self._DesignParameter['NM2'] = \
        self._SrefElementDeclaration(_DesignObj=NMOSWithDummy._NMOS(_Name='NM2In{}'.format(_Name)))[0]
        self._DesignParameter['NM2']['_DesignObj']._CalculateNMOSDesignParameter(
            **dict(_NMOSNumberofGate=NumFinger_NM2, _NMOSChannelWidth=Width_NM2, _NMOSChannellength=Length,
                   _NMOSDummy=Dummy, _GateSpacing=GateSpacing, _SDWidth=66, _XVT=XVT))
        self._DesignParameter['NM2']['_XYCoordinates'] = [[(((NumFinger_NM1 + 1) * (GateSpacing + Length)) / 2), ((((
                                                                                                                                self._DesignParameter[
                                                                                                                                    'VSSRail'][
                                                                                                                                    '_XYCoordinates'][
                                                                                                                                    0][
                                                                                                                                    1] +
                                                                                                                                self._DesignParameter[
                                                                                                                                    'VSSRail'][
                                                                                                                                    '_DesignObj']._DesignParameter[
                                                                                                                                    '_PPLayer'][
                                                                                                                                    '_XYCoordinates'][
                                                                                                                                    0][
                                                                                                                                    1]) + (
                                                                                                                                self._DesignParameter[
                                                                                                                                    'VSSRail'][
                                                                                                                                    '_DesignObj']._DesignParameter[
                                                                                                                                    '_PPLayer'][
                                                                                                                                    '_YWidth'] / 2)) + (
                                                                                                                               self._DesignParameter[
                                                                                                                                   'NM2'][
                                                                                                                                   '_DesignObj']._DesignParameter[
                                                                                                                                   '_ODLayer'][
                                                                                                                                   '_YWidth'] / 2)) + drc._OdMinSpace2Pp)]]
        self._DesignParameter['PM1'] = \
        self._SrefElementDeclaration(_DesignObj=PMOSWithDummy._PMOS(_Name='PM1In{}'.format(_Name)))[0]
        self._DesignParameter['PM1']['_DesignObj']._CalculatePMOSDesignParameter(
            **dict(_PMOSNumberofGate=NumFinger_PM1, _PMOSChannelWidth=Width_PM1, _PMOSChannellength=Length,
                   _PMOSDummy=Dummy, _GateSpacing=GateSpacing, _SDWidth=66, _XVT=XVT))
        self._DesignParameter['PM1']['_XYCoordinates'] = [[(((- (NumFinger_PM2 + 1)) * (GateSpacing + Length)) / 2), (((
                                                                                                                                   (
                                                                                                                                               self._DesignParameter[
                                                                                                                                                   'VDDRail'][
                                                                                                                                                   '_XYCoordinates'][
                                                                                                                                                   0][
                                                                                                                                                   1] +
                                                                                                                                               self._DesignParameter[
                                                                                                                                                   'VDDRail'][
                                                                                                                                                   '_DesignObj']._DesignParameter[
                                                                                                                                                   '_ODLayer'][
                                                                                                                                                   '_XYCoordinates'][
                                                                                                                                                   0][
                                                                                                                                                   1]) - (
                                                                                                                                               self._DesignParameter[
                                                                                                                                                   'VDDRail'][
                                                                                                                                                   '_DesignObj']._DesignParameter[
                                                                                                                                                   '_ODLayer'][
                                                                                                                                                   '_YWidth'] / 2)) - drc._OdMinSpace2Pp) - (
                                                                                                                                  self._DesignParameter[
                                                                                                                                      'PM1'][
                                                                                                                                      '_DesignObj']._DesignParameter[
                                                                                                                                      '_PPLayer'][
                                                                                                                                      '_YWidth'] / 2))]]
        self._DesignParameter['PM2'] = \
        self._SrefElementDeclaration(_DesignObj=PMOSWithDummy._PMOS(_Name='PM2In{}'.format(_Name)))[0]
        self._DesignParameter['PM2']['_DesignObj']._CalculatePMOSDesignParameter(
            **dict(_PMOSNumberofGate=NumFinger_PM2, _PMOSChannelWidth=Width_PM2, _PMOSChannellength=Length,
                   _PMOSDummy=Dummy, _GateSpacing=GateSpacing, _SDWidth=66, _XVT=XVT))
        self._DesignParameter['PM2']['_XYCoordinates'] = [[(((NumFinger_PM1 + 1) * (GateSpacing + Length)) / 2), ((((
                                                                                                                                self._DesignParameter[
                                                                                                                                    'VDDRail'][
                                                                                                                                    '_XYCoordinates'][
                                                                                                                                    0][
                                                                                                                                    1] +
                                                                                                                                self._DesignParameter[
                                                                                                                                    'VDDRail'][
                                                                                                                                    '_DesignObj']._DesignParameter[
                                                                                                                                    '_ODLayer'][
                                                                                                                                    '_XYCoordinates'][
                                                                                                                                    0][
                                                                                                                                    1]) - (
                                                                                                                                self._DesignParameter[
                                                                                                                                    'VDDRail'][
                                                                                                                                    '_DesignObj']._DesignParameter[
                                                                                                                                    '_ODLayer'][
                                                                                                                                    '_YWidth'] / 2)) - drc._OdMinSpace2Pp) - (
                                                                                                                              self._DesignParameter[
                                                                                                                                  'PM2'][
                                                                                                                                  '_DesignObj']._DesignParameter[
                                                                                                                                  '_PPLayer'][
                                                                                                                                  '_YWidth'] / 2))]]
        path_list = []
        if (len(self._DesignParameter['NM1']['_DesignObj']._DesignParameter['_METAL1PINDrawing'][
                    '_XYCoordinates']) == 1):
            mode = 'vertical'
            _width = self._DesignParameter['NM1']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
        elif (self._DesignParameter['NM1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][
                  0] ==
              self._DesignParameter['NM1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][
                  0]):
            mode = 'horizontal'
            _width = self._DesignParameter['NM1']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
        elif (self._DesignParameter['NM1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][
                  1] ==
              self._DesignParameter['NM1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][
                  1]):
            mode = 'vertical'
            _width = self._DesignParameter['NM1']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
        else:
            print('Invalid Target Input')
        if (mode == 'vertical'):
            xy_with_offset = []
            target_y_value = ((self._DesignParameter['VSSRail']['_XYCoordinates'][0][1] +
                               self._DesignParameter['VSSRail']['_DesignObj']._DesignParameter['_Met1Layer'][
                                   '_XYCoordinates'][0][1]) - (
                                          self._DesignParameter['VSSRail']['_DesignObj']._DesignParameter['_Met1Layer'][
                                              '_YWidth'] / 2))
            for i in range(len(self._DesignParameter['NM1']['_DesignObj']._DesignParameter['_METAL1PINDrawing'][
                                   '_XYCoordinates'])):
                if ((i % 2) == 0):
                    xy_with_offset.append([(x + y) for (x, y) in
                                           zip([(0 + self._DesignParameter['NM1']['_XYCoordinates'][0][0]),
                                                (0 + self._DesignParameter['NM1']['_XYCoordinates'][0][1])],
                                               self._DesignParameter['NM1']['_DesignObj']._DesignParameter[
                                                   '_METAL1PINDrawing']['_XYCoordinates'][i])])
            for i in range(len(xy_with_offset)):
                path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
        elif (mode == 'horizontal'):
            xy_with_offset = []
            target_x_value = (self._DesignParameter['VSSRail']['_XYCoordinates'][0][0] +
                              self._DesignParameter['VSSRail']['_DesignObj']._DesignParameter['_Met1Layer'][
                                  '_XYCoordinates'][0][0])
            for i in range(len(self._DesignParameter['NM1']['_DesignObj']._DesignParameter['_METAL1PINDrawing'][
                                   '_XYCoordinates'])):
                if ((i % 2) == 0):
                    xy_with_offset.append([(x + y) for (x, y) in
                                           zip([(0 + self._DesignParameter['NM1']['_XYCoordinates'][0][0]),
                                                (0 + self._DesignParameter['NM1']['_XYCoordinates'][0][1])],
                                               self._DesignParameter['NM1']['_DesignObj']._DesignParameter[
                                                   '_METAL1PINDrawing']['_XYCoordinates'][i])])
            for i in range(len(xy_with_offset)):
                path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
        self._DesignParameter['VSSRouting'] = self._PathElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1],
            _Width=_width)
        self._DesignParameter['VSSRouting']['_XYCoordinates'] = path_list
        path_list = []
        if (len(self._DesignParameter['PM1']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates']) == 1):
            mode = 'vertical'
            _width = self._DesignParameter['PM1']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
        elif (self._DesignParameter['PM1']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0] ==
              self._DesignParameter['PM1']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][(- 1)][0]):
            mode = 'horizontal'
            _width = self._DesignParameter['PM1']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
        elif (self._DesignParameter['PM1']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1] ==
              self._DesignParameter['PM1']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][(- 1)][1]):
            mode = 'vertical'
            _width = self._DesignParameter['PM1']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
        else:
            print('Invalid Target Input')
        if (mode == 'vertical'):
            xy_with_offset = []
            target_y_value = ((self._DesignParameter['VDDRail']['_XYCoordinates'][0][1] +
                               self._DesignParameter['VDDRail']['_DesignObj']._DesignParameter['_Met1Layer'][
                                   '_XYCoordinates'][0][1]) + (
                                          self._DesignParameter['VDDRail']['_DesignObj']._DesignParameter['_Met1Layer'][
                                              '_YWidth'] / 2))
            for i in range(
                    len(self._DesignParameter['PM1']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'])):
                if ((i % 2) == 0):
                    xy_with_offset.append([(x + y) for (x, y) in
                                           zip([(0 + self._DesignParameter['PM1']['_XYCoordinates'][0][0]),
                                                (0 + self._DesignParameter['PM1']['_XYCoordinates'][0][1])],
                                               self._DesignParameter['PM1']['_DesignObj']._DesignParameter[
                                                   '_Met1Layer']['_XYCoordinates'][i])])
            for i in range(len(xy_with_offset)):
                path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
        elif (mode == 'horizontal'):
            xy_with_offset = []
            target_x_value = (self._DesignParameter['VDDRail']['_XYCoordinates'][0][0] +
                              self._DesignParameter['VDDRail']['_DesignObj']._DesignParameter['_Met1Layer'][
                                  '_XYCoordinates'][0][0])
            for i in range(
                    len(self._DesignParameter['PM1']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'])):
                if ((i % 2) == 0):
                    xy_with_offset.append([(x + y) for (x, y) in
                                           zip([(0 + self._DesignParameter['PM1']['_XYCoordinates'][0][0]),
                                                (0 + self._DesignParameter['PM1']['_XYCoordinates'][0][1])],
                                               self._DesignParameter['PM1']['_DesignObj']._DesignParameter[
                                                   '_Met1Layer']['_XYCoordinates'][i])])
            for i in range(len(xy_with_offset)):
                path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
        self._DesignParameter['VDDRouting'] = self._PathElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1],
            _Width=_width)
        self._DesignParameter['VDDRouting']['_XYCoordinates'] = path_list
        path_list = []
        if (len(self._DesignParameter['NM2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates']) == 1):
            mode = 'vertical'
            _width = self._DesignParameter['NM2']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
        elif (self._DesignParameter['NM2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0] ==
              self._DesignParameter['NM2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]):
            mode = 'horizontal'
            _width = self._DesignParameter['NM2']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
        elif (self._DesignParameter['NM2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1] ==
              self._DesignParameter['NM2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][1]):
            mode = 'vertical'
            _width = self._DesignParameter['NM2']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
        else:
            print('Invalid Target Input')
        if (mode == 'vertical'):
            xy_with_offset = []
            target_y_value = (self._DesignParameter['PM2']['_XYCoordinates'][0][1] +
                              self._DesignParameter['PM2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][
                                  0][1])
            for i in range(
                    len(self._DesignParameter['NM2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
                xy_with_offset.append([(x + y) for (x, y) in
                                       zip([(0 + self._DesignParameter['NM2']['_XYCoordinates'][0][0]),
                                            (0 + self._DesignParameter['NM2']['_XYCoordinates'][0][1])],
                                           self._DesignParameter['NM2']['_DesignObj']._DesignParameter['_POLayer'][
                                               '_XYCoordinates'][i])])
            for i in range(len(xy_with_offset)):
                path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
        elif (mode == 'horizontal'):
            xy_with_offset = []
            target_x_value = (self._DesignParameter['PM2']['_XYCoordinates'][0][0] +
                              self._DesignParameter['PM2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][
                                  0][0])
            for i in range(
                    len(self._DesignParameter['NM2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
                xy_with_offset.append([(x + y) for (x, y) in
                                       zip([(0 + self._DesignParameter['NM2']['_XYCoordinates'][0][0]),
                                            (0 + self._DesignParameter['NM2']['_XYCoordinates'][0][1])],
                                           self._DesignParameter['NM2']['_DesignObj']._DesignParameter['_POLayer'][
                                               '_XYCoordinates'][i])])
            for i in range(len(xy_with_offset)):
                path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
        self._DesignParameter['tttt'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0],
                                                                     _Datatype=DesignParameters._LayerMapping['POLY'][
                                                                         1], _Width=_width)
        self._DesignParameter['tttt']['_XYCoordinates'] = path_list
        NumViaX_InputA = int((((((((self._DesignParameter['NM2']['_XYCoordinates'][0][0] +
                                    self._DesignParameter['NM2']['_DesignObj']._DesignParameter['_POLayer'][
                                        '_XYCoordinates'][(- 1)][0]) + (
                                               self._DesignParameter['NM2']['_DesignObj']._DesignParameter['_POLayer'][
                                                   '_XWidth'] / 2)) - ((self._DesignParameter['NM2']['_XYCoordinates'][
                                                                            0][0] + self._DesignParameter['NM2'][
                                                                            '_DesignObj']._DesignParameter['_POLayer'][
                                                                            '_XYCoordinates'][0][0]) - (
                                                                                   self._DesignParameter['NM2'][
                                                                                       '_DesignObj']._DesignParameter[
                                                                                       '_POLayer']['_XWidth'] / 2))) - (
                                             2 * drc._CoMinEnclosureByODAtLeastTwoSide)) - drc._CoMinWidth) // (
                                           drc._CoMinWidth + drc._CoMinSpace)) + 1))
        self._DesignParameter['polyInputA'] = \
        self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_Name='polyInputAIn{}'.format(_Name)))[0]
        self._DesignParameter['polyInputA']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(
            **dict(_ViaPoly2Met1NumberOfCOX=NumViaX_InputA, _ViaPoly2Met1NumberOfCOY=NumViaY_InputA))
        self._DesignParameter['polyInputA']['_XYCoordinates'] = [[(self._DesignParameter['NM2']['_XYCoordinates'][0][
                                                                       0] + self._DesignParameter['NM2'][
                                                                       '_DesignObj']._DesignParameter['_SLVTLayer'][
                                                                       '_XYCoordinates'][0][0]), YCoord_InputA]]
        self._DesignParameter['PolyX_M2'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1],
            _XWidth=(((self._DesignParameter['NM2']['_XYCoordinates'][0][0] +
                       self._DesignParameter['NM2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][
                           0]) + (self._DesignParameter['NM2']['_DesignObj']._DesignParameter['_POLayer'][
                                      '_XWidth'] / 2)) - ((self._DesignParameter['NM2']['_XYCoordinates'][0][0] +
                                                           self._DesignParameter['NM2']['_DesignObj']._DesignParameter[
                                                               '_POLayer']['_XYCoordinates'][0][0]) - (
                                                                      self._DesignParameter['NM2'][
                                                                          '_DesignObj']._DesignParameter['_POLayer'][
                                                                          '_XWidth'] / 2))),
            _YWidth=self._DesignParameter['polyInputA']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'])
        self._DesignParameter['PolyX_M2']['_XYCoordinates'] = [
            [(+ self._DesignParameter['polyInputA']['_XYCoordinates'][0][0]),
             (+ self._DesignParameter['polyInputA']['_XYCoordinates'][0][1])]]
        NumViaX_InputEN = int((((((((self._DesignParameter['NM1']['_XYCoordinates'][0][0] +
                                     self._DesignParameter['NM1']['_DesignObj']._DesignParameter['_POLayer'][
                                         '_XYCoordinates'][(- 1)][0]) + (
                                                self._DesignParameter['NM1']['_DesignObj']._DesignParameter['_POLayer'][
                                                    '_XWidth'] / 2)) - ((self._DesignParameter['NM1']['_XYCoordinates'][
                                                                             0][0] + self._DesignParameter['NM1'][
                                                                             '_DesignObj']._DesignParameter['_POLayer'][
                                                                             '_XYCoordinates'][0][0]) - (
                                                                                    self._DesignParameter['NM1'][
                                                                                        '_DesignObj']._DesignParameter[
                                                                                        '_POLayer'][
                                                                                        '_XWidth'] / 2))) - (
                                              2 * drc._CoMinEnclosureByODAtLeastTwoSide)) - drc._CoMinWidth) // (
                                            drc._CoMinWidth + drc._CoMinSpace)) + 1))
        self._DesignParameter['PolyContactEN'] = \
        self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_Name='PolyContactENIn{}'.format(_Name)))[0]
        self._DesignParameter['PolyContactEN']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(
            **dict(_ViaPoly2Met1NumberOfCOX=NumViaX_InputEN, _ViaPoly2Met1NumberOfCOY=NumViaY_InputEN))
        self._DesignParameter['PolyContactEN']['_XYCoordinates'] = [
            [self._DesignParameter['NM1']['_XYCoordinates'][0][0], YCoord_InputEN]]
        self._DesignParameter['PolyContactEN_0'] = \
        self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_Name='PolyContactEN_0In{}'.format(_Name)))[
            0]
        self._DesignParameter['PolyContactEN_0']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(
            **dict(_ViaPoly2Met1NumberOfCOX=NumViaX_InputEN, _ViaPoly2Met1NumberOfCOY=NumViaY_InputEN))
        self._DesignParameter['PolyContactEN_0']['_XYCoordinates'] = [
            [self._DesignParameter['PM1']['_XYCoordinates'][0][0], YCoord_InputENb]]
        self._DesignParameter['polyboundaryEN'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1],
            _XWidth=(((self._DesignParameter['NM1']['_XYCoordinates'][0][0] +
                       self._DesignParameter['NM1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][
                           0]) + (self._DesignParameter['NM1']['_DesignObj']._DesignParameter['_POLayer'][
                                      '_XWidth'] / 2)) - ((self._DesignParameter['NM1']['_XYCoordinates'][0][0] +
                                                           self._DesignParameter['NM1']['_DesignObj']._DesignParameter[
                                                               '_POLayer']['_XYCoordinates'][0][0]) - (
                                                                      self._DesignParameter['NM1'][
                                                                          '_DesignObj']._DesignParameter['_POLayer'][
                                                                          '_XWidth'] / 2))),
            _YWidth=self._DesignParameter['PolyContactEN']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'])
        self._DesignParameter['polyboundaryEN']['_XYCoordinates'] = [
            [(+ self._DesignParameter['PolyContactEN']['_XYCoordinates'][0][0]),
             (+ self._DesignParameter['PolyContactEN']['_XYCoordinates'][0][1])]]
        self._DesignParameter['polyboundaryEN_0'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1],
            _XWidth=(((self._DesignParameter['NM1']['_XYCoordinates'][0][0] +
                       self._DesignParameter['NM1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][
                           0]) + (self._DesignParameter['NM1']['_DesignObj']._DesignParameter['_POLayer'][
                                      '_XWidth'] / 2)) - ((self._DesignParameter['NM1']['_XYCoordinates'][0][0] +
                                                           self._DesignParameter['NM1']['_DesignObj']._DesignParameter[
                                                               '_POLayer']['_XYCoordinates'][0][0]) - (
                                                                      self._DesignParameter['NM1'][
                                                                          '_DesignObj']._DesignParameter['_POLayer'][
                                                                          '_XWidth'] / 2))),
            _YWidth=self._DesignParameter['PolyContactEN_0']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'])
        self._DesignParameter['polyboundaryEN_0']['_XYCoordinates'] = [
            [(+ self._DesignParameter['PolyContactEN_0']['_XYCoordinates'][0][0]),
             (+ self._DesignParameter['PolyContactEN_0']['_XYCoordinates'][0][1])]]
        path_list = []
        if (len(self._DesignParameter['NM1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates']) == 1):
            mode = 'vertical'
            _width = self._DesignParameter['NM1']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
        elif (self._DesignParameter['NM1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0] ==
              self._DesignParameter['NM1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]):
            mode = 'horizontal'
            _width = self._DesignParameter['NM1']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
        elif (self._DesignParameter['NM1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1] ==
              self._DesignParameter['NM1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][1]):
            mode = 'vertical'
            _width = self._DesignParameter['NM1']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
        else:
            print('Invalid Target Input')
        if (mode == 'vertical'):
            xy_with_offset = []
            target_y_value = ((0 + self._DesignParameter['polyboundaryEN']['_XYCoordinates'][0][1]) - (
                        self._DesignParameter['polyboundaryEN']['_YWidth'] / 2))
            for i in range(
                    len(self._DesignParameter['NM1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
                xy_with_offset.append([(x + y) for (x, y) in
                                       zip([(0 + self._DesignParameter['NM1']['_XYCoordinates'][0][0]),
                                            (0 + self._DesignParameter['NM1']['_XYCoordinates'][0][1])],
                                           self._DesignParameter['NM1']['_DesignObj']._DesignParameter['_POLayer'][
                                               '_XYCoordinates'][i])])
            for i in range(len(xy_with_offset)):
                path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
        elif (mode == 'horizontal'):
            xy_with_offset = []
            target_x_value = (0 + self._DesignParameter['polyboundaryEN']['_XYCoordinates'][0][0])
            for i in range(
                    len(self._DesignParameter['NM1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
                xy_with_offset.append([(x + y) for (x, y) in
                                       zip([(0 + self._DesignParameter['NM1']['_XYCoordinates'][0][0]),
                                            (0 + self._DesignParameter['NM1']['_XYCoordinates'][0][1])],
                                           self._DesignParameter['NM1']['_DesignObj']._DesignParameter['_POLayer'][
                                               '_XYCoordinates'][i])])
            for i in range(len(xy_with_offset)):
                path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
        self._DesignParameter['PolyYForEN'] = self._PathElementDeclaration(
            _Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1],
            _Width=_width)
        self._DesignParameter['PolyYForEN']['_XYCoordinates'] = path_list
        path_list = []
        if (len(self._DesignParameter['PM1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates']) == 1):
            mode = 'vertical'
            _width = self._DesignParameter['PM1']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
        elif (self._DesignParameter['PM1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0] ==
              self._DesignParameter['PM1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]):
            mode = 'horizontal'
            _width = self._DesignParameter['PM1']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
        elif (self._DesignParameter['PM1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1] ==
              self._DesignParameter['PM1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][1]):
            mode = 'vertical'
            _width = self._DesignParameter['PM1']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
        else:
            print('Invalid Target Input')
        if (mode == 'vertical'):
            xy_with_offset = []
            target_y_value = ((0 + self._DesignParameter['polyboundaryEN_0']['_XYCoordinates'][0][1]) + (
                        self._DesignParameter['polyboundaryEN_0']['_YWidth'] / 2))
            for i in range(
                    len(self._DesignParameter['PM1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
                xy_with_offset.append([(x + y) for (x, y) in
                                       zip([(0 + self._DesignParameter['PM1']['_XYCoordinates'][0][0]),
                                            (0 + self._DesignParameter['PM1']['_XYCoordinates'][0][1])],
                                           self._DesignParameter['PM1']['_DesignObj']._DesignParameter['_POLayer'][
                                               '_XYCoordinates'][i])])
            for i in range(len(xy_with_offset)):
                path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
        elif (mode == 'horizontal'):
            xy_with_offset = []
            target_x_value = (0 + self._DesignParameter['polyboundaryEN_0']['_XYCoordinates'][0][0])
            for i in range(
                    len(self._DesignParameter['PM1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
                xy_with_offset.append([(x + y) for (x, y) in
                                       zip([(0 + self._DesignParameter['PM1']['_XYCoordinates'][0][0]),
                                            (0 + self._DesignParameter['PM1']['_XYCoordinates'][0][1])],
                                           self._DesignParameter['PM1']['_DesignObj']._DesignParameter['_POLayer'][
                                               '_XYCoordinates'][i])])
            for i in range(len(xy_with_offset)):
                path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
        self._DesignParameter['PolyYForENb'] = self._PathElementDeclaration(
            _Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1],
            _Width=_width)
        self._DesignParameter['PolyYForENb']['_XYCoordinates'] = path_list
        self._DesignParameter['XVTpath'] = self._PathElementDeclaration(
            _Layer=DesignParameters._LayerMapping['SLVT'][0], _Datatype=DesignParameters._LayerMapping['SLVT'][1],
            _Width=self._DesignParameter['VSSRail']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth'])
        self._DesignParameter['XVTpath']['_XYCoordinates'] = [[[(+self._DesignParameter['VSSRail']['_XYCoordinates'][0][
            0]), (+ self._DesignParameter['VSSRail']['_XYCoordinates'][0][1])], [
                                                                   self._DesignParameter['VSSRail']['_XYCoordinates'][
                                                                       0][0],
                                                                   self._DesignParameter['VDDRail']['_XYCoordinates'][
                                                                       0][1]]]]
        self._DesignParameter['nwlayer'] = self._PathElementDeclaration(
            _Layer=DesignParameters._LayerMapping['NWELL'][0], _Datatype=DesignParameters._LayerMapping['NWELL'][1],
            _Width=((max(abs(((self._DesignParameter['PM2']['_XYCoordinates'][0][0] +
                               self._DesignParameter['PM2']['_DesignObj']._DesignParameter['_ODLayer'][
                                   '_XYCoordinates'][0][0]) + (
                                          self._DesignParameter['PM2']['_DesignObj']._DesignParameter['_ODLayer'][
                                              '_XWidth'] / 2))), abs(((self._DesignParameter['PM1']['_XYCoordinates'][
                                                                           0][0] + self._DesignParameter['PM1'][
                                                                           '_DesignObj']._DesignParameter['_ODLayer'][
                                                                           '_XYCoordinates'][0][0]) - (
                                                                                  self._DesignParameter['PM1'][
                                                                                      '_DesignObj']._DesignParameter[
                                                                                      '_ODLayer'][
                                                                                      '_XWidth'] / 2)))) + drc._NwMinEnclosurePactive2) * 2))
        self._DesignParameter['nwlayer']['_XYCoordinates'] = [[[(self._DesignParameter['VDDRail']['_XYCoordinates'][0][
                                                                     0] + self._DesignParameter['VDDRail'][
                                                                     '_DesignObj']._DesignParameter['_ODLayer'][
                                                                     '_XYCoordinates'][0][0]), (((self._DesignParameter[
                                                                                                      'VDDRail'][
                                                                                                      '_XYCoordinates'][
                                                                                                      0][1] +
                                                                                                  self._DesignParameter[
                                                                                                      'VDDRail'][
                                                                                                      '_DesignObj']._DesignParameter[
                                                                                                      '_ODLayer'][
                                                                                                      '_XYCoordinates'][
                                                                                                      0][1]) + (
                                                                                                             self._DesignParameter[
                                                                                                                 'VDDRail'][
                                                                                                                 '_DesignObj']._DesignParameter[
                                                                                                                 '_ODLayer'][
                                                                                                                 '_YWidth'] / 2)) + drc._NwMinEnclosurePactive)],
                                                               [(self._DesignParameter['VDDRail']['_XYCoordinates'][0][
                                                                     0] + self._DesignParameter['VDDRail'][
                                                                     '_DesignObj']._DesignParameter['_ODLayer'][
                                                                     '_XYCoordinates'][0][0]), (min(((
                                                                                                                 self._DesignParameter[
                                                                                                                     'PM1'][
                                                                                                                     '_XYCoordinates'][
                                                                                                                     0][
                                                                                                                     1] +
                                                                                                                 self._DesignParameter[
                                                                                                                     'PM1'][
                                                                                                                     '_DesignObj']._DesignParameter[
                                                                                                                     '_ODLayer'][
                                                                                                                     '_XYCoordinates'][
                                                                                                                     0][
                                                                                                                     1]) - (
                                                                                                                 self._DesignParameter[
                                                                                                                     'PM1'][
                                                                                                                     '_DesignObj']._DesignParameter[
                                                                                                                     '_ODLayer'][
                                                                                                                     '_YWidth'] / 2)),
                                                                                                    ((
                                                                                                                 self._DesignParameter[
                                                                                                                     'PM2'][
                                                                                                                     '_XYCoordinates'][
                                                                                                                     0][
                                                                                                                     1] +
                                                                                                                 self._DesignParameter[
                                                                                                                     'PM2'][
                                                                                                                     '_DesignObj']._DesignParameter[
                                                                                                                     '_ODLayer'][
                                                                                                                     '_XYCoordinates'][
                                                                                                                     0][
                                                                                                                     1]) - (
                                                                                                                 self._DesignParameter[
                                                                                                                     'PM2'][
                                                                                                                     '_DesignObj']._DesignParameter[
                                                                                                                     '_ODLayer'][
                                                                                                                     '_YWidth'] / 2))) - drc._NwMinEnclosurePactive)]]]
        XYList = []
        xy_offset = (0, ((((- (self._DesignParameter['NM1']['_XYCoordinates'][0][1] +
                               self._DesignParameter['NM1']['_DesignObj']._DesignParameter['_Met1Layer'][
                                   '_XYCoordinates'][0][1])) + ((self._DesignParameter['VSSRail']['_XYCoordinates'][0][
                                                                     1] + self._DesignParameter['VSSRail'][
                                                                     '_DesignObj']._DesignParameter['_Met2Layer'][
                                                                     '_XYCoordinates'][0][1]) + (
                                                                            self._DesignParameter['VSSRail'][
                                                                                '_DesignObj']._DesignParameter[
                                                                                '_Met2Layer'][
                                                                                '_YWidth'] / 2))) + 98) + drc._MetalxMinSpace21))
        for i in range(
                len(self._DesignParameter['NM1']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'])):
            if ((i % 2) == 1):
                XYList.append([((x + y) + z) for (x, y, z) in
                               zip([(0 + self._DesignParameter['NM1']['_XYCoordinates'][0][0]),
                                    (0 + self._DesignParameter['NM1']['_XYCoordinates'][0][1])],
                                   self._DesignParameter['NM1']['_DesignObj']._DesignParameter['_Met1Layer'][
                                       '_XYCoordinates'][i], xy_offset)])
        self._DesignParameter['via1nmos'] = \
        self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='via1nmosIn{}'.format(_Name)))[0]
        self._DesignParameter['via1nmos']['_DesignObj']._CalculateDesignParameterSameEnclosure(
            **dict(_ViaMet12Met2NumberOfCOX=1, _ViaMet12Met2NumberOfCOY=2))
        self._DesignParameter['via1nmos']['_XYCoordinates'] = XYList
        XYList = []
        xy_offset = (0, ((((- self._DesignParameter['PM1']['_XYCoordinates'][0][1]) + ((self._DesignParameter[
                                                                                            'VDDRail'][
                                                                                            '_XYCoordinates'][0][1] +
                                                                                        self._DesignParameter[
                                                                                            'VDDRail'][
                                                                                            '_DesignObj']._DesignParameter[
                                                                                            '_Met2Layer'][
                                                                                            '_XYCoordinates'][0][1]) - (
                                                                                                   self._DesignParameter[
                                                                                                       'VDDRail'][
                                                                                                       '_DesignObj']._DesignParameter[
                                                                                                       '_Met2Layer'][
                                                                                                       '_YWidth'] / 2))) - drc._MetalxMinSpace21) - 98))
        for i in range(
                len(self._DesignParameter['PM1']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'])):
            if ((i % 2) == 1):
                XYList.append([((x + y) + z) for (x, y, z) in
                               zip([(0 + self._DesignParameter['PM1']['_XYCoordinates'][0][0]),
                                    (0 + self._DesignParameter['PM1']['_XYCoordinates'][0][1])],
                                   self._DesignParameter['PM1']['_DesignObj']._DesignParameter['_Met1Layer'][
                                       '_XYCoordinates'][i], xy_offset)])
        self._DesignParameter['via1ForPM1'] = \
        self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='via1ForPM1In{}'.format(_Name)))[0]
        self._DesignParameter['via1ForPM1']['_DesignObj']._CalculateDesignParameterSameEnclosure(
            **dict(_ViaMet12Met2NumberOfCOX=1, _ViaMet12Met2NumberOfCOY=2))
        self._DesignParameter['via1ForPM1']['_XYCoordinates'] = XYList
        XYList = []
        xy_offset = (0, ((- self._DesignParameter['NM2']['_XYCoordinates'][0][1]) +
                         self._DesignParameter['via1nmos']['_XYCoordinates'][0][1]))
        for i in range(
                len(self._DesignParameter['NM2']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'])):
            if ((i % 2) == 0):
                XYList.append([((x + y) + z) for (x, y, z) in
                               zip([(0 + self._DesignParameter['NM2']['_XYCoordinates'][0][0]),
                                    (0 + self._DesignParameter['NM2']['_XYCoordinates'][0][1])],
                                   self._DesignParameter['NM2']['_DesignObj']._DesignParameter['_Met1Layer'][
                                       '_XYCoordinates'][i], xy_offset)])
        self._DesignParameter['via1ForNM2'] = \
        self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='via1ForNM2In{}'.format(_Name)))[0]
        self._DesignParameter['via1ForNM2']['_DesignObj']._CalculateDesignParameterSameEnclosure(
            **dict(_ViaMet12Met2NumberOfCOX=1, _ViaMet12Met2NumberOfCOY=2))
        self._DesignParameter['via1ForNM2']['_XYCoordinates'] = XYList
        XYList = []
        xy_offset = (0, ((- self._DesignParameter['PM2']['_XYCoordinates'][0][1]) +
                         self._DesignParameter['via1ForPM1']['_XYCoordinates'][0][1]))
        for i in range(
                len(self._DesignParameter['PM2']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'])):
            if ((i % 2) == 0):
                XYList.append([((x + y) + z) for (x, y, z) in
                               zip([(0 + self._DesignParameter['PM2']['_XYCoordinates'][0][0]),
                                    (0 + self._DesignParameter['PM2']['_XYCoordinates'][0][1])],
                                   self._DesignParameter['PM2']['_DesignObj']._DesignParameter['_Met1Layer'][
                                       '_XYCoordinates'][i], xy_offset)])
        self._DesignParameter['via1ForPM2'] = \
        self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='via1ForPM2In{}'.format(_Name)))[0]
        self._DesignParameter['via1ForPM2']['_DesignObj']._CalculateDesignParameterSameEnclosure(
            **dict(_ViaMet12Met2NumberOfCOX=1, _ViaMet12Met2NumberOfCOY=2))
        self._DesignParameter['via1ForPM2']['_XYCoordinates'] = XYList
        self._DesignParameter['m2pathnm1nm2'] = self._PathElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1],
            _Width=drc._MetalxMinWidth)
        self._DesignParameter['m2pathnm1nm2']['_XYCoordinates'] = [[[(+self._DesignParameter['via1nmos'][
            '_XYCoordinates'][0][0]), (+ self._DesignParameter['via1nmos']['_XYCoordinates'][0][1])], [
                                                                        self._DesignParameter['via1ForNM2'][
                                                                            '_XYCoordinates'][(- 1)][0],
                                                                        self._DesignParameter['via1nmos'][
                                                                            '_XYCoordinates'][0][1]]]]
        self._DesignParameter['m2pathpm1pm2'] = self._PathElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1],
            _Width=drc._MetalxMinWidth)
        self._DesignParameter['m2pathpm1pm2']['_XYCoordinates'] = [[[(+self._DesignParameter['via1ForPM1'][
            '_XYCoordinates'][0][0]), (+ self._DesignParameter['via1ForPM1']['_XYCoordinates'][0][1])], [
                                                                        self._DesignParameter['via1ForPM2'][
                                                                            '_XYCoordinates'][(- 1)][0],
                                                                        self._DesignParameter['via1ForPM1'][
                                                                            '_XYCoordinates'][0][1]]]]
