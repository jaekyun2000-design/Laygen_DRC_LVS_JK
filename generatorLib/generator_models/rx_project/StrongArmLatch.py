from generatorLib import StickDiagram
from generatorLib import DesignParameters
import copy
import math
from generatorLib import DRC
from generatorLib.generator_models.rx_project import PMOSWithDummy
from generatorLib.generator_models.rx_project import ViaMet22Met3
from generatorLib.generator_models.rx_project import ViaPoly2Met1
from generatorLib.generator_models.rx_project import NSubRing
from generatorLib.generator_models.rx_project import PSubRing
from generatorLib.generator_models.rx_project import NMOSWithDummy
from generatorLib.generator_models.rx_project import ViaMet12Met2
from generatorLib.generator_models.rx_project import ViaStack
from generatorLib.generator_models.rx_project import ViaMet32Met4

class SlicerInSlicerWithSRLatch_0(StickDiagram._StickDiagram):
	def __init__(self, _DesignParameter=None, _Name='SlicerInSlicerWithSRLatch_0'):
		if _DesignParameter != None:
			self._DesignParameter = _DesignParameter
		else:
			self._DesignParameter = dict(_Name=self._NameDeclaration(_Name=_Name), _GDSFile=self._GDSObjDeclaration(_GDSFile=None))
		self._DesignParameter['_Name']['Name'] = _Name

	def _CalculateDesignParameter(self,subring_option={'via_num': 2, 'nmos_subring_addi_width': 100, 'additional_np_distance': 100, 'additional_outer_height': 100},pmos_outer_gate=6,pmos_inner_gate=3,nmos_parms={'common_width': 1000, 'nmos_bot_gate': 8, 'nmos_inner_gate': 2, 'nmos_outer_gate': 12, 'bot_width': 1000, 'nmos_inner_width': 500},pmos_parms={'common_width': 500, 'inner_gate': 3}):
	
		drc = DRC.DRC()
		_Name = self._DesignParameter['_Name']['_Name']
		
		self._DesignParameter['nmos_bot'] = self._SrefElementDeclaration(_DesignObj=NMOSWithDummy._NMOS(_Name='nmos_botIn{}'.format(_Name)))[0]
		self._DesignParameter['nmos_bot']['_DesignObj']._CalculateNMOSDesignParameter(**dict(dict(_NMOSNumberofGate=nmos_parms['nmos_bot_gate'], _NMOSChannelWidth=nmos_parms['bot_width'], _NMOSChannellength=30, _NMOSDummy=True, _GateSpacing=None, _SDWidth=None, _XVT='SLVT', _PCCrit=None)))
		self._DesignParameter['nmos_bot']['_XYCoordinates'] = [[0, (- 2495)]]
		nmos_inner = dict(_NMOSNumberofGate=nmos_parms['nmos_inner_gate'], _NMOSChannelWidth=nmos_parms['nmos_inner_width'], _NMOSChannellength=30, _NMOSDummy=True, _GateSpacing=None, _SDWidth=None, _XVT='SLVT', _PCCrit=None)
		self._DesignParameter['nmos_bot_gate_poly_via'] = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_Name='nmos_bot_gate_poly_viaIn{}'.format(_Name)))[0]
		self._DesignParameter['nmos_bot_gate_poly_via']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(**dict(_ViaPoly2Met1NumberOfCOX=max(1, (1 + int(((((((self._DesignParameter['nmos_bot']['_XYCoordinates'][0][0] + self._DesignParameter['nmos_bot']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]) + (self._DesignParameter['nmos_bot']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)) - ((self._DesignParameter['nmos_bot']['_XYCoordinates'][0][0] + self._DesignParameter['nmos_bot']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['nmos_bot']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2))) - drc._CoMinSpace) - (2 * drc._CoMinEnclosureByPO)) / (drc._CoMinWidth + drc._CoMinSpace))))), _ViaPoly2Met1NumberOfCOY=1))
		self._DesignParameter['nmos_bot_gate_poly_via']['_XYCoordinates'] = [[self._DesignParameter['nmos_bot']['_XYCoordinates'][0][0], ((((self._DesignParameter['nmos_bot']['_XYCoordinates'][0][1] + self._DesignParameter['nmos_bot']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) + (self._DesignParameter['nmos_bot']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)) + drc._Metal1MinSpace21) + (self._DesignParameter['nmos_bot_gate_poly_via']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2))]]
		self._DesignParameter['NMOS3InNMOSSetofSlicer_0'] = self._SrefElementDeclaration(_DesignObj=NMOSWithDummy._NMOS(_Name='NMOS3InNMOSSetofSlicer_0In{}'.format(_Name)))[0]
		self._DesignParameter['NMOS3InNMOSSetofSlicer_0']['_DesignObj']._CalculateNMOSDesignParameter(**dict(**nmos_inner))
		self._DesignParameter['NMOS3InNMOSSetofSlicer_0']['_XYCoordinates'] = [[(((- drc._PolygateMinSpace) / 2) + (- (self._DesignParameter['NMOS3InNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][(- 1)][0] + (self._DesignParameter['NMOS3InNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_PODummyLayer']['_XWidth'] / 2)))), ((((((self._DesignParameter['nmos_bot_gate_poly_via']['_XYCoordinates'][0][1] + self._DesignParameter['nmos_bot_gate_poly_via']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) + (self._DesignParameter['nmos_bot_gate_poly_via']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)) + drc._Metal1MinSpace3) + (self._DesignParameter['nmos_bot_gate_poly_via']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] * 2.5)) + drc._Metal1MinSpace21) - (self._DesignParameter['NMOS3InNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1] - (self._DesignParameter['NMOS3InNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)))]]
		self._DesignParameter['NMOS4InNMOSSetofSlicer_0'] = self._SrefElementDeclaration(_DesignObj=NMOSWithDummy._NMOS(_Name='NMOS4InNMOSSetofSlicer_0In{}'.format(_Name)))[0]
		self._DesignParameter['NMOS4InNMOSSetofSlicer_0']['_DesignObj']._CalculateNMOSDesignParameter(**dict(**nmos_inner))
		self._DesignParameter['NMOS4InNMOSSetofSlicer_0']['_XYCoordinates'] = [[((drc._PolygateMinSpace / 2) + (- (self._DesignParameter['NMOS4InNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][0] - (self._DesignParameter['NMOS4InNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_PODummyLayer']['_XWidth'] / 2)))), self._DesignParameter['NMOS3InNMOSSetofSlicer_0']['_XYCoordinates'][0][1]]]
		nmos_outer = dict(_NMOSNumberofGate=nmos_parms['nmos_outer_gate'], _NMOSChannelWidth=nmos_parms['common_width'], _NMOSChannellength=30, _NMOSDummy=True, _GateSpacing=None, _SDWidth=None, _XVT='SLVT', _PCCrit=None)
		self._DesignParameter['NMOS1InNMOSSetofSlicer_0'] = self._SrefElementDeclaration(_DesignObj=NMOSWithDummy._NMOS(_Name='NMOS1InNMOSSetofSlicer_0In{}'.format(_Name)))[0]
		self._DesignParameter['NMOS1InNMOSSetofSlicer_0']['_DesignObj']._CalculateNMOSDesignParameter(**dict(**nmos_outer))
		self._DesignParameter['NMOS1InNMOSSetofSlicer_0']['_XYCoordinates'] = [[(((- (self._DesignParameter['NMOS1InNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][(- 1)][0] + (self._DesignParameter['NMOS1InNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_PODummyLayer']['_XWidth'] / 2))) + (- drc._PolygateMinSpace)) + ((self._DesignParameter['NMOS3InNMOSSetofSlicer_0']['_XYCoordinates'][0][0] + self._DesignParameter['NMOS3InNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['NMOS3InNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_PODummyLayer']['_XWidth'] / 2))), self._DesignParameter['NMOS3InNMOSSetofSlicer_0']['_XYCoordinates'][0][1]]]
		self._DesignParameter['NMOS2InNMOSSetofSlicer_0'] = self._SrefElementDeclaration(_DesignObj=NMOSWithDummy._NMOS(_Name='NMOS2InNMOSSetofSlicer_0In{}'.format(_Name)))[0]
		self._DesignParameter['NMOS2InNMOSSetofSlicer_0']['_DesignObj']._CalculateNMOSDesignParameter(**dict(**nmos_outer))
		self._DesignParameter['NMOS2InNMOSSetofSlicer_0']['_XYCoordinates'] = [[((((self._DesignParameter['NMOS4InNMOSSetofSlicer_0']['_XYCoordinates'][0][0] + self._DesignParameter['NMOS4InNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][(- 1)][0]) + (self._DesignParameter['NMOS4InNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_PODummyLayer']['_XWidth'] / 2)) - (self._DesignParameter['NMOS2InNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][0] - (self._DesignParameter['NMOS2InNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_PODummyLayer']['_XWidth'] / 2))) + drc._PolygateMinSpace), self._DesignParameter['NMOS4InNMOSSetofSlicer_0']['_XYCoordinates'][0][1]]]
		nmos_bot_coy = max(1, (1 + int((((self._DesignParameter['nmos_bot']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] - drc._VIAxMinSpace) - (2 * drc._VIAxMinEnclosureByMetx)) / (drc._VIAxMinWidth + drc._VIAxMinSpace)))))
		self._DesignParameter['nmos_bot_drain_vias'] = self._SrefElementDeclaration(_DesignObj=ViaStack._ViaStack(_Name='nmos_bot_drain_viasIn{}'.format(_Name)))[0]
		self._DesignParameter['nmos_bot_drain_vias']['_DesignObj']._CalculateStackMinimumEnclosureX(**dict(COX=1, COY=nmos_bot_coy, start_layer=1, end_layer=4))
		self._DesignParameter['nmos_bot_drain_vias']['_XYCoordinates'] = None
		XYList = []
		xy_offset = [0, 0]
		for i in range(len(self._DesignParameter['nmos_bot']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'])):
		    if ((i % 2) == 0):
		        xy = (self._DesignParameter['nmos_bot']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i][0] if (type(self._DesignParameter['nmos_bot']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i][0]) == list) else self._DesignParameter['nmos_bot']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i])
		        XYList.append([((x + y) + z) for (x, y, z) in zip([(0 + self._DesignParameter['nmos_bot']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['nmos_bot']['_XYCoordinates'][0][1])], xy, xy_offset)])
		self._DesignParameter['nmos_bot_drain_vias']['_XYCoordinates'] = XYList
		self._DesignParameter['METAL4_path_14'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL4'][0], _Datatype=DesignParameters._LayerMapping['METAL4'][1], _Width=drc._MetalxMinWidth)
		self._DesignParameter['METAL4_path_14']['_XYCoordinates'] = [[[(+ self._DesignParameter['nmos_bot_drain_vias']['_XYCoordinates'][0][0]), (+ self._DesignParameter['nmos_bot_drain_vias']['_XYCoordinates'][0][1])], [(+ self._DesignParameter['nmos_bot_drain_vias']['_XYCoordinates'][(- 1)][0]), (+ self._DesignParameter['nmos_bot_drain_vias']['_XYCoordinates'][(- 1)][1])]]]
		self._DesignParameter['METAL3_path_27'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0], _Datatype=DesignParameters._LayerMapping['METAL3'][1], _Width=drc._MetalxMinWidth)
		self._DesignParameter['METAL3_path_27']['_XYCoordinates'] = [[[(+ self._DesignParameter['nmos_bot_drain_vias']['_XYCoordinates'][0][0]), (+ self._DesignParameter['nmos_bot_drain_vias']['_XYCoordinates'][0][1])], [(+ self._DesignParameter['nmos_bot_drain_vias']['_XYCoordinates'][(- 1)][0]), (+ self._DesignParameter['nmos_bot_drain_vias']['_XYCoordinates'][(- 1)][1])]]]
		self._DesignParameter['METAL2_path_30'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _Width=drc._MetalxMinWidth)
		self._DesignParameter['METAL2_path_30']['_XYCoordinates'] = [[[(+ self._DesignParameter['nmos_bot_drain_vias']['_XYCoordinates'][0][0]), (+ self._DesignParameter['nmos_bot_drain_vias']['_XYCoordinates'][0][1])], [(+ self._DesignParameter['nmos_bot_drain_vias']['_XYCoordinates'][(- 1)][0]), (+ self._DesignParameter['nmos_bot_drain_vias']['_XYCoordinates'][(- 1)][1])]]]
		self._DesignParameter['nmos_bot_viastack'] = self._SrefElementDeclaration(_DesignObj=ViaStack._ViaStack(_Name='nmos_bot_viastackIn{}'.format(_Name)))[0]
		self._DesignParameter['nmos_bot_viastack']['_DesignObj']._CalculateStackMinimumEnclosureY(**dict(COY=1, start_layer=1, end_layer=3, COX=max(1, (1 + int(((((((self._DesignParameter['nmos_bot']['_XYCoordinates'][0][0] + self._DesignParameter['nmos_bot']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]) + (self._DesignParameter['nmos_bot']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)) - ((self._DesignParameter['nmos_bot']['_XYCoordinates'][0][0] + self._DesignParameter['nmos_bot']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['nmos_bot']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2))) - drc._VIAxMinSpace) - (2 * drc._VIAxMinEnclosureByMetx)) / (drc._VIAxMinWidth + drc._VIAxMinSpace)))))))
		self._DesignParameter['nmos_bot_viastack']['_XYCoordinates'] = [[(+ self._DesignParameter['nmos_bot_gate_poly_via']['_XYCoordinates'][0][0]), (+ self._DesignParameter['nmos_bot_gate_poly_via']['_XYCoordinates'][0][1])]]
		path_list = []
		xy_offset = [0, 0]
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
		    target_y_value = [[(+ self._DesignParameter['nmos_bot_gate_poly_via']['_XYCoordinates'][0][0]), (+ self._DesignParameter['nmos_bot_gate_poly_via']['_XYCoordinates'][0][1])]][0][1]
		    for i in range(len(self._DesignParameter['nmos_bot']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
		        xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['nmos_bot']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['nmos_bot']['_XYCoordinates'][0][1])], self._DesignParameter['nmos_bot']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		elif (mode == 'horizontal'):
		    xy_with_offset = []
		    target_x_value = [[(+ self._DesignParameter['nmos_bot_gate_poly_via']['_XYCoordinates'][0][0]), (+ self._DesignParameter['nmos_bot_gate_poly_via']['_XYCoordinates'][0][1])]][0][0]
		    for i in range(len(self._DesignParameter['nmos_bot']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
		        xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['nmos_bot']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['nmos_bot']['_XYCoordinates'][0][1])], self._DesignParameter['nmos_bot']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		for i in range(len(path_list)):
		    path_list[i][0] = [(xy + offset) for (xy, offset) in zip(path_list[i][0], xy_offset)]
		self._DesignParameter['nmos_bot_gate'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _Width=_width)
		self._DesignParameter['nmos_bot_gate']['_XYCoordinates'] = path_list
		self._DesignParameter['pccam_nmos_left'] = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_Name='pccam_nmos_leftIn{}'.format(_Name)))[0]
		self._DesignParameter['pccam_nmos_left']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(**dict(_ViaPoly2Met1NumberOfCOX=max(1, (1 + int(((((((self._DesignParameter['NMOS1InNMOSSetofSlicer_0']['_XYCoordinates'][0][0] + self._DesignParameter['NMOS1InNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]) + (self._DesignParameter['NMOS1InNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)) - ((self._DesignParameter['NMOS1InNMOSSetofSlicer_0']['_XYCoordinates'][0][0] + self._DesignParameter['NMOS1InNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['NMOS1InNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2))) - drc._CoMinSpace) - (2 * drc._CoMinEnclosureByPO)) / (drc._CoMinWidth + drc._CoMinSpace))))), _ViaPoly2Met1NumberOfCOY=2))
		self._DesignParameter['pccam_nmos_left']['_XYCoordinates'] = [[self._DesignParameter['NMOS1InNMOSSetofSlicer_0']['_XYCoordinates'][0][0], ((((self._DesignParameter['NMOS1InNMOSSetofSlicer_0']['_XYCoordinates'][0][1] + self._DesignParameter['NMOS1InNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) - (self._DesignParameter['NMOS1InNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)) - drc._Metal1MinSpace21) - (self._DesignParameter['pccam_nmos_left']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2))]]
		self._DesignParameter['pccam_nmos_right'] = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_Name='pccam_nmos_rightIn{}'.format(_Name)))[0]
		self._DesignParameter['pccam_nmos_right']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(**dict(_ViaPoly2Met1NumberOfCOX=max(1, (1 + int(((((((self._DesignParameter['NMOS1InNMOSSetofSlicer_0']['_XYCoordinates'][0][0] + self._DesignParameter['NMOS1InNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]) + (self._DesignParameter['NMOS1InNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)) - ((self._DesignParameter['NMOS1InNMOSSetofSlicer_0']['_XYCoordinates'][0][0] + self._DesignParameter['NMOS1InNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['NMOS1InNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2))) - drc._CoMinSpace) - (2 * drc._CoMinEnclosureByPO)) / (drc._CoMinWidth + drc._CoMinSpace))))), _ViaPoly2Met1NumberOfCOY=2))
		self._DesignParameter['pccam_nmos_right']['_XYCoordinates'] = [[self._DesignParameter['NMOS2InNMOSSetofSlicer_0']['_XYCoordinates'][0][0], ((((self._DesignParameter['NMOS1InNMOSSetofSlicer_0']['_XYCoordinates'][0][1] + self._DesignParameter['NMOS1InNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) - (self._DesignParameter['NMOS1InNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)) - drc._Metal1MinSpace21) - (self._DesignParameter['pccam_nmos_left']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2))]]
		path_list = []
		xy_offset = [0, 0]
		if (len(self._DesignParameter['NMOS1InNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates']) == 1):
		    mode = 'vertical'
		    _width = self._DesignParameter['NMOS1InNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
		elif (self._DesignParameter['NMOS1InNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0] == self._DesignParameter['NMOS1InNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]):
		    mode = 'horizontal'
		    _width = self._DesignParameter['NMOS1InNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
		elif (self._DesignParameter['NMOS1InNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1] == self._DesignParameter['NMOS1InNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][1]):
		    mode = 'vertical'
		    _width = self._DesignParameter['NMOS1InNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
		else:
		    print('Invalid Target Input')
		if (mode == 'vertical'):
		    xy_with_offset = []
		    target_y_value = [[(+ self._DesignParameter['pccam_nmos_left']['_XYCoordinates'][0][0]), (+ self._DesignParameter['pccam_nmos_left']['_XYCoordinates'][0][1])]][0][1]
		    for i in range(len(self._DesignParameter['NMOS1InNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
		        xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['NMOS1InNMOSSetofSlicer_0']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['NMOS1InNMOSSetofSlicer_0']['_XYCoordinates'][0][1])], self._DesignParameter['NMOS1InNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		elif (mode == 'horizontal'):
		    xy_with_offset = []
		    target_x_value = [[(+ self._DesignParameter['pccam_nmos_left']['_XYCoordinates'][0][0]), (+ self._DesignParameter['pccam_nmos_left']['_XYCoordinates'][0][1])]][0][0]
		    for i in range(len(self._DesignParameter['NMOS1InNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
		        xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['NMOS1InNMOSSetofSlicer_0']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['NMOS1InNMOSSetofSlicer_0']['_XYCoordinates'][0][1])], self._DesignParameter['NMOS1InNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		for i in range(len(path_list)):
		    path_list[i][0] = [(xy + offset) for (xy, offset) in zip(path_list[i][0], xy_offset)]
		self._DesignParameter['nmos_left_gate'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _Width=_width)
		self._DesignParameter['nmos_left_gate']['_XYCoordinates'] = path_list
		path_list = []
		xy_offset = [0, 0]
		if (len(self._DesignParameter['NMOS2InNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates']) == 1):
		    mode = 'vertical'
		    _width = self._DesignParameter['NMOS2InNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
		elif (self._DesignParameter['NMOS2InNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0] == self._DesignParameter['NMOS2InNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]):
		    mode = 'horizontal'
		    _width = self._DesignParameter['NMOS2InNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
		elif (self._DesignParameter['NMOS2InNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1] == self._DesignParameter['NMOS2InNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][1]):
		    mode = 'vertical'
		    _width = self._DesignParameter['NMOS2InNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
		else:
		    print('Invalid Target Input')
		if (mode == 'vertical'):
		    xy_with_offset = []
		    target_y_value = [[(+ self._DesignParameter['pccam_nmos_right']['_XYCoordinates'][0][0]), (+ self._DesignParameter['pccam_nmos_right']['_XYCoordinates'][0][1])]][0][1]
		    for i in range(len(self._DesignParameter['NMOS2InNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
		        xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['NMOS2InNMOSSetofSlicer_0']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['NMOS2InNMOSSetofSlicer_0']['_XYCoordinates'][0][1])], self._DesignParameter['NMOS2InNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		elif (mode == 'horizontal'):
		    xy_with_offset = []
		    target_x_value = [[(+ self._DesignParameter['pccam_nmos_right']['_XYCoordinates'][0][0]), (+ self._DesignParameter['pccam_nmos_right']['_XYCoordinates'][0][1])]][0][0]
		    for i in range(len(self._DesignParameter['NMOS2InNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
		        xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['NMOS2InNMOSSetofSlicer_0']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['NMOS2InNMOSSetofSlicer_0']['_XYCoordinates'][0][1])], self._DesignParameter['NMOS2InNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		for i in range(len(path_list)):
		    path_list[i][0] = [(xy + offset) for (xy, offset) in zip(path_list[i][0], xy_offset)]
		self._DesignParameter['nmos_right_gate'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _Width=_width)
		self._DesignParameter['nmos_right_gate']['_XYCoordinates'] = path_list
		nmos_coy = max(1, (1 + int((((self._DesignParameter['NMOS1InNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] - drc._VIAxMinSpace) - (2 * drc._VIAxMinEnclosureByMetx)) / (drc._VIAxMinWidth + drc._VIAxMinSpace)))))
		self._DesignParameter['nmos_left_drain'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='nmos_left_drainIn{}'.format(_Name)))[0]
		self._DesignParameter['nmos_left_drain']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(**dict(_ViaMet12Met2NumberOfCOX=1, _ViaMet12Met2NumberOfCOY=nmos_coy))
		self._DesignParameter['nmos_left_drain']['_XYCoordinates'] = None
		XYList = []
		xy_offset = (0, int(((drc._VIAxMinWidth + drc._VIAxMinSpace) / 4)))
		for i in range(len(self._DesignParameter['NMOS1InNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		    if ((i % 2) == 0):
		        xy = (self._DesignParameter['NMOS1InNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i][0] if (type(self._DesignParameter['NMOS1InNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i][0]) == list) else self._DesignParameter['NMOS1InNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])
		        XYList.append([((x + y) + z) for (x, y, z) in zip([(0 + self._DesignParameter['NMOS1InNMOSSetofSlicer_0']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['NMOS1InNMOSSetofSlicer_0']['_XYCoordinates'][0][1])], xy, xy_offset)])
		self._DesignParameter['nmos_left_drain']['_XYCoordinates'] = XYList
		self._DesignParameter['nmos_left_source'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='nmos_left_sourceIn{}'.format(_Name)))[0]
		self._DesignParameter['nmos_left_source']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(**dict(_ViaMet12Met2NumberOfCOX=1, _ViaMet12Met2NumberOfCOY=nmos_coy))
		self._DesignParameter['nmos_left_source']['_XYCoordinates'] = None
		XYList = []
		xy_offset = (0, (- int(((drc._VIAxMinWidth + drc._VIAxMinSpace) / 4))))
		for i in range(len(self._DesignParameter['NMOS1InNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		    if ((i % 2) == 1):
		        xy = (self._DesignParameter['NMOS1InNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i][0] if (type(self._DesignParameter['NMOS1InNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i][0]) == list) else self._DesignParameter['NMOS1InNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])
		        XYList.append([((x + y) + z) for (x, y, z) in zip([(0 + self._DesignParameter['NMOS1InNMOSSetofSlicer_0']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['NMOS1InNMOSSetofSlicer_0']['_XYCoordinates'][0][1])], xy, xy_offset)])
		self._DesignParameter['nmos_left_source']['_XYCoordinates'] = XYList
		self._DesignParameter['nmos_right_drain'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='nmos_right_drainIn{}'.format(_Name)))[0]
		self._DesignParameter['nmos_right_drain']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(**dict(_ViaMet12Met2NumberOfCOX=1, _ViaMet12Met2NumberOfCOY=nmos_coy))
		self._DesignParameter['nmos_right_drain']['_XYCoordinates'] = None
		XYList = []
		xy_offset = (0, int(((drc._VIAxMinWidth + drc._VIAxMinSpace) / 4)))
		for i in range(len(self._DesignParameter['NMOS2InNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		    if ((i % 2) == 0):
		        xy = (self._DesignParameter['NMOS2InNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i][0] if (type(self._DesignParameter['NMOS2InNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i][0]) == list) else self._DesignParameter['NMOS2InNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])
		        XYList.append([((x + y) + z) for (x, y, z) in zip([(0 + self._DesignParameter['NMOS2InNMOSSetofSlicer_0']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['NMOS2InNMOSSetofSlicer_0']['_XYCoordinates'][0][1])], xy, xy_offset)])
		self._DesignParameter['nmos_right_drain']['_XYCoordinates'] = XYList
		self._DesignParameter['nmos_right_source'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='nmos_right_sourceIn{}'.format(_Name)))[0]
		self._DesignParameter['nmos_right_source']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(**dict(_ViaMet12Met2NumberOfCOX=1, _ViaMet12Met2NumberOfCOY=nmos_coy))
		self._DesignParameter['nmos_right_source']['_XYCoordinates'] = None
		XYList = []
		xy_offset = (0, (- int(((drc._VIAxMinWidth + drc._VIAxMinSpace) / 4))))
		for i in range(len(self._DesignParameter['NMOS2InNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		    if ((i % 2) == 1):
		        xy = (self._DesignParameter['NMOS2InNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i][0] if (type(self._DesignParameter['NMOS2InNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i][0]) == list) else self._DesignParameter['NMOS2InNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])
		        XYList.append([((x + y) + z) for (x, y, z) in zip([(0 + self._DesignParameter['NMOS2InNMOSSetofSlicer_0']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['NMOS2InNMOSSetofSlicer_0']['_XYCoordinates'][0][1])], xy, xy_offset)])
		self._DesignParameter['nmos_right_source']['_XYCoordinates'] = XYList
		self._DesignParameter['POLY_path_62'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _Width=self._DesignParameter['pccam_nmos_left']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'])
		self._DesignParameter['POLY_path_62']['_XYCoordinates'] = [[[(self._DesignParameter['nmos_left_gate']['_XYCoordinates'][0][0][0] - (self._DesignParameter['nmos_left_gate']['_Width'] / 2)), self._DesignParameter['pccam_nmos_left']['_XYCoordinates'][0][1]], [(self._DesignParameter['nmos_left_gate']['_XYCoordinates'][(- 1)][0][0] + (self._DesignParameter['nmos_left_gate']['_Width'] / 2)), self._DesignParameter['pccam_nmos_left']['_XYCoordinates'][0][1]]]]
		self._DesignParameter['POLY_path_64'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _Width=self._DesignParameter['pccam_nmos_left']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'])
		self._DesignParameter['POLY_path_64']['_XYCoordinates'] = [[[(self._DesignParameter['nmos_right_gate']['_XYCoordinates'][0][0][0] - (self._DesignParameter['nmos_right_gate']['_Width'] / 2)), self._DesignParameter['pccam_nmos_left']['_XYCoordinates'][0][1]], [(self._DesignParameter['nmos_right_gate']['_XYCoordinates'][(- 1)][0][0] + (self._DesignParameter['nmos_right_gate']['_Width'] / 2)), self._DesignParameter['pccam_nmos_left']['_XYCoordinates'][0][1]]]]
		nmos_coy = max(1, (1 + int((((self._DesignParameter['NMOS3InNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] - drc._VIAxMinSpace) - (2 * drc._VIAxMinEnclosureByMetx)) / (drc._VIAxMinWidth + drc._VIAxMinSpace)))))
		self._DesignParameter['M1V1M2_CDNS_6375475055674_1'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='M1V1M2_CDNS_6375475055674_1In{}'.format(_Name)))[0]
		self._DesignParameter['M1V1M2_CDNS_6375475055674_1']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(**dict(_ViaMet12Met2NumberOfCOX=1, _ViaMet12Met2NumberOfCOY=nmos_coy))
		self._DesignParameter['M1V1M2_CDNS_6375475055674_1']['_XYCoordinates'] = [[(+ (self._DesignParameter['NMOS3InNMOSSetofSlicer_0']['_XYCoordinates'][0][0] + self._DesignParameter['NMOS3InNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][(- 1)][0])), ((- int(((drc._VIAxMinWidth + drc._VIAxMinSpace) / 4))) + (self._DesignParameter['NMOS3InNMOSSetofSlicer_0']['_XYCoordinates'][0][1] + self._DesignParameter['NMOS3InNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][(- 1)][1]))]]
		self._DesignParameter['M1V1M2_CDNS_6375475055674_0'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='M1V1M2_CDNS_6375475055674_0In{}'.format(_Name)))[0]
		self._DesignParameter['M1V1M2_CDNS_6375475055674_0']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(**dict(_ViaMet12Met2NumberOfCOX=1, _ViaMet12Met2NumberOfCOY=nmos_coy))
		self._DesignParameter['M1V1M2_CDNS_6375475055674_0']['_XYCoordinates'] = [[(+ (self._DesignParameter['NMOS4InNMOSSetofSlicer_0']['_XYCoordinates'][0][0] + self._DesignParameter['NMOS4InNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0])), ((- int(((drc._VIAxMinWidth + drc._VIAxMinSpace) / 4))) + (self._DesignParameter['NMOS4InNMOSSetofSlicer_0']['_XYCoordinates'][0][1] + self._DesignParameter['NMOS4InNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]))]]
		self._DesignParameter['nmos_inner_left_vias'] = self._SrefElementDeclaration(_DesignObj=ViaStack._ViaStack(_Name='nmos_inner_left_viasIn{}'.format(_Name)))[0]
		self._DesignParameter['nmos_inner_left_vias']['_DesignObj']._CalculateStackMinimumEnclosureX(**dict(COX=1, COY=nmos_coy, start_layer=2, end_layer=4))
		self._DesignParameter['nmos_inner_left_vias']['_XYCoordinates'] = [[(+ (self._DesignParameter['NMOS3InNMOSSetofSlicer_0']['_XYCoordinates'][0][0] + self._DesignParameter['NMOS3InNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][(- 1)][0])), (+ (self._DesignParameter['NMOS3InNMOSSetofSlicer_0']['_XYCoordinates'][0][1] + self._DesignParameter['NMOS3InNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][(- 1)][1]))]]
		self._DesignParameter['nmos_inner_right_vias'] = self._SrefElementDeclaration(_DesignObj=ViaStack._ViaStack(_Name='nmos_inner_right_viasIn{}'.format(_Name)))[0]
		self._DesignParameter['nmos_inner_right_vias']['_DesignObj']._CalculateStackMinimumEnclosureX(**dict(COX=1, COY=nmos_coy, start_layer=2, end_layer=4))
		self._DesignParameter['nmos_inner_right_vias']['_XYCoordinates'] = [[(+ (self._DesignParameter['NMOS4InNMOSSetofSlicer_0']['_XYCoordinates'][0][0] + self._DesignParameter['NMOS4InNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0])), (+ (self._DesignParameter['NMOS4InNMOSSetofSlicer_0']['_XYCoordinates'][0][1] + self._DesignParameter['NMOS4InNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]))]]
		self._DesignParameter['nmos_inner_left_via_arr'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='nmos_inner_left_via_arrIn{}'.format(_Name)))[0]
		self._DesignParameter['nmos_inner_left_via_arr']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(**dict(_ViaMet12Met2NumberOfCOX=1, _ViaMet12Met2NumberOfCOY=nmos_coy))
		self._DesignParameter['nmos_inner_left_via_arr']['_XYCoordinates'] = None
		XYList = []
		xy_offset = (0, int(((drc._VIAxMinWidth + drc._VIAxMinSpace) / 4)))
		for element in self._DesignParameter['NMOS3InNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][(- 2)::(- 2)]:
		    element = (element[0] if (type(element[0]) == list) else element)
		    XYList.append([((x + y) + z) for (x, y, z) in zip([(0 + self._DesignParameter['NMOS3InNMOSSetofSlicer_0']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['NMOS3InNMOSSetofSlicer_0']['_XYCoordinates'][0][1])], element, xy_offset)])
		self._DesignParameter['nmos_inner_left_via_arr']['_XYCoordinates'] = XYList
		self._DesignParameter['nmos_inner_right_via_arr'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='nmos_inner_right_via_arrIn{}'.format(_Name)))[0]
		self._DesignParameter['nmos_inner_right_via_arr']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(**dict(_ViaMet12Met2NumberOfCOX=1, _ViaMet12Met2NumberOfCOY=nmos_coy))
		self._DesignParameter['nmos_inner_right_via_arr']['_XYCoordinates'] = None
		XYList = []
		xy_offset = (0, int(((drc._VIAxMinWidth + drc._VIAxMinSpace) / 4)))
		for i in range(len(self._DesignParameter['NMOS4InNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'])):
		    if ((i % 2) == 1):
		        xy = (self._DesignParameter['NMOS4InNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i][0] if (type(self._DesignParameter['NMOS4InNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i][0]) == list) else self._DesignParameter['NMOS4InNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i])
		        XYList.append([((x + y) + z) for (x, y, z) in zip([(0 + self._DesignParameter['NMOS4InNMOSSetofSlicer_0']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['NMOS4InNMOSSetofSlicer_0']['_XYCoordinates'][0][1])], xy, xy_offset)])
		self._DesignParameter['nmos_inner_right_via_arr']['_XYCoordinates'] = XYList
		self._DesignParameter['PCCAM1_CDNS_6375475055654_12'] = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_Name='PCCAM1_CDNS_6375475055654_12In{}'.format(_Name)))[0]
		self._DesignParameter['PCCAM1_CDNS_6375475055654_12']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(**dict(_ViaPoly2Met1NumberOfCOX=max(1, (1 + int(((((((self._DesignParameter['NMOS3InNMOSSetofSlicer_0']['_XYCoordinates'][0][0] + self._DesignParameter['NMOS3InNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]) + (self._DesignParameter['NMOS3InNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)) - ((self._DesignParameter['NMOS3InNMOSSetofSlicer_0']['_XYCoordinates'][0][0] + self._DesignParameter['NMOS3InNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['NMOS3InNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2))) - drc._CoMinSpace) - (2 * drc._CoMinEnclosureByPO)) / (drc._CoMinWidth + drc._CoMinSpace))))), _ViaPoly2Met1NumberOfCOY=1))
		self._DesignParameter['PCCAM1_CDNS_6375475055654_12']['_XYCoordinates'] = [[self._DesignParameter['NMOS3InNMOSSetofSlicer_0']['_XYCoordinates'][0][0], ((drc._Metal1MinSpace21 + (self._DesignParameter['PCCAM1_CDNS_6375475055654_12']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)) + ((self._DesignParameter['NMOS3InNMOSSetofSlicer_0']['_XYCoordinates'][0][1] + self._DesignParameter['NMOS3InNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) + (self._DesignParameter['NMOS3InNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)))]]
		self._DesignParameter['PCCAM1_CDNS_6375475055654_13'] = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_Name='PCCAM1_CDNS_6375475055654_13In{}'.format(_Name)))[0]
		self._DesignParameter['PCCAM1_CDNS_6375475055654_13']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(**dict(_ViaPoly2Met1NumberOfCOX=max(1, (1 + int(((((((self._DesignParameter['NMOS3InNMOSSetofSlicer_0']['_XYCoordinates'][0][0] + self._DesignParameter['NMOS3InNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]) + (self._DesignParameter['NMOS3InNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)) - ((self._DesignParameter['NMOS3InNMOSSetofSlicer_0']['_XYCoordinates'][0][0] + self._DesignParameter['NMOS3InNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['NMOS3InNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2))) - drc._CoMinSpace) - (2 * drc._CoMinEnclosureByPO)) / (drc._CoMinWidth + drc._CoMinSpace))))), _ViaPoly2Met1NumberOfCOY=1))
		self._DesignParameter['PCCAM1_CDNS_6375475055654_13']['_XYCoordinates'] = [[self._DesignParameter['NMOS4InNMOSSetofSlicer_0']['_XYCoordinates'][0][0], ((drc._Metal1MinSpace21 + (self._DesignParameter['PCCAM1_CDNS_6375475055654_12']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)) + ((self._DesignParameter['NMOS3InNMOSSetofSlicer_0']['_XYCoordinates'][0][1] + self._DesignParameter['NMOS3InNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) + (self._DesignParameter['NMOS3InNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)))]]
		path_list = []
		xy_offset = [0, 0]
		if (len(self._DesignParameter['NMOS3InNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates']) == 1):
		    mode = 'vertical'
		    _width = self._DesignParameter['NMOS3InNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
		elif (self._DesignParameter['NMOS3InNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0] == self._DesignParameter['NMOS3InNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]):
		    mode = 'horizontal'
		    _width = self._DesignParameter['NMOS3InNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
		elif (self._DesignParameter['NMOS3InNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1] == self._DesignParameter['NMOS3InNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][1]):
		    mode = 'vertical'
		    _width = self._DesignParameter['NMOS3InNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
		else:
		    print('Invalid Target Input')
		if (mode == 'vertical'):
		    xy_with_offset = []
		    target_y_value = [[(+ self._DesignParameter['PCCAM1_CDNS_6375475055654_12']['_XYCoordinates'][0][0]), (+ self._DesignParameter['PCCAM1_CDNS_6375475055654_12']['_XYCoordinates'][0][1])]][0][1]
		    for i in range(len(self._DesignParameter['NMOS3InNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
		        xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['NMOS3InNMOSSetofSlicer_0']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['NMOS3InNMOSSetofSlicer_0']['_XYCoordinates'][0][1])], self._DesignParameter['NMOS3InNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		elif (mode == 'horizontal'):
		    xy_with_offset = []
		    target_x_value = [[(+ self._DesignParameter['PCCAM1_CDNS_6375475055654_12']['_XYCoordinates'][0][0]), (+ self._DesignParameter['PCCAM1_CDNS_6375475055654_12']['_XYCoordinates'][0][1])]][0][0]
		    for i in range(len(self._DesignParameter['NMOS3InNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
		        xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['NMOS3InNMOSSetofSlicer_0']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['NMOS3InNMOSSetofSlicer_0']['_XYCoordinates'][0][1])], self._DesignParameter['NMOS3InNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		for i in range(len(path_list)):
		    path_list[i][0] = [(xy + offset) for (xy, offset) in zip(path_list[i][0], xy_offset)]
		self._DesignParameter['nmos_inner_left_gate'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _Width=_width)
		self._DesignParameter['nmos_inner_left_gate']['_XYCoordinates'] = path_list
		path_list = []
		xy_offset = [0, 0]
		if (len(self._DesignParameter['NMOS4InNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates']) == 1):
		    mode = 'vertical'
		    _width = self._DesignParameter['NMOS4InNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
		elif (self._DesignParameter['NMOS4InNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0] == self._DesignParameter['NMOS4InNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]):
		    mode = 'horizontal'
		    _width = self._DesignParameter['NMOS4InNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
		elif (self._DesignParameter['NMOS4InNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1] == self._DesignParameter['NMOS4InNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][1]):
		    mode = 'vertical'
		    _width = self._DesignParameter['NMOS4InNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
		else:
		    print('Invalid Target Input')
		if (mode == 'vertical'):
		    xy_with_offset = []
		    target_y_value = [[(+ self._DesignParameter['PCCAM1_CDNS_6375475055654_13']['_XYCoordinates'][0][0]), (+ self._DesignParameter['PCCAM1_CDNS_6375475055654_13']['_XYCoordinates'][0][1])]][0][1]
		    for i in range(len(self._DesignParameter['NMOS4InNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
		        xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['NMOS4InNMOSSetofSlicer_0']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['NMOS4InNMOSSetofSlicer_0']['_XYCoordinates'][0][1])], self._DesignParameter['NMOS4InNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		elif (mode == 'horizontal'):
		    xy_with_offset = []
		    target_x_value = [[(+ self._DesignParameter['PCCAM1_CDNS_6375475055654_13']['_XYCoordinates'][0][0]), (+ self._DesignParameter['PCCAM1_CDNS_6375475055654_13']['_XYCoordinates'][0][1])]][0][0]
		    for i in range(len(self._DesignParameter['NMOS4InNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
		        xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['NMOS4InNMOSSetofSlicer_0']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['NMOS4InNMOSSetofSlicer_0']['_XYCoordinates'][0][1])], self._DesignParameter['NMOS4InNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		for i in range(len(path_list)):
		    path_list[i][0] = [(xy + offset) for (xy, offset) in zip(path_list[i][0], xy_offset)]
		self._DesignParameter['nmos_inner_right_gate'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _Width=_width)
		self._DesignParameter['nmos_inner_right_gate']['_XYCoordinates'] = path_list
		self._DesignParameter['POLY_path_63'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _Width=self._DesignParameter['PCCAM1_CDNS_6375475055654_12']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'])
		self._DesignParameter['POLY_path_63']['_XYCoordinates'] = [[[(self._DesignParameter['nmos_inner_left_gate']['_XYCoordinates'][0][0][0] - (self._DesignParameter['nmos_inner_left_gate']['_Width'] / 2)), self._DesignParameter['PCCAM1_CDNS_6375475055654_12']['_XYCoordinates'][0][1]], [(self._DesignParameter['nmos_inner_left_gate']['_XYCoordinates'][(- 1)][0][0] + (self._DesignParameter['nmos_inner_left_gate']['_Width'] / 2)), self._DesignParameter['PCCAM1_CDNS_6375475055654_12']['_XYCoordinates'][0][1]]]]
		self._DesignParameter['POLY_path_66'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _Width=self._DesignParameter['PCCAM1_CDNS_6375475055654_12']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'])
		self._DesignParameter['POLY_path_66']['_XYCoordinates'] = [[[(self._DesignParameter['nmos_inner_right_gate']['_XYCoordinates'][0][0][0] - (self._DesignParameter['nmos_inner_right_gate']['_Width'] / 2)), self._DesignParameter['PCCAM1_CDNS_6375475055654_12']['_XYCoordinates'][0][1]], [(self._DesignParameter['nmos_inner_right_gate']['_XYCoordinates'][(- 1)][0][0] + (self._DesignParameter['nmos_inner_right_gate']['_Width'] / 2)), self._DesignParameter['PCCAM1_CDNS_6375475055654_12']['_XYCoordinates'][0][1]]]]
		self._DesignParameter['METAL1_path_43'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=self._DesignParameter['NMOS3InNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'])
		self._DesignParameter['METAL1_path_43']['_XYCoordinates'] = [[[((self._DesignParameter['NMOS3InNMOSSetofSlicer_0']['_XYCoordinates'][0][0] + self._DesignParameter['NMOS3InNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][(- 1)][0]) + (self._DesignParameter['NMOS3InNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] / 2)), ((((self._DesignParameter['NMOS3InNMOSSetofSlicer_0']['_XYCoordinates'][0][1] + self._DesignParameter['NMOS3InNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) - (self._DesignParameter['NMOS3InNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)) - drc._Metal1MinSpace21) - (self._DesignParameter['NMOS3InNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] / 2))], [((self._DesignParameter['NMOS3InNMOSSetofSlicer_0']['_XYCoordinates'][0][0] + self._DesignParameter['NMOS3InNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0]) - (self._DesignParameter['NMOS3InNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] / 2)), ((((self._DesignParameter['NMOS3InNMOSSetofSlicer_0']['_XYCoordinates'][0][1] + self._DesignParameter['NMOS3InNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) - (self._DesignParameter['NMOS3InNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)) - drc._Metal1MinSpace21) - (self._DesignParameter['NMOS3InNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] / 2))]]]
		self._DesignParameter['METAL1_path_42'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=self._DesignParameter['NMOS4InNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'])
		self._DesignParameter['METAL1_path_42']['_XYCoordinates'] = [[[((self._DesignParameter['NMOS4InNMOSSetofSlicer_0']['_XYCoordinates'][0][0] + self._DesignParameter['NMOS4InNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][(- 1)][0]) + (self._DesignParameter['NMOS4InNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] / 2)), ((((self._DesignParameter['NMOS4InNMOSSetofSlicer_0']['_XYCoordinates'][0][1] + self._DesignParameter['NMOS4InNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) - (self._DesignParameter['NMOS4InNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)) - (self._DesignParameter['NMOS4InNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] / 2)) - drc._Metal1MinSpace21)], [((self._DesignParameter['NMOS4InNMOSSetofSlicer_0']['_XYCoordinates'][0][0] + self._DesignParameter['NMOS4InNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0]) - (self._DesignParameter['NMOS4InNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] / 2)), ((((self._DesignParameter['NMOS4InNMOSSetofSlicer_0']['_XYCoordinates'][0][1] + self._DesignParameter['NMOS4InNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) - (self._DesignParameter['NMOS4InNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)) - (self._DesignParameter['NMOS4InNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] / 2)) - drc._Metal1MinSpace21)]]]
		path_list = []
		xy_offset = [0, 0]
		if (len(self._DesignParameter['NMOS3InNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates']) == 1):
		    mode = 'vertical'
		    _width = self._DesignParameter['NMOS3InNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth']
		elif (self._DesignParameter['NMOS3InNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][0] == self._DesignParameter['NMOS3InNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][0]):
		    mode = 'horizontal'
		    _width = self._DesignParameter['NMOS3InNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth']
		elif (self._DesignParameter['NMOS3InNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1] == self._DesignParameter['NMOS3InNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][1]):
		    mode = 'vertical'
		    _width = self._DesignParameter['NMOS3InNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth']
		else:
		    print('Invalid Target Input')
		if (mode == 'vertical'):
		    xy_with_offset = []
		    target_y_value = [[(+ self._DesignParameter['METAL1_path_43']['_XYCoordinates'][0][0][0]), (+ self._DesignParameter['METAL1_path_43']['_XYCoordinates'][0][0][1])]][0][1]
		    for i in range(len(self._DesignParameter['NMOS3InNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		        if ((i % 2) == 0):
		            xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['NMOS3InNMOSSetofSlicer_0']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['NMOS3InNMOSSetofSlicer_0']['_XYCoordinates'][0][1])], self._DesignParameter['NMOS3InNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		elif (mode == 'horizontal'):
		    xy_with_offset = []
		    target_x_value = [[(+ self._DesignParameter['METAL1_path_43']['_XYCoordinates'][0][0][0]), (+ self._DesignParameter['METAL1_path_43']['_XYCoordinates'][0][0][1])]][0][0]
		    for i in range(len(self._DesignParameter['NMOS3InNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		        if ((i % 2) == 0):
		            xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['NMOS3InNMOSSetofSlicer_0']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['NMOS3InNMOSSetofSlicer_0']['_XYCoordinates'][0][1])], self._DesignParameter['NMOS3InNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		for i in range(len(path_list)):
		    path_list[i][0] = [(xy + offset) for (xy, offset) in zip(path_list[i][0], xy_offset)]
		self._DesignParameter['nmos_inner_left_met1'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=_width)
		self._DesignParameter['nmos_inner_left_met1']['_XYCoordinates'] = path_list
		path_list = []
		xy_offset = [0, 0]
		if (len(self._DesignParameter['NMOS4InNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates']) == 1):
		    mode = 'vertical'
		    _width = self._DesignParameter['NMOS4InNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth']
		elif (self._DesignParameter['NMOS4InNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][0] == self._DesignParameter['NMOS4InNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][0]):
		    mode = 'horizontal'
		    _width = self._DesignParameter['NMOS4InNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth']
		elif (self._DesignParameter['NMOS4InNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1] == self._DesignParameter['NMOS4InNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][1]):
		    mode = 'vertical'
		    _width = self._DesignParameter['NMOS4InNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth']
		else:
		    print('Invalid Target Input')
		if (mode == 'vertical'):
		    xy_with_offset = []
		    target_y_value = [[(+ self._DesignParameter['METAL1_path_42']['_XYCoordinates'][0][0][0]), (+ self._DesignParameter['METAL1_path_42']['_XYCoordinates'][0][0][1])]][0][1]
		    for i in range(len(self._DesignParameter['NMOS4InNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		        if ((i % 2) == 0):
		            xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['NMOS4InNMOSSetofSlicer_0']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['NMOS4InNMOSSetofSlicer_0']['_XYCoordinates'][0][1])], self._DesignParameter['NMOS4InNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		elif (mode == 'horizontal'):
		    xy_with_offset = []
		    target_x_value = [[(+ self._DesignParameter['METAL1_path_42']['_XYCoordinates'][0][0][0]), (+ self._DesignParameter['METAL1_path_42']['_XYCoordinates'][0][0][1])]][0][0]
		    for i in range(len(self._DesignParameter['NMOS4InNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		        if ((i % 2) == 0):
		            xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['NMOS4InNMOSSetofSlicer_0']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['NMOS4InNMOSSetofSlicer_0']['_XYCoordinates'][0][1])], self._DesignParameter['NMOS4InNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		for i in range(len(path_list)):
		    path_list[i][0] = [(xy + offset) for (xy, offset) in zip(path_list[i][0], xy_offset)]
		self._DesignParameter['nmos_inner_right_met1'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=_width)
		self._DesignParameter['nmos_inner_right_met1']['_XYCoordinates'] = path_list
		self._DesignParameter['GuardringInNMOSSetofSlicer_0'] = self._SrefElementDeclaration(_DesignObj=PSubRing.PSubRing(_Name='GuardringInNMOSSetofSlicer_0In{}'.format(_Name)))[0]
		self._DesignParameter['GuardringInNMOSSetofSlicer_0']['_DesignObj']._CalculateDesignParameter(**dict(height=((((self._DesignParameter['PCCAM1_CDNS_6375475055654_12']['_XYCoordinates'][0][1] + self._DesignParameter['PCCAM1_CDNS_6375475055654_12']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) + (self._DesignParameter['PCCAM1_CDNS_6375475055654_12']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)) + drc._Metal1MinSpace22) + (- (((self._DesignParameter['nmos_bot']['_XYCoordinates'][0][1] + self._DesignParameter['nmos_bot']['_DesignObj']._DesignParameter['_ODLayer']['_XYCoordinates'][0][1]) - (self._DesignParameter['nmos_bot']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth'] / 2)) - drc._OdMinSpace))), width=((((self._DesignParameter['NMOS2InNMOSSetofSlicer_0']['_XYCoordinates'][0][0] + self._DesignParameter['NMOS2InNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_ODLayer']['_XYCoordinates'][0][0]) + (self._DesignParameter['NMOS2InNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth'] / 2)) + drc._OdMinSpace) + (- (((self._DesignParameter['NMOS1InNMOSSetofSlicer_0']['_XYCoordinates'][0][0] + self._DesignParameter['NMOS1InNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_ODLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['NMOS1InNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth'] / 2)) - drc._OdMinSpace))), contact=subring_option['via_num']))
		self._DesignParameter['GuardringInNMOSSetofSlicer_0']['_XYCoordinates'] = [[(((((self._DesignParameter['NMOS2InNMOSSetofSlicer_0']['_XYCoordinates'][0][0] + self._DesignParameter['NMOS2InNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_ODLayer']['_XYCoordinates'][0][0]) + (self._DesignParameter['NMOS2InNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth'] / 2)) + drc._OdMinSpace) + (((self._DesignParameter['NMOS1InNMOSSetofSlicer_0']['_XYCoordinates'][0][0] + self._DesignParameter['NMOS1InNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_ODLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['NMOS1InNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth'] / 2)) - drc._OdMinSpace)) / 2), (((((self._DesignParameter['PCCAM1_CDNS_6375475055654_12']['_XYCoordinates'][0][1] + self._DesignParameter['PCCAM1_CDNS_6375475055654_12']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) + (self._DesignParameter['PCCAM1_CDNS_6375475055654_12']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)) + drc._Metal1MinSpace22) + (((self._DesignParameter['nmos_bot']['_XYCoordinates'][0][1] + self._DesignParameter['nmos_bot']['_DesignObj']._DesignParameter['_ODLayer']['_XYCoordinates'][0][1]) - (self._DesignParameter['nmos_bot']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth'] / 2)) - drc._OdMinSpace)) / 2)]]
		self._DesignParameter['GuardringInNMOSSetofSlicer_0']['_DesignObj']._CalculateDesignParameter(**dict(height=((((- (((self._DesignParameter['nmos_bot']['_XYCoordinates'][0][1] + self._DesignParameter['nmos_bot']['_DesignObj']._DesignParameter['_ODLayer']['_XYCoordinates'][0][1]) - (self._DesignParameter['nmos_bot']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth'] / 2)) - drc._OdMinSpace)) + ((self._DesignParameter['GuardringInNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['top']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2) + (self._DesignParameter['GuardringInNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['top']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth'] / 2))) + drc._PpMinSpace) + (max(((self._DesignParameter['NMOS1InNMOSSetofSlicer_0']['_XYCoordinates'][0][1] + self._DesignParameter['NMOS1InNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) + (self._DesignParameter['NMOS1InNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)), ((self._DesignParameter['PCCAM1_CDNS_6375475055654_12']['_XYCoordinates'][0][1] + self._DesignParameter['PCCAM1_CDNS_6375475055654_12']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) + (self._DesignParameter['PCCAM1_CDNS_6375475055654_12']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2))) + drc._Metal1MinSpace22)), width=((((((self._DesignParameter['NMOS2InNMOSSetofSlicer_0']['_XYCoordinates'][0][0] + self._DesignParameter['NMOS2InNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_ODLayer']['_XYCoordinates'][0][0]) + (self._DesignParameter['NMOS2InNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth'] / 2)) + drc._OdMinSpace) + (- (((self._DesignParameter['NMOS1InNMOSSetofSlicer_0']['_XYCoordinates'][0][0] + self._DesignParameter['NMOS1InNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_ODLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['NMOS1InNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth'] / 2)) - drc._OdMinSpace))) + self._DesignParameter['GuardringInNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['right']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth']) + subring_option['nmos_subring_addi_width']), contact=subring_option['via_num']))
		self._DesignParameter['GuardringInPMOSSetofSlicer_0'] = self._SrefElementDeclaration(_DesignObj=NSubRing.NSubRing(_Name='GuardringInPMOSSetofSlicer_0In{}'.format(_Name)))[0]
		self._DesignParameter['GuardringInPMOSSetofSlicer_0']['_DesignObj']._CalculateDesignParameter(**dict(height=2600, width=5000, contact=subring_option['via_num']))
		self._DesignParameter['GuardringInPMOSSetofSlicer_0']['_XYCoordinates'] = [[0.0, 1084.0]]
		pmos_inner_parm = dict(_PMOSNumberofGate=pmos_parms['inner_gate'], _PMOSChannelWidth=pmos_parms['common_width'], _PMOSChannellength=30, _PMOSDummy=True, _GateSpacing=None, _SDWidth=None, _XVT='SLVT', _PCCrit=None)
		self._DesignParameter['PMOS3InPMOSSetofSlicer_0'] = self._SrefElementDeclaration(_DesignObj=PMOSWithDummy._PMOS(_Name='PMOS3InPMOSSetofSlicer_0In{}'.format(_Name)))[0]
		self._DesignParameter['PMOS3InPMOSSetofSlicer_0']['_DesignObj']._CalculatePMOSDesignParameter(**dict(**pmos_inner_parm))
		self._DesignParameter['PMOS3InPMOSSetofSlicer_0']['_XYCoordinates'] = [[((self._DesignParameter['nmos_bot']['_XYCoordinates'][0][0] - (drc._PolygateMinSpace / 2)) - (self._DesignParameter['PMOS3InPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][(- 1)][0] + (self._DesignParameter['PMOS3InPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_PODummyLayer']['_XWidth'] / 2))), ((((((((self._DesignParameter['GuardringInPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['bot']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2) + drc._Metal1MinSpace22) + self._DesignParameter['PCCAM1_CDNS_6375475055654_12']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']) + (drc._Metal1MinSpace21 + (self._DesignParameter['PMOS3InPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2))) + 124) + (- 124)) + (((((self._DesignParameter['GuardringInNMOSSetofSlicer_0']['_XYCoordinates'][0][1] + self._DesignParameter['GuardringInNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['top']['_XYCoordinates'][0][1]) + self._DesignParameter['GuardringInNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['top']['_DesignObj']._DesignParameter['_PPLayer']['_XYCoordinates'][0][1]) + (self._DesignParameter['GuardringInNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['top']['_DesignObj']._DesignParameter['_PPLayer']['_YWidth'] / 2)) + drc._NwMinSpacetoNactive) + (self._DesignParameter['GuardringInPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['nw_bot']['_YWidth'] / 2))) + subring_option['additional_np_distance'])]]
		self._DesignParameter['PMOS4InPMOSSetofSlicer_0'] = self._SrefElementDeclaration(_DesignObj=PMOSWithDummy._PMOS(_Name='PMOS4InPMOSSetofSlicer_0In{}'.format(_Name)))[0]
		self._DesignParameter['PMOS4InPMOSSetofSlicer_0']['_DesignObj']._CalculatePMOSDesignParameter(**dict(**pmos_inner_parm))
		self._DesignParameter['PMOS4InPMOSSetofSlicer_0']['_XYCoordinates'] = [[((self._DesignParameter['nmos_bot']['_XYCoordinates'][0][0] - (self._DesignParameter['PMOS4InPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][0] - (self._DesignParameter['PMOS4InPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_PODummyLayer']['_XWidth'] / 2))) + (drc._PolygateMinSpace / 2)), self._DesignParameter['PMOS3InPMOSSetofSlicer_0']['_XYCoordinates'][0][1]]]
		pmos_outside_parm = dict(_PMOSNumberofGate=(pmos_outer_gate + pmos_inner_gate), _PMOSChannelWidth=pmos_parms['common_width'], _PMOSChannellength=30, _PMOSDummy=True, _GateSpacing=None, _SDWidth=None, _XVT='SLVT', _PCCrit=None)
		self._DesignParameter['PMOS1InPMOSSetofSlicer_0'] = self._SrefElementDeclaration(_DesignObj=PMOSWithDummy._PMOS(_Name='PMOS1InPMOSSetofSlicer_0In{}'.format(_Name)))[0]
		self._DesignParameter['PMOS1InPMOSSetofSlicer_0']['_DesignObj']._CalculatePMOSDesignParameter(**dict(**pmos_outside_parm))
		self._DesignParameter['PMOS1InPMOSSetofSlicer_0']['_XYCoordinates'] = [[((((self._DesignParameter['PMOS3InPMOSSetofSlicer_0']['_XYCoordinates'][0][0] + self._DesignParameter['PMOS3InPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['PMOS3InPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_PODummyLayer']['_XWidth'] / 2)) - drc._PolygateMinSpace) - (self._DesignParameter['PMOS1InPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][(- 1)][0] + (self._DesignParameter['PMOS1InPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_PODummyLayer']['_XWidth'] / 2))), self._DesignParameter['PMOS3InPMOSSetofSlicer_0']['_XYCoordinates'][0][1]]]
		self._DesignParameter['PMOS2InPMOSSetofSlicer_0'] = self._SrefElementDeclaration(_DesignObj=PMOSWithDummy._PMOS(_Name='PMOS2InPMOSSetofSlicer_0In{}'.format(_Name)))[0]
		self._DesignParameter['PMOS2InPMOSSetofSlicer_0']['_DesignObj']._CalculatePMOSDesignParameter(**dict(**pmos_outside_parm))
		self._DesignParameter['PMOS2InPMOSSetofSlicer_0']['_XYCoordinates'] = [[((((self._DesignParameter['PMOS4InPMOSSetofSlicer_0']['_XYCoordinates'][0][0] + self._DesignParameter['PMOS4InPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][(- 1)][0]) + (self._DesignParameter['PMOS4InPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_PODummyLayer']['_XWidth'] / 2)) + drc._PolygateMinSpace) - (self._DesignParameter['PMOS2InPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][0] - (self._DesignParameter['PMOS2InPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_PODummyLayer']['_XWidth'] / 2))), self._DesignParameter['PMOS3InPMOSSetofSlicer_0']['_XYCoordinates'][0][1]]]
		pmos_coy = max(1, (1 + int((((self._DesignParameter['PMOS3InPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] - drc._VIAxMinSpace) - (2 * drc._VIAxMinEnclosureByMetx)) / (drc._VIAxMinWidth + drc._VIAxMinSpace)))))
		self._DesignParameter['pmos_inner_left'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='pmos_inner_leftIn{}'.format(_Name)))[0]
		self._DesignParameter['pmos_inner_left']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(**dict(_ViaMet12Met2NumberOfCOX=1, _ViaMet12Met2NumberOfCOY=pmos_coy))
		self._DesignParameter['pmos_inner_left']['_XYCoordinates'] = None
		XYList = []
		xy_offset = [0, 0]
		for element in self._DesignParameter['PMOS3InPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][(- 1)::(- 2)]:
		    element = (element[0] if (type(element[0]) == list) else element)
		    XYList.append([((x + y) + z) for (x, y, z) in zip([(0 + self._DesignParameter['PMOS3InPMOSSetofSlicer_0']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['PMOS3InPMOSSetofSlicer_0']['_XYCoordinates'][0][1])], element, xy_offset)])
		self._DesignParameter['pmos_inner_left']['_XYCoordinates'] = XYList
		self._DesignParameter['pmos_inside_right_via'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='pmos_inside_right_viaIn{}'.format(_Name)))[0]
		self._DesignParameter['pmos_inside_right_via']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(**dict(_ViaMet12Met2NumberOfCOX=1, _ViaMet12Met2NumberOfCOY=pmos_coy))
		self._DesignParameter['pmos_inside_right_via']['_XYCoordinates'] = None
		XYList = []
		xy_offset = [0, 0]
		for i in range(len(self._DesignParameter['PMOS4InPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'])):
		    if ((i % 2) == 0):
		        xy = (self._DesignParameter['PMOS4InPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i][0] if (type(self._DesignParameter['PMOS4InPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i][0]) == list) else self._DesignParameter['PMOS4InPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i])
		        XYList.append([((x + y) + z) for (x, y, z) in zip([(0 + self._DesignParameter['PMOS4InPMOSSetofSlicer_0']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['PMOS4InPMOSSetofSlicer_0']['_XYCoordinates'][0][1])], xy, xy_offset)])
		self._DesignParameter['pmos_inside_right_via']['_XYCoordinates'] = XYList
		if ((pmos_outer_gate % 2) == 0):
		    self._DesignParameter['left_pmos_outside_via'] = self._SrefElementDeclaration(_DesignObj=ViaStack._ViaStack(_Name='left_pmos_outside_viaIn{}'.format(_Name)))[0]
		    self._DesignParameter['left_pmos_outside_via']['_DesignObj']._CalculateStackMinimumEnclosureX(**dict(COX=1, COY=pmos_coy, start_layer=1, end_layer=4))
		    self._DesignParameter['left_pmos_outside_via']['_XYCoordinates'] = None
		    XYList = []
		    xy_offset = [0, 0]
		    for element in self._DesignParameter['PMOS1InPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][1:pmos_outer_gate:2]:
		        element = (element[0] if (type(element[0]) == list) else element)
		        XYList.append([((x + y) + z) for (x, y, z) in zip([(0 + self._DesignParameter['PMOS1InPMOSSetofSlicer_0']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['PMOS1InPMOSSetofSlicer_0']['_XYCoordinates'][0][1])], element, xy_offset)])
		    self._DesignParameter['left_pmos_outside_via']['_XYCoordinates'] = XYList
		    self._DesignParameter['right_pmos_outside_via'] = self._SrefElementDeclaration(_DesignObj=ViaStack._ViaStack(_Name='right_pmos_outside_viaIn{}'.format(_Name)))[0]
		    self._DesignParameter['right_pmos_outside_via']['_DesignObj']._CalculateStackMinimumEnclosureX(**dict(COX=1, COY=pmos_coy, start_layer=1, end_layer=4))
		    self._DesignParameter['right_pmos_outside_via']['_XYCoordinates'] = None
		    XYList = []
		    xy_offset = [0, 0]
		    for element in self._DesignParameter['PMOS2InPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 2):((- pmos_outer_gate) - 1):(- 2)]:
		        element = (element[0] if (type(element[0]) == list) else element)
		        XYList.append([((x + y) + z) for (x, y, z) in zip([(0 + self._DesignParameter['PMOS2InPMOSSetofSlicer_0']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['PMOS2InPMOSSetofSlicer_0']['_XYCoordinates'][0][1])], element, xy_offset)])
		    self._DesignParameter['right_pmos_outside_via']['_XYCoordinates'] = XYList
		else:
		    self._DesignParameter['left_pmos_outside_via'] = self._SrefElementDeclaration(_DesignObj=ViaStack._ViaStack(_Name='left_pmos_outside_viaIn{}'.format(_Name)))[0]
		    self._DesignParameter['left_pmos_outside_via']['_DesignObj']._CalculateStackMinimumEnclosureX(**dict(COX=1, COY=pmos_coy, start_layer=1, end_layer=4))
		    self._DesignParameter['left_pmos_outside_via']['_XYCoordinates'] = None
		    XYList = []
		    xy_offset = [0, 0]
		    for element in self._DesignParameter['PMOS1InPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0:pmos_outer_gate:2]:
		        element = (element[0] if (type(element[0]) == list) else element)
		        XYList.append([((x + y) + z) for (x, y, z) in zip([(0 + self._DesignParameter['PMOS1InPMOSSetofSlicer_0']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['PMOS1InPMOSSetofSlicer_0']['_XYCoordinates'][0][1])], element, xy_offset)])
		    self._DesignParameter['left_pmos_outside_via']['_XYCoordinates'] = XYList
		    self._DesignParameter['right_pmos_outside_via'] = self._SrefElementDeclaration(_DesignObj=ViaStack._ViaStack(_Name='right_pmos_outside_viaIn{}'.format(_Name)))[0]
		    self._DesignParameter['right_pmos_outside_via']['_DesignObj']._CalculateStackMinimumEnclosureX(**dict(COX=1, COY=pmos_coy, start_layer=1, end_layer=4))
		    self._DesignParameter['right_pmos_outside_via']['_XYCoordinates'] = None
		    XYList = []
		    xy_offset = [0, 0]
		    for element in self._DesignParameter['PMOS2InPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1):((- pmos_outer_gate) - 1):(- 2)]:
		        element = (element[0] if (type(element[0]) == list) else element)
		        XYList.append([((x + y) + z) for (x, y, z) in zip([(0 + self._DesignParameter['PMOS2InPMOSSetofSlicer_0']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['PMOS2InPMOSSetofSlicer_0']['_XYCoordinates'][0][1])], element, xy_offset)])
		    self._DesignParameter['right_pmos_outside_via']['_XYCoordinates'] = XYList
		self._DesignParameter['left_pmos_inside_via'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='left_pmos_inside_viaIn{}'.format(_Name)))[0]
		self._DesignParameter['left_pmos_inside_via']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(**dict(_ViaMet12Met2NumberOfCOX=1, _ViaMet12Met2NumberOfCOY=pmos_coy))
		self._DesignParameter['left_pmos_inside_via']['_XYCoordinates'] = None
		XYList = []
		xy_offset = [0, 0]
		for element in self._DesignParameter['PMOS1InPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(pmos_outer_gate + 1)::2]:
		    element = (element[0] if (type(element[0]) == list) else element)
		    XYList.append([((x + y) + z) for (x, y, z) in zip([(0 + self._DesignParameter['PMOS1InPMOSSetofSlicer_0']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['PMOS1InPMOSSetofSlicer_0']['_XYCoordinates'][0][1])], element, xy_offset)])
		self._DesignParameter['left_pmos_inside_via']['_XYCoordinates'] = XYList
		self._DesignParameter['right_pmos_inside_via'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='right_pmos_inside_viaIn{}'.format(_Name)))[0]
		self._DesignParameter['right_pmos_inside_via']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(**dict(_ViaMet12Met2NumberOfCOX=1, _ViaMet12Met2NumberOfCOY=pmos_coy))
		self._DesignParameter['right_pmos_inside_via']['_XYCoordinates'] = None
		XYList = []
		xy_offset = [0, 0]
		for element in self._DesignParameter['PMOS2InPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][((- pmos_outer_gate) - 2)::(- 2)]:
		    element = (element[0] if (type(element[0]) == list) else element)
		    XYList.append([((x + y) + z) for (x, y, z) in zip([(0 + self._DesignParameter['PMOS2InPMOSSetofSlicer_0']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['PMOS2InPMOSSetofSlicer_0']['_XYCoordinates'][0][1])], element, xy_offset)])
		self._DesignParameter['right_pmos_inside_via']['_XYCoordinates'] = XYList
		self._DesignParameter['PCCAM1_CDNS_6375475055654_15'] = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_Name='PCCAM1_CDNS_6375475055654_15In{}'.format(_Name)))[0]
		self._DesignParameter['PCCAM1_CDNS_6375475055654_15']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(**dict(_ViaPoly2Met1NumberOfCOX=max(1, (1 + int(((((((self._DesignParameter['PMOS3InPMOSSetofSlicer_0']['_XYCoordinates'][0][0] + self._DesignParameter['PMOS3InPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]) + (self._DesignParameter['PMOS3InPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)) - ((self._DesignParameter['PMOS3InPMOSSetofSlicer_0']['_XYCoordinates'][0][0] + self._DesignParameter['PMOS3InPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['PMOS3InPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2))) - drc._CoMinSpace) - (2 * drc._CoMinEnclosureByPO)) / (drc._CoMinWidth + drc._CoMinSpace))))), _ViaPoly2Met1NumberOfCOY=1))
		self._DesignParameter['PCCAM1_CDNS_6375475055654_15']['_XYCoordinates'] = [[self._DesignParameter['PMOS3InPMOSSetofSlicer_0']['_XYCoordinates'][0][0], ((((self._DesignParameter['PMOS3InPMOSSetofSlicer_0']['_XYCoordinates'][0][1] + self._DesignParameter['PMOS3InPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) - (self._DesignParameter['PMOS3InPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)) - drc._Metal1MinSpace21) - (self._DesignParameter['PCCAM1_CDNS_6375475055654_15']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2))]]
		self._DesignParameter['PCCAM1_CDNS_6375475055654_14'] = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_Name='PCCAM1_CDNS_6375475055654_14In{}'.format(_Name)))[0]
		self._DesignParameter['PCCAM1_CDNS_6375475055654_14']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(**dict(_ViaPoly2Met1NumberOfCOX=max(1, (1 + int(((((((self._DesignParameter['PMOS3InPMOSSetofSlicer_0']['_XYCoordinates'][0][0] + self._DesignParameter['PMOS3InPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]) + (self._DesignParameter['PMOS3InPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)) - ((self._DesignParameter['PMOS3InPMOSSetofSlicer_0']['_XYCoordinates'][0][0] + self._DesignParameter['PMOS3InPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['PMOS3InPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2))) - drc._CoMinSpace) - (2 * drc._CoMinEnclosureByPO)) / (drc._CoMinWidth + drc._CoMinSpace))))), _ViaPoly2Met1NumberOfCOY=1))
		self._DesignParameter['PCCAM1_CDNS_6375475055654_14']['_XYCoordinates'] = [[self._DesignParameter['PMOS4InPMOSSetofSlicer_0']['_XYCoordinates'][0][0], ((((self._DesignParameter['PMOS3InPMOSSetofSlicer_0']['_XYCoordinates'][0][1] + self._DesignParameter['PMOS3InPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) - (self._DesignParameter['PMOS3InPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)) - drc._Metal1MinSpace21) - (self._DesignParameter['PCCAM1_CDNS_6375475055654_15']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2))]]
		path_list = []
		xy_offset = [0, 0]
		if (len(self._DesignParameter['PMOS3InPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_POLayerPINDrawing']['_XYCoordinates']) == 1):
		    mode = 'vertical'
		    _width = self._DesignParameter['PMOS3InPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_POLayerPINDrawing']['_XWidth']
		elif (self._DesignParameter['PMOS3InPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_POLayerPINDrawing']['_XYCoordinates'][0][0] == self._DesignParameter['PMOS3InPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_POLayerPINDrawing']['_XYCoordinates'][(- 1)][0]):
		    mode = 'horizontal'
		    _width = self._DesignParameter['PMOS3InPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_POLayerPINDrawing']['_XWidth']
		elif (self._DesignParameter['PMOS3InPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_POLayerPINDrawing']['_XYCoordinates'][0][1] == self._DesignParameter['PMOS3InPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_POLayerPINDrawing']['_XYCoordinates'][(- 1)][1]):
		    mode = 'vertical'
		    _width = self._DesignParameter['PMOS3InPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_POLayerPINDrawing']['_XWidth']
		else:
		    print('Invalid Target Input')
		if (mode == 'vertical'):
		    xy_with_offset = []
		    target_y_value = [[(+ self._DesignParameter['PCCAM1_CDNS_6375475055654_15']['_XYCoordinates'][0][0]), (+ self._DesignParameter['PCCAM1_CDNS_6375475055654_15']['_XYCoordinates'][0][1])]][0][1]
		    for i in range(len(self._DesignParameter['PMOS3InPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_POLayerPINDrawing']['_XYCoordinates'])):
		        xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['PMOS3InPMOSSetofSlicer_0']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['PMOS3InPMOSSetofSlicer_0']['_XYCoordinates'][0][1])], self._DesignParameter['PMOS3InPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_POLayerPINDrawing']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		elif (mode == 'horizontal'):
		    xy_with_offset = []
		    target_x_value = [[(+ self._DesignParameter['PCCAM1_CDNS_6375475055654_15']['_XYCoordinates'][0][0]), (+ self._DesignParameter['PCCAM1_CDNS_6375475055654_15']['_XYCoordinates'][0][1])]][0][0]
		    for i in range(len(self._DesignParameter['PMOS3InPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_POLayerPINDrawing']['_XYCoordinates'])):
		        xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['PMOS3InPMOSSetofSlicer_0']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['PMOS3InPMOSSetofSlicer_0']['_XYCoordinates'][0][1])], self._DesignParameter['PMOS3InPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_POLayerPINDrawing']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		for i in range(len(path_list)):
		    path_list[i][0] = [(xy + offset) for (xy, offset) in zip(path_list[i][0], xy_offset)]
		self._DesignParameter['left_pmos_gate'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _Width=_width)
		self._DesignParameter['left_pmos_gate']['_XYCoordinates'] = path_list
		path_list = []
		xy_offset = [0, 0]
		if (len(self._DesignParameter['PMOS4InPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_POLayerPINDrawing']['_XYCoordinates']) == 1):
		    mode = 'vertical'
		    _width = self._DesignParameter['PMOS4InPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_POLayerPINDrawing']['_XWidth']
		elif (self._DesignParameter['PMOS4InPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_POLayerPINDrawing']['_XYCoordinates'][0][0] == self._DesignParameter['PMOS4InPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_POLayerPINDrawing']['_XYCoordinates'][(- 1)][0]):
		    mode = 'horizontal'
		    _width = self._DesignParameter['PMOS4InPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_POLayerPINDrawing']['_XWidth']
		elif (self._DesignParameter['PMOS4InPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_POLayerPINDrawing']['_XYCoordinates'][0][1] == self._DesignParameter['PMOS4InPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_POLayerPINDrawing']['_XYCoordinates'][(- 1)][1]):
		    mode = 'vertical'
		    _width = self._DesignParameter['PMOS4InPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_POLayerPINDrawing']['_XWidth']
		else:
		    print('Invalid Target Input')
		if (mode == 'vertical'):
		    xy_with_offset = []
		    target_y_value = [[(+ self._DesignParameter['PCCAM1_CDNS_6375475055654_14']['_XYCoordinates'][0][0]), (+ self._DesignParameter['PCCAM1_CDNS_6375475055654_14']['_XYCoordinates'][0][1])]][0][1]
		    for i in range(len(self._DesignParameter['PMOS4InPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_POLayerPINDrawing']['_XYCoordinates'])):
		        xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['PMOS4InPMOSSetofSlicer_0']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['PMOS4InPMOSSetofSlicer_0']['_XYCoordinates'][0][1])], self._DesignParameter['PMOS4InPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_POLayerPINDrawing']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		elif (mode == 'horizontal'):
		    xy_with_offset = []
		    target_x_value = [[(+ self._DesignParameter['PCCAM1_CDNS_6375475055654_14']['_XYCoordinates'][0][0]), (+ self._DesignParameter['PCCAM1_CDNS_6375475055654_14']['_XYCoordinates'][0][1])]][0][0]
		    for i in range(len(self._DesignParameter['PMOS4InPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_POLayerPINDrawing']['_XYCoordinates'])):
		        xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['PMOS4InPMOSSetofSlicer_0']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['PMOS4InPMOSSetofSlicer_0']['_XYCoordinates'][0][1])], self._DesignParameter['PMOS4InPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_POLayerPINDrawing']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		for i in range(len(path_list)):
		    path_list[i][0] = [(xy + offset) for (xy, offset) in zip(path_list[i][0], xy_offset)]
		self._DesignParameter['right_pmos_gate'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _Width=_width)
		self._DesignParameter['right_pmos_gate']['_XYCoordinates'] = path_list
		self._DesignParameter['POLY_path_126'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _Width=self._DesignParameter['PCCAM1_CDNS_6375475055654_15']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'])
		self._DesignParameter['POLY_path_126']['_XYCoordinates'] = [[[((self._DesignParameter['PMOS3InPMOSSetofSlicer_0']['_XYCoordinates'][0][0] + self._DesignParameter['PMOS3InPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['PMOS3InPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)), self._DesignParameter['PCCAM1_CDNS_6375475055654_15']['_XYCoordinates'][0][1]], [((self._DesignParameter['PMOS3InPMOSSetofSlicer_0']['_XYCoordinates'][0][0] + self._DesignParameter['PMOS3InPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]) + (self._DesignParameter['PMOS3InPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)), self._DesignParameter['PCCAM1_CDNS_6375475055654_15']['_XYCoordinates'][0][1]]]]
		self._DesignParameter['POLY_path_125'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _Width=self._DesignParameter['PCCAM1_CDNS_6375475055654_14']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'])
		self._DesignParameter['POLY_path_125']['_XYCoordinates'] = [[[((self._DesignParameter['PMOS4InPMOSSetofSlicer_0']['_XYCoordinates'][0][0] + self._DesignParameter['PMOS4InPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['PMOS4InPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)), self._DesignParameter['PCCAM1_CDNS_6375475055654_14']['_XYCoordinates'][0][1]], [((self._DesignParameter['PMOS4InPMOSSetofSlicer_0']['_XYCoordinates'][0][0] + self._DesignParameter['PMOS4InPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]) + (self._DesignParameter['PMOS4InPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)), self._DesignParameter['PCCAM1_CDNS_6375475055654_14']['_XYCoordinates'][0][1]]]]
		self._DesignParameter['PCCAM1_CDNS_6375475055680_1'] = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_Name='PCCAM1_CDNS_6375475055680_1In{}'.format(_Name)))[0]
		self._DesignParameter['PCCAM1_CDNS_6375475055680_1']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(**dict(_ViaPoly2Met1NumberOfCOX=max(1, (1 + int(((((((self._DesignParameter['PMOS1InPMOSSetofSlicer_0']['_XYCoordinates'][0][0] + self._DesignParameter['PMOS1InPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]) + (self._DesignParameter['PMOS1InPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)) - ((self._DesignParameter['PMOS1InPMOSSetofSlicer_0']['_XYCoordinates'][0][0] + self._DesignParameter['PMOS1InPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['PMOS1InPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2))) - drc._CoMinSpace) - (2 * drc._CoMinEnclosureByPO)) / (drc._CoMinWidth + drc._CoMinSpace))))), _ViaPoly2Met1NumberOfCOY=1))
		self._DesignParameter['PCCAM1_CDNS_6375475055680_1']['_XYCoordinates'] = [[self._DesignParameter['PMOS1InPMOSSetofSlicer_0']['_XYCoordinates'][0][0], ((((self._DesignParameter['PMOS1InPMOSSetofSlicer_0']['_XYCoordinates'][0][1] + self._DesignParameter['PMOS1InPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) - (self._DesignParameter['PMOS1InPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)) - drc._Metal1MinSpace21) - (self._DesignParameter['PCCAM1_CDNS_6375475055680_1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2))]]
		path_list = []
		if (len(self._DesignParameter['PMOS1InPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_POLayerPINDrawing']['_XYCoordinates']) == 1):
		    mode = 'vertical'
		    _width = self._DesignParameter['PMOS1InPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_POLayerPINDrawing']['_XWidth']
		elif (self._DesignParameter['PMOS1InPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_POLayerPINDrawing']['_XYCoordinates'][0][0] == self._DesignParameter['PMOS1InPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_POLayerPINDrawing']['_XYCoordinates'][(- 1)][0]):
		    mode = 'horizontal'
		    _width = self._DesignParameter['PMOS1InPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_POLayerPINDrawing']['_XWidth']
		elif (self._DesignParameter['PMOS1InPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_POLayerPINDrawing']['_XYCoordinates'][0][1] == self._DesignParameter['PMOS1InPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_POLayerPINDrawing']['_XYCoordinates'][(- 1)][1]):
		    mode = 'vertical'
		    _width = self._DesignParameter['PMOS1InPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_POLayerPINDrawing']['_XWidth']
		else:
		    print('Invalid Target Input')
		if (mode == 'vertical'):
		    xy_with_offset = []
		    target_y_value = [[(+ self._DesignParameter['PCCAM1_CDNS_6375475055680_1']['_XYCoordinates'][0][0]), (+ self._DesignParameter['PCCAM1_CDNS_6375475055680_1']['_XYCoordinates'][0][1])]][0][1]
		    for element in self._DesignParameter['PMOS1InPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_POLayerPINDrawing']['_XYCoordinates']:
		        xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['PMOS1InPMOSSetofSlicer_0']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['PMOS1InPMOSSetofSlicer_0']['_XYCoordinates'][0][1])], element)])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		elif (mode == 'horizontal'):
		    xy_with_offset = []
		    target_x_value = [[(+ self._DesignParameter['PCCAM1_CDNS_6375475055680_1']['_XYCoordinates'][0][0]), (+ self._DesignParameter['PCCAM1_CDNS_6375475055680_1']['_XYCoordinates'][0][1])]][0][0]
		    for element in self._DesignParameter['PMOS1InPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_POLayerPINDrawing']['_XYCoordinates']:
		        xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['PMOS1InPMOSSetofSlicer_0']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['PMOS1InPMOSSetofSlicer_0']['_XYCoordinates'][0][1])], element)])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		for i in range(len(path_list)):
		    path_list[i][0] = [(xy + offset) for (xy, offset) in zip(path_list[i][0], xy_offset)]
		self._DesignParameter['left_outside_pmos_gate'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _Width=_width)
		self._DesignParameter['left_outside_pmos_gate']['_XYCoordinates'] = path_list
		self._DesignParameter['PCCAM1_CDNS_6375475055680_0'] = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_Name='PCCAM1_CDNS_6375475055680_0In{}'.format(_Name)))[0]
		self._DesignParameter['PCCAM1_CDNS_6375475055680_0']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(**dict(_ViaPoly2Met1NumberOfCOX=max(1, (1 + int(((((((self._DesignParameter['PMOS1InPMOSSetofSlicer_0']['_XYCoordinates'][0][0] + self._DesignParameter['PMOS1InPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]) + (self._DesignParameter['PMOS1InPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)) - ((self._DesignParameter['PMOS1InPMOSSetofSlicer_0']['_XYCoordinates'][0][0] + self._DesignParameter['PMOS1InPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['PMOS1InPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2))) - drc._CoMinSpace) - (2 * drc._CoMinEnclosureByPO)) / (drc._CoMinWidth + drc._CoMinSpace))))), _ViaPoly2Met1NumberOfCOY=1))
		self._DesignParameter['PCCAM1_CDNS_6375475055680_0']['_XYCoordinates'] = [[self._DesignParameter['PMOS2InPMOSSetofSlicer_0']['_XYCoordinates'][0][0], ((((self._DesignParameter['PMOS1InPMOSSetofSlicer_0']['_XYCoordinates'][0][1] + self._DesignParameter['PMOS1InPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) - (self._DesignParameter['PMOS1InPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)) - drc._Metal1MinSpace21) - (self._DesignParameter['PCCAM1_CDNS_6375475055680_1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2))]]
		path_list = []
		xy_offset = [0, 0]
		if (len(self._DesignParameter['PMOS2InPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_POLayerPINDrawing']['_XYCoordinates']) == 1):
		    mode = 'vertical'
		    _width = self._DesignParameter['PMOS2InPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_POLayerPINDrawing']['_XWidth']
		elif (self._DesignParameter['PMOS2InPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_POLayerPINDrawing']['_XYCoordinates'][0][0] == self._DesignParameter['PMOS2InPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_POLayerPINDrawing']['_XYCoordinates'][(- 1)][0]):
		    mode = 'horizontal'
		    _width = self._DesignParameter['PMOS2InPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_POLayerPINDrawing']['_XWidth']
		elif (self._DesignParameter['PMOS2InPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_POLayerPINDrawing']['_XYCoordinates'][0][1] == self._DesignParameter['PMOS2InPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_POLayerPINDrawing']['_XYCoordinates'][(- 1)][1]):
		    mode = 'vertical'
		    _width = self._DesignParameter['PMOS2InPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_POLayerPINDrawing']['_XWidth']
		else:
		    print('Invalid Target Input')
		if (mode == 'vertical'):
		    xy_with_offset = []
		    target_y_value = [[(+ self._DesignParameter['PCCAM1_CDNS_6375475055680_0']['_XYCoordinates'][0][0]), (+ self._DesignParameter['PCCAM1_CDNS_6375475055680_0']['_XYCoordinates'][0][1])]][0][1]
		    for i in range(len(self._DesignParameter['PMOS2InPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_POLayerPINDrawing']['_XYCoordinates'])):
		        xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['PMOS2InPMOSSetofSlicer_0']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['PMOS2InPMOSSetofSlicer_0']['_XYCoordinates'][0][1])], self._DesignParameter['PMOS2InPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_POLayerPINDrawing']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		elif (mode == 'horizontal'):
		    xy_with_offset = []
		    target_x_value = [[(+ self._DesignParameter['PCCAM1_CDNS_6375475055680_0']['_XYCoordinates'][0][0]), (+ self._DesignParameter['PCCAM1_CDNS_6375475055680_0']['_XYCoordinates'][0][1])]][0][0]
		    for i in range(len(self._DesignParameter['PMOS2InPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_POLayerPINDrawing']['_XYCoordinates'])):
		        xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['PMOS2InPMOSSetofSlicer_0']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['PMOS2InPMOSSetofSlicer_0']['_XYCoordinates'][0][1])], self._DesignParameter['PMOS2InPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_POLayerPINDrawing']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		for i in range(len(path_list)):
		    path_list[i][0] = [(xy + offset) for (xy, offset) in zip(path_list[i][0], xy_offset)]
		self._DesignParameter['right_outside_pmos_gate'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _Width=_width)
		self._DesignParameter['right_outside_pmos_gate']['_XYCoordinates'] = path_list
		self._DesignParameter['METAL4_path_21'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL4'][0], _Datatype=DesignParameters._LayerMapping['METAL4'][1], _Width=drc._MetalxMinWidth)
		self._DesignParameter['METAL4_path_21']['_XYCoordinates'] = [[[(+ self._DesignParameter['left_pmos_outside_via']['_XYCoordinates'][0][0]), (+ self._DesignParameter['left_pmos_outside_via']['_XYCoordinates'][0][1])], [(+ self._DesignParameter['left_pmos_outside_via']['_XYCoordinates'][(- 1)][0]), (+ self._DesignParameter['left_pmos_outside_via']['_XYCoordinates'][(- 1)][1])]]]
		self._DesignParameter['METAL4_path_20'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL4'][0], _Datatype=DesignParameters._LayerMapping['METAL4'][1], _Width=drc._MetalxMinWidth)
		self._DesignParameter['METAL4_path_20']['_XYCoordinates'] = [[[(+ self._DesignParameter['right_pmos_outside_via']['_XYCoordinates'][0][0]), (+ self._DesignParameter['right_pmos_outside_via']['_XYCoordinates'][0][1])], [(+ self._DesignParameter['right_pmos_outside_via']['_XYCoordinates'][(- 1)][0]), (+ self._DesignParameter['right_pmos_outside_via']['_XYCoordinates'][(- 1)][1])]]]
		self._DesignParameter['METAL3_path_29'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0], _Datatype=DesignParameters._LayerMapping['METAL3'][1], _Width=drc._MetalxMinWidth)
		self._DesignParameter['METAL3_path_29']['_XYCoordinates'] = [[[(+ self._DesignParameter['left_pmos_outside_via']['_XYCoordinates'][0][0]), (+ self._DesignParameter['left_pmos_outside_via']['_XYCoordinates'][0][1])], [(+ self._DesignParameter['left_pmos_outside_via']['_XYCoordinates'][(- 1)][0]), (+ self._DesignParameter['left_pmos_outside_via']['_XYCoordinates'][(- 1)][1])]]]
		self._DesignParameter['METAL2_path_38'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _Width=drc._MetalxMinWidth)
		self._DesignParameter['METAL2_path_38']['_XYCoordinates'] = [[[(+ self._DesignParameter['left_pmos_outside_via']['_XYCoordinates'][0][0]), (+ self._DesignParameter['left_pmos_outside_via']['_XYCoordinates'][0][1])], [(+ self._DesignParameter['left_pmos_outside_via']['_XYCoordinates'][(- 1)][0]), (+ self._DesignParameter['left_pmos_outside_via']['_XYCoordinates'][(- 1)][1])]]]
		self._DesignParameter['METAL3_path_28'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0], _Datatype=DesignParameters._LayerMapping['METAL3'][1], _Width=drc._MetalxMinWidth)
		self._DesignParameter['METAL3_path_28']['_XYCoordinates'] = [[[(+ self._DesignParameter['right_pmos_outside_via']['_XYCoordinates'][0][0]), (+ self._DesignParameter['right_pmos_outside_via']['_XYCoordinates'][0][1])], [(+ self._DesignParameter['right_pmos_outside_via']['_XYCoordinates'][(- 1)][0]), (+ self._DesignParameter['right_pmos_outside_via']['_XYCoordinates'][(- 1)][1])]]]
		self._DesignParameter['METAL2_path_37'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _Width=drc._MetalxMinWidth)
		self._DesignParameter['METAL2_path_37']['_XYCoordinates'] = [[[(+ self._DesignParameter['right_pmos_outside_via']['_XYCoordinates'][0][0]), (+ self._DesignParameter['right_pmos_outside_via']['_XYCoordinates'][0][1])], [(+ self._DesignParameter['right_pmos_outside_via']['_XYCoordinates'][(- 1)][0]), (+ self._DesignParameter['right_pmos_outside_via']['_XYCoordinates'][(- 1)][1])]]]
		self._DesignParameter['M2V2M3_CDNS_637547505561_1'] = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_Name='M2V2M3_CDNS_637547505561_1In{}'.format(_Name)))[0]
		self._DesignParameter['M2V2M3_CDNS_637547505561_1']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureY(**dict(_ViaMet22Met3NumberOfCOX=max(1, (1 + int(((((((self._DesignParameter['nmos_left_drain']['_XYCoordinates'][(- 1)][0] + self._DesignParameter['nmos_left_drain']['_DesignObj']._DesignParameter['_Met2Layer']['_XYCoordinates'][0][0]) + (self._DesignParameter['nmos_left_drain']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth'] / 2)) - ((self._DesignParameter['nmos_left_drain']['_XYCoordinates'][0][0] + self._DesignParameter['nmos_left_drain']['_DesignObj']._DesignParameter['_Met2Layer']['_XYCoordinates'][0][0]) - (self._DesignParameter['nmos_left_drain']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth'] / 2))) - drc._VIAxMinSpace) - (2 * drc._VIAxMinEnclosureByMetx)) / (drc._VIAxMinWidth + drc._VIAxMinSpace))))), _ViaMet22Met3NumberOfCOY=1))
		self._DesignParameter['M2V2M3_CDNS_637547505561_1']['_XYCoordinates'] = [[self._DesignParameter['NMOS1InNMOSSetofSlicer_0']['_XYCoordinates'][0][0], ((((self._DesignParameter['nmos_left_source']['_XYCoordinates'][0][1] + self._DesignParameter['nmos_left_source']['_DesignObj']._DesignParameter['_Met2Layer']['_XYCoordinates'][0][1]) + (self._DesignParameter['nmos_left_source']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] / 2)) + drc._MetalxMinSpace2) + (self._DesignParameter['M2V2M3_CDNS_637547505561_1']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] / 2))]]
		self._DesignParameter['m3m4_precharge_via_left'] = self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_Name='m3m4_precharge_via_leftIn{}'.format(_Name)))[0]
		self._DesignParameter['m3m4_precharge_via_left']['_DesignObj']._CalculateViaMet32Met4DesignParameterMinimumEnclosureX(**dict(_ViaMet32Met4NumberOfCOX=1, _ViaMet32Met4NumberOfCOY=2))
		self._DesignParameter['m3m4_precharge_via_left']['_XYCoordinates'] = None
		XYList = []
		xy_offset = (0, (((((- self._DesignParameter['M2V2M3_CDNS_637547505561_1']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth']) / 2) + (self._DesignParameter['m3m4_precharge_via_left']['_DesignObj']._DesignParameter['_Met4Layer']['_YWidth'] / 2)) + self._DesignParameter['M2V2M3_CDNS_637547505561_1']['_XYCoordinates'][0][1]) + (- self._DesignParameter['left_pmos_outside_via']['_XYCoordinates'][0][1])))
		for i in range(len(self._DesignParameter['left_pmos_outside_via']['_XYCoordinates'])):
		    xy = (self._DesignParameter['left_pmos_outside_via']['_XYCoordinates'][i][0] if (type(self._DesignParameter['left_pmos_outside_via']['_XYCoordinates'][i][0]) == list) else self._DesignParameter['left_pmos_outside_via']['_XYCoordinates'][i])
		    XYList.append([((x + y) + z) for (x, y, z) in zip([0, 0], xy, xy_offset)])
		self._DesignParameter['m3m4_precharge_via_left']['_XYCoordinates'] = XYList
		self._DesignParameter['M2V2M3_CDNS_637547505561_0'] = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_Name='M2V2M3_CDNS_637547505561_0In{}'.format(_Name)))[0]
		self._DesignParameter['M2V2M3_CDNS_637547505561_0']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureY(**dict(_ViaMet22Met3NumberOfCOX=max(1, (1 + int(((((((self._DesignParameter['nmos_left_drain']['_XYCoordinates'][(- 1)][0] + self._DesignParameter['nmos_left_drain']['_DesignObj']._DesignParameter['_Met2Layer']['_XYCoordinates'][0][0]) + (self._DesignParameter['nmos_left_drain']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth'] / 2)) - ((self._DesignParameter['nmos_left_drain']['_XYCoordinates'][0][0] + self._DesignParameter['nmos_left_drain']['_DesignObj']._DesignParameter['_Met2Layer']['_XYCoordinates'][0][0]) - (self._DesignParameter['nmos_left_drain']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth'] / 2))) - drc._VIAxMinSpace) - (2 * drc._VIAxMinEnclosureByMetx)) / (drc._VIAxMinWidth + drc._VIAxMinSpace))))), _ViaMet22Met3NumberOfCOY=1))
		self._DesignParameter['M2V2M3_CDNS_637547505561_0']['_XYCoordinates'] = [[self._DesignParameter['NMOS2InNMOSSetofSlicer_0']['_XYCoordinates'][0][0], ((((self._DesignParameter['nmos_left_source']['_XYCoordinates'][0][1] + self._DesignParameter['nmos_left_source']['_DesignObj']._DesignParameter['_Met2Layer']['_XYCoordinates'][0][1]) + (self._DesignParameter['nmos_left_source']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] / 2)) + drc._MetalxMinSpace2) + (self._DesignParameter['M2V2M3_CDNS_637547505561_1']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] / 2))]]
		self._DesignParameter['m3m4_precharge_via_right'] = self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_Name='m3m4_precharge_via_rightIn{}'.format(_Name)))[0]
		self._DesignParameter['m3m4_precharge_via_right']['_DesignObj']._CalculateViaMet32Met4DesignParameterMinimumEnclosureX(**dict(_ViaMet32Met4NumberOfCOX=1, _ViaMet32Met4NumberOfCOY=2))
		self._DesignParameter['m3m4_precharge_via_right']['_XYCoordinates'] = None
		XYList = []
		xy_offset = (0, (((((- self._DesignParameter['M2V2M3_CDNS_637547505561_1']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth']) / 2) + (self._DesignParameter['m3m4_precharge_via_left']['_DesignObj']._DesignParameter['_Met4Layer']['_YWidth'] / 2)) + self._DesignParameter['M2V2M3_CDNS_637547505561_1']['_XYCoordinates'][0][1]) + (- self._DesignParameter['left_pmos_outside_via']['_XYCoordinates'][0][1])))
		for i in range(len(self._DesignParameter['right_pmos_outside_via']['_XYCoordinates'])):
		    xy = (self._DesignParameter['right_pmos_outside_via']['_XYCoordinates'][i][0] if (type(self._DesignParameter['right_pmos_outside_via']['_XYCoordinates'][i][0]) == list) else self._DesignParameter['right_pmos_outside_via']['_XYCoordinates'][i])
		    XYList.append([((x + y) + z) for (x, y, z) in zip([0, 0], xy, xy_offset)])
		self._DesignParameter['m3m4_precharge_via_right']['_XYCoordinates'] = XYList
		path_list = []
		xy_offset = [0, 0]
		if (len(self._DesignParameter['left_pmos_outside_via']['_XYCoordinates']) == 1):
		    mode = 'vertical'
		    _width = self._DesignParameter['left_pmos_outside_via']['_DesignObj']._DesignParameter['ViaMet32Met4']['_DesignObj']._DesignParameter['_Met4Layer']['_XWidth']
		elif (self._DesignParameter['left_pmos_outside_via']['_XYCoordinates'][0][0] == self._DesignParameter['left_pmos_outside_via']['_XYCoordinates'][(- 1)][0]):
		    mode = 'horizontal'
		    _width = self._DesignParameter['left_pmos_outside_via']['_DesignObj']._DesignParameter['ViaMet32Met4']['_DesignObj']._DesignParameter['_Met4Layer']['_XWidth']
		elif (self._DesignParameter['left_pmos_outside_via']['_XYCoordinates'][0][1] == self._DesignParameter['left_pmos_outside_via']['_XYCoordinates'][(- 1)][1]):
		    mode = 'vertical'
		    _width = self._DesignParameter['left_pmos_outside_via']['_DesignObj']._DesignParameter['ViaMet32Met4']['_DesignObj']._DesignParameter['_Met4Layer']['_XWidth']
		else:
		    print('Invalid Target Input')
		if (mode == 'vertical'):
		    xy_with_offset = []
		    target_y_value = [[(+ self._DesignParameter['m3m4_precharge_via_left']['_XYCoordinates'][0][0]), (+ self._DesignParameter['m3m4_precharge_via_left']['_XYCoordinates'][0][1])]][0][1]
		    for i in range(len(self._DesignParameter['left_pmos_outside_via']['_XYCoordinates'])):
		        xy_with_offset.append([(x + y) for (x, y) in zip([0, 0], self._DesignParameter['left_pmos_outside_via']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		elif (mode == 'horizontal'):
		    xy_with_offset = []
		    target_x_value = [[(+ self._DesignParameter['m3m4_precharge_via_left']['_XYCoordinates'][0][0]), (+ self._DesignParameter['m3m4_precharge_via_left']['_XYCoordinates'][0][1])]][0][0]
		    for i in range(len(self._DesignParameter['left_pmos_outside_via']['_XYCoordinates'])):
		        xy_with_offset.append([(x + y) for (x, y) in zip([0, 0], self._DesignParameter['left_pmos_outside_via']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		for i in range(len(path_list)):
		    path_list[i][0] = [(xy + offset) for (xy, offset) in zip(path_list[i][0], xy_offset)]
		self._DesignParameter['np_precharge_left_routing'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL4'][0], _Datatype=DesignParameters._LayerMapping['METAL4'][1], _Width=_width)
		self._DesignParameter['np_precharge_left_routing']['_XYCoordinates'] = path_list
		path_list = []
		xy_offset = [0, 0]
		if (len(self._DesignParameter['right_pmos_outside_via']['_XYCoordinates']) == 1):
		    mode = 'vertical'
		    _width = self._DesignParameter['right_pmos_outside_via']['_DesignObj']._DesignParameter['ViaMet32Met4']['_DesignObj']._DesignParameter['_Met4Layer']['_XWidth']
		elif (self._DesignParameter['right_pmos_outside_via']['_XYCoordinates'][0][0] == self._DesignParameter['right_pmos_outside_via']['_XYCoordinates'][(- 1)][0]):
		    mode = 'horizontal'
		    _width = self._DesignParameter['right_pmos_outside_via']['_DesignObj']._DesignParameter['ViaMet32Met4']['_DesignObj']._DesignParameter['_Met4Layer']['_XWidth']
		elif (self._DesignParameter['right_pmos_outside_via']['_XYCoordinates'][0][1] == self._DesignParameter['right_pmos_outside_via']['_XYCoordinates'][(- 1)][1]):
		    mode = 'vertical'
		    _width = self._DesignParameter['right_pmos_outside_via']['_DesignObj']._DesignParameter['ViaMet32Met4']['_DesignObj']._DesignParameter['_Met4Layer']['_XWidth']
		else:
		    print('Invalid Target Input')
		if (mode == 'vertical'):
		    xy_with_offset = []
		    target_y_value = [[(+ self._DesignParameter['m3m4_precharge_via_right']['_XYCoordinates'][0][0]), (+ self._DesignParameter['m3m4_precharge_via_right']['_XYCoordinates'][0][1])]][0][1]
		    for i in range(len(self._DesignParameter['right_pmos_outside_via']['_XYCoordinates'])):
		        xy_with_offset.append([(x + y) for (x, y) in zip([0, 0], self._DesignParameter['right_pmos_outside_via']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		elif (mode == 'horizontal'):
		    xy_with_offset = []
		    target_x_value = [[(+ self._DesignParameter['m3m4_precharge_via_right']['_XYCoordinates'][0][0]), (+ self._DesignParameter['m3m4_precharge_via_right']['_XYCoordinates'][0][1])]][0][0]
		    for i in range(len(self._DesignParameter['right_pmos_outside_via']['_XYCoordinates'])):
		        xy_with_offset.append([(x + y) for (x, y) in zip([0, 0], self._DesignParameter['right_pmos_outside_via']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		for i in range(len(path_list)):
		    path_list[i][0] = [(xy + offset) for (xy, offset) in zip(path_list[i][0], xy_offset)]
		self._DesignParameter['np_precharge_right_routing'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL4'][0], _Datatype=DesignParameters._LayerMapping['METAL4'][1], _Width=_width)
		self._DesignParameter['np_precharge_right_routing']['_XYCoordinates'] = path_list
		self._DesignParameter['nmos_center_via_stack_2to4'] = self._SrefElementDeclaration(_DesignObj=ViaStack._ViaStack(_Name='nmos_center_via_stack_2to4In{}'.format(_Name)))[0]
		self._DesignParameter['nmos_center_via_stack_2to4']['_DesignObj']._CalculateStackMinimumEnclosureY(**dict(COX=4, COY=1, start_layer=2, end_layer=4))
		self._DesignParameter['nmos_center_via_stack_2to4']['_XYCoordinates'] = [[self._DesignParameter['nmos_bot']['_XYCoordinates'][0][0], ((((- self._DesignParameter['nmos_center_via_stack_2to4']['_DesignObj']._DesignParameter['ViaMet22Met3']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth']) / 2) + (- drc._MetalxMinSpace4)) + min(((self._DesignParameter['M1V1M2_CDNS_6375475055674_1']['_XYCoordinates'][0][1] + self._DesignParameter['M1V1M2_CDNS_6375475055674_1']['_DesignObj']._DesignParameter['_Met2Layer']['_XYCoordinates'][0][1]) - (self._DesignParameter['M1V1M2_CDNS_6375475055674_1']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] / 2)), (((self._DesignParameter['nmos_inner_left_vias']['_XYCoordinates'][0][1] + self._DesignParameter['nmos_inner_left_vias']['_DesignObj']._DesignParameter['ViaMet32Met4']['_XYCoordinates'][0][1]) + self._DesignParameter['nmos_inner_left_vias']['_DesignObj']._DesignParameter['ViaMet32Met4']['_DesignObj']._DesignParameter['_Met4Layer']['_XYCoordinates'][0][1]) - (self._DesignParameter['nmos_inner_left_vias']['_DesignObj']._DesignParameter['ViaMet32Met4']['_DesignObj']._DesignParameter['_Met4Layer']['_YWidth'] / 2))))]]
		self._DesignParameter['METAL2_path_27'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _Width=self._DesignParameter['nmos_center_via_stack_2to4']['_DesignObj']._DesignParameter['ViaMet32Met4']['_DesignObj']._DesignParameter['_Met4Layer']['_YWidth'])
		self._DesignParameter['METAL2_path_27']['_XYCoordinates'] = [[[((self._DesignParameter['nmos_left_source']['_XYCoordinates'][0][0] + self._DesignParameter['nmos_left_source']['_DesignObj']._DesignParameter['_Met2Layer']['_XYCoordinates'][0][0]) - (self._DesignParameter['nmos_left_source']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth'] / 2)), self._DesignParameter['nmos_center_via_stack_2to4']['_XYCoordinates'][0][1]], [((self._DesignParameter['nmos_right_source']['_XYCoordinates'][(- 1)][0] + self._DesignParameter['nmos_right_source']['_DesignObj']._DesignParameter['_Met2Layer']['_XYCoordinates'][0][0]) + (self._DesignParameter['nmos_right_source']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth'] / 2)), self._DesignParameter['nmos_center_via_stack_2to4']['_XYCoordinates'][0][1]]]]
		self._DesignParameter['METAL4_path_17'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL4'][0], _Datatype=DesignParameters._LayerMapping['METAL4'][1], _Width=176)
		self._DesignParameter['METAL4_path_17']['_XYCoordinates'] = [[[(+ self._DesignParameter['nmos_center_via_stack_2to4']['_XYCoordinates'][0][0]), (+ self._DesignParameter['nmos_center_via_stack_2to4']['_XYCoordinates'][0][1])], [self._DesignParameter['nmos_center_via_stack_2to4']['_XYCoordinates'][0][0], (((self._DesignParameter['nmos_bot_drain_vias']['_XYCoordinates'][0][1] + self._DesignParameter['nmos_bot_drain_vias']['_DesignObj']._DesignParameter['ViaMet32Met4']['_XYCoordinates'][0][1]) + self._DesignParameter['nmos_bot_drain_vias']['_DesignObj']._DesignParameter['ViaMet32Met4']['_DesignObj']._DesignParameter['_Met4Layer']['_XYCoordinates'][0][1]) - (self._DesignParameter['nmos_bot_drain_vias']['_DesignObj']._DesignParameter['ViaMet32Met4']['_DesignObj']._DesignParameter['_Met4Layer']['_YWidth'] / 2))]]]
		self._DesignParameter['POLY_path_65'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _Width=self._DesignParameter['nmos_bot_gate_poly_via']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'])
		self._DesignParameter['POLY_path_65']['_XYCoordinates'] = [[[((self._DesignParameter['nmos_bot']['_XYCoordinates'][0][0] + self._DesignParameter['nmos_bot']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['nmos_bot']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)), self._DesignParameter['nmos_bot_gate_poly_via']['_XYCoordinates'][0][1]], [((self._DesignParameter['nmos_bot']['_XYCoordinates'][0][0] + self._DesignParameter['nmos_bot']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]) + (self._DesignParameter['nmos_bot']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)), self._DesignParameter['nmos_bot_gate_poly_via']['_XYCoordinates'][0][1]]]]
		self._DesignParameter['METAL1_boundary_355'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _XWidth=max(self._DesignParameter['nmos_bot_viastack']['_DesignObj']._DesignParameter['ViaMet12Met2']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'], self._DesignParameter['nmos_bot_gate_poly_via']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']), _YWidth=max(self._DesignParameter['nmos_bot_viastack']['_DesignObj']._DesignParameter['ViaMet12Met2']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'], self._DesignParameter['nmos_bot_gate_poly_via']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']))
		self._DesignParameter['METAL1_boundary_355']['_XYCoordinates'] = [[(+ self._DesignParameter['nmos_bot_viastack']['_XYCoordinates'][0][0]), (+ self._DesignParameter['nmos_bot_viastack']['_XYCoordinates'][0][1])]]
		self._DesignParameter['METAL3_path_34'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0], _Datatype=DesignParameters._LayerMapping['METAL3'][1], _Width=drc._MetalxMinWidth)
		self._DesignParameter['METAL3_path_34']['_XYCoordinates'] = [[[self._DesignParameter['m3m4_precharge_via_left']['_XYCoordinates'][0][0], self._DesignParameter['M2V2M3_CDNS_637547505561_1']['_XYCoordinates'][0][1]], [self._DesignParameter['m3m4_precharge_via_left']['_XYCoordinates'][(- 1)][0], self._DesignParameter['M2V2M3_CDNS_637547505561_1']['_XYCoordinates'][0][1]]]]
		self._DesignParameter['METAL3_path_33'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0], _Datatype=DesignParameters._LayerMapping['METAL3'][1], _Width=drc._MetalxMinWidth)
		self._DesignParameter['METAL3_path_33']['_XYCoordinates'] = [[[self._DesignParameter['m3m4_precharge_via_right']['_XYCoordinates'][0][0], self._DesignParameter['M2V2M3_CDNS_637547505561_0']['_XYCoordinates'][0][1]], [self._DesignParameter['m3m4_precharge_via_right']['_XYCoordinates'][(- 1)][0], self._DesignParameter['M2V2M3_CDNS_637547505561_0']['_XYCoordinates'][0][1]]]]
		self._DesignParameter['METAL2_path_29'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _Width=drc._MetalxMinWidth)
		self._DesignParameter['METAL2_path_29']['_XYCoordinates'] = [[[((self._DesignParameter['nmos_left_drain']['_XYCoordinates'][0][0] + self._DesignParameter['nmos_left_drain']['_DesignObj']._DesignParameter['_Met2Layer']['_XYCoordinates'][0][0]) - (self._DesignParameter['nmos_left_drain']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth'] / 2)), self._DesignParameter['M2V2M3_CDNS_637547505561_1']['_XYCoordinates'][0][1]], [self._DesignParameter['nmos_inner_left_via_arr']['_XYCoordinates'][0][0], self._DesignParameter['M2V2M3_CDNS_637547505561_1']['_XYCoordinates'][0][1]], [self._DesignParameter['nmos_inner_left_via_arr']['_XYCoordinates'][0][0], self._DesignParameter['nmos_inner_left_via_arr']['_XYCoordinates'][0][1]]]]
		self._DesignParameter['METAL2_path_28'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _Width=drc._MetalxMinWidth)
		self._DesignParameter['METAL2_path_28']['_XYCoordinates'] = [[[((self._DesignParameter['nmos_right_drain']['_XYCoordinates'][(- 1)][0] + self._DesignParameter['nmos_right_drain']['_DesignObj']._DesignParameter['_Met2Layer']['_XYCoordinates'][0][0]) + (self._DesignParameter['nmos_right_drain']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth'] / 2)), self._DesignParameter['M2V2M3_CDNS_637547505561_0']['_XYCoordinates'][0][1]], [self._DesignParameter['nmos_inner_right_via_arr']['_XYCoordinates'][0][0], self._DesignParameter['M2V2M3_CDNS_637547505561_0']['_XYCoordinates'][0][1]], [self._DesignParameter['nmos_inner_right_via_arr']['_XYCoordinates'][0][0], self._DesignParameter['nmos_inner_right_via_arr']['_XYCoordinates'][0][1]]]]
		self._DesignParameter['POLY_path_128'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _Width=self._DesignParameter['PCCAM1_CDNS_6375475055680_1']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'])
		self._DesignParameter['POLY_path_128']['_XYCoordinates'] = [[[((self._DesignParameter['PMOS1InPMOSSetofSlicer_0']['_XYCoordinates'][0][0] + self._DesignParameter['PMOS1InPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['PMOS1InPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)), self._DesignParameter['PCCAM1_CDNS_6375475055680_1']['_XYCoordinates'][0][1]], [((self._DesignParameter['PMOS1InPMOSSetofSlicer_0']['_XYCoordinates'][0][0] + self._DesignParameter['PMOS1InPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]) + (self._DesignParameter['PMOS1InPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)), self._DesignParameter['PCCAM1_CDNS_6375475055680_1']['_XYCoordinates'][0][1]]]]
		self._DesignParameter['POLY_path_127'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _Width=self._DesignParameter['PCCAM1_CDNS_6375475055680_1']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'])
		self._DesignParameter['POLY_path_127']['_XYCoordinates'] = [[[((self._DesignParameter['PMOS2InPMOSSetofSlicer_0']['_XYCoordinates'][0][0] + self._DesignParameter['PMOS2InPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['PMOS2InPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)), self._DesignParameter['PCCAM1_CDNS_6375475055680_0']['_XYCoordinates'][0][1]], [((self._DesignParameter['PMOS2InPMOSSetofSlicer_0']['_XYCoordinates'][0][0] + self._DesignParameter['PMOS2InPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]) + (self._DesignParameter['PMOS2InPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)), self._DesignParameter['PCCAM1_CDNS_6375475055680_0']['_XYCoordinates'][0][1]]]]
		self._DesignParameter['left_precharge_gate_vias'] = self._SrefElementDeclaration(_DesignObj=ViaStack._ViaStack(_Name='left_precharge_gate_viasIn{}'.format(_Name)))[0]
		self._DesignParameter['left_precharge_gate_vias']['_DesignObj']._CalculateStackMinimumEnclosureY(**dict(COX=max(1, (1 + int((((self._DesignParameter['PCCAM1_CDNS_6375475055680_1']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] - drc._VIAxMinSpace) - (2 * drc._VIAxMinEnclosureByMetx)) / (drc._VIAxMinWidth + drc._VIAxMinSpace))))), COY=1, start_layer=1, end_layer=3))
		self._DesignParameter['left_precharge_gate_vias']['_XYCoordinates'] = [[(+ self._DesignParameter['PCCAM1_CDNS_6375475055680_1']['_XYCoordinates'][0][0]), (+ self._DesignParameter['PCCAM1_CDNS_6375475055680_1']['_XYCoordinates'][0][1])]]
		self._DesignParameter['METAL1_boundary_360'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _XWidth=max(self._DesignParameter['PCCAM1_CDNS_6375475055680_1']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'], self._DesignParameter['left_precharge_gate_vias']['_DesignObj']._DesignParameter['ViaMet12Met2']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']), _YWidth=max(self._DesignParameter['PCCAM1_CDNS_6375475055680_1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'], self._DesignParameter['left_precharge_gate_vias']['_DesignObj']._DesignParameter['ViaMet12Met2']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']))
		self._DesignParameter['METAL1_boundary_360']['_XYCoordinates'] = [[(+ self._DesignParameter['PCCAM1_CDNS_6375475055680_1']['_XYCoordinates'][0][0]), (+ self._DesignParameter['PCCAM1_CDNS_6375475055680_1']['_XYCoordinates'][0][1])]]
		self._DesignParameter['right_precharge_gate_vias'] = self._SrefElementDeclaration(_DesignObj=ViaStack._ViaStack(_Name='right_precharge_gate_viasIn{}'.format(_Name)))[0]
		self._DesignParameter['right_precharge_gate_vias']['_DesignObj']._CalculateStackMinimumEnclosureY(**dict(COX=max(1, (1 + int((((self._DesignParameter['PCCAM1_CDNS_6375475055680_1']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] - drc._VIAxMinSpace) - (2 * drc._VIAxMinEnclosureByMetx)) / (drc._VIAxMinWidth + drc._VIAxMinSpace))))), COY=1, start_layer=1, end_layer=3))
		self._DesignParameter['right_precharge_gate_vias']['_XYCoordinates'] = [[(+ self._DesignParameter['PCCAM1_CDNS_6375475055680_0']['_XYCoordinates'][0][0]), (+ self._DesignParameter['PCCAM1_CDNS_6375475055680_0']['_XYCoordinates'][0][1])]]
		self._DesignParameter['METAL1_boundary_359'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _XWidth=max(self._DesignParameter['PCCAM1_CDNS_6375475055680_1']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'], self._DesignParameter['left_precharge_gate_vias']['_DesignObj']._DesignParameter['ViaMet12Met2']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']), _YWidth=max(self._DesignParameter['PCCAM1_CDNS_6375475055680_1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'], self._DesignParameter['left_precharge_gate_vias']['_DesignObj']._DesignParameter['ViaMet12Met2']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']))
		self._DesignParameter['METAL1_boundary_359']['_XYCoordinates'] = [[(+ self._DesignParameter['PCCAM1_CDNS_6375475055680_0']['_XYCoordinates'][0][0]), (+ self._DesignParameter['PCCAM1_CDNS_6375475055680_0']['_XYCoordinates'][0][1])]]
		self._DesignParameter['METAL2_path_40'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _Width=drc._MetalxMinWidth)
		self._DesignParameter['METAL2_path_40']['_XYCoordinates'] = [[[(+ self._DesignParameter['left_pmos_inside_via']['_XYCoordinates'][0][0]), (+ self._DesignParameter['left_pmos_inside_via']['_XYCoordinates'][0][1])], [(+ self._DesignParameter['pmos_inner_left']['_XYCoordinates'][0][0]), (+ self._DesignParameter['pmos_inner_left']['_XYCoordinates'][0][1])]]]
		self._DesignParameter['METAL2_path_39'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _Width=drc._MetalxMinWidth)
		self._DesignParameter['METAL2_path_39']['_XYCoordinates'] = [[[(+ self._DesignParameter['pmos_inside_right_via']['_XYCoordinates'][0][0]), (+ self._DesignParameter['pmos_inside_right_via']['_XYCoordinates'][0][1])], [(+ self._DesignParameter['right_pmos_inside_via']['_XYCoordinates'][0][0]), (+ self._DesignParameter['right_pmos_inside_via']['_XYCoordinates'][0][1])]]]
		self._DesignParameter['pmos_inner_left_via2to4'] = self._SrefElementDeclaration(_DesignObj=ViaStack._ViaStack(_Name='pmos_inner_left_via2to4In{}'.format(_Name)))[0]
		self._DesignParameter['pmos_inner_left_via2to4']['_DesignObj']._CalculateStackMinimumEnclosureX(**dict(COX=1, COY=max(1, (1 + int((((self._DesignParameter['pmos_inner_left']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] - drc._VIAxMinSpace) - (2 * drc._VIAxMinEnclosureByMetx)) / (drc._VIAxMinWidth + drc._VIAxMinSpace))))), start_layer=2, end_layer=4))
		self._DesignParameter['pmos_inner_left_via2to4']['_XYCoordinates'] = [[(+ self._DesignParameter['pmos_inner_left']['_XYCoordinates'][0][0]), (+ self._DesignParameter['pmos_inner_left']['_XYCoordinates'][0][1])]]
		self._DesignParameter['pmos_inner_right_via2to4'] = self._SrefElementDeclaration(_DesignObj=ViaStack._ViaStack(_Name='pmos_inner_right_via2to4In{}'.format(_Name)))[0]
		self._DesignParameter['pmos_inner_right_via2to4']['_DesignObj']._CalculateStackMinimumEnclosureX(**dict(COX=1, COY=max(1, (1 + int((((self._DesignParameter['pmos_inner_left']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] - drc._VIAxMinSpace) - (2 * drc._VIAxMinEnclosureByMetx)) / (drc._VIAxMinWidth + drc._VIAxMinSpace))))), start_layer=2, end_layer=4))
		self._DesignParameter['pmos_inner_right_via2to4']['_XYCoordinates'] = [[(+ self._DesignParameter['pmos_inside_right_via']['_XYCoordinates'][0][0]), (+ self._DesignParameter['pmos_inside_right_via']['_XYCoordinates'][0][1])]]
		self._DesignParameter['METAL4_path_19'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL4'][0], _Datatype=DesignParameters._LayerMapping['METAL4'][1], _Width=(drc._MetalxMinWidth * 2))
		self._DesignParameter['METAL4_path_19']['_XYCoordinates'] = [[[(+ ((self._DesignParameter['pmos_inner_left_via2to4']['_XYCoordinates'][0][0] + self._DesignParameter['pmos_inner_left_via2to4']['_DesignObj']._DesignParameter['ViaMet32Met4']['_XYCoordinates'][0][0]) + self._DesignParameter['pmos_inner_left_via2to4']['_DesignObj']._DesignParameter['ViaMet32Met4']['_DesignObj']._DesignParameter['_Met4Layer']['_XYCoordinates'][0][0])), (+ (((self._DesignParameter['pmos_inner_left_via2to4']['_XYCoordinates'][0][1] + self._DesignParameter['pmos_inner_left_via2to4']['_DesignObj']._DesignParameter['ViaMet32Met4']['_XYCoordinates'][0][1]) + self._DesignParameter['pmos_inner_left_via2to4']['_DesignObj']._DesignParameter['ViaMet32Met4']['_DesignObj']._DesignParameter['_Met4Layer']['_XYCoordinates'][0][1]) + (self._DesignParameter['pmos_inner_left_via2to4']['_DesignObj']._DesignParameter['ViaMet32Met4']['_DesignObj']._DesignParameter['_Met4Layer']['_YWidth'] / 2)))], [(+ ((self._DesignParameter['nmos_inner_left_vias']['_XYCoordinates'][0][0] + self._DesignParameter['nmos_inner_left_vias']['_DesignObj']._DesignParameter['ViaMet32Met4']['_XYCoordinates'][0][0]) + self._DesignParameter['nmos_inner_left_vias']['_DesignObj']._DesignParameter['ViaMet32Met4']['_DesignObj']._DesignParameter['_Met4Layer']['_XYCoordinates'][0][0])), (+ (((self._DesignParameter['nmos_inner_left_vias']['_XYCoordinates'][0][1] + self._DesignParameter['nmos_inner_left_vias']['_DesignObj']._DesignParameter['ViaMet32Met4']['_XYCoordinates'][0][1]) + self._DesignParameter['nmos_inner_left_vias']['_DesignObj']._DesignParameter['ViaMet32Met4']['_DesignObj']._DesignParameter['_Met4Layer']['_XYCoordinates'][0][1]) - (self._DesignParameter['nmos_inner_left_vias']['_DesignObj']._DesignParameter['ViaMet32Met4']['_DesignObj']._DesignParameter['_Met4Layer']['_YWidth'] / 2)))]]]
		self._DesignParameter['METAL4_path_18'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL4'][0], _Datatype=DesignParameters._LayerMapping['METAL4'][1], _Width=(drc._MetalxMinWidth * 2))
		self._DesignParameter['METAL4_path_18']['_XYCoordinates'] = [[[(+ ((self._DesignParameter['pmos_inner_right_via2to4']['_XYCoordinates'][0][0] + self._DesignParameter['pmos_inner_right_via2to4']['_DesignObj']._DesignParameter['ViaMet32Met4']['_XYCoordinates'][0][0]) + self._DesignParameter['pmos_inner_right_via2to4']['_DesignObj']._DesignParameter['ViaMet32Met4']['_DesignObj']._DesignParameter['_Met4Layer']['_XYCoordinates'][0][0])), (+ (((self._DesignParameter['pmos_inner_right_via2to4']['_XYCoordinates'][0][1] + self._DesignParameter['pmos_inner_right_via2to4']['_DesignObj']._DesignParameter['ViaMet32Met4']['_XYCoordinates'][0][1]) + self._DesignParameter['pmos_inner_right_via2to4']['_DesignObj']._DesignParameter['ViaMet32Met4']['_DesignObj']._DesignParameter['_Met4Layer']['_XYCoordinates'][0][1]) + (self._DesignParameter['pmos_inner_right_via2to4']['_DesignObj']._DesignParameter['ViaMet32Met4']['_DesignObj']._DesignParameter['_Met4Layer']['_YWidth'] / 2)))], [(+ ((self._DesignParameter['nmos_inner_right_vias']['_XYCoordinates'][0][0] + self._DesignParameter['nmos_inner_right_vias']['_DesignObj']._DesignParameter['ViaMet32Met4']['_XYCoordinates'][0][0]) + self._DesignParameter['nmos_inner_right_vias']['_DesignObj']._DesignParameter['ViaMet32Met4']['_DesignObj']._DesignParameter['_Met4Layer']['_XYCoordinates'][0][0])), (+ (((self._DesignParameter['nmos_inner_right_vias']['_XYCoordinates'][0][1] + self._DesignParameter['nmos_inner_right_vias']['_DesignObj']._DesignParameter['ViaMet32Met4']['_XYCoordinates'][0][1]) + self._DesignParameter['nmos_inner_right_vias']['_DesignObj']._DesignParameter['ViaMet32Met4']['_DesignObj']._DesignParameter['_Met4Layer']['_XYCoordinates'][0][1]) - (self._DesignParameter['nmos_inner_right_vias']['_DesignObj']._DesignParameter['ViaMet32Met4']['_DesignObj']._DesignParameter['_Met4Layer']['_YWidth'] / 2)))]]]
		self._DesignParameter['M1V1M2_CDNS_6375475055616_11'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='M1V1M2_CDNS_6375475055616_11In{}'.format(_Name)))[0]
		self._DesignParameter['M1V1M2_CDNS_6375475055616_11']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureY(**dict(_ViaMet12Met2NumberOfCOX=2, _ViaMet12Met2NumberOfCOY=1))
		self._DesignParameter['M1V1M2_CDNS_6375475055616_11']['_XYCoordinates'] = [[(+ self._DesignParameter['PCCAM1_CDNS_6375475055654_15']['_XYCoordinates'][0][0]), (+ self._DesignParameter['PCCAM1_CDNS_6375475055654_15']['_XYCoordinates'][0][1])]]
		self._DesignParameter['M1V1M2_CDNS_6375475055616_10'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='M1V1M2_CDNS_6375475055616_10In{}'.format(_Name)))[0]
		self._DesignParameter['M1V1M2_CDNS_6375475055616_10']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureY(**dict(_ViaMet12Met2NumberOfCOX=2, _ViaMet12Met2NumberOfCOY=1))
		self._DesignParameter['M1V1M2_CDNS_6375475055616_10']['_XYCoordinates'] = [[(+ self._DesignParameter['PCCAM1_CDNS_6375475055654_14']['_XYCoordinates'][0][0]), (+ self._DesignParameter['PCCAM1_CDNS_6375475055654_14']['_XYCoordinates'][0][1])]]
		self._DesignParameter['METAL1_boundary_358'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _XWidth=max(self._DesignParameter['M1V1M2_CDNS_6375475055616_11']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'], self._DesignParameter['PCCAM1_CDNS_6375475055654_15']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']), _YWidth=max(self._DesignParameter['M1V1M2_CDNS_6375475055616_11']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'], self._DesignParameter['PCCAM1_CDNS_6375475055654_15']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']))
		self._DesignParameter['METAL1_boundary_358']['_XYCoordinates'] = [[(+ self._DesignParameter['PCCAM1_CDNS_6375475055654_15']['_XYCoordinates'][0][0]), (+ self._DesignParameter['PCCAM1_CDNS_6375475055654_15']['_XYCoordinates'][0][1])]]
		self._DesignParameter['METAL1_boundary_357'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _XWidth=max(self._DesignParameter['M1V1M2_CDNS_6375475055616_11']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'], self._DesignParameter['PCCAM1_CDNS_6375475055654_15']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']), _YWidth=max(self._DesignParameter['M1V1M2_CDNS_6375475055616_11']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'], self._DesignParameter['PCCAM1_CDNS_6375475055654_15']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']))
		self._DesignParameter['METAL1_boundary_357']['_XYCoordinates'] = [[(+ self._DesignParameter['PCCAM1_CDNS_6375475055654_14']['_XYCoordinates'][0][0]), (+ self._DesignParameter['PCCAM1_CDNS_6375475055654_14']['_XYCoordinates'][0][1])]]
		self._DesignParameter['M1V1M2_CDNS_6375475055616_13'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='M1V1M2_CDNS_6375475055616_13In{}'.format(_Name)))[0]
		self._DesignParameter['M1V1M2_CDNS_6375475055616_13']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureY(**dict(_ViaMet12Met2NumberOfCOX=2, _ViaMet12Met2NumberOfCOY=1))
		self._DesignParameter['M1V1M2_CDNS_6375475055616_13']['_XYCoordinates'] = [[self._DesignParameter['PCCAM1_CDNS_6375475055654_12']['_XYCoordinates'][0][0], ((((self._DesignParameter['M2V2M3_CDNS_637547505561_1']['_XYCoordinates'][0][1] + self._DesignParameter['M2V2M3_CDNS_637547505561_1']['_DesignObj']._DesignParameter['_Met3Layer']['_XYCoordinates'][0][1]) + (self._DesignParameter['M2V2M3_CDNS_637547505561_1']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth'] / 2)) + drc._MetalxMinSpace2) + (self._DesignParameter['M1V1M2_CDNS_6375475055616_13']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] / 2))]]
		self._DesignParameter['M1V1M2_CDNS_6375475055616_12'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='M1V1M2_CDNS_6375475055616_12In{}'.format(_Name)))[0]
		self._DesignParameter['M1V1M2_CDNS_6375475055616_12']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureY(**dict(_ViaMet12Met2NumberOfCOX=2, _ViaMet12Met2NumberOfCOY=1))
		self._DesignParameter['M1V1M2_CDNS_6375475055616_12']['_XYCoordinates'] = [[self._DesignParameter['PCCAM1_CDNS_6375475055654_13']['_XYCoordinates'][0][0], ((((self._DesignParameter['M2V2M3_CDNS_637547505561_1']['_XYCoordinates'][0][1] + self._DesignParameter['M2V2M3_CDNS_637547505561_1']['_DesignObj']._DesignParameter['_Met3Layer']['_XYCoordinates'][0][1]) + (self._DesignParameter['M2V2M3_CDNS_637547505561_1']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth'] / 2)) + drc._MetalxMinSpace2) + (self._DesignParameter['M1V1M2_CDNS_6375475055616_13']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] / 2))]]
		self._DesignParameter['METAL2_path_35'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _Width=(drc._MetalxMinWidth * 2))
		self._DesignParameter['METAL2_path_35']['_XYCoordinates'] = [[[(+ self._DesignParameter['M1V1M2_CDNS_6375475055616_11']['_XYCoordinates'][0][0]), (+ self._DesignParameter['M1V1M2_CDNS_6375475055616_11']['_XYCoordinates'][0][1])], [self._DesignParameter['M1V1M2_CDNS_6375475055616_11']['_XYCoordinates'][0][0], ((self._DesignParameter['M1V1M2_CDNS_6375475055616_13']['_XYCoordinates'][0][1] + self._DesignParameter['M1V1M2_CDNS_6375475055616_13']['_DesignObj']._DesignParameter['_Met2Layer']['_XYCoordinates'][0][1]) - (self._DesignParameter['M1V1M2_CDNS_6375475055616_13']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] / 2))]]]
		self._DesignParameter['METAL2_path_34'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _Width=(drc._MetalxMinWidth * 2))
		self._DesignParameter['METAL2_path_34']['_XYCoordinates'] = [[[(+ self._DesignParameter['M1V1M2_CDNS_6375475055616_10']['_XYCoordinates'][0][0]), (+ self._DesignParameter['M1V1M2_CDNS_6375475055616_10']['_XYCoordinates'][0][1])], [self._DesignParameter['M1V1M2_CDNS_6375475055616_10']['_XYCoordinates'][0][0], ((self._DesignParameter['M1V1M2_CDNS_6375475055616_12']['_XYCoordinates'][0][1] + self._DesignParameter['M1V1M2_CDNS_6375475055616_12']['_DesignObj']._DesignParameter['_Met2Layer']['_XYCoordinates'][0][1]) - (self._DesignParameter['M1V1M2_CDNS_6375475055616_12']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] / 2))]]]
		self._DesignParameter['M3V3M4_CDNS_6375475055652_14'] = self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_Name='M3V3M4_CDNS_6375475055652_14In{}'.format(_Name)))[0]
		self._DesignParameter['M3V3M4_CDNS_6375475055652_14']['_DesignObj']._CalculateViaMet32Met4DesignParameterMinimumEnclosureX(**dict(_ViaMet32Met4NumberOfCOX=1, _ViaMet32Met4NumberOfCOY=2))
		self._DesignParameter['M3V3M4_CDNS_6375475055652_14']['_XYCoordinates'] = [[((((self._DesignParameter['METAL4_path_19']['_XYCoordinates'][0][0][0] - self._DesignParameter['METAL4_path_19']['_Width']) - drc._MetalxMinSpace5) - ((drc._MetalxMinWidth * 3) / 2)) + (self._DesignParameter['M3V3M4_CDNS_6375475055652_14']['_DesignObj']._DesignParameter['_Met4Layer']['_XWidth'] / 2)), ((self._DesignParameter['left_precharge_gate_vias']['_XYCoordinates'][0][1] + (self._DesignParameter['left_precharge_gate_vias']['_DesignObj']._DesignParameter['ViaMet22Met3']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth'] / 2)) + ((- self._DesignParameter['M3V3M4_CDNS_6375475055652_14']['_DesignObj']._DesignParameter['_Met4Layer']['_YWidth']) / 2))]]
		self._DesignParameter['METAL3_path_32'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0], _Datatype=DesignParameters._LayerMapping['METAL3'][1], _Width=(drc._MetalxMinWidth * 2))
		self._DesignParameter['METAL3_path_32']['_XYCoordinates'] = [[[(+ (((self._DesignParameter['left_precharge_gate_vias']['_XYCoordinates'][0][0] + self._DesignParameter['left_precharge_gate_vias']['_DesignObj']._DesignParameter['ViaMet22Met3']['_XYCoordinates'][0][0]) + self._DesignParameter['left_precharge_gate_vias']['_DesignObj']._DesignParameter['ViaMet22Met3']['_DesignObj']._DesignParameter['_Met3Layer']['_XYCoordinates'][0][0]) - (self._DesignParameter['left_precharge_gate_vias']['_DesignObj']._DesignParameter['ViaMet22Met3']['_DesignObj']._DesignParameter['_Met3Layer']['_XWidth'] / 2))), (((- self._DesignParameter['METAL3_path_32']['_Width']) / 2) + (((self._DesignParameter['left_precharge_gate_vias']['_XYCoordinates'][0][1] + self._DesignParameter['left_precharge_gate_vias']['_DesignObj']._DesignParameter['ViaMet22Met3']['_XYCoordinates'][0][1]) + self._DesignParameter['left_precharge_gate_vias']['_DesignObj']._DesignParameter['ViaMet22Met3']['_DesignObj']._DesignParameter['_Met3Layer']['_XYCoordinates'][0][1]) + (self._DesignParameter['left_precharge_gate_vias']['_DesignObj']._DesignParameter['ViaMet22Met3']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth'] / 2)))], [self._DesignParameter['M3V3M4_CDNS_6375475055652_14']['_XYCoordinates'][0][0], (((- self._DesignParameter['METAL3_path_32']['_Width']) / 2) + (((self._DesignParameter['left_precharge_gate_vias']['_XYCoordinates'][0][1] + self._DesignParameter['left_precharge_gate_vias']['_DesignObj']._DesignParameter['ViaMet22Met3']['_XYCoordinates'][0][1]) + self._DesignParameter['left_precharge_gate_vias']['_DesignObj']._DesignParameter['ViaMet22Met3']['_DesignObj']._DesignParameter['_Met3Layer']['_XYCoordinates'][0][1]) + (self._DesignParameter['left_precharge_gate_vias']['_DesignObj']._DesignParameter['ViaMet22Met3']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth'] / 2)))]]]
		self._DesignParameter['M3V3M4_CDNS_6375475055652_12'] = self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_Name='M3V3M4_CDNS_6375475055652_12In{}'.format(_Name)))[0]
		self._DesignParameter['M3V3M4_CDNS_6375475055652_12']['_DesignObj']._CalculateViaMet32Met4DesignParameterMinimumEnclosureX(**dict(_ViaMet32Met4NumberOfCOX=1, _ViaMet32Met4NumberOfCOY=2))
		self._DesignParameter['M3V3M4_CDNS_6375475055652_12']['_XYCoordinates'] = [[(((- self._DesignParameter['M3V3M4_CDNS_6375475055652_14']['_DesignObj']._DesignParameter['_Met4Layer']['_XWidth']) / 2) + (((self._DesignParameter['METAL4_path_18']['_XYCoordinates'][0][0][0] + self._DesignParameter['METAL4_path_18']['_Width']) + drc._MetalxMinSpace5) + ((drc._MetalxMinWidth * 3) / 2))), ((self._DesignParameter['left_precharge_gate_vias']['_XYCoordinates'][0][1] + (self._DesignParameter['left_precharge_gate_vias']['_DesignObj']._DesignParameter['ViaMet22Met3']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth'] / 2)) + ((- self._DesignParameter['M3V3M4_CDNS_6375475055652_14']['_DesignObj']._DesignParameter['_Met4Layer']['_YWidth']) / 2))]]
		self._DesignParameter['METAL3_path_31'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0], _Datatype=DesignParameters._LayerMapping['METAL3'][1], _Width=(drc._MetalxMinWidth * 2))
		self._DesignParameter['METAL3_path_31']['_XYCoordinates'] = [[[(+ (((self._DesignParameter['right_precharge_gate_vias']['_XYCoordinates'][0][0] + self._DesignParameter['right_precharge_gate_vias']['_DesignObj']._DesignParameter['ViaMet22Met3']['_XYCoordinates'][0][0]) + self._DesignParameter['right_precharge_gate_vias']['_DesignObj']._DesignParameter['ViaMet22Met3']['_DesignObj']._DesignParameter['_Met3Layer']['_XYCoordinates'][0][0]) + (self._DesignParameter['right_precharge_gate_vias']['_DesignObj']._DesignParameter['ViaMet22Met3']['_DesignObj']._DesignParameter['_Met3Layer']['_XWidth'] / 2))), (((- self._DesignParameter['METAL3_path_32']['_Width']) / 2) + (((self._DesignParameter['right_precharge_gate_vias']['_XYCoordinates'][0][1] + self._DesignParameter['right_precharge_gate_vias']['_DesignObj']._DesignParameter['ViaMet22Met3']['_XYCoordinates'][0][1]) + self._DesignParameter['right_precharge_gate_vias']['_DesignObj']._DesignParameter['ViaMet22Met3']['_DesignObj']._DesignParameter['_Met3Layer']['_XYCoordinates'][0][1]) + (self._DesignParameter['right_precharge_gate_vias']['_DesignObj']._DesignParameter['ViaMet22Met3']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth'] / 2)))], [self._DesignParameter['M3V3M4_CDNS_6375475055652_12']['_XYCoordinates'][0][0], (((- self._DesignParameter['METAL3_path_32']['_Width']) / 2) + (((self._DesignParameter['right_precharge_gate_vias']['_XYCoordinates'][0][1] + self._DesignParameter['right_precharge_gate_vias']['_DesignObj']._DesignParameter['ViaMet22Met3']['_XYCoordinates'][0][1]) + self._DesignParameter['right_precharge_gate_vias']['_DesignObj']._DesignParameter['ViaMet22Met3']['_DesignObj']._DesignParameter['_Met3Layer']['_XYCoordinates'][0][1]) + (self._DesignParameter['right_precharge_gate_vias']['_DesignObj']._DesignParameter['ViaMet22Met3']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth'] / 2)))]]]
		self._DesignParameter['M3V3M4_CDNS_6375475055652_13'] = self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_Name='M3V3M4_CDNS_6375475055652_13In{}'.format(_Name)))[0]
		self._DesignParameter['M3V3M4_CDNS_6375475055652_13']['_DesignObj']._CalculateViaMet32Met4DesignParameterMinimumEnclosureX(**dict(_ViaMet32Met4NumberOfCOX=1, _ViaMet32Met4NumberOfCOY=2))
		self._DesignParameter['M3V3M4_CDNS_6375475055652_13']['_XYCoordinates'] = [[self._DesignParameter['M3V3M4_CDNS_6375475055652_14']['_XYCoordinates'][0][0], ((((self._DesignParameter['nmos_bot_viastack']['_XYCoordinates'][0][1] + self._DesignParameter['nmos_bot_viastack']['_DesignObj']._DesignParameter['ViaMet22Met3']['_XYCoordinates'][0][1]) + self._DesignParameter['nmos_bot_viastack']['_DesignObj']._DesignParameter['ViaMet22Met3']['_DesignObj']._DesignParameter['_Met3Layer']['_XYCoordinates'][0][1]) - (self._DesignParameter['nmos_bot_viastack']['_DesignObj']._DesignParameter['ViaMet22Met3']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth'] / 2)) + (self._DesignParameter['M3V3M4_CDNS_6375475055652_13']['_DesignObj']._DesignParameter['_Met4Layer']['_YWidth'] / 2))]]
		self._DesignParameter['M3V3M4_CDNS_6375475055652_11'] = self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_Name='M3V3M4_CDNS_6375475055652_11In{}'.format(_Name)))[0]
		self._DesignParameter['M3V3M4_CDNS_6375475055652_11']['_DesignObj']._CalculateViaMet32Met4DesignParameterMinimumEnclosureX(**dict(_ViaMet32Met4NumberOfCOX=1, _ViaMet32Met4NumberOfCOY=2))
		self._DesignParameter['M3V3M4_CDNS_6375475055652_11']['_XYCoordinates'] = [[self._DesignParameter['M3V3M4_CDNS_6375475055652_12']['_XYCoordinates'][0][0], ((((self._DesignParameter['nmos_bot_viastack']['_XYCoordinates'][0][1] + self._DesignParameter['nmos_bot_viastack']['_DesignObj']._DesignParameter['ViaMet22Met3']['_XYCoordinates'][0][1]) + self._DesignParameter['nmos_bot_viastack']['_DesignObj']._DesignParameter['ViaMet22Met3']['_DesignObj']._DesignParameter['_Met3Layer']['_XYCoordinates'][0][1]) - (self._DesignParameter['nmos_bot_viastack']['_DesignObj']._DesignParameter['ViaMet22Met3']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth'] / 2)) + (self._DesignParameter['M3V3M4_CDNS_6375475055652_13']['_DesignObj']._DesignParameter['_Met4Layer']['_YWidth'] / 2))]]
		self._DesignParameter['METAL4_path_16'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL4'][0], _Datatype=DesignParameters._LayerMapping['METAL4'][1], _Width=(drc._MetalxMinWidth * 2))
		self._DesignParameter['METAL4_path_16']['_XYCoordinates'] = [[[(+ (self._DesignParameter['M3V3M4_CDNS_6375475055652_14']['_XYCoordinates'][0][0] + self._DesignParameter['M3V3M4_CDNS_6375475055652_14']['_DesignObj']._DesignParameter['_Met4Layer']['_XYCoordinates'][0][0])), (+ ((self._DesignParameter['M3V3M4_CDNS_6375475055652_14']['_XYCoordinates'][0][1] + self._DesignParameter['M3V3M4_CDNS_6375475055652_14']['_DesignObj']._DesignParameter['_Met4Layer']['_XYCoordinates'][0][1]) + (self._DesignParameter['M3V3M4_CDNS_6375475055652_14']['_DesignObj']._DesignParameter['_Met4Layer']['_YWidth'] / 2)))], [(+ (self._DesignParameter['M3V3M4_CDNS_6375475055652_13']['_XYCoordinates'][0][0] + self._DesignParameter['M3V3M4_CDNS_6375475055652_13']['_DesignObj']._DesignParameter['_Met4Layer']['_XYCoordinates'][0][0])), (+ ((self._DesignParameter['M3V3M4_CDNS_6375475055652_13']['_XYCoordinates'][0][1] + self._DesignParameter['M3V3M4_CDNS_6375475055652_13']['_DesignObj']._DesignParameter['_Met4Layer']['_XYCoordinates'][0][1]) - (self._DesignParameter['M3V3M4_CDNS_6375475055652_13']['_DesignObj']._DesignParameter['_Met4Layer']['_YWidth'] / 2)))]]]
		self._DesignParameter['METAL4_path_15'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL4'][0], _Datatype=DesignParameters._LayerMapping['METAL4'][1], _Width=(drc._MetalxMinWidth * 2))
		self._DesignParameter['METAL4_path_15']['_XYCoordinates'] = [[[(+ (self._DesignParameter['M3V3M4_CDNS_6375475055652_12']['_XYCoordinates'][0][0] + self._DesignParameter['M3V3M4_CDNS_6375475055652_12']['_DesignObj']._DesignParameter['_Met4Layer']['_XYCoordinates'][0][0])), (+ ((self._DesignParameter['M3V3M4_CDNS_6375475055652_12']['_XYCoordinates'][0][1] + self._DesignParameter['M3V3M4_CDNS_6375475055652_12']['_DesignObj']._DesignParameter['_Met4Layer']['_XYCoordinates'][0][1]) + (self._DesignParameter['M3V3M4_CDNS_6375475055652_12']['_DesignObj']._DesignParameter['_Met4Layer']['_YWidth'] / 2)))], [(+ (self._DesignParameter['M3V3M4_CDNS_6375475055652_11']['_XYCoordinates'][0][0] + self._DesignParameter['M3V3M4_CDNS_6375475055652_11']['_DesignObj']._DesignParameter['_Met4Layer']['_XYCoordinates'][0][0])), (+ ((self._DesignParameter['M3V3M4_CDNS_6375475055652_11']['_XYCoordinates'][0][1] + self._DesignParameter['M3V3M4_CDNS_6375475055652_11']['_DesignObj']._DesignParameter['_Met4Layer']['_XYCoordinates'][0][1]) - (self._DesignParameter['M3V3M4_CDNS_6375475055652_11']['_DesignObj']._DesignParameter['_Met4Layer']['_YWidth'] / 2)))]]]
		self._DesignParameter['METAL3_boundary_43'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0], _Datatype=DesignParameters._LayerMapping['METAL3'][1], _XWidth=max((((self._DesignParameter['M3V3M4_CDNS_6375475055652_11']['_XYCoordinates'][0][0] + self._DesignParameter['M3V3M4_CDNS_6375475055652_11']['_DesignObj']._DesignParameter['_Met4Layer']['_XYCoordinates'][0][0]) + (self._DesignParameter['M3V3M4_CDNS_6375475055652_11']['_DesignObj']._DesignParameter['_Met4Layer']['_XWidth'] / 2)) - ((self._DesignParameter['M3V3M4_CDNS_6375475055652_13']['_XYCoordinates'][0][0] + self._DesignParameter['M3V3M4_CDNS_6375475055652_13']['_DesignObj']._DesignParameter['_Met4Layer']['_XYCoordinates'][0][0]) - (self._DesignParameter['M3V3M4_CDNS_6375475055652_13']['_DesignObj']._DesignParameter['_Met4Layer']['_XWidth'] / 2))), self._DesignParameter['nmos_bot_viastack']['_DesignObj']._DesignParameter['ViaMet22Met3']['_DesignObj']._DesignParameter['_Met3Layer']['_XWidth']), _YWidth=(drc._MetalxMinWidth * 2))
		self._DesignParameter['METAL3_boundary_43']['_XYCoordinates'] = [[(+ ((self._DesignParameter['nmos_bot_viastack']['_XYCoordinates'][0][0] + self._DesignParameter['nmos_bot_viastack']['_DesignObj']._DesignParameter['ViaMet22Met3']['_XYCoordinates'][0][0]) + self._DesignParameter['nmos_bot_viastack']['_DesignObj']._DesignParameter['ViaMet22Met3']['_DesignObj']._DesignParameter['_Met3Layer']['_XYCoordinates'][0][0])), ((self._DesignParameter['METAL3_boundary_43']['_YWidth'] / 2) + (((self._DesignParameter['nmos_bot_viastack']['_XYCoordinates'][0][1] + self._DesignParameter['nmos_bot_viastack']['_DesignObj']._DesignParameter['ViaMet22Met3']['_XYCoordinates'][0][1]) + self._DesignParameter['nmos_bot_viastack']['_DesignObj']._DesignParameter['ViaMet22Met3']['_DesignObj']._DesignParameter['_Met3Layer']['_XYCoordinates'][0][1]) - (self._DesignParameter['nmos_bot_viastack']['_DesignObj']._DesignParameter['ViaMet22Met3']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth'] / 2)))]]
		self._DesignParameter['SLVT_boundary_23'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['SLVT'][0], _Datatype=DesignParameters._LayerMapping['SLVT'][1], _XWidth=(((self._DesignParameter['NMOS2InNMOSSetofSlicer_0']['_XYCoordinates'][0][0] + self._DesignParameter['NMOS2InNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_SLVTLayer']['_XYCoordinates'][0][0]) + (self._DesignParameter['NMOS2InNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_SLVTLayer']['_XWidth'] / 2)) - ((self._DesignParameter['NMOS1InNMOSSetofSlicer_0']['_XYCoordinates'][0][0] + self._DesignParameter['NMOS1InNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_SLVTLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['NMOS1InNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_SLVTLayer']['_XWidth'] / 2))), _YWidth=self._DesignParameter['NMOS1InNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_SLVTLayer']['_YWidth'])
		self._DesignParameter['SLVT_boundary_23']['_XYCoordinates'] = [[((((self._DesignParameter['NMOS2InNMOSSetofSlicer_0']['_XYCoordinates'][0][0] + self._DesignParameter['NMOS2InNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_SLVTLayer']['_XYCoordinates'][0][0]) + (self._DesignParameter['NMOS2InNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_SLVTLayer']['_XWidth'] / 2)) + ((self._DesignParameter['NMOS1InNMOSSetofSlicer_0']['_XYCoordinates'][0][0] + self._DesignParameter['NMOS1InNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_SLVTLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['NMOS1InNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_SLVTLayer']['_XWidth'] / 2))) / 2), (self._DesignParameter['NMOS2InNMOSSetofSlicer_0']['_XYCoordinates'][0][1] + self._DesignParameter['NMOS2InNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_SLVTLayer']['_XYCoordinates'][0][1])]]
		self._DesignParameter['SLVT_path_4'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['SLVT'][0], _Datatype=DesignParameters._LayerMapping['SLVT'][1], _Width=self._DesignParameter['nmos_bot']['_DesignObj']._DesignParameter['_SLVTLayer']['_XWidth'])
		self._DesignParameter['SLVT_path_4']['_XYCoordinates'] = [[[(+ self._DesignParameter['nmos_bot']['_XYCoordinates'][0][0]), (+ self._DesignParameter['nmos_bot']['_XYCoordinates'][0][1])], [self._DesignParameter['nmos_bot']['_XYCoordinates'][0][0], ((self._DesignParameter['NMOS3InNMOSSetofSlicer_0']['_XYCoordinates'][0][1] + self._DesignParameter['NMOS3InNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_SLVTLayer']['_XYCoordinates'][0][1]) + (self._DesignParameter['NMOS3InNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_SLVTLayer']['_YWidth'] / 2))]]]
		self._DesignParameter['SLVT_boundary_28'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['SLVT'][0], _Datatype=DesignParameters._LayerMapping['SLVT'][1], _XWidth=(((self._DesignParameter['PMOS2InPMOSSetofSlicer_0']['_XYCoordinates'][0][0] + self._DesignParameter['PMOS2InPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_SLVTLayer']['_XYCoordinates'][0][0]) + (self._DesignParameter['PMOS2InPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_SLVTLayer']['_XWidth'] / 2)) - ((self._DesignParameter['PMOS1InPMOSSetofSlicer_0']['_XYCoordinates'][0][0] + self._DesignParameter['PMOS1InPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_SLVTLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['PMOS1InPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_SLVTLayer']['_XWidth'] / 2))), _YWidth=self._DesignParameter['PMOS1InPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_SLVTLayer']['_YWidth'])
		self._DesignParameter['SLVT_boundary_28']['_XYCoordinates'] = [[self._DesignParameter['SLVT_boundary_23']['_XYCoordinates'][0][0], (self._DesignParameter['PMOS1InPMOSSetofSlicer_0']['_XYCoordinates'][0][1] + self._DesignParameter['PMOS1InPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_SLVTLayer']['_XYCoordinates'][0][1])]]
		self._DesignParameter['METAL1_boundary_354'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _XWidth=max(self._DesignParameter['M1V1M2_CDNS_6375475055616_13']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'], self._DesignParameter['PCCAM1_CDNS_6375475055654_12']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']), _YWidth=(max(((self._DesignParameter['M1V1M2_CDNS_6375475055616_13']['_XYCoordinates'][0][1] + self._DesignParameter['M1V1M2_CDNS_6375475055616_13']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) + (self._DesignParameter['M1V1M2_CDNS_6375475055616_13']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)), ((self._DesignParameter['PCCAM1_CDNS_6375475055654_12']['_XYCoordinates'][0][1] + self._DesignParameter['PCCAM1_CDNS_6375475055654_12']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) + (self._DesignParameter['PCCAM1_CDNS_6375475055654_12']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2))) - min(((self._DesignParameter['PCCAM1_CDNS_6375475055654_12']['_XYCoordinates'][0][1] + self._DesignParameter['PCCAM1_CDNS_6375475055654_12']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) - (self._DesignParameter['PCCAM1_CDNS_6375475055654_12']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)), ((self._DesignParameter['M1V1M2_CDNS_6375475055616_13']['_XYCoordinates'][0][1] + self._DesignParameter['M1V1M2_CDNS_6375475055616_13']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) - (self._DesignParameter['M1V1M2_CDNS_6375475055616_13']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)))))
		self._DesignParameter['METAL1_boundary_354']['_XYCoordinates'] = [[self._DesignParameter['PCCAM1_CDNS_6375475055654_12']['_XYCoordinates'][0][0], ((min(((self._DesignParameter['PCCAM1_CDNS_6375475055654_12']['_XYCoordinates'][0][1] + self._DesignParameter['PCCAM1_CDNS_6375475055654_12']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) - (self._DesignParameter['PCCAM1_CDNS_6375475055654_12']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)), ((self._DesignParameter['M1V1M2_CDNS_6375475055616_13']['_XYCoordinates'][0][1] + self._DesignParameter['M1V1M2_CDNS_6375475055616_13']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) - (self._DesignParameter['M1V1M2_CDNS_6375475055616_13']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2))) + max(((self._DesignParameter['M1V1M2_CDNS_6375475055616_13']['_XYCoordinates'][0][1] + self._DesignParameter['M1V1M2_CDNS_6375475055616_13']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) + (self._DesignParameter['M1V1M2_CDNS_6375475055616_13']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)), ((self._DesignParameter['PCCAM1_CDNS_6375475055654_12']['_XYCoordinates'][0][1] + self._DesignParameter['PCCAM1_CDNS_6375475055654_12']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) + (self._DesignParameter['PCCAM1_CDNS_6375475055654_12']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)))) / 2)]]
		self._DesignParameter['METAL1_boundary_353'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _XWidth=max(self._DesignParameter['M1V1M2_CDNS_6375475055616_13']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'], self._DesignParameter['PCCAM1_CDNS_6375475055654_12']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']), _YWidth=(max(((self._DesignParameter['M1V1M2_CDNS_6375475055616_13']['_XYCoordinates'][0][1] + self._DesignParameter['M1V1M2_CDNS_6375475055616_13']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) + (self._DesignParameter['M1V1M2_CDNS_6375475055616_13']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)), ((self._DesignParameter['PCCAM1_CDNS_6375475055654_12']['_XYCoordinates'][0][1] + self._DesignParameter['PCCAM1_CDNS_6375475055654_12']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) + (self._DesignParameter['PCCAM1_CDNS_6375475055654_12']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2))) - min(((self._DesignParameter['PCCAM1_CDNS_6375475055654_12']['_XYCoordinates'][0][1] + self._DesignParameter['PCCAM1_CDNS_6375475055654_12']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) - (self._DesignParameter['PCCAM1_CDNS_6375475055654_12']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)), ((self._DesignParameter['M1V1M2_CDNS_6375475055616_13']['_XYCoordinates'][0][1] + self._DesignParameter['M1V1M2_CDNS_6375475055616_13']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) - (self._DesignParameter['M1V1M2_CDNS_6375475055616_13']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)))))
		self._DesignParameter['METAL1_boundary_353']['_XYCoordinates'] = [[self._DesignParameter['PCCAM1_CDNS_6375475055654_13']['_XYCoordinates'][0][0], ((min(((self._DesignParameter['PCCAM1_CDNS_6375475055654_12']['_XYCoordinates'][0][1] + self._DesignParameter['PCCAM1_CDNS_6375475055654_12']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) - (self._DesignParameter['PCCAM1_CDNS_6375475055654_12']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)), ((self._DesignParameter['M1V1M2_CDNS_6375475055616_13']['_XYCoordinates'][0][1] + self._DesignParameter['M1V1M2_CDNS_6375475055616_13']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) - (self._DesignParameter['M1V1M2_CDNS_6375475055616_13']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2))) + max(((self._DesignParameter['M1V1M2_CDNS_6375475055616_13']['_XYCoordinates'][0][1] + self._DesignParameter['M1V1M2_CDNS_6375475055616_13']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) + (self._DesignParameter['M1V1M2_CDNS_6375475055616_13']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)), ((self._DesignParameter['PCCAM1_CDNS_6375475055654_12']['_XYCoordinates'][0][1] + self._DesignParameter['PCCAM1_CDNS_6375475055654_12']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) + (self._DesignParameter['PCCAM1_CDNS_6375475055654_12']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)))) / 2)]]
		self._DesignParameter['met224_stack_right'] = self._SrefElementDeclaration(_DesignObj=ViaStack._ViaStack(_Name='met224_stack_rightIn{}'.format(_Name)))[0]
		self._DesignParameter['met224_stack_right']['_DesignObj']._CalculateStackMinimumEnclosureY(**dict(COX=1, COY=2, start_layer=2, end_layer=4))
		self._DesignParameter['met224_stack_right']['_XYCoordinates'] = [[(((- self._DesignParameter['met224_stack_right']['_DesignObj']._DesignParameter['ViaMet32Met4']['_DesignObj']._DesignParameter['_Met4Layer']['_XWidth']) / 2) + self._DesignParameter['METAL4_path_18']['_XYCoordinates'][0][0][0]), ((((self._DesignParameter['M1V1M2_CDNS_6375475055616_12']['_XYCoordinates'][0][1] + self._DesignParameter['M1V1M2_CDNS_6375475055616_12']['_DesignObj']._DesignParameter['_Met2Layer']['_XYCoordinates'][0][1]) + (self._DesignParameter['M1V1M2_CDNS_6375475055616_12']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] / 2)) + drc._MetalxMinSpace3) + self._DesignParameter['met224_stack_right']['_DesignObj']._DesignParameter['ViaMet32Met4']['_DesignObj']._DesignParameter['_Met4Layer']['_YWidth'])]]
		self._DesignParameter['met224_stack_left'] = self._SrefElementDeclaration(_DesignObj=ViaStack._ViaStack(_Name='met224_stack_leftIn{}'.format(_Name)))[0]
		self._DesignParameter['met224_stack_left']['_DesignObj']._CalculateStackMinimumEnclosureY(**dict(COX=1, COY=2, start_layer=2, end_layer=4))
		self._DesignParameter['met224_stack_left']['_XYCoordinates'] = [[(self._DesignParameter['METAL4_path_19']['_XYCoordinates'][0][0][0] + (self._DesignParameter['met224_stack_left']['_DesignObj']._DesignParameter['ViaMet32Met4']['_DesignObj']._DesignParameter['_Met4Layer']['_XWidth'] / 2)), ((((self._DesignParameter['M1V1M2_CDNS_6375475055616_11']['_XYCoordinates'][0][1] + self._DesignParameter['M1V1M2_CDNS_6375475055616_11']['_DesignObj']._DesignParameter['_Met2Layer']['_XYCoordinates'][0][1]) - (self._DesignParameter['M1V1M2_CDNS_6375475055616_11']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] / 2)) - drc._MetalxMinSpace3) + (- self._DesignParameter['met224_stack_left']['_DesignObj']._DesignParameter['ViaMet32Met4']['_DesignObj']._DesignParameter['_Met4Layer']['_YWidth']))]]
		self._DesignParameter['METAL2_path_33'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _Width=(drc._MetalxMinWidth + drc._MetalxMinWidth))
		self._DesignParameter['METAL2_path_33']['_XYCoordinates'] = [[[(+ self._DesignParameter['met224_stack_left']['_XYCoordinates'][0][0]), (+ self._DesignParameter['met224_stack_left']['_XYCoordinates'][0][1])], [self._DesignParameter['METAL2_path_34']['_XYCoordinates'][0][0][0], self._DesignParameter['met224_stack_left']['_XYCoordinates'][0][1]]]]
		self._DesignParameter['METAL2_path_36'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _Width=(drc._MetalxMinWidth + drc._MetalxMinWidth))
		self._DesignParameter['METAL2_path_36']['_XYCoordinates'] = [[[(+ self._DesignParameter['met224_stack_right']['_XYCoordinates'][0][0]), (+ self._DesignParameter['met224_stack_right']['_XYCoordinates'][0][1])], [self._DesignParameter['METAL2_path_35']['_XYCoordinates'][0][0][0], self._DesignParameter['met224_stack_right']['_XYCoordinates'][0][1]]]]
		self._DesignParameter['GuardringInPMOSSetofSlicer_0']['_DesignObj']._CalculateDesignParameter(**dict(height=(((((self._DesignParameter['PMOS3InPMOSSetofSlicer_0']['_XYCoordinates'][0][1] + self._DesignParameter['PMOS3InPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) + (self._DesignParameter['PMOS3InPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)) + drc._Metal1MinSpace3) - (((self._DesignParameter['PCCAM1_CDNS_6375475055654_15']['_XYCoordinates'][0][1] + self._DesignParameter['PCCAM1_CDNS_6375475055654_15']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) - (self._DesignParameter['PCCAM1_CDNS_6375475055654_15']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)) - drc._MetalxMinSpace3)) + self._DesignParameter['GuardringInPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['top']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']), width=(((((self._DesignParameter['NMOS2InNMOSSetofSlicer_0']['_XYCoordinates'][0][0] + self._DesignParameter['NMOS2InNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_ODLayer']['_XYCoordinates'][0][0]) + (self._DesignParameter['NMOS2InNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth'] / 2)) + drc._OdMinSpace) + (- (((self._DesignParameter['NMOS1InNMOSSetofSlicer_0']['_XYCoordinates'][0][0] + self._DesignParameter['NMOS1InNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_ODLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['NMOS1InNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth'] / 2)) - drc._OdMinSpace))) + self._DesignParameter['GuardringInNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['right']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth']), contact=subring_option['via_num']))
		self._DesignParameter['GuardringInPMOSSetofSlicer_0']['_XYCoordinates'] = [[self._DesignParameter['GuardringInNMOSSetofSlicer_0']['_XYCoordinates'][0][0], (((((self._DesignParameter['PMOS3InPMOSSetofSlicer_0']['_XYCoordinates'][0][1] + self._DesignParameter['PMOS3InPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) + (self._DesignParameter['PMOS3InPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)) + drc._Metal1MinSpace3) + (((self._DesignParameter['PCCAM1_CDNS_6375475055654_15']['_XYCoordinates'][0][1] + self._DesignParameter['PCCAM1_CDNS_6375475055654_15']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) - (self._DesignParameter['PCCAM1_CDNS_6375475055654_15']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)) - drc._MetalxMinSpace3)) / 2)]]
		self._DesignParameter['PIMP_boundary_15'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['PIMP'][0], _Datatype=DesignParameters._LayerMapping['PIMP'][1], _XWidth=(((self._DesignParameter['PMOS2InPMOSSetofSlicer_0']['_XYCoordinates'][0][0] + self._DesignParameter['PMOS2InPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_PPLayer']['_XYCoordinates'][0][0]) + (self._DesignParameter['PMOS2InPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_PPLayer']['_XWidth'] / 2)) - ((self._DesignParameter['PMOS1InPMOSSetofSlicer_0']['_XYCoordinates'][0][0] + self._DesignParameter['PMOS1InPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_PPLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['PMOS1InPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_PPLayer']['_XWidth'] / 2))), _YWidth=self._DesignParameter['PMOS1InPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_PPLayer']['_YWidth'])
		self._DesignParameter['PIMP_boundary_15']['_XYCoordinates'] = [[((((self._DesignParameter['PMOS2InPMOSSetofSlicer_0']['_XYCoordinates'][0][0] + self._DesignParameter['PMOS2InPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_PPLayer']['_XYCoordinates'][0][0]) + (self._DesignParameter['PMOS2InPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_PPLayer']['_XWidth'] / 2)) + ((self._DesignParameter['PMOS1InPMOSSetofSlicer_0']['_XYCoordinates'][0][0] + self._DesignParameter['PMOS1InPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_PPLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['PMOS1InPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_PPLayer']['_XWidth'] / 2))) / 2), (self._DesignParameter['PMOS2InPMOSSetofSlicer_0']['_XYCoordinates'][0][1] + self._DesignParameter['PMOS2InPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_PPLayer']['_XYCoordinates'][0][1])]]
		self._DesignParameter['NWELL_boundary_2'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['NWELL'][0], _Datatype=DesignParameters._LayerMapping['NWELL'][1], _XWidth=(((self._DesignParameter['GuardringInPMOSSetofSlicer_0']['_XYCoordinates'][0][0] + self._DesignParameter['GuardringInPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['nw_right']['_XYCoordinates'][0][0]) + (self._DesignParameter['GuardringInPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['nw_right']['_XWidth'] / 2)) - ((self._DesignParameter['GuardringInPMOSSetofSlicer_0']['_XYCoordinates'][0][0] + self._DesignParameter['GuardringInPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['nw_left']['_XYCoordinates'][0][0]) - (self._DesignParameter['GuardringInPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['nw_left']['_XWidth'] / 2))), _YWidth=(((self._DesignParameter['GuardringInPMOSSetofSlicer_0']['_XYCoordinates'][0][1] + self._DesignParameter['GuardringInPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['nw_top']['_XYCoordinates'][0][1]) + (self._DesignParameter['GuardringInPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['nw_top']['_YWidth'] / 2)) - ((self._DesignParameter['GuardringInPMOSSetofSlicer_0']['_XYCoordinates'][0][1] + self._DesignParameter['GuardringInPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['nw_bot']['_XYCoordinates'][0][1]) - (self._DesignParameter['GuardringInPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['nw_bot']['_YWidth'] / 2))))
		self._DesignParameter['NWELL_boundary_2']['_XYCoordinates'] = [[(+ self._DesignParameter['GuardringInPMOSSetofSlicer_0']['_XYCoordinates'][0][0]), (+ self._DesignParameter['GuardringInPMOSSetofSlicer_0']['_XYCoordinates'][0][1])]]
		path_list = []
		if (len(self._DesignParameter['PMOS3InPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][(- 2)::(- 2)]) == 1):
		    mode = 'vertical'
		    _width = self._DesignParameter['PMOS3InPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
		elif (self._DesignParameter['PMOS3InPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][(- 2)::(- 2)][0][0] == self._DesignParameter['PMOS3InPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][(- 2)::(- 2)][(- 1)][0]):
		    mode = 'horizontal'
		    _width = self._DesignParameter['PMOS3InPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
		elif (self._DesignParameter['PMOS3InPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][(- 2)::(- 2)][0][1] == self._DesignParameter['PMOS3InPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][(- 2)::(- 2)][(- 1)][1]):
		    mode = 'vertical'
		    _width = self._DesignParameter['PMOS3InPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
		else:
		    print('Invalid Target Input')
		if (mode == 'vertical'):
		    xy_with_offset = []
		    target_y_value = [[(+ (self._DesignParameter['GuardringInPMOSSetofSlicer_0']['_XYCoordinates'][0][0] + self._DesignParameter['GuardringInPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['top']['_XYCoordinates'][0][0])), (+ (self._DesignParameter['GuardringInPMOSSetofSlicer_0']['_XYCoordinates'][0][1] + self._DesignParameter['GuardringInPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['top']['_XYCoordinates'][0][1]))]][0][1]
		    for element in self._DesignParameter['PMOS3InPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][(- 2)::(- 2)]:
		        xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['PMOS3InPMOSSetofSlicer_0']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['PMOS3InPMOSSetofSlicer_0']['_XYCoordinates'][0][1])], element)])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		elif (mode == 'horizontal'):
		    xy_with_offset = []
		    target_x_value = [[(+ (self._DesignParameter['GuardringInPMOSSetofSlicer_0']['_XYCoordinates'][0][0] + self._DesignParameter['GuardringInPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['top']['_XYCoordinates'][0][0])), (+ (self._DesignParameter['GuardringInPMOSSetofSlicer_0']['_XYCoordinates'][0][1] + self._DesignParameter['GuardringInPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['top']['_XYCoordinates'][0][1]))]][0][0]
		    for element in self._DesignParameter['PMOS3InPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][(- 2)::(- 2)]:
		        xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['PMOS3InPMOSSetofSlicer_0']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['PMOS3InPMOSSetofSlicer_0']['_XYCoordinates'][0][1])], element)])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		for i in range(len(path_list)):
		    path_list[i][0] = [(xy + offset) for (xy, offset) in zip(path_list[i][0], xy_offset)]
		self._DesignParameter['inner_left_pmos_supply'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=_width)
		self._DesignParameter['inner_left_pmos_supply']['_XYCoordinates'] = path_list
		path_list = []
		xy_offset = [0, 0]
		if (len(self._DesignParameter['PMOS4InPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates']) == 1):
		    mode = 'vertical'
		    _width = self._DesignParameter['PMOS4InPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
		elif (self._DesignParameter['PMOS4InPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0] == self._DesignParameter['PMOS4InPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][(- 1)][0]):
		    mode = 'horizontal'
		    _width = self._DesignParameter['PMOS4InPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
		elif (self._DesignParameter['PMOS4InPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1] == self._DesignParameter['PMOS4InPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][(- 1)][1]):
		    mode = 'vertical'
		    _width = self._DesignParameter['PMOS4InPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
		else:
		    print('Invalid Target Input')
		if (mode == 'vertical'):
		    xy_with_offset = []
		    target_y_value = [[(+ (self._DesignParameter['GuardringInPMOSSetofSlicer_0']['_XYCoordinates'][0][0] + self._DesignParameter['GuardringInPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['top']['_XYCoordinates'][0][0])), (+ (self._DesignParameter['GuardringInPMOSSetofSlicer_0']['_XYCoordinates'][0][1] + self._DesignParameter['GuardringInPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['top']['_XYCoordinates'][0][1]))]][0][1]
		    for i in range(len(self._DesignParameter['PMOS4InPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'])):
		        if ((i % 2) == 1):
		            xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['PMOS4InPMOSSetofSlicer_0']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['PMOS4InPMOSSetofSlicer_0']['_XYCoordinates'][0][1])], self._DesignParameter['PMOS4InPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		elif (mode == 'horizontal'):
		    xy_with_offset = []
		    target_x_value = [[(+ (self._DesignParameter['GuardringInPMOSSetofSlicer_0']['_XYCoordinates'][0][0] + self._DesignParameter['GuardringInPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['top']['_XYCoordinates'][0][0])), (+ (self._DesignParameter['GuardringInPMOSSetofSlicer_0']['_XYCoordinates'][0][1] + self._DesignParameter['GuardringInPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['top']['_XYCoordinates'][0][1]))]][0][0]
		    for i in range(len(self._DesignParameter['PMOS4InPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'])):
		        if ((i % 2) == 1):
		            xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['PMOS4InPMOSSetofSlicer_0']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['PMOS4InPMOSSetofSlicer_0']['_XYCoordinates'][0][1])], self._DesignParameter['PMOS4InPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		for i in range(len(path_list)):
		    path_list[i][0] = [(xy + offset) for (xy, offset) in zip(path_list[i][0], xy_offset)]
		self._DesignParameter['inner_right_pmos_supply'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=_width)
		self._DesignParameter['inner_right_pmos_supply']['_XYCoordinates'] = path_list
		path_list = []
		xy_offset = [0, 0]
		if (len(self._DesignParameter['PMOS2InPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates']) == 1):
		    mode = 'vertical'
		    _width = self._DesignParameter['PMOS2InPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
		elif (self._DesignParameter['PMOS2InPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0] == self._DesignParameter['PMOS2InPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][(- 1)][0]):
		    mode = 'horizontal'
		    _width = self._DesignParameter['PMOS2InPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
		elif (self._DesignParameter['PMOS2InPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1] == self._DesignParameter['PMOS2InPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][(- 1)][1]):
		    mode = 'vertical'
		    _width = self._DesignParameter['PMOS2InPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
		else:
		    print('Invalid Target Input')
		if (mode == 'vertical'):
		    xy_with_offset = []
		    target_y_value = [[(+ (self._DesignParameter['GuardringInPMOSSetofSlicer_0']['_XYCoordinates'][0][0] + self._DesignParameter['GuardringInPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['top']['_XYCoordinates'][0][0])), (+ (self._DesignParameter['GuardringInPMOSSetofSlicer_0']['_XYCoordinates'][0][1] + self._DesignParameter['GuardringInPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['top']['_XYCoordinates'][0][1]))]][0][1]
		    for i in range(len(self._DesignParameter['PMOS2InPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'])):
		        if ((i % 2) == 1):
		            xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['PMOS2InPMOSSetofSlicer_0']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['PMOS2InPMOSSetofSlicer_0']['_XYCoordinates'][0][1])], self._DesignParameter['PMOS2InPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		elif (mode == 'horizontal'):
		    xy_with_offset = []
		    target_x_value = [[(+ (self._DesignParameter['GuardringInPMOSSetofSlicer_0']['_XYCoordinates'][0][0] + self._DesignParameter['GuardringInPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['top']['_XYCoordinates'][0][0])), (+ (self._DesignParameter['GuardringInPMOSSetofSlicer_0']['_XYCoordinates'][0][1] + self._DesignParameter['GuardringInPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['top']['_XYCoordinates'][0][1]))]][0][0]
		    for i in range(len(self._DesignParameter['PMOS2InPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'])):
		        if ((i % 2) == 1):
		            xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['PMOS2InPMOSSetofSlicer_0']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['PMOS2InPMOSSetofSlicer_0']['_XYCoordinates'][0][1])], self._DesignParameter['PMOS2InPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		for i in range(len(path_list)):
		    path_list[i][0] = [(xy + offset) for (xy, offset) in zip(path_list[i][0], xy_offset)]
		self._DesignParameter['precharge_right_pmos_supply'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=_width)
		self._DesignParameter['precharge_right_pmos_supply']['_XYCoordinates'] = path_list
		self._DesignParameter['VDD_viastack'] = self._SrefElementDeclaration(_DesignObj=ViaStack._ViaStack(_Name='VDD_viastackIn{}'.format(_Name)))[0]
		self._DesignParameter['VDD_viastack']['_DesignObj']._CalculateStackMinimumEnclosureY(**dict(COX=max(1, (1 + int((((self._DesignParameter['GuardringInPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['met_top']['_XWidth'] - drc._VIAxMinSpace2) - (2 * drc._VIAxMinEnclosureByMetx)) / (drc._VIAxMinWidth + drc._VIAxMinSpace2))))), COY=subring_option['via_num'], start_layer=1, end_layer=3))
		self._DesignParameter['VDD_viastack']['_XYCoordinates'] = [[(+ (self._DesignParameter['GuardringInPMOSSetofSlicer_0']['_XYCoordinates'][0][0] + self._DesignParameter['GuardringInPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['top']['_XYCoordinates'][0][0])), (+ (self._DesignParameter['GuardringInPMOSSetofSlicer_0']['_XYCoordinates'][0][1] + self._DesignParameter['GuardringInPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['top']['_XYCoordinates'][0][1]))]]
		path_list = []
		xy_offset = [0, 0]
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
		    target_y_value = [[(+ (self._DesignParameter['GuardringInNMOSSetofSlicer_0']['_XYCoordinates'][0][0] + self._DesignParameter['GuardringInNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['bot']['_XYCoordinates'][0][0])), (+ (self._DesignParameter['GuardringInNMOSSetofSlicer_0']['_XYCoordinates'][0][1] + self._DesignParameter['GuardringInNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['bot']['_XYCoordinates'][0][1]))]][0][1]
		    for i in range(len(self._DesignParameter['nmos_bot']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'])):
		        if ((i % 2) == 1):
		            xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['nmos_bot']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['nmos_bot']['_XYCoordinates'][0][1])], self._DesignParameter['nmos_bot']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		elif (mode == 'horizontal'):
		    xy_with_offset = []
		    target_x_value = [[(+ (self._DesignParameter['GuardringInNMOSSetofSlicer_0']['_XYCoordinates'][0][0] + self._DesignParameter['GuardringInNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['bot']['_XYCoordinates'][0][0])), (+ (self._DesignParameter['GuardringInNMOSSetofSlicer_0']['_XYCoordinates'][0][1] + self._DesignParameter['GuardringInNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['bot']['_XYCoordinates'][0][1]))]][0][0]
		    for i in range(len(self._DesignParameter['nmos_bot']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'])):
		        if ((i % 2) == 1):
		            xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['nmos_bot']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['nmos_bot']['_XYCoordinates'][0][1])], self._DesignParameter['nmos_bot']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		for i in range(len(path_list)):
		    path_list[i][0] = [(xy + offset) for (xy, offset) in zip(path_list[i][0], xy_offset)]
		self._DesignParameter['NMOS_bot_supply'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=_width)
		self._DesignParameter['NMOS_bot_supply']['_XYCoordinates'] = path_list
		self._DesignParameter['GuardringInSlicer_0'] = self._SrefElementDeclaration(_DesignObj=PSubRing.PSubRing(_Name='GuardringInSlicer_0In{}'.format(_Name)))[0]
		self._DesignParameter['GuardringInSlicer_0']['_DesignObj']._CalculateDesignParameter(**dict(height=((((((self._DesignParameter['GuardringInPMOSSetofSlicer_0']['_XYCoordinates'][0][1] + self._DesignParameter['GuardringInPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['nw_top']['_XYCoordinates'][0][1]) + (self._DesignParameter['GuardringInPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['nw_top']['_YWidth'] / 2)) - (((self._DesignParameter['GuardringInNMOSSetofSlicer_0']['_XYCoordinates'][0][1] + self._DesignParameter['GuardringInNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['bot']['_XYCoordinates'][0][1]) + self._DesignParameter['GuardringInNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['bot']['_DesignObj']._DesignParameter['_PPLayer']['_XYCoordinates'][0][1]) - (self._DesignParameter['GuardringInNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['bot']['_DesignObj']._DesignParameter['_PPLayer']['_YWidth'] / 2))) + (drc._NwMinSpacetoNactive + drc._PpMinSpace)) + self._DesignParameter['GuardringInNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['top']['_DesignObj']._DesignParameter['_PPLayer']['_YWidth']) + subring_option['additional_outer_height']), contact=subring_option['via_num'], width=(self._DesignParameter['GuardringInNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['right']['_DesignObj']._DesignParameter['_PPLayer']['_XWidth'] + max(((((self._DesignParameter['GuardringInPMOSSetofSlicer_0']['_XYCoordinates'][0][0] + self._DesignParameter['GuardringInPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['nw_right']['_XYCoordinates'][0][0]) + (self._DesignParameter['GuardringInPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['nw_right']['_XWidth'] / 2)) - ((self._DesignParameter['GuardringInPMOSSetofSlicer_0']['_XYCoordinates'][0][0] + self._DesignParameter['GuardringInPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['nw_left']['_XYCoordinates'][0][0]) - (self._DesignParameter['GuardringInPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['nw_left']['_XWidth'] / 2))) + (drc._NwMinSpacetoNactive * 2)), (((((self._DesignParameter['GuardringInNMOSSetofSlicer_0']['_XYCoordinates'][0][0] + self._DesignParameter['GuardringInNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['right']['_XYCoordinates'][0][0]) + self._DesignParameter['GuardringInNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['right']['_DesignObj']._DesignParameter['_PPLayer']['_XYCoordinates'][0][0]) + (self._DesignParameter['GuardringInNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['right']['_DesignObj']._DesignParameter['_PPLayer']['_XWidth'] / 2)) - (((self._DesignParameter['GuardringInNMOSSetofSlicer_0']['_XYCoordinates'][0][0] + self._DesignParameter['GuardringInNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['left']['_XYCoordinates'][0][0]) + self._DesignParameter['GuardringInNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['left']['_DesignObj']._DesignParameter['_PPLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['GuardringInNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['left']['_DesignObj']._DesignParameter['_PPLayer']['_XWidth'] / 2))) + (drc._PpMinSpace * 2))))))
		self._DesignParameter['GuardringInSlicer_0']['_XYCoordinates'] = [[self._DesignParameter['GuardringInNMOSSetofSlicer_0']['_XYCoordinates'][0][0], ((((((self._DesignParameter['GuardringInPMOSSetofSlicer_0']['_XYCoordinates'][0][1] + self._DesignParameter['GuardringInPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['nw_top']['_XYCoordinates'][0][1]) + (self._DesignParameter['GuardringInPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['nw_top']['_YWidth'] / 2)) + drc._NwMinSpacetoNactive) + (((self._DesignParameter['GuardringInNMOSSetofSlicer_0']['_XYCoordinates'][0][1] + self._DesignParameter['GuardringInNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['bot']['_XYCoordinates'][0][1]) + self._DesignParameter['GuardringInNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['bot']['_DesignObj']._DesignParameter['_PPLayer']['_XYCoordinates'][0][1]) - (self._DesignParameter['GuardringInNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['bot']['_DesignObj']._DesignParameter['_PPLayer']['_YWidth'] / 2))) - drc._PpMinSpace) / 2)]]
		self._DesignParameter['VSS_viastack_1to3'] = self._SrefElementDeclaration(_DesignObj=ViaStack._ViaStack(_Name='VSS_viastack_1to3In{}'.format(_Name)))[0]
		self._DesignParameter['VSS_viastack_1to3']['_DesignObj']._CalculateStackMinimumEnclosureY(**dict(COX=(max(1, (1 + int(((((((self._DesignParameter['GuardringInSlicer_0']['_XYCoordinates'][0][0] + self._DesignParameter['GuardringInSlicer_0']['_DesignObj']._DesignParameter['met_right']['_XYCoordinates'][0][0]) + (self._DesignParameter['GuardringInSlicer_0']['_DesignObj']._DesignParameter['met_right']['_XWidth'] / 2)) - ((self._DesignParameter['GuardringInSlicer_0']['_XYCoordinates'][0][0] + self._DesignParameter['GuardringInSlicer_0']['_DesignObj']._DesignParameter['met_left']['_XYCoordinates'][0][0]) - (self._DesignParameter['GuardringInSlicer_0']['_DesignObj']._DesignParameter['met_left']['_XWidth'] / 2))) - drc._VIAxMinSpace2) - (2 * drc._VIAxMinEnclosureByMetx)) / (drc._VIAxMinWidth + drc._VIAxMinSpace2))))) - 1), COY=max(1, (1 + int(((((((self._DesignParameter['GuardringInNMOSSetofSlicer_0']['_XYCoordinates'][0][1] + self._DesignParameter['GuardringInNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['met_bot']['_XYCoordinates'][0][1]) + (self._DesignParameter['GuardringInNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['met_bot']['_YWidth'] / 2)) - ((self._DesignParameter['GuardringInSlicer_0']['_XYCoordinates'][0][1] + self._DesignParameter['GuardringInSlicer_0']['_DesignObj']._DesignParameter['met_bot']['_XYCoordinates'][0][1]) - (self._DesignParameter['GuardringInSlicer_0']['_DesignObj']._DesignParameter['met_bot']['_YWidth'] / 2))) - drc._VIAxMinSpace2) - (2 * drc._VIAxMinEnclosureByMetx)) / (drc._VIAxMinWidth + drc._VIAxMinSpace2))))), start_layer=1, end_layer=3))
		self._DesignParameter['VSS_viastack_1to3']['_XYCoordinates'] = [[((((self._DesignParameter['GuardringInSlicer_0']['_XYCoordinates'][0][0] + self._DesignParameter['GuardringInSlicer_0']['_DesignObj']._DesignParameter['met_right']['_XYCoordinates'][0][0]) + (self._DesignParameter['GuardringInSlicer_0']['_DesignObj']._DesignParameter['met_right']['_XWidth'] / 2)) + ((self._DesignParameter['GuardringInSlicer_0']['_XYCoordinates'][0][0] + self._DesignParameter['GuardringInSlicer_0']['_DesignObj']._DesignParameter['met_left']['_XYCoordinates'][0][0]) - (self._DesignParameter['GuardringInSlicer_0']['_DesignObj']._DesignParameter['met_left']['_XWidth'] / 2))) / 2), ((((self._DesignParameter['GuardringInNMOSSetofSlicer_0']['_XYCoordinates'][0][1] + self._DesignParameter['GuardringInNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['met_bot']['_XYCoordinates'][0][1]) + (self._DesignParameter['GuardringInNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['met_bot']['_YWidth'] / 2)) + ((self._DesignParameter['GuardringInSlicer_0']['_XYCoordinates'][0][1] + self._DesignParameter['GuardringInSlicer_0']['_DesignObj']._DesignParameter['met_bot']['_XYCoordinates'][0][1]) - (self._DesignParameter['GuardringInSlicer_0']['_DesignObj']._DesignParameter['met_bot']['_YWidth'] / 2))) / 2)]]
		self._DesignParameter['METAL1_boundary_356'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _XWidth=(((self._DesignParameter['GuardringInSlicer_0']['_XYCoordinates'][0][0] + self._DesignParameter['GuardringInSlicer_0']['_DesignObj']._DesignParameter['met_right']['_XYCoordinates'][0][0]) + (self._DesignParameter['GuardringInSlicer_0']['_DesignObj']._DesignParameter['met_right']['_XWidth'] / 2)) - ((self._DesignParameter['GuardringInSlicer_0']['_XYCoordinates'][0][0] + self._DesignParameter['GuardringInSlicer_0']['_DesignObj']._DesignParameter['met_left']['_XYCoordinates'][0][0]) - (self._DesignParameter['GuardringInSlicer_0']['_DesignObj']._DesignParameter['met_left']['_XWidth'] / 2))), _YWidth=(((self._DesignParameter['GuardringInNMOSSetofSlicer_0']['_XYCoordinates'][0][1] + self._DesignParameter['GuardringInNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['met_bot']['_XYCoordinates'][0][1]) + (self._DesignParameter['GuardringInNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['met_bot']['_YWidth'] / 2)) - ((self._DesignParameter['GuardringInSlicer_0']['_XYCoordinates'][0][1] + self._DesignParameter['GuardringInSlicer_0']['_DesignObj']._DesignParameter['met_bot']['_XYCoordinates'][0][1]) - (self._DesignParameter['GuardringInSlicer_0']['_DesignObj']._DesignParameter['met_bot']['_YWidth'] / 2))))
		self._DesignParameter['METAL1_boundary_356']['_XYCoordinates'] = [[(+ self._DesignParameter['VSS_viastack_1to3']['_XYCoordinates'][0][0]), (+ self._DesignParameter['VSS_viastack_1to3']['_XYCoordinates'][0][1])]]
		self._DesignParameter['METAL2_boundary_46'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _XWidth=(((self._DesignParameter['GuardringInSlicer_0']['_XYCoordinates'][0][0] + self._DesignParameter['GuardringInSlicer_0']['_DesignObj']._DesignParameter['met_right']['_XYCoordinates'][0][0]) + (self._DesignParameter['GuardringInSlicer_0']['_DesignObj']._DesignParameter['met_right']['_XWidth'] / 2)) - ((self._DesignParameter['GuardringInSlicer_0']['_XYCoordinates'][0][0] + self._DesignParameter['GuardringInSlicer_0']['_DesignObj']._DesignParameter['met_left']['_XYCoordinates'][0][0]) - (self._DesignParameter['GuardringInSlicer_0']['_DesignObj']._DesignParameter['met_left']['_XWidth'] / 2))), _YWidth=(((self._DesignParameter['GuardringInNMOSSetofSlicer_0']['_XYCoordinates'][0][1] + self._DesignParameter['GuardringInNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['met_bot']['_XYCoordinates'][0][1]) + (self._DesignParameter['GuardringInNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['met_bot']['_YWidth'] / 2)) - ((self._DesignParameter['GuardringInSlicer_0']['_XYCoordinates'][0][1] + self._DesignParameter['GuardringInSlicer_0']['_DesignObj']._DesignParameter['met_bot']['_XYCoordinates'][0][1]) - (self._DesignParameter['GuardringInSlicer_0']['_DesignObj']._DesignParameter['met_bot']['_YWidth'] / 2))))
		self._DesignParameter['METAL2_boundary_46']['_XYCoordinates'] = [[(+ self._DesignParameter['VSS_viastack_1to3']['_XYCoordinates'][0][0]), (+ self._DesignParameter['VSS_viastack_1to3']['_XYCoordinates'][0][1])]]
		self._DesignParameter['METAL3_boundary_41'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0], _Datatype=DesignParameters._LayerMapping['METAL3'][1], _XWidth=(((self._DesignParameter['GuardringInSlicer_0']['_XYCoordinates'][0][0] + self._DesignParameter['GuardringInSlicer_0']['_DesignObj']._DesignParameter['met_right']['_XYCoordinates'][0][0]) + (self._DesignParameter['GuardringInSlicer_0']['_DesignObj']._DesignParameter['met_right']['_XWidth'] / 2)) - ((self._DesignParameter['GuardringInSlicer_0']['_XYCoordinates'][0][0] + self._DesignParameter['GuardringInSlicer_0']['_DesignObj']._DesignParameter['met_left']['_XYCoordinates'][0][0]) - (self._DesignParameter['GuardringInSlicer_0']['_DesignObj']._DesignParameter['met_left']['_XWidth'] / 2))), _YWidth=(((self._DesignParameter['GuardringInNMOSSetofSlicer_0']['_XYCoordinates'][0][1] + self._DesignParameter['GuardringInNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['met_bot']['_XYCoordinates'][0][1]) + (self._DesignParameter['GuardringInNMOSSetofSlicer_0']['_DesignObj']._DesignParameter['met_bot']['_YWidth'] / 2)) - ((self._DesignParameter['GuardringInSlicer_0']['_XYCoordinates'][0][1] + self._DesignParameter['GuardringInSlicer_0']['_DesignObj']._DesignParameter['met_bot']['_XYCoordinates'][0][1]) - (self._DesignParameter['GuardringInSlicer_0']['_DesignObj']._DesignParameter['met_bot']['_YWidth'] / 2))))
		self._DesignParameter['METAL3_boundary_41']['_XYCoordinates'] = [[(+ self._DesignParameter['VSS_viastack_1to3']['_XYCoordinates'][0][0]), (+ self._DesignParameter['VSS_viastack_1to3']['_XYCoordinates'][0][1])]]
		self._DesignParameter['SSn'] = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1PIN'][0], _Datatype=DesignParameters._LayerMapping['METAL1PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0], _XYCoordinates=[[(+ self._DesignParameter['pmos_inner_left_via2to4']['_XYCoordinates'][0][0]), (+ self._DesignParameter['pmos_inner_left_via2to4']['_XYCoordinates'][0][1])]], _Mag=0.1, _Angle=0, _TEXT='SSn')
		self._DesignParameter['SSp'] = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1PIN'][0], _Datatype=DesignParameters._LayerMapping['METAL1PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0], _XYCoordinates=[[(+ self._DesignParameter['pmos_inner_right_via2to4']['_XYCoordinates'][0][0]), (+ self._DesignParameter['pmos_inner_right_via2to4']['_XYCoordinates'][0][1])]], _Mag=0.1, _Angle=0, _TEXT='SSp')
		self._DesignParameter['VDD_pin'] = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1PIN'][0], _Datatype=DesignParameters._LayerMapping['METAL1PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0], _XYCoordinates=[[(+ self._DesignParameter['VDD_viastack']['_XYCoordinates'][0][0]), (+ self._DesignParameter['VDD_viastack']['_XYCoordinates'][0][1])]], _Mag=0.1, _Angle=0, _TEXT='VDD')
		self._DesignParameter['INp'] = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1PIN'][0], _Datatype=DesignParameters._LayerMapping['METAL1PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0], _XYCoordinates=[[(+ self._DesignParameter['pccam_nmos_left']['_XYCoordinates'][0][0]), (+ self._DesignParameter['pccam_nmos_left']['_XYCoordinates'][0][1])]], _Mag=0.1, _Angle=0, _TEXT='INp')
		self._DesignParameter['INn'] = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1PIN'][0], _Datatype=DesignParameters._LayerMapping['METAL1PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0], _XYCoordinates=[[(+ self._DesignParameter['pccam_nmos_right']['_XYCoordinates'][0][0]), (+ self._DesignParameter['pccam_nmos_right']['_XYCoordinates'][0][1])]], _Mag=0.1, _Angle=0, _TEXT='INn')
		self._DesignParameter['VSS_pin'] = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1PIN'][0], _Datatype=DesignParameters._LayerMapping['METAL1PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0], _XYCoordinates=[[(+ self._DesignParameter['VSS_viastack_1to3']['_XYCoordinates'][0][0]), (+ self._DesignParameter['VSS_viastack_1to3']['_XYCoordinates'][0][1])]], _Mag=0.1, _Angle=0, _TEXT='VSS')
		self._DesignParameter['CLK'] = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1PIN'][0], _Datatype=DesignParameters._LayerMapping['METAL1PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0], _XYCoordinates=[[(+ self._DesignParameter['nmos_bot_viastack']['_XYCoordinates'][0][0]), (+ self._DesignParameter['nmos_bot_viastack']['_XYCoordinates'][0][1])], [(+ self._DesignParameter['right_precharge_gate_vias']['_XYCoordinates'][0][0]), (+ self._DesignParameter['right_precharge_gate_vias']['_XYCoordinates'][0][1])], [(+ self._DesignParameter['left_precharge_gate_vias']['_XYCoordinates'][0][0]), (+ self._DesignParameter['left_precharge_gate_vias']['_XYCoordinates'][0][1])]], _Mag=0.1, _Angle=0, _TEXT='CLK')
		path_list = []
		xy_offset = [0, 0]
		if (len(self._DesignParameter['nmos_left_drain']['_XYCoordinates']) == 1):
		    mode = 'vertical'
		    _width = self._DesignParameter['nmos_left_drain']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth']
		elif (self._DesignParameter['nmos_left_drain']['_XYCoordinates'][0][0] == self._DesignParameter['nmos_left_drain']['_XYCoordinates'][(- 1)][0]):
		    mode = 'horizontal'
		    _width = self._DesignParameter['nmos_left_drain']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth']
		elif (self._DesignParameter['nmos_left_drain']['_XYCoordinates'][0][1] == self._DesignParameter['nmos_left_drain']['_XYCoordinates'][(- 1)][1]):
		    mode = 'vertical'
		    _width = self._DesignParameter['nmos_left_drain']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth']
		else:
		    print('Invalid Target Input')
		if (mode == 'vertical'):
		    xy_with_offset = []
		    target_y_value = [[(+ self._DesignParameter['M2V2M3_CDNS_637547505561_1']['_XYCoordinates'][0][0]), (+ self._DesignParameter['M2V2M3_CDNS_637547505561_1']['_XYCoordinates'][0][1])]][0][1]
		    for i in range(len(self._DesignParameter['nmos_left_drain']['_XYCoordinates'])):
		        xy_with_offset.append([(x + y) for (x, y) in zip([0, 0], self._DesignParameter['nmos_left_drain']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		elif (mode == 'horizontal'):
		    xy_with_offset = []
		    target_x_value = [[(+ self._DesignParameter['M2V2M3_CDNS_637547505561_1']['_XYCoordinates'][0][0]), (+ self._DesignParameter['M2V2M3_CDNS_637547505561_1']['_XYCoordinates'][0][1])]][0][0]
		    for i in range(len(self._DesignParameter['nmos_left_drain']['_XYCoordinates'])):
		        xy_with_offset.append([(x + y) for (x, y) in zip([0, 0], self._DesignParameter['nmos_left_drain']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		for i in range(len(path_list)):
		    path_list[i][0] = [(xy + offset) for (xy, offset) in zip(path_list[i][0], xy_offset)]
		self._DesignParameter['left_nmos_drain_met2'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _Width=_width)
		self._DesignParameter['left_nmos_drain_met2']['_XYCoordinates'] = path_list
		path_list = []
		xy_offset = [0, 0]
		if (len(self._DesignParameter['nmos_left_source']['_XYCoordinates']) == 1):
		    mode = 'vertical'
		    _width = self._DesignParameter['nmos_left_source']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth']
		elif (self._DesignParameter['nmos_left_source']['_XYCoordinates'][0][0] == self._DesignParameter['nmos_left_source']['_XYCoordinates'][(- 1)][0]):
		    mode = 'horizontal'
		    _width = self._DesignParameter['nmos_left_source']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth']
		elif (self._DesignParameter['nmos_left_source']['_XYCoordinates'][0][1] == self._DesignParameter['nmos_left_source']['_XYCoordinates'][(- 1)][1]):
		    mode = 'vertical'
		    _width = self._DesignParameter['nmos_left_source']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth']
		else:
		    print('Invalid Target Input')
		if (mode == 'vertical'):
		    xy_with_offset = []
		    target_y_value = [[(+ self._DesignParameter['nmos_center_via_stack_2to4']['_XYCoordinates'][0][0]), (+ self._DesignParameter['nmos_center_via_stack_2to4']['_XYCoordinates'][0][1])]][0][1]
		    for i in range(len(self._DesignParameter['nmos_left_source']['_XYCoordinates'])):
		        xy_with_offset.append([(x + y) for (x, y) in zip([0, 0], self._DesignParameter['nmos_left_source']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		elif (mode == 'horizontal'):
		    xy_with_offset = []
		    target_x_value = [[(+ self._DesignParameter['nmos_center_via_stack_2to4']['_XYCoordinates'][0][0]), (+ self._DesignParameter['nmos_center_via_stack_2to4']['_XYCoordinates'][0][1])]][0][0]
		    for i in range(len(self._DesignParameter['nmos_left_source']['_XYCoordinates'])):
		        xy_with_offset.append([(x + y) for (x, y) in zip([0, 0], self._DesignParameter['nmos_left_source']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		for i in range(len(path_list)):
		    path_list[i][0] = [(xy + offset) for (xy, offset) in zip(path_list[i][0], xy_offset)]
		self._DesignParameter['left_nmos_source_met2'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _Width=_width)
		self._DesignParameter['left_nmos_source_met2']['_XYCoordinates'] = path_list
		path_list = []
		xy_offset = [0, 0]
		if (len(self._DesignParameter['nmos_right_drain']['_XYCoordinates']) == 1):
		    mode = 'vertical'
		    _width = self._DesignParameter['nmos_right_drain']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth']
		elif (self._DesignParameter['nmos_right_drain']['_XYCoordinates'][0][0] == self._DesignParameter['nmos_right_drain']['_XYCoordinates'][(- 1)][0]):
		    mode = 'horizontal'
		    _width = self._DesignParameter['nmos_right_drain']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth']
		elif (self._DesignParameter['nmos_right_drain']['_XYCoordinates'][0][1] == self._DesignParameter['nmos_right_drain']['_XYCoordinates'][(- 1)][1]):
		    mode = 'vertical'
		    _width = self._DesignParameter['nmos_right_drain']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth']
		else:
		    print('Invalid Target Input')
		if (mode == 'vertical'):
		    xy_with_offset = []
		    target_y_value = [[(+ self._DesignParameter['M2V2M3_CDNS_637547505561_0']['_XYCoordinates'][0][0]), (+ self._DesignParameter['M2V2M3_CDNS_637547505561_0']['_XYCoordinates'][0][1])]][0][1]
		    for i in range(len(self._DesignParameter['nmos_right_drain']['_XYCoordinates'])):
		        xy_with_offset.append([(x + y) for (x, y) in zip([0, 0], self._DesignParameter['nmos_right_drain']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		elif (mode == 'horizontal'):
		    xy_with_offset = []
		    target_x_value = [[(+ self._DesignParameter['M2V2M3_CDNS_637547505561_0']['_XYCoordinates'][0][0]), (+ self._DesignParameter['M2V2M3_CDNS_637547505561_0']['_XYCoordinates'][0][1])]][0][0]
		    for i in range(len(self._DesignParameter['nmos_right_drain']['_XYCoordinates'])):
		        xy_with_offset.append([(x + y) for (x, y) in zip([0, 0], self._DesignParameter['nmos_right_drain']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		for i in range(len(path_list)):
		    path_list[i][0] = [(xy + offset) for (xy, offset) in zip(path_list[i][0], xy_offset)]
		self._DesignParameter['right_nmos_drain_met2'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _Width=_width)
		self._DesignParameter['right_nmos_drain_met2']['_XYCoordinates'] = path_list
		path_list = []
		xy_offset = [0, 0]
		if (len(self._DesignParameter['nmos_right_source']['_XYCoordinates']) == 1):
		    mode = 'vertical'
		    _width = self._DesignParameter['nmos_right_source']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth']
		elif (self._DesignParameter['nmos_right_source']['_XYCoordinates'][0][0] == self._DesignParameter['nmos_right_source']['_XYCoordinates'][(- 1)][0]):
		    mode = 'horizontal'
		    _width = self._DesignParameter['nmos_right_source']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth']
		elif (self._DesignParameter['nmos_right_source']['_XYCoordinates'][0][1] == self._DesignParameter['nmos_right_source']['_XYCoordinates'][(- 1)][1]):
		    mode = 'vertical'
		    _width = self._DesignParameter['nmos_right_source']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth']
		else:
		    print('Invalid Target Input')
		if (mode == 'vertical'):
		    xy_with_offset = []
		    target_y_value = [[(+ self._DesignParameter['nmos_center_via_stack_2to4']['_XYCoordinates'][0][0]), (+ self._DesignParameter['nmos_center_via_stack_2to4']['_XYCoordinates'][0][1])]][0][1]
		    for i in range(len(self._DesignParameter['nmos_right_source']['_XYCoordinates'])):
		        xy_with_offset.append([(x + y) for (x, y) in zip([0, 0], self._DesignParameter['nmos_right_source']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		elif (mode == 'horizontal'):
		    xy_with_offset = []
		    target_x_value = [[(+ self._DesignParameter['nmos_center_via_stack_2to4']['_XYCoordinates'][0][0]), (+ self._DesignParameter['nmos_center_via_stack_2to4']['_XYCoordinates'][0][1])]][0][0]
		    for i in range(len(self._DesignParameter['nmos_right_source']['_XYCoordinates'])):
		        xy_with_offset.append([(x + y) for (x, y) in zip([0, 0], self._DesignParameter['nmos_right_source']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		for i in range(len(path_list)):
		    path_list[i][0] = [(xy + offset) for (xy, offset) in zip(path_list[i][0], xy_offset)]
		self._DesignParameter['right_nmos_source_met2'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _Width=_width)
		self._DesignParameter['right_nmos_source_met2']['_XYCoordinates'] = path_list
		if ((pmos_outer_gate % 2) == 0):
		    self._DesignParameter['left_pmos_outside_via'] = self._SrefElementDeclaration(_DesignObj=ViaStack._ViaStack(_Name='left_pmos_outside_viaIn{}'.format(_Name)))[0]
		    self._DesignParameter['left_pmos_outside_via']['_DesignObj']._CalculateStackMinimumEnclosureX(**dict(COX=1, COY=pmos_coy, start_layer=1, end_layer=4))
		    self._DesignParameter['left_pmos_outside_via']['_XYCoordinates'] = None
		    XYList = []
		    xy_offset = [0, 0]
		    for element in self._DesignParameter['PMOS1InPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][1:pmos_outer_gate:2]:
		        element = (element[0] if (type(element[0]) == list) else element)
		        XYList.append([((x + y) + z) for (x, y, z) in zip([(0 + self._DesignParameter['PMOS1InPMOSSetofSlicer_0']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['PMOS1InPMOSSetofSlicer_0']['_XYCoordinates'][0][1])], element, xy_offset)])
		    self._DesignParameter['left_pmos_outside_via']['_XYCoordinates'] = XYList
		    path_list = []
		    xy_offset = [0, 0]
		    if (len(self._DesignParameter['PMOS1InPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates']) == 1):
		        mode = 'vertical'
		        _width = self._DesignParameter['PMOS1InPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
		    elif (self._DesignParameter['PMOS1InPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0] == self._DesignParameter['PMOS1InPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][(- 1)][0]):
		        mode = 'horizontal'
		        _width = self._DesignParameter['PMOS1InPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
		    elif (self._DesignParameter['PMOS1InPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1] == self._DesignParameter['PMOS1InPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][(- 1)][1]):
		        mode = 'vertical'
		        _width = self._DesignParameter['PMOS1InPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
		    else:
		        print('Invalid Target Input')
		    if (mode == 'vertical'):
		        xy_with_offset = []
		        target_y_value = [[(+ (self._DesignParameter['GuardringInPMOSSetofSlicer_0']['_XYCoordinates'][0][0] + self._DesignParameter['GuardringInPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['top']['_XYCoordinates'][0][0])), (+ (self._DesignParameter['GuardringInPMOSSetofSlicer_0']['_XYCoordinates'][0][1] + self._DesignParameter['GuardringInPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['top']['_XYCoordinates'][0][1]))]][0][1]
		        for i in range(len(self._DesignParameter['PMOS1InPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'])):
		            if ((i % 2) == 0):
		                xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['PMOS1InPMOSSetofSlicer_0']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['PMOS1InPMOSSetofSlicer_0']['_XYCoordinates'][0][1])], self._DesignParameter['PMOS1InPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i])])
		        for i in range(len(xy_with_offset)):
		            path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		    elif (mode == 'horizontal'):
		        xy_with_offset = []
		        target_x_value = [[(+ (self._DesignParameter['GuardringInPMOSSetofSlicer_0']['_XYCoordinates'][0][0] + self._DesignParameter['GuardringInPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['top']['_XYCoordinates'][0][0])), (+ (self._DesignParameter['GuardringInPMOSSetofSlicer_0']['_XYCoordinates'][0][1] + self._DesignParameter['GuardringInPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['top']['_XYCoordinates'][0][1]))]][0][0]
		        for i in range(len(self._DesignParameter['PMOS1InPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'])):
		            if ((i % 2) == 0):
		                xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['PMOS1InPMOSSetofSlicer_0']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['PMOS1InPMOSSetofSlicer_0']['_XYCoordinates'][0][1])], self._DesignParameter['PMOS1InPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i])])
		        for i in range(len(xy_with_offset)):
		            path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		    for i in range(len(path_list)):
		        path_list[i][0] = [(xy + offset) for (xy, offset) in zip(path_list[i][0], xy_offset)]
		    self._DesignParameter['precharge_left_pmos_supply'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=_width)
		    self._DesignParameter['precharge_left_pmos_supply']['_XYCoordinates'] = path_list
		else:
		    self._DesignParameter['left_pmos_outside_via'] = self._SrefElementDeclaration(_DesignObj=ViaStack._ViaStack(_Name='left_pmos_outside_viaIn{}'.format(_Name)))[0]
		    self._DesignParameter['left_pmos_outside_via']['_DesignObj']._CalculateStackMinimumEnclosureX(**dict(COX=1, COY=pmos_coy, start_layer=1, end_layer=4))
		    self._DesignParameter['left_pmos_outside_via']['_XYCoordinates'] = None
		    XYList = []
		    xy_offset = [0, 0]
		    for element in self._DesignParameter['PMOS1InPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0:pmos_outer_gate:2]:
		        element = (element[0] if (type(element[0]) == list) else element)
		        XYList.append([((x + y) + z) for (x, y, z) in zip([(0 + self._DesignParameter['PMOS1InPMOSSetofSlicer_0']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['PMOS1InPMOSSetofSlicer_0']['_XYCoordinates'][0][1])], element, xy_offset)])
		    self._DesignParameter['left_pmos_outside_via']['_XYCoordinates'] = XYList
		    path_list = []
		    xy_offset = [0, 0]
		    if (len(self._DesignParameter['PMOS1InPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates']) == 1):
		        mode = 'vertical'
		        _width = self._DesignParameter['PMOS1InPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
		    elif (self._DesignParameter['PMOS1InPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0] == self._DesignParameter['PMOS1InPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][(- 1)][0]):
		        mode = 'horizontal'
		        _width = self._DesignParameter['PMOS1InPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
		    elif (self._DesignParameter['PMOS1InPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1] == self._DesignParameter['PMOS1InPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][(- 1)][1]):
		        mode = 'vertical'
		        _width = self._DesignParameter['PMOS1InPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
		    else:
		        print('Invalid Target Input')
		    if (mode == 'vertical'):
		        xy_with_offset = []
		        target_y_value = [[(+ (self._DesignParameter['GuardringInPMOSSetofSlicer_0']['_XYCoordinates'][0][0] + self._DesignParameter['GuardringInPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['top']['_XYCoordinates'][0][0])), (+ (self._DesignParameter['GuardringInPMOSSetofSlicer_0']['_XYCoordinates'][0][1] + self._DesignParameter['GuardringInPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['top']['_XYCoordinates'][0][1]))]][0][1]
		        for i in range(len(self._DesignParameter['PMOS1InPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'])):
		            if ((i % 2) == 1):
		                xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['PMOS1InPMOSSetofSlicer_0']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['PMOS1InPMOSSetofSlicer_0']['_XYCoordinates'][0][1])], self._DesignParameter['PMOS1InPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i])])
		        for i in range(len(xy_with_offset)):
		            path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		    elif (mode == 'horizontal'):
		        xy_with_offset = []
		        target_x_value = [[(+ (self._DesignParameter['GuardringInPMOSSetofSlicer_0']['_XYCoordinates'][0][0] + self._DesignParameter['GuardringInPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['top']['_XYCoordinates'][0][0])), (+ (self._DesignParameter['GuardringInPMOSSetofSlicer_0']['_XYCoordinates'][0][1] + self._DesignParameter['GuardringInPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['top']['_XYCoordinates'][0][1]))]][0][0]
		        for i in range(len(self._DesignParameter['PMOS1InPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'])):
		            if ((i % 2) == 1):
		                xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['PMOS1InPMOSSetofSlicer_0']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['PMOS1InPMOSSetofSlicer_0']['_XYCoordinates'][0][1])], self._DesignParameter['PMOS1InPMOSSetofSlicer_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i])])
		        for i in range(len(xy_with_offset)):
		            path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		    for i in range(len(path_list)):
		        path_list[i][0] = [(xy + offset) for (xy, offset) in zip(path_list[i][0], xy_offset)]
		    self._DesignParameter['precharge_left_pmos_supply'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=_width)
		    self._DesignParameter['precharge_left_pmos_supply']['_XYCoordinates'] = path_list
		self._DesignParameter['poly_addi'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _XWidth=self._DesignParameter['nmos_bot']['_DesignObj']._DesignParameter['_PODummyLayer']['_XWidth'], _YWidth=round((drc._PODummyMinArea / self._DesignParameter['nmos_bot']['_DesignObj']._DesignParameter['_PODummyLayer']['_XWidth'])))
		self._DesignParameter['poly_addi']['_XYCoordinates'] = [[(+ (self._DesignParameter['nmos_bot']['_XYCoordinates'][0][0] + self._DesignParameter['nmos_bot']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][0])), (+ (self._DesignParameter['nmos_bot']['_XYCoordinates'][0][1] + self._DesignParameter['nmos_bot']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][1]))], [(+ (self._DesignParameter['nmos_bot']['_XYCoordinates'][0][0] + self._DesignParameter['nmos_bot']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][(- 1)][0])), (+ (self._DesignParameter['nmos_bot']['_XYCoordinates'][0][1] + self._DesignParameter['nmos_bot']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][(- 1)][1]))]]
		self._DesignParameter['met1_drc'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _XWidth=max(self._DesignParameter['VSS_viastack_1to3']['_DesignObj']._DesignParameter['ViaMet22Met3']['_DesignObj']._DesignParameter['_Met3Layer']['_XWidth'], self._DesignParameter['GuardringInSlicer_0']['_DesignObj']._DesignParameter['met_bot']['_XWidth']), _YWidth=self._DesignParameter['VSS_viastack_1to3']['_DesignObj']._DesignParameter['ViaMet22Met3']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth'])
		self._DesignParameter['met1_drc']['_XYCoordinates'] = [[(+ self._DesignParameter['VSS_viastack_1to3']['_XYCoordinates'][0][0]), (+ self._DesignParameter['VSS_viastack_1to3']['_XYCoordinates'][0][1])]]
		self._DesignParameter['met2_drc'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _XWidth=max(self._DesignParameter['VSS_viastack_1to3']['_DesignObj']._DesignParameter['ViaMet22Met3']['_DesignObj']._DesignParameter['_Met3Layer']['_XWidth'], self._DesignParameter['GuardringInSlicer_0']['_DesignObj']._DesignParameter['met_bot']['_XWidth']), _YWidth=self._DesignParameter['VSS_viastack_1to3']['_DesignObj']._DesignParameter['ViaMet22Met3']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth'])
		self._DesignParameter['met2_drc']['_XYCoordinates'] = [[(+ self._DesignParameter['VSS_viastack_1to3']['_XYCoordinates'][0][0]), (+ self._DesignParameter['VSS_viastack_1to3']['_XYCoordinates'][0][1])]]
		self._DesignParameter['met3_drc'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0], _Datatype=DesignParameters._LayerMapping['METAL3'][1], _XWidth=max(self._DesignParameter['VSS_viastack_1to3']['_DesignObj']._DesignParameter['ViaMet22Met3']['_DesignObj']._DesignParameter['_Met3Layer']['_XWidth'], self._DesignParameter['GuardringInSlicer_0']['_DesignObj']._DesignParameter['met_bot']['_XWidth']), _YWidth=self._DesignParameter['VSS_viastack_1to3']['_DesignObj']._DesignParameter['ViaMet22Met3']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth'])
		self._DesignParameter['met3_drc']['_XYCoordinates'] = [[(+ self._DesignParameter['VSS_viastack_1to3']['_XYCoordinates'][0][0]), (+ self._DesignParameter['VSS_viastack_1to3']['_XYCoordinates'][0][1])]]
		