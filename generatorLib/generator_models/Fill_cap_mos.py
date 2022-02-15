from generatorLib import StickDiagram
from generatorLib import DesignParameters
import copy
import math
from generatorLib import DRC

class FILLCAP_5X_STD_RVT_v2(StickDiagram._StickDiagram):
	def __init__(self, _DesignParameter=None, _Name='FILLCAP_5X_STD_RVT_v2'):
		if _DesignParameter != None:
			self._DesignParameter = _DesignParameter
		else:
			self._DesignParameter = dict(_Name=self._NameDeclaration(_Name=_Name), _GDSFile=self._GDSObjDeclaration(_GDSFile=None))
		self._DesignParameter['_Name']['Name'] = _Name

	def _CalculateDesignParameter(self,gate_x_length=600,gate_y_width=200,Dummy_width=40,pmos_flag=1):
	
		drc = DRC.DRC()
		_Name = self._DesignParameter['_Name']['_Name']
		_XYCoordinateofR = [[0, 0]]


		##poly gate
		self._DesignParameter['N_poly'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _XWidth=gate_x_length, _YWidth=((drc._PolylayeroverOd2 * 2) + gate_y_width))
		self._DesignParameter['N_poly']['_XYCoordinates'] = [[0.0, 0.0]]

		##CONT layer
		_CoYNumMax = int((gate_y_width - drc._CoMinEnclosureByOD * 2 - drc._CoMinWidth) // (drc._CoMinWidth + drc._CoMinSpace)) + 1
		tmpdistance = drc._CoMinSpace + drc._CoMinWidth

		self._DesignParameter['_Contact']=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['CONT'][0], _Datatype=DesignParameters._LayerMapping['CONT'][1], _XWidth=None, _YWidth=None, _XYCoordinates=[])
		self._DesignParameter['_Contact']['_XWidth'] = drc._CoMinWidth
		self._DesignParameter['_Contact']['_YWidth'] = drc._CoMinWidth

		self._DesignParameter['_Contact2']=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['CONT'][0], _Datatype=DesignParameters._LayerMapping['CONT'][1], _XWidth=None, _YWidth=None, _XYCoordinates=[])
		self._DesignParameter['_Contact2']['_XWidth'] = drc._CoMinWidth
		self._DesignParameter['_Contact2']['_YWidth'] = drc._CoMinWidth

		tmp = []
		tmp2 = []
		for i in range(0, _CoYNumMax) :
			tmp.append([_XYCoordinateofR[0][0] - self._DesignParameter['N_poly']['_XWidth']/2 - drc._PolygateMinSpace2Co2 - drc._CoMinWidth/2,
						_XYCoordinateofR[0][1] + (_CoYNumMax-1)/2 * tmpdistance - i * tmpdistance])
			tmp2.append([_XYCoordinateofR[0][0] + self._DesignParameter['N_poly']['_XWidth']/2 + drc._PolygateMinSpace2Co2 + drc._CoMinWidth/2,
						_XYCoordinateofR[0][1] + (_CoYNumMax-1)/2 * tmpdistance - i * tmpdistance])

		self._DesignParameter['_Contact']['_XYCoordinates'] = tmp
		self._DesignParameter['_Contact2']['_XYCoordinates'] = tmp2

		del tmp
		del tmp2

		##active region
		self._DesignParameter['DIFF_boundary_2'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['DIFF'][0], _Datatype=DesignParameters._LayerMapping['DIFF'][1],
																					_XWidth=self._DesignParameter['N_poly']['_XWidth'] + drc._PolygateMinSpace2Co2*2 + drc._CoMinWidth + drc._CoMinWidth + 2*drc._CoMinEnclosureByOD,
																					_YWidth=gate_y_width)
		self._DesignParameter['DIFF_boundary_2']['_XYCoordinates'] = [[0.0, 0.0]]

		##M1 layer
		self._DesignParameter['_Met1Layer'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0],
													  _Datatype=DesignParameters._LayerMapping['METAL1'][1])
		self._DesignParameter['_Met1Layer']['_XWidth'] = drc._CoMinWidth + drc._Metal1MinEnclosureCO * 2 # Check drc
		self._DesignParameter['_Met1Layer']['_YWidth'] = (_CoYNumMax - 1) * (drc._CoMinWidth + drc._CoMinSpace) + drc._CoMinWidth + drc._Metal1MinEnclosureCO2 * 2 # Check drc

		self._DesignParameter['_Met1Layer_2'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0],
													  _Datatype=DesignParameters._LayerMapping['METAL1'][1])
		self._DesignParameter['_Met1Layer_2']['_XWidth'] = drc._CoMinWidth + drc._Metal1MinEnclosureCO * 2 # Check drc
		self._DesignParameter['_Met1Layer_2']['_YWidth'] = (_CoYNumMax - 1) * (drc._CoMinWidth + drc._CoMinSpace) + drc._CoMinWidth + drc._Metal1MinEnclosureCO2 * 2 # Check drc

		self._DesignParameter['_Met1Layer']['_XYCoordinates'] = [[self._DesignParameter['_Contact']['_XYCoordinates'][0][0],
																  (self._DesignParameter['_Contact']['_XYCoordinates'][0][1]+self._DesignParameter['_Contact']['_XYCoordinates'][-1][1])/2]]

		self._DesignParameter['_Met1Layer_2']['_XYCoordinates'] = [[self._DesignParameter['_Contact2']['_XYCoordinates'][1][0],
		 														  (self._DesignParameter['_Contact2']['_XYCoordinates'][0][1] + self._DesignParameter['_Contact2']['_XYCoordinates'][-1][1])/2]]

		##RVT layer
		self._DesignParameter['XVT'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['RVT'][0], _Datatype=DesignParameters._LayerMapping['RVT'][1])
		self._DesignParameter['XVT']['_XWidth'] = self._DesignParameter['DIFF_boundary_2']['_XWidth'] + 2 * drc._XvtMinExtensionOnOD
		self._DesignParameter['XVT']['_YWidth'] = self._DesignParameter['DIFF_boundary_2']['_YWidth'] + 2 * drc._XvtMinExtensionOnOD
		self._DesignParameter['XVT']['_XYCoordinates'] = self._DesignParameter['N_poly']['_XYCoordinates']

		##PMOS setting
		if pmos_flag == 1 :

			##PIMP layer
			self._DesignParameter['PIMP'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['PIMP'][0], _Datatype=DesignParameters._LayerMapping['PIMP'][1])
			self._DesignParameter['PIMP']['_XWidth'] = self._DesignParameter['DIFF_boundary_2']['_XWidth'] + 2 * drc._PpMinExtensiononPactive
			self._DesignParameter['PIMP']['_YWidth'] = self._DesignParameter['DIFF_boundary_2']['_YWidth'] + 2 * drc._PpMinExtensiononPactive
			self._DesignParameter['PIMP']['_XYCoordinates'] = self._DesignParameter['N_poly']['_XYCoordinates']
			## NWELL layer
			self._DesignParameter['NWELL'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['NWELL'][0], _Datatype=DesignParameters._LayerMapping['NWELL'][1])
			self._DesignParameter['NWELL']['_XWidth'] = self._DesignParameter['DIFF_boundary_2']['_XWidth'] + 2 * drc._NwMinEnclosurePactive2
			self._DesignParameter['NWELL']['_YWidth'] = self._DesignParameter['DIFF_boundary_2']['_YWidth'] + 2 * drc._NwMinEnclosurePactive2
			self._DesignParameter['NWELL']['_XYCoordinates'] = self._DesignParameter['DIFF_boundary_2']['_XYCoordinates']

			##poly dummy for pmos
			self._DesignParameter['POLY_boundary'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _XWidth=Dummy_width)
			self._DesignParameter['POLY_boundary']['_YWidth'] = self._DesignParameter['DIFF_boundary_2']['_YWidth']
			self._DesignParameter['POLY_boundary2'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _XWidth=Dummy_width)
			self._DesignParameter['POLY_boundary2']['_YWidth'] = self._DesignParameter['DIFF_boundary_2']['_YWidth']

			if float(self._DesignParameter['POLY_boundary']['_XWidth']) * float(self._DesignParameter['POLY_boundary']['_YWidth']) < drc._PODummyMinArea:
				self._DesignParameter['POLY_boundary']['_YWidth'] = self.CeilMinSnapSpacing(float(drc._PODummyMinArea) / float(self._DesignParameter['POLY_boundary']['_XWidth']), drc._MinSnapSpacing * 2)
				self._DesignParameter['POLY_boundary2']['_YWidth'] = self.CeilMinSnapSpacing(float(drc._PODummyMinArea) / float(self._DesignParameter['POLY_boundary2']['_XWidth']), drc._MinSnapSpacing * 2)

			else:
				pass

			Dummy_height = self._DesignParameter['POLY_boundary']['_YWidth']
			self._DesignParameter['POLY_boundary']['_XYCoordinates'] = [[(((self._DesignParameter['N_poly']['_XYCoordinates'][0][0] - (self._DesignParameter['N_poly']['_XWidth'] / 2)) - drc._PolygateMinSpace2) - (Dummy_width / 2)),
																		 ((self._DesignParameter['DIFF_boundary_2']['_XYCoordinates'][0][1] - (self._DesignParameter['DIFF_boundary_2']['_YWidth'] / 2)) + (Dummy_height / 2))]]
			self._DesignParameter['POLY_boundary2']['_XYCoordinates'] = [[(((self._DesignParameter['N_poly']['_XYCoordinates'][0][0] + (self._DesignParameter['N_poly']['_XWidth'] / 2)) + drc._PolygateMinSpace2) + (Dummy_width / 2)),
			 															 ((self._DesignParameter['DIFF_boundary_2']['_XYCoordinates'][0][1] - (self._DesignParameter['DIFF_boundary_2']['_YWidth'] / 2)) + (Dummy_height / 2))]]

		else :

			##poly dummy for nmos
			self._DesignParameter['POLY_boundary'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _XWidth=Dummy_width)
			self._DesignParameter['POLY_boundary']['_YWidth'] = self._DesignParameter['DIFF_boundary_2']['_YWidth']
			self._DesignParameter['POLY_boundary2'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _XWidth=Dummy_width)
			self._DesignParameter['POLY_boundary2']['_YWidth'] = self._DesignParameter['DIFF_boundary_2']['_YWidth']

			if float(self._DesignParameter['POLY_boundary']['_XWidth']) * float(self._DesignParameter['POLY_boundary']['_YWidth']) < drc._PODummyMinArea:
				self._DesignParameter['POLY_boundary']['_YWidth'] = self.CeilMinSnapSpacing(float(drc._PODummyMinArea) / float(self._DesignParameter['POLY_boundary']['_XWidth']), drc._MinSnapSpacing * 2)
				self._DesignParameter['POLY_boundary2']['_YWidth'] = self.CeilMinSnapSpacing(float(drc._PODummyMinArea) / float(self._DesignParameter['POLY_boundary2']['_XWidth']), drc._MinSnapSpacing * 2)

			else:
				pass

			Dummy_height = self._DesignParameter['POLY_boundary']['_YWidth']
			self._DesignParameter['POLY_boundary']['_XYCoordinates'] = [[(((self._DesignParameter['N_poly']['_XYCoordinates'][0][0] - (self._DesignParameter['N_poly']['_XWidth'] / 2)) - drc._PolygateMinSpace2) - (Dummy_width / 2)),
																		 ((self._DesignParameter['DIFF_boundary_2']['_XYCoordinates'][0][1] + (self._DesignParameter['DIFF_boundary_2']['_YWidth'] / 2)) - (Dummy_height / 2))]]
			self._DesignParameter['POLY_boundary2']['_XYCoordinates'] = [[(((self._DesignParameter['N_poly']['_XYCoordinates'][0][0] + (self._DesignParameter['N_poly']['_XWidth'] / 2)) + drc._PolygateMinSpace2) + (Dummy_width / 2)),
																		 ((self._DesignParameter['DIFF_boundary_2']['_XYCoordinates'][0][1] + (self._DesignParameter['DIFF_boundary_2']['_YWidth'] / 2)) - (Dummy_height / 2))]]