from generatorLib import StickDiagram
from generatorLib import DesignParameters
import copy
import math
from generatorLib import DRC
from generatorLib.generator_models import PSubRing
from generatorLib.generator_models import NMOSWithDummy
from generatorLib.generator_models import ViaPoly2Met1
from generatorLib.generator_models import ViaStack

class EasyDebugModule(StickDiagram._StickDiagram):
	def __init__(self, _DesignParameter=None, _Name='EasyDebugModule'):
		if _DesignParameter != None:
			self._DesignParameter = _DesignParameter
		else:
			self._DesignParameter = dict(_Name=self._NameDeclaration(_Name=_Name), _GDSFile=self._GDSObjDeclaration(_GDSFile=None))
		self._DesignParameter['_Name']['Name'] = _Name

	def _CalculateDesignParameter(self,nmos_gate=1,nmos_width=2000,nmos_length=500,nmos_dummy=False,xvt='RVT',pccrit=False,guardring_left=2,guardring_right=2,guardring_top=2,guardring_bot=2,guardring_width=None,guardring_height=None):
	
		drc = DRC.DRC()
		_Name = self._DesignParameter['_Name']['_Name']
		
		self._DesignParameter['nmos'] = self._SrefElementDeclaration(_DesignObj=NMOSWithDummy._NMOS(_Name='nmosIn{}'.format(_Name)))[0]
		self._DesignParameter['nmos']['_DesignObj']._CalculateNMOSDesignParameter(**dict(_NMOSNumberofGate=nmos_gate, _NMOSChannelWidth=nmos_width, _NMOSChannellength=nmos_length, _NMOSDummy=nmos_dummy, _GateSpacing=None, _SDWidth=None, _XVT=xvt, _PCCrit=pccrit))
		self._DesignParameter['nmos']['_XYCoordinates'] = [[0, 0]]
		cont_num = max(1, max(1, (1 + int(((((((self._DesignParameter['nmos']['_XYCoordinates'][0][0] + self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]) - (self._DesignParameter['nmos']['_XYCoordinates'][0][0] + self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0])) + self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']) - drc._CoMinSpace) - (2 * drc._CoMinEnclosureByPO)) / (drc._CoMinWidth + drc._CoMinSpace))))))
		via_num = max(1, max(1, (1 + int((((self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_YWidth'] - drc._VIAxMinSpace) - (2 * drc._VIAxMinEnclosureByMetx)) / (drc._VIAxMinWidth + drc._VIAxMinSpace))))))
		self._DesignParameter['via_m1_m3'] = self._SrefElementDeclaration(_DesignObj=ViaStack._ViaStack(_Name='via_m1_m3In{}'.format(_Name)))[0]
		self._DesignParameter['via_m1_m3']['_DesignObj']._CalculateStackMinimumEnclosureX(**dict(COX=1, COY=via_num, start_layer=1, end_layer=3))
		self._DesignParameter['via_m1_m3']['_XYCoordinates'] = None
		XYList = []
		xy_offset = [0, 0]
		for i in range(len(self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		    if ((i % 2) == 1):
		        xy = (self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i][0] if (type(self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i][0]) == list) else self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])
		        XYList.append([((x + y) + z) for (x, y, z) in zip([(0 + self._DesignParameter['nmos']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['nmos']['_XYCoordinates'][0][1])], xy, xy_offset)])
		self._DesignParameter['via_m1_m3']['_XYCoordinates'] = XYList
		self._DesignParameter['via_gate'] = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_Name='via_gateIn{}'.format(_Name)))[0]
		self._DesignParameter['via_gate']['_DesignObj']._CalculateViaPoly2Met1DesignParameterMinimumEnclosureY(**dict(_ViaPoly2Met1NumberOfCOX=cont_num, _ViaPoly2Met1NumberOfCOY=1))
		self._DesignParameter['via_gate']['_XYCoordinates'] = [[self._DesignParameter['nmos']['_XYCoordinates'][0][0], ((max(((self._DesignParameter['nmos']['_XYCoordinates'][0][1] + self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1]) + (self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_YWidth'] / 2)), (((self._DesignParameter['via_m1_m3']['_XYCoordinates'][0][1] + self._DesignParameter['via_m1_m3']['_DesignObj']._DesignParameter['ViaMet12Met2']['_XYCoordinates'][0][1]) + self._DesignParameter['via_m1_m3']['_DesignObj']._DesignParameter['ViaMet12Met2']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) + (self._DesignParameter['via_m1_m3']['_DesignObj']._DesignParameter['ViaMet12Met2']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2))) + (self._DesignParameter['via_gate']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)) + drc._Metal1MinSpace2)]]
		path_list = []
		xy_offset = [0, 0]
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
		    target_y_value = [[(+ self._DesignParameter['via_gate']['_XYCoordinates'][0][0]), (+ self._DesignParameter['via_gate']['_XYCoordinates'][0][1])]][0][1]
		    for i in range(len(self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
		        xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['nmos']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['nmos']['_XYCoordinates'][0][1])], self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		elif (mode == 'horizontal'):
		    xy_with_offset = []
		    target_x_value = [[(+ self._DesignParameter['via_gate']['_XYCoordinates'][0][0]), (+ self._DesignParameter['via_gate']['_XYCoordinates'][0][1])]][0][0]
		    for i in range(len(self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
		        xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['nmos']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['nmos']['_XYCoordinates'][0][1])], self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		for i in range(len(path_list)):
		    path_list[i][0] = [(xy + offset) for (xy, offset) in zip(path_list[i][0], xy_offset)]
		self._DesignParameter['poly_gate_y'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _Width=_width)
		self._DesignParameter['poly_gate_y']['_XYCoordinates'] = path_list
		self._DesignParameter['poly_gate_x'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _Width=self._DesignParameter['via_gate']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'])
		self._DesignParameter['poly_gate_x']['_XYCoordinates'] = [[[((self._DesignParameter['nmos']['_XYCoordinates'][0][0] + self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)), self._DesignParameter['via_gate']['_XYCoordinates'][0][1]], [((self._DesignParameter['nmos']['_XYCoordinates'][0][0] + self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]) + (self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)), self._DesignParameter['via_gate']['_XYCoordinates'][0][1]]]]
		self._DesignParameter['guardring'] = self._SrefElementDeclaration(_DesignObj=PSubRing.PSubRing(_Name='guardringIn{}'.format(_Name)))[0]
		self._DesignParameter['guardring']['_DesignObj']._CalculateDesignParameter(**dict(height=5000, width=3000, contact_bottom=guardring_bot, contact_top=guardring_top, contact_left=guardring_left, contact_right=guardring_right))
		self._DesignParameter['guardring']['_XYCoordinates'] = [[2478.0, (- 137.0)]]
		if (guardring_width == None):
		    guardring_xwidth = (((((self._DesignParameter['nmos']['_XYCoordinates'][0][0] + self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][0]) + (self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth'] / 2)) + (self._DesignParameter['guardring']['_DesignObj']._DesignParameter['right']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] / 2)) + drc._Metal1MinSpace3) - ((((self._DesignParameter['nmos']['_XYCoordinates'][0][0] + self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][0]) - (self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth'] / 2)) - (self._DesignParameter['guardring']['_DesignObj']._DesignParameter['left']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] / 2)) - drc._Metal1MinSpace3))
		if (guardring_width != None):
		    guardring_xwidth = guardring_width
		if (guardring_height == None):
		    guardring_yheight = (((((self._DesignParameter['via_gate']['_XYCoordinates'][0][1] + self._DesignParameter['via_gate']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) + (self._DesignParameter['via_gate']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)) + (self._DesignParameter['guardring']['_DesignObj']._DesignParameter['top']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)) + drc._Metal1MinSpace3) - ((((self._DesignParameter['nmos']['_XYCoordinates'][0][1] + self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1]) - (self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_YWidth'] / 2)) - (self._DesignParameter['guardring']['_DesignObj']._DesignParameter['bot']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)) - drc._Metal1MinSpace3))
		if (guardring_height != None):
		    guardring_yheight = guardring_height
		self._DesignParameter['guardring']['_DesignObj']._CalculateDesignParameter(**dict(height=guardring_yheight, width=guardring_xwidth, contact_bottom=guardring_bot, contact_top=guardring_top, contact_left=guardring_left, contact_right=guardring_right))
		self._DesignParameter['guardring']['_XYCoordinates'] = [[self._DesignParameter['nmos']['_XYCoordinates'][0][0], ((((self._DesignParameter['via_gate']['_XYCoordinates'][0][1] + self._DesignParameter['via_gate']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) + (self._DesignParameter['via_gate']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)) + ((self._DesignParameter['nmos']['_XYCoordinates'][0][1] + self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1]) - (self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_YWidth'] / 2))) / 2)]]
		self._DesignParameter['m1_source_y'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=drc._Metal1MinWidth*3)
		path_list = []
		xy_offset = (0, (self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_YWidth'] / 2))
		if (len(self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates']) == 1):
		    mode = 'vertical'
		elif (self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][0] == self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][0]):
		    mode = 'horizontal'
		elif (self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1] == self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][1]):
		    mode = 'vertical'
		else:
		    print('Invalid Target Input')
		if (mode == 'vertical'):
		    xy_with_offset = []
		    target_y_value = [[(+ (self._DesignParameter['guardring']['_XYCoordinates'][0][0] + self._DesignParameter['guardring']['_DesignObj']._DesignParameter['bot']['_XYCoordinates'][0][0])), (+ (self._DesignParameter['guardring']['_XYCoordinates'][0][1] + self._DesignParameter['guardring']['_DesignObj']._DesignParameter['bot']['_XYCoordinates'][0][1]))]][0][1]
		    for i in range(len(self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		        if ((i % 2) == 0):
		            xy_with_offset.append([(x + y) for (x, y) in zip([(self._DesignParameter['m1_source_y']['_Width'] / 2 - (self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth'] / 2) + self._DesignParameter['nmos']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['nmos']['_XYCoordinates'][0][1])], self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		elif (mode == 'horizontal'):
		    xy_with_offset = []
		    target_x_value = [[(+ (self._DesignParameter['guardring']['_XYCoordinates'][0][0] + self._DesignParameter['guardring']['_DesignObj']._DesignParameter['bot']['_XYCoordinates'][0][0])), (+ (self._DesignParameter['guardring']['_XYCoordinates'][0][1] + self._DesignParameter['guardring']['_DesignObj']._DesignParameter['bot']['_XYCoordinates'][0][1]))]][0][0]
		    for i in range(len(self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		        if ((i % 2) == 0):
		            xy_with_offset.append([(x + y) for (x, y) in zip([(self._DesignParameter['m1_source_y']['_Width'] / 2 - (self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth'] / 2) + self._DesignParameter['nmos']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['nmos']['_XYCoordinates'][0][1])], self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		for i in range(len(path_list)):
		    path_list[i][0] = [(xy + offset) for (xy, offset) in zip(path_list[i][0], xy_offset)]
		self._DesignParameter['m1_source_y']['_XYCoordinates'] = path_list
		self._DesignParameter['m2_drain_x'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _Width=50)
		self._DesignParameter['m2_drain_x']['_XYCoordinates'] = [[[(+ self._DesignParameter['via_m1_m3']['_XYCoordinates'][0][0]), (+ self._DesignParameter['via_m1_m3']['_XYCoordinates'][0][1])], [(+ self._DesignParameter['via_m1_m3']['_XYCoordinates'][(- 1)][0]), (+ self._DesignParameter['via_m1_m3']['_XYCoordinates'][(- 1)][1])]]]



		if (self._DesignParameter['nmos']['_XYCoordinates'][0][0]+self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][1][0]-self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']/2)-(self._DesignParameter['m1_source_y']['_XYCoordinates'][0][0][0]+self._DesignParameter['m1_source_y']['_Width']/2) < drc._Metal1MinSpace12:
			raise NotImplementedError