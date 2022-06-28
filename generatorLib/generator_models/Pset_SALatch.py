from generatorLib import StickDiagram
from generatorLib import DesignParameters
import copy
import math
from generatorLib import DRC
from generatorLib.generator_models import PMOSWithDummy
from generatorLib.generator_models import ViaPoly2Met1
from generatorLib.generator_models import NSubRing
from generatorLib.generator_models import ViaMet12Met2
from generatorLib.generator_models import ViaStack
import math

class EasyDebugModule(StickDiagram._StickDiagram):
	def __init__(self, _DesignParameter=None, _Name='EasyDebugModule'):
		if _DesignParameter != None:
			self._DesignParameter = _DesignParameter
		else:
			self._DesignParameter = dict(_Name=self._NameDeclaration(_Name=_Name), _GDSFile=self._GDSObjDeclaration(_GDSFile=None))
		self._DesignParameter['_Name']['Name'] = _Name

	def _CalculateDesignParameter(self,dummy=True,pccrit=True,xvt='SLVT',pmos1_gate=3,pmos1_width=400,pmos1_length=30,pmos1_gate_spacing=96,pmos1_sdwidth=50,pmos2_gate=1,pmos2_width=200,pmos2_length=40,pmos2_gate_spacing=96,pmos3_gate=1,pmos3_width=500,pmos3_length=30,pmos3_gate_spacing=96,pmos3_sdwidth=50,pmos4_gate=1,pmos4_width=700,pmos4_length=30,pmos4_gate_spacing=96,pmos4_sdwidth=50,pmos2_sdwidth=50,pguardring_co_bot=2,pguardring_co_top=3,pguardring_co_right=6,pguardring_co_left=6):

		drc = DRC.DRC()
		_Name = self._DesignParameter['_Name']['_Name']
		MinSnapSpacing=drc._MinSnapSpacing
		self._DesignParameter['PMOS1'] = self._SrefElementDeclaration(_DesignObj=PMOSWithDummy._PMOS(_Name='PMOS1In{}'.format(_Name)))[0]
		self._DesignParameter['PMOS1']['_DesignObj']._CalculatePMOSDesignParameter(**dict(_PMOSNumberofGate=pmos1_gate, _PMOSChannelWidth=pmos1_width, _PMOSChannellength=pmos1_length, _PMOSDummy=dummy, _GateSpacing=pmos1_gate_spacing, _SDWidth=pmos1_sdwidth, _XVT=xvt, _PCCrit=pccrit))
		self._DesignParameter['PMOS1']['_XYCoordinates'] = [[0, 0]]
		self._DesignParameter['PMOS2'] = self._SrefElementDeclaration(_DesignObj=PMOSWithDummy._PMOS(_Name='PMOS2In{}'.format(_Name)))[0]
		self._DesignParameter['PMOS2']['_DesignObj']._CalculatePMOSDesignParameter(**dict(_PMOSNumberofGate=pmos2_gate, _PMOSChannelWidth=pmos2_width, _PMOSChannellength=pmos2_length, _PMOSDummy=dummy, _GateSpacing=pmos2_gate_spacing, _SDWidth=pmos2_sdwidth, _XVT=xvt, _PCCrit=pccrit))
		self._DesignParameter['PMOS2']['_XYCoordinates'] = [[((((self._DesignParameter['PMOS1']['_XYCoordinates'][0][0] + self._DesignParameter['PMOS1']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['PMOS1']['_DesignObj']._DesignParameter['_PODummyLayer']['_XWidth'] / 2)) - (self._DesignParameter['PMOS2']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][(- 1)][0] + (self._DesignParameter['PMOS2']['_DesignObj']._DesignParameter['_PODummyLayer']['_XWidth'] / 2))) - drc._PolygateMinSpace), self._DesignParameter['PMOS1']['_XYCoordinates'][0][1]], [((((self._DesignParameter['PMOS1']['_XYCoordinates'][0][0] + self._DesignParameter['PMOS1']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][(- 1)][0]) + (self._DesignParameter['PMOS1']['_DesignObj']._DesignParameter['_PODummyLayer']['_XWidth'] / 2)) - (self._DesignParameter['PMOS2']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][0] - (self._DesignParameter['PMOS2']['_DesignObj']._DesignParameter['_PODummyLayer']['_XWidth'] / 2))) + drc._PolygateMinSpace), self._DesignParameter['PMOS1']['_XYCoordinates'][0][1]]]
		self._DesignParameter['PMOS3'] = self._SrefElementDeclaration(_DesignObj=PMOSWithDummy._PMOS(_Name='PMOS3In{}'.format(_Name)))[0]
		self._DesignParameter['PMOS3']['_DesignObj']._CalculatePMOSDesignParameter(**dict(_PMOSNumberofGate=pmos3_gate, _PMOSChannelWidth=pmos3_width, _PMOSChannellength=pmos3_length, _PMOSDummy=dummy, _GateSpacing=pmos3_gate_spacing, _SDWidth=pmos3_sdwidth, _XVT=xvt, _PCCrit=pccrit))
		self._DesignParameter['PMOS3']['_XYCoordinates'] = [[((((self._DesignParameter['PMOS2']['_XYCoordinates'][0][0] + self._DesignParameter['PMOS2']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['PMOS2']['_DesignObj']._DesignParameter['_PODummyLayer']['_XWidth'] / 2)) - (self._DesignParameter['PMOS3']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][(- 1)][0] + (self._DesignParameter['PMOS3']['_DesignObj']._DesignParameter['_PODummyLayer']['_XWidth'] / 2))) - drc._PolygateMinSpace), self._DesignParameter['PMOS2']['_XYCoordinates'][0][1]], [((((self._DesignParameter['PMOS2']['_XYCoordinates'][1][0] + self._DesignParameter['PMOS2']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][(- 1)][0]) + (self._DesignParameter['PMOS2']['_DesignObj']._DesignParameter['_PODummyLayer']['_XWidth'] / 2)) - (self._DesignParameter['PMOS3']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][0] - (self._DesignParameter['PMOS3']['_DesignObj']._DesignParameter['_PODummyLayer']['_XWidth'] / 2))) + drc._PolygateMinSpace), self._DesignParameter['PMOS2']['_XYCoordinates'][0][1]]]
		self._DesignParameter['PMOS4'] = self._SrefElementDeclaration(_DesignObj=PMOSWithDummy._PMOS(_Name='PMOS4In{}'.format(_Name)))[0]
		self._DesignParameter['PMOS4']['_DesignObj']._CalculatePMOSDesignParameter(**dict(_PMOSNumberofGate=pmos4_gate, _PMOSChannelWidth=pmos4_width, _PMOSChannellength=pmos4_length, _PMOSDummy=dummy, _GateSpacing=pmos4_gate_spacing, _SDWidth=pmos4_sdwidth, _XVT=xvt, _PCCrit=pccrit))
		self._DesignParameter['PMOS4']['_XYCoordinates'] = [[((((self._DesignParameter['PMOS3']['_XYCoordinates'][0][0] + self._DesignParameter['PMOS3']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['PMOS3']['_DesignObj']._DesignParameter['_PODummyLayer']['_XWidth'] / 2)) - (self._DesignParameter['PMOS4']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][(- 1)][0] + (self._DesignParameter['PMOS4']['_DesignObj']._DesignParameter['_PODummyLayer']['_XWidth'] / 2))) - drc._PolygateMinSpace), self._DesignParameter['PMOS3']['_XYCoordinates'][0][1]], [((((self._DesignParameter['PMOS3']['_XYCoordinates'][1][0] + self._DesignParameter['PMOS3']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][(- 1)][0]) + (self._DesignParameter['PMOS3']['_DesignObj']._DesignParameter['_PODummyLayer']['_XWidth'] / 2)) - (self._DesignParameter['PMOS4']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][0] - (self._DesignParameter['PMOS4']['_DesignObj']._DesignParameter['_PODummyLayer']['_XWidth'] / 2))) + drc._PolygateMinSpace), self._DesignParameter['PMOS3']['_XYCoordinates'][0][1]]]

		if self._DesignParameter['PMOS1']['_DesignObj']._DesignParameter['_PODummyLayer']['_XWidth']*self._DesignParameter['PMOS1']['_DesignObj']._DesignParameter['_PODummyLayer']['_YWidth'] < drc._PODummyMinArea :
			self._DesignParameter['PMOS1']['_DesignObj']._DesignParameter['_PODummyLayer']['_YWidth']=int(drc._PODummyMinArea/self._DesignParameter['PMOS1']['_DesignObj']._DesignParameter['_PODummyLayer']['_XWidth'])+2*MinSnapSpacing

		if self._DesignParameter['PMOS2']['_DesignObj']._DesignParameter['_PODummyLayer']['_XWidth']*self._DesignParameter['PMOS2']['_DesignObj']._DesignParameter['_PODummyLayer']['_YWidth'] < drc._PODummyMinArea :
			self._DesignParameter['PMOS2']['_DesignObj']._DesignParameter['_PODummyLayer']['_YWidth']=int(drc._PODummyMinArea/self._DesignParameter['PMOS2']['_DesignObj']._DesignParameter['_PODummyLayer']['_XWidth'])+2*MinSnapSpacing

		if self._DesignParameter['PMOS3']['_DesignObj']._DesignParameter['_PODummyLayer']['_XWidth']*self._DesignParameter['PMOS3']['_DesignObj']._DesignParameter['_PODummyLayer']['_YWidth'] < drc._PODummyMinArea :
			self._DesignParameter['PMOS3']['_DesignObj']._DesignParameter['_PODummyLayer']['_YWidth']=int(drc._PODummyMinArea/self._DesignParameter['PMOS3']['_DesignObj']._DesignParameter['_PODummyLayer']['_XWidth'])+2*MinSnapSpacing

		if self._DesignParameter['PMOS4']['_DesignObj']._DesignParameter['_PODummyLayer']['_XWidth']*self._DesignParameter['PMOS4']['_DesignObj']._DesignParameter['_PODummyLayer']['_YWidth'] < drc._PODummyMinArea :
			self._DesignParameter['PMOS4']['_DesignObj']._DesignParameter['_PODummyLayer']['_YWidth']=int(drc._PODummyMinArea/self._DesignParameter['PMOS4']['_DesignObj']._DesignParameter['_PODummyLayer']['_XWidth'])+2*MinSnapSpacing

		self._DesignParameter['via_m1_m3_pmos_output'] = self._SrefElementDeclaration(_DesignObj=ViaStack._ViaStack(_Name='via_m1_m3_pmos_outputIn{}'.format(_Name)))[0]
		self._DesignParameter['via_m1_m3_pmos_output']['_DesignObj']._CalculateStackMinimumEnclosureX(**dict(COX=1, COY=max(2, max(1, (1 + int((((self._DesignParameter['PMOS1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_YWidth'] - drc._VIAxMinSpace) - (2 * drc._VIAxMinEnclosureByMetx)) / (drc._VIAxMinWidth + drc._VIAxMinSpace)))))), start_layer=1, end_layer=3))
		self._DesignParameter['via_m1_m3_pmos_output']['_XYCoordinates'] = [[(self._DesignParameter['PMOS1']['_XYCoordinates'][0][0] + self._DesignParameter['PMOS1']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][(- 1)][0]), (self._DesignParameter['PMOS1']['_XYCoordinates'][0][1] + self._DesignParameter['PMOS1']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][(- 1)][1])]]

		tmp=[]

		self._DesignParameter['m1_pmos_x'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=self._DesignParameter['PMOS1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth'])

		if pmos1_gate > 1 :
			tmp.append([[((self._DesignParameter['PMOS1']['_XYCoordinates'][0][0] + self._DesignParameter['PMOS1']['_DesignObj']._DesignParameter['_XYCoordinatePMOSSupplyRouting']['_XYCoordinates'][0][0]) - (self._DesignParameter['PMOS1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth'] / 2)), ((((self._DesignParameter['PMOS1']['_XYCoordinates'][0][1] + self._DesignParameter['PMOS1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1]) - (self._DesignParameter['PMOS1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_YWidth'] / 2)) - (self._DesignParameter['m1_pmos_x']['_Width'] / 2)) - drc._Metal1MinSpace2)], \
															 [((self._DesignParameter['PMOS1']['_XYCoordinates'][0][0] + self._DesignParameter['PMOS1']['_DesignObj']._DesignParameter['_XYCoordinatePMOSSupplyRouting']['_XYCoordinates'][(- 1)][0]) + (self._DesignParameter['PMOS1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth'] / 2)), ((((self._DesignParameter['PMOS1']['_XYCoordinates'][0][1] + self._DesignParameter['PMOS1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1]) - (self._DesignParameter['PMOS1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_YWidth'] / 2)) - (self._DesignParameter['m1_pmos_x']['_Width'] / 2)) - drc._Metal1MinSpace2)]])
		if pmos1_gate > 2 :
			tmp.append([[((self._DesignParameter['PMOS1']['_XYCoordinates'][0][0] + self._DesignParameter['PMOS1']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][0][0]) - (self._DesignParameter['PMOS1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth'] / 2)), ((((self._DesignParameter['PMOS1']['_XYCoordinates'][0][1] + self._DesignParameter['PMOS1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1]) + (self._DesignParameter['PMOS1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_YWidth'] / 2)) + (self._DesignParameter['m1_pmos_x']['_Width'] / 2)) + drc._Metal1MinSpace2)], \
																 [((self._DesignParameter['PMOS1']['_XYCoordinates'][0][0] + self._DesignParameter['PMOS1']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][(- 1)][0]) + (self._DesignParameter['PMOS1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth'] / 2)), ((((self._DesignParameter['PMOS1']['_XYCoordinates'][0][1] + self._DesignParameter['PMOS1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1]) + (self._DesignParameter['PMOS1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_YWidth'] / 2)) + (self._DesignParameter['m1_pmos_x']['_Width'] / 2)) + drc._Metal1MinSpace2)]])

		self._DesignParameter['m1_pmos_x']['_XYCoordinates'] = tmp

		path_list = []
		xy_offset = [0, 0]
		if (len(self._DesignParameter['PMOS1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates']) == 1):
		    mode = 'vertical'
		    _width = self._DesignParameter['PMOS1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth']
		elif (self._DesignParameter['PMOS1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][0] == self._DesignParameter['PMOS1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][0]):
		    mode = 'horizontal'
		    _width = self._DesignParameter['PMOS1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth']
		elif (self._DesignParameter['PMOS1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1] == self._DesignParameter['PMOS1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][1]):
		    mode = 'vertical'
		    _width = self._DesignParameter['PMOS1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth']
		else:
		    print('Invalid Target Input')
		if (mode == 'vertical'):
			if pmos1_gate > 1:
				xy_with_offset = []
				target_y_value = [[(+ self._DesignParameter['m1_pmos_x']['_XYCoordinates'][0][0][0]), (+ self._DesignParameter['m1_pmos_x']['_XYCoordinates'][0][0][1])]][0][1]
				for i in range(len(self._DesignParameter['PMOS1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
					if ((i % 2) == 0):
						xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['PMOS1']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['PMOS1']['_XYCoordinates'][0][1])], self._DesignParameter['PMOS1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])])
				for i in range(len(xy_with_offset)):
					path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		elif (mode == 'horizontal'):
		    xy_with_offset = []
		    target_x_value = [[(+ self._DesignParameter['m1_pmos_x']['_XYCoordinates'][0][0][0]), (+ self._DesignParameter['m1_pmos_x']['_XYCoordinates'][0][0][1])]][0][0]
		    for i in range(len(self._DesignParameter['PMOS1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		        if ((i % 2) == 0):
		            xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['PMOS1']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['PMOS1']['_XYCoordinates'][0][1])], self._DesignParameter['PMOS1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		for i in range(len(path_list)):
		    path_list[i][0] = [(xy + offset) for (xy, offset) in zip(path_list[i][0], xy_offset)]
		self._DesignParameter['m1_pmos1_y_bottom'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=_width)
		self._DesignParameter['m1_pmos1_y_bottom']['_XYCoordinates'] = path_list
		path_list = []
		xy_offset = [0, 0]
		if (len(self._DesignParameter['PMOS1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates']) == 1):
		    mode = 'vertical'
		    _width = self._DesignParameter['PMOS1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth']
		elif (self._DesignParameter['PMOS1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][0] == self._DesignParameter['PMOS1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][0]):
		    mode = 'horizontal'
		    _width = self._DesignParameter['PMOS1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth']
		elif (self._DesignParameter['PMOS1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1] == self._DesignParameter['PMOS1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][1]):
		    mode = 'vertical'
		    _width = self._DesignParameter['PMOS1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth']
		else:
		    print('Invalid Target Input')
		if (mode == 'vertical'):
			if pmos1_gate > 2:
				xy_with_offset = []
				target_y_value = [[(+ self._DesignParameter['m1_pmos_x']['_XYCoordinates'][1][0][0]), (+ self._DesignParameter['m1_pmos_x']['_XYCoordinates'][1][0][1])]][0][1]
				for i in range(len(self._DesignParameter['PMOS1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
					if ((i % 2) == 1):
						xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['PMOS1']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['PMOS1']['_XYCoordinates'][0][1])], self._DesignParameter['PMOS1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])])
				for i in range(len(xy_with_offset)):
					path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		elif (mode == 'horizontal'):
		    xy_with_offset = []
		    target_x_value = [[(+ self._DesignParameter['m1_pmos_x']['_XYCoordinates'][1][0][0]), (+ self._DesignParameter['m1_pmos_x']['_XYCoordinates'][1][0][1])]][0][0]
		    for i in range(len(self._DesignParameter['PMOS1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		        if ((i % 2) == 1):
		            xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['PMOS1']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['PMOS1']['_XYCoordinates'][0][1])], self._DesignParameter['PMOS1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		for i in range(len(path_list)):
		    path_list[i][0] = [(xy + offset) for (xy, offset) in zip(path_list[i][0], xy_offset)]
		self._DesignParameter['m1_pmos1_y_top'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=_width)
		self._DesignParameter['m1_pmos1_y_top']['_XYCoordinates'] = path_list
		cont_pmos2 = max(2, max(1, (1 + int((((self._DesignParameter['PMOS2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_YWidth'] - drc._VIAxMinSpace) - (2 * drc._VIAxMinEnclosureByMetx)) / (drc._VIAxMinWidth + drc._VIAxMinSpace))))))
		self._DesignParameter['via_m1_m3_pmos2'] = self._SrefElementDeclaration(_DesignObj=ViaStack._ViaStack(_Name='via_m1_m3_pmos2In{}'.format(_Name)))[0]
		self._DesignParameter['via_m1_m3_pmos2']['_DesignObj']._CalculateStackSameEnclosure(**dict(COX=1, COY=cont_pmos2, start_layer=1, end_layer=3))
		self._DesignParameter['via_m1_m3_pmos2']['_XYCoordinates'] = None
		XYList = []
		xy_offset = [0, 0]
		for i in range(len(self._DesignParameter['PMOS2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		    if ((i % 2) == 1):
		        xy = (self._DesignParameter['PMOS2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i][0] if (type(self._DesignParameter['PMOS2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i][0]) == list) else self._DesignParameter['PMOS2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])
		        XYList.append([((x + y) + z) for (x, y, z) in zip([(0 + self._DesignParameter['PMOS2']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['PMOS2']['_XYCoordinates'][0][1])], xy, xy_offset)])
		self._DesignParameter['via_m1_m3_pmos2']['_XYCoordinates'] = XYList
		self._DesignParameter['via_m1_m3_pmos2_1'] = self._SrefElementDeclaration(_DesignObj=ViaStack._ViaStack(_Name='via_m1_m3_pmos2_1In{}'.format(_Name)))[0]
		self._DesignParameter['via_m1_m3_pmos2_1']['_DesignObj']._CalculateStackSameEnclosure(**dict(COX=1, COY=cont_pmos2, start_layer=1, end_layer=3))
		self._DesignParameter['via_m1_m3_pmos2_1']['_XYCoordinates'] = None
		XYList = []
		xy_offset = [0, 0]
		for element in self._DesignParameter['PMOS2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 2)::(- 2)]:
		    element = (element[0] if (type(element[0]) == list) else element)
		    XYList.append([((x + y) + z) for (x, y, z) in zip([(0 + self._DesignParameter['PMOS2']['_XYCoordinates'][1][0]), (0 + self._DesignParameter['PMOS2']['_XYCoordinates'][1][1])], element, xy_offset)])
		self._DesignParameter['via_m1_m3_pmos2_1']['_XYCoordinates'] = XYList
		cont_pmos3 = max(2, max(1, (1 + int((((self._DesignParameter['PMOS3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_YWidth'] - drc._VIAxMinSpace) - (2 * drc._VIAxMinEnclosureByMetx)) / (drc._VIAxMinWidth + drc._VIAxMinSpace))))))
		self._DesignParameter['via_m1_m3_pmos3'] = self._SrefElementDeclaration(_DesignObj=ViaStack._ViaStack(_Name='via_m1_m3_pmos3In{}'.format(_Name)))[0]
		self._DesignParameter['via_m1_m3_pmos3']['_DesignObj']._CalculateStackSameEnclosure(**dict(COX=1, COY=cont_pmos3, start_layer=1, end_layer=3))
		self._DesignParameter['via_m1_m3_pmos3']['_XYCoordinates'] = None
		XYList = []
		xy_offset = [0, 0]
		for i in range(len(self._DesignParameter['PMOS3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		    if ((i % 2) == 1):
		        xy = (self._DesignParameter['PMOS3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i][0] if (type(self._DesignParameter['PMOS3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i][0]) == list) else self._DesignParameter['PMOS3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])
		        XYList.append([((x + y) + z) for (x, y, z) in zip([(0 + self._DesignParameter['PMOS3']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['PMOS3']['_XYCoordinates'][0][1])], xy, xy_offset)])
		self._DesignParameter['via_m1_m3_pmos3']['_XYCoordinates'] = XYList
		self._DesignParameter['via_m1_m3_pmos3_1'] = self._SrefElementDeclaration(_DesignObj=ViaStack._ViaStack(_Name='via_m1_m3_pmos3_1In{}'.format(_Name)))[0]
		self._DesignParameter['via_m1_m3_pmos3_1']['_DesignObj']._CalculateStackSameEnclosure(**dict(COX=1, COY=cont_pmos3, start_layer=1, end_layer=3))
		self._DesignParameter['via_m1_m3_pmos3_1']['_XYCoordinates'] = None
		XYList = []
		xy_offset = [0, 0]
		for element in self._DesignParameter['PMOS3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 2)::(- 2)]:
		    element = (element[0] if (type(element[0]) == list) else element)
		    XYList.append([((x + y) + z) for (x, y, z) in zip([(0 + self._DesignParameter['PMOS3']['_XYCoordinates'][1][0]), (0 + self._DesignParameter['PMOS3']['_XYCoordinates'][1][1])], element, xy_offset)])
		self._DesignParameter['via_m1_m3_pmos3_1']['_XYCoordinates'] = XYList
		cont_pmos4 = max(2, max(1, (1 + int((((self._DesignParameter['PMOS4']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_YWidth'] - drc._VIAxMinSpace) - (2 * drc._VIAxMinEnclosureByMetx)) / (drc._VIAxMinWidth + drc._VIAxMinSpace))))))
		self._DesignParameter['via_m1_m2_pmos4'] = self._SrefElementDeclaration(_DesignObj=ViaStack._ViaStack(_Name='via_m1_m2_pmos4In{}'.format(_Name)))[0]
		self._DesignParameter['via_m1_m2_pmos4']['_DesignObj']._CalculateStackSameEnclosure(**dict(COX=1, COY=cont_pmos4, start_layer=1, end_layer=2))
		self._DesignParameter['via_m1_m2_pmos4']['_XYCoordinates'] = None
		XYList = []
		xy_offset = [0, 0]
		for i in range(len(self._DesignParameter['PMOS4']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		    if ((i % 2) == 1):
		        xy = (self._DesignParameter['PMOS4']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i][0] if (type(self._DesignParameter['PMOS4']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i][0]) == list) else self._DesignParameter['PMOS4']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])
		        XYList.append([((x + y) + z) for (x, y, z) in zip([(0 + self._DesignParameter['PMOS4']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['PMOS4']['_XYCoordinates'][0][1])], xy, xy_offset)])
		self._DesignParameter['via_m1_m2_pmos4']['_XYCoordinates'] = XYList
		self._DesignParameter['via_m1_m2_pmos4_1'] = self._SrefElementDeclaration(_DesignObj=ViaStack._ViaStack(_Name='via_m1_m2_pmos4_1In{}'.format(_Name)))[0]
		self._DesignParameter['via_m1_m2_pmos4_1']['_DesignObj']._CalculateStackSameEnclosure(**dict(COX=1, COY=cont_pmos4, start_layer=1, end_layer=2))
		self._DesignParameter['via_m1_m2_pmos4_1']['_XYCoordinates'] = None
		XYList = []
		xy_offset = [0, 0]
		for element in self._DesignParameter['PMOS4']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 2)::(- 2)]:
		    element = (element[0] if (type(element[0]) == list) else element)
		    XYList.append([((x + y) + z) for (x, y, z) in zip([(0 + self._DesignParameter['PMOS4']['_XYCoordinates'][1][0]), (0 + self._DesignParameter['PMOS4']['_XYCoordinates'][1][1])], element, xy_offset)])
		self._DesignParameter['via_m1_m2_pmos4_1']['_XYCoordinates'] = XYList
		self._DesignParameter['m3_pmos32'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0], _Datatype=DesignParameters._LayerMapping['METAL3'][1], _Width=min(self._DesignParameter['via_m1_m3_pmos3']['_DesignObj']._DesignParameter['ViaMet22Met3']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth'], self._DesignParameter['via_m1_m3_pmos2']['_DesignObj']._DesignParameter['ViaMet22Met3']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth'], (2 * drc._MetalxMinWidth)))
		self._DesignParameter['m3_pmos32']['_XYCoordinates'] = [[[self._DesignParameter['via_m1_m3_pmos3']['_XYCoordinates'][0][0], self._DesignParameter['via_m1_m3_pmos3']['_XYCoordinates'][0][1]], [self._DesignParameter['via_m1_m3_pmos2']['_XYCoordinates'][(- 1)][0], self._DesignParameter['via_m1_m3_pmos2']['_XYCoordinates'][(- 1)][1]]], [[self._DesignParameter['via_m1_m3_pmos3_1']['_XYCoordinates'][0][0], self._DesignParameter['via_m1_m3_pmos3_1']['_XYCoordinates'][0][1]], [self._DesignParameter['via_m1_m3_pmos2_1']['_XYCoordinates'][(- 1)][0], self._DesignParameter['via_m1_m3_pmos2_1']['_XYCoordinates'][(- 1)][1]]]]
		self._DesignParameter['pmos2_gate'] = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_Name='pmos2_gateIn{}'.format(_Name)))[0]
		self._DesignParameter['pmos2_gate']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(**dict(_ViaPoly2Met1NumberOfCOX=max(1, max(1, (1 + int(((((((self._DesignParameter['PMOS2']['_XYCoordinates'][1][0] + self._DesignParameter['PMOS2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]) + (self._DesignParameter['PMOS2']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)) - ((self._DesignParameter['PMOS2']['_XYCoordinates'][1][0] + self._DesignParameter['PMOS2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['PMOS2']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2))) - drc._CoMinSpace) - (2 * drc._CoMinEnclosureByPO)) / (drc._CoMinWidth + drc._CoMinSpace)))))), _ViaPoly2Met1NumberOfCOY=1))
		self._DesignParameter['pmos2_gate']['_XYCoordinates'] = [[self._DesignParameter['PMOS2']['_XYCoordinates'][0][0], min(((min(((self._DesignParameter['PMOS2']['_XYCoordinates'][0][1] + self._DesignParameter['PMOS2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1]) - (self._DesignParameter['PMOS2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_YWidth'] / 2)), (((self._DesignParameter['via_m1_m3_pmos2']['_XYCoordinates'][0][1] + self._DesignParameter['via_m1_m3_pmos2']['_DesignObj']._DesignParameter['ViaMet12Met2']['_XYCoordinates'][0][1]) + self._DesignParameter['via_m1_m3_pmos2']['_DesignObj']._DesignParameter['ViaMet12Met2']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) - (self._DesignParameter['via_m1_m3_pmos2']['_DesignObj']._DesignParameter['ViaMet12Met2']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2))) - (self._DesignParameter['pmos2_gate']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)) - drc._Metal1MinSpace2), self._DesignParameter['PMOS2']['_XYCoordinates'][0][1]-self._DesignParameter['PMOS2']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth']/2-self._DesignParameter['pmos2_gate']['_DesignObj']._DesignParameter['_POLayer']['_YWidth']/2-31)], [self._DesignParameter['PMOS2']['_XYCoordinates'][(- 1)][0],  min(((min(((self._DesignParameter['PMOS2']['_XYCoordinates'][0][1] + self._DesignParameter['PMOS2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1]) - (self._DesignParameter['PMOS2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_YWidth'] / 2)), (((self._DesignParameter['via_m1_m3_pmos2']['_XYCoordinates'][0][1] + self._DesignParameter['via_m1_m3_pmos2']['_DesignObj']._DesignParameter['ViaMet12Met2']['_XYCoordinates'][0][1]) + self._DesignParameter['via_m1_m3_pmos2']['_DesignObj']._DesignParameter['ViaMet12Met2']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) - (self._DesignParameter['via_m1_m3_pmos2']['_DesignObj']._DesignParameter['ViaMet12Met2']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2))) - (self._DesignParameter['pmos2_gate']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)) - drc._Metal1MinSpace2), self._DesignParameter['PMOS2']['_XYCoordinates'][0][1]-self._DesignParameter['PMOS2']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth']/2-self._DesignParameter['pmos2_gate']['_DesignObj']._DesignParameter['_POLayer']['_YWidth']/2-31)]]
		if (pmos2_gate == 1):
			_tmpLength_x=(self._DesignParameter['PMOS2']['_XYCoordinates'][0][0]+self._DesignParameter['PMOS2']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][-1][0]-self._DesignParameter['PMOS2']['_DesignObj']._DesignParameter['_PODummyLayer']['_XWidth']/2)-(self._DesignParameter['pmos2_gate']['_XYCoordinates'][0][0]+self._DesignParameter['pmos2_gate']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']/2)
			_tmpLength_y=(self._DesignParameter['PMOS2']['_XYCoordinates'][0][1]+self._DesignParameter['PMOS2']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][-1][1]-self._DesignParameter['PMOS2']['_DesignObj']._DesignParameter['_PODummyLayer']['_YWidth']/2)-(self._DesignParameter['pmos2_gate']['_XYCoordinates'][0][1]+self._DesignParameter['pmos2_gate']['_DesignObj']._DesignParameter['_POLayer']['_YWidth']/2)
			if _tmpLength_x*_tmpLength_x+_tmpLength_y*_tmpLength_y < drc._PolygateMinSpaceAtCorner*drc._PolygateMinSpaceAtCorner:
				_tmpY_to_Move=int(math.sqrt(drc._PolygateMinSpaceAtCorner*drc._PolygateMinSpaceAtCorner-_tmpLength_x*_tmpLength_x))+MinSnapSpacing
				self._DesignParameter['pmos2_gate']['_XYCoordinates'][0][1] = self._DesignParameter['PMOS2']['_XYCoordinates'][0][1]+self._DesignParameter['PMOS2']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][1]-self._DesignParameter['PMOS2']['_DesignObj']._DesignParameter['_PODummyLayer']['_YWidth']/2-self._DesignParameter['pmos2_gate']['_DesignObj']._DesignParameter['_POLayer']['_YWidth']/2-_tmpY_to_Move
				self._DesignParameter['pmos2_gate']['_XYCoordinates'][1][1] = self._DesignParameter['PMOS2']['_XYCoordinates'][0][1]+self._DesignParameter['PMOS2']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][1]-self._DesignParameter['PMOS2']['_DesignObj']._DesignParameter['_PODummyLayer']['_YWidth']/2-self._DesignParameter['pmos2_gate']['_DesignObj']._DesignParameter['_POLayer']['_YWidth']/2-_tmpY_to_Move
		path_list = []
		xy_offset = [0, 0]
		if (len(self._DesignParameter['PMOS2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates']) == 1):
		    mode = 'vertical'
		    _width = self._DesignParameter['PMOS2']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
		elif (self._DesignParameter['PMOS2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0] == self._DesignParameter['PMOS2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]):
		    mode = 'horizontal'
		    _width = self._DesignParameter['PMOS2']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
		elif (self._DesignParameter['PMOS2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1] == self._DesignParameter['PMOS2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][1]):
		    mode = 'vertical'
		    _width = self._DesignParameter['PMOS2']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
		else:
		    print('Invalid Target Input')
		if (mode == 'vertical'):
		    xy_with_offset = []
		    target_y_value = [[(+ (self._DesignParameter['pmos2_gate']['_XYCoordinates'][1][0] + self._DesignParameter['pmos2_gate']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0])), (+ ((self._DesignParameter['pmos2_gate']['_XYCoordinates'][1][1] + self._DesignParameter['pmos2_gate']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1]) - (self._DesignParameter['pmos2_gate']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2)))]][0][1]
		    for i in range(len(self._DesignParameter['PMOS2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
		        xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['PMOS2']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['PMOS2']['_XYCoordinates'][0][1])], self._DesignParameter['PMOS2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		elif (mode == 'horizontal'):
		    xy_with_offset = []
		    target_x_value = [[(+ (self._DesignParameter['pmos2_gate']['_XYCoordinates'][1][0] + self._DesignParameter['pmos2_gate']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0])), (+ ((self._DesignParameter['pmos2_gate']['_XYCoordinates'][1][1] + self._DesignParameter['pmos2_gate']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1]) - (self._DesignParameter['pmos2_gate']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2)))]][0][0]
		    for i in range(len(self._DesignParameter['PMOS2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
		        xy_with_offset.Zappend([(x + y) for (x, y) in zip([(0 + self._DesignParameter['PMOS2']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['PMOS2']['_XYCoordinates'][0][1])], self._DesignParameter['PMOS2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		for i in range(len(path_list)):
		    path_list[i][0] = [(xy + offset) for (xy, offset) in zip(path_list[i][0], xy_offset)]
		self._DesignParameter['poly_pmos2_y'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _Width=_width)
		self._DesignParameter['poly_pmos2_y']['_XYCoordinates'] = path_list
		path_list = []
		xy_offset = [0, 0]
		if (len(self._DesignParameter['PMOS2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates']) == 1):
		    mode = 'vertical'
		    _width = self._DesignParameter['PMOS2']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
		elif (self._DesignParameter['PMOS2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0] == self._DesignParameter['PMOS2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]):
		    mode = 'horizontal'
		    _width = self._DesignParameter['PMOS2']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
		elif (self._DesignParameter['PMOS2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1] == self._DesignParameter['PMOS2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][1]):
		    mode = 'vertical'
		    _width = self._DesignParameter['PMOS2']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
		else:
		    print('Invalid Target Input')
		if (mode == 'vertical'):
		    xy_with_offset = []
		    target_y_value = [[(+ (self._DesignParameter['pmos2_gate']['_XYCoordinates'][1][0] + self._DesignParameter['pmos2_gate']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0])), (+ ((self._DesignParameter['pmos2_gate']['_XYCoordinates'][1][1] + self._DesignParameter['pmos2_gate']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1]) - (self._DesignParameter['pmos2_gate']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2)))]][0][1]
		    for i in range(len(self._DesignParameter['PMOS2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
		        xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['PMOS2']['_XYCoordinates'][1][0]), (0 + self._DesignParameter['PMOS2']['_XYCoordinates'][1][1])], self._DesignParameter['PMOS2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		elif (mode == 'horizontal'):
		    xy_with_offset = []
		    target_x_value = [[(+ (self._DesignParameter['pmos2_gate']['_XYCoordinates'][1][0] + self._DesignParameter['pmos2_gate']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0])), (+ ((self._DesignParameter['pmos2_gate']['_XYCoordinates'][1][1] + self._DesignParameter['pmos2_gate']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1]) - (self._DesignParameter['pmos2_gate']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2)))]][0][0]
		    for i in range(len(self._DesignParameter['PMOS2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
		        xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['PMOS2']['_XYCoordinates'][1][0]), (0 + self._DesignParameter['PMOS2']['_XYCoordinates'][1][1])], self._DesignParameter['PMOS2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		for i in range(len(path_list)):
		    path_list[i][0] = [(xy + offset) for (xy, offset) in zip(path_list[i][0], xy_offset)]
		self._DesignParameter['poly_pmos2_1_y'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _Width=_width)
		self._DesignParameter['poly_pmos2_1_y']['_XYCoordinates'] = path_list
		self._DesignParameter['poly_pmos2_x'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _Width=self._DesignParameter['pmos2_gate']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'])
		self._DesignParameter['poly_pmos2_x']['_XYCoordinates'] = [[[((self._DesignParameter['PMOS2']['_XYCoordinates'][0][0] + self._DesignParameter['PMOS2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['PMOS2']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)), self._DesignParameter['pmos2_gate']['_XYCoordinates'][0][1]], [((self._DesignParameter['PMOS2']['_XYCoordinates'][0][0] + self._DesignParameter['PMOS2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]) + (self._DesignParameter['PMOS2']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)), self._DesignParameter['pmos2_gate']['_XYCoordinates'][0][1]]], [[((self._DesignParameter['PMOS2']['_XYCoordinates'][1][0] + self._DesignParameter['PMOS2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['PMOS2']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)), self._DesignParameter['pmos2_gate']['_XYCoordinates'][1][1]], [((self._DesignParameter['PMOS2']['_XYCoordinates'][1][0] + self._DesignParameter['PMOS2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]) + (self._DesignParameter['PMOS2']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)), self._DesignParameter['pmos2_gate']['_XYCoordinates'][1][1]]]]
		self._DesignParameter['pmos1_gate'] = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_Name='pmos1_gateIn{}'.format(_Name)))[0]
		self._DesignParameter['pmos1_gate']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(**dict(_ViaPoly2Met1NumberOfCOX=max(1, max(1, (1 + int(((((((self._DesignParameter['PMOS1']['_XYCoordinates'][0][0] + self._DesignParameter['PMOS1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]) + (self._DesignParameter['PMOS1']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)) - ((self._DesignParameter['PMOS1']['_XYCoordinates'][0][0] + self._DesignParameter['PMOS1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['PMOS1']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2))) - drc._CoMinSpace) - (2 * drc._CoMinEnclosureByPO)) / (drc._CoMinWidth + drc._CoMinSpace)))))), _ViaPoly2Met1NumberOfCOY=1))
		self._DesignParameter['pmos1_gate']['_XYCoordinates'] = [[self._DesignParameter['PMOS1']['_XYCoordinates'][0][0], max(((self._DesignParameter['m1_pmos_x']['_XYCoordinates'][(- 1)][0][1] + (self._DesignParameter['m1_pmos_x']['_Width'] / 2)) + (self._DesignParameter['pmos1_gate']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)) + drc._Metal1MinSpace2, self._DesignParameter['PMOS1']['_XYCoordinates'][0][1]+self._DesignParameter['PMOS1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']/2+self._DesignParameter['pmos1_gate']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']/2+drc._Metal1MinSpace2)]]
		if (pmos1_gate == 1):
			_tmpLength_x=(self._DesignParameter['PMOS1']['_XYCoordinates'][0][0]+self._DesignParameter['PMOS1']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][-1][0]-self._DesignParameter['PMOS1']['_DesignObj']._DesignParameter['_PODummyLayer']['_XWidth']/2)-(self._DesignParameter['pmos1_gate']['_XYCoordinates'][0][0]+self._DesignParameter['pmos1_gate']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']/2)
			_tmpLength_y=(self._DesignParameter['pmos1_gate']['_XYCoordinates'][0][1]-self._DesignParameter['pmos1_gate']['_DesignObj']._DesignParameter['_POLayer']['_YWidth']/2)-(self._DesignParameter['PMOS1']['_XYCoordinates'][0][1]+self._DesignParameter['PMOS1']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][-1][1]+self._DesignParameter['PMOS1']['_DesignObj']._DesignParameter['_PODummyLayer']['_YWidth']/2)
			if _tmpLength_x*_tmpLength_x+_tmpLength_y*_tmpLength_y < drc._PolygateMinSpaceAtCorner*drc._PolygateMinSpaceAtCorner:
				_tmpY_to_Move=int(math.sqrt(drc._PolygateMinSpaceAtCorner*drc._PolygateMinSpaceAtCorner-_tmpLength_x*_tmpLength_x))+MinSnapSpacing
				self._DesignParameter['pmos1_gate']['_XYCoordinates'][0][1] = self._DesignParameter['PMOS1']['_XYCoordinates'][0][1]+self._DesignParameter['PMOS1']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][1]+self._DesignParameter['PMOS1']['_DesignObj']._DesignParameter['_PODummyLayer']['_YWidth']/2+self._DesignParameter['pmos1_gate']['_DesignObj']._DesignParameter['_POLayer']['_YWidth']/2+_tmpY_to_Move

		self._DesignParameter['pmos3_gate'] = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_Name='pmos3_gateIn{}'.format(_Name)))[0]
		self._DesignParameter['pmos3_gate']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(**dict(_ViaPoly2Met1NumberOfCOX=max(1, max(1, (1 + int(((((((self._DesignParameter['PMOS3']['_XYCoordinates'][1][0] + self._DesignParameter['PMOS3']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]) + (self._DesignParameter['PMOS3']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)) - ((self._DesignParameter['PMOS3']['_XYCoordinates'][1][0] + self._DesignParameter['PMOS3']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['PMOS3']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2))) - drc._CoMinSpace) - (2 * drc._CoMinEnclosureByPO)) / (drc._CoMinWidth + drc._CoMinSpace)))))), _ViaPoly2Met1NumberOfCOY=1))
		self._DesignParameter['pmos3_gate']['_XYCoordinates'] = [[self._DesignParameter['PMOS3']['_XYCoordinates'][0][0], max(((((self._DesignParameter['PMOS3']['_XYCoordinates'][1][1] + self._DesignParameter['PMOS3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1]) + (self._DesignParameter['PMOS3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_YWidth'] / 2)) + (self._DesignParameter['pmos3_gate']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)) + drc._Metal1MinSpace2), self._DesignParameter['PMOS3']['_XYCoordinates'][0][1]+self._DesignParameter['PMOS3']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth']/2+self._DesignParameter['pmos3_gate']['_DesignObj']._DesignParameter['_POLayer']['_YWidth']/2+31)], [self._DesignParameter['PMOS3']['_XYCoordinates'][1][0], max(((((self._DesignParameter['PMOS3']['_XYCoordinates'][1][1] + self._DesignParameter['PMOS3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1]) + (self._DesignParameter['PMOS3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_YWidth'] / 2)) + (self._DesignParameter['pmos3_gate']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)) + drc._Metal1MinSpace2), self._DesignParameter['PMOS3']['_XYCoordinates'][0][1]+self._DesignParameter['PMOS3']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth']/2+self._DesignParameter['pmos3_gate']['_DesignObj']._DesignParameter['_POLayer']['_YWidth']/2+31)]]
		if (pmos3_gate == 1):
			_tmpLength_x=(self._DesignParameter['PMOS3']['_XYCoordinates'][0][0]+self._DesignParameter['PMOS3']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][-1][0]-self._DesignParameter['PMOS3']['_DesignObj']._DesignParameter['_PODummyLayer']['_XWidth']/2)-(self._DesignParameter['pmos3_gate']['_XYCoordinates'][0][0]+self._DesignParameter['pmos3_gate']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']/2)
			_tmpLength_y=(self._DesignParameter['pmos3_gate']['_XYCoordinates'][0][1]-self._DesignParameter['pmos3_gate']['_DesignObj']._DesignParameter['_POLayer']['_YWidth']/2)-(self._DesignParameter['PMOS3']['_XYCoordinates'][0][1]+self._DesignParameter['PMOS3']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][-1][1]+self._DesignParameter['PMOS3']['_DesignObj']._DesignParameter['_PODummyLayer']['_YWidth']/2)
			if _tmpLength_x*_tmpLength_x+_tmpLength_y*_tmpLength_y < drc._PolygateMinSpaceAtCorner*drc._PolygateMinSpaceAtCorner:
				_tmpY_to_Move=int(math.sqrt(drc._PolygateMinSpaceAtCorner*drc._PolygateMinSpaceAtCorner-_tmpLength_x*_tmpLength_x))+MinSnapSpacing
				self._DesignParameter['pmos3_gate']['_XYCoordinates'][0][1] = self._DesignParameter['PMOS3']['_XYCoordinates'][0][1]+self._DesignParameter['PMOS3']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][1]+self._DesignParameter['PMOS3']['_DesignObj']._DesignParameter['_PODummyLayer']['_YWidth']/2+self._DesignParameter['pmos3_gate']['_DesignObj']._DesignParameter['_POLayer']['_YWidth']/2+_tmpY_to_Move
				self._DesignParameter['pmos3_gate']['_XYCoordinates'][1][1] = self._DesignParameter['PMOS3']['_XYCoordinates'][0][1]+self._DesignParameter['PMOS3']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][1]+self._DesignParameter['PMOS3']['_DesignObj']._DesignParameter['_PODummyLayer']['_YWidth']/2+self._DesignParameter['pmos3_gate']['_DesignObj']._DesignParameter['_POLayer']['_YWidth']/2+_tmpY_to_Move
		self._DesignParameter['pmos4_gate'] = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_Name='pmos4_gateIn{}'.format(_Name)))[0]
		self._DesignParameter['pmos4_gate']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(**dict(_ViaPoly2Met1NumberOfCOX=max(1, max(1, (1 + int(((((((self._DesignParameter['PMOS4']['_XYCoordinates'][1][0] + self._DesignParameter['PMOS4']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]) + (self._DesignParameter['PMOS4']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)) - ((self._DesignParameter['PMOS4']['_XYCoordinates'][1][0] + self._DesignParameter['PMOS4']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['PMOS4']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2))) - drc._CoMinSpace) - (2 * drc._CoMinEnclosureByPO)) / (drc._CoMinWidth + drc._CoMinSpace)))))), _ViaPoly2Met1NumberOfCOY=1))
		self._DesignParameter['pmos4_gate']['_XYCoordinates'] = [[self._DesignParameter['PMOS4']['_XYCoordinates'][0][0], max(((((self._DesignParameter['PMOS4']['_XYCoordinates'][1][1] + self._DesignParameter['PMOS4']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1]) + (self._DesignParameter['PMOS4']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_YWidth'] / 2)) + (self._DesignParameter['pmos4_gate']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)) + drc._Metal1MinSpace2), self._DesignParameter['PMOS4']['_XYCoordinates'][0][1]+self._DesignParameter['PMOS4']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth']/2+self._DesignParameter['pmos4_gate']['_DesignObj']._DesignParameter['_POLayer']['_YWidth']/2+31)], [self._DesignParameter['PMOS4']['_XYCoordinates'][1][0], max(((((self._DesignParameter['PMOS4']['_XYCoordinates'][1][1] + self._DesignParameter['PMOS4']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1]) + (self._DesignParameter['PMOS4']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_YWidth'] / 2)) + (self._DesignParameter['pmos4_gate']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)) + drc._Metal1MinSpace2), self._DesignParameter['PMOS4']['_XYCoordinates'][0][1]+self._DesignParameter['PMOS4']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth']/2+self._DesignParameter['pmos4_gate']['_DesignObj']._DesignParameter['_POLayer']['_YWidth']/2+31)]]
		if (pmos4_gate == 1):
			_tmpLength_x=(self._DesignParameter['PMOS4']['_XYCoordinates'][0][0]+self._DesignParameter['PMOS4']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][-1][0]-self._DesignParameter['PMOS4']['_DesignObj']._DesignParameter['_PODummyLayer']['_XWidth']/2)-(self._DesignParameter['pmos4_gate']['_XYCoordinates'][0][0]+self._DesignParameter['pmos4_gate']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']/2)
			_tmpLength_y=(self._DesignParameter['pmos4_gate']['_XYCoordinates'][0][1]-self._DesignParameter['pmos4_gate']['_DesignObj']._DesignParameter['_POLayer']['_YWidth']/2)-(self._DesignParameter['PMOS4']['_XYCoordinates'][0][1]+self._DesignParameter['PMOS4']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][-1][1]+self._DesignParameter['PMOS4']['_DesignObj']._DesignParameter['_PODummyLayer']['_YWidth']/2)
			if _tmpLength_x*_tmpLength_x+_tmpLength_y*_tmpLength_y < drc._PolygateMinSpaceAtCorner*drc._PolygateMinSpaceAtCorner:
				_tmpY_to_Move=int(math.sqrt(drc._PolygateMinSpaceAtCorner*drc._PolygateMinSpaceAtCorner-_tmpLength_x*_tmpLength_x))+MinSnapSpacing
				self._DesignParameter['pmos4_gate']['_XYCoordinates'][0][1] = self._DesignParameter['PMOS4']['_XYCoordinates'][0][1]+self._DesignParameter['PMOS4']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][1]+self._DesignParameter['PMOS4']['_DesignObj']._DesignParameter['_PODummyLayer']['_YWidth']/2+self._DesignParameter['pmos4_gate']['_DesignObj']._DesignParameter['_POLayer']['_YWidth']/2+_tmpY_to_Move
				self._DesignParameter['pmos4_gate']['_XYCoordinates'][1][1] = self._DesignParameter['PMOS4']['_XYCoordinates'][0][1]+self._DesignParameter['PMOS4']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][1]+self._DesignParameter['PMOS4']['_DesignObj']._DesignParameter['_PODummyLayer']['_YWidth']/2+self._DesignParameter['pmos4_gate']['_DesignObj']._DesignParameter['_POLayer']['_YWidth']/2+_tmpY_to_Move
		path_list = []
		xy_offset = [0, 0]
		if (len(self._DesignParameter['PMOS1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates']) == 1):
		    mode = 'vertical'
		    _width = self._DesignParameter['PMOS1']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
		elif (self._DesignParameter['PMOS1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0] == self._DesignParameter['PMOS1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]):
		    mode = 'horizontal'
		    _width = self._DesignParameter['PMOS1']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
		elif (self._DesignParameter['PMOS1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1] == self._DesignParameter['PMOS1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][1]):
		    mode = 'vertical'
		    _width = self._DesignParameter['PMOS1']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
		else:
		    print('Invalid Target Input')
		if (mode == 'vertical'):
		    xy_with_offset = []
		    target_y_value = [[(+ (self._DesignParameter['pmos1_gate']['_XYCoordinates'][0][0] + self._DesignParameter['pmos1_gate']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0])), (+ ((self._DesignParameter['pmos1_gate']['_XYCoordinates'][0][1] + self._DesignParameter['pmos1_gate']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1]) + (self._DesignParameter['pmos1_gate']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2)))]][0][1]
		    for i in range(len(self._DesignParameter['PMOS1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
		        xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['PMOS1']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['PMOS1']['_XYCoordinates'][0][1])], self._DesignParameter['PMOS1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		elif (mode == 'horizontal'):
		    xy_with_offset = []
		    target_x_value = [[(+ (self._DesignParameter['pmos1_gate']['_XYCoordinates'][0][0] + self._DesignParameter['pmos1_gate']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0])), (+ ((self._DesignParameter['pmos1_gate']['_XYCoordinates'][0][1] + self._DesignParameter['pmos1_gate']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1]) + (self._DesignParameter['pmos1_gate']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2)))]][0][0]
		    for i in range(len(self._DesignParameter['PMOS1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
		        xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['PMOS1']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['PMOS1']['_XYCoordinates'][0][1])], self._DesignParameter['PMOS1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		for i in range(len(path_list)):
		    path_list[i][0] = [(xy + offset) for (xy, offset) in zip(path_list[i][0], xy_offset)]
		self._DesignParameter['poly_pmos1'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _Width=_width)
		self._DesignParameter['poly_pmos1']['_XYCoordinates'] = path_list
		path_list = []
		xy_offset = [0, 0]
		if (len(self._DesignParameter['PMOS3']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates']) == 1):
		    mode = 'vertical'
		    _width = self._DesignParameter['PMOS3']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
		elif (self._DesignParameter['PMOS3']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0] == self._DesignParameter['PMOS3']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]):
		    mode = 'horizontal'
		    _width = self._DesignParameter['PMOS3']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
		elif (self._DesignParameter['PMOS3']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1] == self._DesignParameter['PMOS3']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][1]):
		    mode = 'vertical'
		    _width = self._DesignParameter['PMOS3']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
		else:
		    print('Invalid Target Input')
		if (mode == 'vertical'):
		    xy_with_offset = []
		    target_y_value = [[(+ (self._DesignParameter['pmos3_gate']['_XYCoordinates'][0][0] + self._DesignParameter['pmos3_gate']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0])), (+ ((self._DesignParameter['pmos3_gate']['_XYCoordinates'][0][1] + self._DesignParameter['pmos3_gate']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1]) + (self._DesignParameter['pmos3_gate']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2)))]][0][1]
		    for i in range(len(self._DesignParameter['PMOS3']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
		        xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['PMOS3']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['PMOS3']['_XYCoordinates'][0][1])], self._DesignParameter['PMOS3']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		elif (mode == 'horizontal'):
		    xy_with_offset = []
		    target_x_value = [[(+ (self._DesignParameter['pmos3_gate']['_XYCoordinates'][0][0] + self._DesignParameter['pmos3_gate']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0])), (+ ((self._DesignParameter['pmos3_gate']['_XYCoordinates'][0][1] + self._DesignParameter['pmos3_gate']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1]) + (self._DesignParameter['pmos3_gate']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2)))]][0][0]
		    for i in range(len(self._DesignParameter['PMOS3']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
		        xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['PMOS3']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['PMOS3']['_XYCoordinates'][0][1])], self._DesignParameter['PMOS3']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		for i in range(len(path_list)):
		    path_list[i][0] = [(xy + offset) for (xy, offset) in zip(path_list[i][0], xy_offset)]
		self._DesignParameter['poly_pmos3'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _Width=_width)
		self._DesignParameter['poly_pmos3']['_XYCoordinates'] = path_list
		path_list = []
		xy_offset = [0, 0]
		if (len(self._DesignParameter['PMOS3']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates']) == 1):
		    mode = 'vertical'
		    _width = self._DesignParameter['PMOS3']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
		elif (self._DesignParameter['PMOS3']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0] == self._DesignParameter['PMOS3']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]):
		    mode = 'horizontal'
		    _width = self._DesignParameter['PMOS3']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
		elif (self._DesignParameter['PMOS3']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1] == self._DesignParameter['PMOS3']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][1]):
		    mode = 'vertical'
		    _width = self._DesignParameter['PMOS3']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
		else:
		    print('Invalid Target Input')
		if (mode == 'vertical'):
		    xy_with_offset = []
		    target_y_value = [[(+ (self._DesignParameter['pmos3_gate']['_XYCoordinates'][1][0] + self._DesignParameter['pmos3_gate']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0])), (+ ((self._DesignParameter['pmos3_gate']['_XYCoordinates'][1][1] + self._DesignParameter['pmos3_gate']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1]) + (self._DesignParameter['pmos3_gate']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2)))]][0][1]
		    for i in range(len(self._DesignParameter['PMOS3']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
		        xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['PMOS3']['_XYCoordinates'][1][0]), (0 + self._DesignParameter['PMOS3']['_XYCoordinates'][1][1])], self._DesignParameter['PMOS3']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		elif (mode == 'horizontal'):
		    xy_with_offset = []
		    target_x_value = [[(+ (self._DesignParameter['pmos3_gate']['_XYCoordinates'][1][0] + self._DesignParameter['pmos3_gate']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0])), (+ ((self._DesignParameter['pmos3_gate']['_XYCoordinates'][1][1] + self._DesignParameter['pmos3_gate']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1]) + (self._DesignParameter['pmos3_gate']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2)))]][0][0]
		    for i in range(len(self._DesignParameter['PMOS3']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
		        xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['PMOS3']['_XYCoordinates'][1][0]), (0 + self._DesignParameter['PMOS3']['_XYCoordinates'][1][1])], self._DesignParameter['PMOS3']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		for i in range(len(path_list)):
		    path_list[i][0] = [(xy + offset) for (xy, offset) in zip(path_list[i][0], xy_offset)]
		self._DesignParameter['poly_pmos3_1'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _Width=_width)
		self._DesignParameter['poly_pmos3_1']['_XYCoordinates'] = path_list
		path_list = []
		xy_offset = [0, 0]
		if (len(self._DesignParameter['PMOS4']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates']) == 1):
		    mode = 'vertical'
		    _width = self._DesignParameter['PMOS4']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
		elif (self._DesignParameter['PMOS4']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0] == self._DesignParameter['PMOS4']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]):
		    mode = 'horizontal'
		    _width = self._DesignParameter['PMOS4']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
		elif (self._DesignParameter['PMOS4']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1] == self._DesignParameter['PMOS4']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][1]):
		    mode = 'vertical'
		    _width = self._DesignParameter['PMOS4']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
		else:
		    print('Invalid Target Input')
		if (mode == 'vertical'):
		    xy_with_offset = []
		    target_y_value = [[(+ (self._DesignParameter['pmos4_gate']['_XYCoordinates'][1][0] + self._DesignParameter['pmos4_gate']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0])), (+ ((self._DesignParameter['pmos4_gate']['_XYCoordinates'][1][1] + self._DesignParameter['pmos4_gate']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1]) + (self._DesignParameter['pmos4_gate']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2)))]][0][1]
		    for i in range(len(self._DesignParameter['PMOS4']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
		        xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['PMOS4']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['PMOS4']['_XYCoordinates'][0][1])], self._DesignParameter['PMOS4']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		elif (mode == 'horizontal'):
		    xy_with_offset = []
		    target_x_value = [[(+ (self._DesignParameter['pmos4_gate']['_XYCoordinates'][1][0] + self._DesignParameter['pmos4_gate']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0])), (+ ((self._DesignParameter['pmos4_gate']['_XYCoordinates'][1][1] + self._DesignParameter['pmos4_gate']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1]) + (self._DesignParameter['pmos4_gate']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2)))]][0][0]
		    for i in range(len(self._DesignParameter['PMOS4']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
		        xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['PMOS4']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['PMOS4']['_XYCoordinates'][0][1])], self._DesignParameter['PMOS4']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		for i in range(len(path_list)):
		    path_list[i][0] = [(xy + offset) for (xy, offset) in zip(path_list[i][0], xy_offset)]
		self._DesignParameter['poly_pmos4'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _Width=_width)
		self._DesignParameter['poly_pmos4']['_XYCoordinates'] = path_list
		path_list = []
		xy_offset = [0, 0]
		if (len(self._DesignParameter['PMOS4']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates']) == 1):
		    mode = 'vertical'
		    _width = self._DesignParameter['PMOS4']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
		elif (self._DesignParameter['PMOS4']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0] == self._DesignParameter['PMOS4']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]):
		    mode = 'horizontal'
		    _width = self._DesignParameter['PMOS4']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
		elif (self._DesignParameter['PMOS4']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1] == self._DesignParameter['PMOS4']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][1]):
		    mode = 'vertical'
		    _width = self._DesignParameter['PMOS4']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
		else:
		    print('Invalid Target Input')
		if (mode == 'vertical'):
		    xy_with_offset = []
		    target_y_value = [[(+ (self._DesignParameter['pmos4_gate']['_XYCoordinates'][1][0] + self._DesignParameter['pmos4_gate']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0])), (+ ((self._DesignParameter['pmos4_gate']['_XYCoordinates'][1][1] + self._DesignParameter['pmos4_gate']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1]) + (self._DesignParameter['pmos4_gate']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2)))]][0][1]
		    for i in range(len(self._DesignParameter['PMOS4']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
		        xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['PMOS4']['_XYCoordinates'][1][0]), (0 + self._DesignParameter['PMOS4']['_XYCoordinates'][1][1])], self._DesignParameter['PMOS4']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		elif (mode == 'horizontal'):
		    xy_with_offset = []
		    target_x_value = [[(+ (self._DesignParameter['pmos4_gate']['_XYCoordinates'][1][0] + self._DesignParameter['pmos4_gate']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0])), (+ ((self._DesignParameter['pmos4_gate']['_XYCoordinates'][1][1] + self._DesignParameter['pmos4_gate']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1]) + (self._DesignParameter['pmos4_gate']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2)))]][0][0]
		    for i in range(len(self._DesignParameter['PMOS4']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
		        xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['PMOS4']['_XYCoordinates'][1][0]), (0 + self._DesignParameter['PMOS4']['_XYCoordinates'][1][1])], self._DesignParameter['PMOS4']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		for i in range(len(path_list)):
		    path_list[i][0] = [(xy + offset) for (xy, offset) in zip(path_list[i][0], xy_offset)]
		self._DesignParameter['poly_pmos4_1'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _Width=_width)
		self._DesignParameter['poly_pmos4_1']['_XYCoordinates'] = path_list
		self._DesignParameter['poly_pmos1_x'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _Width=self._DesignParameter['pmos1_gate']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'])
		self._DesignParameter['poly_pmos1_x']['_XYCoordinates'] = [[[((self._DesignParameter['PMOS1']['_XYCoordinates'][0][0] + self._DesignParameter['PMOS1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['PMOS1']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)), self._DesignParameter['pmos1_gate']['_XYCoordinates'][0][1]], [((self._DesignParameter['PMOS1']['_XYCoordinates'][0][0] + self._DesignParameter['PMOS1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]) + (self._DesignParameter['PMOS1']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)), self._DesignParameter['pmos1_gate']['_XYCoordinates'][0][1]]]]
		self._DesignParameter['poly_pmos3_x'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _Width=self._DesignParameter['pmos3_gate']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'])
		self._DesignParameter['poly_pmos3_x']['_XYCoordinates'] = [[[((self._DesignParameter['PMOS3']['_XYCoordinates'][0][0] + self._DesignParameter['PMOS3']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['PMOS3']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)), self._DesignParameter['pmos3_gate']['_XYCoordinates'][0][1]], [((self._DesignParameter['PMOS3']['_XYCoordinates'][0][0] + self._DesignParameter['PMOS3']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]) + (self._DesignParameter['PMOS3']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)), self._DesignParameter['pmos3_gate']['_XYCoordinates'][0][1]]], [[((self._DesignParameter['PMOS3']['_XYCoordinates'][1][0] + self._DesignParameter['PMOS3']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['PMOS3']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)), self._DesignParameter['pmos3_gate']['_XYCoordinates'][0][1]], [((self._DesignParameter['PMOS3']['_XYCoordinates'][1][0] + self._DesignParameter['PMOS3']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]) + (self._DesignParameter['PMOS3']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)), self._DesignParameter['pmos3_gate']['_XYCoordinates'][0][1]]]]
		self._DesignParameter['poly_pmos4_x'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _Width=self._DesignParameter['pmos4_gate']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'])
		self._DesignParameter['poly_pmos4_x']['_XYCoordinates'] = [[[((self._DesignParameter['PMOS4']['_XYCoordinates'][0][0] + self._DesignParameter['PMOS4']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['PMOS4']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)), self._DesignParameter['pmos4_gate']['_XYCoordinates'][0][1]], [((self._DesignParameter['PMOS4']['_XYCoordinates'][0][0] + self._DesignParameter['PMOS4']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]) + (self._DesignParameter['PMOS4']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)), self._DesignParameter['pmos4_gate']['_XYCoordinates'][0][1]]], [[((self._DesignParameter['PMOS4']['_XYCoordinates'][1][0] + self._DesignParameter['PMOS4']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['PMOS4']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)), self._DesignParameter['pmos4_gate']['_XYCoordinates'][0][1]], [((self._DesignParameter['PMOS4']['_XYCoordinates'][1][0] + self._DesignParameter['PMOS4']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]) + (self._DesignParameter['PMOS4']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)), self._DesignParameter['pmos4_gate']['_XYCoordinates'][0][1]]]]
		self._DesignParameter['via_m1_m2_pmos2_gate'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='via_m1_m2_pmos2_gateIn{}'.format(_Name)))[0]
		self._DesignParameter['via_m1_m2_pmos2_gate']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureY(**dict(_ViaMet12Met2NumberOfCOX=max(2, max(1, (1 + int((((self._DesignParameter['pmos2_gate']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] - drc._VIAxMinSpace) - (2 * drc._VIAxMinEnclosureByMetx)) / (drc._VIAxMinWidth + drc._VIAxMinSpace)))))), _ViaMet12Met2NumberOfCOY=1))
		self._DesignParameter['via_m1_m2_pmos2_gate']['_XYCoordinates'] = [[self._DesignParameter['pmos2_gate']['_XYCoordinates'][0][0], (((self._DesignParameter['pmos2_gate']['_XYCoordinates'][0][1] + self._DesignParameter['pmos2_gate']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) - (self._DesignParameter['pmos2_gate']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)) + (self._DesignParameter['via_m1_m2_pmos2_gate']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2))], [self._DesignParameter['pmos2_gate']['_XYCoordinates'][(- 1)][0], (((self._DesignParameter['pmos2_gate']['_XYCoordinates'][1][1] + self._DesignParameter['pmos2_gate']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) - (self._DesignParameter['pmos2_gate']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)) + (self._DesignParameter['via_m1_m2_pmos2_gate']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2))]]
		self._DesignParameter['via_m1_m3_pmos_supply'] = self._SrefElementDeclaration(_DesignObj=ViaStack._ViaStack(_Name='via_m1_m3_pmos_supplyIn{}'.format(_Name)))[0]
		self._DesignParameter['via_m1_m3_pmos_supply']['_DesignObj']._CalculateStackMinimumEnclosureX(**dict(COX=1, COY=max(2, max(1, (1 + int((((self._DesignParameter['PMOS1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_YWidth'] - drc._VIAxMinSpace) - (2 * drc._VIAxMinEnclosureByMetx)) / (drc._VIAxMinWidth + drc._VIAxMinSpace)))))), start_layer=1, end_layer=3))
		self._DesignParameter['via_m1_m3_pmos_supply']['_XYCoordinates'] = [[(self._DesignParameter['PMOS1']['_XYCoordinates'][0][0] + self._DesignParameter['PMOS1']['_DesignObj']._DesignParameter['_XYCoordinatePMOSSupplyRouting']['_XYCoordinates'][0][0]), (self._DesignParameter['PMOS1']['_XYCoordinates'][0][1] + self._DesignParameter['PMOS1']['_DesignObj']._DesignParameter['_XYCoordinatePMOSSupplyRouting']['_XYCoordinates'][0][1])]]
		# self._DesignParameter['via_m1_m3_pmos_output'] = self._SrefElementDeclaration(_DesignObj=ViaStack._ViaStack(_Name='via_m1_m3_pmos_outputIn{}'.format(_Name)))[0]
		# self._DesignParameter['via_m1_m3_pmos_output']['_DesignObj']._CalculateStackMinimumEnclosureX(**dict(COX=1, COY=max(2, max(1, (1 + int((((self._DesignParameter['PMOS1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_YWidth'] - drc._VIAxMinSpace) - (2 * drc._VIAxMinEnclosureByMetx)) / (drc._VIAxMinWidth + drc._VIAxMinSpace)))))), start_layer=1, end_layer=3))
		# self._DesignParameter['via_m1_m3_pmos_output']['_XYCoordinates'] = [[(self._DesignParameter['PMOS1']['_XYCoordinates'][0][0] + self._DesignParameter['PMOS1']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][(- 1)][0]), (self._DesignParameter['PMOS1']['_XYCoordinates'][0][1] + self._DesignParameter['PMOS1']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][(- 1)][1])]]
		self._DesignParameter['m2_pmos1_pmos2_y'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _Width=self._DesignParameter['via_m1_m3_pmos_supply']['_DesignObj']._DesignParameter['ViaMet22Met3']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth'])
		self._DesignParameter['m2_pmos1_pmos2_y']['_XYCoordinates'] = [[[self._DesignParameter['via_m1_m3_pmos_supply']['_XYCoordinates'][0][0], self._DesignParameter['via_m1_m3_pmos_supply']['_XYCoordinates'][0][1]], [self._DesignParameter['via_m1_m3_pmos_supply']['_XYCoordinates'][0][0], self._DesignParameter['via_m1_m2_pmos2_gate']['_XYCoordinates'][0][1]]], [[self._DesignParameter['via_m1_m3_pmos_output']['_XYCoordinates'][0][0], self._DesignParameter['via_m1_m3_pmos_output']['_XYCoordinates'][0][1]], [self._DesignParameter['via_m1_m3_pmos_output']['_XYCoordinates'][0][0], self._DesignParameter['via_m1_m2_pmos2_gate']['_XYCoordinates'][(- 1)][1]]]]
		self._DesignParameter['m2_pmos1_pmos2_x'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _Width=self._DesignParameter['via_m1_m2_pmos2_gate']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'])
		self._DesignParameter['m2_pmos1_pmos2_x']['_XYCoordinates'] = [[[self._DesignParameter['via_m1_m2_pmos2_gate']['_XYCoordinates'][0][0], self._DesignParameter['via_m1_m2_pmos2_gate']['_XYCoordinates'][0][1]], [(((self._DesignParameter['via_m1_m3_pmos_supply']['_XYCoordinates'][0][0] + self._DesignParameter['via_m1_m3_pmos_supply']['_DesignObj']._DesignParameter['ViaMet22Met3']['_XYCoordinates'][0][0]) + self._DesignParameter['via_m1_m3_pmos_supply']['_DesignObj']._DesignParameter['ViaMet22Met3']['_DesignObj']._DesignParameter['_Met2Layer']['_XYCoordinates'][0][0]) + (self._DesignParameter['via_m1_m3_pmos_supply']['_DesignObj']._DesignParameter['ViaMet22Met3']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth'] / 2)), self._DesignParameter['via_m1_m2_pmos2_gate']['_XYCoordinates'][0][1]]], [[self._DesignParameter['via_m1_m2_pmos2_gate']['_XYCoordinates'][(- 1)][0], self._DesignParameter['via_m1_m2_pmos2_gate']['_XYCoordinates'][(- 1)][1]], [(((self._DesignParameter['via_m1_m3_pmos_output']['_XYCoordinates'][0][0] + self._DesignParameter['via_m1_m3_pmos_output']['_DesignObj']._DesignParameter['ViaMet22Met3']['_XYCoordinates'][0][0]) + self._DesignParameter['via_m1_m3_pmos_output']['_DesignObj']._DesignParameter['ViaMet22Met3']['_DesignObj']._DesignParameter['_Met2Layer']['_XYCoordinates'][0][0]) - (self._DesignParameter['via_m1_m3_pmos_output']['_DesignObj']._DesignParameter['ViaMet22Met3']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth'] / 2)), self._DesignParameter['via_m1_m2_pmos2_gate']['_XYCoordinates'][(- 1)][1]]]]
		self._DesignParameter['nguardring'] = self._SrefElementDeclaration(_DesignObj=NSubRing.NSubRing(_Name='nguardringIn{}'.format(_Name)))[0]
		self._DesignParameter['nguardring']['_DesignObj']._CalculateDesignParameter(**dict(height=5000, width=5000, contact_bottom=pguardring_co_bot, contact_top=pguardring_co_top, contact_left=pguardring_co_left, contact_right=pguardring_co_right))
		self._DesignParameter['nguardring']['_XYCoordinates'] = [[0.0, 0.0]]
		self._DesignParameter['nguardring']['_DesignObj']._CalculateDesignParameter(**dict(height=((max((self._DesignParameter['pmos1_gate']['_XYCoordinates'][0][1] + self._DesignParameter['pmos1_gate']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1] + self._DesignParameter['pmos1_gate']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2), (self._DesignParameter['pmos3_gate']['_XYCoordinates'][0][1] + self._DesignParameter['pmos3_gate']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1] + self._DesignParameter['pmos3_gate']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2), (self._DesignParameter['pmos4_gate']['_XYCoordinates'][0][1] + self._DesignParameter['pmos4_gate']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1] + self._DesignParameter['pmos4_gate']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2), (self._DesignParameter['PMOS2']['_XYCoordinates'][0][1]+self._DesignParameter['PMOS2']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']/2)) + self._DesignParameter['nguardring']['_DesignObj']._DesignParameter['met_top']['_YWidth'] / 2 + drc._Metal1MinSpace3 - ((min(((self._DesignParameter['PMOS4']['_XYCoordinates'][1][1] + self._DesignParameter['PMOS4']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1]) - (self._DesignParameter['PMOS4']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_YWidth'] / 2)), ((self._DesignParameter['PMOS3']['_XYCoordinates'][1][1] + self._DesignParameter['PMOS3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1]) - (self._DesignParameter['PMOS3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_YWidth'] / 2)), ((self._DesignParameter['pmos2_gate']['_XYCoordinates'][1][1] + self._DesignParameter['pmos2_gate']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) - (self._DesignParameter['pmos2_gate']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)), (self._DesignParameter['m1_pmos_x']['_XYCoordinates'][0][0][1] - (self._DesignParameter['m1_pmos_x']['_Width'] / 2))) - (self._DesignParameter['nguardring']['_DesignObj']._DesignParameter['met_bot']['_YWidth'] / 2)) - drc._Metal1MinSpace3))), width=(((((self._DesignParameter['PMOS4']['_XYCoordinates'][1][0] + self._DesignParameter['PMOS4']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][0]) + (self._DesignParameter['PMOS4']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth'] / 2)) + (self._DesignParameter['nguardring']['_DesignObj']._DesignParameter['met_right']['_XWidth'] / 2)) + drc._Metal1MinSpace3 + drc._Metal1MinSpace) - ((((self._DesignParameter['PMOS4']['_XYCoordinates'][0][0] + self._DesignParameter['PMOS4']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][0]) - (self._DesignParameter['PMOS4']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth'] / 2)) - (self._DesignParameter['nguardring']['_DesignObj']._DesignParameter['met_left']['_XWidth'] / 2)) - drc._Metal1MinSpace3 - drc._Metal1MinSpace)), contact_bottom=pguardring_co_bot, contact_top=pguardring_co_top, contact_left=pguardring_co_left, contact_right=pguardring_co_right))
		self._DesignParameter['nguardring']['_XYCoordinates'] = [[self._DesignParameter['PMOS1']['_XYCoordinates'][0][0], (((max((self._DesignParameter['pmos1_gate']['_XYCoordinates'][0][1] + self._DesignParameter['pmos1_gate']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1] + self._DesignParameter['pmos1_gate']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2), (self._DesignParameter['pmos3_gate']['_XYCoordinates'][0][1] + self._DesignParameter['pmos3_gate']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1] + self._DesignParameter['pmos3_gate']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2), (self._DesignParameter['pmos4_gate']['_XYCoordinates'][0][1] + self._DesignParameter['pmos4_gate']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1] + self._DesignParameter['pmos4_gate']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2), (self._DesignParameter['PMOS2']['_XYCoordinates'][0][1]+self._DesignParameter['PMOS2']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']/2)) + self._DesignParameter['nguardring']['_DesignObj']._DesignParameter['met_top']['_YWidth'] / 2 + drc._Metal1MinSpace3 + ((min(((self._DesignParameter['PMOS4']['_XYCoordinates'][1][1] + self._DesignParameter['PMOS4']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1]) - (self._DesignParameter['PMOS4']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_YWidth'] / 2)), ((self._DesignParameter['PMOS3']['_XYCoordinates'][1][1] + self._DesignParameter['PMOS3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1]) - (self._DesignParameter['PMOS3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_YWidth'] / 2)), ((self._DesignParameter['pmos2_gate']['_XYCoordinates'][1][1] + self._DesignParameter['pmos2_gate']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) - (self._DesignParameter['pmos2_gate']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)), (self._DesignParameter['m1_pmos_x']['_XYCoordinates'][0][0][1] - (self._DesignParameter['m1_pmos_x']['_Width'] / 2))) - (self._DesignParameter['nguardring']['_DesignObj']._DesignParameter['met_bot']['_YWidth'] / 2)) - drc._Metal1MinSpace3))))/2]]
		path_list = []
		xy_offset = [0, 0]
		if (len(self._DesignParameter['PMOS4']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates']) == 1):
		    mode = 'vertical'
		    _width = self._DesignParameter['PMOS4']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth']
		elif (self._DesignParameter['PMOS4']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][0] == self._DesignParameter['PMOS4']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][0]):
		    mode = 'horizontal'
		    _width = self._DesignParameter['PMOS4']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth']
		elif (self._DesignParameter['PMOS4']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1] == self._DesignParameter['PMOS4']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][1]):
		    mode = 'vertical'
		    _width = self._DesignParameter['PMOS4']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth']
		else:
		    print('Invalid Target Input')
		if (mode == 'vertical'):
		    xy_with_offset = []
		    target_y_value = [[(+ (self._DesignParameter['nguardring']['_XYCoordinates'][0][0] + self._DesignParameter['nguardring']['_DesignObj']._DesignParameter['met_bot']['_XYCoordinates'][0][0])), (+ (self._DesignParameter['nguardring']['_XYCoordinates'][0][1] + self._DesignParameter['nguardring']['_DesignObj']._DesignParameter['met_bot']['_XYCoordinates'][0][1]))]][0][1]
		    for i in range(len(self._DesignParameter['PMOS4']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		        if ((i % 2) == 0):
		            xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['PMOS4']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['PMOS4']['_XYCoordinates'][0][1])], self._DesignParameter['PMOS4']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		elif (mode == 'horizontal'):
		    xy_with_offset = []
		    target_x_value = [[(+ (self._DesignParameter['nguardring']['_XYCoordinates'][0][0] + self._DesignParameter['nguardring']['_DesignObj']._DesignParameter['met_bot']['_XYCoordinates'][0][0])), (+ (self._DesignParameter['nguardring']['_XYCoordinates'][0][1] + self._DesignParameter['nguardring']['_DesignObj']._DesignParameter['met_bot']['_XYCoordinates'][0][1]))]][0][0]
		    for i in range(len(self._DesignParameter['PMOS4']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		        if ((i % 2) == 0):
		            xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['PMOS4']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['PMOS4']['_XYCoordinates'][0][1])], self._DesignParameter['PMOS4']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		for i in range(len(path_list)):
		    path_list[i][0] = [(xy + offset) for (xy, offset) in zip(path_list[i][0], xy_offset)]
		self._DesignParameter['m1_pmos4_supply'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=_width)
		self._DesignParameter['m1_pmos4_supply']['_XYCoordinates'] = path_list
		path_list = []
		xy_offset = [0, 0]
		if (len(self._DesignParameter['PMOS4']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)::(- 2)]) == 1):
		    mode = 'vertical'
		    _width = self._DesignParameter['PMOS4']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth']
		elif (self._DesignParameter['PMOS4']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)::(- 2)][0][0] == self._DesignParameter['PMOS4']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)::(- 2)][(- 1)][0]):
		    mode = 'horizontal'
		    _width = self._DesignParameter['PMOS4']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth']
		elif (self._DesignParameter['PMOS4']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)::(- 2)][0][1] == self._DesignParameter['PMOS4']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)::(- 2)][(- 1)][1]):
		    mode = 'vertical'
		    _width = self._DesignParameter['PMOS4']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth']
		else:
		    print('Invalid Target Input')
		if (mode == 'vertical'):
		    xy_with_offset = []
		    target_y_value = [[(+ (self._DesignParameter['nguardring']['_XYCoordinates'][0][0] + self._DesignParameter['nguardring']['_DesignObj']._DesignParameter['met_bot']['_XYCoordinates'][0][0])), (+ (self._DesignParameter['nguardring']['_XYCoordinates'][0][1] + self._DesignParameter['nguardring']['_DesignObj']._DesignParameter['met_bot']['_XYCoordinates'][0][1]))]][0][1]
		    for element in self._DesignParameter['PMOS4']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)::(- 2)]:
		        xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['PMOS4']['_XYCoordinates'][1][0]), (0 + self._DesignParameter['PMOS4']['_XYCoordinates'][1][1])], element)])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		elif (mode == 'horizontal'):
		    xy_with_offset = []
		    target_x_value = [[(+ (self._DesignParameter['nguardring']['_XYCoordinates'][0][0] + self._DesignParameter['nguardring']['_DesignObj']._DesignParameter['met_bot']['_XYCoordinates'][0][0])), (+ (self._DesignParameter['nguardring']['_XYCoordinates'][0][1] + self._DesignParameter['nguardring']['_DesignObj']._DesignParameter['met_bot']['_XYCoordinates'][0][1]))]][0][0]
		    for element in self._DesignParameter['PMOS4']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)::(- 2)]:
		        xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['PMOS4']['_XYCoordinates'][1][0]), (0 + self._DesignParameter['PMOS4']['_XYCoordinates'][1][1])], element)])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		for i in range(len(path_list)):
		    path_list[i][0] = [(xy + offset) for (xy, offset) in zip(path_list[i][0], xy_offset)]
		self._DesignParameter['m1_pmos4_1_supply'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=_width)
		self._DesignParameter['m1_pmos4_1_supply']['_XYCoordinates'] = path_list
		path_list = []
		xy_offset = [0, 0]
		if (len(self._DesignParameter['PMOS3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates']) == 1):
		    mode = 'vertical'
		    _width = self._DesignParameter['PMOS3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth']
		elif (self._DesignParameter['PMOS3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][0] == self._DesignParameter['PMOS3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][0]):
		    mode = 'horizontal'
		    _width = self._DesignParameter['PMOS3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth']
		elif (self._DesignParameter['PMOS3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1] == self._DesignParameter['PMOS3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][1]):
		    mode = 'vertical'
		    _width = self._DesignParameter['PMOS3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth']
		else:
		    print('Invalid Target Input')
		if (mode == 'vertical'):
		    xy_with_offset = []
		    target_y_value = [[(+ (self._DesignParameter['nguardring']['_XYCoordinates'][0][0] + self._DesignParameter['nguardring']['_DesignObj']._DesignParameter['met_bot']['_XYCoordinates'][0][0])), (+ (self._DesignParameter['nguardring']['_XYCoordinates'][0][1] + self._DesignParameter['nguardring']['_DesignObj']._DesignParameter['met_bot']['_XYCoordinates'][0][1]))]][0][1]
		    for i in range(len(self._DesignParameter['PMOS3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		        if ((i % 2) == 0):
		            xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['PMOS3']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['PMOS3']['_XYCoordinates'][0][1])], self._DesignParameter['PMOS3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		elif (mode == 'horizontal'):
		    xy_with_offset = []
		    target_x_value = [[(+ (self._DesignParameter['nguardring']['_XYCoordinates'][0][0] + self._DesignParameter['nguardring']['_DesignObj']._DesignParameter['met_bot']['_XYCoordinates'][0][0])), (+ (self._DesignParameter['nguardring']['_XYCoordinates'][0][1] + self._DesignParameter['nguardring']['_DesignObj']._DesignParameter['met_bot']['_XYCoordinates'][0][1]))]][0][0]
		    for i in range(len(self._DesignParameter['PMOS3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		        if ((i % 2) == 0):
		            xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['PMOS3']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['PMOS3']['_XYCoordinates'][0][1])], self._DesignParameter['PMOS3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		for i in range(len(path_list)):
		    path_list[i][0] = [(xy + offset) for (xy, offset) in zip(path_list[i][0], xy_offset)]
		self._DesignParameter['m1_pmos3_supply'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=_width)
		self._DesignParameter['m1_pmos3_supply']['_XYCoordinates'] = path_list
		path_list = []
		xy_offset = [0, 0]
		if (len(self._DesignParameter['PMOS3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)::(- 2)]) == 1):
		    mode = 'vertical'
		    _width = self._DesignParameter['PMOS3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth']
		elif (self._DesignParameter['PMOS3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)::(- 2)][0][0] == self._DesignParameter['PMOS3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)::(- 2)][(- 1)][0]):
		    mode = 'horizontal'
		    _width = self._DesignParameter['PMOS3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth']
		elif (self._DesignParameter['PMOS3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)::(- 2)][0][1] == self._DesignParameter['PMOS3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)::(- 2)][(- 1)][1]):
		    mode = 'vertical'
		    _width = self._DesignParameter['PMOS3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth']
		else:
		    print('Invalid Target Input')
		if (mode == 'vertical'):
		    xy_with_offset = []
		    target_y_value = [[(+ (self._DesignParameter['nguardring']['_XYCoordinates'][0][0] + self._DesignParameter['nguardring']['_DesignObj']._DesignParameter['met_bot']['_XYCoordinates'][0][0])), (+ (self._DesignParameter['nguardring']['_XYCoordinates'][0][1] + self._DesignParameter['nguardring']['_DesignObj']._DesignParameter['met_bot']['_XYCoordinates'][0][1]))]][0][1]
		    for element in self._DesignParameter['PMOS3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)::(- 2)]:
		        xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['PMOS3']['_XYCoordinates'][1][0]), (0 + self._DesignParameter['PMOS3']['_XYCoordinates'][1][1])], element)])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		elif (mode == 'horizontal'):
		    xy_with_offset = []
		    target_x_value = [[(+ (self._DesignParameter['nguardring']['_XYCoordinates'][0][0] + self._DesignParameter['nguardring']['_DesignObj']._DesignParameter['met_bot']['_XYCoordinates'][0][0])), (+ (self._DesignParameter['nguardring']['_XYCoordinates'][0][1] + self._DesignParameter['nguardring']['_DesignObj']._DesignParameter['met_bot']['_XYCoordinates'][0][1]))]][0][0]
		    for element in self._DesignParameter['PMOS3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)::(- 2)]:
		        xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['PMOS3']['_XYCoordinates'][1][0]), (0 + self._DesignParameter['PMOS3']['_XYCoordinates'][1][1])], element)])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		for i in range(len(path_list)):
		    path_list[i][0] = [(xy + offset) for (xy, offset) in zip(path_list[i][0], xy_offset)]
		self._DesignParameter['m1_pmos3_1_supply'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=_width)
		self._DesignParameter['m1_pmos3_1_supply']['_XYCoordinates'] = path_list
		path_list = []
		xy_offset = [0, 0]
		if (len(self._DesignParameter['PMOS2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates']) == 1):
		    mode = 'vertical'
		    _width = self._DesignParameter['PMOS2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth']
		elif (self._DesignParameter['PMOS2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][0] == self._DesignParameter['PMOS2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][0]):
		    mode = 'horizontal'
		    _width = self._DesignParameter['PMOS2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth']
		elif (self._DesignParameter['PMOS2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1] == self._DesignParameter['PMOS2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][1]):
		    mode = 'vertical'
		    _width = self._DesignParameter['PMOS2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth']
		else:
		    print('Invalid Target Input')
		if (mode == 'vertical'):
		    xy_with_offset = []
		    target_y_value = [[(+ (self._DesignParameter['nguardring']['_XYCoordinates'][0][0] + self._DesignParameter['nguardring']['_DesignObj']._DesignParameter['met_top']['_XYCoordinates'][0][0])), (+ (self._DesignParameter['nguardring']['_XYCoordinates'][0][1] + self._DesignParameter['nguardring']['_DesignObj']._DesignParameter['met_top']['_XYCoordinates'][0][1]))]][0][1]
		    for i in range(len(self._DesignParameter['PMOS2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		        if ((i % 2) == 0):
		            xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['PMOS2']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['PMOS2']['_XYCoordinates'][0][1])], self._DesignParameter['PMOS2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		elif (mode == 'horizontal'):
		    xy_with_offset = []
		    target_x_value = [[(+ (self._DesignParameter['nguardring']['_XYCoordinates'][0][0] + self._DesignParameter['nguardring']['_DesignObj']._DesignParameter['met_top']['_XYCoordinates'][0][0])), (+ (self._DesignParameter['nguardring']['_XYCoordinates'][0][1] + self._DesignParameter['nguardring']['_DesignObj']._DesignParameter['met_top']['_XYCoordinates'][0][1]))]][0][0]
		    for i in range(len(self._DesignParameter['PMOS2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		        if ((i % 2) == 0):
		            xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['PMOS2']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['PMOS2']['_XYCoordinates'][0][1])], self._DesignParameter['PMOS2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		for i in range(len(path_list)):
		    path_list[i][0] = [(xy + offset) for (xy, offset) in zip(path_list[i][0], xy_offset)]
		self._DesignParameter['m1_pmos2_supply'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=_width)
		self._DesignParameter['m1_pmos2_supply']['_XYCoordinates'] = path_list
		path_list = []
		xy_offset = [0, 0]
		if (len(self._DesignParameter['PMOS2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)::(- 2)]) == 1):
		    mode = 'vertical'
		    _width = self._DesignParameter['PMOS2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth']
		elif (self._DesignParameter['PMOS2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)::(- 2)][0][0] == self._DesignParameter['PMOS2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)::(- 2)][(- 1)][0]):
		    mode = 'horizontal'
		    _width = self._DesignParameter['PMOS2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth']
		elif (self._DesignParameter['PMOS2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)::(- 2)][0][1] == self._DesignParameter['PMOS2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)::(- 2)][(- 1)][1]):
		    mode = 'vertical'
		    _width = self._DesignParameter['PMOS2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth']
		else:
		    print('Invalid Target Input')
		if (mode == 'vertical'):
		    xy_with_offset = []
		    target_y_value = [[(+ (self._DesignParameter['nguardring']['_XYCoordinates'][0][0] + self._DesignParameter['nguardring']['_DesignObj']._DesignParameter['met_top']['_XYCoordinates'][0][0])), (+ (self._DesignParameter['nguardring']['_XYCoordinates'][0][1] + self._DesignParameter['nguardring']['_DesignObj']._DesignParameter['met_top']['_XYCoordinates'][0][1]))]][0][1]
		    for element in self._DesignParameter['PMOS2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)::(- 2)]:
		        xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['PMOS2']['_XYCoordinates'][1][0]), (0 + self._DesignParameter['PMOS2']['_XYCoordinates'][1][1])], element)])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		elif (mode == 'horizontal'):
		    xy_with_offset = []
		    target_x_value = [[(+ (self._DesignParameter['nguardring']['_XYCoordinates'][0][0] + self._DesignParameter['nguardring']['_DesignObj']._DesignParameter['met_top']['_XYCoordinates'][0][0])), (+ (self._DesignParameter['nguardring']['_XYCoordinates'][0][1] + self._DesignParameter['nguardring']['_DesignObj']._DesignParameter['met_top']['_XYCoordinates'][0][1]))]][0][0]
		    for element in self._DesignParameter['PMOS2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)::(- 2)]:
		        xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['PMOS2']['_XYCoordinates'][1][0]), (0 + self._DesignParameter['PMOS2']['_XYCoordinates'][1][1])], element)])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		for i in range(len(path_list)):
		    path_list[i][0] = [(xy + offset) for (xy, offset) in zip(path_list[i][0], xy_offset)]
		self._DesignParameter['m1_pmos2_1_supply'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=_width)
		self._DesignParameter['m1_pmos2_1_supply']['_XYCoordinates'] = path_list
		self._DesignParameter['slvt'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['SLVT'][0], _Datatype=DesignParameters._LayerMapping['SLVT'][1], _XWidth=(((self._DesignParameter['PMOS4']['_XYCoordinates'][1][0] + self._DesignParameter['PMOS4']['_DesignObj']._DesignParameter['_SLVTLayer']['_XYCoordinates'][0][0]) + (self._DesignParameter['PMOS4']['_DesignObj']._DesignParameter['_SLVTLayer']['_XWidth'] / 2)) - ((self._DesignParameter['PMOS4']['_XYCoordinates'][0][0] + self._DesignParameter['PMOS4']['_DesignObj']._DesignParameter['_SLVTLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['PMOS4']['_DesignObj']._DesignParameter['_SLVTLayer']['_XWidth'] / 2))), _YWidth=max(self._DesignParameter['PMOS4']['_DesignObj']._DesignParameter['_SLVTLayer']['_YWidth'], self._DesignParameter['PMOS3']['_DesignObj']._DesignParameter['_SLVTLayer']['_YWidth'], self._DesignParameter['PMOS2']['_DesignObj']._DesignParameter['_SLVTLayer']['_YWidth'], self._DesignParameter['PMOS1']['_DesignObj']._DesignParameter['_SLVTLayer']['_YWidth']))
		self._DesignParameter['slvt']['_XYCoordinates'] = [[(+ self._DesignParameter['PMOS1']['_XYCoordinates'][0][0]), (+ self._DesignParameter['PMOS1']['_XYCoordinates'][0][1])]]
		self._DesignParameter['pp'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['PIMP'][0], _Datatype=DesignParameters._LayerMapping['PIMP'][1], _XWidth=(((self._DesignParameter['PMOS4']['_XYCoordinates'][1][0] + self._DesignParameter['PMOS4']['_DesignObj']._DesignParameter['_PPLayer']['_XYCoordinates'][0][0]) + (self._DesignParameter['PMOS4']['_DesignObj']._DesignParameter['_PPLayer']['_XWidth'] / 2)) - ((self._DesignParameter['PMOS4']['_XYCoordinates'][0][0] + self._DesignParameter['PMOS4']['_DesignObj']._DesignParameter['_PPLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['PMOS4']['_DesignObj']._DesignParameter['_PPLayer']['_XWidth'] / 2))), _YWidth=max(self._DesignParameter['PMOS4']['_DesignObj']._DesignParameter['_PPLayer']['_YWidth'], self._DesignParameter['PMOS3']['_DesignObj']._DesignParameter['_PPLayer']['_YWidth'], self._DesignParameter['PMOS2']['_DesignObj']._DesignParameter['_PPLayer']['_YWidth'], self._DesignParameter['PMOS1']['_DesignObj']._DesignParameter['_PPLayer']['_YWidth']))
		self._DesignParameter['pp']['_XYCoordinates'] = [[(+ self._DesignParameter['PMOS1']['_XYCoordinates'][0][0]), (+ self._DesignParameter['PMOS1']['_XYCoordinates'][0][1])]]
		self._DesignParameter['nwell'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['NWELL'][0], _Datatype=DesignParameters._LayerMapping['NWELL'][1], _XWidth=((self._DesignParameter['nguardring']['_XYCoordinates'][0][0] + self._DesignParameter['nguardring']['_DesignObj']._DesignParameter['nw_right']['_XYCoordinates'][0][0]) - (self._DesignParameter['nguardring']['_XYCoordinates'][0][0] + self._DesignParameter['nguardring']['_DesignObj']._DesignParameter['nw_left']['_XYCoordinates'][0][0])), _YWidth=((self._DesignParameter['nguardring']['_XYCoordinates'][0][1] + self._DesignParameter['nguardring']['_DesignObj']._DesignParameter['nw_top']['_XYCoordinates'][0][1]) - (self._DesignParameter['nguardring']['_XYCoordinates'][0][1] + self._DesignParameter['nguardring']['_DesignObj']._DesignParameter['nw_bot']['_XYCoordinates'][0][1])))
		self._DesignParameter['nwell']['_XYCoordinates'] = [[(((self._DesignParameter['nguardring']['_XYCoordinates'][0][0] + self._DesignParameter['nguardring']['_DesignObj']._DesignParameter['nw_left']['_XYCoordinates'][0][0]) + (self._DesignParameter['nguardring']['_XYCoordinates'][0][0] + self._DesignParameter['nguardring']['_DesignObj']._DesignParameter['nw_right']['_XYCoordinates'][0][0])) / 2), (((self._DesignParameter['nguardring']['_XYCoordinates'][0][1] + self._DesignParameter['nguardring']['_DesignObj']._DesignParameter['nw_bot']['_XYCoordinates'][0][1]) + (self._DesignParameter['nguardring']['_XYCoordinates'][0][1] + self._DesignParameter['nguardring']['_DesignObj']._DesignParameter['nw_top']['_XYCoordinates'][0][1])) / 2)]]
		self._DesignParameter['via_m1_m2_gate4'] = self._SrefElementDeclaration(_DesignObj=ViaStack._ViaStack(_Name='via_m1_m2_gate4In{}'.format(_Name)))[0]
		self._DesignParameter['via_m1_m2_gate4']['_DesignObj']._CalculateStackMinimumEnclosureY(**dict(COX=max(2, max(1, (1 + int((((self._DesignParameter['pmos4_gate']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] - drc._VIAxMinSpace) - (2 * drc._VIAxMinEnclosureByMetx)) / (drc._VIAxMinWidth + drc._VIAxMinSpace)))))), COY=1, start_layer=1, end_layer=2))
		self._DesignParameter['via_m1_m2_gate4']['_XYCoordinates'] = [[self._DesignParameter['pmos4_gate']['_XYCoordinates'][0][0], self._DesignParameter['pmos4_gate']['_XYCoordinates'][0][1]+self._DesignParameter['pmos4_gate']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']/2-self._DesignParameter['via_m1_m2_gate4']['_DesignObj']._DesignParameter['ViaMet12Met2']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']/2], [self._DesignParameter['pmos4_gate']['_XYCoordinates'][1][0], self._DesignParameter['pmos4_gate']['_XYCoordinates'][1][1]+self._DesignParameter['pmos4_gate']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']/2-self._DesignParameter['via_m1_m2_gate4']['_DesignObj']._DesignParameter['ViaMet12Met2']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']/2]]
		self._DesignParameter['via_m1_m2_gate3'] = self._SrefElementDeclaration(_DesignObj=ViaStack._ViaStack(_Name='via_m1_m2_gate3In{}'.format(_Name)))[0]
		self._DesignParameter['via_m1_m2_gate3']['_DesignObj']._CalculateStackMinimumEnclosureY(**dict(COX=max(2, max(1, (1 + int((((self._DesignParameter['pmos3_gate']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] - drc._VIAxMinSpace) - (2 * drc._VIAxMinEnclosureByMetx)) / (drc._VIAxMinWidth + drc._VIAxMinSpace)))))), COY=1, start_layer=1, end_layer=2))
		self._DesignParameter['via_m1_m2_gate3']['_XYCoordinates'] = [[self._DesignParameter['pmos3_gate']['_XYCoordinates'][0][0], self._DesignParameter['pmos3_gate']['_XYCoordinates'][0][1]+self._DesignParameter['pmos3_gate']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']/2-self._DesignParameter['via_m1_m2_gate3']['_DesignObj']._DesignParameter['ViaMet12Met2']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']/2], [self._DesignParameter['pmos3_gate']['_XYCoordinates'][1][0], self._DesignParameter['pmos3_gate']['_XYCoordinates'][0][1]+self._DesignParameter['pmos3_gate']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']/2-self._DesignParameter['via_m1_m2_gate3']['_DesignObj']._DesignParameter['ViaMet12Met2']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']/2]]
		self._DesignParameter['via_m1_m2_gate1'] = self._SrefElementDeclaration(_DesignObj=ViaStack._ViaStack(_Name='via_m1_m2_gate1In{}'.format(_Name)))[0]
		self._DesignParameter['via_m1_m2_gate1']['_DesignObj']._CalculateStackMinimumEnclosureY(**dict(COX=max(2, max(1, (1 + int((((self._DesignParameter['pmos1_gate']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] - drc._VIAxMinSpace) - (2 * drc._VIAxMinEnclosureByMetx)) / (drc._VIAxMinWidth + drc._VIAxMinSpace)))))), COY=1, start_layer=1, end_layer=2))
		self._DesignParameter['via_m1_m2_gate1']['_XYCoordinates'] = [[self._DesignParameter['pmos1_gate']['_XYCoordinates'][0][0], self._DesignParameter['pmos1_gate']['_XYCoordinates'][0][1]]]
		self._DesignParameter['m2_clk_routing_x'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _Width=self._DesignParameter['via_m1_m2_gate1']['_DesignObj']._DesignParameter['ViaMet12Met2']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'])
		self._DesignParameter['m2_clk_routing_x']['_XYCoordinates'] = [[[self._DesignParameter['via_m1_m2_gate4']['_XYCoordinates'][0][0], self._DesignParameter['via_m1_m2_gate4']['_XYCoordinates'][0][1]], [(((self._DesignParameter['PMOS4']['_XYCoordinates'][0][0] + self._DesignParameter['PMOS4']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][(- 1)][0]) + (self._DesignParameter['PMOS3']['_XYCoordinates'][0][0] + self._DesignParameter['PMOS3']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][0])) / 2), self._DesignParameter['via_m1_m2_gate4']['_XYCoordinates'][0][1]], [(((self._DesignParameter['PMOS4']['_XYCoordinates'][0][0] + self._DesignParameter['PMOS4']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][(- 1)][0]) + (self._DesignParameter['PMOS3']['_XYCoordinates'][0][0] + self._DesignParameter['PMOS3']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][0])) / 2), self._DesignParameter['via_m1_m2_gate3']['_XYCoordinates'][0][1]], [self._DesignParameter['via_m1_m2_gate3']['_XYCoordinates'][0][0], self._DesignParameter['via_m1_m2_gate3']['_XYCoordinates'][0][1]]], [[self._DesignParameter['via_m1_m2_gate4']['_XYCoordinates'][1][0], self._DesignParameter['via_m1_m2_gate4']['_XYCoordinates'][1][1]], [(((self._DesignParameter['PMOS4']['_XYCoordinates'][1][0] + self._DesignParameter['PMOS4']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][0]) + (self._DesignParameter['PMOS3']['_XYCoordinates'][1][0] + self._DesignParameter['PMOS3']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][(- 1)][0])) / 2), self._DesignParameter['via_m1_m2_gate4']['_XYCoordinates'][1][1]], [(((self._DesignParameter['PMOS4']['_XYCoordinates'][1][0] + self._DesignParameter['PMOS4']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][0]) + (self._DesignParameter['PMOS3']['_XYCoordinates'][1][0] + self._DesignParameter['PMOS3']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][(- 1)][0])) / 2), self._DesignParameter['via_m1_m2_gate3']['_XYCoordinates'][1][1]], [self._DesignParameter['via_m1_m2_gate3']['_XYCoordinates'][1][0], self._DesignParameter['via_m1_m2_gate3']['_XYCoordinates'][1][1]]], [[self._DesignParameter['via_m1_m2_gate3']['_XYCoordinates'][0][0], self._DesignParameter['via_m1_m2_gate3']['_XYCoordinates'][0][1]], [(((self._DesignParameter['PMOS3']['_XYCoordinates'][0][0] + self._DesignParameter['PMOS3']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][(- 1)][0]) + (self._DesignParameter['PMOS2']['_XYCoordinates'][0][0] + self._DesignParameter['PMOS2']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][0])) / 2), self._DesignParameter['via_m1_m2_gate3']['_XYCoordinates'][0][1]], [(((self._DesignParameter['PMOS3']['_XYCoordinates'][0][0] + self._DesignParameter['PMOS3']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][(- 1)][0]) + (self._DesignParameter['PMOS2']['_XYCoordinates'][0][0] + self._DesignParameter['PMOS2']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][0])) / 2), max((((((self._DesignParameter['via_m1_m3_pmos2']['_XYCoordinates'][0][1] + self._DesignParameter['via_m1_m3_pmos2']['_DesignObj']._DesignParameter['ViaMet22Met3']['_XYCoordinates'][0][1]) + self._DesignParameter['via_m1_m3_pmos2']['_DesignObj']._DesignParameter['ViaMet22Met3']['_DesignObj']._DesignParameter['_Met3Layer']['_XYCoordinates'][0][1]) + (self._DesignParameter['via_m1_m3_pmos2']['_DesignObj']._DesignParameter['ViaMet22Met3']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth'] / 2)) + (self._DesignParameter['m2_clk_routing_x']['_Width'] / 2)) + drc._MetalxMinSpace2), self._DesignParameter['via_m1_m2_gate1']['_XYCoordinates'][0][1])], [(((self._DesignParameter['PMOS2']['_XYCoordinates'][0][0] + self._DesignParameter['PMOS2']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][(- 1)][0]) + (self._DesignParameter['PMOS1']['_XYCoordinates'][0][0] + self._DesignParameter['PMOS1']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][0])) / 2), max((((((self._DesignParameter['via_m1_m3_pmos2']['_XYCoordinates'][0][1] + self._DesignParameter['via_m1_m3_pmos2']['_DesignObj']._DesignParameter['ViaMet22Met3']['_XYCoordinates'][0][1]) + self._DesignParameter['via_m1_m3_pmos2']['_DesignObj']._DesignParameter['ViaMet22Met3']['_DesignObj']._DesignParameter['_Met3Layer']['_XYCoordinates'][0][1]) + (self._DesignParameter['via_m1_m3_pmos2']['_DesignObj']._DesignParameter['ViaMet22Met3']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth'] / 2)) + (self._DesignParameter['m2_clk_routing_x']['_Width'] / 2)) + drc._MetalxMinSpace2), self._DesignParameter['via_m1_m2_gate1']['_XYCoordinates'][0][1])], [(((self._DesignParameter['PMOS2']['_XYCoordinates'][0][0] + self._DesignParameter['PMOS2']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][(- 1)][0]) + (self._DesignParameter['PMOS1']['_XYCoordinates'][0][0] + self._DesignParameter['PMOS1']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][0])) / 2), self._DesignParameter['via_m1_m2_gate1']['_XYCoordinates'][0][1]], [self._DesignParameter['via_m1_m2_gate1']['_XYCoordinates'][0][0], self._DesignParameter['via_m1_m2_gate1']['_XYCoordinates'][0][1]]], [[self._DesignParameter['via_m1_m2_gate3']['_XYCoordinates'][1][0], self._DesignParameter['via_m1_m2_gate3']['_XYCoordinates'][1][1]], [(((self._DesignParameter['PMOS2']['_XYCoordinates'][1][0] + self._DesignParameter['PMOS2']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][(- 1)][0]) + (self._DesignParameter['PMOS3']['_XYCoordinates'][1][0] + self._DesignParameter['PMOS3']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][0])) / 2), self._DesignParameter['via_m1_m2_gate3']['_XYCoordinates'][1][1]], [(((self._DesignParameter['PMOS2']['_XYCoordinates'][1][0] + self._DesignParameter['PMOS2']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][(- 1)][0]) + (self._DesignParameter['PMOS3']['_XYCoordinates'][1][0] + self._DesignParameter['PMOS3']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][0])) / 2), max((((((self._DesignParameter['via_m1_m3_pmos2_1']['_XYCoordinates'][0][1] + self._DesignParameter['via_m1_m3_pmos2_1']['_DesignObj']._DesignParameter['ViaMet22Met3']['_XYCoordinates'][0][1]) + self._DesignParameter['via_m1_m3_pmos2_1']['_DesignObj']._DesignParameter['ViaMet22Met3']['_DesignObj']._DesignParameter['_Met3Layer']['_XYCoordinates'][0][1]) + (self._DesignParameter['via_m1_m3_pmos2_1']['_DesignObj']._DesignParameter['ViaMet22Met3']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth'] / 2)) + (self._DesignParameter['m2_clk_routing_x']['_Width'] / 2)) + drc._MetalxMinSpace2), self._DesignParameter['via_m1_m2_gate1']['_XYCoordinates'][0][1])], [(((self._DesignParameter['PMOS2']['_XYCoordinates'][1][0] + self._DesignParameter['PMOS2']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][0]) + (self._DesignParameter['PMOS1']['_XYCoordinates'][0][0] + self._DesignParameter['PMOS1']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][(- 1)][0])) / 2), max((((((self._DesignParameter['via_m1_m3_pmos2_1']['_XYCoordinates'][0][1] + self._DesignParameter['via_m1_m3_pmos2_1']['_DesignObj']._DesignParameter['ViaMet22Met3']['_XYCoordinates'][0][1]) + self._DesignParameter['via_m1_m3_pmos2_1']['_DesignObj']._DesignParameter['ViaMet22Met3']['_DesignObj']._DesignParameter['_Met3Layer']['_XYCoordinates'][0][1]) + (self._DesignParameter['via_m1_m3_pmos2_1']['_DesignObj']._DesignParameter['ViaMet22Met3']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth'] / 2)) + (self._DesignParameter['m2_clk_routing_x']['_Width'] / 2)) + drc._MetalxMinSpace2), self._DesignParameter['via_m1_m2_gate1']['_XYCoordinates'][0][1])], [(((self._DesignParameter['PMOS2']['_XYCoordinates'][1][0] + self._DesignParameter['PMOS2']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][0]) + (self._DesignParameter['PMOS1']['_XYCoordinates'][0][0] + self._DesignParameter['PMOS1']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][(- 1)][0])) / 2), self._DesignParameter['via_m1_m2_gate1']['_XYCoordinates'][0][1]], [self._DesignParameter['via_m1_m2_gate1']['_XYCoordinates'][0][0], self._DesignParameter['via_m1_m2_gate1']['_XYCoordinates'][0][1]]]]
