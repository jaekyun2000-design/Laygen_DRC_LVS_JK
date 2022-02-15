from generatorLib import StickDiagram
from generatorLib import DesignParameters
import copy
import math
from generatorLib import DRC
from generatorLib.generator_models import Z_PWR_CNT
from generatorLib.generator_models import ViaPoly2Met1
from generatorLib.generator_models import NMOSWithDummy
from generatorLib.generator_models import PMOSWithDummy

class EasyDebugModule(StickDiagram._StickDiagram):
	def __init__(self, _DesignParameter=None, _Name='EasyDebugModule'):
		if _DesignParameter != None:
			self._DesignParameter = _DesignParameter
		else:
			self._DesignParameter = dict(_Name=self._NameDeclaration(_Name=_Name), _GDSFile=self._GDSObjDeclaration(_GDSFile=None))
		self._DesignParameter['_Name']['Name'] = _Name

	def _CalculateDesignParameter(self,gate_spacing=120,nmos_width1=270,nmos_width2=270,pmos_width1=360,pmos_width2=180,nmos1_y=375,nmos2_y=375,pmos1_y=410,pmos2_y=500,gate_a=5,gate_b=2,gate_c=3,vss2vdd_height=1800,sdwidth=66,supply_xdistance=300,length=30,RVT=None,gate_y=860,nmos_width3=270,pmos_width3=270,nmos3_y=375,pmos3_y=410):
	
		drc = DRC.DRC()
		_Name = self._DesignParameter['_Name']['_Name']
		
		self._DesignParameter['nmos1'] = self._SrefElementDeclaration(_DesignObj=NMOSWithDummy._NMOS(_Name='nmos1In{}'.format(_Name)))[0]
		self._DesignParameter['nmos1']['_DesignObj']._CalculateNMOSDesignParameter(**dict(_NMOSNumberofGate=gate_c, _NMOSChannelWidth=nmos_width1, _NMOSChannellength=length, _NMOSDummy=True, _GateSpacing=gate_spacing, _SDWidth=sdwidth, _XVT='RVT'))
		self._DesignParameter['nmos1']['_XYCoordinates'] = [[0, nmos1_y]]
		self._DesignParameter['nmos3'] = self._SrefElementDeclaration(_DesignObj=NMOSWithDummy._NMOS(_Name='nmos3In{}'.format(_Name)))[0]
		self._DesignParameter['nmos3']['_DesignObj']._CalculateNMOSDesignParameter(**dict(_NMOSNumberofGate=gate_b, _NMOSChannelWidth=nmos_width3, _NMOSChannellength=length, _NMOSDummy=True, _GateSpacing=gate_spacing, _SDWidth=sdwidth, _XVT='RVT', _PCCrit=False))
		self._DesignParameter['nmos3']['_XYCoordinates'] = [[((self._DesignParameter['nmos1']['_XYCoordinates'][0][0] + self._DesignParameter['nmos1']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][(- 1)][0]) + self._DesignParameter['nmos3']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][(- 1)][0]), nmos3_y]]
		self._DesignParameter['nmos2'] = self._SrefElementDeclaration(_DesignObj=NMOSWithDummy._NMOS(_Name='nmos2In{}'.format(_Name)))[0]
		self._DesignParameter['nmos2']['_DesignObj']._CalculateNMOSDesignParameter(**dict(_NMOSNumberofGate=gate_a, _NMOSChannelWidth=nmos_width2, _NMOSChannellength=length, _NMOSDummy=True, _GateSpacing=gate_spacing, _SDWidth=sdwidth, _XVT='RVT'))
		self._DesignParameter['nmos2']['_XYCoordinates'] = [[((self._DesignParameter['nmos3']['_XYCoordinates'][0][0] + self._DesignParameter['nmos3']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][(- 1)][0]) + self._DesignParameter['nmos2']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][(- 1)][0]), nmos2_y]]
		self._DesignParameter['nmos1']['_XYCoordinates'] = [[(((- ((self._DesignParameter['nmos1']['_XYCoordinates'][0][0] + self._DesignParameter['nmos1']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][0]) + (self._DesignParameter['nmos2']['_XYCoordinates'][0][0] + self._DesignParameter['nmos2']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][(- 1)][0]))) / 2) + self._DesignParameter['nmos1']['_XYCoordinates'][0][0]), nmos1_y]]
		self._DesignParameter['nmos3']['_XYCoordinates'] = [[((self._DesignParameter['nmos1']['_XYCoordinates'][0][0] + self._DesignParameter['nmos1']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][(- 1)][0]) + self._DesignParameter['nmos3']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][(- 1)][0]), nmos3_y]]
		self._DesignParameter['nmos2']['_XYCoordinates'] = [[((self._DesignParameter['nmos3']['_XYCoordinates'][0][0] + self._DesignParameter['nmos3']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][(- 1)][0]) + self._DesignParameter['nmos2']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][(- 1)][0]), nmos2_y]]
		self._DesignParameter['pmos1'] = self._SrefElementDeclaration(_DesignObj=PMOSWithDummy._PMOS(_Name='pmos1In{}'.format(_Name)))[0]
		self._DesignParameter['pmos1']['_DesignObj']._CalculatePMOSDesignParameter(**dict(_PMOSNumberofGate=gate_c, _PMOSChannelWidth=pmos_width1, _PMOSChannellength=length, _PMOSDummy=True, _GateSpacing=gate_spacing, _SDWidth=sdwidth, _XVT='RVT', _PCCrit=False))
		self._DesignParameter['pmos1']['_XYCoordinates'] = [[self._DesignParameter['nmos1']['_XYCoordinates'][0][0], (vss2vdd_height - pmos1_y)]]
		self._DesignParameter['pmos3'] = self._SrefElementDeclaration(_DesignObj=PMOSWithDummy._PMOS(_Name='pmos3In{}'.format(_Name)))[0]
		self._DesignParameter['pmos3']['_DesignObj']._CalculatePMOSDesignParameter(**dict(_PMOSNumberofGate=gate_b, _PMOSChannelWidth=pmos_width2, _PMOSChannellength=length, _PMOSDummy=True, _GateSpacing=gate_spacing, _SDWidth=sdwidth, _XVT='RVT', _PCCrit=False))
		self._DesignParameter['pmos3']['_XYCoordinates'] = [[self._DesignParameter['nmos3']['_XYCoordinates'][0][0], (vss2vdd_height - pmos3_y)]]
		self._DesignParameter['pmos2'] = self._SrefElementDeclaration(_DesignObj=PMOSWithDummy._PMOS(_Name='pmos2In{}'.format(_Name)))[0]
		self._DesignParameter['pmos2']['_DesignObj']._CalculatePMOSDesignParameter(**dict(_PMOSNumberofGate=gate_a, _PMOSChannelWidth=pmos_width2, _PMOSChannellength=length, _PMOSDummy=True, _GateSpacing=gate_spacing, _SDWidth=sdwidth, _XVT='RVT'))
		self._DesignParameter['pmos2']['_XYCoordinates'] = [[self._DesignParameter['nmos2']['_XYCoordinates'][0][0], (vss2vdd_height - pmos2_y)]]
		XYList = []
		xy_offset = (0, (- nmos1_y))
		for i in range(len(self._DesignParameter['nmos1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		    if ((i % 2) == 0):
		        xy = (self._DesignParameter['nmos1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i][0] if (type(self._DesignParameter['nmos1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i][0]) == list) else self._DesignParameter['nmos1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])
		        XYList.append([((x + y) + z) for (x, y, z) in zip([(0 + self._DesignParameter['nmos1']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['nmos1']['_XYCoordinates'][0][1])], xy, xy_offset)])
		self._DesignParameter['vss'] = self._SrefElementDeclaration(_DesignObj=Z_PWR_CNT.Z_PWR_CNT(_Name='vssIn{}'.format(_Name)))[0]
		self._DesignParameter['vss']['_DesignObj']._CalculateDesignParameter(**dict(_Xnum=1, _Xdistance=0))
		self._DesignParameter['vss']['_XYCoordinates'] = XYList
		XYList = []
		xy_offset = (0, pmos1_y)
		for i in range(len(self._DesignParameter['pmos1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		    if ((i % 2) == 0):
		        xy = (self._DesignParameter['pmos1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i][0] if (type(self._DesignParameter['pmos1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i][0]) == list) else self._DesignParameter['pmos1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])
		        XYList.append([((x + y) + z) for (x, y, z) in zip([(0 + self._DesignParameter['pmos1']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['pmos1']['_XYCoordinates'][0][1])], xy, xy_offset)])
		self._DesignParameter['vdd'] = self._SrefElementDeclaration(_DesignObj=Z_PWR_CNT.Z_PWR_CNT(_Name='vddIn{}'.format(_Name)))[0]
		self._DesignParameter['vdd']['_DesignObj']._CalculateDesignParameter(**dict(_Xnum=1, _Xdistance=0))
		self._DesignParameter['vdd']['_XYCoordinates'] = XYList
		XYList = []
		xy_offset = (0, pmos2_y)
		for i in range(len(self._DesignParameter['pmos2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		    if ((i % 2) == 0):
		        xy = (self._DesignParameter['pmos2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i][0] if (type(self._DesignParameter['pmos2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i][0]) == list) else self._DesignParameter['pmos2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])
		        XYList.append([((x + y) + z) for (x, y, z) in zip([(0 + self._DesignParameter['pmos2']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['pmos2']['_XYCoordinates'][0][1])], xy, xy_offset)])
		self._DesignParameter['extra_vdd'] = self._SrefElementDeclaration(_DesignObj=Z_PWR_CNT.Z_PWR_CNT(_Name='extra_vddIn{}'.format(_Name)))[0]
		self._DesignParameter['extra_vdd']['_DesignObj']._CalculateDesignParameter(**dict(_Xnum=1, _Xdistance=0))
		self._DesignParameter['extra_vdd']['_XYCoordinates'] = XYList
		XYList = []
		xy_offset = (0, pmos3_y)
		for i in range(len(self._DesignParameter['pmos3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		    if ((i % 2) == 0):
		        xy = (self._DesignParameter['pmos3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i][0] if (type(self._DesignParameter['pmos3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i][0]) == list) else self._DesignParameter['pmos3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])
		        XYList.append([((x + y) + z) for (x, y, z) in zip([(0 + self._DesignParameter['pmos3']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['pmos3']['_XYCoordinates'][0][1])], xy, xy_offset)])
		self._DesignParameter['pmos2_vdd'] = self._SrefElementDeclaration(_DesignObj=Z_PWR_CNT.Z_PWR_CNT(_Name='pmos2_vddIn{}'.format(_Name)))[0]
		self._DesignParameter['pmos2_vdd']['_DesignObj']._CalculateDesignParameter(**dict(_Xnum=1, _Xdistance=0))
		self._DesignParameter['pmos2_vdd']['_XYCoordinates'] = XYList
		path_list = []
		if (len(self._DesignParameter['pmos1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates']) == 1):
		    mode = 'vertical'
		    _width = self._DesignParameter['pmos1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth']
		elif (self._DesignParameter['pmos1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][0] == self._DesignParameter['pmos1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][0]):
		    mode = 'horizontal'
		    _width = self._DesignParameter['pmos1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth']
		elif (self._DesignParameter['pmos1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1] == self._DesignParameter['pmos1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][1]):
		    mode = 'vertical'
		    _width = self._DesignParameter['pmos1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth']
		else:
		    print('Invalid Target Input')
		if (mode == 'vertical'):
		    xy_with_offset = []
		    target_y_value = (0 + self._DesignParameter['vdd']['_XYCoordinates'][0][1])
		    for i in range(len(self._DesignParameter['pmos1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		        if ((i % 2) == 0):
		            xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['pmos1']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['pmos1']['_XYCoordinates'][0][1])], self._DesignParameter['pmos1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		elif (mode == 'horizontal'):
		    xy_with_offset = []
		    target_x_value = (0 + self._DesignParameter['vdd']['_XYCoordinates'][0][0])
		    for i in range(len(self._DesignParameter['pmos1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		        if ((i % 2) == 0):
		            xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['pmos1']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['pmos1']['_XYCoordinates'][0][1])], self._DesignParameter['pmos1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		self._DesignParameter['m1_vdd_routing'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=_width)
		self._DesignParameter['m1_vdd_routing']['_XYCoordinates'] = path_list
		path_list = []
		if (len(self._DesignParameter['pmos2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates']) == 1):
		    mode = 'vertical'
		    _width = self._DesignParameter['pmos2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth']
		elif (self._DesignParameter['pmos2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][0] == self._DesignParameter['pmos2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][0]):
		    mode = 'horizontal'
		    _width = self._DesignParameter['pmos2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth']
		elif (self._DesignParameter['pmos2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1] == self._DesignParameter['pmos2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][1]):
		    mode = 'vertical'
		    _width = self._DesignParameter['pmos2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth']
		else:
		    print('Invalid Target Input')
		if (mode == 'vertical'):
		    xy_with_offset = []
		    target_y_value = (0 + self._DesignParameter['extra_vdd']['_XYCoordinates'][0][1])
		    for i in range(len(self._DesignParameter['pmos2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		        if ((i % 2) == 0):
		            xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['pmos2']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['pmos2']['_XYCoordinates'][0][1])], self._DesignParameter['pmos2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		elif (mode == 'horizontal'):
		    xy_with_offset = []
		    target_x_value = (0 + self._DesignParameter['extra_vdd']['_XYCoordinates'][0][0])
		    for i in range(len(self._DesignParameter['pmos2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		        if ((i % 2) == 0):
		            xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['pmos2']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['pmos2']['_XYCoordinates'][0][1])], self._DesignParameter['pmos2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		self._DesignParameter['m1_extra_vdd_routing'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=_width)
		self._DesignParameter['m1_extra_vdd_routing']['_XYCoordinates'] = path_list
		self._DesignParameter['m1_pmos_parallel_routing_x'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=74)
		self._DesignParameter['m1_pmos_parallel_routing_x']['_XYCoordinates'] = [[[((self._DesignParameter['pmos1']['_XYCoordinates'][0][0] + self._DesignParameter['pmos1']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][0][0]) - (self._DesignParameter['pmos1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth'] / 2)), ((min(((self._DesignParameter['pmos1']['_XYCoordinates'][0][1] + self._DesignParameter['pmos1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1]) - (self._DesignParameter['pmos1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_YWidth'] / 2)), ((self._DesignParameter['pmos2']['_XYCoordinates'][0][1] + self._DesignParameter['pmos2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1]) - (self._DesignParameter['pmos2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_YWidth'] / 2)), ((self._DesignParameter['pmos3']['_XYCoordinates'][0][1] + self._DesignParameter['pmos3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1]) - (self._DesignParameter['pmos3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_YWidth'] / 2))) - (self._DesignParameter['m1_pmos_parallel_routing_x']['_Width'] / 2)) - drc._Metal1MinSpace2)], [((self._DesignParameter['pmos2']['_XYCoordinates'][0][0] + self._DesignParameter['pmos2']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][(- 1)][0]) + (self._DesignParameter['pmos2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth'] / 2)), ((min(((self._DesignParameter['pmos2']['_XYCoordinates'][0][1] + self._DesignParameter['pmos2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1]) - (self._DesignParameter['pmos2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_YWidth'] / 2)), ((self._DesignParameter['pmos1']['_XYCoordinates'][0][1] + self._DesignParameter['pmos1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1]) - (self._DesignParameter['pmos1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_YWidth'] / 2)), ((self._DesignParameter['pmos3']['_XYCoordinates'][0][1] + self._DesignParameter['pmos3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1]) - (self._DesignParameter['pmos3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_YWidth'] / 2))) - (self._DesignParameter['m1_pmos_parallel_routing_x']['_Width'] / 2)) - drc._Metal1MinSpace2)]]]
		path_list = []
		if (len(self._DesignParameter['pmos3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates']) == 1):
		    mode = 'vertical'
		    _width = self._DesignParameter['pmos3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth']
		elif (self._DesignParameter['pmos3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][0] == self._DesignParameter['pmos3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][0]):
		    mode = 'horizontal'
		    _width = self._DesignParameter['pmos3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth']
		elif (self._DesignParameter['pmos3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1] == self._DesignParameter['pmos3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][1]):
		    mode = 'vertical'
		    _width = self._DesignParameter['pmos3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth']
		else:
		    print('Invalid Target Input')
		if (mode == 'vertical'):
		    xy_with_offset = []
		    target_y_value = (0 + self._DesignParameter['pmos2_vdd']['_XYCoordinates'][0][1])
		    for i in range(len(self._DesignParameter['pmos3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		        if ((i % 2) == 0):
		            xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['pmos3']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['pmos3']['_XYCoordinates'][0][1])], self._DesignParameter['pmos3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		elif (mode == 'horizontal'):
		    xy_with_offset = []
		    target_x_value = (0 + self._DesignParameter['pmos2_vdd']['_XYCoordinates'][0][0])
		    for i in range(len(self._DesignParameter['pmos3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		        if ((i % 2) == 0):
		            xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['pmos3']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['pmos3']['_XYCoordinates'][0][1])], self._DesignParameter['pmos3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		self._DesignParameter['m1_pmos3_vdd_routing'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=_width)
		self._DesignParameter['m1_pmos3_vdd_routing']['_XYCoordinates'] = path_list
		path_list = []
		if (len(self._DesignParameter['pmos1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates']) == 1):
		    mode = 'vertical'
		    _width = self._DesignParameter['pmos1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth']
		elif (self._DesignParameter['pmos1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][0] == self._DesignParameter['pmos1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][0]):
		    mode = 'horizontal'
		    _width = self._DesignParameter['pmos1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth']
		elif (self._DesignParameter['pmos1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1] == self._DesignParameter['pmos1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][1]):
		    mode = 'vertical'
		    _width = self._DesignParameter['pmos1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth']
		else:
		    print('Invalid Target Input')
		if (mode == 'vertical'):
		    xy_with_offset = []
		    target_y_value = (0 + self._DesignParameter['m1_pmos_parallel_routing_x']['_XYCoordinates'][0][0][1])
		    for i in range(len(self._DesignParameter['pmos1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		        if ((i % 2) == 1):
		            xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['pmos1']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['pmos1']['_XYCoordinates'][0][1])], self._DesignParameter['pmos1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		elif (mode == 'horizontal'):
		    xy_with_offset = []
		    target_x_value = (0 + self._DesignParameter['m1_pmos_parallel_routing_x']['_XYCoordinates'][0][0][0])
		    for i in range(len(self._DesignParameter['pmos1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		        if ((i % 2) == 1):
		            xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['pmos1']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['pmos1']['_XYCoordinates'][0][1])], self._DesignParameter['pmos1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		self._DesignParameter['m1_pmos1_out_routing'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=_width)
		self._DesignParameter['m1_pmos1_out_routing']['_XYCoordinates'] = path_list
		path_list = []
		if (len(self._DesignParameter['pmos3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates']) == 1):
		    mode = 'vertical'
		    _width = self._DesignParameter['pmos3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth']
		elif (self._DesignParameter['pmos3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][0] == self._DesignParameter['pmos3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][0]):
		    mode = 'horizontal'
		    _width = self._DesignParameter['pmos3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth']
		elif (self._DesignParameter['pmos3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1] == self._DesignParameter['pmos3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][1]):
		    mode = 'vertical'
		    _width = self._DesignParameter['pmos3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth']
		else:
		    print('Invalid Target Input')
		if (mode == 'vertical'):
		    xy_with_offset = []
		    target_y_value = (0 + self._DesignParameter['m1_pmos_parallel_routing_x']['_XYCoordinates'][0][0][1])
		    for i in range(len(self._DesignParameter['pmos3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		        if ((i % 2) == 1):
		            xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['pmos3']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['pmos3']['_XYCoordinates'][0][1])], self._DesignParameter['pmos3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		elif (mode == 'horizontal'):
		    xy_with_offset = []
		    target_x_value = (0 + self._DesignParameter['m1_pmos_parallel_routing_x']['_XYCoordinates'][0][0][0])
		    for i in range(len(self._DesignParameter['pmos3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		        if ((i % 2) == 1):
		            xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['pmos3']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['pmos3']['_XYCoordinates'][0][1])], self._DesignParameter['pmos3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		self._DesignParameter['m1_pmos3_out_routing'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=_width)
		self._DesignParameter['m1_pmos3_out_routing']['_XYCoordinates'] = path_list
		path_list = []
		if (len(self._DesignParameter['nmos2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates']) == 1):
		    mode = 'vertical'
		    _width = self._DesignParameter['nmos2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth']
		elif (self._DesignParameter['nmos2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][0] == self._DesignParameter['nmos2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][0]):
		    mode = 'horizontal'
		    _width = self._DesignParameter['nmos2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth']
		elif (self._DesignParameter['nmos2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1] == self._DesignParameter['nmos2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][1]):
		    mode = 'vertical'
		    _width = self._DesignParameter['nmos2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth']
		else:
		    print('Invalid Target Input')
		if (mode == 'vertical'):
		    xy_with_offset = []
		    target_y_value = (0 + self._DesignParameter['pmos2']['_XYCoordinates'][0][1])
		    for i in range(len(self._DesignParameter['nmos2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		        if ((i % 2) == 1):
		            xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['nmos2']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['nmos2']['_XYCoordinates'][0][1])], self._DesignParameter['nmos2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		elif (mode == 'horizontal'):
		    xy_with_offset = []
		    target_x_value = (0 + self._DesignParameter['pmos2']['_XYCoordinates'][0][0])
		    for i in range(len(self._DesignParameter['nmos2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		        if ((i % 2) == 1):
		            xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['nmos2']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['nmos2']['_XYCoordinates'][0][1])], self._DesignParameter['nmos2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		self._DesignParameter['m1_nmos1_out'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=_width)
		self._DesignParameter['m1_nmos1_out']['_XYCoordinates'] = path_list
		self._DesignParameter['gate_a_input'] = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_Name='gate_a_inputIn{}'.format(_Name)))[0]
		self._DesignParameter['gate_a_input']['_DesignObj']._CalculateViaPoly2Met1DesignParameterMinimumEnclosureX(**dict(_ViaPoly2Met1NumberOfCOX=1, _ViaPoly2Met1NumberOfCOY=2))
		if gate_a%2==0:
			gate_a_x=(self._DesignParameter['nmos1']['_XYCoordinates'][0][0] + self._DesignParameter['nmos1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][0])
		elif gate_a%2!=0:
			gate_a_x=(self._DesignParameter['nmos1']['_XYCoordinates'][0][0] + self._DesignParameter['nmos1']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][-1][0])
		self._DesignParameter['gate_a_input']['_XYCoordinates'] = [[gate_a_x, gate_y]]
		self._DesignParameter['gate_b_input'] = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_Name='gate_b_inputIn{}'.format(_Name)))[0]
		self._DesignParameter['gate_b_input']['_DesignObj']._CalculateViaPoly2Met1DesignParameterMinimumEnclosureX(**dict(_ViaPoly2Met1NumberOfCOX=1, _ViaPoly2Met1NumberOfCOY=2))
		self._DesignParameter['gate_b_input']['_XYCoordinates'] = [[(self._DesignParameter['pmos3']['_XYCoordinates'][0][0] + self._DesignParameter['pmos3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][0]), gate_y]]
		self._DesignParameter['gate_c_input'] = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_Name='gate_c_inputIn{}'.format(_Name)))[0]
		self._DesignParameter['gate_c_input']['_DesignObj']._CalculateViaPoly2Met1DesignParameterMinimumEnclosureX(**dict(_ViaPoly2Met1NumberOfCOX=1, _ViaPoly2Met1NumberOfCOY=2))
		self._DesignParameter['gate_c_input']['_XYCoordinates'] = [[(self._DesignParameter['nmos2']['_XYCoordinates'][0][0] + self._DesignParameter['nmos2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][0]), gate_y]]
		self._DesignParameter['poly_input_a'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _Width=50)
		self._DesignParameter['poly_input_a']['_XYCoordinates'] = [[[((self._DesignParameter['gate_a_input']['_XYCoordinates'][0][0] + self._DesignParameter['gate_a_input']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['gate_a_input']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)), ((self._DesignParameter['gate_a_input']['_XYCoordinates'][0][1] + self._DesignParameter['gate_a_input']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1]) - (self._DesignParameter['gate_a_input']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2))], [((self._DesignParameter['pmos1']['_XYCoordinates'][0][0] + self._DesignParameter['pmos1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]) + (self._DesignParameter['pmos1']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)), ((self._DesignParameter['gate_a_input']['_XYCoordinates'][0][1] + self._DesignParameter['gate_a_input']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1]) - (self._DesignParameter['gate_a_input']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2))]], [[((self._DesignParameter['gate_a_input']['_XYCoordinates'][0][0] + self._DesignParameter['gate_a_input']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['gate_a_input']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)), ((self._DesignParameter['gate_a_input']['_XYCoordinates'][0][1] + self._DesignParameter['gate_a_input']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1]) + (self._DesignParameter['gate_a_input']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2))], [((self._DesignParameter['pmos1']['_XYCoordinates'][0][0] + self._DesignParameter['pmos1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]) + (self._DesignParameter['pmos1']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)), ((self._DesignParameter['gate_a_input']['_XYCoordinates'][0][1] + self._DesignParameter['gate_a_input']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1]) + (self._DesignParameter['gate_a_input']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2))]]]
		self._DesignParameter['poly_input_b'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _Width=50)
		self._DesignParameter['poly_input_b']['_XYCoordinates'] = [[[((self._DesignParameter['gate_b_input']['_XYCoordinates'][0][0] + self._DesignParameter['gate_b_input']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['gate_b_input']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)), ((self._DesignParameter['gate_b_input']['_XYCoordinates'][0][1] + self._DesignParameter['gate_b_input']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1]) - (self._DesignParameter['gate_b_input']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2))], [((self._DesignParameter['nmos3']['_XYCoordinates'][0][0] + self._DesignParameter['nmos3']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]) + (self._DesignParameter['nmos3']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)), ((self._DesignParameter['gate_b_input']['_XYCoordinates'][0][1] + self._DesignParameter['gate_b_input']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1]) - (self._DesignParameter['gate_b_input']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2))]], [[((self._DesignParameter['gate_b_input']['_XYCoordinates'][0][0] + self._DesignParameter['gate_b_input']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['gate_b_input']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)), ((self._DesignParameter['gate_b_input']['_XYCoordinates'][0][1] + self._DesignParameter['gate_b_input']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1]) + (self._DesignParameter['gate_b_input']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2))], [((self._DesignParameter['pmos3']['_XYCoordinates'][0][0] + self._DesignParameter['pmos3']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]) + (self._DesignParameter['pmos3']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)), ((self._DesignParameter['gate_b_input']['_XYCoordinates'][0][1] + self._DesignParameter['gate_b_input']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1]) + (self._DesignParameter['gate_b_input']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2))]]]
		self._DesignParameter['poly_input_c'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _Width=50)
		self._DesignParameter['poly_input_c']['_XYCoordinates'] = [[[((self._DesignParameter['gate_c_input']['_XYCoordinates'][0][0] + self._DesignParameter['gate_c_input']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) + (self._DesignParameter['gate_c_input']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)), ((self._DesignParameter['gate_c_input']['_XYCoordinates'][0][1] + self._DesignParameter['gate_c_input']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1]) - (self._DesignParameter['gate_c_input']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2))], [((self._DesignParameter['nmos2']['_XYCoordinates'][0][0] + self._DesignParameter['nmos2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['nmos2']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)), ((self._DesignParameter['gate_c_input']['_XYCoordinates'][0][1] + self._DesignParameter['gate_c_input']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1]) - (self._DesignParameter['gate_c_input']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2))]], [[((self._DesignParameter['gate_c_input']['_XYCoordinates'][0][0] + self._DesignParameter['gate_c_input']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) + (self._DesignParameter['gate_c_input']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)), ((self._DesignParameter['gate_c_input']['_XYCoordinates'][0][1] + self._DesignParameter['gate_c_input']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1]) + (self._DesignParameter['gate_c_input']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2))], [((self._DesignParameter['pmos2']['_XYCoordinates'][0][0] + self._DesignParameter['pmos2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['pmos2']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)), ((self._DesignParameter['gate_c_input']['_XYCoordinates'][0][1] + self._DesignParameter['gate_c_input']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1]) + (self._DesignParameter['gate_c_input']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2))]]]
		path_list = []
		if (len(self._DesignParameter['pmos1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates']) == 1):
		    mode = 'vertical'
		    _width = self._DesignParameter['pmos1']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
		elif (self._DesignParameter['pmos1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0] == self._DesignParameter['pmos1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]):
		    mode = 'horizontal'
		    _width = self._DesignParameter['pmos1']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
		elif (self._DesignParameter['pmos1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1] == self._DesignParameter['pmos1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][1]):
		    mode = 'vertical'
		    _width = self._DesignParameter['pmos1']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
		else:
		    print('Invalid Target Input')
		if (mode == 'vertical'):
		    xy_with_offset = []
		    target_y_value = (0 + self._DesignParameter['poly_input_a']['_XYCoordinates'][(- 1)][0][1])
		    for i in range(len(self._DesignParameter['pmos1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
		        xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['pmos1']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['pmos1']['_XYCoordinates'][0][1])], self._DesignParameter['pmos1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		elif (mode == 'horizontal'):
		    xy_with_offset = []
		    target_x_value = (0 + self._DesignParameter['poly_input_a']['_XYCoordinates'][(- 1)][0][0])
		    for i in range(len(self._DesignParameter['pmos1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
		        xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['pmos1']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['pmos1']['_XYCoordinates'][0][1])], self._DesignParameter['pmos1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		self._DesignParameter['poly_pmos_routing_y'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _Width=_width)
		self._DesignParameter['poly_pmos_routing_y']['_XYCoordinates'] = path_list
		path_list = []
		if (len(self._DesignParameter['nmos1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates']) == 1):
		    mode = 'vertical'
		    _width = self._DesignParameter['nmos1']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
		elif (self._DesignParameter['nmos1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0] == self._DesignParameter['nmos1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]):
		    mode = 'horizontal'
		    _width = self._DesignParameter['nmos1']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
		elif (self._DesignParameter['nmos1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1] == self._DesignParameter['nmos1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][1]):
		    mode = 'vertical'
		    _width = self._DesignParameter['nmos1']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
		else:
		    print('Invalid Target Input')
		if (mode == 'vertical'):
		    xy_with_offset = []
		    target_y_value = (0 + self._DesignParameter['poly_input_a']['_XYCoordinates'][0][0][1])
		    for i in range(len(self._DesignParameter['nmos1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
		        xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['nmos1']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['nmos1']['_XYCoordinates'][0][1])], self._DesignParameter['nmos1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		elif (mode == 'horizontal'):
		    xy_with_offset = []
		    target_x_value = (0 + self._DesignParameter['poly_input_a']['_XYCoordinates'][0][0][0])
		    for i in range(len(self._DesignParameter['nmos1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
		        xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['nmos1']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['nmos1']['_XYCoordinates'][0][1])], self._DesignParameter['nmos1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		self._DesignParameter['poly_nmos_input_a'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _Width=_width)
		self._DesignParameter['poly_nmos_input_a']['_XYCoordinates'] = path_list
		path_list = []
		if (len(self._DesignParameter['pmos2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates']) == 1):
		    mode = 'vertical'
		    _width = self._DesignParameter['pmos2']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
		elif (self._DesignParameter['pmos2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0] == self._DesignParameter['pmos2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]):
		    mode = 'horizontal'
		    _width = self._DesignParameter['pmos2']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
		elif (self._DesignParameter['pmos2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1] == self._DesignParameter['pmos2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][1]):
		    mode = 'vertical'
		    _width = self._DesignParameter['pmos2']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
		else:
		    print('Invalid Target Input')
		if (mode == 'vertical'):
		    xy_with_offset = []
		    target_y_value = (0 + self._DesignParameter['poly_input_c']['_XYCoordinates'][(- 1)][0][1])
		    for i in range(len(self._DesignParameter['pmos2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
		        xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['pmos2']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['pmos2']['_XYCoordinates'][0][1])], self._DesignParameter['pmos2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		elif (mode == 'horizontal'):
		    xy_with_offset = []
		    target_x_value = (0 + self._DesignParameter['poly_input_c']['_XYCoordinates'][(- 1)][0][0])
		    for i in range(len(self._DesignParameter['pmos2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
		        xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['pmos2']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['pmos2']['_XYCoordinates'][0][1])], self._DesignParameter['pmos2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		self._DesignParameter['poly_pmos_c_routing_y'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _Width=_width)
		self._DesignParameter['poly_pmos_c_routing_y']['_XYCoordinates'] = path_list
		path_list = []
		if (len(self._DesignParameter['nmos2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates']) == 1):
		    mode = 'vertical'
		    _width = self._DesignParameter['nmos2']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
		elif (self._DesignParameter['nmos2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0] == self._DesignParameter['nmos2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]):
		    mode = 'horizontal'
		    _width = self._DesignParameter['nmos2']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
		elif (self._DesignParameter['nmos2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1] == self._DesignParameter['nmos2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][1]):
		    mode = 'vertical'
		    _width = self._DesignParameter['nmos2']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
		else:
		    print('Invalid Target Input')
		if (mode == 'vertical'):
		    xy_with_offset = []
		    target_y_value = (0 + self._DesignParameter['poly_input_c']['_XYCoordinates'][0][0][1])
		    for i in range(len(self._DesignParameter['nmos2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
		        xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['nmos2']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['nmos2']['_XYCoordinates'][0][1])], self._DesignParameter['nmos2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		elif (mode == 'horizontal'):
		    xy_with_offset = []
		    target_x_value = (0 + self._DesignParameter['poly_input_c']['_XYCoordinates'][0][0][0])
		    for i in range(len(self._DesignParameter['nmos2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
		        xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['nmos2']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['nmos2']['_XYCoordinates'][0][1])], self._DesignParameter['nmos2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		self._DesignParameter['poly_nmos_c_routing_y'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _Width=_width)
		self._DesignParameter['poly_nmos_c_routing_y']['_XYCoordinates'] = path_list
		path_list = []
		if (len(self._DesignParameter['nmos3']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates']) == 1):
		    mode = 'vertical'
		    _width = self._DesignParameter['nmos3']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
		elif (self._DesignParameter['nmos3']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0] == self._DesignParameter['nmos3']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]):
		    mode = 'horizontal'
		    _width = self._DesignParameter['nmos3']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
		elif (self._DesignParameter['nmos3']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1] == self._DesignParameter['nmos3']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][1]):
		    mode = 'vertical'
		    _width = self._DesignParameter['nmos3']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
		else:
		    print('Invalid Target Input')
		if (mode == 'vertical'):
		    xy_with_offset = []
		    target_y_value = (0 + self._DesignParameter['poly_input_b']['_XYCoordinates'][0][0][1])
		    for i in range(len(self._DesignParameter['nmos3']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
		        xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['nmos3']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['nmos3']['_XYCoordinates'][0][1])], self._DesignParameter['nmos3']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		elif (mode == 'horizontal'):
		    xy_with_offset = []
		    target_x_value = (0 + self._DesignParameter['poly_input_b']['_XYCoordinates'][0][0][0])
		    for i in range(len(self._DesignParameter['nmos3']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
		        xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['nmos3']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['nmos3']['_XYCoordinates'][0][1])], self._DesignParameter['nmos3']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		self._DesignParameter['poly_nmos_routing_y'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _Width=_width)
		self._DesignParameter['poly_nmos_routing_y']['_XYCoordinates'] = path_list
		path_list = []
		if (len(self._DesignParameter['pmos3']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates']) == 1):
		    mode = 'vertical'
		    _width = self._DesignParameter['pmos3']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
		elif (self._DesignParameter['pmos3']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0] == self._DesignParameter['pmos3']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]):
		    mode = 'horizontal'
		    _width = self._DesignParameter['pmos3']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
		elif (self._DesignParameter['pmos3']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1] == self._DesignParameter['pmos3']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][1]):
		    mode = 'vertical'
		    _width = self._DesignParameter['pmos3']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
		else:
		    print('Invalid Target Input')
		if (mode == 'vertical'):
		    xy_with_offset = []
		    target_y_value = (0 + self._DesignParameter['poly_input_b']['_XYCoordinates'][(- 1)][0][1])
		    for i in range(len(self._DesignParameter['pmos3']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
		        xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['pmos3']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['pmos3']['_XYCoordinates'][0][1])], self._DesignParameter['pmos3']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		elif (mode == 'horizontal'):
		    xy_with_offset = []
		    target_x_value = (0 + self._DesignParameter['poly_input_b']['_XYCoordinates'][(- 1)][0][0])
		    for i in range(len(self._DesignParameter['pmos3']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
		        xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['pmos3']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['pmos3']['_XYCoordinates'][0][1])], self._DesignParameter['pmos3']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		self._DesignParameter['poly_pmos3_input'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _Width=_width)
		self._DesignParameter['poly_pmos3_input']['_XYCoordinates'] = path_list
		path_list = []
		if (len(self._DesignParameter['nmos1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates']) == 1):
		    mode = 'vertical'
		    _width = self._DesignParameter['nmos1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth']
		elif (self._DesignParameter['nmos1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][0] == self._DesignParameter['nmos1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][0]):
		    mode = 'horizontal'
		    _width = self._DesignParameter['nmos1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth']
		elif (self._DesignParameter['nmos1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1] == self._DesignParameter['nmos1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][1]):
		    mode = 'vertical'
		    _width = self._DesignParameter['nmos1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth']
		else:
		    print('Invalid Target Input')
		if (mode == 'vertical'):
		    xy_with_offset = []
		    target_y_value = (0 + self._DesignParameter['vss']['_XYCoordinates'][0][1])
		    for i in range(len(self._DesignParameter['nmos1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		        if ((i % 2) == 0):
		            xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['nmos1']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['nmos1']['_XYCoordinates'][0][1])], self._DesignParameter['nmos1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		elif (mode == 'horizontal'):
		    xy_with_offset = []
		    target_x_value = (0 + self._DesignParameter['vss']['_XYCoordinates'][0][0])
		    for i in range(len(self._DesignParameter['nmos1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		        if ((i % 2) == 0):
		            xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['nmos1']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['nmos1']['_XYCoordinates'][0][1])], self._DesignParameter['nmos1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		self._DesignParameter['nmos1_vss_routing'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=_width)
		self._DesignParameter['nmos1_vss_routing']['_XYCoordinates'] = path_list
		self._DesignParameter['supply_od'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['DIFF'][0], _Datatype=DesignParameters._LayerMapping['DIFF'][1], _XWidth=((self._DesignParameter['nmos2']['_XYCoordinates'][0][0] + self._DesignParameter['nmos2']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][(- 1)][0]) - (self._DesignParameter['nmos1']['_XYCoordinates'][0][0] + self._DesignParameter['nmos1']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][0])), _YWidth=(self._DesignParameter['vss']['_DesignObj']._DesignParameter['CONT_boundary_0']['_YWidth'] + (2 * drc._CoMinEnclosureByODAtLeastTwoSide)))
		self._DesignParameter['supply_od']['_XYCoordinates'] = [[(((self._DesignParameter['nmos1']['_XYCoordinates'][0][0] + self._DesignParameter['nmos1']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][0]) + (self._DesignParameter['nmos2']['_XYCoordinates'][0][0] + self._DesignParameter['nmos2']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][(- 1)][0])) / 2), self._DesignParameter['vss']['_XYCoordinates'][0][1]]]
		self._DesignParameter['vdd_od'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['DIFF'][0], _Datatype=DesignParameters._LayerMapping['DIFF'][1], _XWidth=((self._DesignParameter['pmos2']['_XYCoordinates'][0][0] + self._DesignParameter['pmos2']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][(- 1)][0]) - (self._DesignParameter['pmos1']['_XYCoordinates'][0][0] + self._DesignParameter['pmos1']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][0])), _YWidth=(self._DesignParameter['vdd']['_DesignObj']._DesignParameter['CONT_boundary_0']['_YWidth'] + (2 * drc._CoMinEnclosureByODAtLeastTwoSide)))
		self._DesignParameter['vdd_od']['_XYCoordinates'] = [[(((self._DesignParameter['pmos1']['_XYCoordinates'][0][0] + self._DesignParameter['pmos1']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][0]) + (self._DesignParameter['pmos2']['_XYCoordinates'][0][0] + self._DesignParameter['pmos2']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][(- 1)][0])) / 2), self._DesignParameter['vdd']['_XYCoordinates'][0][1]]]
		self._DesignParameter['pp_vss'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['PIMP'][0], _Datatype=DesignParameters._LayerMapping['PIMP'][1], _XWidth=(self._DesignParameter['supply_od']['_XWidth'] + (2 * drc._PpMinExtensiononPactive)), _YWidth=(self._DesignParameter['supply_od']['_YWidth'] + (2 * drc._PpMinExtensiononPactive)))
		self._DesignParameter['pp_vss']['_XYCoordinates'] = [[(+ self._DesignParameter['supply_od']['_XYCoordinates'][0][0]), (+ self._DesignParameter['supply_od']['_XYCoordinates'][0][1])]]
		self._DesignParameter['pp_pmos'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['PIMP'][0], _Datatype=DesignParameters._LayerMapping['PIMP'][1], _XWidth=self._DesignParameter['pp_vss']['_XWidth'], _YWidth=(max(((self._DesignParameter['pmos1']['_XYCoordinates'][0][1] + self._DesignParameter['pmos1']['_DesignObj']._DesignParameter['_PPLayer']['_XYCoordinates'][0][1]) + (self._DesignParameter['pmos1']['_DesignObj']._DesignParameter['_PPLayer']['_YWidth'] / 2)), ((self._DesignParameter['pmos2']['_XYCoordinates'][0][1] + self._DesignParameter['pmos2']['_DesignObj']._DesignParameter['_PPLayer']['_XYCoordinates'][0][1]) + (self._DesignParameter['pmos2']['_DesignObj']._DesignParameter['_PPLayer']['_YWidth'] / 2))) - ((self._DesignParameter['gate_a_input']['_XYCoordinates'][0][1] + self._DesignParameter['gate_a_input']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1]) - (self._DesignParameter['gate_a_input']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2))))
		self._DesignParameter['pp_pmos']['_XYCoordinates'] = [[self._DesignParameter['pp_vss']['_XYCoordinates'][0][0], ((max(((self._DesignParameter['pmos1']['_XYCoordinates'][0][1] + self._DesignParameter['pmos1']['_DesignObj']._DesignParameter['_PPLayer']['_XYCoordinates'][0][1]) + (self._DesignParameter['pmos1']['_DesignObj']._DesignParameter['_PPLayer']['_YWidth'] / 2)), ((self._DesignParameter['pmos2']['_XYCoordinates'][0][1] + self._DesignParameter['pmos2']['_DesignObj']._DesignParameter['_PPLayer']['_XYCoordinates'][0][1]) + (self._DesignParameter['pmos2']['_DesignObj']._DesignParameter['_PPLayer']['_YWidth'] / 2))) + ((self._DesignParameter['gate_a_input']['_XYCoordinates'][0][1] + self._DesignParameter['gate_a_input']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1]) - (self._DesignParameter['gate_a_input']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2))) / 2)]]
		self._DesignParameter['m2_supply'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _XWidth=self._DesignParameter['supply_od']['_XWidth'], _YWidth=300)
		self._DesignParameter['m2_supply']['_XYCoordinates'] = [[(+ self._DesignParameter['supply_od']['_XYCoordinates'][0][0]), (+ self._DesignParameter['supply_od']['_XYCoordinates'][0][1])], [(+ self._DesignParameter['vdd_od']['_XYCoordinates'][0][0]), (+ self._DesignParameter['vdd_od']['_XYCoordinates'][0][1])]]
		self._DesignParameter['xvtlayer'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['RVT'][0], _Datatype=DesignParameters._LayerMapping['RVT'][1], _XWidth=max(((self._DesignParameter['pmos2']['_XYCoordinates'][0][0] + self._DesignParameter['pmos2']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][(- 1)][0]) - (self._DesignParameter['pmos1']['_XYCoordinates'][0][0] + self._DesignParameter['pmos1']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][0])), ((self._DesignParameter['nmos2']['_XYCoordinates'][0][0] + self._DesignParameter['nmos2']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][(- 1)][0]) - (self._DesignParameter['nmos1']['_XYCoordinates'][0][0] + self._DesignParameter['nmos1']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][0]))), _YWidth=(self._DesignParameter['vdd']['_XYCoordinates'][0][1] - self._DesignParameter['vss']['_XYCoordinates'][0][1]))
		self._DesignParameter['xvtlayer']['_XYCoordinates'] = [[(((self._DesignParameter['nmos1']['_XYCoordinates'][0][0] + self._DesignParameter['nmos1']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][0]) + (self._DesignParameter['nmos2']['_XYCoordinates'][0][0] + self._DesignParameter['nmos2']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][(- 1)][0])) / 2), ((self._DesignParameter['vdd']['_XYCoordinates'][0][1] + self._DesignParameter['vss']['_XYCoordinates'][0][1]) / 2)]]
		self._DesignParameter['nw_layer'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['NWELL'][0], _Datatype=DesignParameters._LayerMapping['NWELL'][1], _XWidth=self._DesignParameter['pp_pmos']['_XWidth'], _YWidth=((self._DesignParameter['m2_supply']['_XYCoordinates'][(- 1)][1] + (self._DesignParameter['m2_supply']['_YWidth'] / 2)) - ((self._DesignParameter['gate_a_input']['_XYCoordinates'][0][1] + self._DesignParameter['gate_a_input']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1]) - (self._DesignParameter['gate_a_input']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2))))
		self._DesignParameter['nw_layer']['_XYCoordinates'] = [[self._DesignParameter['m2_supply']['_XYCoordinates'][0][0], (((self._DesignParameter['m2_supply']['_XYCoordinates'][(- 1)][1] + (self._DesignParameter['m2_supply']['_YWidth'] / 2)) + ((self._DesignParameter['gate_a_input']['_XYCoordinates'][0][1] + self._DesignParameter['gate_a_input']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1]) - (self._DesignParameter['gate_a_input']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2))) / 2)]]
		self._DesignParameter['m1_series_routing_x'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=74)
		self._DesignParameter['m1_series_routing_x']['_XYCoordinates'] = [[[((self._DesignParameter['nmos1']['_XYCoordinates'][0][0] + self._DesignParameter['nmos1']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][0][0]) - (self._DesignParameter['nmos1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth'] / 2)), ((((self._DesignParameter['nmos1']['_XYCoordinates'][0][1] + self._DesignParameter['nmos1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1]) + (self._DesignParameter['nmos1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_YWidth'] / 2)) + (self._DesignParameter['m1_series_routing_x']['_Width'] / 2)) + drc._Metal1MinSpace2)], [((self._DesignParameter['nmos3']['_XYCoordinates'][0][0] + self._DesignParameter['nmos3']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][(- 1)][0]) + (self._DesignParameter['nmos3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth'] / 2)), ((((self._DesignParameter['nmos1']['_XYCoordinates'][0][1] + self._DesignParameter['nmos1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1]) + (self._DesignParameter['nmos1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_YWidth'] / 2)) + (self._DesignParameter['m1_series_routing_x']['_Width'] / 2)) + drc._Metal1MinSpace2)]]]
		self._DesignParameter['m1_series_nmos2_routing_x'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=74)
		self._DesignParameter['m1_series_nmos2_routing_x']['_XYCoordinates'] = [[[((self._DesignParameter['nmos3']['_XYCoordinates'][0][0] + self._DesignParameter['nmos3']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][0][0]) - (self._DesignParameter['nmos3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth'] / 2)), ((((self._DesignParameter['nmos3']['_XYCoordinates'][0][1] + self._DesignParameter['nmos3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1]) - (self._DesignParameter['nmos3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_YWidth'] / 2)) - (self._DesignParameter['m1_series_nmos2_routing_x']['_Width'] / 2)) - drc._Metal1MinSpace2)], [((self._DesignParameter['nmos2']['_XYCoordinates'][0][0] + self._DesignParameter['nmos2']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][(- 1)][0]) + (self._DesignParameter['nmos2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth'] / 2)), ((((self._DesignParameter['nmos3']['_XYCoordinates'][0][1] + self._DesignParameter['nmos3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1]) - (self._DesignParameter['nmos3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_YWidth'] / 2)) - (self._DesignParameter['m1_series_nmos2_routing_x']['_Width'] / 2)) - drc._Metal1MinSpace2)]]]
		path_list = []
		if (len(self._DesignParameter['nmos1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates']) == 1):
		    mode = 'vertical'
		    _width = self._DesignParameter['nmos1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth']
		elif (self._DesignParameter['nmos1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][0] == self._DesignParameter['nmos1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][0]):
		    mode = 'horizontal'
		    _width = self._DesignParameter['nmos1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth']
		elif (self._DesignParameter['nmos1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1] == self._DesignParameter['nmos1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][1]):
		    mode = 'vertical'
		    _width = self._DesignParameter['nmos1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth']
		else:
		    print('Invalid Target Input')
		if (mode == 'vertical'):
		    xy_with_offset = []
		    target_y_value = (0 + self._DesignParameter['m1_series_routing_x']['_XYCoordinates'][0][0][1])
		    for i in range(len(self._DesignParameter['nmos1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		        if ((i % 2) == 1):
		            xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['nmos1']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['nmos1']['_XYCoordinates'][0][1])], self._DesignParameter['nmos1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		elif (mode == 'horizontal'):
		    xy_with_offset = []
		    target_x_value = (0 + self._DesignParameter['m1_series_routing_x']['_XYCoordinates'][0][0][0])
		    for i in range(len(self._DesignParameter['nmos1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		        if ((i % 2) == 1):
		            xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['nmos1']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['nmos1']['_XYCoordinates'][0][1])], self._DesignParameter['nmos1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		self._DesignParameter['m1_nmos1_routing_y'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=_width)
		self._DesignParameter['m1_nmos1_routing_y']['_XYCoordinates'] = path_list
		path_list = []
		if (len(self._DesignParameter['nmos3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates']) == 1):
		    mode = 'vertical'
		    _width = self._DesignParameter['nmos3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth']
		elif (self._DesignParameter['nmos3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][0] == self._DesignParameter['nmos3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][0]):
		    mode = 'horizontal'
		    _width = self._DesignParameter['nmos3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth']
		elif (self._DesignParameter['nmos3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1] == self._DesignParameter['nmos3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][1]):
		    mode = 'vertical'
		    _width = self._DesignParameter['nmos3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth']
		else:
		    print('Invalid Target Input')
		if (mode == 'vertical'):
		    xy_with_offset = []
		    target_y_value = (0 + self._DesignParameter['m1_series_routing_x']['_XYCoordinates'][0][0][1])
		    for i in range(len(self._DesignParameter['nmos3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		        if ((i % 2) == 0):
		            xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['nmos3']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['nmos3']['_XYCoordinates'][0][1])], self._DesignParameter['nmos3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		elif (mode == 'horizontal'):
		    xy_with_offset = []
		    target_x_value = (0 + self._DesignParameter['m1_series_routing_x']['_XYCoordinates'][0][0][0])
		    for i in range(len(self._DesignParameter['nmos3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		        if ((i % 2) == 0):
		            xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['nmos3']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['nmos3']['_XYCoordinates'][0][1])], self._DesignParameter['nmos3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		self._DesignParameter['m1_nmos3_routing_y'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=_width)
		self._DesignParameter['m1_nmos3_routing_y']['_XYCoordinates'] = path_list
		path_list = []
		if (len(self._DesignParameter['nmos3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates']) == 1):
		    mode = 'vertical'
		    _width = self._DesignParameter['nmos3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth']
		elif (self._DesignParameter['nmos3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][0] == self._DesignParameter['nmos3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][0]):
		    mode = 'horizontal'
		    _width = self._DesignParameter['nmos3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth']
		elif (self._DesignParameter['nmos3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1] == self._DesignParameter['nmos3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][1]):
		    mode = 'vertical'
		    _width = self._DesignParameter['nmos3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth']
		else:
		    print('Invalid Target Input')
		if (mode == 'vertical'):
		    xy_with_offset = []
		    target_y_value = (0 + self._DesignParameter['m1_series_nmos2_routing_x']['_XYCoordinates'][0][0][1])
		    for i in range(len(self._DesignParameter['nmos3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		        if ((i % 2) == 1):
		            xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['nmos3']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['nmos3']['_XYCoordinates'][0][1])], self._DesignParameter['nmos3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		elif (mode == 'horizontal'):
		    xy_with_offset = []
		    target_x_value = (0 + self._DesignParameter['m1_series_nmos2_routing_x']['_XYCoordinates'][0][0][0])
		    for i in range(len(self._DesignParameter['nmos3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		        if ((i % 2) == 1):
		            xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['nmos3']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['nmos3']['_XYCoordinates'][0][1])], self._DesignParameter['nmos3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		self._DesignParameter['m1_nmos3_Out_routing_y'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=_width)
		self._DesignParameter['m1_nmos3_Out_routing_y']['_XYCoordinates'] = path_list
		path_list = []
		if (len(self._DesignParameter['nmos2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates']) == 1):
		    mode = 'vertical'
		    _width = self._DesignParameter['nmos2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth']
		elif (self._DesignParameter['nmos2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][0] == self._DesignParameter['nmos2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][0]):
		    mode = 'horizontal'
		    _width = self._DesignParameter['nmos2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth']
		elif (self._DesignParameter['nmos2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1] == self._DesignParameter['nmos2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][1]):
		    mode = 'vertical'
		    _width = self._DesignParameter['nmos2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth']
		else:
		    print('Invalid Target Input')
		if (mode == 'vertical'):
		    xy_with_offset = []
		    target_y_value = (0 + self._DesignParameter['m1_series_nmos2_routing_x']['_XYCoordinates'][0][0][1])
		    for i in range(len(self._DesignParameter['nmos2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		        if ((i % 2) == 0):
		            xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['nmos2']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['nmos2']['_XYCoordinates'][0][1])], self._DesignParameter['nmos2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		elif (mode == 'horizontal'):
		    xy_with_offset = []
		    target_x_value = (0 + self._DesignParameter['m1_series_nmos2_routing_x']['_XYCoordinates'][0][0][0])
		    for i in range(len(self._DesignParameter['nmos2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		        if ((i % 2) == 0):
		            xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['nmos2']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['nmos2']['_XYCoordinates'][0][1])], self._DesignParameter['nmos2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		self._DesignParameter['m1_nmos2_routing_y'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=_width)
		self._DesignParameter['m1_nmos2_routing_y']['_XYCoordinates'] = path_list
		