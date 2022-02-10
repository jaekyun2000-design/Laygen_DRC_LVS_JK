from generatorLib import StickDiagram
from generatorLib import DesignParameters
import copy
import math
from generatorLib import DRC
from generatorLib.generator_models import PMOSWithDummy
from generatorLib.generator_models import ViaPoly2Met1
from generatorLib.generator_models import SupplyRails
from generatorLib.generator_models import NMOSWithDummy

class TIEH_2X_STD_v1(StickDiagram._StickDiagram):
	def __init__(self, _DesignParameter=None, _Name='TIEH_2X_STD_v1'):
		if _DesignParameter != None:
			self._DesignParameter = _DesignParameter
		else:
			self._DesignParameter = dict(_Name=self._NameDeclaration(_Name=_Name), _GDSFile=self._GDSObjDeclaration(_GDSFile=None))
		self._DesignParameter['_Name']['Name'] = _Name

	def _CalculateDesignParameter(self,nmos_y=300,pmos_y=500,gate=6,sd_width=66,gate_spacing=110,vdd2vss_height=1800,nmos_width=200,pmos_width=400,length=40,nmos_gate=1,pmos_gate=1,XVT='RVT'):
	
		drc = DRC.DRC()
		_Name = self._DesignParameter['_Name']['_Name']
		
		self._DesignParameter['vss'] = self._SrefElementDeclaration(_DesignObj=SupplyRails.SupplyRail(_Name='vssIn{}'.format(_Name)))[0]
		self._DesignParameter['vss']['_DesignObj']._CalculateDesignParameter(**dict(NumPitch=2, UnitPitch=130, Met1YWidth=80, Met2YWidth=300, PpNpYWidth=180, isPbody=True))
		self._DesignParameter['vss']['_XYCoordinates'] = [[0.0, 0.0]]
		self._DesignParameter['vdd'] = self._SrefElementDeclaration(_DesignObj=SupplyRails.SupplyRail(_Name='vddIn{}'.format(_Name)))[0]
		self._DesignParameter['vdd']['_DesignObj']._CalculateDesignParameter(**dict(NumPitch=2, UnitPitch=130, Met1YWidth=80, Met2YWidth=300, PpNpYWidth=180, isPbody=False))
		self._DesignParameter['vdd']['_XYCoordinates'] = [[self._DesignParameter['vss']['_XYCoordinates'][0][0], vdd2vss_height]]
		self._DesignParameter['nmos'] = self._SrefElementDeclaration(_DesignObj=NMOSWithDummy._NMOS(_Name='nmosIn{}'.format(_Name)))[0]
		self._DesignParameter['nmos']['_DesignObj']._CalculateNMOSDesignParameter(**dict(_NMOSNumberofGate=nmos_gate, _NMOSChannelWidth=nmos_width, _NMOSChannellength=length, _NMOSDummy=True, _GateSpacing=gate_spacing, _SDWidth=sd_width, _XVT=XVT))
		self._DesignParameter['nmos']['_XYCoordinates'] = [[self._DesignParameter['vss']['_XYCoordinates'][0][0], (self._DesignParameter['vss']['_XYCoordinates'][0][1] + nmos_y)]]
		self._DesignParameter['pmos'] = self._SrefElementDeclaration(_DesignObj=PMOSWithDummy._PMOS(_Name='pmosIn{}'.format(_Name)))[0]
		self._DesignParameter['pmos']['_DesignObj']._CalculatePMOSDesignParameter(**dict(_PMOSNumberofGate=pmos_gate, _PMOSChannelWidth=pmos_width, _PMOSChannellength=length, _PMOSDummy=True, _GateSpacing=gate_spacing, _SDWidth=sd_width, _XVT=XVT))
		self._DesignParameter['pmos']['_XYCoordinates'] = [[self._DesignParameter['vdd']['_XYCoordinates'][0][0], (self._DesignParameter['vdd']['_XYCoordinates'][0][1] - pmos_y)]]
		self._DesignParameter['vss']['_DesignObj']._CalculateDesignParameter(**dict(NumPitch=max(1, (1 + int(((((((self._DesignParameter['nmos']['_XYCoordinates'][0][0] + self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][(- 1)][0]) + (self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_PODummyLayer']['_XWidth'] / 2)) - ((self._DesignParameter['nmos']['_XYCoordinates'][0][0] + self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_PODummyLayer']['_XWidth'] / 2))) - drc._VIAxMinSpace) - (2 * drc._VIAxMinEnclosureByMetx)) / (drc._VIAxMinWidth + drc._VIAxMinSpace))))), UnitPitch=130, Met1YWidth=80, Met2YWidth=300, PpNpYWidth=180, isPbody=True))
		self._DesignParameter['vdd']['_DesignObj']._CalculateDesignParameter(**dict(NumPitch=max(1, (1 + int(((((((self._DesignParameter['pmos']['_XYCoordinates'][0][0] + self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][(- 1)][0]) + (self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_PODummyLayer']['_XWidth'] / 2)) - ((self._DesignParameter['pmos']['_XYCoordinates'][0][0] + self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_PODummyLayer']['_XWidth'] / 2))) - drc._VIAxMinSpace) - (2 * drc._VIAxMinEnclosureByMetx)) / (drc._VIAxMinWidth + drc._VIAxMinSpace))))), UnitPitch=130, Met1YWidth=80, Met2YWidth=300, PpNpYWidth=180, isPbody=True))
		self._DesignParameter['gate_input'] = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_Name='gate_inputIn{}'.format(_Name)))[0]
		self._DesignParameter['gate_input']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(**dict(_ViaPoly2Met1NumberOfCOX=1, _ViaPoly2Met1NumberOfCOY=2))
		self._DesignParameter['gate_input']['_XYCoordinates'] = [[min((self._DesignParameter['nmos']['_XYCoordinates'][0][0] + self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][0]), (self._DesignParameter['pmos']['_XYCoordinates'][0][0] + self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][0])), ((((self._DesignParameter['pmos']['_XYCoordinates'][0][1] + self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) - (self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)) + ((self._DesignParameter['nmos']['_XYCoordinates'][0][1] + self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1]) + (self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_YWidth'] / 2))) / 2)]]
		path_list = []
		if (len(self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates']) == 1):
		    mode = 'vertical'
		    _width = self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
		elif (self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0] == self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]):
		    mode = 'horizontal'
		    _width = self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
		elif (self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1] == self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][1]):
		    mode = 'vertical'
		    _width = self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
		else:
		    print('Invalid Target Input')
		if (mode == 'vertical'):
		    xy_with_offset = []
		    target_y_value = ((self._DesignParameter['gate_input']['_XYCoordinates'][0][1] + self._DesignParameter['gate_input']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1]) - (self._DesignParameter['gate_input']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2))
		    for i in range(len(self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
		        xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['nmos']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['nmos']['_XYCoordinates'][0][1])], self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		elif (mode == 'horizontal'):
		    xy_with_offset = []
		    target_x_value = (self._DesignParameter['gate_input']['_XYCoordinates'][0][0] + self._DesignParameter['gate_input']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0])
		    for i in range(len(self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
		        xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['nmos']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['nmos']['_XYCoordinates'][0][1])], self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		self._DesignParameter['poly_gate_nmos_xy'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _Width=_width)
		self._DesignParameter['poly_gate_nmos_xy']['_XYCoordinates'] = path_list
		path_list = []
		if (len(self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates']) == 1):
		    mode = 'vertical'
		    _width = self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth']
		elif (self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][0] == self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][0]):
		    mode = 'horizontal'
		    _width = self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth']
		elif (self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1] == self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][1]):
		    mode = 'vertical'
		    _width = self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth']
		else:
		    print('Invalid Target Input')
		if (mode == 'vertical'):
		    xy_with_offset = []
		    target_y_value = (self._DesignParameter['vdd']['_XYCoordinates'][0][1] + self._DesignParameter['vdd']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1])
		    for i in range(len(self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		        if ((i % 2) == 0):
		            xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['pmos']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['pmos']['_XYCoordinates'][0][1])], self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		elif (mode == 'horizontal'):
		    xy_with_offset = []
		    target_x_value = (self._DesignParameter['vdd']['_XYCoordinates'][0][0] + self._DesignParameter['vdd']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0])
		    for i in range(len(self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		        if ((i % 2) == 0):
		            xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['pmos']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['pmos']['_XYCoordinates'][0][1])], self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		self._DesignParameter['pmos_supply_routing'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=_width)
		self._DesignParameter['pmos_supply_routing']['_XYCoordinates'] = path_list
		path_list = []
		if (len(self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates']) == 1):
		    mode = 'vertical'
		    _width = self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth']
		elif (self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][0] == self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][0]):
		    mode = 'horizontal'
		    _width = self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth']
		elif (self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1] == self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][1]):
		    mode = 'vertical'
		    _width = self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth']
		else:
		    print('Invalid Target Input')
		if (mode == 'vertical'):
		    xy_with_offset = []
		    target_y_value = (self._DesignParameter['vss']['_XYCoordinates'][0][1] + self._DesignParameter['vss']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1])
		    for i in range(len(self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		        if ((i % 2) == 1):
		            xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['nmos']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['nmos']['_XYCoordinates'][0][1])], self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		elif (mode == 'horizontal'):
		    xy_with_offset = []
		    target_x_value = (self._DesignParameter['vss']['_XYCoordinates'][0][0] + self._DesignParameter['vss']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0])
		    for i in range(len(self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		        if ((i % 2) == 1):
		            xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['nmos']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['nmos']['_XYCoordinates'][0][1])], self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		self._DesignParameter['nmos_supply_routing'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=_width)
		self._DesignParameter['nmos_supply_routing']['_XYCoordinates'] = path_list
		self._DesignParameter['RVT_boundary_0'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['RVT'][0], _Datatype=DesignParameters._LayerMapping['RVT'][1], _XWidth=self._DesignParameter['vdd']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth'], _YWidth=((self._DesignParameter['vdd']['_XYCoordinates'][0][1] + self._DesignParameter['vdd']['_DesignObj']._DesignParameter['_Met2Layer']['_XYCoordinates'][0][1]) - (self._DesignParameter['vss']['_XYCoordinates'][0][1] + self._DesignParameter['vss']['_DesignObj']._DesignParameter['_Met2Layer']['_XYCoordinates'][0][1])))
		self._DesignParameter['RVT_boundary_0']['_XYCoordinates'] = [[self._DesignParameter['vss']['_XYCoordinates'][0][0], (((self._DesignParameter['vdd']['_XYCoordinates'][0][1] + self._DesignParameter['vdd']['_DesignObj']._DesignParameter['_Met2Layer']['_XYCoordinates'][0][1]) + (self._DesignParameter['vss']['_XYCoordinates'][0][1] + self._DesignParameter['vss']['_DesignObj']._DesignParameter['_Met2Layer']['_XYCoordinates'][0][1])) / 2)]]
		self._DesignParameter['gate_input_routing_1'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _Width=50)
		self._DesignParameter['gate_input_routing_1']['_XYCoordinates'] = [[[((self._DesignParameter['gate_input']['_XYCoordinates'][0][0] + self._DesignParameter['gate_input']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['gate_input']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)), (((self._DesignParameter['gate_input']['_XYCoordinates'][0][1] + self._DesignParameter['gate_input']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1]) - (self._DesignParameter['gate_input']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2)) + (self._DesignParameter['gate_input_routing_1']['_Width'] / 2))], [(self._DesignParameter['poly_gate_nmos_xy']['_XYCoordinates'][(- 1)][0][0] + (self._DesignParameter['poly_gate_nmos_xy']['_Width'] / 2)), (((self._DesignParameter['gate_input']['_XYCoordinates'][0][1] + self._DesignParameter['gate_input']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1]) - (self._DesignParameter['gate_input']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2)) + (self._DesignParameter['gate_input_routing_1']['_Width'] / 2))]]]
		self._DesignParameter['nwell_layer'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['NWELL'][0], _Datatype=DesignParameters._LayerMapping['NWELL'][1], _XWidth=(self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth'] + (2 * drc._NwMinEnclosurePactive2)), _YWidth=(((self._DesignParameter['vdd']['_XYCoordinates'][0][1] + self._DesignParameter['vdd']['_DesignObj']._DesignParameter['_Met2Layer']['_XYCoordinates'][0][1]) + (self._DesignParameter['vdd']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] / 2)) - self._DesignParameter['gate_input']['_XYCoordinates'][0][1]))
		self._DesignParameter['nwell_layer']['_XYCoordinates'] = [[self._DesignParameter['vss']['_XYCoordinates'][0][0], ((((self._DesignParameter['vdd']['_XYCoordinates'][0][1] + self._DesignParameter['vdd']['_DesignObj']._DesignParameter['_Met2Layer']['_XYCoordinates'][0][1]) + (self._DesignParameter['vdd']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] / 2)) + self._DesignParameter['gate_input']['_XYCoordinates'][0][1]) / 2)]]
		path_list = []
		if (len(self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates']) == 1):
		    mode = 'vertical'
		    _width = self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth']
		elif (self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][0] == self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][0]):
		    mode = 'horizontal'
		    _width = self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth']
		elif (self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1] == self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][1]):
		    mode = 'vertical'
		    _width = self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth']
		else:
		    print('Invalid Target Input')
		if (mode == 'vertical'):
		    xy_with_offset = []
		    target_y_value = (self._DesignParameter['gate_input']['_XYCoordinates'][0][1] + self._DesignParameter['gate_input']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1])
		    for i in range(len(self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		        if ((i % 2) == 1):
		            xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['pmos']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['pmos']['_XYCoordinates'][0][1])], self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		elif (mode == 'horizontal'):
		    xy_with_offset = []
		    target_x_value = (self._DesignParameter['gate_input']['_XYCoordinates'][0][0] + self._DesignParameter['gate_input']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0])
		    for i in range(len(self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		        if ((i % 2) == 1):
		            xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['pmos']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['pmos']['_XYCoordinates'][0][1])], self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		self._DesignParameter['m1_pmos_drain_gate_routing_x'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=_width)
		self._DesignParameter['m1_pmos_drain_gate_routing_x']['_XYCoordinates'] = path_list
		self._DesignParameter['m1_pmos_drain_routing_x'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=self._DesignParameter['m1_pmos_drain_gate_routing_x']['_Width'])
		self._DesignParameter['m1_pmos_drain_routing_x']['_XYCoordinates'] = [[[(self._DesignParameter['m1_pmos_drain_gate_routing_x']['_XYCoordinates'][0][0][0] - (self._DesignParameter['m1_pmos_drain_gate_routing_x']['_Width'] / 2)), (self._DesignParameter['gate_input']['_XYCoordinates'][0][1] + self._DesignParameter['gate_input']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1])], [(self._DesignParameter['m1_pmos_drain_gate_routing_x']['_XYCoordinates'][(- 1)][0][0] + (self._DesignParameter['m1_pmos_drain_gate_routing_x']['_Width'] / 2)), (self._DesignParameter['gate_input']['_XYCoordinates'][0][1] + self._DesignParameter['gate_input']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1])]]]
		self._DesignParameter['m1_drain_routing_x'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth'])
		self._DesignParameter['m1_drain_routing_x']['_XYCoordinates'] = [[[(self._DesignParameter['gate_input']['_XYCoordinates'][0][0] - (self._DesignParameter['m1_drain_routing_x']['_Width'] / 2)), ((((self._DesignParameter['nmos']['_XYCoordinates'][0][1] + self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1]) + (self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_YWidth'] / 2)) + (self._DesignParameter['m1_drain_routing_x']['_Width'] / 2)) + drc._Metal1MinSpace2)], [((self._DesignParameter['nmos']['_XYCoordinates'][0][0] + self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][(- 1)][0]) + (self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth'] / 2)), ((((self._DesignParameter['nmos']['_XYCoordinates'][0][1] + self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1]) + (self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_YWidth'] / 2)) + (self._DesignParameter['m1_drain_routing_x']['_Width'] / 2)) + drc._Metal1MinSpace2)]]]
		path_list = []
		if (len(self._DesignParameter['gate_input']['_XYCoordinates']) == 1):
		    mode = 'vertical'
		    _width = self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth']
		elif (self._DesignParameter['gate_input']['_XYCoordinates'][0][0] == self._DesignParameter['gate_input']['_XYCoordinates'][(- 1)][0]):
		    mode = 'horizontal'
		    _width = self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth']
		elif (self._DesignParameter['gate_input']['_XYCoordinates'][0][1] == self._DesignParameter['gate_input']['_XYCoordinates'][(- 1)][1]):
		    mode = 'vertical'
		    _width = self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth']
		else:
		    print('Invalid Target Input')
		if (mode == 'vertical'):
		    xy_with_offset = []
		    target_y_value = (0 + self._DesignParameter['m1_drain_routing_x']['_XYCoordinates'][0][0][1])
		    for i in range(len(self._DesignParameter['gate_input']['_XYCoordinates'])):
		        xy_with_offset.append([(x + y) for (x, y) in zip([0, 0], self._DesignParameter['gate_input']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		elif (mode == 'horizontal'):
		    xy_with_offset = []
		    target_x_value = (0 + self._DesignParameter['m1_drain_routing_x']['_XYCoordinates'][0][0][0])
		    for i in range(len(self._DesignParameter['gate_input']['_XYCoordinates'])):
		        xy_with_offset.append([(x + y) for (x, y) in zip([0, 0], self._DesignParameter['gate_input']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		self._DesignParameter['m1_drain_gate'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=_width)
		self._DesignParameter['m1_drain_gate']['_XYCoordinates'] = path_list
		path_list = []
		if (len(self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates']) == 1):
		    mode = 'vertical'
		    _width = self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth']
		elif (self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][0] == self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][0]):
		    mode = 'horizontal'
		    _width = self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth']
		elif (self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1] == self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][1]):
		    mode = 'vertical'
		    _width = self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth']
		else:
		    print('Invalid Target Input')
		if (mode == 'vertical'):
		    xy_with_offset = []
		    target_y_value = (0 + self._DesignParameter['m1_drain_routing_x']['_XYCoordinates'][0][0][1])
		    for i in range(len(self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		        if ((i % 2) == 0):
		            xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['nmos']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['nmos']['_XYCoordinates'][0][1])], self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		elif (mode == 'horizontal'):
		    xy_with_offset = []
		    target_x_value = (0 + self._DesignParameter['m1_drain_routing_x']['_XYCoordinates'][0][0][0])
		    for i in range(len(self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		        if ((i % 2) == 0):
		            xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['nmos']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['nmos']['_XYCoordinates'][0][1])], self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		self._DesignParameter['m1_drain_routing_y'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=_width)
		self._DesignParameter['m1_drain_routing_y']['_XYCoordinates'] = path_list
		path_list = []
		if (len(self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates']) == 1):
		    mode = 'vertical'
		    _width = self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
		elif (self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0] == self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]):
		    mode = 'horizontal'
		    _width = self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
		elif (self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1] == self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][1]):
		    mode = 'vertical'
		    _width = self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
		else:
		    print('Invalid Target Input')
		if (mode == 'vertical'):
		    xy_with_offset = []
		    target_y_value = ((self._DesignParameter['gate_input']['_XYCoordinates'][0][1] + self._DesignParameter['gate_input']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1]) + (self._DesignParameter['gate_input']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2))
		    for i in range(len(self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
		        xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['pmos']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['pmos']['_XYCoordinates'][0][1])], self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		elif (mode == 'horizontal'):
		    xy_with_offset = []
		    target_x_value = (self._DesignParameter['gate_input']['_XYCoordinates'][0][0] + self._DesignParameter['gate_input']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0])
		    for i in range(len(self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
		        xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['pmos']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['pmos']['_XYCoordinates'][0][1])], self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		self._DesignParameter['gate_input_pmos'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _Width=_width)
		self._DesignParameter['gate_input_pmos']['_XYCoordinates'] = path_list
		self._DesignParameter['gate_input_routing_2'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _Width=50)
		self._DesignParameter['gate_input_routing_2']['_XYCoordinates'] = [[[((self._DesignParameter['gate_input']['_XYCoordinates'][0][0] + self._DesignParameter['gate_input']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['gate_input']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)), (((self._DesignParameter['gate_input']['_XYCoordinates'][0][1] + self._DesignParameter['gate_input']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1]) + (self._DesignParameter['gate_input']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2)) - (self._DesignParameter['gate_input_routing_2']['_Width'] / 2))], [(self._DesignParameter['gate_input_pmos']['_XYCoordinates'][(- 1)][0][0] + (self._DesignParameter['gate_input_pmos']['_Width'] / 2)), (((self._DesignParameter['gate_input']['_XYCoordinates'][0][1] + self._DesignParameter['gate_input']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1]) + (self._DesignParameter['gate_input']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2)) - (self._DesignParameter['gate_input_routing_2']['_Width'] / 2))]]]
		