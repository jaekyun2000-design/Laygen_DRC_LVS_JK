from generatorLib import StickDiagram
from generatorLib import DesignParameters
import copy
import math
from generatorLib import DRC
from generatorLib.generator_models import NbodyContact
from generatorLib.generator_models import PbodyContact
from generatorLib.generator_models import PMOSWithDummy
from generatorLib.generator_models import NMOSWithDummy
from generatorLib.generator_models import ViaMet12Met2
from generatorLib.generator_models import ViaMet22Met3
from generatorLib.generator_models import ViaMet32Met4
from generatorLib.generator_models import ViaMet42Met5
from generatorLib.generator_models import ViaMet52Met6
from generatorLib.generator_models import ViaPoly2Met1

class Idac_cell(StickDiagram._StickDiagram):
	def __init__(self, _DesignParameter=None, _Name='idac_cell'):
		if _DesignParameter != None:
			self._DesignParameter = _DesignParameter
		else:
			self._DesignParameter = dict(_Name=self._NameDeclaration(_Name=_Name), _GDSFile=self._GDSObjDeclaration(_GDSFile=None))
		self._DesignParameter['_Name']['Name'] = _Name

	def _CalculateDesignParameter(self,Cell_height=2108,Odd_row_flag=0,nf_aoi_out_pmos=1,W_aoi_out_pmos=1000,L_aoi_out_pmos=30,aoi_out_pmos_y=1000,aoi_XVT='RVT',nf_pbias_pmos=2,W_pbias_pmos=830,L_pbias_pmos=300,pbias_pmos_XVT='LVT',nf_AOI_mos=1,W_AOI_pmos=200,W_AOI_nmos=200,L_AOI_mos=30,VDD2aoi_pmos=58,VSS2aoi_nmos=85):
	
		drc = DRC.DRC()
		_Name = self._DesignParameter['_Name']['_Name']
		
		self._DesignParameter['VSS'] = self._SrefElementDeclaration(_DesignObj=PbodyContact._PbodyContact(_Name='VSSIn{}'.format(_Name)))[0]
		self._DesignParameter['VSS']['_DesignObj']._CalculatePbodyContactDesignParameter(**dict(_NumberOfPbodyCOX=20, _NumberOfPbodyCOY=2, _Met1XWidth=None, _Met1YWidth=None))
		self._DesignParameter['VSS']['_XYCoordinates'] = [[0.0, 0.0]]
		self._DesignParameter['VDD'] = self._SrefElementDeclaration(_DesignObj=NbodyContact._NbodyContact(_Name='VDDIn{}'.format(_Name)))[0]
		self._DesignParameter['VDD']['_DesignObj']._CalculateNbodyContactDesignParameter(**dict(_NumberOfNbodyCOX=20, _NumberOfNbodyCOY=4, _Met1XWidth=None, _Met1YWidth=None))
		self._DesignParameter['VDD']['_XYCoordinates'] = [[self._DesignParameter['VSS']['_XYCoordinates'][0][0], (self._DesignParameter['VSS']['_XYCoordinates'][0][1] + Cell_height)]]

		self._DesignParameter['_VDDpin'] = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1PIN'][0], _Datatype=DesignParameters._LayerMapping['METAL1PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0], _XYCoordinates=[[0, 0]], _Mag=0.05, _Angle=0, _TEXT='VDD')
		self._DesignParameter['_VSSpin'] = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1PIN'][0], _Datatype=DesignParameters._LayerMapping['METAL1PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0], _XYCoordinates=[[0, 0]], _Mag=0.05, _Angle=0, _TEXT='VSS')
		self._DesignParameter['_VDDpin']['_XYCoordinates'] = self._DesignParameter['VDD']['_XYCoordinates']
		self._DesignParameter['_VSSpin']['_XYCoordinates'] = self._DesignParameter['VSS']['_XYCoordinates']

		self._DesignParameter['aoi_out_pmos'] = self._SrefElementDeclaration(_DesignObj=PMOSWithDummy._PMOS(_Name='aoi_out_pmosIn{}'.format(_Name)))[0]
		self._DesignParameter['aoi_out_pmos']['_DesignObj']._CalculatePMOSDesignParameter(**dict(_PMOSNumberofGate=nf_aoi_out_pmos, _PMOSChannelWidth=W_aoi_out_pmos, _PMOSChannellength=L_aoi_out_pmos, _PMOSDummy=True, _GateSpacing=None, _SDWidth=None, _XVT=aoi_XVT, _PCCrit=False))
		self._DesignParameter['aoi_out_pmos']['_XYCoordinates'] = [[self._DesignParameter['VSS']['_XYCoordinates'][0][0], (self._DesignParameter['VSS']['_XYCoordinates'][0][1] + aoi_out_pmos_y)]]
		self._DesignParameter['pbias_pmos'] = self._SrefElementDeclaration(_DesignObj=PMOSWithDummy._PMOS(_Name='pbias_pmosIn{}'.format(_Name)))[0]
		self._DesignParameter['pbias_pmos']['_DesignObj']._CalculatePMOSDesignParameter(**dict(_PMOSNumberofGate=nf_pbias_pmos, _PMOSChannelWidth=W_pbias_pmos, _PMOSChannellength=L_pbias_pmos, _PMOSDummy=False, _GateSpacing=None, _SDWidth=None, _XVT=pbias_pmos_XVT, _PCCrit=False))
		self._DesignParameter['pbias_pmos']['_XYCoordinates'] = [[(((self._DesignParameter['aoi_out_pmos']['_XYCoordinates'][0][0]) + self._DesignParameter['aoi_out_pmos']['_DesignObj']._DesignParameter['_PPLayer']['_XYCoordinates'][0][0]) + (self._DesignParameter['aoi_out_pmos']['_DesignObj']._DesignParameter['_PPLayer']['_XWidth'] / 2)) + (self._DesignParameter['pbias_pmos']['_DesignObj']._DesignParameter['_PPLayer']['_XWidth'] / 2),
																  (((self._DesignParameter['aoi_out_pmos']['_XYCoordinates'][0][1]) + self._DesignParameter['aoi_out_pmos']['_DesignObj']._DesignParameter['_PPLayer']['_XYCoordinates'][0][1]) - (self._DesignParameter['aoi_out_pmos']['_DesignObj']._DesignParameter['_PPLayer']['_YWidth'] / 2)) + (self._DesignParameter['pbias_pmos']['_DesignObj']._DesignParameter['_PPLayer']['_YWidth'] / 2)]]

		self._DesignParameter['AOI_p3'] = self._SrefElementDeclaration(_DesignObj=PMOSWithDummy._PMOS(_Name='AOI_p3In{}'.format(_Name)))[0]
		self._DesignParameter['AOI_p3']['_DesignObj']._CalculatePMOSDesignParameter(**dict(_PMOSNumberofGate=nf_AOI_mos, _PMOSChannelWidth=W_AOI_pmos, _PMOSChannellength=L_AOI_mos, _PMOSDummy=True, _GateSpacing=None, _SDWidth=None, _XVT='RVT', _PCCrit=False))
		self._DesignParameter['AOI_p3']['_XYCoordinates'] = [[(self._DesignParameter['aoi_out_pmos']['_XYCoordinates'][0][0] - self._DesignParameter['aoi_out_pmos']['_DesignObj']._DesignParameter['_PPLayer']['_XWidth']//2 - self._DesignParameter['AOI_p3']['_DesignObj']._DesignParameter['_PPLayer']['_XWidth']//2 - drc._PolygateMinSpace2*2), self._DesignParameter['VDD']['_XYCoordinates'][0][1] - (self._DesignParameter['VDD']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // 2) - VDD2aoi_pmos - (self._DesignParameter['AOI_p3']['_DesignObj']._DesignParameter['_PPLayer']['_YWidth'] // 2)]]
		self._DesignParameter['AOI_p2'] = self._SrefElementDeclaration(_DesignObj=PMOSWithDummy._PMOS(_Name='AOI_p2In{}'.format(_Name)))[0]
		self._DesignParameter['AOI_p2']['_DesignObj']._CalculatePMOSDesignParameter(**dict(_PMOSNumberofGate=nf_AOI_mos, _PMOSChannelWidth=W_AOI_pmos, _PMOSChannellength=L_AOI_mos, _PMOSDummy=True, _GateSpacing=None, _SDWidth=None, _XVT='RVT', _PCCrit=False))
		self._DesignParameter['AOI_p2']['_XYCoordinates'] = [[self._DesignParameter['AOI_p3']['_XYCoordinates'][0][0] - self._DesignParameter['AOI_p3']['_DesignObj']._DesignParameter['_RVTLayer']['_XWidth'], self._DesignParameter['AOI_p3']['_XYCoordinates'][0][1]]]
		self._DesignParameter['AOI_p1'] = self._SrefElementDeclaration(_DesignObj=PMOSWithDummy._PMOS(_Name='AOI_p1In{}'.format(_Name)))[0]
		self._DesignParameter['AOI_p1']['_DesignObj']._CalculatePMOSDesignParameter(**dict(_PMOSNumberofGate=nf_AOI_mos, _PMOSChannelWidth=W_AOI_pmos, _PMOSChannellength=L_AOI_mos, _PMOSDummy=True, _GateSpacing=None, _SDWidth=None, _XVT='RVT', _PCCrit=False))
		self._DesignParameter['AOI_p1']['_XYCoordinates'] = [[self._DesignParameter['AOI_p2']['_XYCoordinates'][0][0] - self._DesignParameter['AOI_p3']['_DesignObj']._DesignParameter['_RVTLayer']['_XWidth'], self._DesignParameter['AOI_p3']['_XYCoordinates'][0][1]]]

		self._DesignParameter['AOI_n3'] = self._SrefElementDeclaration(_DesignObj=NMOSWithDummy._NMOS(_Name='AOI_n3In{}'.format(_Name)))[0]
		self._DesignParameter['AOI_n3']['_DesignObj']._CalculateNMOSDesignParameter(**dict(_NMOSNumberofGate=nf_AOI_mos, _NMOSChannelWidth=W_AOI_nmos, _NMOSChannellength=L_AOI_mos, _NMOSDummy=True, _GateSpacing=None, _SDWidth=None, _XVT='RVT', _PCCrit=False))
		self._DesignParameter['AOI_n3']['_XYCoordinates'] = [[self._DesignParameter['AOI_p3']['_XYCoordinates'][0][0], self._DesignParameter['VSS']['_XYCoordinates'][0][1] + (self._DesignParameter['VSS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // 2)+(self._DesignParameter['AOI_n3']['_DesignObj']._DesignParameter['_RVTLayer']['_YWidth'] // 2)+ VSS2aoi_nmos]]
		self._DesignParameter['AOI_n2'] = self._SrefElementDeclaration(_DesignObj=NMOSWithDummy._NMOS(_Name='AOI_n2In{}'.format(_Name)))[0]
		self._DesignParameter['AOI_n2']['_DesignObj']._CalculateNMOSDesignParameter(**dict(_NMOSNumberofGate=nf_AOI_mos, _NMOSChannelWidth=W_AOI_nmos, _NMOSChannellength=L_AOI_mos, _NMOSDummy=True, _GateSpacing=None, _SDWidth=None, _XVT='RVT', _PCCrit=False))
		self._DesignParameter['AOI_n2']['_XYCoordinates'] = [[self._DesignParameter['AOI_p2']['_XYCoordinates'][0][0], self._DesignParameter['VSS']['_XYCoordinates'][0][1] + (self._DesignParameter['VSS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // 2)+(self._DesignParameter['AOI_n3']['_DesignObj']._DesignParameter['_RVTLayer']['_YWidth'] // 2)+ VSS2aoi_nmos]]
		self._DesignParameter['AOI_n1'] = self._SrefElementDeclaration(_DesignObj=NMOSWithDummy._NMOS(_Name='AOI_n1In{}'.format(_Name)))[0]
		self._DesignParameter['AOI_n1']['_DesignObj']._CalculateNMOSDesignParameter(**dict(_NMOSNumberofGate=nf_AOI_mos, _NMOSChannelWidth=W_AOI_nmos, _NMOSChannellength=L_AOI_mos, _NMOSDummy=True, _GateSpacing=None, _SDWidth=None, _XVT='RVT', _PCCrit=False))
		self._DesignParameter['AOI_n1']['_XYCoordinates'] = [[self._DesignParameter['AOI_p1']['_XYCoordinates'][0][0], self._DesignParameter['VSS']['_XYCoordinates'][0][1] + (self._DesignParameter['VSS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // 2)+(self._DesignParameter['AOI_n3']['_DesignObj']._DesignParameter['_RVTLayer']['_YWidth'] // 2)+ VSS2aoi_nmos]]

		##PC drawing
		self._DesignParameter['AOI_p1_n1'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _Width=L_AOI_mos)
		self._DesignParameter['AOI_p2_n2'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _Width=L_AOI_mos)
		self._DesignParameter['AOI_p3_n3'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _Width=L_AOI_mos)
		tmp_p1n1 = [[]]
		tmp_p2n2 = [[]]
		tmp_p3n3 = [[]]

		for i in range (0,nf_AOI_mos) :
			tmp_p1n1.append([[(+ ((self._DesignParameter['AOI_n1']['_XYCoordinates'][0][0]) + self._DesignParameter['AOI_n1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0])),
							  (+ ((self._DesignParameter['AOI_n1']['_XYCoordinates'][0][1]) + self._DesignParameter['AOI_n1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][1]))],
							 [(+ ((self._DesignParameter['AOI_p1']['_XYCoordinates'][0][0]) + self._DesignParameter['AOI_p1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0])),
							  (+ ((self._DesignParameter['AOI_p1']['_XYCoordinates'][0][1]) + self._DesignParameter['AOI_p1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][1]))]])
			tmp_p2n2.append([[(+ ((self._DesignParameter['AOI_n2']['_XYCoordinates'][0][0]) + self._DesignParameter['AOI_n2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0])),
							  (+ ((self._DesignParameter['AOI_n2']['_XYCoordinates'][0][1]) + self._DesignParameter['AOI_n2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][1]))],
							 [(+ ((self._DesignParameter['AOI_p2']['_XYCoordinates'][0][0]) + self._DesignParameter['AOI_p2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0])),
							  (+ ((self._DesignParameter['AOI_p2']['_XYCoordinates'][0][1]) + self._DesignParameter['AOI_p2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][1]))]])
			tmp_p3n3.append([[(+ ((self._DesignParameter['AOI_n3']['_XYCoordinates'][0][0]) + self._DesignParameter['AOI_n3']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0])),
							  (+ ((self._DesignParameter['AOI_n3']['_XYCoordinates'][0][1]) + self._DesignParameter['AOI_n3']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][1]))],
							 [(+ ((self._DesignParameter['AOI_p3']['_XYCoordinates'][0][0]) + self._DesignParameter['AOI_p3']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0])),
							  (+ ((self._DesignParameter['AOI_p3']['_XYCoordinates'][0][1]) + self._DesignParameter['AOI_p3']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][1]))]])

		self._DesignParameter['AOI_p1_n1']['_XYCoordinates'] = tmp_p1n1
		self._DesignParameter['AOI_p2_n2']['_XYCoordinates'] = tmp_p2n2
		self._DesignParameter['AOI_p3_n3']['_XYCoordinates'] = tmp_p3n3

		del tmp_p1n1, tmp_p2n2, tmp_p3n3

		##VDD routing
		self._DesignParameter['VDD_AOI_p1'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=self._DesignParameter['AOI_p1']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'])
		self._DesignParameter['VDD_AOI_p2'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=self._DesignParameter['AOI_p2']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'])
		tmp_VDDp1 = [[]]
		tmp_VDDp2 = [[]]


		for i in range(0, nf_AOI_mos//2+1):
			tmp_VDDp1.append([[(+ ((self._DesignParameter['AOI_p1']['_XYCoordinates'][0][0]) + self._DesignParameter['AOI_p1']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][2*i][0])),
							  self._DesignParameter['VDD']['_XYCoordinates'][0][1]],
							 [(+ ((self._DesignParameter['AOI_p1']['_XYCoordinates'][0][0]) + self._DesignParameter['AOI_p1']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][2*i][0])),
							  (+ ((self._DesignParameter['AOI_p1']['_XYCoordinates'][0][1]) + self._DesignParameter['AOI_p1']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][2*i][1]))]])
			tmp_VDDp2.append([[(+ ((self._DesignParameter['AOI_p2']['_XYCoordinates'][0][0]) + self._DesignParameter['AOI_p2']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][2*i][0])),
							  self._DesignParameter['VDD']['_XYCoordinates'][0][1]],
							 [(+ ((self._DesignParameter['AOI_p2']['_XYCoordinates'][0][0]) + self._DesignParameter['AOI_p2']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][2*i][0])),
							  (+ ((self._DesignParameter['AOI_p2']['_XYCoordinates'][0][1]) + self._DesignParameter['AOI_p2']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][2*i][1]))]])

		self._DesignParameter['VDD_AOI_p1']['_XYCoordinates'] = tmp_VDDp1
		self._DesignParameter['VDD_AOI_p2']['_XYCoordinates'] = tmp_VDDp2

		del tmp_VDDp1, tmp_VDDp2

		##VSS routing
		self._DesignParameter['VSS_AOI_n1'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=self._DesignParameter['AOI_p1']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'])
		self._DesignParameter['VSS_AOI_n3'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=self._DesignParameter['AOI_p3']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'])
		tmp_VSSn1 = [[]]
		tmp_VSSn3 = [[]]

		for i in range(0, nf_AOI_mos//2+1):
			tmp_VSSn1.append([[(+ ((self._DesignParameter['AOI_n1']['_XYCoordinates'][0][0]) + self._DesignParameter['AOI_n1']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][2*i][0])),
							  self._DesignParameter['VSS']['_XYCoordinates'][0][1]],
							 [(+ ((self._DesignParameter['AOI_n1']['_XYCoordinates'][0][0]) + self._DesignParameter['AOI_n1']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][2*i][0])),
							  (+ ((self._DesignParameter['AOI_n1']['_XYCoordinates'][0][1]) + self._DesignParameter['AOI_n1']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][2*i][1]))]])
			tmp_VSSn3.append([[(+ ((self._DesignParameter['AOI_n3']['_XYCoordinates'][0][0]) + self._DesignParameter['AOI_n3']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][2*i][0])),
							  self._DesignParameter['VSS']['_XYCoordinates'][0][1]],
							 [(+ ((self._DesignParameter['AOI_n3']['_XYCoordinates'][0][0]) + self._DesignParameter['AOI_n3']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][2*i][0])),
							  (+ ((self._DesignParameter['AOI_n3']['_XYCoordinates'][0][1]) + self._DesignParameter['AOI_n3']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][2*i][1]))]])

		self._DesignParameter['VSS_AOI_n1']['_XYCoordinates'] = tmp_VSSn1
		self._DesignParameter['VSS_AOI_n3']['_XYCoordinates'] = tmp_VSSn3

		del tmp_VSSn1, tmp_VSSn3

		##pmos via calculation
		YWidthOfPMOSMet1 = self._DesignParameter['AOI_p1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']
		NumViaYPMOS = int((YWidthOfPMOSMet1 - 2 * drc._Metal1MinEnclosureVia3) / (drc._VIAxMinWidth + drc._VIAxMinSpace)) + 1

		VIAPMOSMet12 = copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation)
		VIAPMOSMet12['_ViaMet12Met2NumberOfCOX'] = 1
		VIAPMOSMet12['_ViaMet12Met2NumberOfCOY'] = NumViaYPMOS if (NumViaYPMOS > 2) else 2

		##aoi_p1_to_p3 via
		self._DesignParameter['aoi_p1_to_p3'] = self._SrefElementDeclaration(
			_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='aoi_p1_to_p3In{}'.format(_Name)))[0]
		self._DesignParameter['aoi_p1_to_p3']['_DesignObj']._CalculateDesignParameterSameEnclosure(**VIAPMOSMet12)

		# 1-1) Metal1 YWidth re-calculation
		self._DesignParameter['aoi_p1_to_p3']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] \
			= max(self.getYWidth('aoi_p1_to_p3', '_Met1Layer'), self.getYWidth('AOI_p1', '_Met1Layer'))

		Area_M1for_aoi_p1_to_p3 = self.getXWidth('aoi_p1_to_p3', '_Met1Layer') \
											  * self.getYWidth('aoi_p1_to_p3', '_Met1Layer')
		if Area_M1for_aoi_p1_to_p3 < drc._Metal1MinArea:
			YWidth_recalculated_byMinArea = self.CeilMinSnapSpacing(drc._Metal1MinArea / self.getXWidth('aoi_p1_to_p3', '_Met1Layer'), 2 * drc._MinSnapSpacing)
			self._DesignParameter['aoi_p1_to_p3']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] = YWidth_recalculated_byMinArea
		else:
			pass

		self._DesignParameter['aoi_p1_to_p3']['_XYCoordinates'] = None
		XYList = []
		xy_offset = [0, 0]
		for i in range(len(self._DesignParameter['AOI_p1']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'])):
		    if ((i % 2) == 1):
		        xy = (self._DesignParameter['AOI_p1']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i][0] if (type(self._DesignParameter['AOI_p1']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i][0]) == list) else self._DesignParameter['AOI_p1']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i])
		        XYList.append([((x + y) + z) for (x, y, z) in zip([(self._DesignParameter['AOI_p1']['_XYCoordinates'][0][0]), (self._DesignParameter['AOI_p1']['_XYCoordinates'][0][1])], xy, xy_offset)])
		self._DesignParameter['aoi_p1_to_p3']['_XYCoordinates'] = XYList

		##aoi_p2_to_p3 via
		self._DesignParameter['aoi_p2_to_p3'] = self._SrefElementDeclaration(
			_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='aoi_p2_to_p3In{}'.format(_Name)))[0]
		self._DesignParameter['aoi_p2_to_p3']['_DesignObj']._CalculateDesignParameterSameEnclosure(**VIAPMOSMet12)

		# 1-1) Metal1 YWidth re-calculation
		self._DesignParameter['aoi_p2_to_p3']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] \
			= max(self.getYWidth('aoi_p2_to_p3', '_Met1Layer'), self.getYWidth('AOI_p2', '_Met1Layer'))

		Area_M1for_aoi_p2_to_p3 = self.getXWidth('aoi_p2_to_p3', '_Met1Layer') \
											  * self.getYWidth('aoi_p2_to_p3', '_Met1Layer')
		if Area_M1for_aoi_p2_to_p3 < drc._Metal1MinArea:
			YWidth_recalculated_byMinArea = self.CeilMinSnapSpacing(drc._Metal1MinArea / self.getXWidth('aoi_p2_to_p3', '_Met1Layer'), 2 * drc._MinSnapSpacing)
			self._DesignParameter['aoi_p2_to_p3']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] = YWidth_recalculated_byMinArea
		else:
			pass

		self._DesignParameter['aoi_p2_to_p3']['_XYCoordinates'] = None
		XYList = []
		xy_offset = [0, 0]
		for i in range(len(self._DesignParameter['AOI_p2']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'])):
		    if ((i % 2) == 1):
		        xy = (self._DesignParameter['AOI_p2']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i][0] if (type(self._DesignParameter['AOI_p2']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i][0]) == list) else self._DesignParameter['AOI_p2']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i])
		        XYList.append([((x + y) + z) for (x, y, z) in zip([(self._DesignParameter['AOI_p2']['_XYCoordinates'][0][0]), (self._DesignParameter['AOI_p2']['_XYCoordinates'][0][1])], xy, xy_offset)])
		self._DesignParameter['aoi_p2_to_p3']['_XYCoordinates'] = XYList


		##aoi_p3_out via
		self._DesignParameter['aoi_p3_out'] = self._SrefElementDeclaration(
			_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='aoi_p3_outIn{}'.format(_Name)))[0]
		self._DesignParameter['aoi_p3_out']['_DesignObj']._CalculateDesignParameterSameEnclosure(**VIAPMOSMet12)

		# 1-1) Metal1 YWidth re-calculation
		self._DesignParameter['aoi_p3_out']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] \
			= max(self.getYWidth('aoi_p3_out', '_Met1Layer'), self.getYWidth('AOI_p3', '_Met1Layer'))

		Area_M1for_aoi_p3_out = self.getXWidth('aoi_p3_out', '_Met1Layer') \
											  * self.getYWidth('aoi_p3_out', '_Met1Layer')
		if Area_M1for_aoi_p3_out < drc._Metal1MinArea:
			YWidth_recalculated_byMinArea = self.CeilMinSnapSpacing(drc._Metal1MinArea / self.getXWidth('aoi_p3_out', '_Met1Layer'), 2 * drc._MinSnapSpacing)
			self._DesignParameter['aoi_p3_out']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] = YWidth_recalculated_byMinArea
		else:
			pass

		self._DesignParameter['aoi_p3_out']['_XYCoordinates'] = None
		XYList = []
		xy_offset = [0, 0]
		for i in range(len(self._DesignParameter['AOI_p3']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'])):
		    if ((i % 2) == 1):
		        xy = (self._DesignParameter['AOI_p3']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i][0] if (type(self._DesignParameter['AOI_p3']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i][0]) == list) else self._DesignParameter['AOI_p3']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i])
		        XYList.append([((x + y) + z) for (x, y, z) in zip([(self._DesignParameter['AOI_p3']['_XYCoordinates'][0][0]), (self._DesignParameter['AOI_p3']['_XYCoordinates'][0][1])], xy, xy_offset)])
		self._DesignParameter['aoi_p3_out']['_XYCoordinates'] = XYList
		# ##aoi_p3_input via
		# self._DesignParameter['aoi_p3_input'] = self._SrefElementDeclaration(
		# 	_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='aoi_p3_inputIn{}'.format(_Name)))[0]
		# self._DesignParameter['aoi_p3_input']['_DesignObj']._CalculateDesignParameterSameEnclosure(**VIAPMOSMet12)
		#
		# # 1-1) Metal1 YWidth re-calculation
		# self._DesignParameter['aoi_p3_input']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] \
		# 	= max(self.getYWidth('aoi_p3_input', '_Met1Layer'), self.getYWidth('AOI_p3', '_Met1Layer'))
		#
		# Area_M1for_aoi_p3_input = self.getXWidth('aoi_p3_input', '_Met1Layer') \
		# 									  * self.getYWidth('aoi_p3_input', '_Met1Layer')
		# if Area_M1for_aoi_p3_input < drc._Metal1MinArea:
		# 	YWidth_recalculated_byMinArea = self.CeilMinSnapSpacing(drc._Metal1MinArea / self.getXWidth('aoi_p3_input', '_Met1Layer'), 2 * drc._MinSnapSpacing)
		# 	self._DesignParameter['aoi_p3_input']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] = YWidth_recalculated_byMinArea
		# else:
		# 	pass
		#
		# self._DesignParameter['aoi_p3_input']['_XYCoordinates'] = None
		# XYList = []
		# xy_offset = [0, 0]
		# for i in range(len(self._DesignParameter['AOI_p3']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'])):
		#     if ((i % 2) == 0):
		#         xy = (self._DesignParameter['AOI_p3']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i][0] if (type(self._DesignParameter['AOI_p3']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i][0]) == list) else self._DesignParameter['AOI_p3']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i])
		#         XYList.append([((x + y) + z) for (x, y, z) in zip([(self._DesignParameter['AOI_p3']['_XYCoordinates'][0][0]), (self._DesignParameter['AOI_p3']['_XYCoordinates'][0][1])], xy, xy_offset)])
		# self._DesignParameter['aoi_p3_input']['_XYCoordinates'] = XYList

		self._DesignParameter['aoi_p1p2_to_p3in'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _Width=self._DesignParameter['aoi_p1_to_p3']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth'])
		self._DesignParameter['aoi_p1p2_to_p3in']['_XYCoordinates'] = [[[(+ self._DesignParameter['aoi_p1_to_p3']['_XYCoordinates'][0][0]), (+ self._DesignParameter['aoi_p1_to_p3']['_XYCoordinates'][0][1])], [(+ self._DesignParameter['aoi_p2_to_p3']['_XYCoordinates'][(- 1)][0]), (+ self._DesignParameter['aoi_p2_to_p3']['_XYCoordinates'][(- 1)][1])]]]

		self._DesignParameter['aoi_p3_out_m2'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _Width=self._DesignParameter['aoi_p3_out']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth'])
		self._DesignParameter['aoi_p3_out_m2']['_XYCoordinates'] = [[[(+ (self._DesignParameter['aoi_p3_out']['_XYCoordinates'][0][0])), (+ (self._DesignParameter['aoi_p3_out']['_XYCoordinates'][0][1]))], [(+ (self._DesignParameter['aoi_p3_out']['_XYCoordinates'][(- 1)][0])), (+ (self._DesignParameter['aoi_p3_out']['_XYCoordinates'][(- 1)][1]))]]]


		##nmos via calculation
		YWidthOfNMOSMet1 = self._DesignParameter['AOI_n1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']
		NumViaYNMOS = int((YWidthOfNMOSMet1 - 2 * drc._Metal1MinEnclosureVia3) / (drc._VIAxMinWidth + drc._VIAxMinSpace)) + 1

		VIANMOSMet12 = copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation)
		VIANMOSMet12['_ViaMet12Met2NumberOfCOX'] = 1
		VIANMOSMet12['_ViaMet12Met2NumberOfCOY'] = NumViaYNMOS if (NumViaYNMOS > 2) else 2

		##aoi_n3_out via
		self._DesignParameter['aoi_n3_out'] = self._SrefElementDeclaration(
			_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='aoi_n3_outIn{}'.format(_Name)))[0]
		self._DesignParameter['aoi_n3_out']['_DesignObj']._CalculateDesignParameterSameEnclosure(**VIAPMOSMet12)

		# 1-1) Metal1 YWidth re-calculation
		self._DesignParameter['aoi_n3_out']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] \
			= max(self.getYWidth('aoi_n3_out', '_Met1Layer'), self.getYWidth('AOI_n3', '_Met1Layer'))

		Area_M1for_aoi_n3_out = self.getXWidth('aoi_n3_out', '_Met1Layer') \
											  * self.getYWidth('aoi_n3_out', '_Met1Layer')
		if Area_M1for_aoi_n3_out < drc._Metal1MinArea:
			YWidth_recalculated_byMinArea = self.CeilMinSnapSpacing(drc._Metal1MinArea / self.getXWidth('aoi_n3_out', '_Met1Layer'), 2 * drc._MinSnapSpacing)
			self._DesignParameter['aoi_n3_out']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] = YWidth_recalculated_byMinArea
		else:
			pass

		self._DesignParameter['aoi_n3_out']['_XYCoordinates'] = None
		XYList = []
		xy_offset = [0, 0]
		for i in range(len(self._DesignParameter['AOI_n3']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'])):
		    if ((i % 2) == 1):
		        xy = (self._DesignParameter['AOI_n3']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i][0] if (type(self._DesignParameter['AOI_n3']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i][0]) == list) else self._DesignParameter['AOI_n3']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i])
		        XYList.append([((x + y) + z) for (x, y, z) in zip([(self._DesignParameter['AOI_n3']['_XYCoordinates'][0][0]), (self._DesignParameter['AOI_n3']['_XYCoordinates'][0][1])], xy, xy_offset)])
		self._DesignParameter['aoi_n3_out']['_XYCoordinates'] = XYList

		##aoi_n2_in via
		self._DesignParameter['aoi_n2_in'] = self._SrefElementDeclaration(
			_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='aoi_n2_inIn{}'.format(_Name)))[0]
		self._DesignParameter['aoi_n2_in']['_DesignObj']._CalculateDesignParameterSameEnclosure(**VIAPMOSMet12)

		# 1-1) Metal1 YWidth re-calculation
		self._DesignParameter['aoi_n2_in']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] \
			= max(self.getYWidth('aoi_n2_in', '_Met1Layer'), self.getYWidth('AOI_n2', '_Met1Layer'))

		Area_M1for_aoi_n3_out = self.getXWidth('aoi_n2_in', '_Met1Layer') \
											  * self.getYWidth('aoi_n2_in', '_Met1Layer')
		if Area_M1for_aoi_n3_out < drc._Metal1MinArea:
			YWidth_recalculated_byMinArea = self.CeilMinSnapSpacing(drc._Metal1MinArea / self.getXWidth('aoi_n2_in', '_Met1Layer'), 2 * drc._MinSnapSpacing)
			self._DesignParameter['aoi_n2_in']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] = YWidth_recalculated_byMinArea
		else:
			pass

		self._DesignParameter['aoi_n2_in']['_XYCoordinates'] = None
		XYList = []
		xy_offset = [0, 0]
		for i in range(len(self._DesignParameter['AOI_n2']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'])):
		    if ((i % 2) == 1):
		        xy = (self._DesignParameter['AOI_n2']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i][0] if (type(self._DesignParameter['AOI_n2']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i][0]) == list) else self._DesignParameter['AOI_n2']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i])
		        XYList.append([((x + y) + z) for (x, y, z) in zip([(self._DesignParameter['AOI_n2']['_XYCoordinates'][0][0]), (self._DesignParameter['AOI_n2']['_XYCoordinates'][0][1])], xy, xy_offset)])
		self._DesignParameter['aoi_n2_in']['_XYCoordinates'] = XYList
		self._DesignParameter['aoi_n3_to_n2'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _Width=self._DesignParameter['aoi_n2_in']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth'])
		self._DesignParameter['aoi_n3_to_n2']['_XYCoordinates'] = [[[(+ self._DesignParameter['aoi_n2_in']['_XYCoordinates'][0][0]), (+ self._DesignParameter['aoi_n2_in']['_XYCoordinates'][0][1])], [(+ self._DesignParameter['aoi_n3_out']['_XYCoordinates'][(- 1)][0]), (+ self._DesignParameter['aoi_n3_out']['_XYCoordinates'][(- 1)][1])]]]
		self._DesignParameter['n1p1_gate_via_1'] = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_Name='n1p1_gate_via_1In{}'.format(_Name)))[0]
		self._DesignParameter['n1p1_gate_via_1']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(**dict(_ViaPoly2Met1NumberOfCOX=1, _ViaPoly2Met1NumberOfCOY=2))
		self._DesignParameter['n1p1_gate_via_1']['_XYCoordinates'] = [[((self._DesignParameter['AOI_p1']['_XYCoordinates'][0][0]) + self._DesignParameter['AOI_p1']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][0]), (((((self._DesignParameter['AOI_p1']['_XYCoordinates'][0][1]) + self._DesignParameter['AOI_p1']['_DesignObj']._DesignParameter['_RVTLayer']['_XYCoordinates'][0][1]) - (self._DesignParameter['AOI_p1']['_DesignObj']._DesignParameter['_RVTLayer']['_YWidth'] / 2)) / 2) + ((((self._DesignParameter['AOI_n1']['_XYCoordinates'][0][1]) + self._DesignParameter['AOI_n1']['_DesignObj']._DesignParameter['_RVTLayer']['_XYCoordinates'][0][1]) + (self._DesignParameter['AOI_n1']['_DesignObj']._DesignParameter['_RVTLayer']['_YWidth'] / 2)) / 2))]]
		self._DesignParameter['n1p1_gate_via_2'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='n1p1_gate_via_2In{}'.format(_Name)))[0]
		self._DesignParameter['n1p1_gate_via_2']['_DesignObj']._CalculateDesignParameterSameEnclosure(**dict(_ViaMet12Met2NumberOfCOX=1, _ViaMet12Met2NumberOfCOY=2))
		self._DesignParameter['n1p1_gate_via_2']['_XYCoordinates'] = [[((self._DesignParameter['AOI_p1']['_XYCoordinates'][0][0]) + self._DesignParameter['AOI_p1']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][0]), (((((self._DesignParameter['AOI_p1']['_XYCoordinates'][0][1]) + self._DesignParameter['AOI_p1']['_DesignObj']._DesignParameter['_RVTLayer']['_XYCoordinates'][0][1]) - (self._DesignParameter['AOI_p1']['_DesignObj']._DesignParameter['_RVTLayer']['_YWidth'] / 2)) / 2) + ((((self._DesignParameter['AOI_n1']['_XYCoordinates'][0][1]) + self._DesignParameter['AOI_n1']['_DesignObj']._DesignParameter['_RVTLayer']['_XYCoordinates'][0][1]) + (self._DesignParameter['AOI_n1']['_DesignObj']._DesignParameter['_RVTLayer']['_YWidth'] / 2)) / 2))]]
		self._DesignParameter['n1p1_gate_via_3'] = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_Name='n1p1_gate_via_3In{}'.format(_Name)))[0]
		self._DesignParameter['n1p1_gate_via_3']['_DesignObj']._CalculateDesignParameterSameEnclosure(**dict(_ViaMet22Met3NumberOfCOX=1, _ViaMet22Met3NumberOfCOY=2))
		self._DesignParameter['n1p1_gate_via_3']['_XYCoordinates'] = [[((self._DesignParameter['AOI_p1']['_XYCoordinates'][0][0]) + self._DesignParameter['AOI_p1']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][0]), (((((self._DesignParameter['AOI_p1']['_XYCoordinates'][0][1]) + self._DesignParameter['AOI_p1']['_DesignObj']._DesignParameter['_RVTLayer']['_XYCoordinates'][0][1]) - (self._DesignParameter['AOI_p1']['_DesignObj']._DesignParameter['_RVTLayer']['_YWidth'] / 2)) / 2) + ((((self._DesignParameter['AOI_n1']['_XYCoordinates'][0][1]) + self._DesignParameter['AOI_n1']['_DesignObj']._DesignParameter['_RVTLayer']['_XYCoordinates'][0][1]) + (self._DesignParameter['AOI_n1']['_DesignObj']._DesignParameter['_RVTLayer']['_YWidth'] / 2)) / 2))]]
		self._DesignParameter['n1p1_gate_via_4'] = self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_Name='n1p1_gate_via_4In{}'.format(_Name)))[0]
		self._DesignParameter['n1p1_gate_via_4']['_DesignObj']._CalculateDesignParameterSameEnclosure(**dict(_ViaMet32Met4NumberOfCOX=1, _ViaMet32Met4NumberOfCOY=2))
		self._DesignParameter['n1p1_gate_via_4']['_XYCoordinates'] = [[((self._DesignParameter['AOI_p1']['_XYCoordinates'][0][0]) + self._DesignParameter['AOI_p1']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][0]), (((((self._DesignParameter['AOI_p1']['_XYCoordinates'][0][1]) + self._DesignParameter['AOI_p1']['_DesignObj']._DesignParameter['_RVTLayer']['_XYCoordinates'][0][1]) - (self._DesignParameter['AOI_p1']['_DesignObj']._DesignParameter['_RVTLayer']['_YWidth'] / 2)) / 2) + ((((self._DesignParameter['AOI_n1']['_XYCoordinates'][0][1]) + self._DesignParameter['AOI_n1']['_DesignObj']._DesignParameter['_RVTLayer']['_XYCoordinates'][0][1]) + (self._DesignParameter['AOI_n1']['_DesignObj']._DesignParameter['_RVTLayer']['_YWidth'] / 2)) / 2))]]
		self._DesignParameter['n1p1_gate_via_5'] = self._SrefElementDeclaration(_DesignObj=ViaMet42Met5._ViaMet42Met5(_Name='n1p1_gate_via_5In{}'.format(_Name)))[0]
		self._DesignParameter['n1p1_gate_via_5']['_DesignObj']._CalculateDesignParameterSameEnclosure(**dict(_ViaMet42Met5NumberOfCOX=1, _ViaMet42Met5NumberOfCOY=2))
		self._DesignParameter['n1p1_gate_via_5']['_XYCoordinates'] = [[((self._DesignParameter['AOI_p1']['_XYCoordinates'][0][0]) + self._DesignParameter['AOI_p1']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][0]), (((((self._DesignParameter['AOI_p1']['_XYCoordinates'][0][1]) + self._DesignParameter['AOI_p1']['_DesignObj']._DesignParameter['_RVTLayer']['_XYCoordinates'][0][1]) - (self._DesignParameter['AOI_p1']['_DesignObj']._DesignParameter['_RVTLayer']['_YWidth'] / 2)) / 2) + ((((self._DesignParameter['AOI_n1']['_XYCoordinates'][0][1]) + self._DesignParameter['AOI_n1']['_DesignObj']._DesignParameter['_RVTLayer']['_XYCoordinates'][0][1]) + (self._DesignParameter['AOI_n1']['_DesignObj']._DesignParameter['_RVTLayer']['_YWidth'] / 2)) / 2))]]
		self._DesignParameter['n1p1_gate_via_6'] = self._SrefElementDeclaration(_DesignObj=ViaMet52Met6._ViaMet52Met6(_Name='n1p1_gate_via_6In{}'.format(_Name)))[0]
		self._DesignParameter['n1p1_gate_via_6']['_DesignObj']._CalculateViaMet52Met6DesignParameter(**dict(_ViaMet52Met6NumberOfCOX=1, _ViaMet52Met6NumberOfCOY=2))
		self._DesignParameter['n1p1_gate_via_6']['_XYCoordinates'] = [[((self._DesignParameter['AOI_p1']['_XYCoordinates'][0][0]) + self._DesignParameter['AOI_p1']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][0]), (((((self._DesignParameter['AOI_p1']['_XYCoordinates'][0][1]) + self._DesignParameter['AOI_p1']['_DesignObj']._DesignParameter['_RVTLayer']['_XYCoordinates'][0][1]) - (self._DesignParameter['AOI_p1']['_DesignObj']._DesignParameter['_RVTLayer']['_YWidth'] / 2)) / 2) + ((((self._DesignParameter['AOI_n1']['_XYCoordinates'][0][1]) + self._DesignParameter['AOI_n1']['_DesignObj']._DesignParameter['_RVTLayer']['_XYCoordinates'][0][1]) + (self._DesignParameter['AOI_n1']['_DesignObj']._DesignParameter['_RVTLayer']['_YWidth'] / 2)) / 2))]]



		self._DesignParameter['n2p2_gate_via1'] = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_Name='n2p2_gate_via1In{}'.format(_Name)))[0]
		self._DesignParameter['n2p2_gate_via1']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(**dict(_ViaPoly2Met1NumberOfCOX=1, _ViaPoly2Met1NumberOfCOY=2))
		self._DesignParameter['n2p2_gate_via1']['_XYCoordinates'] = [[(self._DesignParameter['AOI_p2']['_XYCoordinates'][0][0]), (((((self._DesignParameter['AOI_p2']['_XYCoordinates'][0][1]) + self._DesignParameter['AOI_p2']['_DesignObj']._DesignParameter['_RVTLayer']['_XYCoordinates'][0][1]) - (self._DesignParameter['AOI_p2']['_DesignObj']._DesignParameter['_RVTLayer']['_YWidth'] / 2)) / 2) + ((((self._DesignParameter['AOI_n2']['_XYCoordinates'][0][1]) + self._DesignParameter['AOI_n2']['_DesignObj']._DesignParameter['_RVTLayer']['_XYCoordinates'][0][1]) + (self._DesignParameter['AOI_n2']['_DesignObj']._DesignParameter['_RVTLayer']['_YWidth'] / 2)) / 2))]]
		self._DesignParameter['n2p2_gate_via2'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='n2p2_gate_via2In{}'.format(_Name)))[0]
		self._DesignParameter['n2p2_gate_via2']['_DesignObj']._CalculateDesignParameterSameEnclosure(**dict(_ViaMet12Met2NumberOfCOX=1, _ViaMet12Met2NumberOfCOY=2))
		self._DesignParameter['n2p2_gate_via2']['_XYCoordinates'] = [[(self._DesignParameter['AOI_p2']['_XYCoordinates'][0][0]), (((((self._DesignParameter['AOI_p2']['_XYCoordinates'][0][1]) + self._DesignParameter['AOI_p2']['_DesignObj']._DesignParameter['_RVTLayer']['_XYCoordinates'][0][1]) - (self._DesignParameter['AOI_p2']['_DesignObj']._DesignParameter['_RVTLayer']['_YWidth'] / 2)) / 2) + ((((self._DesignParameter['AOI_n2']['_XYCoordinates'][0][1]) + self._DesignParameter['AOI_n2']['_DesignObj']._DesignParameter['_RVTLayer']['_XYCoordinates'][0][1]) + (self._DesignParameter['AOI_n2']['_DesignObj']._DesignParameter['_RVTLayer']['_YWidth'] / 2)) / 2))]]
		self._DesignParameter['n2p2_gate_via3'] = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_Name='n2p2_gate_via3In{}'.format(_Name)))[0]
		self._DesignParameter['n2p2_gate_via3']['_DesignObj']._CalculateDesignParameterSameEnclosure(**dict(_ViaMet22Met3NumberOfCOX=1, _ViaMet22Met3NumberOfCOY=2))
		self._DesignParameter['n2p2_gate_via3']['_XYCoordinates'] = [[(self._DesignParameter['AOI_p2']['_XYCoordinates'][0][0]), (((((self._DesignParameter['AOI_p2']['_XYCoordinates'][0][1]) + self._DesignParameter['AOI_p2']['_DesignObj']._DesignParameter['_RVTLayer']['_XYCoordinates'][0][1]) - (self._DesignParameter['AOI_p2']['_DesignObj']._DesignParameter['_RVTLayer']['_YWidth'] / 2)) / 2) + ((((self._DesignParameter['AOI_n2']['_XYCoordinates'][0][1]) + self._DesignParameter['AOI_n2']['_DesignObj']._DesignParameter['_RVTLayer']['_XYCoordinates'][0][1]) + (self._DesignParameter['AOI_n2']['_DesignObj']._DesignParameter['_RVTLayer']['_YWidth'] / 2)) / 2))]]
		self._DesignParameter['n2p2_gate_via4'] = self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_Name='n2p2_gate_via4In{}'.format(_Name)))[0]
		self._DesignParameter['n2p2_gate_via4']['_DesignObj']._CalculateDesignParameterSameEnclosure(**dict(_ViaMet32Met4NumberOfCOX=1, _ViaMet32Met4NumberOfCOY=2))
		self._DesignParameter['n2p2_gate_via4']['_XYCoordinates'] = [[(self._DesignParameter['AOI_p2']['_XYCoordinates'][0][0]), (((((self._DesignParameter['AOI_p2']['_XYCoordinates'][0][1]) + self._DesignParameter['AOI_p2']['_DesignObj']._DesignParameter['_RVTLayer']['_XYCoordinates'][0][1]) - (self._DesignParameter['AOI_p2']['_DesignObj']._DesignParameter['_RVTLayer']['_YWidth'] / 2)) / 2) + ((((self._DesignParameter['AOI_n2']['_XYCoordinates'][0][1]) + self._DesignParameter['AOI_n2']['_DesignObj']._DesignParameter['_RVTLayer']['_XYCoordinates'][0][1]) + (self._DesignParameter['AOI_n2']['_DesignObj']._DesignParameter['_RVTLayer']['_YWidth'] / 2)) / 2))]]
		self._DesignParameter['n2p2_gate_via5'] = self._SrefElementDeclaration(_DesignObj=ViaMet42Met5._ViaMet42Met5(_Name='n2p2_gate_via5In{}'.format(_Name)))[0]
		self._DesignParameter['n2p2_gate_via5']['_DesignObj']._CalculateDesignParameterSameEnclosure(**dict(_ViaMet42Met5NumberOfCOX=1, _ViaMet42Met5NumberOfCOY=2))
		self._DesignParameter['n2p2_gate_via5']['_XYCoordinates'] = [[(self._DesignParameter['AOI_p2']['_XYCoordinates'][0][0]), (((((self._DesignParameter['AOI_p2']['_XYCoordinates'][0][1]) + self._DesignParameter['AOI_p2']['_DesignObj']._DesignParameter['_RVTLayer']['_XYCoordinates'][0][1]) - (self._DesignParameter['AOI_p2']['_DesignObj']._DesignParameter['_RVTLayer']['_YWidth'] / 2)) / 2) + ((((self._DesignParameter['AOI_n2']['_XYCoordinates'][0][1]) + self._DesignParameter['AOI_n2']['_DesignObj']._DesignParameter['_RVTLayer']['_XYCoordinates'][0][1]) + (self._DesignParameter['AOI_n2']['_DesignObj']._DesignParameter['_RVTLayer']['_YWidth'] / 2)) / 2))]]



		self._DesignParameter['n3p3_gate_via1'] = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_Name='n3p3_gate_via1In{}'.format(_Name)))[0]
		self._DesignParameter['n3p3_gate_via1']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(**dict(_ViaPoly2Met1NumberOfCOX=1, _ViaPoly2Met1NumberOfCOY=2))
		self._DesignParameter['n3p3_gate_via1']['_XYCoordinates'] = [[((self._DesignParameter['AOI_p3']['_XYCoordinates'][0][0]) + self._DesignParameter['AOI_p3']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][-1][0] + self._DesignParameter['aoi_p3_out']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']//2 + drc._Metal1MinSpace2 + self._DesignParameter['n3p3_gate_via1']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']//2), (((((self._DesignParameter['AOI_p3']['_XYCoordinates'][0][1]) + self._DesignParameter['AOI_p3']['_DesignObj']._DesignParameter['_RVTLayer']['_XYCoordinates'][0][1]) - (self._DesignParameter['AOI_p3']['_DesignObj']._DesignParameter['_RVTLayer']['_YWidth'] / 2)) / 2) + ((((self._DesignParameter['AOI_n3']['_XYCoordinates'][0][1]) + self._DesignParameter['AOI_n3']['_DesignObj']._DesignParameter['_RVTLayer']['_XYCoordinates'][0][1]) + (self._DesignParameter['AOI_n3']['_DesignObj']._DesignParameter['_RVTLayer']['_YWidth'] / 2)) / 2))]]
		self._DesignParameter['n3p3_gate_via2'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='n3p3_gate_via2In{}'.format(_Name)))[0]
		self._DesignParameter['n3p3_gate_via2']['_DesignObj']._CalculateDesignParameterSameEnclosure(**dict(_ViaMet12Met2NumberOfCOX=1, _ViaMet12Met2NumberOfCOY=2))
		self._DesignParameter['n3p3_gate_via2']['_XYCoordinates'] = [[((self._DesignParameter['AOI_p3']['_XYCoordinates'][0][0]) + self._DesignParameter['AOI_p3']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][-1][0] + self._DesignParameter['aoi_p3_out']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']//2 + drc._Metal1MinSpace2 + self._DesignParameter['n3p3_gate_via1']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']//2), (((((self._DesignParameter['AOI_p3']['_XYCoordinates'][0][1]) + self._DesignParameter['AOI_p3']['_DesignObj']._DesignParameter['_RVTLayer']['_XYCoordinates'][0][1]) - (self._DesignParameter['AOI_p3']['_DesignObj']._DesignParameter['_RVTLayer']['_YWidth'] / 2)) / 2) + ((((self._DesignParameter['AOI_n3']['_XYCoordinates'][0][1]) + self._DesignParameter['AOI_n3']['_DesignObj']._DesignParameter['_RVTLayer']['_XYCoordinates'][0][1]) + (self._DesignParameter['AOI_n3']['_DesignObj']._DesignParameter['_RVTLayer']['_YWidth'] / 2)) / 2))]]
		self._DesignParameter['n3p3_gate_via3'] = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_Name='n3p3_gate_via3In{}'.format(_Name)))[0]
		self._DesignParameter['n3p3_gate_via3']['_DesignObj']._CalculateDesignParameterSameEnclosure(**dict(_ViaMet22Met3NumberOfCOX=1, _ViaMet22Met3NumberOfCOY=2))
		self._DesignParameter['n3p3_gate_via3']['_XYCoordinates'] = [[((self._DesignParameter['AOI_p3']['_XYCoordinates'][0][0]) + self._DesignParameter['AOI_p3']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][-1][0] + self._DesignParameter['aoi_p3_out']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']//2 + drc._Metal1MinSpace2 + self._DesignParameter['n3p3_gate_via1']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']//2), (((((self._DesignParameter['AOI_p3']['_XYCoordinates'][0][1]) + self._DesignParameter['AOI_p3']['_DesignObj']._DesignParameter['_RVTLayer']['_XYCoordinates'][0][1]) - (self._DesignParameter['AOI_p3']['_DesignObj']._DesignParameter['_RVTLayer']['_YWidth'] / 2)) / 2) + ((((self._DesignParameter['AOI_n3']['_XYCoordinates'][0][1]) + self._DesignParameter['AOI_n3']['_DesignObj']._DesignParameter['_RVTLayer']['_XYCoordinates'][0][1]) + (self._DesignParameter['AOI_n3']['_DesignObj']._DesignParameter['_RVTLayer']['_YWidth'] / 2)) / 2))]]
		self._DesignParameter['n3p3_gate_via4'] = self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_Name='n3p3_gate_via4In{}'.format(_Name)))[0]
		self._DesignParameter['n3p3_gate_via4']['_DesignObj']._CalculateDesignParameterSameEnclosure(**dict(_ViaMet32Met4NumberOfCOX=1, _ViaMet32Met4NumberOfCOY=2))
		self._DesignParameter['n3p3_gate_via4']['_XYCoordinates'] = [[((self._DesignParameter['AOI_p3']['_XYCoordinates'][0][0]) + self._DesignParameter['AOI_p3']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][-1][0] + self._DesignParameter['aoi_p3_out']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']//2 + drc._Metal1MinSpace2 + self._DesignParameter['n3p3_gate_via1']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']//2), (((((self._DesignParameter['AOI_p3']['_XYCoordinates'][0][1]) + self._DesignParameter['AOI_p3']['_DesignObj']._DesignParameter['_RVTLayer']['_XYCoordinates'][0][1]) - (self._DesignParameter['AOI_p3']['_DesignObj']._DesignParameter['_RVTLayer']['_YWidth'] / 2)) / 2) + ((((self._DesignParameter['AOI_n3']['_XYCoordinates'][0][1]) + self._DesignParameter['AOI_n3']['_DesignObj']._DesignParameter['_RVTLayer']['_XYCoordinates'][0][1]) + (self._DesignParameter['AOI_n3']['_DesignObj']._DesignParameter['_RVTLayer']['_YWidth'] / 2)) / 2))]]
		self._DesignParameter['n3p3_gate_via5'] = self._SrefElementDeclaration(_DesignObj=ViaMet42Met5._ViaMet42Met5(_Name='n3p3_gate_via5In{}'.format(_Name)))[0]
		self._DesignParameter['n3p3_gate_via5']['_DesignObj']._CalculateDesignParameterSameEnclosure(**dict(_ViaMet42Met5NumberOfCOX=1, _ViaMet42Met5NumberOfCOY=2))
		self._DesignParameter['n3p3_gate_via5']['_XYCoordinates'] = [[((self._DesignParameter['AOI_p3']['_XYCoordinates'][0][0]) + self._DesignParameter['AOI_p3']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][-1][0] + self._DesignParameter['aoi_p3_out']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']//2 + drc._Metal1MinSpace2 + self._DesignParameter['n3p3_gate_via1']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']//2), (((((self._DesignParameter['AOI_p3']['_XYCoordinates'][0][1]) + self._DesignParameter['AOI_p3']['_DesignObj']._DesignParameter['_RVTLayer']['_XYCoordinates'][0][1]) - (self._DesignParameter['AOI_p3']['_DesignObj']._DesignParameter['_RVTLayer']['_YWidth'] / 2)) / 2) + ((((self._DesignParameter['AOI_n3']['_XYCoordinates'][0][1]) + self._DesignParameter['AOI_n3']['_DesignObj']._DesignParameter['_RVTLayer']['_XYCoordinates'][0][1]) + (self._DesignParameter['AOI_n3']['_DesignObj']._DesignParameter['_RVTLayer']['_YWidth'] / 2)) / 2))]]
		self._DesignParameter['n3p3_gate_via6'] = self._SrefElementDeclaration(_DesignObj=ViaMet52Met6._ViaMet52Met6(_Name='n3p3_gate_via6In{}'.format(_Name)))[0]
		self._DesignParameter['n3p3_gate_via6']['_DesignObj']._CalculateViaMet52Met6DesignParameter(**dict(_ViaMet52Met6NumberOfCOX=1, _ViaMet52Met6NumberOfCOY=2))
		self._DesignParameter['n3p3_gate_via6']['_XYCoordinates'] = [[((self._DesignParameter['AOI_p3']['_XYCoordinates'][0][0]) + self._DesignParameter['AOI_p3']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][-1][0] + self._DesignParameter['aoi_p3_out']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']//2 + drc._Metal1MinSpace2 + self._DesignParameter['n3p3_gate_via1']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']//2), (((((self._DesignParameter['AOI_p3']['_XYCoordinates'][0][1]) + self._DesignParameter['AOI_p3']['_DesignObj']._DesignParameter['_RVTLayer']['_XYCoordinates'][0][1]) - (self._DesignParameter['AOI_p3']['_DesignObj']._DesignParameter['_RVTLayer']['_YWidth'] / 2)) / 2) + ((((self._DesignParameter['AOI_n3']['_XYCoordinates'][0][1]) + self._DesignParameter['AOI_n3']['_DesignObj']._DesignParameter['_RVTLayer']['_XYCoordinates'][0][1]) + (self._DesignParameter['AOI_n3']['_DesignObj']._DesignParameter['_RVTLayer']['_YWidth'] / 2)) / 2))]]



		self._DesignParameter['n1p1_polygate'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _Width=self._DesignParameter['n1p1_gate_via_1']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'])
		self._DesignParameter['n1p1_polygate']['_XYCoordinates'] = [[[(+ (self._DesignParameter['n1p1_gate_via_1']['_XYCoordinates'][0][0] + self._DesignParameter['n1p1_gate_via_1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0])), (+ (self._DesignParameter['n1p1_gate_via_1']['_XYCoordinates'][0][1] + self._DesignParameter['n1p1_gate_via_1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1]))], [(self._DesignParameter['AOI_p1_n1']['_XYCoordinates'][(- 1)][0][0]), (self._DesignParameter['n1p1_gate_via_1']['_XYCoordinates'][0][1] + self._DesignParameter['n1p1_gate_via_1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1])]]]
		self._DesignParameter['n2p2_gatepoly'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _Width=self._DesignParameter['n2p2_gate_via1']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'])
		self._DesignParameter['n2p2_gatepoly']['_XYCoordinates'] = [[[(self._DesignParameter['AOI_p2_n2']['_XYCoordinates'][1][0][0]), self._DesignParameter['n2p2_gate_via1']['_XYCoordinates'][0][1]], [(self._DesignParameter['AOI_p2_n2']['_XYCoordinates'][(- 1)][0][0]), self._DesignParameter['n2p2_gate_via1']['_XYCoordinates'][0][1]]]]
		self._DesignParameter['n3p3_gatepoly'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _Width=self._DesignParameter['n3p3_gate_via1']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'])
		self._DesignParameter['n3p3_gatepoly']['_XYCoordinates'] = [[[(self._DesignParameter['AOI_p3_n3']['_XYCoordinates'][1][0][0]), (self._DesignParameter['n3p3_gate_via1']['_XYCoordinates'][0][1] + self._DesignParameter['n3p3_gate_via1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1])], [(+ (self._DesignParameter['n3p3_gate_via1']['_XYCoordinates'][0][0] + self._DesignParameter['n3p3_gate_via1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0])), (+ (self._DesignParameter['n3p3_gate_via1']['_XYCoordinates'][0][1] + self._DesignParameter['n3p3_gate_via1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1]))]]]
		self._DesignParameter['n1_to_n2_tmp_m1'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _XWidth=self._DesignParameter['AOI_n1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth'], _YWidth=self._DesignParameter['AOI_n1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth'])
		self._DesignParameter['n1_to_n2_tmp_m1']['_XYCoordinates'] = [[((self._DesignParameter['AOI_n1']['_XYCoordinates'][0][0]) + self._DesignParameter['AOI_n1']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][1][0]), (((((self._DesignParameter['AOI_n1']['_XYCoordinates'][0][1]) + self._DesignParameter['AOI_n1']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) + (self._DesignParameter['AOI_n1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)) + drc._Metal1MinSpace2) + (self._DesignParameter['AOI_n1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth'] / 2))]]
		path_list = []
		xy_offset = [0, 0]
		if (len(self._DesignParameter['AOI_n1']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates']) == 1):
		    mode = 'vertical'
		    _width = self._DesignParameter['AOI_n1']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
		elif (self._DesignParameter['AOI_n1']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0] == self._DesignParameter['AOI_n1']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][(- 1)][0]):
		    mode = 'horizontal'
		    _width = self._DesignParameter['AOI_n1']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
		elif (self._DesignParameter['AOI_n1']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1] == self._DesignParameter['AOI_n1']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][(- 1)][1]):
		    mode = 'vertical'
		    _width = self._DesignParameter['AOI_n1']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
		else:
		    print('Invalid Target Input')
		if (mode == 'vertical'):
		    xy_with_offset = []
		    target_y_value = [[(+ self._DesignParameter['n1_to_n2_tmp_m1']['_XYCoordinates'][0][0]), (+ self._DesignParameter['n1_to_n2_tmp_m1']['_XYCoordinates'][0][1])]][0][1]
		    for i in range(len(self._DesignParameter['AOI_n1']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'])):
		        if ((i % 2) == 1):
		            xy_with_offset.append([(x + y) for (x, y) in zip([(self._DesignParameter['AOI_n1']['_XYCoordinates'][0][0]), (self._DesignParameter['AOI_n1']['_XYCoordinates'][0][1])], self._DesignParameter['AOI_n1']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		elif (mode == 'horizontal'):
		    xy_with_offset = []
		    target_x_value = [[(+ self._DesignParameter['n1_to_n2_tmp_m1']['_XYCoordinates'][0][0]), (+ self._DesignParameter['n1_to_n2_tmp_m1']['_XYCoordinates'][0][1])]][0][0]
		    for i in range(len(self._DesignParameter['AOI_n1']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'])):
		        if ((i % 2) == 1):
		            xy_with_offset.append([(x + y) for (x, y) in zip([(self._DesignParameter['AOI_n1']['_XYCoordinates'][0][0]), (self._DesignParameter['AOI_n1']['_XYCoordinates'][0][1])], self._DesignParameter['AOI_n1']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		for i in range(len(path_list)):
		    path_list[i][0] = [(xy + offset) for (xy, offset) in zip(path_list[i][0], xy_offset)]
		self._DesignParameter['n1_in'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=_width)
		self._DesignParameter['n1_in']['_XYCoordinates'] = path_list
		path_list = []
		xy_offset = [0, 0]
		if (len(self._DesignParameter['AOI_n2']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates']) == 1):
		    mode = 'vertical'
		    _width = self._DesignParameter['AOI_n2']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
		elif (self._DesignParameter['AOI_n2']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0] == self._DesignParameter['AOI_n2']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][(- 1)][0]):
		    mode = 'horizontal'
		    _width = self._DesignParameter['AOI_n2']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
		elif (self._DesignParameter['AOI_n2']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1] == self._DesignParameter['AOI_n2']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][(- 1)][1]):
		    mode = 'vertical'
		    _width = self._DesignParameter['AOI_n2']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
		else:
		    print('Invalid Target Input')
		if (mode == 'vertical'):
		    xy_with_offset = []
		    target_y_value = [[(+ self._DesignParameter['n1_to_n2_tmp_m1']['_XYCoordinates'][0][0]), (+ self._DesignParameter['n1_to_n2_tmp_m1']['_XYCoordinates'][0][1])]][0][1]
		    for i in range(len(self._DesignParameter['AOI_n2']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'])):
		        if ((i % 2) == 0):
		            xy_with_offset.append([(x + y) for (x, y) in zip([(self._DesignParameter['AOI_n2']['_XYCoordinates'][0][0]), (self._DesignParameter['AOI_n2']['_XYCoordinates'][0][1])], self._DesignParameter['AOI_n2']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		elif (mode == 'horizontal'):
		    xy_with_offset = []
		    target_x_value = [[(+ self._DesignParameter['n1_to_n2_tmp_m1']['_XYCoordinates'][0][0]), (+ self._DesignParameter['n1_to_n2_tmp_m1']['_XYCoordinates'][0][1])]][0][0]
		    for i in range(len(self._DesignParameter['AOI_n2']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'])):
		        if ((i % 2) == 0):
		            xy_with_offset.append([(x + y) for (x, y) in zip([(self._DesignParameter['AOI_n2']['_XYCoordinates'][0][0]), (self._DesignParameter['AOI_n2']['_XYCoordinates'][0][1])], self._DesignParameter['AOI_n2']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		for i in range(len(path_list)):
		    path_list[i][0] = [(xy + offset) for (xy, offset) in zip(path_list[i][0], xy_offset)]
		self._DesignParameter['p1_out'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=_width)
		self._DesignParameter['p1_out']['_XYCoordinates'] = path_list
		self._DesignParameter['n1_to_p1'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=50)
		self._DesignParameter['n1_to_p1']['_XYCoordinates'] = [[[(+ self._DesignParameter['n1_to_n2_tmp_m1']['_XYCoordinates'][0][0]), (+ self._DesignParameter['n1_to_n2_tmp_m1']['_XYCoordinates'][0][1])], [((self._DesignParameter['AOI_n2']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] / 2) + self._DesignParameter['p1_out']['_XYCoordinates'][(- 1)][0][0]), self._DesignParameter['n1_to_n2_tmp_m1']['_XYCoordinates'][0][1]]]]

		path_list = []
		xy_offset = [0, 0]
		if (len(self._DesignParameter['AOI_p3']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates']) == 1):
			mode = 'vertical'
			_width = self._DesignParameter['aoi_p3_out']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
		elif (self._DesignParameter['AOI_p3']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0] == self._DesignParameter['AOI_p3']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][(- 1)][0]):
			mode = 'horizontal'
			_width = self._DesignParameter['aoi_p3_out']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
		elif (self._DesignParameter['AOI_p3']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1] == self._DesignParameter['AOI_p3']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][(- 1)][1]):
			mode = 'vertical'
			_width = self._DesignParameter['aoi_p3_out']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
		else:
			print('Invalid Target Input')
		if (mode == 'vertical'):
			xy_with_offset = []
			target_y_value = [[(+ ((self._DesignParameter['AOI_n3']['_XYCoordinates'][0][0]) + self._DesignParameter['AOI_n3']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0])), (+ ((self._DesignParameter['AOI_n3']['_XYCoordinates'][0][1]) + self._DesignParameter['AOI_n3']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]))]][0][1]
			for i in range(len(self._DesignParameter['AOI_p3']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'])):
				if ((i % 2) == 1):
					xy_with_offset.append([(x + y) for (x, y) in zip([(self._DesignParameter['AOI_p3']['_XYCoordinates'][0][0]), (self._DesignParameter['AOI_p3']['_XYCoordinates'][0][1])], self._DesignParameter['AOI_p3']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i])])
			for i in range(len(xy_with_offset)):
				path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		elif (mode == 'horizontal'):
			xy_with_offset = []
			target_x_value = [[(+ ((self._DesignParameter['AOI_n3']['_XYCoordinates'][0][0]) + self._DesignParameter['AOI_n3']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0])), (+ ((self._DesignParameter['AOI_n3']['_XYCoordinates'][0][1]) + self._DesignParameter['AOI_n3']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]))]][0][0]
			for i in range(len(self._DesignParameter['AOI_p3']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'])):
				if ((i % 2) == 1):
					xy_with_offset.append([(x + y) for (x, y) in zip([(self._DesignParameter['AOI_p3']['_XYCoordinates'][0][0]), (self._DesignParameter['AOI_p3']['_XYCoordinates'][0][1])], self._DesignParameter['AOI_p3']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i])])
			for i in range(len(xy_with_offset)):
				path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		for i in range(len(path_list)):
			path_list[i][0] = [(xy + offset) for (xy, offset) in zip(path_list[i][0], xy_offset)]
		self._DesignParameter['AOI_out'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=_width)
		self._DesignParameter['AOI_out']['_XYCoordinates'] = path_list

		self._DesignParameter['aoi2pmos_via'] = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_Name='aoi2pmos_viaIn{}'.format(_Name)))[0]
		self._DesignParameter['aoi2pmos_via']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(**dict(_ViaPoly2Met1NumberOfCOX=2, _ViaPoly2Met1NumberOfCOY=1))
		self._DesignParameter['aoi2pmos_via']['_XYCoordinates'] = [[((((((self._DesignParameter['aoi_out_pmos']['_XYCoordinates'][0][0]) + self._DesignParameter['aoi_out_pmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) + (self._DesignParameter['aoi_out_pmos']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)) - drc._CoMinWidth) - drc._CoMinEnclosureByPOAtLeastTwoSide) - (drc._CoMinSpace2 / 2)),
																	((((((self._DesignParameter['aoi_out_pmos']['_XYCoordinates'][0][1]) - self._DesignParameter['aoi_out_pmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1]) - (self._DesignParameter['aoi_out_pmos']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2)) - drc._PolygateMinSpace2) + (drc._CoMinWidth / 2)) - drc._CoMinEnclosureByPO2)]]
		path_list = []
		xy_offset = [0, 0]
		if (len(self._DesignParameter['aoi_out_pmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates']) == 1):
			mode = 'vertical'
			_width = self._DesignParameter['aoi_out_pmos']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
		elif (self._DesignParameter['aoi_out_pmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0] == self._DesignParameter['aoi_out_pmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]):
			mode = 'horizontal'
			_width = self._DesignParameter['aoi_out_pmos']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
		elif (self._DesignParameter['aoi_out_pmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1] == self._DesignParameter['aoi_out_pmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][1]):
			mode = 'vertical'
			_width = self._DesignParameter['aoi_out_pmos']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
		else:
			print('Invalid Target Input')
		if (mode == 'vertical'):
			xy_with_offset = []
			target_y_value = [[(+ (self._DesignParameter['aoi2pmos_via']['_XYCoordinates'][0][0] + self._DesignParameter['aoi2pmos_via']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0])), (+ (self._DesignParameter['aoi2pmos_via']['_XYCoordinates'][0][1] + self._DesignParameter['aoi2pmos_via']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1]))]][0][1]
			for i in range(len(self._DesignParameter['aoi_out_pmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
				xy_with_offset.append([(x + y) for (x, y) in zip([(self._DesignParameter['aoi_out_pmos']['_XYCoordinates'][0][0]), (self._DesignParameter['aoi_out_pmos']['_XYCoordinates'][0][1])], self._DesignParameter['aoi_out_pmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i])])
			for i in range(len(xy_with_offset)):
				path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		elif (mode == 'horizontal'):
			xy_with_offset = []
			target_x_value = [[(+ (self._DesignParameter['aoi2pmos_via']['_XYCoordinates'][0][0] + self._DesignParameter['aoi2pmos_via']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0])), (+ (self._DesignParameter['aoi2pmos_via']['_XYCoordinates'][0][1] + self._DesignParameter['aoi2pmos_via']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1]))]][0][0]
			for i in range(len(self._DesignParameter['aoi_out_pmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
				xy_with_offset.append([(x + y) for (x, y) in zip([(self._DesignParameter['aoi_out_pmos']['_XYCoordinates'][0][0]), (self._DesignParameter['aoi_out_pmos']['_XYCoordinates'][0][1])], self._DesignParameter['aoi_out_pmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i])])
			for i in range(len(xy_with_offset)):
				path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		for i in range(len(path_list)):
			path_list[i][0] = [(xy + offset) for (xy, offset) in zip(path_list[i][0], xy_offset)]
		self._DesignParameter['aoi2aoipmos_poly1'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _Width=_width)
		self._DesignParameter['aoi2aoipmos_poly1']['_XYCoordinates'] = path_list
		self._DesignParameter['aoi2aoipmos_poly2'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _Width=self._DesignParameter['aoi2pmos_via']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'])
		self._DesignParameter['aoi2aoipmos_poly2']['_XYCoordinates'] = [[[(+ (self._DesignParameter['aoi2pmos_via']['_XYCoordinates'][0][0] + self._DesignParameter['aoi2pmos_via']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0])), (+ (self._DesignParameter['aoi2pmos_via']['_XYCoordinates'][0][1] + self._DesignParameter['aoi2pmos_via']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1]))], [(self._DesignParameter['aoi2aoipmos_poly1']['_XYCoordinates'][(- 1)][0][0] + (self._DesignParameter['aoi_out_pmos']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)), (self._DesignParameter['aoi2pmos_via']['_XYCoordinates'][0][1] + self._DesignParameter['aoi2pmos_via']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1])]]]
		self._DesignParameter['aoi2pmos_m1'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=self._DesignParameter['aoi2pmos_via']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'])
		self._DesignParameter['aoi2pmos_m1']['_XYCoordinates'] = [[[(+ (self._DesignParameter['aoi2pmos_via']['_XYCoordinates'][0][0] + self._DesignParameter['aoi2pmos_via']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0])),
																	(+ (self._DesignParameter['aoi2pmos_via']['_XYCoordinates'][0][1] + self._DesignParameter['aoi2pmos_via']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]))],
																   [(((((self._DesignParameter['aoi_out_pmos']['_XYCoordinates'][0][0]) + self._DesignParameter['aoi_out_pmos']['_DesignObj']._DesignParameter['_RVTLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['aoi_out_pmos']['_DesignObj']._DesignParameter['_RVTLayer']['_XWidth'] / 2)) / 2) + ((((self._DesignParameter['AOI_n3']['_XYCoordinates'][0][0]) + self._DesignParameter['AOI_n3']['_DesignObj']._DesignParameter['_RVTLayer']['_XYCoordinates'][0][0]) + (self._DesignParameter['AOI_n3']['_DesignObj']._DesignParameter['_RVTLayer']['_XWidth'] / 2)) / 2)),
																	(self._DesignParameter['aoi2pmos_via']['_XYCoordinates'][0][1] + self._DesignParameter['aoi2pmos_via']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1])],
																   [(((((self._DesignParameter['AOI_n3']['_XYCoordinates'][0][0]) + self._DesignParameter['AOI_n3']['_DesignObj']._DesignParameter['_RVTLayer']['_XYCoordinates'][0][0]) + (self._DesignParameter['AOI_n3']['_DesignObj']._DesignParameter['_RVTLayer']['_XWidth'] / 2)) / 2) + ((((self._DesignParameter['aoi_out_pmos']['_XYCoordinates'][0][0]) + self._DesignParameter['aoi_out_pmos']['_DesignObj']._DesignParameter['_RVTLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['aoi_out_pmos']['_DesignObj']._DesignParameter['_RVTLayer']['_XWidth'] / 2)) / 2)),
																	(((((self._DesignParameter['AOI_n3']['_XYCoordinates'][0][1]) + self._DesignParameter['AOI_n3']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) + (self._DesignParameter['AOI_n3']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)) + drc._Metal1MinSpace2) + (self._DesignParameter['aoi2pmos_via']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2))],
																   [(self._DesignParameter['AOI_out']['_XYCoordinates'][(- 1)][0][0]),
																	(((((self._DesignParameter['AOI_n3']['_XYCoordinates'][0][1]) + self._DesignParameter['AOI_n3']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) + (self._DesignParameter['AOI_n3']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)) + drc._Metal1MinSpace2) + (self._DesignParameter['aoi2pmos_via']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2))]]]
		path_list = []
		xy_offset = [0, 0]
		if (len(self._DesignParameter['pbias_pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates']) == 1):
			mode = 'vertical'
			_width = self._DesignParameter['pbias_pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth']
		elif (self._DesignParameter['pbias_pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][0] == self._DesignParameter['pbias_pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][0]):
			mode = 'horizontal'
			_width = self._DesignParameter['pbias_pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth']
		elif (self._DesignParameter['pbias_pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1] == self._DesignParameter['pbias_pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][1]):
			mode = 'vertical'
			_width = self._DesignParameter['pbias_pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth']
		else:
			print('Invalid Target Input')
		if (mode == 'vertical'):
			xy_with_offset = []
			target_y_value = [[(+ (self._DesignParameter['VDD']['_XYCoordinates'][0][0])), (+ (self._DesignParameter['VDD']['_XYCoordinates'][0][1]))]][0][1]
			for i in range(len(self._DesignParameter['pbias_pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
				if ((i % 2) == 0):
					xy_with_offset.append([(x + y) for (x, y) in zip([(self._DesignParameter['pbias_pmos']['_XYCoordinates'][0][0]+self._DesignParameter['pbias_pmos']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']), (self._DesignParameter['pbias_pmos']['_XYCoordinates'][0][1]-self._DesignParameter['pbias_pmos']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']//2)], self._DesignParameter['pbias_pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])])
			for i in range(len(xy_with_offset)):
				path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		elif (mode == 'horizontal'):
			xy_with_offset = []
			target_x_value = [[(+ (self._DesignParameter['VDD']['_XYCoordinates'][0][0])), (+ (self._DesignParameter['VDD']['_XYCoordinates'][0][1]))]][0][0]
			for i in range(len(self._DesignParameter['pbias_pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
				if ((i % 2) == 0):
					xy_with_offset.append([(x + y) for (x, y) in zip([(self._DesignParameter['pbias_pmos']['_XYCoordinates'][0][0]), (self._DesignParameter['pbias_pmos']['_XYCoordinates'][0][1]-self._DesignParameter['pbias_pmos']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']//2)], self._DesignParameter['pbias_pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])])
			for i in range(len(xy_with_offset)):
				path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		for i in range(len(path_list)):
			path_list[i][0] = [(xy + offset) for (xy, offset) in zip(path_list[i][0], xy_offset)]
		self._DesignParameter['VDD2pbiaspmos'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=_width*3)
		self._DesignParameter['VDD2pbiaspmos']['_XYCoordinates'] = path_list
		if nf_pbias_pmos > 1:
			self._DesignParameter['VDD2pbiaspmos']['_XYCoordinates'][-1][0][0] -= self._DesignParameter['pbias_pmos']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']*2
			self._DesignParameter['VDD2pbiaspmos']['_XYCoordinates'][-1][1][0] -= self._DesignParameter['pbias_pmos']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']*2

		##pmos via calculation
		YWidthOfPMOSMet1 = (self._DesignParameter['aoi_out_pmos']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']-drc._MetalxMinSpace42)//2
		NumViaYPMOS = int((YWidthOfPMOSMet1 - 2 * drc._Metal1MinEnclosureVia3-drc._VIAxMinWidth) / (drc._VIAxMinWidth + drc._VIAxMinSpace)+1)

		VIAPMOSMet12 = copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation)
		VIAPMOSMet12['_ViaMet12Met2NumberOfCOX'] = 1
		VIAPMOSMet12['_ViaMet12Met2NumberOfCOY'] = NumViaYPMOS if (NumViaYPMOS > 2) else 2

		##pbiaspmos2aoipmos_via
		self._DesignParameter['pbiaspmos2aoipmos_via1'] = self._SrefElementDeclaration(
			_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='pbiaspmos2aoipmos_via1In{}'.format(_Name)))[0]
		self._DesignParameter['pbiaspmos2aoipmos_via1']['_DesignObj']._CalculateDesignParameterSameEnclosure(**VIAPMOSMet12)

		# # 1-1) Metal1 YWidth re-calculation
		# self._DesignParameter['pbiaspmos2aoipmos_via1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] \
		# 	= max(self.getYWidth('pbiaspmos2aoipmos_via1', '_Met1Layer')//2, self.getYWidth('aoi_out_pmos', '_Met1Layer')//2)

		Area_M1for_pbiaspmos2aoipmos_via1 = self.getXWidth('pbiaspmos2aoipmos_via1', '_Met1Layer') \
											  * self.getYWidth('pbiaspmos2aoipmos_via1', '_Met1Layer')
		if Area_M1for_pbiaspmos2aoipmos_via1 < drc._Metal1MinArea:
			YWidth_recalculated_byMinArea = self.CeilMinSnapSpacing(drc._Metal1MinArea / self.getXWidth('pbiaspmos2aoipmos_via1', '_Met1Layer'), 2 * drc._MinSnapSpacing)
			self._DesignParameter['pbiaspmos2aoipmos_via1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] = YWidth_recalculated_byMinArea
		else:
			pass

		self._DesignParameter['pbiaspmos2aoipmos_via1']['_XYCoordinates'] = None
		XYList = []
		xy_offset = (0, (- self._DesignParameter['aoi_out_pmos']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth']//2 + self._DesignParameter['pbiaspmos2aoipmos_via1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']//2))
		for i in range(len(self._DesignParameter['aoi_out_pmos']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'])):
			if ((i % 2) == 1):
				xy = (self._DesignParameter['aoi_out_pmos']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i][0] if (type(self._DesignParameter['aoi_out_pmos']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i][0]) == list) else self._DesignParameter['aoi_out_pmos']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i])
				XYList.append([((x + y) + z) for (x, y, z) in zip([(self._DesignParameter['aoi_out_pmos']['_XYCoordinates'][0][0]), (self._DesignParameter['aoi_out_pmos']['_XYCoordinates'][0][1])], xy, xy_offset)])
		self._DesignParameter['pbiaspmos2aoipmos_via1']['_XYCoordinates'] = XYList


		self._DesignParameter['pbiaspmos2aoipmos_via2'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='pbiaspmos2aoipmos_via2In{}'.format(_Name)))[0]
		self._DesignParameter['pbiaspmos2aoipmos_via2']['_DesignObj']._CalculateDesignParameterSameEnclosure(**VIAPMOSMet12)

		Area_M1for_pbiaspmos2aoipmos_via2 = self.getXWidth('pbiaspmos2aoipmos_via2', '_Met1Layer') \
											  * self.getYWidth('pbiaspmos2aoipmos_via2', '_Met1Layer')
		if Area_M1for_pbiaspmos2aoipmos_via2 < drc._Metal1MinArea:
			YWidth_recalculated_byMinArea = self.CeilMinSnapSpacing(drc._Metal1MinArea / self.getXWidth('pbiaspmos2aoipmos_via2', '_Met1Layer'), 2 * drc._MinSnapSpacing)
			self._DesignParameter['pbiaspmos2aoipmos_via2']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] = YWidth_recalculated_byMinArea
		else:
			pass

		self._DesignParameter['pbiaspmos2aoipmos_via2']['_XYCoordinates'] = None
		XYList = []
		xy_offset = [0, 0]
		for i in range(len(self._DesignParameter['pbias_pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
			if ((i % 2) == 1):
				xy = (self._DesignParameter['pbias_pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i][0] if (type(self._DesignParameter['pbias_pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i][0]) == list) else self._DesignParameter['pbias_pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])
				XYList.append([((x + y) + z) for (x, y, z) in zip([(self._DesignParameter['pbias_pmos']['_XYCoordinates'][0][0]), (self._DesignParameter['pbiaspmos2aoipmos_via1']['_XYCoordinates'][0][1])], xy, xy_offset)])
		self._DesignParameter['pbiaspmos2aoipmos_via2']['_XYCoordinates'] = XYList

		# self._DesignParameter['pbiaspmos_out_via'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='pbiaspmos_out_viaIn{}'.format(_Name)))[0]
		# self._DesignParameter['pbiaspmos_out_via']['_DesignObj']._CalculateDesignParameterSameEnclosure(**dict(_ViaMet12Met2NumberOfCOX=1, _ViaMet12Met2NumberOfCOY=3))

		NumViaYPMOS = int((YWidthOfPMOSMet1 - 2 * drc._Metal1MinEnclosureVia3-drc._VIAxMinWidth) / (drc._VIAxMinWidth + drc._VIAxMinSpace)+1)

		VIAPMOSMet12 = copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation)
		VIAPMOSMet12['_ViaMet12Met2NumberOfCOX'] = 1
		VIAPMOSMet12['_ViaMet12Met2NumberOfCOY'] = NumViaYPMOS if (NumViaYPMOS > 2) else 2

		##pbiaspmos_out_via
		self._DesignParameter['pbiaspmos_out_via'] = self._SrefElementDeclaration(
			_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='pbiaspmos_out_viaIn{}'.format(_Name)))[0]
		self._DesignParameter['pbiaspmos_out_via']['_DesignObj']._CalculateDesignParameterSameEnclosure(**VIAPMOSMet12)

		# # 1-1) Metal1 YWidth re-calculation
		# self._DesignParameter['pbiaspmos_out_via']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] \
		# 	= max(self.getYWidth('pbiaspmos_out_via', '_Met1Layer')//2, self.getYWidth('aoi_out_pmos', '_Met1Layer')//2)

		Area_M1for_pbiaspmos_out_via = self.getXWidth('pbiaspmos_out_via', '_Met1Layer') \
											  * self.getYWidth('pbiaspmos_out_via', '_Met1Layer')
		if Area_M1for_pbiaspmos_out_via < drc._Metal1MinArea:
			YWidth_recalculated_byMinArea = self.CeilMinSnapSpacing(drc._Metal1MinArea / self.getXWidth('pbiaspmos_out_via', '_Met1Layer'), 2 * drc._MinSnapSpacing)
			self._DesignParameter['pbiaspmos_out_via']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] = YWidth_recalculated_byMinArea
		else:
			pass

		self._DesignParameter['pbiaspmos_out_via']['_XYCoordinates'] = None
		XYList = []
		xy_offset = (0, (self._DesignParameter['aoi_out_pmos']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2 - self._DesignParameter['pbiaspmos_out_via']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']//2))
		for i in range(len(self._DesignParameter['aoi_out_pmos']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'])):
			if ((i % 2) == 0):
				xy = (self._DesignParameter['aoi_out_pmos']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i][0] if (type(self._DesignParameter['aoi_out_pmos']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i][0]) == list) else self._DesignParameter['aoi_out_pmos']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i])
				XYList.append([((x + y) + z) for (x, y, z) in zip([(self._DesignParameter['aoi_out_pmos']['_XYCoordinates'][0][0]), (self._DesignParameter['aoi_out_pmos']['_XYCoordinates'][0][1])], xy, xy_offset)])
		self._DesignParameter['pbiaspmos_out_via']['_XYCoordinates'] = XYList

		self._DesignParameter['pbiaspmos_out_via2'] = self._SrefElementDeclaration(
			_DesignObj=ViaMet22Met3._ViaMet22Met3(_Name='pbiaspmos_out_via2In{}'.format(_Name)))[0]
		self._DesignParameter['pbiaspmos_out_via2']['_DesignObj']._CalculateDesignParameterSameEnclosure(**dict(_ViaMet22Met3NumberOfCOX=1, _ViaMet22Met3NumberOfCOY= NumViaYPMOS if (NumViaYPMOS > 2) else 2))
		self._DesignParameter['pbiaspmos_out_via2']['_XYCoordinates'] = [self._DesignParameter['pbiaspmos_out_via']['_XYCoordinates'][0]]

		self._DesignParameter['pbiaspmos2aoipmos_m2path'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _Width=self._DesignParameter['pbiaspmos2aoipmos_via1']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'])
		self._DesignParameter['pbiaspmos2aoipmos_m2path']['_XYCoordinates'] = [[[(+ (self._DesignParameter['pbiaspmos2aoipmos_via1']['_XYCoordinates'][0][0])), (+ (self._DesignParameter['pbiaspmos2aoipmos_via1']['_XYCoordinates'][0][1]))],
																				[(((self._DesignParameter['pbiaspmos2aoipmos_via2']['_XYCoordinates'][(- 1)][0]) + self._DesignParameter['pbiaspmos2aoipmos_via2']['_DesignObj']._DesignParameter['_Met2Layer']['_XYCoordinates'][0][0]) + (self._DesignParameter['pbiaspmos2aoipmos_via2']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth'] / 2)), (self._DesignParameter['pbiaspmos2aoipmos_via1']['_XYCoordinates'][0][1])]]]
		self._DesignParameter['aoi_pmos_out_m2'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _Width=self._DesignParameter['pbiaspmos_out_via']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'])
		self._DesignParameter['aoi_pmos_out_m2']['_XYCoordinates'] = [[[((self._DesignParameter['pbiaspmos_out_via']['_XYCoordinates'][0][0]) + self._DesignParameter['pbiaspmos_out_via']['_DesignObj']._DesignParameter['_Met2Layer']['_XYCoordinates'][0][0]), ((self._DesignParameter['pbiaspmos_out_via']['_XYCoordinates'][0][1]) + self._DesignParameter['pbiaspmos_out_via']['_DesignObj']._DesignParameter['_Met2Layer']['_XYCoordinates'][0][1])],
																	   [((self._DesignParameter['pbiaspmos_out_via']['_XYCoordinates'][(- 1)][0]) + self._DesignParameter['pbiaspmos_out_via']['_DesignObj']._DesignParameter['_Met2Layer']['_XYCoordinates'][0][0]), ((self._DesignParameter['pbiaspmos_out_via']['_XYCoordinates'][0][1]) + self._DesignParameter['pbiaspmos_out_via']['_DesignObj']._DesignParameter['_Met2Layer']['_XYCoordinates'][0][1])]]]


		self._DesignParameter['pbiaspmos_gate_in'] = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_Name='pbiaspmos_gate_inIn{}'.format(_Name)))[0]

		#gate cont calculation
		XWidthOfgateCONT = ((((self._DesignParameter['pbias_pmos']['_XYCoordinates'][0][0]) + self._DesignParameter['pbias_pmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]) + (self._DesignParameter['pbias_pmos']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)) - (((self._DesignParameter['pbias_pmos']['_XYCoordinates'][0][0]) + self._DesignParameter['pbias_pmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['pbias_pmos']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)))
		NumViaX = int((XWidthOfgateCONT - 2 * drc._CoMinEnclosureByPO) / (drc._CoMinWidth + drc._CoMinSpace))
		POLYVIAX = NumViaX if (NumViaX > 2) else 2


		self._DesignParameter['pbiaspmos_gate_in']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(**dict(_ViaPoly2Met1NumberOfCOX=POLYVIAX, _ViaPoly2Met1NumberOfCOY=1))
		self._DesignParameter['pbiaspmos_gate_in']['_XYCoordinates'] = [[(self._DesignParameter['pbias_pmos']['_XYCoordinates'][0][0]),
																		 ((((self._DesignParameter['pbiaspmos2aoipmos_via1']['_XYCoordinates'][0][1]) + self._DesignParameter['pbiaspmos2aoipmos_via1']['_DesignObj']._DesignParameter['_Met2Layer']['_XYCoordinates'][0][1]) - (self._DesignParameter['pbiaspmos2aoipmos_via1']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] / 2) - self._DesignParameter['pbiaspmos_gate_in']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']//2 - drc._MetalxMinSpace42))]]

		self._DesignParameter['PbiasIN_m1pin'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1PIN'][0], _Datatype=DesignParameters._LayerMapping['METAL1PIN'][1], _XWidth=self._DesignParameter['pbiaspmos_gate_in']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'], _YWidth=self._DesignParameter['pbiaspmos_gate_in']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'])
		self._DesignParameter['PbiasIN_m1pin']['_XYCoordinates'] = [[(+ ((self._DesignParameter['pbiaspmos_gate_in']['_XYCoordinates'][0][0]) + self._DesignParameter['pbiaspmos_gate_in']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0])), (+ ((self._DesignParameter['pbiaspmos_gate_in']['_XYCoordinates'][0][1]) + self._DesignParameter['pbiaspmos_gate_in']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]))]]


		self._DesignParameter['pbias_poly_path'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _Width=self._DesignParameter['pbiaspmos_gate_in']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'])
		self._DesignParameter['pbias_poly_path']['_XYCoordinates'] = [[[(((self._DesignParameter['pbias_pmos']['_XYCoordinates'][0][0]) + self._DesignParameter['pbias_pmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['pbias_pmos']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)),
																		self._DesignParameter['pbiaspmos_gate_in']['_XYCoordinates'][0][1]],
																	   [(((self._DesignParameter['pbias_pmos']['_XYCoordinates'][0][0]) + self._DesignParameter['pbias_pmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]) + (self._DesignParameter['pbias_pmos']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)),
																		self._DesignParameter['pbiaspmos_gate_in']['_XYCoordinates'][0][1]]]]

		# self._DesignParameter['pbiaspmos2aoipmos_via1'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='pbiaspmos2aoipmos_via1In{}'.format(_Name)))[0]
		# self._DesignParameter['pbiaspmos2aoipmos_via1']['_DesignObj']._CalculateDesignParameterSameEnclosure(**dict(_ViaMet12Met2NumberOfCOX=1, _ViaMet12Met2NumberOfCOY=3))



		##Power_rail
		Power_length = (((((self._DesignParameter['pbias_pmos']['_XYCoordinates'][0][0]) + self._DesignParameter['pbias_pmos']['_DesignObj']._DesignParameter['_PPLayer']['_XYCoordinates'][0][0]) + (self._DesignParameter['pbias_pmos']['_DesignObj']._DesignParameter['_PPLayer']['_XWidth'] / 2)) + drc._MetalxMinSpace) - ((((self._DesignParameter['n1p1_gate_via_6']['_XYCoordinates'][0][0]) + self._DesignParameter['n1p1_gate_via_6']['_DesignObj']._DesignParameter['_Met6Layer']['_XYCoordinates'][0][0]) - (self._DesignParameter['n1p1_gate_via_6']['_DesignObj']._DesignParameter['_Met6Layer']['_XWidth'] / 2)) - drc._MetalxMinSpace))
		power_COX = int((Power_length - 2 * drc._CoMinEnclosureByOD) // (drc._CoMinWidth + drc._CoMinSpace)) + 3

		self._DesignParameter['VSS']['_DesignObj']._CalculatePbodyContactDesignParameter(**dict(_NumberOfPbodyCOX=power_COX, _NumberOfPbodyCOY=2, _Met1XWidth=None, _Met1YWidth=None))
		self._DesignParameter['VSS']['_XYCoordinates'][0][0] = (((((self._DesignParameter['pbias_pmos']['_XYCoordinates'][0][0]) + self._DesignParameter['pbias_pmos']['_DesignObj']._DesignParameter['_PPLayer']['_XYCoordinates'][0][0]) + (self._DesignParameter['pbias_pmos']['_DesignObj']._DesignParameter['_PPLayer']['_XWidth'] / 2)) / 2) + ((((self._DesignParameter['n1p1_gate_via_6']['_XYCoordinates'][0][0]) + self._DesignParameter['n1p1_gate_via_6']['_DesignObj']._DesignParameter['_Met6Layer']['_XYCoordinates'][0][0]) - (self._DesignParameter['n1p1_gate_via_6']['_DesignObj']._DesignParameter['_Met6Layer']['_XWidth'] / 2)) / 2))
		self._DesignParameter['VDD']['_DesignObj']._CalculateNbodyContactDesignParameter(**dict(_NumberOfNbodyCOX=power_COX, _NumberOfNbodyCOY=4, _Met1XWidth=None, _Met1YWidth=None))
		self._DesignParameter['VDD']['_XYCoordinates'][0][0] = (((((self._DesignParameter['pbias_pmos']['_XYCoordinates'][0][0]) + self._DesignParameter['pbias_pmos']['_DesignObj']._DesignParameter['_PPLayer']['_XYCoordinates'][0][0]) + (self._DesignParameter['pbias_pmos']['_DesignObj']._DesignParameter['_PPLayer']['_XWidth'] / 2)) / 2) + ((((self._DesignParameter['n1p1_gate_via_6']['_XYCoordinates'][0][0]) + self._DesignParameter['n1p1_gate_via_6']['_DesignObj']._DesignParameter['_Met6Layer']['_XYCoordinates'][0][0]) - (self._DesignParameter['n1p1_gate_via_6']['_DesignObj']._DesignParameter['_Met6Layer']['_XWidth'] / 2)) / 2))

		XWidthOfMet1 = self._DesignParameter['pbiaspmos_gate_in']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
		Pbiasgatevia = int((XWidthOfMet1 - 2 * drc._Metal1MinEnclosureVia3) / (drc._VIAxMinWidth + drc._VIAxMinSpace))

		self._DesignParameter['pbiaspmos_gate_in_via2'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='pbiaspmos_gatein_via2In{}'.format(_Name)))[0]
		self._DesignParameter['pbiaspmos_gate_in_via2']['_DesignObj']._CalculateDesignParameterSameEnclosure(**dict(_ViaMet12Met2NumberOfCOX=Pbiasgatevia, _ViaMet12Met2NumberOfCOY=1))
		self._DesignParameter['pbiaspmos_gate_in_via2']['_XYCoordinates'] = [[(+ ((self._DesignParameter['pbiaspmos_gate_in']['_XYCoordinates'][0][0]) + self._DesignParameter['pbiaspmos_gate_in']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0])), (+ ((self._DesignParameter['pbiaspmos_gate_in']['_XYCoordinates'][0][1]) + self._DesignParameter['pbiaspmos_gate_in']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]))]]

		self._DesignParameter['PbiasIN_m2boundary'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _XWidth=self._DesignParameter['pbiaspmos_gate_in']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'], _YWidth=self._DesignParameter['pbiaspmos_gate_in']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'])
		self._DesignParameter['PbiasIN_m2boundary']['_XYCoordinates'] = [[(+ ((self._DesignParameter['pbiaspmos_gate_in']['_XYCoordinates'][0][0]) + self._DesignParameter['pbiaspmos_gate_in']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0])), (+ ((self._DesignParameter['pbiaspmos_gate_in']['_XYCoordinates'][0][1]) + self._DesignParameter['pbiaspmos_gate_in']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]))]]


		self._DesignParameter['pbias_path'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _Width=self._DesignParameter['pbiaspmos_gate_in_via2']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'])
		#self._DesignParameter['pbias_path']['_XYCoordinates'] = [[[(+ (self._DesignParameter['pbiaspmos_gate_in_via2']['_XYCoordinates'][0][0] + self._DesignParameter['pbiaspmos_gate_in_via2']['_DesignObj']._DesignParameter['_Met2Layer']['_XYCoordinates'][0][0])), (+ (self._DesignParameter['pbiaspmos_gate_in_via2']['_XYCoordinates'][0][1] + self._DesignParameter['pbiaspmos_gate_in_via2']['_DesignObj']._DesignParameter['_Met2Layer']['_XYCoordinates'][0][1]))], [(self._DesignParameter['pbiaspmos_gate_in_via2']['_XYCoordinates'][0][0] + self._DesignParameter['pbiaspmos_gate_in_via2']['_DesignObj']._DesignParameter['_Met2Layer']['_XYCoordinates'][0][0]), ((self._DesignParameter['VSS']['_XYCoordinates'][0][1]) + self._DesignParameter['VSS']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1])]]]

		tmp_pbias_path = [[]]

		for i in range(1, nf_pbias_pmos):
			tmp_pbias_path.append([[((self._DesignParameter['pbias_pmos']['_XYCoordinates'][0][0]) + self._DesignParameter['pbias_pmos']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i][0]),
									 (+ (self._DesignParameter['pbiaspmos_gate_in_via2']['_XYCoordinates'][0][1] + self._DesignParameter['pbiaspmos_gate_in_via2']['_DesignObj']._DesignParameter['_Met2Layer']['_XYCoordinates'][0][1]))],
									[((self._DesignParameter['pbias_pmos']['_XYCoordinates'][0][0]) + self._DesignParameter['pbias_pmos']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i][0]),
									 ((self._DesignParameter['VSS']['_XYCoordinates'][0][1]) + self._DesignParameter['VSS']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1])]])
		self._DesignParameter['pbias_path']['_XYCoordinates'] = tmp_pbias_path

		self._DesignParameter['idac_iout'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0], _Datatype=DesignParameters._LayerMapping['METAL3'][1], _Width=(self._DesignParameter['pbiaspmos_out_via2']['_DesignObj']._DesignParameter['_Met3Layer']['_XWidth'] * 3))
		self._DesignParameter['idac_iout']['_XYCoordinates'] = [[[(((self._DesignParameter['pbiaspmos_out_via2']['_XYCoordinates'][0][0]) + self._DesignParameter['pbiaspmos_out_via2']['_DesignObj']._DesignParameter['_Met3Layer']['_XYCoordinates'][0][0]) + (self._DesignParameter['pbiaspmos_out_via2']['_DesignObj']._DesignParameter['_Met3Layer']['_XWidth'])), (((self._DesignParameter['VDD']['_XYCoordinates'][0][1]) + self._DesignParameter['VDD']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) + (self._DesignParameter['VDD']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2))],
																 [(((self._DesignParameter['pbiaspmos_out_via2']['_XYCoordinates'][0][0]) + self._DesignParameter['pbiaspmos_out_via2']['_DesignObj']._DesignParameter['_Met3Layer']['_XYCoordinates'][0][0]) + (self._DesignParameter['pbiaspmos_out_via2']['_DesignObj']._DesignParameter['_Met3Layer']['_XWidth'])), (((self._DesignParameter['VSS']['_XYCoordinates'][0][1]) + self._DesignParameter['VSS']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) - (self._DesignParameter['VSS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2))]]]

		self._DesignParameter['_IOUTpin'] = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3PIN'][0], _Datatype=DesignParameters._LayerMapping['METAL3PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0], _XYCoordinates=[[0, 0]], _Mag=0.05, _Angle=0, _TEXT='Iout')
		self._DesignParameter['_IOUTpin']['_XYCoordinates'] = self._DesignParameter['pbiaspmos_out_via2']['_XYCoordinates']

		self._DesignParameter['VDD_via_m2_to_m3'] = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_Name='VDD_via_m2_to_m3In{}'.format(_Name)))[0]
		self._DesignParameter['VDD_via_m2_to_m3']['_DesignObj']._CalculateDesignParameterSameEnclosure(**dict(_ViaMet22Met3NumberOfCOX=2, _ViaMet22Met3NumberOfCOY=3))
		if nf_pbias_pmos > 1:
			self._DesignParameter['VDD_via_m2_to_m3']['_XYCoordinates'] = [[(self._DesignParameter['VDD2pbiaspmos']['_XYCoordinates'][-1][0][0] + self._DesignParameter['VDD2pbiaspmos']['_Width']//2 - self._DesignParameter['pbiaspmos_out_via2']['_DesignObj']._DesignParameter['_Met3Layer']['_XWidth'] * 3//2),
																			((self._DesignParameter['VDD']['_XYCoordinates'][0][1]) + self._DesignParameter['VDD']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1])]]
		else:
			self._DesignParameter['VDD_via_m2_to_m3']['_XYCoordinates'] = [[(self._DesignParameter['pbiaspmos2aoipmos_via2']['_XYCoordinates'][0][0]),
																			((self._DesignParameter['VDD']['_XYCoordinates'][0][1]) + self._DesignParameter['VDD']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1])]]

		self._DesignParameter['idac_vdd_m3'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0], _Datatype=DesignParameters._LayerMapping['METAL3'][1], _Width=(self._DesignParameter['VDD_via_m2_to_m3']['_DesignObj']._DesignParameter['_Met3Layer']['_XWidth']))

		self._DesignParameter['idac_vdd_m3']['_XYCoordinates'] = [[[self._DesignParameter['VDD_via_m2_to_m3']['_XYCoordinates'][0][0],
																		(((self._DesignParameter['VDD']['_XYCoordinates'][0][1]) + self._DesignParameter['VDD']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) + (self._DesignParameter['VDD']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2))],
																	 [self._DesignParameter['VDD_via_m2_to_m3']['_XYCoordinates'][0][0],
																	  (((self._DesignParameter['VSS']['_XYCoordinates'][0][1]) + self._DesignParameter['VSS']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) - (self._DesignParameter['VSS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2))]]]

		self._DesignParameter['VDD_m2'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _XWidth=self._DesignParameter['VDD']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'], _YWidth=self._DesignParameter['VDD']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'])
		self._DesignParameter['VDD_m2']['_XYCoordinates'] = [[(+ ((self._DesignParameter['VDD']['_XYCoordinates'][0][0]) + self._DesignParameter['VDD']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0])), (+ ((self._DesignParameter['VDD']['_XYCoordinates'][0][1]) + self._DesignParameter['VDD']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]))]]

		self._DesignParameter['VDD_via_m1_to_m2'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='VDD_via_m1_to_m2In{}'.format(_Name)))[0]
		self._DesignParameter['VDD_via_m1_to_m2']['_DesignObj']._CalculateDesignParameterSameEnclosure(**dict(_ViaMet12Met2NumberOfCOX=int((self._DesignParameter['VDD_m2']['_XWidth'] - drc._VIAxMinEnclosureByMetx * 2 - drc._VIAxMinWidth) // (drc._VIAxMinWidth + drc._VIAxMinSpace)) - 4,
																											  _ViaMet12Met2NumberOfCOY=3))
		self._DesignParameter['VDD_via_m1_to_m2']['_XYCoordinates'] = [[(+ ((self._DesignParameter['VDD']['_XYCoordinates'][0][0]) + self._DesignParameter['VDD']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0])), (+ ((self._DesignParameter['VDD']['_XYCoordinates'][0][1]) + self._DesignParameter['VDD']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]))]]

		self._DesignParameter['row2'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL6'][0], _Datatype=DesignParameters._LayerMapping['METAL6'][1], _Width=self._DesignParameter['n3p3_gate_via6']['_DesignObj']._DesignParameter['_Met6Layer']['_XWidth'])

		if Odd_row_flag== 1 :
			self._DesignParameter['row2']['_XYCoordinates'] = [[[(+ ((self._DesignParameter['n3p3_gate_via6']['_XYCoordinates'][0][0]) + self._DesignParameter['n3p3_gate_via6']['_DesignObj']._DesignParameter['_Met6Layer']['_XYCoordinates'][0][0])), (+ ((self._DesignParameter['n3p3_gate_via6']['_XYCoordinates'][0][1]) + self._DesignParameter['n3p3_gate_via6']['_DesignObj']._DesignParameter['_Met6Layer']['_XYCoordinates'][0][1]))],
																[((self._DesignParameter['n3p3_gate_via6']['_XYCoordinates'][0][0]) + self._DesignParameter['n3p3_gate_via6']['_DesignObj']._DesignParameter['_Met6Layer']['_XYCoordinates'][0][0]), ((self._DesignParameter['VDD']['_XYCoordinates'][0][1]) + self._DesignParameter['VDD']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1])]]]
		else :
			self._DesignParameter['row2']['_XYCoordinates'] = [[[(+ ((self._DesignParameter['n3p3_gate_via6']['_XYCoordinates'][0][0]) + self._DesignParameter['n3p3_gate_via6']['_DesignObj']._DesignParameter['_Met6Layer']['_XYCoordinates'][0][0])), (+ ((self._DesignParameter['n3p3_gate_via6']['_XYCoordinates'][0][1]) + self._DesignParameter['n3p3_gate_via6']['_DesignObj']._DesignParameter['_Met6Layer']['_XYCoordinates'][0][1]))],
																[((self._DesignParameter['n3p3_gate_via6']['_XYCoordinates'][0][0]) + self._DesignParameter['n3p3_gate_via6']['_DesignObj']._DesignParameter['_Met6Layer']['_XYCoordinates'][0][0]), ((self._DesignParameter['VSS']['_XYCoordinates'][0][1]) + self._DesignParameter['VSS']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1])]]]


		self._DesignParameter['row1'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL6'][0], _Datatype=DesignParameters._LayerMapping['METAL6'][1], _Width=self._DesignParameter['n1p1_gate_via_6']['_DesignObj']._DesignParameter['_Met6Layer']['_XWidth'])

		if Odd_row_flag == 1 :
			self._DesignParameter['row1']['_XYCoordinates'] = [[[(+ ((self._DesignParameter['n1p1_gate_via_6']['_XYCoordinates'][0][0]) + self._DesignParameter['n1p1_gate_via_6']['_DesignObj']._DesignParameter['_Met6Layer']['_XYCoordinates'][0][0])), (+ ((self._DesignParameter['n1p1_gate_via_6']['_XYCoordinates'][0][1]) + self._DesignParameter['n1p1_gate_via_6']['_DesignObj']._DesignParameter['_Met6Layer']['_XYCoordinates'][0][1]))],
																[((self._DesignParameter['n1p1_gate_via_6']['_XYCoordinates'][0][0]) + self._DesignParameter['n1p1_gate_via_6']['_DesignObj']._DesignParameter['_Met6Layer']['_XYCoordinates'][0][0]), ((self._DesignParameter['VSS']['_XYCoordinates'][0][1]) + self._DesignParameter['VSS']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1])]]]
		else :
			self._DesignParameter['row1']['_XYCoordinates'] = [[[(+ ((self._DesignParameter['n1p1_gate_via_6']['_XYCoordinates'][0][0]) + self._DesignParameter['n1p1_gate_via_6']['_DesignObj']._DesignParameter['_Met6Layer']['_XYCoordinates'][0][0])), (+ ((self._DesignParameter['n1p1_gate_via_6']['_XYCoordinates'][0][1]) + self._DesignParameter['n1p1_gate_via_6']['_DesignObj']._DesignParameter['_Met6Layer']['_XYCoordinates'][0][1]))],
																[((self._DesignParameter['n1p1_gate_via_6']['_XYCoordinates'][0][0]) + self._DesignParameter['n1p1_gate_via_6']['_DesignObj']._DesignParameter['_Met6Layer']['_XYCoordinates'][0][0]), ((self._DesignParameter['VDD']['_XYCoordinates'][0][1]) + self._DesignParameter['VDD']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1])]]]

		self._DesignParameter['col'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL5'][0], _Datatype=DesignParameters._LayerMapping['METAL5'][1], _Width=self._DesignParameter['n2p2_gate_via5']['_DesignObj']._DesignParameter['_Met5Layer']['_XWidth'])
		self._DesignParameter['col']['_XYCoordinates'] = [[[((self._DesignParameter['n2p2_gate_via5']['_XYCoordinates'][0][0]) + self._DesignParameter['n2p2_gate_via5']['_DesignObj']._DesignParameter['_Met5Layer']['_XYCoordinates'][0][0]), ((self._DesignParameter['VDD']['_XYCoordinates'][0][1]) + self._DesignParameter['VDD']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1])],
														   [((self._DesignParameter['n2p2_gate_via5']['_XYCoordinates'][0][0]) + self._DesignParameter['n2p2_gate_via5']['_DesignObj']._DesignParameter['_Met5Layer']['_XYCoordinates'][0][0]), ((self._DesignParameter['VSS']['_XYCoordinates'][0][1]) + self._DesignParameter['VSS']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1])]]]

		self._DesignParameter['_colpin'] = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL5PIN'][0], _Datatype=DesignParameters._LayerMapping['METAL5PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0], _XYCoordinates=[[0, 0]], _Mag=0.05, _Angle=0, _TEXT='Col')
		self._DesignParameter['_colpin']['_XYCoordinates'] = self._DesignParameter['n2p2_gate_via5']['_XYCoordinates']

		if Odd_row_flag==0 :
			self._DesignParameter['row1_rail'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL6'][0], _Datatype=DesignParameters._LayerMapping['METAL6'][1], _Width=self._DesignParameter['row1']['_Width'])
			self._DesignParameter['row1_rail']['_XYCoordinates'] = [[[(((self._DesignParameter['VDD']['_XYCoordinates'][0][0]) + self._DesignParameter['VDD']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0]) - (self._DesignParameter['VDD']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] / 2)), ((self._DesignParameter['VDD']['_XYCoordinates'][0][1]) + self._DesignParameter['VDD']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1])],
																	 [(((self._DesignParameter['VDD']['_XYCoordinates'][0][0]) + self._DesignParameter['VDD']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0]) + (self._DesignParameter['VDD']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] / 2)), ((self._DesignParameter['VDD']['_XYCoordinates'][0][1]) + self._DesignParameter['VDD']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1])]]]
			self._DesignParameter['row2_rail'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL6'][0], _Datatype=DesignParameters._LayerMapping['METAL6'][1], _Width=self._DesignParameter['row2']['_Width'])
			self._DesignParameter['row2_rail']['_XYCoordinates'] = [[[(((self._DesignParameter['VSS']['_XYCoordinates'][0][0]) + self._DesignParameter['VSS']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0]) - (self._DesignParameter['VSS']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] / 2)), ((self._DesignParameter['VSS']['_XYCoordinates'][0][1]) + self._DesignParameter['VSS']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1])],
																	 [(((self._DesignParameter['VSS']['_XYCoordinates'][0][0]) + self._DesignParameter['VSS']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0]) + (self._DesignParameter['VSS']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] / 2)), ((self._DesignParameter['VSS']['_XYCoordinates'][0][1]) + self._DesignParameter['VSS']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1])]]]

			self._DesignParameter['_row1pin'] = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL6PIN'][0], _Datatype=DesignParameters._LayerMapping['METAL6PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0], _XYCoordinates=[[0, 0]], _Mag=0.05, _Angle=0, _TEXT='Row1')
			self._DesignParameter['_row1pin']['_XYCoordinates'] = self._DesignParameter['VDD']['_XYCoordinates']
			self._DesignParameter['_row2pin'] = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL6PIN'][0], _Datatype=DesignParameters._LayerMapping['METAL6PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0], _XYCoordinates=[[0, 0]], _Mag=0.05, _Angle=0, _TEXT='Row2')
			self._DesignParameter['_row2pin']['_XYCoordinates'] = self._DesignParameter['VSS']['_XYCoordinates']
		else :
			self._DesignParameter['row2_rail'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL6'][0], _Datatype=DesignParameters._LayerMapping['METAL6'][1], _Width=self._DesignParameter['row2']['_Width'])
			self._DesignParameter['row2_rail']['_XYCoordinates'] = [[[(((self._DesignParameter['VDD']['_XYCoordinates'][0][0]) + self._DesignParameter['VDD']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0]) - (self._DesignParameter['VDD']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] / 2)), ((self._DesignParameter['VDD']['_XYCoordinates'][0][1]) + self._DesignParameter['VDD']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1])],
																	 [(((self._DesignParameter['VDD']['_XYCoordinates'][0][0]) + self._DesignParameter['VDD']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0]) + (self._DesignParameter['VDD']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] / 2)), ((self._DesignParameter['VDD']['_XYCoordinates'][0][1]) + self._DesignParameter['VDD']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1])]]]
			self._DesignParameter['row1_rail'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL6'][0], _Datatype=DesignParameters._LayerMapping['METAL6'][1], _Width=self._DesignParameter['row1']['_Width'])
			self._DesignParameter['row1_rail']['_XYCoordinates'] = [[[(((self._DesignParameter['VSS']['_XYCoordinates'][0][0]) + self._DesignParameter['VSS']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0]) - (self._DesignParameter['VSS']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] / 2)), ((self._DesignParameter['VSS']['_XYCoordinates'][0][1]) + self._DesignParameter['VSS']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1])],
																	 [(((self._DesignParameter['VSS']['_XYCoordinates'][0][0]) + self._DesignParameter['VSS']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0]) + (self._DesignParameter['VSS']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] / 2)), ((self._DesignParameter['VSS']['_XYCoordinates'][0][1]) + self._DesignParameter['VSS']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1])]]]

			self._DesignParameter['_row1pin'] = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL6PIN'][0], _Datatype=DesignParameters._LayerMapping['METAL6PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0], _XYCoordinates=[[0, 0]], _Mag=0.05, _Angle=0, _TEXT='Row1')
			self._DesignParameter['_row1pin']['_XYCoordinates'] = [[self._DesignParameter['VSS']['_XYCoordinates'][0][0], self._DesignParameter['VSS']['_XYCoordinates'][0][1]]]
			self._DesignParameter['_row2pin'] = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL6PIN'][0], _Datatype=DesignParameters._LayerMapping['METAL6PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0], _XYCoordinates=[[0, 0]], _Mag=0.05, _Angle=0, _TEXT='Row2')
			self._DesignParameter['_row2pin']['_XYCoordinates'] = [[self._DesignParameter['VDD']['_XYCoordinates'][0][0], self._DesignParameter['VDD']['_XYCoordinates'][0][1]]]


		self._DesignParameter['pbias_rail'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _Width=self._DesignParameter['row2']['_Width'])
		self._DesignParameter['pbias_rail']['_XYCoordinates'] = [[[(((self._DesignParameter['VSS']['_XYCoordinates'][0][0]) + self._DesignParameter['VSS']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0]) - (self._DesignParameter['VSS']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] / 2)), ((self._DesignParameter['VSS']['_XYCoordinates'][0][1]) + self._DesignParameter['VSS']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1])],
																 [(((self._DesignParameter['VSS']['_XYCoordinates'][0][0]) + self._DesignParameter['VSS']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0]) + (self._DesignParameter['VSS']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] / 2)), ((self._DesignParameter['VSS']['_XYCoordinates'][0][1]) + self._DesignParameter['VSS']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1])]]]

		self._DesignParameter['_pbiaspin'] = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2PIN'][0], _Datatype=DesignParameters._LayerMapping['METAL2PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0], _XYCoordinates=[[0, 0]], _Mag=0.05, _Angle=0, _TEXT='PBIAS')
		self._DesignParameter['_pbiaspin']['_XYCoordinates'] = self._DesignParameter['VSS']['_XYCoordinates']

		self._DesignParameter['p1p2_to_p3_tmp_m1_0'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _XWidth=self._DesignParameter['AOI_p2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth'], _YWidth=self._DesignParameter['AOI_p2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth'])
		self._DesignParameter['p1p2_to_p3_tmp_m1_0']['_XYCoordinates'] = [[(self._DesignParameter['aoi_p2_to_p3']['_XYCoordinates'][0][0]), (((((self._DesignParameter['AOI_p2']['_XYCoordinates'][0][1]) + self._DesignParameter['AOI_p2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1]) - (self._DesignParameter['AOI_p2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_YWidth'] / 2)) - drc._Metal1MinSpace2) - (self._DesignParameter['AOI_p2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth'] / 2))]]
		if nf_AOI_mos != 1:
			self._DesignParameter['p1p2_to_p3_tmp_m1'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _XWidth=self._DesignParameter['AOI_p2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth'], _YWidth=self._DesignParameter['AOI_p2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth'])
			self._DesignParameter['p1p2_to_p3_tmp_m1']['_XYCoordinates'] = [[(self._DesignParameter['AOI_p3']['_XYCoordinates'][0][0] + self._DesignParameter['AOI_p3']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0]), (((((self._DesignParameter['AOI_p2']['_XYCoordinates'][0][1]) + self._DesignParameter['AOI_p2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1]) + (self._DesignParameter['AOI_p2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_YWidth'] / 2)) + drc._Metal1MinSpace2) + (self._DesignParameter['AOI_p2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth'] / 2))]]

		path_list = []
		xy_offset = [0, 0]
		if (len(self._DesignParameter['AOI_p2']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates']) == 1):
		    mode = 'vertical'
		    _width = self._DesignParameter['aoi_p2_to_p3']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
		elif (self._DesignParameter['AOI_p2']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0] == self._DesignParameter['AOI_p2']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][(- 1)][0]):
		    mode = 'horizontal'
		    _width = self._DesignParameter['aoi_p2_to_p3']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
		elif (self._DesignParameter['AOI_p2']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1] == self._DesignParameter['AOI_p2']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][(- 1)][1]):
		    mode = 'vertical'
		    _width = self._DesignParameter['aoi_p2_to_p3']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
		else:
		    print('Invalid Target Input')
		if (mode == 'vertical'):
		    xy_with_offset = []
		    target_y_value = [[(+ self._DesignParameter['p1p2_to_p3_tmp_m1_0']['_XYCoordinates'][0][0]), (- self._DesignParameter['p1p2_to_p3_tmp_m1_0']['_YWidth']//2 + self._DesignParameter['p1p2_to_p3_tmp_m1_0']['_XYCoordinates'][0][1])]][0][1]
		    for i in range(len(self._DesignParameter['AOI_p2']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'])):
		        if ((i % 2) == 1):
		            xy_with_offset.append([(x + y) for (x, y) in zip([(self._DesignParameter['AOI_p2']['_XYCoordinates'][0][0]), (self._DesignParameter['AOI_p2']['_XYCoordinates'][0][1])], self._DesignParameter['AOI_p2']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		elif (mode == 'horizontal'):
		    xy_with_offset = []
		    target_x_value = [[(+ self._DesignParameter['p1p2_to_p3_tmp_m1_0']['_XYCoordinates'][0][0]), (- self._DesignParameter['p1p2_to_p3_tmp_m1_0']['_YWidth']//2 + self._DesignParameter['p1p2_to_p3_tmp_m1_0']['_XYCoordinates'][0][1])]][0][0]
		    for i in range(len(self._DesignParameter['AOI_p2']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'])):
		        if ((i % 2) == 1):
		            xy_with_offset.append([(x + y) for (x, y) in zip([(self._DesignParameter['AOI_p2']['_XYCoordinates'][0][0]), (self._DesignParameter['AOI_p2']['_XYCoordinates'][0][1])], self._DesignParameter['AOI_p2']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][i])])
		    for i in range(len(xy_with_offset)):
		        path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		for i in range(len(path_list)):
		    path_list[i][0] = [(xy + offset) for (xy, offset) in zip(path_list[i][0], xy_offset)]
		self._DesignParameter['p2_out'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=_width)
		self._DesignParameter['p2_out']['_XYCoordinates'] = path_list

		if nf_AOI_mos != 1:
			path_list = []
			xy_offset = [0, 0]
			if (len(self._DesignParameter['AOI_p3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates']) == 1):
			    mode = 'vertical'
			    _width = self._DesignParameter['AOI_p3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth']
			elif (self._DesignParameter['AOI_p3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][0] == self._DesignParameter['AOI_p3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][0]):
			    mode = 'horizontal'
			    _width = self._DesignParameter['AOI_p3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth']
			elif (self._DesignParameter['AOI_p3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1] == self._DesignParameter['AOI_p3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][1]):
			    mode = 'vertical'
			    _width = self._DesignParameter['AOI_p3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth']
			else:
			    print('Invalid Target Input')
			if (mode == 'vertical'):
			    xy_with_offset = []
			    target_y_value = [[(+ self._DesignParameter['p1p2_to_p3_tmp_m1']['_XYCoordinates'][0][0]), (+ self._DesignParameter['p1p2_to_p3_tmp_m1']['_XYCoordinates'][0][1])]][0][1]
			    for i in range(len(self._DesignParameter['AOI_p3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
			        if ((i % 2) == 0):
			            xy_with_offset.append([(x + y) for (x, y) in zip([(self._DesignParameter['AOI_p3']['_XYCoordinates'][0][0]), (self._DesignParameter['AOI_p3']['_XYCoordinates'][0][1])], self._DesignParameter['AOI_p3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])])
			    for i in range(len(xy_with_offset)):
			        path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
			elif (mode == 'horizontal'):
			    xy_with_offset = []
			    target_x_value = [[(+ self._DesignParameter['p1p2_to_p3_tmp_m1']['_XYCoordinates'][0][0]), (+ self._DesignParameter['p1p2_to_p3_tmp_m1']['_XYCoordinates'][0][1])]][0][0]
			    for i in range(len(self._DesignParameter['AOI_p3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
			        if ((i % 2) == 0):
			            xy_with_offset.append([(x + y) for (x, y) in zip([(self._DesignParameter['AOI_p3']['_XYCoordinates'][0][0]), (self._DesignParameter['AOI_p3']['_XYCoordinates'][0][1])], self._DesignParameter['AOI_p3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])])
			    for i in range(len(xy_with_offset)):
			        path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
			for i in range(len(path_list)):
			    path_list[i][0] = [(xy + offset) for (xy, offset) in zip(path_list[i][0], xy_offset)]
			self._DesignParameter['p3_in'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=_width)
			self._DesignParameter['p3_in']['_XYCoordinates'] = path_list

			self._DesignParameter['p2_to_p3_m1_path'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=self._DesignParameter['p1p2_to_p3_tmp_m1']['_YWidth'])
			self._DesignParameter['p2_to_p3_m1_path']['_XYCoordinates'] = [[[(+ self._DesignParameter['p1p2_to_p3_tmp_m1']['_XYCoordinates'][0][0]), (+ self._DesignParameter['p1p2_to_p3_tmp_m1']['_XYCoordinates'][0][1])], [(self._DesignParameter['p3_in']['_XYCoordinates'][(- 1)][0][0] + (self._DesignParameter['AOI_p3']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] / 2)), self._DesignParameter['p1p2_to_p3_tmp_m1']['_XYCoordinates'][0][1]]]]

		self._DesignParameter['p2_to_p3_path_m1_0'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=50)
		self._DesignParameter['p2_to_p3_path_m1_0']['_XYCoordinates'] = [[[(+ (self._DesignParameter['p1p2_to_p3_tmp_m1_0']['_XYCoordinates'][0][0])), (+ (self._DesignParameter['p1p2_to_p3_tmp_m1_0']['_XYCoordinates'][0][1]))], [(((self._DesignParameter['AOI_p3']['_XYCoordinates'][0][0]) + self._DesignParameter['AOI_p3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][0]) + (self._DesignParameter['AOI_p3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth'] / 2)), (self._DesignParameter['p1p2_to_p3_tmp_m1_0']['_XYCoordinates'][0][1])]]]
		self._DesignParameter['p3_in_m1'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=self._DesignParameter['AOI_p3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth'])
		self._DesignParameter['p3_in_m1']['_XYCoordinates'] = [[[((self._DesignParameter['AOI_p3']['_XYCoordinates'][0][0]) + self._DesignParameter['AOI_p3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][0]), (self._DesignParameter['p1p2_to_p3_tmp_m1_0']['_XYCoordinates'][0][1])], [(+ ((self._DesignParameter['AOI_p3']['_XYCoordinates'][0][0]) + self._DesignParameter['AOI_p3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][0])), (+ ((self._DesignParameter['AOI_p3']['_XYCoordinates'][0][1]) + self._DesignParameter['AOI_p3']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1]))]]]

		self._DesignParameter['n1p1_met1'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _XWidth=self._DesignParameter['n1p1_gate_via_1']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'], _YWidth=self._DesignParameter['n1p1_gate_via_2']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'])
		self._DesignParameter['n1p1_met1']['_XYCoordinates'] = [[(+ (self._DesignParameter['n1p1_gate_via_1']['_XYCoordinates'][0][0])), (+ (self._DesignParameter['n1p1_gate_via_1']['_XYCoordinates'][0][1]))]]
		self._DesignParameter['n2p2_met1'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _XWidth=self._DesignParameter['n2p2_gate_via1']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'], _YWidth=self._DesignParameter['n2p2_gate_via2']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'])
		self._DesignParameter['n2p2_met1']['_XYCoordinates'] = [[(+ (self._DesignParameter['n2p2_gate_via1']['_XYCoordinates'][0][0])), (+ (self._DesignParameter['n2p2_gate_via1']['_XYCoordinates'][0][1]))]]
		self._DesignParameter['n3p3_met1'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _XWidth=self._DesignParameter['n3p3_gate_via1']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'], _YWidth=self._DesignParameter['n3p3_gate_via2']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'])
		self._DesignParameter['n3p3_met1']['_XYCoordinates'] = [[(+ (self._DesignParameter['n3p3_gate_via1']['_XYCoordinates'][0][0])), (+ (self._DesignParameter['n3p3_gate_via1']['_XYCoordinates'][0][1]))]]

		self._DesignParameter['VDD_AOI_NW'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['NWELL'][0], _Datatype=DesignParameters._LayerMapping['NWELL'][1], _Width=(self._DesignParameter['VDD']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth'] + (2 * drc._NwMinSpacetoRX)))
		self._DesignParameter['VDD_AOI_NW']['_XYCoordinates'] = [[[((self._DesignParameter['VDD']['_XYCoordinates'][0][0]) + self._DesignParameter['VDD']['_DesignObj']._DesignParameter['_ODLayer']['_XYCoordinates'][0][0]), ((((self._DesignParameter['VDD']['_XYCoordinates'][0][1]) + self._DesignParameter['VDD']['_DesignObj']._DesignParameter['_ODLayer']['_XYCoordinates'][0][1]) + (self._DesignParameter['VDD']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth'] / 2)) + drc._NwMinSpacetoRX)],
																  [((self._DesignParameter['VDD']['_XYCoordinates'][0][0]) + self._DesignParameter['VDD']['_DesignObj']._DesignParameter['_ODLayer']['_XYCoordinates'][0][0]), (((self._DesignParameter['AOI_p3']['_XYCoordinates'][0][1]) + self._DesignParameter['AOI_p3']['_DesignObj']._DesignParameter['_PPLayer']['_XYCoordinates'][0][1]) - (self._DesignParameter['AOI_p3']['_DesignObj']._DesignParameter['_PPLayer']['_YWidth'] / 2))]]]
		self._DesignParameter['pbiaspmos_NW'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['NWELL'][0], _Datatype=DesignParameters._LayerMapping['NWELL'][1], _Width=(
					((((self._DesignParameter['pbias_pmos']['_XYCoordinates'][0][0]) + self._DesignParameter['pbias_pmos']['_DesignObj']._DesignParameter['_PPLayer']['_XYCoordinates'][0][0]) + (self._DesignParameter['pbias_pmos']['_DesignObj']._DesignParameter['_PPLayer']['_XWidth'] / 2)) - (((self._DesignParameter['aoi_out_pmos']['_XYCoordinates'][0][0]) + self._DesignParameter['aoi_out_pmos']['_DesignObj']._DesignParameter['_PPLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['aoi_out_pmos']['_DesignObj']._DesignParameter['_PPLayer']['_XWidth'] / 2))) + (2 * drc._NwMinEnclosurePactive2)))
		self._DesignParameter['pbiaspmos_NW']['_XYCoordinates'] = [
			[[(((((self._DesignParameter['pbias_pmos']['_XYCoordinates'][0][0]) + self._DesignParameter['pbias_pmos']['_DesignObj']._DesignParameter['_PPLayer']['_XYCoordinates'][0][0]) + (self._DesignParameter['pbias_pmos']['_DesignObj']._DesignParameter['_PPLayer']['_XWidth'] / 2)) / 2) + ((((self._DesignParameter['aoi_out_pmos']['_XYCoordinates'][0][0]) + self._DesignParameter['aoi_out_pmos']['_DesignObj']._DesignParameter['_PPLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['aoi_out_pmos']['_DesignObj']._DesignParameter['_PPLayer']['_XWidth'] / 2)) / 2)), self._DesignParameter['VDD_AOI_NW']['_XYCoordinates'][0][0][1]],
			 [(((((self._DesignParameter['pbias_pmos']['_XYCoordinates'][0][0]) + self._DesignParameter['pbias_pmos']['_DesignObj']._DesignParameter['_PPLayer']['_XYCoordinates'][0][0]) + (self._DesignParameter['pbias_pmos']['_DesignObj']._DesignParameter['_PPLayer']['_XWidth'] / 2)) / 2) + ((((self._DesignParameter['aoi_out_pmos']['_XYCoordinates'][0][0]) + self._DesignParameter['aoi_out_pmos']['_DesignObj']._DesignParameter['_PPLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['aoi_out_pmos']['_DesignObj']._DesignParameter['_PPLayer']['_XWidth'] / 2)) / 2)),
			  (((self._DesignParameter['pbias_pmos']['_XYCoordinates'][0][1]) + self._DesignParameter['pbias_pmos']['_DesignObj']._DesignParameter['_PPLayer']['_XYCoordinates'][0][1]) - (self._DesignParameter['pbias_pmos']['_DesignObj']._DesignParameter['_PPLayer']['_YWidth'] / 2))]]]


		##pmos POLY dummy for AOI
		self._DesignParameter['POLY_dummy_p1'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _XWidth=L_AOI_mos)
		self._DesignParameter['POLY_dummy_p1']['_YWidth'] = self._DesignParameter['AOI_p1']['_DesignObj']._DesignParameter['_PODummyLayer']['_YWidth']

		self._DesignParameter['POLY_dummy_p1']['_XYCoordinates'] = [[(self._DesignParameter['AOI_p1']['_XYCoordinates'][0][0] + self._DesignParameter['AOI_p1']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][0]),
																	 (self._DesignParameter['AOI_p1']['_XYCoordinates'][0][1] + self._DesignParameter['AOI_p1']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][1])]]

		if float(self._DesignParameter['POLY_dummy_p1']['_XWidth']) * float(self._DesignParameter['POLY_dummy_p1']['_YWidth']) < drc._PODummyMinArea:
			self._DesignParameter['POLY_dummy_p1']['_YWidth'] = self.CeilMinSnapSpacing(float(drc._PODummyMinArea) / float(self._DesignParameter['POLY_dummy_p1']['_XWidth']), drc._MinSnapSpacing * 2)
		else:
			pass

		self._DesignParameter['POLY_dummy_p2'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _XWidth=L_AOI_mos)
		self._DesignParameter['POLY_dummy_p2']['_YWidth'] = self._DesignParameter['AOI_p2']['_DesignObj']._DesignParameter['_PODummyLayer']['_YWidth']

		self._DesignParameter['POLY_dummy_p2']['_XYCoordinates'] = [[(self._DesignParameter['AOI_p2']['_XYCoordinates'][0][0] + self._DesignParameter['AOI_p2']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][0]),
																	 (self._DesignParameter['AOI_p2']['_XYCoordinates'][0][1] + self._DesignParameter['AOI_p2']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][1])]]

		if float(self._DesignParameter['POLY_dummy_p2']['_XWidth']) * float(self._DesignParameter['POLY_dummy_p2']['_YWidth']) < drc._PODummyMinArea:
			self._DesignParameter['POLY_dummy_p2']['_YWidth'] = self.CeilMinSnapSpacing(float(drc._PODummyMinArea) / float(self._DesignParameter['POLY_dummy_p2']['_XWidth']), drc._MinSnapSpacing * 2)
		else:
			pass

		self._DesignParameter['POLY_dummy_p3'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _XWidth=L_AOI_mos)
		self._DesignParameter['POLY_dummy_p3']['_YWidth'] = self._DesignParameter['AOI_p3']['_DesignObj']._DesignParameter['_PODummyLayer']['_YWidth']

		self._DesignParameter['POLY_dummy_p3']['_XYCoordinates'] = [[(self._DesignParameter['AOI_p3']['_XYCoordinates'][0][0] + self._DesignParameter['AOI_p3']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][0]),
																	 (self._DesignParameter['AOI_p3']['_XYCoordinates'][0][1] + self._DesignParameter['AOI_p3']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][1])],
																	[(self._DesignParameter['AOI_p3']['_XYCoordinates'][0][0] + self._DesignParameter['AOI_p3']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][-1][0]),
																	 (self._DesignParameter['AOI_p3']['_XYCoordinates'][0][1] + self._DesignParameter['AOI_p3']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][-1][1])]]

		if float(self._DesignParameter['POLY_dummy_p3']['_XWidth']) * float(self._DesignParameter['POLY_dummy_p3']['_YWidth']) < drc._PODummyMinArea:
			self._DesignParameter['POLY_dummy_p3']['_YWidth'] = self.CeilMinSnapSpacing(float(drc._PODummyMinArea) / float(self._DesignParameter['POLY_dummy_p3']['_XWidth']), drc._MinSnapSpacing * 2)
		else:
			pass

		self._DesignParameter['POLY_dummy_n1'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _XWidth=L_AOI_mos)
		self._DesignParameter['POLY_dummy_n1']['_YWidth'] = self._DesignParameter['AOI_n1']['_DesignObj']._DesignParameter['_PODummyLayer']['_YWidth']

		self._DesignParameter['POLY_dummy_n1']['_XYCoordinates'] = [[(self._DesignParameter['AOI_n1']['_XYCoordinates'][0][0] + self._DesignParameter['AOI_n1']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][0]),
																	 (self._DesignParameter['AOI_n1']['_XYCoordinates'][0][1] + self._DesignParameter['AOI_n1']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][1])]]

		if float(self._DesignParameter['POLY_dummy_n1']['_XWidth']) * float(self._DesignParameter['POLY_dummy_n1']['_YWidth']) < drc._PODummyMinArea:
			self._DesignParameter['POLY_dummy_n1']['_YWidth'] = self.CeilMinSnapSpacing(float(drc._PODummyMinArea) / float(self._DesignParameter['POLY_dummy_n1']['_XWidth']), drc._MinSnapSpacing * 2)
		else:
			pass

		self._DesignParameter['POLY_dummy_n2'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _XWidth=L_AOI_mos)
		self._DesignParameter['POLY_dummy_n2']['_YWidth'] = self._DesignParameter['AOI_n2']['_DesignObj']._DesignParameter['_PODummyLayer']['_YWidth']

		self._DesignParameter['POLY_dummy_n2']['_XYCoordinates'] = [[(self._DesignParameter['AOI_n2']['_XYCoordinates'][0][0] + self._DesignParameter['AOI_n2']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][0]),
																	 (self._DesignParameter['AOI_n2']['_XYCoordinates'][0][1] + self._DesignParameter['AOI_n2']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][1])]]

		if float(self._DesignParameter['POLY_dummy_n2']['_XWidth']) * float(self._DesignParameter['POLY_dummy_n2']['_YWidth']) < drc._PODummyMinArea:
			self._DesignParameter['POLY_dummy_n2']['_YWidth'] = self.CeilMinSnapSpacing(float(drc._PODummyMinArea) / float(self._DesignParameter['POLY_dummy_n2']['_XWidth']), drc._MinSnapSpacing * 2)
		else:
			pass

		self._DesignParameter['POLY_dummy_n3'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _XWidth=L_AOI_mos)
		self._DesignParameter['POLY_dummy_n3']['_YWidth'] = self._DesignParameter['AOI_n3']['_DesignObj']._DesignParameter['_PODummyLayer']['_YWidth']

		self._DesignParameter['POLY_dummy_n3']['_XYCoordinates'] = [[(self._DesignParameter['AOI_n3']['_XYCoordinates'][0][0] + self._DesignParameter['AOI_n3']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][0]),
																	 (self._DesignParameter['AOI_n3']['_XYCoordinates'][0][1] + self._DesignParameter['AOI_n3']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][1])],
																	[(self._DesignParameter['AOI_n3']['_XYCoordinates'][0][0] + self._DesignParameter['AOI_n3']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][-1][0]),
																	 (self._DesignParameter['AOI_n3']['_XYCoordinates'][0][1] + self._DesignParameter['AOI_n3']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][-1][1])]]

		if float(self._DesignParameter['POLY_dummy_n3']['_XWidth']) * float(self._DesignParameter['POLY_dummy_n3']['_YWidth']) < drc._PODummyMinArea:
			self._DesignParameter['POLY_dummy_n3']['_YWidth'] = self.CeilMinSnapSpacing(float(drc._PODummyMinArea) / float(self._DesignParameter['POLY_dummy_n3']['_XWidth']), drc._MinSnapSpacing * 2)
		else:
			pass

		self._DesignParameter['Iout_via'] = self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_Name='Iout_viaIn{}'.format(_Name)))[0]
		self._DesignParameter['Iout_via']['_DesignObj']._CalculateDesignParameterSameEnclosure(**dict(_ViaMet32Met4NumberOfCOX=3, _ViaMet32Met4NumberOfCOY=2))
		self._DesignParameter['Iout_via']['_XYCoordinates'] = [[(self._DesignParameter['idac_iout']['_XYCoordinates'][0][0][0]), (self._DesignParameter['VDD']['_XYCoordinates'][0][1])],
															   [(self._DesignParameter['idac_iout']['_XYCoordinates'][0][0][0]), (self._DesignParameter['VSS']['_XYCoordinates'][0][1])]]
		self._DesignParameter['Iout_M4'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL4'][0], _Datatype=DesignParameters._LayerMapping['METAL4'][1], _Width=self._DesignParameter['Iout_via']['_DesignObj']._DesignParameter['_Met4Layer']['_YWidth'])
		self._DesignParameter['Iout_M4']['_XYCoordinates'] = [[[(((self._DesignParameter['VDD']['_XYCoordinates'][0][0]) + self._DesignParameter['VDD']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0]) - (self._DesignParameter['VDD']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] / 2)),
																((self._DesignParameter['VDD']['_XYCoordinates'][0][1]) + self._DesignParameter['VDD']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1])],
															   [(((self._DesignParameter['VDD']['_XYCoordinates'][0][0]) + self._DesignParameter['VDD']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0]) + (self._DesignParameter['VDD']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] / 2)),
																((self._DesignParameter['VDD']['_XYCoordinates'][0][1]) + self._DesignParameter['VDD']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1])]],
															  [[(((self._DesignParameter['VSS']['_XYCoordinates'][0][0]) + self._DesignParameter['VSS']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0]) - (self._DesignParameter['VSS']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] / 2)),
																((self._DesignParameter['VSS']['_XYCoordinates'][0][1]) + self._DesignParameter['VSS']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1])],
															   [(((self._DesignParameter['VSS']['_XYCoordinates'][0][0]) + self._DesignParameter['VSS']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0]) + (self._DesignParameter['VSS']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] / 2)),
																((self._DesignParameter['VSS']['_XYCoordinates'][0][1]) + self._DesignParameter['VSS']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1])]]]

		# self._DesignParameter['PIMP_around_1'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['PIMP'][0], _Datatype=DesignParameters._LayerMapping['PIMP'][1], _Width=self._DesignParameter['AOI_p3']['_DesignObj']._DesignParameter['_PPLayer']['_YWidth'])
		# self._DesignParameter['PIMP_around_1']['_XYCoordinates'] = [[[(+ ((self._DesignParameter['AOI_p3']['_XYCoordinates'][0][0]) + self._DesignParameter['AOI_p3']['_DesignObj']._DesignParameter['_PPLayer']['_XYCoordinates'][0][0])),
		# 															  (+ ((self._DesignParameter['AOI_p3']['_XYCoordinates'][0][1]) + self._DesignParameter['AOI_p3']['_DesignObj']._DesignParameter['_PPLayer']['_XYCoordinates'][0][1]))],
		# 															 [(((self._DesignParameter['aoi_out_pmos']['_XYCoordinates'][0][0]) + self._DesignParameter['aoi_out_pmos']['_DesignObj']._DesignParameter['_PPLayer']['_XYCoordinates'][0][0]) + (self._DesignParameter['aoi_out_pmos']['_DesignObj']._DesignParameter['_PPLayer']['_XWidth'] / 2)),
		# 															  ((self._DesignParameter['AOI_p3']['_XYCoordinates'][0][1]) + self._DesignParameter['AOI_p3']['_DesignObj']._DesignParameter['_PPLayer']['_XYCoordinates'][0][1])]]]

		self._DesignParameter['BP_around'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['PIMP'][0], _Datatype=DesignParameters._LayerMapping['PIMP'][1], _Width=((((self._DesignParameter['aoi_out_pmos']['_XYCoordinates'][0][0]) + self._DesignParameter['aoi_out_pmos']['_DesignObj']._DesignParameter['_PPLayer']['_XYCoordinates'][0][0]) + (self._DesignParameter['aoi_out_pmos']['_DesignObj']._DesignParameter['_PPLayer']['_XWidth'] / 2)) - (((self._DesignParameter['AOI_p1']['_XYCoordinates'][0][0]) + self._DesignParameter['AOI_p1']['_DesignObj']._DesignParameter['_PPLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['AOI_p1']['_DesignObj']._DesignParameter['_PPLayer']['_XWidth'] / 2))))
		if (((self._DesignParameter['aoi_out_pmos']['_XYCoordinates'][0][1]) + self._DesignParameter['aoi_out_pmos']['_DesignObj']._DesignParameter['_PPLayer']['_XYCoordinates'][0][1]) + (self._DesignParameter['aoi_out_pmos']['_DesignObj']._DesignParameter['_PPLayer']['_YWidth'] / 2)) > (((self._DesignParameter['AOI_p1']['_XYCoordinates'][0][1]) + self._DesignParameter['AOI_p1']['_DesignObj']._DesignParameter['_PPLayer']['_XYCoordinates'][0][1]) - (self._DesignParameter['AOI_p1']['_DesignObj']._DesignParameter['_PPLayer']['_YWidth'] / 2)) :
			self._DesignParameter['BP_around']['_XYCoordinates'] = [[[(((((self._DesignParameter['AOI_p1']['_XYCoordinates'][0][0]) + self._DesignParameter['AOI_p1']['_DesignObj']._DesignParameter['_PPLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['AOI_p1']['_DesignObj']._DesignParameter['_PPLayer']['_XWidth'] / 2)) / 2) + ((((self._DesignParameter['aoi_out_pmos']['_XYCoordinates'][0][0]) + self._DesignParameter['aoi_out_pmos']['_DesignObj']._DesignParameter['_PPLayer']['_XYCoordinates'][0][0]) + (self._DesignParameter['aoi_out_pmos']['_DesignObj']._DesignParameter['_PPLayer']['_XWidth'] / 2)) / 2)),
																  (((self._DesignParameter['AOI_p1']['_XYCoordinates'][0][1]) + self._DesignParameter['AOI_p1']['_DesignObj']._DesignParameter['_PPLayer']['_XYCoordinates'][0][1]) + (self._DesignParameter['AOI_p1']['_DesignObj']._DesignParameter['_PPLayer']['_YWidth'] / 2))],
																 [(((((self._DesignParameter['AOI_p1']['_XYCoordinates'][0][0]) + self._DesignParameter['AOI_p1']['_DesignObj']._DesignParameter['_PPLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['AOI_p1']['_DesignObj']._DesignParameter['_PPLayer']['_XWidth'] / 2)) / 2) + ((((self._DesignParameter['aoi_out_pmos']['_XYCoordinates'][0][0]) + self._DesignParameter['aoi_out_pmos']['_DesignObj']._DesignParameter['_PPLayer']['_XYCoordinates'][0][0]) + (self._DesignParameter['aoi_out_pmos']['_DesignObj']._DesignParameter['_PPLayer']['_XWidth'] / 2)) / 2)),
																  (((self._DesignParameter['AOI_p1']['_XYCoordinates'][0][1]) + self._DesignParameter['AOI_p1']['_DesignObj']._DesignParameter['_PPLayer']['_XYCoordinates'][0][1]) - (self._DesignParameter['AOI_p1']['_DesignObj']._DesignParameter['_PPLayer']['_YWidth'] / 2))]]]

		else:
			self._DesignParameter['BP_around']['_XYCoordinates'] = [[[(((((self._DesignParameter['AOI_p1']['_XYCoordinates'][0][0]) + self._DesignParameter['AOI_p1']['_DesignObj']._DesignParameter['_PPLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['AOI_p1']['_DesignObj']._DesignParameter['_PPLayer']['_XWidth'] / 2)) / 2) + ((((self._DesignParameter['aoi_out_pmos']['_XYCoordinates'][0][0]) + self._DesignParameter['aoi_out_pmos']['_DesignObj']._DesignParameter['_PPLayer']['_XYCoordinates'][0][0]) + (self._DesignParameter['aoi_out_pmos']['_DesignObj']._DesignParameter['_PPLayer']['_XWidth'] / 2)) / 2)),
																  (((self._DesignParameter['AOI_p1']['_XYCoordinates'][0][1]) + self._DesignParameter['AOI_p1']['_DesignObj']._DesignParameter['_PPLayer']['_XYCoordinates'][0][1]) + (self._DesignParameter['AOI_p1']['_DesignObj']._DesignParameter['_PPLayer']['_YWidth'] / 2))],
																 [(((((self._DesignParameter['AOI_p1']['_XYCoordinates'][0][0]) + self._DesignParameter['AOI_p1']['_DesignObj']._DesignParameter['_PPLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['AOI_p1']['_DesignObj']._DesignParameter['_PPLayer']['_XWidth'] / 2)) / 2) + ((((self._DesignParameter['aoi_out_pmos']['_XYCoordinates'][0][0]) + self._DesignParameter['aoi_out_pmos']['_DesignObj']._DesignParameter['_PPLayer']['_XYCoordinates'][0][0]) + (self._DesignParameter['aoi_out_pmos']['_DesignObj']._DesignParameter['_PPLayer']['_XWidth'] / 2)) / 2)),
																  (((self._DesignParameter['aoi_out_pmos']['_XYCoordinates'][0][1]) + self._DesignParameter['aoi_out_pmos']['_DesignObj']._DesignParameter['_PPLayer']['_XYCoordinates'][0][1]) + (self._DesignParameter['aoi_out_pmos']['_DesignObj']._DesignParameter['_PPLayer']['_YWidth'] / 2))]]]


	# self._DesignParameter['PIMP_around_2'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['PIMP'][0], _Datatype=DesignParameters._LayerMapping['PIMP'][1], _Width=((((self._DesignParameter['pbias_pmos']['_XYCoordinates'][0][0]) + self._DesignParameter['pbias_pmos']['_DesignObj']._DesignParameter['_PPLayer']['_XYCoordinates'][0][0]) + (self._DesignParameter['pbias_pmos']['_DesignObj']._DesignParameter['_PPLayer']['_XWidth'] / 2)) - (((self._DesignParameter['aoi_out_pmos']['_XYCoordinates'][0][0]) + self._DesignParameter['aoi_out_pmos']['_DesignObj']._DesignParameter['_PPLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['aoi_out_pmos']['_DesignObj']._DesignParameter['_PPLayer']['_XWidth'] / 2))))
		# self._DesignParameter['PIMP_around_2']['_XYCoordinates'] = [[[(((((self._DesignParameter['aoi_out_pmos']['_XYCoordinates'][0][0]) + self._DesignParameter['aoi_out_pmos']['_DesignObj']._DesignParameter['_PPLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['aoi_out_pmos']['_DesignObj']._DesignParameter['_PPLayer']['_XWidth'] / 2)) / 2) + ((((self._DesignParameter['pbias_pmos']['_XYCoordinates'][0][0]) + self._DesignParameter['pbias_pmos']['_DesignObj']._DesignParameter['_PPLayer']['_XYCoordinates'][0][0]) + (self._DesignParameter['pbias_pmos']['_DesignObj']._DesignParameter['_PPLayer']['_XWidth'] / 2)) / 2)), self._DesignParameter['PIMP_around_1']['_XYCoordinates'][0][0][1]], [(((((self._DesignParameter['aoi_out_pmos']['_XYCoordinates'][0][0]) + self._DesignParameter['aoi_out_pmos']['_DesignObj']._DesignParameter['_PPLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['aoi_out_pmos']['_DesignObj']._DesignParameter['_PPLayer']['_XWidth'] / 2)) / 2) + ((((self._DesignParameter['pbias_pmos']['_XYCoordinates'][0][0]) + self._DesignParameter['pbias_pmos']['_DesignObj']._DesignParameter['_PPLayer']['_XYCoordinates'][0][0]) + (self._DesignParameter['pbias_pmos']['_DesignObj']._DesignParameter['_PPLayer']['_XWidth'] / 2)) / 2)), (((self._DesignParameter['pbias_pmos']['_XYCoordinates'][0][1]) + self._DesignParameter['pbias_pmos']['_DesignObj']._DesignParameter['_PPLayer']['_XYCoordinates'][0][1]) - (self._DesignParameter['pbias_pmos']['_DesignObj']._DesignParameter['_PPLayer']['_YWidth'] / 2))]]]
