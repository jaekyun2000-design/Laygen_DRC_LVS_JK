from generatorLib import StickDiagram
from generatorLib import DesignParameters
import copy
import math
from generatorLib import DRC
from generatorLib.generator_models import NbodyContact
from generatorLib.generator_models import PMOSWithDummy
from generatorLib.generator_models import ViaMet12Met2
from generatorLib.generator_models import NMOSWithDummy
from generatorLib.generator_models import ViaPoly2Met1
from generatorLib.generator_models import ViaMet32Met4
from generatorLib.generator_models import PbodyContact
from generatorLib.generator_models import ViaStack
from generatorLib.generator_models import ViaMet22Met3

class SRLatchInSlicerWithSRLatch_0(StickDiagram._StickDiagram):
	def __init__(self, _DesignParameter=None, _Name='SRLatchInSlicerWithSRLatch_0'):
		if _DesignParameter != None:
			self._DesignParameter = _DesignParameter
		else:
			self._DesignParameter = dict(_Name=self._NameDeclaration(_Name=_Name), _GDSFile=self._GDSObjDeclaration(_GDSFile=None))
		self._DesignParameter['_Name']['Name'] = _Name

	def _CalculateDesignParameter(self,supply_via=2,supply_height=1707,SLVT=None,gate1=5,gate2=1,gate3=2,gate4=2,nwidth1=200,nwidth2=200,nwidth3=200,nwidth4=200,np_ratio=2):
	
		drc = DRC.DRC()
		_Name = self._DesignParameter['_Name']['_Name']
		
		self._DesignParameter['VSS'] = self._SrefElementDeclaration(_DesignObj=PbodyContact._PbodyContact(_Name='VSSIn{}'.format(_Name)))[0]
		self._DesignParameter['VSS']['_DesignObj']._CalculatePbodyContactDesignParameter(**dict(_NumberOfPbodyCOX=20, _NumberOfPbodyCOY=2, _Met1XWidth=None, _Met1YWidth=None))
		self._DesignParameter['VSS']['_XYCoordinates'] = [[350.0, 0.0]]
		self._DesignParameter['VDD_up'] = self._SrefElementDeclaration(_DesignObj=NbodyContact._NbodyContact(_Name='VDD_upIn{}'.format(_Name)))[0]
		self._DesignParameter['VDD_up']['_DesignObj']._CalculateNbodyContactDesignParameter(**dict(_NumberOfNbodyCOX=20, _NumberOfNbodyCOY=supply_via, _Met1XWidth=None, _Met1YWidth=None))
		self._DesignParameter['VDD_up']['_XYCoordinates'] = [[self._DesignParameter['VSS']['_XYCoordinates'][0][0], supply_height]]
		self._DesignParameter['VDD_down'] = self._SrefElementDeclaration(_DesignObj=NbodyContact._NbodyContact(_Name='VDD_downIn{}'.format(_Name)))[0]
		self._DesignParameter['VDD_down']['_DesignObj']._CalculateNbodyContactDesignParameter(**dict(_NumberOfNbodyCOX=20, _NumberOfNbodyCOY=supply_via, _Met1XWidth=None, _Met1YWidth=None))
		self._DesignParameter['VDD_down']['_XYCoordinates'] = [[self._DesignParameter['VSS']['_XYCoordinates'][0][0], (- supply_height)]]
		self._DesignParameter['NMOS1InSRLatch_0'] = self._SrefElementDeclaration(_DesignObj=NMOSWithDummy._NMOS(_Name='NMOS1InSRLatch_0In{}'.format(_Name)))[0]
		self._DesignParameter['NMOS1InSRLatch_0']['_DesignObj']._CalculateNMOSDesignParameter(**dict(_NMOSNumberofGate=gate1, _NMOSChannelWidth=nwidth1, _NMOSChannellength=30, _NMOSDummy=True, _GateSpacing=None, _XVT='SLVT'))
		self._DesignParameter['NMOS1InSRLatch_0']['_XYCoordinates'] = [[(- 343), ((((self._DesignParameter['VSS']['_XYCoordinates'][0][1] + self._DesignParameter['VSS']['_DesignObj']._DesignParameter['_PPLayer']['_XYCoordinates'][0][1]) + (self._DesignParameter['VSS']['_DesignObj']._DesignParameter['_PPLayer']['_YWidth'] / 2)) + drc._RXMinSpacetoOP) + (self._DesignParameter['NMOS1InSRLatch_0']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth'] / 2))]]
		self._DesignParameter['NMOS2InSRLatch_0'] = self._SrefElementDeclaration(_DesignObj=NMOSWithDummy._NMOS(_Name='NMOS2InSRLatch_0In{}'.format(_Name)))[0]
		self._DesignParameter['NMOS2InSRLatch_0']['_DesignObj']._CalculateNMOSDesignParameter(**dict(_NMOSNumberofGate=gate2, _NMOSChannelWidth=nwidth2, _NMOSChannellength=30, _NMOSDummy=True, _GateSpacing=None, _XVT='SLVT'))
		self._DesignParameter['NMOS2InSRLatch_0']['_XYCoordinates'] = [[((((self._DesignParameter['NMOS1InSRLatch_0']['_XYCoordinates'][0][0] + self._DesignParameter['NMOS1InSRLatch_0']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][(- 1)][0]) + (self._DesignParameter['NMOS1InSRLatch_0']['_DesignObj']._DesignParameter['_PODummyLayer']['_XWidth'] / 2)) + drc._PolygateMinSpace) - (self._DesignParameter['NMOS2InSRLatch_0']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][0] - (self._DesignParameter['NMOS2InSRLatch_0']['_DesignObj']._DesignParameter['_PODummyLayer']['_XWidth'] / 2))), self._DesignParameter['NMOS1InSRLatch_0']['_XYCoordinates'][0][1]]]
		self._DesignParameter['NMOS3InSRLatch_0'] = self._SrefElementDeclaration(_DesignObj=NMOSWithDummy._NMOS(_Name='NMOS3InSRLatch_0In{}'.format(_Name)))[0]
		self._DesignParameter['NMOS3InSRLatch_0']['_DesignObj']._CalculateNMOSDesignParameter(**dict(_NMOSNumberofGate=gate3, _NMOSChannelWidth=nwidth3, _NMOSChannellength=30, _NMOSDummy=True, _GateSpacing=None, _XVT='SLVT'))
		self._DesignParameter['NMOS3InSRLatch_0']['_XYCoordinates'] = [[((((self._DesignParameter['NMOS2InSRLatch_0']['_XYCoordinates'][0][0] + self._DesignParameter['NMOS2InSRLatch_0']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][(- 1)][0]) + (self._DesignParameter['NMOS2InSRLatch_0']['_DesignObj']._DesignParameter['_PODummyLayer']['_XWidth'] / 2)) + drc._PolygateMinSpace) - (self._DesignParameter['NMOS3InSRLatch_0']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][0] - (self._DesignParameter['NMOS3InSRLatch_0']['_DesignObj']._DesignParameter['_PODummyLayer']['_XWidth'] / 2))), self._DesignParameter['NMOS2InSRLatch_0']['_XYCoordinates'][0][1]]]
		self._DesignParameter['NMOS4InSRLatch_0'] = self._SrefElementDeclaration(_DesignObj=NMOSWithDummy._NMOS(_Name='NMOS4InSRLatch_0In{}'.format(_Name)))[0]
		self._DesignParameter['NMOS4InSRLatch_0']['_DesignObj']._CalculateNMOSDesignParameter(**dict(_NMOSNumberofGate=gate4, _NMOSChannelWidth=nwidth4, _NMOSChannellength=30, _NMOSDummy=True, _GateSpacing=None, _XVT='SLVT'))
		self._DesignParameter['NMOS4InSRLatch_0']['_XYCoordinates'] = [[((((self._DesignParameter['NMOS3InSRLatch_0']['_XYCoordinates'][0][0] + self._DesignParameter['NMOS3InSRLatch_0']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][(- 1)][0]) + (self._DesignParameter['NMOS3InSRLatch_0']['_DesignObj']._DesignParameter['_PODummyLayer']['_XWidth'] / 2)) + drc._PolygateMinSpace) - (self._DesignParameter['NMOS4InSRLatch_0']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][0] - (self._DesignParameter['NMOS4InSRLatch_0']['_DesignObj']._DesignParameter['_PODummyLayer']['_XWidth'] / 2))), self._DesignParameter['NMOS3InSRLatch_0']['_XYCoordinates'][0][1]]]
		self._DesignParameter['PMOS1InSRLatch_0'] = self._SrefElementDeclaration(_DesignObj=PMOSWithDummy._PMOS(_Name='PMOS1InSRLatch_0In{}'.format(_Name)))[0]
		self._DesignParameter['PMOS1InSRLatch_0']['_DesignObj']._CalculatePMOSDesignParameter(**dict(_PMOSNumberofGate=gate1, _PMOSChannelWidth=(np_ratio * nwidth1), _PMOSChannellength=30, _PMOSDummy=True, _GateSpacing=None, _XVT='SLVT'))
		self._DesignParameter['PMOS1InSRLatch_0']['_XYCoordinates'] = [[self._DesignParameter['NMOS1InSRLatch_0']['_XYCoordinates'][0][0], ((((self._DesignParameter['VDD_up']['_XYCoordinates'][0][1] + self._DesignParameter['VDD_up']['_DesignObj']._DesignParameter['_ODLayer']['_XYCoordinates'][0][1]) - (self._DesignParameter['VDD_up']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth'] / 2)) - drc._OdMinSpace) - (self._DesignParameter['PMOS1InSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2))]]
		self._DesignParameter['PMOS2InSRLatch_0'] = self._SrefElementDeclaration(_DesignObj=PMOSWithDummy._PMOS(_Name='PMOS2InSRLatch_0In{}'.format(_Name)))[0]
		self._DesignParameter['PMOS2InSRLatch_0']['_DesignObj']._CalculatePMOSDesignParameter(**dict(_PMOSNumberofGate=gate2, _PMOSChannelWidth=(np_ratio * nwidth2), _PMOSChannellength=30, _PMOSDummy=True, _GateSpacing=None, _XVT='SLVT'))
		self._DesignParameter['PMOS2InSRLatch_0']['_XYCoordinates'] = [[self._DesignParameter['NMOS2InSRLatch_0']['_XYCoordinates'][0][0], ((((self._DesignParameter['VDD_up']['_XYCoordinates'][0][1] + self._DesignParameter['VDD_up']['_DesignObj']._DesignParameter['_ODLayer']['_XYCoordinates'][0][1]) - (self._DesignParameter['VDD_up']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth'] / 2)) - drc._OdMinSpace) - (self._DesignParameter['PMOS1InSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2))]]
		self._DesignParameter['PMOS4InSRLatch_0'] = self._SrefElementDeclaration(_DesignObj=PMOSWithDummy._PMOS(_Name='PMOS4InSRLatch_0In{}'.format(_Name)))[0]
		self._DesignParameter['PMOS4InSRLatch_0']['_DesignObj']._CalculatePMOSDesignParameter(**dict(_PMOSNumberofGate=gate4, _PMOSChannelWidth=(np_ratio * nwidth4), _PMOSChannellength=30, _PMOSDummy=True, _GateSpacing=None, _XVT='SLVT'))
		self._DesignParameter['PMOS4InSRLatch_0']['_XYCoordinates'] = [[self._DesignParameter['NMOS4InSRLatch_0']['_XYCoordinates'][0][0], ((((self._DesignParameter['VDD_up']['_XYCoordinates'][0][1] + self._DesignParameter['VDD_up']['_DesignObj']._DesignParameter['_ODLayer']['_XYCoordinates'][0][1]) - (self._DesignParameter['VDD_up']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth'] / 2)) - drc._OdMinSpace) - (self._DesignParameter['PMOS1InSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2))]]
		self._DesignParameter['NMOS1_rInSRLatch_0'] = self._SrefElementDeclaration(_DesignObj=NMOSWithDummy._NMOS(_Name='NMOS1_rInSRLatch_0In{}'.format(_Name)))[0]
		self._DesignParameter['NMOS1_rInSRLatch_0']['_DesignObj']._CalculateNMOSDesignParameter(**dict(_NMOSNumberofGate=gate1, _NMOSChannelWidth=nwidth1, _NMOSChannellength=30, _NMOSDummy=True, _GateSpacing=None, _XVT='SLVT'))
		self._DesignParameter['NMOS1_rInSRLatch_0']['_XYCoordinates'] = [[self._DesignParameter['NMOS1InSRLatch_0']['_XYCoordinates'][0][0], ((((self._DesignParameter['VSS']['_XYCoordinates'][0][1] + self._DesignParameter['VSS']['_DesignObj']._DesignParameter['_PPLayer']['_XYCoordinates'][0][1]) - (self._DesignParameter['VSS']['_DesignObj']._DesignParameter['_PPLayer']['_YWidth'] / 2)) - drc._RXMinSpacetoOP) - (self._DesignParameter['NMOS1_rInSRLatch_0']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth'] / 2))]]
		self._DesignParameter['NMOS2_rInSRLatch_0'] = self._SrefElementDeclaration(_DesignObj=NMOSWithDummy._NMOS(_Name='NMOS2_rInSRLatch_0In{}'.format(_Name)))[0]
		self._DesignParameter['NMOS2_rInSRLatch_0']['_DesignObj']._CalculateNMOSDesignParameter(**dict(_NMOSNumberofGate=gate2, _NMOSChannelWidth=nwidth2, _NMOSChannellength=30, _NMOSDummy=True, _GateSpacing=None, _XVT='SLVT'))
		self._DesignParameter['NMOS2_rInSRLatch_0']['_XYCoordinates'] = [[self._DesignParameter['NMOS2InSRLatch_0']['_XYCoordinates'][0][0], self._DesignParameter['NMOS1_rInSRLatch_0']['_XYCoordinates'][0][1]]]
		self._DesignParameter['NMOS3_rInSRLatch_0'] = self._SrefElementDeclaration(_DesignObj=NMOSWithDummy._NMOS(_Name='NMOS3_rInSRLatch_0In{}'.format(_Name)))[0]
		self._DesignParameter['NMOS3_rInSRLatch_0']['_DesignObj']._CalculateNMOSDesignParameter(**dict(_NMOSNumberofGate=gate3, _NMOSChannelWidth=nwidth3, _NMOSChannellength=30, _NMOSDummy=True, _GateSpacing=None, _XVT='SLVT'))
		self._DesignParameter['NMOS3_rInSRLatch_0']['_XYCoordinates'] = [[self._DesignParameter['NMOS3InSRLatch_0']['_XYCoordinates'][0][0], self._DesignParameter['NMOS2_rInSRLatch_0']['_XYCoordinates'][0][1]]]
		self._DesignParameter['NMOS4_rInSRLatch_0'] = self._SrefElementDeclaration(_DesignObj=NMOSWithDummy._NMOS(_Name='NMOS4_rInSRLatch_0In{}'.format(_Name)))[0]
		self._DesignParameter['NMOS4_rInSRLatch_0']['_DesignObj']._CalculateNMOSDesignParameter(**dict(_NMOSNumberofGate=gate4, _NMOSChannelWidth=nwidth4, _NMOSChannellength=30, _NMOSDummy=True, _GateSpacing=None, _XVT='SLVT'))
		self._DesignParameter['NMOS4_rInSRLatch_0']['_XYCoordinates'] = [[self._DesignParameter['NMOS4InSRLatch_0']['_XYCoordinates'][0][0], self._DesignParameter['NMOS3_rInSRLatch_0']['_XYCoordinates'][0][1]]]
		self._DesignParameter['PMOS1_rInSRLatch_0'] = self._SrefElementDeclaration(_DesignObj=PMOSWithDummy._PMOS(_Name='PMOS1_rInSRLatch_0In{}'.format(_Name)))[0]
		self._DesignParameter['PMOS1_rInSRLatch_0']['_DesignObj']._CalculatePMOSDesignParameter(**dict(_PMOSNumberofGate=gate1, _PMOSChannelWidth=(np_ratio * nwidth1), _PMOSChannellength=30, _PMOSDummy=True, _GateSpacing=None, _XVT='SLVT'))
		self._DesignParameter['PMOS1_rInSRLatch_0']['_XYCoordinates'] = [[self._DesignParameter['NMOS1InSRLatch_0']['_XYCoordinates'][0][0], ((((self._DesignParameter['VDD_down']['_XYCoordinates'][0][1] + self._DesignParameter['VDD_down']['_DesignObj']._DesignParameter['_ODLayer']['_XYCoordinates'][0][1]) + (self._DesignParameter['VDD_down']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth'] / 2)) + drc._OdMinSpace) + (self._DesignParameter['PMOS1_rInSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2))]]
		self._DesignParameter['PMOS2_rInSRLatch_0'] = self._SrefElementDeclaration(_DesignObj=PMOSWithDummy._PMOS(_Name='PMOS2_rInSRLatch_0In{}'.format(_Name)))[0]
		self._DesignParameter['PMOS2_rInSRLatch_0']['_DesignObj']._CalculatePMOSDesignParameter(**dict(_PMOSNumberofGate=gate2, _PMOSChannelWidth=(np_ratio * nwidth2), _PMOSChannellength=30, _PMOSDummy=True, _GateSpacing=None, _XVT='SLVT'))
		self._DesignParameter['PMOS2_rInSRLatch_0']['_XYCoordinates'] = [[self._DesignParameter['NMOS2InSRLatch_0']['_XYCoordinates'][0][0], self._DesignParameter['PMOS1_rInSRLatch_0']['_XYCoordinates'][0][1]]]
		self._DesignParameter['PMOS3_rInSRLatch_0'] = self._SrefElementDeclaration(_DesignObj=PMOSWithDummy._PMOS(_Name='PMOS3_rInSRLatch_0In{}'.format(_Name)))[0]
		self._DesignParameter['PMOS3_rInSRLatch_0']['_DesignObj']._CalculatePMOSDesignParameter(**dict(_PMOSNumberofGate=gate3, _PMOSChannelWidth=(np_ratio * nwidth3), _PMOSChannellength=30, _PMOSDummy=True, _GateSpacing=None, _XVT='SLVT'))
		self._DesignParameter['PMOS3_rInSRLatch_0']['_XYCoordinates'] = [[self._DesignParameter['NMOS3InSRLatch_0']['_XYCoordinates'][0][0], self._DesignParameter['PMOS2_rInSRLatch_0']['_XYCoordinates'][0][1]]]
		self._DesignParameter['PMOS4_rInSRLatch_0'] = self._SrefElementDeclaration(_DesignObj=PMOSWithDummy._PMOS(_Name='PMOS4_rInSRLatch_0In{}'.format(_Name)))[0]
		self._DesignParameter['PMOS4_rInSRLatch_0']['_DesignObj']._CalculatePMOSDesignParameter(**dict(_PMOSNumberofGate=gate4, _PMOSChannelWidth=(np_ratio * nwidth4), _PMOSChannellength=30, _PMOSDummy=True, _GateSpacing=None, _XVT='SLVT'))
		self._DesignParameter['PMOS4_rInSRLatch_0']['_XYCoordinates'] = [[self._DesignParameter['NMOS4InSRLatch_0']['_XYCoordinates'][0][0], self._DesignParameter['PMOS3_rInSRLatch_0']['_XYCoordinates'][0][1]]]
		path_list = []
		if (len(self._DesignParameter['NMOS1InSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates']) == 1):
		    mode = 'vertical'
		    _width = self._DesignParameter['NMOS1InSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
		elif (self._DesignParameter['NMOS1InSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0] == self._DesignParameter['NMOS1InSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][(- 1)][0]):
		    mode = 'horizontal'
		    _width = self._DesignParameter['NMOS1InSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
		elif (self._DesignParameter['NMOS1InSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1] == self._DesignParameter['NMOS1InSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][(- 1)][1]):
		    mode = 'vertical'
		    _width = self._DesignParameter['NMOS1InSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
		else:
		    print('Invalid Target Input')
		if (mode == 'vertical'):
		    xy_with_offset = []
		    target_y_value = (0 + self._DesignParameter['VSS']['_XYCoordinates'][0][1])
		    for i in range(len(self._DesignParameter['NMOS1InSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'])):
		        if ((i % 2) == 0):
		            xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['NMOS1InSRLatch_0']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['NMOS1InSRLatch_0']['_XYCoordinates'][0][1])], self._DesignParameter['NMOS1InSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		elif (mode == 'horizontal'):
		    xy_with_offset = []
		    target_x_value = (0 + self._DesignParameter['VSS']['_XYCoordinates'][0][0])
		    for i in range(len(self._DesignParameter['NMOS1InSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'])):
		        if ((i % 2) == 0):
		            xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['NMOS1InSRLatch_0']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['NMOS1InSRLatch_0']['_XYCoordinates'][0][1])], self._DesignParameter['NMOS1InSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		self._DesignParameter['nmos_u1_supply'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=_width)
		self._DesignParameter['nmos_u1_supply']['_XYCoordinates'] = path_list
		path_list = []
		if (len(self._DesignParameter['NMOS1_rInSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates']) == 1):
		    mode = 'vertical'
		    _width = self._DesignParameter['NMOS1_rInSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
		elif (self._DesignParameter['NMOS1_rInSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0] == self._DesignParameter['NMOS1_rInSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][(- 1)][0]):
		    mode = 'horizontal'
		    _width = self._DesignParameter['NMOS1_rInSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
		elif (self._DesignParameter['NMOS1_rInSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1] == self._DesignParameter['NMOS1_rInSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][(- 1)][1]):
		    mode = 'vertical'
		    _width = self._DesignParameter['NMOS1_rInSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
		else:
		    print('Invalid Target Input')
		if (mode == 'vertical'):
		    xy_with_offset = []
		    target_y_value = (0 + self._DesignParameter['VSS']['_XYCoordinates'][0][1])
		    for i in range(len(self._DesignParameter['NMOS1_rInSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'])):
		        if ((i % 2) == 0):
		            xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['NMOS1_rInSRLatch_0']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['NMOS1_rInSRLatch_0']['_XYCoordinates'][0][1])], self._DesignParameter['NMOS1_rInSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		elif (mode == 'horizontal'):
		    xy_with_offset = []
		    target_x_value = (0 + self._DesignParameter['VSS']['_XYCoordinates'][0][0])
		    for i in range(len(self._DesignParameter['NMOS1_rInSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'])):
		        if ((i % 2) == 0):
		            xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['NMOS1_rInSRLatch_0']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['NMOS1_rInSRLatch_0']['_XYCoordinates'][0][1])], self._DesignParameter['NMOS1_rInSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		self._DesignParameter['nmos_d1_supply'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=_width)
		self._DesignParameter['nmos_d1_supply']['_XYCoordinates'] = path_list
		path_list = []
		if (len(self._DesignParameter['NMOS2InSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates']) == 1):
		    mode = 'vertical'
		    _width = self._DesignParameter['NMOS2InSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
		elif (self._DesignParameter['NMOS2InSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0] == self._DesignParameter['NMOS2InSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][(- 1)][0]):
		    mode = 'horizontal'
		    _width = self._DesignParameter['NMOS2InSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
		elif (self._DesignParameter['NMOS2InSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1] == self._DesignParameter['NMOS2InSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][(- 1)][1]):
		    mode = 'vertical'
		    _width = self._DesignParameter['NMOS2InSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
		else:
		    print('Invalid Target Input')
		if (mode == 'vertical'):
		    xy_with_offset = []
		    target_y_value = (0 + self._DesignParameter['VSS']['_XYCoordinates'][0][1])
		    for i in range(len(self._DesignParameter['NMOS2InSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'])):
		        if ((i % 2) == 0):
		            xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['NMOS2InSRLatch_0']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['NMOS2InSRLatch_0']['_XYCoordinates'][0][1])], self._DesignParameter['NMOS2InSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		elif (mode == 'horizontal'):
		    xy_with_offset = []
		    target_x_value = (0 + self._DesignParameter['VSS']['_XYCoordinates'][0][0])
		    for i in range(len(self._DesignParameter['NMOS2InSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'])):
		        if ((i % 2) == 0):
		            xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['NMOS2InSRLatch_0']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['NMOS2InSRLatch_0']['_XYCoordinates'][0][1])], self._DesignParameter['NMOS2InSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		self._DesignParameter['nmos_u2'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=_width)
		self._DesignParameter['nmos_u2']['_XYCoordinates'] = path_list
		self._DesignParameter['PMOS3InSRLatch_0'] = self._SrefElementDeclaration(_DesignObj=PMOSWithDummy._PMOS(_Name='PMOS3InSRLatch_0In{}'.format(_Name)))[0]
		self._DesignParameter['PMOS3InSRLatch_0']['_DesignObj']._CalculatePMOSDesignParameter(**dict(_PMOSNumberofGate=gate3, _PMOSChannelWidth=(np_ratio * nwidth3), _PMOSChannellength=30, _PMOSDummy=True, _GateSpacing=None, _XVT='SLVT'))
		self._DesignParameter['PMOS3InSRLatch_0']['_XYCoordinates'] = [[self._DesignParameter['NMOS3InSRLatch_0']['_XYCoordinates'][0][0], ((((self._DesignParameter['VDD_up']['_XYCoordinates'][0][1] + self._DesignParameter['VDD_up']['_DesignObj']._DesignParameter['_ODLayer']['_XYCoordinates'][0][1]) - (self._DesignParameter['VDD_up']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth'] / 2)) - drc._OdMinSpace) - (self._DesignParameter['PMOS1InSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2))]]
		path_list = []
		if (len(self._DesignParameter['NMOS2_rInSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates']) == 1):
		    mode = 'vertical'
		    _width = self._DesignParameter['NMOS2_rInSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
		elif (self._DesignParameter['NMOS2_rInSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0] == self._DesignParameter['NMOS2_rInSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][(- 1)][0]):
		    mode = 'horizontal'
		    _width = self._DesignParameter['NMOS2_rInSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
		elif (self._DesignParameter['NMOS2_rInSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1] == self._DesignParameter['NMOS2_rInSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][(- 1)][1]):
		    mode = 'vertical'
		    _width = self._DesignParameter['NMOS2_rInSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
		else:
		    print('Invalid Target Input')
		if (mode == 'vertical'):
		    xy_with_offset = []
		    target_y_value = (0 + self._DesignParameter['VSS']['_XYCoordinates'][0][1])
		    for i in range(len(self._DesignParameter['NMOS2_rInSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'])):
		        if ((i % 2) == 0):
		            xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['NMOS2_rInSRLatch_0']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['NMOS2_rInSRLatch_0']['_XYCoordinates'][0][1])], self._DesignParameter['NMOS2_rInSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		elif (mode == 'horizontal'):
		    xy_with_offset = []
		    target_x_value = (0 + self._DesignParameter['VSS']['_XYCoordinates'][0][0])
		    for i in range(len(self._DesignParameter['NMOS2_rInSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'])):
		        if ((i % 2) == 0):
		            xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['NMOS2_rInSRLatch_0']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['NMOS2_rInSRLatch_0']['_XYCoordinates'][0][1])], self._DesignParameter['NMOS2_rInSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		self._DesignParameter['nmos_d2_supply'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=_width)
		self._DesignParameter['nmos_d2_supply']['_XYCoordinates'] = path_list
		path_list = []
		if (len(self._DesignParameter['NMOS4InSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates']) == 1):
		    mode = 'vertical'
		    _width = self._DesignParameter['NMOS4InSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
		elif (self._DesignParameter['NMOS4InSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0] == self._DesignParameter['NMOS4InSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][(- 1)][0]):
		    mode = 'horizontal'
		    _width = self._DesignParameter['NMOS4InSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
		elif (self._DesignParameter['NMOS4InSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1] == self._DesignParameter['NMOS4InSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][(- 1)][1]):
		    mode = 'vertical'
		    _width = self._DesignParameter['NMOS4InSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
		else:
		    print('Invalid Target Input')
		if (mode == 'vertical'):
		    xy_with_offset = []
		    target_y_value = (0 + self._DesignParameter['VSS']['_XYCoordinates'][0][1])
		    for i in range(len(self._DesignParameter['NMOS4InSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'])):
		        if ((i % 2) == 0):
		            xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['NMOS4InSRLatch_0']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['NMOS4InSRLatch_0']['_XYCoordinates'][0][1])], self._DesignParameter['NMOS4InSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		elif (mode == 'horizontal'):
		    xy_with_offset = []
		    target_x_value = (0 + self._DesignParameter['VSS']['_XYCoordinates'][0][0])
		    for i in range(len(self._DesignParameter['NMOS4InSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'])):
		        if ((i % 2) == 0):
		            xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['NMOS4InSRLatch_0']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['NMOS4InSRLatch_0']['_XYCoordinates'][0][1])], self._DesignParameter['NMOS4InSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		self._DesignParameter['nmos_u4'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=_width)
		self._DesignParameter['nmos_u4']['_XYCoordinates'] = path_list
		path_list = []
		if (len(self._DesignParameter['NMOS4_rInSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates']) == 1):
		    mode = 'vertical'
		    _width = self._DesignParameter['NMOS4_rInSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
		elif (self._DesignParameter['NMOS4_rInSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0] == self._DesignParameter['NMOS4_rInSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][(- 1)][0]):
		    mode = 'horizontal'
		    _width = self._DesignParameter['NMOS4_rInSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
		elif (self._DesignParameter['NMOS4_rInSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1] == self._DesignParameter['NMOS4_rInSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][(- 1)][1]):
		    mode = 'vertical'
		    _width = self._DesignParameter['NMOS4_rInSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
		else:
		    print('Invalid Target Input')
		if (mode == 'vertical'):
		    xy_with_offset = []
		    target_y_value = (0 + self._DesignParameter['VSS']['_XYCoordinates'][0][1])
		    for i in range(len(self._DesignParameter['NMOS4_rInSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'])):
		        if ((i % 2) == 0):
		            xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['NMOS4_rInSRLatch_0']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['NMOS4_rInSRLatch_0']['_XYCoordinates'][0][1])], self._DesignParameter['NMOS4_rInSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		elif (mode == 'horizontal'):
		    xy_with_offset = []
		    target_x_value = (0 + self._DesignParameter['VSS']['_XYCoordinates'][0][0])
		    for i in range(len(self._DesignParameter['NMOS4_rInSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'])):
		        if ((i % 2) == 0):
		            xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['NMOS4_rInSRLatch_0']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['NMOS4_rInSRLatch_0']['_XYCoordinates'][0][1])], self._DesignParameter['NMOS4_rInSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		self._DesignParameter['nmos_d4_supply'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=_width)
		self._DesignParameter['nmos_d4_supply']['_XYCoordinates'] = path_list
		self._DesignParameter['PCCAM1_nu1'] = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_Name='PCCAM1_nu1In{}'.format(_Name)))[0]
		self._DesignParameter['PCCAM1_nu1']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(**dict(_ViaPoly2Met1NumberOfCOY=1, _ViaPoly2Met1NumberOfCOX=max(1, (1 + int(((((((self._DesignParameter['NMOS1InSRLatch_0']['_XYCoordinates'][0][0] + self._DesignParameter['NMOS1InSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]) + (self._DesignParameter['NMOS1InSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)) - ((self._DesignParameter['NMOS1InSRLatch_0']['_XYCoordinates'][0][0] + self._DesignParameter['NMOS1InSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['NMOS1InSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2))) - drc._CoMinSpace) - (2 * drc._CoMinEnclosureByPO)) / (drc._CoMinWidth + drc._CoMinSpace)))))))
		self._DesignParameter['PCCAM1_nu1']['_XYCoordinates'] = [[self._DesignParameter['NMOS1InSRLatch_0']['_XYCoordinates'][0][0], ((((self._DesignParameter['NMOS1InSRLatch_0']['_XYCoordinates'][0][1] + self._DesignParameter['NMOS1InSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) + (self._DesignParameter['NMOS1InSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)) + drc._Metal1MinSpace2) + (self._DesignParameter['PCCAM1_nu1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2))]]
		self._DesignParameter['M1V1M2_nu_1'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='M1V1M2_nu_1In{}'.format(_Name)))[0]
		self._DesignParameter['M1V1M2_nu_1']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureY(**dict(_ViaMet12Met2NumberOfCOX=max(1, (1 + int(((((((self._DesignParameter['NMOS1InSRLatch_0']['_XYCoordinates'][0][0] + self._DesignParameter['NMOS1InSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]) + (self._DesignParameter['NMOS1InSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)) - ((self._DesignParameter['NMOS1InSRLatch_0']['_XYCoordinates'][0][0] + self._DesignParameter['NMOS1InSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['NMOS1InSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2))) - drc._VIAxMinSpace) - (2 * drc._VIAxMinEnclosureByMetx)) / (drc._VIAxMinWidth + drc._VIAxMinSpace))))), _ViaMet12Met2NumberOfCOY=1))
		self._DesignParameter['M1V1M2_nu_1']['_XYCoordinates'] = [[(- 343.0), 591.0]]
		self._DesignParameter['METAL1_boundary_191'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _XWidth=max(self._DesignParameter['PCCAM1_nu1']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'], self._DesignParameter['M1V1M2_nu_1']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']), _YWidth=max(self._DesignParameter['PCCAM1_nu1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'], self._DesignParameter['M1V1M2_nu_1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']))
		self._DesignParameter['METAL1_boundary_191']['_XYCoordinates'] = [[(+ self._DesignParameter['PCCAM1_nu1']['_XYCoordinates'][0][0]), (+ self._DesignParameter['PCCAM1_nu1']['_XYCoordinates'][0][1])]]
		self._DesignParameter['POLY_boundary_187'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _XWidth=(((self._DesignParameter['NMOS1InSRLatch_0']['_XYCoordinates'][0][0] + self._DesignParameter['NMOS1InSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]) + (self._DesignParameter['NMOS1InSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)) - ((self._DesignParameter['NMOS1InSRLatch_0']['_XYCoordinates'][0][0] + self._DesignParameter['NMOS1InSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['NMOS1InSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2))), _YWidth=self._DesignParameter['PCCAM1_nu1']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'])
		self._DesignParameter['POLY_boundary_187']['_XYCoordinates'] = [[(+ self._DesignParameter['PCCAM1_nu1']['_XYCoordinates'][0][0]), (+ self._DesignParameter['PCCAM1_nu1']['_XYCoordinates'][0][1])]]
		path_list = []
		if (len(self._DesignParameter['NMOS1InSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates']) == 1):
		    mode = 'vertical'
		    _width = self._DesignParameter['NMOS1InSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
		elif (self._DesignParameter['NMOS1InSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0] == self._DesignParameter['NMOS1InSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]):
		    mode = 'horizontal'
		    _width = self._DesignParameter['NMOS1InSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
		elif (self._DesignParameter['NMOS1InSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1] == self._DesignParameter['NMOS1InSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][1]):
		    mode = 'vertical'
		    _width = self._DesignParameter['NMOS1InSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
		else:
		    print('Invalid Target Input')
		if (mode == 'vertical'):
		    xy_with_offset = []
		    target_y_value = (0 + self._DesignParameter['PCCAM1_nu1']['_XYCoordinates'][0][1])
		    for i in range(len(self._DesignParameter['NMOS1InSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
		        xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['NMOS1InSRLatch_0']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['NMOS1InSRLatch_0']['_XYCoordinates'][0][1])], self._DesignParameter['NMOS1InSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		elif (mode == 'horizontal'):
		    xy_with_offset = []
		    target_x_value = (0 + self._DesignParameter['PCCAM1_nu1']['_XYCoordinates'][0][0])
		    for i in range(len(self._DesignParameter['NMOS1InSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
		        xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['NMOS1InSRLatch_0']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['NMOS1InSRLatch_0']['_XYCoordinates'][0][1])], self._DesignParameter['NMOS1InSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		self._DesignParameter['nl1_gate_array'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _Width=_width)
		self._DesignParameter['nl1_gate_array']['_XYCoordinates'] = path_list
		nmos_via = max(max(1, (1 + int((((self._DesignParameter['NMOS1InSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] - drc._VIAxMinSpace) - (2 * drc._VIAxMinEnclosureByMetx)) / (drc._VIAxMinWidth + drc._VIAxMinSpace))))), 2)
		self._DesignParameter['nu1_drain_via12'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='nu1_drain_via12In{}'.format(_Name)))[0]
		self._DesignParameter['nu1_drain_via12']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(**dict(_ViaMet12Met2NumberOfCOX=1, _ViaMet12Met2NumberOfCOY=nmos_via))
		self._DesignParameter['nu1_drain_via12']['_XYCoordinates'] = None
		XYList = []
		xy_offset = (0, (- int(((drc._VIAxMinWidth + drc._VIAxMinSpace) / 4))))
		for i in range(len(self._DesignParameter['NMOS1InSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'])):
		    if ((i % 2) == 1):
		        xy = (self._DesignParameter['NMOS1InSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i][0] if (type(self._DesignParameter['NMOS1InSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i][0]) == list) else self._DesignParameter['NMOS1InSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i])
		        XYList.append([((x + y) + z) for (x, y, z) in zip([(0 + self._DesignParameter['NMOS1InSRLatch_0']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['NMOS1InSRLatch_0']['_XYCoordinates'][0][1])], xy, xy_offset)])
		self._DesignParameter['nu1_drain_via12']['_XYCoordinates'] = XYList
		self._DesignParameter['nu1_drain_via23'] = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_Name='nu1_drain_via23In{}'.format(_Name)))[0]
		self._DesignParameter['nu1_drain_via23']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureX(**dict(_ViaMet22Met3NumberOfCOX=1, _ViaMet22Met3NumberOfCOY=nmos_via))
		self._DesignParameter['nu1_drain_via23']['_XYCoordinates'] = None
		XYList = []
		xy_offset = [0, 0]
		for i in range(len(self._DesignParameter['nu1_drain_via12']['_XYCoordinates'])):
		    xy = (self._DesignParameter['nu1_drain_via12']['_XYCoordinates'][i][0] if (type(self._DesignParameter['nu1_drain_via12']['_XYCoordinates'][i][0]) == list) else self._DesignParameter['nu1_drain_via12']['_XYCoordinates'][i])
		    XYList.append([((x + y) + z) for (x, y, z) in zip([0, 0], xy, xy_offset)])
		self._DesignParameter['nu1_drain_via23']['_XYCoordinates'] = XYList
		self._DesignParameter['METAL2_path_26'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _Width=drc._MetalxMinWidth)
		self._DesignParameter['METAL2_path_26']['_XYCoordinates'] = [[[(+ self._DesignParameter['nu1_drain_via23']['_XYCoordinates'][0][0]), (+ self._DesignParameter['nu1_drain_via23']['_XYCoordinates'][0][1])], [(+ self._DesignParameter['nu1_drain_via23']['_XYCoordinates'][(- 1)][0]), (+ self._DesignParameter['nu1_drain_via23']['_XYCoordinates'][(- 1)][1])]]]
		nmos_via = max(max(1, (1 + int((((self._DesignParameter['NMOS2InSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] - drc._VIAxMinSpace) - (2 * drc._VIAxMinEnclosureByMetx)) / (drc._VIAxMinWidth + drc._VIAxMinSpace))))), 2)
		self._DesignParameter['nu2_drain_via12'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='nu2_drain_via12In{}'.format(_Name)))[0]
		self._DesignParameter['nu2_drain_via12']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(**dict(_ViaMet12Met2NumberOfCOX=1, _ViaMet12Met2NumberOfCOY=nmos_via))
		self._DesignParameter['nu2_drain_via12']['_XYCoordinates'] = None
		XYList = []
		xy_offset = (0, (- int(((drc._VIAxMinWidth + drc._VIAxMinSpace) / 4))))
		for i in range(len(self._DesignParameter['NMOS2InSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'])):
		    if ((i % 2) == 1):
		        xy = (self._DesignParameter['NMOS2InSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i][0] if (type(self._DesignParameter['NMOS2InSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i][0]) == list) else self._DesignParameter['NMOS2InSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i])
		        XYList.append([((x + y) + z) for (x, y, z) in zip([(0 + self._DesignParameter['NMOS2InSRLatch_0']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['NMOS2InSRLatch_0']['_XYCoordinates'][0][1])], xy, xy_offset)])
		self._DesignParameter['nu2_drain_via12']['_XYCoordinates'] = XYList
		nmos_via = max(max(1, (1 + int((((self._DesignParameter['NMOS3InSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] - drc._VIAxMinSpace) - (2 * drc._VIAxMinEnclosureByMetx)) / (drc._VIAxMinWidth + drc._VIAxMinSpace))))), 2)
		self._DesignParameter['nu3_s_via12'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='nu3_s_via12In{}'.format(_Name)))[0]
		self._DesignParameter['nu3_s_via12']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(**dict(_ViaMet12Met2NumberOfCOX=1, _ViaMet12Met2NumberOfCOY=nmos_via))
		self._DesignParameter['nu3_s_via12']['_XYCoordinates'] = None
		XYList = []
		xy_offset = (0, ((- int(((drc._VIAxMinWidth + drc._VIAxMinSpace) / 4))) * 2))
		for i in range(len(self._DesignParameter['NMOS3InSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'])):
		    if ((i % 2) == 0):
		        xy = (self._DesignParameter['NMOS3InSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i][0] if (type(self._DesignParameter['NMOS3InSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i][0]) == list) else self._DesignParameter['NMOS3InSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i])
		        XYList.append([((x + y) + z) for (x, y, z) in zip([(0 + self._DesignParameter['NMOS3InSRLatch_0']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['NMOS3InSRLatch_0']['_XYCoordinates'][0][1])], xy, xy_offset)])
		self._DesignParameter['nu3_s_via12']['_XYCoordinates'] = XYList
		self._DesignParameter['nu3_s_via23'] = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_Name='nu3_s_via23In{}'.format(_Name)))[0]
		self._DesignParameter['nu3_s_via23']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureX(**dict(_ViaMet22Met3NumberOfCOX=1, _ViaMet22Met3NumberOfCOY=nmos_via))
		self._DesignParameter['nu3_s_via23']['_XYCoordinates'] = None
		XYList = []
		xy_offset = [0, 0]
		for i in range(len(self._DesignParameter['nu3_s_via12']['_XYCoordinates'])):
		    xy = (self._DesignParameter['nu3_s_via12']['_XYCoordinates'][i][0] if (type(self._DesignParameter['nu3_s_via12']['_XYCoordinates'][i][0]) == list) else self._DesignParameter['nu3_s_via12']['_XYCoordinates'][i])
		    XYList.append([((x + y) + z) for (x, y, z) in zip([0, 0], xy, xy_offset)])
		self._DesignParameter['nu3_s_via23']['_XYCoordinates'] = XYList
		self._DesignParameter['nu3_d_via12'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='nu3_d_via12In{}'.format(_Name)))[0]
		self._DesignParameter['nu3_d_via12']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(**dict(_ViaMet12Met2NumberOfCOX=1, _ViaMet12Met2NumberOfCOY=nmos_via))
		self._DesignParameter['nu3_d_via12']['_XYCoordinates'] = None
		XYList = []
		xy_offset = [0, 0]
		for i in range(len(self._DesignParameter['NMOS3InSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'])):
		    if ((i % 2) == 1):
		        xy = (self._DesignParameter['NMOS3InSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i][0] if (type(self._DesignParameter['NMOS3InSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i][0]) == list) else self._DesignParameter['NMOS3InSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i])
		        XYList.append([((x + y) + z) for (x, y, z) in zip([(0 + self._DesignParameter['NMOS3InSRLatch_0']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['NMOS3InSRLatch_0']['_XYCoordinates'][0][1])], xy, xy_offset)])
		self._DesignParameter['nu3_d_via12']['_XYCoordinates'] = XYList
		nmos_via = max(max(1, (1 + int((((self._DesignParameter['NMOS4InSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] - drc._VIAxMinSpace) - (2 * drc._VIAxMinEnclosureByMetx)) / (drc._VIAxMinWidth + drc._VIAxMinSpace))))), 2)
		self._DesignParameter['nu4_d_via12'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='nu4_d_via12In{}'.format(_Name)))[0]
		self._DesignParameter['nu4_d_via12']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(**dict(_ViaMet12Met2NumberOfCOX=1, _ViaMet12Met2NumberOfCOY=nmos_via))
		self._DesignParameter['nu4_d_via12']['_XYCoordinates'] = None
		XYList = []
		xy_offset = [0, 0]
		for i in range(len(self._DesignParameter['NMOS4InSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'])):
		    if ((i % 2) == 1):
		        xy = (self._DesignParameter['NMOS4InSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i][0] if (type(self._DesignParameter['NMOS4InSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i][0]) == list) else self._DesignParameter['NMOS4InSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i])
		        XYList.append([((x + y) + z) for (x, y, z) in zip([(0 + self._DesignParameter['NMOS4InSRLatch_0']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['NMOS4InSRLatch_0']['_XYCoordinates'][0][1])], xy, xy_offset)])
		self._DesignParameter['nu4_d_via12']['_XYCoordinates'] = XYList
		self._DesignParameter['METAL2_path_20'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _Width=drc._MetalxMinWidth)
		self._DesignParameter['METAL2_path_20']['_XYCoordinates'] = [[[((self._DesignParameter['nu3_d_via12']['_XYCoordinates'][0][0] + self._DesignParameter['nu3_d_via12']['_DesignObj']._DesignParameter['_Met2Layer']['_XYCoordinates'][0][0]) - (self._DesignParameter['nu3_d_via12']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth'] / 2)), ((((self._DesignParameter['nu3_s_via23']['_XYCoordinates'][0][1] + self._DesignParameter['nu3_s_via23']['_DesignObj']._DesignParameter['_Met2Layer']['_XYCoordinates'][0][1]) + (self._DesignParameter['nu3_s_via23']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] / 2)) + drc._MetalxMinSpace3) + (drc._MetalxMinWidth / 2))], [((self._DesignParameter['nu4_d_via12']['_XYCoordinates'][(- 1)][0] + self._DesignParameter['nu4_d_via12']['_DesignObj']._DesignParameter['_Met2Layer']['_XYCoordinates'][0][0]) + (self._DesignParameter['nu4_d_via12']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth'] / 2)), ((((self._DesignParameter['nu3_s_via23']['_XYCoordinates'][0][1] + self._DesignParameter['nu3_s_via23']['_DesignObj']._DesignParameter['_Met2Layer']['_XYCoordinates'][0][1]) + (self._DesignParameter['nu3_s_via23']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] / 2)) + drc._MetalxMinSpace3) + (drc._MetalxMinWidth / 2))]]]
		cont_x = max(max(1, (1 + int(((((((self._DesignParameter['NMOS2InSRLatch_0']['_XYCoordinates'][0][0] + self._DesignParameter['NMOS2InSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]) + (self._DesignParameter['NMOS2InSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)) - ((self._DesignParameter['NMOS2InSRLatch_0']['_XYCoordinates'][0][0] + self._DesignParameter['NMOS2InSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['NMOS2InSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2))) - drc._CoMinSpace) - (2 * drc._CoMinEnclosureByPO)) / (drc._CoMinWidth + drc._CoMinSpace))))), 1)
		self._DesignParameter['PCCAM1_nu2'] = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_Name='PCCAM1_nu2In{}'.format(_Name)))[0]
		self._DesignParameter['PCCAM1_nu2']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(**dict(_ViaPoly2Met1NumberOfCOX=cont_x, _ViaPoly2Met1NumberOfCOY=1))
		self._DesignParameter['PCCAM1_nu2']['_XYCoordinates'] = [[self._DesignParameter['NMOS2InSRLatch_0']['_XYCoordinates'][0][0], (round((math.sqrt(((drc._PolygateMinSpace ** 2) - ((abs((((self._DesignParameter['NMOS2InSRLatch_0']['_XYCoordinates'][0][0] + self._DesignParameter['NMOS2InSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) - self._DesignParameter['NMOS2InSRLatch_0']['_XYCoordinates'][0][0]) + self._DesignParameter['NMOS2InSRLatch_0']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][0])) - ((self._DesignParameter['NMOS2InSRLatch_0']['_DesignObj']._DesignParameter['_PODummyLayer']['_XWidth'] + self._DesignParameter['PCCAM1_nu2']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']) / 2)) ** 2))) + (self._DesignParameter['PCCAM1_nu2']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2))) + ((self._DesignParameter['NMOS2InSRLatch_0']['_XYCoordinates'][0][1] + self._DesignParameter['NMOS2InSRLatch_0']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][1]) + (self._DesignParameter['NMOS2InSRLatch_0']['_DesignObj']._DesignParameter['_PODummyLayer']['_YWidth'] / 2)))]]
		path_list = []
		if (len(self._DesignParameter['NMOS2InSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates']) == 1):
		    mode = 'vertical'
		    _width = self._DesignParameter['NMOS2InSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
		elif (self._DesignParameter['NMOS2InSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0] == self._DesignParameter['NMOS2InSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]):
		    mode = 'horizontal'
		    _width = self._DesignParameter['NMOS2InSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
		elif (self._DesignParameter['NMOS2InSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1] == self._DesignParameter['NMOS2InSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][1]):
		    mode = 'vertical'
		    _width = self._DesignParameter['NMOS2InSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
		else:
		    print('Invalid Target Input')
		if (mode == 'vertical'):
		    xy_with_offset = []
		    target_y_value = (0 + self._DesignParameter['PCCAM1_nu2']['_XYCoordinates'][0][1])
		    for i in range(len(self._DesignParameter['NMOS2InSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
		        xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['NMOS2InSRLatch_0']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['NMOS2InSRLatch_0']['_XYCoordinates'][0][1])], self._DesignParameter['NMOS2InSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		elif (mode == 'horizontal'):
		    xy_with_offset = []
		    target_x_value = (0 + self._DesignParameter['PCCAM1_nu2']['_XYCoordinates'][0][0])
		    for i in range(len(self._DesignParameter['NMOS2InSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
		        xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['NMOS2InSRLatch_0']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['NMOS2InSRLatch_0']['_XYCoordinates'][0][1])], self._DesignParameter['NMOS2InSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		self._DesignParameter['nu2_gate_array'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _Width=_width)
		self._DesignParameter['nu2_gate_array']['_XYCoordinates'] = path_list
		self._DesignParameter['PCCAM1_nu_3'] = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_Name='PCCAM1_nu_3In{}'.format(_Name)))[0]
		self._DesignParameter['PCCAM1_nu_3']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(**dict(_ViaPoly2Met1NumberOfCOX=max(max(1, (1 + int(((((((self._DesignParameter['NMOS3InSRLatch_0']['_XYCoordinates'][0][0] + self._DesignParameter['NMOS3InSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) + (self._DesignParameter['NMOS3InSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)) - ((self._DesignParameter['NMOS3InSRLatch_0']['_XYCoordinates'][0][0] + self._DesignParameter['NMOS3InSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['NMOS3InSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2))) - drc._CoMinSpace) - (2 * drc._CoMinEnclosureByPO)) / (drc._CoMinWidth + drc._CoMinSpace))))), 1), _ViaPoly2Met1NumberOfCOY=1))
		self._DesignParameter['PCCAM1_nu_3']['_XYCoordinates'] = [[self._DesignParameter['NMOS3InSRLatch_0']['_XYCoordinates'][0][0], ((((self._DesignParameter['NMOS3InSRLatch_0']['_XYCoordinates'][0][1] + self._DesignParameter['NMOS3InSRLatch_0']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][1]) + (self._DesignParameter['NMOS3InSRLatch_0']['_DesignObj']._DesignParameter['_PODummyLayer']['_YWidth'] / 2)) + drc._PoDummyLengthToMove) + (self._DesignParameter['PCCAM1_nu_3']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2))]]
		self._DesignParameter['nu3_gate_vias'] = self._SrefElementDeclaration(_DesignObj=ViaStack._ViaStack(_Name='nu3_gate_viasIn{}'.format(_Name)))[0]
		self._DesignParameter['nu3_gate_vias']['_DesignObj']._CalculateStackMinimumEnclosureY(**dict(COX=2, COY=1, start_layer=1, end_layer=4))
		self._DesignParameter['nu3_gate_vias']['_XYCoordinates'] = [[self._DesignParameter['NMOS3InSRLatch_0']['_XYCoordinates'][0][0], (((self._DesignParameter['METAL2_path_20']['_XYCoordinates'][0][0][1] + (self._DesignParameter['METAL2_path_20']['_Width'] / 2)) + drc._MetalxMinSpace2) + (self._DesignParameter['nu3_gate_vias']['_DesignObj']._DesignParameter['ViaMet12Met2']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] / 2))]]
		self._DesignParameter['METAL1_boundary_195'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _XWidth=max(self._DesignParameter['nu3_gate_vias']['_DesignObj']._DesignParameter['ViaMet12Met2']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'], self._DesignParameter['PCCAM1_nu_3']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']), _YWidth=max(self._DesignParameter['nu3_gate_vias']['_DesignObj']._DesignParameter['ViaMet12Met2']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'], self._DesignParameter['PCCAM1_nu_3']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']))
		self._DesignParameter['METAL1_boundary_195']['_XYCoordinates'] = [[(+ self._DesignParameter['PCCAM1_nu_3']['_XYCoordinates'][0][0]), (+ self._DesignParameter['PCCAM1_nu_3']['_XYCoordinates'][0][1])]]
		self._DesignParameter['POLY_boundary_191'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _XWidth=(((self._DesignParameter['NMOS3InSRLatch_0']['_XYCoordinates'][0][0] + self._DesignParameter['NMOS3InSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]) + (self._DesignParameter['NMOS3InSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)) - ((self._DesignParameter['NMOS3InSRLatch_0']['_XYCoordinates'][0][0] + self._DesignParameter['NMOS3InSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['NMOS3InSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2))), _YWidth=self._DesignParameter['PCCAM1_nu_3']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'])
		self._DesignParameter['POLY_boundary_191']['_XYCoordinates'] = [[(+ self._DesignParameter['PCCAM1_nu_3']['_XYCoordinates'][0][0]), (+ self._DesignParameter['PCCAM1_nu_3']['_XYCoordinates'][0][1])]]
		path_list = []
		if (len(self._DesignParameter['NMOS3InSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates']) == 1):
		    mode = 'vertical'
		    _width = self._DesignParameter['NMOS3InSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
		elif (self._DesignParameter['NMOS3InSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0] == self._DesignParameter['NMOS3InSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]):
		    mode = 'horizontal'
		    _width = self._DesignParameter['NMOS3InSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
		elif (self._DesignParameter['NMOS3InSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1] == self._DesignParameter['NMOS3InSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][1]):
		    mode = 'vertical'
		    _width = self._DesignParameter['NMOS3InSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
		else:
		    print('Invalid Target Input')
		if (mode == 'vertical'):
		    xy_with_offset = []
		    target_y_value = (0 + self._DesignParameter['PCCAM1_nu_3']['_XYCoordinates'][0][1])
		    for i in range(len(self._DesignParameter['NMOS3InSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
		        xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['NMOS3InSRLatch_0']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['NMOS3InSRLatch_0']['_XYCoordinates'][0][1])], self._DesignParameter['NMOS3InSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		elif (mode == 'horizontal'):
		    xy_with_offset = []
		    target_x_value = (0 + self._DesignParameter['PCCAM1_nu_3']['_XYCoordinates'][0][0])
		    for i in range(len(self._DesignParameter['NMOS3InSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
		        xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['NMOS3InSRLatch_0']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['NMOS3InSRLatch_0']['_XYCoordinates'][0][1])], self._DesignParameter['NMOS3InSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		self._DesignParameter['nu3_gate_array'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _Width=_width)
		self._DesignParameter['nu3_gate_array']['_XYCoordinates'] = path_list
		self._DesignParameter['PCCAM1_nu4'] = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_Name='PCCAM1_nu4In{}'.format(_Name)))[0]
		self._DesignParameter['PCCAM1_nu4']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(**dict(_ViaPoly2Met1NumberOfCOX=max(max(1, (1 + int(((((((self._DesignParameter['NMOS4InSRLatch_0']['_XYCoordinates'][0][0] + self._DesignParameter['NMOS4InSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) + (self._DesignParameter['NMOS4InSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)) - ((self._DesignParameter['NMOS4InSRLatch_0']['_XYCoordinates'][0][0] + self._DesignParameter['NMOS4InSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['NMOS4InSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2))) - drc._CoMinSpace) - (2 * drc._CoMinEnclosureByPO)) / (drc._CoMinWidth + drc._CoMinSpace))))), 1), _ViaPoly2Met1NumberOfCOY=1))
		self._DesignParameter['PCCAM1_nu4']['_XYCoordinates'] = [[self._DesignParameter['NMOS4InSRLatch_0']['_XYCoordinates'][0][0], ((max(((self._DesignParameter['nu4_d_via12']['_XYCoordinates'][0][1] + self._DesignParameter['nu4_d_via12']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) + (self._DesignParameter['nu4_d_via12']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)), ((self._DesignParameter['NMOS4InSRLatch_0']['_XYCoordinates'][0][1] + self._DesignParameter['NMOS4InSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) + (self._DesignParameter['NMOS4InSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2))) + drc._Metal1MinSpace2) + (self._DesignParameter['PCCAM1_nu4']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2))]]
		self._DesignParameter['POLY_boundary_183'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _XWidth=(((self._DesignParameter['NMOS4InSRLatch_0']['_XYCoordinates'][0][0] + self._DesignParameter['NMOS4InSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]) + (self._DesignParameter['NMOS4InSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)) - ((self._DesignParameter['NMOS4InSRLatch_0']['_XYCoordinates'][0][0] + self._DesignParameter['NMOS4InSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['NMOS4InSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2))), _YWidth=self._DesignParameter['PCCAM1_nu4']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'])
		self._DesignParameter['POLY_boundary_183']['_XYCoordinates'] = [[(+ self._DesignParameter['PCCAM1_nu4']['_XYCoordinates'][0][0]), (+ self._DesignParameter['PCCAM1_nu4']['_XYCoordinates'][0][1])]]
		path_list = []
		if (len(self._DesignParameter['NMOS4InSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates']) == 1):
		    mode = 'vertical'
		    _width = self._DesignParameter['NMOS4InSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
		elif (self._DesignParameter['NMOS4InSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0] == self._DesignParameter['NMOS4InSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]):
		    mode = 'horizontal'
		    _width = self._DesignParameter['NMOS4InSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
		elif (self._DesignParameter['NMOS4InSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1] == self._DesignParameter['NMOS4InSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][1]):
		    mode = 'vertical'
		    _width = self._DesignParameter['NMOS4InSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
		else:
		    print('Invalid Target Input')
		if (mode == 'vertical'):
		    xy_with_offset = []
		    target_y_value = (0 + self._DesignParameter['PCCAM1_nu4']['_XYCoordinates'][0][1])
		    for i in range(len(self._DesignParameter['NMOS4InSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
		        xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['NMOS4InSRLatch_0']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['NMOS4InSRLatch_0']['_XYCoordinates'][0][1])], self._DesignParameter['NMOS4InSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		elif (mode == 'horizontal'):
		    xy_with_offset = []
		    target_x_value = (0 + self._DesignParameter['PCCAM1_nu4']['_XYCoordinates'][0][0])
		    for i in range(len(self._DesignParameter['NMOS4InSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
		        xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['NMOS4InSRLatch_0']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['NMOS4InSRLatch_0']['_XYCoordinates'][0][1])], self._DesignParameter['NMOS4InSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		self._DesignParameter['nu4_gate_array'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _Width=_width)
		self._DesignParameter['nu4_gate_array']['_XYCoordinates'] = path_list
		pmos_via = max(1, (1 + int((((self._DesignParameter['PMOS1InSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] - drc._VIAxMinSpace) - (2 * drc._VIAxMinEnclosureByMetx)) / (drc._VIAxMinWidth + drc._VIAxMinSpace)))))
		self._DesignParameter['pu_drain_vias'] = self._SrefElementDeclaration(_DesignObj=ViaStack._ViaStack(_Name='pu_drain_viasIn{}'.format(_Name)))[0]
		self._DesignParameter['pu_drain_vias']['_DesignObj']._CalculateStackMinimumEnclosureX(**dict(COX=1, COY=pmos_via, start_layer=1, end_layer=3))
		self._DesignParameter['pu_drain_vias']['_XYCoordinates'] = None
		XYList = []
		xy_offset = [0, 0]
		for i in range(len(self._DesignParameter['PMOS1InSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'])):
		    if ((i % 2) == 1):
		        xy = (self._DesignParameter['PMOS1InSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i][0] if (type(self._DesignParameter['PMOS1InSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i][0]) == list) else self._DesignParameter['PMOS1InSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i])
		        XYList.append([((x + y) + z) for (x, y, z) in zip([(0 + self._DesignParameter['PMOS1InSRLatch_0']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['PMOS1InSRLatch_0']['_XYCoordinates'][0][1])], xy, xy_offset)])
		self._DesignParameter['pu_drain_vias']['_XYCoordinates'] = XYList
		path_list = []
		if (len(self._DesignParameter['PMOS1InSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates']) == 1):
		    mode = 'vertical'
		    _width = self._DesignParameter['PMOS1InSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
		elif (self._DesignParameter['PMOS1InSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0] == self._DesignParameter['PMOS1InSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][(- 1)][0]):
		    mode = 'horizontal'
		    _width = self._DesignParameter['PMOS1InSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
		elif (self._DesignParameter['PMOS1InSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1] == self._DesignParameter['PMOS1InSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][(- 1)][1]):
		    mode = 'vertical'
		    _width = self._DesignParameter['PMOS1InSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
		else:
		    print('Invalid Target Input')
		if (mode == 'vertical'):
		    xy_with_offset = []
		    target_y_value = (0 + self._DesignParameter['VDD_up']['_XYCoordinates'][0][1])
		    for i in range(len(self._DesignParameter['PMOS1InSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'])):
		        if ((i % 2) == 0):
		            xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['PMOS1InSRLatch_0']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['PMOS1InSRLatch_0']['_XYCoordinates'][0][1])], self._DesignParameter['PMOS1InSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		elif (mode == 'horizontal'):
		    xy_with_offset = []
		    target_x_value = (0 + self._DesignParameter['VDD_up']['_XYCoordinates'][0][0])
		    for i in range(len(self._DesignParameter['PMOS1InSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'])):
		        if ((i % 2) == 0):
		            xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['PMOS1InSRLatch_0']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['PMOS1InSRLatch_0']['_XYCoordinates'][0][1])], self._DesignParameter['PMOS1InSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		self._DesignParameter['pu1_supply'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=_width)
		self._DesignParameter['pu1_supply']['_XYCoordinates'] = path_list
		self._DesignParameter['PCCAM1_pu1'] = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_Name='PCCAM1_pu1In{}'.format(_Name)))[0]
		self._DesignParameter['PCCAM1_pu1']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(**dict(_ViaPoly2Met1NumberOfCOX=5, _ViaPoly2Met1NumberOfCOY=1))
		self._DesignParameter['PCCAM1_pu1']['_XYCoordinates'] = [[self._DesignParameter['PMOS1InSRLatch_0']['_XYCoordinates'][0][0], ((((self._DesignParameter['PMOS1InSRLatch_0']['_XYCoordinates'][0][1] + self._DesignParameter['PMOS1InSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) - (self._DesignParameter['PMOS1InSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)) - drc._Metal1MinSpace2) - (self._DesignParameter['PCCAM1_pu1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2))]]
		self._DesignParameter['pu1_gate_vias'] = self._SrefElementDeclaration(_DesignObj=ViaStack._ViaStack(_Name='pu1_gate_viasIn{}'.format(_Name)))[0]
		self._DesignParameter['pu1_gate_vias']['_DesignObj']._CalculateStackMinimumEnclosureY(**dict(COX=max(1, (1 + int(((((((self._DesignParameter['PMOS1InSRLatch_0']['_XYCoordinates'][0][0] + self._DesignParameter['PMOS1InSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]) + (self._DesignParameter['PMOS1InSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)) - ((self._DesignParameter['PMOS1InSRLatch_0']['_XYCoordinates'][0][0] + self._DesignParameter['PMOS1InSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['PMOS1InSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2))) - drc._VIAxMinSpace) - (2 * drc._VIAxMinEnclosureByMetx)) / (drc._VIAxMinWidth + drc._VIAxMinSpace))))), COY=1, start_layer=1, end_layer=3))
		self._DesignParameter['pu1_gate_vias']['_XYCoordinates'] = [[(+ self._DesignParameter['PCCAM1_pu1']['_XYCoordinates'][0][0]), (+ self._DesignParameter['PCCAM1_pu1']['_XYCoordinates'][0][1])]]
		self._DesignParameter['POLY_boundary_189'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _XWidth=(((self._DesignParameter['PMOS1InSRLatch_0']['_XYCoordinates'][0][0] + self._DesignParameter['PMOS1InSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]) + (self._DesignParameter['PMOS1InSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)) - ((self._DesignParameter['PMOS1InSRLatch_0']['_XYCoordinates'][0][0] + self._DesignParameter['PMOS1InSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['PMOS1InSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2))), _YWidth=self._DesignParameter['PCCAM1_pu1']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'])
		self._DesignParameter['POLY_boundary_189']['_XYCoordinates'] = [[(+ self._DesignParameter['PCCAM1_pu1']['_XYCoordinates'][0][0]), (+ self._DesignParameter['PCCAM1_pu1']['_XYCoordinates'][0][1])]]
		self._DesignParameter['METAL1_boundary_193'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _XWidth=max(self._DesignParameter['PCCAM1_pu1']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'], self._DesignParameter['pu1_gate_vias']['_DesignObj']._DesignParameter['ViaMet12Met2']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']), _YWidth=max(self._DesignParameter['pu1_gate_vias']['_DesignObj']._DesignParameter['ViaMet12Met2']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'], self._DesignParameter['PCCAM1_pu1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']))
		self._DesignParameter['METAL1_boundary_193']['_XYCoordinates'] = [[(+ self._DesignParameter['PCCAM1_pu1']['_XYCoordinates'][0][0]), (+ self._DesignParameter['PCCAM1_pu1']['_XYCoordinates'][0][1])]]
		path_list = []
		if (len(self._DesignParameter['PMOS1InSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates']) == 1):
		    mode = 'vertical'
		    _width = self._DesignParameter['PMOS1InSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
		elif (self._DesignParameter['PMOS1InSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0] == self._DesignParameter['PMOS1InSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]):
		    mode = 'horizontal'
		    _width = self._DesignParameter['PMOS1InSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
		elif (self._DesignParameter['PMOS1InSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1] == self._DesignParameter['PMOS1InSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][1]):
		    mode = 'vertical'
		    _width = self._DesignParameter['PMOS1InSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
		else:
		    print('Invalid Target Input')
		if (mode == 'vertical'):
		    xy_with_offset = []
		    target_y_value = (0 + self._DesignParameter['PCCAM1_pu1']['_XYCoordinates'][0][1])
		    for i in range(len(self._DesignParameter['PMOS1InSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
		        xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['PMOS1InSRLatch_0']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['PMOS1InSRLatch_0']['_XYCoordinates'][0][1])], self._DesignParameter['PMOS1InSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		elif (mode == 'horizontal'):
		    xy_with_offset = []
		    target_x_value = (0 + self._DesignParameter['PCCAM1_pu1']['_XYCoordinates'][0][0])
		    for i in range(len(self._DesignParameter['PMOS1InSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
		        xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['PMOS1InSRLatch_0']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['PMOS1InSRLatch_0']['_XYCoordinates'][0][1])], self._DesignParameter['PMOS1InSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		self._DesignParameter['pu1_gate_array'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _Width=_width)
		self._DesignParameter['pu1_gate_array']['_XYCoordinates'] = path_list
		self._DesignParameter['METAL2_path_24'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _Width=drc._MetalxMinWidth)
		self._DesignParameter['METAL2_path_24']['_XYCoordinates'] = [[[(+ self._DesignParameter['pu_drain_vias']['_XYCoordinates'][0][0]), (+ self._DesignParameter['pu_drain_vias']['_XYCoordinates'][0][1])], [(+ self._DesignParameter['pu_drain_vias']['_XYCoordinates'][(- 1)][0]), (+ self._DesignParameter['pu_drain_vias']['_XYCoordinates'][(- 1)][1])]]]
		path_list = []
		if (len(self._DesignParameter['PMOS1_rInSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates']) == 1):
		    mode = 'vertical'
		    _width = self._DesignParameter['PMOS1_rInSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
		elif (self._DesignParameter['PMOS1_rInSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0] == self._DesignParameter['PMOS1_rInSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][(- 1)][0]):
		    mode = 'horizontal'
		    _width = self._DesignParameter['PMOS1_rInSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
		elif (self._DesignParameter['PMOS1_rInSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1] == self._DesignParameter['PMOS1_rInSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][(- 1)][1]):
		    mode = 'vertical'
		    _width = self._DesignParameter['PMOS1_rInSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
		else:
		    print('Invalid Target Input')
		if (mode == 'vertical'):
		    xy_with_offset = []
		    target_y_value = (0 + self._DesignParameter['VDD_down']['_XYCoordinates'][0][1])
		    for i in range(len(self._DesignParameter['PMOS1_rInSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'])):
		        if ((i % 2) == 0):
		            xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['PMOS1_rInSRLatch_0']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['PMOS1_rInSRLatch_0']['_XYCoordinates'][0][1])], self._DesignParameter['PMOS1_rInSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		elif (mode == 'horizontal'):
		    xy_with_offset = []
		    target_x_value = (0 + self._DesignParameter['VDD_down']['_XYCoordinates'][0][0])
		    for i in range(len(self._DesignParameter['PMOS1_rInSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'])):
		        if ((i % 2) == 0):
		            xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['PMOS1_rInSRLatch_0']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['PMOS1_rInSRLatch_0']['_XYCoordinates'][0][1])], self._DesignParameter['PMOS1_rInSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		self._DesignParameter['pd_1_supply'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=_width)
		self._DesignParameter['pd_1_supply']['_XYCoordinates'] = path_list
		path_list = []
		if (len(self._DesignParameter['PMOS2_rInSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates']) == 1):
		    mode = 'vertical'
		    _width = self._DesignParameter['PMOS2_rInSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
		elif (self._DesignParameter['PMOS2_rInSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0] == self._DesignParameter['PMOS2_rInSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][(- 1)][0]):
		    mode = 'horizontal'
		    _width = self._DesignParameter['PMOS2_rInSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
		elif (self._DesignParameter['PMOS2_rInSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1] == self._DesignParameter['PMOS2_rInSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][(- 1)][1]):
		    mode = 'vertical'
		    _width = self._DesignParameter['PMOS2_rInSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
		else:
		    print('Invalid Target Input')
		if (mode == 'vertical'):
		    xy_with_offset = []
		    target_y_value = (0 + self._DesignParameter['VDD_down']['_XYCoordinates'][0][1])
		    for i in range(len(self._DesignParameter['PMOS2_rInSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'])):
		        if ((i % 2) == 0):
		            xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['PMOS2_rInSRLatch_0']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['PMOS2_rInSRLatch_0']['_XYCoordinates'][0][1])], self._DesignParameter['PMOS2_rInSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		elif (mode == 'horizontal'):
		    xy_with_offset = []
		    target_x_value = (0 + self._DesignParameter['VDD_down']['_XYCoordinates'][0][0])
		    for i in range(len(self._DesignParameter['PMOS2_rInSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'])):
		        if ((i % 2) == 0):
		            xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['PMOS2_rInSRLatch_0']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['PMOS2_rInSRLatch_0']['_XYCoordinates'][0][1])], self._DesignParameter['PMOS2_rInSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		self._DesignParameter['pd2_supply'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=_width)
		self._DesignParameter['pd2_supply']['_XYCoordinates'] = path_list
		path_list = []
		if (len(self._DesignParameter['PMOS4_rInSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates']) == 1):
		    mode = 'vertical'
		    _width = self._DesignParameter['PMOS4_rInSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
		elif (self._DesignParameter['PMOS4_rInSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0] == self._DesignParameter['PMOS4_rInSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][(- 1)][0]):
		    mode = 'horizontal'
		    _width = self._DesignParameter['PMOS4_rInSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
		elif (self._DesignParameter['PMOS4_rInSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1] == self._DesignParameter['PMOS4_rInSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][(- 1)][1]):
		    mode = 'vertical'
		    _width = self._DesignParameter['PMOS4_rInSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
		else:
		    print('Invalid Target Input')
		if (mode == 'vertical'):
		    xy_with_offset = []
		    target_y_value = (0 + self._DesignParameter['VDD_down']['_XYCoordinates'][0][1])
		    for i in range(len(self._DesignParameter['PMOS4_rInSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'])):
		        if ((i % 2) == 0):
		            xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['PMOS4_rInSRLatch_0']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['PMOS4_rInSRLatch_0']['_XYCoordinates'][0][1])], self._DesignParameter['PMOS4_rInSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		elif (mode == 'horizontal'):
		    xy_with_offset = []
		    target_x_value = (0 + self._DesignParameter['VDD_down']['_XYCoordinates'][0][0])
		    for i in range(len(self._DesignParameter['PMOS4_rInSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'])):
		        if ((i % 2) == 0):
		            xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['PMOS4_rInSRLatch_0']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['PMOS4_rInSRLatch_0']['_XYCoordinates'][0][1])], self._DesignParameter['PMOS4_rInSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		self._DesignParameter['pd4_supply'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=_width)
		self._DesignParameter['pd4_supply']['_XYCoordinates'] = path_list
		path_list = []
		if (len(self._DesignParameter['PMOS2InSRLatch_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates']) == 1):
		    mode = 'vertical'
		    _width = self._DesignParameter['PMOS2InSRLatch_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth']
		elif (self._DesignParameter['PMOS2InSRLatch_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][0] == self._DesignParameter['PMOS2InSRLatch_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][0]):
		    mode = 'horizontal'
		    _width = self._DesignParameter['PMOS2InSRLatch_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth']
		elif (self._DesignParameter['PMOS2InSRLatch_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1] == self._DesignParameter['PMOS2InSRLatch_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][1]):
		    mode = 'vertical'
		    _width = self._DesignParameter['PMOS2InSRLatch_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth']
		else:
		    print('Invalid Target Input')
		if (mode == 'vertical'):
		    xy_with_offset = []
		    target_y_value = (0 + self._DesignParameter['VDD_up']['_XYCoordinates'][0][1])
		    for i in range(len(self._DesignParameter['PMOS2InSRLatch_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		        if ((i % 2) == 0):
		            xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['PMOS2InSRLatch_0']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['PMOS2InSRLatch_0']['_XYCoordinates'][0][1])], self._DesignParameter['PMOS2InSRLatch_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		elif (mode == 'horizontal'):
		    xy_with_offset = []
		    target_x_value = (0 + self._DesignParameter['VDD_up']['_XYCoordinates'][0][0])
		    for i in range(len(self._DesignParameter['PMOS2InSRLatch_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		        if ((i % 2) == 0):
		            xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['PMOS2InSRLatch_0']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['PMOS2InSRLatch_0']['_XYCoordinates'][0][1])], self._DesignParameter['PMOS2InSRLatch_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		self._DesignParameter['pu2_supply'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=_width)
		self._DesignParameter['pu2_supply']['_XYCoordinates'] = path_list
		path_list = []
		if (len(self._DesignParameter['PMOS4InSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates']) == 1):
		    mode = 'vertical'
		    _width = self._DesignParameter['PMOS4InSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
		elif (self._DesignParameter['PMOS4InSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0] == self._DesignParameter['PMOS4InSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][(- 1)][0]):
		    mode = 'horizontal'
		    _width = self._DesignParameter['PMOS4InSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
		elif (self._DesignParameter['PMOS4InSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1] == self._DesignParameter['PMOS4InSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][(- 1)][1]):
		    mode = 'vertical'
		    _width = self._DesignParameter['PMOS4InSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
		else:
		    print('Invalid Target Input')
		if (mode == 'vertical'):
		    xy_with_offset = []
		    target_y_value = (0 + self._DesignParameter['VDD_up']['_XYCoordinates'][0][1])
		    for i in range(len(self._DesignParameter['PMOS4InSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'])):
		        if ((i % 2) == 0):
		            xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['PMOS4InSRLatch_0']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['PMOS4InSRLatch_0']['_XYCoordinates'][0][1])], self._DesignParameter['PMOS4InSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		elif (mode == 'horizontal'):
		    xy_with_offset = []
		    target_x_value = (0 + self._DesignParameter['VDD_up']['_XYCoordinates'][0][0])
		    for i in range(len(self._DesignParameter['PMOS4InSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'])):
		        if ((i % 2) == 0):
		            xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['PMOS4InSRLatch_0']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['PMOS4InSRLatch_0']['_XYCoordinates'][0][1])], self._DesignParameter['PMOS4InSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		self._DesignParameter['pu4_supply'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=_width)
		self._DesignParameter['pu4_supply']['_XYCoordinates'] = path_list
		pmos_via = max(1, (1 + int((((self._DesignParameter['PMOS1_rInSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] - drc._VIAxMinSpace) - (2 * drc._VIAxMinEnclosureByMetx)) / (drc._VIAxMinWidth + drc._VIAxMinSpace)))))
		self._DesignParameter['pd1_drain_vias'] = self._SrefElementDeclaration(_DesignObj=ViaStack._ViaStack(_Name='pd1_drain_viasIn{}'.format(_Name)))[0]
		self._DesignParameter['pd1_drain_vias']['_DesignObj']._CalculateStackMinimumEnclosureX(**dict(COX=1, COY=pmos_via, start_layer=1, end_layer=3))
		self._DesignParameter['pd1_drain_vias']['_XYCoordinates'] = None
		XYList = []
		xy_offset = [0, 0]
		for i in range(len(self._DesignParameter['PMOS1_rInSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'])):
		    if ((i % 2) == 1):
		        xy = (self._DesignParameter['PMOS1_rInSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i][0] if (type(self._DesignParameter['PMOS1_rInSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i][0]) == list) else self._DesignParameter['PMOS1_rInSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i])
		        XYList.append([((x + y) + z) for (x, y, z) in zip([(0 + self._DesignParameter['PMOS1_rInSRLatch_0']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['PMOS1_rInSRLatch_0']['_XYCoordinates'][0][1])], xy, xy_offset)])
		self._DesignParameter['pd1_drain_vias']['_XYCoordinates'] = XYList
		self._DesignParameter['METAL2_path_23'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _Width=drc._MetalxMinWidth)
		self._DesignParameter['METAL2_path_23']['_XYCoordinates'] = [[[(+ self._DesignParameter['pd1_drain_vias']['_XYCoordinates'][0][0]), (+ self._DesignParameter['pd1_drain_vias']['_XYCoordinates'][0][1])], [(+ self._DesignParameter['pd1_drain_vias']['_XYCoordinates'][(- 1)][0]), (+ self._DesignParameter['pd1_drain_vias']['_XYCoordinates'][(- 1)][1])]]]
		self._DesignParameter['nd1_drain_vias'] = self._SrefElementDeclaration(_DesignObj=ViaStack._ViaStack(_Name='nd1_drain_viasIn{}'.format(_Name)))[0]
		self._DesignParameter['nd1_drain_vias']['_DesignObj']._CalculateStackMinimumEnclosureX(**dict(COX=1, COY=nmos_via, start_layer=1, end_layer=3))
		self._DesignParameter['nd1_drain_vias']['_XYCoordinates'] = None
		XYList = []
		xy_offset = (0, int(((drc._VIAxMinWidth + drc._VIAxMinSpace) / 4)))
		for i in range(len(self._DesignParameter['NMOS1_rInSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'])):
		    if ((i % 2) == 1):
		        xy = (self._DesignParameter['NMOS1_rInSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i][0] if (type(self._DesignParameter['NMOS1_rInSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i][0]) == list) else self._DesignParameter['NMOS1_rInSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i])
		        XYList.append([((x + y) + z) for (x, y, z) in zip([(0 + self._DesignParameter['NMOS1_rInSRLatch_0']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['NMOS1_rInSRLatch_0']['_XYCoordinates'][0][1])], xy, xy_offset)])
		self._DesignParameter['nd1_drain_vias']['_XYCoordinates'] = XYList
		self._DesignParameter['PCCAM1_pd1'] = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_Name='PCCAM1_pd1In{}'.format(_Name)))[0]
		self._DesignParameter['PCCAM1_pd1']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(**dict(_ViaPoly2Met1NumberOfCOX=max(1, (1 + int(((((((self._DesignParameter['PMOS1_rInSRLatch_0']['_XYCoordinates'][0][0] + self._DesignParameter['PMOS1_rInSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]) + (self._DesignParameter['PMOS1_rInSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)) - ((self._DesignParameter['PMOS1_rInSRLatch_0']['_XYCoordinates'][0][0] + self._DesignParameter['PMOS1_rInSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['PMOS1_rInSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2))) - drc._CoMinSpace) - (2 * drc._CoMinEnclosureByPO)) / (drc._CoMinWidth + drc._CoMinSpace))))), _ViaPoly2Met1NumberOfCOY=1))
		self._DesignParameter['PCCAM1_pd1']['_XYCoordinates'] = [[self._DesignParameter['PMOS1_rInSRLatch_0']['_XYCoordinates'][0][0], ((((self._DesignParameter['PMOS1_rInSRLatch_0']['_XYCoordinates'][0][1] + self._DesignParameter['PMOS1_rInSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) + (self._DesignParameter['PMOS1_rInSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)) + drc._Metal1MinSpace2) + (self._DesignParameter['PCCAM1_pd1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2))]]
		self._DesignParameter['pd1_gate_vias'] = self._SrefElementDeclaration(_DesignObj=ViaStack._ViaStack(_Name='pd1_gate_viasIn{}'.format(_Name)))[0]
		self._DesignParameter['pd1_gate_vias']['_DesignObj']._CalculateStackMinimumEnclosureY(**dict(COX=max(1, (1 + int(((((((self._DesignParameter['PMOS1_rInSRLatch_0']['_XYCoordinates'][0][0] + self._DesignParameter['PMOS1_rInSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]) + (self._DesignParameter['PMOS1_rInSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)) - ((self._DesignParameter['PMOS1_rInSRLatch_0']['_XYCoordinates'][0][0] + self._DesignParameter['PMOS1_rInSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['PMOS1_rInSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2))) - drc._VIAxMinSpace) - (2 * drc._VIAxMinEnclosureByMetx)) / (drc._VIAxMinWidth + drc._VIAxMinSpace))))), COY=1, start_layer=1, end_layer=4))
		self._DesignParameter['pd1_gate_vias']['_XYCoordinates'] = [[(+ self._DesignParameter['PCCAM1_pd1']['_XYCoordinates'][0][0]), (+ self._DesignParameter['PCCAM1_pd1']['_XYCoordinates'][0][1])]]
		self._DesignParameter['POLY_boundary_188'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _XWidth=(((self._DesignParameter['PMOS1_rInSRLatch_0']['_XYCoordinates'][0][0] + self._DesignParameter['PMOS1_rInSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]) + (self._DesignParameter['PMOS1_rInSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)) - ((self._DesignParameter['PMOS1_rInSRLatch_0']['_XYCoordinates'][0][0] + self._DesignParameter['PMOS1_rInSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['PMOS1_rInSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2))), _YWidth=self._DesignParameter['PCCAM1_pd1']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'])
		self._DesignParameter['POLY_boundary_188']['_XYCoordinates'] = [[(+ self._DesignParameter['PCCAM1_pd1']['_XYCoordinates'][0][0]), (+ self._DesignParameter['PCCAM1_pd1']['_XYCoordinates'][0][1])]]
		self._DesignParameter['METAL1_boundary_192'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _XWidth=max(self._DesignParameter['pd1_gate_vias']['_DesignObj']._DesignParameter['ViaMet12Met2']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'], self._DesignParameter['PCCAM1_pd1']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']), _YWidth=max(self._DesignParameter['PCCAM1_pd1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'], self._DesignParameter['pd1_gate_vias']['_DesignObj']._DesignParameter['ViaMet12Met2']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']))
		self._DesignParameter['METAL1_boundary_192']['_XYCoordinates'] = [[(+ self._DesignParameter['PCCAM1_pd1']['_XYCoordinates'][0][0]), (+ self._DesignParameter['PCCAM1_pd1']['_XYCoordinates'][0][1])]]
		path_list = []
		if (len(self._DesignParameter['PMOS1_rInSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates']) == 1):
		    mode = 'vertical'
		    _width = self._DesignParameter['PMOS1_rInSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
		elif (self._DesignParameter['PMOS1_rInSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0] == self._DesignParameter['PMOS1_rInSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]):
		    mode = 'horizontal'
		    _width = self._DesignParameter['PMOS1_rInSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
		elif (self._DesignParameter['PMOS1_rInSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1] == self._DesignParameter['PMOS1_rInSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][1]):
		    mode = 'vertical'
		    _width = self._DesignParameter['PMOS1_rInSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
		else:
		    print('Invalid Target Input')
		if (mode == 'vertical'):
		    xy_with_offset = []
		    target_y_value = (0 + self._DesignParameter['POLY_boundary_188']['_XYCoordinates'][0][1])
		    for i in range(len(self._DesignParameter['PMOS1_rInSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
		        xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['PMOS1_rInSRLatch_0']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['PMOS1_rInSRLatch_0']['_XYCoordinates'][0][1])], self._DesignParameter['PMOS1_rInSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		elif (mode == 'horizontal'):
		    xy_with_offset = []
		    target_x_value = (0 + self._DesignParameter['POLY_boundary_188']['_XYCoordinates'][0][0])
		    for i in range(len(self._DesignParameter['PMOS1_rInSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
		        xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['PMOS1_rInSRLatch_0']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['PMOS1_rInSRLatch_0']['_XYCoordinates'][0][1])], self._DesignParameter['PMOS1_rInSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		self._DesignParameter['pd1_gate_array'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _Width=_width)
		self._DesignParameter['pd1_gate_array']['_XYCoordinates'] = path_list
		self._DesignParameter['PCCAM1_nd1'] = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_Name='PCCAM1_nd1In{}'.format(_Name)))[0]
		self._DesignParameter['PCCAM1_nd1']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(**dict(_ViaPoly2Met1NumberOfCOX=max(1, (1 + int(((((((self._DesignParameter['NMOS1_rInSRLatch_0']['_XYCoordinates'][0][0] + self._DesignParameter['NMOS1_rInSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]) + (self._DesignParameter['NMOS1_rInSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)) - ((self._DesignParameter['NMOS1_rInSRLatch_0']['_XYCoordinates'][0][0] + self._DesignParameter['NMOS1_rInSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['NMOS1_rInSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2))) - drc._CoMinSpace) - (2 * drc._CoMinEnclosureByPO)) / (drc._CoMinWidth + drc._CoMinSpace))))), _ViaPoly2Met1NumberOfCOY=1))
		self._DesignParameter['PCCAM1_nd1']['_XYCoordinates'] = [[self._DesignParameter['NMOS1_rInSRLatch_0']['_XYCoordinates'][0][0], ((((self._DesignParameter['NMOS1_rInSRLatch_0']['_XYCoordinates'][0][1] + self._DesignParameter['NMOS1_rInSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) - (self._DesignParameter['NMOS1_rInSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)) - drc._Metal1MinSpace2) - (self._DesignParameter['PCCAM1_nd1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2))]]
		self._DesignParameter['M1V1M2_nd1_gate'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='M1V1M2_nd1_gateIn{}'.format(_Name)))[0]
		self._DesignParameter['M1V1M2_nd1_gate']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureY(**dict(_ViaMet12Met2NumberOfCOX=max(1, (1 + int(((((((self._DesignParameter['NMOS1_rInSRLatch_0']['_XYCoordinates'][0][0] + self._DesignParameter['NMOS1_rInSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]) + (self._DesignParameter['NMOS1_rInSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)) - ((self._DesignParameter['NMOS1_rInSRLatch_0']['_XYCoordinates'][0][0] + self._DesignParameter['NMOS1_rInSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['NMOS1_rInSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2))) - drc._VIAxMinSpace) - (2 * drc._VIAxMinEnclosureByMetx)) / (drc._VIAxMinWidth + drc._VIAxMinSpace))))), _ViaMet12Met2NumberOfCOY=1))
		self._DesignParameter['M1V1M2_nd1_gate']['_XYCoordinates'] = [[(+ self._DesignParameter['PCCAM1_nd1']['_XYCoordinates'][0][0]), (+ self._DesignParameter['PCCAM1_nd1']['_XYCoordinates'][0][1])]]
		self._DesignParameter['METAL1_boundary_190'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _XWidth=max(self._DesignParameter['PCCAM1_nd1']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'], self._DesignParameter['M1V1M2_nd1_gate']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']), _YWidth=max(self._DesignParameter['PCCAM1_nd1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'], self._DesignParameter['M1V1M2_nd1_gate']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']))
		self._DesignParameter['METAL1_boundary_190']['_XYCoordinates'] = [[(+ self._DesignParameter['PCCAM1_nd1']['_XYCoordinates'][0][0]), (+ self._DesignParameter['PCCAM1_nd1']['_XYCoordinates'][0][1])]]
		self._DesignParameter['POLY_boundary_186'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _XWidth=(((self._DesignParameter['NMOS1_rInSRLatch_0']['_XYCoordinates'][0][0] + self._DesignParameter['NMOS1_rInSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]) + (self._DesignParameter['NMOS1_rInSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)) - ((self._DesignParameter['NMOS1_rInSRLatch_0']['_XYCoordinates'][0][0] + self._DesignParameter['NMOS1_rInSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['NMOS1_rInSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2))), _YWidth=self._DesignParameter['PCCAM1_nd1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'])
		self._DesignParameter['POLY_boundary_186']['_XYCoordinates'] = [[(+ self._DesignParameter['PCCAM1_nd1']['_XYCoordinates'][0][0]), (+ self._DesignParameter['PCCAM1_nd1']['_XYCoordinates'][0][1])]]
		path_list = []
		if (len(self._DesignParameter['NMOS1_rInSRLatch_0']['_DesignObj']._DesignParameter['_POLayerPINDrawing']['_XYCoordinates']) == 1):
		    mode = 'vertical'
		    _width = self._DesignParameter['NMOS1_rInSRLatch_0']['_DesignObj']._DesignParameter['_POLayerPINDrawing']['_XWidth']
		elif (self._DesignParameter['NMOS1_rInSRLatch_0']['_DesignObj']._DesignParameter['_POLayerPINDrawing']['_XYCoordinates'][0][0] == self._DesignParameter['NMOS1_rInSRLatch_0']['_DesignObj']._DesignParameter['_POLayerPINDrawing']['_XYCoordinates'][(- 1)][0]):
		    mode = 'horizontal'
		    _width = self._DesignParameter['NMOS1_rInSRLatch_0']['_DesignObj']._DesignParameter['_POLayerPINDrawing']['_XWidth']
		elif (self._DesignParameter['NMOS1_rInSRLatch_0']['_DesignObj']._DesignParameter['_POLayerPINDrawing']['_XYCoordinates'][0][1] == self._DesignParameter['NMOS1_rInSRLatch_0']['_DesignObj']._DesignParameter['_POLayerPINDrawing']['_XYCoordinates'][(- 1)][1]):
		    mode = 'vertical'
		    _width = self._DesignParameter['NMOS1_rInSRLatch_0']['_DesignObj']._DesignParameter['_POLayerPINDrawing']['_XWidth']
		else:
		    print('Invalid Target Input')
		if (mode == 'vertical'):
		    xy_with_offset = []
		    target_y_value = (0 + self._DesignParameter['POLY_boundary_186']['_XYCoordinates'][0][1])
		    for i in range(len(self._DesignParameter['NMOS1_rInSRLatch_0']['_DesignObj']._DesignParameter['_POLayerPINDrawing']['_XYCoordinates'])):
		        xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['NMOS1_rInSRLatch_0']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['NMOS1_rInSRLatch_0']['_XYCoordinates'][0][1])], self._DesignParameter['NMOS1_rInSRLatch_0']['_DesignObj']._DesignParameter['_POLayerPINDrawing']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		elif (mode == 'horizontal'):
		    xy_with_offset = []
		    target_x_value = (0 + self._DesignParameter['POLY_boundary_186']['_XYCoordinates'][0][0])
		    for i in range(len(self._DesignParameter['NMOS1_rInSRLatch_0']['_DesignObj']._DesignParameter['_POLayerPINDrawing']['_XYCoordinates'])):
		        xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['NMOS1_rInSRLatch_0']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['NMOS1_rInSRLatch_0']['_XYCoordinates'][0][1])], self._DesignParameter['NMOS1_rInSRLatch_0']['_DesignObj']._DesignParameter['_POLayerPINDrawing']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		self._DesignParameter['nd1_gate_array'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _Width=_width)
		self._DesignParameter['nd1_gate_array']['_XYCoordinates'] = path_list
		pmos_via = max(2, max(1, (1 + int((((self._DesignParameter['PMOS2InSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] - drc._VIAxMinSpace) - (2 * drc._VIAxMinEnclosureByMetx)) / (drc._VIAxMinWidth + drc._VIAxMinSpace))))))
		self._DesignParameter['pu2_drain_via'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='pu2_drain_viaIn{}'.format(_Name)))[0]
		self._DesignParameter['pu2_drain_via']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(**dict(_ViaMet12Met2NumberOfCOX=1, _ViaMet12Met2NumberOfCOY=pmos_via))
		self._DesignParameter['pu2_drain_via']['_XYCoordinates'] = None
		XYList = []
		xy_offset = [0, 0]
		for i in range(len(self._DesignParameter['PMOS2InSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'])):
		    if ((i % 2) == 1):
		        xy = (self._DesignParameter['PMOS2InSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i][0] if (type(self._DesignParameter['PMOS2InSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i][0]) == list) else self._DesignParameter['PMOS2InSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i])
		        XYList.append([((x + y) + z) for (x, y, z) in zip([(0 + self._DesignParameter['PMOS2InSRLatch_0']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['PMOS2InSRLatch_0']['_XYCoordinates'][0][1])], xy, xy_offset)])
		self._DesignParameter['pu2_drain_via']['_XYCoordinates'] = XYList
		pmos_via = max(2, max(1, (1 + int((((self._DesignParameter['PMOS3InSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] - drc._VIAxMinSpace) - (2 * drc._VIAxMinEnclosureByMetx)) / (drc._VIAxMinWidth + drc._VIAxMinSpace))))))
		self._DesignParameter['pu3_svias'] = self._SrefElementDeclaration(_DesignObj=ViaStack._ViaStack(_Name='pu3_sviasIn{}'.format(_Name)))[0]
		self._DesignParameter['pu3_svias']['_DesignObj']._CalculateStackMinimumEnclosureX(**dict(COX=1, COY=pmos_via, start_layer=1, end_layer=3))
		self._DesignParameter['pu3_svias']['_XYCoordinates'] = None
		XYList = []
		xy_offset = (0, (int(((drc._VIAxMinWidth + drc._VIAxMinSpace) / 4)) * 2))
		for i in range(len(self._DesignParameter['PMOS3InSRLatch_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		    if ((i % 2) == 0):
		        xy = (self._DesignParameter['PMOS3InSRLatch_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i][0] if (type(self._DesignParameter['PMOS3InSRLatch_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i][0]) == list) else self._DesignParameter['PMOS3InSRLatch_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])
		        XYList.append([((x + y) + z) for (x, y, z) in zip([(0 + self._DesignParameter['PMOS3InSRLatch_0']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['PMOS3InSRLatch_0']['_XYCoordinates'][0][1])], xy, xy_offset)])
		self._DesignParameter['pu3_svias']['_XYCoordinates'] = XYList
		self._DesignParameter['pu3_dvia12'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='pu3_dvia12In{}'.format(_Name)))[0]
		self._DesignParameter['pu3_dvia12']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(**dict(_ViaMet12Met2NumberOfCOX=1, _ViaMet12Met2NumberOfCOY=pmos_via))
		self._DesignParameter['pu3_dvia12']['_XYCoordinates'] = None
		XYList = []
		xy_offset = [0, 0]
		for i in range(len(self._DesignParameter['PMOS3InSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'])):
		    if ((i % 2) == 1):
		        xy = (self._DesignParameter['PMOS3InSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i][0] if (type(self._DesignParameter['PMOS3InSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i][0]) == list) else self._DesignParameter['PMOS3InSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i])
		        XYList.append([((x + y) + z) for (x, y, z) in zip([(0 + self._DesignParameter['PMOS3InSRLatch_0']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['PMOS3InSRLatch_0']['_XYCoordinates'][0][1])], xy, xy_offset)])
		self._DesignParameter['pu3_dvia12']['_XYCoordinates'] = XYList
		self._DesignParameter['pu4_dvia12'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='pu4_dvia12In{}'.format(_Name)))[0]
		self._DesignParameter['pu4_dvia12']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(**dict(_ViaMet12Met2NumberOfCOX=1, _ViaMet12Met2NumberOfCOY=pmos_via))
		self._DesignParameter['pu4_dvia12']['_XYCoordinates'] = None
		XYList = []
		xy_offset = [0, 0]
		for i in range(len(self._DesignParameter['PMOS4InSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'])):
		    if ((i % 2) == 1):
		        xy = (self._DesignParameter['PMOS4InSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i][0] if (type(self._DesignParameter['PMOS4InSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i][0]) == list) else self._DesignParameter['PMOS4InSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i])
		        XYList.append([((x + y) + z) for (x, y, z) in zip([(0 + self._DesignParameter['PMOS4InSRLatch_0']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['PMOS4InSRLatch_0']['_XYCoordinates'][0][1])], xy, xy_offset)])
		self._DesignParameter['pu4_dvia12']['_XYCoordinates'] = XYList
		self._DesignParameter['METAL2_path_22'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _Width=drc._MetalxMinWidth)
		self._DesignParameter['METAL2_path_22']['_XYCoordinates'] = [[[((self._DesignParameter['pu3_dvia12']['_XYCoordinates'][0][0] + self._DesignParameter['pu3_dvia12']['_DesignObj']._DesignParameter['_Met2Layer']['_XYCoordinates'][0][0]) - (self._DesignParameter['pu3_dvia12']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth'] / 2)), (((((self._DesignParameter['pu3_svias']['_XYCoordinates'][0][1] + self._DesignParameter['pu3_svias']['_DesignObj']._DesignParameter['ViaMet22Met3']['_XYCoordinates'][0][1]) + self._DesignParameter['pu3_svias']['_DesignObj']._DesignParameter['ViaMet22Met3']['_DesignObj']._DesignParameter['_Met2Layer']['_XYCoordinates'][0][1]) - (self._DesignParameter['pu3_svias']['_DesignObj']._DesignParameter['ViaMet22Met3']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] / 2)) - drc._MetalxMinSpace3) - (drc._MetalxMinWidth / 2))], [((self._DesignParameter['pu4_dvia12']['_XYCoordinates'][(- 1)][0] + self._DesignParameter['pu4_dvia12']['_DesignObj']._DesignParameter['_Met2Layer']['_XYCoordinates'][0][0]) + (self._DesignParameter['pu4_dvia12']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth'] / 2)), (((((self._DesignParameter['pu3_svias']['_XYCoordinates'][0][1] + self._DesignParameter['pu3_svias']['_DesignObj']._DesignParameter['ViaMet22Met3']['_XYCoordinates'][0][1]) + self._DesignParameter['pu3_svias']['_DesignObj']._DesignParameter['ViaMet22Met3']['_DesignObj']._DesignParameter['_Met2Layer']['_XYCoordinates'][0][1]) - (self._DesignParameter['pu3_svias']['_DesignObj']._DesignParameter['ViaMet22Met3']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] / 2)) - drc._MetalxMinSpace3) - (drc._MetalxMinWidth / 2))]]]
		pmos_via = max(1, (1 + int((((self._DesignParameter['PMOS2_rInSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] - drc._VIAxMinSpace) - (2 * drc._VIAxMinEnclosureByMetx)) / (drc._VIAxMinWidth + drc._VIAxMinSpace)))))
		self._DesignParameter['pd2_draing_via12'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='pd2_draing_via12In{}'.format(_Name)))[0]
		self._DesignParameter['pd2_draing_via12']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(**dict(_ViaMet12Met2NumberOfCOX=1, _ViaMet12Met2NumberOfCOY=pmos_via))
		self._DesignParameter['pd2_draing_via12']['_XYCoordinates'] = None
		XYList = []
		xy_offset = [0, 0]
		for i in range(len(self._DesignParameter['PMOS2_rInSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'])):
		    if ((i % 2) == 1):
		        xy = (self._DesignParameter['PMOS2_rInSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i][0] if (type(self._DesignParameter['PMOS2_rInSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i][0]) == list) else self._DesignParameter['PMOS2_rInSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i])
		        XYList.append([((x + y) + z) for (x, y, z) in zip([(0 + self._DesignParameter['PMOS2_rInSRLatch_0']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['PMOS2_rInSRLatch_0']['_XYCoordinates'][0][1])], xy, xy_offset)])
		self._DesignParameter['pd2_draing_via12']['_XYCoordinates'] = XYList
		pmos_via = max(1, (1 + int((((self._DesignParameter['PMOS3_rInSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] - drc._VIAxMinSpace) - (2 * drc._VIAxMinEnclosureByMetx)) / (drc._VIAxMinWidth + drc._VIAxMinSpace)))))
		self._DesignParameter['pd3_svias'] = self._SrefElementDeclaration(_DesignObj=ViaStack._ViaStack(_Name='pd3_sviasIn{}'.format(_Name)))[0]
		self._DesignParameter['pd3_svias']['_DesignObj']._CalculateStackMinimumEnclosureX(**dict(COX=1, COY=pmos_via, start_layer=1, end_layer=3))
		self._DesignParameter['pd3_svias']['_XYCoordinates'] = None
		XYList = []
		xy_offset = (0, (- int(((drc._VIAxMinWidth + drc._VIAxMinSpace) / 4))))
		for i in range(len(self._DesignParameter['PMOS3_rInSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'])):
		    if ((i % 2) == 0):
		        xy = (self._DesignParameter['PMOS3_rInSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i][0] if (type(self._DesignParameter['PMOS3_rInSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i][0]) == list) else self._DesignParameter['PMOS3_rInSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i])
		        XYList.append([((x + y) + z) for (x, y, z) in zip([(0 + self._DesignParameter['PMOS3_rInSRLatch_0']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['PMOS3_rInSRLatch_0']['_XYCoordinates'][0][1])], xy, xy_offset)])
		self._DesignParameter['pd3_svias']['_XYCoordinates'] = XYList
		self._DesignParameter['PCCAM1_pd2'] = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_Name='PCCAM1_pd2In{}'.format(_Name)))[0]
		self._DesignParameter['PCCAM1_pd2']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(**dict(_ViaPoly2Met1NumberOfCOX=max(max(1, (1 + int(((((((self._DesignParameter['PMOS2_rInSRLatch_0']['_XYCoordinates'][0][0] + self._DesignParameter['PMOS2_rInSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]) + (self._DesignParameter['PMOS2_rInSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)) - ((self._DesignParameter['PMOS2_rInSRLatch_0']['_XYCoordinates'][0][0] + self._DesignParameter['PMOS2_rInSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['PMOS2_rInSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2))) - drc._CoMinSpace) - (2 * drc._CoMinEnclosureByPO)) / (drc._CoMinWidth + drc._CoMinSpace))))), 1), _ViaPoly2Met1NumberOfCOY=1))
		self._DesignParameter['PCCAM1_pd2']['_XYCoordinates'] = [[self._DesignParameter['PMOS2_rInSRLatch_0']['_XYCoordinates'][0][0], (round((math.sqrt(((drc._PolygateMinSpace ** 2) - ((abs((((self._DesignParameter['PMOS2_rInSRLatch_0']['_XYCoordinates'][0][0] + self._DesignParameter['PMOS2_rInSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) - self._DesignParameter['PMOS2_rInSRLatch_0']['_XYCoordinates'][0][0]) + self._DesignParameter['PMOS2_rInSRLatch_0']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][0])) - ((self._DesignParameter['PMOS2_rInSRLatch_0']['_DesignObj']._DesignParameter['_PODummyLayer']['_XWidth'] + self._DesignParameter['PCCAM1_pd2']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']) / 2)) ** 2))) + (self._DesignParameter['PCCAM1_pd2']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2))) + ((self._DesignParameter['PMOS2_rInSRLatch_0']['_XYCoordinates'][0][1] + self._DesignParameter['PMOS2_rInSRLatch_0']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][1]) + (self._DesignParameter['PMOS2_rInSRLatch_0']['_DesignObj']._DesignParameter['_PODummyLayer']['_YWidth'] / 2)))]]
		path_list = []
		if (len(self._DesignParameter['PMOS2_rInSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates']) == 1):
		    mode = 'vertical'
		    _width = self._DesignParameter['PMOS2_rInSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
		elif (self._DesignParameter['PMOS2_rInSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0] == self._DesignParameter['PMOS2_rInSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]):
		    mode = 'horizontal'
		    _width = self._DesignParameter['PMOS2_rInSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
		elif (self._DesignParameter['PMOS2_rInSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1] == self._DesignParameter['PMOS2_rInSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][1]):
		    mode = 'vertical'
		    _width = self._DesignParameter['PMOS2_rInSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
		else:
		    print('Invalid Target Input')
		if (mode == 'vertical'):
		    xy_with_offset = []
		    target_y_value = (0 + self._DesignParameter['PCCAM1_pd2']['_XYCoordinates'][0][1])
		    for i in range(len(self._DesignParameter['PMOS2_rInSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
		        xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['PMOS2_rInSRLatch_0']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['PMOS2_rInSRLatch_0']['_XYCoordinates'][0][1])], self._DesignParameter['PMOS2_rInSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		elif (mode == 'horizontal'):
		    xy_with_offset = []
		    target_x_value = (0 + self._DesignParameter['PCCAM1_pd2']['_XYCoordinates'][0][0])
		    for i in range(len(self._DesignParameter['PMOS2_rInSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
		        xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['PMOS2_rInSRLatch_0']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['PMOS2_rInSRLatch_0']['_XYCoordinates'][0][1])], self._DesignParameter['PMOS2_rInSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		self._DesignParameter['pd2_gate_array'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _Width=_width)
		self._DesignParameter['pd2_gate_array']['_XYCoordinates'] = path_list
		self._DesignParameter['PCCAM1_nd2'] = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_Name='PCCAM1_nd2In{}'.format(_Name)))[0]
		self._DesignParameter['PCCAM1_nd2']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(**dict(_ViaPoly2Met1NumberOfCOX=max(max(1, (1 + int(((((((self._DesignParameter['PMOS2_rInSRLatch_0']['_XYCoordinates'][0][0] + self._DesignParameter['PMOS2_rInSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]) + (self._DesignParameter['PMOS2_rInSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)) - ((self._DesignParameter['PMOS2_rInSRLatch_0']['_XYCoordinates'][0][0] + self._DesignParameter['PMOS2_rInSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['PMOS2_rInSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2))) - drc._CoMinSpace) - (2 * drc._CoMinEnclosureByPO)) / (drc._CoMinWidth + drc._CoMinSpace))))), 1), _ViaPoly2Met1NumberOfCOY=1))
		self._DesignParameter['PCCAM1_nd2']['_XYCoordinates'] = [[self._DesignParameter['NMOS2_rInSRLatch_0']['_XYCoordinates'][0][0], ((- round((math.sqrt(((drc._PolygateMinSpace ** 2) - ((abs((((self._DesignParameter['PMOS2_rInSRLatch_0']['_XYCoordinates'][0][0] + self._DesignParameter['PMOS2_rInSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) - self._DesignParameter['PMOS2_rInSRLatch_0']['_XYCoordinates'][0][0]) + self._DesignParameter['PMOS2_rInSRLatch_0']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][0])) - ((self._DesignParameter['PMOS2_rInSRLatch_0']['_DesignObj']._DesignParameter['_PODummyLayer']['_XWidth'] + self._DesignParameter['PCCAM1_pd2']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']) / 2)) ** 2))) + (self._DesignParameter['PCCAM1_pd2']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2)))) + ((self._DesignParameter['NMOS2_rInSRLatch_0']['_XYCoordinates'][0][1] + self._DesignParameter['NMOS2_rInSRLatch_0']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][1]) - (self._DesignParameter['NMOS2_rInSRLatch_0']['_DesignObj']._DesignParameter['_PODummyLayer']['_YWidth'] / 2)))]]
		path_list = []
		if (len(self._DesignParameter['NMOS2_rInSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates']) == 1):
		    mode = 'vertical'
		    _width = self._DesignParameter['NMOS2_rInSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
		elif (self._DesignParameter['NMOS2_rInSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0] == self._DesignParameter['NMOS2_rInSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]):
		    mode = 'horizontal'
		    _width = self._DesignParameter['NMOS2_rInSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
		elif (self._DesignParameter['NMOS2_rInSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1] == self._DesignParameter['NMOS2_rInSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][1]):
		    mode = 'vertical'
		    _width = self._DesignParameter['NMOS2_rInSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
		else:
		    print('Invalid Target Input')
		if (mode == 'vertical'):
		    xy_with_offset = []
		    target_y_value = (0 + self._DesignParameter['PCCAM1_nd2']['_XYCoordinates'][0][1])
		    for i in range(len(self._DesignParameter['NMOS2_rInSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
		        xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['NMOS2_rInSRLatch_0']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['NMOS2_rInSRLatch_0']['_XYCoordinates'][0][1])], self._DesignParameter['NMOS2_rInSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		elif (mode == 'horizontal'):
		    xy_with_offset = []
		    target_x_value = (0 + self._DesignParameter['PCCAM1_nd2']['_XYCoordinates'][0][0])
		    for i in range(len(self._DesignParameter['NMOS2_rInSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
		        xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['NMOS2_rInSRLatch_0']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['NMOS2_rInSRLatch_0']['_XYCoordinates'][0][1])], self._DesignParameter['NMOS2_rInSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		self._DesignParameter['nd2_gate_array'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _Width=_width)
		self._DesignParameter['nd2_gate_array']['_XYCoordinates'] = path_list
		self._DesignParameter['METAL1_path_18'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=drc._Metal1MinWidth)
		self._DesignParameter['METAL1_path_18']['_XYCoordinates'] = [[[(+ self._DesignParameter['PCCAM1_nd2']['_XYCoordinates'][0][0]), (+ self._DesignParameter['PCCAM1_nd2']['_XYCoordinates'][0][1])], [(+ self._DesignParameter['PCCAM1_pd2']['_XYCoordinates'][0][0]), (+ self._DesignParameter['PCCAM1_pd2']['_XYCoordinates'][0][1])]]]
		nmos_via = min(max(1, (1 + int((((self._DesignParameter['PMOS3_rInSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] - drc._VIAxMinSpace) - (2 * drc._VIAxMinEnclosureByMetx)) / (drc._VIAxMinWidth + drc._VIAxMinSpace))))), 2)
		self._DesignParameter['nd2_drain_via12'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='nd2_drain_via12In{}'.format(_Name)))[0]
		self._DesignParameter['nd2_drain_via12']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(**dict(_ViaMet12Met2NumberOfCOX=1, _ViaMet12Met2NumberOfCOY=nmos_via))
		self._DesignParameter['nd2_drain_via12']['_XYCoordinates'] = None
		XYList = []
		xy_offset = (0, int(((drc._VIAxMinWidth + drc._VIAxMinSpace) / 4)))
		for i in range(len(self._DesignParameter['NMOS2_rInSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'])):
		    if ((i % 2) == 1):
		        xy = (self._DesignParameter['NMOS2_rInSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i][0] if (type(self._DesignParameter['NMOS2_rInSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i][0]) == list) else self._DesignParameter['NMOS2_rInSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i])
		        XYList.append([((x + y) + z) for (x, y, z) in zip([(0 + self._DesignParameter['NMOS2_rInSRLatch_0']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['NMOS2_rInSRLatch_0']['_XYCoordinates'][0][1])], xy, xy_offset)])
		self._DesignParameter['nd2_drain_via12']['_XYCoordinates'] = XYList
		self._DesignParameter['METAL2_path_18'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _Width=drc._MetalxMinWidth)
		self._DesignParameter['METAL2_path_18']['_XYCoordinates'] = [[[(+ self._DesignParameter['nd2_drain_via12']['_XYCoordinates'][0][0]), (+ self._DesignParameter['nd2_drain_via12']['_XYCoordinates'][0][1])], [(+ self._DesignParameter['pd2_draing_via12']['_XYCoordinates'][0][0]), (+ self._DesignParameter['pd2_draing_via12']['_XYCoordinates'][0][1])]]]
		pmos_via = max(1, (1 + int((((self._DesignParameter['NMOS3_rInSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] - drc._VIAxMinSpace) - (2 * drc._VIAxMinEnclosureByMetx)) / (drc._VIAxMinWidth + drc._VIAxMinSpace)))))
		self._DesignParameter['nd3_svias'] = self._SrefElementDeclaration(_DesignObj=ViaStack._ViaStack(_Name='nd3_sviasIn{}'.format(_Name)))[0]
		self._DesignParameter['nd3_svias']['_DesignObj']._CalculateStackMinimumEnclosureX(**dict(COX=1, COY=nmos_via, start_layer=1, end_layer=3))
		self._DesignParameter['nd3_svias']['_XYCoordinates'] = None
		XYList = []
		xy_offset = (0, int(((drc._VIAxMinWidth + drc._VIAxMinSpace) / 4)))
		for i in range(len(self._DesignParameter['NMOS3_rInSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'])):
		    if ((i % 2) == 0):
		        xy = (self._DesignParameter['NMOS3_rInSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i][0] if (type(self._DesignParameter['NMOS3_rInSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i][0]) == list) else self._DesignParameter['NMOS3_rInSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i])
		        XYList.append([((x + y) + z) for (x, y, z) in zip([(0 + self._DesignParameter['NMOS3_rInSRLatch_0']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['NMOS3_rInSRLatch_0']['_XYCoordinates'][0][1])], xy, xy_offset)])
		self._DesignParameter['nd3_svias']['_XYCoordinates'] = XYList
		pmos_via = max(1, (1 + int((((self._DesignParameter['PMOS3_rInSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] - drc._VIAxMinSpace) - (2 * drc._VIAxMinEnclosureByMetx)) / (drc._VIAxMinWidth + drc._VIAxMinSpace)))))
		self._DesignParameter['pd3_d_via12'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='pd3_d_via12In{}'.format(_Name)))[0]
		self._DesignParameter['pd3_d_via12']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(**dict(_ViaMet12Met2NumberOfCOX=1, _ViaMet12Met2NumberOfCOY=pmos_via))
		self._DesignParameter['pd3_d_via12']['_XYCoordinates'] = None
		XYList = []
		xy_offset = (0, int(((drc._VIAxMinWidth + drc._VIAxMinSpace) / 4)))
		for i in range(len(self._DesignParameter['PMOS3_rInSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'])):
		    if ((i % 2) == 1):
		        xy = (self._DesignParameter['PMOS3_rInSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i][0] if (type(self._DesignParameter['PMOS3_rInSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i][0]) == list) else self._DesignParameter['PMOS3_rInSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i])
		        XYList.append([((x + y) + z) for (x, y, z) in zip([(0 + self._DesignParameter['PMOS3_rInSRLatch_0']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['PMOS3_rInSRLatch_0']['_XYCoordinates'][0][1])], xy, xy_offset)])
		self._DesignParameter['pd3_d_via12']['_XYCoordinates'] = XYList
		self._DesignParameter['pd4_drain_via12'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='pd4_drain_via12In{}'.format(_Name)))[0]
		self._DesignParameter['pd4_drain_via12']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(**dict(_ViaMet12Met2NumberOfCOX=1, _ViaMet12Met2NumberOfCOY=pmos_via))
		self._DesignParameter['pd4_drain_via12']['_XYCoordinates'] = None
		XYList = []
		xy_offset = (0, int(((drc._VIAxMinWidth + drc._VIAxMinSpace) / 4)))
		for i in range(len(self._DesignParameter['PMOS4_rInSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'])):
		    if ((i % 2) == 1):
		        xy = (self._DesignParameter['PMOS4_rInSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i][0] if (type(self._DesignParameter['PMOS4_rInSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i][0]) == list) else self._DesignParameter['PMOS4_rInSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i])
		        XYList.append([((x + y) + z) for (x, y, z) in zip([(0 + self._DesignParameter['PMOS4_rInSRLatch_0']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['PMOS4_rInSRLatch_0']['_XYCoordinates'][0][1])], xy, xy_offset)])
		self._DesignParameter['pd4_drain_via12']['_XYCoordinates'] = XYList
		self._DesignParameter['METAL2_path_21'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _Width=drc._MetalxMinWidth)
		self._DesignParameter['METAL2_path_21']['_XYCoordinates'] = [[[((self._DesignParameter['pd3_d_via12']['_XYCoordinates'][0][0] + self._DesignParameter['pd3_d_via12']['_DesignObj']._DesignParameter['_Met2Layer']['_XYCoordinates'][0][0]) - (self._DesignParameter['pd3_d_via12']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth'] / 2)), (((((self._DesignParameter['pd3_svias']['_XYCoordinates'][0][1] + self._DesignParameter['pd3_svias']['_DesignObj']._DesignParameter['ViaMet22Met3']['_XYCoordinates'][0][1]) + self._DesignParameter['pd3_svias']['_DesignObj']._DesignParameter['ViaMet22Met3']['_DesignObj']._DesignParameter['_Met2Layer']['_XYCoordinates'][0][1]) + (self._DesignParameter['pd3_svias']['_DesignObj']._DesignParameter['ViaMet22Met3']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] / 2)) + drc._MetalxMinSpace2) + (drc._MetalxMinWidth / 2))], [((self._DesignParameter['pd4_drain_via12']['_XYCoordinates'][(- 1)][0] + self._DesignParameter['pd4_drain_via12']['_DesignObj']._DesignParameter['_Met2Layer']['_XYCoordinates'][0][0]) + (self._DesignParameter['pd4_drain_via12']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth'] / 2)), (((((self._DesignParameter['pd3_svias']['_XYCoordinates'][0][1] + self._DesignParameter['pd3_svias']['_DesignObj']._DesignParameter['ViaMet22Met3']['_XYCoordinates'][0][1]) + self._DesignParameter['pd3_svias']['_DesignObj']._DesignParameter['ViaMet22Met3']['_DesignObj']._DesignParameter['_Met2Layer']['_XYCoordinates'][0][1]) + (self._DesignParameter['pd3_svias']['_DesignObj']._DesignParameter['ViaMet22Met3']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] / 2)) + drc._MetalxMinSpace2) + (drc._MetalxMinWidth / 2))]]]
		self._DesignParameter['PCCAM1_pd3'] = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_Name='PCCAM1_pd3In{}'.format(_Name)))[0]
		self._DesignParameter['PCCAM1_pd3']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(**dict(_ViaPoly2Met1NumberOfCOX=1, _ViaPoly2Met1NumberOfCOY=1))
		self._DesignParameter['PCCAM1_pd3']['_XYCoordinates'] = [[self._DesignParameter['PMOS3_rInSRLatch_0']['_XYCoordinates'][0][0], ((((self._DesignParameter['pd3_d_via12']['_XYCoordinates'][0][1] + self._DesignParameter['pd3_d_via12']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) + (self._DesignParameter['pd3_d_via12']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)) + drc._Metal1MinSpace2) + (self._DesignParameter['PCCAM1_pd3']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2))]]
		self._DesignParameter['M1V1M2_pd3_gate'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='M1V1M2_pd3_gateIn{}'.format(_Name)))[0]
		self._DesignParameter['M1V1M2_pd3_gate']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureY(**dict(_ViaMet12Met2NumberOfCOX=2, _ViaMet12Met2NumberOfCOY=1))
		self._DesignParameter['M1V1M2_pd3_gate']['_XYCoordinates'] = [[self._DesignParameter['PCCAM1_pd3']['_XYCoordinates'][0][0], (((self._DesignParameter['METAL2_path_21']['_XYCoordinates'][0][0][1] + (self._DesignParameter['METAL2_path_21']['_Width'] / 2)) + drc._MetalxMinSpace) + (self._DesignParameter['M1V1M2_pd3_gate']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] / 2))]]
		self._DesignParameter['POLY_boundary_192'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _XWidth=(((self._DesignParameter['PMOS3_rInSRLatch_0']['_XYCoordinates'][0][0] + self._DesignParameter['PMOS3_rInSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]) + (self._DesignParameter['PMOS3_rInSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)) - ((self._DesignParameter['PMOS3_rInSRLatch_0']['_XYCoordinates'][0][0] + self._DesignParameter['PMOS3_rInSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['PMOS3_rInSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2))), _YWidth=self._DesignParameter['PCCAM1_pd3']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'])
		self._DesignParameter['POLY_boundary_192']['_XYCoordinates'] = [[(+ self._DesignParameter['PCCAM1_pd3']['_XYCoordinates'][0][0]), (+ self._DesignParameter['PCCAM1_pd3']['_XYCoordinates'][0][1])]]
		path_list = []
		if (len(self._DesignParameter['PMOS3_rInSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates']) == 1):
		    mode = 'vertical'
		    _width = self._DesignParameter['PMOS3_rInSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
		elif (self._DesignParameter['PMOS3_rInSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0] == self._DesignParameter['PMOS3_rInSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]):
		    mode = 'horizontal'
		    _width = self._DesignParameter['PMOS3_rInSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
		elif (self._DesignParameter['PMOS3_rInSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1] == self._DesignParameter['PMOS3_rInSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][1]):
		    mode = 'vertical'
		    _width = self._DesignParameter['PMOS3_rInSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
		else:
		    print('Invalid Target Input')
		if (mode == 'vertical'):
		    xy_with_offset = []
		    target_y_value = (0 + self._DesignParameter['POLY_boundary_192']['_XYCoordinates'][0][1])
		    for i in range(len(self._DesignParameter['PMOS3_rInSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
		        xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['PMOS3_rInSRLatch_0']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['PMOS3_rInSRLatch_0']['_XYCoordinates'][0][1])], self._DesignParameter['PMOS3_rInSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		elif (mode == 'horizontal'):
		    xy_with_offset = []
		    target_x_value = (0 + self._DesignParameter['POLY_boundary_192']['_XYCoordinates'][0][0])
		    for i in range(len(self._DesignParameter['PMOS3_rInSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
		        xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['PMOS3_rInSRLatch_0']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['PMOS3_rInSRLatch_0']['_XYCoordinates'][0][1])], self._DesignParameter['PMOS3_rInSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		self._DesignParameter['pd3_gate_array'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _Width=_width)
		self._DesignParameter['pd3_gate_array']['_XYCoordinates'] = path_list
		self._DesignParameter['METAL1_boundary_196'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _XWidth=max(self._DesignParameter['M1V1M2_pd3_gate']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'], self._DesignParameter['PCCAM1_pd3']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']), _YWidth=self._DesignParameter['PCCAM1_pd3']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'])
		self._DesignParameter['METAL1_boundary_196']['_XYCoordinates'] = [[(+ self._DesignParameter['PCCAM1_pd3']['_XYCoordinates'][0][0]), (+ self._DesignParameter['PCCAM1_pd3']['_XYCoordinates'][0][1])]]
		self._DesignParameter['METAL2_path_7'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _Width=drc._MetalxMinWidth)
		self._DesignParameter['METAL2_path_7']['_XYCoordinates'] = [[[(+ self._DesignParameter['M1V1M2_pd3_gate']['_XYCoordinates'][0][0]), (+ self._DesignParameter['M1V1M2_pd3_gate']['_XYCoordinates'][0][1])], [self._DesignParameter['METAL2_path_18']['_XYCoordinates'][0][0][0], self._DesignParameter['M1V1M2_pd3_gate']['_XYCoordinates'][0][1]]]]
		nmos_via = max(2, max(1, (1 + int((((self._DesignParameter['NMOS3_rInSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] - drc._VIAxMinSpace) - (2 * drc._VIAxMinEnclosureByMetx)) / (drc._VIAxMinWidth + drc._VIAxMinSpace))))))
		self._DesignParameter['nd3_dvia12'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='nd3_dvia12In{}'.format(_Name)))[0]
		self._DesignParameter['nd3_dvia12']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(**dict(_ViaMet12Met2NumberOfCOX=1, _ViaMet12Met2NumberOfCOY=nmos_via))
		self._DesignParameter['nd3_dvia12']['_XYCoordinates'] = None
		XYList = []
		xy_offset = (0, (- int(((drc._VIAxMinWidth + drc._VIAxMinSpace) / 4))))
		for i in range(len(self._DesignParameter['NMOS3_rInSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'])):
		    if ((i % 2) == 1):
		        xy = (self._DesignParameter['NMOS3_rInSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i][0] if (type(self._DesignParameter['NMOS3_rInSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i][0]) == list) else self._DesignParameter['NMOS3_rInSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i])
		        XYList.append([((x + y) + z) for (x, y, z) in zip([(0 + self._DesignParameter['NMOS3_rInSRLatch_0']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['NMOS3_rInSRLatch_0']['_XYCoordinates'][0][1])], xy, xy_offset)])
		self._DesignParameter['nd3_dvia12']['_XYCoordinates'] = XYList
		self._DesignParameter['nd4_drain_via12'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='nd4_drain_via12In{}'.format(_Name)))[0]
		self._DesignParameter['nd4_drain_via12']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(**dict(_ViaMet12Met2NumberOfCOX=1, _ViaMet12Met2NumberOfCOY=nmos_via))
		self._DesignParameter['nd4_drain_via12']['_XYCoordinates'] = None
		XYList = []
		xy_offset = (0, (- int(((drc._VIAxMinWidth + drc._VIAxMinSpace) / 4))))
		for i in range(len(self._DesignParameter['NMOS4_rInSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'])):
		    if ((i % 2) == 1):
		        xy = (self._DesignParameter['NMOS4_rInSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i][0] if (type(self._DesignParameter['NMOS4_rInSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i][0]) == list) else self._DesignParameter['NMOS4_rInSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i])
		        XYList.append([((x + y) + z) for (x, y, z) in zip([(0 + self._DesignParameter['NMOS4_rInSRLatch_0']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['NMOS4_rInSRLatch_0']['_XYCoordinates'][0][1])], xy, xy_offset)])
		self._DesignParameter['nd4_drain_via12']['_XYCoordinates'] = XYList
		self._DesignParameter['METAL2_path_19'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _Width=drc._MetalxMinWidth)
		self._DesignParameter['METAL2_path_19']['_XYCoordinates'] = [[[((self._DesignParameter['nd3_dvia12']['_XYCoordinates'][0][0] + self._DesignParameter['nd3_dvia12']['_DesignObj']._DesignParameter['_Met2Layer']['_XYCoordinates'][0][0]) - (self._DesignParameter['nd3_dvia12']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth'] / 2)), (((((self._DesignParameter['nd3_svias']['_XYCoordinates'][0][1] + self._DesignParameter['nd3_svias']['_DesignObj']._DesignParameter['ViaMet12Met2']['_XYCoordinates'][0][1]) + self._DesignParameter['nd3_svias']['_DesignObj']._DesignParameter['ViaMet12Met2']['_DesignObj']._DesignParameter['_Met2Layer']['_XYCoordinates'][0][1]) - (self._DesignParameter['nd3_svias']['_DesignObj']._DesignParameter['ViaMet12Met2']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] / 2)) - drc._MetalxMinSpace2) - (drc._MetalxMinWidth / 2))], [((self._DesignParameter['nd4_drain_via12']['_XYCoordinates'][(- 1)][0] + self._DesignParameter['nd4_drain_via12']['_DesignObj']._DesignParameter['_Met2Layer']['_XYCoordinates'][0][0]) + (self._DesignParameter['nd4_drain_via12']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth'] / 2)), (((((self._DesignParameter['nd3_svias']['_XYCoordinates'][0][1] + self._DesignParameter['nd3_svias']['_DesignObj']._DesignParameter['ViaMet12Met2']['_XYCoordinates'][0][1]) + self._DesignParameter['nd3_svias']['_DesignObj']._DesignParameter['ViaMet12Met2']['_DesignObj']._DesignParameter['_Met2Layer']['_XYCoordinates'][0][1]) - (self._DesignParameter['nd3_svias']['_DesignObj']._DesignParameter['ViaMet12Met2']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] / 2)) - drc._MetalxMinSpace2) - (drc._MetalxMinWidth / 2))]]]
		self._DesignParameter['PCCAM1_nd3'] = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_Name='PCCAM1_nd3In{}'.format(_Name)))[0]
		self._DesignParameter['PCCAM1_nd3']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(**dict(_ViaPoly2Met1NumberOfCOX=max(max(1, (1 + int(((((((self._DesignParameter['NMOS3_rInSRLatch_0']['_XYCoordinates'][0][0] + self._DesignParameter['NMOS3_rInSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]) + (self._DesignParameter['NMOS3_rInSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)) - ((self._DesignParameter['NMOS3_rInSRLatch_0']['_XYCoordinates'][0][0] + self._DesignParameter['NMOS3_rInSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['NMOS3_rInSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2))) - drc._CoMinSpace) - (2 * drc._CoMinEnclosureByPO)) / (drc._CoMinWidth + drc._CoMinSpace))))), 1), _ViaPoly2Met1NumberOfCOY=1))
		self._DesignParameter['PCCAM1_nd3']['_XYCoordinates'] = [[self._DesignParameter['NMOS3_rInSRLatch_0']['_XYCoordinates'][0][0], ((((self._DesignParameter['NMOS3_rInSRLatch_0']['_XYCoordinates'][0][1] + self._DesignParameter['NMOS3_rInSRLatch_0']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][1]) - (self._DesignParameter['NMOS3_rInSRLatch_0']['_DesignObj']._DesignParameter['_PODummyLayer']['_YWidth'] / 2)) - drc._PoDummyLengthToMove) - (self._DesignParameter['PCCAM1_nd3']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2))]]
		self._DesignParameter['nd3_gate_vias'] = self._SrefElementDeclaration(_DesignObj=ViaStack._ViaStack(_Name='nd3_gate_viasIn{}'.format(_Name)))[0]
		self._DesignParameter['nd3_gate_vias']['_DesignObj']._CalculateStackMinimumEnclosureY(**dict(COX=2, COY=1, start_layer=1, end_layer=3))
		self._DesignParameter['nd3_gate_vias']['_XYCoordinates'] = [[self._DesignParameter['PCCAM1_nd3']['_XYCoordinates'][0][0], (((self._DesignParameter['METAL2_path_19']['_XYCoordinates'][0][0][1] - (self._DesignParameter['METAL2_path_19']['_Width'] / 2)) - drc._MetalxMinSpace) - (self._DesignParameter['nd3_gate_vias']['_DesignObj']._DesignParameter['ViaMet12Met2']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] / 2))]]
		self._DesignParameter['METAL1_boundary_194'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _XWidth=max(self._DesignParameter['nd3_gate_vias']['_DesignObj']._DesignParameter['ViaMet12Met2']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'], self._DesignParameter['PCCAM1_nd3']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']), _YWidth=self._DesignParameter['PCCAM1_nd3']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'])
		self._DesignParameter['METAL1_boundary_194']['_XYCoordinates'] = [[(+ self._DesignParameter['PCCAM1_nd3']['_XYCoordinates'][0][0]), (+ self._DesignParameter['PCCAM1_nd3']['_XYCoordinates'][0][1])]]
		self._DesignParameter['POLY_boundary_190'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _XWidth=(((self._DesignParameter['NMOS3_rInSRLatch_0']['_XYCoordinates'][0][0] + self._DesignParameter['NMOS3_rInSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]) + (self._DesignParameter['NMOS3_rInSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)) - ((self._DesignParameter['NMOS3_rInSRLatch_0']['_XYCoordinates'][0][0] + self._DesignParameter['NMOS3_rInSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['NMOS3_rInSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2))), _YWidth=self._DesignParameter['PCCAM1_nd3']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'])
		self._DesignParameter['POLY_boundary_190']['_XYCoordinates'] = [[(+ self._DesignParameter['PCCAM1_nd3']['_XYCoordinates'][0][0]), (+ self._DesignParameter['PCCAM1_nd3']['_XYCoordinates'][0][1])]]
		path_list = []
		if (len(self._DesignParameter['NMOS3_rInSRLatch_0']['_DesignObj']._DesignParameter['_POLayerPINDrawing']['_XYCoordinates']) == 1):
		    mode = 'vertical'
		    _width = self._DesignParameter['NMOS3_rInSRLatch_0']['_DesignObj']._DesignParameter['_POLayerPINDrawing']['_XWidth']
		elif (self._DesignParameter['NMOS3_rInSRLatch_0']['_DesignObj']._DesignParameter['_POLayerPINDrawing']['_XYCoordinates'][0][0] == self._DesignParameter['NMOS3_rInSRLatch_0']['_DesignObj']._DesignParameter['_POLayerPINDrawing']['_XYCoordinates'][(- 1)][0]):
		    mode = 'horizontal'
		    _width = self._DesignParameter['NMOS3_rInSRLatch_0']['_DesignObj']._DesignParameter['_POLayerPINDrawing']['_XWidth']
		elif (self._DesignParameter['NMOS3_rInSRLatch_0']['_DesignObj']._DesignParameter['_POLayerPINDrawing']['_XYCoordinates'][0][1] == self._DesignParameter['NMOS3_rInSRLatch_0']['_DesignObj']._DesignParameter['_POLayerPINDrawing']['_XYCoordinates'][(- 1)][1]):
		    mode = 'vertical'
		    _width = self._DesignParameter['NMOS3_rInSRLatch_0']['_DesignObj']._DesignParameter['_POLayerPINDrawing']['_XWidth']
		else:
		    print('Invalid Target Input')
		if (mode == 'vertical'):
		    xy_with_offset = []
		    target_y_value = (0 + self._DesignParameter['POLY_boundary_190']['_XYCoordinates'][0][1])
		    for i in range(len(self._DesignParameter['NMOS3_rInSRLatch_0']['_DesignObj']._DesignParameter['_POLayerPINDrawing']['_XYCoordinates'])):
		        xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['NMOS3_rInSRLatch_0']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['NMOS3_rInSRLatch_0']['_XYCoordinates'][0][1])], self._DesignParameter['NMOS3_rInSRLatch_0']['_DesignObj']._DesignParameter['_POLayerPINDrawing']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		elif (mode == 'horizontal'):
		    xy_with_offset = []
		    target_x_value = (0 + self._DesignParameter['POLY_boundary_190']['_XYCoordinates'][0][0])
		    for i in range(len(self._DesignParameter['NMOS3_rInSRLatch_0']['_DesignObj']._DesignParameter['_POLayerPINDrawing']['_XYCoordinates'])):
		        xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['NMOS3_rInSRLatch_0']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['NMOS3_rInSRLatch_0']['_XYCoordinates'][0][1])], self._DesignParameter['NMOS3_rInSRLatch_0']['_DesignObj']._DesignParameter['_POLayerPINDrawing']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		self._DesignParameter['nd3_gate_array'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _Width=_width)
		self._DesignParameter['nd3_gate_array']['_XYCoordinates'] = path_list
		self._DesignParameter['M3V3M4_CDNS_6375475055620_7'] = self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_Name='M3V3M4_CDNS_6375475055620_7In{}'.format(_Name)))[0]
		self._DesignParameter['M3V3M4_CDNS_6375475055620_7']['_DesignObj']._CalculateViaMet32Met4DesignParameterMinimumEnclosureY(**dict(_ViaMet32Met4NumberOfCOX=2, _ViaMet32Met4NumberOfCOY=1))
		self._DesignParameter['M3V3M4_CDNS_6375475055620_7']['_XYCoordinates'] = [[self._DesignParameter['pd1_gate_vias']['_XYCoordinates'][0][0], self._DesignParameter['nd3_gate_vias']['_XYCoordinates'][0][1]]]
		self._DesignParameter['METAL3_path_23'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0], _Datatype=DesignParameters._LayerMapping['METAL3'][1], _Width=drc._MetalxMinWidth)
		self._DesignParameter['METAL3_path_23']['_XYCoordinates'] = [[[(+ self._DesignParameter['nd3_gate_vias']['_XYCoordinates'][0][0]), (+ self._DesignParameter['nd3_gate_vias']['_XYCoordinates'][0][1])], [(+ self._DesignParameter['M3V3M4_CDNS_6375475055620_7']['_XYCoordinates'][0][0]), (+ self._DesignParameter['M3V3M4_CDNS_6375475055620_7']['_XYCoordinates'][0][1])]]]
		self._DesignParameter['METAL2_path_13'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _Width=drc._MetalxMinWidth)
		self._DesignParameter['METAL2_path_13']['_XYCoordinates'] = [[[(+ self._DesignParameter['M1V1M2_nd1_gate']['_XYCoordinates'][0][0]), (+ self._DesignParameter['M1V1M2_nd1_gate']['_XYCoordinates'][0][1])], [self._DesignParameter['METAL2_path_18']['_XYCoordinates'][0][0][0], self._DesignParameter['M1V1M2_nd1_gate']['_XYCoordinates'][0][1]]]]
		self._DesignParameter['PCCAM1_pd4'] = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_Name='PCCAM1_pd4In{}'.format(_Name)))[0]
		self._DesignParameter['PCCAM1_pd4']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(**dict(_ViaPoly2Met1NumberOfCOX=max(1, (1 + int(((((((self._DesignParameter['PMOS4_rInSRLatch_0']['_XYCoordinates'][0][0] + self._DesignParameter['PMOS4_rInSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]) + (self._DesignParameter['PMOS4_rInSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)) - ((self._DesignParameter['PMOS4_rInSRLatch_0']['_XYCoordinates'][0][0] + self._DesignParameter['PMOS4_rInSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['PMOS4_rInSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2))) - drc._CoMinSpace) - (2 * drc._CoMinEnclosureByPO)) / (drc._CoMinWidth + drc._CoMinSpace))))), _ViaPoly2Met1NumberOfCOY=1))
		self._DesignParameter['PCCAM1_pd4']['_XYCoordinates'] = [[self._DesignParameter['PMOS4_rInSRLatch_0']['_XYCoordinates'][0][0], ((max(((self._DesignParameter['pd4_drain_via12']['_XYCoordinates'][0][1] + self._DesignParameter['pd4_drain_via12']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) + (self._DesignParameter['pd4_drain_via12']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)), ((self._DesignParameter['PMOS4_rInSRLatch_0']['_XYCoordinates'][0][1] + self._DesignParameter['PMOS4_rInSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) + (self._DesignParameter['PMOS4_rInSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2))) + drc._Metal1MinSpace2) + (self._DesignParameter['PCCAM1_pd4']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2))]]
		self._DesignParameter['POLY_boundary_184'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _XWidth=(((self._DesignParameter['PMOS4_rInSRLatch_0']['_XYCoordinates'][0][0] + self._DesignParameter['PMOS4_rInSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]) + (self._DesignParameter['PMOS4_rInSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)) - ((self._DesignParameter['PMOS4_rInSRLatch_0']['_XYCoordinates'][0][0] + self._DesignParameter['PMOS4_rInSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['PMOS4_rInSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2))), _YWidth=self._DesignParameter['PCCAM1_pd4']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'])
		self._DesignParameter['POLY_boundary_184']['_XYCoordinates'] = [[(+ self._DesignParameter['PCCAM1_pd4']['_XYCoordinates'][0][0]), (+ self._DesignParameter['PCCAM1_pd4']['_XYCoordinates'][0][1])]]
		path_list = []
		if (len(self._DesignParameter['PMOS4_rInSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates']) == 1):
		    mode = 'vertical'
		    _width = self._DesignParameter['PMOS4_rInSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
		elif (self._DesignParameter['PMOS4_rInSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0] == self._DesignParameter['PMOS4_rInSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]):
		    mode = 'horizontal'
		    _width = self._DesignParameter['PMOS4_rInSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
		elif (self._DesignParameter['PMOS4_rInSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1] == self._DesignParameter['PMOS4_rInSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][1]):
		    mode = 'vertical'
		    _width = self._DesignParameter['PMOS4_rInSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
		else:
		    print('Invalid Target Input')
		if (mode == 'vertical'):
		    xy_with_offset = []
		    target_y_value = (0 + self._DesignParameter['POLY_boundary_184']['_XYCoordinates'][0][1])
		    for i in range(len(self._DesignParameter['PMOS4_rInSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
		        xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['PMOS4_rInSRLatch_0']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['PMOS4_rInSRLatch_0']['_XYCoordinates'][0][1])], self._DesignParameter['PMOS4_rInSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		elif (mode == 'horizontal'):
		    xy_with_offset = []
		    target_x_value = (0 + self._DesignParameter['POLY_boundary_184']['_XYCoordinates'][0][0])
		    for i in range(len(self._DesignParameter['PMOS4_rInSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
		        xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['PMOS4_rInSRLatch_0']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['PMOS4_rInSRLatch_0']['_XYCoordinates'][0][1])], self._DesignParameter['PMOS4_rInSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		self._DesignParameter['pd4_gate_array'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _Width=_width)
		self._DesignParameter['pd4_gate_array']['_XYCoordinates'] = path_list
		self._DesignParameter['PCCAM1_nd4'] = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_Name='PCCAM1_nd4In{}'.format(_Name)))[0]
		self._DesignParameter['PCCAM1_nd4']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(**dict(_ViaPoly2Met1NumberOfCOX=max(1, (1 + int(((((((self._DesignParameter['NMOS4_rInSRLatch_0']['_XYCoordinates'][0][0] + self._DesignParameter['NMOS4_rInSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]) + (self._DesignParameter['NMOS4_rInSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)) - ((self._DesignParameter['NMOS4_rInSRLatch_0']['_XYCoordinates'][0][0] + self._DesignParameter['NMOS4_rInSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['NMOS4_rInSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2))) - drc._CoMinSpace) - (2 * drc._CoMinEnclosureByPO)) / (drc._CoMinWidth + drc._CoMinSpace))))), _ViaPoly2Met1NumberOfCOY=1))
		self._DesignParameter['PCCAM1_nd4']['_XYCoordinates'] = [[self._DesignParameter['NMOS4_rInSRLatch_0']['_XYCoordinates'][0][0], ((((self._DesignParameter['NMOS4_rInSRLatch_0']['_XYCoordinates'][0][1] + self._DesignParameter['NMOS4_rInSRLatch_0']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][1]) - (self._DesignParameter['NMOS4_rInSRLatch_0']['_DesignObj']._DesignParameter['_PODummyLayer']['_YWidth'] / 2)) - drc._PoDummyLengthToMove) - (self._DesignParameter['PCCAM1_nd4']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2))]]
		self._DesignParameter['POLY_boundary_182'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _XWidth=(((self._DesignParameter['NMOS4_rInSRLatch_0']['_XYCoordinates'][0][0] + self._DesignParameter['NMOS4_rInSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]) + (self._DesignParameter['NMOS4_rInSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)) - ((self._DesignParameter['NMOS4_rInSRLatch_0']['_XYCoordinates'][0][0] + self._DesignParameter['NMOS4_rInSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['NMOS4_rInSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2))), _YWidth=self._DesignParameter['PCCAM1_nd4']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'])
		self._DesignParameter['POLY_boundary_182']['_XYCoordinates'] = [[(+ self._DesignParameter['PCCAM1_nd4']['_XYCoordinates'][0][0]), (+ self._DesignParameter['PCCAM1_nd4']['_XYCoordinates'][0][1])]]
		path_list = []
		if (len(self._DesignParameter['NMOS4_rInSRLatch_0']['_DesignObj']._DesignParameter['_POLayerPINDrawing']['_XYCoordinates']) == 1):
		    mode = 'vertical'
		    _width = self._DesignParameter['NMOS4_rInSRLatch_0']['_DesignObj']._DesignParameter['_POLayerPINDrawing']['_XWidth']
		elif (self._DesignParameter['NMOS4_rInSRLatch_0']['_DesignObj']._DesignParameter['_POLayerPINDrawing']['_XYCoordinates'][0][0] == self._DesignParameter['NMOS4_rInSRLatch_0']['_DesignObj']._DesignParameter['_POLayerPINDrawing']['_XYCoordinates'][(- 1)][0]):
		    mode = 'horizontal'
		    _width = self._DesignParameter['NMOS4_rInSRLatch_0']['_DesignObj']._DesignParameter['_POLayerPINDrawing']['_XWidth']
		elif (self._DesignParameter['NMOS4_rInSRLatch_0']['_DesignObj']._DesignParameter['_POLayerPINDrawing']['_XYCoordinates'][0][1] == self._DesignParameter['NMOS4_rInSRLatch_0']['_DesignObj']._DesignParameter['_POLayerPINDrawing']['_XYCoordinates'][(- 1)][1]):
		    mode = 'vertical'
		    _width = self._DesignParameter['NMOS4_rInSRLatch_0']['_DesignObj']._DesignParameter['_POLayerPINDrawing']['_XWidth']
		else:
		    print('Invalid Target Input')
		if (mode == 'vertical'):
		    xy_with_offset = []
		    target_y_value = (0 + self._DesignParameter['POLY_boundary_182']['_XYCoordinates'][0][1])
		    for i in range(len(self._DesignParameter['NMOS4_rInSRLatch_0']['_DesignObj']._DesignParameter['_POLayerPINDrawing']['_XYCoordinates'])):
		        xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['NMOS4_rInSRLatch_0']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['NMOS4_rInSRLatch_0']['_XYCoordinates'][0][1])], self._DesignParameter['NMOS4_rInSRLatch_0']['_DesignObj']._DesignParameter['_POLayerPINDrawing']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		elif (mode == 'horizontal'):
		    xy_with_offset = []
		    target_x_value = (0 + self._DesignParameter['POLY_boundary_182']['_XYCoordinates'][0][0])
		    for i in range(len(self._DesignParameter['NMOS4_rInSRLatch_0']['_DesignObj']._DesignParameter['_POLayerPINDrawing']['_XYCoordinates'])):
		        xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['NMOS4_rInSRLatch_0']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['NMOS4_rInSRLatch_0']['_XYCoordinates'][0][1])], self._DesignParameter['NMOS4_rInSRLatch_0']['_DesignObj']._DesignParameter['_POLayerPINDrawing']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		self._DesignParameter['nd4_gate_array'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _Width=_width)
		self._DesignParameter['nd4_gate_array']['_XYCoordinates'] = path_list
		self._DesignParameter['METAL1_path_2'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=50)
		self._DesignParameter['METAL1_path_2']['_XYCoordinates'] = [[[(+ self._DesignParameter['PCCAM1_nd4']['_XYCoordinates'][0][0]), (+ self._DesignParameter['PCCAM1_nd4']['_XYCoordinates'][0][1])], [(+ self._DesignParameter['PCCAM1_pd4']['_XYCoordinates'][0][0]), (+ self._DesignParameter['PCCAM1_pd4']['_XYCoordinates'][0][1])]]]
		self._DesignParameter['PCCAM1_pu2'] = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_Name='PCCAM1_pu2In{}'.format(_Name)))[0]
		self._DesignParameter['PCCAM1_pu2']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(**dict(_ViaPoly2Met1NumberOfCOX=1, _ViaPoly2Met1NumberOfCOY=1))
		self._DesignParameter['PCCAM1_pu2']['_XYCoordinates'] = [[self._DesignParameter['PMOS2InSRLatch_0']['_XYCoordinates'][0][0], ((- round((math.sqrt(((drc._PolygateMinSpace ** 2) - ((abs((((self._DesignParameter['NMOS2InSRLatch_0']['_XYCoordinates'][0][0] + self._DesignParameter['NMOS2InSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) - self._DesignParameter['NMOS2InSRLatch_0']['_XYCoordinates'][0][0]) + self._DesignParameter['NMOS2InSRLatch_0']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][0])) - ((self._DesignParameter['NMOS2InSRLatch_0']['_DesignObj']._DesignParameter['_PODummyLayer']['_XWidth'] + self._DesignParameter['PCCAM1_nu2']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']) / 2)) ** 2))) + (self._DesignParameter['PCCAM1_nu2']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2)))) + ((self._DesignParameter['PMOS2InSRLatch_0']['_XYCoordinates'][0][1] + self._DesignParameter['PMOS2InSRLatch_0']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][1]) - (self._DesignParameter['PMOS2InSRLatch_0']['_DesignObj']._DesignParameter['_PODummyLayer']['_YWidth'] / 2)))]]
		path_list = []
		if (len(self._DesignParameter['PMOS2InSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates']) == 1):
		    mode = 'vertical'
		    _width = self._DesignParameter['PMOS2InSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
		elif (self._DesignParameter['PMOS2InSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0] == self._DesignParameter['PMOS2InSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]):
		    mode = 'horizontal'
		    _width = self._DesignParameter['PMOS2InSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
		elif (self._DesignParameter['PMOS2InSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1] == self._DesignParameter['PMOS2InSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][1]):
		    mode = 'vertical'
		    _width = self._DesignParameter['PMOS2InSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
		else:
		    print('Invalid Target Input')
		if (mode == 'vertical'):
		    xy_with_offset = []
		    target_y_value = (0 + self._DesignParameter['PCCAM1_pu2']['_XYCoordinates'][0][1])
		    for i in range(len(self._DesignParameter['PMOS2InSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
		        xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['PMOS2InSRLatch_0']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['PMOS2InSRLatch_0']['_XYCoordinates'][0][1])], self._DesignParameter['PMOS2InSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		elif (mode == 'horizontal'):
		    xy_with_offset = []
		    target_x_value = (0 + self._DesignParameter['PCCAM1_pu2']['_XYCoordinates'][0][0])
		    for i in range(len(self._DesignParameter['PMOS2InSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
		        xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['PMOS2InSRLatch_0']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['PMOS2InSRLatch_0']['_XYCoordinates'][0][1])], self._DesignParameter['PMOS2InSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		self._DesignParameter['pu2_gate_array'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _Width=_width)
		self._DesignParameter['pu2_gate_array']['_XYCoordinates'] = path_list
		self._DesignParameter['METAL1_path_19'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=drc._Metal1MinWidth)
		self._DesignParameter['METAL1_path_19']['_XYCoordinates'] = [[[(+ self._DesignParameter['PCCAM1_pu2']['_XYCoordinates'][0][0]), (+ self._DesignParameter['PCCAM1_pu2']['_XYCoordinates'][0][1])], [(+ self._DesignParameter['PCCAM1_nu2']['_XYCoordinates'][0][0]), (+ self._DesignParameter['PCCAM1_nu2']['_XYCoordinates'][0][1])]]]
		self._DesignParameter['PCCAM1_pu4'] = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_Name='PCCAM1_pu4In{}'.format(_Name)))[0]
		self._DesignParameter['PCCAM1_pu4']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(**dict(_ViaPoly2Met1NumberOfCOX=max(1, (1 + int(((((((self._DesignParameter['PMOS4InSRLatch_0']['_XYCoordinates'][0][0] + self._DesignParameter['PMOS4InSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]) + (self._DesignParameter['PMOS4InSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)) - ((self._DesignParameter['PMOS4InSRLatch_0']['_XYCoordinates'][0][0] + self._DesignParameter['PMOS4InSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['PMOS4InSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2))) - drc._CoMinSpace) - (2 * drc._CoMinEnclosureByPO)) / (drc._CoMinWidth + drc._CoMinSpace))))), _ViaPoly2Met1NumberOfCOY=1))
		self._DesignParameter['PCCAM1_pu4']['_XYCoordinates'] = [[self._DesignParameter['PMOS4InSRLatch_0']['_XYCoordinates'][0][0], ((((self._DesignParameter['PMOS4InSRLatch_0']['_XYCoordinates'][0][1] + self._DesignParameter['PMOS4InSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) - (self._DesignParameter['PMOS4InSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)) - drc._Metal1MinSpace2) - (self._DesignParameter['PCCAM1_pu4']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2))]]
		self._DesignParameter['POLY_boundary_185'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _XWidth=(((self._DesignParameter['PMOS4InSRLatch_0']['_XYCoordinates'][0][0] + self._DesignParameter['PMOS4InSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]) + (self._DesignParameter['PMOS4InSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)) - ((self._DesignParameter['PMOS4InSRLatch_0']['_XYCoordinates'][0][0] + self._DesignParameter['PMOS4InSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['PMOS4InSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2))), _YWidth=self._DesignParameter['PCCAM1_pu4']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'])
		self._DesignParameter['POLY_boundary_185']['_XYCoordinates'] = [[(+ self._DesignParameter['PCCAM1_pu4']['_XYCoordinates'][0][0]), (+ self._DesignParameter['PCCAM1_pu4']['_XYCoordinates'][0][1])]]
		path_list = []
		if (len(self._DesignParameter['PMOS4InSRLatch_0']['_DesignObj']._DesignParameter['_POLayerPINDrawing']['_XYCoordinates']) == 1):
		    mode = 'vertical'
		    _width = self._DesignParameter['PMOS4InSRLatch_0']['_DesignObj']._DesignParameter['_POLayerPINDrawing']['_XWidth']
		elif (self._DesignParameter['PMOS4InSRLatch_0']['_DesignObj']._DesignParameter['_POLayerPINDrawing']['_XYCoordinates'][0][0] == self._DesignParameter['PMOS4InSRLatch_0']['_DesignObj']._DesignParameter['_POLayerPINDrawing']['_XYCoordinates'][(- 1)][0]):
		    mode = 'horizontal'
		    _width = self._DesignParameter['PMOS4InSRLatch_0']['_DesignObj']._DesignParameter['_POLayerPINDrawing']['_XWidth']
		elif (self._DesignParameter['PMOS4InSRLatch_0']['_DesignObj']._DesignParameter['_POLayerPINDrawing']['_XYCoordinates'][0][1] == self._DesignParameter['PMOS4InSRLatch_0']['_DesignObj']._DesignParameter['_POLayerPINDrawing']['_XYCoordinates'][(- 1)][1]):
		    mode = 'vertical'
		    _width = self._DesignParameter['PMOS4InSRLatch_0']['_DesignObj']._DesignParameter['_POLayerPINDrawing']['_XWidth']
		else:
		    print('Invalid Target Input')
		if (mode == 'vertical'):
		    xy_with_offset = []
		    target_y_value = (0 + self._DesignParameter['POLY_boundary_185']['_XYCoordinates'][0][1])
		    for i in range(len(self._DesignParameter['PMOS4InSRLatch_0']['_DesignObj']._DesignParameter['_POLayerPINDrawing']['_XYCoordinates'])):
		        xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['PMOS4InSRLatch_0']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['PMOS4InSRLatch_0']['_XYCoordinates'][0][1])], self._DesignParameter['PMOS4InSRLatch_0']['_DesignObj']._DesignParameter['_POLayerPINDrawing']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		elif (mode == 'horizontal'):
		    xy_with_offset = []
		    target_x_value = (0 + self._DesignParameter['POLY_boundary_185']['_XYCoordinates'][0][0])
		    for i in range(len(self._DesignParameter['PMOS4InSRLatch_0']['_DesignObj']._DesignParameter['_POLayerPINDrawing']['_XYCoordinates'])):
		        xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['PMOS4InSRLatch_0']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['PMOS4InSRLatch_0']['_XYCoordinates'][0][1])], self._DesignParameter['PMOS4InSRLatch_0']['_DesignObj']._DesignParameter['_POLayerPINDrawing']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		self._DesignParameter['pu4_gate_array'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _Width=_width)
		self._DesignParameter['pu4_gate_array']['_XYCoordinates'] = path_list
		self._DesignParameter['METAL1_path_3'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=drc._Metal1MinWidth)
		self._DesignParameter['METAL1_path_3']['_XYCoordinates'] = [[[(+ self._DesignParameter['PCCAM1_pu4']['_XYCoordinates'][0][0]), (+ self._DesignParameter['PCCAM1_pu4']['_XYCoordinates'][0][1])], [(+ self._DesignParameter['PCCAM1_nu4']['_XYCoordinates'][0][0]), (+ self._DesignParameter['PCCAM1_nu4']['_XYCoordinates'][0][1])]]]
		self._DesignParameter['PCCAM1_pu3'] = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_Name='PCCAM1_pu3In{}'.format(_Name)))[0]
		self._DesignParameter['PCCAM1_pu3']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(**dict(_ViaPoly2Met1NumberOfCOX=1, _ViaPoly2Met1NumberOfCOY=1))
		self._DesignParameter['PCCAM1_pu3']['_XYCoordinates'] = [[self._DesignParameter['PMOS3InSRLatch_0']['_XYCoordinates'][0][0], ((((self._DesignParameter['PMOS3InSRLatch_0']['_XYCoordinates'][0][1] + self._DesignParameter['PMOS3InSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) - (self._DesignParameter['PMOS3InSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)) - drc._Metal1MinSpace2) - (self._DesignParameter['PCCAM1_pu3']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2))]]
		self._DesignParameter['POLY_boundary_193'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _XWidth=(((self._DesignParameter['PMOS3InSRLatch_0']['_XYCoordinates'][0][0] + self._DesignParameter['PMOS3InSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]) + (self._DesignParameter['PMOS3InSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)) - ((self._DesignParameter['PMOS3InSRLatch_0']['_XYCoordinates'][0][0] + self._DesignParameter['PMOS3InSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['PMOS3InSRLatch_0']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2))), _YWidth=self._DesignParameter['PCCAM1_pu3']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'])
		self._DesignParameter['POLY_boundary_193']['_XYCoordinates'] = [[(+ self._DesignParameter['PCCAM1_pu3']['_XYCoordinates'][0][0]), (+ self._DesignParameter['PCCAM1_pu3']['_XYCoordinates'][0][1])]]
		path_list = []
		if (len(self._DesignParameter['PMOS3InSRLatch_0']['_DesignObj']._DesignParameter['_POLayerPINDrawing']['_XYCoordinates']) == 1):
		    mode = 'vertical'
		    _width = self._DesignParameter['PMOS3InSRLatch_0']['_DesignObj']._DesignParameter['_POLayerPINDrawing']['_XWidth']
		elif (self._DesignParameter['PMOS3InSRLatch_0']['_DesignObj']._DesignParameter['_POLayerPINDrawing']['_XYCoordinates'][0][0] == self._DesignParameter['PMOS3InSRLatch_0']['_DesignObj']._DesignParameter['_POLayerPINDrawing']['_XYCoordinates'][(- 1)][0]):
		    mode = 'horizontal'
		    _width = self._DesignParameter['PMOS3InSRLatch_0']['_DesignObj']._DesignParameter['_POLayerPINDrawing']['_XWidth']
		elif (self._DesignParameter['PMOS3InSRLatch_0']['_DesignObj']._DesignParameter['_POLayerPINDrawing']['_XYCoordinates'][0][1] == self._DesignParameter['PMOS3InSRLatch_0']['_DesignObj']._DesignParameter['_POLayerPINDrawing']['_XYCoordinates'][(- 1)][1]):
		    mode = 'vertical'
		    _width = self._DesignParameter['PMOS3InSRLatch_0']['_DesignObj']._DesignParameter['_POLayerPINDrawing']['_XWidth']
		else:
		    print('Invalid Target Input')
		if (mode == 'vertical'):
		    xy_with_offset = []
		    target_y_value = (0 + self._DesignParameter['POLY_boundary_193']['_XYCoordinates'][0][1])
		    for i in range(len(self._DesignParameter['PMOS3InSRLatch_0']['_DesignObj']._DesignParameter['_POLayerPINDrawing']['_XYCoordinates'])):
		        xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['PMOS3InSRLatch_0']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['PMOS3InSRLatch_0']['_XYCoordinates'][0][1])], self._DesignParameter['PMOS3InSRLatch_0']['_DesignObj']._DesignParameter['_POLayerPINDrawing']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		elif (mode == 'horizontal'):
		    xy_with_offset = []
		    target_x_value = (0 + self._DesignParameter['POLY_boundary_193']['_XYCoordinates'][0][0])
		    for i in range(len(self._DesignParameter['PMOS3InSRLatch_0']['_DesignObj']._DesignParameter['_POLayerPINDrawing']['_XYCoordinates'])):
		        xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['PMOS3InSRLatch_0']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['PMOS3InSRLatch_0']['_XYCoordinates'][0][1])], self._DesignParameter['PMOS3InSRLatch_0']['_DesignObj']._DesignParameter['_POLayerPINDrawing']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		self._DesignParameter['pu3_gate_array'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _Width=_width)
		self._DesignParameter['pu3_gate_array']['_XYCoordinates'] = path_list
		self._DesignParameter['M1V1M2_p3_gate_via'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='M1V1M2_p3_gate_viaIn{}'.format(_Name)))[0]
		self._DesignParameter['M1V1M2_p3_gate_via']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureY(**dict(_ViaMet12Met2NumberOfCOX=2, _ViaMet12Met2NumberOfCOY=1))
		self._DesignParameter['M1V1M2_p3_gate_via']['_XYCoordinates'] = [[self._DesignParameter['nu3_gate_vias']['_XYCoordinates'][0][0], (((self._DesignParameter['METAL2_path_22']['_XYCoordinates'][0][0][1] - (self._DesignParameter['METAL2_path_22']['_Width'] / 2)) - drc._MetalxMinSpace2) - (self._DesignParameter['M1V1M2_p3_gate_via']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] / 2))]]
		self._DesignParameter['METAL2_path_15'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _Width=drc._MetalxMinWidth)
		self._DesignParameter['METAL2_path_15']['_XYCoordinates'] = [[[(+ self._DesignParameter['nu2_drain_via12']['_XYCoordinates'][(- 1)][0]), (+ self._DesignParameter['nu2_drain_via12']['_XYCoordinates'][(- 1)][1])], [self._DesignParameter['nu2_drain_via12']['_XYCoordinates'][(- 1)][0], self._DesignParameter['pu2_drain_via']['_XYCoordinates'][0][1]]]]
		self._DesignParameter['METAL2_path_8'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _Width=drc._MetalxMinWidth)
		self._DesignParameter['METAL2_path_8']['_XYCoordinates'] = [[[(+ self._DesignParameter['M1V1M2_p3_gate_via']['_XYCoordinates'][0][0]), (+ self._DesignParameter['M1V1M2_p3_gate_via']['_XYCoordinates'][0][1])], [self._DesignParameter['METAL2_path_15']['_XYCoordinates'][0][0][0], self._DesignParameter['M1V1M2_p3_gate_via']['_XYCoordinates'][0][1]]]]
		self._DesignParameter['METAL2_path_14'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _Width=drc._MetalxMinWidth)
		self._DesignParameter['METAL2_path_14']['_XYCoordinates'] = [[[(+ self._DesignParameter['M1V1M2_nu_1']['_XYCoordinates'][0][0]), (+ self._DesignParameter['M1V1M2_nu_1']['_XYCoordinates'][0][1])], [self._DesignParameter['METAL2_path_15']['_XYCoordinates'][0][0][0], self._DesignParameter['M1V1M2_nu_1']['_XYCoordinates'][0][1]]]]
		self._DesignParameter['M3V3M4_upupright'] = self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_Name='M3V3M4_upuprightIn{}'.format(_Name)))[0]
		self._DesignParameter['M3V3M4_upupright']['_DesignObj']._CalculateViaMet32Met4DesignParameterMinimumEnclosureY(**dict(_ViaMet32Met4NumberOfCOX=2, _ViaMet32Met4NumberOfCOY=1))
		self._DesignParameter['M3V3M4_upupright']['_XYCoordinates'] = [[self._DesignParameter['nu3_gate_vias']['_XYCoordinates'][0][0], (((self._DesignParameter['METAL2_path_22']['_XYCoordinates'][0][0][1] - (self._DesignParameter['METAL2_path_22']['_Width'] / 2)) - drc._MetalxMinSpace2) - (self._DesignParameter['M1V1M2_p3_gate_via']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] / 2))]]
		self._DesignParameter['METAL3_path_24'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0], _Datatype=DesignParameters._LayerMapping['METAL3'][1], _Width=drc._MetalxMinWidth)
		self._DesignParameter['METAL3_path_24']['_XYCoordinates'] = [[[(+ self._DesignParameter['M1V1M2_p3_gate_via']['_XYCoordinates'][0][0]), (+ self._DesignParameter['M1V1M2_p3_gate_via']['_XYCoordinates'][0][1])], [(((self._DesignParameter['pu1_gate_vias']['_XYCoordinates'][0][0] + self._DesignParameter['pu1_gate_vias']['_DesignObj']._DesignParameter['ViaMet22Met3']['_XYCoordinates'][0][0]) + self._DesignParameter['pu1_gate_vias']['_DesignObj']._DesignParameter['ViaMet22Met3']['_DesignObj']._DesignParameter['_Met3Layer']['_XYCoordinates'][0][0]) - (self._DesignParameter['pu1_gate_vias']['_DesignObj']._DesignParameter['ViaMet22Met3']['_DesignObj']._DesignParameter['_Met3Layer']['_XWidth'] / 2)), self._DesignParameter['M1V1M2_p3_gate_via']['_XYCoordinates'][0][1]]]]
		self._DesignParameter['METAL1_boundary_197'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _XWidth=max(self._DesignParameter['PCCAM1_pu3']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'], self._DesignParameter['M1V1M2_p3_gate_via']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']), _YWidth=self._DesignParameter['PCCAM1_pu3']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'])
		self._DesignParameter['METAL1_boundary_197']['_XYCoordinates'] = [[(+ self._DesignParameter['PCCAM1_pu3']['_XYCoordinates'][0][0]), (+ self._DesignParameter['PCCAM1_pu3']['_XYCoordinates'][0][1])]]
		self._DesignParameter['via1to4_lu'] = self._SrefElementDeclaration(_DesignObj=ViaStack._ViaStack(_Name='via1to4_luIn{}'.format(_Name)))[0]
		self._DesignParameter['via1to4_lu']['_DesignObj']._CalculateStackMinimumEnclosureY(**dict(COX=2, COY=1, start_layer=1, end_layer=4))
		self._DesignParameter['via1to4_lu']['_XYCoordinates'] = [[self._DesignParameter['M1V1M2_nu_1']['_XYCoordinates'][0][0], ((self._DesignParameter['pu1_gate_vias']['_XYCoordinates'][0][1] + self._DesignParameter['M1V1M2_nu_1']['_XYCoordinates'][0][1]) / 2)]]
		self._DesignParameter['METAL1_path_20'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=drc._MetalxMinWidth)
		self._DesignParameter['METAL1_path_20']['_XYCoordinates'] = [[[(+ self._DesignParameter['via1to4_lu']['_XYCoordinates'][0][0]), (+ self._DesignParameter['via1to4_lu']['_XYCoordinates'][0][1])], [self._DesignParameter['METAL1_path_19']['_XYCoordinates'][0][0][0], self._DesignParameter['via1to4_lu']['_XYCoordinates'][0][1]]]]
		self._DesignParameter['METAL4_path_11'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL4'][0], _Datatype=DesignParameters._LayerMapping['METAL4'][1], _Width=self._DesignParameter['via1to4_lu']['_DesignObj']._DesignParameter['ViaMet32Met4']['_DesignObj']._DesignParameter['_Met4Layer']['_XWidth'])
		self._DesignParameter['METAL4_path_11']['_XYCoordinates'] = [[[(+ self._DesignParameter['via1to4_lu']['_XYCoordinates'][0][0]), (+ self._DesignParameter['via1to4_lu']['_XYCoordinates'][0][1])], [(+ self._DesignParameter['pd1_gate_vias']['_XYCoordinates'][0][0]), (+ self._DesignParameter['pd1_gate_vias']['_XYCoordinates'][0][1])]]]
		self._DesignParameter['via1to4_rd'] = self._SrefElementDeclaration(_DesignObj=ViaStack._ViaStack(_Name='via1to4_rdIn{}'.format(_Name)))[0]
		self._DesignParameter['via1to4_rd']['_DesignObj']._CalculateStackMinimumEnclosureY(**dict(COX=2, COY=1, start_layer=1, end_layer=4))
		self._DesignParameter['via1to4_rd']['_XYCoordinates'] = [[((self._DesignParameter['M3V3M4_upupright']['_XYCoordinates'][0][0] + (- int(((drc._VIAxMinWidth + drc._VIAxMinSpace) / 4)))) + (- int(((drc._VIAxMinWidth + drc._VIAxMinSpace) / 4)))), ((self._DesignParameter['M1V1M2_pd3_gate']['_XYCoordinates'][0][1] + self._DesignParameter['nd3_gate_vias']['_XYCoordinates'][0][1]) / 2)]]
		self._DesignParameter['METAL1_path_21'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=drc._Metal1MinWidth)
		self._DesignParameter['METAL1_path_21']['_XYCoordinates'] = [[[(+ self._DesignParameter['via1to4_rd']['_XYCoordinates'][0][0]), (+ self._DesignParameter['via1to4_rd']['_XYCoordinates'][0][1])], [self._DesignParameter['METAL1_path_18']['_XYCoordinates'][0][0][0], self._DesignParameter['via1to4_rd']['_XYCoordinates'][0][1]]]]
		self._DesignParameter['METAL4_path_9'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL4'][0], _Datatype=DesignParameters._LayerMapping['METAL4'][1], _Width=self._DesignParameter['via1to4_rd']['_DesignObj']._DesignParameter['ViaMet32Met4']['_DesignObj']._DesignParameter['_Met4Layer']['_XWidth'])
		self._DesignParameter['METAL4_path_9']['_XYCoordinates'] = [[[(+ self._DesignParameter['M3V3M4_upupright']['_XYCoordinates'][0][0]), (+ self._DesignParameter['M3V3M4_upupright']['_XYCoordinates'][0][1])], [self._DesignParameter['M3V3M4_upupright']['_XYCoordinates'][0][0], (((self._DesignParameter['via1to4_rd']['_XYCoordinates'][0][1] + self._DesignParameter['via1to4_rd']['_DesignObj']._DesignParameter['ViaMet32Met4']['_XYCoordinates'][0][1]) + self._DesignParameter['via1to4_rd']['_DesignObj']._DesignParameter['ViaMet32Met4']['_DesignObj']._DesignParameter['_Met4Layer']['_XYCoordinates'][0][1]) - (self._DesignParameter['via1to4_rd']['_DesignObj']._DesignParameter['ViaMet32Met4']['_DesignObj']._DesignParameter['_Met4Layer']['_YWidth'] / 2))]]]
		self._DesignParameter['METAL2_path_25'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _Width=drc._MetalxMinWidth)
		self._DesignParameter['METAL2_path_25']['_XYCoordinates'] = [[[(+ self._DesignParameter['nd1_drain_vias']['_XYCoordinates'][0][0]), (+ self._DesignParameter['nd1_drain_vias']['_XYCoordinates'][0][1])], [(+ self._DesignParameter['nd1_drain_vias']['_XYCoordinates'][(- 1)][0]), (+ self._DesignParameter['nd1_drain_vias']['_XYCoordinates'][(- 1)][1])]]]
		self._DesignParameter['M3V3M4_CDNS_6375475055652_2'] = self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_Name='M3V3M4_CDNS_6375475055652_2In{}'.format(_Name)))[0]
		self._DesignParameter['M3V3M4_CDNS_6375475055652_2']['_DesignObj']._CalculateViaMet32Met4DesignParameterMinimumEnclosureX(**dict(_ViaMet32Met4NumberOfCOX=1, _ViaMet32Met4NumberOfCOY=2))
		self._DesignParameter['M3V3M4_CDNS_6375475055652_2']['_XYCoordinates'] = [[(((self._DesignParameter['M3V3M4_CDNS_6375475055652_2']['_DesignObj']._DesignParameter['_Met4Layer']['_XWidth'] / 2) + (((self._DesignParameter['via1to4_rd']['_XYCoordinates'][0][0] + self._DesignParameter['via1to4_rd']['_DesignObj']._DesignParameter['ViaMet32Met4']['_XYCoordinates'][0][0]) + self._DesignParameter['via1to4_rd']['_DesignObj']._DesignParameter['ViaMet32Met4']['_DesignObj']._DesignParameter['_Met4Layer']['_XYCoordinates'][0][0]) + (self._DesignParameter['via1to4_rd']['_DesignObj']._DesignParameter['ViaMet32Met4']['_DesignObj']._DesignParameter['_Met4Layer']['_XWidth'] / 2))) + drc._MetalxMinSpace6), ((self._DesignParameter['pd1_drain_vias']['_XYCoordinates'][0][1] + (self._DesignParameter['M3V3M4_CDNS_6375475055652_2']['_DesignObj']._DesignParameter['_Met4Layer']['_YWidth'] / 2)) - (drc._MetalxMinWidth / 2))]]
		self._DesignParameter['METAL3_path_25'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0], _Datatype=DesignParameters._LayerMapping['METAL3'][1], _Width=drc._MetalxMinWidth)
		self._DesignParameter['METAL3_path_25']['_XYCoordinates'] = [[[(+ self._DesignParameter['pd1_drain_vias']['_XYCoordinates'][0][0]), (+ self._DesignParameter['pd1_drain_vias']['_XYCoordinates'][0][1])], [self._DesignParameter['M3V3M4_CDNS_6375475055652_2']['_XYCoordinates'][0][0], self._DesignParameter['pd1_drain_vias']['_XYCoordinates'][0][1]]]]
		self._DesignParameter['M3V3M4_CDNS_6375475055652_3'] = self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_Name='M3V3M4_CDNS_6375475055652_3In{}'.format(_Name)))[0]
		self._DesignParameter['M3V3M4_CDNS_6375475055652_3']['_DesignObj']._CalculateViaMet32Met4DesignParameterMinimumEnclosureX(**dict(_ViaMet32Met4NumberOfCOX=1, _ViaMet32Met4NumberOfCOY=2))
		self._DesignParameter['M3V3M4_CDNS_6375475055652_3']['_XYCoordinates'] = [[self._DesignParameter['M3V3M4_CDNS_6375475055652_2']['_XYCoordinates'][0][0], ((self._DesignParameter['nd1_drain_vias']['_XYCoordinates'][0][1] - (self._DesignParameter['M3V3M4_CDNS_6375475055652_3']['_DesignObj']._DesignParameter['_Met4Layer']['_YWidth'] / 2)) + (drc._MetalxMinWidth / 2))]]
		self._DesignParameter['ur_vias14'] = self._SrefElementDeclaration(_DesignObj=ViaStack._ViaStack(_Name='ur_vias14In{}'.format(_Name)))[0]
		self._DesignParameter['ur_vias14']['_DesignObj']._CalculateStackMinimumEnclosureY(**dict(COX=2, COY=1, start_layer=1, end_layer=4))
		self._DesignParameter['ur_vias14']['_XYCoordinates'] = [[((self._DesignParameter['METAL1_path_3']['_XYCoordinates'][0][0][0] + (drc._Metal1MinWidth / 2)) + (self._DesignParameter['ur_vias14']['_DesignObj']._DesignParameter['ViaMet12Met2']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth'] / 2)), ((self._DesignParameter['PCCAM1_pu4']['_XYCoordinates'][0][1] + self._DesignParameter['PCCAM1_nu4']['_XYCoordinates'][0][1]) / 2)]]
		self._DesignParameter['M3V3M4_CDNS_6375475055652_4'] = self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_Name='M3V3M4_CDNS_6375475055652_4In{}'.format(_Name)))[0]
		self._DesignParameter['M3V3M4_CDNS_6375475055652_4']['_DesignObj']._CalculateViaMet32Met4DesignParameterMinimumEnclosureX(**dict(_ViaMet32Met4NumberOfCOX=1, _ViaMet32Met4NumberOfCOY=2))
		self._DesignParameter['M3V3M4_CDNS_6375475055652_4']['_XYCoordinates'] = [[self._DesignParameter['ur_vias14']['_XYCoordinates'][0][0], self._DesignParameter['nd1_drain_vias']['_XYCoordinates'][0][1]]]
		self._DesignParameter['M1V1M2_CDNS_6375475055616_7'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='M1V1M2_CDNS_6375475055616_7In{}'.format(_Name)))[0]
		self._DesignParameter['M1V1M2_CDNS_6375475055616_7']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureY(**dict(_ViaMet12Met2NumberOfCOX=2, _ViaMet12Met2NumberOfCOY=1))
		self._DesignParameter['M1V1M2_CDNS_6375475055616_7']['_XYCoordinates'] = [[self._DesignParameter['ur_vias14']['_XYCoordinates'][0][0], ((self._DesignParameter['PCCAM1_nd4']['_XYCoordinates'][0][1] + self._DesignParameter['PCCAM1_pd4']['_XYCoordinates'][0][1]) / 2)]]
		self._DesignParameter['M2V2M3_CDNS_6375475055631_16'] = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_Name='M2V2M3_CDNS_6375475055631_16In{}'.format(_Name)))[0]
		self._DesignParameter['M2V2M3_CDNS_6375475055631_16']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureX(**dict(_ViaMet22Met3NumberOfCOX=1, _ViaMet22Met3NumberOfCOY=2))
		self._DesignParameter['M2V2M3_CDNS_6375475055631_16']['_XYCoordinates'] = [[self._DesignParameter['M1V1M2_CDNS_6375475055616_7']['_XYCoordinates'][0][0], self._DesignParameter['nu1_drain_via23']['_XYCoordinates'][0][1]]]
		self._DesignParameter['METAL3_path_19'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0], _Datatype=DesignParameters._LayerMapping['METAL3'][1], _Width=drc._MetalxMinWidth)
		self._DesignParameter['METAL3_path_19']['_XYCoordinates'] = [[[(+ self._DesignParameter['nd1_drain_vias']['_XYCoordinates'][0][0]), (+ self._DesignParameter['nd1_drain_vias']['_XYCoordinates'][0][1])], [self._DesignParameter['M3V3M4_CDNS_6375475055652_4']['_XYCoordinates'][0][0], self._DesignParameter['nd1_drain_vias']['_XYCoordinates'][0][1]]]]
		self._DesignParameter['METAL3_path_20'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0], _Datatype=DesignParameters._LayerMapping['METAL3'][1], _Width=drc._MetalxMinWidth)
		self._DesignParameter['METAL3_path_20']['_XYCoordinates'] = [[[(+ self._DesignParameter['nu1_drain_via23']['_XYCoordinates'][0][0]), (+ self._DesignParameter['nu1_drain_via23']['_XYCoordinates'][0][1])], [self._DesignParameter['M2V2M3_CDNS_6375475055631_16']['_XYCoordinates'][0][0], self._DesignParameter['nu1_drain_via23']['_XYCoordinates'][0][1]]]]
		self._DesignParameter['METAL4_path_10'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL4'][0], _Datatype=DesignParameters._LayerMapping['METAL4'][1], _Width=(drc._MetalxMinWidth * 2))
		self._DesignParameter['METAL4_path_10']['_XYCoordinates'] = [[[(+ self._DesignParameter['ur_vias14']['_XYCoordinates'][0][0]), (+ self._DesignParameter['ur_vias14']['_XYCoordinates'][0][1])], [self._DesignParameter['ur_vias14']['_XYCoordinates'][0][0], ((self._DesignParameter['M3V3M4_CDNS_6375475055652_4']['_XYCoordinates'][0][1] + self._DesignParameter['M3V3M4_CDNS_6375475055652_4']['_DesignObj']._DesignParameter['_Met4Layer']['_XYCoordinates'][0][1]) - (self._DesignParameter['M3V3M4_CDNS_6375475055652_4']['_DesignObj']._DesignParameter['_Met4Layer']['_YWidth'] / 2))]]]
		self._DesignParameter['METAL2_path_6'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _Width=(drc._MetalxMinWidth * 2))
		self._DesignParameter['METAL2_path_6']['_XYCoordinates'] = [[[(+ self._DesignParameter['M1V1M2_CDNS_6375475055616_7']['_XYCoordinates'][0][0]), (+ self._DesignParameter['M1V1M2_CDNS_6375475055616_7']['_XYCoordinates'][0][1])], [self._DesignParameter['M1V1M2_CDNS_6375475055616_7']['_XYCoordinates'][0][0], ((self._DesignParameter['M2V2M3_CDNS_6375475055631_16']['_XYCoordinates'][0][1] + self._DesignParameter['M2V2M3_CDNS_6375475055631_16']['_DesignObj']._DesignParameter['_Met3Layer']['_XYCoordinates'][0][1]) + (self._DesignParameter['M2V2M3_CDNS_6375475055631_16']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth'] / 2))]]]
		self._DesignParameter['METAL4_path_12'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL4'][0], _Datatype=DesignParameters._LayerMapping['METAL4'][1], _Width=drc._MetalxMinWidth)
		self._DesignParameter['METAL4_path_12']['_XYCoordinates'] = [[[(+ self._DesignParameter['M3V3M4_CDNS_6375475055652_3']['_XYCoordinates'][0][0]), (+ self._DesignParameter['M3V3M4_CDNS_6375475055652_3']['_XYCoordinates'][0][1])], [(+ self._DesignParameter['M3V3M4_CDNS_6375475055652_2']['_XYCoordinates'][0][0]), (+ self._DesignParameter['M3V3M4_CDNS_6375475055652_2']['_XYCoordinates'][0][1])]]]
		self._DesignParameter['M3V3M4_CDNS_6375475055652_1'] = self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_Name='M3V3M4_CDNS_6375475055652_1In{}'.format(_Name)))[0]
		self._DesignParameter['M3V3M4_CDNS_6375475055652_1']['_DesignObj']._CalculateViaMet32Met4DesignParameterMinimumEnclosureX(**dict(_ViaMet32Met4NumberOfCOX=1, _ViaMet32Met4NumberOfCOY=2))
		self._DesignParameter['M3V3M4_CDNS_6375475055652_1']['_XYCoordinates'] = [[self._DesignParameter['M3V3M4_CDNS_6375475055652_3']['_XYCoordinates'][0][0], ((self._DesignParameter['nu1_drain_via23']['_XYCoordinates'][0][1] + (self._DesignParameter['M3V3M4_CDNS_6375475055652_1']['_DesignObj']._DesignParameter['_Met4Layer']['_YWidth'] / 2)) - (drc._MetalxMinWidth / 2))]]
		self._DesignParameter['M3V3M4_CDNS_6375475055652_0'] = self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_Name='M3V3M4_CDNS_6375475055652_0In{}'.format(_Name)))[0]
		self._DesignParameter['M3V3M4_CDNS_6375475055652_0']['_DesignObj']._CalculateViaMet32Met4DesignParameterMinimumEnclosureX(**dict(_ViaMet32Met4NumberOfCOX=1, _ViaMet32Met4NumberOfCOY=2))
		self._DesignParameter['M3V3M4_CDNS_6375475055652_0']['_XYCoordinates'] = [[self._DesignParameter['M3V3M4_CDNS_6375475055652_1']['_XYCoordinates'][0][0], ((self._DesignParameter['pu_drain_vias']['_XYCoordinates'][0][1] - (self._DesignParameter['M3V3M4_CDNS_6375475055652_0']['_DesignObj']._DesignParameter['_Met4Layer']['_YWidth'] / 2)) + (drc._MetalxMinWidth / 2))]]
		self._DesignParameter['METAL3_path_26'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0], _Datatype=DesignParameters._LayerMapping['METAL3'][1], _Width=drc._MetalxMinWidth)
		self._DesignParameter['METAL3_path_26']['_XYCoordinates'] = [[[(+ self._DesignParameter['pu_drain_vias']['_XYCoordinates'][0][0]), (+ self._DesignParameter['pu_drain_vias']['_XYCoordinates'][0][1])], [self._DesignParameter['M3V3M4_CDNS_6375475055652_0']['_XYCoordinates'][0][0], self._DesignParameter['pu_drain_vias']['_XYCoordinates'][0][1]]]]
		self._DesignParameter['METAL4_path_13'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL4'][0], _Datatype=DesignParameters._LayerMapping['METAL4'][1], _Width=drc._MetalxMinWidth)
		self._DesignParameter['METAL4_path_13']['_XYCoordinates'] = [[[(+ self._DesignParameter['M3V3M4_CDNS_6375475055652_0']['_XYCoordinates'][0][0]), (+ self._DesignParameter['M3V3M4_CDNS_6375475055652_0']['_XYCoordinates'][0][1])], [(+ self._DesignParameter['M3V3M4_CDNS_6375475055652_1']['_XYCoordinates'][0][0]), (+ self._DesignParameter['M3V3M4_CDNS_6375475055652_1']['_XYCoordinates'][0][1])]]]
		self._DesignParameter['SLVT_path_2'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['SLVT'][0], _Datatype=DesignParameters._LayerMapping['SLVT'][1], _Width=self._DesignParameter['NMOS4_rInSRLatch_0']['_DesignObj']._DesignParameter['_SLVTLayer']['_YWidth'])
		self._DesignParameter['SLVT_path_2']['_XYCoordinates'] = [[[(+ ((self._DesignParameter['NMOS1_rInSRLatch_0']['_XYCoordinates'][0][0] + self._DesignParameter['NMOS1_rInSRLatch_0']['_DesignObj']._DesignParameter['_SLVTLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['NMOS1_rInSRLatch_0']['_DesignObj']._DesignParameter['_SLVTLayer']['_XWidth'] / 2))), (+ (self._DesignParameter['NMOS1_rInSRLatch_0']['_XYCoordinates'][0][1] + self._DesignParameter['NMOS1_rInSRLatch_0']['_DesignObj']._DesignParameter['_SLVTLayer']['_XYCoordinates'][0][1]))], [(+ ((self._DesignParameter['NMOS4_rInSRLatch_0']['_XYCoordinates'][0][0] + self._DesignParameter['NMOS4_rInSRLatch_0']['_DesignObj']._DesignParameter['_SLVTLayer']['_XYCoordinates'][0][0]) + (self._DesignParameter['NMOS4_rInSRLatch_0']['_DesignObj']._DesignParameter['_SLVTLayer']['_XWidth'] / 2))), (+ (self._DesignParameter['NMOS4_rInSRLatch_0']['_XYCoordinates'][0][1] + self._DesignParameter['NMOS4_rInSRLatch_0']['_DesignObj']._DesignParameter['_SLVTLayer']['_XYCoordinates'][0][1]))]]]
		self._DesignParameter['SLVT_path_3'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['SLVT'][0], _Datatype=DesignParameters._LayerMapping['SLVT'][1], _Width=self._DesignParameter['NMOS4InSRLatch_0']['_DesignObj']._DesignParameter['_SLVTLayer']['_YWidth'])
		self._DesignParameter['SLVT_path_3']['_XYCoordinates'] = [[[(+ ((self._DesignParameter['NMOS1InSRLatch_0']['_XYCoordinates'][0][0] + self._DesignParameter['NMOS1InSRLatch_0']['_DesignObj']._DesignParameter['_SLVTLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['NMOS1InSRLatch_0']['_DesignObj']._DesignParameter['_SLVTLayer']['_XWidth'] / 2))), (+ (self._DesignParameter['NMOS1InSRLatch_0']['_XYCoordinates'][0][1] + self._DesignParameter['NMOS1InSRLatch_0']['_DesignObj']._DesignParameter['_SLVTLayer']['_XYCoordinates'][0][1]))], [((self._DesignParameter['NMOS4InSRLatch_0']['_XYCoordinates'][0][0] + self._DesignParameter['NMOS4InSRLatch_0']['_DesignObj']._DesignParameter['_SLVTLayer']['_XYCoordinates'][0][0]) + (self._DesignParameter['NMOS4InSRLatch_0']['_DesignObj']._DesignParameter['_SLVTLayer']['_XWidth'] / 2)), (self._DesignParameter['NMOS1InSRLatch_0']['_XYCoordinates'][0][1] + self._DesignParameter['NMOS1InSRLatch_0']['_DesignObj']._DesignParameter['_SLVTLayer']['_XYCoordinates'][0][1])]]]
		self._DesignParameter['PIMP_path_3'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['PIMP'][0], _Datatype=DesignParameters._LayerMapping['PIMP'][1], _Width=self._DesignParameter['PMOS1InSRLatch_0']['_DesignObj']._DesignParameter['_PPLayer']['_YWidth'])
		self._DesignParameter['PIMP_path_3']['_XYCoordinates'] = [[[(+ ((self._DesignParameter['PMOS1InSRLatch_0']['_XYCoordinates'][0][0] + self._DesignParameter['PMOS1InSRLatch_0']['_DesignObj']._DesignParameter['_SLVTLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['PMOS1InSRLatch_0']['_DesignObj']._DesignParameter['_SLVTLayer']['_XWidth'] / 2))), (+ (self._DesignParameter['PMOS1InSRLatch_0']['_XYCoordinates'][0][1] + self._DesignParameter['PMOS1InSRLatch_0']['_DesignObj']._DesignParameter['_SLVTLayer']['_XYCoordinates'][0][1]))], [(+ ((self._DesignParameter['PMOS4InSRLatch_0']['_XYCoordinates'][0][0] + self._DesignParameter['PMOS4InSRLatch_0']['_DesignObj']._DesignParameter['_SLVTLayer']['_XYCoordinates'][0][0]) + (self._DesignParameter['PMOS4InSRLatch_0']['_DesignObj']._DesignParameter['_SLVTLayer']['_XWidth'] / 2))), (+ (self._DesignParameter['PMOS4InSRLatch_0']['_XYCoordinates'][0][1] + self._DesignParameter['PMOS4InSRLatch_0']['_DesignObj']._DesignParameter['_SLVTLayer']['_XYCoordinates'][0][1]))]]]
		self._DesignParameter['PIMP_path_2'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['PIMP'][0], _Datatype=DesignParameters._LayerMapping['PIMP'][1], _Width=self._DesignParameter['PMOS1_rInSRLatch_0']['_DesignObj']._DesignParameter['_PPLayer']['_YWidth'])
		self._DesignParameter['PIMP_path_2']['_XYCoordinates'] = [[[(+ ((self._DesignParameter['PMOS1_rInSRLatch_0']['_XYCoordinates'][0][0] + self._DesignParameter['PMOS1_rInSRLatch_0']['_DesignObj']._DesignParameter['_SLVTLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['PMOS1_rInSRLatch_0']['_DesignObj']._DesignParameter['_SLVTLayer']['_XWidth'] / 2))), (+ (self._DesignParameter['PMOS1_rInSRLatch_0']['_XYCoordinates'][0][1] + self._DesignParameter['PMOS1_rInSRLatch_0']['_DesignObj']._DesignParameter['_SLVTLayer']['_XYCoordinates'][0][1]))], [(+ ((self._DesignParameter['PMOS4_rInSRLatch_0']['_XYCoordinates'][0][0] + self._DesignParameter['PMOS4_rInSRLatch_0']['_DesignObj']._DesignParameter['_SLVTLayer']['_XYCoordinates'][0][0]) + (self._DesignParameter['PMOS4_rInSRLatch_0']['_DesignObj']._DesignParameter['_SLVTLayer']['_XWidth'] / 2))), (+ (self._DesignParameter['PMOS4_rInSRLatch_0']['_XYCoordinates'][0][1] + self._DesignParameter['PMOS4_rInSRLatch_0']['_DesignObj']._DesignParameter['_SLVTLayer']['_XYCoordinates'][0][1]))]]]
		supply_cox = int((max(1, (1 + int(((((((self._DesignParameter['NMOS4InSRLatch_0']['_XYCoordinates'][0][0] + self._DesignParameter['NMOS4InSRLatch_0']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][(- 1)][0]) + (self._DesignParameter['NMOS4InSRLatch_0']['_DesignObj']._DesignParameter['_PODummyLayer']['_XWidth'] / 2)) - ((self._DesignParameter['NMOS1InSRLatch_0']['_XYCoordinates'][0][0] + self._DesignParameter['NMOS1InSRLatch_0']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['NMOS1InSRLatch_0']['_DesignObj']._DesignParameter['_PODummyLayer']['_XWidth'] / 2))) - drc._VIAxMinSpace) - (2 * drc._VIAxMinEnclosureByMetx)) / (drc._VIAxMinWidth + drc._VIAxMinSpace))))) * 1.5))
		self._DesignParameter['VSS']['_DesignObj']._CalculatePbodyContactDesignParameter(**dict(_NumberOfPbodyCOX=supply_cox, _NumberOfPbodyCOY=supply_via, _Met1XWidth=None, _Met1YWidth=None))
		self._DesignParameter['VDD_down']['_DesignObj']._CalculateNbodyContactDesignParameter(**dict(_NumberOfNbodyCOX=supply_cox, _NumberOfNbodyCOY=supply_via, _Met1XWidth=None, _Met1YWidth=None))
		self._DesignParameter['VDD_up']['_DesignObj']._CalculateNbodyContactDesignParameter(**dict(_NumberOfNbodyCOX=supply_cox, _NumberOfNbodyCOY=supply_via, _Met1XWidth=None, _Met1YWidth=None))
		self._DesignParameter['NWELL_boundary_0'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['NWELL'][0], _Datatype=DesignParameters._LayerMapping['NWELL'][1], _XWidth=(self._DesignParameter['VDD_down']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth'] + (2 * drc._NwMinEnclosurePactive)), _YWidth=((((self._DesignParameter['PMOS1_rInSRLatch_0']['_XYCoordinates'][0][1] + self._DesignParameter['PMOS1_rInSRLatch_0']['_DesignObj']._DesignParameter['_PPLayer']['_XYCoordinates'][0][1]) + (self._DesignParameter['PMOS1_rInSRLatch_0']['_DesignObj']._DesignParameter['_PPLayer']['_YWidth'] / 2)) - ((self._DesignParameter['VDD_down']['_XYCoordinates'][0][1] + self._DesignParameter['VDD_down']['_DesignObj']._DesignParameter['_ODLayer']['_XYCoordinates'][0][1]) - (self._DesignParameter['VDD_down']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth'] / 2))) + drc._NwMinEnclosurePactive))
		self._DesignParameter['NWELL_boundary_0']['_XYCoordinates'] = [[self._DesignParameter['VDD_down']['_XYCoordinates'][0][0], ((((self._DesignParameter['PMOS1_rInSRLatch_0']['_XYCoordinates'][0][1] + self._DesignParameter['PMOS1_rInSRLatch_0']['_DesignObj']._DesignParameter['_PPLayer']['_XYCoordinates'][0][1]) + (self._DesignParameter['PMOS1_rInSRLatch_0']['_DesignObj']._DesignParameter['_PPLayer']['_YWidth'] / 2)) + (((self._DesignParameter['VDD_down']['_XYCoordinates'][0][1] + self._DesignParameter['VDD_down']['_DesignObj']._DesignParameter['_ODLayer']['_XYCoordinates'][0][1]) - (self._DesignParameter['VDD_down']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth'] / 2)) - drc._NwMinEnclosurePactive)) / 2)]]
		self._DesignParameter['NWELL_boundary_1'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['NWELL'][0], _Datatype=DesignParameters._LayerMapping['NWELL'][1], _XWidth=(self._DesignParameter['VDD_down']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth'] + (2 * drc._NwMinEnclosurePactive)), _YWidth=((((self._DesignParameter['VDD_up']['_XYCoordinates'][0][1] + self._DesignParameter['VDD_up']['_DesignObj']._DesignParameter['_ODLayer']['_XYCoordinates'][0][1]) + (self._DesignParameter['VDD_up']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth'] / 2)) + drc._NwMinEnclosurePactive) - ((self._DesignParameter['PMOS1InSRLatch_0']['_XYCoordinates'][0][1] + self._DesignParameter['PMOS1InSRLatch_0']['_DesignObj']._DesignParameter['_PPLayer']['_XYCoordinates'][0][1]) - (self._DesignParameter['PMOS1InSRLatch_0']['_DesignObj']._DesignParameter['_PPLayer']['_YWidth'] / 2))))
		self._DesignParameter['NWELL_boundary_1']['_XYCoordinates'] = [[self._DesignParameter['VDD_up']['_XYCoordinates'][0][0], (((((self._DesignParameter['VDD_up']['_XYCoordinates'][0][1] + self._DesignParameter['VDD_up']['_DesignObj']._DesignParameter['_ODLayer']['_XYCoordinates'][0][1]) + (self._DesignParameter['VDD_up']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth'] / 2)) + drc._NwMinEnclosurePactive) + ((self._DesignParameter['PMOS1InSRLatch_0']['_XYCoordinates'][0][1] + self._DesignParameter['PMOS1InSRLatch_0']['_DesignObj']._DesignParameter['_PPLayer']['_XYCoordinates'][0][1]) - (self._DesignParameter['PMOS1InSRLatch_0']['_DesignObj']._DesignParameter['_PPLayer']['_YWidth'] / 2))) / 2)]]
		self._DesignParameter['SLVT_path_4'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['SLVT'][0], _Datatype=DesignParameters._LayerMapping['SLVT'][1], _Width=self._DesignParameter['PMOS1_rInSRLatch_0']['_DesignObj']._DesignParameter['_SLVTLayer']['_YWidth'])
		self._DesignParameter['SLVT_path_4']['_XYCoordinates'] = [[[(+ ((self._DesignParameter['PMOS1_rInSRLatch_0']['_XYCoordinates'][0][0] + self._DesignParameter['PMOS1_rInSRLatch_0']['_DesignObj']._DesignParameter['_SLVTLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['PMOS1_rInSRLatch_0']['_DesignObj']._DesignParameter['_SLVTLayer']['_XWidth'] / 2))), (+ (self._DesignParameter['PMOS1_rInSRLatch_0']['_XYCoordinates'][0][1] + self._DesignParameter['PMOS1_rInSRLatch_0']['_DesignObj']._DesignParameter['_SLVTLayer']['_XYCoordinates'][0][1]))], [((self._DesignParameter['PMOS4_rInSRLatch_0']['_XYCoordinates'][0][0] + self._DesignParameter['PMOS4_rInSRLatch_0']['_DesignObj']._DesignParameter['_SLVTLayer']['_XYCoordinates'][0][0]) + (self._DesignParameter['PMOS4_rInSRLatch_0']['_DesignObj']._DesignParameter['_SLVTLayer']['_XWidth'] / 2)), (self._DesignParameter['PMOS1_rInSRLatch_0']['_XYCoordinates'][0][1] + self._DesignParameter['PMOS1_rInSRLatch_0']['_DesignObj']._DesignParameter['_SLVTLayer']['_XYCoordinates'][0][1])]]]
		self._DesignParameter['SLVT_path_5'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['SLVT'][0], _Datatype=DesignParameters._LayerMapping['SLVT'][1], _Width=self._DesignParameter['PMOS1InSRLatch_0']['_DesignObj']._DesignParameter['_SLVTLayer']['_YWidth'])
		self._DesignParameter['SLVT_path_5']['_XYCoordinates'] = [[[(+ ((self._DesignParameter['PMOS1InSRLatch_0']['_XYCoordinates'][0][0] + self._DesignParameter['PMOS1InSRLatch_0']['_DesignObj']._DesignParameter['_SLVTLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['PMOS1InSRLatch_0']['_DesignObj']._DesignParameter['_SLVTLayer']['_XWidth'] / 2))), (+ (self._DesignParameter['PMOS1InSRLatch_0']['_XYCoordinates'][0][1] + self._DesignParameter['PMOS1InSRLatch_0']['_DesignObj']._DesignParameter['_SLVTLayer']['_XYCoordinates'][0][1]))], [((self._DesignParameter['PMOS4InSRLatch_0']['_XYCoordinates'][0][0] + self._DesignParameter['PMOS4InSRLatch_0']['_DesignObj']._DesignParameter['_SLVTLayer']['_XYCoordinates'][0][0]) + (self._DesignParameter['PMOS4InSRLatch_0']['_DesignObj']._DesignParameter['_SLVTLayer']['_XWidth'] / 2)), (self._DesignParameter['PMOS1InSRLatch_0']['_XYCoordinates'][0][1] + self._DesignParameter['PMOS1InSRLatch_0']['_DesignObj']._DesignParameter['_SLVTLayer']['_XYCoordinates'][0][1])]]]
		self._DesignParameter['pu1_gate_vias']['_XYCoordinates'] = [[self._DesignParameter['PCCAM1_pu1']['_XYCoordinates'][0][0], self._DesignParameter['M3V3M4_upupright']['_XYCoordinates'][0][1]]]
		path_list = []
		if (len(self._DesignParameter['pd3_d_via12']['_DesignObj']._DesignParameter['_Met2Layer']['_XYCoordinates']) == 1):
		    mode = 'vertical'
		    _width = self._DesignParameter['pd3_d_via12']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth']
		elif (self._DesignParameter['pd3_d_via12']['_DesignObj']._DesignParameter['_Met2Layer']['_XYCoordinates'][0][0] == self._DesignParameter['pd3_d_via12']['_DesignObj']._DesignParameter['_Met2Layer']['_XYCoordinates'][(- 1)][0]):
		    mode = 'horizontal'
		    _width = self._DesignParameter['pd3_d_via12']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth']
		elif (self._DesignParameter['pd3_d_via12']['_DesignObj']._DesignParameter['_Met2Layer']['_XYCoordinates'][0][1] == self._DesignParameter['pd3_d_via12']['_DesignObj']._DesignParameter['_Met2Layer']['_XYCoordinates'][(- 1)][1]):
		    mode = 'vertical'
		    _width = self._DesignParameter['pd3_d_via12']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth']
		else:
		    print('Invalid Target Input')
		if (mode == 'vertical'):
		    xy_with_offset = []
		    target_y_value = (0 + self._DesignParameter['METAL2_path_21']['_XYCoordinates'][0][0][1])
		    for i in range(len(self._DesignParameter['pd3_d_via12']['_DesignObj']._DesignParameter['_Met2Layer']['_XYCoordinates'])):
		        xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['pd3_d_via12']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['pd3_d_via12']['_XYCoordinates'][0][1])], self._DesignParameter['pd3_d_via12']['_DesignObj']._DesignParameter['_Met2Layer']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		elif (mode == 'horizontal'):
		    xy_with_offset = []
		    target_x_value = (0 + self._DesignParameter['METAL2_path_21']['_XYCoordinates'][0][0][0])
		    for i in range(len(self._DesignParameter['pd3_d_via12']['_DesignObj']._DesignParameter['_Met2Layer']['_XYCoordinates'])):
		        xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['pd3_d_via12']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['pd3_d_via12']['_XYCoordinates'][0][1])], self._DesignParameter['pd3_d_via12']['_DesignObj']._DesignParameter['_Met2Layer']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		self._DesignParameter['met2_routing_bot'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _Width=_width)
		self._DesignParameter['met2_routing_bot']['_XYCoordinates'] = path_list
		path_list = []
		if (len(self._DesignParameter['pd4_drain_via12']['_DesignObj']._DesignParameter['_Met2Layer']['_XYCoordinates']) == 1):
		    mode = 'vertical'
		    _width = self._DesignParameter['pd4_drain_via12']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth']
		elif (self._DesignParameter['pd4_drain_via12']['_DesignObj']._DesignParameter['_Met2Layer']['_XYCoordinates'][0][0] == self._DesignParameter['pd4_drain_via12']['_DesignObj']._DesignParameter['_Met2Layer']['_XYCoordinates'][(- 1)][0]):
		    mode = 'horizontal'
		    _width = self._DesignParameter['pd4_drain_via12']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth']
		elif (self._DesignParameter['pd4_drain_via12']['_DesignObj']._DesignParameter['_Met2Layer']['_XYCoordinates'][0][1] == self._DesignParameter['pd4_drain_via12']['_DesignObj']._DesignParameter['_Met2Layer']['_XYCoordinates'][(- 1)][1]):
		    mode = 'vertical'
		    _width = self._DesignParameter['pd4_drain_via12']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth']
		else:
		    print('Invalid Target Input')
		if (mode == 'vertical'):
		    xy_with_offset = []
		    target_y_value = (0 + self._DesignParameter['METAL2_path_21']['_XYCoordinates'][0][0][1])
		    for i in range(len(self._DesignParameter['pd4_drain_via12']['_DesignObj']._DesignParameter['_Met2Layer']['_XYCoordinates'])):
		        xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['pd4_drain_via12']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['pd4_drain_via12']['_XYCoordinates'][0][1])], self._DesignParameter['pd4_drain_via12']['_DesignObj']._DesignParameter['_Met2Layer']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		elif (mode == 'horizontal'):
		    xy_with_offset = []
		    target_x_value = (0 + self._DesignParameter['METAL2_path_21']['_XYCoordinates'][0][0][0])
		    for i in range(len(self._DesignParameter['pd4_drain_via12']['_DesignObj']._DesignParameter['_Met2Layer']['_XYCoordinates'])):
		        xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['pd4_drain_via12']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['pd4_drain_via12']['_XYCoordinates'][0][1])], self._DesignParameter['pd4_drain_via12']['_DesignObj']._DesignParameter['_Met2Layer']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		self._DesignParameter['met2_array_bot_right'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _Width=_width)
		self._DesignParameter['met2_array_bot_right']['_XYCoordinates'] = path_list
		path_list = []
		if (len(self._DesignParameter['nu3_d_via12']['_DesignObj']._DesignParameter['_Met2Layer']['_XYCoordinates']) == 1):
		    mode = 'vertical'
		    _width = self._DesignParameter['nu3_d_via12']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth']
		elif (self._DesignParameter['nu3_d_via12']['_DesignObj']._DesignParameter['_Met2Layer']['_XYCoordinates'][0][0] == self._DesignParameter['nu3_d_via12']['_DesignObj']._DesignParameter['_Met2Layer']['_XYCoordinates'][(- 1)][0]):
		    mode = 'horizontal'
		    _width = self._DesignParameter['nu3_d_via12']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth']
		elif (self._DesignParameter['nu3_d_via12']['_DesignObj']._DesignParameter['_Met2Layer']['_XYCoordinates'][0][1] == self._DesignParameter['nu3_d_via12']['_DesignObj']._DesignParameter['_Met2Layer']['_XYCoordinates'][(- 1)][1]):
		    mode = 'vertical'
		    _width = self._DesignParameter['nu3_d_via12']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth']
		else:
		    print('Invalid Target Input')
		if (mode == 'vertical'):
		    xy_with_offset = []
		    target_y_value = (0 + self._DesignParameter['METAL2_path_20']['_XYCoordinates'][0][0][1])
		    for i in range(len(self._DesignParameter['nu3_d_via12']['_DesignObj']._DesignParameter['_Met2Layer']['_XYCoordinates'])):
		        xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['nu3_d_via12']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['nu3_d_via12']['_XYCoordinates'][0][1])], self._DesignParameter['nu3_d_via12']['_DesignObj']._DesignParameter['_Met2Layer']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		elif (mode == 'horizontal'):
		    xy_with_offset = []
		    target_x_value = (0 + self._DesignParameter['METAL2_path_20']['_XYCoordinates'][0][0][0])
		    for i in range(len(self._DesignParameter['nu3_d_via12']['_DesignObj']._DesignParameter['_Met2Layer']['_XYCoordinates'])):
		        xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['nu3_d_via12']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['nu3_d_via12']['_XYCoordinates'][0][1])], self._DesignParameter['nu3_d_via12']['_DesignObj']._DesignParameter['_Met2Layer']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		self._DesignParameter['met_array_nmos_top'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _Width=_width)
		self._DesignParameter['met_array_nmos_top']['_XYCoordinates'] = path_list
		path_list = []
		if (len(self._DesignParameter['nu4_d_via12']['_DesignObj']._DesignParameter['_Met2Layer']['_XYCoordinates']) == 1):
		    mode = 'vertical'
		    _width = self._DesignParameter['nu4_d_via12']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth']
		elif (self._DesignParameter['nu4_d_via12']['_DesignObj']._DesignParameter['_Met2Layer']['_XYCoordinates'][0][0] == self._DesignParameter['nu4_d_via12']['_DesignObj']._DesignParameter['_Met2Layer']['_XYCoordinates'][(- 1)][0]):
		    mode = 'horizontal'
		    _width = self._DesignParameter['nu4_d_via12']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth']
		elif (self._DesignParameter['nu4_d_via12']['_DesignObj']._DesignParameter['_Met2Layer']['_XYCoordinates'][0][1] == self._DesignParameter['nu4_d_via12']['_DesignObj']._DesignParameter['_Met2Layer']['_XYCoordinates'][(- 1)][1]):
		    mode = 'vertical'
		    _width = self._DesignParameter['nu4_d_via12']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth']
		else:
		    print('Invalid Target Input')
		if (mode == 'vertical'):
		    xy_with_offset = []
		    target_y_value = (0 + self._DesignParameter['METAL2_path_20']['_XYCoordinates'][0][0][1])
		    for i in range(len(self._DesignParameter['nu4_d_via12']['_DesignObj']._DesignParameter['_Met2Layer']['_XYCoordinates'])):
		        xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['nu4_d_via12']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['nu4_d_via12']['_XYCoordinates'][0][1])], self._DesignParameter['nu4_d_via12']['_DesignObj']._DesignParameter['_Met2Layer']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		elif (mode == 'horizontal'):
		    xy_with_offset = []
		    target_x_value = (0 + self._DesignParameter['METAL2_path_20']['_XYCoordinates'][0][0][0])
		    for i in range(len(self._DesignParameter['nu4_d_via12']['_DesignObj']._DesignParameter['_Met2Layer']['_XYCoordinates'])):
		        xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['nu4_d_via12']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['nu4_d_via12']['_XYCoordinates'][0][1])], self._DesignParameter['nu4_d_via12']['_DesignObj']._DesignParameter['_Met2Layer']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		self._DesignParameter['met2_array_nmos_top_right'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _Width=_width)
		self._DesignParameter['met2_array_nmos_top_right']['_XYCoordinates'] = path_list
		path_list = []
		if (len(self._DesignParameter['nd3_dvia12']['_DesignObj']._DesignParameter['_Met2Layer']['_XYCoordinates']) == 1):
		    mode = 'vertical'
		    _width = self._DesignParameter['nd3_dvia12']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth']
		elif (self._DesignParameter['nd3_dvia12']['_DesignObj']._DesignParameter['_Met2Layer']['_XYCoordinates'][0][0] == self._DesignParameter['nd3_dvia12']['_DesignObj']._DesignParameter['_Met2Layer']['_XYCoordinates'][(- 1)][0]):
		    mode = 'horizontal'
		    _width = self._DesignParameter['nd3_dvia12']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth']
		elif (self._DesignParameter['nd3_dvia12']['_DesignObj']._DesignParameter['_Met2Layer']['_XYCoordinates'][0][1] == self._DesignParameter['nd3_dvia12']['_DesignObj']._DesignParameter['_Met2Layer']['_XYCoordinates'][(- 1)][1]):
		    mode = 'vertical'
		    _width = self._DesignParameter['nd3_dvia12']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth']
		else:
		    print('Invalid Target Input')
		if (mode == 'vertical'):
		    xy_with_offset = []
		    target_y_value = (0 + self._DesignParameter['METAL2_path_19']['_XYCoordinates'][0][0][1])
		    for i in range(len(self._DesignParameter['nd3_dvia12']['_DesignObj']._DesignParameter['_Met2Layer']['_XYCoordinates'])):
		        xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['nd3_dvia12']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['nd3_dvia12']['_XYCoordinates'][0][1])], self._DesignParameter['nd3_dvia12']['_DesignObj']._DesignParameter['_Met2Layer']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		elif (mode == 'horizontal'):
		    xy_with_offset = []
		    target_x_value = (0 + self._DesignParameter['METAL2_path_19']['_XYCoordinates'][0][0][0])
		    for i in range(len(self._DesignParameter['nd3_dvia12']['_DesignObj']._DesignParameter['_Met2Layer']['_XYCoordinates'])):
		        xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['nd3_dvia12']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['nd3_dvia12']['_XYCoordinates'][0][1])], self._DesignParameter['nd3_dvia12']['_DesignObj']._DesignParameter['_Met2Layer']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		self._DesignParameter['met2_array_pmos_bot'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _Width=_width)
		self._DesignParameter['met2_array_pmos_bot']['_XYCoordinates'] = path_list
		path_list = []
		if (len(self._DesignParameter['nd4_drain_via12']['_DesignObj']._DesignParameter['_Met2Layer']['_XYCoordinates']) == 1):
		    mode = 'vertical'
		    _width = self._DesignParameter['nd4_drain_via12']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth']
		elif (self._DesignParameter['nd4_drain_via12']['_DesignObj']._DesignParameter['_Met2Layer']['_XYCoordinates'][0][0] == self._DesignParameter['nd4_drain_via12']['_DesignObj']._DesignParameter['_Met2Layer']['_XYCoordinates'][(- 1)][0]):
		    mode = 'horizontal'
		    _width = self._DesignParameter['nd4_drain_via12']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth']
		elif (self._DesignParameter['nd4_drain_via12']['_DesignObj']._DesignParameter['_Met2Layer']['_XYCoordinates'][0][1] == self._DesignParameter['nd4_drain_via12']['_DesignObj']._DesignParameter['_Met2Layer']['_XYCoordinates'][(- 1)][1]):
		    mode = 'vertical'
		    _width = self._DesignParameter['nd4_drain_via12']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth']
		else:
		    print('Invalid Target Input')
		if (mode == 'vertical'):
		    xy_with_offset = []
		    target_y_value = (0 + self._DesignParameter['METAL2_path_19']['_XYCoordinates'][0][0][1])
		    for i in range(len(self._DesignParameter['nd4_drain_via12']['_DesignObj']._DesignParameter['_Met2Layer']['_XYCoordinates'])):
		        xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['nd4_drain_via12']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['nd4_drain_via12']['_XYCoordinates'][0][1])], self._DesignParameter['nd4_drain_via12']['_DesignObj']._DesignParameter['_Met2Layer']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		elif (mode == 'horizontal'):
		    xy_with_offset = []
		    target_x_value = (0 + self._DesignParameter['METAL2_path_19']['_XYCoordinates'][0][0][0])
		    for i in range(len(self._DesignParameter['nd4_drain_via12']['_DesignObj']._DesignParameter['_Met2Layer']['_XYCoordinates'])):
		        xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['nd4_drain_via12']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['nd4_drain_via12']['_XYCoordinates'][0][1])], self._DesignParameter['nd4_drain_via12']['_DesignObj']._DesignParameter['_Met2Layer']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		self._DesignParameter['pmos_array_bot_right'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _Width=_width)
		self._DesignParameter['pmos_array_bot_right']['_XYCoordinates'] = path_list
		path_list = []
		if (len(self._DesignParameter['pu3_dvia12']['_DesignObj']._DesignParameter['_Met2Layer']['_XYCoordinates']) == 1):
		    mode = 'vertical'
		    _width = self._DesignParameter['pu3_dvia12']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth']
		elif (self._DesignParameter['pu3_dvia12']['_DesignObj']._DesignParameter['_Met2Layer']['_XYCoordinates'][0][0] == self._DesignParameter['pu3_dvia12']['_DesignObj']._DesignParameter['_Met2Layer']['_XYCoordinates'][(- 1)][0]):
		    mode = 'horizontal'
		    _width = self._DesignParameter['pu3_dvia12']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth']
		elif (self._DesignParameter['pu3_dvia12']['_DesignObj']._DesignParameter['_Met2Layer']['_XYCoordinates'][0][1] == self._DesignParameter['pu3_dvia12']['_DesignObj']._DesignParameter['_Met2Layer']['_XYCoordinates'][(- 1)][1]):
		    mode = 'vertical'
		    _width = self._DesignParameter['pu3_dvia12']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth']
		else:
		    print('Invalid Target Input')
		if (mode == 'vertical'):
		    xy_with_offset = []
		    target_y_value = (0 + self._DesignParameter['METAL2_path_22']['_XYCoordinates'][0][0][1])
		    for i in range(len(self._DesignParameter['pu3_dvia12']['_DesignObj']._DesignParameter['_Met2Layer']['_XYCoordinates'])):
		        xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['pu3_dvia12']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['pu3_dvia12']['_XYCoordinates'][0][1])], self._DesignParameter['pu3_dvia12']['_DesignObj']._DesignParameter['_Met2Layer']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		elif (mode == 'horizontal'):
		    xy_with_offset = []
		    target_x_value = (0 + self._DesignParameter['METAL2_path_22']['_XYCoordinates'][0][0][0])
		    for i in range(len(self._DesignParameter['pu3_dvia12']['_DesignObj']._DesignParameter['_Met2Layer']['_XYCoordinates'])):
		        xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['pu3_dvia12']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['pu3_dvia12']['_XYCoordinates'][0][1])], self._DesignParameter['pu3_dvia12']['_DesignObj']._DesignParameter['_Met2Layer']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		self._DesignParameter['pmos_met2_array_top'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _Width=_width)
		self._DesignParameter['pmos_met2_array_top']['_XYCoordinates'] = path_list
		path_list = []
		if (len(self._DesignParameter['pu4_dvia12']['_DesignObj']._DesignParameter['_Met2Layer']['_XYCoordinates']) == 1):
		    mode = 'vertical'
		    _width = self._DesignParameter['pu4_dvia12']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth']
		elif (self._DesignParameter['pu4_dvia12']['_DesignObj']._DesignParameter['_Met2Layer']['_XYCoordinates'][0][0] == self._DesignParameter['pu4_dvia12']['_DesignObj']._DesignParameter['_Met2Layer']['_XYCoordinates'][(- 1)][0]):
		    mode = 'horizontal'
		    _width = self._DesignParameter['pu4_dvia12']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth']
		elif (self._DesignParameter['pu4_dvia12']['_DesignObj']._DesignParameter['_Met2Layer']['_XYCoordinates'][0][1] == self._DesignParameter['pu4_dvia12']['_DesignObj']._DesignParameter['_Met2Layer']['_XYCoordinates'][(- 1)][1]):
		    mode = 'vertical'
		    _width = self._DesignParameter['pu4_dvia12']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth']
		else:
		    print('Invalid Target Input')
		if (mode == 'vertical'):
		    xy_with_offset = []
		    target_y_value = (0 + self._DesignParameter['METAL2_path_22']['_XYCoordinates'][0][0][1])
		    for i in range(len(self._DesignParameter['pu4_dvia12']['_DesignObj']._DesignParameter['_Met2Layer']['_XYCoordinates'])):
		        xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['pu4_dvia12']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['pu4_dvia12']['_XYCoordinates'][0][1])], self._DesignParameter['pu4_dvia12']['_DesignObj']._DesignParameter['_Met2Layer']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		elif (mode == 'horizontal'):
		    xy_with_offset = []
		    target_x_value = (0 + self._DesignParameter['METAL2_path_22']['_XYCoordinates'][0][0][0])
		    for i in range(len(self._DesignParameter['pu4_dvia12']['_DesignObj']._DesignParameter['_Met2Layer']['_XYCoordinates'])):
		        xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['pu4_dvia12']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['pu4_dvia12']['_XYCoordinates'][0][1])], self._DesignParameter['pu4_dvia12']['_DesignObj']._DesignParameter['_Met2Layer']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		self._DesignParameter['pmos_met2_array_top_right'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _Width=_width)
		self._DesignParameter['pmos_met2_array_top_right']['_XYCoordinates'] = path_list
		self._DesignParameter['VDD'] = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1PIN'][0], _Datatype=DesignParameters._LayerMapping['METAL1PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0], _XYCoordinates=[[(+ self._DesignParameter['VDD_up']['_XYCoordinates'][0][0]), (+ self._DesignParameter['VDD_up']['_XYCoordinates'][0][1])], [(+ self._DesignParameter['VDD_down']['_XYCoordinates'][0][0]), (+ self._DesignParameter['VDD_down']['_XYCoordinates'][0][1])]], _Mag=0.05, _Angle=0, _TEXT='VDD')
		self._DesignParameter['VSS_PIN'] = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1PIN'][0], _Datatype=DesignParameters._LayerMapping['METAL1PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0], _XYCoordinates=[[(+ self._DesignParameter['VSS']['_XYCoordinates'][0][0]), (+ self._DesignParameter['VSS']['_XYCoordinates'][0][1])]], _Mag=0.05, _Angle=0, _TEXT='VSS')
		self._DesignParameter['INb'] = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1PIN'][0], _Datatype=DesignParameters._LayerMapping['METAL1PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0], _XYCoordinates=[[self._DesignParameter['PCCAM1_nu2']['_XYCoordinates'][0][0], self._DesignParameter['via1to4_lu']['_XYCoordinates'][0][1]]], _Mag=0.05, _Angle=0, _TEXT='INb')
		self._DesignParameter['IN'] = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1PIN'][0], _Datatype=DesignParameters._LayerMapping['METAL1PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0], _XYCoordinates=[[self._DesignParameter['PCCAM1_pd2']['_XYCoordinates'][0][0], self._DesignParameter['via1to4_rd']['_XYCoordinates'][0][1]]], _Mag=0.05, _Angle=0, _TEXT='IN')
		self._DesignParameter['OUTb'] = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1PIN'][0], _Datatype=DesignParameters._LayerMapping['METAL1PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0], _XYCoordinates=[[(+ (self._DesignParameter['PMOS1InSRLatch_0']['_XYCoordinates'][0][0] + self._DesignParameter['PMOS1InSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][1][0])), (+ (self._DesignParameter['PMOS1InSRLatch_0']['_XYCoordinates'][0][1] + self._DesignParameter['PMOS1InSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][1][1]))]], _Mag=0.05, _Angle=0, _TEXT='OUTb')
		self._DesignParameter['OUT'] = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1PIN'][0], _Datatype=DesignParameters._LayerMapping['METAL1PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0], _XYCoordinates=[[(+ (self._DesignParameter['PMOS1_rInSRLatch_0']['_XYCoordinates'][0][0] + self._DesignParameter['PMOS1_rInSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][1][0])), (+ (self._DesignParameter['PMOS1_rInSRLatch_0']['_XYCoordinates'][0][1] + self._DesignParameter['PMOS1_rInSRLatch_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][1][1]))]], _Mag=0.05, _Angle=0, _TEXT='OUT')
		self._DesignParameter['VDD_stack'] = self._SrefElementDeclaration(_DesignObj=ViaStack._ViaStack(_Name='VDD_stackIn{}'.format(_Name)))[0]
		self._DesignParameter['VDD_stack']['_DesignObj']._CalculateStackMinimumEnclosureY(**dict(COX=max(1, (1 + int((((self._DesignParameter['VDD_up']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] - drc._VIAxMinSpace2) - (2 * drc._VIAxMinEnclosureByMetx)) / (drc._VIAxMinWidth + drc._VIAxMinSpace2))))), COY=2, start_layer=1, end_layer=4))
		self._DesignParameter['VDD_stack']['_XYCoordinates'] = [[(+ self._DesignParameter['VDD_up']['_XYCoordinates'][0][0]), (+ self._DesignParameter['VDD_up']['_XYCoordinates'][0][1])]]
		self._DesignParameter['VDD_stack_bot'] = self._SrefElementDeclaration(_DesignObj=ViaStack._ViaStack(_Name='VDD_stack_botIn{}'.format(_Name)))[0]
		self._DesignParameter['VDD_stack_bot']['_DesignObj']._CalculateStackMinimumEnclosureY(**dict(COX=max(1, (1 + int((((self._DesignParameter['VDD_up']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] - drc._VIAxMinSpace2) - (2 * drc._VIAxMinEnclosureByMetx)) / (drc._VIAxMinWidth + drc._VIAxMinSpace2))))), COY=2, start_layer=1, end_layer=4))
		self._DesignParameter['VDD_stack_bot']['_XYCoordinates'] = [[(+ self._DesignParameter['VDD_down']['_XYCoordinates'][0][0]), (+ self._DesignParameter['VDD_down']['_XYCoordinates'][0][1])]]
		