from generatorLib import StickDiagram
from generatorLib import DesignParameters
import copy
import math
from generatorLib import DRC

class Z_PWR_CNT(StickDiagram._StickDiagram):
	_ParametersForDesignCalculation = dict(_Xnum=None, _Xdistance=None)

	def __init__(self, _DesignParameter=None, _Name='Z_PWR_CNT'):
		if _DesignParameter != None:
			self._DesignParameter = _DesignParameter
		else:
			self._DesignParameter = dict(_Name=self._NameDeclaration(_Name=_Name), _GDSFile=self._GDSObjDeclaration(_GDSFile=None))
		self._DesignParameter['_Name']['Name'] = _Name

	def _CalculateDesignParameter(self, _Xnum=None, _Xdistance=None):
	
		drc = DRC.DRC()
		_Name = self._DesignParameter['_Name']['_Name']

		center = [[0,0]]
		self._DesignParameter['CONT_boundary_0'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['CONT'][0], _Datatype=DesignParameters._LayerMapping['CONT'][1], _XWidth=40, _YWidth=40)
		#self._DesignParameter['CONT_boundary_0']['_XYCoordinates'] = [[0.0, 0.0]]
		self._DesignParameter['METAL1_boundary_0'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _XWidth=66, _YWidth=152)
		#self._DesignParameter['METAL1_boundary_0']['_XYCoordinates'] = [[0.0, 0.0]]
		self._DesignParameter['METAL1_boundary_1'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _XWidth=66, _YWidth=80)
		#self._DesignParameter['METAL1_boundary_1']['_XYCoordinates'] = [[0.0, 0.0]]
		self._DesignParameter['VIA12_boundary_0'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['VIA12'][0], _Datatype=DesignParameters._LayerMapping['VIA12'][1], _XWidth=50, _YWidth=100)
		#self._DesignParameter['VIA12_boundary_0']['_XYCoordinates'] = [[0.0, 0.0]]
		self._DesignParameter['DIFF_boundary_0'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['DIFF'][0], _Datatype=DesignParameters._LayerMapping['DIFF'][1], _XWidth=66, _YWidth=80)
		#self._DesignParameter['DIFF_boundary_0']['_XYCoordinates'] = [[0.0, 0.0]]
		self._DesignParameter['METAL2_boundary_0'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _XWidth=66, _YWidth=152)
		#self._DesignParameter['METAL2_boundary_0']['_XYCoordinates'] = [[0.0, 0.0]]

		tmp = []
		for i in range(_Xnum) :
			tmp.append([center[0][0] - (_Xnum-1) / 2 * _Xdistance + i * _Xdistance, center[0][1]])

		self._DesignParameter['CONT_boundary_0']['_XYCoordinates'] = tmp
		self._DesignParameter['METAL1_boundary_0']['_XYCoordinates'] = tmp
		self._DesignParameter['METAL1_boundary_1']['_XYCoordinates'] = tmp
		self._DesignParameter['VIA12_boundary_0']['_XYCoordinates'] = tmp
		self._DesignParameter['DIFF_boundary_0']['_XYCoordinates'] = tmp
		self._DesignParameter['METAL2_boundary_0']['_XYCoordinates'] = tmp

		del tmp