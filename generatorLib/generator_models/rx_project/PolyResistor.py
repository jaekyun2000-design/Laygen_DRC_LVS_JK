from generatorLib import StickDiagram
from generatorLib import DesignParameters
import copy
import math
from generatorLib import DRC
from generatorLib.generator_models.rx_project import ViaPoly2Met1

class OpppcresInResistorBank_0(StickDiagram._StickDiagram):
	def __init__(self, _DesignParameter=None, _Name='OpppcresInResistorBank_0'):
		if _DesignParameter != None:
			self._DesignParameter = _DesignParameter
		else:
			self._DesignParameter = dict(_Name=self._NameDeclaration(_Name=_Name), _GDSFile=self._GDSObjDeclaration(_GDSFile=None))
		self._DesignParameter['_Name']['Name'] = _Name

	def _CalculateDesignParameter(self,width=1250,height=1234,contact=2):
	
		drc = DRC.DRC()
		_Name = self._DesignParameter['_Name']['_Name']
		
		self._DesignParameter['OP_boundary_0'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['OP'][0], _Datatype=DesignParameters._LayerMapping['OP'][1], _XWidth=((drc._OPMinspace * 2) + width), _YWidth=height)
		self._DesignParameter['OP_boundary_0']['_XYCoordinates'] = [[0.0, 0.0]]
		self._DesignParameter['POLY_boundary_0'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _XWidth=width, _YWidth=((self._DesignParameter['OP_boundary_0']['_YWidth'] + drc._PolyoverOPlayer) + drc._PolyoverOPlayer))
		self._DesignParameter['POLY_boundary_0']['_XYCoordinates'] = [[0.0, 0.0]]
		self._DesignParameter['PIMP_boundary_0'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['PIMP'][0], _Datatype=DesignParameters._LayerMapping['PIMP'][1], _XWidth=((2 * drc._PRESlayeroverPoly) + self._DesignParameter['POLY_boundary_0']['_XWidth']), _YWidth=(self._DesignParameter['POLY_boundary_0']['_YWidth'] + (drc._PRESlayeroverPoly * 2)))
		self._DesignParameter['PIMP_boundary_0']['_XYCoordinates'] = [[0.0, 0.0]]
		self._DesignParameter['PRES_boundary_0'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['PRES'][0], _Datatype=DesignParameters._LayerMapping['PRES'][1], _XWidth=self._DesignParameter['PIMP_boundary_0']['_XWidth'], _YWidth=self._DesignParameter['PIMP_boundary_0']['_YWidth'])
		self._DesignParameter['PRES_boundary_0']['_XYCoordinates'] = [[0.0, 0.0]]
		self._DesignParameter['bot_contact'] = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_Name='bot_contactIn{}'.format(_Name)))[0]
		self._DesignParameter['bot_contact']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(**dict(_ViaPoly2Met1NumberOfCOY=contact, _ViaPoly2Met1NumberOfCOX=max(1, (1 + int((((self._DesignParameter['POLY_boundary_0']['_XWidth'] - drc._CoMinSpace) - (2 * drc._CoMinEnclosureByPO)) / (drc._CoMinWidth + drc._CoMinSpace)))))))
		self._DesignParameter['bot_contact']['_XYCoordinates'] = [[self._DesignParameter['OP_boundary_0']['_XYCoordinates'][0][0], (((self._DesignParameter['OP_boundary_0']['_XYCoordinates'][0][1] - (self._DesignParameter['OP_boundary_0']['_YWidth'] / 2)) - drc._CoMinSpace2OP) + (- (self._DesignParameter['bot_contact']['_DesignObj']._DesignParameter['_COLayer']['_XYCoordinates'][(- 1)][1] + (self._DesignParameter['bot_contact']['_DesignObj']._DesignParameter['_COLayer']['_YWidth'] / 2))))]]
		self._DesignParameter['top_contact'] = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_Name='top_contactIn{}'.format(_Name)))[0]
		self._DesignParameter['top_contact']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(**dict(_ViaPoly2Met1NumberOfCOX=max(1, (1 + int((((self._DesignParameter['POLY_boundary_0']['_XWidth'] - drc._CoMinSpace) - (2 * drc._CoMinEnclosureByPO)) / (drc._CoMinWidth + drc._CoMinSpace))))), _ViaPoly2Met1NumberOfCOY=contact))
		self._DesignParameter['top_contact']['_XYCoordinates'] = [[self._DesignParameter['OP_boundary_0']['_XYCoordinates'][0][0], (((self._DesignParameter['OP_boundary_0']['_XYCoordinates'][0][1] + (self._DesignParameter['OP_boundary_0']['_YWidth'] / 2)) + drc._CoMinSpace2OP) + (- (self._DesignParameter['top_contact']['_DesignObj']._DesignParameter['_COLayer']['_XYCoordinates'][0][1] - (self._DesignParameter['top_contact']['_DesignObj']._DesignParameter['_COLayer']['_YWidth'] / 2))))]]
		