from generatorLib import StickDiagram
from generatorLib import DesignParameters
import copy
import math
from generatorLib import DRC
from generatorLib.generator_models import ViaPoly2Met1
from generatorLib.generator_models import NbodyContact
from generatorLib.generator_models import NMOSWithDummy
from generatorLib.generator_models import PbodyContact
from generatorLib.generator_models import ViaStack
from generatorLib.generator_models import PMOSWithDummy

class _inverter_ksh(StickDiagram._StickDiagram):
	def __init__(self, _DesignParameter=None, _Name='inverter_ksh'):
		if _DesignParameter != None:
			self._DesignParameter = _DesignParameter
		else:
			self._DesignParameter = dict(_Name=self._NameDeclaration(_Name=_Name), _GDSFile=self._GDSObjDeclaration(_GDSFile=None))
		self._DesignParameter['_Name']['Name'] = _Name

	def _CalculateDesignParameter(self,n_gate=3,n_width=600,n_length=80,dummy=False,p_gate=3,p_width=1200,p_length=80,supply_coy=2,supply_height=2600):
	
		drc = DRC.DRC()
		_Name = self._DesignParameter['_Name']['_Name']
		
		self._DesignParameter['nmos'] = self._SrefElementDeclaration(_DesignObj=NMOSWithDummy._NMOS(_Name='nmosIn{}'.format(_Name)))[0]
		self._DesignParameter['nmos']['_DesignObj']._CalculateNMOSDesignParameter(**dict(_NMOSNumberofGate=n_gate, _NMOSChannelWidth=n_width, _NMOSChannellength=n_length, _NMOSDummy=dummy, _GateSpacing=None, _SDWidth=None, _XVT='SLVT', _PCCrit=None))
		self._DesignParameter['nmos']['_XYCoordinates'] = [[0, 362]]
		self._DesignParameter['pmos'] = self._SrefElementDeclaration(_DesignObj=PMOSWithDummy._PMOS(_Name='pmosIn{}'.format(_Name)))[0]
		self._DesignParameter['pmos']['_DesignObj']._CalculatePMOSDesignParameter(**dict(_PMOSNumberofGate=p_gate, _PMOSChannelWidth=p_width, _PMOSChannellength=p_length, _PMOSDummy=dummy, _GateSpacing=None, _SDWidth=None, _XVT='SLVT', _PCCrit=None))
		self._DesignParameter['pmos']['_XYCoordinates'] = [[0, 1600]]
		self._DesignParameter['vss_supply'] = self._SrefElementDeclaration(_DesignObj=PbodyContact._PbodyContact(_Name='vss_supplyIn{}'.format(_Name)))[0]
		self._DesignParameter['vss_supply']['_DesignObj']._CalculatePbodyContactDesignParameter(**dict(_NumberOfPbodyCOX=max((1 + max(1, (1 + int((((self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth'] - drc._CoMinSpace) - (2 * drc._CoMinEnclosureByPO)) / (drc._CoMinWidth + drc._CoMinSpace)))))), (1 + max(1, (1 + int((((self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth'] - drc._CoMinSpace) - (2 * drc._CoMinEnclosureByPO)) / (drc._CoMinWidth + drc._CoMinSpace))))))), _NumberOfPbodyCOY=supply_coy, _Met1XWidth=None, _Met1YWidth=None))
		self._DesignParameter['vss_supply']['_XYCoordinates'] = [[0, (- 169)]]
		self._DesignParameter['vdd_supply'] = self._SrefElementDeclaration(_DesignObj=NbodyContact._NbodyContact(_Name='vdd_supplyIn{}'.format(_Name)))[0]
		self._DesignParameter['vdd_supply']['_DesignObj']._CalculateNbodyContactDesignParameter(**dict(_NumberOfNbodyCOX=max((1 + max(1, (1 + int((((self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth'] - drc._CoMinSpace) - (2 * drc._CoMinEnclosureByPO)) / (drc._CoMinWidth + drc._CoMinSpace)))))), (1 + max(1, (1 + int((((self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth'] - drc._CoMinSpace) - (2 * drc._CoMinEnclosureByPO)) / (drc._CoMinWidth + drc._CoMinSpace))))))), _NumberOfNbodyCOY=supply_coy, _Met1XWidth=None, _Met1YWidth=None))
		self._DesignParameter['vdd_supply']['_XYCoordinates'] = [[(+ self._DesignParameter['vss_supply']['_XYCoordinates'][0][0]), (supply_height + self._DesignParameter['vss_supply']['_XYCoordinates'][0][1])]]
		self._DesignParameter['nmos']['_XYCoordinates'] = [[self._DesignParameter['vss_supply']['_XYCoordinates'][0][0], ((((self._DesignParameter['vss_supply']['_XYCoordinates'][0][1] + self._DesignParameter['vss_supply']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) + (self._DesignParameter['vss_supply']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)) + (self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)) + drc._Metal1MinSpace3)]]
		self._DesignParameter['pmos']['_XYCoordinates'] = [[self._DesignParameter['vdd_supply']['_XYCoordinates'][0][0], ((((self._DesignParameter['vdd_supply']['_XYCoordinates'][0][1] + self._DesignParameter['vdd_supply']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) - (self._DesignParameter['vdd_supply']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)) - (self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)) - drc._Metal1MinSpace3)]]
		path_list = []
		xy_offset = [0, 0]
		if (len(self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates']) == 1):
		    mode = 'vertical'
		    _width = self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth']
		elif (self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][0] == self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][0]):
		    mode = 'horizontal'
		    _width = self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth']
		elif (self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1] == self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][1]):
		    mode = 'vertical'
		    _width = self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth']
		else:
		    print('Invalid Target Input')
		if (mode == 'vertical'):
		    xy_with_offset = []
		    target_y_value = [[(+ (self._DesignParameter['vss_supply']['_XYCoordinates'][0][0] + self._DesignParameter['vss_supply']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0])), (+ (self._DesignParameter['vss_supply']['_XYCoordinates'][0][1] + self._DesignParameter['vss_supply']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]))]][0][1]
		    for i in range(len(self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		        if ((i % 2) == 0):
		            xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['nmos']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['nmos']['_XYCoordinates'][0][1])], self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		elif (mode == 'horizontal'):
		    xy_with_offset = []
		    target_x_value = [[(+ (self._DesignParameter['vss_supply']['_XYCoordinates'][0][0] + self._DesignParameter['vss_supply']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0])), (+ (self._DesignParameter['vss_supply']['_XYCoordinates'][0][1] + self._DesignParameter['vss_supply']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]))]][0][0]
		    for i in range(len(self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		        if ((i % 2) == 0):
		            xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['nmos']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['nmos']['_XYCoordinates'][0][1])], self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		for i in range(len(path_list)):
		    path_list[i][0] = [(xy + offset) for (xy, offset) in zip(path_list[i][0], xy_offset)]
		self._DesignParameter['nmos_supply'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=_width)
		self._DesignParameter['nmos_supply']['_XYCoordinates'] = path_list
		self._DesignParameter['nmos_vias'] = self._SrefElementDeclaration(_DesignObj=ViaStack._ViaStack(_Name='nmos_viasIn{}'.format(_Name)))[0]
		self._DesignParameter['nmos_vias']['_DesignObj']._CalculateStackMinimumEnclosureX(**dict(COY=max(2, max(1, (1 + int((((self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] - drc._VIAxMinSpace) - (2 * drc._VIAxMinEnclosureByMetx)) / (drc._VIAxMinWidth + drc._VIAxMinSpace)))))), COX=1, start_layer=1, end_layer=2))
		self._DesignParameter['nmos_vias']['_XYCoordinates'] = None
		XYList = []
		xy_offset = [0, 0]
		for i in range(len(self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		    if ((i % 2) == 1):
		        xy = (self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i][0] if (type(self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i][0]) == list) else self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])
		        XYList.append([((x + y) + z) for (x, y, z) in zip([(0 + self._DesignParameter['nmos']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['nmos']['_XYCoordinates'][0][1])], xy, xy_offset)])
		self._DesignParameter['nmos_vias']['_XYCoordinates'] = XYList
		self._DesignParameter['METAL2_path_1'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _Width=drc._MetalxMinWidth)
		self._DesignParameter['METAL2_path_1']['_XYCoordinates'] = [[[(+ self._DesignParameter['nmos_vias']['_XYCoordinates'][(- 1)][0]), (+ self._DesignParameter['nmos_vias']['_XYCoordinates'][(- 1)][1])], [(+ self._DesignParameter['nmos_vias']['_XYCoordinates'][0][0]), (+ self._DesignParameter['nmos_vias']['_XYCoordinates'][0][1])]]]
		path_list = []
		xy_offset = [0, 0]
		if (len(self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates']) == 1):
		    mode = 'vertical'
		    _width = self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth']
		elif (self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][0] == self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][0]):
		    mode = 'horizontal'
		    _width = self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth']
		elif (self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1] == self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][1]):
		    mode = 'vertical'
		    _width = self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth']
		else:
		    print('Invalid Target Input')
		if (mode == 'vertical'):
		    xy_with_offset = []
		    target_y_value = [[(+ (self._DesignParameter['vdd_supply']['_XYCoordinates'][0][0] + self._DesignParameter['vdd_supply']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0])), (+ (self._DesignParameter['vdd_supply']['_XYCoordinates'][0][1] + self._DesignParameter['vdd_supply']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]))]][0][1]
		    for i in range(len(self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		        if ((i % 2) == 0):
		            xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['pmos']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['pmos']['_XYCoordinates'][0][1])], self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		elif (mode == 'horizontal'):
		    xy_with_offset = []
		    target_x_value = [[(+ (self._DesignParameter['vdd_supply']['_XYCoordinates'][0][0] + self._DesignParameter['vdd_supply']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0])), (+ (self._DesignParameter['vdd_supply']['_XYCoordinates'][0][1] + self._DesignParameter['vdd_supply']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]))]][0][0]
		    for i in range(len(self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
		        if ((i % 2) == 0):
		            xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['pmos']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['pmos']['_XYCoordinates'][0][1])], self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		for i in range(len(path_list)):
		    path_list[i][0] = [(xy + offset) for (xy, offset) in zip(path_list[i][0], xy_offset)]
		self._DesignParameter['pmos_supply'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=_width)
		self._DesignParameter['pmos_supply']['_XYCoordinates'] = path_list
		self._DesignParameter['pmos_vias'] = self._SrefElementDeclaration(_DesignObj=ViaStack._ViaStack(_Name='pmos_viasIn{}'.format(_Name)))[0]
		self._DesignParameter['pmos_vias']['_DesignObj']._CalculateStackMinimumEnclosureX(**dict(COY=max(2, max(1, (1 + int((((self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] - drc._VIAxMinSpace) - (2 * drc._VIAxMinEnclosureByMetx)) / (drc._VIAxMinWidth + drc._VIAxMinSpace)))))), COX=1, start_layer=1, end_layer=2))
		self._DesignParameter['pmos_vias']['_XYCoordinates'] = None
		XYList = []
		xy_offset = [0, 0]
		for i in range(len(self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'])):
		    if ((i % 2) == 1):
		        xy = (self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i][0] if (type(self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i][0]) == list) else self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i])
		        XYList.append([((x + y) + z) for (x, y, z) in zip([(0 + self._DesignParameter['pmos']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['pmos']['_XYCoordinates'][0][1])], xy, xy_offset)])
		self._DesignParameter['pmos_vias']['_XYCoordinates'] = XYList
		self._DesignParameter['gate_contacts'] = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_Name='gate_contactsIn{}'.format(_Name)))[0]
		self._DesignParameter['gate_contacts']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(**dict(_ViaPoly2Met1NumberOfCOX=max(1, (1 + int((((max((((self._DesignParameter['nmos']['_XYCoordinates'][0][0] + self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]) + (self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)) - ((self._DesignParameter['nmos']['_XYCoordinates'][0][0] + self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2))), (((self._DesignParameter['pmos']['_XYCoordinates'][0][0] + self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]) + (self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)) - ((self._DesignParameter['pmos']['_XYCoordinates'][0][0] + self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)))) - drc._CoMinSpace) - (2 * drc._CoMinEnclosureByPO)) / (drc._CoMinWidth + drc._CoMinSpace))))), _ViaPoly2Met1NumberOfCOY=1))
		self._DesignParameter['gate_contacts']['_XYCoordinates'] = [[self._DesignParameter['pmos']['_XYCoordinates'][0][0], ((((self._DesignParameter['nmos']['_XYCoordinates'][0][1] + self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1]) + (self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2)) + ((self._DesignParameter['pmos']['_XYCoordinates'][0][1] + self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1]) - (self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2))) / 2)]]
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
		    target_y_value = [[(+ self._DesignParameter['gate_contacts']['_XYCoordinates'][0][0]), (+ self._DesignParameter['gate_contacts']['_XYCoordinates'][0][1])]][0][1]
		    for i in range(len(self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
		        xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['nmos']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['nmos']['_XYCoordinates'][0][1])], self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		elif (mode == 'horizontal'):
		    xy_with_offset = []
		    target_x_value = [[(+ self._DesignParameter['gate_contacts']['_XYCoordinates'][0][0]), (+ self._DesignParameter['gate_contacts']['_XYCoordinates'][0][1])]][0][0]
		    for i in range(len(self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
		        xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['nmos']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['nmos']['_XYCoordinates'][0][1])], self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		for i in range(len(path_list)):
		    path_list[i][0] = [(xy + offset) for (xy, offset) in zip(path_list[i][0], xy_offset)]
		self._DesignParameter['nmos_gate'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _Width=_width)
		self._DesignParameter['nmos_gate']['_XYCoordinates'] = path_list
		path_list = []
		xy_offset = [0, 0]
		if (len(self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates']) == 1):
		    mode = 'vertical'
		    _width = self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
		elif (self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0] == self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]):
		    mode = 'horizontal'
		    _width = self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
		elif (self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1] == self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][1]):
		    mode = 'vertical'
		    _width = self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
		else:
		    print('Invalid Target Input')
		if (mode == 'vertical'):
		    xy_with_offset = []
		    target_y_value = [[(+ self._DesignParameter['gate_contacts']['_XYCoordinates'][0][0]), (+ self._DesignParameter['gate_contacts']['_XYCoordinates'][0][1])]][0][1]
		    for i in range(len(self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
		        xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['pmos']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['pmos']['_XYCoordinates'][0][1])], self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		elif (mode == 'horizontal'):
		    xy_with_offset = []
		    target_x_value = [[(+ self._DesignParameter['gate_contacts']['_XYCoordinates'][0][0]), (+ self._DesignParameter['gate_contacts']['_XYCoordinates'][0][1])]][0][0]
		    for i in range(len(self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
		        xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['pmos']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['pmos']['_XYCoordinates'][0][1])], self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		for i in range(len(path_list)):
		    path_list[i][0] = [(xy + offset) for (xy, offset) in zip(path_list[i][0], xy_offset)]
		self._DesignParameter['pmos_gate'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _Width=_width)
		self._DesignParameter['pmos_gate']['_XYCoordinates'] = path_list
		self._DesignParameter['METAL2_path_0'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _Width=drc._MetalxMinWidth)
		self._DesignParameter['METAL2_path_0']['_XYCoordinates'] = [[[(+ self._DesignParameter['pmos_vias']['_XYCoordinates'][0][0]), (+ self._DesignParameter['pmos_vias']['_XYCoordinates'][0][1])], [(+ self._DesignParameter['pmos_vias']['_XYCoordinates'][(- 1)][0]), (+ self._DesignParameter['pmos_vias']['_XYCoordinates'][(- 1)][1])]]]
		self._DesignParameter['POLY_boundary_13'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _XWidth=max((((self._DesignParameter['nmos']['_XYCoordinates'][0][0] + self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]) + (self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)) - ((self._DesignParameter['nmos']['_XYCoordinates'][0][0] + self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2))), (((self._DesignParameter['pmos']['_XYCoordinates'][0][0] + self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]) + (self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)) - ((self._DesignParameter['pmos']['_XYCoordinates'][0][0] + self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)))), _YWidth=self._DesignParameter['gate_contacts']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'])
		self._DesignParameter['POLY_boundary_13']['_XYCoordinates'] = [[(+ self._DesignParameter['gate_contacts']['_XYCoordinates'][0][0]), (+ self._DesignParameter['gate_contacts']['_XYCoordinates'][0][1])]]
		path_list = []
		xy_offset = [0, 0]
		if (len(self._DesignParameter['pmos_vias']['_XYCoordinates']) == 1):
		    mode = 'vertical'
		    _width = drc._MetalxMinWidth
		elif (self._DesignParameter['pmos_vias']['_XYCoordinates'][0][0] == self._DesignParameter['pmos_vias']['_XYCoordinates'][(- 1)][0]):
		    mode = 'horizontal'
		    _width = drc._MetalxMinWidth
		elif (self._DesignParameter['pmos_vias']['_XYCoordinates'][0][1] == self._DesignParameter['pmos_vias']['_XYCoordinates'][(- 1)][1]):
		    mode = 'vertical'
		    _width = drc._MetalxMinWidth
		else:
		    print('Invalid Target Input')
		if (mode == 'vertical'):
		    xy_with_offset = []
		    target_y_value = [[(+ self._DesignParameter['nmos_vias']['_XYCoordinates'][0][0]), (+ self._DesignParameter['nmos_vias']['_XYCoordinates'][0][1])]][0][1]
		    for i in range(len(self._DesignParameter['pmos_vias']['_XYCoordinates'])):
		        xy_with_offset.append([(x + y) for (x, y) in zip([0, 0], self._DesignParameter['pmos_vias']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		elif (mode == 'horizontal'):
		    xy_with_offset = []
		    target_x_value = [[(+ self._DesignParameter['nmos_vias']['_XYCoordinates'][0][0]), (+ self._DesignParameter['nmos_vias']['_XYCoordinates'][0][1])]][0][0]
		    for i in range(len(self._DesignParameter['pmos_vias']['_XYCoordinates'])):
		        xy_with_offset.append([(x + y) for (x, y) in zip([0, 0], self._DesignParameter['pmos_vias']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		for i in range(len(path_list)):
		    path_list[i][0] = [(xy + offset) for (xy, offset) in zip(path_list[i][0], xy_offset)]
		self._DesignParameter['vout_array'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _Width=_width)
		self._DesignParameter['vout_array']['_XYCoordinates'] = path_list
		if (n_gate > p_gate):
		    path_list = []
		    xy_offset = [0, 0]
		    if (len(self._DesignParameter['pmos_vias']['_XYCoordinates']) == 1):
		        mode = 'vertical'
		        _width = drc._MetalxMinWidth
		    elif (self._DesignParameter['pmos_vias']['_XYCoordinates'][0][0] == self._DesignParameter['pmos_vias']['_XYCoordinates'][(- 1)][0]):
		        mode = 'horizontal'
		        _width = drc._MetalxMinWidth
		    elif (self._DesignParameter['pmos_vias']['_XYCoordinates'][0][1] == self._DesignParameter['pmos_vias']['_XYCoordinates'][(- 1)][1]):
		        mode = 'vertical'
		        _width = drc._MetalxMinWidth
		    else:
		        print('Invalid Target Input')
		    if (mode == 'vertical'):
		        xy_with_offset = []
		        target_y_value = [[(+ self._DesignParameter['nmos_vias']['_XYCoordinates'][0][0]), (+ self._DesignParameter['nmos_vias']['_XYCoordinates'][0][1])]][0][1]
		        for i in range(len(self._DesignParameter['pmos_vias']['_XYCoordinates'])):
		            xy_with_offset.append([(x + y) for (x, y) in zip([0, 0], self._DesignParameter['pmos_vias']['_XYCoordinates'][i])])
		        for i in range(len(xy_with_offset)):
		            path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		    elif (mode == 'horizontal'):
		        xy_with_offset = []
		        target_x_value = [[(+ self._DesignParameter['nmos_vias']['_XYCoordinates'][0][0]), (+ self._DesignParameter['nmos_vias']['_XYCoordinates'][0][1])]][0][0]
		        for i in range(len(self._DesignParameter['pmos_vias']['_XYCoordinates'])):
		            xy_with_offset.append([(x + y) for (x, y) in zip([0, 0], self._DesignParameter['pmos_vias']['_XYCoordinates'][i])])
		        for i in range(len(xy_with_offset)):
		            path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		    for i in range(len(path_list)):
		        path_list[i][0] = [(xy + offset) for (xy, offset) in zip(path_list[i][0], xy_offset)]
		    self._DesignParameter['vout_array'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _Width=_width)
		    self._DesignParameter['vout_array']['_XYCoordinates'] = path_list
		else:
		    path_list = []
		    xy_offset = [0, 0]
		    if (len(self._DesignParameter['nmos_vias']['_XYCoordinates']) == 1):
		        mode = 'vertical'
		        _width = drc._MetalxMinWidth
		    elif (self._DesignParameter['nmos_vias']['_XYCoordinates'][0][0] == self._DesignParameter['nmos_vias']['_XYCoordinates'][(- 1)][0]):
		        mode = 'horizontal'
		        _width = drc._MetalxMinWidth
		    elif (self._DesignParameter['nmos_vias']['_XYCoordinates'][0][1] == self._DesignParameter['nmos_vias']['_XYCoordinates'][(- 1)][1]):
		        mode = 'vertical'
		        _width = drc._MetalxMinWidth
		    else:
		        print('Invalid Target Input')
		    if (mode == 'vertical'):
		        xy_with_offset = []
		        target_y_value = [[(+ self._DesignParameter['pmos_vias']['_XYCoordinates'][0][0]), (+ self._DesignParameter['pmos_vias']['_XYCoordinates'][0][1])]][0][1]
		        for i in range(len(self._DesignParameter['nmos_vias']['_XYCoordinates'])):
		            xy_with_offset.append([(x + y) for (x, y) in zip([0, 0], self._DesignParameter['nmos_vias']['_XYCoordinates'][i])])
		        for i in range(len(xy_with_offset)):
		            path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		    elif (mode == 'horizontal'):
		        xy_with_offset = []
		        target_x_value = [[(+ self._DesignParameter['pmos_vias']['_XYCoordinates'][0][0]), (+ self._DesignParameter['pmos_vias']['_XYCoordinates'][0][1])]][0][0]
		        for i in range(len(self._DesignParameter['nmos_vias']['_XYCoordinates'])):
		            xy_with_offset.append([(x + y) for (x, y) in zip([0, 0], self._DesignParameter['nmos_vias']['_XYCoordinates'][i])])
		        for i in range(len(xy_with_offset)):
		            path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		    for i in range(len(path_list)):
		        path_list[i][0] = [(xy + offset) for (xy, offset) in zip(path_list[i][0], xy_offset)]
		    self._DesignParameter['vout_array'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _Width=_width)
		    self._DesignParameter['vout_array']['_XYCoordinates'] = path_list
		self._DesignParameter['NWELL_boundary_0'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['NWELL'][0], _Datatype=DesignParameters._LayerMapping['NWELL'][1], _XWidth=(self._DesignParameter['vdd_supply']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth'] + (2 * drc._NwMinEnclosurePactive2)), _YWidth=((((self._DesignParameter['vdd_supply']['_XYCoordinates'][0][1] + self._DesignParameter['vdd_supply']['_DesignObj']._DesignParameter['_ODLayer']['_XYCoordinates'][0][1]) + (self._DesignParameter['vdd_supply']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth'] / 2)) - ((self._DesignParameter['pmos']['_XYCoordinates'][0][1] + self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_PPLayer']['_XYCoordinates'][0][1]) - (self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_PPLayer']['_YWidth'] / 2))) + drc._NwMinEnclosurePactive2))
		self._DesignParameter['NWELL_boundary_0']['_XYCoordinates'] = [[self._DesignParameter['pmos']['_XYCoordinates'][0][0], (((((self._DesignParameter['vdd_supply']['_XYCoordinates'][0][1] + self._DesignParameter['vdd_supply']['_DesignObj']._DesignParameter['_ODLayer']['_XYCoordinates'][0][1]) + (self._DesignParameter['vdd_supply']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth'] / 2)) + ((self._DesignParameter['pmos']['_XYCoordinates'][0][1] + self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_PPLayer']['_XYCoordinates'][0][1]) - (self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_PPLayer']['_YWidth'] / 2))) + drc._NwMinEnclosurePactive2) / 2)]]
		self._DesignParameter['SLVT_boundary_2'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['SLVT'][0], _Datatype=DesignParameters._LayerMapping['SLVT'][1], _XWidth=max(self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_SLVTLayer']['_XWidth'], self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_SLVTLayer']['_XWidth']), _YWidth=(((self._DesignParameter['pmos']['_XYCoordinates'][0][1] + self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_SLVTLayer']['_XYCoordinates'][0][1]) + (self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_SLVTLayer']['_YWidth'] / 2)) - ((self._DesignParameter['nmos']['_XYCoordinates'][0][1] + self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_SLVTLayer']['_XYCoordinates'][0][1]) - (self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_SLVTLayer']['_YWidth'] / 2))))
		self._DesignParameter['SLVT_boundary_2']['_XYCoordinates'] = [[self._DesignParameter['nmos']['_XYCoordinates'][0][0], ((((self._DesignParameter['pmos']['_XYCoordinates'][0][1] + self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_SLVTLayer']['_XYCoordinates'][0][1]) + (self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_SLVTLayer']['_YWidth'] / 2)) + ((self._DesignParameter['nmos']['_XYCoordinates'][0][1] + self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_SLVTLayer']['_XYCoordinates'][0][1]) - (self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_SLVTLayer']['_YWidth'] / 2))) / 2)]]
		self._DesignParameter['METAL1_text_0'] = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1PIN'][0], _Datatype=DesignParameters._LayerMapping['METAL1PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0], _XYCoordinates=[[(self._DesignParameter['nmos']['_XYCoordinates'][0][0] + self._DesignParameter['vss_supply']['_XYCoordinates'][0][0]), (((((self._DesignParameter['pmos']['_XYCoordinates'][0][1] + self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_SLVTLayer']['_XYCoordinates'][0][1]) + (self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_SLVTLayer']['_YWidth'] / 2)) + ((self._DesignParameter['nmos']['_XYCoordinates'][0][1] + self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_SLVTLayer']['_XYCoordinates'][0][1]) - (self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_SLVTLayer']['_YWidth'] / 2))) / 2) + self._DesignParameter['vss_supply']['_XYCoordinates'][0][1])]], _Mag=0.1, _Angle=0, _TEXT='VSS')
		self._DesignParameter['METAL1_text_1'] = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1PIN'][0], _Datatype=DesignParameters._LayerMapping['METAL1PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0], _XYCoordinates=[[(+ self._DesignParameter['vdd_supply']['_XYCoordinates'][0][0]), (+ self._DesignParameter['vdd_supply']['_XYCoordinates'][0][1])]], _Mag=0.1, _Angle=0, _TEXT='VDD')
		self._DesignParameter['METAL2_text_0'] = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2PIN'][0], _Datatype=DesignParameters._LayerMapping['METAL2PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0], _XYCoordinates=[[self._DesignParameter['vout_array']['_XYCoordinates'][(- 1)][0][0], ((self._DesignParameter['vout_array']['_XYCoordinates'][0][0][1] + self._DesignParameter['vout_array']['_XYCoordinates'][0][(- 1)][1]) / 2)]], _Mag=0.1, _Angle=0, _TEXT='VOUT')
		self._DesignParameter['METAL1_text_2'] = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1PIN'][0], _Datatype=DesignParameters._LayerMapping['METAL1PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0], _XYCoordinates=[[(self._DesignParameter['vout_array']['_XYCoordinates'][(- 1)][0][0] + self._DesignParameter['gate_contacts']['_XYCoordinates'][0][0]), (((self._DesignParameter['vout_array']['_XYCoordinates'][0][0][1] + self._DesignParameter['vout_array']['_XYCoordinates'][0][(- 1)][1]) / 2) + self._DesignParameter['gate_contacts']['_XYCoordinates'][0][1])]], _Mag=0.1, _Angle=0, _TEXT='VIN')
		self._DesignParameter['METAL2_path_2'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _Width=50)
		self._DesignParameter['METAL2_path_2']['_XYCoordinates'] = [[[(- 97), 362], [(- 97), 1600]]]
		self._DesignParameter['METAL2_path_3'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _Width=50)
		self._DesignParameter['METAL2_path_3']['_XYCoordinates'] = [[[291, 362], [291, 1600]]]




#### control+/ -> 여러줄 주석처리
#
if __name__ == '__main__':

	InputParams = dict(
		n_gate= 3,
		n_width= 600,
		n_length= 80,
		dummy= False,
		p_gate= 3,
		p_width= 1200,
		p_length= 80,
		supply_coy= 2,
		supply_height= 2600
	)

	# Generate Layout Object
	LayoutObj = _inverter_ksh(_DesignParameter=None, _Name='Inverter_ksh')
	LayoutObj._CalculateDesignParameter(**InputParams)
	LayoutObj._UpdateDesignParameter2GDSStructure(_DesignParameterInDictionary=LayoutObj._DesignParameter)
	testStreamFile = open('./{}'.format('Inverter_ksh.gds'), 'wb')
	tmp = LayoutObj._CreateGDSStream(LayoutObj._DesignParameter['_GDSFile']['_GDSFile'])
	tmp.write_binary_gds_stream(testStreamFile)
	testStreamFile.close()

	print('##########################   Finished   ##########################')
