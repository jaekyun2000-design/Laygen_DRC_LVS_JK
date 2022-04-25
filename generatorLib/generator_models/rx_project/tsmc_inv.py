from generatorLib import StickDiagram
from generatorLib import DesignParameters
import copy
import math
from generatorLib import DRC
from generatorLib.generator_models.rx_project import NMOSWithDummy
from generatorLib.generator_models.rx_project import ViaPoly2Met1
from generatorLib.generator_models.rx_project import NbodyContact
from generatorLib.generator_models.rx_project import PbodyContact
from generatorLib.generator_models.rx_project import PMOSWithDummy
from generatorLib.generator_models.rx_project import ViaMet12Met2

class EasyDebugModule(StickDiagram._StickDiagram):
	def __init__(self, _DesignParameter=None, _Name='EasyDebugModule'):
		if _DesignParameter != None:
			self._DesignParameter = _DesignParameter
		else:
			self._DesignParameter = dict(_Name=self._NameDeclaration(_Name=_Name), _GDSFile=self._GDSObjDeclaration(_GDSFile=None))
		self._DesignParameter['_Name']['Name'] = _Name

	def _CalculateDesignParameter(self,number_of_gate=4,dummy=False,reverse=False):
	
		drc = DRC.DRC()
		_Name = self._DesignParameter['_Name']['_Name']
		
		self._DesignParameter['VSS'] = self._SrefElementDeclaration(_DesignObj=PbodyContact._PbodyContact(_Name='VSSIn{}'.format(_Name)))[0]
		self._DesignParameter['VSS']['_DesignObj']._CalculatePbodyContactDesignParameter(**dict(_NumberOfPbodyCOY=1, _Met1XWidth=None, _Met1YWidth=None, _NumberOfPbodyCOX=10))
		self._DesignParameter['VSS']['_XYCoordinates'] = [[0, 0]]
		self._DesignParameter['nmos'] = self._SrefElementDeclaration(_DesignObj=NMOSWithDummy._NMOS(_Name='nmosIn{}'.format(_Name)))[0]
		self._DesignParameter['nmos']['_DesignObj']._CalculateNMOSDesignParameter(**dict(_NMOSNumberofGate=number_of_gate, _NMOSChannelWidth=600, _NMOSChannellength=60, _NMOSDummy=dummy, _GateSpacing=None, _SDWidth=None, _XVT='LVT', _PCCrit=None))
		self._DesignParameter['nmos']['_XYCoordinates'] = [[(+ (self._DesignParameter['VSS']['_XYCoordinates'][0][0] + self._DesignParameter['VSS']['_DesignObj']._DesignParameter['_PPLayer']['_XYCoordinates'][0][0])), ((self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_PDKLayer']['_YWidth'] / 2) + ((self._DesignParameter['VSS']['_XYCoordinates'][0][1] + self._DesignParameter['VSS']['_DesignObj']._DesignParameter['_PPLayer']['_XYCoordinates'][0][1]) + (self._DesignParameter['VSS']['_DesignObj']._DesignParameter['_PPLayer']['_YWidth'] / 2)))]]
		self._DesignParameter['pmos'] = self._SrefElementDeclaration(_DesignObj=PMOSWithDummy._PMOS(_Name='pmosIn{}'.format(_Name)))[0]
		self._DesignParameter['pmos']['_DesignObj']._CalculatePMOSDesignParameter(**dict(_PMOSNumberofGate=number_of_gate, _PMOSChannelWidth=1000, _PMOSChannellength=60, _PMOSDummy=dummy, _GateSpacing=None, _SDWidth=None, _XVT='LVT', _PCCrit=None))
		self._DesignParameter['pmos']['_XYCoordinates'] = [[(+ (self._DesignParameter['nmos']['_XYCoordinates'][0][0] + self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_PDKLayer']['_XYCoordinates'][0][0])), ((self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_PPLayer']['_YWidth'] / 2) + ((self._DesignParameter['nmos']['_XYCoordinates'][0][1] + self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_PDKLayer']['_XYCoordinates'][0][1]) + (self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_PDKLayer']['_YWidth'] / 2)))]]
		self._DesignParameter['vdd'] = self._SrefElementDeclaration(_DesignObj=NbodyContact._NbodyContact(_Name='vddIn{}'.format(_Name)))[0]
		self._DesignParameter['vdd']['_DesignObj']._CalculateNbodyContactDesignParameter(**dict(_NumberOfNbodyCOX=(max(1, (1 + int((((self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth'] - drc._CoMinSpace) - (2 * drc._CoMinEnclosureByPO)) / (drc._CoMinWidth + drc._CoMinSpace))))) + 1), _NumberOfNbodyCOY=1, _Met1XWidth=None, _Met1YWidth=None))
		self._DesignParameter['vdd']['_XYCoordinates'] = [[(+ (self._DesignParameter['pmos']['_XYCoordinates'][0][0] + self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_PPLayer']['_XYCoordinates'][0][0])), ((self._DesignParameter['vdd']['_DesignObj']._DesignParameter['_NPLayer']['_YWidth'] / 2) + ((self._DesignParameter['pmos']['_XYCoordinates'][0][1] + self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_PPLayer']['_XYCoordinates'][0][1]) + (self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_PPLayer']['_YWidth'] / 2)))]]
		self._DesignParameter['VSS']['_DesignObj']._CalculatePbodyContactDesignParameter(**dict(_NumberOfPbodyCOY=1, _Met1XWidth=None, _Met1YWidth=None, _NumberOfPbodyCOX=(max(1, (1 + int((((self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth'] - drc._CoMinSpace) - (2 * drc._CoMinEnclosureByPO)) / (drc._CoMinWidth + drc._CoMinSpace))))) + 1)))
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
		    target_y_value = [[(+ (self._DesignParameter['pmos']['_XYCoordinates'][0][0] + self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0])), (+ (self._DesignParameter['pmos']['_XYCoordinates'][0][1] + self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1]))]][0][1]
		    for i in range(len(self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
		        xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['nmos']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['nmos']['_XYCoordinates'][0][1])], self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		elif (mode == 'horizontal'):
		    xy_with_offset = []
		    target_x_value = [[(+ (self._DesignParameter['pmos']['_XYCoordinates'][0][0] + self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0])), (+ (self._DesignParameter['pmos']['_XYCoordinates'][0][1] + self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1]))]][0][0]
		    for i in range(len(self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
		        xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['nmos']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['nmos']['_XYCoordinates'][0][1])], self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		for i in range(len(path_list)):
		    path_list[i][0] = [(xy + offset) for (xy, offset) in zip(path_list[i][0], xy_offset)]
		self._DesignParameter['poly_routing'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _Width=_width)
		self._DesignParameter['poly_routing']['_XYCoordinates'] = path_list
		path_list = []
		xy_offset = [0, 0]
		if (len(self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates']) == 1):
		    mode = 'vertical'
		    _width = self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
		elif (self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0] == self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][(- 1)][0]):
		    mode = 'horizontal'
		    _width = self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
		elif (self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1] == self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][(- 1)][1]):
		    mode = 'vertical'
		    _width = self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
		else:
		    print('Invalid Target Input')
		if (mode == 'vertical'):
		    xy_with_offset = []
		    target_y_value = [[(+ self._DesignParameter['VSS']['_XYCoordinates'][0][0]), (+ self._DesignParameter['VSS']['_XYCoordinates'][0][1])]][0][1]
		    for i in range(len(self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'])):
		        if ((i % 2) == 0):
		            xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['nmos']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['nmos']['_XYCoordinates'][0][1])], self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		elif (mode == 'horizontal'):
		    xy_with_offset = []
		    target_x_value = [[(+ self._DesignParameter['VSS']['_XYCoordinates'][0][0]), (+ self._DesignParameter['VSS']['_XYCoordinates'][0][1])]][0][0]
		    for i in range(len(self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'])):
		        if ((i % 2) == 0):
		            xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['nmos']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['nmos']['_XYCoordinates'][0][1])], self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		for i in range(len(path_list)):
		    path_list[i][0] = [(xy + offset) for (xy, offset) in zip(path_list[i][0], xy_offset)]
		self._DesignParameter['nmos_supply'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=_width)
		self._DesignParameter['nmos_supply']['_XYCoordinates'] = path_list
		path_list = []
		xy_offset = [0, 0]
		if (len(self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates']) == 1):
		    mode = 'vertical'
		    _width = self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
		elif (self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0] == self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][(- 1)][0]):
		    mode = 'horizontal'
		    _width = self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
		elif (self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1] == self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][(- 1)][1]):
		    mode = 'vertical'
		    _width = self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
		else:
		    print('Invalid Target Input')
		if (mode == 'vertical'):
		    xy_with_offset = []
		    target_y_value = [[(+ self._DesignParameter['vdd']['_XYCoordinates'][0][0]), (+ self._DesignParameter['vdd']['_XYCoordinates'][0][1])]][0][1]
		    for i in range(len(self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'])):
		        if ((i % 2) == 0):
		            xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['pmos']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['pmos']['_XYCoordinates'][0][1])], self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		elif (mode == 'horizontal'):
		    xy_with_offset = []
		    target_x_value = [[(+ self._DesignParameter['vdd']['_XYCoordinates'][0][0]), (+ self._DesignParameter['vdd']['_XYCoordinates'][0][1])]][0][0]
		    for i in range(len(self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'])):
		        if ((i % 2) == 0):
		            xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['pmos']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['pmos']['_XYCoordinates'][0][1])], self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		for i in range(len(path_list)):
		    path_list[i][0] = [(xy + offset) for (xy, offset) in zip(path_list[i][0], xy_offset)]
		self._DesignParameter['pmos_supply'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=_width)
		self._DesignParameter['pmos_supply']['_XYCoordinates'] = path_list
		self._DesignParameter['input'] = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_Name='inputIn{}'.format(_Name)))[0]
		self._DesignParameter['input']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(**dict(_ViaPoly2Met1NumberOfCOX=max(1, (1 + int(((((((self._DesignParameter['pmos']['_XYCoordinates'][0][0] + self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]) + (self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)) - ((self._DesignParameter['pmos']['_XYCoordinates'][0][0] + self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2))) - drc._VIAxMinSpace) - (2 * drc._VIAxMinEnclosureByMetx)) / (drc._VIAxMinWidth + drc._VIAxMinSpace))))), _ViaPoly2Met1NumberOfCOY=1))
		self._DesignParameter['input']['_XYCoordinates'] = [[self._DesignParameter['nmos']['_XYCoordinates'][0][0], ((((self._DesignParameter['nmos']['_XYCoordinates'][0][1] + self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_ODLayer']['_XYCoordinates'][0][1]) + (self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth'] / 2)) + ((self._DesignParameter['pmos']['_XYCoordinates'][0][1] + self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_ODLayer']['_XYCoordinates'][0][1]) - (self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth'] / 2))) / 2)]]
		self._DesignParameter['n_drain_via'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='n_drain_viaIn{}'.format(_Name)))[0]
		self._DesignParameter['n_drain_via']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(**dict(_ViaMet12Met2NumberOfCOX=1, _ViaMet12Met2NumberOfCOY=3))
		self._DesignParameter['n_drain_via']['_XYCoordinates'] = None
		XYList = []
		xy_offset = [0, 0]
		for i in range(len(self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'])):
		    if ((i % 2) == 1):
		        xy = (self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i][0] if (type(self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i][0]) == list) else self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i])
		        XYList.append([((x + y) + z) for (x, y, z) in zip([(0 + self._DesignParameter['nmos']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['nmos']['_XYCoordinates'][0][1])], xy, xy_offset)])
		self._DesignParameter['n_drain_via']['_XYCoordinates'] = XYList
		self._DesignParameter['p_drain_via'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='p_drain_viaIn{}'.format(_Name)))[0]
		self._DesignParameter['p_drain_via']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(**dict(_ViaMet12Met2NumberOfCOX=1, _ViaMet12Met2NumberOfCOY=5))
		self._DesignParameter['p_drain_via']['_XYCoordinates'] = None
		XYList = []
		xy_offset = [0, 0]
		for i in range(len(self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'])):
		    if ((i % 2) == 1):
		        xy = (self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i][0] if (type(self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i][0]) == list) else self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i])
		        XYList.append([((x + y) + z) for (x, y, z) in zip([(0 + self._DesignParameter['pmos']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['pmos']['_XYCoordinates'][0][1])], xy, xy_offset)])
		self._DesignParameter['p_drain_via']['_XYCoordinates'] = XYList
		if reverse:
		    path_list = []
		    xy_offset = [0, 0]
		    if (len(self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates']) == 1):
		        mode = 'vertical'
		        _width = self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
		    elif (self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0] == self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][(- 1)][0]):
		        mode = 'horizontal'
		        _width = self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
		    elif (self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1] == self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][(- 1)][1]):
		        mode = 'vertical'
		        _width = self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
		    else:
		        print('Invalid Target Input')
		    if (mode == 'vertical'):
		        xy_with_offset = []
		        target_y_value = [[(+ self._DesignParameter['VSS']['_XYCoordinates'][0][0]), (+ self._DesignParameter['VSS']['_XYCoordinates'][0][1])]][0][1]
		        for i in range(len(self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'])):
		            if ((i % 2) == 1):
		                xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['nmos']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['nmos']['_XYCoordinates'][0][1])], self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i])])
		        for i in range(len(xy_with_offset)):
		            path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		    elif (mode == 'horizontal'):
		        xy_with_offset = []
		        target_x_value = [[(+ self._DesignParameter['VSS']['_XYCoordinates'][0][0]), (+ self._DesignParameter['VSS']['_XYCoordinates'][0][1])]][0][0]
		        for i in range(len(self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'])):
		            if ((i % 2) == 1):
		                xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['nmos']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['nmos']['_XYCoordinates'][0][1])], self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i])])
		        for i in range(len(xy_with_offset)):
		            path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		    for i in range(len(path_list)):
		        path_list[i][0] = [(xy + offset) for (xy, offset) in zip(path_list[i][0], xy_offset)]
		    self._DesignParameter['nmos_supply'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=_width)
		    self._DesignParameter['nmos_supply']['_XYCoordinates'] = path_list
		    self._DesignParameter['n_drain_via'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='n_drain_viaIn{}'.format(_Name)))[0]
		    self._DesignParameter['n_drain_via']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(**dict(_ViaMet12Met2NumberOfCOX=1, _ViaMet12Met2NumberOfCOY=3))
		    self._DesignParameter['n_drain_via']['_XYCoordinates'] = None
		    XYList = []
		    xy_offset = [0, 0]
		    for i in range(len(self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'])):
		        if ((i % 2) == 0):
		            xy = (self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i][0] if (type(self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i][0]) == list) else self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i])
		            XYList.append([((x + y) + z) for (x, y, z) in zip([(0 + self._DesignParameter['nmos']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['nmos']['_XYCoordinates'][0][1])], xy, xy_offset)])
		    self._DesignParameter['n_drain_via']['_XYCoordinates'] = XYList
		    self._DesignParameter['p_drain_via'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='p_drain_viaIn{}'.format(_Name)))[0]
		    self._DesignParameter['p_drain_via']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(**dict(_ViaMet12Met2NumberOfCOX=1, _ViaMet12Met2NumberOfCOY=5))
		    self._DesignParameter['p_drain_via']['_XYCoordinates'] = None
		    XYList = []
		    xy_offset = [0, 0]
		    for i in range(len(self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'])):
		        if ((i % 2) == 0):
		            xy = (self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i][0] if (type(self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i][0]) == list) else self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i])
		            XYList.append([((x + y) + z) for (x, y, z) in zip([(0 + self._DesignParameter['pmos']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['pmos']['_XYCoordinates'][0][1])], xy, xy_offset)])
		    self._DesignParameter['p_drain_via']['_XYCoordinates'] = XYList
		    path_list = []
		    xy_offset = [0, 0]
		    if (len(self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates']) == 1):
		        mode = 'vertical'
		        _width = self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
		    elif (self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0] == self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][(- 1)][0]):
		        mode = 'horizontal'
		        _width = self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
		    elif (self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1] == self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][(- 1)][1]):
		        mode = 'vertical'
		        _width = self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
		    else:
		        print('Invalid Target Input')
		    if (mode == 'vertical'):
		        xy_with_offset = []
		        target_y_value = [[(+ self._DesignParameter['vdd']['_XYCoordinates'][0][0]), (+ self._DesignParameter['vdd']['_XYCoordinates'][0][1])]][0][1]
		        for i in range(len(self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'])):
		            if ((i % 2) == 1):
		                xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['pmos']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['pmos']['_XYCoordinates'][0][1])], self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i])])
		        for i in range(len(xy_with_offset)):
		            path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		    elif (mode == 'horizontal'):
		        xy_with_offset = []
		        target_x_value = [[(+ self._DesignParameter['vdd']['_XYCoordinates'][0][0]), (+ self._DesignParameter['vdd']['_XYCoordinates'][0][1])]][0][0]
		        for i in range(len(self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'])):
		            if ((i % 2) == 1):
		                xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['pmos']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['pmos']['_XYCoordinates'][0][1])], self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i])])
		        for i in range(len(xy_with_offset)):
		            path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		    for i in range(len(path_list)):
		        path_list[i][0] = [(xy + offset) for (xy, offset) in zip(path_list[i][0], xy_offset)]
		    self._DesignParameter['pmos_supply'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=_width)
		    self._DesignParameter['pmos_supply']['_XYCoordinates'] = path_list
		self._DesignParameter['nmos_drain'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _XWidth=(((self._DesignParameter['n_drain_via']['_XYCoordinates'][(- 1)][0] + self._DesignParameter['n_drain_via']['_DesignObj']._DesignParameter['_Met2Layer']['_XYCoordinates'][0][0]) + (self._DesignParameter['n_drain_via']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth'] / 2)) - ((self._DesignParameter['n_drain_via']['_XYCoordinates'][0][0] + self._DesignParameter['n_drain_via']['_DesignObj']._DesignParameter['_Met2Layer']['_XYCoordinates'][0][0]) - (self._DesignParameter['n_drain_via']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth'] / 2))), _YWidth=self._DesignParameter['n_drain_via']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'])
		self._DesignParameter['nmos_drain']['_XYCoordinates'] = [[((self._DesignParameter['n_drain_via']['_XYCoordinates'][0][0] + self._DesignParameter['n_drain_via']['_XYCoordinates'][(- 1)][0]) / 2), self._DesignParameter['n_drain_via']['_XYCoordinates'][0][1]]]
		self._DesignParameter['nmos_drain_0'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _XWidth=(((self._DesignParameter['n_drain_via']['_XYCoordinates'][(- 1)][0] + self._DesignParameter['n_drain_via']['_DesignObj']._DesignParameter['_Met2Layer']['_XYCoordinates'][0][0]) + (self._DesignParameter['n_drain_via']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth'] / 2)) - ((self._DesignParameter['n_drain_via']['_XYCoordinates'][0][0] + self._DesignParameter['n_drain_via']['_DesignObj']._DesignParameter['_Met2Layer']['_XYCoordinates'][0][0]) - (self._DesignParameter['n_drain_via']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth'] / 2))), _YWidth=self._DesignParameter['p_drain_via']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'])
		self._DesignParameter['nmos_drain_0']['_XYCoordinates'] = [[((self._DesignParameter['p_drain_via']['_XYCoordinates'][0][0] + self._DesignParameter['p_drain_via']['_XYCoordinates'][(- 1)][0]) / 2), self._DesignParameter['p_drain_via']['_XYCoordinates'][0][1]]]
		path_list = []
		xy_offset = [0, 0]
		if (len(self._DesignParameter['n_drain_via']['_XYCoordinates']) == 1):
		    mode = 'vertical'
		    _width = self._DesignParameter['n_drain_via']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth']
		elif (self._DesignParameter['n_drain_via']['_XYCoordinates'][0][0] == self._DesignParameter['n_drain_via']['_XYCoordinates'][(- 1)][0]):
		    mode = 'horizontal'
		    _width = self._DesignParameter['n_drain_via']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth']
		elif (self._DesignParameter['n_drain_via']['_XYCoordinates'][0][1] == self._DesignParameter['n_drain_via']['_XYCoordinates'][(- 1)][1]):
		    mode = 'vertical'
		    _width = self._DesignParameter['n_drain_via']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth']
		else:
		    print('Invalid Target Input')
		if (mode == 'vertical'):
		    xy_with_offset = []
		    target_y_value = [[(+ self._DesignParameter['p_drain_via']['_XYCoordinates'][0][0]), (+ self._DesignParameter['p_drain_via']['_XYCoordinates'][0][1])]][0][1]
		    for i in range(len(self._DesignParameter['n_drain_via']['_XYCoordinates'])):
		        xy_with_offset.append([(x + y) for (x, y) in zip([0, 0], self._DesignParameter['n_drain_via']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		elif (mode == 'horizontal'):
		    xy_with_offset = []
		    target_x_value = [[(+ self._DesignParameter['p_drain_via']['_XYCoordinates'][0][0]), (+ self._DesignParameter['p_drain_via']['_XYCoordinates'][0][1])]][0][0]
		    for i in range(len(self._DesignParameter['n_drain_via']['_XYCoordinates'])):
		        xy_with_offset.append([(x + y) for (x, y) in zip([0, 0], self._DesignParameter['n_drain_via']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		for i in range(len(path_list)):
		    path_list[i][0] = [(xy + offset) for (xy, offset) in zip(path_list[i][0], xy_offset)]
		self._DesignParameter['drain_routing'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _Width=_width)
		self._DesignParameter['drain_routing']['_XYCoordinates'] = path_list
		