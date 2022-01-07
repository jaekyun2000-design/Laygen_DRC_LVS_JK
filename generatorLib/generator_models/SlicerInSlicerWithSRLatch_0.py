from generatorLib import StickDiagram
from generatorLib import DesignParameters
import copy
import math
from generatorLib import DRC
from generatorLib.generator_models import ViaMet22Met3
from generatorLib.generator_models import NMOSWithDummy
from generatorLib.generator_models import ViaPoly2Met1
from generatorLib.generator_models import ViaMet32Met4
from generatorLib.generator_models import ViaMet12Met2

class SlicerInSlicerWithSRLatch_0(StickDiagram._StickDiagram):
	def __init__(self, _DesignParameter=None, _Name='SlicerInSlicerWithSRLatch_0'):
		if _DesignParameter != None:
			self._DesignParameter = _DesignParameter
		else:
			self._DesignParameter = dict(_Name=self._NameDeclaration(_Name=_Name), _GDSFile=self._GDSObjDeclaration(_GDSFile=None))
		self._DesignParameter['_Name']['Name'] = _Name

	def _CalculateDesignParameter(self,SLVT=None,input_via_y=2,gate_spacing=96):
	
		drc = DRC.DRC()
		_Name = self._DesignParameter['_Name']['_Name']
		
		self._DesignParameter['nmos_bot'] = self._SrefElementDeclaration(_DesignObj=NMOSWithDummy._NMOS(_Name='nmos_botIn{}'.format(_Name)))[0]
		self._DesignParameter['nmos_bot']['_DesignObj']._CalculateNMOSDesignParameter(**dict(_NMOSNumberofGate=8, _NMOSChannelWidth=1000, _NMOSChannellength=30, _NMOSDummy=True, _GateSpacing=None, _XVT='SLVT'))
		self._DesignParameter['nmos_bot']['_XYCoordinates'] = [[0.0, (- 2495.0)]]
		bot_nmos_via_num = int((((self._DesignParameter['nmos_bot']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] - drc._VIAxMinSpace) - (2 * drc._VIAxMinEnclosureByMetx)) / (drc._VIAxMinWidth + drc._VIAxMinSpace)))
		XYList = []
		xy_offset = [0, 0]
		for i in range(len(self._DesignParameter['nmos_bot']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'])):
		    if ((i % 2) == 0):
		        XYList.append([((x + y) + z) for (x, y, z) in zip([(0 + self._DesignParameter['nmos_bot']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['nmos_bot']['_XYCoordinates'][0][1])], self._DesignParameter['nmos_bot']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i], xy_offset)])
		self._DesignParameter['bot_nmos_via12'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='bot_nmos_via12In{}'.format(_Name)))[0]
		self._DesignParameter['bot_nmos_via12']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(**dict(_ViaMet12Met2NumberOfCOX=1, _ViaMet12Met2NumberOfCOY=bot_nmos_via_num))
		self._DesignParameter['bot_nmos_via12']['_XYCoordinates'] = XYList
		XYList = []
		xy_offset = [0, 0]
		for i in range(len(self._DesignParameter['bot_nmos_via12']['_XYCoordinates'])):
		    XYList.append([((x + y) + z) for (x, y, z) in zip([0, 0], self._DesignParameter['bot_nmos_via12']['_XYCoordinates'][i], xy_offset)])
		self._DesignParameter['bot_nmos_via23'] = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_Name='bot_nmos_via23In{}'.format(_Name)))[0]
		self._DesignParameter['bot_nmos_via23']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureX(**dict(_ViaMet22Met3NumberOfCOX=1, _ViaMet22Met3NumberOfCOY=bot_nmos_via_num))
		self._DesignParameter['bot_nmos_via23']['_XYCoordinates'] = XYList
		XYList = []
		xy_offset = [0, 0]
		for i in range(len(self._DesignParameter['bot_nmos_via12']['_XYCoordinates'])):
		    XYList.append([((x + y) + z) for (x, y, z) in zip([0, 0], self._DesignParameter['bot_nmos_via12']['_XYCoordinates'][i], xy_offset)])
		self._DesignParameter['bot_nmos_via34'] = self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_Name='bot_nmos_via34In{}'.format(_Name)))[0]
		self._DesignParameter['bot_nmos_via34']['_DesignObj']._CalculateViaMet32Met4DesignParameterMinimumEnclosureX(**dict(_ViaMet32Met4NumberOfCOX=1, _ViaMet32Met4NumberOfCOY=bot_nmos_via_num))
		self._DesignParameter['bot_nmos_via34']['_XYCoordinates'] = XYList
		self._DesignParameter['METAL4_path_14'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL4'][0], _Datatype=DesignParameters._LayerMapping['METAL4'][1], _Width=drc._MetalxMinWidth)
		self._DesignParameter['METAL4_path_14']['_XYCoordinates'] = [[[(+ self._DesignParameter['bot_nmos_via34']['_XYCoordinates'][0][0]), (+ self._DesignParameter['bot_nmos_via34']['_XYCoordinates'][0][1])], [(+ self._DesignParameter['bot_nmos_via34']['_XYCoordinates'][(- 1)][0]), (+ self._DesignParameter['bot_nmos_via34']['_XYCoordinates'][(- 1)][1])]]]
		self._DesignParameter['bot_mos_gate_via'] = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_Name='bot_mos_gate_viaIn{}'.format(_Name)))[0]
		self._DesignParameter['bot_mos_gate_via']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(**dict(_ViaPoly2Met1NumberOfCOX=int(((((((self._DesignParameter['nmos_bot']['_XYCoordinates'][0][0] + self._DesignParameter['nmos_bot']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]) + (self._DesignParameter['nmos_bot']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)) - ((self._DesignParameter['nmos_bot']['_XYCoordinates'][0][0] + self._DesignParameter['nmos_bot']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['nmos_bot']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2))) - drc._CoMinSpace) - (2 * drc._CoMinEnclosureByPO)) / (drc._CoMinWidth + drc._CoMinSpace))), _ViaPoly2Met1NumberOfCOY=1))
		self._DesignParameter['bot_mos_gate_via']['_XYCoordinates'] = [[self._DesignParameter['nmos_bot']['_XYCoordinates'][0][0], (max((((self._DesignParameter['nmos_bot']['_XYCoordinates'][0][1] + self._DesignParameter['nmos_bot']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) + (self._DesignParameter['nmos_bot']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)) + drc._Metal1MinSpace), (((self._DesignParameter['bot_nmos_via12']['_XYCoordinates'][4][1] + self._DesignParameter['bot_nmos_via12']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) + (self._DesignParameter['bot_nmos_via12']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)) + drc._Metal1MinSpace), (((self._DesignParameter['bot_nmos_via12']['_XYCoordinates'][4][1] + self._DesignParameter['bot_nmos_via12']['_DesignObj']._DesignParameter['_Met2Layer']['_XYCoordinates'][0][1]) + (self._DesignParameter['bot_nmos_via12']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] / 2)) + drc._MetalxMinSpace)) + (self._DesignParameter['bot_mos_gate_via']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2))]]
		self._DesignParameter['POLY_path_65'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _Width=self._DesignParameter['bot_mos_gate_via']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'])
		self._DesignParameter['POLY_path_65']['_XYCoordinates'] = [[[((self._DesignParameter['nmos_bot']['_XYCoordinates'][0][0] + self._DesignParameter['nmos_bot']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['nmos_bot']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)), self._DesignParameter['bot_mos_gate_via']['_XYCoordinates'][0][1]], [((self._DesignParameter['nmos_bot']['_XYCoordinates'][0][0] + self._DesignParameter['nmos_bot']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]) + (self._DesignParameter['nmos_bot']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)), self._DesignParameter['bot_mos_gate_via']['_XYCoordinates'][0][1]]]]
		self._DesignParameter['M1V1M2_bot_nmos_gate'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='M1V1M2_bot_nmos_gateIn{}'.format(_Name)))[0]
		self._DesignParameter['M1V1M2_bot_nmos_gate']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureY(**dict(_ViaMet12Met2NumberOfCOX=int(((((((self._DesignParameter['nmos_bot']['_XYCoordinates'][0][0] + self._DesignParameter['nmos_bot']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]) + (self._DesignParameter['nmos_bot']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)) - ((self._DesignParameter['nmos_bot']['_XYCoordinates'][0][0] + self._DesignParameter['nmos_bot']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['nmos_bot']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2))) - drc._VIAxMinSpace) - (drc._VIAxMinEnclosureByMetx * 2)) / (drc._VIAxMinWidth + drc._VIAxMinSpace))), _ViaMet12Met2NumberOfCOY=1))
		self._DesignParameter['M1V1M2_bot_nmos_gate']['_XYCoordinates'] = [[(+ self._DesignParameter['bot_mos_gate_via']['_XYCoordinates'][0][0]), (+ self._DesignParameter['bot_mos_gate_via']['_XYCoordinates'][0][1])]]
		self._DesignParameter['M2V2M3_bot_nmos_gate'] = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_Name='M2V2M3_bot_nmos_gateIn{}'.format(_Name)))[0]
		self._DesignParameter['M2V2M3_bot_nmos_gate']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureY(**dict(_ViaMet22Met3NumberOfCOX=int(((((((self._DesignParameter['nmos_bot']['_XYCoordinates'][0][0] + self._DesignParameter['nmos_bot']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]) + (self._DesignParameter['nmos_bot']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)) - ((self._DesignParameter['nmos_bot']['_XYCoordinates'][0][0] + self._DesignParameter['nmos_bot']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['nmos_bot']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2))) - drc._VIAxMinSpace) - (drc._VIAxMinEnclosureByMetx * 2)) / (drc._VIAxMinWidth + drc._VIAxMinSpace))), _ViaMet22Met3NumberOfCOY=1))
		self._DesignParameter['M2V2M3_bot_nmos_gate']['_XYCoordinates'] = [[(+ self._DesignParameter['bot_mos_gate_via']['_XYCoordinates'][0][0]), (+ self._DesignParameter['bot_mos_gate_via']['_XYCoordinates'][0][1])]]
		path_list = []
		if (self._DesignParameter['nmos_bot']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0] == self._DesignParameter['nmos_bot']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]):
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
		self._DesignParameter['mid_nmos_left']['_DesignObj']._CalculateNMOSDesignParameter(**dict(_NMOSNumberofGate=2, _NMOSChannelWidth=1000, _NMOSChannellength=30, _NMOSDummy=True, _GateSpacing=None, _XVT='SLVT'))
		self._DesignParameter['mid_nmos_left']['_XYCoordinates'] = [[int(((self._DesignParameter['nmos_bot']['_XYCoordinates'][0][0] - (self._DesignParameter['mid_nmos_left']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][(- 1)][0] + (self._DesignParameter['mid_nmos_left']['_DesignObj']._DesignParameter['_PODummyLayer']['_XWidth'] / 2))) - (gate_spacing / 2))), int((((((((self._DesignParameter['METAL1_boundary_355']['_XYCoordinates'][0][1] + (self._DesignParameter['METAL1_boundary_355']['_YWidth'] / 2)) + drc._Metal1MinSpace) + (input_via_y * (drc._CoMinWidth + drc._CoMinSpace))) - drc._CoMinSpace) + (2 * drc._CoMinEnclosureByPO)) + drc._PolygateMinSpace) + (self._DesignParameter['mid_nmos_left']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2)))]]
		self._DesignParameter['mid_nmos_right'] = self._SrefElementDeclaration(_DesignObj=NMOSWithDummy._NMOS(_Name='mid_nmos_rightIn{}'.format(_Name)))[0]
		self._DesignParameter['mid_nmos_right']['_DesignObj']._CalculateNMOSDesignParameter(**dict(_NMOSNumberofGate=2, _NMOSChannelWidth=1000, _NMOSChannellength=30, _NMOSDummy=True, _GateSpacing=None, _XVT='SLVT'))
		self._DesignParameter['mid_nmos_right']['_XYCoordinates'] = [[int(((self._DesignParameter['nmos_bot']['_XYCoordinates'][0][0] - (self._DesignParameter['mid_nmos_right']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][0] - (self._DesignParameter['mid_nmos_right']['_DesignObj']._DesignParameter['_PODummyLayer']['_XWidth'] / 2))) + (gate_spacing / 2))), int((((((((self._DesignParameter['METAL1_boundary_355']['_XYCoordinates'][0][1] + (self._DesignParameter['METAL1_boundary_355']['_YWidth'] / 2)) + drc._Metal1MinSpace) + (input_via_y * (drc._CoMinWidth + drc._CoMinSpace))) - drc._CoMinSpace) + (2 * drc._CoMinEnclosureByPO)) + drc._PolygateMinSpace) + (self._DesignParameter['mid_nmos_left']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2)))]]
		self._DesignParameter['METAL1_path_41'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=self._DesignParameter['mid_nmos_left']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'])
		self._DesignParameter['METAL1_path_41']['_XYCoordinates'] = [[[(+ (self._DesignParameter['mid_nmos_left']['_XYCoordinates'][0][0] + self._DesignParameter['mid_nmos_left']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0])), (+ (self._DesignParameter['mid_nmos_left']['_XYCoordinates'][0][1] + self._DesignParameter['mid_nmos_left']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]))], [(self._DesignParameter['mid_nmos_left']['_XYCoordinates'][0][0] + self._DesignParameter['mid_nmos_left']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0]), ((((self._DesignParameter['mid_nmos_left']['_XYCoordinates'][0][1] + self._DesignParameter['mid_nmos_left']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) - (self._DesignParameter['mid_nmos_left']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)) - drc._Metal1MinSpace) - (self._DesignParameter['mid_nmos_left']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] / 2))], [(self._DesignParameter['mid_nmos_left']['_XYCoordinates'][0][0] + self._DesignParameter['mid_nmos_left']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][(- 1)][0]), ((((self._DesignParameter['mid_nmos_left']['_XYCoordinates'][0][1] + self._DesignParameter['mid_nmos_left']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) - (self._DesignParameter['mid_nmos_left']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)) - drc._Metal1MinSpace) - (self._DesignParameter['mid_nmos_left']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] / 2))], [(+ (self._DesignParameter['mid_nmos_left']['_XYCoordinates'][0][0] + self._DesignParameter['mid_nmos_left']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][(- 1)][0])), (+ (self._DesignParameter['mid_nmos_left']['_XYCoordinates'][0][1] + self._DesignParameter['mid_nmos_left']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][(- 1)][1]))]]]
		self._DesignParameter['METAL1_path_38'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=self._DesignParameter['mid_nmos_left']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'])
		self._DesignParameter['METAL1_path_38']['_XYCoordinates'] = [[[(+ (self._DesignParameter['mid_nmos_right']['_XYCoordinates'][0][0] + self._DesignParameter['mid_nmos_right']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0])), (+ (self._DesignParameter['mid_nmos_right']['_XYCoordinates'][0][1] + self._DesignParameter['mid_nmos_right']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]))], [(self._DesignParameter['mid_nmos_right']['_XYCoordinates'][0][0] + self._DesignParameter['mid_nmos_right']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0]), ((((self._DesignParameter['mid_nmos_right']['_XYCoordinates'][0][1] + self._DesignParameter['mid_nmos_right']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) - (self._DesignParameter['mid_nmos_right']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)) - drc._Metal1MinSpace) - (self._DesignParameter['mid_nmos_right']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] / 2))], [(self._DesignParameter['mid_nmos_right']['_XYCoordinates'][0][0] + self._DesignParameter['mid_nmos_right']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][(- 1)][0]), ((((self._DesignParameter['mid_nmos_right']['_XYCoordinates'][0][1] + self._DesignParameter['mid_nmos_right']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) - (self._DesignParameter['mid_nmos_right']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)) - drc._Metal1MinSpace) - (self._DesignParameter['mid_nmos_right']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] / 2))], [(+ (self._DesignParameter['mid_nmos_right']['_XYCoordinates'][0][0] + self._DesignParameter['mid_nmos_right']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][(- 1)][0])), (+ (self._DesignParameter['mid_nmos_right']['_XYCoordinates'][0][1] + self._DesignParameter['mid_nmos_right']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][(- 1)][1]))]]]
		num_of_mid_nmos_via = int((((self._DesignParameter['mid_nmos_left']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] - drc._VIAxMinSpace) - (2 * drc._VIAxMinEnclosureByMetx)) / (drc._VIAxMinWidth + drc._VIAxMinSpace)))
		XYList = []
		xy_offset = (0, int(((drc._CoMinWidth + drc._CoMinSpace) / 4)))
		for i in range(len(self._DesignParameter['mid_nmos_left']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'])):
		    if ((i % 2) == 1):
		        XYList.append([((x + y) + z) for (x, y, z) in zip([(0 + self._DesignParameter['mid_nmos_left']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['mid_nmos_left']['_XYCoordinates'][0][1])], self._DesignParameter['mid_nmos_left']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i], xy_offset)])
		self._DesignParameter['mid_nmos_left_via'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='mid_nmos_left_viaIn{}'.format(_Name)))[0]
		self._DesignParameter['mid_nmos_left_via']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(**dict(_ViaMet12Met2NumberOfCOX=1, _ViaMet12Met2NumberOfCOY=num_of_mid_nmos_via))
		self._DesignParameter['mid_nmos_left_via']['_XYCoordinates'] = XYList
		XYList = []
		xy_offset = (0, ((drc._VIAxMinWidth + drc._VIAxMinSpace) / 4))
		for i in range(len(self._DesignParameter['mid_nmos_right']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'])):
		    if ((i % 2) == 1):
		        XYList.append([((x + y) + z) for (x, y, z) in zip([(0 + self._DesignParameter['mid_nmos_right']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['mid_nmos_right']['_XYCoordinates'][0][1])], self._DesignParameter['mid_nmos_right']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i], xy_offset)])
		self._DesignParameter['min_nmos_right_via'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='min_nmos_right_viaIn{}'.format(_Name)))[0]
		self._DesignParameter['min_nmos_right_via']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(**dict(_ViaMet12Met2NumberOfCOX=1, _ViaMet12Met2NumberOfCOY=num_of_mid_nmos_via))
		self._DesignParameter['min_nmos_right_via']['_XYCoordinates'] = XYList
		self._DesignParameter['PCCAM1_mid_nmos_left'] = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_Name='PCCAM1_mid_nmos_leftIn{}'.format(_Name)))[0]
		self._DesignParameter['PCCAM1_mid_nmos_left']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(**dict(_ViaPoly2Met1NumberOfCOX=int((len(self._DesignParameter['mid_nmos_left']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates']) - 1)), _ViaPoly2Met1NumberOfCOY=1))
		self._DesignParameter['PCCAM1_mid_nmos_left']['_XYCoordinates'] = [[self._DesignParameter['mid_nmos_left']['_XYCoordinates'][0][0], max(math.ceil(((((self._DesignParameter['mid_nmos_left_via']['_XYCoordinates'][0][1] + self._DesignParameter['mid_nmos_left_via']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) + (self._DesignParameter['mid_nmos_left_via']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)) + drc._Metal1MinSpace) + (self._DesignParameter['PCCAM1_mid_nmos_left']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2))), math.ceil(((((self._DesignParameter['mid_nmos_left']['_XYCoordinates'][0][1] + self._DesignParameter['mid_nmos_left']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) + (self._DesignParameter['mid_nmos_left']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)) + drc._Metal1MinSpace) + (self._DesignParameter['PCCAM1_mid_nmos_left']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2))))]]
		self._DesignParameter['PCCAM1_mid_nmos_right'] = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_Name='PCCAM1_mid_nmos_rightIn{}'.format(_Name)))[0]
		self._DesignParameter['PCCAM1_mid_nmos_right']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(**dict(_ViaPoly2Met1NumberOfCOX=int((len(self._DesignParameter['mid_nmos_left']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates']) - 1)), _ViaPoly2Met1NumberOfCOY=1))
		self._DesignParameter['PCCAM1_mid_nmos_right']['_XYCoordinates'] = [[self._DesignParameter['mid_nmos_right']['_XYCoordinates'][0][0], max(math.ceil(((((self._DesignParameter['mid_nmos_left_via']['_XYCoordinates'][0][1] + self._DesignParameter['mid_nmos_left_via']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) + (self._DesignParameter['mid_nmos_left_via']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)) + drc._Metal1MinSpace) + (self._DesignParameter['PCCAM1_mid_nmos_left']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2))), math.ceil(((((self._DesignParameter['mid_nmos_left']['_XYCoordinates'][0][1] + self._DesignParameter['mid_nmos_left']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) + (self._DesignParameter['mid_nmos_left']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)) + drc._Metal1MinSpace) + (self._DesignParameter['PCCAM1_mid_nmos_left']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2))))]]
		self._DesignParameter['M1V1M2_mid_mos_left'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='M1V1M2_mid_mos_leftIn{}'.format(_Name)))[0]
		self._DesignParameter['M1V1M2_mid_mos_left']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(**dict(_ViaMet12Met2NumberOfCOX=1, _ViaMet12Met2NumberOfCOY=int((((self._DesignParameter['mid_nmos_left']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] - drc._VIAxMinSpace) - (2 * drc._VIAxMinEnclosureByMetx)) / (drc._VIAxMinWidth + drc._VIAxMinSpace)))))
		self._DesignParameter['M1V1M2_mid_mos_left']['_XYCoordinates'] = [[(+ (self._DesignParameter['mid_nmos_left']['_XYCoordinates'][0][0] + self._DesignParameter['mid_nmos_left']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][(- 1)][0])), ((- int(((drc._VIAxMinWidth + drc._VIAxMinSpace) / 4))) + (self._DesignParameter['mid_nmos_left']['_XYCoordinates'][0][1] + self._DesignParameter['mid_nmos_left']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][(- 1)][1]))]]
		self._DesignParameter['M2V2M3_mid_mos_left'] = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_Name='M2V2M3_mid_mos_leftIn{}'.format(_Name)))[0]
		self._DesignParameter['M2V2M3_mid_mos_left']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureX(**dict(_ViaMet22Met3NumberOfCOX=1, _ViaMet22Met3NumberOfCOY=int((((self._DesignParameter['mid_nmos_left']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] - drc._VIAxMinSpace) - (2 * drc._VIAxMinEnclosureByMetx)) / (drc._VIAxMinWidth + drc._VIAxMinSpace)))))
		self._DesignParameter['M2V2M3_mid_mos_left']['_XYCoordinates'] = [[(+ (self._DesignParameter['mid_nmos_left']['_XYCoordinates'][0][0] + self._DesignParameter['mid_nmos_left']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][(- 1)][0])), ((- int(((drc._VIAxMinWidth + drc._VIAxMinSpace) / 4))) + (self._DesignParameter['mid_nmos_left']['_XYCoordinates'][0][1] + self._DesignParameter['mid_nmos_left']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][(- 1)][1]))]]
		self._DesignParameter['M3V3M4_mid_mod_left'] = self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_Name='M3V3M4_mid_mod_leftIn{}'.format(_Name)))[0]
		self._DesignParameter['M3V3M4_mid_mod_left']['_DesignObj']._CalculateViaMet32Met4DesignParameterMinimumEnclosureX(**dict(_ViaMet32Met4NumberOfCOX=1, _ViaMet32Met4NumberOfCOY=int((((self._DesignParameter['mid_nmos_left']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] - drc._VIAxMinSpace) - (2 * drc._VIAxMinEnclosureByMetx)) / (drc._VIAxMinWidth + drc._VIAxMinSpace)))))
		self._DesignParameter['M3V3M4_mid_mod_left']['_XYCoordinates'] = [[(+ (self._DesignParameter['mid_nmos_left']['_XYCoordinates'][0][0] + self._DesignParameter['mid_nmos_left']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][(- 1)][0])), ((- int(((drc._VIAxMinWidth + drc._VIAxMinSpace) / 4))) + (self._DesignParameter['mid_nmos_left']['_XYCoordinates'][0][1] + self._DesignParameter['mid_nmos_left']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][(- 1)][1]))]]
		self._DesignParameter['M1V1M2_mid_mos_right'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='M1V1M2_mid_mos_rightIn{}'.format(_Name)))[0]
		self._DesignParameter['M1V1M2_mid_mos_right']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(**dict(_ViaMet12Met2NumberOfCOX=1, _ViaMet12Met2NumberOfCOY=int((((self._DesignParameter['mid_nmos_right']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] - drc._VIAxMinSpace) - (2 * drc._VIAxMinEnclosureByMetx)) / (drc._VIAxMinWidth + drc._VIAxMinSpace)))))
		self._DesignParameter['M1V1M2_mid_mos_right']['_XYCoordinates'] = [[(+ (self._DesignParameter['mid_nmos_right']['_XYCoordinates'][0][0] + self._DesignParameter['mid_nmos_right']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0])), ((- int(((drc._VIAxMinWidth + drc._VIAxMinSpace) / 4))) + (self._DesignParameter['mid_nmos_right']['_XYCoordinates'][0][1] + self._DesignParameter['mid_nmos_right']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]))]]
		self._DesignParameter['M2V2M3_mid_mos_right'] = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_Name='M2V2M3_mid_mos_rightIn{}'.format(_Name)))[0]
		self._DesignParameter['M2V2M3_mid_mos_right']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureX(**dict(_ViaMet22Met3NumberOfCOX=1, _ViaMet22Met3NumberOfCOY=int((((self._DesignParameter['mid_nmos_right']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] - drc._VIAxMinSpace) - (2 * drc._VIAxMinEnclosureByMetx)) / (drc._VIAxMinWidth + drc._VIAxMinSpace)))))
		self._DesignParameter['M2V2M3_mid_mos_right']['_XYCoordinates'] = [[(+ (self._DesignParameter['mid_nmos_right']['_XYCoordinates'][0][0] + self._DesignParameter['mid_nmos_right']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0])), ((- int(((drc._VIAxMinWidth + drc._VIAxMinSpace) / 4))) + (self._DesignParameter['mid_nmos_right']['_XYCoordinates'][0][1] + self._DesignParameter['mid_nmos_right']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]))]]
		self._DesignParameter['M3V3M4_mid_mos_right'] = self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_Name='M3V3M4_mid_mos_rightIn{}'.format(_Name)))[0]
		self._DesignParameter['M3V3M4_mid_mos_right']['_DesignObj']._CalculateViaMet32Met4DesignParameterMinimumEnclosureX(**dict(_ViaMet32Met4NumberOfCOX=1, _ViaMet32Met4NumberOfCOY=int((((self._DesignParameter['mid_nmos_right']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] - drc._VIAxMinSpace) - (2 * drc._VIAxMinEnclosureByMetx)) / (drc._VIAxMinWidth + drc._VIAxMinSpace)))))
		self._DesignParameter['M3V3M4_mid_mos_right']['_XYCoordinates'] = [[(+ (self._DesignParameter['mid_nmos_right']['_XYCoordinates'][0][0] + self._DesignParameter['mid_nmos_right']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0])), ((- int(((drc._VIAxMinWidth + drc._VIAxMinSpace) / 4))) + (self._DesignParameter['mid_nmos_right']['_XYCoordinates'][0][1] + self._DesignParameter['mid_nmos_right']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]))]]
		self._DesignParameter['M1V1M2_mid_mos_left_gate'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='M1V1M2_mid_mos_left_gateIn{}'.format(_Name)))[0]
		self._DesignParameter['M1V1M2_mid_mos_left_gate']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureY(**dict(_ViaMet12Met2NumberOfCOX=2, _ViaMet12Met2NumberOfCOY=1))
		self._DesignParameter['M1V1M2_mid_mos_left_gate']['_XYCoordinates'] = [[self._DesignParameter['PCCAM1_mid_nmos_left']['_XYCoordinates'][0][0], ((((((self._DesignParameter['mid_nmos_left_via']['_XYCoordinates'][0][1] + self._DesignParameter['mid_nmos_left_via']['_DesignObj']._DesignParameter['_Met2Layer']['_XYCoordinates'][0][1]) + (self._DesignParameter['mid_nmos_left_via']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] / 2)) + drc._MetalxMinSpace) + self._DesignParameter['mid_nmos_left_via']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth']) + drc._VIAxMinSpace) + (self._DesignParameter['M1V1M2_mid_mos_left_gate']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] / 2))]]
		self._DesignParameter['METAL1_boundary_354'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _XWidth=(max(((self._DesignParameter['M1V1M2_mid_mos_left_gate']['_XYCoordinates'][0][0] + self._DesignParameter['M1V1M2_mid_mos_left_gate']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0]) + (self._DesignParameter['M1V1M2_mid_mos_left_gate']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] / 2)), ((self._DesignParameter['PCCAM1_mid_nmos_left']['_XYCoordinates'][0][0] + self._DesignParameter['PCCAM1_mid_nmos_left']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0]) + (self._DesignParameter['PCCAM1_mid_nmos_left']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] / 2))) - min(((self._DesignParameter['PCCAM1_mid_nmos_left']['_XYCoordinates'][0][0] + self._DesignParameter['PCCAM1_mid_nmos_left']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0]) - (self._DesignParameter['PCCAM1_mid_nmos_left']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] / 2)), ((self._DesignParameter['M1V1M2_mid_mos_left_gate']['_XYCoordinates'][0][0] + self._DesignParameter['M1V1M2_mid_mos_left_gate']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0]) - (self._DesignParameter['M1V1M2_mid_mos_left_gate']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] / 2)))), _YWidth=(max(((self._DesignParameter['PCCAM1_mid_nmos_left']['_XYCoordinates'][0][1] + self._DesignParameter['PCCAM1_mid_nmos_left']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) + (self._DesignParameter['PCCAM1_mid_nmos_left']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)), ((self._DesignParameter['M1V1M2_mid_mos_left_gate']['_XYCoordinates'][0][1] + self._DesignParameter['M1V1M2_mid_mos_left_gate']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) + (self._DesignParameter['M1V1M2_mid_mos_left_gate']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2))) - min(((self._DesignParameter['M1V1M2_mid_mos_left_gate']['_XYCoordinates'][0][1] + self._DesignParameter['M1V1M2_mid_mos_left_gate']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) - (self._DesignParameter['M1V1M2_mid_mos_left_gate']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)), ((self._DesignParameter['PCCAM1_mid_nmos_left']['_XYCoordinates'][0][1] + self._DesignParameter['PCCAM1_mid_nmos_left']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) - (self._DesignParameter['PCCAM1_mid_nmos_left']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)))))
		self._DesignParameter['METAL1_boundary_354']['_XYCoordinates'] = [[int(((max(((self._DesignParameter['M1V1M2_mid_mos_left_gate']['_XYCoordinates'][0][0] + self._DesignParameter['M1V1M2_mid_mos_left_gate']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0]) + (self._DesignParameter['M1V1M2_mid_mos_left_gate']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] / 2)), ((self._DesignParameter['PCCAM1_mid_nmos_left']['_XYCoordinates'][0][0] + self._DesignParameter['PCCAM1_mid_nmos_left']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0]) + (self._DesignParameter['PCCAM1_mid_nmos_left']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] / 2))) + min(((self._DesignParameter['PCCAM1_mid_nmos_left']['_XYCoordinates'][0][0] + self._DesignParameter['PCCAM1_mid_nmos_left']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0]) - (self._DesignParameter['PCCAM1_mid_nmos_left']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] / 2)), ((self._DesignParameter['M1V1M2_mid_mos_left_gate']['_XYCoordinates'][0][0] + self._DesignParameter['M1V1M2_mid_mos_left_gate']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0]) - (self._DesignParameter['M1V1M2_mid_mos_left_gate']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] / 2)))) / 2)), int(((max(((self._DesignParameter['PCCAM1_mid_nmos_left']['_XYCoordinates'][0][1] + self._DesignParameter['PCCAM1_mid_nmos_left']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) + (self._DesignParameter['PCCAM1_mid_nmos_left']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)), ((self._DesignParameter['M1V1M2_mid_mos_left_gate']['_XYCoordinates'][0][1] + self._DesignParameter['M1V1M2_mid_mos_left_gate']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) + (self._DesignParameter['M1V1M2_mid_mos_left_gate']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2))) + min(((self._DesignParameter['M1V1M2_mid_mos_left_gate']['_XYCoordinates'][0][1] + self._DesignParameter['M1V1M2_mid_mos_left_gate']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) - (self._DesignParameter['M1V1M2_mid_mos_left_gate']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)), ((self._DesignParameter['PCCAM1_mid_nmos_left']['_XYCoordinates'][0][1] + self._DesignParameter['PCCAM1_mid_nmos_left']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) - (self._DesignParameter['PCCAM1_mid_nmos_left']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)))) / 2))]]
		self._DesignParameter['M1V1M2_mid_mos_right_gate'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='M1V1M2_mid_mos_right_gateIn{}'.format(_Name)))[0]
		self._DesignParameter['M1V1M2_mid_mos_right_gate']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureY(**dict(_ViaMet12Met2NumberOfCOX=2, _ViaMet12Met2NumberOfCOY=1))
		self._DesignParameter['M1V1M2_mid_mos_right_gate']['_XYCoordinates'] = [[self._DesignParameter['PCCAM1_mid_nmos_right']['_XYCoordinates'][0][0], self._DesignParameter['M1V1M2_mid_mos_left_gate']['_XYCoordinates'][0][1]]]
		self._DesignParameter['METAL1_boundary_353'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _XWidth=(max(((self._DesignParameter['PCCAM1_mid_nmos_right']['_XYCoordinates'][0][0] + self._DesignParameter['PCCAM1_mid_nmos_right']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0]) + (self._DesignParameter['PCCAM1_mid_nmos_right']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] / 2)), ((self._DesignParameter['M1V1M2_mid_mos_right_gate']['_XYCoordinates'][0][0] + self._DesignParameter['M1V1M2_mid_mos_right_gate']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0]) + (self._DesignParameter['M1V1M2_mid_mos_right_gate']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] / 2))) - min(((self._DesignParameter['M1V1M2_mid_mos_right_gate']['_XYCoordinates'][0][0] + self._DesignParameter['M1V1M2_mid_mos_right_gate']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0]) - (self._DesignParameter['M1V1M2_mid_mos_right_gate']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] / 2)), ((self._DesignParameter['PCCAM1_mid_nmos_right']['_XYCoordinates'][0][0] + self._DesignParameter['PCCAM1_mid_nmos_right']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0]) - (self._DesignParameter['PCCAM1_mid_nmos_right']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] / 2)))), _YWidth=(max(((self._DesignParameter['M1V1M2_mid_mos_right_gate']['_XYCoordinates'][0][1] + self._DesignParameter['M1V1M2_mid_mos_right_gate']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) + (self._DesignParameter['M1V1M2_mid_mos_right_gate']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)), ((self._DesignParameter['PCCAM1_mid_nmos_right']['_XYCoordinates'][0][1] + self._DesignParameter['PCCAM1_mid_nmos_right']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) + (self._DesignParameter['PCCAM1_mid_nmos_right']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2))) - min(((self._DesignParameter['PCCAM1_mid_nmos_right']['_XYCoordinates'][0][1] + self._DesignParameter['PCCAM1_mid_nmos_right']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) - (self._DesignParameter['PCCAM1_mid_nmos_right']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)), ((self._DesignParameter['M1V1M2_mid_mos_right_gate']['_XYCoordinates'][0][1] + self._DesignParameter['M1V1M2_mid_mos_right_gate']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) - (self._DesignParameter['M1V1M2_mid_mos_right_gate']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)))))
		self._DesignParameter['METAL1_boundary_353']['_XYCoordinates'] = [[int(((max(((self._DesignParameter['PCCAM1_mid_nmos_right']['_XYCoordinates'][0][0] + self._DesignParameter['PCCAM1_mid_nmos_right']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0]) + (self._DesignParameter['PCCAM1_mid_nmos_right']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] / 2)), ((self._DesignParameter['M1V1M2_mid_mos_right_gate']['_XYCoordinates'][0][0] + self._DesignParameter['M1V1M2_mid_mos_right_gate']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0]) + (self._DesignParameter['M1V1M2_mid_mos_right_gate']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] / 2))) + min(((self._DesignParameter['M1V1M2_mid_mos_right_gate']['_XYCoordinates'][0][0] + self._DesignParameter['M1V1M2_mid_mos_right_gate']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0]) - (self._DesignParameter['M1V1M2_mid_mos_right_gate']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] / 2)), ((self._DesignParameter['PCCAM1_mid_nmos_right']['_XYCoordinates'][0][0] + self._DesignParameter['PCCAM1_mid_nmos_right']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0]) - (self._DesignParameter['PCCAM1_mid_nmos_right']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] / 2)))) / 2)), int(((max(((self._DesignParameter['M1V1M2_mid_mos_right_gate']['_XYCoordinates'][0][1] + self._DesignParameter['M1V1M2_mid_mos_right_gate']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) + (self._DesignParameter['M1V1M2_mid_mos_right_gate']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)), ((self._DesignParameter['PCCAM1_mid_nmos_right']['_XYCoordinates'][0][1] + self._DesignParameter['PCCAM1_mid_nmos_right']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) + (self._DesignParameter['PCCAM1_mid_nmos_right']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2))) + min(((self._DesignParameter['PCCAM1_mid_nmos_right']['_XYCoordinates'][0][1] + self._DesignParameter['PCCAM1_mid_nmos_right']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) - (self._DesignParameter['PCCAM1_mid_nmos_right']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)), ((self._DesignParameter['M1V1M2_mid_mos_right_gate']['_XYCoordinates'][0][1] + self._DesignParameter['M1V1M2_mid_mos_right_gate']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) - (self._DesignParameter['M1V1M2_mid_mos_right_gate']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)))) / 2))]]
		path_list = []
		if (self._DesignParameter['mid_nmos_left']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0] == self._DesignParameter['mid_nmos_left']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]):
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
		if (self._DesignParameter['mid_nmos_right']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0] == self._DesignParameter['mid_nmos_right']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]):
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
		self._DesignParameter['nmos_inp']['_DesignObj']._CalculateNMOSDesignParameter(**dict(_NMOSNumberofGate=12, _NMOSChannelWidth=1000, _NMOSChannellength=30, _NMOSDummy=True, _GateSpacing=None, _XVT='SLVT'))
		self._DesignParameter['nmos_inp']['_XYCoordinates'] = [[(- 1386.0), (- 1016.0)]]
		num_of_inp_via = int((((self._DesignParameter['nmos_inp']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] - drc._VIAxMinSpace) - (2 * drc._VIAxMinEnclosureByMetx)) / (drc._VIAxMinWidth + drc._VIAxMinSpace)))
		XYList = []
		xy_offset = (0, int(((drc._VIAxMinWidth + drc._VIAxMinSpace) / 4)))
		for i in range(len(self._DesignParameter['nmos_inp']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'])):
		    if ((i % 2) == 0):
		        XYList.append([((x + y) + z) for (x, y, z) in zip([(0 + self._DesignParameter['nmos_inp']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['nmos_inp']['_XYCoordinates'][0][1])], self._DesignParameter['nmos_inp']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i], xy_offset)])
		self._DesignParameter['nmos_inp_drain_via'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='nmos_inp_drain_viaIn{}'.format(_Name)))[0]
		self._DesignParameter['nmos_inp_drain_via']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(**dict(_ViaMet12Met2NumberOfCOX=1, _ViaMet12Met2NumberOfCOY=num_of_inp_via))
		self._DesignParameter['nmos_inp_drain_via']['_XYCoordinates'] = XYList
		XYList = []
		xy_offset = (0, (- int(((drc._VIAxMinWidth + drc._VIAxMinSpace) / 4))))
		for i in range(len(self._DesignParameter['nmos_inp']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'])):
		    if ((i % 2) == 1):
		        XYList.append([((x + y) + z) for (x, y, z) in zip([(0 + self._DesignParameter['nmos_inp']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['nmos_inp']['_XYCoordinates'][0][1])], self._DesignParameter['nmos_inp']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i], xy_offset)])
		self._DesignParameter['nmos_inp_source_via'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='nmos_inp_source_viaIn{}'.format(_Name)))[0]
		self._DesignParameter['nmos_inp_source_via']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(**dict(_ViaMet12Met2NumberOfCOX=1, _ViaMet12Met2NumberOfCOY=num_of_inp_via))
		self._DesignParameter['nmos_inp_source_via']['_XYCoordinates'] = XYList
		self._DesignParameter['M2V2M3_inp_mos_drain'] = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_Name='M2V2M3_inp_mos_drainIn{}'.format(_Name)))[0]
		self._DesignParameter['M2V2M3_inp_mos_drain']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureY(**dict(_ViaMet22Met3NumberOfCOX=int(((((((self._DesignParameter['nmos_inp']['_XYCoordinates'][0][0] + self._DesignParameter['nmos_inp']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][(- 1)][0]) + (self._DesignParameter['nmos_inp']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] / 2)) - ((self._DesignParameter['nmos_inp']['_XYCoordinates'][0][0] + self._DesignParameter['nmos_inp']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0]) - (self._DesignParameter['nmos_inp']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] / 2))) - drc._VIAxMinSpace) - (2 * drc._VIAxMinEnclosureByMetx)) / (drc._VIAxMinWidth + drc._VIAxMinSpace))), _ViaMet22Met3NumberOfCOY=1))
		self._DesignParameter['M2V2M3_inp_mos_drain']['_XYCoordinates'] = [[self._DesignParameter['nmos_inp']['_XYCoordinates'][0][0], ((drc._VIAxMinSpace + ((self._DesignParameter['nmos_inp_drain_via']['_XYCoordinates'][0][1] + self._DesignParameter['nmos_inp_drain_via']['_DesignObj']._DesignParameter['_Met2Layer']['_XYCoordinates'][0][1]) + (self._DesignParameter['nmos_inp_drain_via']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] / 2))) + (self._DesignParameter['M2V2M3_inp_mos_drain']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] / 2))]]
		path_list = []
		if (self._DesignParameter['nmos_inp']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0] == self._DesignParameter['nmos_inp']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][(- 1)][0]):
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
		if (self._DesignParameter['mid_nmos_left']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0] == self._DesignParameter['mid_nmos_left']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][(- 1)][0]):
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
		self._DesignParameter['nmos_inn']['_DesignObj']._CalculateNMOSDesignParameter(**dict(_NMOSNumberofGate=12, _NMOSChannelWidth=1000, _NMOSChannellength=30, _NMOSDummy=True, _GateSpacing=None, _XVT='SLVT'))
		self._DesignParameter['nmos_inn']['_XYCoordinates'] = [[1386.0, (- 1016.0)]]
		self._DesignParameter['M2V2M3_inn_mos_drain'] = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_Name='M2V2M3_inn_mos_drainIn{}'.format(_Name)))[0]
		self._DesignParameter['M2V2M3_inn_mos_drain']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureY(**dict(_ViaMet22Met3NumberOfCOX=int(((((((self._DesignParameter['nmos_inp']['_XYCoordinates'][0][0] + self._DesignParameter['nmos_inp']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][(- 1)][0]) + (self._DesignParameter['nmos_inp']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] / 2)) - ((self._DesignParameter['nmos_inp']['_XYCoordinates'][0][0] + self._DesignParameter['nmos_inp']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0]) - (self._DesignParameter['nmos_inp']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] / 2))) - drc._VIAxMinSpace) - (2 * drc._VIAxMinEnclosureByMetx)) / (drc._VIAxMinWidth + drc._VIAxMinSpace))), _ViaMet22Met3NumberOfCOY=1))
		self._DesignParameter['M2V2M3_inn_mos_drain']['_XYCoordinates'] = [[self._DesignParameter['nmos_inn']['_XYCoordinates'][0][0], ((drc._VIAxMinSpace + ((self._DesignParameter['nmos_inp_drain_via']['_XYCoordinates'][0][1] + self._DesignParameter['nmos_inp_drain_via']['_DesignObj']._DesignParameter['_Met2Layer']['_XYCoordinates'][0][1]) + (self._DesignParameter['nmos_inp_drain_via']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] / 2))) + (self._DesignParameter['M2V2M3_inp_mos_drain']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] / 2))]]
		XYList = []
		xy_offset = (0, int(((drc._VIAxMinWidth + drc._VIAxMinSpace) / 4)))
		for i in range(len(self._DesignParameter['nmos_inn']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		    if ((i % 2) == 0):
		        XYList.append([((x + y) + z) for (x, y, z) in zip([(0 + self._DesignParameter['nmos_inn']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['nmos_inn']['_XYCoordinates'][0][1])], self._DesignParameter['nmos_inn']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i], xy_offset)])
		self._DesignParameter['nmos_inn_drain_via'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='nmos_inn_drain_viaIn{}'.format(_Name)))[0]
		self._DesignParameter['nmos_inn_drain_via']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(**dict(_ViaMet12Met2NumberOfCOX=1, _ViaMet12Met2NumberOfCOY=num_of_inp_via))
		self._DesignParameter['nmos_inn_drain_via']['_XYCoordinates'] = XYList
		XYList = []
		xy_offset = (0, (- int(((drc._VIAxMinWidth + drc._VIAxMinSpace) / 4))))
		for i in range(len(self._DesignParameter['nmos_inn']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		    if ((i % 2) == 1):
		        XYList.append([((x + y) + z) for (x, y, z) in zip([(0 + self._DesignParameter['nmos_inn']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['nmos_inn']['_XYCoordinates'][0][1])], self._DesignParameter['nmos_inn']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i], xy_offset)])
		self._DesignParameter['nmos_inn_source_via'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='nmos_inn_source_viaIn{}'.format(_Name)))[0]
		self._DesignParameter['nmos_inn_source_via']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(**dict(_ViaMet12Met2NumberOfCOX=1, _ViaMet12Met2NumberOfCOY=num_of_inp_via))
		self._DesignParameter['nmos_inn_source_via']['_XYCoordinates'] = XYList
		self._DesignParameter['M2V2M3_mid_node'] = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_Name='M2V2M3_mid_nodeIn{}'.format(_Name)))[0]
		self._DesignParameter['M2V2M3_mid_node']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureY(**dict(_ViaMet22Met3NumberOfCOX=4, _ViaMet22Met3NumberOfCOY=1))
		self._DesignParameter['M2V2M3_mid_node']['_XYCoordinates'] = [[self._DesignParameter['nmos_bot']['_XYCoordinates'][0][0], min(((((self._DesignParameter['M3V3M4_mid_mod_left']['_XYCoordinates'][0][1] + self._DesignParameter['M3V3M4_mid_mod_left']['_DesignObj']._DesignParameter['_Met4Layer']['_XYCoordinates'][0][1]) - (self._DesignParameter['M3V3M4_mid_mod_left']['_DesignObj']._DesignParameter['_Met4Layer']['_YWidth'] / 2)) - drc._MetalxMinSpace) - (self._DesignParameter['M2V2M3_mid_node']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth'] / 2)), ((((self._DesignParameter['nmos_inp_source_via']['_XYCoordinates'][0][1] + self._DesignParameter['nmos_inp_source_via']['_DesignObj']._DesignParameter['_Met2Layer']['_XYCoordinates'][0][1]) - (self._DesignParameter['nmos_inp_source_via']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] / 2)) - drc._MetalxMinSpace) - (self._DesignParameter['M2V2M3_mid_node']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] / 2)))]]
		self._DesignParameter['M3V3M4_mid_node'] = self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_Name='M3V3M4_mid_nodeIn{}'.format(_Name)))[0]
		self._DesignParameter['M3V3M4_mid_node']['_DesignObj']._CalculateViaMet32Met4DesignParameterMinimumEnclosureY(**dict(_ViaMet32Met4NumberOfCOX=4, _ViaMet32Met4NumberOfCOY=1))
		self._DesignParameter['M3V3M4_mid_node']['_XYCoordinates'] = [[self._DesignParameter['nmos_bot']['_XYCoordinates'][0][0], min(((((self._DesignParameter['M3V3M4_mid_mod_left']['_XYCoordinates'][0][1] + self._DesignParameter['M3V3M4_mid_mod_left']['_DesignObj']._DesignParameter['_Met4Layer']['_XYCoordinates'][0][1]) - (self._DesignParameter['M3V3M4_mid_mod_left']['_DesignObj']._DesignParameter['_Met4Layer']['_YWidth'] / 2)) - drc._MetalxMinSpace) - (self._DesignParameter['M2V2M3_mid_node']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth'] / 2)), ((((self._DesignParameter['nmos_inp_source_via']['_XYCoordinates'][0][1] + self._DesignParameter['nmos_inp_source_via']['_DesignObj']._DesignParameter['_Met2Layer']['_XYCoordinates'][0][1]) - (self._DesignParameter['nmos_inp_source_via']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] / 2)) - drc._MetalxMinSpace) - (self._DesignParameter['M2V2M3_mid_node']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] / 2)))]]
		self._DesignParameter['METAL2_path_27'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _Width=self._DesignParameter['M3V3M4_mid_node']['_DesignObj']._DesignParameter['_Met4Layer']['_YWidth'])
		self._DesignParameter['METAL2_path_27']['_XYCoordinates'] = [[[((self._DesignParameter['nmos_inp_source_via']['_XYCoordinates'][0][0] + self._DesignParameter['nmos_inp_source_via']['_DesignObj']._DesignParameter['_Met2Layer']['_XYCoordinates'][0][0]) - (self._DesignParameter['nmos_inp_source_via']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth'] / 2)), self._DesignParameter['M3V3M4_mid_node']['_XYCoordinates'][0][1]], [((self._DesignParameter['nmos_inn_source_via']['_XYCoordinates'][(- 1)][0] + self._DesignParameter['nmos_inn_source_via']['_DesignObj']._DesignParameter['_Met2Layer']['_XYCoordinates'][0][0]) + (self._DesignParameter['nmos_inn_source_via']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth'] / 2)), self._DesignParameter['M3V3M4_mid_node']['_XYCoordinates'][0][1]]]]
		path_list = []
		if (self._DesignParameter['nmos_inp']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0] == self._DesignParameter['nmos_inp']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][(- 1)][0]):
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
		if (self._DesignParameter['nmos_inn']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0] == self._DesignParameter['nmos_inn']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][(- 1)][0]):
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
		self._DesignParameter['PCCAM1_inp_mos_gate']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(**dict(_ViaPoly2Met1NumberOfCOX=int(((((((self._DesignParameter['nmos_inp']['_XYCoordinates'][0][0] + self._DesignParameter['nmos_inp']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]) + (self._DesignParameter['nmos_inp']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)) - ((self._DesignParameter['nmos_inp']['_XYCoordinates'][0][0] + self._DesignParameter['nmos_inp']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['nmos_inp']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2))) - drc._CoMinSpace) - (2 * drc._CoMinEnclosureByPO)) / (drc._CoMinWidth + drc._CoMinSpace))), _ViaPoly2Met1NumberOfCOY=input_via_y))
		self._DesignParameter['PCCAM1_inp_mos_gate']['_XYCoordinates'] = [[self._DesignParameter['nmos_inp']['_XYCoordinates'][0][0], (((- self._DesignParameter['PCCAM1_inp_mos_gate']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']) / 2) + ((self._DesignParameter['METAL2_path_27']['_XYCoordinates'][0][0][1] - self._DesignParameter['METAL2_path_27']['_Width']) - drc._Metal1MinSpace))]]
		path_list = []
		if (self._DesignParameter['nmos_inp']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0] == self._DesignParameter['nmos_inp']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]):
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
		self._DesignParameter['PCCAM1_inn_mos_gate']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(**dict(_ViaPoly2Met1NumberOfCOX=int(((((((self._DesignParameter['nmos_inp']['_XYCoordinates'][0][0] + self._DesignParameter['nmos_inp']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]) + (self._DesignParameter['nmos_inp']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)) - ((self._DesignParameter['nmos_inp']['_XYCoordinates'][0][0] + self._DesignParameter['nmos_inp']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['nmos_inp']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2))) - drc._CoMinSpace) - (2 * drc._CoMinEnclosureByPO)) / (drc._CoMinWidth + drc._CoMinSpace))), _ViaPoly2Met1NumberOfCOY=input_via_y))
		self._DesignParameter['PCCAM1_inn_mos_gate']['_XYCoordinates'] = [[self._DesignParameter['nmos_inn']['_XYCoordinates'][0][0], (((- self._DesignParameter['PCCAM1_inp_mos_gate']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']) / 2) + ((self._DesignParameter['METAL2_path_27']['_XYCoordinates'][0][0][1] - self._DesignParameter['METAL2_path_27']['_Width']) - drc._Metal1MinSpace))]]
		path_list = []
		if (self._DesignParameter['nmos_inn']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0] == self._DesignParameter['nmos_inn']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]):
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
		if (self._DesignParameter['mid_nmos_right']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0] == self._DesignParameter['mid_nmos_right']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][(- 1)][0]):
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
		if (self._DesignParameter['nmos_inn']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0] == self._DesignParameter['nmos_inn']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][(- 1)][0]):
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
		