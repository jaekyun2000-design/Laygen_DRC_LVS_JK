from generatorLib import StickDiagram
from generatorLib import DesignParameters
import copy
import math
from generatorLib import DRC
from generatorLib.generator_models import ViaMet32Met4
from generatorLib.generator_models import NSubRing
from generatorLib.generator_models import NMOSWithDummy
from generatorLib.generator_models import PMOSWithDummy
from generatorLib.generator_models import ViaMet22Met3
from generatorLib.generator_models import ViaMet12Met2
from generatorLib.generator_models import ViaPoly2Met1
from generatorLib.generator_models import PSubRing

class SlicerInSlicerWithSRLatch_0(StickDiagram._StickDiagram):
	def __init__(self, _DesignParameter=None, _Name='SlicerInSlicerWithSRLatch_0'):
		if _DesignParameter != None:
			self._DesignParameter = _DesignParameter
		else:
			self._DesignParameter = dict(_Name=self._NameDeclaration(_Name=_Name), _GDSFile=self._GDSObjDeclaration(_GDSFile=None))
		self._DesignParameter['_Name']['Name'] = _Name

	def _CalculateDesignParameter(self,SLVT=None,input_via_y=2,gate_spacing=96,subring_via=2,precharge_outside_gate=6,precharge_inside_gate=3,subring_addi=200,pmos_fwidth=1000,nmos_fwidth=1000):
	
		drc = DRC.DRC()
		_Name = self._DesignParameter['_Name']['_Name']
		
		self._DesignParameter['nmos_bot'] = self._SrefElementDeclaration(_DesignObj=NMOSWithDummy._NMOS(_Name='nmos_botIn{}'.format(_Name)))[0]
		self._DesignParameter['nmos_bot']['_DesignObj']._CalculateNMOSDesignParameter(**dict(_NMOSNumberofGate=8, _NMOSChannelWidth=nmos_fwidth, _NMOSChannellength=30, _NMOSDummy=True, _GateSpacing=None, _XVT='SLVT'))
		self._DesignParameter['nmos_bot']['_XYCoordinates'] = [[0.0, (- 2495.0)]]
		bot_nmos_via_num = int((((self._DesignParameter['nmos_bot']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] - drc._VIAxMinSpace) - (2 * drc._VIAxMinEnclosureByMetx)) / (drc._VIAxMinWidth + drc._VIAxMinSpace)))
		XYList = []
		xy_offset = [0, 0]
		for i in range(len(self._DesignParameter['nmos_bot']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'])):
		    if ((i % 2) == 0):
		        xy = (self._DesignParameter['nmos_bot']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i][0] if (type(self._DesignParameter['nmos_bot']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i][0]) == list) else self._DesignParameter['nmos_bot']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i])
		        XYList.append([((x + y) + z) for (x, y, z) in zip([(0 + self._DesignParameter['nmos_bot']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['nmos_bot']['_XYCoordinates'][0][1])], xy, xy_offset)])
		self._DesignParameter['bot_nmos_via12'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='bot_nmos_via12In{}'.format(_Name)))[0]
		self._DesignParameter['bot_nmos_via12']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(**dict(_ViaMet12Met2NumberOfCOX=1, _ViaMet12Met2NumberOfCOY=bot_nmos_via_num))
		self._DesignParameter['bot_nmos_via12']['_XYCoordinates'] = XYList
		XYList = []
		xy_offset = [0, 0]
		for i in range(len(self._DesignParameter['bot_nmos_via12']['_XYCoordinates'])):
		    xy = (self._DesignParameter['bot_nmos_via12']['_XYCoordinates'][i][0] if (type(self._DesignParameter['bot_nmos_via12']['_XYCoordinates'][i][0]) == list) else self._DesignParameter['bot_nmos_via12']['_XYCoordinates'][i])
		    XYList.append([((x + y) + z) for (x, y, z) in zip([0, 0], xy, xy_offset)])
		self._DesignParameter['bot_nmos_via23'] = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_Name='bot_nmos_via23In{}'.format(_Name)))[0]
		self._DesignParameter['bot_nmos_via23']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureX(**dict(_ViaMet22Met3NumberOfCOX=1, _ViaMet22Met3NumberOfCOY=bot_nmos_via_num))
		self._DesignParameter['bot_nmos_via23']['_XYCoordinates'] = XYList
		XYList = []
		xy_offset = [0, 0]
		for i in range(len(self._DesignParameter['bot_nmos_via12']['_XYCoordinates'])):
		    xy = (self._DesignParameter['bot_nmos_via12']['_XYCoordinates'][i][0] if (type(self._DesignParameter['bot_nmos_via12']['_XYCoordinates'][i][0]) == list) else self._DesignParameter['bot_nmos_via12']['_XYCoordinates'][i])
		    XYList.append([((x + y) + z) for (x, y, z) in zip([0, 0], xy, xy_offset)])
		self._DesignParameter['bot_nmos_via34'] = self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_Name='bot_nmos_via34In{}'.format(_Name)))[0]
		self._DesignParameter['bot_nmos_via34']['_DesignObj']._CalculateViaMet32Met4DesignParameterMinimumEnclosureX(**dict(_ViaMet32Met4NumberOfCOX=1, _ViaMet32Met4NumberOfCOY=bot_nmos_via_num))
		self._DesignParameter['bot_nmos_via34']['_XYCoordinates'] = XYList
		self._DesignParameter['METAL4_path_14'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL4'][0], _Datatype=DesignParameters._LayerMapping['METAL4'][1], _Width=drc._MetalxMinWidth)
		self._DesignParameter['METAL4_path_14']['_XYCoordinates'] = [[[(+ self._DesignParameter['bot_nmos_via34']['_XYCoordinates'][0][0]), (+ self._DesignParameter['bot_nmos_via34']['_XYCoordinates'][0][1])], [(+ self._DesignParameter['bot_nmos_via34']['_XYCoordinates'][(- 1)][0]), (+ self._DesignParameter['bot_nmos_via34']['_XYCoordinates'][(- 1)][1])]]]
		self._DesignParameter['bot_mos_gate_via'] = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_Name='bot_mos_gate_viaIn{}'.format(_Name)))[0]
		self._DesignParameter['bot_mos_gate_via']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(**dict(_ViaPoly2Met1NumberOfCOX=int(((((((self._DesignParameter['nmos_bot']['_XYCoordinates'][0][0] + self._DesignParameter['nmos_bot']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]) + (self._DesignParameter['nmos_bot']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)) - ((self._DesignParameter['nmos_bot']['_XYCoordinates'][0][0] + self._DesignParameter['nmos_bot']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['nmos_bot']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2))) - drc._CoMinSpace) - (2 * drc._CoMinEnclosureByPO)) / (drc._CoMinWidth + drc._CoMinSpace))), _ViaPoly2Met1NumberOfCOY=1))
		self._DesignParameter['bot_mos_gate_via']['_XYCoordinates'] = [[self._DesignParameter['nmos_bot']['_XYCoordinates'][0][0], ((self._DesignParameter['bot_mos_gate_via']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2) + (((self._DesignParameter['nmos_bot']['_XYCoordinates'][0][1] + self._DesignParameter['nmos_bot']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) + (self._DesignParameter['nmos_bot']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)) + drc._Metal1MinSpace2))]]
		self._DesignParameter['POLY_path_65'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _Width=self._DesignParameter['bot_mos_gate_via']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'])
		self._DesignParameter['POLY_path_65']['_XYCoordinates'] = [[[((self._DesignParameter['nmos_bot']['_XYCoordinates'][0][0] + self._DesignParameter['nmos_bot']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['nmos_bot']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)), self._DesignParameter['bot_mos_gate_via']['_XYCoordinates'][0][1]], [((self._DesignParameter['nmos_bot']['_XYCoordinates'][0][0] + self._DesignParameter['nmos_bot']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]) + (self._DesignParameter['nmos_bot']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)), self._DesignParameter['bot_mos_gate_via']['_XYCoordinates'][0][1]]]]
		self._DesignParameter['M1V1M2_bot_nmos_gate'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='M1V1M2_bot_nmos_gateIn{}'.format(_Name)))[0]
		self._DesignParameter['M1V1M2_bot_nmos_gate']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureY(**dict(_ViaMet12Met2NumberOfCOX=int(((((((self._DesignParameter['nmos_bot']['_XYCoordinates'][0][0] + self._DesignParameter['nmos_bot']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]) + (self._DesignParameter['nmos_bot']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)) - ((self._DesignParameter['nmos_bot']['_XYCoordinates'][0][0] + self._DesignParameter['nmos_bot']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['nmos_bot']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2))) - drc._VIAxMinSpace) - (drc._VIAxMinEnclosureByMetx * 2)) / (drc._VIAxMinWidth + drc._VIAxMinSpace))), _ViaMet12Met2NumberOfCOY=1))
		self._DesignParameter['M1V1M2_bot_nmos_gate']['_XYCoordinates'] = [[(+ self._DesignParameter['bot_mos_gate_via']['_XYCoordinates'][0][0]), (+ self._DesignParameter['bot_mos_gate_via']['_XYCoordinates'][0][1])]]
		self._DesignParameter['M2V2M3_bot_nmos_gate'] = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_Name='M2V2M3_bot_nmos_gateIn{}'.format(_Name)))[0]
		self._DesignParameter['M2V2M3_bot_nmos_gate']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureY(**dict(_ViaMet22Met3NumberOfCOX=int(((((((self._DesignParameter['nmos_bot']['_XYCoordinates'][0][0] + self._DesignParameter['nmos_bot']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]) + (self._DesignParameter['nmos_bot']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)) - ((self._DesignParameter['nmos_bot']['_XYCoordinates'][0][0] + self._DesignParameter['nmos_bot']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['nmos_bot']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2))) - drc._VIAxMinSpace) - (drc._VIAxMinEnclosureByMetx * 2)) / (drc._VIAxMinWidth + drc._VIAxMinSpace))), _ViaMet22Met3NumberOfCOY=1))
		self._DesignParameter['M2V2M3_bot_nmos_gate']['_XYCoordinates'] = [[(+ self._DesignParameter['bot_mos_gate_via']['_XYCoordinates'][0][0]), (+ self._DesignParameter['bot_mos_gate_via']['_XYCoordinates'][0][1])]]
		path_list = []
		if (len(self._DesignParameter['nmos_bot']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates']) == 1):
		    mode = 'vertical'
		    _width = self._DesignParameter['nmos_bot']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
		elif (self._DesignParameter['nmos_bot']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0] == self._DesignParameter['nmos_bot']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]):
		    mode = 'horizontal'
		    _width = self._DesignParameter['nmos_bot']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
		elif (self._DesignParameter['nmos_bot']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1] == self._DesignParameter['nmos_bot']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][1]):
		    mode = 'vertical'
		    _width = self._DesignParameter['nmos_bot']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
		else:
		    print('Invalid Target Input')
		if (mode == 'vertical'):
		    xy_with_offset = []
		    target_y_value = (0 + self._DesignParameter['bot_mos_gate_via']['_XYCoordinates'][0][1])
		    for i in range(len(self._DesignParameter['nmos_bot']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
		        xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['nmos_bot']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['nmos_bot']['_XYCoordinates'][0][1])], self._DesignParameter['nmos_bot']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		elif (mode == 'horizontal'):
		    xy_with_offset = []
		    target_x_value = (0 + self._DesignParameter['bot_mos_gate_via']['_XYCoordinates'][0][0])
		    for i in range(len(self._DesignParameter['nmos_bot']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
		        xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['nmos_bot']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['nmos_bot']['_XYCoordinates'][0][1])], self._DesignParameter['nmos_bot']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		self._DesignParameter['bot_nmos_poly'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _Width=_width)
		self._DesignParameter['bot_nmos_poly']['_XYCoordinates'] = path_list
		self._DesignParameter['METAL1_boundary_355'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _XWidth=(max(((self._DesignParameter['bot_mos_gate_via']['_XYCoordinates'][0][0] + self._DesignParameter['bot_mos_gate_via']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0]) + (self._DesignParameter['bot_mos_gate_via']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] / 2)), ((self._DesignParameter['M1V1M2_bot_nmos_gate']['_XYCoordinates'][0][0] + self._DesignParameter['M1V1M2_bot_nmos_gate']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0]) + (self._DesignParameter['M1V1M2_bot_nmos_gate']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] / 2))) - min(((self._DesignParameter['bot_mos_gate_via']['_XYCoordinates'][0][0] + self._DesignParameter['bot_mos_gate_via']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0]) - (self._DesignParameter['bot_mos_gate_via']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] / 2)), ((self._DesignParameter['M1V1M2_bot_nmos_gate']['_XYCoordinates'][0][0] + self._DesignParameter['M1V1M2_bot_nmos_gate']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0]) - (self._DesignParameter['M1V1M2_bot_nmos_gate']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] / 2)))), _YWidth=(max(((self._DesignParameter['M1V1M2_bot_nmos_gate']['_XYCoordinates'][0][1] + self._DesignParameter['M1V1M2_bot_nmos_gate']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) + (self._DesignParameter['M1V1M2_bot_nmos_gate']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)), ((self._DesignParameter['bot_mos_gate_via']['_XYCoordinates'][0][1] + self._DesignParameter['bot_mos_gate_via']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) + (self._DesignParameter['bot_mos_gate_via']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2))) - min(((self._DesignParameter['bot_mos_gate_via']['_XYCoordinates'][0][1] + self._DesignParameter['bot_mos_gate_via']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) - (self._DesignParameter['bot_mos_gate_via']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)), ((self._DesignParameter['M1V1M2_bot_nmos_gate']['_XYCoordinates'][0][1] + self._DesignParameter['M1V1M2_bot_nmos_gate']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) - (self._DesignParameter['M1V1M2_bot_nmos_gate']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)))))
		self._DesignParameter['METAL1_boundary_355']['_XYCoordinates'] = [[(+ self._DesignParameter['M2V2M3_bot_nmos_gate']['_XYCoordinates'][0][0]), (+ self._DesignParameter['M2V2M3_bot_nmos_gate']['_XYCoordinates'][0][1])]]
		self._DesignParameter['METAL3_path_27'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0], _Datatype=DesignParameters._LayerMapping['METAL3'][1], _Width=drc._MetalxMinWidth)
		self._DesignParameter['METAL3_path_27']['_XYCoordinates'] = [[[(+ self._DesignParameter['bot_nmos_via34']['_XYCoordinates'][0][0]), (+ self._DesignParameter['bot_nmos_via34']['_XYCoordinates'][0][1])], [(+ self._DesignParameter['bot_nmos_via34']['_XYCoordinates'][(- 1)][0]), (+ self._DesignParameter['bot_nmos_via34']['_XYCoordinates'][(- 1)][1])]]]
		self._DesignParameter['METAL2_path_30'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _Width=drc._MetalxMinWidth)
		self._DesignParameter['METAL2_path_30']['_XYCoordinates'] = [[[(+ self._DesignParameter['bot_nmos_via34']['_XYCoordinates'][0][0]), (+ self._DesignParameter['bot_nmos_via34']['_XYCoordinates'][0][1])], [(+ self._DesignParameter['bot_nmos_via34']['_XYCoordinates'][(- 1)][0]), (+ self._DesignParameter['bot_nmos_via34']['_XYCoordinates'][(- 1)][1])]]]
		self._DesignParameter['mid_nmos_left'] = self._SrefElementDeclaration(_DesignObj=NMOSWithDummy._NMOS(_Name='mid_nmos_leftIn{}'.format(_Name)))[0]
		self._DesignParameter['mid_nmos_left']['_DesignObj']._CalculateNMOSDesignParameter(**dict(_NMOSNumberofGate=2, _NMOSChannelWidth=nmos_fwidth, _NMOSChannellength=30, _NMOSDummy=True, _GateSpacing=None, _XVT='SLVT'))
		self._DesignParameter['mid_nmos_left']['_XYCoordinates'] = [[int(((self._DesignParameter['nmos_bot']['_XYCoordinates'][0][0] - (self._DesignParameter['mid_nmos_left']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][(- 1)][0] + (self._DesignParameter['mid_nmos_left']['_DesignObj']._DesignParameter['_PODummyLayer']['_XWidth'] / 2))) - (gate_spacing / 2))), int((((((((self._DesignParameter['METAL1_boundary_355']['_XYCoordinates'][0][1] + (self._DesignParameter['METAL1_boundary_355']['_YWidth'] / 2)) + drc._Metal1MinSpace) + (input_via_y * (drc._CoMinWidth + drc._CoMinSpace))) - drc._CoMinSpace) + (2 * drc._CoMinEnclosureByPO)) + drc._PolygateMinSpace) + (self._DesignParameter['mid_nmos_left']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2)))]]
		self._DesignParameter['mid_nmos_right'] = self._SrefElementDeclaration(_DesignObj=NMOSWithDummy._NMOS(_Name='mid_nmos_rightIn{}'.format(_Name)))[0]
		self._DesignParameter['mid_nmos_right']['_DesignObj']._CalculateNMOSDesignParameter(**dict(_NMOSNumberofGate=2, _NMOSChannelWidth=nmos_fwidth, _NMOSChannellength=30, _NMOSDummy=True, _GateSpacing=None, _XVT='SLVT'))
		self._DesignParameter['mid_nmos_right']['_XYCoordinates'] = [[int(((self._DesignParameter['nmos_bot']['_XYCoordinates'][0][0] - (self._DesignParameter['mid_nmos_right']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][0] - (self._DesignParameter['mid_nmos_right']['_DesignObj']._DesignParameter['_PODummyLayer']['_XWidth'] / 2))) + (gate_spacing / 2))), int((((((((self._DesignParameter['METAL1_boundary_355']['_XYCoordinates'][0][1] + (self._DesignParameter['METAL1_boundary_355']['_YWidth'] / 2)) + drc._Metal1MinSpace) + (input_via_y * (drc._CoMinWidth + drc._CoMinSpace))) - drc._CoMinSpace) + (2 * drc._CoMinEnclosureByPO)) + drc._PolygateMinSpace) + (self._DesignParameter['mid_nmos_left']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2)))]]
		num_of_mid_nmos_via = max(1, (1 + int((((self._DesignParameter['mid_nmos_left']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] - drc._VIAxMinSpace) - (2 * drc._VIAxMinEnclosureByMetx)) / (drc._VIAxMinWidth + drc._VIAxMinSpace)))))
		XYList = []
		xy_offset = (0, int(((drc._VIAxMinWidth + drc._VIAxMinSpace) / 4)))
		for i in range(len(self._DesignParameter['mid_nmos_left']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'])):
		    if ((i % 2) == 1):
		        xy = (self._DesignParameter['mid_nmos_left']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i][0] if (type(self._DesignParameter['mid_nmos_left']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i][0]) == list) else self._DesignParameter['mid_nmos_left']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i])
		        XYList.append([((x + y) + z) for (x, y, z) in zip([(0 + self._DesignParameter['mid_nmos_left']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['mid_nmos_left']['_XYCoordinates'][0][1])], xy, xy_offset)])
		self._DesignParameter['mid_nmos_left_via'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='mid_nmos_left_viaIn{}'.format(_Name)))[0]
		self._DesignParameter['mid_nmos_left_via']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(**dict(_ViaMet12Met2NumberOfCOX=1, _ViaMet12Met2NumberOfCOY=num_of_mid_nmos_via))
		self._DesignParameter['mid_nmos_left_via']['_XYCoordinates'] = XYList
		XYList = []
		xy_offset = (0, ((drc._VIAxMinWidth + drc._VIAxMinSpace) / 4))
		for i in range(len(self._DesignParameter['mid_nmos_right']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'])):
		    if ((i % 2) == 1):
		        xy = (self._DesignParameter['mid_nmos_right']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i][0] if (type(self._DesignParameter['mid_nmos_right']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i][0]) == list) else self._DesignParameter['mid_nmos_right']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i])
		        XYList.append([((x + y) + z) for (x, y, z) in zip([(0 + self._DesignParameter['mid_nmos_right']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['mid_nmos_right']['_XYCoordinates'][0][1])], xy, xy_offset)])
		self._DesignParameter['min_nmos_right_via'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='min_nmos_right_viaIn{}'.format(_Name)))[0]
		self._DesignParameter['min_nmos_right_via']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(**dict(_ViaMet12Met2NumberOfCOX=1, _ViaMet12Met2NumberOfCOY=num_of_mid_nmos_via))
		self._DesignParameter['min_nmos_right_via']['_XYCoordinates'] = XYList
		self._DesignParameter['PCCAM1_mid_nmos_left'] = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_Name='PCCAM1_mid_nmos_leftIn{}'.format(_Name)))[0]
		self._DesignParameter['PCCAM1_mid_nmos_left']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(**dict(_ViaPoly2Met1NumberOfCOX=int((len(self._DesignParameter['mid_nmos_left']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates']) - 1)), _ViaPoly2Met1NumberOfCOY=1))
		self._DesignParameter['PCCAM1_mid_nmos_left']['_XYCoordinates'] = [[self._DesignParameter['mid_nmos_left']['_XYCoordinates'][0][0], ((((self._DesignParameter['mid_nmos_left']['_XYCoordinates'][0][1] + self._DesignParameter['mid_nmos_left']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) + (self._DesignParameter['mid_nmos_left']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)) + drc._Metal1MinSpace2) + (self._DesignParameter['PCCAM1_mid_nmos_left']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2))]]
		self._DesignParameter['PCCAM1_mid_nmos_right'] = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_Name='PCCAM1_mid_nmos_rightIn{}'.format(_Name)))[0]
		self._DesignParameter['PCCAM1_mid_nmos_right']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(**dict(_ViaPoly2Met1NumberOfCOX=int((len(self._DesignParameter['mid_nmos_left']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates']) - 1)), _ViaPoly2Met1NumberOfCOY=1))
		self._DesignParameter['PCCAM1_mid_nmos_right']['_XYCoordinates'] = [[self._DesignParameter['mid_nmos_right']['_XYCoordinates'][0][0], ((((self._DesignParameter['mid_nmos_left']['_XYCoordinates'][0][1] + self._DesignParameter['mid_nmos_left']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) + (self._DesignParameter['mid_nmos_left']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)) + drc._Metal1MinSpace2) + (self._DesignParameter['PCCAM1_mid_nmos_left']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2))]]
		self._DesignParameter['M1V1M2_mid_mos_left'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='M1V1M2_mid_mos_leftIn{}'.format(_Name)))[0]
		self._DesignParameter['M1V1M2_mid_mos_left']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(**dict(_ViaMet12Met2NumberOfCOX=1, _ViaMet12Met2NumberOfCOY=max(1, (1 + int((((self._DesignParameter['mid_nmos_left']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] - drc._VIAxMinSpace) - (2 * drc._VIAxMinEnclosureByMetx)) / (drc._VIAxMinWidth + drc._VIAxMinSpace)))))))
		self._DesignParameter['M1V1M2_mid_mos_left']['_XYCoordinates'] = [[(+ (self._DesignParameter['mid_nmos_left']['_XYCoordinates'][0][0] + self._DesignParameter['mid_nmos_left']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][(- 1)][0])), ((- int(((drc._VIAxMinWidth + drc._VIAxMinSpace) / 4))) + (self._DesignParameter['mid_nmos_left']['_XYCoordinates'][0][1] + self._DesignParameter['mid_nmos_left']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][(- 1)][1]))]]
		self._DesignParameter['M2V2M3_mid_mos_left'] = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_Name='M2V2M3_mid_mos_leftIn{}'.format(_Name)))[0]
		self._DesignParameter['M2V2M3_mid_mos_left']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureX(**dict(_ViaMet22Met3NumberOfCOX=1, _ViaMet22Met3NumberOfCOY=max(1, (1 + int((((self._DesignParameter['mid_nmos_left']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] - drc._VIAxMinSpace) - (2 * drc._VIAxMinEnclosureByMetx)) / (drc._VIAxMinWidth + drc._VIAxMinSpace)))))))
		self._DesignParameter['M2V2M3_mid_mos_left']['_XYCoordinates'] = [[(+ (self._DesignParameter['mid_nmos_left']['_XYCoordinates'][0][0] + self._DesignParameter['mid_nmos_left']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][(- 1)][0])), ((- int(((drc._VIAxMinWidth + drc._VIAxMinSpace) / 4))) + (self._DesignParameter['mid_nmos_left']['_XYCoordinates'][0][1] + self._DesignParameter['mid_nmos_left']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][(- 1)][1]))]]
		self._DesignParameter['M3V3M4_mid_mod_left'] = self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_Name='M3V3M4_mid_mod_leftIn{}'.format(_Name)))[0]
		self._DesignParameter['M3V3M4_mid_mod_left']['_DesignObj']._CalculateViaMet32Met4DesignParameterMinimumEnclosureX(**dict(_ViaMet32Met4NumberOfCOX=1, _ViaMet32Met4NumberOfCOY=max(1, (1 + int((((self._DesignParameter['mid_nmos_left']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] - drc._VIAxMinSpace) - (2 * drc._VIAxMinEnclosureByMetx)) / (drc._VIAxMinWidth + drc._VIAxMinSpace)))))))
		self._DesignParameter['M3V3M4_mid_mod_left']['_XYCoordinates'] = [[(+ (self._DesignParameter['mid_nmos_left']['_XYCoordinates'][0][0] + self._DesignParameter['mid_nmos_left']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][(- 1)][0])), ((- int(((drc._VIAxMinWidth + drc._VIAxMinSpace) / 4))) + (self._DesignParameter['mid_nmos_left']['_XYCoordinates'][0][1] + self._DesignParameter['mid_nmos_left']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][(- 1)][1]))]]
		self._DesignParameter['M1V1M2_mid_mos_right'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='M1V1M2_mid_mos_rightIn{}'.format(_Name)))[0]
		self._DesignParameter['M1V1M2_mid_mos_right']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(**dict(_ViaMet12Met2NumberOfCOX=1, _ViaMet12Met2NumberOfCOY=max(1, (1 + int((((self._DesignParameter['mid_nmos_right']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] - drc._VIAxMinSpace) - (2 * drc._VIAxMinEnclosureByMetx)) / (drc._VIAxMinWidth + drc._VIAxMinSpace)))))))
		self._DesignParameter['M1V1M2_mid_mos_right']['_XYCoordinates'] = [[(+ (self._DesignParameter['mid_nmos_right']['_XYCoordinates'][0][0] + self._DesignParameter['mid_nmos_right']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0])), ((- int(((drc._VIAxMinWidth + drc._VIAxMinSpace) / 4))) + (self._DesignParameter['mid_nmos_right']['_XYCoordinates'][0][1] + self._DesignParameter['mid_nmos_right']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]))]]
		self._DesignParameter['M2V2M3_mid_mos_right'] = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_Name='M2V2M3_mid_mos_rightIn{}'.format(_Name)))[0]
		self._DesignParameter['M2V2M3_mid_mos_right']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureX(**dict(_ViaMet22Met3NumberOfCOX=1, _ViaMet22Met3NumberOfCOY=max(1, (1 + int((((self._DesignParameter['mid_nmos_right']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] - drc._VIAxMinSpace) - (2 * drc._VIAxMinEnclosureByMetx)) / (drc._VIAxMinWidth + drc._VIAxMinSpace)))))))
		self._DesignParameter['M2V2M3_mid_mos_right']['_XYCoordinates'] = [[(+ (self._DesignParameter['mid_nmos_right']['_XYCoordinates'][0][0] + self._DesignParameter['mid_nmos_right']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0])), ((- int(((drc._VIAxMinWidth + drc._VIAxMinSpace) / 4))) + (self._DesignParameter['mid_nmos_right']['_XYCoordinates'][0][1] + self._DesignParameter['mid_nmos_right']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]))]]
		self._DesignParameter['M3V3M4_mid_mos_right'] = self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_Name='M3V3M4_mid_mos_rightIn{}'.format(_Name)))[0]
		self._DesignParameter['M3V3M4_mid_mos_right']['_DesignObj']._CalculateViaMet32Met4DesignParameterMinimumEnclosureX(**dict(_ViaMet32Met4NumberOfCOX=1, _ViaMet32Met4NumberOfCOY=max(1, (1 + int((((self._DesignParameter['mid_nmos_right']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] - drc._VIAxMinSpace) - (2 * drc._VIAxMinEnclosureByMetx)) / (drc._VIAxMinWidth + drc._VIAxMinSpace)))))))
		self._DesignParameter['M3V3M4_mid_mos_right']['_XYCoordinates'] = [[(+ (self._DesignParameter['mid_nmos_right']['_XYCoordinates'][0][0] + self._DesignParameter['mid_nmos_right']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0])), ((- int(((drc._VIAxMinWidth + drc._VIAxMinSpace) / 4))) + (self._DesignParameter['mid_nmos_right']['_XYCoordinates'][0][1] + self._DesignParameter['mid_nmos_right']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]))]]
		self._DesignParameter['M1V1M2_mid_mos_left_gate'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='M1V1M2_mid_mos_left_gateIn{}'.format(_Name)))[0]
		self._DesignParameter['M1V1M2_mid_mos_left_gate']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureY(**dict(_ViaMet12Met2NumberOfCOX=2, _ViaMet12Met2NumberOfCOY=1))
		self._DesignParameter['M1V1M2_mid_mos_left_gate']['_XYCoordinates'] = [[self._DesignParameter['mid_nmos_left']['_XYCoordinates'][0][0], ((((self._DesignParameter['PCCAM1_mid_nmos_left']['_XYCoordinates'][0][1] + self._DesignParameter['PCCAM1_mid_nmos_left']['_DesignObj']._DesignParameter['_COLayer']['_XYCoordinates'][0][1]) + (self._DesignParameter['PCCAM1_mid_nmos_left']['_DesignObj']._DesignParameter['_COLayer']['_YWidth'] / 2)) + drc._MetalxMinSpace2) + (self._DesignParameter['M1V1M2_mid_mos_left_gate']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] / 2))]]
		self._DesignParameter['METAL1_boundary_354'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _XWidth=(max(((self._DesignParameter['M1V1M2_mid_mos_left_gate']['_XYCoordinates'][0][0] + self._DesignParameter['M1V1M2_mid_mos_left_gate']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0]) + (self._DesignParameter['M1V1M2_mid_mos_left_gate']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] / 2)), ((self._DesignParameter['PCCAM1_mid_nmos_left']['_XYCoordinates'][0][0] + self._DesignParameter['PCCAM1_mid_nmos_left']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0]) + (self._DesignParameter['PCCAM1_mid_nmos_left']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] / 2))) - min(((self._DesignParameter['PCCAM1_mid_nmos_left']['_XYCoordinates'][0][0] + self._DesignParameter['PCCAM1_mid_nmos_left']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0]) - (self._DesignParameter['PCCAM1_mid_nmos_left']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] / 2)), ((self._DesignParameter['M1V1M2_mid_mos_left_gate']['_XYCoordinates'][0][0] + self._DesignParameter['M1V1M2_mid_mos_left_gate']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0]) - (self._DesignParameter['M1V1M2_mid_mos_left_gate']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] / 2)))), _YWidth=(max(((self._DesignParameter['PCCAM1_mid_nmos_left']['_XYCoordinates'][0][1] + self._DesignParameter['PCCAM1_mid_nmos_left']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) + (self._DesignParameter['PCCAM1_mid_nmos_left']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)), ((self._DesignParameter['M1V1M2_mid_mos_left_gate']['_XYCoordinates'][0][1] + self._DesignParameter['M1V1M2_mid_mos_left_gate']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) + (self._DesignParameter['M1V1M2_mid_mos_left_gate']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2))) - min(((self._DesignParameter['M1V1M2_mid_mos_left_gate']['_XYCoordinates'][0][1] + self._DesignParameter['M1V1M2_mid_mos_left_gate']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) - (self._DesignParameter['M1V1M2_mid_mos_left_gate']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)), ((self._DesignParameter['PCCAM1_mid_nmos_left']['_XYCoordinates'][0][1] + self._DesignParameter['PCCAM1_mid_nmos_left']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) - (self._DesignParameter['PCCAM1_mid_nmos_left']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)))))
		self._DesignParameter['METAL1_boundary_354']['_XYCoordinates'] = [[int(((max(((self._DesignParameter['M1V1M2_mid_mos_left_gate']['_XYCoordinates'][0][0] + self._DesignParameter['M1V1M2_mid_mos_left_gate']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0]) + (self._DesignParameter['M1V1M2_mid_mos_left_gate']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] / 2)), ((self._DesignParameter['PCCAM1_mid_nmos_left']['_XYCoordinates'][0][0] + self._DesignParameter['PCCAM1_mid_nmos_left']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0]) + (self._DesignParameter['PCCAM1_mid_nmos_left']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] / 2))) + min(((self._DesignParameter['PCCAM1_mid_nmos_left']['_XYCoordinates'][0][0] + self._DesignParameter['PCCAM1_mid_nmos_left']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0]) - (self._DesignParameter['PCCAM1_mid_nmos_left']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] / 2)), ((self._DesignParameter['M1V1M2_mid_mos_left_gate']['_XYCoordinates'][0][0] + self._DesignParameter['M1V1M2_mid_mos_left_gate']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0]) - (self._DesignParameter['M1V1M2_mid_mos_left_gate']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] / 2)))) / 2)), int(((max(((self._DesignParameter['PCCAM1_mid_nmos_left']['_XYCoordinates'][0][1] + self._DesignParameter['PCCAM1_mid_nmos_left']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) + (self._DesignParameter['PCCAM1_mid_nmos_left']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)), ((self._DesignParameter['M1V1M2_mid_mos_left_gate']['_XYCoordinates'][0][1] + self._DesignParameter['M1V1M2_mid_mos_left_gate']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) + (self._DesignParameter['M1V1M2_mid_mos_left_gate']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2))) + min(((self._DesignParameter['M1V1M2_mid_mos_left_gate']['_XYCoordinates'][0][1] + self._DesignParameter['M1V1M2_mid_mos_left_gate']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) - (self._DesignParameter['M1V1M2_mid_mos_left_gate']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)), ((self._DesignParameter['PCCAM1_mid_nmos_left']['_XYCoordinates'][0][1] + self._DesignParameter['PCCAM1_mid_nmos_left']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) - (self._DesignParameter['PCCAM1_mid_nmos_left']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)))) / 2))]]
		self._DesignParameter['M1V1M2_mid_mos_right_gate'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='M1V1M2_mid_mos_right_gateIn{}'.format(_Name)))[0]
		self._DesignParameter['M1V1M2_mid_mos_right_gate']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureY(**dict(_ViaMet12Met2NumberOfCOX=2, _ViaMet12Met2NumberOfCOY=1))
		self._DesignParameter['M1V1M2_mid_mos_right_gate']['_XYCoordinates'] = [[self._DesignParameter['PCCAM1_mid_nmos_right']['_XYCoordinates'][0][0], self._DesignParameter['M1V1M2_mid_mos_left_gate']['_XYCoordinates'][0][1]]]
		self._DesignParameter['METAL1_boundary_353'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _XWidth=(max(((self._DesignParameter['PCCAM1_mid_nmos_right']['_XYCoordinates'][0][0] + self._DesignParameter['PCCAM1_mid_nmos_right']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0]) + (self._DesignParameter['PCCAM1_mid_nmos_right']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] / 2)), ((self._DesignParameter['M1V1M2_mid_mos_right_gate']['_XYCoordinates'][0][0] + self._DesignParameter['M1V1M2_mid_mos_right_gate']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0]) + (self._DesignParameter['M1V1M2_mid_mos_right_gate']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] / 2))) - min(((self._DesignParameter['M1V1M2_mid_mos_right_gate']['_XYCoordinates'][0][0] + self._DesignParameter['M1V1M2_mid_mos_right_gate']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0]) - (self._DesignParameter['M1V1M2_mid_mos_right_gate']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] / 2)), ((self._DesignParameter['PCCAM1_mid_nmos_right']['_XYCoordinates'][0][0] + self._DesignParameter['PCCAM1_mid_nmos_right']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0]) - (self._DesignParameter['PCCAM1_mid_nmos_right']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] / 2)))), _YWidth=(max(((self._DesignParameter['M1V1M2_mid_mos_right_gate']['_XYCoordinates'][0][1] + self._DesignParameter['M1V1M2_mid_mos_right_gate']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) + (self._DesignParameter['M1V1M2_mid_mos_right_gate']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)), ((self._DesignParameter['PCCAM1_mid_nmos_right']['_XYCoordinates'][0][1] + self._DesignParameter['PCCAM1_mid_nmos_right']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) + (self._DesignParameter['PCCAM1_mid_nmos_right']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2))) - min(((self._DesignParameter['PCCAM1_mid_nmos_right']['_XYCoordinates'][0][1] + self._DesignParameter['PCCAM1_mid_nmos_right']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) - (self._DesignParameter['PCCAM1_mid_nmos_right']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)), ((self._DesignParameter['M1V1M2_mid_mos_right_gate']['_XYCoordinates'][0][1] + self._DesignParameter['M1V1M2_mid_mos_right_gate']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) - (self._DesignParameter['M1V1M2_mid_mos_right_gate']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)))))
		self._DesignParameter['METAL1_boundary_353']['_XYCoordinates'] = [[int(((max(((self._DesignParameter['PCCAM1_mid_nmos_right']['_XYCoordinates'][0][0] + self._DesignParameter['PCCAM1_mid_nmos_right']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0]) + (self._DesignParameter['PCCAM1_mid_nmos_right']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] / 2)), ((self._DesignParameter['M1V1M2_mid_mos_right_gate']['_XYCoordinates'][0][0] + self._DesignParameter['M1V1M2_mid_mos_right_gate']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0]) + (self._DesignParameter['M1V1M2_mid_mos_right_gate']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] / 2))) + min(((self._DesignParameter['M1V1M2_mid_mos_right_gate']['_XYCoordinates'][0][0] + self._DesignParameter['M1V1M2_mid_mos_right_gate']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0]) - (self._DesignParameter['M1V1M2_mid_mos_right_gate']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] / 2)), ((self._DesignParameter['PCCAM1_mid_nmos_right']['_XYCoordinates'][0][0] + self._DesignParameter['PCCAM1_mid_nmos_right']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0]) - (self._DesignParameter['PCCAM1_mid_nmos_right']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] / 2)))) / 2)), int(((max(((self._DesignParameter['M1V1M2_mid_mos_right_gate']['_XYCoordinates'][0][1] + self._DesignParameter['M1V1M2_mid_mos_right_gate']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) + (self._DesignParameter['M1V1M2_mid_mos_right_gate']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)), ((self._DesignParameter['PCCAM1_mid_nmos_right']['_XYCoordinates'][0][1] + self._DesignParameter['PCCAM1_mid_nmos_right']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) + (self._DesignParameter['PCCAM1_mid_nmos_right']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2))) + min(((self._DesignParameter['PCCAM1_mid_nmos_right']['_XYCoordinates'][0][1] + self._DesignParameter['PCCAM1_mid_nmos_right']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) - (self._DesignParameter['PCCAM1_mid_nmos_right']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)), ((self._DesignParameter['M1V1M2_mid_mos_right_gate']['_XYCoordinates'][0][1] + self._DesignParameter['M1V1M2_mid_mos_right_gate']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) - (self._DesignParameter['M1V1M2_mid_mos_right_gate']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)))) / 2))]]
		path_list = []
		if (len(self._DesignParameter['mid_nmos_left']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates']) == 1):
		    mode = 'vertical'
		    _width = self._DesignParameter['mid_nmos_left']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
		elif (self._DesignParameter['mid_nmos_left']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0] == self._DesignParameter['mid_nmos_left']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]):
		    mode = 'horizontal'
		    _width = self._DesignParameter['mid_nmos_left']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
		elif (self._DesignParameter['mid_nmos_left']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1] == self._DesignParameter['mid_nmos_left']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][1]):
		    mode = 'vertical'
		    _width = self._DesignParameter['mid_nmos_left']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
		else:
		    print('Invalid Target Input')
		if (mode == 'vertical'):
		    xy_with_offset = []
		    target_y_value = (0 + self._DesignParameter['PCCAM1_mid_nmos_left']['_XYCoordinates'][0][1])
		    for i in range(len(self._DesignParameter['mid_nmos_left']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
		        xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['mid_nmos_left']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['mid_nmos_left']['_XYCoordinates'][0][1])], self._DesignParameter['mid_nmos_left']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		elif (mode == 'horizontal'):
		    xy_with_offset = []
		    target_x_value = (0 + self._DesignParameter['PCCAM1_mid_nmos_left']['_XYCoordinates'][0][0])
		    for i in range(len(self._DesignParameter['mid_nmos_left']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
		        xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['mid_nmos_left']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['mid_nmos_left']['_XYCoordinates'][0][1])], self._DesignParameter['mid_nmos_left']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		self._DesignParameter['mid_mos_left_gate_array'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _Width=_width)
		self._DesignParameter['mid_mos_left_gate_array']['_XYCoordinates'] = path_list
		self._DesignParameter['POLY_path_63'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _Width=int(self._DesignParameter['PCCAM1_mid_nmos_left']['_DesignObj']._DesignParameter['_POLayer']['_YWidth']))
		self._DesignParameter['POLY_path_63']['_XYCoordinates'] = [[[(self._DesignParameter['mid_mos_left_gate_array']['_XYCoordinates'][0][0][0] - (self._DesignParameter['mid_mos_left_gate_array']['_Width'] / 2)), self._DesignParameter['PCCAM1_mid_nmos_left']['_XYCoordinates'][0][1]], [(self._DesignParameter['mid_mos_left_gate_array']['_XYCoordinates'][(- 1)][0][0] + (self._DesignParameter['mid_mos_left_gate_array']['_Width'] / 2)), self._DesignParameter['PCCAM1_mid_nmos_left']['_XYCoordinates'][0][1]]]]
		path_list = []
		if (len(self._DesignParameter['mid_nmos_right']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates']) == 1):
		    mode = 'vertical'
		    _width = self._DesignParameter['mid_nmos_right']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
		elif (self._DesignParameter['mid_nmos_right']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0] == self._DesignParameter['mid_nmos_right']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]):
		    mode = 'horizontal'
		    _width = self._DesignParameter['mid_nmos_right']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
		elif (self._DesignParameter['mid_nmos_right']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1] == self._DesignParameter['mid_nmos_right']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][1]):
		    mode = 'vertical'
		    _width = self._DesignParameter['mid_nmos_right']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
		else:
		    print('Invalid Target Input')
		if (mode == 'vertical'):
		    xy_with_offset = []
		    target_y_value = (0 + self._DesignParameter['PCCAM1_mid_nmos_right']['_XYCoordinates'][0][1])
		    for i in range(len(self._DesignParameter['mid_nmos_right']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
		        xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['mid_nmos_right']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['mid_nmos_right']['_XYCoordinates'][0][1])], self._DesignParameter['mid_nmos_right']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		elif (mode == 'horizontal'):
		    xy_with_offset = []
		    target_x_value = (0 + self._DesignParameter['PCCAM1_mid_nmos_right']['_XYCoordinates'][0][0])
		    for i in range(len(self._DesignParameter['mid_nmos_right']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
		        xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['mid_nmos_right']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['mid_nmos_right']['_XYCoordinates'][0][1])], self._DesignParameter['mid_nmos_right']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		self._DesignParameter['mid_mos_right_gate_array'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _Width=_width)
		self._DesignParameter['mid_mos_right_gate_array']['_XYCoordinates'] = path_list
		self._DesignParameter['POLY_path_66'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _Width=self._DesignParameter['PCCAM1_mid_nmos_right']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'])
		self._DesignParameter['POLY_path_66']['_XYCoordinates'] = [[[(self._DesignParameter['mid_mos_right_gate_array']['_XYCoordinates'][0][0][0] - (self._DesignParameter['mid_mos_right_gate_array']['_Width'] / 2)), self._DesignParameter['PCCAM1_mid_nmos_right']['_XYCoordinates'][0][1]], [(self._DesignParameter['mid_mos_right_gate_array']['_XYCoordinates'][(- 1)][0][0] + (self._DesignParameter['mid_mos_right_gate_array']['_Width'] / 2)), self._DesignParameter['PCCAM1_mid_nmos_right']['_XYCoordinates'][0][1]]]]
		self._DesignParameter['nmos_inp'] = self._SrefElementDeclaration(_DesignObj=NMOSWithDummy._NMOS(_Name='nmos_inpIn{}'.format(_Name)))[0]
		self._DesignParameter['nmos_inp']['_DesignObj']._CalculateNMOSDesignParameter(**dict(_NMOSNumberofGate=12, _NMOSChannelWidth=nmos_fwidth, _NMOSChannellength=30, _NMOSDummy=True, _GateSpacing=None, _XVT='SLVT'))
		self._DesignParameter['nmos_inp']['_XYCoordinates'] = [[((((self._DesignParameter['mid_nmos_left']['_XYCoordinates'][0][0] + self._DesignParameter['mid_nmos_left']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['mid_nmos_left']['_DesignObj']._DesignParameter['_PODummyLayer']['_XWidth'] / 2)) - (self._DesignParameter['nmos_inp']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][(- 1)][0] + (self._DesignParameter['nmos_inp']['_DesignObj']._DesignParameter['_PODummyLayer']['_XWidth'] / 2))) - drc._PolygateMinSpace), self._DesignParameter['mid_nmos_left']['_XYCoordinates'][0][1]]]
		num_of_inp_via = max(1, (1 + int((((self._DesignParameter['nmos_inp']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] - drc._VIAxMinSpace) - (2 * drc._VIAxMinEnclosureByMetx)) / (drc._VIAxMinWidth + drc._VIAxMinSpace)))))
		XYList = []
		xy_offset = (0, int(((drc._VIAxMinWidth + drc._VIAxMinSpace) / 4)))
		for i in range(len(self._DesignParameter['nmos_inp']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'])):
		    if ((i % 2) == 0):
		        xy = (self._DesignParameter['nmos_inp']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i][0] if (type(self._DesignParameter['nmos_inp']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i][0]) == list) else self._DesignParameter['nmos_inp']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i])
		        XYList.append([((x + y) + z) for (x, y, z) in zip([(0 + self._DesignParameter['nmos_inp']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['nmos_inp']['_XYCoordinates'][0][1])], xy, xy_offset)])
		self._DesignParameter['nmos_inp_drain_via'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='nmos_inp_drain_viaIn{}'.format(_Name)))[0]
		self._DesignParameter['nmos_inp_drain_via']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(**dict(_ViaMet12Met2NumberOfCOX=1, _ViaMet12Met2NumberOfCOY=num_of_inp_via))
		self._DesignParameter['nmos_inp_drain_via']['_XYCoordinates'] = XYList
		XYList = []
		xy_offset = (0, (- int(((drc._VIAxMinWidth + drc._VIAxMinSpace) / 4))))
		for i in range(len(self._DesignParameter['nmos_inp']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'])):
		    if ((i % 2) == 1):
		        xy = (self._DesignParameter['nmos_inp']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i][0] if (type(self._DesignParameter['nmos_inp']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i][0]) == list) else self._DesignParameter['nmos_inp']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i])
		        XYList.append([((x + y) + z) for (x, y, z) in zip([(0 + self._DesignParameter['nmos_inp']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['nmos_inp']['_XYCoordinates'][0][1])], xy, xy_offset)])
		self._DesignParameter['nmos_inp_source_via'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='nmos_inp_source_viaIn{}'.format(_Name)))[0]
		self._DesignParameter['nmos_inp_source_via']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(**dict(_ViaMet12Met2NumberOfCOX=1, _ViaMet12Met2NumberOfCOY=num_of_inp_via))
		self._DesignParameter['nmos_inp_source_via']['_XYCoordinates'] = XYList
		self._DesignParameter['M2V2M3_inp_mos_drain'] = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_Name='M2V2M3_inp_mos_drainIn{}'.format(_Name)))[0]
		self._DesignParameter['M2V2M3_inp_mos_drain']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureY(**dict(_ViaMet22Met3NumberOfCOX=max(1, (1 + int(((((((self._DesignParameter['nmos_inp']['_XYCoordinates'][0][0] + self._DesignParameter['nmos_inp']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][(- 1)][0]) + (self._DesignParameter['nmos_inp']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] / 2)) - ((self._DesignParameter['nmos_inp']['_XYCoordinates'][0][0] + self._DesignParameter['nmos_inp']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0]) - (self._DesignParameter['nmos_inp']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] / 2))) - drc._VIAxMinSpace) - (2 * drc._VIAxMinEnclosureByMetx)) / (drc._VIAxMinWidth + drc._VIAxMinSpace))))), _ViaMet22Met3NumberOfCOY=1))
		self._DesignParameter['M2V2M3_inp_mos_drain']['_XYCoordinates'] = [[self._DesignParameter['nmos_inp']['_XYCoordinates'][0][0], ((((self._DesignParameter['nmos_inp_drain_via']['_XYCoordinates'][0][1] + self._DesignParameter['nmos_inp_drain_via']['_DesignObj']._DesignParameter['_Met2Layer']['_XYCoordinates'][0][1]) + (self._DesignParameter['nmos_inp_drain_via']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] / 2)) + (self._DesignParameter['M2V2M3_inp_mos_drain']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] / 2)) + drc._VIAxMinSpace2)]]
		path_list = []
		if (len(self._DesignParameter['nmos_inp']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates']) == 1):
		    mode = 'vertical'
		    _width = self._DesignParameter['nmos_inp']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
		elif (self._DesignParameter['nmos_inp']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0] == self._DesignParameter['nmos_inp']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][(- 1)][0]):
		    mode = 'horizontal'
		    _width = self._DesignParameter['nmos_inp']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
		elif (self._DesignParameter['nmos_inp']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1] == self._DesignParameter['nmos_inp']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][(- 1)][1]):
		    mode = 'vertical'
		    _width = self._DesignParameter['nmos_inp']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
		else:
		    print('Invalid Target Input')
		if (mode == 'vertical'):
		    xy_with_offset = []
		    target_y_value = (0 + self._DesignParameter['M2V2M3_inp_mos_drain']['_XYCoordinates'][0][1])
		    for i in range(len(self._DesignParameter['nmos_inp']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'])):
		        if ((i % 2) == 0):
		            xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['nmos_inp']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['nmos_inp']['_XYCoordinates'][0][1])], self._DesignParameter['nmos_inp']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		elif (mode == 'horizontal'):
		    xy_with_offset = []
		    target_x_value = (0 + self._DesignParameter['M2V2M3_inp_mos_drain']['_XYCoordinates'][0][0])
		    for i in range(len(self._DesignParameter['nmos_inp']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'])):
		        if ((i % 2) == 0):
		            xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['nmos_inp']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['nmos_inp']['_XYCoordinates'][0][1])], self._DesignParameter['nmos_inp']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		self._DesignParameter['inp_mos_drain_met2_array'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _Width=_width)
		self._DesignParameter['inp_mos_drain_met2_array']['_XYCoordinates'] = path_list
		path_list = []
		if (len(self._DesignParameter['mid_nmos_left']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates']) == 1):
		    mode = 'vertical'
		    _width = self._DesignParameter['mid_nmos_left']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
		elif (self._DesignParameter['mid_nmos_left']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0] == self._DesignParameter['mid_nmos_left']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][(- 1)][0]):
		    mode = 'horizontal'
		    _width = self._DesignParameter['mid_nmos_left']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
		elif (self._DesignParameter['mid_nmos_left']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1] == self._DesignParameter['mid_nmos_left']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][(- 1)][1]):
		    mode = 'vertical'
		    _width = self._DesignParameter['mid_nmos_left']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
		else:
		    print('Invalid Target Input')
		if (mode == 'vertical'):
		    xy_with_offset = []
		    target_y_value = (0 + self._DesignParameter['M2V2M3_inp_mos_drain']['_XYCoordinates'][0][1])
		    for i in range(len(self._DesignParameter['mid_nmos_left']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'])):
		        if ((i % 2) == 1):
		            xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['mid_nmos_left']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['mid_nmos_left']['_XYCoordinates'][0][1])], self._DesignParameter['mid_nmos_left']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		elif (mode == 'horizontal'):
		    xy_with_offset = []
		    target_x_value = (0 + self._DesignParameter['M2V2M3_inp_mos_drain']['_XYCoordinates'][0][0])
		    for i in range(len(self._DesignParameter['mid_nmos_left']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'])):
		        if ((i % 2) == 1):
		            xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['mid_nmos_left']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['mid_nmos_left']['_XYCoordinates'][0][1])], self._DesignParameter['mid_nmos_left']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		self._DesignParameter['mid_mos_left_drain_array_met2'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _Width=_width)
		self._DesignParameter['mid_mos_left_drain_array_met2']['_XYCoordinates'] = path_list
		self._DesignParameter['met2_routing_left'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _Width=self._DesignParameter['M2V2M3_inp_mos_drain']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'])
		self._DesignParameter['met2_routing_left']['_XYCoordinates'] = [[[(self._DesignParameter['inp_mos_drain_met2_array']['_XYCoordinates'][0][0][0] - (self._DesignParameter['inp_mos_drain_met2_array']['_Width'] / 2)), self._DesignParameter['M2V2M3_inp_mos_drain']['_XYCoordinates'][0][1]], [(self._DesignParameter['mid_mos_left_drain_array_met2']['_XYCoordinates'][(- 1)][0][0] + (self._DesignParameter['mid_mos_left_drain_array_met2']['_Width'] / 2)), self._DesignParameter['M2V2M3_inp_mos_drain']['_XYCoordinates'][0][1]]]]
		self._DesignParameter['nmos_inn'] = self._SrefElementDeclaration(_DesignObj=NMOSWithDummy._NMOS(_Name='nmos_innIn{}'.format(_Name)))[0]
		self._DesignParameter['nmos_inn']['_DesignObj']._CalculateNMOSDesignParameter(**dict(_NMOSNumberofGate=12, _NMOSChannelWidth=nmos_fwidth, _NMOSChannellength=30, _NMOSDummy=True, _GateSpacing=None, _XVT='SLVT'))
		self._DesignParameter['nmos_inn']['_XYCoordinates'] = [[((((self._DesignParameter['mid_nmos_right']['_XYCoordinates'][0][0] + self._DesignParameter['mid_nmos_right']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][(- 1)][0]) + (self._DesignParameter['mid_nmos_right']['_DesignObj']._DesignParameter['_PODummyLayer']['_XWidth'] / 2)) - (self._DesignParameter['nmos_inn']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][0] - (self._DesignParameter['nmos_inn']['_DesignObj']._DesignParameter['_PODummyLayer']['_XWidth'] / 2))) + drc._PolygateMinSpace), self._DesignParameter['mid_nmos_right']['_XYCoordinates'][0][1]]]
		self._DesignParameter['M2V2M3_inn_mos_drain'] = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_Name='M2V2M3_inn_mos_drainIn{}'.format(_Name)))[0]
		self._DesignParameter['M2V2M3_inn_mos_drain']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureY(**dict(_ViaMet22Met3NumberOfCOX=max(1, (1 + int(((((((self._DesignParameter['nmos_inp']['_XYCoordinates'][0][0] + self._DesignParameter['nmos_inp']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][(- 1)][0]) + (self._DesignParameter['nmos_inp']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] / 2)) - ((self._DesignParameter['nmos_inp']['_XYCoordinates'][0][0] + self._DesignParameter['nmos_inp']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0]) - (self._DesignParameter['nmos_inp']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] / 2))) - drc._VIAxMinSpace) - (2 * drc._VIAxMinEnclosureByMetx)) / (drc._VIAxMinWidth + drc._VIAxMinSpace))))), _ViaMet22Met3NumberOfCOY=1))
		self._DesignParameter['M2V2M3_inn_mos_drain']['_XYCoordinates'] = [[self._DesignParameter['nmos_inn']['_XYCoordinates'][0][0], self._DesignParameter['M2V2M3_inp_mos_drain']['_XYCoordinates'][0][1]]]
		XYList = []
		xy_offset = (0, int(((drc._VIAxMinWidth + drc._VIAxMinSpace) / 4)))
		for i in range(len(self._DesignParameter['nmos_inn']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		    if ((i % 2) == 0):
		        xy = (self._DesignParameter['nmos_inn']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i][0] if (type(self._DesignParameter['nmos_inn']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i][0]) == list) else self._DesignParameter['nmos_inn']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])
		        XYList.append([((x + y) + z) for (x, y, z) in zip([(0 + self._DesignParameter['nmos_inn']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['nmos_inn']['_XYCoordinates'][0][1])], xy, xy_offset)])
		self._DesignParameter['nmos_inn_drain_via'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='nmos_inn_drain_viaIn{}'.format(_Name)))[0]
		self._DesignParameter['nmos_inn_drain_via']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(**dict(_ViaMet12Met2NumberOfCOX=1, _ViaMet12Met2NumberOfCOY=num_of_inp_via))
		self._DesignParameter['nmos_inn_drain_via']['_XYCoordinates'] = XYList
		XYList = []
		xy_offset = (0, (- int(((drc._VIAxMinWidth + drc._VIAxMinSpace) / 4))))
		for i in range(len(self._DesignParameter['nmos_inn']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		    if ((i % 2) == 1):
		        xy = (self._DesignParameter['nmos_inn']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i][0] if (type(self._DesignParameter['nmos_inn']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i][0]) == list) else self._DesignParameter['nmos_inn']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])
		        XYList.append([((x + y) + z) for (x, y, z) in zip([(0 + self._DesignParameter['nmos_inn']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['nmos_inn']['_XYCoordinates'][0][1])], xy, xy_offset)])
		self._DesignParameter['nmos_inn_source_via'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='nmos_inn_source_viaIn{}'.format(_Name)))[0]
		self._DesignParameter['nmos_inn_source_via']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(**dict(_ViaMet12Met2NumberOfCOX=1, _ViaMet12Met2NumberOfCOY=num_of_inp_via))
		self._DesignParameter['nmos_inn_source_via']['_XYCoordinates'] = XYList
		self._DesignParameter['M2V2M3_mid_node'] = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_Name='M2V2M3_mid_nodeIn{}'.format(_Name)))[0]
		self._DesignParameter['M2V2M3_mid_node']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureY(**dict(_ViaMet22Met3NumberOfCOX=4, _ViaMet22Met3NumberOfCOY=1))
		self._DesignParameter['M2V2M3_mid_node']['_XYCoordinates'] = [[self._DesignParameter['nmos_bot']['_XYCoordinates'][0][0], ((((self._DesignParameter['M3V3M4_mid_mod_left']['_XYCoordinates'][0][1] + self._DesignParameter['M3V3M4_mid_mod_left']['_DesignObj']._DesignParameter['_Met4Layer']['_XYCoordinates'][0][1]) - (self._DesignParameter['M3V3M4_mid_mod_left']['_DesignObj']._DesignParameter['_Met4Layer']['_YWidth'] / 2)) - drc._MetalxMinSpace4) - (self._DesignParameter['M2V2M3_mid_node']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth'] / 2))]]
		self._DesignParameter['M3V3M4_mid_node'] = self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_Name='M3V3M4_mid_nodeIn{}'.format(_Name)))[0]
		self._DesignParameter['M3V3M4_mid_node']['_DesignObj']._CalculateViaMet32Met4DesignParameterMinimumEnclosureY(**dict(_ViaMet32Met4NumberOfCOX=4, _ViaMet32Met4NumberOfCOY=1))
		self._DesignParameter['M3V3M4_mid_node']['_XYCoordinates'] = [[self._DesignParameter['nmos_bot']['_XYCoordinates'][0][0], ((((self._DesignParameter['M3V3M4_mid_mod_left']['_XYCoordinates'][0][1] + self._DesignParameter['M3V3M4_mid_mod_left']['_DesignObj']._DesignParameter['_Met4Layer']['_XYCoordinates'][0][1]) - (self._DesignParameter['M3V3M4_mid_mod_left']['_DesignObj']._DesignParameter['_Met4Layer']['_YWidth'] / 2)) - drc._MetalxMinSpace4) - (self._DesignParameter['M2V2M3_mid_node']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth'] / 2))]]
		self._DesignParameter['METAL2_path_27'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _Width=self._DesignParameter['M3V3M4_mid_node']['_DesignObj']._DesignParameter['_Met4Layer']['_YWidth'])
		self._DesignParameter['METAL2_path_27']['_XYCoordinates'] = [[[((self._DesignParameter['nmos_inp_source_via']['_XYCoordinates'][0][0] + self._DesignParameter['nmos_inp_source_via']['_DesignObj']._DesignParameter['_Met2Layer']['_XYCoordinates'][0][0]) - (self._DesignParameter['nmos_inp_source_via']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth'] / 2)), self._DesignParameter['M3V3M4_mid_node']['_XYCoordinates'][0][1]], [((self._DesignParameter['nmos_inn_source_via']['_XYCoordinates'][(- 1)][0] + self._DesignParameter['nmos_inn_source_via']['_DesignObj']._DesignParameter['_Met2Layer']['_XYCoordinates'][0][0]) + (self._DesignParameter['nmos_inn_source_via']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth'] / 2)), self._DesignParameter['M3V3M4_mid_node']['_XYCoordinates'][0][1]]]]
		path_list = []
		if (len(self._DesignParameter['nmos_inp']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates']) == 1):
		    mode = 'vertical'
		    _width = self._DesignParameter['nmos_inp']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
		elif (self._DesignParameter['nmos_inp']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0] == self._DesignParameter['nmos_inp']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][(- 1)][0]):
		    mode = 'horizontal'
		    _width = self._DesignParameter['nmos_inp']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
		elif (self._DesignParameter['nmos_inp']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1] == self._DesignParameter['nmos_inp']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][(- 1)][1]):
		    mode = 'vertical'
		    _width = self._DesignParameter['nmos_inp']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
		else:
		    print('Invalid Target Input')
		if (mode == 'vertical'):
		    xy_with_offset = []
		    target_y_value = (0 + self._DesignParameter['M3V3M4_mid_node']['_XYCoordinates'][0][1])
		    for i in range(len(self._DesignParameter['nmos_inp']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'])):
		        if ((i % 2) == 1):
		            xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['nmos_inp']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['nmos_inp']['_XYCoordinates'][0][1])], self._DesignParameter['nmos_inp']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		elif (mode == 'horizontal'):
		    xy_with_offset = []
		    target_x_value = (0 + self._DesignParameter['M3V3M4_mid_node']['_XYCoordinates'][0][0])
		    for i in range(len(self._DesignParameter['nmos_inp']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'])):
		        if ((i % 2) == 1):
		            xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['nmos_inp']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['nmos_inp']['_XYCoordinates'][0][1])], self._DesignParameter['nmos_inp']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		self._DesignParameter['inp_mos_source_met2_array'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _Width=_width)
		self._DesignParameter['inp_mos_source_met2_array']['_XYCoordinates'] = path_list
		path_list = []
		if (len(self._DesignParameter['nmos_inn']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates']) == 1):
		    mode = 'vertical'
		    _width = self._DesignParameter['nmos_inn']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
		elif (self._DesignParameter['nmos_inn']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0] == self._DesignParameter['nmos_inn']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][(- 1)][0]):
		    mode = 'horizontal'
		    _width = self._DesignParameter['nmos_inn']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
		elif (self._DesignParameter['nmos_inn']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1] == self._DesignParameter['nmos_inn']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][(- 1)][1]):
		    mode = 'vertical'
		    _width = self._DesignParameter['nmos_inn']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
		else:
		    print('Invalid Target Input')
		if (mode == 'vertical'):
		    xy_with_offset = []
		    target_y_value = (0 + self._DesignParameter['M3V3M4_mid_node']['_XYCoordinates'][0][1])
		    for i in range(len(self._DesignParameter['nmos_inn']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'])):
		        if ((i % 2) == 1):
		            xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['nmos_inn']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['nmos_inn']['_XYCoordinates'][0][1])], self._DesignParameter['nmos_inn']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		elif (mode == 'horizontal'):
		    xy_with_offset = []
		    target_x_value = (0 + self._DesignParameter['M3V3M4_mid_node']['_XYCoordinates'][0][0])
		    for i in range(len(self._DesignParameter['nmos_inn']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'])):
		        if ((i % 2) == 1):
		            xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['nmos_inn']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['nmos_inn']['_XYCoordinates'][0][1])], self._DesignParameter['nmos_inn']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		self._DesignParameter['inn_mos_source_met2_array'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _Width=_width)
		self._DesignParameter['inn_mos_source_met2_array']['_XYCoordinates'] = path_list
		self._DesignParameter['PCCAM1_inp_mos_gate'] = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_Name='PCCAM1_inp_mos_gateIn{}'.format(_Name)))[0]
		self._DesignParameter['PCCAM1_inp_mos_gate']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(**dict(_ViaPoly2Met1NumberOfCOX=max(1, (1 + int(((((((self._DesignParameter['nmos_inp']['_XYCoordinates'][0][0] + self._DesignParameter['nmos_inp']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]) + (self._DesignParameter['nmos_inp']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)) - ((self._DesignParameter['nmos_inp']['_XYCoordinates'][0][0] + self._DesignParameter['nmos_inp']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['nmos_inp']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2))) - drc._CoMinSpace) - (2 * drc._CoMinEnclosureByPO)) / (drc._CoMinWidth + drc._CoMinSpace))))), _ViaPoly2Met1NumberOfCOY=input_via_y))
		self._DesignParameter['PCCAM1_inp_mos_gate']['_XYCoordinates'] = [[self._DesignParameter['nmos_inp']['_XYCoordinates'][0][0], (((- self._DesignParameter['PCCAM1_inp_mos_gate']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']) / 2) + ((self._DesignParameter['METAL2_path_27']['_XYCoordinates'][0][0][1] - self._DesignParameter['METAL2_path_27']['_Width']) - drc._Metal1MinSpace))]]
		path_list = []
		if (len(self._DesignParameter['nmos_inp']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates']) == 1):
		    mode = 'vertical'
		    _width = self._DesignParameter['nmos_inp']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
		elif (self._DesignParameter['nmos_inp']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0] == self._DesignParameter['nmos_inp']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]):
		    mode = 'horizontal'
		    _width = self._DesignParameter['nmos_inp']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
		elif (self._DesignParameter['nmos_inp']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1] == self._DesignParameter['nmos_inp']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][1]):
		    mode = 'vertical'
		    _width = self._DesignParameter['nmos_inp']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
		else:
		    print('Invalid Target Input')
		if (mode == 'vertical'):
		    xy_with_offset = []
		    target_y_value = (0 + self._DesignParameter['PCCAM1_inp_mos_gate']['_XYCoordinates'][0][1])
		    for i in range(len(self._DesignParameter['nmos_inp']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
		        xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['nmos_inp']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['nmos_inp']['_XYCoordinates'][0][1])], self._DesignParameter['nmos_inp']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		elif (mode == 'horizontal'):
		    xy_with_offset = []
		    target_x_value = (0 + self._DesignParameter['PCCAM1_inp_mos_gate']['_XYCoordinates'][0][0])
		    for i in range(len(self._DesignParameter['nmos_inp']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
		        xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['nmos_inp']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['nmos_inp']['_XYCoordinates'][0][1])], self._DesignParameter['nmos_inp']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		self._DesignParameter['inp_mos_gate_array'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _Width=_width)
		self._DesignParameter['inp_mos_gate_array']['_XYCoordinates'] = path_list
		self._DesignParameter['POLY_path_62'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _Width=self._DesignParameter['PCCAM1_inp_mos_gate']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'])
		self._DesignParameter['POLY_path_62']['_XYCoordinates'] = [[[((self._DesignParameter['nmos_inp']['_XYCoordinates'][0][0] + self._DesignParameter['nmos_inp']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['nmos_inp']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)), self._DesignParameter['PCCAM1_inp_mos_gate']['_XYCoordinates'][0][1]], [((self._DesignParameter['nmos_inp']['_XYCoordinates'][0][0] + self._DesignParameter['nmos_inp']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]) + (self._DesignParameter['nmos_inp']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)), self._DesignParameter['PCCAM1_inp_mos_gate']['_XYCoordinates'][0][1]]]]
		self._DesignParameter['PCCAM1_inn_mos_gate'] = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_Name='PCCAM1_inn_mos_gateIn{}'.format(_Name)))[0]
		self._DesignParameter['PCCAM1_inn_mos_gate']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(**dict(_ViaPoly2Met1NumberOfCOX=max(1, (1 + int(((((((self._DesignParameter['nmos_inp']['_XYCoordinates'][0][0] + self._DesignParameter['nmos_inp']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]) + (self._DesignParameter['nmos_inp']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)) - ((self._DesignParameter['nmos_inp']['_XYCoordinates'][0][0] + self._DesignParameter['nmos_inp']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['nmos_inp']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2))) - drc._CoMinSpace) - (2 * drc._CoMinEnclosureByPO)) / (drc._CoMinWidth + drc._CoMinSpace))))), _ViaPoly2Met1NumberOfCOY=input_via_y))
		self._DesignParameter['PCCAM1_inn_mos_gate']['_XYCoordinates'] = [[self._DesignParameter['nmos_inn']['_XYCoordinates'][0][0], (((- self._DesignParameter['PCCAM1_inp_mos_gate']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']) / 2) + ((self._DesignParameter['METAL2_path_27']['_XYCoordinates'][0][0][1] - self._DesignParameter['METAL2_path_27']['_Width']) - drc._Metal1MinSpace))]]
		path_list = []
		if (len(self._DesignParameter['nmos_inn']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates']) == 1):
		    mode = 'vertical'
		    _width = self._DesignParameter['nmos_inn']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
		elif (self._DesignParameter['nmos_inn']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0] == self._DesignParameter['nmos_inn']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]):
		    mode = 'horizontal'
		    _width = self._DesignParameter['nmos_inn']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
		elif (self._DesignParameter['nmos_inn']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1] == self._DesignParameter['nmos_inn']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][1]):
		    mode = 'vertical'
		    _width = self._DesignParameter['nmos_inn']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
		else:
		    print('Invalid Target Input')
		if (mode == 'vertical'):
		    xy_with_offset = []
		    target_y_value = (0 + self._DesignParameter['PCCAM1_inn_mos_gate']['_XYCoordinates'][0][1])
		    for i in range(len(self._DesignParameter['nmos_inn']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
		        xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['nmos_inn']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['nmos_inn']['_XYCoordinates'][0][1])], self._DesignParameter['nmos_inn']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		elif (mode == 'horizontal'):
		    xy_with_offset = []
		    target_x_value = (0 + self._DesignParameter['PCCAM1_inn_mos_gate']['_XYCoordinates'][0][0])
		    for i in range(len(self._DesignParameter['nmos_inn']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
		        xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['nmos_inn']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['nmos_inn']['_XYCoordinates'][0][1])], self._DesignParameter['nmos_inn']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		self._DesignParameter['inn_mos_gate_array'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _Width=_width)
		self._DesignParameter['inn_mos_gate_array']['_XYCoordinates'] = path_list
		self._DesignParameter['POLY_path_64'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _Width=self._DesignParameter['PCCAM1_inn_mos_gate']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'])
		self._DesignParameter['POLY_path_64']['_XYCoordinates'] = [[[((self._DesignParameter['nmos_inn']['_XYCoordinates'][0][0] + self._DesignParameter['nmos_inn']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['nmos_inn']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)), self._DesignParameter['PCCAM1_inn_mos_gate']['_XYCoordinates'][0][1]], [((self._DesignParameter['nmos_inn']['_XYCoordinates'][0][0] + self._DesignParameter['nmos_inn']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]) + (self._DesignParameter['nmos_inn']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)), self._DesignParameter['PCCAM1_inn_mos_gate']['_XYCoordinates'][0][1]]]]
		self._DesignParameter['METAL4_path_17'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL4'][0], _Datatype=DesignParameters._LayerMapping['METAL4'][1], _Width=(((((self._DesignParameter['nmos_bot']['_XYCoordinates'][0][0] + self._DesignParameter['nmos_bot']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][1][0]) - (self._DesignParameter['nmos_bot']['_XYCoordinates'][0][0] + self._DesignParameter['nmos_bot']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0])) * 2) - (self._DesignParameter['nmos_bot']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] / 2)) - drc._MetalxMinSpace2))
		self._DesignParameter['METAL4_path_17']['_XYCoordinates'] = [[[(+ (self._DesignParameter['M3V3M4_mid_node']['_XYCoordinates'][0][0] + self._DesignParameter['M3V3M4_mid_node']['_DesignObj']._DesignParameter['_Met4Layer']['_XYCoordinates'][0][0])), (+ (self._DesignParameter['M3V3M4_mid_node']['_XYCoordinates'][0][1] + self._DesignParameter['M3V3M4_mid_node']['_DesignObj']._DesignParameter['_Met4Layer']['_XYCoordinates'][0][1]))], [(self._DesignParameter['M3V3M4_mid_node']['_XYCoordinates'][0][0] + self._DesignParameter['M3V3M4_mid_node']['_DesignObj']._DesignParameter['_Met4Layer']['_XYCoordinates'][0][0]), ((self._DesignParameter['bot_nmos_via23']['_XYCoordinates'][0][1] + self._DesignParameter['bot_nmos_via23']['_DesignObj']._DesignParameter['_Met2Layer']['_XYCoordinates'][0][1]) - (self._DesignParameter['bot_nmos_via23']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] / 2))]]]
		path_list = []
		if (len(self._DesignParameter['mid_nmos_right']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates']) == 1):
		    mode = 'vertical'
		    _width = self._DesignParameter['mid_nmos_right']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
		elif (self._DesignParameter['mid_nmos_right']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0] == self._DesignParameter['mid_nmos_right']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][(- 1)][0]):
		    mode = 'horizontal'
		    _width = self._DesignParameter['mid_nmos_right']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
		elif (self._DesignParameter['mid_nmos_right']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1] == self._DesignParameter['mid_nmos_right']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][(- 1)][1]):
		    mode = 'vertical'
		    _width = self._DesignParameter['mid_nmos_right']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
		else:
		    print('Invalid Target Input')
		if (mode == 'vertical'):
		    xy_with_offset = []
		    target_y_value = (0 + self._DesignParameter['M2V2M3_inn_mos_drain']['_XYCoordinates'][0][1])
		    for i in range(len(self._DesignParameter['mid_nmos_right']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'])):
		        if ((i % 2) == 1):
		            xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['mid_nmos_right']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['mid_nmos_right']['_XYCoordinates'][0][1])], self._DesignParameter['mid_nmos_right']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		elif (mode == 'horizontal'):
		    xy_with_offset = []
		    target_x_value = (0 + self._DesignParameter['M2V2M3_inn_mos_drain']['_XYCoordinates'][0][0])
		    for i in range(len(self._DesignParameter['mid_nmos_right']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'])):
		        if ((i % 2) == 1):
		            xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['mid_nmos_right']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['mid_nmos_right']['_XYCoordinates'][0][1])], self._DesignParameter['mid_nmos_right']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		self._DesignParameter['mid_mos_right_drain_array_met2'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _Width=_width)
		self._DesignParameter['mid_mos_right_drain_array_met2']['_XYCoordinates'] = path_list
		self._DesignParameter['METAL2_path_28'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _Width=self._DesignParameter['M2V2M3_inn_mos_drain']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'])
		self._DesignParameter['METAL2_path_28']['_XYCoordinates'] = [[[(self._DesignParameter['mid_mos_right_drain_array_met2']['_XYCoordinates'][0][0][0] - (self._DesignParameter['mid_mos_right_drain_array_met2']['_Width'] / 2)), (self._DesignParameter['M2V2M3_inn_mos_drain']['_XYCoordinates'][0][1] + self._DesignParameter['M2V2M3_inn_mos_drain']['_DesignObj']._DesignParameter['_Met2Layer']['_XYCoordinates'][0][1])], [((self._DesignParameter['nmos_inn_drain_via']['_XYCoordinates'][(- 1)][0] + self._DesignParameter['nmos_inn_drain_via']['_DesignObj']._DesignParameter['_Met2Layer']['_XYCoordinates'][0][0]) + (self._DesignParameter['nmos_inn_drain_via']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth'] / 2)), (self._DesignParameter['M2V2M3_inn_mos_drain']['_XYCoordinates'][0][1] + self._DesignParameter['M2V2M3_inn_mos_drain']['_DesignObj']._DesignParameter['_Met2Layer']['_XYCoordinates'][0][1])]]]
		path_list = []
		if (len(self._DesignParameter['nmos_inn']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates']) == 1):
		    mode = 'vertical'
		    _width = self._DesignParameter['nmos_inn']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
		elif (self._DesignParameter['nmos_inn']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0] == self._DesignParameter['nmos_inn']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][(- 1)][0]):
		    mode = 'horizontal'
		    _width = self._DesignParameter['nmos_inn']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
		elif (self._DesignParameter['nmos_inn']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1] == self._DesignParameter['nmos_inn']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][(- 1)][1]):
		    mode = 'vertical'
		    _width = self._DesignParameter['nmos_inn']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
		else:
		    print('Invalid Target Input')
		if (mode == 'vertical'):
		    xy_with_offset = []
		    target_y_value = (0 + self._DesignParameter['M2V2M3_inn_mos_drain']['_XYCoordinates'][0][1])
		    for i in range(len(self._DesignParameter['nmos_inn']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'])):
		        if ((i % 2) == 0):
		            xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['nmos_inn']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['nmos_inn']['_XYCoordinates'][0][1])], self._DesignParameter['nmos_inn']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		elif (mode == 'horizontal'):
		    xy_with_offset = []
		    target_x_value = (0 + self._DesignParameter['M2V2M3_inn_mos_drain']['_XYCoordinates'][0][0])
		    for i in range(len(self._DesignParameter['nmos_inn']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'])):
		        if ((i % 2) == 0):
		            xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['nmos_inn']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['nmos_inn']['_XYCoordinates'][0][1])], self._DesignParameter['nmos_inn']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		self._DesignParameter['inn_mos_drain_met2_array'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _Width=_width)
		self._DesignParameter['inn_mos_drain_met2_array']['_XYCoordinates'] = path_list
		self._DesignParameter['GuardringInNMOSSetofSlicer_0'] = self._SrefElementDeclaration(_DesignObj=PSubRing.PSubRing(_Name='GuardringInNMOSSetofSlicer_0In{}'.format(_Name)))[0]
		self._DesignParameter['GuardringInNMOSSetofSlicer_0']['_DesignObj']._CalculateDesignParameter(**dict(height=3170, width=4860, contact=subring_via))
		self._DesignParameter['GuardringInNMOSSetofSlicer_0']['_XYCoordinates'] = [[0.0, (- 1668.0)]]
		self._DesignParameter['GuardringInNMOSSetofSlicer_0']['_DesignObj']._CalculateDesignParameter(**dict(height=(max(((((self._DesignParameter['M1V1M2_mid_mos_left_gate']['_XYCoordinates'][0][1] + self._DesignParameter['M1V1M2_mid_mos_left_gate']['_DesignObj']._DesignParameter['_Met2Layer']['_XYCoordinates'][0][1]) + (self._DesignParameter['M1V1M2_mid_mos_left_gate']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] / 2)) + drc._MetalxMinSpace) + (self._DesignParameter['GuardringInNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['met_top']['_YWidth'] / 2)), ((((self._DesignParameter['mid_nmos_left']['_XYCoordinates'][0][1] + self._DesignParameter['mid_nmos_left']['_DesignObj']._DesignParameter['_SLVTLayer']['_XYCoordinates'][0][1]) + (self._DesignParameter['mid_nmos_left']['_DesignObj']._DesignParameter['_SLVTLayer']['_YWidth'] / 2)) + drc._PpMinSpace) + (self._DesignParameter['GuardringInNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['nw_top']['_YWidth'] / 2)), (((((((self._DesignParameter['M2V2M3_inp_mos_drain']['_XYCoordinates'][0][1] + self._DesignParameter['M2V2M3_inp_mos_drain']['_DesignObj']._DesignParameter['_Met3Layer']['_XYCoordinates'][0][1]) - (self._DesignParameter['M2V2M3_inp_mos_drain']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth'] / 2)) + (2 * drc._VIAxMinWidth)) + drc._VIAxMinSpace) + (2 * drc._VIAxMinEnclosureByMetx)) + drc._MetalxMinSpace) + (self._DesignParameter['GuardringInNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['met_top']['_YWidth'] / 2))) - ((((self._DesignParameter['nmos_bot']['_XYCoordinates'][0][1] + self._DesignParameter['nmos_bot']['_DesignObj']._DesignParameter['_SLVTLayer']['_XYCoordinates'][0][1]) - (self._DesignParameter['nmos_bot']['_DesignObj']._DesignParameter['_SLVTLayer']['_YWidth'] / 2)) - (self._DesignParameter['GuardringInNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['nw_bot']['_YWidth'] / 2)) - drc._PpMinSpacetoPRES)), width=(((((self._DesignParameter['nmos_inn']['_XYCoordinates'][0][0] + self._DesignParameter['nmos_inn']['_DesignObj']._DesignParameter['_SLVTLayer']['_XYCoordinates'][0][0]) + (self._DesignParameter['nmos_inn']['_DesignObj']._DesignParameter['_SLVTLayer']['_XWidth'] / 2)) + drc._PpMinSpacetoPRES) + (self._DesignParameter['GuardringInNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['nw_left']['_XWidth'] / 2)) - ((((self._DesignParameter['nmos_inp']['_XYCoordinates'][0][0] + self._DesignParameter['nmos_inp']['_DesignObj']._DesignParameter['_SLVTLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['nmos_inp']['_DesignObj']._DesignParameter['_SLVTLayer']['_XWidth'] / 2)) - drc._PpMinSpacetoPRES) - (self._DesignParameter['GuardringInNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['nw_left']['_XWidth'] / 2))), contact=subring_via))
		self._DesignParameter['GuardringInPMOSSetofSlicer_0'] = self._SrefElementDeclaration(_DesignObj=NSubRing.NSubRing(_Name='GuardringInPMOSSetofSlicer_0In{}'.format(_Name)))[0]
		self._DesignParameter['GuardringInPMOSSetofSlicer_0']['_DesignObj']._CalculateDesignParameter(**dict(height=1660, width=4100, contact=subring_via))
		self._DesignParameter['GuardringInPMOSSetofSlicer_0']['_XYCoordinates'] = [[0.0, 1084.0]]
		self._DesignParameter['pmos_mid_left'] = self._SrefElementDeclaration(_DesignObj=PMOSWithDummy._PMOS(_Name='pmos_mid_leftIn{}'.format(_Name)))[0]
		self._DesignParameter['pmos_mid_left']['_DesignObj']._CalculatePMOSDesignParameter(**dict(_PMOSNumberofGate=2, _PMOSChannelWidth=pmos_fwidth, _PMOSChannellength=30, _PMOSDummy=True, _GateSpacing=None, _XVT='SLVT'))
		self._DesignParameter['pmos_mid_left']['_XYCoordinates'] = [[self._DesignParameter['mid_nmos_left']['_XYCoordinates'][0][0], ((((((((((self._DesignParameter['GuardringInNMOSSetofSlicer_0']['_XYCoordinates'][0][1] + self._DesignParameter['GuardringInNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['nw_top']['_XYCoordinates'][0][1]) + (self._DesignParameter['GuardringInNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['nw_top']['_YWidth'] / 2)) + (self._DesignParameter['GuardringInPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['nw_bot']['_YWidth'] / 2)) + (self._DesignParameter['GuardringInPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['met_bot']['_YWidth'] / 2)) + drc._Metal1MinSpace) + drc._CoMinWidth) + drc._Metal1MinWidth) + drc._Metal1MinSpace) + (self._DesignParameter['pmos_mid_left']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)) + (subring_addi * 2))]]
		self._DesignParameter['pmos_left'] = self._SrefElementDeclaration(_DesignObj=PMOSWithDummy._PMOS(_Name='pmos_leftIn{}'.format(_Name)))[0]
		self._DesignParameter['pmos_left']['_DesignObj']._CalculatePMOSDesignParameter(**dict(_PMOSNumberofGate=(precharge_outside_gate + precharge_inside_gate), _PMOSChannelWidth=pmos_fwidth, _PMOSChannellength=30, _PMOSDummy=True, _GateSpacing=None, _XVT='SLVT'))
		self._DesignParameter['pmos_left']['_XYCoordinates'] = [[((((self._DesignParameter['pmos_mid_left']['_XYCoordinates'][0][0] + self._DesignParameter['pmos_mid_left']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['pmos_mid_left']['_DesignObj']._DesignParameter['_PODummyLayer']['_XWidth'] / 2)) - drc._PolygateMinSpace) - (self._DesignParameter['pmos_left']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][(- 1)][0] + (self._DesignParameter['pmos_left']['_DesignObj']._DesignParameter['_PODummyLayer']['_XWidth'] / 2))), self._DesignParameter['pmos_mid_left']['_XYCoordinates'][0][1]]]
		self._DesignParameter['pmos_mid_right'] = self._SrefElementDeclaration(_DesignObj=PMOSWithDummy._PMOS(_Name='pmos_mid_rightIn{}'.format(_Name)))[0]
		self._DesignParameter['pmos_mid_right']['_DesignObj']._CalculatePMOSDesignParameter(**dict(_PMOSNumberofGate=2, _PMOSChannelWidth=pmos_fwidth, _PMOSChannellength=30, _PMOSDummy=True, _GateSpacing=None, _XVT='SLVT'))
		self._DesignParameter['pmos_mid_right']['_XYCoordinates'] = [[self._DesignParameter['mid_nmos_right']['_XYCoordinates'][0][0], self._DesignParameter['pmos_mid_left']['_XYCoordinates'][0][1]]]
		self._DesignParameter['pmos_right'] = self._SrefElementDeclaration(_DesignObj=PMOSWithDummy._PMOS(_Name='pmos_rightIn{}'.format(_Name)))[0]
		self._DesignParameter['pmos_right']['_DesignObj']._CalculatePMOSDesignParameter(**dict(_PMOSNumberofGate=(precharge_outside_gate + precharge_inside_gate), _PMOSChannelWidth=pmos_fwidth, _PMOSChannellength=30, _PMOSDummy=True, _GateSpacing=None, _XVT='SLVT'))
		self._DesignParameter['pmos_right']['_XYCoordinates'] = [[((((self._DesignParameter['pmos_mid_right']['_XYCoordinates'][0][0] + self._DesignParameter['pmos_mid_right']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][(- 1)][0]) + (self._DesignParameter['pmos_mid_right']['_DesignObj']._DesignParameter['_PODummyLayer']['_XWidth'] / 2)) - (self._DesignParameter['pmos_right']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][0] - (self._DesignParameter['pmos_right']['_DesignObj']._DesignParameter['_PODummyLayer']['_XWidth'] / 2))) + drc._PolygateMinSpace), self._DesignParameter['pmos_mid_right']['_XYCoordinates'][0][1]]]
		precharge_via = max(1, (1 + int((((self._DesignParameter['pmos_left']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] - drc._VIAxMinSpace) - (2 * drc._VIAxMinEnclosureByMetx)) / (drc._VIAxMinWidth + drc._VIAxMinSpace)))))
		XYList = []
		xy_offset = (0, (- int(((drc._VIAxMinWidth + drc._VIAxMinSpace) / 4))))
		for element in self._DesignParameter['pmos_left']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][1:(precharge_outside_gate + 1):2]:
		    element = (element[0] if (type(element[0]) == list) else element)
		    XYList.append([((x + y) + z) for (x, y, z) in zip([(0 + self._DesignParameter['pmos_left']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['pmos_left']['_XYCoordinates'][0][1])], element, xy_offset)])
		self._DesignParameter['precharge_left_left'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='precharge_left_leftIn{}'.format(_Name)))[0]
		self._DesignParameter['precharge_left_left']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(**dict(_ViaMet12Met2NumberOfCOX=1, _ViaMet12Met2NumberOfCOY=precharge_via))
		self._DesignParameter['precharge_left_left']['_XYCoordinates'] = XYList
		XYList = []
		xy_offset = [0, 0]
		for i in range(len(self._DesignParameter['precharge_left_left']['_XYCoordinates'])):
		    xy = (self._DesignParameter['precharge_left_left']['_XYCoordinates'][i][0] if (type(self._DesignParameter['precharge_left_left']['_XYCoordinates'][i][0]) == list) else self._DesignParameter['precharge_left_left']['_XYCoordinates'][i])
		    XYList.append([((x + y) + z) for (x, y, z) in zip([0, 0], xy, xy_offset)])
		self._DesignParameter['precharge_left_left_via23'] = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_Name='precharge_left_left_via23In{}'.format(_Name)))[0]
		self._DesignParameter['precharge_left_left_via23']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureX(**dict(_ViaMet22Met3NumberOfCOX=1, _ViaMet22Met3NumberOfCOY=precharge_via))
		self._DesignParameter['precharge_left_left_via23']['_XYCoordinates'] = XYList
		XYList = []
		xy_offset = [0, 0]
		for i in range(len(self._DesignParameter['precharge_left_left']['_XYCoordinates'])):
		    xy = (self._DesignParameter['precharge_left_left']['_XYCoordinates'][i][0] if (type(self._DesignParameter['precharge_left_left']['_XYCoordinates'][i][0]) == list) else self._DesignParameter['precharge_left_left']['_XYCoordinates'][i])
		    XYList.append([((x + y) + z) for (x, y, z) in zip([0, 0], xy, xy_offset)])
		self._DesignParameter['precharge_left_left_via34'] = self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_Name='precharge_left_left_via34In{}'.format(_Name)))[0]
		self._DesignParameter['precharge_left_left_via34']['_DesignObj']._CalculateViaMet32Met4DesignParameterMinimumEnclosureX(**dict(_ViaMet32Met4NumberOfCOX=1, _ViaMet32Met4NumberOfCOY=precharge_via))
		self._DesignParameter['precharge_left_left_via34']['_XYCoordinates'] = XYList
		XYList = []
		xy_offset = (0, (- int(((drc._VIAxMinWidth + drc._VIAxMinSpace) / 4))))
		for element in self._DesignParameter['pmos_left']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][(- 1):None:(- 1)][0:(precharge_inside_gate + 1):2][(- 1):None:(- 1)]:
		    element = (element[0] if (type(element[0]) == list) else element)
		    XYList.append([((x + y) + z) for (x, y, z) in zip([(0 + self._DesignParameter['pmos_left']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['pmos_left']['_XYCoordinates'][0][1])], element, xy_offset)])
		self._DesignParameter['precharge_left_right'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='precharge_left_rightIn{}'.format(_Name)))[0]
		self._DesignParameter['precharge_left_right']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(**dict(_ViaMet12Met2NumberOfCOX=1, _ViaMet12Met2NumberOfCOY=precharge_via))
		self._DesignParameter['precharge_left_right']['_XYCoordinates'] = XYList
		self._DesignParameter['PCCAM1_pmos_left'] = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_Name='PCCAM1_pmos_leftIn{}'.format(_Name)))[0]
		self._DesignParameter['PCCAM1_pmos_left']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(**dict(_ViaPoly2Met1NumberOfCOX=max(1, (1 + int(((((((self._DesignParameter['pmos_left']['_XYCoordinates'][0][0] + self._DesignParameter['pmos_left']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]) + (self._DesignParameter['pmos_left']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)) - ((self._DesignParameter['pmos_left']['_XYCoordinates'][0][0] + self._DesignParameter['pmos_left']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['pmos_left']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2))) - drc._CoMinSpace) - (2 * drc._CoMinEnclosureByPO)) / (drc._CoMinWidth + drc._CoMinSpace))))), _ViaPoly2Met1NumberOfCOY=1))
		self._DesignParameter['PCCAM1_pmos_left']['_XYCoordinates'] = [[self._DesignParameter['pmos_left']['_XYCoordinates'][0][0], ((((self._DesignParameter['pmos_left']['_XYCoordinates'][0][1] + self._DesignParameter['pmos_left']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) - (self._DesignParameter['pmos_left']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)) - drc._Metal1MinSpace2) - (self._DesignParameter['PCCAM1_pmos_left']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2))]]
		path_list = []
		if (len(self._DesignParameter['pmos_left']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates']) == 1):
		    mode = 'vertical'
		    _width = self._DesignParameter['pmos_left']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
		elif (self._DesignParameter['pmos_left']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0] == self._DesignParameter['pmos_left']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]):
		    mode = 'horizontal'
		    _width = self._DesignParameter['pmos_left']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
		elif (self._DesignParameter['pmos_left']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1] == self._DesignParameter['pmos_left']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][1]):
		    mode = 'vertical'
		    _width = self._DesignParameter['pmos_left']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
		else:
		    print('Invalid Target Input')
		if (mode == 'vertical'):
		    xy_with_offset = []
		    target_y_value = (0 + self._DesignParameter['PCCAM1_pmos_left']['_XYCoordinates'][0][1])
		    for i in range(len(self._DesignParameter['pmos_left']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
		        xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['pmos_left']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['pmos_left']['_XYCoordinates'][0][1])], self._DesignParameter['pmos_left']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		elif (mode == 'horizontal'):
		    xy_with_offset = []
		    target_x_value = (0 + self._DesignParameter['PCCAM1_pmos_left']['_XYCoordinates'][0][0])
		    for i in range(len(self._DesignParameter['pmos_left']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
		        xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['pmos_left']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['pmos_left']['_XYCoordinates'][0][1])], self._DesignParameter['pmos_left']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		self._DesignParameter['precharge_left_mos_gate_array'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _Width=_width)
		self._DesignParameter['precharge_left_mos_gate_array']['_XYCoordinates'] = path_list
		self._DesignParameter['POLY_path_128'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _Width=self._DesignParameter['PCCAM1_pmos_left']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'])
		self._DesignParameter['POLY_path_128']['_XYCoordinates'] = [[[((self._DesignParameter['pmos_left']['_XYCoordinates'][0][0] + self._DesignParameter['pmos_left']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['pmos_left']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)), self._DesignParameter['PCCAM1_pmos_left']['_XYCoordinates'][0][1]], [((self._DesignParameter['pmos_left']['_XYCoordinates'][0][0] + self._DesignParameter['pmos_left']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]) + (self._DesignParameter['pmos_left']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)), self._DesignParameter['PCCAM1_pmos_left']['_XYCoordinates'][0][1]]]]
		self._DesignParameter['M1V1M2_CDNS_6375475055673_1'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='M1V1M2_CDNS_6375475055673_1In{}'.format(_Name)))[0]
		self._DesignParameter['M1V1M2_CDNS_6375475055673_1']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureY(**dict(_ViaMet12Met2NumberOfCOX=max(1, (1 + int(((((((self._DesignParameter['pmos_left']['_XYCoordinates'][0][0] + self._DesignParameter['pmos_left']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]) + (self._DesignParameter['pmos_left']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)) - ((self._DesignParameter['pmos_left']['_XYCoordinates'][0][0] + self._DesignParameter['pmos_left']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['pmos_left']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2))) - drc._VIAxMinSpace) - (2 * drc._VIAxMinEnclosureByMetx)) / (drc._VIAxMinWidth + drc._VIAxMinSpace))))), _ViaMet12Met2NumberOfCOY=1))
		self._DesignParameter['M1V1M2_CDNS_6375475055673_1']['_XYCoordinates'] = [[(+ self._DesignParameter['PCCAM1_pmos_left']['_XYCoordinates'][0][0]), (+ self._DesignParameter['PCCAM1_pmos_left']['_XYCoordinates'][0][1])]]
		self._DesignParameter['M2V2M3_CDNS_6375475055672_1'] = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_Name='M2V2M3_CDNS_6375475055672_1In{}'.format(_Name)))[0]
		self._DesignParameter['M2V2M3_CDNS_6375475055672_1']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureY(**dict(_ViaMet22Met3NumberOfCOX=max(1, (1 + int(((((((self._DesignParameter['pmos_left']['_XYCoordinates'][0][0] + self._DesignParameter['pmos_left']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]) + (self._DesignParameter['pmos_left']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)) - ((self._DesignParameter['pmos_left']['_XYCoordinates'][0][0] + self._DesignParameter['pmos_left']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['pmos_left']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2))) - drc._VIAxMinSpace) - (2 * drc._VIAxMinEnclosureByMetx)) / (drc._VIAxMinWidth + drc._VIAxMinSpace))))), _ViaMet22Met3NumberOfCOY=1))
		self._DesignParameter['M2V2M3_CDNS_6375475055672_1']['_XYCoordinates'] = [[(+ self._DesignParameter['M1V1M2_CDNS_6375475055673_1']['_XYCoordinates'][0][0]), (+ self._DesignParameter['M1V1M2_CDNS_6375475055673_1']['_XYCoordinates'][0][1])]]
		self._DesignParameter['METAL1_boundary_360'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _XWidth=max((((self._DesignParameter['M1V1M2_CDNS_6375475055673_1']['_XYCoordinates'][0][0] + self._DesignParameter['M1V1M2_CDNS_6375475055673_1']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0]) + (self._DesignParameter['M1V1M2_CDNS_6375475055673_1']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] / 2)) - ((self._DesignParameter['M1V1M2_CDNS_6375475055673_1']['_XYCoordinates'][0][0] + self._DesignParameter['M1V1M2_CDNS_6375475055673_1']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0]) - (self._DesignParameter['M1V1M2_CDNS_6375475055673_1']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] / 2))), (((self._DesignParameter['PCCAM1_pmos_left']['_XYCoordinates'][0][0] + self._DesignParameter['PCCAM1_pmos_left']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0]) + (self._DesignParameter['PCCAM1_pmos_left']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] / 2)) - ((self._DesignParameter['PCCAM1_pmos_left']['_XYCoordinates'][0][0] + self._DesignParameter['PCCAM1_pmos_left']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0]) - (self._DesignParameter['PCCAM1_pmos_left']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] / 2)))), _YWidth=max((((self._DesignParameter['M1V1M2_CDNS_6375475055673_1']['_XYCoordinates'][0][1] + self._DesignParameter['M1V1M2_CDNS_6375475055673_1']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) + (self._DesignParameter['M1V1M2_CDNS_6375475055673_1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)) - ((self._DesignParameter['M1V1M2_CDNS_6375475055673_1']['_XYCoordinates'][0][1] + self._DesignParameter['M1V1M2_CDNS_6375475055673_1']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) - (self._DesignParameter['M1V1M2_CDNS_6375475055673_1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2))), (((self._DesignParameter['PCCAM1_pmos_left']['_XYCoordinates'][0][1] + self._DesignParameter['PCCAM1_pmos_left']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) + (self._DesignParameter['PCCAM1_pmos_left']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)) - ((self._DesignParameter['PCCAM1_pmos_left']['_XYCoordinates'][0][1] + self._DesignParameter['PCCAM1_pmos_left']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) - (self._DesignParameter['PCCAM1_pmos_left']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)))))
		self._DesignParameter['METAL1_boundary_360']['_XYCoordinates'] = [[(+ self._DesignParameter['PCCAM1_pmos_left']['_XYCoordinates'][0][0]), (+ self._DesignParameter['PCCAM1_pmos_left']['_XYCoordinates'][0][1])]]
		self._DesignParameter['METAL4_path_21'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL4'][0], _Datatype=DesignParameters._LayerMapping['METAL4'][1], _Width=drc._MetalxMinWidth)
		self._DesignParameter['METAL4_path_21']['_XYCoordinates'] = [[[(+ (self._DesignParameter['precharge_left_left_via34']['_XYCoordinates'][0][0] + self._DesignParameter['precharge_left_left_via34']['_DesignObj']._DesignParameter['_Met4Layer']['_XYCoordinates'][0][0])), (+ (self._DesignParameter['precharge_left_left_via34']['_XYCoordinates'][0][1] + self._DesignParameter['precharge_left_left_via34']['_DesignObj']._DesignParameter['_Met4Layer']['_XYCoordinates'][0][1]))], [(+ (self._DesignParameter['precharge_left_left_via34']['_XYCoordinates'][(- 1)][0] + self._DesignParameter['precharge_left_left_via34']['_DesignObj']._DesignParameter['_Met4Layer']['_XYCoordinates'][0][0])), (+ (self._DesignParameter['precharge_left_left_via34']['_XYCoordinates'][(- 1)][1] + self._DesignParameter['precharge_left_left_via34']['_DesignObj']._DesignParameter['_Met4Layer']['_XYCoordinates'][0][1]))]]]
		self._DesignParameter['METAL3_path_29'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0], _Datatype=DesignParameters._LayerMapping['METAL3'][1], _Width=drc._MetalxMinWidth)
		self._DesignParameter['METAL3_path_29']['_XYCoordinates'] = [[[(+ (self._DesignParameter['precharge_left_left_via34']['_XYCoordinates'][0][0] + self._DesignParameter['precharge_left_left_via34']['_DesignObj']._DesignParameter['_Met4Layer']['_XYCoordinates'][0][0])), (+ (self._DesignParameter['precharge_left_left_via34']['_XYCoordinates'][0][1] + self._DesignParameter['precharge_left_left_via34']['_DesignObj']._DesignParameter['_Met4Layer']['_XYCoordinates'][0][1]))], [(+ (self._DesignParameter['precharge_left_left_via34']['_XYCoordinates'][(- 1)][0] + self._DesignParameter['precharge_left_left_via34']['_DesignObj']._DesignParameter['_Met4Layer']['_XYCoordinates'][0][0])), (+ (self._DesignParameter['precharge_left_left_via34']['_XYCoordinates'][(- 1)][1] + self._DesignParameter['precharge_left_left_via34']['_DesignObj']._DesignParameter['_Met4Layer']['_XYCoordinates'][0][1]))]]]
		self._DesignParameter['METAL2_path_38'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _Width=drc._MetalxMinWidth)
		self._DesignParameter['METAL2_path_38']['_XYCoordinates'] = [[[(+ (self._DesignParameter['precharge_left_left_via34']['_XYCoordinates'][0][0] + self._DesignParameter['precharge_left_left_via34']['_DesignObj']._DesignParameter['_Met4Layer']['_XYCoordinates'][0][0])), (+ (self._DesignParameter['precharge_left_left_via34']['_XYCoordinates'][0][1] + self._DesignParameter['precharge_left_left_via34']['_DesignObj']._DesignParameter['_Met4Layer']['_XYCoordinates'][0][1]))], [(+ (self._DesignParameter['precharge_left_left_via34']['_XYCoordinates'][(- 1)][0] + self._DesignParameter['precharge_left_left_via34']['_DesignObj']._DesignParameter['_Met4Layer']['_XYCoordinates'][0][0])), (+ (self._DesignParameter['precharge_left_left_via34']['_XYCoordinates'][(- 1)][1] + self._DesignParameter['precharge_left_left_via34']['_DesignObj']._DesignParameter['_Met4Layer']['_XYCoordinates'][0][1]))]]]
		path_list = []
		if (len(self._DesignParameter['precharge_left_left_via34']['_XYCoordinates']) == 1):
		    mode = 'vertical'
		    _width = self._DesignParameter['precharge_left_left_via34']['_DesignObj']._DesignParameter['_Met4Layer']['_XWidth']
		elif (self._DesignParameter['precharge_left_left_via34']['_XYCoordinates'][0][0] == self._DesignParameter['precharge_left_left_via34']['_XYCoordinates'][(- 1)][0]):
		    mode = 'horizontal'
		    _width = self._DesignParameter['precharge_left_left_via34']['_DesignObj']._DesignParameter['_Met4Layer']['_XWidth']
		elif (self._DesignParameter['precharge_left_left_via34']['_XYCoordinates'][0][1] == self._DesignParameter['precharge_left_left_via34']['_XYCoordinates'][(- 1)][1]):
		    mode = 'vertical'
		    _width = self._DesignParameter['precharge_left_left_via34']['_DesignObj']._DesignParameter['_Met4Layer']['_XWidth']
		else:
		    print('Invalid Target Input')
		if (mode == 'vertical'):
		    xy_with_offset = []
		    target_y_value = (0 + self._DesignParameter['M2V2M3_inp_mos_drain']['_XYCoordinates'][0][1])
		    for i in range(len(self._DesignParameter['precharge_left_left_via34']['_XYCoordinates'])):
		        xy_with_offset.append([(x + y) for (x, y) in zip([0, 0], self._DesignParameter['precharge_left_left_via34']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		elif (mode == 'horizontal'):
		    xy_with_offset = []
		    target_x_value = (0 + self._DesignParameter['M2V2M3_inp_mos_drain']['_XYCoordinates'][0][0])
		    for i in range(len(self._DesignParameter['precharge_left_left_via34']['_XYCoordinates'])):
		        xy_with_offset.append([(x + y) for (x, y) in zip([0, 0], self._DesignParameter['precharge_left_left_via34']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		self._DesignParameter['left_precharge_met4_routing_array'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL4'][0], _Datatype=DesignParameters._LayerMapping['METAL4'][1], _Width=_width)
		self._DesignParameter['left_precharge_met4_routing_array']['_XYCoordinates'] = path_list
		precharge_via = max(1, (1 + int((((self._DesignParameter['pmos_right']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] - drc._VIAxMinSpace) - (2 * drc._VIAxMinEnclosureByMetx)) / (drc._VIAxMinWidth + drc._VIAxMinSpace)))))
		XYList = []
		xy_offset = (0, (- int(((drc._VIAxMinWidth + drc._VIAxMinSpace) / 4))))
		for element in self._DesignParameter['pmos_right']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0:precharge_inside_gate:2]:
		    element = (element[0] if (type(element[0]) == list) else element)
		    XYList.append([((x + y) + z) for (x, y, z) in zip([(0 + self._DesignParameter['pmos_right']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['pmos_right']['_XYCoordinates'][0][1])], element, xy_offset)])
		self._DesignParameter['precharge_right_left'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='precharge_right_leftIn{}'.format(_Name)))[0]
		self._DesignParameter['precharge_right_left']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(**dict(_ViaMet12Met2NumberOfCOX=1, _ViaMet12Met2NumberOfCOY=precharge_via))
		self._DesignParameter['precharge_right_left']['_XYCoordinates'] = XYList
		XYList = []
		xy_offset = (0, (- int(((drc._VIAxMinWidth + drc._VIAxMinSpace) / 4))))
		for element in self._DesignParameter['pmos_right']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][(- 1):None:(- 1)][1:precharge_outside_gate:2][(- 1):None:(- 1)]:
		    element = (element[0] if (type(element[0]) == list) else element)
		    XYList.append([((x + y) + z) for (x, y, z) in zip([(0 + self._DesignParameter['pmos_right']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['pmos_right']['_XYCoordinates'][0][1])], element, xy_offset)])
		self._DesignParameter['precharge_right_right_via34'] = self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_Name='precharge_right_right_via34In{}'.format(_Name)))[0]
		self._DesignParameter['precharge_right_right_via34']['_DesignObj']._CalculateViaMet32Met4DesignParameterMinimumEnclosureX(**dict(_ViaMet32Met4NumberOfCOX=1, _ViaMet32Met4NumberOfCOY=precharge_via))
		self._DesignParameter['precharge_right_right_via34']['_XYCoordinates'] = XYList
		XYList = []
		xy_offset = [0, 0]
		for i in range(len(self._DesignParameter['precharge_right_right_via34']['_XYCoordinates'])):
		    xy = (self._DesignParameter['precharge_right_right_via34']['_XYCoordinates'][i][0] if (type(self._DesignParameter['precharge_right_right_via34']['_XYCoordinates'][i][0]) == list) else self._DesignParameter['precharge_right_right_via34']['_XYCoordinates'][i])
		    XYList.append([((x + y) + z) for (x, y, z) in zip([0, 0], xy, xy_offset)])
		self._DesignParameter['precharge_right_right_via23'] = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_Name='precharge_right_right_via23In{}'.format(_Name)))[0]
		self._DesignParameter['precharge_right_right_via23']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureX(**dict(_ViaMet22Met3NumberOfCOX=1, _ViaMet22Met3NumberOfCOY=precharge_via))
		self._DesignParameter['precharge_right_right_via23']['_XYCoordinates'] = XYList
		XYList = []
		xy_offset = [0, 0]
		for i in range(len(self._DesignParameter['precharge_right_right_via34']['_XYCoordinates'])):
		    xy = (self._DesignParameter['precharge_right_right_via34']['_XYCoordinates'][i][0] if (type(self._DesignParameter['precharge_right_right_via34']['_XYCoordinates'][i][0]) == list) else self._DesignParameter['precharge_right_right_via34']['_XYCoordinates'][i])
		    XYList.append([((x + y) + z) for (x, y, z) in zip([0, 0], xy, xy_offset)])
		self._DesignParameter['precharge_right_right_via12'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='precharge_right_right_via12In{}'.format(_Name)))[0]
		self._DesignParameter['precharge_right_right_via12']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(**dict(_ViaMet12Met2NumberOfCOX=1, _ViaMet12Met2NumberOfCOY=precharge_via))
		self._DesignParameter['precharge_right_right_via12']['_XYCoordinates'] = XYList
		self._DesignParameter['PCCAM1_pmos_right'] = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_Name='PCCAM1_pmos_rightIn{}'.format(_Name)))[0]
		self._DesignParameter['PCCAM1_pmos_right']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(**dict(_ViaPoly2Met1NumberOfCOX=max(1, (1 + int(((((((self._DesignParameter['pmos_left']['_XYCoordinates'][0][0] + self._DesignParameter['pmos_left']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]) + (self._DesignParameter['pmos_left']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)) - ((self._DesignParameter['pmos_left']['_XYCoordinates'][0][0] + self._DesignParameter['pmos_left']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['pmos_left']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2))) - drc._CoMinSpace) - (2 * drc._CoMinEnclosureByPO)) / (drc._CoMinWidth + drc._CoMinSpace))))), _ViaPoly2Met1NumberOfCOY=1))
		self._DesignParameter['PCCAM1_pmos_right']['_XYCoordinates'] = [[self._DesignParameter['pmos_right']['_XYCoordinates'][0][0], ((((self._DesignParameter['pmos_left']['_XYCoordinates'][0][1] + self._DesignParameter['pmos_left']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) - (self._DesignParameter['pmos_left']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)) - drc._Metal1MinSpace2) - (self._DesignParameter['PCCAM1_pmos_left']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2))]]
		self._DesignParameter['M1V1M2_precharge_right_gate'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='M1V1M2_precharge_right_gateIn{}'.format(_Name)))[0]
		self._DesignParameter['M1V1M2_precharge_right_gate']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureY(**dict(_ViaMet12Met2NumberOfCOX=max(1, (1 + int(((((((self._DesignParameter['PCCAM1_pmos_right']['_XYCoordinates'][0][0] + self._DesignParameter['PCCAM1_pmos_right']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0]) + (self._DesignParameter['PCCAM1_pmos_right']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] / 2)) - ((self._DesignParameter['PCCAM1_pmos_right']['_XYCoordinates'][0][0] + self._DesignParameter['PCCAM1_pmos_right']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0]) - (self._DesignParameter['PCCAM1_pmos_right']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] / 2))) - drc._VIAxMinSpace) - (2 * drc._VIAxMinEnclosureByMetx)) / (drc._VIAxMinWidth + drc._VIAxMinSpace))))), _ViaMet12Met2NumberOfCOY=1))
		self._DesignParameter['M1V1M2_precharge_right_gate']['_XYCoordinates'] = [[self._DesignParameter['pmos_right']['_XYCoordinates'][0][0], ((((self._DesignParameter['pmos_left']['_XYCoordinates'][0][1] + self._DesignParameter['pmos_left']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) - (self._DesignParameter['pmos_left']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)) - drc._Metal1MinSpace2) - (self._DesignParameter['PCCAM1_pmos_left']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2))]]
		self._DesignParameter['M2V2M3_precharge_right_gate'] = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_Name='M2V2M3_precharge_right_gateIn{}'.format(_Name)))[0]
		self._DesignParameter['M2V2M3_precharge_right_gate']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureY(**dict(_ViaMet22Met3NumberOfCOX=max(1, (1 + int(((((((self._DesignParameter['PCCAM1_pmos_right']['_XYCoordinates'][0][0] + self._DesignParameter['PCCAM1_pmos_right']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0]) + (self._DesignParameter['PCCAM1_pmos_right']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] / 2)) - ((self._DesignParameter['PCCAM1_pmos_right']['_XYCoordinates'][0][0] + self._DesignParameter['PCCAM1_pmos_right']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0]) - (self._DesignParameter['PCCAM1_pmos_right']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] / 2))) - drc._VIAxMinSpace) - (2 * drc._VIAxMinEnclosureByMetx)) / (drc._VIAxMinWidth + drc._VIAxMinSpace))))), _ViaMet22Met3NumberOfCOY=1))
		self._DesignParameter['M2V2M3_precharge_right_gate']['_XYCoordinates'] = [[self._DesignParameter['pmos_right']['_XYCoordinates'][0][0], ((((self._DesignParameter['pmos_left']['_XYCoordinates'][0][1] + self._DesignParameter['pmos_left']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) - (self._DesignParameter['pmos_left']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)) - drc._Metal1MinSpace2) - (self._DesignParameter['PCCAM1_pmos_left']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2))]]
		self._DesignParameter['METAL1_boundary_359'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _XWidth=((- min(((self._DesignParameter['PCCAM1_pmos_right']['_XYCoordinates'][0][0] + self._DesignParameter['PCCAM1_pmos_right']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0]) - (self._DesignParameter['PCCAM1_pmos_right']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] / 2)), ((self._DesignParameter['M1V1M2_precharge_right_gate']['_XYCoordinates'][0][0] + self._DesignParameter['M1V1M2_precharge_right_gate']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0]) - (self._DesignParameter['M1V1M2_precharge_right_gate']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] / 2)))) + max(((self._DesignParameter['PCCAM1_pmos_right']['_XYCoordinates'][0][0] + self._DesignParameter['PCCAM1_pmos_right']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0]) + (self._DesignParameter['PCCAM1_pmos_right']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] / 2)), ((self._DesignParameter['M1V1M2_precharge_right_gate']['_XYCoordinates'][0][0] + self._DesignParameter['M1V1M2_precharge_right_gate']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0]) + (self._DesignParameter['M1V1M2_precharge_right_gate']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] / 2)))), _YWidth=(max(((self._DesignParameter['PCCAM1_pmos_right']['_XYCoordinates'][0][1] + self._DesignParameter['PCCAM1_pmos_right']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) + (self._DesignParameter['PCCAM1_pmos_right']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)), ((self._DesignParameter['M1V1M2_precharge_right_gate']['_XYCoordinates'][0][1] + self._DesignParameter['M1V1M2_precharge_right_gate']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) + (self._DesignParameter['M1V1M2_precharge_right_gate']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2))) + (- min(((self._DesignParameter['PCCAM1_pmos_right']['_XYCoordinates'][0][1] + self._DesignParameter['PCCAM1_pmos_right']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) - (self._DesignParameter['PCCAM1_pmos_right']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)), ((self._DesignParameter['M1V1M2_precharge_right_gate']['_XYCoordinates'][0][1] + self._DesignParameter['M1V1M2_precharge_right_gate']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) - (self._DesignParameter['M1V1M2_precharge_right_gate']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2))))))
		self._DesignParameter['METAL1_boundary_359']['_XYCoordinates'] = [[self._DesignParameter['pmos_right']['_XYCoordinates'][0][0], ((((self._DesignParameter['pmos_left']['_XYCoordinates'][0][1] + self._DesignParameter['pmos_left']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) - (self._DesignParameter['pmos_left']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)) - drc._Metal1MinSpace2) - (self._DesignParameter['PCCAM1_pmos_left']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2))]]
		self._DesignParameter['POLY_path_127'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _Width=self._DesignParameter['PCCAM1_pmos_right']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'])
		self._DesignParameter['POLY_path_127']['_XYCoordinates'] = [[[((self._DesignParameter['pmos_right']['_XYCoordinates'][0][0] + self._DesignParameter['pmos_right']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['pmos_right']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)), self._DesignParameter['METAL1_boundary_359']['_XYCoordinates'][0][1]], [((self._DesignParameter['pmos_right']['_XYCoordinates'][0][0] + self._DesignParameter['pmos_right']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]) + (self._DesignParameter['pmos_right']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)), self._DesignParameter['METAL1_boundary_359']['_XYCoordinates'][0][1]]]]
		path_list = []
		if (len(self._DesignParameter['pmos_right']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates']) == 1):
		    mode = 'vertical'
		    _width = self._DesignParameter['pmos_right']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
		elif (self._DesignParameter['pmos_right']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0] == self._DesignParameter['pmos_right']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]):
		    mode = 'horizontal'
		    _width = self._DesignParameter['pmos_right']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
		elif (self._DesignParameter['pmos_right']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1] == self._DesignParameter['pmos_right']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][1]):
		    mode = 'vertical'
		    _width = self._DesignParameter['pmos_right']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
		else:
		    print('Invalid Target Input')
		if (mode == 'vertical'):
		    xy_with_offset = []
		    target_y_value = (0 + self._DesignParameter['PCCAM1_pmos_right']['_XYCoordinates'][0][1])
		    for i in range(len(self._DesignParameter['pmos_right']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
		        xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['pmos_right']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['pmos_right']['_XYCoordinates'][0][1])], self._DesignParameter['pmos_right']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		elif (mode == 'horizontal'):
		    xy_with_offset = []
		    target_x_value = (0 + self._DesignParameter['PCCAM1_pmos_right']['_XYCoordinates'][0][0])
		    for i in range(len(self._DesignParameter['pmos_right']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
		        xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['pmos_right']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['pmos_right']['_XYCoordinates'][0][1])], self._DesignParameter['pmos_right']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		self._DesignParameter['precharge_right_mos_gate_array'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _Width=_width)
		self._DesignParameter['precharge_right_mos_gate_array']['_XYCoordinates'] = path_list
		self._DesignParameter['METAL4_path_20'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL4'][0], _Datatype=DesignParameters._LayerMapping['METAL4'][1], _Width=drc._MetalxMinWidth)
		self._DesignParameter['METAL4_path_20']['_XYCoordinates'] = [[[(+ self._DesignParameter['precharge_right_right_via12']['_XYCoordinates'][0][0]), (+ self._DesignParameter['precharge_right_right_via12']['_XYCoordinates'][0][1])], [(+ self._DesignParameter['precharge_right_right_via12']['_XYCoordinates'][(- 1)][0]), (+ self._DesignParameter['precharge_right_right_via12']['_XYCoordinates'][(- 1)][1])]]]
		self._DesignParameter['METAL3_path_28'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0], _Datatype=DesignParameters._LayerMapping['METAL3'][1], _Width=drc._MetalxMinWidth)
		self._DesignParameter['METAL3_path_28']['_XYCoordinates'] = [[[(+ self._DesignParameter['precharge_right_right_via12']['_XYCoordinates'][0][0]), (+ self._DesignParameter['precharge_right_right_via12']['_XYCoordinates'][0][1])], [(+ self._DesignParameter['precharge_right_right_via12']['_XYCoordinates'][(- 1)][0]), (+ self._DesignParameter['precharge_right_right_via12']['_XYCoordinates'][(- 1)][1])]]]
		self._DesignParameter['METAL2_path_37'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _Width=drc._MetalxMinWidth)
		self._DesignParameter['METAL2_path_37']['_XYCoordinates'] = [[[(+ self._DesignParameter['precharge_right_right_via12']['_XYCoordinates'][0][0]), (+ self._DesignParameter['precharge_right_right_via12']['_XYCoordinates'][0][1])], [(+ self._DesignParameter['precharge_right_right_via12']['_XYCoordinates'][(- 1)][0]), (+ self._DesignParameter['precharge_right_right_via12']['_XYCoordinates'][(- 1)][1])]]]
		path_list = []
		if (len(self._DesignParameter['precharge_right_right_via34']['_XYCoordinates']) == 1):
		    mode = 'vertical'
		    _width = self._DesignParameter['precharge_right_right_via34']['_DesignObj']._DesignParameter['_Met4Layer']['_XWidth']
		elif (self._DesignParameter['precharge_right_right_via34']['_XYCoordinates'][0][0] == self._DesignParameter['precharge_right_right_via34']['_XYCoordinates'][(- 1)][0]):
		    mode = 'horizontal'
		    _width = self._DesignParameter['precharge_right_right_via34']['_DesignObj']._DesignParameter['_Met4Layer']['_XWidth']
		elif (self._DesignParameter['precharge_right_right_via34']['_XYCoordinates'][0][1] == self._DesignParameter['precharge_right_right_via34']['_XYCoordinates'][(- 1)][1]):
		    mode = 'vertical'
		    _width = self._DesignParameter['precharge_right_right_via34']['_DesignObj']._DesignParameter['_Met4Layer']['_XWidth']
		else:
		    print('Invalid Target Input')
		if (mode == 'vertical'):
		    xy_with_offset = []
		    target_y_value = (0 + self._DesignParameter['M2V2M3_inn_mos_drain']['_XYCoordinates'][0][1])
		    for i in range(len(self._DesignParameter['precharge_right_right_via34']['_XYCoordinates'])):
		        xy_with_offset.append([(x + y) for (x, y) in zip([0, 0], self._DesignParameter['precharge_right_right_via34']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		elif (mode == 'horizontal'):
		    xy_with_offset = []
		    target_x_value = (0 + self._DesignParameter['M2V2M3_inn_mos_drain']['_XYCoordinates'][0][0])
		    for i in range(len(self._DesignParameter['precharge_right_right_via34']['_XYCoordinates'])):
		        xy_with_offset.append([(x + y) for (x, y) in zip([0, 0], self._DesignParameter['precharge_right_right_via34']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		self._DesignParameter['right_precharge_met4_routing_arrayo'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL4'][0], _Datatype=DesignParameters._LayerMapping['METAL4'][1], _Width=_width)
		self._DesignParameter['right_precharge_met4_routing_arrayo']['_XYCoordinates'] = path_list
		precharge_via = max(1, (1 + int((((self._DesignParameter['pmos_mid_left']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] - drc._VIAxMinSpace) - (2 * drc._VIAxMinEnclosureByMetx)) / (drc._VIAxMinWidth + drc._VIAxMinSpace)))))
		XYList = []
		xy_offset = (0, (- int(((drc._VIAxMinWidth + drc._VIAxMinSpace) / 4))))
		for i in range(len(self._DesignParameter['pmos_mid_left']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'])):
		    if ((i % 2) == 0):
		        xy = (self._DesignParameter['pmos_mid_left']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i][0] if (type(self._DesignParameter['pmos_mid_left']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i][0]) == list) else self._DesignParameter['pmos_mid_left']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i])
		        XYList.append([((x + y) + z) for (x, y, z) in zip([(0 + self._DesignParameter['pmos_mid_left']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['pmos_mid_left']['_XYCoordinates'][0][1])], xy, xy_offset)])
		self._DesignParameter['pmos_mid_left_drain_via'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='pmos_mid_left_drain_viaIn{}'.format(_Name)))[0]
		self._DesignParameter['pmos_mid_left_drain_via']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(**dict(_ViaMet12Met2NumberOfCOX=1, _ViaMet12Met2NumberOfCOY=precharge_via))
		self._DesignParameter['pmos_mid_left_drain_via']['_XYCoordinates'] = XYList
		XYList = []
		xy_offset = [0, 0]
		for i in range(len(self._DesignParameter['pmos_mid_right']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'])):
		    if ((i % 2) == 0):
		        xy = (self._DesignParameter['pmos_mid_right']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i][0] if (type(self._DesignParameter['pmos_mid_right']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i][0]) == list) else self._DesignParameter['pmos_mid_right']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i])
		        XYList.append([((x + y) + z) for (x, y, z) in zip([(0 + self._DesignParameter['pmos_mid_right']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['pmos_mid_right']['_XYCoordinates'][0][1])], xy, xy_offset)])
		self._DesignParameter['pmos_mid_right_drain_via'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='pmos_mid_right_drain_viaIn{}'.format(_Name)))[0]
		self._DesignParameter['pmos_mid_right_drain_via']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(**dict(_ViaMet12Met2NumberOfCOX=1, _ViaMet12Met2NumberOfCOY=precharge_via))
		self._DesignParameter['pmos_mid_right_drain_via']['_XYCoordinates'] = XYList
		self._DesignParameter['METAL2_path_40'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _Width=drc._MetalxMinWidth)
		self._DesignParameter['METAL2_path_40']['_XYCoordinates'] = [[[(+ self._DesignParameter['precharge_left_right']['_XYCoordinates'][0][0]), (+ self._DesignParameter['precharge_left_right']['_XYCoordinates'][0][1])], [self._DesignParameter['pmos_mid_left_drain_via']['_XYCoordinates'][(- 1)][0], self._DesignParameter['precharge_left_right']['_XYCoordinates'][0][1]]]]
		self._DesignParameter['METAL2_path_39'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _Width=drc._MetalxMinWidth)
		self._DesignParameter['METAL2_path_39']['_XYCoordinates'] = [[[(+ self._DesignParameter['precharge_right_left']['_XYCoordinates'][(- 1)][0]), (+ self._DesignParameter['precharge_right_left']['_XYCoordinates'][(- 1)][1])], [self._DesignParameter['pmos_mid_right_drain_via']['_XYCoordinates'][0][0], self._DesignParameter['precharge_right_left']['_XYCoordinates'][(- 1)][1]]]]
		self._DesignParameter['PCCAM1_mid_pmos_left'] = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_Name='PCCAM1_mid_pmos_leftIn{}'.format(_Name)))[0]
		self._DesignParameter['PCCAM1_mid_pmos_left']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(**dict(_ViaPoly2Met1NumberOfCOX=max(1, (1 + int(((((((self._DesignParameter['pmos_mid_left']['_XYCoordinates'][0][0] + self._DesignParameter['pmos_mid_left']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]) + (self._DesignParameter['pmos_mid_left']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)) - ((self._DesignParameter['pmos_mid_left']['_XYCoordinates'][0][0] + self._DesignParameter['pmos_mid_left']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['pmos_mid_left']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2))) - drc._CoMinSpace) - (2 * drc._CoMinEnclosureByPO)) / (drc._CoMinWidth + drc._CoMinSpace))))), _ViaPoly2Met1NumberOfCOY=1))
		self._DesignParameter['PCCAM1_mid_pmos_left']['_XYCoordinates'] = [[self._DesignParameter['pmos_mid_left']['_XYCoordinates'][0][0], self._DesignParameter['PCCAM1_pmos_left']['_XYCoordinates'][0][1]]]
		self._DesignParameter['PCCAM1_mid_pmos_right'] = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_Name='PCCAM1_mid_pmos_rightIn{}'.format(_Name)))[0]
		self._DesignParameter['PCCAM1_mid_pmos_right']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(**dict(_ViaPoly2Met1NumberOfCOX=max(1, (1 + int((((((self._DesignParameter['pmos_mid_right']['_XYCoordinates'][0][1] + self._DesignParameter['pmos_mid_right']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][1]) - (self._DesignParameter['pmos_mid_right']['_XYCoordinates'][0][1] + self._DesignParameter['pmos_mid_right']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1])) - drc._CoMinSpace) - (2 * drc._CoMinEnclosureByPO)) / (drc._CoMinWidth + drc._CoMinSpace))))), _ViaPoly2Met1NumberOfCOY=1))
		self._DesignParameter['PCCAM1_mid_pmos_right']['_XYCoordinates'] = [[self._DesignParameter['pmos_mid_right']['_XYCoordinates'][0][0], self._DesignParameter['PCCAM1_pmos_right']['_XYCoordinates'][0][1]]]
		self._DesignParameter['POLY_path_126'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _Width=self._DesignParameter['PCCAM1_mid_pmos_left']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'])
		self._DesignParameter['POLY_path_126']['_XYCoordinates'] = [[[((self._DesignParameter['pmos_mid_left']['_XYCoordinates'][0][0] + self._DesignParameter['pmos_mid_left']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['pmos_mid_left']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)), self._DesignParameter['PCCAM1_mid_pmos_left']['_XYCoordinates'][0][1]], [((self._DesignParameter['pmos_mid_left']['_XYCoordinates'][0][0] + self._DesignParameter['pmos_mid_left']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]) + (self._DesignParameter['pmos_mid_left']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)), self._DesignParameter['PCCAM1_mid_pmos_left']['_XYCoordinates'][0][1]]]]
		self._DesignParameter['POLY_path_125'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _Width=self._DesignParameter['PCCAM1_mid_pmos_left']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'])
		self._DesignParameter['POLY_path_125']['_XYCoordinates'] = [[[((self._DesignParameter['pmos_mid_right']['_XYCoordinates'][0][0] + self._DesignParameter['pmos_mid_right']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['pmos_mid_right']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)), self._DesignParameter['PCCAM1_mid_pmos_right']['_XYCoordinates'][0][1]], [((self._DesignParameter['pmos_mid_right']['_XYCoordinates'][0][0] + self._DesignParameter['pmos_mid_right']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]) + (self._DesignParameter['pmos_mid_right']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)), self._DesignParameter['PCCAM1_mid_pmos_right']['_XYCoordinates'][0][1]]]]
		path_list = []
		if (len(self._DesignParameter['pmos_mid_left']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates']) == 1):
		    mode = 'vertical'
		    _width = self._DesignParameter['pmos_mid_left']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
		elif (self._DesignParameter['pmos_mid_left']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0] == self._DesignParameter['pmos_mid_left']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]):
		    mode = 'horizontal'
		    _width = self._DesignParameter['pmos_mid_left']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
		elif (self._DesignParameter['pmos_mid_left']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1] == self._DesignParameter['pmos_mid_left']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][1]):
		    mode = 'vertical'
		    _width = self._DesignParameter['pmos_mid_left']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
		else:
		    print('Invalid Target Input')
		if (mode == 'vertical'):
		    xy_with_offset = []
		    target_y_value = (0 + self._DesignParameter['PCCAM1_mid_pmos_left']['_XYCoordinates'][0][1])
		    for i in range(len(self._DesignParameter['pmos_mid_left']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
		        xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['pmos_mid_left']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['pmos_mid_left']['_XYCoordinates'][0][1])], self._DesignParameter['pmos_mid_left']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		elif (mode == 'horizontal'):
		    xy_with_offset = []
		    target_x_value = (0 + self._DesignParameter['PCCAM1_mid_pmos_left']['_XYCoordinates'][0][0])
		    for i in range(len(self._DesignParameter['pmos_mid_left']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
		        xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['pmos_mid_left']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['pmos_mid_left']['_XYCoordinates'][0][1])], self._DesignParameter['pmos_mid_left']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		self._DesignParameter['pmos_mid_left_gate_array'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _Width=_width)
		self._DesignParameter['pmos_mid_left_gate_array']['_XYCoordinates'] = path_list
		path_list = []
		if (len(self._DesignParameter['pmos_mid_right']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates']) == 1):
		    mode = 'vertical'
		    _width = self._DesignParameter['pmos_mid_right']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
		elif (self._DesignParameter['pmos_mid_right']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0] == self._DesignParameter['pmos_mid_right']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]):
		    mode = 'horizontal'
		    _width = self._DesignParameter['pmos_mid_right']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
		elif (self._DesignParameter['pmos_mid_right']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1] == self._DesignParameter['pmos_mid_right']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][1]):
		    mode = 'vertical'
		    _width = self._DesignParameter['pmos_mid_right']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
		else:
		    print('Invalid Target Input')
		if (mode == 'vertical'):
		    xy_with_offset = []
		    target_y_value = (0 + self._DesignParameter['PCCAM1_mid_pmos_right']['_XYCoordinates'][0][1])
		    for i in range(len(self._DesignParameter['pmos_mid_right']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
		        xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['pmos_mid_right']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['pmos_mid_right']['_XYCoordinates'][0][1])], self._DesignParameter['pmos_mid_right']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		elif (mode == 'horizontal'):
		    xy_with_offset = []
		    target_x_value = (0 + self._DesignParameter['PCCAM1_mid_pmos_right']['_XYCoordinates'][0][0])
		    for i in range(len(self._DesignParameter['pmos_mid_right']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
		        xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['pmos_mid_right']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['pmos_mid_right']['_XYCoordinates'][0][1])], self._DesignParameter['pmos_mid_right']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		self._DesignParameter['pmos_mid_right_gate_array'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _Width=_width)
		self._DesignParameter['pmos_mid_right_gate_array']['_XYCoordinates'] = path_list
		self._DesignParameter['M2V2M3_mid_left_pmos'] = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_Name='M2V2M3_mid_left_pmosIn{}'.format(_Name)))[0]
		self._DesignParameter['M2V2M3_mid_left_pmos']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureX(**dict(_ViaMet22Met3NumberOfCOX=1, _ViaMet22Met3NumberOfCOY=precharge_via))
		self._DesignParameter['M2V2M3_mid_left_pmos']['_XYCoordinates'] = [[(+ self._DesignParameter['pmos_mid_left_drain_via']['_XYCoordinates'][(- 1)][0]), (+ self._DesignParameter['pmos_mid_left_drain_via']['_XYCoordinates'][(- 1)][1])]]
		self._DesignParameter['M3V3M4_mid_left_pmos'] = self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_Name='M3V3M4_mid_left_pmosIn{}'.format(_Name)))[0]
		self._DesignParameter['M3V3M4_mid_left_pmos']['_DesignObj']._CalculateViaMet32Met4DesignParameterMinimumEnclosureX(**dict(_ViaMet32Met4NumberOfCOX=1, _ViaMet32Met4NumberOfCOY=precharge_via))
		self._DesignParameter['M3V3M4_mid_left_pmos']['_XYCoordinates'] = [[(+ self._DesignParameter['pmos_mid_left_drain_via']['_XYCoordinates'][(- 1)][0]), (+ self._DesignParameter['pmos_mid_left_drain_via']['_XYCoordinates'][(- 1)][1])]]
		self._DesignParameter['M2V2M3_mid_right_pmos'] = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_Name='M2V2M3_mid_right_pmosIn{}'.format(_Name)))[0]
		self._DesignParameter['M2V2M3_mid_right_pmos']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureX(**dict(_ViaMet22Met3NumberOfCOX=1, _ViaMet22Met3NumberOfCOY=precharge_via))
		self._DesignParameter['M2V2M3_mid_right_pmos']['_XYCoordinates'] = [[(+ self._DesignParameter['pmos_mid_right_drain_via']['_XYCoordinates'][0][0]), (+ self._DesignParameter['pmos_mid_right_drain_via']['_XYCoordinates'][0][1])]]
		self._DesignParameter['M3V3M4_mid_right_pmos'] = self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_Name='M3V3M4_mid_right_pmosIn{}'.format(_Name)))[0]
		self._DesignParameter['M3V3M4_mid_right_pmos']['_DesignObj']._CalculateViaMet32Met4DesignParameterMinimumEnclosureX(**dict(_ViaMet32Met4NumberOfCOX=1, _ViaMet32Met4NumberOfCOY=precharge_via))
		self._DesignParameter['M3V3M4_mid_right_pmos']['_XYCoordinates'] = [[(+ self._DesignParameter['pmos_mid_right_drain_via']['_XYCoordinates'][0][0]), (+ self._DesignParameter['pmos_mid_right_drain_via']['_XYCoordinates'][0][1])]]
		self._DesignParameter['METAL4_path_19'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL4'][0], _Datatype=DesignParameters._LayerMapping['METAL4'][1], _Width=(drc._MetalxMinWidth * 2))
		self._DesignParameter['METAL4_path_19']['_XYCoordinates'] = [[[(+ (self._DesignParameter['M2V2M3_mid_left_pmos']['_XYCoordinates'][0][0] + self._DesignParameter['M2V2M3_mid_left_pmos']['_DesignObj']._DesignParameter['_Met2Layer']['_XYCoordinates'][0][0])), (+ ((self._DesignParameter['M2V2M3_mid_left_pmos']['_XYCoordinates'][0][1] + self._DesignParameter['M2V2M3_mid_left_pmos']['_DesignObj']._DesignParameter['_Met2Layer']['_XYCoordinates'][0][1]) + (self._DesignParameter['M2V2M3_mid_left_pmos']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] / 2)))], [(self._DesignParameter['M2V2M3_mid_left_pmos']['_XYCoordinates'][0][0] + self._DesignParameter['M2V2M3_mid_left_pmos']['_DesignObj']._DesignParameter['_Met2Layer']['_XYCoordinates'][0][0]), ((self._DesignParameter['M2V2M3_mid_mos_left']['_XYCoordinates'][0][1] + self._DesignParameter['M2V2M3_mid_mos_left']['_DesignObj']._DesignParameter['_Met2Layer']['_XYCoordinates'][0][1]) - (self._DesignParameter['M2V2M3_mid_mos_left']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] / 2))]]]
		self._DesignParameter['METAL4_path_18'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL4'][0], _Datatype=DesignParameters._LayerMapping['METAL4'][1], _Width=(drc._MetalxMinWidth * 2))
		self._DesignParameter['METAL4_path_18']['_XYCoordinates'] = [[[(+ (self._DesignParameter['M2V2M3_mid_right_pmos']['_XYCoordinates'][0][0] + self._DesignParameter['M2V2M3_mid_right_pmos']['_DesignObj']._DesignParameter['_Met2Layer']['_XYCoordinates'][0][0])), (+ ((self._DesignParameter['M2V2M3_mid_right_pmos']['_XYCoordinates'][0][1] + self._DesignParameter['M2V2M3_mid_right_pmos']['_DesignObj']._DesignParameter['_Met2Layer']['_XYCoordinates'][0][1]) + (self._DesignParameter['M2V2M3_mid_right_pmos']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] / 2)))], [(self._DesignParameter['M2V2M3_mid_right_pmos']['_XYCoordinates'][0][0] + self._DesignParameter['M2V2M3_mid_right_pmos']['_DesignObj']._DesignParameter['_Met2Layer']['_XYCoordinates'][0][0]), ((self._DesignParameter['M2V2M3_mid_mos_right']['_XYCoordinates'][0][1] + self._DesignParameter['M2V2M3_mid_mos_right']['_DesignObj']._DesignParameter['_Met2Layer']['_XYCoordinates'][0][1]) - (self._DesignParameter['M2V2M3_mid_mos_right']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] / 2))]]]
		self._DesignParameter['M1V1M2_mid_left_pmos_gate'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='M1V1M2_mid_left_pmos_gateIn{}'.format(_Name)))[0]
		self._DesignParameter['M1V1M2_mid_left_pmos_gate']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureY(**dict(_ViaMet12Met2NumberOfCOX=2, _ViaMet12Met2NumberOfCOY=1))
		self._DesignParameter['M1V1M2_mid_left_pmos_gate']['_XYCoordinates'] = [[(+ self._DesignParameter['PCCAM1_mid_pmos_left']['_XYCoordinates'][0][0]), (+ self._DesignParameter['PCCAM1_mid_pmos_left']['_XYCoordinates'][0][1])]]
		self._DesignParameter['M1V1M2_mid_right_pmos_gate'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='M1V1M2_mid_right_pmos_gateIn{}'.format(_Name)))[0]
		self._DesignParameter['M1V1M2_mid_right_pmos_gate']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureY(**dict(_ViaMet12Met2NumberOfCOX=2, _ViaMet12Met2NumberOfCOY=1))
		self._DesignParameter['M1V1M2_mid_right_pmos_gate']['_XYCoordinates'] = [[(+ self._DesignParameter['PCCAM1_mid_pmos_right']['_XYCoordinates'][0][0]), (+ self._DesignParameter['PCCAM1_mid_pmos_right']['_XYCoordinates'][0][1])]]
		self._DesignParameter['METAL1_boundary_358'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _XWidth=max(self._DesignParameter['M1V1M2_mid_left_pmos_gate']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'], self._DesignParameter['PCCAM1_mid_pmos_left']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']), _YWidth=(max(((self._DesignParameter['PCCAM1_mid_pmos_left']['_XYCoordinates'][0][1] + self._DesignParameter['PCCAM1_mid_pmos_left']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) + (self._DesignParameter['PCCAM1_mid_pmos_left']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)), ((self._DesignParameter['M1V1M2_mid_left_pmos_gate']['_XYCoordinates'][0][1] + self._DesignParameter['M1V1M2_mid_left_pmos_gate']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) + (self._DesignParameter['M1V1M2_mid_left_pmos_gate']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2))) + (- min(((self._DesignParameter['PCCAM1_mid_pmos_left']['_XYCoordinates'][0][1] + self._DesignParameter['PCCAM1_mid_pmos_left']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) - (self._DesignParameter['PCCAM1_mid_pmos_left']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)), ((self._DesignParameter['M1V1M2_mid_left_pmos_gate']['_XYCoordinates'][0][1] + self._DesignParameter['M1V1M2_mid_left_pmos_gate']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) - (self._DesignParameter['M1V1M2_mid_left_pmos_gate']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2))))))
		self._DesignParameter['METAL1_boundary_358']['_XYCoordinates'] = [[(+ self._DesignParameter['PCCAM1_mid_pmos_left']['_XYCoordinates'][0][0]), (+ self._DesignParameter['PCCAM1_mid_pmos_left']['_XYCoordinates'][0][1])]]
		self._DesignParameter['METAL1_boundary_357'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _XWidth=max(self._DesignParameter['M1V1M2_mid_left_pmos_gate']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'], self._DesignParameter['PCCAM1_mid_pmos_left']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']), _YWidth=(max(((self._DesignParameter['PCCAM1_mid_pmos_left']['_XYCoordinates'][0][1] + self._DesignParameter['PCCAM1_mid_pmos_left']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) + (self._DesignParameter['PCCAM1_mid_pmos_left']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)), ((self._DesignParameter['M1V1M2_mid_left_pmos_gate']['_XYCoordinates'][0][1] + self._DesignParameter['M1V1M2_mid_left_pmos_gate']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) + (self._DesignParameter['M1V1M2_mid_left_pmos_gate']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2))) + (- min(((self._DesignParameter['PCCAM1_mid_pmos_left']['_XYCoordinates'][0][1] + self._DesignParameter['PCCAM1_mid_pmos_left']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) - (self._DesignParameter['PCCAM1_mid_pmos_left']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)), ((self._DesignParameter['M1V1M2_mid_left_pmos_gate']['_XYCoordinates'][0][1] + self._DesignParameter['M1V1M2_mid_left_pmos_gate']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) - (self._DesignParameter['M1V1M2_mid_left_pmos_gate']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2))))))
		self._DesignParameter['METAL1_boundary_357']['_XYCoordinates'] = [[(+ self._DesignParameter['PCCAM1_mid_pmos_right']['_XYCoordinates'][0][0]), (+ self._DesignParameter['PCCAM1_mid_pmos_right']['_XYCoordinates'][0][1])]]
		self._DesignParameter['METAL2_path_35'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _Width=(drc._MetalxMinWidth * 2))
		self._DesignParameter['METAL2_path_35']['_XYCoordinates'] = [[[(+ (self._DesignParameter['M1V1M2_mid_left_pmos_gate']['_XYCoordinates'][0][0] + self._DesignParameter['M1V1M2_mid_left_pmos_gate']['_DesignObj']._DesignParameter['_Met2Layer']['_XYCoordinates'][0][0])), (+ ((self._DesignParameter['M1V1M2_mid_left_pmos_gate']['_XYCoordinates'][0][1] + self._DesignParameter['M1V1M2_mid_left_pmos_gate']['_DesignObj']._DesignParameter['_Met2Layer']['_XYCoordinates'][0][1]) + (self._DesignParameter['M1V1M2_mid_left_pmos_gate']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] / 2)))], [(self._DesignParameter['M1V1M2_mid_left_pmos_gate']['_XYCoordinates'][0][0] + self._DesignParameter['M1V1M2_mid_left_pmos_gate']['_DesignObj']._DesignParameter['_Met2Layer']['_XYCoordinates'][0][0]), ((self._DesignParameter['M1V1M2_mid_mos_left_gate']['_XYCoordinates'][0][1] + self._DesignParameter['M1V1M2_mid_mos_left_gate']['_DesignObj']._DesignParameter['_Met2Layer']['_XYCoordinates'][0][1]) - (self._DesignParameter['M1V1M2_mid_mos_left_gate']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] / 2))]]]
		self._DesignParameter['METAL2_path_34'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _Width=(drc._MetalxMinWidth * 2))
		self._DesignParameter['METAL2_path_34']['_XYCoordinates'] = [[[(+ (self._DesignParameter['M1V1M2_mid_right_pmos_gate']['_XYCoordinates'][0][0] + self._DesignParameter['M1V1M2_mid_right_pmos_gate']['_DesignObj']._DesignParameter['_Met2Layer']['_XYCoordinates'][0][0])), (+ ((self._DesignParameter['M1V1M2_mid_right_pmos_gate']['_XYCoordinates'][0][1] + self._DesignParameter['M1V1M2_mid_right_pmos_gate']['_DesignObj']._DesignParameter['_Met2Layer']['_XYCoordinates'][0][1]) + (self._DesignParameter['M1V1M2_mid_right_pmos_gate']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] / 2)))], [(self._DesignParameter['M1V1M2_mid_right_pmos_gate']['_XYCoordinates'][0][0] + self._DesignParameter['M1V1M2_mid_right_pmos_gate']['_DesignObj']._DesignParameter['_Met2Layer']['_XYCoordinates'][0][0]), ((self._DesignParameter['M1V1M2_mid_mos_right_gate']['_XYCoordinates'][0][1] + self._DesignParameter['M1V1M2_mid_mos_right_gate']['_DesignObj']._DesignParameter['_Met2Layer']['_XYCoordinates'][0][1]) - (self._DesignParameter['M1V1M2_mid_mos_right_gate']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] / 2))]]]
		self._DesignParameter['M3V3M4_clk_lt'] = self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_Name='M3V3M4_clk_ltIn{}'.format(_Name)))[0]
		self._DesignParameter['M3V3M4_clk_lt']['_DesignObj']._CalculateViaMet32Met4DesignParameterMinimumEnclosureX(**dict(_ViaMet32Met4NumberOfCOX=1, _ViaMet32Met4NumberOfCOY=2))
		self._DesignParameter['M3V3M4_clk_lt']['_XYCoordinates'] = [[(((((self._DesignParameter['M3V3M4_mid_node']['_XYCoordinates'][0][0] + self._DesignParameter['M3V3M4_mid_node']['_DesignObj']._DesignParameter['_Met4Layer']['_XYCoordinates'][0][0]) - (self._DesignParameter['M3V3M4_mid_node']['_DesignObj']._DesignParameter['_Met4Layer']['_XWidth'] / 2)) - drc._MetalxMinWidth) - drc._MetalxMinSpace2) + (- self._DesignParameter['M3V3M4_clk_lt']['_DesignObj']._DesignParameter['_Met4Layer']['_XWidth'])), ((((- self._DesignParameter['M3V3M4_clk_lt']['_DesignObj']._DesignParameter['_Met4Layer']['_YWidth']) / 2) + (self._DesignParameter['M1V1M2_mid_left_pmos_gate']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] / 2)) + self._DesignParameter['M1V1M2_mid_left_pmos_gate']['_XYCoordinates'][0][1])]]
		self._DesignParameter['M3V3M4_clk_rt'] = self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_Name='M3V3M4_clk_rtIn{}'.format(_Name)))[0]
		self._DesignParameter['M3V3M4_clk_rt']['_DesignObj']._CalculateViaMet32Met4DesignParameterMinimumEnclosureX(**dict(_ViaMet32Met4NumberOfCOX=1, _ViaMet32Met4NumberOfCOY=2))
		self._DesignParameter['M3V3M4_clk_rt']['_XYCoordinates'] = [[(((((self._DesignParameter['M3V3M4_mid_node']['_XYCoordinates'][0][0] + self._DesignParameter['M3V3M4_mid_node']['_DesignObj']._DesignParameter['_Met4Layer']['_XYCoordinates'][0][0]) + (self._DesignParameter['M3V3M4_mid_node']['_DesignObj']._DesignParameter['_Met4Layer']['_XWidth'] / 2)) + drc._MetalxMinWidth) + drc._MetalxMinSpace2) + self._DesignParameter['M3V3M4_clk_rt']['_DesignObj']._DesignParameter['_Met4Layer']['_XWidth']), ((self._DesignParameter['M1V1M2_mid_right_pmos_gate']['_XYCoordinates'][0][1] + (self._DesignParameter['M1V1M2_mid_right_pmos_gate']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] / 2)) + ((- self._DesignParameter['M3V3M4_clk_rt']['_DesignObj']._DesignParameter['_Met4Layer']['_YWidth']) / 2))]]
		self._DesignParameter['METAL3_path_32'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0], _Datatype=DesignParameters._LayerMapping['METAL3'][1], _Width=(drc._MetalxMinWidth * 2))
		self._DesignParameter['METAL3_path_32']['_XYCoordinates'] = [[[(+ ((self._DesignParameter['M2V2M3_CDNS_6375475055672_1']['_XYCoordinates'][0][0] + self._DesignParameter['M2V2M3_CDNS_6375475055672_1']['_DesignObj']._DesignParameter['_Met3Layer']['_XYCoordinates'][0][0]) - (self._DesignParameter['M2V2M3_CDNS_6375475055672_1']['_DesignObj']._DesignParameter['_Met3Layer']['_XWidth'] / 2))), (((- (self._DesignParameter['METAL3_path_32']['_Width'] - self._DesignParameter['M2V2M3_CDNS_6375475055672_1']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth'])) / 2) + (self._DesignParameter['M2V2M3_CDNS_6375475055672_1']['_XYCoordinates'][0][1] + self._DesignParameter['M2V2M3_CDNS_6375475055672_1']['_DesignObj']._DesignParameter['_Met3Layer']['_XYCoordinates'][0][1]))], [self._DesignParameter['M3V3M4_clk_lt']['_XYCoordinates'][0][0], (((- (self._DesignParameter['METAL3_path_32']['_Width'] - self._DesignParameter['M2V2M3_CDNS_6375475055672_1']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth'])) / 2) + (self._DesignParameter['M2V2M3_CDNS_6375475055672_1']['_XYCoordinates'][0][1] + self._DesignParameter['M2V2M3_CDNS_6375475055672_1']['_DesignObj']._DesignParameter['_Met3Layer']['_XYCoordinates'][0][1]))]]]
		self._DesignParameter['METAL3_path_31'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0], _Datatype=DesignParameters._LayerMapping['METAL3'][1], _Width=100)
		self._DesignParameter['METAL3_path_31']['_XYCoordinates'] = [[[(+ ((self._DesignParameter['M2V2M3_precharge_right_gate']['_XYCoordinates'][0][0] + self._DesignParameter['M2V2M3_precharge_right_gate']['_DesignObj']._DesignParameter['_Met3Layer']['_XYCoordinates'][0][0]) + (self._DesignParameter['M2V2M3_precharge_right_gate']['_DesignObj']._DesignParameter['_Met3Layer']['_XWidth'] / 2))), (((- (self._DesignParameter['METAL3_path_31']['_Width'] - self._DesignParameter['M2V2M3_precharge_right_gate']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth'])) / 2) + (self._DesignParameter['M2V2M3_precharge_right_gate']['_XYCoordinates'][0][1] + self._DesignParameter['M2V2M3_precharge_right_gate']['_DesignObj']._DesignParameter['_Met3Layer']['_XYCoordinates'][0][1]))], [self._DesignParameter['M3V3M4_clk_rt']['_XYCoordinates'][0][0], (((- (self._DesignParameter['METAL3_path_31']['_Width'] - self._DesignParameter['M2V2M3_precharge_right_gate']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth'])) / 2) + (self._DesignParameter['M2V2M3_precharge_right_gate']['_XYCoordinates'][0][1] + self._DesignParameter['M2V2M3_precharge_right_gate']['_DesignObj']._DesignParameter['_Met3Layer']['_XYCoordinates'][0][1]))]]]
		self._DesignParameter['M3V3M4_clk_ld'] = self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_Name='M3V3M4_clk_ldIn{}'.format(_Name)))[0]
		self._DesignParameter['M3V3M4_clk_ld']['_DesignObj']._CalculateViaMet32Met4DesignParameterMinimumEnclosureX(**dict(_ViaMet32Met4NumberOfCOX=1, _ViaMet32Met4NumberOfCOY=2))
		self._DesignParameter['M3V3M4_clk_ld']['_XYCoordinates'] = [[self._DesignParameter['M3V3M4_clk_lt']['_XYCoordinates'][0][0], ((self._DesignParameter['M2V2M3_bot_nmos_gate']['_XYCoordinates'][0][1] + self._DesignParameter['M2V2M3_bot_nmos_gate']['_DesignObj']._DesignParameter['_Met2Layer']['_XYCoordinates'][0][1]) + ((self._DesignParameter['M3V3M4_clk_ld']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth'] - self._DesignParameter['M2V2M3_bot_nmos_gate']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth']) / 2))]]
		self._DesignParameter['M3V3M4_clk_rd'] = self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_Name='M3V3M4_clk_rdIn{}'.format(_Name)))[0]
		self._DesignParameter['M3V3M4_clk_rd']['_DesignObj']._CalculateViaMet32Met4DesignParameterMinimumEnclosureX(**dict(_ViaMet32Met4NumberOfCOX=1, _ViaMet32Met4NumberOfCOY=2))
		self._DesignParameter['M3V3M4_clk_rd']['_XYCoordinates'] = [[self._DesignParameter['M3V3M4_clk_rt']['_XYCoordinates'][0][0], ((self._DesignParameter['M2V2M3_bot_nmos_gate']['_XYCoordinates'][0][1] + self._DesignParameter['M2V2M3_bot_nmos_gate']['_DesignObj']._DesignParameter['_Met2Layer']['_XYCoordinates'][0][1]) + ((self._DesignParameter['M3V3M4_clk_ld']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth'] - self._DesignParameter['M2V2M3_bot_nmos_gate']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth']) / 2))]]
		self._DesignParameter['METAL4_path_16'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL4'][0], _Datatype=DesignParameters._LayerMapping['METAL4'][1], _Width=(drc._MetalxMinWidth * 2))
		self._DesignParameter['METAL4_path_16']['_XYCoordinates'] = [[[(+ (self._DesignParameter['M3V3M4_clk_lt']['_XYCoordinates'][0][0] + self._DesignParameter['M3V3M4_clk_lt']['_DesignObj']._DesignParameter['_Met4Layer']['_XYCoordinates'][0][0])), (+ ((self._DesignParameter['M3V3M4_clk_lt']['_XYCoordinates'][0][1] + self._DesignParameter['M3V3M4_clk_lt']['_DesignObj']._DesignParameter['_Met4Layer']['_XYCoordinates'][0][1]) + (self._DesignParameter['M3V3M4_clk_lt']['_DesignObj']._DesignParameter['_Met4Layer']['_YWidth'] / 2)))], [(+ (self._DesignParameter['M3V3M4_clk_ld']['_XYCoordinates'][0][0] + self._DesignParameter['M3V3M4_clk_ld']['_DesignObj']._DesignParameter['_Met4Layer']['_XYCoordinates'][0][0])), (+ ((self._DesignParameter['M3V3M4_clk_ld']['_XYCoordinates'][0][1] + self._DesignParameter['M3V3M4_clk_ld']['_DesignObj']._DesignParameter['_Met4Layer']['_XYCoordinates'][0][1]) - (self._DesignParameter['M3V3M4_clk_ld']['_DesignObj']._DesignParameter['_Met4Layer']['_YWidth'] / 2)))]]]
		self._DesignParameter['METAL4_path_15'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL4'][0], _Datatype=DesignParameters._LayerMapping['METAL4'][1], _Width=(drc._MetalxMinWidth * 2))
		self._DesignParameter['METAL4_path_15']['_XYCoordinates'] = [[[(+ (self._DesignParameter['M3V3M4_clk_rt']['_XYCoordinates'][0][0] + self._DesignParameter['M3V3M4_clk_rt']['_DesignObj']._DesignParameter['_Met4Layer']['_XYCoordinates'][0][0])), (+ ((self._DesignParameter['M3V3M4_clk_rt']['_XYCoordinates'][0][1] + self._DesignParameter['M3V3M4_clk_rt']['_DesignObj']._DesignParameter['_Met4Layer']['_XYCoordinates'][0][1]) + (self._DesignParameter['M3V3M4_clk_rt']['_DesignObj']._DesignParameter['_Met4Layer']['_YWidth'] / 2)))], [(+ (self._DesignParameter['M3V3M4_clk_rd']['_XYCoordinates'][0][0] + self._DesignParameter['M3V3M4_clk_rd']['_DesignObj']._DesignParameter['_Met4Layer']['_XYCoordinates'][0][0])), (+ ((self._DesignParameter['M3V3M4_clk_rd']['_XYCoordinates'][0][1] + self._DesignParameter['M3V3M4_clk_rd']['_DesignObj']._DesignParameter['_Met4Layer']['_XYCoordinates'][0][1]) - (self._DesignParameter['M3V3M4_clk_rd']['_DesignObj']._DesignParameter['_Met4Layer']['_YWidth'] / 2)))]]]
		XYList = []
		xy_offset = (0, (((self._DesignParameter['M3V3M4_clk_lt']['_DesignObj']._DesignParameter['_Met4Layer']['_YWidth'] - self._DesignParameter['M2V2M3_inp_mos_drain']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth']) / 2) + ((- self._DesignParameter['precharge_left_left_via34']['_XYCoordinates'][0][1]) + self._DesignParameter['M2V2M3_inp_mos_drain']['_XYCoordinates'][0][1])))
		for i in range(len(self._DesignParameter['precharge_left_left_via34']['_XYCoordinates'])):
		    xy = (self._DesignParameter['precharge_left_left_via34']['_XYCoordinates'][i][0] if (type(self._DesignParameter['precharge_left_left_via34']['_XYCoordinates'][i][0]) == list) else self._DesignParameter['precharge_left_left_via34']['_XYCoordinates'][i])
		    XYList.append([((x + y) + z) for (x, y, z) in zip([0, 0], xy, xy_offset)])
		self._DesignParameter['M3V3M4_nmos_inp_gate'] = self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_Name='M3V3M4_nmos_inp_gateIn{}'.format(_Name)))[0]
		self._DesignParameter['M3V3M4_nmos_inp_gate']['_DesignObj']._CalculateViaMet32Met4DesignParameterMinimumEnclosureX(**dict(_ViaMet32Met4NumberOfCOX=1, _ViaMet32Met4NumberOfCOY=2))
		self._DesignParameter['M3V3M4_nmos_inp_gate']['_XYCoordinates'] = XYList
		XYList = []
		xy_offset = (0, ((self._DesignParameter['M2V2M3_inn_mos_drain']['_XYCoordinates'][0][1] - self._DesignParameter['precharge_right_right_via34']['_XYCoordinates'][0][1]) + ((self._DesignParameter['M3V3M4_clk_rt']['_DesignObj']._DesignParameter['_Met4Layer']['_YWidth'] - self._DesignParameter['M2V2M3_inn_mos_drain']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth']) / 2)))
		for i in range(len(self._DesignParameter['precharge_right_right_via34']['_XYCoordinates'])):
		    xy = (self._DesignParameter['precharge_right_right_via34']['_XYCoordinates'][i][0] if (type(self._DesignParameter['precharge_right_right_via34']['_XYCoordinates'][i][0]) == list) else self._DesignParameter['precharge_right_right_via34']['_XYCoordinates'][i])
		    XYList.append([((x + y) + z) for (x, y, z) in zip([0, 0], xy, xy_offset)])
		self._DesignParameter['M3VM4_nmos_inn_gate'] = self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_Name='M3VM4_nmos_inn_gateIn{}'.format(_Name)))[0]
		self._DesignParameter['M3VM4_nmos_inn_gate']['_DesignObj']._CalculateViaMet32Met4DesignParameterMinimumEnclosureX(**dict(_ViaMet32Met4NumberOfCOX=1, _ViaMet32Met4NumberOfCOY=2))
		self._DesignParameter['M3VM4_nmos_inn_gate']['_XYCoordinates'] = XYList
		self._DesignParameter['METAL3_boundary_43'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0], _Datatype=DesignParameters._LayerMapping['METAL3'][1], _XWidth=(self._DesignParameter['M3V3M4_clk_rd']['_XYCoordinates'][0][0] - self._DesignParameter['M3V3M4_clk_ld']['_XYCoordinates'][0][0]), _YWidth=(drc._MetalxMinWidth * 2))
		self._DesignParameter['METAL3_boundary_43']['_XYCoordinates'] = [[self._DesignParameter['M2V2M3_bot_nmos_gate']['_XYCoordinates'][0][0], (((self._DesignParameter['M3V3M4_clk_ld']['_XYCoordinates'][0][1] + self._DesignParameter['M3V3M4_clk_ld']['_DesignObj']._DesignParameter['_Met3Layer']['_XYCoordinates'][0][1]) - (self._DesignParameter['M3V3M4_clk_ld']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth'] / 2)) + (self._DesignParameter['METAL3_boundary_43']['_YWidth'] / 2))]]
		self._DesignParameter['M3V3M4_CDNS_6375475055661_0'] = self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_Name='M3V3M4_CDNS_6375475055661_0In{}'.format(_Name)))[0]
		self._DesignParameter['M3V3M4_CDNS_6375475055661_0']['_DesignObj']._CalculateViaMet32Met4DesignParameterMinimumEnclosureY(**dict(_ViaMet32Met4NumberOfCOX=1, _ViaMet32Met4NumberOfCOY=2))
		self._DesignParameter['M3V3M4_CDNS_6375475055661_0']['_XYCoordinates'] = [[(self._DesignParameter['M3V3M4_mid_right_pmos']['_XYCoordinates'][0][0] + ((- self._DesignParameter['M3V3M4_CDNS_6375475055661_0']['_DesignObj']._DesignParameter['_Met4Layer']['_XWidth']) / 2)), ((((self._DesignParameter['M1V1M2_mid_mos_right_gate']['_XYCoordinates'][0][1] + self._DesignParameter['M1V1M2_mid_mos_right_gate']['_DesignObj']._DesignParameter['_Met2Layer']['_XYCoordinates'][0][1]) + (self._DesignParameter['M1V1M2_mid_mos_right_gate']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] / 2)) + drc._MetalxMinSpace2) + (self._DesignParameter['M3V3M4_CDNS_6375475055661_0']['_DesignObj']._DesignParameter['_Met4Layer']['_YWidth'] / 2))]]
		self._DesignParameter['M2V2M3_CDNS_6375475055619_1'] = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_Name='M2V2M3_CDNS_6375475055619_1In{}'.format(_Name)))[0]
		self._DesignParameter['M2V2M3_CDNS_6375475055619_1']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureY(**dict(_ViaMet22Met3NumberOfCOX=1, _ViaMet22Met3NumberOfCOY=2))
		self._DesignParameter['M2V2M3_CDNS_6375475055619_1']['_XYCoordinates'] = [[(self._DesignParameter['M3V3M4_mid_right_pmos']['_XYCoordinates'][0][0] + ((- self._DesignParameter['M3V3M4_CDNS_6375475055661_0']['_DesignObj']._DesignParameter['_Met4Layer']['_XWidth']) / 2)), ((((self._DesignParameter['M1V1M2_mid_mos_right_gate']['_XYCoordinates'][0][1] + self._DesignParameter['M1V1M2_mid_mos_right_gate']['_DesignObj']._DesignParameter['_Met2Layer']['_XYCoordinates'][0][1]) + (self._DesignParameter['M1V1M2_mid_mos_right_gate']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] / 2)) + drc._MetalxMinSpace2) + (self._DesignParameter['M3V3M4_CDNS_6375475055661_0']['_DesignObj']._DesignParameter['_Met4Layer']['_YWidth'] / 2))]]
		self._DesignParameter['M3V3M4_CDNS_6375475055661_1'] = self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_Name='M3V3M4_CDNS_6375475055661_1In{}'.format(_Name)))[0]
		self._DesignParameter['M3V3M4_CDNS_6375475055661_1']['_DesignObj']._CalculateViaMet32Met4DesignParameterMinimumEnclosureY(**dict(_ViaMet32Met4NumberOfCOX=1, _ViaMet32Met4NumberOfCOY=2))
		self._DesignParameter['M3V3M4_CDNS_6375475055661_1']['_XYCoordinates'] = [[(self._DesignParameter['M3V3M4_mid_left_pmos']['_XYCoordinates'][0][0] + (self._DesignParameter['M3V3M4_CDNS_6375475055661_1']['_DesignObj']._DesignParameter['_Met4Layer']['_XWidth'] / 2)), ((((self._DesignParameter['M1V1M2_mid_left_pmos_gate']['_XYCoordinates'][0][1] + self._DesignParameter['M1V1M2_mid_left_pmos_gate']['_DesignObj']._DesignParameter['_Met2Layer']['_XYCoordinates'][0][1]) - (self._DesignParameter['M1V1M2_mid_left_pmos_gate']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] / 2)) - drc._MetalxMinSpace2) + ((- self._DesignParameter['M3V3M4_CDNS_6375475055661_1']['_DesignObj']._DesignParameter['_Met4Layer']['_YWidth']) / 2))]]
		self._DesignParameter['M2V2M3_CDNS_6375475055619_2'] = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_Name='M2V2M3_CDNS_6375475055619_2In{}'.format(_Name)))[0]
		self._DesignParameter['M2V2M3_CDNS_6375475055619_2']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureY(**dict(_ViaMet22Met3NumberOfCOX=1, _ViaMet22Met3NumberOfCOY=2))
		self._DesignParameter['M2V2M3_CDNS_6375475055619_2']['_XYCoordinates'] = [[(self._DesignParameter['M3V3M4_mid_left_pmos']['_XYCoordinates'][0][0] + (self._DesignParameter['M3V3M4_CDNS_6375475055661_1']['_DesignObj']._DesignParameter['_Met4Layer']['_XWidth'] / 2)), ((((self._DesignParameter['M1V1M2_mid_left_pmos_gate']['_XYCoordinates'][0][1] + self._DesignParameter['M1V1M2_mid_left_pmos_gate']['_DesignObj']._DesignParameter['_Met2Layer']['_XYCoordinates'][0][1]) - (self._DesignParameter['M1V1M2_mid_left_pmos_gate']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] / 2)) - drc._MetalxMinSpace2) + ((- self._DesignParameter['M3V3M4_CDNS_6375475055661_1']['_DesignObj']._DesignParameter['_Met4Layer']['_YWidth']) / 2))]]
		self._DesignParameter['METAL2_path_33'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _Width=(drc._MetalxMinWidth * 2))
		self._DesignParameter['METAL2_path_33']['_XYCoordinates'] = [[[(+ self._DesignParameter['M3V3M4_CDNS_6375475055661_1']['_XYCoordinates'][0][0]), (+ self._DesignParameter['M3V3M4_CDNS_6375475055661_1']['_XYCoordinates'][0][1])], [self._DesignParameter['M1V1M2_mid_right_pmos_gate']['_XYCoordinates'][0][0], self._DesignParameter['M3V3M4_CDNS_6375475055661_1']['_XYCoordinates'][0][1]]]]
		self._DesignParameter['METAL2_path_36'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _Width=(drc._MetalxMinWidth * 2))
		self._DesignParameter['METAL2_path_36']['_XYCoordinates'] = [[[(+ self._DesignParameter['M3V3M4_CDNS_6375475055661_0']['_XYCoordinates'][0][0]), (+ self._DesignParameter['M3V3M4_CDNS_6375475055661_0']['_XYCoordinates'][0][1])], [self._DesignParameter['M1V1M2_mid_left_pmos_gate']['_XYCoordinates'][0][0], self._DesignParameter['M3V3M4_CDNS_6375475055661_0']['_XYCoordinates'][0][1]]]]
		self._DesignParameter['GuardringInNMOSSetofSlicer_0']['_DesignObj']._CalculateDesignParameter(**dict(height=((((((self._DesignParameter['M1V1M2_mid_mos_left_gate']['_XYCoordinates'][0][1] + self._DesignParameter['M1V1M2_mid_mos_left_gate']['_DesignObj']._DesignParameter['_Met2Layer']['_XYCoordinates'][0][1]) + (self._DesignParameter['M1V1M2_mid_mos_left_gate']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] / 2)) + drc._MetalxMinSpace2) + (- min((((self._DesignParameter['nmos_bot']['_XYCoordinates'][0][1] + self._DesignParameter['nmos_bot']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1]) - (self._DesignParameter['nmos_bot']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2)) - drc._PolygateMinSpace2OD), (((self._DesignParameter['nmos_bot']['_XYCoordinates'][0][1] + self._DesignParameter['nmos_bot']['_DesignObj']._DesignParameter['_PCCRITLayer']['_XYCoordinates'][0][1]) - (self._DesignParameter['nmos_bot']['_DesignObj']._DesignParameter['_PCCRITLayer']['_YWidth'] / 2)) - drc._OdMinSpace)))) + self._DesignParameter['GuardringInNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['nw_top']['_YWidth']) + subring_addi), width=((((((self._DesignParameter['nmos_inn']['_XYCoordinates'][0][0] + self._DesignParameter['nmos_inn']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][(- 1)][0]) + (self._DesignParameter['nmos_inn']['_DesignObj']._DesignParameter['_PODummyLayer']['_XWidth'] / 2)) - ((self._DesignParameter['nmos_inp']['_XYCoordinates'][0][0] + self._DesignParameter['nmos_inp']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['nmos_inp']['_DesignObj']._DesignParameter['_PODummyLayer']['_XWidth'] / 2))) + (2 * drc._PolygateMinSpace2OD)) + subring_addi) + self._DesignParameter['GuardringInNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['right']['_DesignObj']._DesignParameter['_PPLayer']['_XWidth']), contact=subring_via))
		self._DesignParameter['GuardringInNMOSSetofSlicer_0']['_XYCoordinates'] = [[self._DesignParameter['nmos_bot']['_XYCoordinates'][0][0], ((((self._DesignParameter['M1V1M2_mid_mos_left_gate']['_XYCoordinates'][0][1] + self._DesignParameter['M1V1M2_mid_mos_left_gate']['_DesignObj']._DesignParameter['_Met2Layer']['_XYCoordinates'][0][1]) + (self._DesignParameter['M1V1M2_mid_mos_left_gate']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] / 2)) + ((self._DesignParameter['nmos_bot']['_XYCoordinates'][0][1] + self._DesignParameter['nmos_bot']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1]) - (self._DesignParameter['nmos_bot']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2))) / 2)]]
		self._DesignParameter['GuardringInPMOSSetofSlicer_0']['_DesignObj']._CalculateDesignParameter(**dict(height=((((((self._DesignParameter['pmos_mid_left']['_XYCoordinates'][0][1] + self._DesignParameter['pmos_mid_left']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1]) + (self._DesignParameter['pmos_mid_left']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2)) + drc._PolygateMinSpace2OD) + self._DesignParameter['GuardringInPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['met_bot']['_YWidth']) + ((- ((self._DesignParameter['PCCAM1_mid_pmos_left']['_XYCoordinates'][0][1] + self._DesignParameter['PCCAM1_mid_pmos_left']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) - (self._DesignParameter['PCCAM1_mid_pmos_left']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2))) + drc._Metal1MinSpace2)) + subring_addi), width=(((((((self._DesignParameter['pmos_right']['_XYCoordinates'][0][0] + self._DesignParameter['pmos_right']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][(- 1)][0]) + (self._DesignParameter['pmos_right']['_DesignObj']._DesignParameter['_PODummyLayer']['_XWidth'] / 2)) - ((self._DesignParameter['pmos_left']['_XYCoordinates'][0][0] + self._DesignParameter['pmos_left']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['pmos_left']['_DesignObj']._DesignParameter['_PODummyLayer']['_XWidth'] / 2))) + drc._PolygateMinSpace2OD) + self._DesignParameter['GuardringInPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['met_right']['_XWidth']) + drc._PolygateMinSpace2OD) + subring_addi), contact=subring_via))
		self._DesignParameter['GuardringInPMOSSetofSlicer_0']['_XYCoordinates'] = [[self._DesignParameter['GuardringInNMOSSetofSlicer_0']['_XYCoordinates'][0][0], ((((self._DesignParameter['pmos_mid_left']['_XYCoordinates'][0][1] + self._DesignParameter['pmos_mid_left']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1]) + (self._DesignParameter['pmos_mid_left']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2)) + ((self._DesignParameter['PCCAM1_mid_pmos_left']['_XYCoordinates'][0][1] + self._DesignParameter['PCCAM1_mid_pmos_left']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) - (self._DesignParameter['PCCAM1_mid_pmos_left']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2))) / 2)]]
		self._DesignParameter['NWELL_boundary_2'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['NWELL'][0], _Datatype=DesignParameters._LayerMapping['NWELL'][1], _XWidth=(((self._DesignParameter['GuardringInPMOSSetofSlicer_0']['_XYCoordinates'][0][0] + self._DesignParameter['GuardringInPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['nw_right']['_XYCoordinates'][0][0]) + (self._DesignParameter['GuardringInPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['nw_right']['_XWidth'] / 2)) - ((self._DesignParameter['GuardringInPMOSSetofSlicer_0']['_XYCoordinates'][0][0] + self._DesignParameter['GuardringInPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['nw_left']['_XYCoordinates'][0][0]) - (self._DesignParameter['GuardringInPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['nw_left']['_XWidth'] / 2))), _YWidth=(((self._DesignParameter['GuardringInPMOSSetofSlicer_0']['_XYCoordinates'][0][1] + self._DesignParameter['GuardringInPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['nw_top']['_XYCoordinates'][0][1]) + (self._DesignParameter['GuardringInPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['nw_top']['_YWidth'] / 2)) - ((self._DesignParameter['GuardringInPMOSSetofSlicer_0']['_XYCoordinates'][0][1] + self._DesignParameter['GuardringInPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['nw_bot']['_XYCoordinates'][0][1]) - (self._DesignParameter['GuardringInPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['nw_bot']['_YWidth'] / 2))))
		self._DesignParameter['NWELL_boundary_2']['_XYCoordinates'] = [[(+ self._DesignParameter['GuardringInPMOSSetofSlicer_0']['_XYCoordinates'][0][0]), (+ self._DesignParameter['GuardringInPMOSSetofSlicer_0']['_XYCoordinates'][0][1])]]
		path_list = []
		if (len(self._DesignParameter['pmos_left']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates']) == 1):
		    mode = 'vertical'
		    _width = self._DesignParameter['pmos_left']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
		elif (self._DesignParameter['pmos_left']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0] == self._DesignParameter['pmos_left']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][(- 1)][0]):
		    mode = 'horizontal'
		    _width = self._DesignParameter['pmos_left']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
		elif (self._DesignParameter['pmos_left']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1] == self._DesignParameter['pmos_left']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][(- 1)][1]):
		    mode = 'vertical'
		    _width = self._DesignParameter['pmos_left']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
		else:
		    print('Invalid Target Input')
		if (mode == 'vertical'):
		    xy_with_offset = []
		    target_y_value = (self._DesignParameter['GuardringInPMOSSetofSlicer_0']['_XYCoordinates'][0][1] + self._DesignParameter['GuardringInPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['top']['_XYCoordinates'][0][1])
		    for i in range(len(self._DesignParameter['pmos_left']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'])):
		        if ((i % 2) == 0):
		            xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['pmos_left']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['pmos_left']['_XYCoordinates'][0][1])], self._DesignParameter['pmos_left']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		elif (mode == 'horizontal'):
		    xy_with_offset = []
		    target_x_value = (self._DesignParameter['GuardringInPMOSSetofSlicer_0']['_XYCoordinates'][0][0] + self._DesignParameter['GuardringInPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['top']['_XYCoordinates'][0][0])
		    for i in range(len(self._DesignParameter['pmos_left']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'])):
		        if ((i % 2) == 0):
		            xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['pmos_left']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['pmos_left']['_XYCoordinates'][0][1])], self._DesignParameter['pmos_left']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		self._DesignParameter['subring_left_supply'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=_width)
		self._DesignParameter['subring_left_supply']['_XYCoordinates'] = path_list
		path_list = []
		if (len(self._DesignParameter['pmos_right']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates']) == 1):
		    mode = 'vertical'
		    _width = self._DesignParameter['pmos_right']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
		elif (self._DesignParameter['pmos_right']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0] == self._DesignParameter['pmos_right']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][(- 1)][0]):
		    mode = 'horizontal'
		    _width = self._DesignParameter['pmos_right']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
		elif (self._DesignParameter['pmos_right']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1] == self._DesignParameter['pmos_right']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][(- 1)][1]):
		    mode = 'vertical'
		    _width = self._DesignParameter['pmos_right']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
		else:
		    print('Invalid Target Input')
		if (mode == 'vertical'):
		    xy_with_offset = []
		    target_y_value = (self._DesignParameter['GuardringInPMOSSetofSlicer_0']['_XYCoordinates'][0][1] + self._DesignParameter['GuardringInPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['top']['_XYCoordinates'][0][1])
		    for i in range(len(self._DesignParameter['pmos_right']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'])):
		        if ((i % 2) == 1):
		            xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['pmos_right']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['pmos_right']['_XYCoordinates'][0][1])], self._DesignParameter['pmos_right']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		elif (mode == 'horizontal'):
		    xy_with_offset = []
		    target_x_value = (self._DesignParameter['GuardringInPMOSSetofSlicer_0']['_XYCoordinates'][0][0] + self._DesignParameter['GuardringInPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['top']['_XYCoordinates'][0][0])
		    for i in range(len(self._DesignParameter['pmos_right']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'])):
		        if ((i % 2) == 1):
		            xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['pmos_right']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['pmos_right']['_XYCoordinates'][0][1])], self._DesignParameter['pmos_right']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		self._DesignParameter['precharge_right_supply'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=_width)
		self._DesignParameter['precharge_right_supply']['_XYCoordinates'] = path_list
		path_list = []
		if (len(self._DesignParameter['nmos_bot']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates']) == 1):
		    mode = 'vertical'
		    _width = self._DesignParameter['nmos_bot']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
		elif (self._DesignParameter['nmos_bot']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0] == self._DesignParameter['nmos_bot']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][(- 1)][0]):
		    mode = 'horizontal'
		    _width = self._DesignParameter['nmos_bot']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
		elif (self._DesignParameter['nmos_bot']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1] == self._DesignParameter['nmos_bot']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][(- 1)][1]):
		    mode = 'vertical'
		    _width = self._DesignParameter['nmos_bot']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
		else:
		    print('Invalid Target Input')
		if (mode == 'vertical'):
		    xy_with_offset = []
		    target_y_value = (self._DesignParameter['GuardringInNMOSSetofSlicer_0']['_XYCoordinates'][0][1] + self._DesignParameter['GuardringInNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['bot']['_XYCoordinates'][0][1])
		    for i in range(len(self._DesignParameter['nmos_bot']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'])):
		        if ((i % 2) == 1):
		            xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['nmos_bot']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['nmos_bot']['_XYCoordinates'][0][1])], self._DesignParameter['nmos_bot']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		elif (mode == 'horizontal'):
		    xy_with_offset = []
		    target_x_value = (self._DesignParameter['GuardringInNMOSSetofSlicer_0']['_XYCoordinates'][0][0] + self._DesignParameter['GuardringInNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['bot']['_XYCoordinates'][0][0])
		    for i in range(len(self._DesignParameter['nmos_bot']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'])):
		        if ((i % 2) == 1):
		            xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['nmos_bot']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['nmos_bot']['_XYCoordinates'][0][1])], self._DesignParameter['nmos_bot']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		self._DesignParameter['bot_nmos_supply_array'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=_width)
		self._DesignParameter['bot_nmos_supply_array']['_XYCoordinates'] = path_list
		path_list = []
		if (len(self._DesignParameter['pmos_mid_left']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates']) == 1):
		    mode = 'vertical'
		    _width = self._DesignParameter['pmos_mid_left']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
		elif (self._DesignParameter['pmos_mid_left']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0] == self._DesignParameter['pmos_mid_left']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][(- 1)][0]):
		    mode = 'horizontal'
		    _width = self._DesignParameter['pmos_mid_left']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
		elif (self._DesignParameter['pmos_mid_left']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1] == self._DesignParameter['pmos_mid_left']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][(- 1)][1]):
		    mode = 'vertical'
		    _width = self._DesignParameter['pmos_mid_left']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
		else:
		    print('Invalid Target Input')
		if (mode == 'vertical'):
		    xy_with_offset = []
		    target_y_value = (self._DesignParameter['GuardringInPMOSSetofSlicer_0']['_XYCoordinates'][0][1] + self._DesignParameter['GuardringInPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['top']['_XYCoordinates'][0][1])
		    for i in range(len(self._DesignParameter['pmos_mid_left']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'])):
		        if ((i % 2) == 1):
		            xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['pmos_mid_left']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['pmos_mid_left']['_XYCoordinates'][0][1])], self._DesignParameter['pmos_mid_left']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		elif (mode == 'horizontal'):
		    xy_with_offset = []
		    target_x_value = (self._DesignParameter['GuardringInPMOSSetofSlicer_0']['_XYCoordinates'][0][0] + self._DesignParameter['GuardringInPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['top']['_XYCoordinates'][0][0])
		    for i in range(len(self._DesignParameter['pmos_mid_left']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'])):
		        if ((i % 2) == 1):
		            xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['pmos_mid_left']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['pmos_mid_left']['_XYCoordinates'][0][1])], self._DesignParameter['pmos_mid_left']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		self._DesignParameter['pmos_mid_left_supply'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=_width)
		self._DesignParameter['pmos_mid_left_supply']['_XYCoordinates'] = path_list
		path_list = []
		if (len(self._DesignParameter['pmos_mid_right']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates']) == 1):
		    mode = 'vertical'
		    _width = self._DesignParameter['pmos_mid_right']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
		elif (self._DesignParameter['pmos_mid_right']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0] == self._DesignParameter['pmos_mid_right']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][(- 1)][0]):
		    mode = 'horizontal'
		    _width = self._DesignParameter['pmos_mid_right']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
		elif (self._DesignParameter['pmos_mid_right']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1] == self._DesignParameter['pmos_mid_right']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][(- 1)][1]):
		    mode = 'vertical'
		    _width = self._DesignParameter['pmos_mid_right']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
		else:
		    print('Invalid Target Input')
		if (mode == 'vertical'):
		    xy_with_offset = []
		    target_y_value = (self._DesignParameter['GuardringInPMOSSetofSlicer_0']['_XYCoordinates'][0][1] + self._DesignParameter['GuardringInPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['top']['_XYCoordinates'][0][1])
		    for i in range(len(self._DesignParameter['pmos_mid_right']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'])):
		        if ((i % 2) == 1):
		            xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['pmos_mid_right']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['pmos_mid_right']['_XYCoordinates'][0][1])], self._DesignParameter['pmos_mid_right']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		elif (mode == 'horizontal'):
		    xy_with_offset = []
		    target_x_value = (self._DesignParameter['GuardringInPMOSSetofSlicer_0']['_XYCoordinates'][0][0] + self._DesignParameter['GuardringInPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['top']['_XYCoordinates'][0][0])
		    for i in range(len(self._DesignParameter['pmos_mid_right']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'])):
		        if ((i % 2) == 1):
		            xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['pmos_mid_right']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['pmos_mid_right']['_XYCoordinates'][0][1])], self._DesignParameter['pmos_mid_right']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		self._DesignParameter['mid_right_pmos_supply'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=_width)
		self._DesignParameter['mid_right_pmos_supply']['_XYCoordinates'] = path_list
		self._DesignParameter['M1V1M2_VDD'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='M1V1M2_VDDIn{}'.format(_Name)))[0]
		self._DesignParameter['M1V1M2_VDD']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureY(**dict(_ViaMet12Met2NumberOfCOX=max(1, (1 + int((((self._DesignParameter['GuardringInPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['met_top']['_XWidth'] - drc._VIAxMinSpace2) - (2 * drc._VIAxMinEnclosureByMetx)) / (drc._VIAxMinWidth + drc._VIAxMinSpace2))))), _ViaMet12Met2NumberOfCOY=subring_via))
		self._DesignParameter['M1V1M2_VDD']['_XYCoordinates'] = [[(+ (self._DesignParameter['GuardringInPMOSSetofSlicer_0']['_XYCoordinates'][0][0] + self._DesignParameter['GuardringInPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['top']['_XYCoordinates'][0][0])), (+ (self._DesignParameter['GuardringInPMOSSetofSlicer_0']['_XYCoordinates'][0][1] + self._DesignParameter['GuardringInPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['top']['_XYCoordinates'][0][1]))]]
		self._DesignParameter['M2V2M3_VDD'] = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_Name='M2V2M3_VDDIn{}'.format(_Name)))[0]
		self._DesignParameter['M2V2M3_VDD']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureY(**dict(_ViaMet22Met3NumberOfCOX=max(1, (1 + int((((self._DesignParameter['GuardringInPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['met_top']['_XWidth'] - drc._VIAxMinSpace2) - (2 * drc._VIAxMinEnclosureByMetx)) / (drc._VIAxMinWidth + drc._VIAxMinSpace2))))), _ViaMet22Met3NumberOfCOY=subring_via))
		self._DesignParameter['M2V2M3_VDD']['_XYCoordinates'] = [[(+ (self._DesignParameter['GuardringInPMOSSetofSlicer_0']['_XYCoordinates'][0][0] + self._DesignParameter['GuardringInPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['top']['_XYCoordinates'][0][0])), (+ (self._DesignParameter['GuardringInPMOSSetofSlicer_0']['_XYCoordinates'][0][1] + self._DesignParameter['GuardringInPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['top']['_XYCoordinates'][0][1]))]]
		self._DesignParameter['METAL2_boundary_47'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _XWidth=max(self._DesignParameter['GuardringInPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['met_top']['_XWidth'], self._DesignParameter['M1V1M2_VDD']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth']), _YWidth=max(self._DesignParameter['GuardringInPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['met_top']['_YWidth'], self._DesignParameter['M1V1M2_VDD']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth']))
		self._DesignParameter['METAL2_boundary_47']['_XYCoordinates'] = [[(+ (self._DesignParameter['GuardringInPMOSSetofSlicer_0']['_XYCoordinates'][0][0] + self._DesignParameter['GuardringInPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['top']['_XYCoordinates'][0][0])), (+ (self._DesignParameter['GuardringInPMOSSetofSlicer_0']['_XYCoordinates'][0][1] + self._DesignParameter['GuardringInPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['top']['_XYCoordinates'][0][1]))]]
		self._DesignParameter['METAL3_boundary_42'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0], _Datatype=DesignParameters._LayerMapping['METAL3'][1], _XWidth=max(self._DesignParameter['GuardringInPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['met_top']['_XWidth'], self._DesignParameter['M1V1M2_VDD']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth']), _YWidth=max(self._DesignParameter['GuardringInPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['met_top']['_YWidth'], self._DesignParameter['M1V1M2_VDD']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth']))
		self._DesignParameter['METAL3_boundary_42']['_XYCoordinates'] = [[(+ (self._DesignParameter['GuardringInPMOSSetofSlicer_0']['_XYCoordinates'][0][0] + self._DesignParameter['GuardringInPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['top']['_XYCoordinates'][0][0])), (+ (self._DesignParameter['GuardringInPMOSSetofSlicer_0']['_XYCoordinates'][0][1] + self._DesignParameter['GuardringInPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['top']['_XYCoordinates'][0][1]))]]
		self._DesignParameter['Guardring_outside'] = self._SrefElementDeclaration(_DesignObj=PSubRing.PSubRing(_Name='Guardring_outsideIn{}'.format(_Name)))[0]
		self._DesignParameter['Guardring_outside']['_DesignObj']._CalculateDesignParameter(**dict(height=6000, width=5640, contact=subring_via))
		self._DesignParameter['Guardring_outside']['_XYCoordinates'] = [[0.0, (- 670.0)]]
		self._DesignParameter['Guardring_outside']['_DesignObj']._CalculateDesignParameter(**dict(height=((((((self._DesignParameter['GuardringInPMOSSetofSlicer_0']['_XYCoordinates'][0][1] + self._DesignParameter['GuardringInPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['nw_top']['_XYCoordinates'][0][1]) + (self._DesignParameter['GuardringInPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['nw_top']['_YWidth'] / 2)) + drc._NwMinEnclosurePactive2) + (- (((self._DesignParameter['GuardringInNMOSSetofSlicer_0']['_XYCoordinates'][0][1] + self._DesignParameter['GuardringInNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['nw_bot']['_XYCoordinates'][0][1]) - (self._DesignParameter['GuardringInNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['nw_bot']['_YWidth'] / 2)) - drc._PpMinExtensiononPactive2))) + self._DesignParameter['Guardring_outside']['_DesignObj']._DesignParameter['nw_top']['_YWidth']) + subring_addi), width=(max(((((((self._DesignParameter['GuardringInNMOSSetofSlicer_0']['_XYCoordinates'][0][0] + self._DesignParameter['GuardringInNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['nw_right']['_XYCoordinates'][0][0]) + (self._DesignParameter['GuardringInNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['nw_right']['_XWidth'] / 2)) - ((self._DesignParameter['GuardringInNMOSSetofSlicer_0']['_XYCoordinates'][0][0] + self._DesignParameter['GuardringInNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['nw_left']['_XYCoordinates'][0][0]) - (self._DesignParameter['GuardringInNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['nw_left']['_XWidth'] / 2))) + self._DesignParameter['Guardring_outside']['_DesignObj']._DesignParameter['nw_left']['_XWidth']) + subring_addi) + (drc._PpMinExtensiononPactive2 * 2)), (((subring_addi + (((self._DesignParameter['GuardringInPMOSSetofSlicer_0']['_XYCoordinates'][0][0] + self._DesignParameter['GuardringInPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['nw_right']['_XYCoordinates'][0][0]) + (self._DesignParameter['GuardringInPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['nw_right']['_XWidth'] / 2)) - ((self._DesignParameter['GuardringInPMOSSetofSlicer_0']['_XYCoordinates'][0][0] + self._DesignParameter['GuardringInPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['nw_left']['_XYCoordinates'][0][0]) - (self._DesignParameter['GuardringInPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['nw_left']['_XWidth'] / 2)))) + (drc._NwMinEnclosurePactive2 * 2)) + self._DesignParameter['Guardring_outside']['_DesignObj']._DesignParameter['nw_left']['_XWidth'])) + subring_addi), contact=subring_via))
		self._DesignParameter['Guardring_outside']['_XYCoordinates'] = [[self._DesignParameter['nmos_bot']['_XYCoordinates'][0][0], ((((((self._DesignParameter['GuardringInPMOSSetofSlicer_0']['_XYCoordinates'][0][1] + self._DesignParameter['GuardringInPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['nw_top']['_XYCoordinates'][0][1]) + (self._DesignParameter['GuardringInPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['nw_top']['_YWidth'] / 2)) + drc._NwMinEnclosurePactive) + ((self._DesignParameter['GuardringInNMOSSetofSlicer_0']['_XYCoordinates'][0][1] + self._DesignParameter['GuardringInNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['nw_bot']['_XYCoordinates'][0][1]) - (self._DesignParameter['GuardringInNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['nw_bot']['_YWidth'] / 2))) - drc._PpMinSpacetoPRES) / 2)]]
		self._DesignParameter['M1V1M2_VSS'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='M1V1M2_VSSIn{}'.format(_Name)))[0]
		self._DesignParameter['M1V1M2_VSS']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureY(**dict(_ViaMet12Met2NumberOfCOX=max(1, (1 + int((((self._DesignParameter['Guardring_outside']['_DesignObj']._DesignParameter['met_bot']['_XWidth'] - drc._VIAxMinSpace2) - (2 * drc._VIAxMinEnclosureByMetx)) / (drc._VIAxMinWidth + drc._VIAxMinSpace2))))), _ViaMet12Met2NumberOfCOY=max(1, (1 + int(((((((self._DesignParameter['GuardringInNMOSSetofSlicer_0']['_XYCoordinates'][0][1] + self._DesignParameter['GuardringInNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['met_bot']['_XYCoordinates'][0][1]) + (self._DesignParameter['GuardringInNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['met_bot']['_YWidth'] / 2)) - ((self._DesignParameter['Guardring_outside']['_XYCoordinates'][0][1] + self._DesignParameter['Guardring_outside']['_DesignObj']._DesignParameter['met_bot']['_XYCoordinates'][0][1]) - (self._DesignParameter['Guardring_outside']['_DesignObj']._DesignParameter['met_bot']['_YWidth'] / 2))) - drc._VIAxMinSpace) - (2 * drc._VIAxMinEnclosureByMetx)) / (drc._VIAxMinWidth + drc._VIAxMinSpace)))))))
		self._DesignParameter['M1V1M2_VSS']['_XYCoordinates'] = [[self._DesignParameter['nmos_bot']['_XYCoordinates'][0][0], ((((self._DesignParameter['GuardringInNMOSSetofSlicer_0']['_XYCoordinates'][0][1] + self._DesignParameter['GuardringInNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['met_bot']['_XYCoordinates'][0][1]) + (self._DesignParameter['GuardringInNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['met_bot']['_YWidth'] / 2)) + ((self._DesignParameter['Guardring_outside']['_XYCoordinates'][0][1] + self._DesignParameter['Guardring_outside']['_DesignObj']._DesignParameter['met_bot']['_XYCoordinates'][0][1]) - (self._DesignParameter['Guardring_outside']['_DesignObj']._DesignParameter['met_bot']['_YWidth'] / 2))) / 2)]]
		self._DesignParameter['M2V2M3_VSS'] = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_Name='M2V2M3_VSSIn{}'.format(_Name)))[0]
		self._DesignParameter['M2V2M3_VSS']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureY(**dict(_ViaMet22Met3NumberOfCOX=max(1, (1 + int((((self._DesignParameter['Guardring_outside']['_DesignObj']._DesignParameter['met_bot']['_XWidth'] - drc._VIAxMinSpace2) - (2 * drc._VIAxMinEnclosureByMetx)) / (drc._VIAxMinWidth + drc._VIAxMinSpace2))))), _ViaMet22Met3NumberOfCOY=max(1, (1 + int(((((((self._DesignParameter['GuardringInNMOSSetofSlicer_0']['_XYCoordinates'][0][1] + self._DesignParameter['GuardringInNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['met_bot']['_XYCoordinates'][0][1]) + (self._DesignParameter['GuardringInNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['met_bot']['_YWidth'] / 2)) - ((self._DesignParameter['Guardring_outside']['_XYCoordinates'][0][1] + self._DesignParameter['Guardring_outside']['_DesignObj']._DesignParameter['met_bot']['_XYCoordinates'][0][1]) - (self._DesignParameter['Guardring_outside']['_DesignObj']._DesignParameter['met_bot']['_YWidth'] / 2))) - drc._VIAxMinSpace) - (2 * drc._VIAxMinEnclosureByMetx)) / (drc._VIAxMinWidth + drc._VIAxMinSpace)))))))
		self._DesignParameter['M2V2M3_VSS']['_XYCoordinates'] = [[(+ self._DesignParameter['M1V1M2_VSS']['_XYCoordinates'][0][0]), (+ self._DesignParameter['M1V1M2_VSS']['_XYCoordinates'][0][1])]]
		self._DesignParameter['METAL3_boundary_41'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0], _Datatype=DesignParameters._LayerMapping['METAL3'][1], _XWidth=self._DesignParameter['Guardring_outside']['_DesignObj']._DesignParameter['met_bot']['_XWidth'], _YWidth=(((self._DesignParameter['GuardringInNMOSSetofSlicer_0']['_XYCoordinates'][0][1] + self._DesignParameter['GuardringInNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['met_bot']['_XYCoordinates'][0][1]) + (self._DesignParameter['GuardringInNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['met_bot']['_YWidth'] / 2)) - ((self._DesignParameter['Guardring_outside']['_XYCoordinates'][0][1] + self._DesignParameter['Guardring_outside']['_DesignObj']._DesignParameter['met_bot']['_XYCoordinates'][0][1]) - (self._DesignParameter['Guardring_outside']['_DesignObj']._DesignParameter['met_bot']['_YWidth'] / 2))))
		self._DesignParameter['METAL3_boundary_41']['_XYCoordinates'] = [[(+ self._DesignParameter['M1V1M2_VSS']['_XYCoordinates'][0][0]), (+ self._DesignParameter['M1V1M2_VSS']['_XYCoordinates'][0][1])]]
		self._DesignParameter['METAL1_boundary_356'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _XWidth=self._DesignParameter['Guardring_outside']['_DesignObj']._DesignParameter['met_bot']['_XWidth'], _YWidth=(((self._DesignParameter['GuardringInNMOSSetofSlicer_0']['_XYCoordinates'][0][1] + self._DesignParameter['GuardringInNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['met_bot']['_XYCoordinates'][0][1]) + (self._DesignParameter['GuardringInNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['met_bot']['_YWidth'] / 2)) - ((self._DesignParameter['Guardring_outside']['_XYCoordinates'][0][1] + self._DesignParameter['Guardring_outside']['_DesignObj']._DesignParameter['met_bot']['_XYCoordinates'][0][1]) - (self._DesignParameter['Guardring_outside']['_DesignObj']._DesignParameter['met_bot']['_YWidth'] / 2))))
		self._DesignParameter['METAL1_boundary_356']['_XYCoordinates'] = [[(+ self._DesignParameter['M1V1M2_VSS']['_XYCoordinates'][0][0]), (+ self._DesignParameter['M1V1M2_VSS']['_XYCoordinates'][0][1])]]
		self._DesignParameter['METAL2_boundary_46'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _XWidth=self._DesignParameter['Guardring_outside']['_DesignObj']._DesignParameter['met_bot']['_XWidth'], _YWidth=(((self._DesignParameter['GuardringInNMOSSetofSlicer_0']['_XYCoordinates'][0][1] + self._DesignParameter['GuardringInNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['met_bot']['_XYCoordinates'][0][1]) + (self._DesignParameter['GuardringInNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['met_bot']['_YWidth'] / 2)) - ((self._DesignParameter['Guardring_outside']['_XYCoordinates'][0][1] + self._DesignParameter['Guardring_outside']['_DesignObj']._DesignParameter['met_bot']['_XYCoordinates'][0][1]) - (self._DesignParameter['Guardring_outside']['_DesignObj']._DesignParameter['met_bot']['_YWidth'] / 2))))
		self._DesignParameter['METAL2_boundary_46']['_XYCoordinates'] = [[(+ self._DesignParameter['M1V1M2_VSS']['_XYCoordinates'][0][0]), (+ self._DesignParameter['M1V1M2_VSS']['_XYCoordinates'][0][1])]]
		self._DesignParameter['met4_left'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL4'][0], _Datatype=DesignParameters._LayerMapping['METAL4'][1], _Width=drc._MetalxMinWidth)
		self._DesignParameter['met4_left']['_XYCoordinates'] = [[[self._DesignParameter['M3V3M4_nmos_inp_gate']['_XYCoordinates'][0][0], self._DesignParameter['M2V2M3_inp_mos_drain']['_XYCoordinates'][0][1]], [self._DesignParameter['M3V3M4_nmos_inp_gate']['_XYCoordinates'][(- 1)][0], self._DesignParameter['M2V2M3_inp_mos_drain']['_XYCoordinates'][0][1]]]]
		self._DesignParameter['met4_right'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL4'][0], _Datatype=DesignParameters._LayerMapping['METAL4'][1], _Width=drc._MetalxMinWidth)
		self._DesignParameter['met4_right']['_XYCoordinates'] = [[[self._DesignParameter['M3VM4_nmos_inn_gate']['_XYCoordinates'][0][0], self._DesignParameter['M2V2M3_inn_mos_drain']['_XYCoordinates'][0][1]], [self._DesignParameter['M3VM4_nmos_inn_gate']['_XYCoordinates'][(- 1)][0], self._DesignParameter['M2V2M3_inn_mos_drain']['_XYCoordinates'][0][1]]]]
		self._DesignParameter['slvt_nmos'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['SLVT'][0], _Datatype=DesignParameters._LayerMapping['SLVT'][1], _XWidth=(((self._DesignParameter['nmos_inn']['_XYCoordinates'][0][0] + self._DesignParameter['nmos_inn']['_DesignObj']._DesignParameter['_SLVTLayer']['_XYCoordinates'][0][0]) + (self._DesignParameter['nmos_inn']['_DesignObj']._DesignParameter['_SLVTLayer']['_XWidth'] / 2)) - ((self._DesignParameter['nmos_inp']['_XYCoordinates'][0][0] + self._DesignParameter['nmos_inp']['_DesignObj']._DesignParameter['_SLVTLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['nmos_inp']['_DesignObj']._DesignParameter['_SLVTLayer']['_XWidth'] / 2))), _YWidth=(((self._DesignParameter['nmos_inn']['_XYCoordinates'][0][1] + self._DesignParameter['nmos_inn']['_DesignObj']._DesignParameter['_SLVTLayer']['_XYCoordinates'][0][1]) + (self._DesignParameter['nmos_inn']['_DesignObj']._DesignParameter['_SLVTLayer']['_YWidth'] / 2)) - ((self._DesignParameter['nmos_bot']['_XYCoordinates'][0][1] + self._DesignParameter['nmos_bot']['_DesignObj']._DesignParameter['_SLVTLayer']['_XYCoordinates'][0][1]) - (self._DesignParameter['nmos_bot']['_DesignObj']._DesignParameter['_SLVTLayer']['_YWidth'] / 2))))
		self._DesignParameter['slvt_nmos']['_XYCoordinates'] = [[((self._DesignParameter['nmos_inp']['_XYCoordinates'][0][0] + self._DesignParameter['nmos_inn']['_XYCoordinates'][0][0]) / 2), ((((self._DesignParameter['mid_nmos_left']['_XYCoordinates'][0][1] + self._DesignParameter['mid_nmos_left']['_DesignObj']._DesignParameter['_SLVTLayer']['_XYCoordinates'][0][1]) + (self._DesignParameter['mid_nmos_left']['_DesignObj']._DesignParameter['_SLVTLayer']['_YWidth'] / 2)) + ((self._DesignParameter['nmos_bot']['_XYCoordinates'][0][1] + self._DesignParameter['nmos_bot']['_DesignObj']._DesignParameter['_SLVTLayer']['_XYCoordinates'][0][1]) - (self._DesignParameter['nmos_bot']['_DesignObj']._DesignParameter['_SLVTLayer']['_YWidth'] / 2))) / 2)]]
		self._DesignParameter['slvt_pmos'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['SLVT'][0], _Datatype=DesignParameters._LayerMapping['SLVT'][1], _XWidth=(((self._DesignParameter['pmos_right']['_XYCoordinates'][0][0] + self._DesignParameter['pmos_right']['_DesignObj']._DesignParameter['_SLVTLayer']['_XYCoordinates'][0][0]) + (self._DesignParameter['pmos_right']['_DesignObj']._DesignParameter['_SLVTLayer']['_XWidth'] / 2)) - ((self._DesignParameter['pmos_left']['_XYCoordinates'][0][0] + self._DesignParameter['pmos_left']['_DesignObj']._DesignParameter['_SLVTLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['pmos_left']['_DesignObj']._DesignParameter['_SLVTLayer']['_XWidth'] / 2))), _YWidth=self._DesignParameter['pmos_mid_right']['_DesignObj']._DesignParameter['_SLVTLayer']['_YWidth'])
		self._DesignParameter['slvt_pmos']['_XYCoordinates'] = [[self._DesignParameter['nmos_bot']['_XYCoordinates'][0][0], self._DesignParameter['pmos_mid_left']['_XYCoordinates'][0][1]]]
		self._DesignParameter['mid_left_nmos_met1'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _XWidth=(((self._DesignParameter['pmos_mid_right']['_XYCoordinates'][0][0] + self._DesignParameter['pmos_mid_right']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][0]) + (self._DesignParameter['pmos_mid_right']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth'] / 2)) - ((self._DesignParameter['pmos_mid_right']['_XYCoordinates'][0][0] + self._DesignParameter['pmos_mid_right']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][0]) - (self._DesignParameter['pmos_mid_right']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth'] / 2))), _YWidth=drc._Metal1MinWidth)
		self._DesignParameter['mid_left_nmos_met1']['_XYCoordinates'] = [[self._DesignParameter['mid_nmos_left']['_XYCoordinates'][0][0], ((((self._DesignParameter['mid_nmos_left']['_XYCoordinates'][0][1] + self._DesignParameter['mid_nmos_left']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) - (self._DesignParameter['mid_nmos_left']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)) - (drc._Metal1MinWidth / 2)) - drc._Metal1MinSpace2)]]
		self._DesignParameter['mid_right_nmos_met1'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _XWidth=(((self._DesignParameter['pmos_mid_right']['_XYCoordinates'][0][0] + self._DesignParameter['pmos_mid_right']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][0]) + (self._DesignParameter['pmos_mid_right']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth'] / 2)) - ((self._DesignParameter['pmos_mid_right']['_XYCoordinates'][0][0] + self._DesignParameter['pmos_mid_right']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][0]) - (self._DesignParameter['pmos_mid_right']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth'] / 2))), _YWidth=drc._Metal1MinWidth)
		self._DesignParameter['mid_right_nmos_met1']['_XYCoordinates'] = [[self._DesignParameter['mid_nmos_right']['_XYCoordinates'][0][0], ((((self._DesignParameter['mid_nmos_left']['_XYCoordinates'][0][1] + self._DesignParameter['mid_nmos_left']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) - (self._DesignParameter['mid_nmos_left']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)) - (drc._Metal1MinWidth / 2)) - drc._Metal1MinSpace2)]]
		path_list = []
		if (len(self._DesignParameter['mid_nmos_left']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates']) == 1):
		    mode = 'vertical'
		    _width = self._DesignParameter['mid_nmos_left']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
		elif (self._DesignParameter['mid_nmos_left']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0] == self._DesignParameter['mid_nmos_left']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][(- 1)][0]):
		    mode = 'horizontal'
		    _width = self._DesignParameter['mid_nmos_left']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
		elif (self._DesignParameter['mid_nmos_left']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1] == self._DesignParameter['mid_nmos_left']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][(- 1)][1]):
		    mode = 'vertical'
		    _width = self._DesignParameter['mid_nmos_left']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
		else:
		    print('Invalid Target Input')
		if (mode == 'vertical'):
		    xy_with_offset = []
		    target_y_value = (0 + self._DesignParameter['mid_left_nmos_met1']['_XYCoordinates'][0][1])
		    for i in range(len(self._DesignParameter['mid_nmos_left']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'])):
		        if ((i % 2) == 0):
		            xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['mid_nmos_left']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['mid_nmos_left']['_XYCoordinates'][0][1])], self._DesignParameter['mid_nmos_left']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		elif (mode == 'horizontal'):
		    xy_with_offset = []
		    target_x_value = (0 + self._DesignParameter['mid_left_nmos_met1']['_XYCoordinates'][0][0])
		    for i in range(len(self._DesignParameter['mid_nmos_left']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'])):
		        if ((i % 2) == 0):
		            xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['mid_nmos_left']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['mid_nmos_left']['_XYCoordinates'][0][1])], self._DesignParameter['mid_nmos_left']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		self._DesignParameter['mid_left_nmos_met1_array'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=_width)
		self._DesignParameter['mid_left_nmos_met1_array']['_XYCoordinates'] = path_list
		path_list = []
		if (len(self._DesignParameter['mid_nmos_right']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates']) == 1):
		    mode = 'vertical'
		    _width = self._DesignParameter['mid_nmos_right']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
		elif (self._DesignParameter['mid_nmos_right']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0] == self._DesignParameter['mid_nmos_right']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][(- 1)][0]):
		    mode = 'horizontal'
		    _width = self._DesignParameter['mid_nmos_right']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
		elif (self._DesignParameter['mid_nmos_right']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1] == self._DesignParameter['mid_nmos_right']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][(- 1)][1]):
		    mode = 'vertical'
		    _width = self._DesignParameter['mid_nmos_right']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
		else:
		    print('Invalid Target Input')
		if (mode == 'vertical'):
		    xy_with_offset = []
		    target_y_value = (0 + self._DesignParameter['mid_right_nmos_met1']['_XYCoordinates'][0][1])
		    for i in range(len(self._DesignParameter['mid_nmos_right']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'])):
		        if ((i % 2) == 0):
		            xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['mid_nmos_right']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['mid_nmos_right']['_XYCoordinates'][0][1])], self._DesignParameter['mid_nmos_right']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		elif (mode == 'horizontal'):
		    xy_with_offset = []
		    target_x_value = (0 + self._DesignParameter['mid_right_nmos_met1']['_XYCoordinates'][0][0])
		    for i in range(len(self._DesignParameter['mid_nmos_right']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'])):
		        if ((i % 2) == 0):
		            xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['mid_nmos_right']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['mid_nmos_right']['_XYCoordinates'][0][1])], self._DesignParameter['mid_nmos_right']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		self._DesignParameter['mid_right_nmos_met1_array'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=_width)
		self._DesignParameter['mid_right_nmos_met1_array']['_XYCoordinates'] = path_list
		self._DesignParameter['pimp_pmos'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['PIMP'][0], _Datatype=DesignParameters._LayerMapping['PIMP'][1], _XWidth=(((self._DesignParameter['pmos_right']['_XYCoordinates'][0][0] + self._DesignParameter['pmos_right']['_DesignObj']._DesignParameter['_PPLayer']['_XYCoordinates'][0][0]) + (self._DesignParameter['pmos_right']['_DesignObj']._DesignParameter['_PPLayer']['_XWidth'] / 2)) - ((self._DesignParameter['pmos_left']['_XYCoordinates'][0][0] + self._DesignParameter['pmos_left']['_DesignObj']._DesignParameter['_PPLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['pmos_left']['_DesignObj']._DesignParameter['_PPLayer']['_XWidth'] / 2))), _YWidth=self._DesignParameter['pmos_left']['_DesignObj']._DesignParameter['_PPLayer']['_YWidth'])
		self._DesignParameter['pimp_pmos']['_XYCoordinates'] = [[self._DesignParameter['nmos_bot']['_XYCoordinates'][0][0], self._DesignParameter['pmos_mid_left']['_XYCoordinates'][0][1]]]
		self._DesignParameter['CLK'] = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1PIN'][0], _Datatype=DesignParameters._LayerMapping['METAL1PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0], _XYCoordinates=[[(+ self._DesignParameter['M2V2M3_CDNS_6375475055672_1']['_XYCoordinates'][0][0]), (+ self._DesignParameter['M2V2M3_CDNS_6375475055672_1']['_XYCoordinates'][0][1])], [(+ self._DesignParameter['M2V2M3_bot_nmos_gate']['_XYCoordinates'][0][0]), (+ self._DesignParameter['M2V2M3_bot_nmos_gate']['_XYCoordinates'][0][1])], [(+ self._DesignParameter['M2V2M3_precharge_right_gate']['_XYCoordinates'][0][0]), (+ self._DesignParameter['M2V2M3_precharge_right_gate']['_XYCoordinates'][0][1])]], _Mag=0.05, _Angle=0, _TEXT='CLK')
		[[(+ self._DesignParameter['M2V2M3_precharge_right_gate']['_XYCoordinates'][0][0]), (+ self._DesignParameter['M2V2M3_precharge_right_gate']['_XYCoordinates'][0][1])]]
		self._DesignParameter['VDD_PIN'] = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1PIN'][0], _Datatype=DesignParameters._LayerMapping['METAL1PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0], _XYCoordinates=[[(+ self._DesignParameter['METAL3_boundary_42']['_XYCoordinates'][0][0]), (+ self._DesignParameter['METAL3_boundary_42']['_XYCoordinates'][0][1])]], _Mag=0.05, _Angle=0, _TEXT='VDD')
		self._DesignParameter['SSn'] = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1PIN'][0], _Datatype=DesignParameters._LayerMapping['METAL1PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0], _XYCoordinates=[[(+ (self._DesignParameter['pmos_mid_left']['_XYCoordinates'][0][0] + self._DesignParameter['pmos_mid_left']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][(- 1)][0])), (+ (self._DesignParameter['pmos_mid_left']['_XYCoordinates'][0][1] + self._DesignParameter['pmos_mid_left']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][(- 1)][1]))]], _Mag=0.05, _Angle=0, _TEXT='SSn')
		self._DesignParameter['SSp'] = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1PIN'][0], _Datatype=DesignParameters._LayerMapping['METAL1PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0], _XYCoordinates=[[(+ (self._DesignParameter['pmos_mid_right']['_XYCoordinates'][0][0] + self._DesignParameter['pmos_mid_right']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0])), (+ (self._DesignParameter['pmos_mid_right']['_XYCoordinates'][0][1] + self._DesignParameter['pmos_mid_right']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]))]], _Mag=0.05, _Angle=0, _TEXT='SSp')
		self._DesignParameter['INp'] = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1PIN'][0], _Datatype=DesignParameters._LayerMapping['METAL1PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0], _XYCoordinates=[[(+ self._DesignParameter['PCCAM1_inp_mos_gate']['_XYCoordinates'][0][0]), (+ self._DesignParameter['PCCAM1_inp_mos_gate']['_XYCoordinates'][0][1])]], _Mag=0.05, _Angle=0, _TEXT='INp')
		self._DesignParameter['INn'] = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1PIN'][0], _Datatype=DesignParameters._LayerMapping['METAL1PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0], _XYCoordinates=[[(+ self._DesignParameter['PCCAM1_inn_mos_gate']['_XYCoordinates'][0][0]), (+ self._DesignParameter['PCCAM1_inn_mos_gate']['_XYCoordinates'][0][1])]], _Mag=0.05, _Angle=0, _TEXT='INn')
		self._DesignParameter['VSS_PIN'] = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1PIN'][0], _Datatype=DesignParameters._LayerMapping['METAL1PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0], _XYCoordinates=[[(+ (self._DesignParameter['GuardringInNMOSSetofSlicer_0']['_XYCoordinates'][0][0] + self._DesignParameter['GuardringInNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['bot']['_XYCoordinates'][0][0])), (+ (self._DesignParameter['GuardringInNMOSSetofSlicer_0']['_XYCoordinates'][0][1] + self._DesignParameter['GuardringInNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['bot']['_XYCoordinates'][0][1]))]], _Mag=0.05, _Angle=0, _TEXT='VSS')
		