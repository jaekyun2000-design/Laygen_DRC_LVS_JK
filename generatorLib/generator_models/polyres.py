from generatorLib import StickDiagram
from generatorLib import DesignParameters
import copy
from generatorLib import DRC
from generatorLib.generator_models import ViaPoly2Met1

class PolyResWithOD(StickDiagram._StickDiagram):
	def __init__(self, _DesignParameter=None, _Name='poly_res_od'):
		if _DesignParameter != None:
			self._DesignParameter = _DesignParameter
		else:
			self._DesignParameter = dict(_Name=self._NameDeclaration(_Name=_Name), _GDSFile=self._GDSObjDeclaration(_GDSFile=None))
		self._DesignParameter['_Name']['Name'] = _Name

	def _CalculateDesignParameter(self,res_length=800,res_width=400,contact_y=2):
	
		drc = DRC.DRC()
		_Name = self._DesignParameter['_Name']['_Name']
		
		self._DesignParameter['OP_boundary_0'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['OP'][0], _Datatype=DesignParameters._LayerMapping['OP'][1], _XWidth=(((drc._OPlayeroverPoly * 2) + res_width) + 0), _YWidth=res_length)
		self._DesignParameter['OP_boundary_0']['_XYCoordinates'] = [[0.0, 0.0]]
		self._DesignParameter['POLY_boundary_48'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _XWidth=res_width, _YWidth=((0 + self._DesignParameter['OP_boundary_0']['_YWidth']) + (2 * drc._PolyoverOPlayer)))
		self._DesignParameter['POLY_boundary_48']['_XYCoordinates'] = [[0.0, 0.0]]
		self._DesignParameter['PRES_boundary_0'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['PRES'][0], _Datatype=DesignParameters._LayerMapping['PRES'][1], _XWidth=(((drc._PRESlayeroverPoly * 2) + self._DesignParameter['POLY_boundary_48']['_XWidth']) + 0), _YWidth=((0 + (drc._PRESlayeroverPoly * 2)) + self._DesignParameter['POLY_boundary_48']['_YWidth']))
		self._DesignParameter['PRES_boundary_0']['_XYCoordinates'] = [[0.0, 0.0]]
		self._DesignParameter['rectarray_CDNS_6330718089180_1'] = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_Name='rectarray_CDNS_6330718089180_1In{}'.format(_Name)))[0]
		self._DesignParameter['rectarray_CDNS_6330718089180_1']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(**dict(_ViaPoly2Met1NumberOfCOX=(int((((res_width + drc._CoMinSpace2) - (2 * drc._CoMinEnclosureByPOAtLeastTwoSide)) / (drc._CoMinWidth + drc._CoMinSpace2))) + 0), _ViaPoly2Met1NumberOfCOY=contact_y))
		self._DesignParameter['rectarray_CDNS_6330718089180_1']['_XYCoordinates'] = [[(0 + self._DesignParameter['OP_boundary_0']['_XYCoordinates'][0][0]), (((((0 + self._DesignParameter['OP_boundary_0']['_XYCoordinates'][0][1]) + (((- (drc._CoMinSpace2 + drc._CoMinWidth)) / 2) * (contact_y - 1))) + (- drc._CoMinSpace2OP)) + ((- drc._CoMinWidth) / 2)) + ((- self._DesignParameter['OP_boundary_0']['_YWidth']) / 2))]]
		self._DesignParameter['rectarray_CDNS_6330718089180_0'] = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_Name='rectarray_CDNS_6330718089180_0In{}'.format(_Name)))[0]
		self._DesignParameter['rectarray_CDNS_6330718089180_0']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(**dict(_ViaPoly2Met1NumberOfCOX=(int((((res_width + drc._CoMinSpace2) - (2 * drc._CoMinEnclosureByPOAtLeastTwoSide)) / (drc._CoMinWidth + drc._CoMinSpace2))) + 0), _ViaPoly2Met1NumberOfCOY=contact_y))
		self._DesignParameter['rectarray_CDNS_6330718089180_0']['_XYCoordinates'] = [[(0 + self._DesignParameter['OP_boundary_0']['_XYCoordinates'][0][0]), (((((0 + self._DesignParameter['OP_boundary_0']['_XYCoordinates'][0][1]) + drc._CoMinSpace2OP) + (drc._CoMinWidth / 2)) + (self._DesignParameter['OP_boundary_0']['_YWidth'] / 2)) + (((drc._CoMinSpace + drc._CoMinWidth) / 2) * (contact_y - 1)))]]
		self._DesignParameter['PIMP_boundary_5'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['PIMP'][0], _Datatype=DesignParameters._LayerMapping['PIMP'][1], _XWidth=(self._DesignParameter['PRES_boundary_0']['_XWidth'] + 0), _YWidth=(0 + self._DesignParameter['PRES_boundary_0']['_YWidth']))
		self._DesignParameter['PIMP_boundary_5']['_XYCoordinates'] = [[0.0, 0.0]]
		