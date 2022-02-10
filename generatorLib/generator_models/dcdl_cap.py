from generatorLib import StickDiagram
from generatorLib import DesignParameters
import copy
import math
from generatorLib import DRC
from generatorLib.generator_models import ViaMet12Met2
from generatorLib.generator_models import ViaStack
from generatorLib.generator_models import NMOSWithDummy
from generatorLib.generator_models import PMOSWithDummy
from generatorLib.generator_models import ViaPoly2Met1

class dcdl_cap(StickDiagram._StickDiagram):
	def __init__(self, _DesignParameter=None, _Name='dcdl_cap'):
		if _DesignParameter != None:
			self._DesignParameter = _DesignParameter
		else:
			self._DesignParameter = dict(_Name=self._NameDeclaration(_Name=_Name), _GDSFile=self._GDSObjDeclaration(_GDSFile=None))
		self._DesignParameter['_Name']['Name'] = _Name

	def _CalculateDesignParameter(self,tg_gate=2,cap_gate=1,tg_gate_spacing=None,cap_gate_spacing=None,tg_nmos_width=200,tg_pmos_width=200,tg_length=30,tg_sdwidth=None,cap_sdwidth=None,tg_dummy=False,cap_dummy=False,tg_xvt='SLVT',cap_xvt='SLVT',pmos_y=420,cap_nmos_width=200,cap_pmos_width=200,cap_length=150,cap_x=384):
	
		drc = DRC.DRC()
		_Name = self._DesignParameter['_Name']['_Name']
		
		self._DesignParameter['slvtnfet_b_CDNS_6377315927614_0'] = self._SrefElementDeclaration(_DesignObj=NMOSWithDummy._NMOS(_Name='slvtnfet_b_CDNS_6377315927614_0In{}'.format(_Name)))[0]
		self._DesignParameter['slvtnfet_b_CDNS_6377315927614_0']['_DesignObj']._CalculateNMOSDesignParameter(**dict(_NMOSNumberofGate=tg_gate, _NMOSChannelWidth=tg_nmos_width, _NMOSChannellength=tg_length, _NMOSDummy=tg_dummy, _GateSpacing=tg_gate_spacing, _SDWidth=tg_sdwidth, _XVT=tg_xvt))
		self._DesignParameter['slvtnfet_b_CDNS_6377315927614_0']['_XYCoordinates'] = [[0, 0]]
		self._DesignParameter['slvtpfet_b_CDNS_6377315927615_0'] = self._SrefElementDeclaration(_DesignObj=PMOSWithDummy._PMOS(_Name='slvtpfet_b_CDNS_6377315927615_0In{}'.format(_Name)))[0]
		self._DesignParameter['slvtpfet_b_CDNS_6377315927615_0']['_DesignObj']._CalculatePMOSDesignParameter(**dict(_PMOSNumberofGate=tg_gate, _PMOSChannelWidth=tg_pmos_width, _PMOSChannellength=tg_length, _PMOSDummy=tg_dummy, _GateSpacing=tg_gate_spacing, _SDWidth=tg_sdwidth, _XVT=tg_xvt))
		self._DesignParameter['slvtpfet_b_CDNS_6377315927615_0']['_XYCoordinates'] = [[self._DesignParameter['slvtnfet_b_CDNS_6377315927614_0']['_XYCoordinates'][0][0], (self._DesignParameter['slvtnfet_b_CDNS_6377315927614_0']['_XYCoordinates'][0][1] + pmos_y)]]
		self._DesignParameter['slvtnfet_b_CDNS_6377315927612_0'] = self._SrefElementDeclaration(_DesignObj=NMOSWithDummy._NMOS(_Name='slvtnfet_b_CDNS_6377315927612_0In{}'.format(_Name)))[0]
		self._DesignParameter['slvtnfet_b_CDNS_6377315927612_0']['_DesignObj']._CalculateNMOSDesignParameter(**dict(_NMOSNumberofGate=cap_gate, _NMOSChannelWidth=cap_nmos_width, _NMOSChannellength=cap_length, _NMOSDummy=cap_dummy, _GateSpacing=cap_gate_spacing, _SDWidth=cap_sdwidth, _XVT=cap_xvt))
		self._DesignParameter['slvtnfet_b_CDNS_6377315927612_0']['_XYCoordinates'] = [[(self._DesignParameter['slvtnfet_b_CDNS_6377315927614_0']['_XYCoordinates'][0][0] + cap_x), self._DesignParameter['slvtnfet_b_CDNS_6377315927614_0']['_XYCoordinates'][0][1]]]
		self._DesignParameter['slvtpfet_b_CDNS_6377315927613_0'] = self._SrefElementDeclaration(_DesignObj=PMOSWithDummy._PMOS(_Name='slvtpfet_b_CDNS_6377315927613_0In{}'.format(_Name)))[0]
		self._DesignParameter['slvtpfet_b_CDNS_6377315927613_0']['_DesignObj']._CalculatePMOSDesignParameter(**dict(_PMOSNumberofGate=cap_gate, _PMOSChannelWidth=cap_pmos_width, _PMOSChannellength=cap_length, _PMOSDummy=cap_dummy, _GateSpacing=cap_gate_spacing, _SDWidth=cap_sdwidth, _XVT=cap_xvt))
		self._DesignParameter['slvtpfet_b_CDNS_6377315927613_0']['_XYCoordinates'] = [[self._DesignParameter['slvtnfet_b_CDNS_6377315927612_0']['_XYCoordinates'][0][0], (self._DesignParameter['slvtnfet_b_CDNS_6377315927612_0']['_XYCoordinates'][0][1] + pmos_y)]]
		self._DesignParameter['cap_input'] = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_Name='cap_inputIn{}'.format(_Name)))[0]
		self._DesignParameter['cap_input']['_DesignObj']._CalculateViaPoly2Met1DesignParameterMinimumEnclosureX(**dict(_ViaPoly2Met1NumberOfCOX=max(1, (int(((((self._DesignParameter['slvtnfet_b_CDNS_6377315927612_0']['_XYCoordinates'][0][0] + self._DesignParameter['slvtnfet_b_CDNS_6377315927612_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]) - (self._DesignParameter['slvtnfet_b_CDNS_6377315927612_0']['_XYCoordinates'][0][0] + self._DesignParameter['slvtnfet_b_CDNS_6377315927612_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0])) + self._DesignParameter['slvtnfet_b_CDNS_6377315927612_0']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']) / (drc._CoMinWidth + drc._CoMinSpace))) + 1)), _ViaPoly2Met1NumberOfCOY=1))
		self._DesignParameter['cap_input']['_XYCoordinates'] = [[self._DesignParameter['slvtnfet_b_CDNS_6377315927612_0']['_XYCoordinates'][0][0], ((((self._DesignParameter['slvtnfet_b_CDNS_6377315927612_0']['_XYCoordinates'][0][1] + self._DesignParameter['slvtnfet_b_CDNS_6377315927612_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1]) + (self._DesignParameter['slvtnfet_b_CDNS_6377315927612_0']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2)) + ((self._DesignParameter['slvtpfet_b_CDNS_6377315927613_0']['_XYCoordinates'][0][1] + self._DesignParameter['slvtpfet_b_CDNS_6377315927613_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1]) - (self._DesignParameter['slvtpfet_b_CDNS_6377315927613_0']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2))) / 2)]]
		path_list = []
		if (len(self._DesignParameter['slvtpfet_b_CDNS_6377315927613_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates']) == 1):
		    mode = 'vertical'
		    _width = self._DesignParameter['slvtpfet_b_CDNS_6377315927613_0']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
		elif (self._DesignParameter['slvtpfet_b_CDNS_6377315927613_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0] == self._DesignParameter['slvtpfet_b_CDNS_6377315927613_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]):
		    mode = 'horizontal'
		    _width = self._DesignParameter['slvtpfet_b_CDNS_6377315927613_0']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
		elif (self._DesignParameter['slvtpfet_b_CDNS_6377315927613_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1] == self._DesignParameter['slvtpfet_b_CDNS_6377315927613_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][1]):
		    mode = 'vertical'
		    _width = self._DesignParameter['slvtpfet_b_CDNS_6377315927613_0']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
		else:
		    print('Invalid Target Input')
		if (mode == 'vertical'):
		    xy_with_offset = []
		    target_y_value = (self._DesignParameter['slvtnfet_b_CDNS_6377315927612_0']['_XYCoordinates'][0][1] + self._DesignParameter['slvtnfet_b_CDNS_6377315927612_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1])
		    for i in range(len(self._DesignParameter['slvtpfet_b_CDNS_6377315927613_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
		        xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['slvtpfet_b_CDNS_6377315927613_0']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['slvtpfet_b_CDNS_6377315927613_0']['_XYCoordinates'][0][1])], self._DesignParameter['slvtpfet_b_CDNS_6377315927613_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		elif (mode == 'horizontal'):
		    xy_with_offset = []
		    target_x_value = (self._DesignParameter['slvtnfet_b_CDNS_6377315927612_0']['_XYCoordinates'][0][0] + self._DesignParameter['slvtnfet_b_CDNS_6377315927612_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0])
		    for i in range(len(self._DesignParameter['slvtpfet_b_CDNS_6377315927613_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
		        xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['slvtpfet_b_CDNS_6377315927613_0']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['slvtpfet_b_CDNS_6377315927613_0']['_XYCoordinates'][0][1])], self._DesignParameter['slvtpfet_b_CDNS_6377315927613_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		self._DesignParameter['poly_cap_gate'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _Width=_width)
		self._DesignParameter['poly_cap_gate']['_XYCoordinates'] = path_list
		path_list = []
		if (len(self._DesignParameter['slvtpfet_b_CDNS_6377315927615_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates']) == 1):
		    mode = 'vertical'
		    _width = self._DesignParameter['slvtpfet_b_CDNS_6377315927615_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth']
		elif (self._DesignParameter['slvtpfet_b_CDNS_6377315927615_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][0] == self._DesignParameter['slvtpfet_b_CDNS_6377315927615_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][0]):
		    mode = 'horizontal'
		    _width = self._DesignParameter['slvtpfet_b_CDNS_6377315927615_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth']
		elif (self._DesignParameter['slvtpfet_b_CDNS_6377315927615_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1] == self._DesignParameter['slvtpfet_b_CDNS_6377315927615_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][1]):
		    mode = 'vertical'
		    _width = self._DesignParameter['slvtpfet_b_CDNS_6377315927615_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth']
		else:
		    print('Invalid Target Input')
		if (mode == 'vertical'):
		    xy_with_offset = []
		    target_y_value = (self._DesignParameter['slvtnfet_b_CDNS_6377315927614_0']['_XYCoordinates'][0][1] + self._DesignParameter['slvtnfet_b_CDNS_6377315927614_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1])
		    for i in range(len(self._DesignParameter['slvtpfet_b_CDNS_6377315927615_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		        if ((i % 2) == 0):
		            xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['slvtpfet_b_CDNS_6377315927615_0']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['slvtpfet_b_CDNS_6377315927615_0']['_XYCoordinates'][0][1])], self._DesignParameter['slvtpfet_b_CDNS_6377315927615_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		elif (mode == 'horizontal'):
		    xy_with_offset = []
		    target_x_value = (self._DesignParameter['slvtnfet_b_CDNS_6377315927614_0']['_XYCoordinates'][0][0] + self._DesignParameter['slvtnfet_b_CDNS_6377315927614_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][0])
		    for i in range(len(self._DesignParameter['slvtpfet_b_CDNS_6377315927615_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		        if ((i % 2) == 0):
		            xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['slvtpfet_b_CDNS_6377315927615_0']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['slvtpfet_b_CDNS_6377315927615_0']['_XYCoordinates'][0][1])], self._DesignParameter['slvtpfet_b_CDNS_6377315927615_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		self._DesignParameter['m1_tg_source_routing_y'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=_width)
		self._DesignParameter['m1_tg_source_routing_y']['_XYCoordinates'] = path_list
		self._DesignParameter['m1_tg_cap_routing_x'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=50)
		self._DesignParameter['m1_tg_cap_routing_x']['_XYCoordinates'] = [[[self._DesignParameter['m1_tg_source_routing_y']['_XYCoordinates'][0][0][0], self._DesignParameter['cap_input']['_XYCoordinates'][0][1]], [self._DesignParameter['cap_input']['_XYCoordinates'][0][0], self._DesignParameter['cap_input']['_XYCoordinates'][0][1]]]]
		self._DesignParameter['tg_pmos_input'] = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_Name='tg_pmos_inputIn{}'.format(_Name)))[0]
		self._DesignParameter['tg_pmos_input']['_DesignObj']._CalculateViaPoly2Met1DesignParameterMinimumEnclosureY(**dict(_ViaPoly2Met1NumberOfCOX=max(2, int((((((self._DesignParameter['slvtpfet_b_CDNS_6377315927615_0']['_XYCoordinates'][0][0] + self._DesignParameter['slvtpfet_b_CDNS_6377315927615_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]) - (self._DesignParameter['slvtpfet_b_CDNS_6377315927615_0']['_XYCoordinates'][0][0] + self._DesignParameter['slvtpfet_b_CDNS_6377315927615_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0])) + self._DesignParameter['slvtpfet_b_CDNS_6377315927615_0']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']) / (drc._CoMinWidth + drc._CoMinSpace)) + 1))), _ViaPoly2Met1NumberOfCOY=1))
		self._DesignParameter['tg_pmos_input']['_XYCoordinates'] = [[self._DesignParameter['slvtpfet_b_CDNS_6377315927615_0']['_XYCoordinates'][0][0], ((((self._DesignParameter['slvtpfet_b_CDNS_6377315927615_0']['_XYCoordinates'][0][1] + self._DesignParameter['slvtpfet_b_CDNS_6377315927615_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) + (self._DesignParameter['slvtpfet_b_CDNS_6377315927615_0']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)) + (self._DesignParameter['tg_pmos_input']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)) + 60)]]
		self._DesignParameter['tg_nmos_input'] = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_Name='tg_nmos_inputIn{}'.format(_Name)))[0]
		self._DesignParameter['tg_nmos_input']['_DesignObj']._CalculateViaPoly2Met1DesignParameterMinimumEnclosureY(**dict(_ViaPoly2Met1NumberOfCOX=max(2, int((((((self._DesignParameter['slvtnfet_b_CDNS_6377315927614_0']['_XYCoordinates'][0][0] + self._DesignParameter['slvtnfet_b_CDNS_6377315927614_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]) - (self._DesignParameter['slvtnfet_b_CDNS_6377315927614_0']['_XYCoordinates'][0][0] + self._DesignParameter['slvtnfet_b_CDNS_6377315927614_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0])) + self._DesignParameter['slvtnfet_b_CDNS_6377315927614_0']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']) / (drc._CoMinWidth + drc._CoMinSpace)) + 1))), _ViaPoly2Met1NumberOfCOY=1))
		self._DesignParameter['tg_nmos_input']['_XYCoordinates'] = [[self._DesignParameter['slvtnfet_b_CDNS_6377315927614_0']['_XYCoordinates'][0][0], ((((self._DesignParameter['slvtnfet_b_CDNS_6377315927614_0']['_XYCoordinates'][0][1] + self._DesignParameter['slvtnfet_b_CDNS_6377315927614_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1]) - (self._DesignParameter['slvtnfet_b_CDNS_6377315927614_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_YWidth'] / 2)) - (self._DesignParameter['tg_nmos_input']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)) - 60)]]
		path_list = []
		if (len(self._DesignParameter['slvtpfet_b_CDNS_6377315927615_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates']) == 1):
		    mode = 'vertical'
		    _width = self._DesignParameter['slvtpfet_b_CDNS_6377315927615_0']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
		elif (self._DesignParameter['slvtpfet_b_CDNS_6377315927615_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0] == self._DesignParameter['slvtpfet_b_CDNS_6377315927615_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]):
		    mode = 'horizontal'
		    _width = self._DesignParameter['slvtpfet_b_CDNS_6377315927615_0']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
		elif (self._DesignParameter['slvtpfet_b_CDNS_6377315927615_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1] == self._DesignParameter['slvtpfet_b_CDNS_6377315927615_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][1]):
		    mode = 'vertical'
		    _width = self._DesignParameter['slvtpfet_b_CDNS_6377315927615_0']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
		else:
		    print('Invalid Target Input')
		if (mode == 'vertical'):
		    xy_with_offset = []
		    target_y_value = ((self._DesignParameter['tg_pmos_input']['_XYCoordinates'][0][1] + self._DesignParameter['tg_pmos_input']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1]) + (self._DesignParameter['tg_pmos_input']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2))
		    for i in range(len(self._DesignParameter['slvtpfet_b_CDNS_6377315927615_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
		        xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['slvtpfet_b_CDNS_6377315927615_0']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['slvtpfet_b_CDNS_6377315927615_0']['_XYCoordinates'][0][1])], self._DesignParameter['slvtpfet_b_CDNS_6377315927615_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		elif (mode == 'horizontal'):
		    xy_with_offset = []
		    target_x_value = (self._DesignParameter['tg_pmos_input']['_XYCoordinates'][0][0] + self._DesignParameter['tg_pmos_input']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0])
		    for i in range(len(self._DesignParameter['slvtpfet_b_CDNS_6377315927615_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
		        xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['slvtpfet_b_CDNS_6377315927615_0']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['slvtpfet_b_CDNS_6377315927615_0']['_XYCoordinates'][0][1])], self._DesignParameter['slvtpfet_b_CDNS_6377315927615_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		self._DesignParameter['po_tg_pmos_input_routing_y'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _Width=_width)
		self._DesignParameter['po_tg_pmos_input_routing_y']['_XYCoordinates'] = path_list
		path_list = []
		if (len(self._DesignParameter['slvtnfet_b_CDNS_6377315927614_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates']) == 1):
		    mode = 'vertical'
		    _width = self._DesignParameter['slvtnfet_b_CDNS_6377315927614_0']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
		elif (self._DesignParameter['slvtnfet_b_CDNS_6377315927614_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0] == self._DesignParameter['slvtnfet_b_CDNS_6377315927614_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]):
		    mode = 'horizontal'
		    _width = self._DesignParameter['slvtnfet_b_CDNS_6377315927614_0']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
		elif (self._DesignParameter['slvtnfet_b_CDNS_6377315927614_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1] == self._DesignParameter['slvtnfet_b_CDNS_6377315927614_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][1]):
		    mode = 'vertical'
		    _width = self._DesignParameter['slvtnfet_b_CDNS_6377315927614_0']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
		else:
		    print('Invalid Target Input')
		if (mode == 'vertical'):
		    xy_with_offset = []
		    target_y_value = ((self._DesignParameter['tg_nmos_input']['_XYCoordinates'][0][1] + self._DesignParameter['tg_nmos_input']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1]) - (self._DesignParameter['tg_nmos_input']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2))
		    for i in range(len(self._DesignParameter['slvtnfet_b_CDNS_6377315927614_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
		        xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['slvtnfet_b_CDNS_6377315927614_0']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['slvtnfet_b_CDNS_6377315927614_0']['_XYCoordinates'][0][1])], self._DesignParameter['slvtnfet_b_CDNS_6377315927614_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		elif (mode == 'horizontal'):
		    xy_with_offset = []
		    target_x_value = (self._DesignParameter['tg_nmos_input']['_XYCoordinates'][0][0] + self._DesignParameter['tg_nmos_input']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0])
		    for i in range(len(self._DesignParameter['slvtnfet_b_CDNS_6377315927614_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
		        xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['slvtnfet_b_CDNS_6377315927614_0']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['slvtnfet_b_CDNS_6377315927614_0']['_XYCoordinates'][0][1])], self._DesignParameter['slvtnfet_b_CDNS_6377315927614_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		self._DesignParameter['po_tg_nmos_routing_y'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _Width=_width)
		self._DesignParameter['po_tg_nmos_routing_y']['_XYCoordinates'] = path_list
		self._DesignParameter['NWELL_boundary_2'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['NWELL'][0], _Datatype=DesignParameters._LayerMapping['NWELL'][1], _XWidth=((((self._DesignParameter['slvtpfet_b_CDNS_6377315927613_0']['_XYCoordinates'][0][0] + self._DesignParameter['slvtpfet_b_CDNS_6377315927613_0']['_DesignObj']._DesignParameter['_ODLayer']['_XYCoordinates'][0][0]) + (self._DesignParameter['slvtpfet_b_CDNS_6377315927613_0']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth'] / 2)) - ((self._DesignParameter['slvtpfet_b_CDNS_6377315927615_0']['_XYCoordinates'][0][0] + self._DesignParameter['slvtpfet_b_CDNS_6377315927615_0']['_DesignObj']._DesignParameter['_ODLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['slvtpfet_b_CDNS_6377315927615_0']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth'] / 2))) + (2 * drc._NwMinEnclosurePactive2)), _YWidth=((((self._DesignParameter['slvtpfet_b_CDNS_6377315927615_0']['_XYCoordinates'][0][1] + self._DesignParameter['slvtpfet_b_CDNS_6377315927615_0']['_DesignObj']._DesignParameter['_ODLayer']['_XYCoordinates'][0][1]) + (self._DesignParameter['slvtpfet_b_CDNS_6377315927615_0']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth'] / 2)) + drc._NwMinEnclosurePactive2) - ((self._DesignParameter['slvtpfet_b_CDNS_6377315927615_0']['_XYCoordinates'][0][1] + self._DesignParameter['slvtpfet_b_CDNS_6377315927615_0']['_DesignObj']._DesignParameter['_PPLayer']['_XYCoordinates'][0][1]) - (self._DesignParameter['slvtpfet_b_CDNS_6377315927615_0']['_DesignObj']._DesignParameter['_PPLayer']['_YWidth'] / 2))))
		self._DesignParameter['NWELL_boundary_2']['_XYCoordinates'] = [[((((self._DesignParameter['slvtpfet_b_CDNS_6377315927615_0']['_XYCoordinates'][0][0] + self._DesignParameter['slvtpfet_b_CDNS_6377315927615_0']['_DesignObj']._DesignParameter['_ODLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['slvtpfet_b_CDNS_6377315927615_0']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth'] / 2)) + ((self._DesignParameter['slvtpfet_b_CDNS_6377315927613_0']['_XYCoordinates'][0][0] + self._DesignParameter['slvtpfet_b_CDNS_6377315927613_0']['_DesignObj']._DesignParameter['_ODLayer']['_XYCoordinates'][0][0]) + (self._DesignParameter['slvtpfet_b_CDNS_6377315927613_0']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth'] / 2))) / 2), (((((self._DesignParameter['slvtpfet_b_CDNS_6377315927615_0']['_XYCoordinates'][0][1] + self._DesignParameter['slvtpfet_b_CDNS_6377315927615_0']['_DesignObj']._DesignParameter['_ODLayer']['_XYCoordinates'][0][1]) + (self._DesignParameter['slvtpfet_b_CDNS_6377315927615_0']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth'] / 2)) + drc._NwMinEnclosurePactive2) + ((self._DesignParameter['slvtpfet_b_CDNS_6377315927615_0']['_XYCoordinates'][0][1] + self._DesignParameter['slvtpfet_b_CDNS_6377315927615_0']['_DesignObj']._DesignParameter['_PPLayer']['_XYCoordinates'][0][1]) - (self._DesignParameter['slvtpfet_b_CDNS_6377315927615_0']['_DesignObj']._DesignParameter['_PPLayer']['_YWidth'] / 2))) / 2)]]
		XYList = []
		xy_offset = [0, 0]
		for i in range(len(self._DesignParameter['slvtpfet_b_CDNS_6377315927615_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		    if ((i % 2) == 1):
		        xy = (self._DesignParameter['slvtpfet_b_CDNS_6377315927615_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i][0] if (type(self._DesignParameter['slvtpfet_b_CDNS_6377315927615_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i][0]) == list) else self._DesignParameter['slvtpfet_b_CDNS_6377315927615_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])
		        XYList.append([((x + y) + z) for (x, y, z) in zip([(0 + self._DesignParameter['slvtpfet_b_CDNS_6377315927615_0']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['slvtpfet_b_CDNS_6377315927615_0']['_XYCoordinates'][0][1])], xy, xy_offset)])
		self._DesignParameter['via_m1_m3_pmos_output'] = self._SrefElementDeclaration(_DesignObj=ViaStack._ViaStack(_Name='via_m1_m3_pmos_outputIn{}'.format(_Name)))[0]
		self._DesignParameter['via_m1_m3_pmos_output']['_DesignObj']._CalculateStackMinimumEnclosureX(**dict(COX=1, COY=2, start_layer=1, end_layer=3))
		self._DesignParameter['via_m1_m3_pmos_output']['_XYCoordinates'] = XYList
		XYList = []
		xy_offset = [0, 0]
		for i in range(len(self._DesignParameter['slvtnfet_b_CDNS_6377315927614_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		    if ((i % 2) == 1):
		        xy = (self._DesignParameter['slvtnfet_b_CDNS_6377315927614_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i][0] if (type(self._DesignParameter['slvtnfet_b_CDNS_6377315927614_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i][0]) == list) else self._DesignParameter['slvtnfet_b_CDNS_6377315927614_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])
		        XYList.append([((x + y) + z) for (x, y, z) in zip([(0 + self._DesignParameter['slvtnfet_b_CDNS_6377315927614_0']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['slvtnfet_b_CDNS_6377315927614_0']['_XYCoordinates'][0][1])], xy, xy_offset)])
		self._DesignParameter['via_m1_m3_nmos_ouput'] = self._SrefElementDeclaration(_DesignObj=ViaStack._ViaStack(_Name='via_m1_m3_nmos_ouputIn{}'.format(_Name)))[0]
		self._DesignParameter['via_m1_m3_nmos_ouput']['_DesignObj']._CalculateStackMinimumEnclosureX(**dict(COX=1, COY=2, start_layer=1, end_layer=3))
		self._DesignParameter['via_m1_m3_nmos_ouput']['_XYCoordinates'] = XYList
		path_list = []
		if (len(self._DesignParameter['slvtpfet_b_CDNS_6377315927615_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates']) == 1):
		    mode = 'vertical'
		    _width = self._DesignParameter['slvtpfet_b_CDNS_6377315927615_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth']
		elif (self._DesignParameter['slvtpfet_b_CDNS_6377315927615_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][0] == self._DesignParameter['slvtpfet_b_CDNS_6377315927615_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][0]):
		    mode = 'horizontal'
		    _width = self._DesignParameter['slvtpfet_b_CDNS_6377315927615_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth']
		elif (self._DesignParameter['slvtpfet_b_CDNS_6377315927615_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1] == self._DesignParameter['slvtpfet_b_CDNS_6377315927615_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][1]):
		    mode = 'vertical'
		    _width = self._DesignParameter['slvtpfet_b_CDNS_6377315927615_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth']
		else:
		    print('Invalid Target Input')
		if (mode == 'vertical'):
		    xy_with_offset = []
		    target_y_value = (self._DesignParameter['slvtnfet_b_CDNS_6377315927614_0']['_XYCoordinates'][0][1] + self._DesignParameter['slvtnfet_b_CDNS_6377315927614_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1])
		    for i in range(len(self._DesignParameter['slvtpfet_b_CDNS_6377315927615_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		        if ((i % 2) == 1):
		            xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['slvtpfet_b_CDNS_6377315927615_0']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['slvtpfet_b_CDNS_6377315927615_0']['_XYCoordinates'][0][1])], self._DesignParameter['slvtpfet_b_CDNS_6377315927615_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		elif (mode == 'horizontal'):
		    xy_with_offset = []
		    target_x_value = (self._DesignParameter['slvtnfet_b_CDNS_6377315927614_0']['_XYCoordinates'][0][0] + self._DesignParameter['slvtnfet_b_CDNS_6377315927614_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][0])
		    for i in range(len(self._DesignParameter['slvtpfet_b_CDNS_6377315927615_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		        if ((i % 2) == 1):
		            xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['slvtpfet_b_CDNS_6377315927615_0']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['slvtpfet_b_CDNS_6377315927615_0']['_XYCoordinates'][0][1])], self._DesignParameter['slvtpfet_b_CDNS_6377315927615_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		self._DesignParameter['m3_input'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0], _Datatype=DesignParameters._LayerMapping['METAL3'][1], _Width=_width)
		self._DesignParameter['m3_input']['_XYCoordinates'] = path_list
		path_list = []
		if (len(self._DesignParameter['slvtpfet_b_CDNS_6377315927613_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates']) == 1):
		    mode = 'vertical'
		    _width = self._DesignParameter['slvtpfet_b_CDNS_6377315927613_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth']
		elif (self._DesignParameter['slvtpfet_b_CDNS_6377315927613_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][0] == self._DesignParameter['slvtpfet_b_CDNS_6377315927613_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][0]):
		    mode = 'horizontal'
		    _width = self._DesignParameter['slvtpfet_b_CDNS_6377315927613_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth']
		elif (self._DesignParameter['slvtpfet_b_CDNS_6377315927613_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1] == self._DesignParameter['slvtpfet_b_CDNS_6377315927613_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][1]):
		    mode = 'vertical'
		    _width = self._DesignParameter['slvtpfet_b_CDNS_6377315927613_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth']
		else:
		    print('Invalid Target Input')
		if (mode == 'vertical'):
		    xy_with_offset = []
		    target_y_value = ((self._DesignParameter['slvtpfet_b_CDNS_6377315927613_0']['_XYCoordinates'][0][1] + self._DesignParameter['slvtpfet_b_CDNS_6377315927613_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1]) + (self._DesignParameter['slvtpfet_b_CDNS_6377315927613_0']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2))
		    for i in range(len(self._DesignParameter['slvtpfet_b_CDNS_6377315927613_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		        xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['slvtpfet_b_CDNS_6377315927613_0']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['slvtpfet_b_CDNS_6377315927613_0']['_XYCoordinates'][0][1])], self._DesignParameter['slvtpfet_b_CDNS_6377315927613_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		elif (mode == 'horizontal'):
		    xy_with_offset = []
		    target_x_value = (self._DesignParameter['slvtpfet_b_CDNS_6377315927613_0']['_XYCoordinates'][0][0] + self._DesignParameter['slvtpfet_b_CDNS_6377315927613_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0])
		    for i in range(len(self._DesignParameter['slvtpfet_b_CDNS_6377315927613_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		        xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['slvtpfet_b_CDNS_6377315927613_0']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['slvtpfet_b_CDNS_6377315927613_0']['_XYCoordinates'][0][1])], self._DesignParameter['slvtpfet_b_CDNS_6377315927613_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		self._DesignParameter['m1_cap_vdd_routing'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=_width)
		self._DesignParameter['m1_cap_vdd_routing']['_XYCoordinates'] = path_list
		path_list = []
		if (len(self._DesignParameter['slvtnfet_b_CDNS_6377315927612_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates']) == 1):
		    mode = 'vertical'
		    _width = self._DesignParameter['slvtnfet_b_CDNS_6377315927612_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth']
		elif (self._DesignParameter['slvtnfet_b_CDNS_6377315927612_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][0] == self._DesignParameter['slvtnfet_b_CDNS_6377315927612_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][0]):
		    mode = 'horizontal'
		    _width = self._DesignParameter['slvtnfet_b_CDNS_6377315927612_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth']
		elif (self._DesignParameter['slvtnfet_b_CDNS_6377315927612_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1] == self._DesignParameter['slvtnfet_b_CDNS_6377315927612_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][1]):
		    mode = 'vertical'
		    _width = self._DesignParameter['slvtnfet_b_CDNS_6377315927612_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth']
		else:
		    print('Invalid Target Input')
		if (mode == 'vertical'):
		    xy_with_offset = []
		    target_y_value = ((self._DesignParameter['slvtnfet_b_CDNS_6377315927612_0']['_XYCoordinates'][0][1] + self._DesignParameter['slvtnfet_b_CDNS_6377315927612_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1]) - (self._DesignParameter['slvtnfet_b_CDNS_6377315927612_0']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2))
		    for i in range(len(self._DesignParameter['slvtnfet_b_CDNS_6377315927612_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		        xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['slvtnfet_b_CDNS_6377315927612_0']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['slvtnfet_b_CDNS_6377315927612_0']['_XYCoordinates'][0][1])], self._DesignParameter['slvtnfet_b_CDNS_6377315927612_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		elif (mode == 'horizontal'):
		    xy_with_offset = []
		    target_x_value = (self._DesignParameter['slvtnfet_b_CDNS_6377315927612_0']['_XYCoordinates'][0][0] + self._DesignParameter['slvtnfet_b_CDNS_6377315927612_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0])
		    for i in range(len(self._DesignParameter['slvtnfet_b_CDNS_6377315927612_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		        xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['slvtnfet_b_CDNS_6377315927612_0']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['slvtnfet_b_CDNS_6377315927612_0']['_XYCoordinates'][0][1])], self._DesignParameter['slvtnfet_b_CDNS_6377315927612_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		self._DesignParameter['m1_nmos_vss_routing'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=_width)
		self._DesignParameter['m1_nmos_vss_routing']['_XYCoordinates'] = path_list
		self._DesignParameter['via_m1_m2_pmos_input'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='via_m1_m2_pmos_inputIn{}'.format(_Name)))[0]
		self._DesignParameter['via_m1_m2_pmos_input']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureY(**dict(_ViaMet12Met2NumberOfCOX=int(max((self._DesignParameter['tg_pmos_input']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] / (drc._CoMinWidth + drc._CoMinSpace)), 2)), _ViaMet12Met2NumberOfCOY=1))
		self._DesignParameter['via_m1_m2_pmos_input']['_XYCoordinates'] = [[(+ self._DesignParameter['tg_pmos_input']['_XYCoordinates'][0][0]), (+ self._DesignParameter['tg_pmos_input']['_XYCoordinates'][0][1])]]
		self._DesignParameter['via_m1_m2_nmos_input'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='via_m1_m2_nmos_inputIn{}'.format(_Name)))[0]
		self._DesignParameter['via_m1_m2_nmos_input']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureY(**dict(_ViaMet12Met2NumberOfCOX=int(max((self._DesignParameter['tg_pmos_input']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] / (drc._CoMinWidth + drc._CoMinSpace)), 2)), _ViaMet12Met2NumberOfCOY=1))
		self._DesignParameter['via_m1_m2_nmos_input']['_XYCoordinates'] = [[(+ self._DesignParameter['tg_nmos_input']['_XYCoordinates'][0][0]), (+ self._DesignParameter['tg_nmos_input']['_XYCoordinates'][0][1])]]
		