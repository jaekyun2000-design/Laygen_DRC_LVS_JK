from generatorLib import StickDiagram
from generatorLib import DesignParameters
import copy
import math
from generatorLib import DRC
from generatorLib.generator_models import ViaMet12Met2
from generatorLib.generator_models import PMOSWithDummy
from generatorLib.generator_models import NSubRing
from generatorLib.generator_models import ViaStack
from generatorLib.generator_models import ViaPoly2Met1

class _pmos_cap_current_mirror(StickDiagram._StickDiagram):
	def __init__(self, _DesignParameter=None, _Name='pmos_cap_current_mirror'):
		if _DesignParameter != None:
			self._DesignParameter = _DesignParameter
		else:
			self._DesignParameter = dict(_Name=self._NameDeclaration(_Name=_Name), _GDSFile=self._GDSObjDeclaration(_GDSFile=None))
		self._DesignParameter['_Name']['Name'] = _Name

	def _CalculateDesignParameter(self,pmos_cap_gate=16,pmos_cap_width=1500,pmos_cap_length=100,pmos_cap_dummy=False,pmos_cap_xvt='LVT',pmos_cap_pccrit=False,pmos_sw1_gate=1,pmos_sw1_width=1000,pmos_sw1_length=30,pmos_sw1_dummy=True,pmos_sw1_xvt='LVT',pmos_sw1_pccrit=True,pmos_sw2_gate=1,pmos_sw2_width=1000,pmos_sw2_length=30,pmos_sw2_dummy=True,pmos_sw2_xvt='LVT',pmos_sw2_pccrit=True,guardring_co_bottom=4,guardring_co_top=3,guardring_co_left=3,guardring_co_right=3,guardring_width=None,guardring_height=None):

		drc = DRC.DRC()
		_Name = self._DesignParameter['_Name']['_Name']

		self._DesignParameter['pmos_cap'] = self._SrefElementDeclaration(_DesignObj=PMOSWithDummy._PMOS(_Name='pmos_capIn{}'.format(_Name)))[0]
		self._DesignParameter['pmos_cap']['_DesignObj']._CalculatePMOSDesignParameter(**dict(_PMOSNumberofGate=pmos_cap_gate, _PMOSChannelWidth=pmos_cap_width, _PMOSChannellength=pmos_cap_length, _PMOSDummy=pmos_cap_dummy, _GateSpacing=None, _SDWidth=None, _XVT=pmos_cap_xvt, _PCCrit=pmos_cap_pccrit))
		self._DesignParameter['pmos_cap']['_XYCoordinates'] = [[0.0, 0.0]]
		self._DesignParameter['pmos_sw1'] = self._SrefElementDeclaration(_DesignObj=PMOSWithDummy._PMOS(_Name='pmos_sw1In{}'.format(_Name)))[0]
		self._DesignParameter['pmos_sw1']['_DesignObj']._CalculatePMOSDesignParameter(**dict(_PMOSNumberofGate=pmos_sw1_gate, _PMOSChannelWidth=pmos_sw1_width, _PMOSChannellength=pmos_sw1_length, _PMOSDummy=pmos_sw1_dummy, _GateSpacing=None, _SDWidth=None, _XVT=pmos_sw1_xvt, _PCCrit=pmos_sw1_pccrit))
		self._DesignParameter['pmos_sw1']['_XYCoordinates'] = [[((((self._DesignParameter['pmos_cap']['_XYCoordinates'][0][0] + self._DesignParameter['pmos_cap']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][(- 1)][0]) - self._DesignParameter['pmos_sw1']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][0]) + (self._DesignParameter['pmos_sw1']['_DesignObj']._DesignParameter['_PODummyLayer']['_XWidth'] / 2)) + drc._PolygateMinSpace), (((self._DesignParameter['pmos_cap']['_XYCoordinates'][0][1] + self._DesignParameter['pmos_cap']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) + (self._DesignParameter['pmos_cap']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)) - (self._DesignParameter['pmos_sw1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2))]]
		self._DesignParameter['pmos_sw2'] = self._SrefElementDeclaration(_DesignObj=PMOSWithDummy._PMOS(_Name='pmos_sw2In{}'.format(_Name)))[0]
		self._DesignParameter['pmos_sw2']['_DesignObj']._CalculatePMOSDesignParameter(**dict(_PMOSNumberofGate=pmos_sw2_gate, _PMOSChannelWidth=pmos_sw2_width, _PMOSChannellength=pmos_sw2_length, _PMOSDummy=pmos_sw2_dummy, _GateSpacing=None, _SDWidth=None, _XVT=pmos_sw2_xvt, _PCCrit=pmos_sw2_pccrit))
		self._DesignParameter['pmos_sw2']['_XYCoordinates'] = [[(((((self._DesignParameter['pmos_sw1']['_XYCoordinates'][0][0] + self._DesignParameter['pmos_sw1']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][(- 1)][0]) - self._DesignParameter['pmos_sw2']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][0]) + (self._DesignParameter['pmos_sw2']['_DesignObj']._DesignParameter['_PODummyLayer']['_XWidth'] / 2)) + (self._DesignParameter['pmos_sw1']['_DesignObj']._DesignParameter['_PODummyLayer']['_XWidth'] / 2)) + drc._PolygateMinSpace), (((self._DesignParameter['pmos_cap']['_XYCoordinates'][0][1] + self._DesignParameter['pmos_cap']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) + (self._DesignParameter['pmos_cap']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)) - (self._DesignParameter['pmos_sw2']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2))]]
		path_list = []
		xy_offset = (0, ((- self._DesignParameter['pmos_cap']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_YWidth']) / 2))
		if (len(self._DesignParameter['pmos_cap']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates']) == 1):
		    mode = 'vertical'
		    _width = self.getXWidth('pmos_sw1','_Met1Layer')#(drc._Metal1MinWidth * 2.2)
		elif (self._DesignParameter['pmos_cap']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][0] == self._DesignParameter['pmos_cap']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][0]):
		    mode = 'horizontal'
		    _width = self.getXWidth('pmos_sw1','_Met1Layer')#(drc._Metal1MinWidth * 2.2)
		elif (self._DesignParameter['pmos_cap']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1] == self._DesignParameter['pmos_cap']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][1]):
		    mode = 'vertical'
		    _width = self.getXWidth('pmos_sw1','_Met1Layer')#(drc._Metal1MinWidth * 2.2)
		else:
		    print('Invalid Target Input')
		if (mode == 'vertical'):
		    xy_with_offset = []
		    target_y_value = [[(+ (self._DesignParameter['pmos_cap']['_XYCoordinates'][0][0] + self._DesignParameter['pmos_cap']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][0])), (+ (self._DesignParameter['pmos_cap']['_XYCoordinates'][0][1] + self._DesignParameter['pmos_cap']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1]))]][0][1]
		    for i in range(len(self._DesignParameter['pmos_cap']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		        xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['pmos_cap']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['pmos_cap']['_XYCoordinates'][0][1])], self._DesignParameter['pmos_cap']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		elif (mode == 'horizontal'):
		    xy_with_offset = []
		    target_x_value = [[(+ (self._DesignParameter['pmos_cap']['_XYCoordinates'][0][0] + self._DesignParameter['pmos_cap']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][0])), (+ (self._DesignParameter['pmos_cap']['_XYCoordinates'][0][1] + self._DesignParameter['pmos_cap']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1]))]][0][0]
		    for i in range(len(self._DesignParameter['pmos_cap']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		        xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['pmos_cap']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['pmos_cap']['_XYCoordinates'][0][1])], self._DesignParameter['pmos_cap']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		for i in range(len(path_list)):
		    path_list[i][0] = [(xy + offset) for (xy, offset) in zip(path_list[i][0], xy_offset)]
		self._DesignParameter['m1_pmos_cap_routing'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=_width)
		self._DesignParameter['m1_pmos_cap_routing']['_XYCoordinates'] = path_list
		path_list = []
		xy_offset = (0, ((- self._DesignParameter['pmos_sw1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_YWidth']) / 2))
		if (len(self._DesignParameter['pmos_sw1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates']) == 1):
		    mode = 'vertical'
		    _width = (drc._Metal1MinWidth * 1.72)
		elif (self._DesignParameter['pmos_sw1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][0] == self._DesignParameter['pmos_sw1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][0]):
		    mode = 'horizontal'
		    _width = (drc._Metal1MinWidth * 1.72)
		elif (self._DesignParameter['pmos_sw1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1] == self._DesignParameter['pmos_sw1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][1]):
		    mode = 'vertical'
		    _width = (drc._Metal1MinWidth * 1.72)
		else:
		    print('Invalid Target Input')
		if (mode == 'vertical'):
		    xy_with_offset = []
		    target_y_value = [[(+ (self._DesignParameter['pmos_sw1']['_XYCoordinates'][0][0] + self._DesignParameter['pmos_sw1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][0])), (+ (self._DesignParameter['pmos_sw1']['_XYCoordinates'][0][1] + self._DesignParameter['pmos_sw1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1]))]][0][1]
		    for i in range(len(self._DesignParameter['pmos_sw1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		        if ((i % 2) == 1):
		            xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['pmos_sw1']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['pmos_sw1']['_XYCoordinates'][0][1])], self._DesignParameter['pmos_sw1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		elif (mode == 'horizontal'):
		    xy_with_offset = []
		    target_x_value = [[(+ (self._DesignParameter['pmos_sw1']['_XYCoordinates'][0][0] + self._DesignParameter['pmos_sw1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][0])), (+ (self._DesignParameter['pmos_sw1']['_XYCoordinates'][0][1] + self._DesignParameter['pmos_sw1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1]))]][0][0]
		    for i in range(len(self._DesignParameter['pmos_sw1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		        if ((i % 2) == 1):
		            xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['pmos_sw1']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['pmos_sw1']['_XYCoordinates'][0][1])], self._DesignParameter['pmos_sw1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		for i in range(len(path_list)):
		    path_list[i][0] = [(xy + offset) for (xy, offset) in zip(path_list[i][0], xy_offset)]
		self._DesignParameter['m1_pmos_sw1_routing'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=_width)
		self._DesignParameter['m1_pmos_sw1_routing']['_XYCoordinates'] = path_list
		path_list = []
		xy_offset = (0, ((- self._DesignParameter['pmos_sw2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_YWidth']) / 2))
		if (len(self._DesignParameter['pmos_sw2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates']) == 1):
		    mode = 'vertical'
		    _width = (drc._Metal1MinWidth * 1.72)
		elif (self._DesignParameter['pmos_sw2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][0] == self._DesignParameter['pmos_sw2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][0]):
		    mode = 'horizontal'
		    _width = (drc._Metal1MinWidth * 1.72)
		elif (self._DesignParameter['pmos_sw2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1] == self._DesignParameter['pmos_sw2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][1]):
		    mode = 'vertical'
		    _width = (drc._Metal1MinWidth * 1.72)
		else:
		    print('Invalid Target Input')
		if (mode == 'vertical'):
		    xy_with_offset = []
		    target_y_value = [[(+ (self._DesignParameter['pmos_sw2']['_XYCoordinates'][0][0] + self._DesignParameter['pmos_sw2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][0])), (+ (self._DesignParameter['pmos_sw2']['_XYCoordinates'][0][1] + self._DesignParameter['pmos_sw2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1]))]][0][1]
		    for i in range(len(self._DesignParameter['pmos_sw2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		        if ((i % 2) == 0):
		            xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['pmos_sw2']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['pmos_sw2']['_XYCoordinates'][0][1])], self._DesignParameter['pmos_sw2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		elif (mode == 'horizontal'):
		    xy_with_offset = []
		    target_x_value = [[(+ (self._DesignParameter['pmos_sw2']['_XYCoordinates'][0][0] + self._DesignParameter['pmos_sw2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][0])), (+ (self._DesignParameter['pmos_sw2']['_XYCoordinates'][0][1] + self._DesignParameter['pmos_sw2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1]))]][0][0]
		    for i in range(len(self._DesignParameter['pmos_sw2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		        if ((i % 2) == 0):
		            xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['pmos_sw2']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['pmos_sw2']['_XYCoordinates'][0][1])], self._DesignParameter['pmos_sw2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		for i in range(len(path_list)):
		    path_list[i][0] = [(xy + offset) for (xy, offset) in zip(path_list[i][0], xy_offset)]
		self._DesignParameter['m1_pmos_sw2_routing'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=_width)
		self._DesignParameter['m1_pmos_sw2_routing']['_XYCoordinates'] = path_list
		self._DesignParameter['guardring'] = self._SrefElementDeclaration(_DesignObj=NSubRing.NSubRing(_Name='guardringIn{}'.format(_Name)))[0]
		self._DesignParameter['guardring']['_DesignObj']._CalculateDesignParameter(**dict(height=5000, width=5000, contact_bottom=guardring_co_bottom, contact_top=guardring_co_top, contact_left=guardring_co_left, contact_right=guardring_co_right))
		self._DesignParameter['guardring']['_XYCoordinates'] = [[263.0, (- 79.0)]]
		self._DesignParameter['via_poly_m1_pmos_cap'] = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_Name='via_poly_m1_pmos_capIn{}'.format(_Name)))[0]
		self._DesignParameter['via_poly_m1_pmos_cap']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(**dict(_ViaPoly2Met1NumberOfCOX=max(2, max(1, (1 + int(((((((self._DesignParameter['pmos_cap']['_XYCoordinates'][0][0] + self._DesignParameter['pmos_cap']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]) - (self._DesignParameter['pmos_cap']['_XYCoordinates'][0][0] + self._DesignParameter['pmos_cap']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0])) + self._DesignParameter['pmos_cap']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']) - drc._CoMinSpace) - (2 * drc._CoMinEnclosureByPO)) / (drc._CoMinWidth + drc._CoMinSpace)))))), _ViaPoly2Met1NumberOfCOY=2))
		self._DesignParameter['via_poly_m1_pmos_cap']['_XYCoordinates'] = [[self._DesignParameter['pmos_cap']['_XYCoordinates'][0][0], ((((self._DesignParameter['pmos_cap']['_XYCoordinates'][0][1] + self._DesignParameter['pmos_cap']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1]) - (self._DesignParameter['pmos_cap']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_YWidth'] / 2)) - (self._DesignParameter['via_poly_m1_pmos_cap']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)) - drc._Metal1MinSpace21)]]
		self._DesignParameter['via_poly_m1_sw1'] = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_Name='via_poly_m1_sw1In{}'.format(_Name)))[0]
		self._DesignParameter['via_poly_m1_sw1']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(**dict(_ViaPoly2Met1NumberOfCOX=max(1, max(1, (1 + int(((((((self._DesignParameter['pmos_sw1']['_XYCoordinates'][0][0] + self._DesignParameter['pmos_sw1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]) - (self._DesignParameter['pmos_sw1']['_XYCoordinates'][0][0] + self._DesignParameter['pmos_sw1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0])) + self._DesignParameter['pmos_sw1']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']) - drc._CoMinSpace) - (2 * drc._CoMinEnclosureByPO)) / (drc._CoMinWidth + drc._CoMinSpace)))))), _ViaPoly2Met1NumberOfCOY=1))
		self._DesignParameter['via_poly_m1_sw1']['_XYCoordinates'] = [[self._DesignParameter['pmos_sw1']['_XYCoordinates'][0][0], ((((self._DesignParameter['pmos_sw1']['_XYCoordinates'][0][1] + self._DesignParameter['pmos_sw1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1]) - (self._DesignParameter['pmos_sw1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_YWidth'] / 2)) - (self._DesignParameter['via_poly_m1_sw1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)) - drc._Metal1MinSpace2)]]
		# if pmos_sw1_gate == 1 :
		# 	self._DesignParameter['via_poly_m1_sw1']['_XYCoordinates']=[[self._DesignParameter['via_poly_m1_sw1']['_XYCoordinates'][0][0],self._DesignParameter['via_poly_m1_sw1']['_XYCoordinates'][0][1]-]]
		self._DesignParameter['via_poly_m1_sw2'] = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_Name='via_poly_m1_sw2In{}'.format(_Name)))[0]
		self._DesignParameter['via_poly_m1_sw2']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(**dict(_ViaPoly2Met1NumberOfCOX=max(1, max(1, (1 + int(((((((self._DesignParameter['pmos_sw2']['_XYCoordinates'][0][0] + self._DesignParameter['pmos_sw2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]) - (self._DesignParameter['pmos_sw2']['_XYCoordinates'][0][0] + self._DesignParameter['pmos_sw2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0])) + self._DesignParameter['pmos_sw2']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']) - drc._CoMinSpace) - (2 * drc._CoMinEnclosureByPO)) / (drc._CoMinWidth + drc._CoMinSpace)))))), _ViaPoly2Met1NumberOfCOY=1))

		self._DesignParameter['via_poly_m1_sw2']['_XYCoordinates'] = [[self._DesignParameter['pmos_sw2']['_XYCoordinates'][0][0], ((((self._DesignParameter['pmos_sw2']['_XYCoordinates'][0][1] + self._DesignParameter['pmos_sw2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1]) - (self._DesignParameter['pmos_sw2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_YWidth'] / 2)) - (self._DesignParameter['via_poly_m1_sw2']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)) - drc._Metal1MinSpace2)]]
		self._DesignParameter['poly_gate_pmos_cap'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _Width=self._DesignParameter['via_poly_m1_pmos_cap']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'])
		self._DesignParameter['poly_gate_pmos_cap']['_XYCoordinates'] = [[[((self._DesignParameter['pmos_cap']['_XYCoordinates'][0][0] + self._DesignParameter['pmos_cap']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['pmos_cap']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)), self._DesignParameter['via_poly_m1_pmos_cap']['_XYCoordinates'][0][1]], [((self._DesignParameter['pmos_cap']['_XYCoordinates'][0][0] + self._DesignParameter['pmos_cap']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]) + (self._DesignParameter['pmos_cap']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)), self._DesignParameter['via_poly_m1_pmos_cap']['_XYCoordinates'][0][1]]]]
		self._DesignParameter['poly_gate_sw1'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _Width=self._DesignParameter['via_poly_m1_sw1']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'])
		self._DesignParameter['poly_gate_sw1']['_XYCoordinates'] = [[[((self._DesignParameter['pmos_sw1']['_XYCoordinates'][0][0] + self._DesignParameter['pmos_sw1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['pmos_sw1']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)), self._DesignParameter['via_poly_m1_sw1']['_XYCoordinates'][0][1]], [((self._DesignParameter['pmos_sw1']['_XYCoordinates'][0][0] + self._DesignParameter['pmos_sw1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]) + (self._DesignParameter['pmos_sw1']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)), self._DesignParameter['via_poly_m1_sw1']['_XYCoordinates'][0][1]]]]
		self._DesignParameter['poly_gate_sw2'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _Width=self._DesignParameter['via_poly_m1_sw2']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'])
		self._DesignParameter['poly_gate_sw2']['_XYCoordinates'] = [[[((self._DesignParameter['pmos_sw2']['_XYCoordinates'][0][0] + self._DesignParameter['pmos_sw2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['pmos_sw2']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)), self._DesignParameter['via_poly_m1_sw2']['_XYCoordinates'][0][1]], [((self._DesignParameter['pmos_sw2']['_XYCoordinates'][0][0] + self._DesignParameter['pmos_sw2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]) + (self._DesignParameter['pmos_sw2']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)), self._DesignParameter['via_poly_m1_sw2']['_XYCoordinates'][0][1]]]]
		path_list = []
		xy_offset = [0, 0]
		if (len(self._DesignParameter['pmos_cap']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates']) == 1):
		    mode = 'vertical'
		    _width = self._DesignParameter['pmos_cap']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
		elif (self._DesignParameter['pmos_cap']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0] == self._DesignParameter['pmos_cap']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]):
		    mode = 'horizontal'
		    _width = self._DesignParameter['pmos_cap']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
		elif (self._DesignParameter['pmos_cap']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1] == self._DesignParameter['pmos_cap']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][1]):
		    mode = 'vertical'
		    _width = self._DesignParameter['pmos_cap']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
		else:
		    print('Invalid Target Input')
		if (mode == 'vertical'):
		    xy_with_offset = []
		    target_y_value = [[(+ self._DesignParameter['via_poly_m1_pmos_cap']['_XYCoordinates'][0][0]), (+ self._DesignParameter['via_poly_m1_pmos_cap']['_XYCoordinates'][0][1])]][0][1]
		    for i in range(len(self._DesignParameter['pmos_cap']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
		        xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['pmos_cap']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['pmos_cap']['_XYCoordinates'][0][1])], self._DesignParameter['pmos_cap']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		elif (mode == 'horizontal'):
		    xy_with_offset = []
		    target_x_value = [[(+ self._DesignParameter['via_poly_m1_pmos_cap']['_XYCoordinates'][0][0]), (+ self._DesignParameter['via_poly_m1_pmos_cap']['_XYCoordinates'][0][1])]][0][0]
		    for i in range(len(self._DesignParameter['pmos_cap']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
		        xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['pmos_cap']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['pmos_cap']['_XYCoordinates'][0][1])], self._DesignParameter['pmos_cap']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		for i in range(len(path_list)):
		    path_list[i][0] = [(xy + offset) for (xy, offset) in zip(path_list[i][0], xy_offset)]
		self._DesignParameter['poly_pmos_cap'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _Width=_width)
		self._DesignParameter['poly_pmos_cap']['_XYCoordinates'] = path_list
		path_list = []
		xy_offset = [0, 0]
		if (len(self._DesignParameter['pmos_sw1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates']) == 1):
		    mode = 'vertical'
		    _width = self._DesignParameter['pmos_sw1']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
		elif (self._DesignParameter['pmos_sw1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0] == self._DesignParameter['pmos_sw1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]):
		    mode = 'horizontal'
		    _width = self._DesignParameter['pmos_sw1']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
		elif (self._DesignParameter['pmos_sw1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1] == self._DesignParameter['pmos_sw1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][1]):
		    mode = 'vertical'
		    _width = self._DesignParameter['pmos_sw1']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
		else:
		    print('Invalid Target Input')
		if (mode == 'vertical'):
		    xy_with_offset = []
		    target_y_value = [[(+ self._DesignParameter['via_poly_m1_sw1']['_XYCoordinates'][0][0]), (+ self._DesignParameter['via_poly_m1_sw1']['_XYCoordinates'][0][1])]][0][1]
		    for i in range(len(self._DesignParameter['pmos_sw1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
		        xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['pmos_sw1']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['pmos_sw1']['_XYCoordinates'][0][1])], self._DesignParameter['pmos_sw1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		elif (mode == 'horizontal'):
		    xy_with_offset = []
		    target_x_value = [[(+ self._DesignParameter['via_poly_m1_sw1']['_XYCoordinates'][0][0]), (+ self._DesignParameter['via_poly_m1_sw1']['_XYCoordinates'][0][1])]][0][0]
		    for i in range(len(self._DesignParameter['pmos_sw1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
		        xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['pmos_sw1']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['pmos_sw1']['_XYCoordinates'][0][1])], self._DesignParameter['pmos_sw1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		for i in range(len(path_list)):
		    path_list[i][0] = [(xy + offset) for (xy, offset) in zip(path_list[i][0], xy_offset)]
		self._DesignParameter['poly_sw1'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _Width=_width)
		self._DesignParameter['poly_sw1']['_XYCoordinates'] = path_list
		path_list = []
		xy_offset = [0, 0]
		if (len(self._DesignParameter['pmos_sw2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates']) == 1):
		    mode = 'vertical'
		    _width = self._DesignParameter['pmos_sw2']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
		elif (self._DesignParameter['pmos_sw2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0] == self._DesignParameter['pmos_sw2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]):
		    mode = 'horizontal'
		    _width = self._DesignParameter['pmos_sw2']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
		elif (self._DesignParameter['pmos_sw2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1] == self._DesignParameter['pmos_sw2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][1]):
		    mode = 'vertical'
		    _width = self._DesignParameter['pmos_sw2']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
		else:
		    print('Invalid Target Input')
		if (mode == 'vertical'):
		    xy_with_offset = []
		    target_y_value = [[(+ self._DesignParameter['via_poly_m1_sw2']['_XYCoordinates'][0][0]), (+ self._DesignParameter['via_poly_m1_sw2']['_XYCoordinates'][0][1])]][0][1]
		    for i in range(len(self._DesignParameter['pmos_sw2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
		        xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['pmos_sw2']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['pmos_sw2']['_XYCoordinates'][0][1])], self._DesignParameter['pmos_sw2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		elif (mode == 'horizontal'):
		    xy_with_offset = []
		    target_x_value = [[(+ self._DesignParameter['via_poly_m1_sw2']['_XYCoordinates'][0][0]), (+ self._DesignParameter['via_poly_m1_sw2']['_XYCoordinates'][0][1])]][0][0]
		    for i in range(len(self._DesignParameter['pmos_sw2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
		        xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['pmos_sw2']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['pmos_sw2']['_XYCoordinates'][0][1])], self._DesignParameter['pmos_sw2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		for i in range(len(path_list)):
		    path_list[i][0] = [(xy + offset) for (xy, offset) in zip(path_list[i][0], xy_offset)]
		self._DesignParameter['poly_sw2'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _Width=_width)
		self._DesignParameter['poly_sw2']['_XYCoordinates'] = path_list
		self._DesignParameter['via_m1_m3_pmos_cap'] = self._SrefElementDeclaration(_DesignObj=ViaStack._ViaStack(_Name='via_m1_m3_pmos_capIn{}'.format(_Name)))[0]
		self._DesignParameter['via_m1_m3_pmos_cap']['_DesignObj']._CalculateStackMinimumEnclosureY(**dict(COX=max(2, max(1, (1 + int((((self._DesignParameter['via_poly_m1_pmos_cap']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] - drc._VIAxMinSpace) - (2 * drc._VIAxMinEnclosureByMetx)) / (drc._VIAxMinWidth + drc._VIAxMinSpace)))))), COY=2, start_layer=1, end_layer=3))
		self._DesignParameter['via_m1_m3_pmos_cap']['_XYCoordinates'] = [[self._DesignParameter['via_poly_m1_pmos_cap']['_XYCoordinates'][0][0], ((self._DesignParameter['via_poly_m1_pmos_cap']['_XYCoordinates'][0][1] + (self._DesignParameter['via_poly_m1_pmos_cap']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)) - (self._DesignParameter['via_m1_m3_pmos_cap']['_DesignObj']._DesignParameter['ViaMet12Met2']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2))]]
		self._DesignParameter['via_m1_m4_sw1'] = self._SrefElementDeclaration(_DesignObj=ViaStack._ViaStack(_Name='via_m1_m4_sw1In{}'.format(_Name)))[0]
		self._DesignParameter['via_m1_m4_sw1']['_DesignObj']._CalculateStackMinimumEnclosureY(**dict(COX=max(2, max(1, (1 + int((((self._DesignParameter['via_poly_m1_sw1']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] - drc._VIAxMinSpace) - (2 * drc._VIAxMinEnclosureByMetx)) / (drc._VIAxMinWidth + drc._VIAxMinSpace)))))), COY=1, start_layer=1, end_layer=4))
		self._DesignParameter['via_m1_m4_sw1']['_XYCoordinates'] = [[self._DesignParameter['via_poly_m1_sw1']['_XYCoordinates'][0][0], ((self._DesignParameter['via_poly_m1_sw1']['_XYCoordinates'][0][1] - (self._DesignParameter['via_poly_m1_sw1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)) + (self._DesignParameter['via_m1_m4_sw1']['_DesignObj']._DesignParameter['ViaMet12Met2']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2))]]
		self._DesignParameter['via_m1_m4_sw2'] = self._SrefElementDeclaration(_DesignObj=ViaStack._ViaStack(_Name='via_m1_m4_sw2In{}'.format(_Name)))[0]
		self._DesignParameter['via_m1_m4_sw2']['_DesignObj']._CalculateStackMinimumEnclosureY(**dict(COX=max(2, max(1, (1 + int((((self._DesignParameter['via_poly_m1_sw2']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] - drc._VIAxMinSpace) - (2 * drc._VIAxMinEnclosureByMetx)) / (drc._VIAxMinWidth + drc._VIAxMinSpace)))))), COY=1, start_layer=1, end_layer=4))
		self._DesignParameter['via_m1_m4_sw2']['_XYCoordinates'] = [[self._DesignParameter['via_poly_m1_sw2']['_XYCoordinates'][0][0], ((self._DesignParameter['via_poly_m1_sw2']['_XYCoordinates'][0][1] - (self._DesignParameter['via_poly_m1_sw2']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)) + (self._DesignParameter['via_m1_m4_sw2']['_DesignObj']._DesignParameter['ViaMet12Met2']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2))]]
		guardring_left = (((self._DesignParameter['m1_pmos_cap_routing']['_XYCoordinates'][0][0][0] - (self._DesignParameter['m1_pmos_cap_routing']['_Width'] / 2)) - (self._DesignParameter['guardring']['_DesignObj']._DesignParameter['left']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] / 2)) - drc._Metal1MinSpace3)
		guardring_right = ((max(((self._DesignParameter['pmos_sw2']['_XYCoordinates'][0][0] + self._DesignParameter['pmos_sw2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][0]) + (self._DesignParameter['pmos_sw2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth'] / 2)), (((self._DesignParameter['via_m1_m4_sw2']['_XYCoordinates'][0][0] + self._DesignParameter['via_m1_m4_sw2']['_DesignObj']._DesignParameter['ViaMet12Met2']['_XYCoordinates'][0][0]) + self._DesignParameter['via_m1_m4_sw2']['_DesignObj']._DesignParameter['ViaMet12Met2']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0]) + (self._DesignParameter['via_m1_m4_sw2']['_DesignObj']._DesignParameter['ViaMet12Met2']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] / 2)), (self._DesignParameter['m1_pmos_sw2_routing']['_XYCoordinates'][(- 1)][0][0] + (self._DesignParameter['m1_pmos_sw2_routing']['_Width'] / 2))) + (self._DesignParameter['guardring']['_DesignObj']._DesignParameter['right']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] / 2)) + drc._Metal1MinSpace3)
		guardring_top = ((((self._DesignParameter['pmos_cap']['_XYCoordinates'][0][1] + self._DesignParameter['pmos_cap']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1]) + (self._DesignParameter['pmos_cap']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_YWidth'] / 2)) + (self._DesignParameter['guardring']['_DesignObj']._DesignParameter['top']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)) + drc._Metal1MinSpace3)
		guardring_bottom = ((min(((self._DesignParameter['via_poly_m1_pmos_cap']['_XYCoordinates'][0][1] + self._DesignParameter['via_poly_m1_pmos_cap']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) - (self._DesignParameter['via_poly_m1_pmos_cap']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)), ((self._DesignParameter['via_poly_m1_sw1']['_XYCoordinates'][0][1] + self._DesignParameter['via_poly_m1_sw1']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) - (self._DesignParameter['via_poly_m1_sw1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)), ((self._DesignParameter['via_poly_m1_sw2']['_XYCoordinates'][0][1] + self._DesignParameter['via_poly_m1_sw2']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) - (self._DesignParameter['via_poly_m1_sw2']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)), (((self._DesignParameter['via_m1_m3_pmos_cap']['_XYCoordinates'][0][1] + self._DesignParameter['via_m1_m3_pmos_cap']['_DesignObj']._DesignParameter['ViaMet12Met2']['_XYCoordinates'][0][1]) + self._DesignParameter['via_m1_m3_pmos_cap']['_DesignObj']._DesignParameter['ViaMet12Met2']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) - (self._DesignParameter['via_m1_m3_pmos_cap']['_DesignObj']._DesignParameter['ViaMet12Met2']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2))) - (self._DesignParameter['guardring']['_DesignObj']._DesignParameter['bot']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)) - drc._Metal1MinSpace3)
		if guardring_width == None :
			guardring_xwidth=guardring_right - guardring_left
		elif guardring_width != None :
			guardring_xwidth=guardring_width

		if guardring_height == None :
			guardring_yheight=guardring_top - guardring_bottom
		elif guardring_width != None :
			guardring_yheight=guardring_height


		self._DesignParameter['guardring']['_DesignObj']._CalculateDesignParameter(**dict(height=guardring_yheight, width=guardring_xwidth, contact_bottom=guardring_co_bottom, contact_top=guardring_co_top, contact_left=guardring_co_left, contact_right=guardring_co_right))
		self._DesignParameter['guardring']['_XYCoordinates'] = [[((guardring_right + guardring_left) / 2), ((guardring_top + guardring_bottom) / 2)]]
		path_list = []
		xy_offset = [0, 0]
		if (len(self._DesignParameter['pmos_cap']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates']) == 1):
		    mode = 'vertical'
		    _width = (drc._Metal1MinWidth * 2.2)
		elif (self._DesignParameter['pmos_cap']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][0] == self._DesignParameter['pmos_cap']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][0]):
		    mode = 'horizontal'
		    _width = (drc._Metal1MinWidth * 2.2)
		elif (self._DesignParameter['pmos_cap']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1] == self._DesignParameter['pmos_cap']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][1]):
		    mode = 'vertical'
		    _width = (drc._Metal1MinWidth * 2.2)
		else:
		    print('Invalid Target Input')
		if (mode == 'vertical'):
		    xy_with_offset = []
		    target_y_value = [[(+ (self._DesignParameter['guardring']['_XYCoordinates'][0][0] + self._DesignParameter['guardring']['_DesignObj']._DesignParameter['top']['_XYCoordinates'][0][0])), (+ (self._DesignParameter['guardring']['_XYCoordinates'][0][1] + self._DesignParameter['guardring']['_DesignObj']._DesignParameter['top']['_XYCoordinates'][0][1]))]][0][1]
		    for i in range(len(self._DesignParameter['pmos_cap']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		        xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['pmos_cap']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['pmos_cap']['_XYCoordinates'][0][1])], self._DesignParameter['pmos_cap']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		elif (mode == 'horizontal'):
		    xy_with_offset = []
		    target_x_value = [[(+ (self._DesignParameter['guardring']['_XYCoordinates'][0][0] + self._DesignParameter['guardring']['_DesignObj']._DesignParameter['top']['_XYCoordinates'][0][0])), (+ (self._DesignParameter['guardring']['_XYCoordinates'][0][1] + self._DesignParameter['guardring']['_DesignObj']._DesignParameter['top']['_XYCoordinates'][0][1]))]][0][0]
		    for i in range(len(self._DesignParameter['pmos_cap']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		        xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['pmos_cap']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['pmos_cap']['_XYCoordinates'][0][1])], self._DesignParameter['pmos_cap']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		for i in range(len(path_list)):
		    path_list[i][0] = [(xy + offset) for (xy, offset) in zip(path_list[i][0], xy_offset)]
		self._DesignParameter['m1_pmos_cap'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=_width)
		self._DesignParameter['m1_pmos_cap']['_XYCoordinates'] = path_list
		path_list = []
		xy_offset = [0, 0]
		if (len(self._DesignParameter['pmos_sw1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates']) == 1):
		    mode = 'vertical'
		    _width = (drc._Metal1MinWidth * 1.72)
		elif (self._DesignParameter['pmos_sw1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][0] == self._DesignParameter['pmos_sw1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][0]):
		    mode = 'horizontal'
		    _width = (drc._Metal1MinWidth * 1.72)
		elif (self._DesignParameter['pmos_sw1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1] == self._DesignParameter['pmos_sw1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][1]):
		    mode = 'vertical'
		    _width = (drc._Metal1MinWidth * 1.72)
		else:
		    print('Invalid Target Input')
		if (mode == 'vertical'):
		    xy_with_offset = []
		    target_y_value = [[(+ (self._DesignParameter['guardring']['_XYCoordinates'][0][0] + self._DesignParameter['guardring']['_DesignObj']._DesignParameter['top']['_XYCoordinates'][0][0])), (+ (self._DesignParameter['guardring']['_XYCoordinates'][0][1] + self._DesignParameter['guardring']['_DesignObj']._DesignParameter['top']['_XYCoordinates'][0][1]))]][0][1]
		    for i in range(len(self._DesignParameter['pmos_sw1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		        if ((i % 2) == 1):
		            xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['pmos_sw1']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['pmos_sw1']['_XYCoordinates'][0][1])], self._DesignParameter['pmos_sw1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		elif (mode == 'horizontal'):
		    xy_with_offset = []
		    target_x_value = [[(+ (self._DesignParameter['guardring']['_XYCoordinates'][0][0] + self._DesignParameter['guardring']['_DesignObj']._DesignParameter['top']['_XYCoordinates'][0][0])), (+ (self._DesignParameter['guardring']['_XYCoordinates'][0][1] + self._DesignParameter['guardring']['_DesignObj']._DesignParameter['top']['_XYCoordinates'][0][1]))]][0][0]
		    for i in range(len(self._DesignParameter['pmos_sw1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		        if ((i % 2) == 1):
		            xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['pmos_sw1']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['pmos_sw1']['_XYCoordinates'][0][1])], self._DesignParameter['pmos_sw1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		for i in range(len(path_list)):
		    path_list[i][0] = [(xy + offset) for (xy, offset) in zip(path_list[i][0], xy_offset)]
		self._DesignParameter['m1_sw1'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=_width)
		self._DesignParameter['m1_sw1']['_XYCoordinates'] = path_list
		path_list = []
		xy_offset = [0, 0]
		if (len(self._DesignParameter['pmos_sw2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates']) == 1):
		    mode = 'vertical'
		    _width = (drc._Metal1MinWidth * 1.72)
		elif (self._DesignParameter['pmos_sw2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][0] == self._DesignParameter['pmos_sw2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][0]):
		    mode = 'horizontal'
		    _width = (drc._Metal1MinWidth * 1.72)
		elif (self._DesignParameter['pmos_sw2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1] == self._DesignParameter['pmos_sw2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][1]):
		    mode = 'vertical'
		    _width = (drc._Metal1MinWidth * 1.72)
		else:
		    print('Invalid Target Input')
		if (mode == 'vertical'):
		    xy_with_offset = []
		    target_y_value = [[(+ (self._DesignParameter['guardring']['_XYCoordinates'][0][0] + self._DesignParameter['guardring']['_DesignObj']._DesignParameter['top']['_XYCoordinates'][0][0])), (+ (self._DesignParameter['guardring']['_XYCoordinates'][0][1] + self._DesignParameter['guardring']['_DesignObj']._DesignParameter['top']['_XYCoordinates'][0][1]))]][0][1]
		    for i in range(len(self._DesignParameter['pmos_sw2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		        if ((i % 2) == 0):
		            xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['pmos_sw2']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['pmos_sw2']['_XYCoordinates'][0][1])], self._DesignParameter['pmos_sw2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		elif (mode == 'horizontal'):
		    xy_with_offset = []
		    target_x_value = [[(+ (self._DesignParameter['guardring']['_XYCoordinates'][0][0] + self._DesignParameter['guardring']['_DesignObj']._DesignParameter['top']['_XYCoordinates'][0][0])), (+ (self._DesignParameter['guardring']['_XYCoordinates'][0][1] + self._DesignParameter['guardring']['_DesignObj']._DesignParameter['top']['_XYCoordinates'][0][1]))]][0][0]
		    for i in range(len(self._DesignParameter['pmos_sw2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		        if ((i % 2) == 0):
		            xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['pmos_sw2']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['pmos_sw2']['_XYCoordinates'][0][1])], self._DesignParameter['pmos_sw2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		for i in range(len(path_list)):
		    path_list[i][0] = [(xy + offset) for (xy, offset) in zip(path_list[i][0], xy_offset)]
		self._DesignParameter['m1_sw2'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=_width)
		self._DesignParameter['m1_sw2']['_XYCoordinates'] = path_list
		self._DesignParameter['additional_m1_pmos_cap'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _XWidth=max(self._DesignParameter['via_poly_m1_pmos_cap']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'], self._DesignParameter['via_m1_m3_pmos_cap']['_DesignObj']._DesignParameter['ViaMet12Met2']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']), _YWidth=max(self._DesignParameter['via_m1_m3_pmos_cap']['_DesignObj']._DesignParameter['ViaMet12Met2']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'], self._DesignParameter['via_poly_m1_pmos_cap']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']))
		self._DesignParameter['additional_m1_pmos_cap']['_XYCoordinates'] = [[(+ self._DesignParameter['via_m1_m3_pmos_cap']['_XYCoordinates'][0][0]), (+ self._DesignParameter['via_m1_m3_pmos_cap']['_XYCoordinates'][0][1])]]
		self._DesignParameter['additional_m1_pmos_sw1'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _XWidth=max(self._DesignParameter['via_m1_m4_sw1']['_DesignObj']._DesignParameter['ViaMet12Met2']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'], self._DesignParameter['via_poly_m1_sw1']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']), _YWidth=max(self._DesignParameter['via_poly_m1_sw1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'], self._DesignParameter['via_m1_m4_sw1']['_DesignObj']._DesignParameter['ViaMet12Met2']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']))
		self._DesignParameter['additional_m1_pmos_sw1']['_XYCoordinates'] = [[(+ self._DesignParameter['via_poly_m1_sw1']['_XYCoordinates'][0][0]), (+ self._DesignParameter['via_poly_m1_sw1']['_XYCoordinates'][0][1])]]
		self._DesignParameter['additional_m1_pmos_sw2'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _XWidth=max(self._DesignParameter['via_m1_m4_sw2']['_DesignObj']._DesignParameter['ViaMet12Met2']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'], self._DesignParameter['via_poly_m1_sw2']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']), _YWidth=max(self._DesignParameter['via_poly_m1_sw2']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'], self._DesignParameter['via_m1_m4_sw2']['_DesignObj']._DesignParameter['ViaMet12Met2']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']))
		self._DesignParameter['additional_m1_pmos_sw2']['_XYCoordinates'] = [[(+ self._DesignParameter['via_poly_m1_sw2']['_XYCoordinates'][0][0]), (+ self._DesignParameter['via_poly_m1_sw2']['_XYCoordinates'][0][1])]]
		self._DesignParameter['m1_guardring_bot'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _XWidth=self._DesignParameter['guardring']['_DesignObj']._DesignParameter['bot']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'], _YWidth=self._DesignParameter['guardring']['_DesignObj']._DesignParameter['bot']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'])
		self._DesignParameter['m1_guardring_bot']['_XYCoordinates'] = [[(+ ((self._DesignParameter['guardring']['_XYCoordinates'][0][0] + self._DesignParameter['guardring']['_DesignObj']._DesignParameter['bot']['_XYCoordinates'][0][0]) + self._DesignParameter['guardring']['_DesignObj']._DesignParameter['bot']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0])), (+ ((self._DesignParameter['guardring']['_XYCoordinates'][0][1] + self._DesignParameter['guardring']['_DesignObj']._DesignParameter['bot']['_XYCoordinates'][0][1]) + self._DesignParameter['guardring']['_DesignObj']._DesignParameter['bot']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]))]]
		via_num_sw2 = max(1, max(1, (1 + int(((((self._DesignParameter['pmos_sw2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_YWidth'] / 2) - drc._VIAxMinSpace) - (2 * drc._VIAxMinEnclosureByMetx)) / (drc._VIAxMinWidth + drc._VIAxMinSpace))))))
		via_num_sw1 = max(1, max(1, (1 + int(((((self._DesignParameter['pmos_sw1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_YWidth'] / 2) - drc._VIAxMinSpace) - (2 * drc._VIAxMinEnclosureByMetx)) / (drc._VIAxMinWidth + drc._VIAxMinSpace))))))
		self._DesignParameter['nwell'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['NWELL'][0], _Datatype=DesignParameters._LayerMapping['NWELL'][1], _XWidth=((self._DesignParameter['guardring']['_XYCoordinates'][0][0] + self._DesignParameter['guardring']['_DesignObj']._DesignParameter['nw_right']['_XYCoordinates'][0][0]) - (self._DesignParameter['guardring']['_XYCoordinates'][0][0] + self._DesignParameter['guardring']['_DesignObj']._DesignParameter['nw_left']['_XYCoordinates'][0][0])), _YWidth=((self._DesignParameter['guardring']['_XYCoordinates'][0][1] + self._DesignParameter['guardring']['_DesignObj']._DesignParameter['nw_top']['_XYCoordinates'][0][1]) - (self._DesignParameter['guardring']['_XYCoordinates'][0][1] + self._DesignParameter['guardring']['_DesignObj']._DesignParameter['nw_bot']['_XYCoordinates'][0][1])))
		self._DesignParameter['nwell']['_XYCoordinates'] = [[(+ self._DesignParameter['guardring']['_XYCoordinates'][0][0]), (+ self._DesignParameter['guardring']['_XYCoordinates'][0][1])]]
		self._DesignParameter['via_drain_sw2'] = self._SrefElementDeclaration(_DesignObj=ViaStack._ViaStack(_Name='via_drain_sw2In{}'.format(_Name)))[0]
		self._DesignParameter['via_drain_sw2']['_DesignObj']._CalculateStackMinimumEnclosureX(**dict(COX=1, COY=via_num_sw2, start_layer=1, end_layer=4))
		self._DesignParameter['via_drain_sw2']['_XYCoordinates'] = None
		XYList = []
		xy_offset = (0, ((self._DesignParameter['pmos_sw2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_YWidth'] / 2) - (self._DesignParameter['via_drain_sw2']['_DesignObj']._DesignParameter['ViaMet12Met2']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)))
		for i in range(len(self._DesignParameter['pmos_sw2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		    if ((i % 2) == 1):
		        xy = (self._DesignParameter['pmos_sw2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i][0] if (type(self._DesignParameter['pmos_sw2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i][0]) == list) else self._DesignParameter['pmos_sw2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])
		        XYList.append([((x + y) + z) for (x, y, z) in zip([(0 + self._DesignParameter['pmos_sw2']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['pmos_sw2']['_XYCoordinates'][0][1])], xy, xy_offset)])
		self._DesignParameter['via_drain_sw2']['_XYCoordinates'] = XYList
		self._DesignParameter['via_source_sw1'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='via_source_sw1In{}'.format(_Name)))[0]
		self._DesignParameter['via_source_sw1']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(**dict(_ViaMet12Met2NumberOfCOX=1, _ViaMet12Met2NumberOfCOY=via_num_sw1))
		self._DesignParameter['via_source_sw1']['_XYCoordinates'] = None
		XYList = []
		xy_offset = (0, (((- self._DesignParameter['pmos_sw1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_YWidth']) / 2) + (self._DesignParameter['via_source_sw1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)))
		for i in range(len(self._DesignParameter['pmos_sw1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		    if ((i % 2) == 0):
		        xy = (self._DesignParameter['pmos_sw1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i][0] if (type(self._DesignParameter['pmos_sw1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i][0]) == list) else self._DesignParameter['pmos_sw1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])
		        XYList.append([((x + y) + z) for (x, y, z) in zip([(0 + self._DesignParameter['pmos_sw1']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['pmos_sw1']['_XYCoordinates'][0][1])], xy, xy_offset)])
		self._DesignParameter['via_source_sw1']['_XYCoordinates'] = XYList
		self._DesignParameter['additional_pp_layer'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['PIMP'][0], _Datatype=DesignParameters._LayerMapping['PIMP'][1], _XWidth=(((self._DesignParameter['pmos_sw2']['_XYCoordinates'][0][0] + self._DesignParameter['pmos_sw2']['_DesignObj']._DesignParameter['_PPLayer']['_XYCoordinates'][0][0]) + (self._DesignParameter['pmos_sw2']['_DesignObj']._DesignParameter['_PPLayer']['_XWidth'] / 2)) - ((self._DesignParameter['pmos_cap']['_XYCoordinates'][0][0] + self._DesignParameter['pmos_cap']['_DesignObj']._DesignParameter['_PPLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['pmos_cap']['_DesignObj']._DesignParameter['_PPLayer']['_XWidth'] / 2))), _YWidth=(((self._DesignParameter['pmos_cap']['_XYCoordinates'][0][1] + self._DesignParameter['pmos_cap']['_DesignObj']._DesignParameter['_PPLayer']['_XYCoordinates'][0][1]) + (self._DesignParameter['pmos_cap']['_DesignObj']._DesignParameter['_PPLayer']['_YWidth'] / 2)) - min(((self._DesignParameter['pmos_cap']['_XYCoordinates'][0][1] + self._DesignParameter['pmos_cap']['_DesignObj']._DesignParameter['_PPLayer']['_XYCoordinates'][0][1]) - (self._DesignParameter['pmos_cap']['_DesignObj']._DesignParameter['_PPLayer']['_YWidth'] / 2)), ((self._DesignParameter['pmos_sw1']['_XYCoordinates'][0][1] + self._DesignParameter['pmos_sw1']['_DesignObj']._DesignParameter['_PPLayer']['_XYCoordinates'][0][1]) - (self._DesignParameter['pmos_sw1']['_DesignObj']._DesignParameter['_PPLayer']['_YWidth'] / 2)), ((self._DesignParameter['pmos_sw2']['_XYCoordinates'][0][1] + self._DesignParameter['pmos_sw2']['_DesignObj']._DesignParameter['_PPLayer']['_XYCoordinates'][0][1]) - (self._DesignParameter['pmos_sw2']['_DesignObj']._DesignParameter['_PPLayer']['_YWidth'] / 2)))))
		self._DesignParameter['additional_pp_layer']['_XYCoordinates'] = [[((((self._DesignParameter['pmos_sw2']['_XYCoordinates'][0][0] + self._DesignParameter['pmos_sw2']['_DesignObj']._DesignParameter['_PPLayer']['_XYCoordinates'][0][0]) + (self._DesignParameter['pmos_sw2']['_DesignObj']._DesignParameter['_PPLayer']['_XWidth'] / 2)) + ((self._DesignParameter['pmos_cap']['_XYCoordinates'][0][0] + self._DesignParameter['pmos_cap']['_DesignObj']._DesignParameter['_PPLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['pmos_cap']['_DesignObj']._DesignParameter['_PPLayer']['_XWidth'] / 2))) / 2), ((((self._DesignParameter['pmos_cap']['_XYCoordinates'][0][1] + self._DesignParameter['pmos_cap']['_DesignObj']._DesignParameter['_PPLayer']['_XYCoordinates'][0][1]) + (self._DesignParameter['pmos_cap']['_DesignObj']._DesignParameter['_PPLayer']['_YWidth'] / 2)) + min(((self._DesignParameter['pmos_cap']['_XYCoordinates'][0][1] + self._DesignParameter['pmos_cap']['_DesignObj']._DesignParameter['_PPLayer']['_XYCoordinates'][0][1]) - (self._DesignParameter['pmos_cap']['_DesignObj']._DesignParameter['_PPLayer']['_YWidth'] / 2)), ((self._DesignParameter['pmos_sw1']['_XYCoordinates'][0][1] + self._DesignParameter['pmos_sw1']['_DesignObj']._DesignParameter['_PPLayer']['_XYCoordinates'][0][1]) - (self._DesignParameter['pmos_sw1']['_DesignObj']._DesignParameter['_PPLayer']['_YWidth'] / 2)), ((self._DesignParameter['pmos_sw2']['_XYCoordinates'][0][1] + self._DesignParameter['pmos_sw2']['_DesignObj']._DesignParameter['_PPLayer']['_XYCoordinates'][0][1]) - (self._DesignParameter['pmos_sw2']['_DesignObj']._DesignParameter['_PPLayer']['_YWidth'] / 2)))) / 2)]]

		xvtlayer=pmos_cap_xvt
		_xvtlayer='_'+pmos_cap_xvt+'layer'
		self._DesignParameter['additional_xvt_layer']=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping[xvtlayer][0], _Datatype=DesignParameters._LayerMapping[xvtlayer][1], _XWidth=(((self._DesignParameter['pmos_sw2']['_XYCoordinates'][0][0] + self._DesignParameter['pmos_sw2']['_DesignObj']._DesignParameter['_LVTLayer']['_XYCoordinates'][0][0]) + (self._DesignParameter['pmos_sw2']['_DesignObj']._DesignParameter['_LVTLayer']['_XWidth'] / 2)) - ((self._DesignParameter['pmos_cap']['_XYCoordinates'][0][0] + self._DesignParameter['pmos_cap']['_DesignObj']._DesignParameter['_LVTLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['pmos_cap']['_DesignObj']._DesignParameter['_LVTLayer']['_XWidth'] / 2))), _YWidth=(((self._DesignParameter['pmos_cap']['_XYCoordinates'][0][1] + self._DesignParameter['pmos_cap']['_DesignObj']._DesignParameter['_LVTLayer']['_XYCoordinates'][0][1]) + (self._DesignParameter['pmos_cap']['_DesignObj']._DesignParameter['_LVTLayer']['_YWidth'] / 2)) - min(((self._DesignParameter['pmos_cap']['_XYCoordinates'][0][1] + self._DesignParameter['pmos_cap']['_DesignObj']._DesignParameter['_LVTLayer']['_XYCoordinates'][0][1]) - (self._DesignParameter['pmos_cap']['_DesignObj']._DesignParameter['_LVTLayer']['_YWidth'] / 2)), ((self._DesignParameter['pmos_sw1']['_XYCoordinates'][0][1] + self._DesignParameter['pmos_sw1']['_DesignObj']._DesignParameter['_LVTLayer']['_XYCoordinates'][0][1]) - (self._DesignParameter['pmos_sw1']['_DesignObj']._DesignParameter['_LVTLayer']['_YWidth'] / 2)), ((self._DesignParameter['pmos_sw2']['_XYCoordinates'][0][1] + self._DesignParameter['pmos_sw2']['_DesignObj']._DesignParameter['_LVTLayer']['_XYCoordinates'][0][1]) - (self._DesignParameter['pmos_sw2']['_DesignObj']._DesignParameter['_LVTLayer']['_YWidth'] / 2)))))
		self._DesignParameter['additional_xvt_layer']['_XYCoordinates']=[[((((self._DesignParameter['pmos_sw2']['_XYCoordinates'][0][0] + self._DesignParameter['pmos_sw2']['_DesignObj']._DesignParameter['_LVTLayer']['_XYCoordinates'][0][0]) + (self._DesignParameter['pmos_sw2']['_DesignObj']._DesignParameter['_LVTLayer']['_XWidth'] / 2)) + ((self._DesignParameter['pmos_cap']['_XYCoordinates'][0][0] + self._DesignParameter['pmos_cap']['_DesignObj']._DesignParameter['_LVTLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['pmos_cap']['_DesignObj']._DesignParameter['_LVTLayer']['_XWidth'] / 2))) / 2), \
																		  (self._DesignParameter['pmos_cap']['_XYCoordinates'][0][1] + self._DesignParameter['pmos_cap']['_DesignObj']._DesignParameter['_LVTLayer']['_XYCoordinates'][0][1] + self._DesignParameter['pmos_cap']['_DesignObj']._DesignParameter['_LVTLayer']['_YWidth'] / 2 + min(self._DesignParameter['pmos_cap']['_XYCoordinates'][0][1] + self._DesignParameter['pmos_cap']['_DesignObj']._DesignParameter['_LVTLayer']['_XYCoordinates'][0][1] - self._DesignParameter['pmos_cap']['_DesignObj']._DesignParameter['_LVTLayer']['_YWidth'] / 2, self._DesignParameter['pmos_sw1']['_XYCoordinates'][0][1] + self._DesignParameter['pmos_sw1']['_DesignObj']._DesignParameter['_LVTLayer']['_XYCoordinates'][0][1] - self._DesignParameter['pmos_sw1']['_DesignObj']._DesignParameter['_LVTLayer']['_YWidth'] / 2, self._DesignParameter['pmos_sw2']['_XYCoordinates'][0][1] + self._DesignParameter['pmos_sw2']['_DesignObj']._DesignParameter['_LVTLayer']['_XYCoordinates'][0][1] - self._DesignParameter['pmos_sw2']['_DesignObj']._DesignParameter['_LVTLayer']['_YWidth'] / 2))/2]]

		self._DesignParameter['guardring']['_DesignObj']._DesignParameter['bot']['_DesignObj']._DesignParameter['_COLayer']['_XYCoordinates'] = []
