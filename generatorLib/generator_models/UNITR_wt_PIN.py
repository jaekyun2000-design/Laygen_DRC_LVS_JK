from generatorLib import StickDiagram
from generatorLib import DesignParameters
import copy
import math
from generatorLib import DRC
from generatorLib.generator_models import opppcres_b_CDNS_6377410485842

class UNITR_wt_PIN(StickDiagram._StickDiagram):
	def __init__(self, _DesignParameter=None, _Name='UNITR_wt_PIN'):
		if _DesignParameter != None:
			self._DesignParameter = _DesignParameter
		else:
			self._DesignParameter = dict(_Name=self._NameDeclaration(_Name=_Name), _GDSFile=self._GDSObjDeclaration(_GDSFile=None))
		self._DesignParameter['_Name']['Name'] = _Name

	def _CalculateDesignParameter(self,R_X_WIDTH=1500,CONT_X_NUM=None,CONT_Y_NUM=None,R_Y_LENGTH=1000):
	
		drc = DRC.DRC()
		_Name = self._DesignParameter['_Name']['_Name']
		
		self._DesignParameter['UNITR'] = self._SrefElementDeclaration(_DesignObj=opppcres_b_CDNS_6377410485842.opppcres_b_CDNS_6377410485842(_Name='UNITRIn{}'.format(_Name)))[0]
		self._DesignParameter['UNITR']['_DesignObj']._CalculateDesignParameter(**dict(R_X_width=R_X_WIDTH, R_Y_length=R_Y_LENGTH, _CoXNum=CONT_X_NUM, _CoYNum=CONT_Y_NUM))
		self._DesignParameter['UNITR']['_XYCoordinates'] = [[0.0, 0.0]]
		self._DesignParameter['upperpin'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1PINDrawing'][0], _Datatype=DesignParameters._LayerMapping['METAL1PINDrawing'][1], _XWidth=self._DesignParameter['UNITR']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'], _YWidth=self._DesignParameter['UNITR']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'])
		self._DesignParameter['upperpin']['_XYCoordinates'] = [[(+ (self._DesignParameter['UNITR']['_XYCoordinates'][0][0] + self._DesignParameter['UNITR']['_DesignObj']._DesignParameter['POLY_boundary_1']['_XYCoordinates'][0][0])), (+ (self._DesignParameter['UNITR']['_XYCoordinates'][0][1] + self._DesignParameter['UNITR']['_DesignObj']._DesignParameter['POLY_boundary_1']['_XYCoordinates'][0][1]))]]
		self._DesignParameter['lowerpin'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1PINDrawing'][0], _Datatype=DesignParameters._LayerMapping['METAL1PINDrawing'][1], _XWidth=self._DesignParameter['UNITR']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'], _YWidth=self._DesignParameter['UNITR']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'])
		self._DesignParameter['lowerpin']['_XYCoordinates'] = [[(+ (self._DesignParameter['UNITR']['_XYCoordinates'][0][0] + self._DesignParameter['UNITR']['_DesignObj']._DesignParameter['POLY_boundary_2']['_XYCoordinates'][0][0])), (+ (self._DesignParameter['UNITR']['_XYCoordinates'][0][1] + self._DesignParameter['UNITR']['_DesignObj']._DesignParameter['POLY_boundary_2']['_XYCoordinates'][0][1]))]]
		