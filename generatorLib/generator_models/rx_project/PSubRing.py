from generatorLib import StickDiagram
from generatorLib import DesignParameters
import copy
from generatorLib import DRC
from generatorLib.generator_models import PbodyContact

class PSubRing(StickDiagram._StickDiagram):
	def __init__(self, _DesignParameter=None, _Name='p_sub_ring'):
		if _DesignParameter != None:
			self._DesignParameter = _DesignParameter
		else:
			self._DesignParameter = dict(_Name=self._NameDeclaration(_Name=_Name), _GDSFile=self._GDSObjDeclaration(_GDSFile=None))
		self._DesignParameter['_Name']['Name'] = _Name

	def _CalculateDesignParameter(self,height=5000,width=3000,contact=2):
	
		drc = DRC.DRC()
		_Name = self._DesignParameter['_Name']['_Name']
		
		self._DesignParameter['bot'] = self._SrefElementDeclaration(_DesignObj=PbodyContact._PbodyContact(_Name='botIn{}'.format(_Name)))[0]
		self._DesignParameter['bot']['_DesignObj']._CalculatePbodyContactDesignParameter(**dict(_NumberOfPbodyCOX=((int(((width - (2 * drc._CoMinEnclosureByOD)) / (drc._CoMinWidth + drc._CoMinSpace2))) - contact) + 0), _NumberOfPbodyCOY=contact, _Met1XWidth=None, _Met1YWidth=None))
		self._DesignParameter['bot']['_XYCoordinates'] = [[0, ((- height) / 2)]]
		self._DesignParameter['top'] = self._SrefElementDeclaration(_DesignObj=PbodyContact._PbodyContact(_Name='topIn{}'.format(_Name)))[0]
		self._DesignParameter['top']['_DesignObj']._CalculatePbodyContactDesignParameter(**dict(_NumberOfPbodyCOX=((int(((width - (2 * drc._CoMinEnclosureByOD)) / (drc._CoMinWidth + drc._CoMinSpace2))) - contact) + 0), _NumberOfPbodyCOY=contact, _Met1XWidth=None, _Met1YWidth=None))
		self._DesignParameter['top']['_XYCoordinates'] = [[0, (height / 2)]]
		self._DesignParameter['left'] = self._SrefElementDeclaration(_DesignObj=PbodyContact._PbodyContact(_Name='leftIn{}'.format(_Name)))[0]
		self._DesignParameter['left']['_DesignObj']._CalculatePbodyContactDesignParameter(**dict(_NumberOfPbodyCOX=contact, _NumberOfPbodyCOY=((0 + int(((height - (2 * drc._CoMinEnclosureByOD)) / (drc._CoMinWidth + drc._CoMinSpace2)))) - contact), _Met1XWidth=None, _Met1YWidth=None))
		self._DesignParameter['left']['_XYCoordinates'] = [[((- width) / 2), 0]]
		self._DesignParameter['right'] = self._SrefElementDeclaration(_DesignObj=PbodyContact._PbodyContact(_Name='rightIn{}'.format(_Name)))[0]
		self._DesignParameter['right']['_DesignObj']._CalculatePbodyContactDesignParameter(**dict(_NumberOfPbodyCOX=contact, _NumberOfPbodyCOY=((0 + int(((height - (2 * drc._CoMinEnclosureByOD)) / (drc._CoMinWidth + drc._CoMinSpace2)))) - contact), _Met1XWidth=None, _Met1YWidth=None))
		self._DesignParameter['right']['_XYCoordinates'] = [[(width / 2), 0]]
		self._DesignParameter['od'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['DIFF'][0], _Datatype=DesignParameters._LayerMapping['DIFF'][1], _Width=(0 + self._DesignParameter['bot']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth']))
		self._DesignParameter['od']['_XYCoordinates'] = [[[(0 + self._DesignParameter['left']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['bot']['_XYCoordinates'][0][1])], [(0 + self._DesignParameter['right']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['bot']['_XYCoordinates'][0][1])], [(0 + self._DesignParameter['right']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['top']['_XYCoordinates'][0][1])], [(0 + self._DesignParameter['left']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['top']['_XYCoordinates'][0][1])], [(0 + self._DesignParameter['left']['_XYCoordinates'][0][0]), ((self._DesignParameter['bot']['_XYCoordinates'][0][1] + self._DesignParameter['bot']['_DesignObj']._DesignParameter['_ODLayer']['_XYCoordinates'][0][1]) - (self._DesignParameter['bot']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth'] / 2))]]]
		self._DesignParameter['nw_bot'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['PIMP'][0], _Datatype=DesignParameters._LayerMapping['PIMP'][1], _XWidth=((width + self._DesignParameter['left']['_DesignObj']._DesignParameter['_PPLayer']['_XWidth']) + 0), _YWidth=(0 + self._DesignParameter['bot']['_DesignObj']._DesignParameter['_PPLayer']['_YWidth']))
		self._DesignParameter['nw_bot']['_XYCoordinates'] = [[(0 + self._DesignParameter['bot']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['bot']['_XYCoordinates'][0][1])]]
		self._DesignParameter['nw_right'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['PIMP'][0], _Datatype=DesignParameters._LayerMapping['PIMP'][1], _XWidth=(self._DesignParameter['left']['_DesignObj']._DesignParameter['_PPLayer']['_XWidth'] + 0), _YWidth=((0 + height) + self._DesignParameter['top']['_DesignObj']._DesignParameter['_PPLayer']['_YWidth']))
		self._DesignParameter['nw_right']['_XYCoordinates'] = [[(0 + self._DesignParameter['right']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['right']['_XYCoordinates'][0][1])]]
		self._DesignParameter['nw_top'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['PIMP'][0], _Datatype=DesignParameters._LayerMapping['PIMP'][1], _XWidth=((width + self._DesignParameter['left']['_DesignObj']._DesignParameter['_PPLayer']['_XWidth']) + 0), _YWidth=(0 + self._DesignParameter['bot']['_DesignObj']._DesignParameter['_PPLayer']['_YWidth']))
		self._DesignParameter['nw_top']['_XYCoordinates'] = [[(0 + self._DesignParameter['top']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['top']['_XYCoordinates'][0][1])]]
		self._DesignParameter['nw_left'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['PIMP'][0], _Datatype=DesignParameters._LayerMapping['PIMP'][1], _XWidth=(self._DesignParameter['left']['_DesignObj']._DesignParameter['_PPLayer']['_XWidth'] + 0), _YWidth=((0 + height) + self._DesignParameter['top']['_DesignObj']._DesignParameter['_PPLayer']['_YWidth']))
		self._DesignParameter['nw_left']['_XYCoordinates'] = [[(0 + self._DesignParameter['left']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['left']['_XYCoordinates'][0][1])]]
		self._DesignParameter['met_right'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _XWidth=(0 + self._DesignParameter['bot']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']), _YWidth=((0 + height) + self._DesignParameter['bot']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']))
		self._DesignParameter['met_right']['_XYCoordinates'] = [[(0 + self._DesignParameter['right']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['right']['_XYCoordinates'][0][1])]]
		self._DesignParameter['met_left'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _XWidth=(0 + self._DesignParameter['bot']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']), _YWidth=((0 + height) + self._DesignParameter['bot']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']))
		self._DesignParameter['met_left']['_XYCoordinates'] = [[(0 + self._DesignParameter['left']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['left']['_XYCoordinates'][0][1])]]
		self._DesignParameter['met_top'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _XWidth=((width + self._DesignParameter['right']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']) + 0), _YWidth=(0 + self._DesignParameter['right']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']))
		self._DesignParameter['met_top']['_XYCoordinates'] = [[(0 + self._DesignParameter['top']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['top']['_XYCoordinates'][0][1])]]
		self._DesignParameter['met_bot'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _XWidth=((width + self._DesignParameter['right']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']) + 0), _YWidth=(0 + self._DesignParameter['bot']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']))
		self._DesignParameter['met_bot']['_XYCoordinates'] = [[(0 + self._DesignParameter['bot']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['bot']['_XYCoordinates'][0][1])]]
		