from generatorLib import StickDiagram
from generatorLib import DesignParameters
import copy
import math
from generatorLib import DRC
from generatorLib.generator_models import NMOSWithDummy

class EasyDebugModule(StickDiagram._StickDiagram):
	def __init__(self, _DesignParameter=None, _Name='EasyDebugModule'):
		if _DesignParameter != None:
			self._DesignParameter = _DesignParameter
		else:
			self._DesignParameter = dict(_Name=self._NameDeclaration(_Name=_Name), _GDSFile=self._GDSObjDeclaration(_GDSFile=None))
		self._DesignParameter['_Name']['Name'] = _Name

	def _CalculateDesignParameter(self,nmos1_gate=4,nmos1_width=200,nmos1_length=30,nmos1_gate_spacing=96,nmos1_sdwidth=50,dummy=True,pccrit=True,xvt='SLVT',nmos2_gate=4,nmos2_width=200,nmos2_length=40,nmos2_gate_spacing=96,nmos2_sdwidth=50,nmos3_gate=6,nmos3_width=200,nmos3_length=40,nmos3_gate_spacing=96,nmos3_sdwidth=50):
	
		drc = DRC.DRC()
		_Name = self._DesignParameter['_Name']['_Name']
		
		self._DesignParameter['NMOS1'] = self._SrefElementDeclaration(_DesignObj=NMOSWithDummy._NMOS(_Name='NMOS1In{}'.format(_Name)))[0]
		self._DesignParameter['NMOS1']['_DesignObj']._CalculateNMOSDesignParameter(**dict(_NMOSNumberofGate=nmos1_gate, _NMOSChannelWidth=nmos1_width, _NMOSChannellength=nmos1_length, _NMOSDummy=dummy, _GateSpacing=nmos1_gate_spacing, _SDWidth=nmos1_sdwidth, _XVT=xvt, _PCCrit=pccrit))
		self._DesignParameter['NMOS1']['_XYCoordinates'] = [[0.0, 0.0]]
		self._DesignParameter['NMOS2'] = self._SrefElementDeclaration(_DesignObj=NMOSWithDummy._NMOS(_Name='NMOS2In{}'.format(_Name)))[0]
		self._DesignParameter['NMOS2']['_DesignObj']._CalculateNMOSDesignParameter(**dict(_NMOSNumberofGate=nmos2_gate, _NMOSChannelWidth=nmos2_width, _NMOSChannellength=nmos2_length, _NMOSDummy=dummy, _GateSpacing=nmos2_gate_spacing, _SDWidth=nmos2_sdwidth, _XVT=xvt, _PCCrit=pccrit))
		self._DesignParameter['NMOS2']['_XYCoordinates'] = [[((((self._DesignParameter['NMOS1']['_XYCoordinates'][0][0] + self._DesignParameter['NMOS1']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['NMOS1']['_DesignObj']._DesignParameter['_PODummyLayer']['_XWidth'] / 2)) - (self._DesignParameter['NMOS2']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][(- 1)][0] + (self._DesignParameter['NMOS2']['_DesignObj']._DesignParameter['_PODummyLayer']['_XWidth'] / 2))) - drc._PolygateMinSpace), (((self._DesignParameter['NMOS1']['_XYCoordinates'][0][1] + self._DesignParameter['NMOS1']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][1]) + (self._DesignParameter['NMOS1']['_DesignObj']._DesignParameter['_PODummyLayer']['_YWidth'] / 2)) - (self._DesignParameter['NMOS2']['_DesignObj']._DesignParameter['_PODummyLayer']['_YWidth'] / 2))], [((((self._DesignParameter['NMOS1']['_XYCoordinates'][0][0] + self._DesignParameter['NMOS1']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][(- 1)][0]) + (self._DesignParameter['NMOS1']['_DesignObj']._DesignParameter['_PODummyLayer']['_XWidth'] / 2)) - (self._DesignParameter['NMOS2']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][0] - (self._DesignParameter['NMOS2']['_DesignObj']._DesignParameter['_PODummyLayer']['_XWidth'] / 2))) + drc._PolygateMinSpace), (((self._DesignParameter['NMOS1']['_XYCoordinates'][0][1] + self._DesignParameter['NMOS1']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][1]) + (self._DesignParameter['NMOS1']['_DesignObj']._DesignParameter['_PODummyLayer']['_YWidth'] / 2)) - (self._DesignParameter['NMOS2']['_DesignObj']._DesignParameter['_PODummyLayer']['_YWidth'] / 2))]]
		self._DesignParameter['NMOS3'] = self._SrefElementDeclaration(_DesignObj=NMOSWithDummy._NMOS(_Name='NMOS3In{}'.format(_Name)))[0]
		self._DesignParameter['NMOS3']['_DesignObj']._CalculateNMOSDesignParameter(**dict(_NMOSNumberofGate=nmos3_gate, _NMOSChannelWidth=nmos3_width, _NMOSChannellength=nmos3_length, _NMOSDummy=dummy, _GateSpacing=nmos3_gate_spacing, _SDWidth=nmos3_sdwidth, _XVT=xvt, _PCCrit=pccrit))
		self._DesignParameter['NMOS3']['_XYCoordinates'] = [[((((self._DesignParameter['NMOS2']['_XYCoordinates'][0][0] + self._DesignParameter['NMOS2']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['NMOS2']['_DesignObj']._DesignParameter['_PODummyLayer']['_XWidth'] / 2)) - (self._DesignParameter['NMOS3']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][(- 1)][0] + (self._DesignParameter['NMOS3']['_DesignObj']._DesignParameter['_PODummyLayer']['_XWidth'] / 2))) - drc._PolygateMinSpace), (((self._DesignParameter['NMOS2']['_XYCoordinates'][1][1] + self._DesignParameter['NMOS2']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][1]) + (self._DesignParameter['NMOS2']['_DesignObj']._DesignParameter['_PODummyLayer']['_YWidth'] / 2)) - (self._DesignParameter['NMOS3']['_DesignObj']._DesignParameter['_PODummyLayer']['_YWidth'] / 2))], [((((self._DesignParameter['NMOS2']['_XYCoordinates'][1][0] + self._DesignParameter['NMOS2']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][(- 1)][0]) + (self._DesignParameter['NMOS2']['_DesignObj']._DesignParameter['_PODummyLayer']['_XWidth'] / 2)) - (self._DesignParameter['NMOS3']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][0] - (self._DesignParameter['NMOS3']['_DesignObj']._DesignParameter['_PODummyLayer']['_XWidth'] / 2))) + drc._PolygateMinSpace), (((self._DesignParameter['NMOS2']['_XYCoordinates'][1][1] + self._DesignParameter['NMOS2']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][1]) + (self._DesignParameter['NMOS2']['_DesignObj']._DesignParameter['_PODummyLayer']['_YWidth'] / 2)) - (self._DesignParameter['NMOS3']['_DesignObj']._DesignParameter['_PODummyLayer']['_YWidth'] / 2))]]

