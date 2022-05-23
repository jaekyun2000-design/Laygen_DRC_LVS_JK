from generatorLib import StickDiagram
from generatorLib import DesignParameters
import copy
import math
from generatorLib import DRC
from generatorLib.generator_models import ViaMet12Met2
from generatorLib.generator_models import PMOSWithDummy
from generatorLib.generator_models import ViaStack
from generatorLib.generator_models import NMOSWithDummy
from generatorLib.generator_models import ViaPoly2Met1

class dcdl_cap(StickDiagram._StickDiagram):
	def __init__(self, _DesignParameter=None, _Name='dcdl_cap'):
		if _DesignParameter != None:
			self._DesignParameter = _DesignParameter
		else:
			self._DesignParameter = dict(_Name=self._NameDeclaration(_Name=_Name), _GDSFile=self._GDSObjDeclaration(_GDSFile=None))
		self._DesignParameter['_Name']['Name'] = _Name

	def _CalculateDesignParameter(self,tg_pmos_gate=2,tg_nmos_gate=2,cap_gate=1,tg_gate_spacing=None,cap_gate_spacing=None,tg_nmos_width=200,tg_pmos_width=200,tg_length=30,tg_sdwidth=None,cap_sdwidth=None,tg_dummy=False,cap_dummy=False,tg_xvt='SLVT',cap_xvt='SLVT',tg_pmos_y=None,tg_nmos_y=None,cap_nmos_width=200,cap_pmos_width=200,cap_length=150,cap_pmos_gate_y=None,cap_nmos_gate_y=None):
	
		drc = DRC.DRC()
		_Name = self._DesignParameter['_Name']['_Name']

		if tg_gate_spacing==None:
			tg_gate_spacing=96

		_OriginXY = [[0,0]]

		self._DesignParameter['tg_nmos'] = self._SrefElementDeclaration(_DesignObj=NMOSWithDummy._NMOS(_Name='tg_nmosIn{}'.format(_Name)))[0]
		self._DesignParameter['tg_nmos']['_DesignObj']._CalculateNMOSDesignParameter(**dict(_NMOSNumberofGate=tg_nmos_gate, _NMOSChannelWidth=tg_nmos_width, _NMOSChannellength=tg_length, _NMOSDummy=tg_dummy, _GateSpacing=tg_gate_spacing, _SDWidth=tg_sdwidth, _XVT=tg_xvt,_PCCrit=False))
		if tg_nmos_y == None :
			self._DesignParameter['tg_nmos']['_XYCoordinates'] = [[0, _OriginXY[0][1]-self._DesignParameter['tg_nmos']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']/2-self._DesignParameter['tg_nmos']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']/2-drc._Metal1MinSpace2]]
		else :
			self._DesignParameter['tg_nmos']['_XYCoordinates'] = [[0, _OriginXY[0][1]-tg_nmos_y]]
		self._DesignParameter['tg_pmos'] = self._SrefElementDeclaration(_DesignObj=PMOSWithDummy._PMOS(_Name='tg_pmosIn{}'.format(_Name)))[0]
		self._DesignParameter['tg_pmos']['_DesignObj']._CalculatePMOSDesignParameter(**dict(_PMOSNumberofGate=tg_pmos_gate, _PMOSChannelWidth=tg_pmos_width, _PMOSChannellength=tg_length, _PMOSDummy=tg_dummy, _GateSpacing=tg_gate_spacing, _SDWidth=tg_sdwidth, _XVT=tg_xvt,_PCCrit=False))
		if tg_pmos_y == None :
			self._DesignParameter['tg_pmos']['_XYCoordinates'] = [[0, _OriginXY[0][1]+self._DesignParameter['tg_pmos']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']/2+self._DesignParameter['tg_pmos']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']/2+drc._Metal1MinSpace2]]
		else :
			self._DesignParameter['tg_pmos']['_XYCoordinates'] = [[self._DesignParameter['tg_nmos']['_XYCoordinates'][0][0], _OriginXY[0][1]+tg_pmos_y]]



		self._DesignParameter['cap_nmos'] = self._SrefElementDeclaration(_DesignObj=NMOSWithDummy._NMOS(_Name='cap_nmosIn{}'.format(_Name)))[0]
		self._DesignParameter['cap_nmos']['_DesignObj']._CalculateNMOSDesignParameter(**dict(_NMOSNumberofGate=cap_gate, _NMOSChannelWidth=cap_nmos_width, _NMOSChannellength=cap_length, _NMOSDummy=cap_dummy, _GateSpacing=cap_gate_spacing, _SDWidth=cap_sdwidth, _XVT=cap_xvt,_PCCrit=False))
		self._DesignParameter['cap_nmos']['_XYCoordinates'] = [[self._DesignParameter['tg_nmos']['_XYCoordinates'][0][0], (self._DesignParameter['tg_nmos']['_XYCoordinates'][0][1])]]
		self._DesignParameter['cap_pmos'] = self._SrefElementDeclaration(_DesignObj=PMOSWithDummy._PMOS(_Name='cap_pmosIn{}'.format(_Name)))[0]
		self._DesignParameter['cap_pmos']['_DesignObj']._CalculatePMOSDesignParameter(**dict(_PMOSNumberofGate=cap_gate, _PMOSChannelWidth=cap_pmos_width, _PMOSChannellength=cap_length, _PMOSDummy=cap_dummy, _GateSpacing=cap_gate_spacing, _SDWidth=cap_sdwidth, _XVT=cap_xvt,_PCCrit=False))
		self._DesignParameter['cap_pmos']['_XYCoordinates'] = [[self._DesignParameter['cap_nmos']['_XYCoordinates'][0][0], (self._DesignParameter['cap_nmos']['_XYCoordinates'][0][1])]]

		mosmetalspacing=tg_gate_spacing+self._DesignParameter['tg_pmos']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
		if tg_pmos_gate<tg_nmos_gate:
			if tg_pmos_gate%4==0:
				if tg_nmos_gate%4==1:
					self._DesignParameter['tg_pmos']['_XYCoordinates'] = [[self._DesignParameter['tg_pmos']['_XYCoordinates'][0][0]-mosmetalspacing/2, self._DesignParameter['tg_pmos']['_XYCoordinates'][0][1]]]
				elif tg_nmos_gate%4==2:
					self._DesignParameter['tg_pmos']['_XYCoordinates'] = [[self._DesignParameter['tg_pmos']['_XYCoordinates'][0][0]-mosmetalspacing, self._DesignParameter['tg_pmos']['_XYCoordinates'][0][1]]]
				elif tg_nmos_gate%4==3:
					self._DesignParameter['tg_pmos']['_XYCoordinates'] = [[self._DesignParameter['tg_pmos']['_XYCoordinates'][0][0]+mosmetalspacing/2, self._DesignParameter['tg_pmos']['_XYCoordinates'][0][1]]]
			elif tg_pmos_gate%4==1:
				if tg_nmos_gate%4==0:
					self._DesignParameter['tg_pmos']['_XYCoordinates'] = [[self._DesignParameter['tg_pmos']['_XYCoordinates'][0][0]+mosmetalspacing/2, self._DesignParameter['tg_pmos']['_XYCoordinates'][0][1]]]
				elif tg_nmos_gate%4==2:
					self._DesignParameter['tg_pmos']['_XYCoordinates'] = [[self._DesignParameter['tg_pmos']['_XYCoordinates'][0][0]-mosmetalspacing/2, self._DesignParameter['tg_pmos']['_XYCoordinates'][0][1]]]
				elif tg_nmos_gate%4==3:
					self._DesignParameter['tg_pmos']['_XYCoordinates'] = [[self._DesignParameter['tg_pmos']['_XYCoordinates'][0][0]+mosmetalspacing, self._DesignParameter['tg_pmos']['_XYCoordinates'][0][1]]]
			elif tg_pmos_gate%4==2:
				if tg_nmos_gate%4==0:
					self._DesignParameter['tg_pmos']['_XYCoordinates'] = [[self._DesignParameter['tg_pmos']['_XYCoordinates'][0][0]+mosmetalspacing, self._DesignParameter['tg_pmos']['_XYCoordinates'][0][1]]]
				elif tg_nmos_gate%4==1:
					self._DesignParameter['tg_pmos']['_XYCoordinates'] = [[self._DesignParameter['tg_pmos']['_XYCoordinates'][0][0]+mosmetalspacing/2, self._DesignParameter['tg_pmos']['_XYCoordinates'][0][1]]]
				elif tg_nmos_gate%4==3:
					self._DesignParameter['tg_pmos']['_XYCoordinates'] = [[self._DesignParameter['tg_pmos']['_XYCoordinates'][0][0]-mosmetalspacing/2, self._DesignParameter['tg_pmos']['_XYCoordinates'][0][1]]]
			elif tg_pmos_gate%4==3:
				if tg_nmos_gate%4==0:
					self._DesignParameter['tg_pmos']['_XYCoordinates'] = [[self._DesignParameter['tg_pmos']['_XYCoordinates'][0][0]-mosmetalspacing/2, self._DesignParameter['tg_pmos']['_XYCoordinates'][0][1]]]
				elif tg_nmos_gate%4==1:
					self._DesignParameter['tg_pmos']['_XYCoordinates'] = [[self._DesignParameter['tg_pmos']['_XYCoordinates'][0][0]-mosmetalspacing, self._DesignParameter['tg_pmos']['_XYCoordinates'][0][1]]]
				elif tg_nmos_gate%4==2:
					self._DesignParameter['tg_pmos']['_XYCoordinates'] = [[self._DesignParameter['tg_pmos']['_XYCoordinates'][0][0]+mosmetalspacing/2, self._DesignParameter['tg_pmos']['_XYCoordinates'][0][1]]]

		if tg_pmos_gate>tg_nmos_gate:
			if tg_nmos_gate%4==0:
				if tg_pmos_gate%4==1:
					self._DesignParameter['tg_nmos']['_XYCoordinates'] = [[self._DesignParameter['tg_nmos']['_XYCoordinates'][0][0]-mosmetalspacing/2, self._DesignParameter['tg_nmos']['_XYCoordinates'][0][1]]]
				elif tg_pmos_gate%4==2:
					self._DesignParameter['tg_nmos']['_XYCoordinates'] = [[self._DesignParameter['tg_nmos']['_XYCoordinates'][0][0]-mosmetalspacing, self._DesignParameter['tg_nmos']['_XYCoordinates'][0][1]]]
				elif tg_pmos_gate%4==3:
					self._DesignParameter['tg_nmos']['_XYCoordinates'] = [[self._DesignParameter['tg_nmos']['_XYCoordinates'][0][0]+mosmetalspacing/2, self._DesignParameter['tg_nmos']['_XYCoordinates'][0][1]]]
			elif tg_nmos_gate%4==1:
				if tg_pmos_gate%4==0:
					self._DesignParameter['tg_nmos']['_XYCoordinates'] = [[self._DesignParameter['tg_nmos']['_XYCoordinates'][0][0]+mosmetalspacing/2, self._DesignParameter['tg_nmos']['_XYCoordinates'][0][1]]]
				elif tg_pmos_gate%4==2:
					self._DesignParameter['tg_nmos']['_XYCoordinates'] = [[self._DesignParameter['tg_nmos']['_XYCoordinates'][0][0]-mosmetalspacing/2, self._DesignParameter['tg_nmos']['_XYCoordinates'][0][1]]]
				elif tg_pmos_gate%4==3:
					self._DesignParameter['tg_nmos']['_XYCoordinates'] = [[self._DesignParameter['tg_nmos']['_XYCoordinates'][0][0]+mosmetalspacing, self._DesignParameter['tg_nmos']['_XYCoordinates'][0][1]]]
			elif tg_nmos_gate%4==2:
				if tg_pmos_gate%4==0:
					self._DesignParameter['tg_nmos']['_XYCoordinates'] = [[self._DesignParameter['tg_nmos']['_XYCoordinates'][0][0]+mosmetalspacing, self._DesignParameter['tg_nmos']['_XYCoordinates'][0][1]]]
				elif tg_pmos_gate%4==1:
					self._DesignParameter['tg_nmos']['_XYCoordinates'] = [[self._DesignParameter['tg_nmos']['_XYCoordinates'][0][0]+mosmetalspacing/2, self._DesignParameter['tg_nmos']['_XYCoordinates'][0][1]]]
				elif tg_pmos_gate%4==3:
					self._DesignParameter['tg_nmos']['_XYCoordinates'] = [[self._DesignParameter['tg_nmos']['_XYCoordinates'][0][0]-mosmetalspacing/2, self._DesignParameter['tg_nmos']['_XYCoordinates'][0][1]]]
			elif tg_nmos_gate%4==3:
				if tg_pmos_gate%4==0:
					self._DesignParameter['tg_nmos']['_XYCoordinates'] = [[self._DesignParameter['tg_nmos']['_XYCoordinates'][0][0]-mosmetalspacing/2, self._DesignParameter['tg_nmos']['_XYCoordinates'][0][1]]]
				elif tg_pmos_gate%4==1:
					self._DesignParameter['tg_nmos']['_XYCoordinates'] = [[self._DesignParameter['tg_nmos']['_XYCoordinates'][0][0]-mosmetalspacing, self._DesignParameter['tg_nmos']['_XYCoordinates'][0][1]]]
				elif tg_pmos_gate%4==2:
					self._DesignParameter['tg_nmos']['_XYCoordinates'] = [[self._DesignParameter['tg_nmos']['_XYCoordinates'][0][0]+mosmetalspacing/2, self._DesignParameter['tg_nmos']['_XYCoordinates'][0][1]]]

		YCenterbtwtgmos=_OriginXY[0][1]#((self._DesignParameter['tg_nmos']['_XYCoordinates'][0][1]+self._DesignParameter['tg_nmos']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']/2)+(self._DesignParameter['tg_pmos']['_XYCoordinates'][0][1]-self._DesignParameter['tg_pmos']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']/2))/2

		self._DesignParameter['cap_input'] = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_Name='cap_inputIn{}'.format(_Name)))[0]
		self._DesignParameter['cap_input']['_DesignObj']._CalculateViaPoly2Met1DesignParameterMinimumEnclosureX(**dict(_ViaPoly2Met1NumberOfCOX=max(1, (int(((((self._DesignParameter['cap_nmos']['_XYCoordinates'][0][0] + self._DesignParameter['cap_nmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]) - (self._DesignParameter['cap_nmos']['_XYCoordinates'][0][0] + self._DesignParameter['cap_nmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0])) + self._DesignParameter['cap_nmos']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']) / (drc._CoMinWidth + drc._CoMinSpace))) + 1)), _ViaPoly2Met1NumberOfCOY=1))


		if cap_nmos_gate_y == None :
			self._DesignParameter['cap_nmos']['_XYCoordinates'] = [[max((((((self._DesignParameter['tg_nmos']['_XYCoordinates'][0][0] + self._DesignParameter['tg_nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][0]) + self._DesignParameter['cap_nmos']['_XYCoordinates'][0][0]) - (self._DesignParameter['cap_nmos']['_XYCoordinates'][0][0] + self._DesignParameter['cap_nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][0])) + (self._DesignParameter['tg_nmos']['_XYCoordinates'][0][0] + self._DesignParameter['tg_nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][1][0])) - (self._DesignParameter['tg_nmos']['_XYCoordinates'][0][0] + self._DesignParameter['tg_nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][0])),(((((self._DesignParameter['tg_pmos']['_XYCoordinates'][0][0] + self._DesignParameter['tg_pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][0]) + self._DesignParameter['cap_pmos']['_XYCoordinates'][0][0]) - (self._DesignParameter['cap_pmos']['_XYCoordinates'][0][0] + self._DesignParameter['cap_pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][0])) + (self._DesignParameter['tg_pmos']['_XYCoordinates'][0][0] + self._DesignParameter['tg_pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][1][0])) - (self._DesignParameter['tg_pmos']['_XYCoordinates'][0][0] + self._DesignParameter['tg_pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][0]))), \
																						   _OriginXY[0][1]-self._DesignParameter['cap_input']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']/2-self._DesignParameter['cap_nmos']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']/2-drc._Metal1MinSpace2]]
		else :
			self._DesignParameter['cap_nmos']['_XYCoordinates'] = [[max((((((self._DesignParameter['tg_nmos']['_XYCoordinates'][0][0] + self._DesignParameter['tg_nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][0]) + self._DesignParameter['cap_nmos']['_XYCoordinates'][0][0]) - (self._DesignParameter['cap_nmos']['_XYCoordinates'][0][0] + self._DesignParameter['cap_nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][0])) + (self._DesignParameter['tg_nmos']['_XYCoordinates'][0][0] + self._DesignParameter['tg_nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][1][0])) - (self._DesignParameter['tg_nmos']['_XYCoordinates'][0][0] + self._DesignParameter['tg_nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][0])),(((((self._DesignParameter['tg_pmos']['_XYCoordinates'][0][0] + self._DesignParameter['tg_pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][0]) + self._DesignParameter['cap_pmos']['_XYCoordinates'][0][0]) - (self._DesignParameter['cap_pmos']['_XYCoordinates'][0][0] + self._DesignParameter['cap_pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][0])) + (self._DesignParameter['tg_pmos']['_XYCoordinates'][0][0] + self._DesignParameter['tg_pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][1][0])) - (self._DesignParameter['tg_pmos']['_XYCoordinates'][0][0] + self._DesignParameter['tg_pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][0]))), (YCenterbtwtgmos - cap_nmos_gate_y)]]

		if cap_pmos_gate_y == None :
			self._DesignParameter['cap_pmos']['_XYCoordinates'] = [[self._DesignParameter['cap_nmos']['_XYCoordinates'][0][0], \
																						   _OriginXY[0][1]+self._DesignParameter['cap_input']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']/2+self._DesignParameter['cap_pmos']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']/2+drc._Metal1MinSpace2]]
		else :
			self._DesignParameter['cap_pmos']['_XYCoordinates'] = [[self._DesignParameter['cap_nmos']['_XYCoordinates'][0][0], (YCenterbtwtgmos + cap_pmos_gate_y)]]

		for i in range(0,cap_gate):
			self._DesignParameter['cap_input']['_XYCoordinates'] = [[self._DesignParameter['cap_nmos']['_XYCoordinates'][0][0]+self._DesignParameter['cap_nmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0], _OriginXY[0][1]]]  # YCenterbtwtgmos]]#((((self._DesignParameter['cap_nmos']['_XYCoordinates'][0][1] + self._DesignParameter['cap_nmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1]) + (self._DesignParameter['cap_nmos']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2)) + ((self._DesignParameter['cap_pmos']['_XYCoordinates'][0][1] + self._DesignParameter['cap_pmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1]) - (self._DesignParameter['cap_pmos']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2))) / 2)]]

		path_list = []
		if (len(self._DesignParameter['tg_pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates']) == 1):
		    mode = 'vertical'
		    _width = self._DesignParameter['tg_pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth']
		elif (self._DesignParameter['tg_pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][0] == self._DesignParameter['tg_pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][0]):
		    mode = 'horizontal'
		    _width = self._DesignParameter['tg_pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth']
		elif (self._DesignParameter['tg_pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1] == self._DesignParameter['tg_pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][1]):
		    mode = 'vertical'
		    _width = self._DesignParameter['tg_pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth']
		else:
		    print('Invalid Target Input')
		if (mode == 'vertical'):
		    xy_with_offset = []
		    target_y_value = YCenterbtwtgmos #(self._DesignParameter['tg_nmos']['_XYCoordinates'][0][1] + self._DesignParameter['tg_nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1])
		    for i in range(len(self._DesignParameter['tg_pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		        if ((i % 2) == 0):
		            xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['tg_pmos']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['tg_pmos']['_XYCoordinates'][0][1])], self._DesignParameter['tg_pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [xy_with_offset[i][0],target_y_value]])
		    for i in range(len(self._DesignParameter['tg_nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		        if ((i % 2) == 0):
		            xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['tg_nmos']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['tg_nmos']['_XYCoordinates'][0][1])], self._DesignParameter['tg_nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [xy_with_offset[i][0],target_y_value]])

		# elif (mode == 'horizontal'):
		#     xy_with_offset = []
		#     target_x_value = (self._DesignParameter['tg_nmos']['_XYCoordinates'][0][0] + self._DesignParameter['tg_nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][0])
		#     for i in range(len(self._DesignParameter['tg_pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		#         if ((i % 2) == 0):
		#             xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['tg_pmos']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['tg_pmos']['_XYCoordinates'][0][1])], self._DesignParameter['tg_pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])])
		#     for i in range(len(xy_with_offset)):
		#         path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		self._DesignParameter['m1_tg_source_routing_y'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=_width)
		self._DesignParameter['m1_tg_source_routing_y']['_XYCoordinates'] = path_list
		self._DesignParameter['m1_tg_cap_routing_x'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=self._DesignParameter['tg_nmos']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'])
		self._DesignParameter['m1_tg_cap_routing_x']['_XYCoordinates'] = [[[min(self._DesignParameter['tg_pmos']['_XYCoordinates'][0][0]+self._DesignParameter['tg_pmos']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0]-self._DesignParameter['tg_pmos']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']/2,self._DesignParameter['tg_nmos']['_XYCoordinates'][0][0]+self._DesignParameter['tg_nmos']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0]-self._DesignParameter['tg_nmos']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']/2), self._DesignParameter['cap_input']['_XYCoordinates'][0][1]], [self._DesignParameter['cap_input']['_XYCoordinates'][0][0],self._DesignParameter['cap_input']['_XYCoordinates'][0][1]]]]
		# self._DesignParameter['tg_pmos_input'] = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_Name='tg_pmos_inputIn{}'.format(_Name)))[0]
		# self._DesignParameter['tg_pmos_input']['_DesignObj']._CalculateViaPoly2Met1DesignParameterMinimumEnclosureY(**dict(_ViaPoly2Met1NumberOfCOX=max(2, int((((((self._DesignParameter['tg_pmos']['_XYCoordinates'][0][0] + self._DesignParameter['tg_pmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]) - (self._DesignParameter['tg_pmos']['_XYCoordinates'][0][0] + self._DesignParameter['tg_pmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0])) + self._DesignParameter['tg_pmos']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']) / (drc._CoMinWidth + drc._CoMinSpace)) + 1))), _ViaPoly2Met1NumberOfCOY=1))
		# self._DesignParameter['tg_pmos_input']['_XYCoordinates'] = [[self._DesignParameter['tg_pmos']['_XYCoordinates'][0][0], ((((self._DesignParameter['tg_pmos']['_XYCoordinates'][0][1] + self._DesignParameter['tg_pmos']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) + (self._DesignParameter['tg_pmos']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)) + (self._DesignParameter['tg_pmos_input']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)) + 71)]]
		# self._DesignParameter['tg_nmos_input'] = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_Name='tg_nmos_inputIn{}'.format(_Name)))[0]
		# self._DesignParameter['tg_nmos_input']['_DesignObj']._CalculateViaPoly2Met1DesignParameterMinimumEnclosureY(**dict(_ViaPoly2Met1NumberOfCOX=max(2, int((((((self._DesignParameter['tg_nmos']['_XYCoordinates'][0][0] + self._DesignParameter['tg_nmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]) - (self._DesignParameter['tg_nmos']['_XYCoordinates'][0][0] + self._DesignParameter['tg_nmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0])) + self._DesignParameter['tg_nmos']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']) / (drc._CoMinWidth + drc._CoMinSpace)) + 1))), _ViaPoly2Met1NumberOfCOY=1))
		# self._DesignParameter['tg_nmos_input']['_XYCoordinates'] = [[self._DesignParameter['tg_nmos']['_XYCoordinates'][0][0], ((((self._DesignParameter['tg_nmos']['_XYCoordinates'][0][1] + self._DesignParameter['tg_nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1]) - (self._DesignParameter['tg_nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_YWidth'] / 2)) - (self._DesignParameter['tg_nmos_input']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)) - 71)]]
		# self._DesignParameter['via_m1_m2_pmos_input'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='via_m1_m2_pmos_inputIn{}'.format(_Name)))[0]
		# self._DesignParameter['via_m1_m2_pmos_input']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureY(**dict(_ViaMet12Met2NumberOfCOX=int(max((self._DesignParameter['tg_pmos_input']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] / (drc._CoMinWidth + drc._CoMinSpace)), 2)), _ViaMet12Met2NumberOfCOY=1))
		# self._DesignParameter['via_m1_m2_pmos_input']['_XYCoordinates'] = [[(+ self._DesignParameter['tg_pmos_input']['_XYCoordinates'][0][0]), (+ self._DesignParameter['tg_pmos_input']['_XYCoordinates'][0][1])]]
		# self._DesignParameter['via_m1_m2_nmos_input'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='via_m1_m2_nmos_inputIn{}'.format(_Name)))[0]
		# self._DesignParameter['via_m1_m2_nmos_input']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureY(**dict(_ViaMet12Met2NumberOfCOX=int(max((self._DesignParameter['tg_pmos_input']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] / (drc._CoMinWidth + drc._CoMinSpace)), 2)), _ViaMet12Met2NumberOfCOY=1))
		# self._DesignParameter['via_m1_m2_nmos_input']['_XYCoordinates'] = [[(+ self._DesignParameter['tg_nmos_input']['_XYCoordinates'][0][0]), (+ self._DesignParameter['tg_nmos_input']['_XYCoordinates'][0][1])]]
		path_list = []
		if (len(self._DesignParameter['cap_pmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates']) == 1):
		    mode = 'vertical'
		    _width = self._DesignParameter['cap_pmos']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
		elif (self._DesignParameter['cap_pmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0] == self._DesignParameter['cap_pmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]):
		    mode = 'horizontal'
		    _width = self._DesignParameter['cap_pmos']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
		elif (self._DesignParameter['cap_pmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1] == self._DesignParameter['cap_pmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][1]):
		    mode = 'vertical'
		    _width = self._DesignParameter['cap_pmos']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
		else:
		    print('Invalid Target Input')
		if (mode == 'vertical'):
		    xy_with_offset = []
		    target_y_value = (self._DesignParameter['cap_nmos']['_XYCoordinates'][0][1] + self._DesignParameter['cap_nmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1])
		    for i in range(len(self._DesignParameter['cap_pmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
		        xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['cap_pmos']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['cap_pmos']['_XYCoordinates'][0][1])], self._DesignParameter['cap_pmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		elif (mode == 'horizontal'):
		    xy_with_offset = []
		    target_x_value = (self._DesignParameter['cap_nmos']['_XYCoordinates'][0][0] + self._DesignParameter['cap_nmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0])
		    for i in range(len(self._DesignParameter['cap_pmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
		        xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['cap_pmos']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['cap_pmos']['_XYCoordinates'][0][1])], self._DesignParameter['cap_pmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		self._DesignParameter['poly_cap_gate'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _Width=_width)
		self._DesignParameter['poly_cap_gate']['_XYCoordinates'] = path_list
		XYList = []
		xy_offset = [0, 0]
		for i in range(len(self._DesignParameter['tg_pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		    if ((i % 2) == 1):
		        xy = (self._DesignParameter['tg_pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i][0] if (type(self._DesignParameter['tg_pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i][0]) == list) else self._DesignParameter['tg_pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])
		        XYList.append([((x + y) + z) for (x, y, z) in zip([(0 + self._DesignParameter['tg_pmos']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['tg_pmos']['_XYCoordinates'][0][1])], xy, xy_offset)])
		self._DesignParameter['via_m1_m3_pmos_output'] = self._SrefElementDeclaration(_DesignObj=ViaStack._ViaStack(_Name='via_m1_m3_pmos_outputIn{}'.format(_Name)))[0]
		self._DesignParameter['via_m1_m3_pmos_output']['_DesignObj']._CalculateStackSameEnclosure(**dict(COX=1, COY=max(2,int(self._DesignParameter['tg_pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_YWidth']/(drc._CoMinWidth+drc._CoMinSpace))), start_layer=1, end_layer=3))
		self._DesignParameter['via_m1_m3_pmos_output']['_XYCoordinates'] = XYList
		# if (self._DesignParameter['via_m1_m2_pmos_input']['_XYCoordinates'][0][1]-self._DesignParameter['via_m1_m2_pmos_input']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']/2)-(self._DesignParameter['via_m1_m3_pmos_output']['_XYCoordinates'][0][1]+self._DesignParameter['via_m1_m3_pmos_output']['_DesignObj']._DesignParameter['ViaMet12Met2']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']/2)<60:
		# 	tmp=60-((self._DesignParameter['via_m1_m2_pmos_input']['_XYCoordinates'][0][1]-self._DesignParameter['via_m1_m2_pmos_input']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']/2)-(self._DesignParameter['via_m1_m3_pmos_output']['_XYCoordinates'][0][1]+self._DesignParameter['via_m1_m3_pmos_output']['_DesignObj']._DesignParameter['ViaMet12Met2']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']/2))
		# 	tmpXYList=[]
		# 	for i in range(0,len(XYList)):
		# 		tmpXYList.append([XYList[i][0],XYList[i][1]-tmp])
		# 	self._DesignParameter['via_m1_m3_pmos_output']['_XYCoordinates']=tmpXYList
		# 	del tmp
		XYList = []
		xy_offset = [0, 0]
		for i in range(len(self._DesignParameter['tg_nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		    if ((i % 2) == 1):
		        xy = (self._DesignParameter['tg_nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i][0] if (type(self._DesignParameter['tg_nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i][0]) == list) else self._DesignParameter['tg_nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])
		        XYList.append([((x + y) + z) for (x, y, z) in zip([(0 + self._DesignParameter['tg_nmos']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['tg_nmos']['_XYCoordinates'][0][1])], xy, xy_offset)])
		self._DesignParameter['via_m1_m3_nmos_output'] = self._SrefElementDeclaration(_DesignObj=ViaStack._ViaStack(_Name='via_m1_m3_nmos_outputIn{}'.format(_Name)))[0]
		self._DesignParameter['via_m1_m3_nmos_output']['_DesignObj']._CalculateStackSameEnclosure(**dict(COX=1, COY=max(2,int(self._DesignParameter['tg_nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_YWidth']/(drc._CoMinWidth+drc._CoMinSpace))), start_layer=1, end_layer=3))
		self._DesignParameter['via_m1_m3_nmos_output']['_XYCoordinates'] = XYList

		self._DesignParameter['m2_routing_tg_output']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _Width=None)
		self._DesignParameter['m2_routing_tg_output']['_Width']=self._DesignParameter['via_m1_m3_nmos_output']['_DesignObj']._DesignParameter['ViaMet22Met3']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth']
		self._DesignParameter['m2_routing_tg_output']['_XYCoordinates']=[[[self._DesignParameter['tg_nmos']['_XYCoordinates'][0][0]+self._DesignParameter['tg_nmos']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][0][0],self._DesignParameter['tg_nmos']['_XYCoordinates'][0][1]],[self._DesignParameter['tg_nmos']['_XYCoordinates'][0][0]+self._DesignParameter['tg_nmos']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][-1][0],self._DesignParameter['tg_nmos']['_XYCoordinates'][0][1]]],[[self._DesignParameter['tg_pmos']['_XYCoordinates'][0][0]+self._DesignParameter['tg_pmos']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][0][0],self._DesignParameter['tg_pmos']['_XYCoordinates'][0][1]],[self._DesignParameter['tg_pmos']['_XYCoordinates'][0][0]+self._DesignParameter['tg_pmos']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][-1][0],self._DesignParameter['tg_pmos']['_XYCoordinates'][0][1]]]]


		# if -(self._DesignParameter['via_m1_m2_nmos_input']['_XYCoordinates'][0][1]+self._DesignParameter['via_m1_m2_nmos_input']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']/2)+(self._DesignParameter['via_m1_m3_nmos_output']['_XYCoordinates'][0][1]-self._DesignParameter['via_m1_m3_nmos_output']['_DesignObj']._DesignParameter['ViaMet12Met2']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']/2)<60:
		# 	tmp=60-(-(self._DesignParameter['via_m1_m2_nmos_input']['_XYCoordinates'][0][1]+self._DesignParameter['via_m1_m2_nmos_input']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']/2)+(self._DesignParameter['via_m1_m3_nmos_output']['_XYCoordinates'][0][1]-self._DesignParameter['via_m1_m3_nmos_output']['_DesignObj']._DesignParameter['ViaMet12Met2']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']/2))
		# 	tmpXYList=[]
		# 	for i in range(0,len(XYList)):
		# 		tmpXYList.append([XYList[i][0],XYList[i][1]+tmp])
		# 	self._DesignParameter['via_m1_m3_nmos_output']['_XYCoordinates']=tmpXYList
		# 	del tmp
		path_list = []
		if (len(self._DesignParameter['tg_pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates']) == 1):
		    mode = 'vertical'
		    _width = self._DesignParameter['tg_pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth']
		elif (self._DesignParameter['tg_pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][0] == self._DesignParameter['tg_pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][0]):
		    mode = 'horizontal'
		    _width = self._DesignParameter['tg_pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth']
		elif (self._DesignParameter['tg_pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1] == self._DesignParameter['tg_pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][1]):
		    mode = 'vertical'
		    _width = self._DesignParameter['tg_pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth']
		else:
		    print('Invalid Target Input')
		if (mode == 'vertical'):
			if tg_pmos_gate<tg_nmos_gate:
				xy_with_offset = []
				target_y_value = (self._DesignParameter['tg_nmos']['_XYCoordinates'][0][1] + self._DesignParameter['tg_nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1])
				for i in range(len(self._DesignParameter['tg_pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
					if ((i % 2) == 1):
						xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['tg_pmos']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['tg_pmos']['_XYCoordinates'][0][1])], self._DesignParameter['tg_pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])])
				for i in range(len(xy_with_offset)):
					path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
			else:
				xy_with_offset = []
				target_y_value = (self._DesignParameter['tg_pmos']['_XYCoordinates'][0][1] + self._DesignParameter['tg_pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1])
				for i in range(len(self._DesignParameter['tg_nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
					if ((i % 2) == 1):
						xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['tg_nmos']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['tg_nmos']['_XYCoordinates'][0][1])], self._DesignParameter['tg_nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])])
				for i in range(len(xy_with_offset)):
					path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])

		# elif (mode == 'horizontal'):
		#     xy_with_offset = []
		#     target_x_value = (self._DesignParameter['tg_nmos']['_XYCoordinates'][0][0] + self._DesignParameter['tg_nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][0])
		#     for i in range(len(self._DesignParameter['tg_pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		#         if ((i % 2) == 1):
		#             xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['tg_pmos']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['tg_pmos']['_XYCoordinates'][0][1])], self._DesignParameter['tg_pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])])
		#     for i in range(len(xy_with_offset)):
		#         path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		self._DesignParameter['m3_input'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0], _Datatype=DesignParameters._LayerMapping['METAL3'][1], _Width=_width)
		self._DesignParameter['m3_input']['_XYCoordinates'] = path_list
		path_list = []
		if (len(self._DesignParameter['cap_pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates']) == 1):
		    mode = 'vertical'
		    _width = self._DesignParameter['cap_pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth']
		elif (self._DesignParameter['cap_pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][0] == self._DesignParameter['cap_pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][0]):
		    mode = 'horizontal'
		    _width = self._DesignParameter['cap_pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth']
		elif (self._DesignParameter['cap_pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1] == self._DesignParameter['cap_pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][1]):
		    mode = 'vertical'
		    _width = self._DesignParameter['cap_pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth']
		else:
		    print('Invalid Target Input')
		if (mode == 'vertical'):
		    xy_with_offset = []
		    target_y_value = ((self._DesignParameter['cap_pmos']['_XYCoordinates'][0][1] + self._DesignParameter['cap_pmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1]) + (self._DesignParameter['cap_pmos']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2))
		    for i in range(len(self._DesignParameter['cap_pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		        xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['cap_pmos']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['cap_pmos']['_XYCoordinates'][0][1])], self._DesignParameter['cap_pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		elif (mode == 'horizontal'):
		    xy_with_offset = []
		    target_x_value = (self._DesignParameter['cap_pmos']['_XYCoordinates'][0][0] + self._DesignParameter['cap_pmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0])
		    for i in range(len(self._DesignParameter['cap_pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		        xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['cap_pmos']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['cap_pmos']['_XYCoordinates'][0][1])], self._DesignParameter['cap_pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		self._DesignParameter['m1_cap_vdd_routing'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=_width)
		self._DesignParameter['m1_cap_vdd_routing']['_XYCoordinates'] = path_list
		path_list = []
		if (len(self._DesignParameter['cap_nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates']) == 1):
		    mode = 'vertical'
		    _width = self._DesignParameter['cap_nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth']
		elif (self._DesignParameter['cap_nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][0] == self._DesignParameter['cap_nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][0]):
		    mode = 'horizontal'
		    _width = self._DesignParameter['cap_nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth']
		elif (self._DesignParameter['cap_nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1] == self._DesignParameter['cap_nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][1]):
		    mode = 'vertical'
		    _width = self._DesignParameter['cap_nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth']
		else:
		    print('Invalid Target Input')
		if (mode == 'vertical'):
		    xy_with_offset = []
		    target_y_value = ((self._DesignParameter['cap_nmos']['_XYCoordinates'][0][1] + self._DesignParameter['cap_nmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1]) - (self._DesignParameter['cap_nmos']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2))
		    for i in range(len(self._DesignParameter['cap_nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		        xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['cap_nmos']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['cap_nmos']['_XYCoordinates'][0][1])], self._DesignParameter['cap_nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		elif (mode == 'horizontal'):
		    xy_with_offset = []
		    target_x_value = (self._DesignParameter['cap_nmos']['_XYCoordinates'][0][0] + self._DesignParameter['cap_nmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0])
		    for i in range(len(self._DesignParameter['cap_nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		        xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['cap_nmos']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['cap_nmos']['_XYCoordinates'][0][1])], self._DesignParameter['cap_nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		self._DesignParameter['m1_nmos_vss_routing'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=_width)
		self._DesignParameter['m1_nmos_vss_routing']['_XYCoordinates'] = path_list
		self._DesignParameter['NWELL_boundary_2'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['NWELL'][0], _Datatype=DesignParameters._LayerMapping['NWELL'][1], _XWidth=((((self._DesignParameter['cap_pmos']['_XYCoordinates'][0][0] + self._DesignParameter['cap_pmos']['_DesignObj']._DesignParameter['_ODLayer']['_XYCoordinates'][0][0]) + (self._DesignParameter['cap_pmos']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth'] / 2)) - ((self._DesignParameter['tg_pmos']['_XYCoordinates'][0][0] + self._DesignParameter['tg_pmos']['_DesignObj']._DesignParameter['_ODLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['tg_pmos']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth'] / 2))) + (2 * drc._NwMinEnclosurePactive2)), _YWidth=((max(((self._DesignParameter['tg_pmos']['_XYCoordinates'][0][1] + self._DesignParameter['tg_pmos']['_DesignObj']._DesignParameter['_ODLayer']['_XYCoordinates'][0][1]) + (self._DesignParameter['tg_pmos']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth'] / 2)),((self._DesignParameter['cap_pmos']['_XYCoordinates'][0][1] + self._DesignParameter['cap_pmos']['_DesignObj']._DesignParameter['_ODLayer']['_XYCoordinates'][0][1]) + (self._DesignParameter['cap_pmos']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth'] / 2))) + drc._NwMinEnclosurePactive2) - min(((self._DesignParameter['tg_pmos']['_XYCoordinates'][0][1] + self._DesignParameter['tg_pmos']['_DesignObj']._DesignParameter['_PPLayer']['_XYCoordinates'][0][1]) - (self._DesignParameter['tg_pmos']['_DesignObj']._DesignParameter['_PPLayer']['_YWidth'] / 2)),((self._DesignParameter['cap_pmos']['_XYCoordinates'][0][1] + self._DesignParameter['cap_pmos']['_DesignObj']._DesignParameter['_PPLayer']['_XYCoordinates'][0][1]) - (self._DesignParameter['cap_pmos']['_DesignObj']._DesignParameter['_PPLayer']['_YWidth'] / 2)))))
		self._DesignParameter['NWELL_boundary_2']['_XYCoordinates'] = [[((((self._DesignParameter['tg_pmos']['_XYCoordinates'][0][0] + self._DesignParameter['tg_pmos']['_DesignObj']._DesignParameter['_ODLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['tg_pmos']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth'] / 2)) + ((self._DesignParameter['cap_pmos']['_XYCoordinates'][0][0] + self._DesignParameter['cap_pmos']['_DesignObj']._DesignParameter['_ODLayer']['_XYCoordinates'][0][0]) + (self._DesignParameter['cap_pmos']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth'] / 2))) / 2), (((max(((self._DesignParameter['tg_pmos']['_XYCoordinates'][0][1] + self._DesignParameter['tg_pmos']['_DesignObj']._DesignParameter['_ODLayer']['_XYCoordinates'][0][1]) + (self._DesignParameter['tg_pmos']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth'] / 2)),((self._DesignParameter['cap_pmos']['_XYCoordinates'][0][1] + self._DesignParameter['cap_pmos']['_DesignObj']._DesignParameter['_ODLayer']['_XYCoordinates'][0][1]) + (self._DesignParameter['cap_pmos']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth'] / 2))) + drc._NwMinEnclosurePactive2) + min(((self._DesignParameter['tg_pmos']['_XYCoordinates'][0][1] + self._DesignParameter['tg_pmos']['_DesignObj']._DesignParameter['_PPLayer']['_XYCoordinates'][0][1]) - (self._DesignParameter['tg_pmos']['_DesignObj']._DesignParameter['_PPLayer']['_YWidth'] / 2)),((self._DesignParameter['cap_pmos']['_XYCoordinates'][0][1] + self._DesignParameter['cap_pmos']['_DesignObj']._DesignParameter['_PPLayer']['_XYCoordinates'][0][1]) - (self._DesignParameter['cap_pmos']['_DesignObj']._DesignParameter['_PPLayer']['_YWidth'] / 2)))))/2]]
		self._DesignParameter['xvtlayer']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping[tg_xvt][0], _Datatype=DesignParameters._LayerMapping[tg_xvt][1], _Width=None)
		_XVTLayer='_'+tg_xvt+'Layer'
		self._DesignParameter['xvtlayer']['_Width']=max((self._DesignParameter['cap_nmos']['_XYCoordinates'][0][0]+self._DesignParameter['cap_nmos']['_DesignObj']._DesignParameter[_XVTLayer]['_XWidth']/2-(self._DesignParameter['tg_nmos']['_XYCoordinates'][0][0]-self._DesignParameter['tg_nmos']['_DesignObj']._DesignParameter[_XVTLayer]['_XWidth']/2)),(self._DesignParameter['cap_pmos']['_XYCoordinates'][0][0]+self._DesignParameter['cap_pmos']['_DesignObj']._DesignParameter[_XVTLayer]['_XWidth']/2-self._DesignParameter['tg_pmos']['_XYCoordinates'][0][0]-self._DesignParameter['tg_pmos']['_DesignObj']._DesignParameter[_XVTLayer]['_XWidth']/2))
		self._DesignParameter['xvtlayer']['_XYCoordinates']=[[[(self._DesignParameter['cap_nmos']['_XYCoordinates'][0][0]+self._DesignParameter['cap_nmos']['_DesignObj']._DesignParameter[_XVTLayer]['_XWidth']/2+self._DesignParameter['tg_nmos']['_XYCoordinates'][0][0]-self._DesignParameter['tg_nmos']['_DesignObj']._DesignParameter[_XVTLayer]['_XWidth']/2)/2,self._DesignParameter['cap_pmos']['_XYCoordinates'][0][1]+self._DesignParameter['cap_pmos']['_DesignObj']._DesignParameter[_XVTLayer]['_YWidth']/2],[(self._DesignParameter['cap_nmos']['_XYCoordinates'][0][0]+self._DesignParameter['cap_nmos']['_DesignObj']._DesignParameter[_XVTLayer]['_XWidth']/2+self._DesignParameter['tg_nmos']['_XYCoordinates'][0][0]-self._DesignParameter['tg_nmos']['_DesignObj']._DesignParameter[_XVTLayer]['_XWidth']/2)/2,self._DesignParameter['cap_nmos']['_XYCoordinates'][0][1]-self._DesignParameter['tg_nmos']['_DesignObj']._DesignParameter[_XVTLayer]['_YWidth']/2]]]

		self._DesignParameter['tg_pmos_input'] = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_Name='tg_pmos_inputIn{}'.format(_Name)))[0]
		self._DesignParameter['tg_pmos_input']['_DesignObj']._CalculateViaPoly2Met1DesignParameterMinimumEnclosureX(**dict(_ViaPoly2Met1NumberOfCOX=max(2, int((((((self._DesignParameter['tg_pmos']['_XYCoordinates'][0][0] + self._DesignParameter['tg_pmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]) - (self._DesignParameter['tg_pmos']['_XYCoordinates'][0][0] + self._DesignParameter['tg_pmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]))-2*drc._CoMinEnclosureByPOAtLeastTwoSide) / (drc._CoMinWidth + drc._CoMinSpace)) + 1))), _ViaPoly2Met1NumberOfCOY=1))
		self._DesignParameter['tg_pmos_input']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']=drc._CoMinWidth+2*drc._Metal1MinEnclosureCO
		self._DesignParameter['tg_pmos_input']['_XYCoordinates'] = [[self._DesignParameter['tg_pmos']['_XYCoordinates'][0][0], max(self._DesignParameter['tg_pmos']['_XYCoordinates'][0][1] + self._DesignParameter['tg_pmos']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1] + self._DesignParameter['tg_pmos']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2 + self._DesignParameter['tg_pmos_input']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2, self._DesignParameter['via_m1_m3_pmos_output']['_XYCoordinates'][0][1]+self._DesignParameter['via_m1_m3_pmos_output']['_DesignObj']._DesignParameter['ViaMet12Met2']['_XYCoordinates'][0][1]+self._DesignParameter['via_m1_m3_pmos_output']['_DesignObj']._DesignParameter['ViaMet12Met2']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']/2+self._DesignParameter['tg_pmos_input']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)+70]]
		self._DesignParameter['tg_nmos_input'] = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_Name='tg_nmos_inputIn{}'.format(_Name)))[0]
		self._DesignParameter['tg_nmos_input']['_DesignObj']._CalculateViaPoly2Met1DesignParameterMinimumEnclosureX(**dict(_ViaPoly2Met1NumberOfCOX=max(2, int((((((self._DesignParameter['tg_nmos']['_XYCoordinates'][0][0] + self._DesignParameter['tg_nmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]) - (self._DesignParameter['tg_nmos']['_XYCoordinates'][0][0] + self._DesignParameter['tg_nmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]))-2*drc._CoMinEnclosureByPOAtLeastTwoSide) / (drc._CoMinWidth + drc._CoMinSpace)) + 1))), _ViaPoly2Met1NumberOfCOY=1))
		self._DesignParameter['tg_nmos_input']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']=drc._CoMinWidth+2*drc._Metal1MinEnclosureCO
		self._DesignParameter['tg_nmos_input']['_XYCoordinates'] = [[self._DesignParameter['tg_nmos']['_XYCoordinates'][0][0], min(self._DesignParameter['tg_nmos']['_XYCoordinates'][0][1] + self._DesignParameter['tg_nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1] - self._DesignParameter['tg_nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_YWidth'] / 2 - self._DesignParameter['tg_nmos_input']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2, self._DesignParameter['via_m1_m3_nmos_output']['_XYCoordinates'][0][1]+self._DesignParameter['via_m1_m3_nmos_output']['_DesignObj']._DesignParameter['ViaMet12Met2']['_XYCoordinates'][0][1]-self._DesignParameter['via_m1_m3_nmos_output']['_DesignObj']._DesignParameter['ViaMet12Met2']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']/2-self._DesignParameter['tg_nmos_input']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)-70]]
		self._DesignParameter['additional_poly_input']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _Width=None)
		self._DesignParameter['additional_poly_input']['_Width']=self._DesignParameter['tg_pmos_input']['_DesignObj']._DesignParameter['_POLayer']['_YWidth']
		self._DesignParameter['additional_poly_input']['_XYCoordinates']=[[[self._DesignParameter['tg_pmos']['_XYCoordinates'][0][0]+self._DesignParameter['tg_pmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0],self._DesignParameter['tg_pmos_input']['_XYCoordinates'][0][1]],[self._DesignParameter['tg_pmos']['_XYCoordinates'][0][0]+self._DesignParameter['tg_pmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][-1][0],self._DesignParameter['tg_pmos_input']['_XYCoordinates'][0][1]]],[[self._DesignParameter['tg_nmos']['_XYCoordinates'][0][0]+self._DesignParameter['tg_nmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0],self._DesignParameter['tg_nmos_input']['_XYCoordinates'][0][1]],[self._DesignParameter['tg_nmos']['_XYCoordinates'][0][0]+self._DesignParameter['tg_nmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][-1][0],self._DesignParameter['tg_nmos_input']['_XYCoordinates'][0][1]]]]


		self._DesignParameter['via_m1_m2_pmos_input'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='via_m1_m2_pmos_inputIn{}'.format(_Name)))[0]
		self._DesignParameter['via_m1_m2_pmos_input']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureY(**dict(_ViaMet12Met2NumberOfCOX=int(max((self._DesignParameter['tg_pmos_input']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] / (drc._CoMinWidth + drc._CoMinSpace)), 2)), _ViaMet12Met2NumberOfCOY=1))
		self._DesignParameter['via_m1_m2_pmos_input']['_XYCoordinates'] = [[(+ self._DesignParameter['tg_pmos_input']['_XYCoordinates'][0][0]), (+ self._DesignParameter['tg_pmos_input']['_XYCoordinates'][0][1])]]
		self._DesignParameter['via_m1_m2_nmos_input'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='via_m1_m2_nmos_inputIn{}'.format(_Name)))[0]
		self._DesignParameter['via_m1_m2_nmos_input']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureY(**dict(_ViaMet12Met2NumberOfCOX=int(max((self._DesignParameter['tg_nmos_input']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] / (drc._CoMinWidth + drc._CoMinSpace)), 2)), _ViaMet12Met2NumberOfCOY=1))
		self._DesignParameter['via_m1_m2_nmos_input']['_XYCoordinates'] = [[(+ self._DesignParameter['tg_nmos_input']['_XYCoordinates'][0][0]), (+ self._DesignParameter['tg_nmos_input']['_XYCoordinates'][0][1])]]

		path_list = []
		if (len(self._DesignParameter['tg_pmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates']) == 1):
		    mode = 'vertical'
		    _width = self._DesignParameter['tg_pmos']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
		elif (self._DesignParameter['tg_pmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0] == self._DesignParameter['tg_pmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]):
		    mode = 'horizontal'
		    _width = self._DesignParameter['tg_pmos']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
		elif (self._DesignParameter['tg_pmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1] == self._DesignParameter['tg_pmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][1]):
		    mode = 'vertical'
		    _width = self._DesignParameter['tg_pmos']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
		else:
		    print('Invalid Target Input')
		if (mode == 'vertical'):
		    xy_with_offset = []
		    target_y_value = ((self._DesignParameter['tg_pmos_input']['_XYCoordinates'][0][1] + self._DesignParameter['tg_pmos_input']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1]) + (self._DesignParameter['tg_pmos_input']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2))
		    for i in range(len(self._DesignParameter['tg_pmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
		        xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['tg_pmos']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['tg_pmos']['_XYCoordinates'][0][1])], self._DesignParameter['tg_pmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		elif (mode == 'horizontal'):
		    xy_with_offset = []
		    target_x_value = (self._DesignParameter['tg_pmos_input']['_XYCoordinates'][0][0] + self._DesignParameter['tg_pmos_input']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0])
		    for i in range(len(self._DesignParameter['tg_pmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
		        xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['tg_pmos']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['tg_pmos']['_XYCoordinates'][0][1])], self._DesignParameter['tg_pmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		self._DesignParameter['po_tg_pmos_input_routing_y'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _Width=_width)
		self._DesignParameter['po_tg_pmos_input_routing_y']['_XYCoordinates'] = path_list
		path_list = []
		if (len(self._DesignParameter['tg_nmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates']) == 1):
		    mode = 'vertical'
		    _width = self._DesignParameter['tg_nmos']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
		elif (self._DesignParameter['tg_nmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0] == self._DesignParameter['tg_nmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]):
		    mode = 'horizontal'
		    _width = self._DesignParameter['tg_nmos']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
		elif (self._DesignParameter['tg_nmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1] == self._DesignParameter['tg_nmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][1]):
		    mode = 'vertical'
		    _width = self._DesignParameter['tg_nmos']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
		else:
		    print('Invalid Target Input')
		if (mode == 'vertical'):
		    xy_with_offset = []
		    target_y_value = ((self._DesignParameter['tg_nmos_input']['_XYCoordinates'][0][1] + self._DesignParameter['tg_nmos_input']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1]) - (self._DesignParameter['tg_nmos_input']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2))
		    for i in range(len(self._DesignParameter['tg_nmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
		        xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['tg_nmos']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['tg_nmos']['_XYCoordinates'][0][1])], self._DesignParameter['tg_nmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		elif (mode == 'horizontal'):
		    xy_with_offset = []
		    target_x_value = (self._DesignParameter['tg_nmos_input']['_XYCoordinates'][0][0] + self._DesignParameter['tg_nmos_input']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0])
		    for i in range(len(self._DesignParameter['tg_nmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
		        xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['tg_nmos']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['tg_nmos']['_XYCoordinates'][0][1])], self._DesignParameter['tg_nmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		self._DesignParameter['po_tg_nmos_routing_y'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _Width=_width)
		self._DesignParameter['po_tg_nmos_routing_y']['_XYCoordinates'] = path_list

		self._DesignParameter['additional_nmos_m1']=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _XWidth=None, _YWidth=None)
		self._DesignParameter['additional_nmos_m1']['_XWidth']=max(self._DesignParameter['tg_nmos']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'], self._DesignParameter['via_m1_m3_nmos_output']['_DesignObj']._DesignParameter['ViaMet12Met2']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'])
		self._DesignParameter['additional_nmos_m1']['_YWidth']=max(self._DesignParameter['tg_nmos']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'], self._DesignParameter['via_m1_m3_nmos_output']['_DesignObj']._DesignParameter['ViaMet12Met2']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'])
		tmp=[]
		for i in range(0,len(self._DesignParameter['tg_nmos']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'])):
			tmp.append([self._DesignParameter['tg_nmos']['_XYCoordinates'][0][0]+self._DesignParameter['tg_nmos']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][i][0], self._DesignParameter['tg_nmos']['_XYCoordinates'][0][1]+self._DesignParameter['tg_nmos']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][i][1]])

		self._DesignParameter['additional_nmos_m1']['_XYCoordinates']=tmp
		del tmp

		self._DesignParameter['additional_pmos_m1']=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _XWidth=None, _YWidth=None)
		self._DesignParameter['additional_pmos_m1']['_XWidth']=max(self._DesignParameter['tg_pmos']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'], self._DesignParameter['via_m1_m3_pmos_output']['_DesignObj']._DesignParameter['ViaMet12Met2']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'])
		self._DesignParameter['additional_pmos_m1']['_YWidth']=max(self._DesignParameter['tg_pmos']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'], self._DesignParameter['via_m1_m3_pmos_output']['_DesignObj']._DesignParameter['ViaMet12Met2']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'])
		tmp=[]
		for i in range(0,len(self._DesignParameter['tg_pmos']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'])):
			tmp.append([self._DesignParameter['tg_pmos']['_XYCoordinates'][0][0]+self._DesignParameter['tg_pmos']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][i][0], self._DesignParameter['tg_pmos']['_XYCoordinates'][0][1]+self._DesignParameter['tg_pmos']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][i][1]])

		self._DesignParameter['additional_pmos_m1']['_XYCoordinates']=tmp
		del tmp

