from generatorLib import StickDiagram
from generatorLib import DesignParameters
import copy
import math
from generatorLib import DRC
from generatorLib.generator_models import PMOSWithDummy
from generatorLib.generator_models import NSubRing
from generatorLib.generator_models import ViaStack
from generatorLib.generator_models import ViaPoly2Met1
from generatorLib.generator_models import ViaMet12Met2

class EasyDebugModule(StickDiagram._StickDiagram):
	def __init__(self, _DesignParameter=None, _Name='EasyDebugModule'):
		if _DesignParameter != None:
			self._DesignParameter = _DesignParameter
		else:
			self._DesignParameter = dict(_Name=self._NameDeclaration(_Name=_Name), _GDSFile=self._GDSObjDeclaration(_GDSFile=None))
		self._DesignParameter['_Name']['Name'] = _Name

	def _CalculateDesignParameter(self,finger=2,width=1500,length=100,dummy=True,xvt='LVT',pccrit=False,guardring_co_right=3,guardring_co_left=3,guardring_co_top=4,guardring_co_bottom=2):
	
		drc = DRC.DRC()
		_Name = self._DesignParameter['_Name']['_Name']
		
		self._DesignParameter['pmos'] = self._SrefElementDeclaration(_DesignObj=PMOSWithDummy._PMOS(_Name='pmosIn{}'.format(_Name)))[0]
		self._DesignParameter['pmos']['_DesignObj']._CalculatePMOSDesignParameter(**dict(_PMOSNumberofGate=finger, _PMOSChannelWidth=width, _PMOSChannellength=length, _PMOSDummy=dummy, _GateSpacing=None, _SDWidth=None, _XVT=xvt, _PCCrit=pccrit))
		self._DesignParameter['pmos']['_XYCoordinates'] = [[213.0, (- 184.0)]]
		via_num = max(2, max(1, (1 + int((((self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] - drc._VIAxMinSpace) - (2 * drc._VIAxMinEnclosureByMetx)) / (drc._VIAxMinWidth + drc._VIAxMinSpace))))))
		self._DesignParameter['via_m1_m2_drain'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='via_m1_m2_drainIn{}'.format(_Name)))[0]
		self._DesignParameter['via_m1_m2_drain']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(**dict(_ViaMet12Met2NumberOfCOX=1, _ViaMet12Met2NumberOfCOY=via_num))
		self._DesignParameter['via_m1_m2_drain']['_XYCoordinates'] = None
		XYList = []
		xy_offset = [0, 0]
		for i in range(len(self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'])):
		    if ((i % 2) == 1):
		        xy = (self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i][0] if (type(self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i][0]) == list) else self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i])
		        XYList.append([((x + y) + z) for (x, y, z) in zip([(0 + self._DesignParameter['pmos']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['pmos']['_XYCoordinates'][0][1])], xy, xy_offset)])
		self._DesignParameter['via_m1_m2_drain']['_XYCoordinates'] = XYList
		self._DesignParameter['via_gate'] = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_Name='via_gateIn{}'.format(_Name)))[0]
		self._DesignParameter['via_gate']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(**dict(_ViaPoly2Met1NumberOfCOX=max(1, (1 + int(((((((self._DesignParameter['pmos']['_XYCoordinates'][0][0] + self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]) - (self._DesignParameter['pmos']['_XYCoordinates'][0][0] + self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0])) + self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']) - drc._CoMinSpace) - (2 * drc._CoMinEnclosureByPO)) / (drc._CoMinWidth + drc._CoMinSpace))))), _ViaPoly2Met1NumberOfCOY=1))
		self._DesignParameter['via_gate']['_XYCoordinates'] = [[self._DesignParameter['pmos']['_XYCoordinates'][0][0], ((min(((self._DesignParameter['pmos']['_XYCoordinates'][0][1] + self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) - (self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)), ((self._DesignParameter['via_m1_m2_drain']['_XYCoordinates'][0][1] + self._DesignParameter['via_m1_m2_drain']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) - (self._DesignParameter['via_m1_m2_drain']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2))) - (self._DesignParameter['via_gate']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)) - drc._Metal1MinSpace2)]]
		self._DesignParameter['poly_gate'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _Width=self._DesignParameter['via_gate']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'])
		self._DesignParameter['poly_gate']['_XYCoordinates'] = [[[((self._DesignParameter['pmos']['_XYCoordinates'][0][0] + self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)), self._DesignParameter['via_gate']['_XYCoordinates'][0][1]], [((self._DesignParameter['pmos']['_XYCoordinates'][0][0] + self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]) + (self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)), self._DesignParameter['via_gate']['_XYCoordinates'][0][1]]]]
		self._DesignParameter['pguardring'] = self._SrefElementDeclaration(_DesignObj=NSubRing.NSubRing(_Name='pguardringIn{}'.format(_Name)))[0]
		self._DesignParameter['pguardring']['_DesignObj']._CalculateDesignParameter(**dict(height=5000, width=8000, contact_bottom=guardring_co_bottom, contact_top=guardring_co_top, contact_left=guardring_co_left, contact_right=guardring_co_right))
		self._DesignParameter['pguardring']['_XYCoordinates'] = [[817.5, (- 208.0)]]
		path_list = []
		xy_offset = (0, ((- self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']) / 2))
		if (len(self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates']) == 1):
		    mode = 'vertical'
		    _width = (drc._Metal1MinWidth * 3)
		elif (self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0] == self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][(- 1)][0]):
		    mode = 'horizontal'
		    _width = (drc._Metal1MinWidth * 3)
		elif (self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1] == self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][(- 1)][1]):
		    mode = 'vertical'
		    _width = (drc._Metal1MinWidth * 3)
		else:
		    print('Invalid Target Input')
		if (mode == 'vertical'):
		    xy_with_offset = []
		    target_y_value = [[(+ (self._DesignParameter['pmos']['_XYCoordinates'][0][0] + self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0])), (+ (self._DesignParameter['pmos']['_XYCoordinates'][0][1] + self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]))]][0][1]
		    for i in range(len(self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'])):
		        if ((i % 2) == 0):
		            xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['pmos']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['pmos']['_XYCoordinates'][0][1])], self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		elif (mode == 'horizontal'):
		    xy_with_offset = []
		    target_x_value = [[(+ (self._DesignParameter['pmos']['_XYCoordinates'][0][0] + self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0])), (+ (self._DesignParameter['pmos']['_XYCoordinates'][0][1] + self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]))]][0][0]
		    for i in range(len(self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'])):
		        if ((i % 2) == 0):
		            xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['pmos']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['pmos']['_XYCoordinates'][0][1])], self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		for i in range(len(path_list)):
		    path_list[i][0] = [(xy + offset) for (xy, offset) in zip(path_list[i][0], xy_offset)]
		self._DesignParameter['m1_source_routing'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=_width)
		self._DesignParameter['m1_source_routing']['_XYCoordinates'] = path_list
		guardring_right = max(((max((self._DesignParameter['m1_source_routing']['_XYCoordinates'][(- 1)][0][0] + (self._DesignParameter['m1_source_routing']['_Width'] / 2)), ((self._DesignParameter['pmos']['_XYCoordinates'][0][0] + self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][(- 1)][0]) + (self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] / 2))) + (self._DesignParameter['pguardring']['_DesignObj']._DesignParameter['right']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] / 2)) + drc._Metal1MinSpace3), ((((self._DesignParameter['pmos']['_XYCoordinates'][0][0] + self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][(- 1)][0]) + (self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_PODummyLayer']['_XWidth'] / 2)) - (((self._DesignParameter['pguardring']['_XYCoordinates'][0][0] + self._DesignParameter['pguardring']['_DesignObj']._DesignParameter['right']['_XYCoordinates'][0][0]) + self._DesignParameter['pguardring']['_DesignObj']._DesignParameter['right']['_DesignObj']._DesignParameter['_COLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['pguardring']['_DesignObj']._DesignParameter['right']['_DesignObj']._DesignParameter['_COLayer']['_XWidth'] / 2))) + drc._PolygateMinSpace2Co), ((((self._DesignParameter['pmos']['_XYCoordinates'][0][0] + self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][(- 1)][0]) + (self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_PODummyLayer']['_XWidth'] / 2)) + (self._DesignParameter['pguardring']['_DesignObj']._DesignParameter['right']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth'] / 2)) + drc._PolygateMinSpace2OD))
		guardring_left = min(((min((self._DesignParameter['m1_source_routing']['_XYCoordinates'][0][0][0] - (self._DesignParameter['m1_source_routing']['_Width'] / 2)), ((self._DesignParameter['pmos']['_XYCoordinates'][0][0] + self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0]) - (self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] / 2))) - (self._DesignParameter['pguardring']['_DesignObj']._DesignParameter['left']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] / 2)) - drc._Metal1MinSpace3), ((((self._DesignParameter['pmos']['_XYCoordinates'][0][0] + self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_PODummyLayer']['_XWidth'] / 2)) - (((self._DesignParameter['pguardring']['_XYCoordinates'][0][0] + self._DesignParameter['pguardring']['_DesignObj']._DesignParameter['left']['_XYCoordinates'][0][0]) + self._DesignParameter['pguardring']['_DesignObj']._DesignParameter['left']['_DesignObj']._DesignParameter['_COLayer']['_XYCoordinates'][(- 1)][0]) - (self._DesignParameter['pguardring']['_DesignObj']._DesignParameter['left']['_DesignObj']._DesignParameter['_COLayer']['_XWidth'] / 2))) - drc._PolygateMinSpace2Co), ((((self._DesignParameter['pmos']['_XYCoordinates'][0][0] + self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_PODummyLayer']['_XWidth'] / 2)) - (self._DesignParameter['pguardring']['_DesignObj']._DesignParameter['left']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth'] / 2)) - drc._PolygateMinSpace2OD))
		guardring_top = ((((self._DesignParameter['pmos']['_XYCoordinates'][0][1] + self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) + (self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)) + (self._DesignParameter['pguardring']['_DesignObj']._DesignParameter['top']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)) + drc._Metal1MinSpace3)
		guardring_bottom = ((((self._DesignParameter['via_gate']['_XYCoordinates'][0][1] + self._DesignParameter['via_gate']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) - (self._DesignParameter['via_gate']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)) - (self._DesignParameter['pguardring']['_DesignObj']._DesignParameter['bot']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)) - drc._Metal1MinSpace3)
		self._DesignParameter['pguardring']['_DesignObj']._CalculateDesignParameter(**dict(height=(guardring_top - guardring_bottom), width=(guardring_right - guardring_left), contact_bottom=guardring_co_bottom, contact_top=guardring_co_top, contact_left=guardring_co_left, contact_right=guardring_co_right))
		self._DesignParameter['pguardring']['_XYCoordinates'] = [[((guardring_right + guardring_left) / 2), ((guardring_top + guardring_bottom) / 2)]]
		self._DesignParameter['nwell'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['NWELL'][0], _Datatype=DesignParameters._LayerMapping['NWELL'][1], _XWidth=(guardring_right - guardring_left), _YWidth=(guardring_top - guardring_bottom))
		self._DesignParameter['nwell']['_XYCoordinates'] = [[((guardring_right + guardring_left) / 2), ((guardring_top + guardring_bottom) / 2)]]
		self._DesignParameter['via_m1_m4'] = self._SrefElementDeclaration(_DesignObj=ViaStack._ViaStack(_Name='via_m1_m4In{}'.format(_Name)))[0]
		self._DesignParameter['via_m1_m4']['_DesignObj']._CalculateStackMinimumEnclosureY(**dict(COX=max(2, max(1, (1 + int((((self._DesignParameter['via_gate']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] - drc._VIAxMinSpace) - (2 * drc._VIAxMinEnclosureByMetx)) / (drc._VIAxMinWidth + drc._VIAxMinSpace)))))), COY=1, start_layer=1, end_layer=4))
		self._DesignParameter['via_m1_m4']['_XYCoordinates'] = [[(+ self._DesignParameter['via_gate']['_XYCoordinates'][0][0]), (+ self._DesignParameter['via_gate']['_XYCoordinates'][0][1])]]
		self._DesignParameter['m1_gate'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _XWidth=max(self._DesignParameter['via_m1_m4']['_DesignObj']._DesignParameter['ViaMet12Met2']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'], self._DesignParameter['via_gate']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']), _YWidth=max(self._DesignParameter['via_m1_m4']['_DesignObj']._DesignParameter['ViaMet12Met2']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'], self._DesignParameter['via_gate']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']))
		self._DesignParameter['m1_gate']['_XYCoordinates'] = [[(+ self._DesignParameter['via_m1_m4']['_XYCoordinates'][0][0]), (+ self._DesignParameter['via_m1_m4']['_XYCoordinates'][0][1])]]
		path_list = []
		xy_offset = [0, 0]
		if (len(self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates']) == 1):
		    mode = 'vertical'
		    _width = (drc._Metal1MinWidth * 3)
		elif (self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0] == self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][(- 1)][0]):
		    mode = 'horizontal'
		    _width = (drc._Metal1MinWidth * 3)
		elif (self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1] == self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][(- 1)][1]):
		    mode = 'vertical'
		    _width = (drc._Metal1MinWidth * 3)
		else:
		    print('Invalid Target Input')
		if (mode == 'vertical'):
		    xy_with_offset = []
		    target_y_value = [[(+ (self._DesignParameter['pguardring']['_XYCoordinates'][0][0] + self._DesignParameter['pguardring']['_DesignObj']._DesignParameter['top']['_XYCoordinates'][0][0])), (+ (self._DesignParameter['pguardring']['_XYCoordinates'][0][1] + self._DesignParameter['pguardring']['_DesignObj']._DesignParameter['top']['_XYCoordinates'][0][1]))]][0][1]
		    for i in range(len(self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'])):
		        if ((i % 2) == 0):
		            xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['pmos']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['pmos']['_XYCoordinates'][0][1])], self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		elif (mode == 'horizontal'):
		    xy_with_offset = []
		    target_x_value = [[(+ (self._DesignParameter['pguardring']['_XYCoordinates'][0][0] + self._DesignParameter['pguardring']['_DesignObj']._DesignParameter['top']['_XYCoordinates'][0][0])), (+ (self._DesignParameter['pguardring']['_XYCoordinates'][0][1] + self._DesignParameter['pguardring']['_DesignObj']._DesignParameter['top']['_XYCoordinates'][0][1]))]][0][0]
		    for i in range(len(self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'])):
		        if ((i % 2) == 0):
		            xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['pmos']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['pmos']['_XYCoordinates'][0][1])], self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		for i in range(len(path_list)):
		    path_list[i][0] = [(xy + offset) for (xy, offset) in zip(path_list[i][0], xy_offset)]
		self._DesignParameter['m1_source_routing2'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=_width)
		self._DesignParameter['m1_source_routing2']['_XYCoordinates'] = path_list
		