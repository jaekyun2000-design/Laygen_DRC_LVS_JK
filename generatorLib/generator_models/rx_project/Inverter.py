from generatorLib import StickDiagram
from generatorLib import DesignParameters
import copy
import math
from generatorLib import DRC
from generatorLib.generator_models.rx_project import NbodyContact
from generatorLib.generator_models.rx_project import ViaMet12Met2
from generatorLib.generator_models.rx_project import ViaPoly2Met1
from generatorLib.generator_models.rx_project import NMOSWithDummy
from generatorLib.generator_models.rx_project import PMOSWithDummy
from generatorLib.generator_models.rx_project import ViaStack
from generatorLib.generator_models.rx_project import PbodyContact

class InverterInSlicerWithSRLatch_0(StickDiagram._StickDiagram):
	def __init__(self, _DesignParameter=None, _Name='InverterInSlicerWithSRLatch_0'):
		if _DesignParameter != None:
			self._DesignParameter = _DesignParameter
		else:
			self._DesignParameter = dict(_Name=self._NameDeclaration(_Name=_Name), _GDSFile=self._GDSObjDeclaration(_GDSFile=None))
		self._DesignParameter['_Name']['Name'] = _Name

	def _CalculateDesignParameter(self,gate=2,nmos_width=200,length=30,supply_coy=2,supply_height=None,pmos_width=600):
	
		drc = DRC.DRC()
		_Name = self._DesignParameter['_Name']['_Name']
		
		self._DesignParameter['NMOSInInverter_0'] = self._SrefElementDeclaration(_DesignObj=NMOSWithDummy._NMOS(_Name='NMOSInInverter_0In{}'.format(_Name)))[0]
		self._DesignParameter['NMOSInInverter_0']['_DesignObj']._CalculateNMOSDesignParameter(**dict(_NMOSNumberofGate=gate, _NMOSChannelWidth=nmos_width, _NMOSChannellength=length, _NMOSDummy=True, _GateSpacing=None, _SDWidth=None, _XVT='SLVT', _PCCrit=None))
		self._DesignParameter['NMOSInInverter_0']['_XYCoordinates'] = [[0, 362]]
		self._DesignParameter['PbodyContactInInverter_0'] = self._SrefElementDeclaration(_DesignObj=PbodyContact._PbodyContact(_Name='PbodyContactInInverter_0In{}'.format(_Name)))[0]
		self._DesignParameter['PbodyContactInInverter_0']['_DesignObj']._CalculatePbodyContactDesignParameter(**dict(_NumberOfPbodyCOX=max(1, (1 + int(((((((self._DesignParameter['NMOSInInverter_0']['_XYCoordinates'][0][0] + self._DesignParameter['NMOSInInverter_0']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][(- 1)][0]) + (self._DesignParameter['NMOSInInverter_0']['_DesignObj']._DesignParameter['_PODummyLayer']['_XWidth'] / 2)) - ((self._DesignParameter['NMOSInInverter_0']['_XYCoordinates'][0][0] + self._DesignParameter['NMOSInInverter_0']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['NMOSInInverter_0']['_DesignObj']._DesignParameter['_PODummyLayer']['_XWidth'] / 2))) - drc._CoMinSpace) - (2 * drc._CoMinEnclosureByPO)) / (drc._CoMinWidth + drc._CoMinSpace))))), _NumberOfPbodyCOY=supply_coy, _Met1XWidth=None, _Met1YWidth=None))
		self._DesignParameter['PbodyContactInInverter_0']['_XYCoordinates'] = [[self._DesignParameter['NMOSInInverter_0']['_XYCoordinates'][0][0], ((((self._DesignParameter['NMOSInInverter_0']['_XYCoordinates'][0][1] + self._DesignParameter['NMOSInInverter_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) - (self._DesignParameter['NMOSInInverter_0']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)) - drc._Metal1MinSpace3) - (self._DesignParameter['PbodyContactInInverter_0']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2))]]
		path_list = []
		xy_offset = [0, 0]
		if (len(self._DesignParameter['NMOSInInverter_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates']) == 1):
		    mode = 'vertical'
		    _width = self._DesignParameter['NMOSInInverter_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth']
		elif (self._DesignParameter['NMOSInInverter_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][0] == self._DesignParameter['NMOSInInverter_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][0]):
		    mode = 'horizontal'
		    _width = self._DesignParameter['NMOSInInverter_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth']
		elif (self._DesignParameter['NMOSInInverter_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1] == self._DesignParameter['NMOSInInverter_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][1]):
		    mode = 'vertical'
		    _width = self._DesignParameter['NMOSInInverter_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth']
		else:
		    print('Invalid Target Input')
		if (mode == 'vertical'):
		    xy_with_offset = []
		    target_y_value = [[(+ (self._DesignParameter['PbodyContactInInverter_0']['_XYCoordinates'][0][0] + self._DesignParameter['PbodyContactInInverter_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0])), (+ (self._DesignParameter['PbodyContactInInverter_0']['_XYCoordinates'][0][1] + self._DesignParameter['PbodyContactInInverter_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]))]][0][1]
		    for i in range(len(self._DesignParameter['NMOSInInverter_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		        if ((i % 2) == 0):
		            xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['NMOSInInverter_0']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['NMOSInInverter_0']['_XYCoordinates'][0][1])], self._DesignParameter['NMOSInInverter_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		elif (mode == 'horizontal'):
		    xy_with_offset = []
		    target_x_value = [[(+ (self._DesignParameter['PbodyContactInInverter_0']['_XYCoordinates'][0][0] + self._DesignParameter['PbodyContactInInverter_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0])), (+ (self._DesignParameter['PbodyContactInInverter_0']['_XYCoordinates'][0][1] + self._DesignParameter['PbodyContactInInverter_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]))]][0][0]
		    for i in range(len(self._DesignParameter['NMOSInInverter_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		        if ((i % 2) == 0):
		            xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['NMOSInInverter_0']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['NMOSInInverter_0']['_XYCoordinates'][0][1])], self._DesignParameter['NMOSInInverter_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		for i in range(len(path_list)):
		    path_list[i][0] = [(xy + offset) for (xy, offset) in zip(path_list[i][0], xy_offset)]
		self._DesignParameter['nmos_supply'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=_width)
		self._DesignParameter['nmos_supply']['_XYCoordinates'] = path_list
		nmos_coy = max(max(1, (1 + int((((self._DesignParameter['NMOSInInverter_0']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] - drc._VIAxMinSpace) - (2 * drc._VIAxMinEnclosureByMetx)) / (drc._VIAxMinWidth + drc._VIAxMinSpace))))), 2)
		self._DesignParameter['nmos_drain'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='nmos_drainIn{}'.format(_Name)))[0]
		self._DesignParameter['nmos_drain']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(**dict(_ViaMet12Met2NumberOfCOX=1, _ViaMet12Met2NumberOfCOY=nmos_coy))
		self._DesignParameter['nmos_drain']['_XYCoordinates'] = None
		XYList = []
		xy_offset = [0, 0]
		for i in range(len(self._DesignParameter['NMOSInInverter_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		    if ((i % 2) == 1):
		        xy = (self._DesignParameter['NMOSInInverter_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i][0] if (type(self._DesignParameter['NMOSInInverter_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i][0]) == list) else self._DesignParameter['NMOSInInverter_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])
		        XYList.append([((x + y) + z) for (x, y, z) in zip([(0 + self._DesignParameter['NMOSInInverter_0']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['NMOSInInverter_0']['_XYCoordinates'][0][1])], xy, xy_offset)])
		self._DesignParameter['nmos_drain']['_XYCoordinates'] = XYList
		self._DesignParameter['METAL2_path_45'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _Width=drc._MetalxMinWidth)
		self._DesignParameter['METAL2_path_45']['_XYCoordinates'] = [[[(+ self._DesignParameter['nmos_drain']['_XYCoordinates'][0][0]), (+ self._DesignParameter['nmos_drain']['_XYCoordinates'][0][1])], [(+ self._DesignParameter['nmos_drain']['_XYCoordinates'][(- 1)][0]), (+ self._DesignParameter['nmos_drain']['_XYCoordinates'][(- 1)][1])]]]
		self._DesignParameter['PCCAM1_CDNS_6375475055681_1'] = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_Name='PCCAM1_CDNS_6375475055681_1In{}'.format(_Name)))[0]
		self._DesignParameter['PCCAM1_CDNS_6375475055681_1']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(**dict(_ViaPoly2Met1NumberOfCOY=1, _ViaPoly2Met1NumberOfCOX=max(1, (1 + int(((((((self._DesignParameter['NMOSInInverter_0']['_XYCoordinates'][0][0] + self._DesignParameter['NMOSInInverter_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]) + (self._DesignParameter['NMOSInInverter_0']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)) - ((self._DesignParameter['NMOSInInverter_0']['_XYCoordinates'][0][0] + self._DesignParameter['NMOSInInverter_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['NMOSInInverter_0']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2))) - drc._CoMinSpace) - (2 * drc._CoMinEnclosureByPO)) / (drc._CoMinWidth + drc._CoMinSpace)))))))
		self._DesignParameter['PCCAM1_CDNS_6375475055681_1']['_XYCoordinates'] = [[self._DesignParameter['NMOSInInverter_0']['_XYCoordinates'][0][0], max(((((self._DesignParameter['NMOSInInverter_0']['_XYCoordinates'][0][1] + self._DesignParameter['NMOSInInverter_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) + (self._DesignParameter['NMOSInInverter_0']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)) + drc._Metal1MinSpace21) + (self._DesignParameter['PCCAM1_CDNS_6375475055681_1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)), ((((self._DesignParameter['nmos_drain']['_XYCoordinates'][0][1] + self._DesignParameter['nmos_drain']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) + (self._DesignParameter['nmos_drain']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)) + drc._Metal1MinSpace21) + (self._DesignParameter['PCCAM1_CDNS_6375475055681_1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)))]]
		self._DesignParameter['PMOSInInverter_0'] = self._SrefElementDeclaration(_DesignObj=PMOSWithDummy._PMOS(_Name='PMOSInInverter_0In{}'.format(_Name)))[0]
		self._DesignParameter['PMOSInInverter_0']['_DesignObj']._CalculatePMOSDesignParameter(**dict(_PMOSNumberofGate=gate, _PMOSChannelWidth=pmos_width, _PMOSChannellength=length, _PMOSDummy=True, _GateSpacing=None, _SDWidth=None, _XVT='SLVT', _PCCrit=None))
		self._DesignParameter['PMOSInInverter_0']['_XYCoordinates'] = [[self._DesignParameter['NMOSInInverter_0']['_XYCoordinates'][0][0], (((- (self._DesignParameter['PMOSInInverter_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1] - (self._DesignParameter['PMOSInInverter_0']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2))) + drc._Metal1MinSpace21) + ((self._DesignParameter['PCCAM1_CDNS_6375475055681_1']['_XYCoordinates'][0][1] + self._DesignParameter['PCCAM1_CDNS_6375475055681_1']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) + (self._DesignParameter['PCCAM1_CDNS_6375475055681_1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)))]]
		self._DesignParameter['NbodyContactInInverter_0'] = self._SrefElementDeclaration(_DesignObj=NbodyContact._NbodyContact(_Name='NbodyContactInInverter_0In{}'.format(_Name)))[0]
		self._DesignParameter['NbodyContactInInverter_0']['_DesignObj']._CalculateNbodyContactDesignParameter(**dict(_NumberOfNbodyCOX=max(1, (1 + int(((((((self._DesignParameter['NMOSInInverter_0']['_XYCoordinates'][0][0] + self._DesignParameter['NMOSInInverter_0']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][(- 1)][0]) + (self._DesignParameter['NMOSInInverter_0']['_DesignObj']._DesignParameter['_PODummyLayer']['_XWidth'] / 2)) - ((self._DesignParameter['NMOSInInverter_0']['_XYCoordinates'][0][0] + self._DesignParameter['NMOSInInverter_0']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['NMOSInInverter_0']['_DesignObj']._DesignParameter['_PODummyLayer']['_XWidth'] / 2))) - drc._CoMinSpace) - (2 * drc._CoMinEnclosureByPO)) / (drc._CoMinWidth + drc._CoMinSpace))))), _NumberOfNbodyCOY=supply_coy, _Met1XWidth=None, _Met1YWidth=None))
		self._DesignParameter['NbodyContactInInverter_0']['_XYCoordinates'] = [[self._DesignParameter['NMOSInInverter_0']['_XYCoordinates'][0][0], ((drc._Metal1MinSpace3 + (self._DesignParameter['NbodyContactInInverter_0']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)) + ((self._DesignParameter['PMOSInInverter_0']['_XYCoordinates'][0][1] + self._DesignParameter['PMOSInInverter_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) + (self._DesignParameter['PMOSInInverter_0']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)))]]
		path_list = []
		xy_offset = [0, 0]
		if (len(self._DesignParameter['PMOSInInverter_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates']) == 1):
		    mode = 'vertical'
		    _width = self._DesignParameter['PMOSInInverter_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
		elif (self._DesignParameter['PMOSInInverter_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0] == self._DesignParameter['PMOSInInverter_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][(- 1)][0]):
		    mode = 'horizontal'
		    _width = self._DesignParameter['PMOSInInverter_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
		elif (self._DesignParameter['PMOSInInverter_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1] == self._DesignParameter['PMOSInInverter_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][(- 1)][1]):
		    mode = 'vertical'
		    _width = self._DesignParameter['PMOSInInverter_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
		else:
		    print('Invalid Target Input')
		if (mode == 'vertical'):
		    xy_with_offset = []
		    target_y_value = [[(+ (self._DesignParameter['NbodyContactInInverter_0']['_XYCoordinates'][0][0] + self._DesignParameter['NbodyContactInInverter_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0])), (+ (self._DesignParameter['NbodyContactInInverter_0']['_XYCoordinates'][0][1] + self._DesignParameter['NbodyContactInInverter_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]))]][0][1]
		    for i in range(len(self._DesignParameter['PMOSInInverter_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'])):
		        if ((i % 2) == 0):
		            xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['PMOSInInverter_0']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['PMOSInInverter_0']['_XYCoordinates'][0][1])], self._DesignParameter['PMOSInInverter_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		elif (mode == 'horizontal'):
		    xy_with_offset = []
		    target_x_value = [[(+ (self._DesignParameter['NbodyContactInInverter_0']['_XYCoordinates'][0][0] + self._DesignParameter['NbodyContactInInverter_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0])), (+ (self._DesignParameter['NbodyContactInInverter_0']['_XYCoordinates'][0][1] + self._DesignParameter['NbodyContactInInverter_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]))]][0][0]
		    for i in range(len(self._DesignParameter['PMOSInInverter_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'])):
		        if ((i % 2) == 0):
		            xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['PMOSInInverter_0']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['PMOSInInverter_0']['_XYCoordinates'][0][1])], self._DesignParameter['PMOSInInverter_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		for i in range(len(path_list)):
		    path_list[i][0] = [(xy + offset) for (xy, offset) in zip(path_list[i][0], xy_offset)]
		self._DesignParameter['pmos_supply'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=_width)
		self._DesignParameter['pmos_supply']['_XYCoordinates'] = path_list
		pmos_coy = max(1, (1 + int((((self._DesignParameter['PMOSInInverter_0']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] - drc._VIAxMinSpace) - (2 * drc._VIAxMinEnclosureByMetx)) / (drc._VIAxMinWidth + drc._VIAxMinSpace)))))
		self._DesignParameter['pmos_drain_via'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='pmos_drain_viaIn{}'.format(_Name)))[0]
		self._DesignParameter['pmos_drain_via']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(**dict(_ViaMet12Met2NumberOfCOX=1, _ViaMet12Met2NumberOfCOY=pmos_coy))
		self._DesignParameter['pmos_drain_via']['_XYCoordinates'] = None
		XYList = []
		xy_offset = [0, 0]
		for i in range(len(self._DesignParameter['PMOSInInverter_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		    if ((i % 2) == 1):
		        xy = (self._DesignParameter['PMOSInInverter_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i][0] if (type(self._DesignParameter['PMOSInInverter_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i][0]) == list) else self._DesignParameter['PMOSInInverter_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])
		        XYList.append([((x + y) + z) for (x, y, z) in zip([(0 + self._DesignParameter['PMOSInInverter_0']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['PMOSInInverter_0']['_XYCoordinates'][0][1])], xy, xy_offset)])
		self._DesignParameter['pmos_drain_via']['_XYCoordinates'] = XYList
		self._DesignParameter['METAL2_path_46'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _Width=drc._MetalxMinWidth)
		self._DesignParameter['METAL2_path_46']['_XYCoordinates'] = [[[(+ self._DesignParameter['pmos_drain_via']['_XYCoordinates'][0][0]), (+ self._DesignParameter['pmos_drain_via']['_XYCoordinates'][0][1])], [(+ self._DesignParameter['pmos_drain_via']['_XYCoordinates'][(- 1)][0]), (+ self._DesignParameter['pmos_drain_via']['_XYCoordinates'][(- 1)][1])]]]
		path_list = []
		xy_offset = [0, 0]
		if (len(self._DesignParameter['NMOSInInverter_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates']) == 1):
		    mode = 'vertical'
		    _width = self._DesignParameter['NMOSInInverter_0']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
		elif (self._DesignParameter['NMOSInInverter_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0] == self._DesignParameter['NMOSInInverter_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]):
		    mode = 'horizontal'
		    _width = self._DesignParameter['NMOSInInverter_0']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
		elif (self._DesignParameter['NMOSInInverter_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1] == self._DesignParameter['NMOSInInverter_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][1]):
		    mode = 'vertical'
		    _width = self._DesignParameter['NMOSInInverter_0']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
		else:
		    print('Invalid Target Input')
		if (mode == 'vertical'):
		    xy_with_offset = []
		    target_y_value = [[(+ (self._DesignParameter['PMOSInInverter_0']['_XYCoordinates'][0][0] + self._DesignParameter['PMOSInInverter_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0])), (+ (self._DesignParameter['PMOSInInverter_0']['_XYCoordinates'][0][1] + self._DesignParameter['PMOSInInverter_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1]))]][0][1]
		    for i in range(len(self._DesignParameter['NMOSInInverter_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
		        xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['NMOSInInverter_0']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['NMOSInInverter_0']['_XYCoordinates'][0][1])], self._DesignParameter['NMOSInInverter_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		elif (mode == 'horizontal'):
		    xy_with_offset = []
		    target_x_value = [[(+ (self._DesignParameter['PMOSInInverter_0']['_XYCoordinates'][0][0] + self._DesignParameter['PMOSInInverter_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0])), (+ (self._DesignParameter['PMOSInInverter_0']['_XYCoordinates'][0][1] + self._DesignParameter['PMOSInInverter_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1]))]][0][0]
		    for i in range(len(self._DesignParameter['NMOSInInverter_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
		        xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['NMOSInInverter_0']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['NMOSInInverter_0']['_XYCoordinates'][0][1])], self._DesignParameter['NMOSInInverter_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		for i in range(len(path_list)):
		    path_list[i][0] = [(xy + offset) for (xy, offset) in zip(path_list[i][0], xy_offset)]
		self._DesignParameter['gate_routing'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _Width=_width)
		self._DesignParameter['gate_routing']['_XYCoordinates'] = path_list
		path_list = []
		xy_offset = [0, 0]
		if (len(self._DesignParameter['pmos_drain_via']['_XYCoordinates'][0::2]) == 1):
		    mode = 'vertical'
		    _width = self._DesignParameter['pmos_drain_via']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth']
		elif (self._DesignParameter['pmos_drain_via']['_XYCoordinates'][0::2][0][0] == self._DesignParameter['pmos_drain_via']['_XYCoordinates'][0::2][(- 1)][0]):
		    mode = 'horizontal'
		    _width = self._DesignParameter['pmos_drain_via']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth']
		elif (self._DesignParameter['pmos_drain_via']['_XYCoordinates'][0::2][0][1] == self._DesignParameter['pmos_drain_via']['_XYCoordinates'][0::2][(- 1)][1]):
		    mode = 'vertical'
		    _width = self._DesignParameter['pmos_drain_via']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth']
		else:
		    print('Invalid Target Input')
		if (mode == 'vertical'):
		    xy_with_offset = []
		    target_y_value = [[(+ self._DesignParameter['METAL2_path_45']['_XYCoordinates'][0][0][0]), (+ self._DesignParameter['METAL2_path_45']['_XYCoordinates'][0][0][1])]][0][1]
		    for element in self._DesignParameter['pmos_drain_via']['_XYCoordinates'][0::2]:
		        xy_with_offset.append([(x + y) for (x, y) in zip([0, 0], element)])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		elif (mode == 'horizontal'):
		    xy_with_offset = []
		    target_x_value = [[(+ self._DesignParameter['METAL2_path_45']['_XYCoordinates'][0][0][0]), (+ self._DesignParameter['METAL2_path_45']['_XYCoordinates'][0][0][1])]][0][0]
		    for element in self._DesignParameter['pmos_drain_via']['_XYCoordinates'][0::2]:
		        xy_with_offset.append([(x + y) for (x, y) in zip([0, 0], element)])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		for i in range(len(path_list)):
		    path_list[i][0] = [(xy + offset) for (xy, offset) in zip(path_list[i][0], xy_offset)]
		self._DesignParameter['met2_array'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _Width=_width)
		self._DesignParameter['met2_array']['_XYCoordinates'] = path_list
		self._DesignParameter['poly_boundary'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _XWidth=(((self._DesignParameter['NMOSInInverter_0']['_XYCoordinates'][0][0] + self._DesignParameter['NMOSInInverter_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]) + (self._DesignParameter['NMOSInInverter_0']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)) - ((self._DesignParameter['NMOSInInverter_0']['_XYCoordinates'][0][0] + self._DesignParameter['NMOSInInverter_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['NMOSInInverter_0']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2))), _YWidth=self._DesignParameter['PCCAM1_CDNS_6375475055681_1']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'])
		self._DesignParameter['poly_boundary']['_XYCoordinates'] = [[(+ self._DesignParameter['PCCAM1_CDNS_6375475055681_1']['_XYCoordinates'][0][0]), (+ self._DesignParameter['PCCAM1_CDNS_6375475055681_1']['_XYCoordinates'][0][1])]]
		self._DesignParameter['input_vias'] = self._SrefElementDeclaration(_DesignObj=ViaStack._ViaStack(_Name='input_viasIn{}'.format(_Name)))[0]
		self._DesignParameter['input_vias']['_DesignObj']._CalculateStackMinimumEnclosureY(**dict(COX=2, COY=1, start_layer=1, end_layer=3))
		self._DesignParameter['input_vias']['_XYCoordinates'] = None
		XYList = []
		xy_offset = (0, (self._DesignParameter['PCCAM1_CDNS_6375475055681_1']['_XYCoordinates'][0][1] - self._DesignParameter['nmos_drain']['_XYCoordinates'][0][1]))
		for i in range(len(self._DesignParameter['nmos_drain']['_XYCoordinates'])):
		    if ((i % 2) == 1):
		        xy = (self._DesignParameter['nmos_drain']['_XYCoordinates'][i][0] if (type(self._DesignParameter['nmos_drain']['_XYCoordinates'][i][0]) == list) else self._DesignParameter['nmos_drain']['_XYCoordinates'][i])
		        XYList.append([((x + y) + z) for (x, y, z) in zip([0, 0], xy, xy_offset)])
		self._DesignParameter['input_vias']['_XYCoordinates'] = XYList
		if (len(self._DesignParameter['input_vias']['_XYCoordinates']) >= 1):
		    self._DesignParameter['METAL3_path_37'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0], _Datatype=DesignParameters._LayerMapping['METAL3'][1], _Width=self._DesignParameter['input_vias']['_DesignObj']._DesignParameter['ViaMet22Met3']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth'])
		    self._DesignParameter['METAL3_path_37']['_XYCoordinates'] = [[[(+ self._DesignParameter['input_vias']['_XYCoordinates'][0][0]), (+ self._DesignParameter['input_vias']['_XYCoordinates'][0][1])], [(+ self._DesignParameter['input_vias']['_XYCoordinates'][(- 1)][0]), (+ self._DesignParameter['input_vias']['_XYCoordinates'][(- 1)][1])]]]
		self._DesignParameter['SLVT_boundary_31'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['SLVT'][0], _Datatype=DesignParameters._LayerMapping['SLVT'][1], _XWidth=self._DesignParameter['NMOSInInverter_0']['_DesignObj']._DesignParameter['_SLVTLayer']['_XWidth'], _YWidth=(((self._DesignParameter['PMOSInInverter_0']['_XYCoordinates'][0][1] + self._DesignParameter['PMOSInInverter_0']['_DesignObj']._DesignParameter['_SLVTLayer']['_XYCoordinates'][0][1]) + (self._DesignParameter['PMOSInInverter_0']['_DesignObj']._DesignParameter['_SLVTLayer']['_YWidth'] / 2)) - ((self._DesignParameter['NMOSInInverter_0']['_XYCoordinates'][0][1] + self._DesignParameter['NMOSInInverter_0']['_DesignObj']._DesignParameter['_SLVTLayer']['_XYCoordinates'][0][1]) - (self._DesignParameter['NMOSInInverter_0']['_DesignObj']._DesignParameter['_SLVTLayer']['_YWidth'] / 2))))
		self._DesignParameter['SLVT_boundary_31']['_XYCoordinates'] = [[self._DesignParameter['NMOSInInverter_0']['_XYCoordinates'][0][0], ((((self._DesignParameter['PMOSInInverter_0']['_XYCoordinates'][0][1] + self._DesignParameter['PMOSInInverter_0']['_DesignObj']._DesignParameter['_SLVTLayer']['_XYCoordinates'][0][1]) + (self._DesignParameter['PMOSInInverter_0']['_DesignObj']._DesignParameter['_SLVTLayer']['_YWidth'] / 2)) + ((self._DesignParameter['NMOSInInverter_0']['_XYCoordinates'][0][1] + self._DesignParameter['NMOSInInverter_0']['_DesignObj']._DesignParameter['_SLVTLayer']['_XYCoordinates'][0][1]) - (self._DesignParameter['NMOSInInverter_0']['_DesignObj']._DesignParameter['_SLVTLayer']['_YWidth'] / 2))) / 2)]]
		self._DesignParameter['VOUT'] = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2PIN'][0], _Datatype=DesignParameters._LayerMapping['METAL2PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0], _XYCoordinates=[[self._DesignParameter['met2_array']['_XYCoordinates'][0][0][0], self._DesignParameter['PCCAM1_CDNS_6375475055681_1']['_XYCoordinates'][0][1]]], _Mag=0.1, _Angle=0, _TEXT='VOUT')
		self._DesignParameter['VIN'] = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1PIN'][0], _Datatype=DesignParameters._LayerMapping['METAL1PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0], _XYCoordinates=[[(+ self._DesignParameter['PCCAM1_CDNS_6375475055681_1']['_XYCoordinates'][0][0]), (+ self._DesignParameter['PCCAM1_CDNS_6375475055681_1']['_XYCoordinates'][0][1])]], _Mag=0.1, _Angle=0, _TEXT='VIN')
		self._DesignParameter['VDD'] = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1PIN'][0], _Datatype=DesignParameters._LayerMapping['METAL1PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0], _XYCoordinates=[[(+ self._DesignParameter['NbodyContactInInverter_0']['_XYCoordinates'][0][0]), (+ self._DesignParameter['NbodyContactInInverter_0']['_XYCoordinates'][0][1])]], _Mag=0.1, _Angle=0, _TEXT='VDD')
		self._DesignParameter['VSS'] = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1PIN'][0], _Datatype=DesignParameters._LayerMapping['METAL1PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0], _XYCoordinates=[[(+ self._DesignParameter['PbodyContactInInverter_0']['_XYCoordinates'][0][0]), (+ self._DesignParameter['PbodyContactInInverter_0']['_XYCoordinates'][0][1])]], _Mag=0.1, _Angle=0, _TEXT='VSS')
		self._DesignParameter['NWELL_boundary_3'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['NWELL'][0], _Datatype=DesignParameters._LayerMapping['NWELL'][1], _XWidth=(self._DesignParameter['NbodyContactInInverter_0']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth'] + (2 * drc._NwMinEnclosurePactive2)), _YWidth=((((self._DesignParameter['NbodyContactInInverter_0']['_XYCoordinates'][0][1] + self._DesignParameter['NbodyContactInInverter_0']['_DesignObj']._DesignParameter['_ODLayer']['_XYCoordinates'][0][1]) + (self._DesignParameter['NbodyContactInInverter_0']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth'] / 2)) - ((self._DesignParameter['PMOSInInverter_0']['_XYCoordinates'][0][1] + self._DesignParameter['PMOSInInverter_0']['_DesignObj']._DesignParameter['_PPLayer']['_XYCoordinates'][0][1]) - (self._DesignParameter['PMOSInInverter_0']['_DesignObj']._DesignParameter['_PPLayer']['_YWidth'] / 2))) + drc._NwMinEnclosurePactive2))
		self._DesignParameter['NWELL_boundary_3']['_XYCoordinates'] = [[self._DesignParameter['PMOSInInverter_0']['_XYCoordinates'][0][0], (((((self._DesignParameter['NbodyContactInInverter_0']['_XYCoordinates'][0][1] + self._DesignParameter['NbodyContactInInverter_0']['_DesignObj']._DesignParameter['_ODLayer']['_XYCoordinates'][0][1]) + (self._DesignParameter['NbodyContactInInverter_0']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth'] / 2)) + ((self._DesignParameter['PMOSInInverter_0']['_XYCoordinates'][0][1] + self._DesignParameter['PMOSInInverter_0']['_DesignObj']._DesignParameter['_PPLayer']['_XYCoordinates'][0][1]) - (self._DesignParameter['PMOSInInverter_0']['_DesignObj']._DesignParameter['_PPLayer']['_YWidth'] / 2))) + drc._NwMinEnclosurePactive2) / 2)]]
		