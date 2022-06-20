from generatorLib import StickDiagram
from generatorLib import DesignParameters
import copy
import math
from generatorLib import DRC
from generatorLib import CoordinateCalc as CoordCalc
from generatorLib.generator_models import ViaPoly2Met1
from generatorLib.generator_models import ViaMet12Met2
from generatorLib.generator_models import NMOSWithDummy
from generatorLib.generator_models import PMOSWithDummy
from generatorLib.generator_models import Z_PWR_CNT

class Transmission_gate(StickDiagram._StickDiagram):
	def __init__(self, _DesignParameter=None, _Name='Transmission_gate'):
		if _DesignParameter != None:
			self._DesignParameter = _DesignParameter
		else:
			self._DesignParameter = dict(_Name=self._NameDeclaration(_Name=_Name), _GDSFile=self._GDSObjDeclaration(_GDSFile=None))
		self._DesignParameter['_Name']['Name'] = _Name

	def _CalculateDesignParameter(self,nmos_gate=3,pmos_gate=3,nmos_width=320,pmos_width=584,length=30,XVT='SLVT',vss2nmos=350,vdd2pmos=433,gate_y=860,vss2vdd_height=1800,gate_spacing=100,sdwidth=66,power_xdistance=130, out_even_up_mode=True):

		drc = DRC.DRC()
		_Name = self._DesignParameter['_Name']['_Name']

		MinSnapSpacing = drc._MinSnapSpacing

		self._DesignParameter['nmos'] = self._SrefElementDeclaration(_DesignObj=NMOSWithDummy._NMOS(_Name='nmosIn{}'.format(_Name)))[0]
		self._DesignParameter['nmos']['_DesignObj']._CalculateNMOSDesignParameter(**dict(_NMOSNumberofGate=nmos_gate, _NMOSChannelWidth=nmos_width, _NMOSChannellength=length, _NMOSDummy=True, _GateSpacing=gate_spacing, _SDWidth=sdwidth, _XVT=XVT))
		self._DesignParameter['pmos'] = self._SrefElementDeclaration(_DesignObj=PMOSWithDummy._PMOS(_Name='pmosIn{}'.format(_Name)))[0]
		self._DesignParameter['pmos']['_DesignObj']._CalculatePMOSDesignParameter(**dict(_PMOSNumberofGate=pmos_gate, _PMOSChannelWidth=pmos_width, _PMOSChannellength=length, _PMOSDummy=True, _GateSpacing=gate_spacing, _SDWidth=sdwidth, _XVT=XVT))

		if self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_PODummyLayer']['_XWidth']*self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_PODummyLayer']['_YWidth'] < drc._PODummyMinArea :
			self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_PODummyLayer']['_YWidth']=drc._PODummyMinArea//self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_PODummyLayer']['_XWidth']+2*MinSnapSpacing

		if self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_PODummyLayer']['_XWidth']*self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_PODummyLayer']['_YWidth'] < drc._PODummyMinArea :
			self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_PODummyLayer']['_YWidth']=drc._PODummyMinArea//self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_PODummyLayer']['_XWidth']+2*MinSnapSpacing

		if power_xdistance == None :
			power_xdistance=self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][1][0]-self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0]

		self._DesignParameter['vss'] = self._SrefElementDeclaration(_DesignObj=Z_PWR_CNT.Z_PWR_CNT(_Name='vssIn{}'.format(_Name)))[0]
		self._DesignParameter['vss']['_DesignObj']._CalculateDesignParameter(**dict(_Xnum=(nmos_gate + 1), _Xdistance=power_xdistance))
		self._DesignParameter['vss']['_XYCoordinates'] = [[0, 0]]
		self._DesignParameter['vdd'] = self._SrefElementDeclaration(_DesignObj=Z_PWR_CNT.Z_PWR_CNT(_Name='vddIn{}'.format(_Name)))[0]
		self._DesignParameter['vdd']['_DesignObj']._CalculateDesignParameter(**dict(_Xnum=(pmos_gate + 1), _Xdistance=power_xdistance))
		self._DesignParameter['vdd']['_XYCoordinates'] = [[0, vss2vdd_height]]

		if vss2nmos == None :
			vss2nmos=self._DesignParameter['vss']['_XYCoordinates'][0][1]+max(self._DesignParameter['vss']['_DesignObj']._DesignParameter['METAL1_boundary_0']['_YWidth'], self._DesignParameter['vss']['_DesignObj']._DesignParameter['METAL1_boundary_1']['_YWidth'])/2+self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']/2+drc._Metal1MinSpace3

		self._DesignParameter['nmos']['_XYCoordinates'] = [[self._DesignParameter['vss']['_XYCoordinates'][0][0], vss2nmos]]

		if vdd2pmos == None :
			vdd2pmos=max(self._DesignParameter['vss']['_DesignObj']._DesignParameter['METAL1_boundary_0']['_YWidth'],self._DesignParameter['vdd']['_DesignObj']._DesignParameter['METAL1_boundary_1']['_YWidth'])/2+self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']/2+drc._Metal1MinSpace3

		self._DesignParameter['pmos']['_XYCoordinates'] = [[self._DesignParameter['vdd']['_XYCoordinates'][0][0], (vss2vdd_height - vdd2pmos)]]
		self._DesignParameter['pmos_second_podummy'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _XWidth=length, _YWidth=self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_PODummyLayer']['_YWidth'])
		self._DesignParameter['pmos_second_podummy']['_XYCoordinates'] = [[((((self._DesignParameter['pmos']['_XYCoordinates'][0][0] + self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][(- 1)][0]) + (self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_PODummyLayer']['_XWidth'] / 2)) + (self._DesignParameter['pmos_second_podummy']['_XWidth'] / 2)) + gate_spacing), self._DesignParameter['pmos']['_XYCoordinates'][0][1]], [((((self._DesignParameter['pmos']['_XYCoordinates'][0][0] + self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_PODummyLayer']['_XWidth'] / 2)) - (self._DesignParameter['pmos_second_podummy']['_XWidth'] / 2)) - gate_spacing), self._DesignParameter['pmos']['_XYCoordinates'][0][1]]]
		self._DesignParameter['nmos_second_podummy'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _XWidth=length, _YWidth=self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_PODummyLayer']['_YWidth'])
		self._DesignParameter['nmos_second_podummy']['_XYCoordinates'] = [[((((self._DesignParameter['nmos']['_XYCoordinates'][0][0] + self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_PODummyLayer']['_XWidth'] / 2)) - (self._DesignParameter['nmos_second_podummy']['_XWidth'] / 2)) - gate_spacing), self._DesignParameter['nmos']['_XYCoordinates'][0][1]], [((((self._DesignParameter['nmos']['_XYCoordinates'][0][0] + self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][(- 1)][0]) + (self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_PODummyLayer']['_XWidth'] / 2)) + (self._DesignParameter['nmos_second_podummy']['_XWidth'] / 2)) + gate_spacing), self._DesignParameter['nmos']['_XYCoordinates'][0][1]]]
		self._DesignParameter['vss_odlayer'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['DIFF'][0], _Datatype=DesignParameters._LayerMapping['DIFF'][1], _XWidth=((self._DesignParameter['nmos_second_podummy']['_XYCoordinates'][-1][0] - self._DesignParameter['nmos_second_podummy']['_XYCoordinates'][0][0]) + self._DesignParameter['nmos_second_podummy']['_XWidth']), _YWidth=(2 * drc._CoMinWidth))
		self._DesignParameter['vss_odlayer']['_XYCoordinates'] = [[self._DesignParameter['vss']['_XYCoordinates'][0][0], self._DesignParameter['vss']['_XYCoordinates'][0][1]]]
		self._DesignParameter['vss_supply_m2_y'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _XWidth=self._DesignParameter['vss_odlayer']['_XWidth'], _YWidth=6*drc._MetalxMinWidth)
		self._DesignParameter['vss_supply_m2_y']['_XYCoordinates'] = [[(+ self._DesignParameter['vss_odlayer']['_XYCoordinates'][0][0]), (+ self._DesignParameter['vss_odlayer']['_XYCoordinates'][0][1])]]
		self._DesignParameter['vdd_odlayer'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['DIFF'][0], _Datatype=DesignParameters._LayerMapping['DIFF'][1], _XWidth=((self._DesignParameter['pmos_second_podummy']['_XYCoordinates'][0][0] - self._DesignParameter['pmos_second_podummy']['_XYCoordinates'][(- 1)][0]) - self._DesignParameter['pmos_second_podummy']['_XWidth']), _YWidth=(2 * drc._CoMinWidth))
		self._DesignParameter['vdd_odlayer']['_XYCoordinates'] = [[self._DesignParameter['vss_odlayer']['_XYCoordinates'][0][0], self._DesignParameter['vdd']['_XYCoordinates'][0][1]]]
		self._DesignParameter['vdd_supply_m2_y'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _XWidth=self._DesignParameter['vdd_odlayer']['_XWidth'], _YWidth=6*drc._MetalxMinWidth)
		self._DesignParameter['vdd_supply_m2_y']['_XYCoordinates'] = [[(+ self._DesignParameter['vdd_odlayer']['_XYCoordinates'][0][0]), (+ self._DesignParameter['vdd_odlayer']['_XYCoordinates'][0][1])]]
		self._DesignParameter['gate_input'] = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_Name='gate_inputIn{}'.format(_Name)))[0]
		self._DesignParameter['gate_input']['_DesignObj']._CalculateViaPoly2Met1DesignParameterMinimumEnclosureX(**dict(_ViaPoly2Met1NumberOfCOX=1, _ViaPoly2Met1NumberOfCOY=2))

		if gate_y == None :
			gate_y=((self._DesignParameter['pmos_second_podummy']['_XYCoordinates'][0][1]-self._DesignParameter['pmos_second_podummy']['_YWidth']/2)+(self._DesignParameter['nmos_second_podummy']['_XYCoordinates'][0][1]+self._DesignParameter['nmos_second_podummy']['_YWidth']/2))/2

		self._DesignParameter['gate_input']['_XYCoordinates'] = [[(min((self._DesignParameter['nmos_second_podummy']['_XYCoordinates'][0][0] + (self._DesignParameter['nmos']['_XYCoordinates'][0][0] + self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][0])), (self._DesignParameter['pmos_second_podummy']['_XYCoordinates'][(- 1)][0] + (self._DesignParameter['pmos']['_XYCoordinates'][0][0] + self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][0]))) / 2), gate_y]]
		self._DesignParameter['gate_output'] = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_Name='gate_outputIn{}'.format(_Name)))[0]
		self._DesignParameter['gate_output']['_DesignObj']._CalculateViaPoly2Met1DesignParameterMinimumEnclosureX(**dict(_ViaPoly2Met1NumberOfCOX=1, _ViaPoly2Met1NumberOfCOY=2))
		self._DesignParameter['gate_output']['_XYCoordinates'] = [[(max((self._DesignParameter['nmos_second_podummy']['_XYCoordinates'][(- 1)][0] + (self._DesignParameter['nmos']['_XYCoordinates'][0][0] + self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][(- 1)][0])), (self._DesignParameter['pmos_second_podummy']['_XYCoordinates'][0][0] + (self._DesignParameter['pmos']['_XYCoordinates'][0][0] + self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][(- 1)][0]))) / 2), self._DesignParameter['gate_input']['_XYCoordinates'][0][1]]]
		self._DesignParameter['pmos_poly_gate_routing_x'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _Width=50)
		self._DesignParameter['pmos_poly_gate_routing_x']['_XYCoordinates'] = [[[((self._DesignParameter['gate_input']['_XYCoordinates'][0][0] + self._DesignParameter['gate_input']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['gate_input']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)), (((self._DesignParameter['gate_input']['_XYCoordinates'][0][1] + self._DesignParameter['gate_input']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1]) + (self._DesignParameter['gate_input']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2)))], [((self._DesignParameter['pmos']['_XYCoordinates'][0][0] + self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]) + (self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)), (((self._DesignParameter['gate_input']['_XYCoordinates'][0][1] + self._DesignParameter['gate_input']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1]) + (self._DesignParameter['gate_input']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2)))]]]
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
		    target_y_value = (0 + self._DesignParameter['pmos_poly_gate_routing_x']['_XYCoordinates'][0][0][1])
		    for i in range(len(self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
		        xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['pmos']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['pmos']['_XYCoordinates'][0][1])], self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		elif (mode == 'horizontal'):
		    xy_with_offset = []
		    target_x_value = (0 + self._DesignParameter['pmos_poly_gate_routing_x']['_XYCoordinates'][0][0][0])
		    for i in range(len(self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
		        xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['pmos']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['pmos']['_XYCoordinates'][0][1])], self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		self._DesignParameter['pmos_poly_gate_routing_y'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _Width=_width)
		self._DesignParameter['pmos_poly_gate_routing_y']['_XYCoordinates'] = path_list
		self._DesignParameter['nmos_poly_gate_routing_x'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _Width=50)
		self._DesignParameter['nmos_poly_gate_routing_x']['_XYCoordinates'] = [[[((self._DesignParameter['nmos']['_XYCoordinates'][0][0] + self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)), (((self._DesignParameter['gate_output']['_XYCoordinates'][0][1] + self._DesignParameter['gate_output']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1]) - (self._DesignParameter['gate_output']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2)))], [((self._DesignParameter['gate_output']['_XYCoordinates'][0][0] + self._DesignParameter['gate_output']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0] + self._DesignParameter['gate_output']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)), (((self._DesignParameter['gate_output']['_XYCoordinates'][0][1] + self._DesignParameter['gate_output']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1]) - (self._DesignParameter['gate_output']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2)))]]]
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
		    target_y_value = (0 + self._DesignParameter['nmos_poly_gate_routing_x']['_XYCoordinates'][0][0][1])
		    for i in range(len(self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
		        xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['nmos']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['nmos']['_XYCoordinates'][0][1])], self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		elif (mode == 'horizontal'):
		    xy_with_offset = []
		    target_x_value = (0 + self._DesignParameter['nmos_poly_gate_routing_x']['_XYCoordinates'][0][0][0])
		    for i in range(len(self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
		        xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['nmos']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['nmos']['_XYCoordinates'][0][1])], self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		self._DesignParameter['nmos_poly_gate_routing_y'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _Width=_width)
		self._DesignParameter['nmos_poly_gate_routing_y']['_XYCoordinates'] = path_list
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
		    target_y_value = (0 + self._DesignParameter['nmos']['_XYCoordinates'][0][1])
		    for i in range(len(self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		        if ((i % 2) == 0):
		            xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['pmos']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['pmos']['_XYCoordinates'][0][1])], self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		elif (mode == 'horizontal'):
		    xy_with_offset = []
		    target_x_value = (0 + self._DesignParameter['nmos']['_XYCoordinates'][0][0])
		    for i in range(len(self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		        if ((i % 2) == 0):
		            xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['pmos']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['pmos']['_XYCoordinates'][0][1])], self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		self._DesignParameter['m1_source_routing_y'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=_width)
		self._DesignParameter['m1_source_routing_y']['_XYCoordinates'] = path_list
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
		    target_y_value = (0 + self._DesignParameter['pmos']['_XYCoordinates'][0][1])
		    for i in range(len(self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		        if ((i % 2) == 1):
		            xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['nmos']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['nmos']['_XYCoordinates'][0][1])], self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		elif (mode == 'horizontal'):
		    xy_with_offset = []
		    target_x_value = (0 + self._DesignParameter['pmos']['_XYCoordinates'][0][0])
		    for i in range(len(self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		        if ((i % 2) == 1):
		            xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['nmos']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['nmos']['_XYCoordinates'][0][1])], self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		self._DesignParameter['m1_drain_routing_y'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=_width)
		self._DesignParameter['m1_drain_routing_y']['_XYCoordinates'] = path_list


		##modified by 1joon
		assert XVT in ('SLVT', 'LVT', 'RVT', 'HVT')
		self._DesignParameter['XVT_boundary_1'] = self._BoundaryElementDeclaration(
			_Layer=DesignParameters._LayerMapping[XVT][0], _Datatype=DesignParameters._LayerMapping[XVT][1])
		self._DesignParameter['XVT_boundary_1']['_XWidth'] = max((self._DesignParameter['pmos_second_podummy']['_XYCoordinates'][0][0] - self._DesignParameter['pmos_second_podummy']['_XYCoordinates'][(- 1)][0]), (self._DesignParameter['nmos_second_podummy']['_XYCoordinates'][(- 1)][0] - self._DesignParameter['nmos_second_podummy']['_XYCoordinates'][0][0]))
		self._DesignParameter['XVT_boundary_1']['_YWidth'] = (self._DesignParameter['vdd']['_XYCoordinates'][0][1] - self._DesignParameter['vss']['_XYCoordinates'][0][1])
		self._DesignParameter['XVT_boundary_1']['_XYCoordinates'] = [[self._DesignParameter['vss']['_XYCoordinates'][0][0], ((self._DesignParameter['vdd']['_XYCoordinates'][0][1] + self._DesignParameter['vss']['_XYCoordinates'][0][1]) / 2)]]
		##end of modification

		self._DesignParameter['NWELL_boundary_0'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['NWELL'][0], _Datatype=DesignParameters._LayerMapping['NWELL'][1], _XWidth=(max(self._DesignParameter['vdd_odlayer']['_XWidth'], self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth']) + (2 * drc._NwMinEnclosurePactive)), _YWidth=(((self._DesignParameter['vdd_odlayer']['_XYCoordinates'][0][1] + (self._DesignParameter['vdd_odlayer']['_YWidth'] / 2)) + 2*drc._NwMinEnclosurePactive2) - ((self._DesignParameter['gate_input']['_XYCoordinates'][0][1] + self._DesignParameter['gate_input']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) - (self._DesignParameter['gate_input']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2))))
		self._DesignParameter['NWELL_boundary_0']['_XYCoordinates'] = [[self._DesignParameter['vss']['_XYCoordinates'][0][0], ((((self._DesignParameter['vdd_odlayer']['_XYCoordinates'][0][1] + (self._DesignParameter['vdd_odlayer']['_YWidth'] / 2)) + 2*drc._NwMinEnclosurePactive2) + ((self._DesignParameter['gate_input']['_XYCoordinates'][0][1] + self._DesignParameter['gate_input']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) - (self._DesignParameter['gate_input']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2))) / 2)]]
		self._DesignParameter['vss_pplayer'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['PIMP'][0], _Datatype=DesignParameters._LayerMapping['PIMP'][1], _XWidth=(self._DesignParameter['vss_odlayer']['_XWidth'] + (2 * drc._PpMinExtensiononPactive)), _YWidth=(self._DesignParameter['vss_odlayer']['_YWidth'] + (2 * drc._PpMinExtensiononPactive)))
		self._DesignParameter['vss_pplayer']['_XYCoordinates'] = [[(+ self._DesignParameter['vss_odlayer']['_XYCoordinates'][0][0]), (+ self._DesignParameter['vss_odlayer']['_XYCoordinates'][0][1])]]


		if out_even_up_mode == True :
			_ViaOnPMOSOutput = copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation)
			_tmpNumCoX = 1
			_tmpNumCoY = max(1, int(self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / (drc._VIAxMinWidth + drc._VIAxMinSpace)))
			_ViaOnPMOSOutput['_ViaMet12Met2NumberOfCOX'] = _tmpNumCoX
			_ViaOnPMOSOutput['_ViaMet12Met2NumberOfCOY'] = _tmpNumCoY

			self._DesignParameter['output1']=self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='output1In{}'.format(_Name)))[0]
			self._DesignParameter['output1']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(**_ViaOnPMOSOutput)
			del _ViaOnPMOSOutput

			tmp=[]
			for i in range(0, pmos_gate//2 + 1) :
				tmp.append([self._DesignParameter['pmos']['_XYCoordinates'][0][0]+self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_XYCoordinatePMOSSupplyRouting']['_XYCoordinates'][i][0], self._DesignParameter['pmos']['_XYCoordinates'][0][1]])

			self._DesignParameter['output1']['_XYCoordinates']=tmp
			del tmp

			_ViaOnNMOSOutput = copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation)
			_tmpNumCoX = 1
			_tmpNumCoY = max(1, int(self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / (drc._VIAxMinWidth + drc._VIAxMinSpace)))
			_ViaOnNMOSOutput['_ViaMet12Met2NumberOfCOX'] = _tmpNumCoX
			_ViaOnNMOSOutput['_ViaMet12Met2NumberOfCOY'] = _tmpNumCoY

			self._DesignParameter['output2'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='output2In{}'.format(_Name)))[0]
			self._DesignParameter['output2']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(**_ViaOnNMOSOutput)
			del _ViaOnNMOSOutput

			tmp = []
			for i in range(0, (nmos_gate+1) // 2):
				tmp.append([self._DesignParameter['nmos']['_XYCoordinates'][0][0] + self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][i][0], self._DesignParameter['nmos']['_XYCoordinates'][0][1]])

			self._DesignParameter['output2']['_XYCoordinates'] = tmp
			del tmp

		elif out_even_up_mode == False :
			_ViaOnNMOSOutput = copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation)
			_tmpNumCoX = 1
			_tmpNumCoY = max(2, int(self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / (drc._VIAxMinWidth + drc._VIAxMinSpace)))
			_ViaOnNMOSOutput['_ViaMet12Met2NumberOfCOX'] = _tmpNumCoX
			_ViaOnNMOSOutput['_ViaMet12Met2NumberOfCOY'] = _tmpNumCoY

			self._DesignParameter['output1']=self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='output1In{}'.format(_Name)))[0]
			self._DesignParameter['output1']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(**_ViaOnNMOSOutput)
			del _ViaOnNMOSOutput

			tmp=[]
			for i in range(0, nmos_gate//2 + 1) :
				tmp.append([self._DesignParameter['nmos']['_XYCoordinates'][0][0]+self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][i][0], self._DesignParameter['nmos']['_XYCoordinates'][0][1]+self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']/2-self._DesignParameter['output1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']/2])

			self._DesignParameter['output1']['_XYCoordinates']=tmp
			del tmp

			_ViaOnPMOSOutput = copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation)
			_tmpNumCoX = 1
			_tmpNumCoY = max(2, int(self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / (drc._VIAxMinWidth + drc._VIAxMinSpace)))
			_ViaOnPMOSOutput['_ViaMet12Met2NumberOfCOX'] = _tmpNumCoX
			_ViaOnPMOSOutput['_ViaMet12Met2NumberOfCOY'] = _tmpNumCoY

			self._DesignParameter['output2'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='output2In{}'.format(_Name)))[0]
			self._DesignParameter['output2']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(**_ViaOnPMOSOutput)
			del _ViaOnPMOSOutput

			tmp = []
			for i in range(0, (pmos_gate+1) // 2):
				tmp.append([self._DesignParameter['pmos']['_XYCoordinates'][0][0] + self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][i][0], self._DesignParameter['pmos']['_XYCoordinates'][0][1]-self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']/2+self._DesignParameter['output2']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']/2])

			self._DesignParameter['output2']['_XYCoordinates'] = tmp
			del tmp

		rightBoundary = self.getXYRight('output2', '_Met2Layer')[-1][0]
		leftBoundary = self.getXYLeft('output2', '_Met2Layer')[0][0]
		if len(self._DesignParameter['output2']['_XYCoordinates']) != 1 :
			self._DesignParameter['m2_output2_routing_x'] = self._BoundaryElementDeclaration(
				_Layer=DesignParameters._LayerMapping['METAL2'][0],
				_Datatype=DesignParameters._LayerMapping['METAL2'][1],
				_XWidth=rightBoundary-leftBoundary,
				_YWidth=sdwidth,
				_XYCoordinates=[[(rightBoundary + leftBoundary) / 2, self.getXY('output2')[0][1]]]
			)


		rightBoundary = self.getXYRight('output1', '_Met2Layer')[-1][0]
		leftBoundary = self.getXYLeft('output1', '_Met2Layer')[0][0]
		if len(self._DesignParameter['output1']['_XYCoordinates']) != 1 :
			self._DesignParameter['m2_output1_routing_x'] = self._BoundaryElementDeclaration(
				_Layer=DesignParameters._LayerMapping['METAL2'][0],
				_Datatype=DesignParameters._LayerMapping['METAL2'][1],
				_XWidth=rightBoundary - leftBoundary,
				_YWidth=sdwidth,
				_XYCoordinates=[[(rightBoundary + leftBoundary) / 2, self.getXY('output1')[0][1]]]
			)


		self._DesignParameter['_AddtionalMetal1onNMOS']=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1],_XWidth=None,_YWidth=None)
		self._DesignParameter['_AddtionalMetal1onNMOS']['_XWidth']=max(self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'],self._DesignParameter['output1']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'])
		self._DesignParameter['_AddtionalMetal1onNMOS']['_YWidth']=max(self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'],min(self._DesignParameter['output1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'], self._DesignParameter['output2']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']))

		self._DesignParameter['_AddtionalMetal1onPMOS']=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1],_XWidth=None,_YWidth=None)
		self._DesignParameter['_AddtionalMetal1onPMOS']['_XWidth']=max(self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'],self._DesignParameter['output1']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'])
		self._DesignParameter['_AddtionalMetal1onPMOS']['_YWidth']=max(self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'],max(self._DesignParameter['output1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'], self._DesignParameter['output2']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']))

		tmp1=[]
		tmp2=[]

		for i in range(0, len(self._DesignParameter['output1']['_XYCoordinates'])):
			if out_even_up_mode==True:
				tmp1=self._DesignParameter['output2']['_XYCoordinates']
				tmp2=self._DesignParameter['output1']['_XYCoordinates']

			elif out_even_up_mode==False:
				tmp1=self._DesignParameter['output1']['_XYCoordinates']
				tmp2=self._DesignParameter['output2']['_XYCoordinates']

		self._DesignParameter['_AddtionalMetal1onNMOS']['_XYCoordinates']=tmp1
		self._DesignParameter['_AddtionalMetal1onPMOS']['_XYCoordinates']=tmp2

		if len(self._DesignParameter['output2']['_XYCoordinates']) == 1 :
			self._DesignParameter['output2']['_XYCoordinates']=[]
		if len(self._DesignParameter['output1']['_XYCoordinates']) == 1 :
			self._DesignParameter['output1']['_XYCoordinates']=[]


		if out_even_up_mode == True:
			self._DesignParameter['output_nm'] = self._DesignParameter.pop('output2')
			self._DesignParameter['output_pm'] = self._DesignParameter.pop('output1')
			if len(self._DesignParameter['output_nm']['_XYCoordinates']) != 1 and len(self._DesignParameter['output_nm']['_XYCoordinates']) != 0 :
				self._DesignParameter['m2_output_nm_routing_x'] = self._DesignParameter.pop('m2_output2_routing_x')
			if len(self._DesignParameter['output_pm']['_XYCoordinates']) != 1 and len(self._DesignParameter['output_pm']['_XYCoordinates']) != 0 :
				self._DesignParameter['m2_output_pm_routing_x'] = self._DesignParameter.pop('m2_output1_routing_x')
		else:
			self._DesignParameter['output_nm'] = self._DesignParameter.pop('output1')
			self._DesignParameter['output_pm'] = self._DesignParameter.pop('output2')
			if len(self._DesignParameter['output_nm']['_XYCoordinates']) != 1 and len(self._DesignParameter['output_nm']['_XYCoordinates']) != 0 :
				self._DesignParameter['m2_output_nm_routing_x'] = self._DesignParameter.pop('m2_output1_routing_x')
			if len(self._DesignParameter['output_pm']['_XYCoordinates']) != 1 and len(self._DesignParameter['output_pm']['_XYCoordinates']) != 0 :
				self._DesignParameter['m2_output_pm_routing_x'] = self._DesignParameter.pop('m2_output2_routing_x')


		# CellXWidth
		self.CellXWidth = self.getXY('nmos_second_podummy')[-1][0] - self.getXY('nmos_second_podummy')[0][0]


		self._DesignParameter['_VDDpin'] = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2PIN'][0], _Datatype=DesignParameters._LayerMapping['METAL2PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0], _XYCoordinates=[[0, 0]], _Mag=0.05, _Angle=0, _TEXT='VDD')
		self._DesignParameter['_VSSpin'] = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2PIN'][0], _Datatype=DesignParameters._LayerMapping['METAL2PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0], _XYCoordinates=[[0, 0]], _Mag=0.05, _Angle=0, _TEXT='VSS')
		self._DesignParameter['_ENpin'] = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1PIN'][0], _Datatype=DesignParameters._LayerMapping['METAL1PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0],_XYCoordinates=[[0, 0]], _Mag=0.05, _Angle=0, _TEXT='EN')
		self._DesignParameter['_ENbpin'] = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1PIN'][0], _Datatype=DesignParameters._LayerMapping['METAL1PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0],_XYCoordinates=[[0, 0]], _Mag=0.05, _Angle=0, _TEXT='ENb')
		self._DesignParameter['_Apin'] = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1PIN'][0], _Datatype=DesignParameters._LayerMapping['METAL1PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0],_XYCoordinates=[[0, 0]], _Mag=0.05, _Angle=0, _TEXT='A')
		self._DesignParameter['_Ypin'] = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1PIN'][0], _Datatype=DesignParameters._LayerMapping['METAL1PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0],_XYCoordinates=[[0, 0]], _Mag=0.05, _Angle=0, _TEXT='Y')

		self._DesignParameter['_VDDpin']['_XYCoordinates']=self._DesignParameter['vdd']['_XYCoordinates']
		self._DesignParameter['_VSSpin']['_XYCoordinates']=self._DesignParameter['vss']['_XYCoordinates']
		self._DesignParameter['_ENpin']['_XYCoordinates']=self._DesignParameter['gate_output']['_XYCoordinates']
		self._DesignParameter['_ENbpin']['_XYCoordinates']=self._DesignParameter['gate_input']['_XYCoordinates']
		self._DesignParameter['_Apin']['_XYCoordinates']=[[self._DesignParameter['m1_source_routing_y']['_XYCoordinates'][0][0][0], (self._DesignParameter['m1_source_routing_y']['_XYCoordinates'][0][0][1]+self._DesignParameter['m1_source_routing_y']['_XYCoordinates'][0][1][1])/2]]
		self._DesignParameter['_Ypin']['_XYCoordinates']=[[self._DesignParameter['m1_drain_routing_y']['_XYCoordinates'][0][0][0], (self._DesignParameter['m1_drain_routing_y']['_XYCoordinates'][0][0][1]+self._DesignParameter['m1_drain_routing_y']['_XYCoordinates'][0][1][1])/2]]


	def _CalculateDesignParameter_v2(self, nmgateY=None, pmgateY=None, nmos_gate=3, pmos_gate=3, nmos_width=320, pmos_width=584, length=30, XVT='SLVT', vss2nmos=350, vdd2pmos=433, gate_y=860, vss2vdd_height=1800, gate_spacing=100, sdwidth=66, power_xdistance=130, out_even_up_mode=True):

		drc = DRC.DRC()
		_Name = self._DesignParameter['_Name']['_Name']
		MinSnapSpacing = drc._MinSnapSpacing

		_vss2nmos = 0
		_vdd2pmos = 0
		InputParams = dict(
			nmos_gate=nmos_gate, pmos_gate=pmos_gate, nmos_width=nmos_width, pmos_width=pmos_width,
			length=length, XVT=XVT,
			vss2nmos=_vss2nmos, vdd2pmos=_vdd2pmos, gate_y=gate_y, vss2vdd_height=vss2vdd_height,
			gate_spacing=gate_spacing, sdwidth=sdwidth, power_xdistance=power_xdistance,
			out_even_up_mode=out_even_up_mode
		)
		self._CalculateDesignParameter(**InputParams)

		ObjNMOS = 'nmos'
		ObjPMOS = 'pmos'

		''' Poly Dummy Extension '''
		ObjList = [ObjNMOS, ObjPMOS]
		for Obj in ObjList:
			if '_PODummyLayer' in self._DesignParameter[Obj]['_DesignObj']._DesignParameter:
				Area_Dummy = self.getXWidth(Obj, '_PODummyLayer') * self.getYWidth(Obj, '_PODummyLayer')
				if Area_Dummy < drc._PODummyMinArea:
					YWidth_Dummy_Recalc = self.CeilMinSnapSpacing(drc._PODummyMinArea / self.getXWidth(Obj, '_PODummyLayer'), MinSnapSpacing * 2)
					self._DesignParameter[Obj]['_DesignObj']._DesignParameter['_PODummyLayer']['_YWidth'] = YWidth_Dummy_Recalc
				else:
					pass
			else:
				pass

		self._DesignParameter['nmos_second_podummy']['_YWidth'] = self.getYWidth(ObjNMOS, '_PODummyLayer')
		self._DesignParameter['pmos_second_podummy']['_YWidth'] = self.getYWidth(ObjPMOS, '_PODummyLayer')


		''' Recalculate YCoordinates of MOSFETs  '''
		# NMOS
		DistanceBtwVSS2NMOS = list()
		DistanceBtwVSS2NMOS.append(0.5 * (self.getYWidth('vss_odlayer') + self.getYWidth(ObjNMOS, '_ODLayer')) + drc._OdMinSpace)
		DistanceBtwVSS2NMOS.append(0.5 * (self.getYWidth('vss_pplayer') + self.getYWidth(ObjNMOS, '_ODLayer')) + drc._OdMinSpace2Pp)
		DistanceBtwVSS2NMOS.append(0.5 * (self.getYWidth('vss_odlayer') + self.getYWidth(ObjNMOS, '_PODummyLayer')) + drc._PolygateMinSpace2OD if '_PODummyLayer' in self._DesignParameter[ObjNMOS]['_DesignObj']._DesignParameter else 0)
		DistanceBtwVSS2NMOS.append(0.5 * (self.getYWidth('vss', 'METAL1_boundary_0') + self.getYWidth(ObjNMOS, '_Met1Layer')) + drc._Metal1MinWidth)
		DistanceBtwVSS2NMOS.append(0.5 * (self.getYWidth('vss_supply_m2_y') + self.getYWidth('output_nm', '_Met2Layer')) + drc._MetalxMinSpace21 if 'output_nm' in self._DesignParameter else 0)
		VSS2NMOS_min = max(DistanceBtwVSS2NMOS)

		if vss2nmos == None:
			YCoordOfNMOS = VSS2NMOS_min
		elif vss2nmos < VSS2NMOS_min:
			raise NotImplementedError(f'vss2nmos={vss2nmos}, But vss2nmos_min={VSS2NMOS_min}')
		else:
			YCoordOfNMOS = vss2nmos
		yShiftOffset = YCoordOfNMOS - self.getXY(ObjNMOS)[0][1]

		ObjList_NMSide = [ObjNMOS, 'nmos_second_podummy', 'm2_output_nm_routing_x', 'output_nm', '_AddtionalMetal1onNMOS']
		for Obj in ObjList_NMSide:
			self._YShiftUp(Obj, yShiftOffset)

		# PMOS
		DistanceBtwVDD2PMOS = list()
		DistanceBtwVDD2PMOS.append(0.5 * (self.getYWidth('vdd_odlayer') + self.getYWidth(ObjPMOS, '_ODLayer')) + drc._OdMinSpace)
		# DistanceBtwVDD2PMOS.append(0.5 * (self.getYWidth('vss_pplayer') + self.getYWidth(ObjPMOS, '_ODLayer')) + drc._OdMinSpace2Pp)
		DistanceBtwVDD2PMOS.append(0.5 * (self.getYWidth('vdd_odlayer') + self.getYWidth(ObjPMOS, '_PODummyLayer')) + drc._PolygateMinSpace2OD if '_PODummyLayer' in self._DesignParameter[ObjPMOS]['_DesignObj']._DesignParameter else 0)
		DistanceBtwVDD2PMOS.append(0.5 * (self.getYWidth('vdd', 'METAL1_boundary_0') + self.getYWidth(ObjPMOS, '_Met1Layer')) + drc._Metal1MinWidth)
		DistanceBtwVDD2PMOS.append(0.5 * (self.getYWidth('vdd_supply_m2_y') + self.getYWidth('output_pm', '_Met2Layer')) + drc._MetalxMinSpace21 if 'output_pm' in self._DesignParameter else 0)
		VDD2PMOS_min = max(DistanceBtwVDD2PMOS)

		if vdd2pmos == None:
			YCoordOfPMOS = vss2vdd_height - VDD2PMOS_min
		elif vdd2pmos > vss2vdd_height - VDD2PMOS_min:
			raise NotImplementedError(f'vdd2pmos={vdd2pmos}, But vdd2pmos_min={vss2vdd_height - VDD2PMOS_min}')
		else:
			YCoordOfPMOS = vss2vdd_height - VDD2PMOS_min
		yShiftOffset = YCoordOfPMOS - self.getXY(ObjPMOS)[0][1]

		ObjList_PMSide = [ObjPMOS, 'pmos_second_podummy', 'm2_output_pm_routing_x', 'output_pm', '_AddtionalMetal1onPMOS']
		for Obj in ObjList_PMSide:
			self._YShiftUp(Obj, yShiftOffset)

		# MOSFET source drain metal1 redraw
		tmpXYs = []
		for XY in self._DesignParameter['m1_drain_routing_y']['_XYCoordinates']:
			tmpXYs.append([[XY[0][0], self.getXY(ObjNMOS)[0][1]], [XY[0][0], self.getXY(ObjPMOS)[0][1]]])
		self._DesignParameter['m1_drain_routing_y']['_XYCoordinates'] = tmpXYs
		tmpXYs = []
		for XY in self._DesignParameter['m1_source_routing_y']['_XYCoordinates']:
			tmpXYs.append([[XY[0][0], self.getXY(ObjNMOS)[0][1]], [XY[0][0], self.getXY(ObjPMOS)[0][1]]])
		self._DesignParameter['m1_source_routing_y']['_XYCoordinates'] = tmpXYs


		''' Gate PolyContact ReCalculation(YCoordinates) '''
		## NM Gate reCalc
		tmpDRC_polyspace = 96
		tmpDRC_PolygateMinSpace2Co3 = 30

		botCO2CenterPCCOM1 = self.getXY('gate_output')[0][1] - CoordCalc.getXYCoords_MinY(self.getXYBot('gate_output', '_COLayer'))[0][1]
		yCoord_MinGate = self.getXYTop('nmos', '_PODummyLayer')[0][1] + tmpDRC_polyspace + tmpDRC_PolygateMinSpace2Co3 + botCO2CenterPCCOM1

		if nmgateY == None:
			_nmgateY = yCoord_MinGate
		elif nmgateY < yCoord_MinGate:
			raise Exception("Invalid Input: nmgateY")
		else:
			_nmgateY = nmgateY

		self._DesignParameter['gate_output']['_XYCoordinates'] = [[self.getXY('gate_output')[0][0], _nmgateY]]

		YCoord_nmos_poly_gate_routing_x = self.getXYTop('nmos', '_PODummyLayer')[0][1] + tmpDRC_polyspace + self.getWidth('nmos_poly_gate_routing_x') / 2
		self._DesignParameter['nmos_poly_gate_routing_x']['_XYCoordinates'] = [[
			[self._DesignParameter['nmos_poly_gate_routing_x']['_XYCoordinates'][0][0][0], YCoord_nmos_poly_gate_routing_x],
			[self._DesignParameter['nmos_poly_gate_routing_x']['_XYCoordinates'][0][1][0], YCoord_nmos_poly_gate_routing_x]
		]]

		tmpXYs = []
		for XYs in self.getXY('nmos', '_POLayer'):
			tmpXYs.append(
				[[XYs[0], XYs[1]], [XYs[0], YCoord_nmos_poly_gate_routing_x]]
			)
		self._DesignParameter['nmos_poly_gate_routing_y']['_XYCoordinates'] = tmpXYs


		## PM Gate reCalc
		topCO2CenterPCCOM1 = CoordCalc.getXYCoords_MaxY(self.getXYTop('gate_input', '_COLayer'))[0][1] - self.getXY('gate_input')[0][1]
		yCoord_MaxGate = self.getXYBot('pmos', '_PODummyLayer')[0][1] - tmpDRC_polyspace - tmpDRC_PolygateMinSpace2Co3 - topCO2CenterPCCOM1

		if pmgateY == None:
			_pmgateY = yCoord_MaxGate
		elif pmgateY > yCoord_MaxGate:
			raise Exception("Invalid Input: pmgateY")
		else:
			_pmgateY = pmgateY

		self._DesignParameter['gate_input']['_XYCoordinates'] = [[self.getXY('gate_input')[0][0], _pmgateY]]

		# YCoord_pmos_poly_gate_routing_x = self.getXYTop('gate_input', '_POLayer')[0][1] - self.getWidth('pmos_poly_gate_routing_x') / 2
		YCoord_pmos_poly_gate_routing_x = self.getXYBot('pmos', '_PODummyLayer')[0][1] - tmpDRC_polyspace - self.getWidth('pmos_poly_gate_routing_x') / 2
		self._DesignParameter['pmos_poly_gate_routing_x']['_XYCoordinates'] = [[
			[self._DesignParameter['pmos_poly_gate_routing_x']['_XYCoordinates'][0][0][0], YCoord_pmos_poly_gate_routing_x],
			[self._DesignParameter['pmos_poly_gate_routing_x']['_XYCoordinates'][0][1][0], YCoord_pmos_poly_gate_routing_x]
		]]

		tmpXYs = []
		for XYs in self.getXY('pmos', '_POLayer'):
			tmpXYs.append(
				[[XYs[0], XYs[1]], [XYs[0], YCoord_pmos_poly_gate_routing_x]]
			)
		self._DesignParameter['pmos_poly_gate_routing_y']['_XYCoordinates'] = tmpXYs


	def _YShiftUp(self, DesignObj, OffsetY):  # Need to Modify when empty
		tmpXYs = []

		if DesignObj in self._DesignParameter:
			for XY in self._DesignParameter[DesignObj]['_XYCoordinates']:
				tmpXYs.append(CoordCalc.Add(XY, [0, OffsetY]))
			self._DesignParameter[DesignObj]['_XYCoordinates'] = tmpXYs
