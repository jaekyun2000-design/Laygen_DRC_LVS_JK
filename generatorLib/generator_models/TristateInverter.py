from generatorLib import StickDiagram
from generatorLib import DesignParameters
import copy
import math
from generatorLib import DRC
from generatorLib import CoordinateCalc as CoordCalc
from generatorLib.generator_models import SupplyRails
from generatorLib.generator_models import ViaMet12Met2
from generatorLib.generator_models import NMOSWithDummy
from generatorLib.generator_models import ViaPoly2Met1
from generatorLib.generator_models import PMOSWithDummy
from generatorLib.generator_models import ViaPoly2Met1_resize
from generatorLib.generator_models import CascodePMOS
from generatorLib.generator_models import CascodeNMOS
from generatorLib.generator_models import Z_PWR_CNT


class TristateInverter(StickDiagram._StickDiagram):
    def __init__(self, _DesignParameter=None, _Name='TristateInverter'):
        if _DesignParameter != None:
            self._DesignParameter = _DesignParameter
        else:
            self._DesignParameter = dict(_Name=self._NameDeclaration(_Name=_Name), _GDSFile=self._GDSObjDeclaration(_GDSFile=None))
        self._DesignParameter['_Name']['Name'] = _Name


    def _CalculateDesignParameterFinger1(self,
                                         NMOSWidth=250,
                                         PMOSWidth=500,

                                         ChannelLength=30,
                                         GateSpacing=100,
                                         XVT='SLVT',

                                         CellHeight=1800,           # Required
                                         VDD2PMOS=400,              # Required
                                         VSS2NMOS=275,              # Required

                                         YCoordOfInputA=None,       # Optional
                                         YCoordOfInputEN=None,      # Optional
                                         YCoordOfInputENb=None,     # Optional
                                         SupplyRailType=1
                                         ):

        drc = DRC.DRC()
        _Name = self._DesignParameter['_Name']['_Name']


        if SupplyRailType == 1:
            bool_deleteViaAndMet1 = False
        elif SupplyRailType == 2:
            bool_deleteViaAndMet1 = True
        else:
            raise NotImplementedError

        self._DesignParameter['VSSRail'] = self._SrefElementDeclaration(_DesignObj=SupplyRails.SupplyRail(_Name='VSSRailIn{}'.format(_Name)))[0]
        self._DesignParameter['VDDRail'] = self._SrefElementDeclaration(_DesignObj=SupplyRails.SupplyRail(_Name='VDDRailIn{}'.format(_Name)))[0]
        self._DesignParameter['VSSRail']['_DesignObj']._CalculateDesignParameter(
            **dict(NumPitch=3, UnitPitch=(GateSpacing + ChannelLength), Met1YWidth=80, Met2YWidth=300, PpNpYWidth=180,
                   isPbody=True, deleteViaAndMet1=bool_deleteViaAndMet1))
        self._DesignParameter['VDDRail']['_DesignObj']._CalculateDesignParameter(
            **dict(NumPitch=3, UnitPitch=(GateSpacing + ChannelLength), Met1YWidth=80, Met2YWidth=300, PpNpYWidth=180,
                   isPbody=False, deleteViaAndMet1=bool_deleteViaAndMet1))
        self._DesignParameter['VSSRail']['_XYCoordinates'] = [[0, 0]]
        self._DesignParameter['VDDRail']['_XYCoordinates'] = [[0, CellHeight]]

        self._DesignParameter['NMOS'] = self._SrefElementDeclaration(_DesignObj=CascodeNMOS._CascodeNMOS(_Name='CascodeNMOSIn{}'.format(_Name)))[0]
        self._DesignParameter['NMOS']['_DesignObj']._CalculateDesignParameter(**dict(_NMOSChannelWidth=NMOSWidth, _NMOSChannellength=ChannelLength, _NMOSDummy=True, _XVT=XVT, _GateSpacing=GateSpacing))
        self._DesignParameter['NMOS']['_XYCoordinates'] = [[0, VSS2NMOS]]
        self._DesignParameter['PMOS'] = self._SrefElementDeclaration(_DesignObj=CascodePMOS._CascodePMOS(_Name='CascodePMOSIn{}'.format(_Name)))[0]
        self._DesignParameter['PMOS']['_DesignObj']._CalculateDesignParameter(**dict(_PMOSChannelWidth=PMOSWidth, _PMOSChannellength=ChannelLength, _PMOSDummy=True, _XVT=XVT, _GateSpacing=GateSpacing))
        self._DesignParameter['PMOS']['_XYCoordinates'] = [[0, (CellHeight - VDD2PMOS)]]

        self._DesignParameter['VSSRouting'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1'][0],
            _Datatype=DesignParameters._LayerMapping['METAL1'][1],
            _XWidth=self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'],
            _YWidth=(((self._DesignParameter['NMOS']['_XYCoordinates'][0][1] + self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) + (self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)) - (self._DesignParameter['VSSRail']['_XYCoordinates'][0][1])))
        self._DesignParameter['VSSRouting']['_XYCoordinates'] = [[
            (self._DesignParameter['NMOS']['_XYCoordinates'][0][0] + self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][1][0]),
            ((((self._DesignParameter['NMOS']['_XYCoordinates'][0][1] + self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) + (self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)) + (self._DesignParameter['VSSRail']['_XYCoordinates'][0][1])) / 2)]]
        self._DesignParameter['VDDRouting'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1'][0],
            _Datatype=DesignParameters._LayerMapping['METAL1'][1],
            _XWidth=self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'],
            _YWidth=(self._DesignParameter['VDDRail']['_XYCoordinates'][0][1] - ((self._DesignParameter['PMOS']['_XYCoordinates'][0][1] + self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) - (self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2))))
        self._DesignParameter['VDDRouting']['_XYCoordinates'] = [[(self._DesignParameter['PMOS']['_XYCoordinates'][0][0] + self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][1][0]), (((self._DesignParameter['VDDRail']['_XYCoordinates'][0][1]) + ((self._DesignParameter['PMOS']['_XYCoordinates'][0][1] + self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) - (self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2))) / 2)]]

        if SupplyRailType == 2:
            tmpXYs = []
            for XYs in self.getXY('VSSRouting'):
                tmpXYs.append([XYs[0], 0])
            self._DesignParameter['ViaForVSS'] = self._SrefElementDeclaration(_DesignObj=Z_PWR_CNT.Z_PWR_CNT(_Name='ViaForVSSIn{}'.format(_Name)))[0]
            self._DesignParameter['ViaForVSS']['_DesignObj']._CalculateDesignParameter(**dict(_Xnum=1, _Xdistance=0))
            self._DesignParameter['ViaForVSS']['_XYCoordinates'] = tmpXYs

            tmpXYs = []
            for XYs in self.getXY('VDDRouting'):
                tmpXYs.append([XYs[0], CellHeight])
            self._DesignParameter['ViaForVDD'] = self._SrefElementDeclaration(_DesignObj=Z_PWR_CNT.Z_PWR_CNT(_Name='ViaForVDDIn{}'.format(_Name)))[0]
            self._DesignParameter['ViaForVDD']['_DesignObj']._CalculateDesignParameter(**dict(_Xnum=1, _Xdistance=0))
            self._DesignParameter['ViaForVDD']['_XYCoordinates'] = tmpXYs
        else:
            pass

        self._DesignParameter['XVTLayer'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping[XVT][0], _Datatype=DesignParameters._LayerMapping[XVT][1],
            _XWidth=self._DesignParameter['VSSRail']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth'],
            _YWidth=CellHeight,
            _XYCoordinates=[[0, (CellHeight / 2)]]
        )

        ''' Calculate InputVia(EN,ENb)'s YCoordinates '''
        self._DesignParameter['InputVia_EN'] = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1_resize._ViaPoly2Met1_resize(_Name='InputVia_ENIn{}'.format(_Name)))[0]
        self._DesignParameter['InputVia_EN']['_DesignObj']._CalculateDesignParameter(
            **dict(_ViaPoly2Met1NumberOfCOX=1, _ViaPoly2Met1NumberOfCOY=2,
                   Met1XWidth=66, Met1YWidth=200, POXWidth=40, POYWidth=200))
        self._DesignParameter['InputVia_ENb'] = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1_resize._ViaPoly2Met1_resize(_Name='InputVia_ENbIn{}'.format(_Name)))[0]
        self._DesignParameter['InputVia_ENb']['_DesignObj']._CalculateDesignParameter(
            **dict(_ViaPoly2Met1NumberOfCOX=1, _ViaPoly2Met1NumberOfCOY=2,
                   Met1XWidth=66, Met1YWidth=200, POXWidth=40, POYWidth=200))
        self._DesignParameter['InputVia_A'] = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1_resize._ViaPoly2Met1_resize(_Name='InputVia_AIn{}'.format(_Name)))[0]
        self._DesignParameter['InputVia_A']['_DesignObj']._CalculateDesignParameter(
            **dict(_ViaPoly2Met1NumberOfCOX=1, _ViaPoly2Met1NumberOfCOY=2,
                   Met1XWidth=66, Met1YWidth=200, POXWidth=50, POYWidth=200))

        Xgap_InputContactPoly2DummyPoly = (-(GateSpacing + ChannelLength) - self.getXWidth('InputVia_EN', '_POLayer') / 2) \
                                          - (self.getXY('NMOS', '_PODummyLayer')[0][0] + self.getXWidth('NMOS', '_PODummyLayer') / 2)
        Ygap_InputContactPoly2DummyPoly = math.ceil(math.sqrt(drc._PolygateMinSpaceAtCorner ** 2 - Xgap_InputContactPoly2DummyPoly ** 2))

        if YCoordOfInputEN == None:
            YCoordOfInputVia_EN = math.ceil(self.getXY('NMOS', '_PODummyLayer')[0][1] + self.getYWidth('NMOS', '_PODummyLayer') / 2 \
                                            + Ygap_InputContactPoly2DummyPoly \
                                            + self.getYWidth('InputVia_EN', '_POLayer') / 2)
        else:
            YCoordOfInputVia_EN = YCoordOfInputEN

        if YCoordOfInputENb == None:
            YCoordOfInputVia_ENb = math.floor(self.getXY('PMOS', '_PODummyLayer')[0][1] - self.getYWidth('PMOS', '_PODummyLayer') / 2 \
                                              - Ygap_InputContactPoly2DummyPoly \
                                              - self.getYWidth('InputVia_ENb', '_POLayer') / 2)
        else:
            YCoordOfInputVia_ENb = YCoordOfInputENb

        if YCoordOfInputA == None:
            YCoordOfInputVia_A = math.ceil((self.getXY('NMOS')[0][1] + self.getXY('PMOS')[0][1]) / 2)
        else:
            YCoordOfInputVia_A = YCoordOfInputA

        self._DesignParameter['InputVia_EN']['_XYCoordinates'] = [[int(self.getXY('NMOS', '_Met1Layer')[0][0]), YCoordOfInputVia_EN]]
        self._DesignParameter['InputVia_ENb']['_XYCoordinates'] = [[int(self.getXY('NMOS', '_Met1Layer')[0][0]), YCoordOfInputVia_ENb]]
        self._DesignParameter['InputVia_A']['_XYCoordinates'] = [[int(self.getXY('NMOS', '_Met1Layer')[-1][0]), YCoordOfInputVia_A]]
        self._DesignParameter['POLY_boundary_30'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _XWidth=ChannelLength, _YWidth=(((self._DesignParameter['InputVia_EN']['_XYCoordinates'][0][1] + self._DesignParameter['InputVia_EN']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1]) - (self._DesignParameter['InputVia_EN']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2)) - ((self._DesignParameter['NMOS']['_XYCoordinates'][0][1] + self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1]) + (self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2))))
        self._DesignParameter['POLY_boundary_30']['_XYCoordinates'] = [[(self._DesignParameter['NMOS']['_XYCoordinates'][0][0] + self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]), ((((self._DesignParameter['InputVia_EN']['_XYCoordinates'][0][1] + self._DesignParameter['InputVia_EN']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1]) - (self._DesignParameter['InputVia_EN']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2)) + ((self._DesignParameter['NMOS']['_XYCoordinates'][0][1] + self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1]) + (self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2))) / 2)]]
        self._DesignParameter['POLY_boundary_29'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _XWidth=(((self._DesignParameter['NMOS']['_XYCoordinates'][0][0] + self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) + (self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)) - ((self._DesignParameter['InputVia_EN']['_XYCoordinates'][0][0] + self._DesignParameter['InputVia_EN']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) + (self._DesignParameter['InputVia_EN']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2))), _YWidth=((self._DesignParameter['InputVia_EN']['_XYCoordinates'][0][1] + self._DesignParameter['InputVia_EN']['_DesignObj']._DesignParameter['_COLayer']['_XYCoordinates'][0][1]) - ((self._DesignParameter['InputVia_EN']['_XYCoordinates'][0][1] + self._DesignParameter['InputVia_EN']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1]) - (self._DesignParameter['InputVia_EN']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2))))
        self._DesignParameter['POLY_boundary_29']['_XYCoordinates'] = [[((((self._DesignParameter['InputVia_EN']['_XYCoordinates'][0][0] + self._DesignParameter['InputVia_EN']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) + (self._DesignParameter['InputVia_EN']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)) + ((self._DesignParameter['NMOS']['_XYCoordinates'][0][0] + self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) + (self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2))) / 2), (((self._DesignParameter['InputVia_EN']['_XYCoordinates'][0][1] + self._DesignParameter['InputVia_EN']['_DesignObj']._DesignParameter['_COLayer']['_XYCoordinates'][0][1]) + ((self._DesignParameter['InputVia_EN']['_XYCoordinates'][0][1] + self._DesignParameter['InputVia_EN']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1]) - (self._DesignParameter['InputVia_EN']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2))) / 2)]]
        self._DesignParameter['POLY_boundary_24'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _XWidth=ChannelLength, _YWidth=(((self._DesignParameter['PMOS']['_XYCoordinates'][0][1] + self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1]) - (self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2)) - ((self._DesignParameter['InputVia_ENb']['_XYCoordinates'][0][1] + self._DesignParameter['InputVia_ENb']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1]) + (self._DesignParameter['InputVia_ENb']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2))))
        self._DesignParameter['POLY_boundary_24']['_XYCoordinates'] = [[(self._DesignParameter['PMOS']['_XYCoordinates'][0][0] + self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]), ((((self._DesignParameter['PMOS']['_XYCoordinates'][0][1] + self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1]) - (self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2)) + ((self._DesignParameter['InputVia_ENb']['_XYCoordinates'][0][1] + self._DesignParameter['InputVia_ENb']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1]) + (self._DesignParameter['InputVia_ENb']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2))) / 2)]]
        self._DesignParameter['POLY_boundary_23'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _XWidth=(((self._DesignParameter['PMOS']['_XYCoordinates'][0][0] + self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) + (self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)) - ((self._DesignParameter['InputVia_ENb']['_XYCoordinates'][0][0] + self._DesignParameter['InputVia_ENb']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) + (self._DesignParameter['InputVia_ENb']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2))), _YWidth=(((self._DesignParameter['InputVia_ENb']['_XYCoordinates'][0][1] + self._DesignParameter['InputVia_ENb']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1]) + (self._DesignParameter['InputVia_ENb']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2)) - (self._DesignParameter['InputVia_ENb']['_XYCoordinates'][0][1] + self._DesignParameter['InputVia_ENb']['_DesignObj']._DesignParameter['_COLayer']['_XYCoordinates'][1][1])))
        self._DesignParameter['POLY_boundary_23']['_XYCoordinates'] = [[((((self._DesignParameter['PMOS']['_XYCoordinates'][0][0] + self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) + (self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)) + ((self._DesignParameter['InputVia_ENb']['_XYCoordinates'][0][0] + self._DesignParameter['InputVia_ENb']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) + (self._DesignParameter['InputVia_ENb']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2))) / 2), ((((self._DesignParameter['InputVia_ENb']['_XYCoordinates'][0][1] + self._DesignParameter['InputVia_ENb']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1]) + (self._DesignParameter['InputVia_ENb']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2)) + (self._DesignParameter['InputVia_ENb']['_XYCoordinates'][0][1] + self._DesignParameter['InputVia_ENb']['_DesignObj']._DesignParameter['_COLayer']['_XYCoordinates'][1][1])) / 2)]]
        self._DesignParameter['NWELL_boundary_2'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['NWELL'][0], _Datatype=DesignParameters._LayerMapping['NWELL'][1], _XWidth=max((self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth'] + (2 * drc._NwMinEnclosurePactive2)), (self._DesignParameter['VDDRail']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth'] + (2 * drc._NwMinEnclosurePactive))), _YWidth=((((self._DesignParameter['VDDRail']['_XYCoordinates'][0][1] + self._DesignParameter['VDDRail']['_DesignObj']._DesignParameter['_ODLayer']['_XYCoordinates'][0][1]) + (self._DesignParameter['VDDRail']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth'] / 2)) - ((self._DesignParameter['PMOS']['_XYCoordinates'][0][1] + self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_ODLayer']['_XYCoordinates'][0][1]) - (self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth'] / 2))) + (2 * drc._NwMinEnclosurePactive)))
        self._DesignParameter['NWELL_boundary_2']['_XYCoordinates'] = [[0, ((((self._DesignParameter['VDDRail']['_XYCoordinates'][0][1] + self._DesignParameter['VDDRail']['_DesignObj']._DesignParameter['_ODLayer']['_XYCoordinates'][0][1]) + (self._DesignParameter['VDDRail']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth'] / 2)) + ((self._DesignParameter['PMOS']['_XYCoordinates'][0][1] + self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_ODLayer']['_XYCoordinates'][0][1]) - (self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth'] / 2))) / 2)]]
        self._DesignParameter['OutputRouting'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'])
        self._DesignParameter['OutputRouting']['_XYCoordinates'] = [[[((self._DesignParameter['PMOS']['_XYCoordinates'][0][0] + self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0]) + (self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] / 2)), (((self._DesignParameter['PMOS']['_XYCoordinates'][0][1] + self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) - (self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)) + (self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] / 2))], [(self._DesignParameter['PMOS']['_XYCoordinates'][0][0] + self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_PPLayer']['_XYCoordinates'][0][0]), (((self._DesignParameter['PMOS']['_XYCoordinates'][0][1] + self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) - (self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)) + (self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] / 2))], [(self._DesignParameter['PMOS']['_XYCoordinates'][0][0] + self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_PPLayer']['_XYCoordinates'][0][0]), (((self._DesignParameter['NMOS']['_XYCoordinates'][0][1] + self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) + (self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)) - (self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] / 2))], [((self._DesignParameter['NMOS']['_XYCoordinates'][0][0] + self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0]) + (self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] / 2)), (((self._DesignParameter['NMOS']['_XYCoordinates'][0][1] + self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) + (self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)) - (self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] / 2))]]]
        self._DesignParameter['POLY_boundary_21'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _XWidth=ChannelLength, _YWidth=(((self._DesignParameter['PMOS']['_XYCoordinates'][0][1] + self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][1][1]) - (self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2)) - ((self._DesignParameter['InputVia_A']['_XYCoordinates'][0][1] + self._DesignParameter['InputVia_A']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1]) + (self._DesignParameter['InputVia_A']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2))))
        self._DesignParameter['POLY_boundary_21']['_XYCoordinates'] = [[(self._DesignParameter['PMOS']['_XYCoordinates'][0][0] + self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][1][0]), ((((self._DesignParameter['PMOS']['_XYCoordinates'][0][1] + self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][1][1]) - (self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2)) + ((self._DesignParameter['InputVia_A']['_XYCoordinates'][0][1] + self._DesignParameter['InputVia_A']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1]) + (self._DesignParameter['InputVia_A']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2))) / 2)]]
        self._DesignParameter['POLY_boundary_28'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _XWidth=ChannelLength, _YWidth=(((self._DesignParameter['InputVia_A']['_XYCoordinates'][0][1] + self._DesignParameter['InputVia_A']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1]) - (self._DesignParameter['InputVia_A']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2)) - ((self._DesignParameter['NMOS']['_XYCoordinates'][0][1] + self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][1][1]) + (self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2))))
        self._DesignParameter['POLY_boundary_28']['_XYCoordinates'] = [[(self._DesignParameter['NMOS']['_XYCoordinates'][0][0] + self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][1][0]), ((((self._DesignParameter['InputVia_A']['_XYCoordinates'][0][1] + self._DesignParameter['InputVia_A']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1]) - (self._DesignParameter['InputVia_A']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2)) + ((self._DesignParameter['NMOS']['_XYCoordinates'][0][1] + self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][1][1]) + (self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2))) / 2)]]
        self._DesignParameter['POLY_boundary_25'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _XWidth=(((self._DesignParameter['InputVia_A']['_XYCoordinates'][0][0] + self._DesignParameter['InputVia_A']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['InputVia_A']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)) - ((self._DesignParameter['PMOS']['_XYCoordinates'][0][0] + self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][1][0]) - (self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2))), _YWidth=(((self._DesignParameter['InputVia_A']['_XYCoordinates'][0][1] + self._DesignParameter['InputVia_A']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1]) + (self._DesignParameter['InputVia_A']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2)) - (self._DesignParameter['InputVia_A']['_XYCoordinates'][0][1] + self._DesignParameter['InputVia_A']['_DesignObj']._DesignParameter['_COLayer']['_XYCoordinates'][1][1])))
        self._DesignParameter['POLY_boundary_25']['_XYCoordinates'] = [[((((self._DesignParameter['InputVia_A']['_XYCoordinates'][0][0] + self._DesignParameter['InputVia_A']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['InputVia_A']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)) + ((self._DesignParameter['PMOS']['_XYCoordinates'][0][0] + self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][1][0]) - (self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2))) / 2), ((((self._DesignParameter['InputVia_A']['_XYCoordinates'][0][1] + self._DesignParameter['InputVia_A']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1]) + (self._DesignParameter['InputVia_A']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2)) + (self._DesignParameter['InputVia_A']['_XYCoordinates'][0][1] + self._DesignParameter['InputVia_A']['_DesignObj']._DesignParameter['_COLayer']['_XYCoordinates'][1][1])) / 2)]]
        self._DesignParameter['POLY_boundary_27'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _XWidth=(((self._DesignParameter['InputVia_A']['_XYCoordinates'][0][0] + self._DesignParameter['InputVia_A']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['InputVia_A']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)) - ((self._DesignParameter['NMOS']['_XYCoordinates'][0][0] + self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][1][0]) - (self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2))), _YWidth=((self._DesignParameter['InputVia_A']['_XYCoordinates'][0][1] + self._DesignParameter['InputVia_A']['_DesignObj']._DesignParameter['_COLayer']['_XYCoordinates'][0][1]) - ((self._DesignParameter['InputVia_A']['_XYCoordinates'][0][1] + self._DesignParameter['InputVia_A']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1]) - (self._DesignParameter['InputVia_A']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2))))
        self._DesignParameter['POLY_boundary_27']['_XYCoordinates'] = [[((((self._DesignParameter['InputVia_A']['_XYCoordinates'][0][0] + self._DesignParameter['InputVia_A']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['InputVia_A']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)) + ((self._DesignParameter['NMOS']['_XYCoordinates'][0][0] + self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][1][0]) - (self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2))) / 2), (((self._DesignParameter['InputVia_A']['_XYCoordinates'][0][1] + self._DesignParameter['InputVia_A']['_DesignObj']._DesignParameter['_COLayer']['_XYCoordinates'][0][1]) + ((self._DesignParameter['InputVia_A']['_XYCoordinates'][0][1] + self._DesignParameter['InputVia_A']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1]) - (self._DesignParameter['InputVia_A']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2))) / 2)]]


        ''' Pin(Label) '''
        self._DesignParameter['PIN_VSS'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL2PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL2PIN'][1],
            _Presentation=[0, 1, 1], _Reflect=[0, 0, 0], _Mag=0.04, _Angle=0, _TEXT='VSS',
            _XYCoordinates=[[0, 0]]
        )
        self._DesignParameter['PIN_VDD'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL2PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL2PIN'][1],
            _Presentation=[0, 1, 1], _Reflect=[0, 0, 0], _Mag=0.04, _Angle=0, _TEXT='VDD',
            _XYCoordinates=[[0, CellHeight]]
        )
        self._DesignParameter['PIN_A'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL1PIN'][1],
            _Presentation=[0, 1, 1], _Reflect=[0, 0, 0], _Mag=0.01, _Angle=0, _TEXT='A',
            _XYCoordinates=[self.getXY('InputVia_A')[0]],
        )
        # print('XYs: ', self._DesignParameter['PIN_A']['_XYCoordinates'])
        # self._DesignParameter['PIN_EN'] = self._TextElementDeclaration(
        #     _Layer=DesignParameters._LayerMapping['METAL1PIN'][0],
        #     _Datatype=DesignParameters._LayerMapping['METAL1PIN'][1],
        #     _Presentation=[0, 1, 1], _Reflect=[0, 0, 0], _Mag=0.01, _Angle=0, _TEXT='EN',
        #     _XYCoordinates=[self.getXY('InputVia_EN')[0]],
        # )
        self._DesignParameter['PIN_EN'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL1PIN'][1],
            _Presentation=[0, 1, 1], _Reflect=[0, 0, 0], _Mag=0.01, _Angle=0, _TEXT='EN',
            _XYCoordinates=[[int(self.getXY('NMOS', '_Met1Layer')[0][0]), YCoordOfInputVia_EN]],
        )
        print('XYs: ', self._DesignParameter['PIN_EN']['_XYCoordinates'])
        self._DesignParameter['PIN_ENb'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL1PIN'][1],
            _Presentation=[0, 1, 1], _Reflect=[0, 0, 0], _Mag=0.01, _Angle=0, _TEXT='ENb',
            _XYCoordinates=[self.getXY('InputVia_ENb')[0]],
        )
        # print('XYs: ', self._DesignParameter['PIN_ENb']['_XYCoordinates'])
        self._DesignParameter['PIN_Y'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL1PIN'][1],
            _Presentation=[0, 1, 1], _Reflect=[0, 0, 0], _Mag=0.01, _Angle=0, _TEXT='Y',
            _XYCoordinates=[[0, self.getXY('InputVia_A')[0][1]]]
        )
        # print('XYs: ', self._DesignParameter['PIN_Y']['_XYCoordinates'])

        # CellXWidth
        self.CellXWidth = self.getXY('NMOS', '_PODummyLayer')[-1][0] - self.getXY('NMOS', '_PODummyLayer')[0][0]

    def _CalculateDesignParameterFinger2(self,
                                         NMOSWidth=200,
                                         PMOSWidth=400,

                                         ChannelLength=30,
                                         GateSpacing=100,
                                         XVT='SLVT',

                                         CellHeight=1800,       # Required
                                         VDD2PMOS=410,          # Required
                                         VSS2NMOS=310,           # Required
                                         SupplyRailType=1
                                         ):

        drc = DRC.DRC()
        _Name = self._DesignParameter['_Name']['_Name']


        if SupplyRailType == 1:
            bool_deleteViaAndMet1 = False
        elif SupplyRailType == 2:
            bool_deleteViaAndMet1 = True
        else:
            raise NotImplementedError

        self._DesignParameter['VSSRail'] = self._SrefElementDeclaration(_DesignObj=SupplyRails.SupplyRail(_Name='VSSRailIn{}'.format(_Name)))[0]
        self._DesignParameter['VDDRail'] = self._SrefElementDeclaration(_DesignObj=SupplyRails.SupplyRail(_Name='VDDRailIn{}'.format(_Name)))[0]
        self._DesignParameter['VSSRail']['_DesignObj']._CalculateDesignParameter(
            **dict(NumPitch=5, UnitPitch=(GateSpacing + ChannelLength), Met1YWidth=80, Met2YWidth=300, PpNpYWidth=180,
                   isPbody=True, deleteViaAndMet1=bool_deleteViaAndMet1))
        self._DesignParameter['VDDRail']['_DesignObj']._CalculateDesignParameter(
            **dict(NumPitch=5, UnitPitch=(GateSpacing + ChannelLength), Met1YWidth=80, Met2YWidth=300, PpNpYWidth=180,
                   isPbody=False, deleteViaAndMet1=bool_deleteViaAndMet1))
        self._DesignParameter['VSSRail']['_XYCoordinates'] = [[0.0, 0.0]]
        self._DesignParameter['VDDRail']['_XYCoordinates'] = [[0, CellHeight]]

        self._DesignParameter['NMOS'] = self._SrefElementDeclaration(_DesignObj=NMOSWithDummy._NMOS(_Name='NMOSIn{}'.format(_Name)))[0]
        self._DesignParameter['NMOS']['_DesignObj']._CalculateNMOSDesignParameter(**dict(_NMOSNumberofGate=4, _NMOSChannelWidth=NMOSWidth, _NMOSChannellength=ChannelLength, _NMOSDummy=True, _GateSpacing=GateSpacing, _SDWidth=None, _XVT=XVT))
        self._DesignParameter['NMOS']['_XYCoordinates'] = [[0, VSS2NMOS]]
        self._DesignParameter['PMOS'] = self._SrefElementDeclaration(_DesignObj=PMOSWithDummy._PMOS(_Name='PMOSIn{}'.format(_Name)))[0]
        self._DesignParameter['PMOS']['_DesignObj']._CalculatePMOSDesignParameter(**dict(_PMOSNumberofGate=4, _PMOSChannelWidth=PMOSWidth, _PMOSChannellength=ChannelLength, _PMOSDummy=True, _GateSpacing=GateSpacing, _SDWidth=None, _XVT=XVT))
        self._DesignParameter['PMOS']['_XYCoordinates'] = [[0, (CellHeight - VDD2PMOS)]]

        self._DesignParameter['VSSRouting1'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1],
            _XWidth=self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'],
            _YWidth=(((self._DesignParameter['NMOS']['_XYCoordinates'][0][1] + self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) + (self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)) - (self._DesignParameter['VSSRail']['_XYCoordinates'][0][1])))
        self._DesignParameter['VSSRouting1']['_XYCoordinates'] = [
            [(self._DesignParameter['NMOS']['_XYCoordinates'][0][0] + self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0]),
             ((((self._DesignParameter['NMOS']['_XYCoordinates'][0][1] + self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) + (self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)) + (self._DesignParameter['VSSRail']['_XYCoordinates'][0][1])) / 2)]]
        self._DesignParameter['VSSRouting2'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _XWidth=self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'],  _YWidth=self.getYWidth('VSSRouting1'))
        self._DesignParameter['VSSRouting2']['_XYCoordinates'] = [
            [(self._DesignParameter['NMOS']['_XYCoordinates'][0][0] + self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][(- 1)][0]),
             ((((self._DesignParameter['NMOS']['_XYCoordinates'][0][1] + self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][(- 1)][1]) + (self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)) + (self._DesignParameter['VSSRail']['_XYCoordinates'][0][1])) / 2)]
        ]
        self._DesignParameter['VDDRouting1'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1],
            _XWidth=self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'],
            _YWidth=((self._DesignParameter['VDDRail']['_XYCoordinates'][0][1]) - ((self._DesignParameter['PMOS']['_XYCoordinates'][0][1] + self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) - (self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2))))
        self._DesignParameter['VDDRouting1']['_XYCoordinates'] = [[(self._DesignParameter['PMOS']['_XYCoordinates'][0][0] + self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0]), (((self._DesignParameter['VDDRail']['_XYCoordinates'][0][1]) + ((self._DesignParameter['PMOS']['_XYCoordinates'][0][1] + self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) - (self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2))) / 2)]]
        self._DesignParameter['VDDRouting2'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _XWidth=self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'], _YWidth=self.getYWidth('VDDRouting1'))
        self._DesignParameter['VDDRouting2']['_XYCoordinates'] = [[(self._DesignParameter['PMOS']['_XYCoordinates'][0][0] + self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][(- 1)][0]), (((self._DesignParameter['VDDRail']['_XYCoordinates'][0][1]) + ((self._DesignParameter['PMOS']['_XYCoordinates'][0][1] + self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) - (self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2))) / 2)]]

        if SupplyRailType == 2:
            self._DesignParameter['ViaForVSS'] = self._SrefElementDeclaration(_DesignObj=Z_PWR_CNT.Z_PWR_CNT(_Name='ViaForVSSIn{}'.format(_Name)))[0]
            self._DesignParameter['ViaForVSS']['_DesignObj']._CalculateDesignParameter(**dict(_Xnum=1, _Xdistance=0))
            self._DesignParameter['ViaForVSS']['_XYCoordinates'] = [
                [self.getXY('PMOS', '_Met1Layer')[0][0],  0],
                [self.getXY('PMOS', '_Met1Layer')[-1][0], 0]
            ]
            self._DesignParameter['ViaForVDD'] = self._SrefElementDeclaration(_DesignObj=Z_PWR_CNT.Z_PWR_CNT(_Name='ViaForVDDIn{}'.format(_Name)))[0]
            self._DesignParameter['ViaForVDD']['_DesignObj']._CalculateDesignParameter(**dict(_Xnum=1, _Xdistance=0))
            self._DesignParameter['ViaForVDD']['_XYCoordinates'] = [
                [self.getXY('PMOS', '_Met1Layer')[0][0],  CellHeight],
                [self.getXY('PMOS', '_Met1Layer')[-1][0], CellHeight]
            ]
        else:
            pass

        self._DesignParameter['polygate1'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _XWidth=ChannelLength, _YWidth=(((self._DesignParameter['PMOS']['_XYCoordinates'][0][1] + self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1]) - (self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2)) - ((self._DesignParameter['NMOS']['_XYCoordinates'][0][1] + self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1]) + (self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2))))
        self._DesignParameter['polygate1']['_XYCoordinates'] = [[(self._DesignParameter['NMOS']['_XYCoordinates'][0][0] + self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]), ((((self._DesignParameter['PMOS']['_XYCoordinates'][0][1] + self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1]) - (self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2)) + ((self._DesignParameter['NMOS']['_XYCoordinates'][0][1] + self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1]) + (self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2))) / 2)]]
        self._DesignParameter['polygate2'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _XWidth=ChannelLength, _YWidth=(((self._DesignParameter['PMOS']['_XYCoordinates'][0][1] + self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][1]) - (self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2)) - ((self._DesignParameter['NMOS']['_XYCoordinates'][0][1] + self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][1]) + (self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2))))
        self._DesignParameter['polygate2']['_XYCoordinates'] = [[(self._DesignParameter['NMOS']['_XYCoordinates'][0][0] + self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]), ((((self._DesignParameter['PMOS']['_XYCoordinates'][0][1] + self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][1]) - (self._DesignParameter['PMOS']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2)) + ((self._DesignParameter['NMOS']['_XYCoordinates'][0][1] + self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][1]) + (self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2))) / 2)]]
        self._DesignParameter['InputVia_A'] = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1_resize._ViaPoly2Met1_resize(_Name='InputVia_AIn{}'.format(_Name)))[0]
        self._DesignParameter['InputVia_A']['_DesignObj']._CalculateDesignParameter(**dict(_ViaPoly2Met1NumberOfCOX=1, _ViaPoly2Met1NumberOfCOY=2, Met1XWidth=66, Met1YWidth=200, POXWidth=40, POYWidth=200))
        self._DesignParameter['InputVia_A']['_XYCoordinates'] = [[(self._DesignParameter['NMOS']['_XYCoordinates'][0][0] + self._DesignParameter['NMOS']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]), self._DesignParameter['polygate1']['_XYCoordinates'][0][1]]]
        self._DesignParameter['polygate3'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _XWidth=((self._DesignParameter['polygate2']['_XYCoordinates'][0][0] - (self._DesignParameter['polygate2']['_XWidth'] / 2)) - (self._DesignParameter['polygate1']['_XYCoordinates'][0][0] + (self._DesignParameter['polygate1']['_XWidth'] / 2))), _YWidth=50.0)
        self._DesignParameter['polygate3']['_XYCoordinates'] = [[(((self._DesignParameter['polygate1']['_XYCoordinates'][0][0] + (self._DesignParameter['polygate1']['_XWidth'] / 2)) + (self._DesignParameter['polygate2']['_XYCoordinates'][0][0] - (self._DesignParameter['polygate2']['_XWidth'] / 2))) / 2), self._DesignParameter['InputVia_A']['_XYCoordinates'][0][1]]]

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
        self._DesignParameter['XVTLayer'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping[XVT][0], _Datatype=DesignParameters._LayerMapping[XVT][1],
            _XWidth=self._DesignParameter['VSSRail']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth'],
            _YWidth=CellHeight,
            _XYCoordinates=[[0, (CellHeight / 2)]]
        )

        ''' ---------------------------------------------- Pin(Label) ---------------------------------------------- '''
        self._DesignParameter['PIN_VSS'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL2PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL2PIN'][1],
            _Presentation=[0, 1, 1], _Reflect=[0, 0, 0], _Mag=0.04, _Angle=0, _TEXT='VSS',
            _XYCoordinates=[[0, 0]]
        )
        self._DesignParameter['PIN_VDD'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL2PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL2PIN'][1],
            _Presentation=[0, 1, 1], _Reflect=[0, 0, 0], _Mag=0.04, _Angle=0, _TEXT='VDD',
            _XYCoordinates=[[0, CellHeight]]
        )
        self._DesignParameter['PIN_A'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL1PIN'][1],
            _Presentation=[0, 1, 1], _Reflect=[0, 0, 0], _Mag=0.01, _Angle=0, _TEXT='A',
            _XYCoordinates=[self.getXY('InputVia_A')[0]],
        )
        self._DesignParameter['PIN_EN'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL1PIN'][1],
            _Presentation=[0, 1, 1], _Reflect=[0, 0, 0], _Mag=0.01, _Angle=0, _TEXT='EN',
            _XYCoordinates=[self.getXY('InputVia_EN')[0]],
        )
        self._DesignParameter['PIN_ENb'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL1PIN'][1],
            _Presentation=[0, 1, 1], _Reflect=[0, 0, 0], _Mag=0.01, _Angle=0, _TEXT='ENb',
            _XYCoordinates=[self.getXY('InputVia_ENb')[0]],
        )
        self._DesignParameter['PIN_Y'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL1PIN'][1],
            _Presentation=[0, 1, 1], _Reflect=[0, 0, 0], _Mag=0.01, _Angle=0, _TEXT='Y',
            _XYCoordinates=[[self.getXY('met1_output_5')[0][0], self.getXY('InputVia_A')[0][1]]]
        )

        # CellXWidth
        self.CellXWidth = self.getXY('NMOS', '_PODummyLayer')[-1][0] - self.getXY('NMOS', '_PODummyLayer')[0][0]


    def _CalculateDesignParameterFinger3orMore(self,
                                               NumFinger_NM1=3,
                                               NumFinger_NM2=5,
                                               Width_NM1=250,
                                               Width_NM2=300,
                                               Width_PM1=500,
                                               Width_PM2=600,

                                               ChannelLength=30,
                                               GateSpacing=100,
                                               XVT='SLVT',

                                               CellHeight=1800,         # Required
                                               YCoord_InputA=750,       # Required
                                               YCoord_InputEN=500,      # Required
                                               YCoord_InputENb=1000     # Required
                                               ):

        drc = DRC.DRC()
        _Name = self._DesignParameter['_Name']['_Name']

        NumFinger_PM1 = NumFinger_NM1
        NumFinger_PM2 = NumFinger_NM2

        NumViaY_InputA = 1
        NumViaY_InputEN = 1


        NumPitch_NM = ((NumFinger_NM1 + NumFinger_NM2) + 2)
        NumPitch_PM = ((NumFinger_PM1 + NumFinger_PM2) + 2)


        self._DesignParameter['VSSRail'] = self._SrefElementDeclaration(_DesignObj=SupplyRails.SupplyRail(_Name='VSSRailIn{}'.format(_Name)))[0]
        self._DesignParameter['VSSRail']['_DesignObj']._CalculateDesignParameter(
            **dict(NumPitch=max(NumPitch_NM, NumPitch_PM), UnitPitch=(GateSpacing + ChannelLength), Met1YWidth=80,
                   Met2YWidth=300, PpNpYWidth=180, isPbody=True))
        self._DesignParameter['VSSRail']['_XYCoordinates'] = [[0.0, 0.0]]
        self._DesignParameter['VDDRail'] = self._SrefElementDeclaration(_DesignObj=SupplyRails.SupplyRail(_Name='VDDRailIn{}'.format(_Name)))[0]
        self._DesignParameter['VDDRail']['_DesignObj']._CalculateDesignParameter(
            **dict(NumPitch=max(NumPitch_NM, NumPitch_PM), UnitPitch=130, Met1YWidth=80, Met2YWidth=300, PpNpYWidth=180,
                   isPbody=False))
        self._DesignParameter['VDDRail']['_XYCoordinates'] = [[0, CellHeight]]



        self._DesignParameter['NM1'] = self._SrefElementDeclaration(_DesignObj=NMOSWithDummy._NMOS(_Name='NM1In{}'.format(_Name)))[0]
        self._DesignParameter['NM1']['_DesignObj']._CalculateNMOSDesignParameter(
            **dict(_NMOSNumberofGate=NumFinger_NM1, _NMOSChannelWidth=Width_NM1, _NMOSChannellength=ChannelLength,
                   _NMOSDummy=True, _GateSpacing=GateSpacing, _SDWidth=66, _XVT=XVT))
        self._DesignParameter['NM1']['_XYCoordinates'] = [[(((- (NumFinger_NM2 + 1)) * (GateSpacing + ChannelLength)) / 2), ((( (self._DesignParameter['VSSRail']['_XYCoordinates'][0][1] + self._DesignParameter['VSSRail']['_DesignObj']._DesignParameter['_PPLayer']['_XYCoordinates'][0][1]) + (self._DesignParameter['VSSRail']['_DesignObj']._DesignParameter['_PPLayer']['_YWidth'] / 2)) + (self._DesignParameter['NM1']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth'] / 2)) + drc._OdMinSpace2Pp)]]
        self._DesignParameter['NM2'] = self._SrefElementDeclaration(_DesignObj=NMOSWithDummy._NMOS(_Name='NM2In{}'.format(_Name)))[0]
        self._DesignParameter['NM2']['_DesignObj']._CalculateNMOSDesignParameter(
            **dict(_NMOSNumberofGate=NumFinger_NM2, _NMOSChannelWidth=Width_NM2, _NMOSChannellength=ChannelLength,
                   _NMOSDummy=True, _GateSpacing=GateSpacing, _SDWidth=66, _XVT=XVT))
        self._DesignParameter['NM2']['_XYCoordinates'] = [[(((NumFinger_NM1 + 1) * (GateSpacing + ChannelLength)) / 2), ((((self._DesignParameter['VSSRail']['_XYCoordinates'][0][1] + self._DesignParameter['VSSRail']['_DesignObj']._DesignParameter['_PPLayer']['_XYCoordinates'][0][1]) + (self._DesignParameter['VSSRail']['_DesignObj']._DesignParameter['_PPLayer']['_YWidth'] / 2)) + (self._DesignParameter['NM2']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth'] / 2)) + drc._OdMinSpace2Pp)]]
        self._DesignParameter['PM1'] = self._SrefElementDeclaration(_DesignObj=PMOSWithDummy._PMOS(_Name='PM1In{}'.format(_Name)))[0]
        self._DesignParameter['PM1']['_DesignObj']._CalculatePMOSDesignParameter(
            **dict(_PMOSNumberofGate=NumFinger_PM1, _PMOSChannelWidth=Width_PM1, _PMOSChannellength=ChannelLength,
                   _PMOSDummy=True, _GateSpacing=GateSpacing, _SDWidth=66, _XVT=XVT))
        self._DesignParameter['PM1']['_XYCoordinates'] = [[(((- (NumFinger_PM2 + 1)) * (GateSpacing + ChannelLength)) / 2), ((((self._DesignParameter['VDDRail']['_XYCoordinates'][0][1] + self._DesignParameter['VDDRail']['_DesignObj']._DesignParameter['_ODLayer']['_XYCoordinates'][0][1]) - (self._DesignParameter['VDDRail']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth'] / 2)) - drc._OdMinSpace2Pp) - (self._DesignParameter['PM1']['_DesignObj']._DesignParameter['_PPLayer']['_YWidth'] / 2))]]
        self._DesignParameter['PM2'] = self._SrefElementDeclaration(_DesignObj=PMOSWithDummy._PMOS(_Name='PM2In{}'.format(_Name)))[0]
        self._DesignParameter['PM2']['_DesignObj']._CalculatePMOSDesignParameter(
            **dict(_PMOSNumberofGate=NumFinger_PM2, _PMOSChannelWidth=Width_PM2, _PMOSChannellength=ChannelLength,
                   _PMOSDummy=True, _GateSpacing=GateSpacing, _SDWidth=66, _XVT=XVT))
        self._DesignParameter['PM2']['_XYCoordinates'] = [[(((NumFinger_PM1 + 1) * (GateSpacing + ChannelLength)) / 2), ((((self._DesignParameter['VDDRail']['_XYCoordinates'][0][1] + self._DesignParameter['VDDRail']['_DesignObj']._DesignParameter['_ODLayer']['_XYCoordinates'][0][1]) - (self._DesignParameter['VDDRail']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth'] / 2)) - drc._OdMinSpace2Pp) - (self._DesignParameter['PM2']['_DesignObj']._DesignParameter['_PPLayer']['_YWidth'] / 2))]]
        path_list = []
        if (len(self._DesignParameter['NM1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates']) == 1):
            mode = 'vertical'
            _width = self._DesignParameter['NM1']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
        elif (self._DesignParameter['NM1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][0] ==self._DesignParameter['NM1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][0]):
            mode = 'horizontal'
            _width = self._DesignParameter['NM1']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
        elif (self._DesignParameter['NM1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1] ==self._DesignParameter['NM1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][1]):
            mode = 'vertical'
            _width = self._DesignParameter['NM1']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
        else:
            print('Invalid Target Input')
        if (mode == 'vertical'):
            xy_with_offset = []
            target_y_value = ((self._DesignParameter['VSSRail']['_XYCoordinates'][0][1] + self._DesignParameter['VSSRail']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) - (self._DesignParameter['VSSRail']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2))
            for i in range(len(self._DesignParameter['NM1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
                if ((i % 2) == 0):
                    xy_with_offset.append([(x + y) for (x, y) in
                                           zip([(0 + self._DesignParameter['NM1']['_XYCoordinates'][0][0]),
                                                (0 + self._DesignParameter['NM1']['_XYCoordinates'][0][1])],
                                               self._DesignParameter['NM1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])])
            for i in range(len(xy_with_offset)):
                path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
        elif (mode == 'horizontal'):
            xy_with_offset = []
            target_x_value = (self._DesignParameter['VSSRail']['_XYCoordinates'][0][0] + self._DesignParameter['VSSRail']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0])
            for i in range(len(self._DesignParameter['NM1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
                if ((i % 2) == 0):
                    xy_with_offset.append([(x + y) for (x, y) in
                                           zip([(0 + self._DesignParameter['NM1']['_XYCoordinates'][0][0]),
                                                (0 + self._DesignParameter['NM1']['_XYCoordinates'][0][1])],
                                               self._DesignParameter['NM1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])])
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
        elif (self._DesignParameter['PM1']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0] == self._DesignParameter['PM1']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][(- 1)][0]):
            mode = 'horizontal'
            _width = self._DesignParameter['PM1']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
        elif (self._DesignParameter['PM1']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1] == self._DesignParameter['PM1']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][(- 1)][1]):
            mode = 'vertical'
            _width = self._DesignParameter['PM1']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
        else:
            print('Invalid Target Input')
        if (mode == 'vertical'):
            xy_with_offset = []
            target_y_value = ((self._DesignParameter['VDDRail']['_XYCoordinates'][0][1] + self._DesignParameter['VDDRail']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) + (self._DesignParameter['VDDRail']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2))
            for i in range(
                    len(self._DesignParameter['PM1']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'])):
                if ((i % 2) == 0):
                    xy_with_offset.append([(x + y) for (x, y) in
                                           zip([(0 + self._DesignParameter['PM1']['_XYCoordinates'][0][0]),
                                                (0 + self._DesignParameter['PM1']['_XYCoordinates'][0][1])],
                                               self._DesignParameter['PM1']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i])])
            for i in range(len(xy_with_offset)):
                path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
        elif (mode == 'horizontal'):
            xy_with_offset = []
            target_x_value = (self._DesignParameter['VDDRail']['_XYCoordinates'][0][0] +
                              self._DesignParameter['VDDRail']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0])
            for i in range(
                    len(self._DesignParameter['PM1']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'])):
                if ((i % 2) == 0):
                    xy_with_offset.append([(x + y) for (x, y) in
                                           zip([(0 + self._DesignParameter['PM1']['_XYCoordinates'][0][0]),
                                                (0 + self._DesignParameter['PM1']['_XYCoordinates'][0][1])],
                                               self._DesignParameter['PM1']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i])])
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
        elif (self._DesignParameter['NM2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0] == self._DesignParameter['NM2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]):
            mode = 'horizontal'
            _width = self._DesignParameter['NM2']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
        elif (self._DesignParameter['NM2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1] == self._DesignParameter['NM2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][1]):
            mode = 'vertical'
            _width = self._DesignParameter['NM2']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
        else:
            print('Invalid Target Input')
        if (mode == 'vertical'):
            xy_with_offset = []
            target_y_value = (self._DesignParameter['PM2']['_XYCoordinates'][0][1] +
                              self._DesignParameter['PM2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1])
            for i in range(len(self._DesignParameter['NM2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
                xy_with_offset.append([(x + y) for (x, y) in
                                       zip([(0 + self._DesignParameter['NM2']['_XYCoordinates'][0][0]),
                                            (0 + self._DesignParameter['NM2']['_XYCoordinates'][0][1])],
                                           self._DesignParameter['NM2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i])])
            for i in range(len(xy_with_offset)):
                path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
        elif (mode == 'horizontal'):
            xy_with_offset = []
            target_x_value = (self._DesignParameter['PM2']['_XYCoordinates'][0][0] +
                              self._DesignParameter['PM2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0])
            for i in range(
                    len(self._DesignParameter['NM2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
                xy_with_offset.append([(x + y) for (x, y) in
                                       zip([(0 + self._DesignParameter['NM2']['_XYCoordinates'][0][0]),
                                            (0 + self._DesignParameter['NM2']['_XYCoordinates'][0][1])],
                                           self._DesignParameter['NM2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i])])
            for i in range(len(xy_with_offset)):
                path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
        self._DesignParameter['tttt'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0],
                                                                     _Datatype=DesignParameters._LayerMapping['POLY'][1], _Width=_width)
        self._DesignParameter['tttt']['_XYCoordinates'] = path_list


        NumViaX_InputEN = int((((((((self._DesignParameter['NM1']['_XYCoordinates'][0][0] + self._DesignParameter['NM1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]) + (self._DesignParameter['NM1']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)) - ((self._DesignParameter['NM1']['_XYCoordinates'][0][0] + self._DesignParameter['NM1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['NM1']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2))) - (2 * drc._CoMinEnclosureByODAtLeastTwoSide)) - drc._CoMinWidth) // (drc._CoMinWidth + drc._CoMinSpace)) + 1))
        self._DesignParameter['PolyContactEN'] = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_Name='PolyContactENIn{}'.format(_Name)))[0]
        self._DesignParameter['PolyContactEN']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(
            **dict(_ViaPoly2Met1NumberOfCOX=NumViaX_InputEN, _ViaPoly2Met1NumberOfCOY=NumViaY_InputEN))
        self._DesignParameter['PolyContactEN']['_XYCoordinates'] = [
            [self._DesignParameter['NM1']['_XYCoordinates'][0][0], YCoord_InputEN]]
        self._DesignParameter['PolyContactEN_0'] = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_Name='PolyContactEN_0In{}'.format(_Name)))[0]
        self._DesignParameter['PolyContactEN_0']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(
            **dict(_ViaPoly2Met1NumberOfCOX=NumViaX_InputEN, _ViaPoly2Met1NumberOfCOY=NumViaY_InputEN))
        self._DesignParameter['PolyContactEN_0']['_XYCoordinates'] = [
            [self._DesignParameter['PM1']['_XYCoordinates'][0][0], YCoord_InputENb]]
        self._DesignParameter['polyboundaryEN'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1],
            _XWidth=(((self._DesignParameter['NM1']['_XYCoordinates'][0][0] + self._DesignParameter['NM1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]) + (self._DesignParameter['NM1']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)) - ((self._DesignParameter['NM1']['_XYCoordinates'][0][0] + self._DesignParameter['NM1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['NM1']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2))),
            _YWidth=self._DesignParameter['PolyContactEN']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'])
        self._DesignParameter['polyboundaryEN']['_XYCoordinates'] = [
            [(+ self._DesignParameter['PolyContactEN']['_XYCoordinates'][0][0]),
             (+ self._DesignParameter['PolyContactEN']['_XYCoordinates'][0][1])]]
        self._DesignParameter['polyboundaryEN_0'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1],
            _XWidth=(((self._DesignParameter['NM1']['_XYCoordinates'][0][0] + self._DesignParameter['NM1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]) + (self._DesignParameter['NM1']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)) - ((self._DesignParameter['NM1']['_XYCoordinates'][0][0] + self._DesignParameter['NM1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['NM1']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2))),
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
                                           self._DesignParameter['NM1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i])])
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
                                           self._DesignParameter['NM1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i])])
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
            target_y_value = ((0 + self._DesignParameter['polyboundaryEN_0']['_XYCoordinates'][0][1]) + (self._DesignParameter['polyboundaryEN_0']['_YWidth'] / 2))
            for i in range(
                    len(self._DesignParameter['PM1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
                xy_with_offset.append([(x + y) for (x, y) in
                                       zip([(0 + self._DesignParameter['PM1']['_XYCoordinates'][0][0]),
                                            (0 + self._DesignParameter['PM1']['_XYCoordinates'][0][1])],
                                           self._DesignParameter['PM1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i])])
            for i in range(len(xy_with_offset)):
                path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
        elif (mode == 'horizontal'):
            xy_with_offset = []
            target_x_value = (0 + self._DesignParameter['polyboundaryEN_0']['_XYCoordinates'][0][0])
            for i in range(len(self._DesignParameter['PM1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
                xy_with_offset.append([(x + y) for (x, y) in
                                       zip([(0 + self._DesignParameter['PM1']['_XYCoordinates'][0][0]),
                                            (0 + self._DesignParameter['PM1']['_XYCoordinates'][0][1])],
                                           self._DesignParameter['PM1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i])])
            for i in range(len(xy_with_offset)):
                path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
        self._DesignParameter['PolyYForENb'] = self._PathElementDeclaration(
            _Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1],
            _Width=_width)
        self._DesignParameter['PolyYForENb']['_XYCoordinates'] = path_list
        self._DesignParameter['XVTpath'] = self._PathElementDeclaration(
            _Layer=DesignParameters._LayerMapping['SLVT'][0], _Datatype=DesignParameters._LayerMapping['SLVT'][1],
            _Width=self._DesignParameter['VSSRail']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth'])
        self._DesignParameter['XVTpath']['_XYCoordinates'] = [[[(+self._DesignParameter['VSSRail']['_XYCoordinates'][0][0]), (+ self._DesignParameter['VSSRail']['_XYCoordinates'][0][1])],
                                                               [self._DesignParameter['VSSRail']['_XYCoordinates'][0][0], self._DesignParameter['VDDRail']['_XYCoordinates'][0][1]]]]
        self._DesignParameter['nwlayer'] = self._PathElementDeclaration(
            _Layer=DesignParameters._LayerMapping['NWELL'][0], _Datatype=DesignParameters._LayerMapping['NWELL'][1],
            _Width=((max(abs(((self._DesignParameter['PM2']['_XYCoordinates'][0][0] + self._DesignParameter['PM2']['_DesignObj']._DesignParameter['_ODLayer']['_XYCoordinates'][0][0]) + (self._DesignParameter['PM2']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth'] / 2))), abs(((self._DesignParameter['PM1']['_XYCoordinates'][0][0] + self._DesignParameter['PM1']['_DesignObj']._DesignParameter['_ODLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['PM1']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth'] / 2)))) + drc._NwMinEnclosurePactive2) * 2))
        self._DesignParameter['nwlayer']['_XYCoordinates'] = [[[(self._DesignParameter['VDDRail']['_XYCoordinates'][0][0] + self._DesignParameter['VDDRail']['_DesignObj']._DesignParameter['_ODLayer']['_XYCoordinates'][0][0]), (((self._DesignParameter['VDDRail']['_XYCoordinates'][0][1] + self._DesignParameter['VDDRail']['_DesignObj']._DesignParameter['_ODLayer']['_XYCoordinates'][0][1]) + (self._DesignParameter['VDDRail']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth'] / 2)) + drc._NwMinEnclosurePactive)],
                                                               [(self._DesignParameter['VDDRail']['_XYCoordinates'][0][0] + self._DesignParameter['VDDRail']['_DesignObj']._DesignParameter['_ODLayer']['_XYCoordinates'][0][0]), (min(((self._DesignParameter['PM1']['_XYCoordinates'][0][1] + self._DesignParameter['PM1']['_DesignObj']._DesignParameter['_ODLayer']['_XYCoordinates'][0][1]) - (self._DesignParameter['PM1']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth'] / 2)), ((self._DesignParameter['PM2']['_XYCoordinates'][0][1] + self._DesignParameter['PM2']['_DesignObj']._DesignParameter['_ODLayer']['_XYCoordinates'][0][1]) - (self._DesignParameter['PM2']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth'] / 2))) - drc._NwMinEnclosurePactive)]]]
        XYList = []
        xy_offset = (0, ((((- (self._DesignParameter['NM1']['_XYCoordinates'][0][1] + self._DesignParameter['NM1']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1])) + ((self._DesignParameter['VSSRail']['_XYCoordinates'][0][1] + self._DesignParameter['VSSRail']['_DesignObj']._DesignParameter['_Met2Layer']['_XYCoordinates'][0][1]) + (self._DesignParameter['VSSRail']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] / 2))) + 98) + drc._MetalxMinSpace21))
        for i in range(
                len(self._DesignParameter['NM1']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'])):
            if (i % 2) == 1:
                XYList.append([((x + y) + z) for (x, y, z) in
                               zip([(0 + self._DesignParameter['NM1']['_XYCoordinates'][0][0]),
                                    (0 + self._DesignParameter['NM1']['_XYCoordinates'][0][1])],
                                   self._DesignParameter['NM1']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i], xy_offset)])
        self._DesignParameter['via1nmos'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='via1nmosIn{}'.format(_Name)))[0]
        self._DesignParameter['via1nmos']['_DesignObj']._CalculateDesignParameterSameEnclosure(
            **dict(_ViaMet12Met2NumberOfCOX=1, _ViaMet12Met2NumberOfCOY=2))
        self._DesignParameter['via1nmos']['_XYCoordinates'] = XYList
        XYList = []
        xy_offset = (0, ((((- self._DesignParameter['PM1']['_XYCoordinates'][0][1]) + ((self._DesignParameter['VDDRail']['_XYCoordinates'][0][1] + self._DesignParameter['VDDRail']['_DesignObj']._DesignParameter['_Met2Layer']['_XYCoordinates'][0][1]) - (self._DesignParameter['VDDRail']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] / 2))) - drc._MetalxMinSpace21) - 98))
        for i in range(
                len(self._DesignParameter['PM1']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'])):
            if (i % 2) == 1:
                XYList.append([((x + y) + z) for (x, y, z) in
                               zip([(0 + self._DesignParameter['PM1']['_XYCoordinates'][0][0]),
                                    (0 + self._DesignParameter['PM1']['_XYCoordinates'][0][1])],
                                   self._DesignParameter['PM1']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i], xy_offset)])
        self._DesignParameter['via1ForPM1'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='via1ForPM1In{}'.format(_Name)))[0]
        self._DesignParameter['via1ForPM1']['_DesignObj']._CalculateDesignParameterSameEnclosure(
            **dict(_ViaMet12Met2NumberOfCOX=1, _ViaMet12Met2NumberOfCOY=2))
        self._DesignParameter['via1ForPM1']['_XYCoordinates'] = XYList


        self._DesignParameter['XVTLayer'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping[XVT][0], _Datatype=DesignParameters._LayerMapping[XVT][1],
            _XWidth=self._DesignParameter['VSSRail']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth'],
            _YWidth=CellHeight)
        self._DesignParameter['XVTLayer']['_XYCoordinates'] = [[0, (CellHeight / 2)]]

        # Previous Code
        # XYList = []
        # xy_offset = (0, ((- self._DesignParameter['NM2']['_XYCoordinates'][0][1]) +
        #                  self._DesignParameter['via1nmos']['_XYCoordinates'][0][1]))
        # for i in range(
        #         len(self._DesignParameter['NM2']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'])):
        #     if ((i % 2) == 0):
        #         XYList.append([((x + y) + z) for (x, y, z) in
        #                        zip([(0 + self._DesignParameter['NM2']['_XYCoordinates'][0][0]),
        #                             (0 + self._DesignParameter['NM2']['_XYCoordinates'][0][1])],
        #                            self._DesignParameter['NM2']['_DesignObj']._DesignParameter['_Met1Layer'][
        #                                '_XYCoordinates'][i], xy_offset)])
        # self._DesignParameter['via1ForNM2'] = \
        # self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='via1ForNM2In{}'.format(_Name)))[0]
        # self._DesignParameter['via1ForNM2']['_DesignObj']._CalculateDesignParameterSameEnclosure(
        #     **dict(_ViaMet12Met2NumberOfCOX=1, _ViaMet12Met2NumberOfCOY=2))
        # self._DesignParameter['via1ForNM2']['_XYCoordinates'] = XYList
        # XYList = []
        # xy_offset = (0, ((- self._DesignParameter['PM2']['_XYCoordinates'][0][1]) +
        #                  self._DesignParameter['via1ForPM1']['_XYCoordinates'][0][1]))
        # for i in range(
        #         len(self._DesignParameter['PM2']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'])):
        #     if ((i % 2) == 0):
        #         XYList.append([((x + y) + z) for (x, y, z) in
        #                        zip([(0 + self._DesignParameter['PM2']['_XYCoordinates'][0][0]),
        #                             (0 + self._DesignParameter['PM2']['_XYCoordinates'][0][1])],
        #                            self._DesignParameter['PM2']['_DesignObj']._DesignParameter['_Met1Layer'][
        #                                '_XYCoordinates'][i], xy_offset)])
        # self._DesignParameter['via1ForPM2'] = \
        # self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='via1ForPM2In{}'.format(_Name)))[0]
        # self._DesignParameter['via1ForPM2']['_DesignObj']._CalculateDesignParameterSameEnclosure(
        #     **dict(_ViaMet12Met2NumberOfCOX=1, _ViaMet12Met2NumberOfCOY=2))
        # self._DesignParameter['via1ForPM2']['_XYCoordinates'] = XYList
        # self._DesignParameter['m2pathnm1nm2'] = self._PathElementDeclaration(
        #     _Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1],
        #     _Width=drc._MetalxMinWidth)
        # self._DesignParameter['m2pathnm1nm2']['_XYCoordinates'] = [[[(+self._DesignParameter['via1nmos'][
        #     '_XYCoordinates'][0][0]), (+ self._DesignParameter['via1nmos']['_XYCoordinates'][0][1])], [
        #                                                                 self._DesignParameter['via1ForNM2'][
        #                                                                     '_XYCoordinates'][(- 1)][0],
        #                                                                 self._DesignParameter['via1nmos'][
        #                                                                     '_XYCoordinates'][0][1]]]]
        ''' '''
        YWidth_Met1HorizontalRouting = 66
        self._DesignParameter['via1ForNM2'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='via1ForNM2In{}'.format(_Name)))[0]
        self._DesignParameter['via1ForNM2']['_DesignObj']._CalculateDesignParameterSameEnclosure(**dict(_ViaMet12Met2NumberOfCOX=1, _ViaMet12Met2NumberOfCOY=2))
        self._DesignParameter['via1ForPM2'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='via1ForPM2In{}'.format(_Name)))[0]
        self._DesignParameter['via1ForPM2']['_DesignObj']._CalculateDesignParameterSameEnclosure(**dict(_ViaMet12Met2NumberOfCOX=1, _ViaMet12Met2NumberOfCOY=2))

        self._DesignParameter['Met1RouteY_NMout'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1],
            _XWidth=self.getXWidth('NM2', '_Met1Layer'),
            _YWidth=drc._Metal1MinSpaceAtCorner + YWidth_Met1HorizontalRouting)
        self._DesignParameter['Met1RouteY_PMout'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1],
            _XWidth=self.getXWidth('PM2', '_Met1Layer'),
            _YWidth=drc._Metal1MinSpaceAtCorner + YWidth_Met1HorizontalRouting)

        tmpXYs_NMout = []
        tmpXYs_PMout = []
        tmpXYs_NMintermediate = []
        tmpXYs_PMintermediate = []
        for i in range(len(self.getXY('NM2', '_Met1Layer'))):
            if i % 2 == 0:  # output node
                tmpXYs_NMout.append([
                    self.getXY('NM2', '_Met1Layer')[NumFinger_NM2 - i][0],
                    self.getXY('NM2', '_Met1Layer')[0][1] + self.getYWidth('NM2', '_Met1Layer') / 2 + self.getYWidth('Met1RouteY_NMout') / 2
                ])
                tmpXYs_PMout.append([
                    self.getXY('NM2', '_Met1Layer')[NumFinger_NM2 - i][0],
                    self.getXY('PM2', '_Met1Layer')[0][1] - self.getYWidth('PM2', '_Met1Layer') / 2 - self.getYWidth('Met1RouteY_NMout') / 2
                ])
            else:  # intermediate node
                tmpXYs_NMintermediate.append([
                    self.getXY('NM2', '_Met1Layer')[NumFinger_NM2 - i][0],
                    self.getXY('via1nmos')[0][1]
                ])
                tmpXYs_PMintermediate.append([
                    self.getXY('NM2', '_Met1Layer')[NumFinger_NM2 - i][0],
                    self.getXY('via1ForPM1')[0][1]
                ])
        self._DesignParameter['via1ForNM2']['_XYCoordinates'] = tmpXYs_NMintermediate
        self._DesignParameter['via1ForPM2']['_XYCoordinates'] = tmpXYs_PMintermediate
        self._DesignParameter['Met1RouteY_NMout']['_XYCoordinates'] = tmpXYs_NMout
        self._DesignParameter['Met1RouteY_PMout']['_XYCoordinates'] = tmpXYs_PMout



        ''' '''
        RightBoundary_Met2RouteX = CoordCalc.getXYCoords_MaxX(self.getXY('via1ForPM1') + self.getXY('via1ForPM2'))[0][0]
        LeftBoundary_Met2RouteX = CoordCalc.getXYCoords_MinX(self.getXY('via1ForPM1') + self.getXY('via1ForPM2'))[0][0]

        self._DesignParameter['Met2RouteX_PM1PM2'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1],
            _XWidth=(RightBoundary_Met2RouteX - LeftBoundary_Met2RouteX),
            _YWidth=YWidth_Met1HorizontalRouting
        )
        self._DesignParameter['Met2RouteX_PM1PM2']['_XYCoordinates'] = [[
            (RightBoundary_Met2RouteX + LeftBoundary_Met2RouteX) / 2,
            self.getXY('via1ForPM2')[0][1]
        ]]

        self._DesignParameter['Met2RouteX_NM1NM2'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1],
            _XWidth=(RightBoundary_Met2RouteX - LeftBoundary_Met2RouteX),
            _YWidth=YWidth_Met1HorizontalRouting
        )
        self._DesignParameter['Met2RouteX_NM1NM2']['_XYCoordinates'] = [[
            (RightBoundary_Met2RouteX + LeftBoundary_Met2RouteX) / 2,
            self.getXY('via1ForNM2')[0][1]
        ]]

        RightBoundary_Met1XOut = CoordCalc.getXYCoords_MaxX(self.getXY('Met1RouteY_NMout') + self.getXY('Met1RouteY_NMout'))[0][0]
        LeftBoundary_Met1XOut = CoordCalc.getXYCoords_MinX(self.getXY('Met1RouteY_NMout') + self.getXY('Met1RouteY_NMout'))[0][0]

        self._DesignParameter['Met1RouteX_NMOut'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1],
            _XWidth=(RightBoundary_Met1XOut - LeftBoundary_Met1XOut) + self.getXWidth('Met1RouteY_NMout'),
            _YWidth=YWidth_Met1HorizontalRouting
        )
        self._DesignParameter['Met1RouteX_NMOut']['_XYCoordinates'] = [[
            (RightBoundary_Met1XOut + LeftBoundary_Met1XOut) / 2,
            self.getXY('Met1RouteY_NMout')[0][1] + self.getYWidth('Met1RouteY_NMout') / 2 - self.getYWidth('Met1RouteX_NMOut') / 2
        ]]

        self._DesignParameter['Met1RouteX_PMOut'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1],
            _XWidth=(RightBoundary_Met1XOut - LeftBoundary_Met1XOut) + self.getXWidth('Met1RouteY_PMout'),
            _YWidth=YWidth_Met1HorizontalRouting
        )
        self._DesignParameter['Met1RouteX_PMOut']['_XYCoordinates'] = [[
            (RightBoundary_Met1XOut + LeftBoundary_Met1XOut) / 2,
            self.getXY('Met1RouteY_PMout')[0][1] - self.getYWidth('Met1RouteY_PMout') / 2 + self.getYWidth('Met1RouteX_PMOut') / 2
        ]]

        TopBoundary_Met1YOut = (self.getXY('Met1RouteX_PMOut')[0][1] - self.getYWidth('Met1RouteX_PMOut') / 2)
        BotBoundary_Met1YOut = (self.getXY('Met1RouteX_NMOut')[0][1] + self.getYWidth('Met1RouteX_NMOut') / 2)
        XWidth_Met1YOut = self.getXWidth('Met1RouteY_PMout') * (len(self.getXY('Met1RouteY_PMout')) // 2)

        self._DesignParameter['Met1RouteY_Out'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1],
            _XWidth=XWidth_Met1YOut,
            _YWidth=TopBoundary_Met1YOut - BotBoundary_Met1YOut
        )
        self._DesignParameter['Met1RouteY_Out']['_XYCoordinates'] = [[
            self.getXY('NM2', '_Met1Layer')[-1][0] + self.getXWidth('NM2', '_Met1Layer') / 2 - self.getXWidth('Met1RouteY_Out') / 2,
            (TopBoundary_Met1YOut + BotBoundary_Met1YOut) / 2
        ]]

        RightBoudary_InputViaA = self.getXY('Met1RouteY_Out')[0][0] - self.getXWidth('Met1RouteY_Out') / 2 - drc._Metal1MinSpaceAtCorner - drc._Metal1MinEnclosureCO2
        LeftBoudary_InputViaA = self.getXY('NM2', '_POLayer')[0][0] - self.getXWidth('NM2', '_POLayer') / 2 + drc._CoMinEnclosureByPOAtLeastTwoSide
        NumViaX_InputA = int((RightBoudary_InputViaA - LeftBoudary_InputViaA - drc._CoMinWidth) // (drc._CoMinWidth + drc._CoMinSpace) + 1)
        # NumViaX_InputA = int((((((((self._DesignParameter['NM2']['_XYCoordinates'][0][0] + self._DesignParameter['NM2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0])
        #                            + (self._DesignParameter['NM2']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)) - ((self._DesignParameter['NM2']['_XYCoordinates'][
        #                                                                     0][0] + self._DesignParameter['NM2'][
        #                                                                     '_DesignObj']._DesignParameter['_POLayer'][
        #                                                                     '_XYCoordinates'][0][0]) - (
        #                                                                            self._DesignParameter['NM2'][
        #                                                                                '_DesignObj']._DesignParameter[
        #                                                                                '_POLayer']['_XWidth'] / 2))) - (
        #                                      2 * drc._CoMinEnclosureByODAtLeastTwoSide)) - drc._CoMinWidth) // (
        #                                    drc._CoMinWidth + drc._CoMinSpace)) + 1))

        self._DesignParameter['polyInputA'] = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_Name='polyInputAIn{}'.format(_Name)))[0]
        self._DesignParameter['polyInputA']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(
            **dict(_ViaPoly2Met1NumberOfCOX=NumViaX_InputA, _ViaPoly2Met1NumberOfCOY=NumViaY_InputA))
        self._DesignParameter['polyInputA']['_XYCoordinates'] = [
            [(RightBoudary_InputViaA + LeftBoudary_InputViaA) / 2, YCoord_InputA]
        ]
        self._DesignParameter['PolyX_M2'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1],
            _XWidth=(((self._DesignParameter['NM2']['_XYCoordinates'][0][0] +
                       self._DesignParameter['NM2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0])
                      + (self._DesignParameter['NM2']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2))
                     - ((self._DesignParameter['NM2']['_XYCoordinates'][0][0] +
                         self._DesignParameter['NM2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['NM2']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2))),
            _YWidth=self._DesignParameter['polyInputA']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'])
        self._DesignParameter['PolyX_M2']['_XYCoordinates'] = [
            [(+ self._DesignParameter['NM2']['_XYCoordinates'][0][0]),
             (+ self._DesignParameter['polyInputA']['_XYCoordinates'][0][1])]
        ]

