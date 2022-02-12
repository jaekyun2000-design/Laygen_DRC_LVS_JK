from generatorLib import StickDiagram
from generatorLib import DesignParameters
import copy
import math
from generatorLib import DRC

class opppcres_b_CDNS_6377410485842(StickDiagram._StickDiagram):
	def __init__(self, _DesignParameter=None, _Name='opppcres_b_CDNS_6377410485842'):
		if _DesignParameter != None:
			self._DesignParameter = _DesignParameter
		else:
			self._DesignParameter = dict(_Name=self._NameDeclaration(_Name=_Name), _GDSFile=self._GDSObjDeclaration(_GDSFile=None))
		self._DesignParameter['_Name']['Name'] = _Name

	def _CalculateDesignParameter(self,R_X_width=2500, R_Y_length=1500, _CoXNum=None, _CoYNum=None):
	
		drc = DRC.DRC()
		_Name = self._DesignParameter['_Name']['_Name']
		_XYCoordinateofR = [[0,0]]


		self._DesignParameter['_Contact']=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['CONT'][0], _Datatype=DesignParameters._LayerMapping['CONT'][1], _XWidth=None, _YWidth=None, _XYCoordinates=[])
		self._DesignParameter['_Contact']['_XWidth'] = drc._CoMinWidth
		self._DesignParameter['_Contact']['_YWidth'] = drc._CoMinWidth

		_CoXNumMax = int((R_X_width - drc._CoMinEnclosureByPO2 * 2 - drc._CoMinWidth) // (drc._CoMinWidth + drc._CoMinSpace)) + 1

		tmpdistance = drc._CoMinSpace + drc._CoMinWidth


		if _CoXNum == None:
			_CoXNum = _CoXNumMax
		if _CoYNum == None:
			_CoYNum = 1

		if _CoXNum > _CoXNumMax:
			raise NotImplementedError

		tmp = []
		for i in range(0, _CoXNum) :
			for j in range(0, _CoYNum) :
				tmp.append([_XYCoordinateofR[0][0] - (_CoXNum-1)/2 * tmpdistance + i * tmpdistance,
							_XYCoordinateofR[0][1] + R_Y_length/2 + drc._CoMinSpace2OP + 0.5 * drc._CoMinWidth + j * tmpdistance])
				tmp.append([_XYCoordinateofR[0][0] - (_CoXNum-1)/2 * tmpdistance + i * tmpdistance,
							_XYCoordinateofR[0][1] - R_Y_length/2 - drc._CoMinSpace2OP - 0.5 * drc._CoMinWidth - j * tmpdistance])

		self._DesignParameter['_Contact']['_XYCoordinates'] = tmp

		del tmp

		self._DesignParameter['POLY_boundary_0'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _XWidth=R_X_width, _YWidth=((drc._PolyoverOPlayer * 2) + R_Y_length))
		self._DesignParameter['POLY_boundary_0']['_XYCoordinates'] = _XYCoordinateofR
		self._DesignParameter['OP_boundary_0'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['OP'][0], _Datatype=DesignParameters._LayerMapping['OP'][1], _XWidth=((drc._OPlayeroverPoly * 2) + R_X_width), _YWidth=R_Y_length)
		self._DesignParameter['OP_boundary_0']['_XYCoordinates'] = _XYCoordinateofR

		self._DesignParameter['POLY_boundary_1'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _XWidth=R_X_width, _YWidth=(drc._CoMinWidth + (_CoYNum-1) * tmpdistance + drc._CoMinEnclosureByPO2 * 2))
		self._DesignParameter['POLY_boundary_1']['_XYCoordinates'] = [[_XYCoordinateofR[0][0], _XYCoordinateofR[0][1] + R_Y_length/2 + drc._CoMinSpace2OP + 0.5 * drc._CoMinWidth + (_CoYNum-1)/2 * tmpdistance]]

		self._DesignParameter['POLY_boundary_2'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _XWidth=R_X_width, _YWidth=(drc._CoMinWidth + (_CoYNum-1) * tmpdistance + drc._CoMinEnclosureByPO2 * 2))
		self._DesignParameter['POLY_boundary_2']['_XYCoordinates'] = [[_XYCoordinateofR[0][0], _XYCoordinateofR[0][1] - R_Y_length/2 - drc._CoMinSpace2OP - 0.5 * drc._CoMinWidth - (_CoYNum-1)/2 * tmpdistance]]

		CONT_POLY_height = R_Y_length + drc._CoMinSpace2OP * 2 + drc._CoMinWidth + (_CoYNum-1) * tmpdistance + self._DesignParameter['POLY_boundary_1']['_YWidth']

		if CONT_POLY_height < self._DesignParameter['POLY_boundary_0']['_YWidth'] :
			self._DesignParameter['PRES_boundary_0'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['PRES'][0], _Datatype=DesignParameters._LayerMapping['PRES'][1], _XWidth=((drc._PRESlayeroverPoly * 2) + self._DesignParameter['POLY_boundary_0']['_XWidth']), _YWidth= (self._DesignParameter['POLY_boundary_0']['_YWidth'] + drc._PRESlayeroverPoly * 2))
			self._DesignParameter['PRES_boundary_0']['_XYCoordinates'] = _XYCoordinateofR
		else :
			self._DesignParameter['PRES_boundary_0'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['PRES'][0], _Datatype=DesignParameters._LayerMapping['PRES'][1], _XWidth=((drc._PRESlayeroverPoly * 2) + self._DesignParameter['POLY_boundary_0']['_XWidth']), _YWidth= CONT_POLY_height + drc._PRESlayeroverPoly * 2)
			self._DesignParameter['PRES_boundary_0']['_XYCoordinates'] = _XYCoordinateofR

		self._DesignParameter['PIMP_boundary_0'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['PIMP'][0], _Datatype=DesignParameters._LayerMapping['PIMP'][1], _XWidth=self._DesignParameter['PRES_boundary_0']['_XWidth'], _YWidth=self._DesignParameter['PRES_boundary_0']['_YWidth'])
		self._DesignParameter['PIMP_boundary_0']['_XYCoordinates'] = _XYCoordinateofR

		self._DesignParameter['_Met1Layer'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0],
													  _Datatype=DesignParameters._LayerMapping['METAL1'][1],
													  _XYCoordinates=[], _XWidth=400, _YWidth=400)

		print(
			'#############################     Metal1 Layer Calculation    #############################################')

		self._DesignParameter['_Met1Layer']['_XWidth'] = (_CoXNum - 1) * (drc._CoMinWidth + drc._CoMinSpace) + drc._CoMinWidth + drc._Metal1MinEnclosureCO2 * 2 # Check drc
		self._DesignParameter['_Met1Layer']['_YWidth'] = (_CoYNum - 1) * (drc._CoMinWidth + drc._CoMinSpace) + drc._CoMinWidth + drc._Metal1MinEnclosureCO2 * 2 # Check drc
		self._DesignParameter['_Met1Layer']['_XYCoordinates'] = [self._DesignParameter['POLY_boundary_1']['_XYCoordinates'][0], self._DesignParameter['POLY_boundary_2']['_XYCoordinates'][0]]
		del tmpdistance