from generatorLib import StickDiagram
from generatorLib import DesignParameters
import copy
import math
from generatorLib import DRC
from generatorLib.generator_models import ViaPoly2Met1
from generatorLib.generator_models import NMOSWithDummy
from generatorLib.generator_models import PMOSWithDummy
from generatorLib.generator_models import Z_PWR_CNT

class TG_2X_CRIT_SLVT_v1(StickDiagram._StickDiagram):
	def __init__(self, _DesignParameter=None, _Name='TG_2X_CRIT_SLVT_v1'):
		if _DesignParameter != None:
			self._DesignParameter = _DesignParameter
		else:
			self._DesignParameter = dict(_Name=self._NameDeclaration(_Name=_Name), _GDSFile=self._GDSObjDeclaration(_GDSFile=None))
		self._DesignParameter['_Name']['Name'] = _Name

	def _CalculateDesignParameter(self,nmos_gate=3,pmos_gate=3,nmos_width=250,pmos_width=550,length=30,XVT='SLVT',nmos_y=385,pmos_y=500,vss2vdd_height=1800,gate_spacing=100,sdwidth=66,power_xnum=2,power_xdistance=130):
	
		drc = DRC.DRC()
		_Name = self._DesignParameter['_Name']['_Name']
		
		# self._DesignParameter['vss'] = self._SrefElementDeclaration(_DesignObj=Z_PWR_CNT.Z_PWR_CNT(_Name='vssIn{}'.format(_Name)))[0]
		# self._DesignParameter['vss']['_DesignObj']._CalculateDesignParameter(**dict(_Xnum=(nmos_gate + 1), _Xdistance=power_xdistance))
		# self._DesignParameter['vss']['_XYCoordinates'] = [[0, 0]]
		# self._DesignParameter['vdd'] = self._SrefElementDeclaration(_DesignObj=Z_PWR_CNT.Z_PWR_CNT(_Name='vddIn{}'.format(_Name)))[0]
		# self._DesignParameter['vdd']['_DesignObj']._CalculateDesignParameter(**dict(_Xnum=(pmos_gate + 1), _Xdistance=power_xdistance))
		# self._DesignParameter['vdd']['_XYCoordinates'] = [[0, vss2vdd_height]]
		# self._DesignParameter['slvtnfet_b_CDNS_637732429400_0'] = self._SrefElementDeclaration(_DesignObj=NMOSWithDummy._NMOS(_Name='slvtnfet_b_CDNS_637732429400_0In{}'.format(_Name)))[0]
		# self._DesignParameter['slvtnfet_b_CDNS_637732429400_0']['_DesignObj']._CalculateNMOSDesignParameter(**dict(_NMOSNumberofGate=nmos_gate, _NMOSChannelWidth=nmos_width, _NMOSChannellength=length, _NMOSDummy=True, _GateSpacing=gate_spacing, _SDWidth=sdwidth, _XVT=XVT))
		# self._DesignParameter['slvtnfet_b_CDNS_637732429400_0']['_XYCoordinates'] = [[self._DesignParameter['vss']['_XYCoordinates'][0][0], nmos_y]]
		# self._DesignParameter['slvtpfet_b_CDNS_637732429401_0'] = self._SrefElementDeclaration(_DesignObj=PMOSWithDummy._PMOS(_Name='slvtpfet_b_CDNS_637732429401_0In{}'.format(_Name)))[0]
		# self._DesignParameter['slvtpfet_b_CDNS_637732429401_0']['_DesignObj']._CalculatePMOSDesignParameter(**dict(_PMOSNumberofGate=pmos_gate, _PMOSChannelWidth=pmos_width, _PMOSChannellength=length, _PMOSDummy=True, _GateSpacing=gate_spacing, _SDWidth=sdwidth, _XVT=XVT))
		# self._DesignParameter['slvtpfet_b_CDNS_637732429401_0']['_XYCoordinates'] = [[self._DesignParameter['vdd']['_XYCoordinates'][0][0], (vss2vdd_height - pmos_y)]]
		# self._DesignParameter['pmos_second_podummy'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _XWidth=length, _YWidth=self._DesignParameter['slvtpfet_b_CDNS_637732429401_0']['_DesignObj']._DesignParameter['_PODummyLayer']['_YWidth'])
		# self._DesignParameter['pmos_second_podummy']['_XYCoordinates'] = [[((((self._DesignParameter['slvtpfet_b_CDNS_637732429401_0']['_XYCoordinates'][0][0] + self._DesignParameter['slvtpfet_b_CDNS_637732429401_0']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][(- 1)][0]) + (self._DesignParameter['slvtpfet_b_CDNS_637732429401_0']['_DesignObj']._DesignParameter['_PODummyLayer']['_XWidth'] / 2)) + (self._DesignParameter['pmos_second_podummy']['_XWidth'] / 2)) + gate_spacing), self._DesignParameter['slvtpfet_b_CDNS_637732429401_0']['_XYCoordinates'][0][1]], [((((self._DesignParameter['slvtpfet_b_CDNS_637732429401_0']['_XYCoordinates'][0][0] + self._DesignParameter['slvtpfet_b_CDNS_637732429401_0']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['slvtpfet_b_CDNS_637732429401_0']['_DesignObj']._DesignParameter['_PODummyLayer']['_XWidth'] / 2)) - (self._DesignParameter['pmos_second_podummy']['_XWidth'] / 2)) - gate_spacing), self._DesignParameter['slvtpfet_b_CDNS_637732429401_0']['_XYCoordinates'][0][1]]]
		# self._DesignParameter['nmos_second_podummy'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _XWidth=length, _YWidth=self._DesignParameter['slvtnfet_b_CDNS_637732429400_0']['_DesignObj']._DesignParameter['_PODummyLayer']['_YWidth'])
		# self._DesignParameter['nmos_second_podummy']['_XYCoordinates'] = [[((((self._DesignParameter['slvtnfet_b_CDNS_637732429400_0']['_XYCoordinates'][0][0] + self._DesignParameter['slvtnfet_b_CDNS_637732429400_0']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['slvtnfet_b_CDNS_637732429400_0']['_DesignObj']._DesignParameter['_PODummyLayer']['_XWidth'] / 2)) - (self._DesignParameter['nmos_second_podummy']['_XWidth'] / 2)) - gate_spacing), self._DesignParameter['slvtnfet_b_CDNS_637732429400_0']['_XYCoordinates'][0][1]], [((((self._DesignParameter['slvtnfet_b_CDNS_637732429400_0']['_XYCoordinates'][0][0] + self._DesignParameter['slvtnfet_b_CDNS_637732429400_0']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][(- 1)][0]) + (self._DesignParameter['slvtnfet_b_CDNS_637732429400_0']['_DesignObj']._DesignParameter['_PODummyLayer']['_XWidth'] / 2)) + (self._DesignParameter['nmos_second_podummy']['_XWidth'] / 2)) + gate_spacing), self._DesignParameter['slvtnfet_b_CDNS_637732429400_0']['_XYCoordinates'][0][1]]]
		# self._DesignParameter['vss_odlayer'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['DIFF'][0], _Datatype=DesignParameters._LayerMapping['DIFF'][1], _XWidth=((self._DesignParameter['nmos_second_podummy']['_XYCoordinates'][0][0] - self._DesignParameter['nmos_second_podummy']['_XYCoordinates'][(- 1)][0]) + self._DesignParameter['nmos_second_podummy']['_XWidth']), _YWidth=(2 * drc._CoMinWidth))
		# self._DesignParameter['vss_odlayer']['_XYCoordinates'] = [[self._DesignParameter['vss']['_XYCoordinates'][0][0], self._DesignParameter['vss']['_XYCoordinates'][0][1]]]
		# self._DesignParameter['vss_supply_m2_y'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _XWidth=self._DesignParameter['vss_odlayer']['_XWidth'], _YWidth=300)
		# self._DesignParameter['vss_supply_m2_y']['_XYCoordinates'] = [[(+ self._DesignParameter['vss_odlayer']['_XYCoordinates'][0][0]), (+ self._DesignParameter['vss_odlayer']['_XYCoordinates'][0][1])]]
		# self._DesignParameter['vdd_odlayer'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['DIFF'][0], _Datatype=DesignParameters._LayerMapping['DIFF'][1], _XWidth=((self._DesignParameter['pmos_second_podummy']['_XYCoordinates'][0][0] - self._DesignParameter['pmos_second_podummy']['_XYCoordinates'][(- 1)][0]) - self._DesignParameter['pmos_second_podummy']['_XWidth']), _YWidth=(2 * drc._CoMinWidth))
		# self._DesignParameter['vdd_odlayer']['_XYCoordinates'] = [[self._DesignParameter['vss_odlayer']['_XYCoordinates'][0][0], self._DesignParameter['vdd']['_XYCoordinates'][0][1]]]
		# self._DesignParameter['vdd_supply_m2_y'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _XWidth=self._DesignParameter['vdd_odlayer']['_XWidth'], _YWidth=300)
		# self._DesignParameter['vdd_supply_m2_y']['_XYCoordinates'] = [[(+ self._DesignParameter['vdd_odlayer']['_XYCoordinates'][0][0]), (+ self._DesignParameter['vdd_odlayer']['_XYCoordinates'][0][1])]]
		# self._DesignParameter['gate_input'] = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_Name='gate_inputIn{}'.format(_Name)))[0]
		# self._DesignParameter['gate_input']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(**dict(_ViaPoly2Met1NumberOfCOX=1, _ViaPoly2Met1NumberOfCOY=2))
		# self._DesignParameter['gate_input']['_XYCoordinates'] = [[(min((self._DesignParameter['nmos_second_podummy']['_XYCoordinates'][0][0] + (self._DesignParameter['slvtnfet_b_CDNS_637732429400_0']['_XYCoordinates'][0][0] + self._DesignParameter['slvtnfet_b_CDNS_637732429400_0']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][0])), (self._DesignParameter['pmos_second_podummy']['_XYCoordinates'][(- 1)][0] + (self._DesignParameter['slvtpfet_b_CDNS_637732429401_0']['_XYCoordinates'][0][0] + self._DesignParameter['slvtpfet_b_CDNS_637732429401_0']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][0]))) / 2), (((self._DesignParameter['pmos_second_podummy']['_XYCoordinates'][0][1] - (self._DesignParameter['pmos_second_podummy']['_YWidth'] / 2)) + (self._DesignParameter['nmos_second_podummy']['_XYCoordinates'][0][1] + (self._DesignParameter['nmos_second_podummy']['_YWidth'] / 2))) / 2)]]
		# self._DesignParameter['gate_output'] = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_Name='gate_outputIn{}'.format(_Name)))[0]
		# self._DesignParameter['gate_output']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(**dict(_ViaPoly2Met1NumberOfCOX=1, _ViaPoly2Met1NumberOfCOY=2))
		# self._DesignParameter['gate_output']['_XYCoordinates'] = [[(max((self._DesignParameter['nmos_second_podummy']['_XYCoordinates'][(- 1)][0] + (self._DesignParameter['slvtnfet_b_CDNS_637732429400_0']['_XYCoordinates'][0][0] + self._DesignParameter['slvtnfet_b_CDNS_637732429400_0']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][(- 1)][0])), (self._DesignParameter['pmos_second_podummy']['_XYCoordinates'][0][0] + (self._DesignParameter['slvtpfet_b_CDNS_637732429401_0']['_XYCoordinates'][0][0] + self._DesignParameter['slvtpfet_b_CDNS_637732429401_0']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][(- 1)][0]))) / 2), (((self._DesignParameter['pmos_second_podummy']['_XYCoordinates'][0][1] - (self._DesignParameter['pmos_second_podummy']['_YWidth'] / 2)) + (self._DesignParameter['nmos_second_podummy']['_XYCoordinates'][0][1] + (self._DesignParameter['nmos_second_podummy']['_YWidth'] / 2))) / 2)]]
		# self._DesignParameter['pmos_poly_gate_routing_x'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _Width=50)
		# self._DesignParameter['pmos_poly_gate_routing_x']['_XYCoordinates'] = [[[((self._DesignParameter['gate_input']['_XYCoordinates'][0][0] + self._DesignParameter['gate_input']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['gate_input']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)), (((self._DesignParameter['gate_input']['_XYCoordinates'][0][1] + self._DesignParameter['gate_input']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) + (self._DesignParameter['gate_input']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)) - (self._DesignParameter['pmos_poly_gate_routing_x']['_Width'] / 2))], [((self._DesignParameter['slvtpfet_b_CDNS_637732429401_0']['_XYCoordinates'][0][0] + self._DesignParameter['slvtpfet_b_CDNS_637732429401_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]) + (self._DesignParameter['slvtpfet_b_CDNS_637732429401_0']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)), (((self._DesignParameter['gate_input']['_XYCoordinates'][0][1] + self._DesignParameter['gate_input']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) + (self._DesignParameter['gate_input']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)) - (self._DesignParameter['pmos_poly_gate_routing_x']['_Width'] / 2))]]]
		# path_list = []
		# if (len(self._DesignParameter['slvtpfet_b_CDNS_637732429401_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates']) == 1):
		#     mode = 'vertical'
		#     _width = self._DesignParameter['slvtpfet_b_CDNS_637732429401_0']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
		# elif (self._DesignParameter['slvtpfet_b_CDNS_637732429401_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0] == self._DesignParameter['slvtpfet_b_CDNS_637732429401_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]):
		#     mode = 'horizontal'
		#     _width = self._DesignParameter['slvtpfet_b_CDNS_637732429401_0']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
		# elif (self._DesignParameter['slvtpfet_b_CDNS_637732429401_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1] == self._DesignParameter['slvtpfet_b_CDNS_637732429401_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][1]):
		#     mode = 'vertical'
		#     _width = self._DesignParameter['slvtpfet_b_CDNS_637732429401_0']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
		# else:
		#     print('Invalid Target Input')
		# if (mode == 'vertical'):
		#     xy_with_offset = []
		#     target_y_value = (0 + self._DesignParameter['pmos_poly_gate_routing_x']['_XYCoordinates'][0][0][1])
		#     for i in range(len(self._DesignParameter['slvtpfet_b_CDNS_637732429401_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
		#         xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['slvtpfet_b_CDNS_637732429401_0']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['slvtpfet_b_CDNS_637732429401_0']['_XYCoordinates'][0][1])], self._DesignParameter['slvtpfet_b_CDNS_637732429401_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i])])
		#     for i in range(len(xy_with_offset)):
		#         path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		# elif (mode == 'horizontal'):
		#     xy_with_offset = []
		#     target_x_value = (0 + self._DesignParameter['pmos_poly_gate_routing_x']['_XYCoordinates'][0][0][0])
		#     for i in range(len(self._DesignParameter['slvtpfet_b_CDNS_637732429401_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
		#         xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['slvtpfet_b_CDNS_637732429401_0']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['slvtpfet_b_CDNS_637732429401_0']['_XYCoordinates'][0][1])], self._DesignParameter['slvtpfet_b_CDNS_637732429401_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i])])
		#     for i in range(len(xy_with_offset)):
		#         path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		# self._DesignParameter['pmos_poly_gate_routing_y'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _Width=_width)
		# self._DesignParameter['pmos_poly_gate_routing_y']['_XYCoordinates'] = path_list
		# self._DesignParameter['nmos_poly_gate_routing_x'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _Width=50)
		# self._DesignParameter['nmos_poly_gate_routing_x']['_XYCoordinates'] = [[[((self._DesignParameter['slvtnfet_b_CDNS_637732429400_0']['_XYCoordinates'][0][0] + self._DesignParameter['slvtnfet_b_CDNS_637732429400_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['slvtnfet_b_CDNS_637732429400_0']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)), (((self._DesignParameter['gate_output']['_XYCoordinates'][0][1] + self._DesignParameter['gate_output']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) - (self._DesignParameter['gate_output']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)) + (self._DesignParameter['nmos_poly_gate_routing_x']['_Width'] / 2))], [((self._DesignParameter['gate_output']['_XYCoordinates'][0][0] + self._DesignParameter['gate_output']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) + (self._DesignParameter['gate_output']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)), (((self._DesignParameter['gate_output']['_XYCoordinates'][0][1] + self._DesignParameter['gate_output']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) - (self._DesignParameter['gate_output']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)) + (self._DesignParameter['nmos_poly_gate_routing_x']['_Width'] / 2))]]]
		# path_list = []
		# if (len(self._DesignParameter['slvtnfet_b_CDNS_637732429400_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates']) == 1):
		#     mode = 'vertical'
		#     _width = self._DesignParameter['slvtnfet_b_CDNS_637732429400_0']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
		# elif (self._DesignParameter['slvtnfet_b_CDNS_637732429400_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0] == self._DesignParameter['slvtnfet_b_CDNS_637732429400_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]):
		#     mode = 'horizontal'
		#     _width = self._DesignParameter['slvtnfet_b_CDNS_637732429400_0']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
		# elif (self._DesignParameter['slvtnfet_b_CDNS_637732429400_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1] == self._DesignParameter['slvtnfet_b_CDNS_637732429400_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][1]):
		#     mode = 'vertical'
		#     _width = self._DesignParameter['slvtnfet_b_CDNS_637732429400_0']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
		# else:
		#     print('Invalid Target Input')
		# if (mode == 'vertical'):
		#     xy_with_offset = []
		#     target_y_value = (0 + self._DesignParameter['nmos_poly_gate_routing_x']['_XYCoordinates'][0][0][1])
		#     for i in range(len(self._DesignParameter['slvtnfet_b_CDNS_637732429400_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
		#         xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['slvtnfet_b_CDNS_637732429400_0']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['slvtnfet_b_CDNS_637732429400_0']['_XYCoordinates'][0][1])], self._DesignParameter['slvtnfet_b_CDNS_637732429400_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i])])
		#     for i in range(len(xy_with_offset)):
		#         path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		# elif (mode == 'horizontal'):
		#     xy_with_offset = []
		#     target_x_value = (0 + self._DesignParameter['nmos_poly_gate_routing_x']['_XYCoordinates'][0][0][0])
		#     for i in range(len(self._DesignParameter['slvtnfet_b_CDNS_637732429400_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
		#         xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['slvtnfet_b_CDNS_637732429400_0']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['slvtnfet_b_CDNS_637732429400_0']['_XYCoordinates'][0][1])], self._DesignParameter['slvtnfet_b_CDNS_637732429400_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i])])
		#     for i in range(len(xy_with_offset)):
		#         path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		# self._DesignParameter['nmos_poly_gate_routing_y'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _Width=_width)
		# self._DesignParameter['nmos_poly_gate_routing_y']['_XYCoordinates'] = path_list
		# if nmos_gate > 1:
		# 	self._DesignParameter['nmos_source_m1_routing_x'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=self._DesignParameter['slvtnfet_b_CDNS_637732429400_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth'])
		# 	self._DesignParameter['nmos_source_m1_routing_x']['_XYCoordinates'] = [[[((self._DesignParameter['slvtnfet_b_CDNS_637732429400_0']['_XYCoordinates'][0][0] + self._DesignParameter['slvtnfet_b_CDNS_637732429400_0']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][0][0]) - (self._DesignParameter['slvtnfet_b_CDNS_637732429400_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth'] / 2)), ((((self._DesignParameter['slvtnfet_b_CDNS_637732429400_0']['_XYCoordinates'][0][1] + self._DesignParameter['slvtnfet_b_CDNS_637732429400_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1]) - (self._DesignParameter['slvtnfet_b_CDNS_637732429400_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_YWidth'] / 2)) - (self._DesignParameter['nmos_source_m1_routing_x']['_Width'] / 2)) - 60)], [((self._DesignParameter['slvtnfet_b_CDNS_637732429400_0']['_XYCoordinates'][0][0] + self._DesignParameter['slvtnfet_b_CDNS_637732429400_0']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][(- 1)][0]) + (self._DesignParameter['slvtnfet_b_CDNS_637732429400_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth'] / 2)), ((((self._DesignParameter['slvtnfet_b_CDNS_637732429400_0']['_XYCoordinates'][0][1] + self._DesignParameter['slvtnfet_b_CDNS_637732429400_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1]) - (self._DesignParameter['slvtnfet_b_CDNS_637732429400_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_YWidth'] / 2)) - (self._DesignParameter['nmos_source_m1_routing_x']['_Width'] / 2)) - 60)]]]
		# path_list = []
		# if (len(self._DesignParameter['slvtpfet_b_CDNS_637732429401_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates']) == 1):
		#     mode = 'vertical'
		#     _width = self._DesignParameter['slvtpfet_b_CDNS_637732429401_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth']
		# elif (self._DesignParameter['slvtpfet_b_CDNS_637732429401_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][0] == self._DesignParameter['slvtpfet_b_CDNS_637732429401_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][0]):
		#     mode = 'horizontal'
		#     _width = self._DesignParameter['slvtpfet_b_CDNS_637732429401_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth']
		# elif (self._DesignParameter['slvtpfet_b_CDNS_637732429401_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1] == self._DesignParameter['slvtpfet_b_CDNS_637732429401_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][1]):
		#     mode = 'vertical'
		#     _width = self._DesignParameter['slvtpfet_b_CDNS_637732429401_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth']
		# else:
		#     print('Invalid Target Input')
		# if (mode == 'vertical'):
		#     xy_with_offset = []
		#     target_y_value = (0 + self._DesignParameter['slvtnfet_b_CDNS_637732429400_0']['_XYCoordinates'][0][1])
		#     for i in range(len(self._DesignParameter['slvtpfet_b_CDNS_637732429401_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		#         if ((i % 2) == 0):
		#             xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['slvtpfet_b_CDNS_637732429401_0']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['slvtpfet_b_CDNS_637732429401_0']['_XYCoordinates'][0][1])], self._DesignParameter['slvtpfet_b_CDNS_637732429401_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])])
		#     for i in range(len(xy_with_offset)):
		#         path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		# elif (mode == 'horizontal'):
		#     xy_with_offset = []
		#     target_x_value = (0 + self._DesignParameter['slvtnfet_b_CDNS_637732429400_0']['_XYCoordinates'][0][0])
		#     for i in range(len(self._DesignParameter['slvtpfet_b_CDNS_637732429401_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		#         if ((i % 2) == 0):
		#             xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['slvtpfet_b_CDNS_637732429401_0']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['slvtpfet_b_CDNS_637732429401_0']['_XYCoordinates'][0][1])], self._DesignParameter['slvtpfet_b_CDNS_637732429401_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])])
		#     for i in range(len(xy_with_offset)):
		#         path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		# self._DesignParameter['m1_source_routing_y'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=_width)
		# self._DesignParameter['m1_source_routing_y']['_XYCoordinates'] = path_list
		# if pmos_gate > 2:
		# 	self._DesignParameter['pmos_drain_m1_routing_x'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=self._DesignParameter['slvtpfet_b_CDNS_637732429401_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth'])
		# 	self._DesignParameter['pmos_drain_m1_routing_x']['_XYCoordinates'] = [[[((self._DesignParameter['slvtpfet_b_CDNS_637732429401_0']['_XYCoordinates'][0][0] + self._DesignParameter['slvtpfet_b_CDNS_637732429401_0']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][0][0]) - (self._DesignParameter['slvtpfet_b_CDNS_637732429401_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth'] / 2)), ((((self._DesignParameter['slvtpfet_b_CDNS_637732429401_0']['_XYCoordinates'][0][1] + self._DesignParameter['slvtpfet_b_CDNS_637732429401_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1]) + (self._DesignParameter['slvtpfet_b_CDNS_637732429401_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_YWidth'] / 2)) + (self._DesignParameter['pmos_drain_m1_routing_x']['_Width'] / 2)) + 60)], [((self._DesignParameter['slvtpfet_b_CDNS_637732429401_0']['_XYCoordinates'][0][0] + self._DesignParameter['slvtpfet_b_CDNS_637732429401_0']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][(- 1)][0]) + (self._DesignParameter['slvtpfet_b_CDNS_637732429401_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth'] / 2)), ((((self._DesignParameter['slvtpfet_b_CDNS_637732429401_0']['_XYCoordinates'][0][1] + self._DesignParameter['slvtpfet_b_CDNS_637732429401_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1]) + (self._DesignParameter['slvtpfet_b_CDNS_637732429401_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_YWidth'] / 2)) + (self._DesignParameter['pmos_drain_m1_routing_x']['_Width'] / 2)) + 60)]]]
		# path_list = []
		# if (len(self._DesignParameter['slvtnfet_b_CDNS_637732429400_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates']) == 1):
		#     mode = 'vertical'
		#     _width = self._DesignParameter['slvtnfet_b_CDNS_637732429400_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth']
		# elif (self._DesignParameter['slvtnfet_b_CDNS_637732429400_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][0] == self._DesignParameter['slvtnfet_b_CDNS_637732429400_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][0]):
		#     mode = 'horizontal'
		#     _width = self._DesignParameter['slvtnfet_b_CDNS_637732429400_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth']
		# elif (self._DesignParameter['slvtnfet_b_CDNS_637732429400_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1] == self._DesignParameter['slvtnfet_b_CDNS_637732429400_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][1]):
		#     mode = 'vertical'
		#     _width = self._DesignParameter['slvtnfet_b_CDNS_637732429400_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth']
		# else:
		#     print('Invalid Target Input')
		# if (mode == 'vertical'):
		#     xy_with_offset = []
		#     target_y_value = (0 + self._DesignParameter['slvtpfet_b_CDNS_637732429401_0']['_XYCoordinates'][0][1])
		#     for i in range(len(self._DesignParameter['slvtnfet_b_CDNS_637732429400_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		#         if ((i % 2) == 1):
		#             xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['slvtnfet_b_CDNS_637732429400_0']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['slvtnfet_b_CDNS_637732429400_0']['_XYCoordinates'][0][1])], self._DesignParameter['slvtnfet_b_CDNS_637732429400_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])])
		#     for i in range(len(xy_with_offset)):
		#         path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		# elif (mode == 'horizontal'):
		#     xy_with_offset = []
		#     target_x_value = (0 + self._DesignParameter['slvtpfet_b_CDNS_637732429401_0']['_XYCoordinates'][0][0])
		#     for i in range(len(self._DesignParameter['slvtnfet_b_CDNS_637732429400_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		#         if ((i % 2) == 1):
		#             xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['slvtnfet_b_CDNS_637732429400_0']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['slvtnfet_b_CDNS_637732429400_0']['_XYCoordinates'][0][1])], self._DesignParameter['slvtnfet_b_CDNS_637732429400_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])])
		#     for i in range(len(xy_with_offset)):
		#         path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		# self._DesignParameter['m1_drain_routing_y'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=_width)
		# self._DesignParameter['m1_drain_routing_y']['_XYCoordinates'] = path_list
		# self._DesignParameter['SLVT_boundary_1'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['SLVT'][0], _Datatype=DesignParameters._LayerMapping['SLVT'][1], _XWidth=max((self._DesignParameter['pmos_second_podummy']['_XYCoordinates'][0][0] - self._DesignParameter['pmos_second_podummy']['_XYCoordinates'][(- 1)][0]), (self._DesignParameter['nmos_second_podummy']['_XYCoordinates'][(- 1)][0] - self._DesignParameter['nmos_second_podummy']['_XYCoordinates'][0][0])), _YWidth=(self._DesignParameter['vdd']['_XYCoordinates'][0][1] - self._DesignParameter['vss']['_XYCoordinates'][0][1]))
		# self._DesignParameter['SLVT_boundary_1']['_XYCoordinates'] = [[self._DesignParameter['vss']['_XYCoordinates'][0][0], ((self._DesignParameter['vdd']['_XYCoordinates'][0][1] + self._DesignParameter['vss']['_XYCoordinates'][0][1]) / 2)]]
		# self._DesignParameter['NWELL_boundary_0'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['NWELL'][0], _Datatype=DesignParameters._LayerMapping['NWELL'][1], _XWidth=(max(self._DesignParameter['vdd_odlayer']['_XWidth'], self._DesignParameter['slvtpfet_b_CDNS_637732429401_0']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth']) + (2 * drc._NwMinEnclosurePactive)), _YWidth=(((self._DesignParameter['vdd_odlayer']['_XYCoordinates'][0][1] + (self._DesignParameter['vdd_odlayer']['_YWidth'] / 2)) + drc._NwMinEnclosurePactive2) - ((self._DesignParameter['gate_input']['_XYCoordinates'][0][1] + self._DesignParameter['gate_input']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) - (self._DesignParameter['gate_input']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2))))
		# self._DesignParameter['NWELL_boundary_0']['_XYCoordinates'] = [[self._DesignParameter['vss']['_XYCoordinates'][0][0], ((((self._DesignParameter['vdd_odlayer']['_XYCoordinates'][0][1] + (self._DesignParameter['vdd_odlayer']['_YWidth'] / 2)) + drc._NwMinEnclosurePactive2) + ((self._DesignParameter['gate_input']['_XYCoordinates'][0][1] + self._DesignParameter['gate_input']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) - (self._DesignParameter['gate_input']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2))) / 2)]]
		# self._DesignParameter['PIMP_boundary_1'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['PIMP'][0], _Datatype=DesignParameters._LayerMapping['PIMP'][1], _XWidth=(self._DesignParameter['slvtpfet_b_CDNS_637732429401_0']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth'] + (2 * drc._PpMinExtensiononPactive)), _YWidth=(self._DesignParameter['slvtpfet_b_CDNS_637732429401_0']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth'] + (2 * drc._PpMinExtensiononPactive)))
		# self._DesignParameter['PIMP_boundary_1']['_XYCoordinates'] = [[self._DesignParameter['slvtpfet_b_CDNS_637732429401_0']['_XYCoordinates'][0][0], self._DesignParameter['slvtpfet_b_CDNS_637732429401_0']['_XYCoordinates'][0][1]]]
		# self._DesignParameter['vss_pplayer'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['PIMP'][0], _Datatype=DesignParameters._LayerMapping['PIMP'][1], _XWidth=(self._DesignParameter['vss_odlayer']['_XWidth'] + (2 * drc._PpMinExtensiononPactive)), _YWidth=(self._DesignParameter['vss_odlayer']['_YWidth'] + (2 * drc._PpMinExtensiononPactive)))
		# self._DesignParameter['vss_pplayer']['_XYCoordinates'] = [[(+ self._DesignParameter['vss_odlayer']['_XYCoordinates'][0][0]), (+ self._DesignParameter['vss_odlayer']['_XYCoordinates'][0][1])]]
		# if pmos_gate > 2 :
		# 	path_list = []
		# 	if (len(self._DesignParameter['slvtpfet_b_CDNS_637732429401_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates']) == 1):
		# 		mode = 'vertical'
		# 		_width = self._DesignParameter['slvtpfet_b_CDNS_637732429401_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth']
		# 	elif (self._DesignParameter['slvtpfet_b_CDNS_637732429401_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][0] == self._DesignParameter['slvtpfet_b_CDNS_637732429401_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][0]):
		# 		mode = 'horizontal'
		# 		_width = self._DesignParameter['slvtpfet_b_CDNS_637732429401_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth']
		# 	elif (self._DesignParameter['slvtpfet_b_CDNS_637732429401_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1] == self._DesignParameter['slvtpfet_b_CDNS_637732429401_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][1]):
		# 		mode = 'vertical'
		# 		_width = self._DesignParameter['slvtpfet_b_CDNS_637732429401_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth']
		# 	else:
		# 		print('Invalid Target Input')
		# 	if (mode == 'vertical'):
		# 		xy_with_offset = []
		# 		target_y_value = (0 + self._DesignParameter['pmos_drain_m1_routing_x']['_XYCoordinates'][0][0][1])
		# 		for i in range(len(self._DesignParameter['slvtpfet_b_CDNS_637732429401_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		# 			if ((i % 2) == 1):
		# 				xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['slvtpfet_b_CDNS_637732429401_0']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['slvtpfet_b_CDNS_637732429401_0']['_XYCoordinates'][0][1])], self._DesignParameter['slvtpfet_b_CDNS_637732429401_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])])
		# 		for i in range(len(xy_with_offset)):
		# 			path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		# 	elif (mode == 'horizontal'):
		# 		xy_with_offset = []
		# 		target_x_value = (0 + self._DesignParameter['pmos_drain_m1_routing_x']['_XYCoordinates'][0][0][0])
		# 		for i in range(len(self._DesignParameter['slvtpfet_b_CDNS_637732429401_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		# 			if ((i % 2) == 1):
		# 				xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['slvtpfet_b_CDNS_637732429401_0']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['slvtpfet_b_CDNS_637732429401_0']['_XYCoordinates'][0][1])], self._DesignParameter['slvtpfet_b_CDNS_637732429401_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])])
		# 		for i in range(len(xy_with_offset)):
		# 			path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		# 	self._DesignParameter['additional_m1_drain'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=_width)
		# 	self._DesignParameter['additional_m1_drain']['_XYCoordinates'] = path_list
		# if nmos_gate > 1 :
		# 	path_list = []
		# 	if (len(self._DesignParameter['slvtnfet_b_CDNS_637732429400_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates']) == 1):
		# 		mode = 'vertical'
		# 		_width = self._DesignParameter['slvtnfet_b_CDNS_637732429400_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth']
		# 	elif (self._DesignParameter['slvtnfet_b_CDNS_637732429400_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][0] == self._DesignParameter['slvtnfet_b_CDNS_637732429400_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][0]):
		# 		mode = 'horizontal'
		# 		_width = self._DesignParameter['slvtnfet_b_CDNS_637732429400_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth']
		# 	elif (self._DesignParameter['slvtnfet_b_CDNS_637732429400_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1] == self._DesignParameter['slvtnfet_b_CDNS_637732429400_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][1]):
		# 		mode = 'vertical'
		# 		_width = self._DesignParameter['slvtnfet_b_CDNS_637732429400_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth']
		# 	else:
		# 		print('Invalid Target Input')
		# 	if (mode == 'vertical'):
		# 		xy_with_offset = []
		# 		target_y_value = (0 + self._DesignParameter['nmos_source_m1_routing_x']['_XYCoordinates'][0][0][1])
		# 		for i in range(len(self._DesignParameter['slvtnfet_b_CDNS_637732429400_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		# 			if ((i % 2) == 0):
		# 				xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['slvtnfet_b_CDNS_637732429400_0']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['slvtnfet_b_CDNS_637732429400_0']['_XYCoordinates'][0][1])], self._DesignParameter['slvtnfet_b_CDNS_637732429400_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])])
		# 		for i in range(len(xy_with_offset)):
		# 			path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		# 	elif (mode == 'horizontal'):
		# 		xy_with_offset = []
		# 		target_x_value = (0 + self._DesignParameter['nmos_source_m1_routing_x']['_XYCoordinates'][0][0][0])
		# 		for i in range(len(self._DesignParameter['slvtnfet_b_CDNS_637732429400_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		# 			if ((i % 2) == 0):
		# 				xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['slvtnfet_b_CDNS_637732429400_0']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['slvtnfet_b_CDNS_637732429400_0']['_XYCoordinates'][0][1])], self._DesignParameter['slvtnfet_b_CDNS_637732429400_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])])
		# 		for i in range(len(xy_with_offset)):
		# 			path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		# 	self._DesignParameter['additional_m1_source'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=_width)
		# 	self._DesignParameter['additional_m1_source']['_XYCoordinates'] = path_list
		self._DesignParameter['vss'] = self._SrefElementDeclaration(_DesignObj=Z_PWR_CNT.Z_PWR_CNT(_Name='vssIn{}'.format(_Name)))[0]
		self._DesignParameter['vss']['_DesignObj']._CalculateDesignParameter(**dict(_Xnum=(nmos_gate + 1), _Xdistance=power_xdistance))
		self._DesignParameter['vss']['_XYCoordinates'] = [[0, 0]]
		self._DesignParameter['vdd'] = self._SrefElementDeclaration(_DesignObj=Z_PWR_CNT.Z_PWR_CNT(_Name='vddIn{}'.format(_Name)))[0]
		self._DesignParameter['vdd']['_DesignObj']._CalculateDesignParameter(**dict(_Xnum=(pmos_gate + 1), _Xdistance=power_xdistance))
		self._DesignParameter['vdd']['_XYCoordinates'] = [[0, vss2vdd_height]]
		self._DesignParameter['slvtnfet_b_CDNS_637732429400_0'] = self._SrefElementDeclaration(_DesignObj=NMOSWithDummy._NMOS(_Name='slvtnfet_b_CDNS_637732429400_0In{}'.format(_Name)))[0]
		self._DesignParameter['slvtnfet_b_CDNS_637732429400_0']['_DesignObj']._CalculateNMOSDesignParameter(**dict(_NMOSNumberofGate=nmos_gate, _NMOSChannelWidth=nmos_width, _NMOSChannellength=length, _NMOSDummy=True, _GateSpacing=gate_spacing, _SDWidth=sdwidth, _XVT=XVT))
		self._DesignParameter['slvtnfet_b_CDNS_637732429400_0']['_XYCoordinates'] = [[self._DesignParameter['vss']['_XYCoordinates'][0][0], nmos_y]]
		self._DesignParameter['slvtpfet_b_CDNS_637732429401_0'] = self._SrefElementDeclaration(_DesignObj=PMOSWithDummy._PMOS(_Name='slvtpfet_b_CDNS_637732429401_0In{}'.format(_Name)))[0]
		self._DesignParameter['slvtpfet_b_CDNS_637732429401_0']['_DesignObj']._CalculatePMOSDesignParameter(**dict(_PMOSNumberofGate=pmos_gate, _PMOSChannelWidth=pmos_width, _PMOSChannellength=length, _PMOSDummy=True, _GateSpacing=gate_spacing, _SDWidth=sdwidth, _XVT=XVT))
		self._DesignParameter['slvtpfet_b_CDNS_637732429401_0']['_XYCoordinates'] = [[self._DesignParameter['vdd']['_XYCoordinates'][0][0], (vss2vdd_height - pmos_y)]]
		self._DesignParameter['pmos_second_podummy'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _XWidth=length, _YWidth=self._DesignParameter['slvtpfet_b_CDNS_637732429401_0']['_DesignObj']._DesignParameter['_PODummyLayer']['_YWidth'])
		self._DesignParameter['pmos_second_podummy']['_XYCoordinates'] = [[((((self._DesignParameter['slvtpfet_b_CDNS_637732429401_0']['_XYCoordinates'][0][0] + self._DesignParameter['slvtpfet_b_CDNS_637732429401_0']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][(- 1)][0]) + (self._DesignParameter['slvtpfet_b_CDNS_637732429401_0']['_DesignObj']._DesignParameter['_PODummyLayer']['_XWidth'] / 2)) + (self._DesignParameter['pmos_second_podummy']['_XWidth'] / 2)) + gate_spacing), self._DesignParameter['slvtpfet_b_CDNS_637732429401_0']['_XYCoordinates'][0][1]], [((((self._DesignParameter['slvtpfet_b_CDNS_637732429401_0']['_XYCoordinates'][0][0] + self._DesignParameter['slvtpfet_b_CDNS_637732429401_0']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['slvtpfet_b_CDNS_637732429401_0']['_DesignObj']._DesignParameter['_PODummyLayer']['_XWidth'] / 2)) - (self._DesignParameter['pmos_second_podummy']['_XWidth'] / 2)) - gate_spacing), self._DesignParameter['slvtpfet_b_CDNS_637732429401_0']['_XYCoordinates'][0][1]]]
		self._DesignParameter['nmos_second_podummy'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _XWidth=length, _YWidth=self._DesignParameter['slvtnfet_b_CDNS_637732429400_0']['_DesignObj']._DesignParameter['_PODummyLayer']['_YWidth'])
		self._DesignParameter['nmos_second_podummy']['_XYCoordinates'] = [[((((self._DesignParameter['slvtnfet_b_CDNS_637732429400_0']['_XYCoordinates'][0][0] + self._DesignParameter['slvtnfet_b_CDNS_637732429400_0']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['slvtnfet_b_CDNS_637732429400_0']['_DesignObj']._DesignParameter['_PODummyLayer']['_XWidth'] / 2)) - (self._DesignParameter['nmos_second_podummy']['_XWidth'] / 2)) - gate_spacing), self._DesignParameter['slvtnfet_b_CDNS_637732429400_0']['_XYCoordinates'][0][1]], [((((self._DesignParameter['slvtnfet_b_CDNS_637732429400_0']['_XYCoordinates'][0][0] + self._DesignParameter['slvtnfet_b_CDNS_637732429400_0']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][(- 1)][0]) + (self._DesignParameter['slvtnfet_b_CDNS_637732429400_0']['_DesignObj']._DesignParameter['_PODummyLayer']['_XWidth'] / 2)) + (self._DesignParameter['nmos_second_podummy']['_XWidth'] / 2)) + gate_spacing), self._DesignParameter['slvtnfet_b_CDNS_637732429400_0']['_XYCoordinates'][0][1]]]
		self._DesignParameter['vss_odlayer'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['DIFF'][0], _Datatype=DesignParameters._LayerMapping['DIFF'][1], _XWidth=((self._DesignParameter['nmos_second_podummy']['_XYCoordinates'][0][0] - self._DesignParameter['nmos_second_podummy']['_XYCoordinates'][(- 1)][0]) + self._DesignParameter['nmos_second_podummy']['_XWidth']), _YWidth=(2 * drc._CoMinWidth))
		self._DesignParameter['vss_odlayer']['_XYCoordinates'] = [[self._DesignParameter['vss']['_XYCoordinates'][0][0], self._DesignParameter['vss']['_XYCoordinates'][0][1]]]
		self._DesignParameter['vss_supply_m2_y'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _XWidth=self._DesignParameter['vss_odlayer']['_XWidth'], _YWidth=300)
		self._DesignParameter['vss_supply_m2_y']['_XYCoordinates'] = [[(+ self._DesignParameter['vss_odlayer']['_XYCoordinates'][0][0]), (+ self._DesignParameter['vss_odlayer']['_XYCoordinates'][0][1])]]
		self._DesignParameter['vdd_odlayer'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['DIFF'][0], _Datatype=DesignParameters._LayerMapping['DIFF'][1], _XWidth=((self._DesignParameter['pmos_second_podummy']['_XYCoordinates'][0][0] - self._DesignParameter['pmos_second_podummy']['_XYCoordinates'][(- 1)][0]) - self._DesignParameter['pmos_second_podummy']['_XWidth']), _YWidth=(2 * drc._CoMinWidth))
		self._DesignParameter['vdd_odlayer']['_XYCoordinates'] = [[self._DesignParameter['vss_odlayer']['_XYCoordinates'][0][0], self._DesignParameter['vdd']['_XYCoordinates'][0][1]]]
		self._DesignParameter['vdd_supply_m2_y'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _XWidth=self._DesignParameter['vdd_odlayer']['_XWidth'], _YWidth=300)
		self._DesignParameter['vdd_supply_m2_y']['_XYCoordinates'] = [[(+ self._DesignParameter['vdd_odlayer']['_XYCoordinates'][0][0]), (+ self._DesignParameter['vdd_odlayer']['_XYCoordinates'][0][1])]]
		self._DesignParameter['gate_input'] = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_Name='gate_inputIn{}'.format(_Name)))[0]
		self._DesignParameter['gate_input']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(**dict(_ViaPoly2Met1NumberOfCOX=1, _ViaPoly2Met1NumberOfCOY=2))
		self._DesignParameter['gate_input']['_XYCoordinates'] = [[(min((self._DesignParameter['nmos_second_podummy']['_XYCoordinates'][0][0] + (self._DesignParameter['slvtnfet_b_CDNS_637732429400_0']['_XYCoordinates'][0][0] + self._DesignParameter['slvtnfet_b_CDNS_637732429400_0']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][0])), (self._DesignParameter['pmos_second_podummy']['_XYCoordinates'][(- 1)][0] + (self._DesignParameter['slvtpfet_b_CDNS_637732429401_0']['_XYCoordinates'][0][0] + self._DesignParameter['slvtpfet_b_CDNS_637732429401_0']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][0]))) / 2), (((self._DesignParameter['pmos_second_podummy']['_XYCoordinates'][0][1] - (self._DesignParameter['pmos_second_podummy']['_YWidth'] / 2)) + (self._DesignParameter['nmos_second_podummy']['_XYCoordinates'][0][1] + (self._DesignParameter['nmos_second_podummy']['_YWidth'] / 2))) / 2)]]
		self._DesignParameter['gate_output'] = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_Name='gate_outputIn{}'.format(_Name)))[0]
		self._DesignParameter['gate_output']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(**dict(_ViaPoly2Met1NumberOfCOX=1, _ViaPoly2Met1NumberOfCOY=2))
		self._DesignParameter['gate_output']['_XYCoordinates'] = [[(max((self._DesignParameter['nmos_second_podummy']['_XYCoordinates'][(- 1)][0] + (self._DesignParameter['slvtnfet_b_CDNS_637732429400_0']['_XYCoordinates'][0][0] + self._DesignParameter['slvtnfet_b_CDNS_637732429400_0']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][(- 1)][0])), (self._DesignParameter['pmos_second_podummy']['_XYCoordinates'][0][0] + (self._DesignParameter['slvtpfet_b_CDNS_637732429401_0']['_XYCoordinates'][0][0] + self._DesignParameter['slvtpfet_b_CDNS_637732429401_0']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][(- 1)][0]))) / 2), (((self._DesignParameter['pmos_second_podummy']['_XYCoordinates'][0][1] - (self._DesignParameter['pmos_second_podummy']['_YWidth'] / 2)) + (self._DesignParameter['nmos_second_podummy']['_XYCoordinates'][0][1] + (self._DesignParameter['nmos_second_podummy']['_YWidth'] / 2))) / 2)]]
		self._DesignParameter['pmos_poly_gate_routing_x'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _Width=50)
		self._DesignParameter['pmos_poly_gate_routing_x']['_XYCoordinates'] = [[[((self._DesignParameter['gate_input']['_XYCoordinates'][0][0] + self._DesignParameter['gate_input']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['gate_input']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)), (((self._DesignParameter['gate_input']['_XYCoordinates'][0][1] + self._DesignParameter['gate_input']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) + (self._DesignParameter['gate_input']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)) - (self._DesignParameter['pmos_poly_gate_routing_x']['_Width'] / 2))], [((self._DesignParameter['slvtpfet_b_CDNS_637732429401_0']['_XYCoordinates'][0][0] + self._DesignParameter['slvtpfet_b_CDNS_637732429401_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]) + (self._DesignParameter['slvtpfet_b_CDNS_637732429401_0']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)), (((self._DesignParameter['gate_input']['_XYCoordinates'][0][1] + self._DesignParameter['gate_input']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) + (self._DesignParameter['gate_input']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)) - (self._DesignParameter['pmos_poly_gate_routing_x']['_Width'] / 2))]]]
		path_list = []
		if (len(self._DesignParameter['slvtpfet_b_CDNS_637732429401_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates']) == 1):
		    mode = 'vertical'
		    _width = self._DesignParameter['slvtpfet_b_CDNS_637732429401_0']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
		elif (self._DesignParameter['slvtpfet_b_CDNS_637732429401_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0] == self._DesignParameter['slvtpfet_b_CDNS_637732429401_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]):
		    mode = 'horizontal'
		    _width = self._DesignParameter['slvtpfet_b_CDNS_637732429401_0']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
		elif (self._DesignParameter['slvtpfet_b_CDNS_637732429401_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1] == self._DesignParameter['slvtpfet_b_CDNS_637732429401_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][1]):
		    mode = 'vertical'
		    _width = self._DesignParameter['slvtpfet_b_CDNS_637732429401_0']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
		else:
		    print('Invalid Target Input')
		if (mode == 'vertical'):
		    xy_with_offset = []
		    target_y_value = (0 + self._DesignParameter['pmos_poly_gate_routing_x']['_XYCoordinates'][0][0][1])
		    for i in range(len(self._DesignParameter['slvtpfet_b_CDNS_637732429401_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
		        xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['slvtpfet_b_CDNS_637732429401_0']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['slvtpfet_b_CDNS_637732429401_0']['_XYCoordinates'][0][1])], self._DesignParameter['slvtpfet_b_CDNS_637732429401_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		elif (mode == 'horizontal'):
		    xy_with_offset = []
		    target_x_value = (0 + self._DesignParameter['pmos_poly_gate_routing_x']['_XYCoordinates'][0][0][0])
		    for i in range(len(self._DesignParameter['slvtpfet_b_CDNS_637732429401_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
		        xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['slvtpfet_b_CDNS_637732429401_0']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['slvtpfet_b_CDNS_637732429401_0']['_XYCoordinates'][0][1])], self._DesignParameter['slvtpfet_b_CDNS_637732429401_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		self._DesignParameter['pmos_poly_gate_routing_y'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _Width=_width)
		self._DesignParameter['pmos_poly_gate_routing_y']['_XYCoordinates'] = path_list
		self._DesignParameter['nmos_poly_gate_routing_x'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _Width=50)
		self._DesignParameter['nmos_poly_gate_routing_x']['_XYCoordinates'] = [[[((self._DesignParameter['slvtnfet_b_CDNS_637732429400_0']['_XYCoordinates'][0][0] + self._DesignParameter['slvtnfet_b_CDNS_637732429400_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['slvtnfet_b_CDNS_637732429400_0']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)), (((self._DesignParameter['gate_output']['_XYCoordinates'][0][1] + self._DesignParameter['gate_output']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) - (self._DesignParameter['gate_output']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)) + (self._DesignParameter['nmos_poly_gate_routing_x']['_Width'] / 2))], [((self._DesignParameter['gate_output']['_XYCoordinates'][0][0] + self._DesignParameter['gate_output']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) + (self._DesignParameter['gate_output']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)), (((self._DesignParameter['gate_output']['_XYCoordinates'][0][1] + self._DesignParameter['gate_output']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) - (self._DesignParameter['gate_output']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)) + (self._DesignParameter['nmos_poly_gate_routing_x']['_Width'] / 2))]]]
		path_list = []
		if (len(self._DesignParameter['slvtnfet_b_CDNS_637732429400_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates']) == 1):
		    mode = 'vertical'
		    _width = self._DesignParameter['slvtnfet_b_CDNS_637732429400_0']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
		elif (self._DesignParameter['slvtnfet_b_CDNS_637732429400_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0] == self._DesignParameter['slvtnfet_b_CDNS_637732429400_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]):
		    mode = 'horizontal'
		    _width = self._DesignParameter['slvtnfet_b_CDNS_637732429400_0']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
		elif (self._DesignParameter['slvtnfet_b_CDNS_637732429400_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1] == self._DesignParameter['slvtnfet_b_CDNS_637732429400_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][1]):
		    mode = 'vertical'
		    _width = self._DesignParameter['slvtnfet_b_CDNS_637732429400_0']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
		else:
		    print('Invalid Target Input')
		if (mode == 'vertical'):
		    xy_with_offset = []
		    target_y_value = (0 + self._DesignParameter['nmos_poly_gate_routing_x']['_XYCoordinates'][0][0][1])
		    for i in range(len(self._DesignParameter['slvtnfet_b_CDNS_637732429400_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
		        xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['slvtnfet_b_CDNS_637732429400_0']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['slvtnfet_b_CDNS_637732429400_0']['_XYCoordinates'][0][1])], self._DesignParameter['slvtnfet_b_CDNS_637732429400_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		elif (mode == 'horizontal'):
		    xy_with_offset = []
		    target_x_value = (0 + self._DesignParameter['nmos_poly_gate_routing_x']['_XYCoordinates'][0][0][0])
		    for i in range(len(self._DesignParameter['slvtnfet_b_CDNS_637732429400_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
		        xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['slvtnfet_b_CDNS_637732429400_0']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['slvtnfet_b_CDNS_637732429400_0']['_XYCoordinates'][0][1])], self._DesignParameter['slvtnfet_b_CDNS_637732429400_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		self._DesignParameter['nmos_poly_gate_routing_y'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _Width=_width)
		self._DesignParameter['nmos_poly_gate_routing_y']['_XYCoordinates'] = path_list
		if nmos_gate>1:
			self._DesignParameter['nmos_source_m1_routing_x'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=self._DesignParameter['slvtnfet_b_CDNS_637732429400_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth'])
			self._DesignParameter['nmos_source_m1_routing_x']['_XYCoordinates'] = [[[((self._DesignParameter['slvtnfet_b_CDNS_637732429400_0']['_XYCoordinates'][0][0] + self._DesignParameter['slvtnfet_b_CDNS_637732429400_0']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][0][0]) - (self._DesignParameter['slvtnfet_b_CDNS_637732429400_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth'] / 2)), ((((self._DesignParameter['slvtnfet_b_CDNS_637732429400_0']['_XYCoordinates'][0][1] + self._DesignParameter['slvtnfet_b_CDNS_637732429400_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1]) - (self._DesignParameter['slvtnfet_b_CDNS_637732429400_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_YWidth'] / 2)) - (self._DesignParameter['nmos_source_m1_routing_x']['_Width'] / 2)) - 60)], [((self._DesignParameter['slvtnfet_b_CDNS_637732429400_0']['_XYCoordinates'][0][0] + self._DesignParameter['slvtnfet_b_CDNS_637732429400_0']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][(- 1)][0]) + (self._DesignParameter['slvtnfet_b_CDNS_637732429400_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth'] / 2)), ((((self._DesignParameter['slvtnfet_b_CDNS_637732429400_0']['_XYCoordinates'][0][1] + self._DesignParameter['slvtnfet_b_CDNS_637732429400_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1]) - (self._DesignParameter['slvtnfet_b_CDNS_637732429400_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_YWidth'] / 2)) - (self._DesignParameter['nmos_source_m1_routing_x']['_Width'] / 2)) - 60)]]]
		path_list = []
		if (len(self._DesignParameter['slvtpfet_b_CDNS_637732429401_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates']) == 1):
		    mode = 'vertical'
		    _width = self._DesignParameter['slvtpfet_b_CDNS_637732429401_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth']
		elif (self._DesignParameter['slvtpfet_b_CDNS_637732429401_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][0] == self._DesignParameter['slvtpfet_b_CDNS_637732429401_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][0]):
		    mode = 'horizontal'
		    _width = self._DesignParameter['slvtpfet_b_CDNS_637732429401_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth']
		elif (self._DesignParameter['slvtpfet_b_CDNS_637732429401_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1] == self._DesignParameter['slvtpfet_b_CDNS_637732429401_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][1]):
		    mode = 'vertical'
		    _width = self._DesignParameter['slvtpfet_b_CDNS_637732429401_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth']
		else:
		    print('Invalid Target Input')
		if (mode == 'vertical'):
		    xy_with_offset = []
		    target_y_value = (0 + self._DesignParameter['slvtnfet_b_CDNS_637732429400_0']['_XYCoordinates'][0][1])
		    for i in range(len(self._DesignParameter['slvtpfet_b_CDNS_637732429401_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		        if ((i % 2) == 0):
		            xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['slvtpfet_b_CDNS_637732429401_0']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['slvtpfet_b_CDNS_637732429401_0']['_XYCoordinates'][0][1])], self._DesignParameter['slvtpfet_b_CDNS_637732429401_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		elif (mode == 'horizontal'):
		    xy_with_offset = []
		    target_x_value = (0 + self._DesignParameter['slvtnfet_b_CDNS_637732429400_0']['_XYCoordinates'][0][0])
		    for i in range(len(self._DesignParameter['slvtpfet_b_CDNS_637732429401_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		        if ((i % 2) == 0):
		            xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['slvtpfet_b_CDNS_637732429401_0']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['slvtpfet_b_CDNS_637732429401_0']['_XYCoordinates'][0][1])], self._DesignParameter['slvtpfet_b_CDNS_637732429401_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		self._DesignParameter['m1_source_routing_y'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=_width)
		self._DesignParameter['m1_source_routing_y']['_XYCoordinates'] = path_list
		if pmos_gate > 2 :
			self._DesignParameter['pmos_drain_m1_routing_x'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=self._DesignParameter['slvtpfet_b_CDNS_637732429401_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth'])
			self._DesignParameter['pmos_drain_m1_routing_x']['_XYCoordinates'] = [[[((self._DesignParameter['slvtpfet_b_CDNS_637732429401_0']['_XYCoordinates'][0][0] + self._DesignParameter['slvtpfet_b_CDNS_637732429401_0']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][0][0]) - (self._DesignParameter['slvtpfet_b_CDNS_637732429401_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth'] / 2)), ((((self._DesignParameter['slvtpfet_b_CDNS_637732429401_0']['_XYCoordinates'][0][1] + self._DesignParameter['slvtpfet_b_CDNS_637732429401_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1]) + (self._DesignParameter['slvtpfet_b_CDNS_637732429401_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_YWidth'] / 2)) + (self._DesignParameter['pmos_drain_m1_routing_x']['_Width'] / 2)) + 60)], [((self._DesignParameter['slvtpfet_b_CDNS_637732429401_0']['_XYCoordinates'][0][0] + self._DesignParameter['slvtpfet_b_CDNS_637732429401_0']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][(- 1)][0]) + (self._DesignParameter['slvtpfet_b_CDNS_637732429401_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth'] / 2)), ((((self._DesignParameter['slvtpfet_b_CDNS_637732429401_0']['_XYCoordinates'][0][1] + self._DesignParameter['slvtpfet_b_CDNS_637732429401_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1]) + (self._DesignParameter['slvtpfet_b_CDNS_637732429401_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_YWidth'] / 2)) + (self._DesignParameter['pmos_drain_m1_routing_x']['_Width'] / 2)) + 60)]]]
		path_list = []
		if (len(self._DesignParameter['slvtnfet_b_CDNS_637732429400_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates']) == 1):
		    mode = 'vertical'
		    _width = self._DesignParameter['slvtnfet_b_CDNS_637732429400_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth']
		elif (self._DesignParameter['slvtnfet_b_CDNS_637732429400_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][0] == self._DesignParameter['slvtnfet_b_CDNS_637732429400_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][0]):
		    mode = 'horizontal'
		    _width = self._DesignParameter['slvtnfet_b_CDNS_637732429400_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth']
		elif (self._DesignParameter['slvtnfet_b_CDNS_637732429400_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1] == self._DesignParameter['slvtnfet_b_CDNS_637732429400_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][1]):
		    mode = 'vertical'
		    _width = self._DesignParameter['slvtnfet_b_CDNS_637732429400_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth']
		else:
		    print('Invalid Target Input')
		if (mode == 'vertical'):
		    xy_with_offset = []
		    target_y_value = (0 + self._DesignParameter['slvtpfet_b_CDNS_637732429401_0']['_XYCoordinates'][0][1])
		    for i in range(len(self._DesignParameter['slvtnfet_b_CDNS_637732429400_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		        if ((i % 2) == 1):
		            xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['slvtnfet_b_CDNS_637732429400_0']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['slvtnfet_b_CDNS_637732429400_0']['_XYCoordinates'][0][1])], self._DesignParameter['slvtnfet_b_CDNS_637732429400_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		elif (mode == 'horizontal'):
		    xy_with_offset = []
		    target_x_value = (0 + self._DesignParameter['slvtpfet_b_CDNS_637732429401_0']['_XYCoordinates'][0][0])
		    for i in range(len(self._DesignParameter['slvtnfet_b_CDNS_637732429400_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		        if ((i % 2) == 1):
		            xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['slvtnfet_b_CDNS_637732429400_0']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['slvtnfet_b_CDNS_637732429400_0']['_XYCoordinates'][0][1])], self._DesignParameter['slvtnfet_b_CDNS_637732429400_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		self._DesignParameter['m1_drain_routing_y'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=_width)
		self._DesignParameter['m1_drain_routing_y']['_XYCoordinates'] = path_list
		self._DesignParameter['SLVT_boundary_1'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['SLVT'][0], _Datatype=DesignParameters._LayerMapping['SLVT'][1], _XWidth=max((self._DesignParameter['pmos_second_podummy']['_XYCoordinates'][0][0] - self._DesignParameter['pmos_second_podummy']['_XYCoordinates'][(- 1)][0]), (self._DesignParameter['nmos_second_podummy']['_XYCoordinates'][(- 1)][0] - self._DesignParameter['nmos_second_podummy']['_XYCoordinates'][0][0])), _YWidth=(self._DesignParameter['vdd']['_XYCoordinates'][0][1] - self._DesignParameter['vss']['_XYCoordinates'][0][1]))
		self._DesignParameter['SLVT_boundary_1']['_XYCoordinates'] = [[self._DesignParameter['vss']['_XYCoordinates'][0][0], ((self._DesignParameter['vdd']['_XYCoordinates'][0][1] + self._DesignParameter['vss']['_XYCoordinates'][0][1]) / 2)]]
		self._DesignParameter['NWELL_boundary_0'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['NWELL'][0], _Datatype=DesignParameters._LayerMapping['NWELL'][1], _XWidth=(max(self._DesignParameter['vdd_odlayer']['_XWidth'], self._DesignParameter['slvtpfet_b_CDNS_637732429401_0']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth']) + (2 * drc._NwMinEnclosurePactive)), _YWidth=(((self._DesignParameter['vdd_odlayer']['_XYCoordinates'][0][1] + (self._DesignParameter['vdd_odlayer']['_YWidth'] / 2)) + drc._NwMinEnclosurePactive2) - ((self._DesignParameter['gate_input']['_XYCoordinates'][0][1] + self._DesignParameter['gate_input']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) - (self._DesignParameter['gate_input']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2))))
		self._DesignParameter['NWELL_boundary_0']['_XYCoordinates'] = [[self._DesignParameter['vss']['_XYCoordinates'][0][0], ((((self._DesignParameter['vdd_odlayer']['_XYCoordinates'][0][1] + (self._DesignParameter['vdd_odlayer']['_YWidth'] / 2)) + drc._NwMinEnclosurePactive2) + ((self._DesignParameter['gate_input']['_XYCoordinates'][0][1] + self._DesignParameter['gate_input']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) - (self._DesignParameter['gate_input']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2))) / 2)]]
		self._DesignParameter['PIMP_boundary_1'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['PIMP'][0], _Datatype=DesignParameters._LayerMapping['PIMP'][1], _XWidth=(self._DesignParameter['slvtpfet_b_CDNS_637732429401_0']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth'] + (2 * drc._PpMinExtensiononPactive)), _YWidth=(self._DesignParameter['slvtpfet_b_CDNS_637732429401_0']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth'] + (2 * drc._PpMinExtensiononPactive)))
		self._DesignParameter['PIMP_boundary_1']['_XYCoordinates'] = [[self._DesignParameter['slvtpfet_b_CDNS_637732429401_0']['_XYCoordinates'][0][0], self._DesignParameter['slvtpfet_b_CDNS_637732429401_0']['_XYCoordinates'][0][1]]]
		self._DesignParameter['vss_pplayer'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['PIMP'][0], _Datatype=DesignParameters._LayerMapping['PIMP'][1], _XWidth=(self._DesignParameter['vss_odlayer']['_XWidth'] + (2 * drc._PpMinExtensiononPactive)), _YWidth=(self._DesignParameter['vss_odlayer']['_YWidth'] + (2 * drc._PpMinExtensiononPactive)))
		self._DesignParameter['vss_pplayer']['_XYCoordinates'] = [[(+ self._DesignParameter['vss_odlayer']['_XYCoordinates'][0][0]), (+ self._DesignParameter['vss_odlayer']['_XYCoordinates'][0][1])]]
		if pmos_gate > 2:
			path_list = []
			if (len(self._DesignParameter['slvtpfet_b_CDNS_637732429401_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates']) == 1):
				mode = 'vertical'
				_width = self._DesignParameter['slvtpfet_b_CDNS_637732429401_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth']
			elif (self._DesignParameter['slvtpfet_b_CDNS_637732429401_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][0] == self._DesignParameter['slvtpfet_b_CDNS_637732429401_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][0]):
				mode = 'horizontal'
				_width = self._DesignParameter['slvtpfet_b_CDNS_637732429401_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth']
			elif (self._DesignParameter['slvtpfet_b_CDNS_637732429401_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1] == self._DesignParameter['slvtpfet_b_CDNS_637732429401_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][1]):
				mode = 'vertical'
				_width = self._DesignParameter['slvtpfet_b_CDNS_637732429401_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth']
			else:
				print('Invalid Target Input')
			if (mode == 'vertical'):
				xy_with_offset = []
				target_y_value = (0 + self._DesignParameter['pmos_drain_m1_routing_x']['_XYCoordinates'][0][0][1])
				for i in range(len(self._DesignParameter['slvtpfet_b_CDNS_637732429401_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
					if ((i % 2) == 1):
						xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['slvtpfet_b_CDNS_637732429401_0']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['slvtpfet_b_CDNS_637732429401_0']['_XYCoordinates'][0][1])], self._DesignParameter['slvtpfet_b_CDNS_637732429401_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])])
				for i in range(len(xy_with_offset)):
					path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
			elif (mode == 'horizontal'):
				xy_with_offset = []
				target_x_value = (0 + self._DesignParameter['pmos_drain_m1_routing_x']['_XYCoordinates'][0][0][0])
				for i in range(len(self._DesignParameter['slvtpfet_b_CDNS_637732429401_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
					if ((i % 2) == 1):
						xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['slvtpfet_b_CDNS_637732429401_0']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['slvtpfet_b_CDNS_637732429401_0']['_XYCoordinates'][0][1])], self._DesignParameter['slvtpfet_b_CDNS_637732429401_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])])
				for i in range(len(xy_with_offset)):
					path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
			self._DesignParameter['additional_m1_drain'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=_width)
			self._DesignParameter['additional_m1_drain']['_XYCoordinates'] = path_list
		if nmos_gate > 1:
			path_list = []
			if (len(self._DesignParameter['slvtnfet_b_CDNS_637732429400_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates']) == 1):
				mode = 'vertical'
				_width = self._DesignParameter['slvtnfet_b_CDNS_637732429400_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth']
			elif (self._DesignParameter['slvtnfet_b_CDNS_637732429400_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][0] == self._DesignParameter['slvtnfet_b_CDNS_637732429400_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][0]):
				mode = 'horizontal'
				_width = self._DesignParameter['slvtnfet_b_CDNS_637732429400_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth']
			elif (self._DesignParameter['slvtnfet_b_CDNS_637732429400_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1] == self._DesignParameter['slvtnfet_b_CDNS_637732429400_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][1]):
				mode = 'vertical'
				_width = self._DesignParameter['slvtnfet_b_CDNS_637732429400_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth']
			else:
				print('Invalid Target Input')
			if (mode == 'vertical'):
				xy_with_offset = []
				target_y_value = (0 + self._DesignParameter['nmos_source_m1_routing_x']['_XYCoordinates'][0][0][1])
				for i in range(len(self._DesignParameter['slvtnfet_b_CDNS_637732429400_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
					if ((i % 2) == 0):
						xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['slvtnfet_b_CDNS_637732429400_0']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['slvtnfet_b_CDNS_637732429400_0']['_XYCoordinates'][0][1])], self._DesignParameter['slvtnfet_b_CDNS_637732429400_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])])
				for i in range(len(xy_with_offset)):
					path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
			elif (mode == 'horizontal'):
				xy_with_offset = []
				target_x_value = (0 + self._DesignParameter['nmos_source_m1_routing_x']['_XYCoordinates'][0][0][0])
				for i in range(len(self._DesignParameter['slvtnfet_b_CDNS_637732429400_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
					if ((i % 2) == 0):
						xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['slvtnfet_b_CDNS_637732429400_0']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['slvtnfet_b_CDNS_637732429400_0']['_XYCoordinates'][0][1])], self._DesignParameter['slvtnfet_b_CDNS_637732429400_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])])
				for i in range(len(xy_with_offset)):
					path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
			self._DesignParameter['additional_m1_source'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=_width)
			self._DesignParameter['additional_m1_source']['_XYCoordinates'] = path_list
		