from generatorLib import StickDiagram
from generatorLib import DesignParameters
import copy
import math
from generatorLib import DRC
from generatorLib.generator_models import ViaPoly2Met1
from generatorLib.generator_models import PSubRing
from generatorLib.generator_models import ViaMet12Met2
from generatorLib.generator_models import NMOSWithDummy
from generatorLib.generator_models import ViaStack
from generatorLib.generator_models import ViaMet22Met3

class _Nset_SALatch(StickDiagram._StickDiagram):
	def __init__(self, _DesignParameter=None, _Name='Nset_SALatch'):
		if _DesignParameter != None:
			self._DesignParameter = _DesignParameter
		else:
			self._DesignParameter = dict(_Name=self._NameDeclaration(_Name=_Name), _GDSFile=self._GDSObjDeclaration(_GDSFile=None))
		self._DesignParameter['_Name']['Name'] = _Name

	def _CalculateDesignParameter(self,nmos1_gate=2,nmos1_width=600,nmos1_length=30,nmos1_gate_spacing=96,nmos1_sdwidth=50,dummy=True,pccrit=True,xvt='SLVT',nmos2_gate=2,nmos2_width=200,nmos2_length=40,nmos2_gate_spacing=96,nmos2_sdwidth=50,nmos3_gate=1,nmos3_width=200,nmos3_length=40,nmos3_gate_spacing=96,nmos3_sdwidth=50,nguardring_co_bot=3,nguardring_co_top=2,nguardring_co_right=6,nguardring_co_left=6):

		drc = DRC.DRC()
		_Name = self._DesignParameter['_Name']['_Name']
		MinSnapSpacing=drc._MinSnapSpacing
		self._DesignParameter['NMOS1'] = self._SrefElementDeclaration(_DesignObj=NMOSWithDummy._NMOS(_Name='NMOS1In{}'.format(_Name)))[0]
		self._DesignParameter['NMOS1']['_DesignObj']._CalculateNMOSDesignParameter(**dict(_NMOSNumberofGate=nmos1_gate, _NMOSChannelWidth=nmos1_width, _NMOSChannellength=nmos1_length, _NMOSDummy=dummy, _GateSpacing=nmos1_gate_spacing, _SDWidth=nmos1_sdwidth, _XVT=xvt, _PCCrit=pccrit))
		self._DesignParameter['NMOS1']['_XYCoordinates'] = [[0.0, 0.0]]
		self._DesignParameter['NMOS2'] = self._SrefElementDeclaration(_DesignObj=NMOSWithDummy._NMOS(_Name='NMOS2In{}'.format(_Name)))[0]
		self._DesignParameter['NMOS2']['_DesignObj']._CalculateNMOSDesignParameter(**dict(_NMOSNumberofGate=nmos2_gate, _NMOSChannelWidth=nmos2_width, _NMOSChannellength=nmos2_length, _NMOSDummy=dummy, _GateSpacing=nmos2_gate_spacing, _SDWidth=nmos2_sdwidth, _XVT=xvt, _PCCrit=pccrit))
		self._DesignParameter['NMOS2']['_XYCoordinates'] = [[((((self._DesignParameter['NMOS1']['_XYCoordinates'][0][0] + self._DesignParameter['NMOS1']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['NMOS1']['_DesignObj']._DesignParameter['_PODummyLayer']['_XWidth'] / 2)) - (self._DesignParameter['NMOS2']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][(- 1)][0] + (self._DesignParameter['NMOS2']['_DesignObj']._DesignParameter['_PODummyLayer']['_XWidth'] / 2))) - drc._PolygateMinSpace), (((self._DesignParameter['NMOS1']['_XYCoordinates'][0][1] + self._DesignParameter['NMOS1']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][1]) + (self._DesignParameter['NMOS1']['_DesignObj']._DesignParameter['_PODummyLayer']['_YWidth'] / 2)) - (self._DesignParameter['NMOS2']['_DesignObj']._DesignParameter['_PODummyLayer']['_YWidth'] / 2))], [((((self._DesignParameter['NMOS1']['_XYCoordinates'][0][0] + self._DesignParameter['NMOS1']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][(- 1)][0]) + (self._DesignParameter['NMOS1']['_DesignObj']._DesignParameter['_PODummyLayer']['_XWidth'] / 2)) - (self._DesignParameter['NMOS2']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][0] - (self._DesignParameter['NMOS2']['_DesignObj']._DesignParameter['_PODummyLayer']['_XWidth'] / 2))) + drc._PolygateMinSpace), (((self._DesignParameter['NMOS1']['_XYCoordinates'][0][1] + self._DesignParameter['NMOS1']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][1]) + (self._DesignParameter['NMOS1']['_DesignObj']._DesignParameter['_PODummyLayer']['_YWidth'] / 2)) - (self._DesignParameter['NMOS2']['_DesignObj']._DesignParameter['_PODummyLayer']['_YWidth'] / 2))]]
		self._DesignParameter['NMOS3'] = self._SrefElementDeclaration(_DesignObj=NMOSWithDummy._NMOS(_Name='NMOS3In{}'.format(_Name)))[0]
		self._DesignParameter['NMOS3']['_DesignObj']._CalculateNMOSDesignParameter(**dict(_NMOSNumberofGate=nmos3_gate, _NMOSChannelWidth=nmos3_width, _NMOSChannellength=nmos3_length, _NMOSDummy=dummy, _GateSpacing=nmos3_gate_spacing, _SDWidth=nmos3_sdwidth, _XVT=xvt, _PCCrit=pccrit))
		self._DesignParameter['NMOS3']['_XYCoordinates'] = [[((((self._DesignParameter['NMOS2']['_XYCoordinates'][0][0] + self._DesignParameter['NMOS2']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['NMOS2']['_DesignObj']._DesignParameter['_PODummyLayer']['_XWidth'] / 2)) - (self._DesignParameter['NMOS3']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][(- 1)][0] + (self._DesignParameter['NMOS3']['_DesignObj']._DesignParameter['_PODummyLayer']['_XWidth'] / 2))) - drc._PolygateMinSpace), (((self._DesignParameter['NMOS2']['_XYCoordinates'][1][1] + self._DesignParameter['NMOS2']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][1]) + (self._DesignParameter['NMOS2']['_DesignObj']._DesignParameter['_PODummyLayer']['_YWidth'] / 2)) - (self._DesignParameter['NMOS3']['_DesignObj']._DesignParameter['_PODummyLayer']['_YWidth'] / 2))], [((((self._DesignParameter['NMOS2']['_XYCoordinates'][1][0] + self._DesignParameter['NMOS2']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][(- 1)][0]) + (self._DesignParameter['NMOS2']['_DesignObj']._DesignParameter['_PODummyLayer']['_XWidth'] / 2)) - (self._DesignParameter['NMOS3']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][0] - (self._DesignParameter['NMOS3']['_DesignObj']._DesignParameter['_PODummyLayer']['_XWidth'] / 2))) + drc._PolygateMinSpace), (((self._DesignParameter['NMOS2']['_XYCoordinates'][1][1] + self._DesignParameter['NMOS2']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][1]) + (self._DesignParameter['NMOS2']['_DesignObj']._DesignParameter['_PODummyLayer']['_YWidth'] / 2)) - (self._DesignParameter['NMOS3']['_DesignObj']._DesignParameter['_PODummyLayer']['_YWidth'] / 2))]]

		if self._DesignParameter['NMOS1']['_DesignObj']._DesignParameter['_PODummyLayer']['_XWidth']*self._DesignParameter['NMOS1']['_DesignObj']._DesignParameter['_PODummyLayer']['_YWidth'] < drc._PODummyMinArea :
			self._DesignParameter['NMOS1']['_DesignObj']._DesignParameter['_PODummyLayer']['_YWidth']=int(drc._PODummyMinArea/self._DesignParameter['NMOS1']['_DesignObj']._DesignParameter['_PODummyLayer']['_XWidth'])+2*MinSnapSpacing

		if self._DesignParameter['NMOS2']['_DesignObj']._DesignParameter['_PODummyLayer']['_XWidth']*self._DesignParameter['NMOS2']['_DesignObj']._DesignParameter['_PODummyLayer']['_YWidth'] < drc._PODummyMinArea :
			self._DesignParameter['NMOS2']['_DesignObj']._DesignParameter['_PODummyLayer']['_YWidth']=int(drc._PODummyMinArea/self._DesignParameter['NMOS2']['_DesignObj']._DesignParameter['_PODummyLayer']['_XWidth'])+2*MinSnapSpacing

		if self._DesignParameter['NMOS3']['_DesignObj']._DesignParameter['_PODummyLayer']['_XWidth']*self._DesignParameter['NMOS3']['_DesignObj']._DesignParameter['_PODummyLayer']['_YWidth'] < drc._PODummyMinArea :
			self._DesignParameter['NMOS3']['_DesignObj']._DesignParameter['_PODummyLayer']['_YWidth']=int(drc._PODummyMinArea/self._DesignParameter['NMOS3']['_DesignObj']._DesignParameter['_PODummyLayer']['_XWidth'])+2*MinSnapSpacing

		cont_nmos3 = max(1, max(1, (1 + int(((((min(self._DesignParameter['NMOS3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_YWidth'], self._DesignParameter['NMOS2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_YWidth']) / 2) - drc._VIAxMinSpace) - (2 * drc._VIAxMinEnclosureByMetx)) / (drc._VIAxMinWidth + drc._VIAxMinSpace))))))
		self._DesignParameter['via_nmos3_m1_m2_drain'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='via_nmos3_m1_m2_drainIn{}'.format(_Name)))[0]
		self._DesignParameter['via_nmos3_m1_m2_drain']['_DesignObj']._CalculateDesignParameterSameEnclosure(**dict(_ViaMet12Met2NumberOfCOX=1, _ViaMet12Met2NumberOfCOY=cont_nmos3))
		self._DesignParameter['via_nmos3_m1_m2_drain']['_XYCoordinates'] = None
		XYList = []
		xy_offset = (0, ((self._DesignParameter['NMOS3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_YWidth'] / 2) - (self._DesignParameter['via_nmos3_m1_m2_drain']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)))
		for i in range(len(self._DesignParameter['NMOS3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		    if ((i % 2) == 1):
		        xy = (self._DesignParameter['NMOS3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i][0] if (type(self._DesignParameter['NMOS3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i][0]) == list) else self._DesignParameter['NMOS3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])
		        XYList.append([((x + y) + z) for (x, y, z) in zip([(0 + self._DesignParameter['NMOS3']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['NMOS3']['_XYCoordinates'][0][1])], xy, xy_offset)])
		self._DesignParameter['via_nmos3_m1_m2_drain']['_XYCoordinates'] = XYList
		self._DesignParameter['via_nmos3_1_m1_m2_drain'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='via_nmos3_1_m1_m2_drainIn{}'.format(_Name)))[0]
		self._DesignParameter['via_nmos3_1_m1_m2_drain']['_DesignObj']._CalculateDesignParameterSameEnclosure(**dict(_ViaMet12Met2NumberOfCOX=1, _ViaMet12Met2NumberOfCOY=cont_nmos3))
		self._DesignParameter['via_nmos3_1_m1_m2_drain']['_XYCoordinates'] = None
		XYList = []
		xy_offset = (0, ((self._DesignParameter['NMOS3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_YWidth'] / 2) - (self._DesignParameter['via_nmos3_1_m1_m2_drain']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)))
		for element in self._DesignParameter['NMOS3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 2)::(- 2)]:
		    element = (element[0] if (type(element[0]) == list) else element)
		    XYList.append([((x + y) + z) for (x, y, z) in zip([(0 + self._DesignParameter['NMOS3']['_XYCoordinates'][1][0]), (0 + self._DesignParameter['NMOS3']['_XYCoordinates'][1][1])], element, xy_offset)])
		self._DesignParameter['via_nmos3_1_m1_m2_drain']['_XYCoordinates'] = XYList
		cont_nmos3_supply = max(1, max(1, (1 + int((((((self._DesignParameter['NMOS3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_YWidth'] - self._DesignParameter['via_nmos3_m1_m2_drain']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']) - drc._Metal1MinSpace2) - drc._VIAxMinSpace) - (2 * drc._VIAxMinEnclosureByMetx)) / (drc._VIAxMinWidth + drc._VIAxMinSpace))))))
		self._DesignParameter['via_nmos3_m1_m2_supply'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='via_nmos3_m1_m2_supplyIn{}'.format(_Name)))[0]
		self._DesignParameter['via_nmos3_m1_m2_supply']['_DesignObj']._CalculateDesignParameterSameEnclosure(**dict(_ViaMet12Met2NumberOfCOX=1, _ViaMet12Met2NumberOfCOY=cont_nmos3_supply))
		self._DesignParameter['via_nmos3_m1_m2_supply']['_XYCoordinates'] = None
		XYList = []
		xy_offset = (0, (((- self._DesignParameter['NMOS3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_YWidth']) / 2) + (self._DesignParameter['via_nmos3_m1_m2_supply']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)))
		for i in range(len(self._DesignParameter['NMOS3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		    if ((i % 2) == 0):
		        xy = (self._DesignParameter['NMOS3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i][0] if (type(self._DesignParameter['NMOS3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i][0]) == list) else self._DesignParameter['NMOS3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])
		        XYList.append([((x + y) + z) for (x, y, z) in zip([(0 + self._DesignParameter['NMOS3']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['NMOS3']['_XYCoordinates'][0][1])], xy, xy_offset)])
		self._DesignParameter['via_nmos3_m1_m2_supply']['_XYCoordinates'] = XYList
		self._DesignParameter['via_nmos3_1_m1_m2_supply'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='via_nmos3_1_m1_m2_supplyIn{}'.format(_Name)))[0]
		self._DesignParameter['via_nmos3_1_m1_m2_supply']['_DesignObj']._CalculateDesignParameterSameEnclosure(**dict(_ViaMet12Met2NumberOfCOX=1, _ViaMet12Met2NumberOfCOY=cont_nmos3_supply))
		self._DesignParameter['via_nmos3_1_m1_m2_supply']['_XYCoordinates'] = None
		XYList = []
		xy_offset = (0, (((- self._DesignParameter['NMOS3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_YWidth']) / 2) + (self._DesignParameter['via_nmos3_1_m1_m2_supply']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)))
		for element in self._DesignParameter['NMOS3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)::(- 2)]:
		    element = (element[0] if (type(element[0]) == list) else element)
		    XYList.append([((x + y) + z) for (x, y, z) in zip([(0 + self._DesignParameter['NMOS3']['_XYCoordinates'][1][0]), (0 + self._DesignParameter['NMOS3']['_XYCoordinates'][1][1])], element, xy_offset)])
		self._DesignParameter['via_nmos3_1_m1_m2_supply']['_XYCoordinates'] = XYList
		self._DesignParameter['nmos3_input'] = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_Name='nmos3_inputIn{}'.format(_Name)))[0]
		self._DesignParameter['nmos3_input']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(**dict(_ViaPoly2Met1NumberOfCOX=max(1, (1 + int(((((((self._DesignParameter['NMOS3']['_XYCoordinates'][1][0] + self._DesignParameter['NMOS3']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]) - (self._DesignParameter['NMOS3']['_XYCoordinates'][1][0] + self._DesignParameter['NMOS3']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0])) + self._DesignParameter['NMOS3']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']) - drc._CoMinSpace) - (2 * drc._CoMinEnclosureByPO)) / (drc._CoMinWidth + drc._CoMinSpace))))), _ViaPoly2Met1NumberOfCOY=1))
		self._DesignParameter['nmos3_input']['_XYCoordinates'] = [[self._DesignParameter['NMOS3']['_XYCoordinates'][0][0], max(((((self._DesignParameter['NMOS3']['_XYCoordinates'][1][1] + self._DesignParameter['NMOS3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1]) + (self._DesignParameter['NMOS3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_YWidth'] / 2)) + (self._DesignParameter['nmos3_input']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)) + drc._Metal1MinSpace2), self._DesignParameter['NMOS3']['_XYCoordinates'][0][1]+self._DesignParameter['NMOS3']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth']/2+self._DesignParameter['nmos3_input']['_DesignObj']._DesignParameter['_POLayer']['_YWidth']/2+31)], [self._DesignParameter['NMOS3']['_XYCoordinates'][1][0], max(((((self._DesignParameter['NMOS3']['_XYCoordinates'][1][1] + self._DesignParameter['NMOS3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1]) + (self._DesignParameter['NMOS3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_YWidth'] / 2)) + (self._DesignParameter['nmos3_input']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)) + drc._Metal1MinSpace2), self._DesignParameter['NMOS3']['_XYCoordinates'][0][1]+self._DesignParameter['NMOS3']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth']/2+self._DesignParameter['nmos3_input']['_DesignObj']._DesignParameter['_POLayer']['_YWidth']/2+31)]]
		if (nmos3_gate == 1):
			_tmpLength_x=(self._DesignParameter['NMOS3']['_XYCoordinates'][0][0]+self._DesignParameter['NMOS3']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][-1][0]-self._DesignParameter['NMOS3']['_DesignObj']._DesignParameter['_PODummyLayer']['_XWidth']/2)-(self._DesignParameter['nmos3_input']['_XYCoordinates'][0][0]+self._DesignParameter['nmos3_input']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']/2)
			_tmpLength_y=(self._DesignParameter['nmos3_input']['_XYCoordinates'][0][1]-self._DesignParameter['nmos3_input']['_DesignObj']._DesignParameter['_POLayer']['_YWidth']/2)-(self._DesignParameter['NMOS3']['_XYCoordinates'][0][1]+self._DesignParameter['NMOS3']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][-1][1]+self._DesignParameter['NMOS3']['_DesignObj']._DesignParameter['_PODummyLayer']['_YWidth']/2)
			if _tmpLength_x*_tmpLength_x+_tmpLength_y*_tmpLength_y < drc._PolygateMinSpaceAtCorner*drc._PolygateMinSpaceAtCorner:
				_tmpY_to_Move=int(math.sqrt(drc._PolygateMinSpaceAtCorner*drc._PolygateMinSpaceAtCorner-_tmpLength_x*_tmpLength_x))+MinSnapSpacing
				self._DesignParameter['nmos3_input']['_XYCoordinates'][0][1] = self._DesignParameter['NMOS3']['_XYCoordinates'][0][1]+self._DesignParameter['NMOS3']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][1]+self._DesignParameter['NMOS3']['_DesignObj']._DesignParameter['_PODummyLayer']['_YWidth']/2+self._DesignParameter['nmos3_input']['_DesignObj']._DesignParameter['_POLayer']['_YWidth']/2+_tmpY_to_Move
				self._DesignParameter['nmos3_input']['_XYCoordinates'][1][1] = self._DesignParameter['NMOS3']['_XYCoordinates'][0][1]+self._DesignParameter['NMOS3']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][1]+self._DesignParameter['NMOS3']['_DesignObj']._DesignParameter['_PODummyLayer']['_YWidth']/2+self._DesignParameter['nmos3_input']['_DesignObj']._DesignParameter['_POLayer']['_YWidth']/2+_tmpY_to_Move
		path_list = []
		xy_offset = [0, 0]
		if (len(self._DesignParameter['NMOS3']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates']) == 1):
		    mode = 'vertical'
		    _width = self._DesignParameter['NMOS3']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
		elif (self._DesignParameter['NMOS3']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0] == self._DesignParameter['NMOS3']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]):
		    mode = 'horizontal'
		    _width = self._DesignParameter['NMOS3']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
		elif (self._DesignParameter['NMOS3']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1] == self._DesignParameter['NMOS3']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][1]):
		    mode = 'vertical'
		    _width = self._DesignParameter['NMOS3']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
		else:
		    print('Invalid Target Input')
		if (mode == 'vertical'):
		    xy_with_offset = []
		    target_y_value = [[(+ (self._DesignParameter['nmos3_input']['_XYCoordinates'][0][0] + self._DesignParameter['nmos3_input']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0])), (+ ((self._DesignParameter['nmos3_input']['_XYCoordinates'][0][1] + self._DesignParameter['nmos3_input']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1]) + (self._DesignParameter['nmos3_input']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2)))]][0][1]
		    for i in range(len(self._DesignParameter['NMOS3']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
		        xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['NMOS3']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['NMOS3']['_XYCoordinates'][0][1])], self._DesignParameter['NMOS3']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		elif (mode == 'horizontal'):
		    xy_with_offset = []
		    target_x_value = [[(+ (self._DesignParameter['nmos3_input']['_XYCoordinates'][0][0] + self._DesignParameter['nmos3_input']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0])), (+ ((self._DesignParameter['nmos3_input']['_XYCoordinates'][0][1] + self._DesignParameter['nmos3_input']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1]) + (self._DesignParameter['nmos3_input']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2)))]][0][0]
		    for i in range(len(self._DesignParameter['NMOS3']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
		        xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['NMOS3']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['NMOS3']['_XYCoordinates'][0][1])], self._DesignParameter['NMOS3']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		for i in range(len(path_list)):
		    path_list[i][0] = [(xy + offset) for (xy, offset) in zip(path_list[i][0], xy_offset)]
		self._DesignParameter['poly_nmos3_l'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _Width=_width)
		self._DesignParameter['poly_nmos3_l']['_XYCoordinates'] = path_list
		path_list = []
		xy_offset = [0, 0]
		if (len(self._DesignParameter['NMOS3']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates']) == 1):
		    mode = 'vertical'
		    _width = self._DesignParameter['NMOS3']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
		elif (self._DesignParameter['NMOS3']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0] == self._DesignParameter['NMOS3']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]):
		    mode = 'horizontal'
		    _width = self._DesignParameter['NMOS3']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
		elif (self._DesignParameter['NMOS3']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1] == self._DesignParameter['NMOS3']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][1]):
		    mode = 'vertical'
		    _width = self._DesignParameter['NMOS3']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
		else:
		    print('Invalid Target Input')
		if (mode == 'vertical'):
		    xy_with_offset = []
		    target_y_value = [[(+ (self._DesignParameter['nmos3_input']['_XYCoordinates'][1][0] + self._DesignParameter['nmos3_input']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0])), (+ ((self._DesignParameter['nmos3_input']['_XYCoordinates'][1][1] + self._DesignParameter['nmos3_input']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1]) + (self._DesignParameter['nmos3_input']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2)))]][0][1]
		    for i in range(len(self._DesignParameter['NMOS3']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
		        xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['NMOS3']['_XYCoordinates'][1][0]), (0 + self._DesignParameter['NMOS3']['_XYCoordinates'][1][1])], self._DesignParameter['NMOS3']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		elif (mode == 'horizontal'):
		    xy_with_offset = []
		    target_x_value = [[(+ (self._DesignParameter['nmos3_input']['_XYCoordinates'][1][0] + self._DesignParameter['nmos3_input']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0])), (+ ((self._DesignParameter['nmos3_input']['_XYCoordinates'][1][1] + self._DesignParameter['nmos3_input']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1]) + (self._DesignParameter['nmos3_input']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2)))]][0][0]
		    for i in range(len(self._DesignParameter['NMOS3']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
		        xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['NMOS3']['_XYCoordinates'][1][0]), (0 + self._DesignParameter['NMOS3']['_XYCoordinates'][1][1])], self._DesignParameter['NMOS3']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		for i in range(len(path_list)):
		    path_list[i][0] = [(xy + offset) for (xy, offset) in zip(path_list[i][0], xy_offset)]
		self._DesignParameter['poly_nmos3_r'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _Width=_width)
		self._DesignParameter['poly_nmos3_r']['_XYCoordinates'] = path_list
		self._DesignParameter['via_nmos3_m2_m3_supply'] = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_Name='via_nmos3_m2_m3_supplyIn{}'.format(_Name)))[0]
		self._DesignParameter['via_nmos3_m2_m3_supply']['_DesignObj']._CalculateDesignParameterSameEnclosure(**dict(_ViaMet22Met3NumberOfCOX=1, _ViaMet22Met3NumberOfCOY=cont_nmos3_supply))
		self._DesignParameter['via_nmos3_m2_m3_supply']['_XYCoordinates'] = None
		XYList = []
		xy_offset = [0, 0]
		for i in range(len(self._DesignParameter['via_nmos3_m1_m2_supply']['_XYCoordinates'])):
		    xy = (self._DesignParameter['via_nmos3_m1_m2_supply']['_XYCoordinates'][i][0] if (type(self._DesignParameter['via_nmos3_m1_m2_supply']['_XYCoordinates'][i][0]) == list) else self._DesignParameter['via_nmos3_m1_m2_supply']['_XYCoordinates'][i])
		    XYList.append([((x + y) + z) for (x, y, z) in zip([0, 0], xy, xy_offset)])
		self._DesignParameter['via_nmos3_m2_m3_supply']['_XYCoordinates'] = XYList
		self._DesignParameter['via_nmos3_1_m2_m3_supply'] = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_Name='via_nmos3_1_m2_m3_supplyIn{}'.format(_Name)))[0]
		self._DesignParameter['via_nmos3_1_m2_m3_supply']['_DesignObj']._CalculateDesignParameterSameEnclosure(**dict(_ViaMet22Met3NumberOfCOX=1, _ViaMet22Met3NumberOfCOY=cont_nmos3_supply))
		self._DesignParameter['via_nmos3_1_m2_m3_supply']['_XYCoordinates'] = None
		XYList = []
		xy_offset = [0, 0]
		for i in range(len(self._DesignParameter['via_nmos3_1_m1_m2_supply']['_XYCoordinates'])):
		    xy = (self._DesignParameter['via_nmos3_1_m1_m2_supply']['_XYCoordinates'][i][0] if (type(self._DesignParameter['via_nmos3_1_m1_m2_supply']['_XYCoordinates'][i][0]) == list) else self._DesignParameter['via_nmos3_1_m1_m2_supply']['_XYCoordinates'][i])
		    XYList.append([((x + y) + z) for (x, y, z) in zip([0, 0], xy, xy_offset)])
		self._DesignParameter['via_nmos3_1_m2_m3_supply']['_XYCoordinates'] = XYList
		self._DesignParameter['m3_nmos3_source'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0], _Datatype=DesignParameters._LayerMapping['METAL3'][1], _Width=min((2 * drc._MetalxMinWidth), self._DesignParameter['via_nmos3_m2_m3_supply']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth']))
		self._DesignParameter['m3_nmos3_source']['_XYCoordinates'] = [[[self._DesignParameter['via_nmos3_m2_m3_supply']['_XYCoordinates'][0][0], (((self._DesignParameter['via_nmos3_m2_m3_supply']['_XYCoordinates'][0][1] + self._DesignParameter['via_nmos3_m2_m3_supply']['_DesignObj']._DesignParameter['_Met3Layer']['_XYCoordinates'][0][1]) + (self._DesignParameter['via_nmos3_m2_m3_supply']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth'] / 2)) - (self._DesignParameter['m3_nmos3_source']['_Width'] / 2))], [(self._DesignParameter['NMOS3']['_XYCoordinates'][0][0] + self._DesignParameter['NMOS3']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][(- 1)][0]), (((self._DesignParameter['via_nmos3_m2_m3_supply']['_XYCoordinates'][0][1] + self._DesignParameter['via_nmos3_m2_m3_supply']['_DesignObj']._DesignParameter['_Met3Layer']['_XYCoordinates'][0][1]) + (self._DesignParameter['via_nmos3_m2_m3_supply']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth'] / 2)) - (self._DesignParameter['m3_nmos3_source']['_Width'] / 2))]], [[self._DesignParameter['via_nmos3_1_m2_m3_supply']['_XYCoordinates'][0][0], (((self._DesignParameter['via_nmos3_1_m2_m3_supply']['_XYCoordinates'][0][1] + self._DesignParameter['via_nmos3_1_m2_m3_supply']['_DesignObj']._DesignParameter['_Met3Layer']['_XYCoordinates'][0][1]) + (self._DesignParameter['via_nmos3_1_m2_m3_supply']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth'] / 2)) - (self._DesignParameter['m3_nmos3_source']['_Width'] / 2))], [(self._DesignParameter['NMOS3']['_XYCoordinates'][1][0] + self._DesignParameter['NMOS3']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][0]), (((self._DesignParameter['via_nmos3_1_m2_m3_supply']['_XYCoordinates'][0][1] + self._DesignParameter['via_nmos3_1_m2_m3_supply']['_DesignObj']._DesignParameter['_Met3Layer']['_XYCoordinates'][0][1]) + (self._DesignParameter['via_nmos3_1_m2_m3_supply']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth'] / 2)) - (self._DesignParameter['m3_nmos3_source']['_Width'] / 2))]]]
		self._DesignParameter['m2_nmos3_source'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _Width=min((2 * drc._MetalxMinWidth), self._DesignParameter['via_nmos3_m2_m3_supply']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth']))
		self._DesignParameter['m2_nmos3_source']['_XYCoordinates'] = [[[self._DesignParameter['via_nmos3_m2_m3_supply']['_XYCoordinates'][0][0], (((self._DesignParameter['via_nmos3_m2_m3_supply']['_XYCoordinates'][0][1] + self._DesignParameter['via_nmos3_m2_m3_supply']['_DesignObj']._DesignParameter['_Met3Layer']['_XYCoordinates'][0][1]) + (self._DesignParameter['via_nmos3_m2_m3_supply']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth'] / 2)) - (self._DesignParameter['m3_nmos3_source']['_Width'] / 2))], [self._DesignParameter['via_nmos3_m2_m3_supply']['_XYCoordinates'][-1][0], (((self._DesignParameter['via_nmos3_m2_m3_supply']['_XYCoordinates'][0][1] + self._DesignParameter['via_nmos3_m2_m3_supply']['_DesignObj']._DesignParameter['_Met3Layer']['_XYCoordinates'][0][1]) + (self._DesignParameter['via_nmos3_m2_m3_supply']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth'] / 2)) - (self._DesignParameter['m3_nmos3_source']['_Width'] / 2))]], [[self._DesignParameter['via_nmos3_1_m2_m3_supply']['_XYCoordinates'][0][0], (((self._DesignParameter['via_nmos3_1_m2_m3_supply']['_XYCoordinates'][0][1] + self._DesignParameter['via_nmos3_1_m2_m3_supply']['_DesignObj']._DesignParameter['_Met3Layer']['_XYCoordinates'][0][1]) + (self._DesignParameter['via_nmos3_1_m2_m3_supply']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth'] / 2)) - (self._DesignParameter['m3_nmos3_source']['_Width'] / 2))], [self._DesignParameter['via_nmos3_1_m2_m3_supply']['_XYCoordinates'][-1][0], (((self._DesignParameter['via_nmos3_1_m2_m3_supply']['_XYCoordinates'][0][1] + self._DesignParameter['via_nmos3_1_m2_m3_supply']['_DesignObj']._DesignParameter['_Met3Layer']['_XYCoordinates'][0][1]) + (self._DesignParameter['via_nmos3_1_m2_m3_supply']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth'] / 2)) - (self._DesignParameter['m3_nmos3_source']['_Width'] / 2))]]]
		self._DesignParameter['poly_nmos3_input'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _Width=self._DesignParameter['nmos3_input']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'])
		self._DesignParameter['poly_nmos3_input']['_XYCoordinates'] = [[[(self._DesignParameter['poly_nmos3_l']['_XYCoordinates'][0][0][0] - (self._DesignParameter['poly_nmos3_l']['_Width'] / 2)), (self._DesignParameter['nmos3_input']['_XYCoordinates'][1][1] + self._DesignParameter['nmos3_input']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1])], [(self._DesignParameter['poly_nmos3_l']['_XYCoordinates'][(- 1)][0][0] + (self._DesignParameter['poly_nmos3_l']['_Width'] / 2)), (self._DesignParameter['nmos3_input']['_XYCoordinates'][1][1] + self._DesignParameter['nmos3_input']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1])]], [[(self._DesignParameter['poly_nmos3_r']['_XYCoordinates'][0][0][0] - (self._DesignParameter['poly_nmos3_r']['_Width'] / 2)), (self._DesignParameter['nmos3_input']['_XYCoordinates'][1][1] + self._DesignParameter['nmos3_input']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1])], [(self._DesignParameter['poly_nmos3_r']['_XYCoordinates'][(- 1)][0][0] + (self._DesignParameter['poly_nmos3_r']['_Width'] / 2)), (self._DesignParameter['nmos3_input']['_XYCoordinates'][1][1] + self._DesignParameter['nmos3_input']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1])]]]
		self._DesignParameter['via_nmos2_m1_m2_drain'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='via_nmos2_m1_m2_drainIn{}'.format(_Name)))[0]
		self._DesignParameter['via_nmos2_m1_m2_drain']['_DesignObj']._CalculateDesignParameterSameEnclosure(**dict(_ViaMet12Met2NumberOfCOX=1, _ViaMet12Met2NumberOfCOY=cont_nmos3))
		self._DesignParameter['via_nmos2_m1_m2_drain']['_XYCoordinates'] = None
		XYList = []
		xy_offset = (0, ((- (self._DesignParameter['NMOS2']['_XYCoordinates'][0][1] + self._DesignParameter['NMOS2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1])) + self._DesignParameter['via_nmos3_m1_m2_drain']['_XYCoordinates'][0][1]))
		for i in range(len(self._DesignParameter['NMOS2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		    if ((i % 2) == 1):
		        xy = (self._DesignParameter['NMOS2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i][0] if (type(self._DesignParameter['NMOS2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i][0]) == list) else self._DesignParameter['NMOS2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])
		        XYList.append([((x + y) + z) for (x, y, z) in zip([(0 + self._DesignParameter['NMOS2']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['NMOS2']['_XYCoordinates'][0][1])], xy, xy_offset)])
		self._DesignParameter['via_nmos2_m1_m2_drain']['_XYCoordinates'] = XYList
		self._DesignParameter['via_nmos2_1_m1_m2_drain'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='via_nmos2_1_m1_m2_drainIn{}'.format(_Name)))[0]
		self._DesignParameter['via_nmos2_1_m1_m2_drain']['_DesignObj']._CalculateDesignParameterSameEnclosure(**dict(_ViaMet12Met2NumberOfCOX=1, _ViaMet12Met2NumberOfCOY=cont_nmos3))
		self._DesignParameter['via_nmos2_1_m1_m2_drain']['_XYCoordinates'] = None
		XYList = []
		xy_offset = (0, ((- (self._DesignParameter['NMOS2']['_XYCoordinates'][1][1] + self._DesignParameter['NMOS2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1])) + self._DesignParameter['via_nmos3_1_m1_m2_drain']['_XYCoordinates'][0][1]))
		for element in self._DesignParameter['NMOS2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 2)::(- 2)]:
		    element = (element[0] if (type(element[0]) == list) else element)
		    XYList.append([((x + y) + z) for (x, y, z) in zip([(0 + self._DesignParameter['NMOS2']['_XYCoordinates'][1][0]), (0 + self._DesignParameter['NMOS2']['_XYCoordinates'][1][1])], element, xy_offset)])
		self._DesignParameter['via_nmos2_1_m1_m2_drain']['_XYCoordinates'] = XYList
		self._DesignParameter['m2_nmos3_drain'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _Width=min(self._DesignParameter['via_nmos3_m1_m2_drain']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'], (4 * drc._MetalxMinWidth)))
		self._DesignParameter['m2_nmos3_drain']['_XYCoordinates'] = [[[self._DesignParameter['via_nmos3_m1_m2_drain']['_XYCoordinates'][0][0], self._DesignParameter['via_nmos3_m1_m2_drain']['_XYCoordinates'][0][1]], [self._DesignParameter['via_nmos2_m1_m2_drain']['_XYCoordinates'][(- 1)][0], self._DesignParameter['via_nmos2_m1_m2_drain']['_XYCoordinates'][(- 1)][1]]], [[self._DesignParameter['via_nmos3_1_m1_m2_drain']['_XYCoordinates'][0][0], self._DesignParameter['via_nmos3_1_m1_m2_drain']['_XYCoordinates'][0][1]], [self._DesignParameter['via_nmos2_1_m1_m2_drain']['_XYCoordinates'][(- 1)][0], self._DesignParameter['via_nmos2_1_m1_m2_drain']['_XYCoordinates'][(- 1)][1]]]]
		cont_nmos2_supply = max(1, max(1, (1 + int((((((self._DesignParameter['NMOS2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_YWidth'] - self._DesignParameter['via_nmos2_m1_m2_drain']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']) - drc._Metal1MinSpace2) - drc._VIAxMinSpace) - (2 * drc._VIAxMinEnclosureByMetx)) / (drc._VIAxMinWidth + drc._VIAxMinSpace))))))
		self._DesignParameter['via_nmos2_m1_m2_supply'] = self._SrefElementDeclaration(_DesignObj=ViaStack._ViaStack(_Name='via_nmos2_m1_m2_supplyIn{}'.format(_Name)))[0]
		self._DesignParameter['via_nmos2_m1_m2_supply']['_DesignObj']._CalculateStackSameEnclosure(**dict(COX=1, COY=cont_nmos2_supply, start_layer=1, end_layer=2))
		self._DesignParameter['via_nmos2_m1_m2_supply']['_XYCoordinates'] = None
		XYList = []
		xy_offset = (0, min((((((- (self._DesignParameter['NMOS2']['_XYCoordinates'][0][1] + self._DesignParameter['NMOS2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1])) + self._DesignParameter['m2_nmos3_drain']['_XYCoordinates'][0][0][1]) - (self._DesignParameter['m2_nmos3_drain']['_Width'] / 2)) - (self._DesignParameter['via_nmos2_m1_m2_supply']['_DesignObj']._DesignParameter['ViaMet12Met2']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] / 2)) - drc._MetalxMinSpace3), (((- self._DesignParameter['NMOS2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_YWidth']) / 2) + (self._DesignParameter['via_nmos2_m1_m2_supply']['_DesignObj']._DesignParameter['ViaMet12Met2']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] / 2))))
		for i in range(len(self._DesignParameter['NMOS2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		    if ((i % 2) == 0):
		        xy = (self._DesignParameter['NMOS2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i][0] if (type(self._DesignParameter['NMOS2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i][0]) == list) else self._DesignParameter['NMOS2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])
		        XYList.append([((x + y) + z) for (x, y, z) in zip([(0 + self._DesignParameter['NMOS2']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['NMOS2']['_XYCoordinates'][0][1])], xy, xy_offset)])
		self._DesignParameter['via_nmos2_m1_m2_supply']['_XYCoordinates'] = XYList
		self._DesignParameter['via_nmos2_1_m1_m2_supply'] = self._SrefElementDeclaration(_DesignObj=ViaStack._ViaStack(_Name='via_nmos2_1_m1_m2_supplyIn{}'.format(_Name)))[0]
		self._DesignParameter['via_nmos2_1_m1_m2_supply']['_DesignObj']._CalculateStackSameEnclosure(**dict(COX=1, COY=cont_nmos2_supply, start_layer=1, end_layer=2))
		self._DesignParameter['via_nmos2_1_m1_m2_supply']['_XYCoordinates'] = None
		XYList = []
		xy_offset = (0, min((((((- (self._DesignParameter['NMOS2']['_XYCoordinates'][1][1] + self._DesignParameter['NMOS2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1])) + self._DesignParameter['m2_nmos3_drain']['_XYCoordinates'][1][0][1]) - (self._DesignParameter['m2_nmos3_drain']['_Width'] / 2)) - (self._DesignParameter['via_nmos2_1_m1_m2_supply']['_DesignObj']._DesignParameter['ViaMet12Met2']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] / 2)) - drc._MetalxMinSpace3), (((- self._DesignParameter['NMOS2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_YWidth']) / 2) + (self._DesignParameter['via_nmos2_1_m1_m2_supply']['_DesignObj']._DesignParameter['ViaMet12Met2']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] / 2))))
		for element in self._DesignParameter['NMOS2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)::(- 2)]:
		    element = (element[0] if (type(element[0]) == list) else element)
		    XYList.append([((x + y) + z) for (x, y, z) in zip([(0 + self._DesignParameter['NMOS2']['_XYCoordinates'][1][0]), (0 + self._DesignParameter['NMOS2']['_XYCoordinates'][1][1])], element, xy_offset)])
		self._DesignParameter['via_nmos2_1_m1_m2_supply']['_XYCoordinates'] = XYList
		cont_nmos1 = max(1, max(1, (1 + int((((self._DesignParameter['NMOS1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_YWidth'] - drc._VIAxMinSpace) - (2 * drc._VIAxMinEnclosureByMetx)) / (drc._VIAxMinWidth + drc._VIAxMinSpace))))))
		if (nmos1_width < nmos2_width):
		    self._DesignParameter['via_nmos1_m1_m2_supply'] = self._SrefElementDeclaration(_DesignObj=ViaStack._ViaStack(_Name='via_nmos1_m1_m2_supplyIn{}'.format(_Name)))[0]
		    self._DesignParameter['via_nmos1_m1_m2_supply']['_DesignObj']._CalculateStackSameEnclosure(**dict(COX=1, COY=cont_nmos1, start_layer=1, end_layer=2))
		    self._DesignParameter['via_nmos1_m1_m2_supply']['_XYCoordinates'] = None
		    XYList = []
		    xy_offset = [0, 0]
		    for i in range(len(self._DesignParameter['NMOS1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		        if ((i % 2) == 1):
		            xy = (self._DesignParameter['NMOS1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i][0] if (type(self._DesignParameter['NMOS1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i][0]) == list) else self._DesignParameter['NMOS1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])
		            XYList.append([((x + y) + z) for (x, y, z) in zip([(0 + self._DesignParameter['NMOS1']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['NMOS1']['_XYCoordinates'][0][1])], xy, xy_offset)])
		    self._DesignParameter['via_nmos1_m1_m2_supply']['_XYCoordinates'] = XYList
		else:
		    self._DesignParameter['via_nmos1_m1_m2_supply'] = self._SrefElementDeclaration(_DesignObj=ViaStack._ViaStack(_Name='via_nmos1_m1_m2_supplyIn{}'.format(_Name)))[0]
		    self._DesignParameter['via_nmos1_m1_m2_supply']['_DesignObj']._CalculateStackSameEnclosure(**dict(COX=1, COY=cont_nmos2_supply, start_layer=1, end_layer=2))
		    self._DesignParameter['via_nmos1_m1_m2_supply']['_XYCoordinates'] = None
		    XYList = []
		    xy_offset = (0, ((- (self._DesignParameter['NMOS1']['_XYCoordinates'][0][1] + self._DesignParameter['NMOS1']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1])) + self._DesignParameter['via_nmos2_m1_m2_supply']['_XYCoordinates'][0][1]))
		    for i in range(len(self._DesignParameter['NMOS1']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'])):
		        if ((i % 2) == 1):
		            xy = (self._DesignParameter['NMOS1']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i][0] if (type(self._DesignParameter['NMOS1']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i][0]) == list) else self._DesignParameter['NMOS1']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i])
		            XYList.append([((x + y) + z) for (x, y, z) in zip([(0 + self._DesignParameter['NMOS1']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['NMOS1']['_XYCoordinates'][0][1])], xy, xy_offset)])
		    self._DesignParameter['via_nmos1_m1_m2_supply']['_XYCoordinates'] = XYList
		self._DesignParameter['m2_nmos2_nmo3'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _Width=min(self._DesignParameter['via_nmos2_m1_m2_supply']['_DesignObj']._DesignParameter['ViaMet12Met2']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'], (4 * drc._MetalxMinWidth)))
		self._DesignParameter['m2_nmos2_nmo3']['_XYCoordinates'] = [[[self._DesignParameter['via_nmos2_m1_m2_supply']['_XYCoordinates'][0][0], self._DesignParameter['via_nmos2_m1_m2_supply']['_XYCoordinates'][0][1]], [self._DesignParameter['via_nmos2_1_m1_m2_supply']['_XYCoordinates'][0][0], self._DesignParameter['via_nmos2_1_m1_m2_supply']['_XYCoordinates'][0][1]]]]
		self._DesignParameter['nmos2_input'] = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_Name='nmos2_inputIn{}'.format(_Name)))[0]
		self._DesignParameter['nmos2_input']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(**dict(_ViaPoly2Met1NumberOfCOX=max(1, (1 + int(((((((self._DesignParameter['NMOS2']['_XYCoordinates'][1][0] + self._DesignParameter['NMOS2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]) - (self._DesignParameter['NMOS2']['_XYCoordinates'][1][0] + self._DesignParameter['NMOS2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0])) + self._DesignParameter['NMOS2']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']) - drc._CoMinSpace) - (2 * drc._CoMinEnclosureByPO)) / (drc._CoMinWidth + drc._CoMinSpace))))), _ViaPoly2Met1NumberOfCOY=1))
		self._DesignParameter['nmos2_input']['_XYCoordinates'] = [[self._DesignParameter['NMOS2']['_XYCoordinates'][0][0], max(((((self._DesignParameter['NMOS2']['_XYCoordinates'][1][1] + self._DesignParameter['NMOS2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1]) + (self._DesignParameter['NMOS2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_YWidth'] / 2)) + (self._DesignParameter['nmos2_input']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)) + drc._Metal1MinSpace2), self._DesignParameter['NMOS2']['_XYCoordinates'][0][1]+self._DesignParameter['NMOS2']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth']/2+self._DesignParameter['nmos2_input']['_DesignObj']._DesignParameter['_POLayer']['_YWidth']/2+31, self._DesignParameter['via_nmos3_m1_m2_drain']['_XYCoordinates'][0][1]+self._DesignParameter['via_nmos3_m1_m2_drain']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']/2+self._DesignParameter['nmos2_input']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']/2+drc._Metal1MinSpace2)], [self._DesignParameter['NMOS2']['_XYCoordinates'][1][0], max(((((self._DesignParameter['NMOS2']['_XYCoordinates'][1][1] + self._DesignParameter['NMOS2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1]) + (self._DesignParameter['NMOS2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_YWidth'] / 2)) + (self._DesignParameter['nmos2_input']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)) + drc._Metal1MinSpace2), self._DesignParameter['NMOS2']['_XYCoordinates'][0][1]+self._DesignParameter['NMOS2']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth']/2+self._DesignParameter['nmos2_input']['_DesignObj']._DesignParameter['_POLayer']['_YWidth']/2+31, self._DesignParameter['via_nmos3_m1_m2_drain']['_XYCoordinates'][0][1]+self._DesignParameter['via_nmos3_m1_m2_drain']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']/2+self._DesignParameter['nmos2_input']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']/2+drc._Metal1MinSpace2)]]
		if (nmos2_gate == 1):
			_tmpLength_x=(self._DesignParameter['NMOS2']['_XYCoordinates'][0][0]+self._DesignParameter['NMOS2']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][-1][0]-self._DesignParameter['NMOS2']['_DesignObj']._DesignParameter['_PODummyLayer']['_XWidth']/2)-(self._DesignParameter['nmos2_input']['_XYCoordinates'][0][0]+self._DesignParameter['nmos2_input']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']/2)
			_tmpLength_y=(self._DesignParameter['nmos2_input']['_XYCoordinates'][0][1]-self._DesignParameter['nmos2_input']['_DesignObj']._DesignParameter['_POLayer']['_YWidth']/2)-(self._DesignParameter['NMOS2']['_XYCoordinates'][0][1]+self._DesignParameter['NMOS2']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][-1][1]+self._DesignParameter['NMOS2']['_DesignObj']._DesignParameter['_PODummyLayer']['_YWidth']/2)
			if _tmpLength_x*_tmpLength_x+_tmpLength_y*_tmpLength_y < drc._PolygateMinSpaceAtCorner*drc._PolygateMinSpaceAtCorner:
				_tmpY_to_Move=int(math.sqrt(drc._PolygateMinSpaceAtCorner*drc._PolygateMinSpaceAtCorner-_tmpLength_x*_tmpLength_x))+MinSnapSpacing
				self._DesignParameter['nmos2_input']['_XYCoordinates'][0][1] = self._DesignParameter['NMOS2']['_XYCoordinates'][0][1]+self._DesignParameter['NMOS2']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][1]+self._DesignParameter['NMOS2']['_DesignObj']._DesignParameter['_PODummyLayer']['_YWidth']/2+self._DesignParameter['nmos2_input']['_DesignObj']._DesignParameter['_POLayer']['_YWidth']/2+_tmpY_to_Move
				self._DesignParameter['nmos2_input']['_XYCoordinates'][1][1] = self._DesignParameter['NMOS2']['_XYCoordinates'][0][1]+self._DesignParameter['NMOS2']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][1]+self._DesignParameter['NMOS2']['_DesignObj']._DesignParameter['_PODummyLayer']['_YWidth']/2+self._DesignParameter['nmos2_input']['_DesignObj']._DesignParameter['_POLayer']['_YWidth']/2+_tmpY_to_Move
		path_list = []
		xy_offset = [0, 0]
		if (len(self._DesignParameter['NMOS2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates']) == 1):
		    mode = 'vertical'
		    _width = self._DesignParameter['NMOS2']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
		elif (self._DesignParameter['NMOS2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0] == self._DesignParameter['NMOS2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]):
		    mode = 'horizontal'
		    _width = self._DesignParameter['NMOS2']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
		elif (self._DesignParameter['NMOS2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1] == self._DesignParameter['NMOS2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][1]):
		    mode = 'vertical'
		    _width = self._DesignParameter['NMOS2']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
		else:
		    print('Invalid Target Input')
		if (mode == 'vertical'):
		    xy_with_offset = []
		    target_y_value = [[(+ self._DesignParameter['nmos2_input']['_XYCoordinates'][0][0]), (+ self._DesignParameter['nmos2_input']['_XYCoordinates'][0][1])]][0][1]
		    for i in range(len(self._DesignParameter['NMOS2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
		        xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['NMOS2']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['NMOS2']['_XYCoordinates'][0][1])], self._DesignParameter['NMOS2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		elif (mode == 'horizontal'):
		    xy_with_offset = []
		    target_x_value = [[(+ self._DesignParameter['nmos2_input']['_XYCoordinates'][0][0]), (+ self._DesignParameter['nmos2_input']['_XYCoordinates'][0][1])]][0][0]
		    for i in range(len(self._DesignParameter['NMOS2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
		        xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['NMOS2']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['NMOS2']['_XYCoordinates'][0][1])], self._DesignParameter['NMOS2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		for i in range(len(path_list)):
		    path_list[i][0] = [(xy + offset) for (xy, offset) in zip(path_list[i][0], xy_offset)]
		self._DesignParameter['poly_nmos2_input'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _Width=_width)
		self._DesignParameter['poly_nmos2_input']['_XYCoordinates'] = path_list
		path_list = []
		xy_offset = [0, 0]
		if (len(self._DesignParameter['NMOS2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates']) == 1):
		    mode = 'vertical'
		    _width = self._DesignParameter['NMOS2']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
		elif (self._DesignParameter['NMOS2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0] == self._DesignParameter['NMOS2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]):
		    mode = 'horizontal'
		    _width = self._DesignParameter['NMOS2']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
		elif (self._DesignParameter['NMOS2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1] == self._DesignParameter['NMOS2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][1]):
		    mode = 'vertical'
		    _width = self._DesignParameter['NMOS2']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
		else:
		    print('Invalid Target Input')
		if (mode == 'vertical'):
		    xy_with_offset = []
		    target_y_value = [[(+ self._DesignParameter['nmos2_input']['_XYCoordinates'][1][0]), (+ self._DesignParameter['nmos2_input']['_XYCoordinates'][1][1])]][0][1]
		    for i in range(len(self._DesignParameter['NMOS2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
		        xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['NMOS2']['_XYCoordinates'][1][0]), (0 + self._DesignParameter['NMOS2']['_XYCoordinates'][1][1])], self._DesignParameter['NMOS2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		elif (mode == 'horizontal'):
		    xy_with_offset = []
		    target_x_value = [[(+ self._DesignParameter['nmos2_input']['_XYCoordinates'][1][0]), (+ self._DesignParameter['nmos2_input']['_XYCoordinates'][1][1])]][0][0]
		    for i in range(len(self._DesignParameter['NMOS2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
		        xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['NMOS2']['_XYCoordinates'][1][0]), (0 + self._DesignParameter['NMOS2']['_XYCoordinates'][1][1])], self._DesignParameter['NMOS2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		for i in range(len(path_list)):
		    path_list[i][0] = [(xy + offset) for (xy, offset) in zip(path_list[i][0], xy_offset)]
		self._DesignParameter['poly_nmos2_1_input'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _Width=_width)
		self._DesignParameter['poly_nmos2_1_input']['_XYCoordinates'] = path_list
		self._DesignParameter['poly_nmos2_input_gate'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _Width=self._DesignParameter['nmos2_input']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'])
		self._DesignParameter['poly_nmos2_input_gate']['_XYCoordinates'] = [[[((self._DesignParameter['NMOS2']['_XYCoordinates'][0][0] + self._DesignParameter['NMOS2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['NMOS2']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)), self._DesignParameter['nmos2_input']['_XYCoordinates'][0][1]], [((self._DesignParameter['NMOS2']['_XYCoordinates'][0][0] + self._DesignParameter['NMOS2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]) + (self._DesignParameter['NMOS2']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)), self._DesignParameter['nmos2_input']['_XYCoordinates'][0][1]]], [[((self._DesignParameter['NMOS2']['_XYCoordinates'][1][0] + self._DesignParameter['NMOS2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['NMOS2']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)), self._DesignParameter['nmos2_input']['_XYCoordinates'][0][1]], [((self._DesignParameter['NMOS2']['_XYCoordinates'][1][0] + self._DesignParameter['NMOS2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]) + (self._DesignParameter['NMOS2']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)), self._DesignParameter['nmos2_input']['_XYCoordinates'][0][1]]]]
		self._DesignParameter['nmos1_input'] = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_Name='nmos1_inputIn{}'.format(_Name)))[0]
		self._DesignParameter['nmos1_input']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(**dict(_ViaPoly2Met1NumberOfCOX=max(1, (1 + int(((((((self._DesignParameter['NMOS1']['_XYCoordinates'][0][0] + self._DesignParameter['NMOS1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]) - (self._DesignParameter['NMOS1']['_XYCoordinates'][0][0] + self._DesignParameter['NMOS1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0])) + self._DesignParameter['NMOS1']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']) - drc._CoMinSpace) - (2 * drc._CoMinEnclosureByPO)) / (drc._CoMinWidth + drc._CoMinSpace))))), _ViaPoly2Met1NumberOfCOY=1))
		self._DesignParameter['nmos1_input']['_XYCoordinates'] = [[self._DesignParameter['NMOS1']['_XYCoordinates'][0][0], max(((((self._DesignParameter['NMOS1']['_XYCoordinates'][0][1] + self._DesignParameter['NMOS1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1]) + (self._DesignParameter['NMOS1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_YWidth'] / 2)) + (self._DesignParameter['nmos1_input']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)) + drc._Metal1MinSpace2), self._DesignParameter['NMOS1']['_XYCoordinates'][0][1]+self._DesignParameter['NMOS1']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth']/2+self._DesignParameter['nmos1_input']['_DesignObj']._DesignParameter['_POLayer']['_YWidth']/2+31)]]
		if nmos1_gate == 1:
			_tmpLength_x=(self._DesignParameter['NMOS1']['_XYCoordinates'][0][0]+self._DesignParameter['NMOS1']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][-1][0]-self._DesignParameter['NMOS1']['_DesignObj']._DesignParameter['_PODummyLayer']['_XWidth']/2)-(self._DesignParameter['nmos1_input']['_XYCoordinates'][0][0]+self._DesignParameter['nmos1_input']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']/2)
			_tmpLength_y=(self._DesignParameter['nmos1_input']['_XYCoordinates'][0][1]-self._DesignParameter['nmos1_input']['_DesignObj']._DesignParameter['_POLayer']['_YWidth']/2)-(self._DesignParameter['NMOS1']['_XYCoordinates'][0][1]+self._DesignParameter['NMOS1']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][-1][1]+self._DesignParameter['NMOS1']['_DesignObj']._DesignParameter['_PODummyLayer']['_YWidth']/2)
			if _tmpLength_x*_tmpLength_x+_tmpLength_y*_tmpLength_y < drc._PolygateMinSpaceAtCorner*drc._PolygateMinSpaceAtCorner:
				_tmpY_to_Move=int(math.sqrt(drc._PolygateMinSpaceAtCorner*drc._PolygateMinSpaceAtCorner-_tmpLength_x*_tmpLength_x))+MinSnapSpacing
				self._DesignParameter['nmos1_input']['_XYCoordinates'][0][1] = self._DesignParameter['NMOS1']['_XYCoordinates'][0][1]+self._DesignParameter['NMOS1']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][1]+self._DesignParameter['NMOS1']['_DesignObj']._DesignParameter['_PODummyLayer']['_YWidth']/2+self._DesignParameter['nmos1_input']['_DesignObj']._DesignParameter['_POLayer']['_YWidth']/2+_tmpY_to_Move
		path_list = []
		xy_offset = [0, 0]
		if (len(self._DesignParameter['NMOS1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates']) == 1):
		    mode = 'vertical'
		    _width = self._DesignParameter['NMOS1']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
		elif (self._DesignParameter['NMOS1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0] == self._DesignParameter['NMOS1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]):
		    mode = 'horizontal'
		    _width = self._DesignParameter['NMOS1']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
		elif (self._DesignParameter['NMOS1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1] == self._DesignParameter['NMOS1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][1]):
		    mode = 'vertical'
		    _width = self._DesignParameter['NMOS1']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
		else:
		    print('Invalid Target Input')
		if (mode == 'vertical'):
		    xy_with_offset = []
		    target_y_value = [[(+ (self._DesignParameter['nmos1_input']['_XYCoordinates'][0][0] + self._DesignParameter['nmos1_input']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0])), (+ ((self._DesignParameter['nmos1_input']['_XYCoordinates'][0][1] + self._DesignParameter['nmos1_input']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1]) + (self._DesignParameter['nmos1_input']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2)))]][0][1]
		    for i in range(len(self._DesignParameter['NMOS1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
		        xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['NMOS1']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['NMOS1']['_XYCoordinates'][0][1])], self._DesignParameter['NMOS1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		elif (mode == 'horizontal'):
		    xy_with_offset = []
		    target_x_value = [[(+ (self._DesignParameter['nmos1_input']['_XYCoordinates'][0][0] + self._DesignParameter['nmos1_input']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0])), (+ ((self._DesignParameter['nmos1_input']['_XYCoordinates'][0][1] + self._DesignParameter['nmos1_input']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1]) + (self._DesignParameter['nmos1_input']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2)))]][0][0]
		    for i in range(len(self._DesignParameter['NMOS1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
		        xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['NMOS1']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['NMOS1']['_XYCoordinates'][0][1])], self._DesignParameter['NMOS1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		for i in range(len(path_list)):
		    path_list[i][0] = [(xy + offset) for (xy, offset) in zip(path_list[i][0], xy_offset)]
		self._DesignParameter['poly_nmos1'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _Width=_width)
		self._DesignParameter['poly_nmos1']['_XYCoordinates'] = path_list
		self._DesignParameter['poly_nmos2_gate'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _Width=self._DesignParameter['nmos1_input']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'])
		self._DesignParameter['poly_nmos2_gate']['_XYCoordinates'] = [[[((self._DesignParameter['NMOS1']['_XYCoordinates'][0][0] + self._DesignParameter['NMOS1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['NMOS1']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)), self._DesignParameter['nmos1_input']['_XYCoordinates'][0][1]], [((self._DesignParameter['NMOS1']['_XYCoordinates'][0][0] + self._DesignParameter['NMOS1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]) + (self._DesignParameter['NMOS1']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)), self._DesignParameter['nmos1_input']['_XYCoordinates'][0][1]]]]

		self._DesignParameter['psubring'] = self._SrefElementDeclaration(_DesignObj=PSubRing.PSubRing(_Name='psubringIn{}'.format(_Name)))[0]
		self._DesignParameter['psubring']['_DesignObj']._CalculateDesignParameter(**dict(height=5000, width=3000, contact_bottom=nguardring_co_bot, contact_top=nguardring_co_top, contact_left=nguardring_co_left, contact_right=nguardring_co_right))
		self._DesignParameter['psubring']['_XYCoordinates'] = [[0.0, (- 179.0)]]
		self._DesignParameter['psubring']['_DesignObj']._CalculateDesignParameter(**dict(height=(((max(((self._DesignParameter['nmos1_input']['_XYCoordinates'][0][1] + self._DesignParameter['nmos1_input']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) + (self._DesignParameter['nmos1_input']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)), ((self._DesignParameter['nmos2_input']['_XYCoordinates'][1][1] + self._DesignParameter['nmos2_input']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) + (self._DesignParameter['nmos2_input']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)), ((self._DesignParameter['nmos3_input']['_XYCoordinates'][1][1] + self._DesignParameter['nmos3_input']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) + (self._DesignParameter['nmos3_input']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2))) + (self._DesignParameter['psubring']['_DesignObj']._DesignParameter['met_top']['_YWidth'] / 2)) + drc._Metal1MinSpace3) - ((min(((self._DesignParameter['NMOS1']['_XYCoordinates'][0][1] + self._DesignParameter['NMOS1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1]) - (self._DesignParameter['NMOS1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_YWidth'] / 2)), ((self._DesignParameter['NMOS2']['_XYCoordinates'][1][1] + self._DesignParameter['NMOS2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1]) - (self._DesignParameter['NMOS2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_YWidth'] / 2)), ((self._DesignParameter['NMOS3']['_XYCoordinates'][1][1] + self._DesignParameter['NMOS3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1]) - (self._DesignParameter['NMOS3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_YWidth'] / 2))) - (self._DesignParameter['psubring']['_DesignObj']._DesignParameter['met_bot']['_YWidth'] / 2)) - drc._Metal1MinSpace3)), width=(((max(((self._DesignParameter['NMOS3']['_XYCoordinates'][1][0] + self._DesignParameter['NMOS3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][0]) + (self._DesignParameter['NMOS3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth'] / 2)), ((self._DesignParameter['via_nmos3_1_m1_m2_supply']['_XYCoordinates'][0][0] + self._DesignParameter['via_nmos3_1_m1_m2_supply']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0]) + (self._DesignParameter['via_nmos3_1_m1_m2_supply']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] / 2))) + (self._DesignParameter['psubring']['_DesignObj']._DesignParameter['met_right']['_XWidth'] / 2)) + drc._Metal1MinSpace3 + drc._Metal1MinSpace) - ((min(((self._DesignParameter['NMOS3']['_XYCoordinates'][0][0] + self._DesignParameter['NMOS3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][0]) - (self._DesignParameter['NMOS3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth'] / 2)), ((self._DesignParameter['via_nmos3_m1_m2_supply']['_XYCoordinates'][0][0] + self._DesignParameter['via_nmos3_m1_m2_supply']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0]) - (self._DesignParameter['via_nmos3_m1_m2_supply']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] / 2))) - (self._DesignParameter['psubring']['_DesignObj']._DesignParameter['met_left']['_XWidth'] / 2)) - drc._Metal1MinSpace3 - drc._Metal1MinSpace)), contact_bottom=nguardring_co_bot, contact_top=nguardring_co_top, contact_left=nguardring_co_left, contact_right=nguardring_co_right))
		self._DesignParameter['psubring']['_XYCoordinates'] = [[self._DesignParameter['NMOS1']['_XYCoordinates'][0][0], ((((((max(((self._DesignParameter['nmos3_input']['_XYCoordinates'][0][1] + self._DesignParameter['nmos3_input']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) + (self._DesignParameter['nmos3_input']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)), ((self._DesignParameter['nmos2_input']['_XYCoordinates'][0][1] + self._DesignParameter['nmos2_input']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) + (self._DesignParameter['nmos2_input']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)), ((self._DesignParameter['nmos1_input']['_XYCoordinates'][0][1] + self._DesignParameter['nmos1_input']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) + (self._DesignParameter['nmos1_input']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2))) + (self._DesignParameter['psubring']['_DesignObj']._DesignParameter['top']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)) + drc._Metal1MinSpace3) + min(((self._DesignParameter['NMOS3']['_XYCoordinates'][0][1] + self._DesignParameter['NMOS3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1]) - (self._DesignParameter['NMOS3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_YWidth'] / 2)), ((self._DesignParameter['NMOS2']['_XYCoordinates'][0][1] + self._DesignParameter['NMOS2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1]) - (self._DesignParameter['NMOS2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_YWidth'] / 2)), ((self._DesignParameter['NMOS1']['_XYCoordinates'][0][1] + self._DesignParameter['NMOS1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1]) - (self._DesignParameter['NMOS1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_YWidth'] / 2)))) - (self._DesignParameter['psubring']['_DesignObj']._DesignParameter['bot']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)) - drc._Metal1MinSpace3) / 2)]]
		path_list = []
		xy_offset = [0, 0]
		if (len(self._DesignParameter['NMOS1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates']) == 1):
		    mode = 'vertical'
		    _width = self._DesignParameter['NMOS1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth']
		elif (self._DesignParameter['NMOS1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][0] == self._DesignParameter['NMOS1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][0]):
		    mode = 'horizontal'
		    _width = self._DesignParameter['NMOS1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth']
		elif (self._DesignParameter['NMOS1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1] == self._DesignParameter['NMOS1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][1]):
		    mode = 'vertical'
		    _width = self._DesignParameter['NMOS1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth']
		else:
		    print('Invalid Target Input')
		if (mode == 'vertical'):
		    xy_with_offset = []
		    target_y_value = [[(+ (self._DesignParameter['psubring']['_XYCoordinates'][0][0] + self._DesignParameter['psubring']['_DesignObj']._DesignParameter['met_bot']['_XYCoordinates'][0][0])), (+ (self._DesignParameter['psubring']['_XYCoordinates'][0][1] + self._DesignParameter['psubring']['_DesignObj']._DesignParameter['met_bot']['_XYCoordinates'][0][1]))]][0][1]
		    for i in range(len(self._DesignParameter['NMOS1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		        if ((i % 2) == 0):
		            xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['NMOS1']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['NMOS1']['_XYCoordinates'][0][1])], self._DesignParameter['NMOS1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		elif (mode == 'horizontal'):
		    xy_with_offset = []
		    target_x_value = [[(+ (self._DesignParameter['psubring']['_XYCoordinates'][0][0] + self._DesignParameter['psubring']['_DesignObj']._DesignParameter['met_bot']['_XYCoordinates'][0][0])), (+ (self._DesignParameter['psubring']['_XYCoordinates'][0][1] + self._DesignParameter['psubring']['_DesignObj']._DesignParameter['met_bot']['_XYCoordinates'][0][1]))]][0][0]
		    for i in range(len(self._DesignParameter['NMOS1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		        if ((i % 2) == 0):
		            xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['NMOS1']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['NMOS1']['_XYCoordinates'][0][1])], self._DesignParameter['NMOS1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		for i in range(len(path_list)):
		    path_list[i][0] = [(xy + offset) for (xy, offset) in zip(path_list[i][0], xy_offset)]
		self._DesignParameter['m1_nmos1_supply'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=self._DesignParameter['NMOS1']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'])
		self._DesignParameter['m1_nmos1_supply']['_XYCoordinates'] = path_list
		self._DesignParameter['slvt_nmos2_nmos3'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['SLVT'][0], _Datatype=DesignParameters._LayerMapping['SLVT'][1], _XWidth=(self._DesignParameter['NMOS2']['_XYCoordinates'][0][0] - self._DesignParameter['NMOS3']['_XYCoordinates'][0][0]), _YWidth=min(self._DesignParameter['NMOS3']['_DesignObj']._DesignParameter['_SLVTLayer']['_YWidth'], self._DesignParameter['NMOS2']['_DesignObj']._DesignParameter['_SLVTLayer']['_YWidth']))
		self._DesignParameter['slvt_nmos2_nmos3']['_XYCoordinates'] = [[(((self._DesignParameter['NMOS3']['_XYCoordinates'][0][0] + self._DesignParameter['NMOS3']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][(- 1)][0]) + (self._DesignParameter['NMOS2']['_XYCoordinates'][0][0] + self._DesignParameter['NMOS2']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][0])) / 2), ((min(((self._DesignParameter['NMOS3']['_XYCoordinates'][1][1] + self._DesignParameter['NMOS3']['_DesignObj']._DesignParameter['_SLVTLayer']['_XYCoordinates'][0][1]) + (self._DesignParameter['NMOS3']['_DesignObj']._DesignParameter['_SLVTLayer']['_YWidth'] / 2)), ((self._DesignParameter['NMOS2']['_XYCoordinates'][1][1] + self._DesignParameter['NMOS2']['_DesignObj']._DesignParameter['_SLVTLayer']['_XYCoordinates'][0][1]) + (self._DesignParameter['NMOS2']['_DesignObj']._DesignParameter['_SLVTLayer']['_YWidth'] / 2))) + max(((self._DesignParameter['NMOS3']['_XYCoordinates'][1][1] + self._DesignParameter['NMOS3']['_DesignObj']._DesignParameter['_SLVTLayer']['_XYCoordinates'][0][1]) - (self._DesignParameter['NMOS3']['_DesignObj']._DesignParameter['_SLVTLayer']['_YWidth'] / 2)), ((self._DesignParameter['NMOS2']['_XYCoordinates'][1][1] + self._DesignParameter['NMOS2']['_DesignObj']._DesignParameter['_SLVTLayer']['_XYCoordinates'][0][1]) - (self._DesignParameter['NMOS2']['_DesignObj']._DesignParameter['_SLVTLayer']['_YWidth'] / 2)))) / 2)], [(((self._DesignParameter['NMOS2']['_XYCoordinates'][1][0] + self._DesignParameter['NMOS2']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][(- 1)][0]) + (self._DesignParameter['NMOS3']['_XYCoordinates'][1][0] + self._DesignParameter['NMOS3']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][0])) / 2), ((min(((self._DesignParameter['NMOS3']['_XYCoordinates'][1][1] + self._DesignParameter['NMOS3']['_DesignObj']._DesignParameter['_SLVTLayer']['_XYCoordinates'][0][1]) + (self._DesignParameter['NMOS3']['_DesignObj']._DesignParameter['_SLVTLayer']['_YWidth'] / 2)), ((self._DesignParameter['NMOS2']['_XYCoordinates'][1][1] + self._DesignParameter['NMOS2']['_DesignObj']._DesignParameter['_SLVTLayer']['_XYCoordinates'][0][1]) + (self._DesignParameter['NMOS2']['_DesignObj']._DesignParameter['_SLVTLayer']['_YWidth'] / 2))) + max(((self._DesignParameter['NMOS3']['_XYCoordinates'][1][1] + self._DesignParameter['NMOS3']['_DesignObj']._DesignParameter['_SLVTLayer']['_XYCoordinates'][0][1]) - (self._DesignParameter['NMOS3']['_DesignObj']._DesignParameter['_SLVTLayer']['_YWidth'] / 2)), ((self._DesignParameter['NMOS2']['_XYCoordinates'][1][1] + self._DesignParameter['NMOS2']['_DesignObj']._DesignParameter['_SLVTLayer']['_XYCoordinates'][0][1]) - (self._DesignParameter['NMOS2']['_DesignObj']._DesignParameter['_SLVTLayer']['_YWidth'] / 2)))) / 2)]]
		self._DesignParameter['slvt_nmos1_nmos2'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['SLVT'][0], _Datatype=DesignParameters._LayerMapping['SLVT'][1], _XWidth=(self._DesignParameter['NMOS1']['_XYCoordinates'][0][0] - self._DesignParameter['NMOS2']['_XYCoordinates'][0][0]), _YWidth=min(self._DesignParameter['NMOS2']['_DesignObj']._DesignParameter['_SLVTLayer']['_YWidth'], self._DesignParameter['NMOS1']['_DesignObj']._DesignParameter['_SLVTLayer']['_YWidth']))
		self._DesignParameter['slvt_nmos1_nmos2']['_XYCoordinates'] = [[((self._DesignParameter['NMOS2']['_XYCoordinates'][0][0] + self._DesignParameter['NMOS1']['_XYCoordinates'][0][0]) / 2), ((min(((self._DesignParameter['NMOS1']['_XYCoordinates'][0][1] + self._DesignParameter['NMOS1']['_DesignObj']._DesignParameter['_SLVTLayer']['_XYCoordinates'][0][1]) + (self._DesignParameter['NMOS1']['_DesignObj']._DesignParameter['_SLVTLayer']['_YWidth'] / 2)), ((self._DesignParameter['NMOS2']['_XYCoordinates'][1][1] + self._DesignParameter['NMOS2']['_DesignObj']._DesignParameter['_SLVTLayer']['_XYCoordinates'][0][1]) + (self._DesignParameter['NMOS2']['_DesignObj']._DesignParameter['_SLVTLayer']['_YWidth'] / 2))) + max(((self._DesignParameter['NMOS2']['_XYCoordinates'][1][1] + self._DesignParameter['NMOS2']['_DesignObj']._DesignParameter['_SLVTLayer']['_XYCoordinates'][0][1]) - (self._DesignParameter['NMOS2']['_DesignObj']._DesignParameter['_SLVTLayer']['_YWidth'] / 2)), ((self._DesignParameter['NMOS1']['_XYCoordinates'][0][1] + self._DesignParameter['NMOS1']['_DesignObj']._DesignParameter['_SLVTLayer']['_XYCoordinates'][0][1]) - (self._DesignParameter['NMOS1']['_DesignObj']._DesignParameter['_SLVTLayer']['_YWidth'] / 2)))) / 2)], [((self._DesignParameter['NMOS2']['_XYCoordinates'][1][0] + self._DesignParameter['NMOS1']['_XYCoordinates'][0][0]) / 2), ((min(((self._DesignParameter['NMOS1']['_XYCoordinates'][0][1] + self._DesignParameter['NMOS1']['_DesignObj']._DesignParameter['_SLVTLayer']['_XYCoordinates'][0][1]) + (self._DesignParameter['NMOS1']['_DesignObj']._DesignParameter['_SLVTLayer']['_YWidth'] / 2)), ((self._DesignParameter['NMOS2']['_XYCoordinates'][1][1] + self._DesignParameter['NMOS2']['_DesignObj']._DesignParameter['_SLVTLayer']['_XYCoordinates'][0][1]) + (self._DesignParameter['NMOS2']['_DesignObj']._DesignParameter['_SLVTLayer']['_YWidth'] / 2))) + max(((self._DesignParameter['NMOS2']['_XYCoordinates'][1][1] + self._DesignParameter['NMOS2']['_DesignObj']._DesignParameter['_SLVTLayer']['_XYCoordinates'][0][1]) - (self._DesignParameter['NMOS2']['_DesignObj']._DesignParameter['_SLVTLayer']['_YWidth'] / 2)), ((self._DesignParameter['NMOS1']['_XYCoordinates'][0][1] + self._DesignParameter['NMOS1']['_DesignObj']._DesignParameter['_SLVTLayer']['_XYCoordinates'][0][1]) - (self._DesignParameter['NMOS1']['_DesignObj']._DesignParameter['_SLVTLayer']['_YWidth'] / 2)))) / 2)]]
		self._DesignParameter['via_nmos3_gate'] = self._SrefElementDeclaration(_DesignObj=ViaStack._ViaStack(_Name='via_nmos3_gateIn{}'.format(_Name)))[0]
		self._DesignParameter['via_nmos3_gate']['_DesignObj']._CalculateStackMinimumEnclosureY(**dict(COX=max(2, max(1, (1 + int((((self._DesignParameter['nmos3_input']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] - drc._VIAxMinSpace) - (2 * drc._VIAxMinEnclosureByMetx)) / (drc._VIAxMinWidth + drc._VIAxMinSpace)))))), COY=1, start_layer=1, end_layer=2))
		self._DesignParameter['via_nmos3_gate']['_XYCoordinates'] = [[self._DesignParameter['nmos3_input']['_XYCoordinates'][0][0], (((self._DesignParameter['nmos3_input']['_XYCoordinates'][0][1] + self._DesignParameter['nmos3_input']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) + (self._DesignParameter['nmos3_input']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)) - (self._DesignParameter['via_nmos3_gate']['_DesignObj']._DesignParameter['ViaMet12Met2']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2))], [self._DesignParameter['nmos3_input']['_XYCoordinates'][1][0], (((self._DesignParameter['nmos3_input']['_XYCoordinates'][1][1] + self._DesignParameter['nmos3_input']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) + (self._DesignParameter['nmos3_input']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)) - (self._DesignParameter['via_nmos3_gate']['_DesignObj']._DesignParameter['ViaMet12Met2']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2))]]
		self._DesignParameter['via23_nmos3'] = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_Name='via23_nmos3In{}'.format(_Name)))[0]
		self._DesignParameter['via23_nmos3']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureX(**dict(_ViaMet22Met3NumberOfCOX=1, _ViaMet22Met3NumberOfCOY=2))
		self._DesignParameter['via23_nmos3']['_XYCoordinates'] = [[self._DesignParameter['via_nmos3_gate']['_XYCoordinates'][0][0], ((self._DesignParameter['via_nmos3_gate']['_XYCoordinates'][0][1] + (self._DesignParameter['via23_nmos3']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] / 2)) - (self._DesignParameter['via_nmos3_gate']['_DesignObj']._DesignParameter['ViaMet12Met2']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] / 2))], [self._DesignParameter['via_nmos3_gate']['_XYCoordinates'][1][0], ((self._DesignParameter['via_nmos3_gate']['_XYCoordinates'][1][1] + (self._DesignParameter['via23_nmos3']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] / 2)) - (self._DesignParameter['via_nmos3_gate']['_DesignObj']._DesignParameter['ViaMet12Met2']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] / 2))]]
		self._DesignParameter['via_nmos2_gate'] = self._SrefElementDeclaration(_DesignObj=ViaStack._ViaStack(_Name='via_nmos2_gateIn{}'.format(_Name)))[0]
		self._DesignParameter['via_nmos2_gate']['_DesignObj']._CalculateStackMinimumEnclosureY(**dict(COX=max(2, max(1, (1 + int((((self._DesignParameter['nmos2_input']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] - drc._VIAxMinSpace) - (2 * drc._VIAxMinEnclosureByMetx)) / (drc._VIAxMinWidth + drc._VIAxMinSpace)))))), COY=1, start_layer=1, end_layer=3))
		self._DesignParameter['via_nmos2_gate']['_XYCoordinates'] = [[self._DesignParameter['nmos2_input']['_XYCoordinates'][0][0], (((self._DesignParameter['nmos2_input']['_XYCoordinates'][0][1] + self._DesignParameter['nmos2_input']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) + (self._DesignParameter['nmos2_input']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)) - (self._DesignParameter['via_nmos2_gate']['_DesignObj']._DesignParameter['ViaMet12Met2']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2))], [self._DesignParameter['nmos2_input']['_XYCoordinates'][1][0], (((self._DesignParameter['nmos2_input']['_XYCoordinates'][1][1] + self._DesignParameter['nmos2_input']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) + (self._DesignParameter['nmos2_input']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)) - (self._DesignParameter['via_nmos2_gate']['_DesignObj']._DesignParameter['ViaMet12Met2']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2))]]
		self._DesignParameter['via_nmos1_gate'] = self._SrefElementDeclaration(_DesignObj=ViaStack._ViaStack(_Name='via_nmos1_gateIn{}'.format(_Name)))[0]
		self._DesignParameter['via_nmos1_gate']['_DesignObj']._CalculateStackMinimumEnclosureY(**dict(COX=max(2, max(1, (1 + int((((self._DesignParameter['nmos1_input']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] - drc._VIAxMinSpace) - (2 * drc._VIAxMinEnclosureByMetx)) / (drc._VIAxMinWidth + drc._VIAxMinSpace)))))), COY=1, start_layer=1, end_layer=3))
		self._DesignParameter['via_nmos1_gate']['_XYCoordinates'] = [[self._DesignParameter['nmos1_input']['_XYCoordinates'][0][0], (((self._DesignParameter['nmos1_input']['_XYCoordinates'][0][1] + self._DesignParameter['nmos1_input']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) + (self._DesignParameter['nmos1_input']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)) - (self._DesignParameter['via_nmos1_gate']['_DesignObj']._DesignParameter['ViaMet12Met2']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2))]]
		path_list = []
		xy_offset = [0, 0]
		if (len(self._DesignParameter['via_nmos1_m1_m2_supply']['_XYCoordinates']) == 1):
		    mode = 'vertical'
		    _width = self._DesignParameter['via_nmos1_m1_m2_supply']['_DesignObj']._DesignParameter['ViaMet12Met2']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth']
		elif (self._DesignParameter['via_nmos1_m1_m2_supply']['_XYCoordinates'][0][0] == self._DesignParameter['via_nmos1_m1_m2_supply']['_XYCoordinates'][(- 1)][0]):
		    mode = 'horizontal'
		    _width = self._DesignParameter['via_nmos1_m1_m2_supply']['_DesignObj']._DesignParameter['ViaMet12Met2']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth']
		elif (self._DesignParameter['via_nmos1_m1_m2_supply']['_XYCoordinates'][0][1] == self._DesignParameter['via_nmos1_m1_m2_supply']['_XYCoordinates'][(- 1)][1]):
		    mode = 'vertical'
		    _width = self._DesignParameter['via_nmos1_m1_m2_supply']['_DesignObj']._DesignParameter['ViaMet12Met2']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth']
		else:
		    print('Invalid Target Input')
		if (mode == 'vertical'):
		    xy_with_offset = []
		    target_y_value = [[(+ self._DesignParameter['m2_nmos2_nmo3']['_XYCoordinates'][0][0][0]), (+ self._DesignParameter['m2_nmos2_nmo3']['_XYCoordinates'][0][0][1])]][0][1]
		    for i in range(len(self._DesignParameter['via_nmos1_m1_m2_supply']['_XYCoordinates'])):
		        xy_with_offset.append([(x + y) for (x, y) in zip([0, 0], self._DesignParameter['via_nmos1_m1_m2_supply']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		elif (mode == 'horizontal'):
		    xy_with_offset = []
		    target_x_value = [[(+ self._DesignParameter['m2_nmos2_nmo3']['_XYCoordinates'][0][0][0]), (+ self._DesignParameter['m2_nmos2_nmo3']['_XYCoordinates'][0][0][1])]][0][0]
		    for i in range(len(self._DesignParameter['via_nmos1_m1_m2_supply']['_XYCoordinates'])):
		        xy_with_offset.append([(x + y) for (x, y) in zip([0, 0], self._DesignParameter['via_nmos1_m1_m2_supply']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		for i in range(len(path_list)) :
		    path_list[i][0] = [(xy + offset) for (xy, offset) in zip(path_list[i][0], xy_offset)]
		self._DesignParameter['m2_nmos1_drain'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _Width=_width)
		self._DesignParameter['m2_nmos1_drain']['_XYCoordinates'] = path_list

		self._DesignParameter['NMOS1']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']=self._DesignParameter['via_nmos1_m1_m2_supply']['_DesignObj']._DesignParameter['ViaMet12Met2']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
		self._DesignParameter['NMOS2']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']=self._DesignParameter['via_nmos2_m1_m2_supply']['_DesignObj']._DesignParameter['ViaMet12Met2']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
		self._DesignParameter['NMOS3']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']=self._DesignParameter['via_nmos2_m1_m2_supply']['_DesignObj']._DesignParameter['ViaMet12Met2']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']

		self._DesignParameter['m1_nmos2_source_y']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=None)
		self._DesignParameter['m1_nmos2_source_y']['_Width']=self.getXWidth('NMOS2','_Met1Layer')
		tmp=[]
		for i in range(0,len(self._DesignParameter['NMOS2']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'])):
			tmp.append([[self._DesignParameter['via_nmos2_m1_m2_supply']['_XYCoordinates'][i][0], self._DesignParameter['NMOS2']['_XYCoordinates'][0][1]], [self._DesignParameter['via_nmos2_m1_m2_supply']['_XYCoordinates'][i][0], self._DesignParameter['via_nmos2_m1_m2_supply']['_XYCoordinates'][0][1]]])
			tmp.append([[self._DesignParameter['via_nmos2_1_m1_m2_supply']['_XYCoordinates'][i][0], self._DesignParameter['NMOS2']['_XYCoordinates'][1][1]], [self._DesignParameter['via_nmos2_1_m1_m2_supply']['_XYCoordinates'][i][0], self._DesignParameter['via_nmos2_1_m1_m2_supply']['_XYCoordinates'][0][1]]])
		self._DesignParameter['m1_nmos2_source_y']['_XYCoordinates']=tmp