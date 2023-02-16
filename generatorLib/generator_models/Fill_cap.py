from generatorLib import StickDiagram
from generatorLib import DesignParameters
import copy
import math
from generatorLib import DRC
from generatorLib.generator_models import Fill_cap_mos
from generatorLib.generator_models import ViaPoly2Met1
from generatorLib.generator_models import SupplyRails

class FillCapCell(StickDiagram._StickDiagram):
	def __init__(self, _DesignParameter=None, _Name='FillCapCell'):
		if _DesignParameter != None:
			self._DesignParameter = _DesignParameter
		else:
			self._DesignParameter = dict(_Name=self._NameDeclaration(_Name=_Name), _GDSFile=self._GDSObjDeclaration(_GDSFile=None))
		self._DesignParameter['_Name']['Name'] = _Name

	def calc_minHeight(self,Cap_poly_x_length=500,Cap_poly_nmos_y_width=200,Cap_poly_pmos_y_width=500,Cell_height=1800,Power_CO_Pitch=150,Power_CO_Num=None,vss_nmosgate_space=58,vdd_pmosgate_space=58,gate2pwr_co_num=2, XVT='RVT'):
		drc = DRC.DRC()

		Poly_NW_edge_spacing = drc._PolygateMinSpace2 // 2

		Min_height = drc._PolylayeroverOd2 * 4 + vss_nmosgate_space + vdd_pmosgate_space + Cap_poly_nmos_y_width + Cap_poly_pmos_y_width + 3*drc._PolygateMinSpace2 + (drc._CoMinWidth + 2 * drc._CoMinEnclosureByPOAtLeastTwoSide)*2 + 80

		return Min_height

	def _CalculateDesignParameter(self,Cap_poly_x_length=500,Cap_poly_nmos_y_width=200,Cap_poly_pmos_y_width=500,Cell_height=1800,Power_CO_Pitch=150,Power_CO_Num=None,vss_nmosgate_space=58,vdd_pmosgate_space=58,gate2pwr_co_num=2, XVT='RVT'):
	
		drc = DRC.DRC()
		_Name = self._DesignParameter['_Name']['_Name']

		Poly_NW_edge_spacing = drc._PolygateMinSpace2 // 2

		Min_height = drc._PolylayeroverOd2 * 4 + vss_nmosgate_space + vdd_pmosgate_space + Cap_poly_nmos_y_width + Cap_poly_pmos_y_width + 3*drc._PolygateMinSpace2 + (drc._CoMinWidth + 2 * drc._CoMinEnclosureByPOAtLeastTwoSide)*2 + 80

		if Min_height > Cell_height :
			raise NotImplementedError
		elif Power_CO_Pitch < (drc._VIAxMinSpace + drc._VIAxMinWidth) :
			raise NotImplementedError
		else:

			Auto_Numpitch_flag = 0
			if Power_CO_Num == None :
				Power_CO_Num = 1
				Auto_Numpitch_flag = 1

			self._DesignParameter['vssrail'] = self._SrefElementDeclaration(_DesignObj=SupplyRails.SupplyRail(_Name='vssrailIn{}'.format(_Name)))[0]
			self._DesignParameter['vssrail']['_DesignObj']._CalculateDesignParameter(**dict(NumPitch=Power_CO_Num, UnitPitch=Power_CO_Pitch, Met1YWidth=80, Met2YWidth=300, PpNpYWidth=180, isPbody=True, deleteViaAndMet1=False))
			self._DesignParameter['vssrail']['_XYCoordinates'] = [[0.0, 0.0]]
			self._DesignParameter['vddrail'] = self._SrefElementDeclaration(_DesignObj=SupplyRails.SupplyRail(_Name='vddrailIn{}'.format(_Name)))[0]
			self._DesignParameter['vddrail']['_DesignObj']._CalculateDesignParameter(**dict(NumPitch=Power_CO_Num, UnitPitch=Power_CO_Pitch, Met1YWidth=80, Met2YWidth=300, PpNpYWidth=180, isPbody=False, deleteViaAndMet1=False))
			self._DesignParameter['vddrail']['_XYCoordinates'] = [[self._DesignParameter['vssrail']['_XYCoordinates'][0][0], (self._DesignParameter['vssrail']['_XYCoordinates'][0][1] + Cell_height)]]

			self._DesignParameter['_VDDpin'] = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2PIN'][0], _Datatype=DesignParameters._LayerMapping['METAL2PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0], _XYCoordinates=[[0, 0]], _Mag=0.05, _Angle=0, _TEXT='VDD')
			self._DesignParameter['_VSSpin'] = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2PIN'][0], _Datatype=DesignParameters._LayerMapping['METAL2PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0], _XYCoordinates=[[0, 0]], _Mag=0.05, _Angle=0, _TEXT='VSS')
			self._DesignParameter['_VDDpin']['_XYCoordinates']=self._DesignParameter['vddrail']['_XYCoordinates']
			self._DesignParameter['_VSSpin']['_XYCoordinates']=self._DesignParameter['vssrail']['_XYCoordinates']

			self._DesignParameter['nmoscap'] = self._SrefElementDeclaration(_DesignObj=Fill_cap_mos.FILLCAP_MOS(_Name='nmoscapIn{}'.format(_Name)))[0]
			self._DesignParameter['nmoscap']['_DesignObj']._CalculateDesignParameter(**dict(gate_x_length=Cap_poly_x_length, gate_y_width=Cap_poly_nmos_y_width, Dummy_width=40, _XVT=XVT, pmos_flag=0))
			self._DesignParameter['nmoscap']['_XYCoordinates'] = [[self._DesignParameter['vssrail']['_XYCoordinates'][0][0], ((((self._DesignParameter['vssrail']['_XYCoordinates'][0][1] + self._DesignParameter['vssrail']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) + (self._DesignParameter['vssrail']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // 2)) + (self._DesignParameter['nmoscap']['_DesignObj']._DesignParameter['N_poly']['_YWidth'] // 2)) + vss_nmosgate_space)]]
			self._DesignParameter['pmoscap'] = self._SrefElementDeclaration(_DesignObj=Fill_cap_mos.FILLCAP_MOS(_Name='pmoscapIn{}'.format(_Name)))[0]
			self._DesignParameter['pmoscap']['_DesignObj']._CalculateDesignParameter(**dict(gate_x_length=Cap_poly_x_length, gate_y_width=Cap_poly_pmos_y_width, Dummy_width=40, _XVT=XVT, pmos_flag=1))
			self._DesignParameter['pmoscap']['_XYCoordinates'] = [[(self._DesignParameter['vddrail']['_XYCoordinates'][0][0] + self._DesignParameter['vddrail']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0]), ((((self._DesignParameter['vddrail']['_XYCoordinates'][0][1] + self._DesignParameter['vddrail']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) - (self._DesignParameter['vddrail']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // 2)) - (self._DesignParameter['pmoscap']['_DesignObj']._DesignParameter['N_poly']['_YWidth'] // 2)) - vdd_pmosgate_space)]]
			self._DesignParameter['PIMP'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['PIMP'][0], _Datatype=DesignParameters._LayerMapping['PIMP'][1], _Width=self._DesignParameter['pmoscap']['_DesignObj']._DesignParameter['XVT']['_XWidth'])
			self._DesignParameter['PIMP']['_XYCoordinates'] = [[[(self._DesignParameter['pmoscap']['_XYCoordinates'][0][0] + self._DesignParameter['pmoscap']['_DesignObj']._DesignParameter['XVT']['_XYCoordinates'][0][0]), ((self._DesignParameter['pmoscap']['_XYCoordinates'][0][1] + self._DesignParameter['pmoscap']['_DesignObj']._DesignParameter['XVT']['_XYCoordinates'][0][1]) + (self._DesignParameter['pmoscap']['_DesignObj']._DesignParameter['XVT']['_YWidth'] // 2))], [(self._DesignParameter['pmoscap']['_XYCoordinates'][0][0] + self._DesignParameter['pmoscap']['_DesignObj']._DesignParameter['XVT']['_XYCoordinates'][0][0]), ((((self._DesignParameter['pmoscap']['_XYCoordinates'][0][1] + self._DesignParameter['pmoscap']['_DesignObj']._DesignParameter['N_poly']['_XYCoordinates'][0][1]) - (self._DesignParameter['pmoscap']['_DesignObj']._DesignParameter['N_poly']['_YWidth'] // 2)) // 2) + (((self._DesignParameter['nmoscap']['_XYCoordinates'][0][1] + self._DesignParameter['nmoscap']['_DesignObj']._DesignParameter['N_poly']['_XYCoordinates'][0][1]) + (self._DesignParameter['nmoscap']['_DesignObj']._DesignParameter['N_poly']['_YWidth'] // 2)) // 2))]]]


			if DesignParameters._Technology == 'SS28nm':
				assert XVT in ('SLVT', 'LVT', 'RVT', 'HVT')
				self._DesignParameter['XVT'] = self._PathElementDeclaration(
					_Layer=DesignParameters._LayerMapping[XVT][0], _Datatype=DesignParameters._LayerMapping[XVT][1])

			elif DesignParameters._Technology == 'TSMC65nm':
				pass  # No Need to Modify XVT Layer
			else:
				raise NotImplementedError

			#self._DesignParameter['XVT'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['RVT'][0], _Datatype=DesignParameters._LayerMapping['RVT'][1], _Width=self._DesignParameter['nmoscap']['_DesignObj']._DesignParameter['XVT']['_XWidth'])
			self._DesignParameter['XVT']['_Width'] = self._DesignParameter['nmoscap']['_DesignObj']._DesignParameter['XVT']['_XWidth']
			self._DesignParameter['XVT']['_XYCoordinates'] = [[[(self._DesignParameter['pmoscap']['_XYCoordinates'][0][0] + self._DesignParameter['pmoscap']['_DesignObj']._DesignParameter['XVT']['_XYCoordinates'][0][0]), ((self._DesignParameter['pmoscap']['_XYCoordinates'][0][1] + self._DesignParameter['pmoscap']['_DesignObj']._DesignParameter['XVT']['_XYCoordinates'][0][1]) + (self._DesignParameter['pmoscap']['_DesignObj']._DesignParameter['XVT']['_YWidth'] // 2))], [(self._DesignParameter['pmoscap']['_XYCoordinates'][0][0] + self._DesignParameter['pmoscap']['_DesignObj']._DesignParameter['XVT']['_XYCoordinates'][0][0]), ((self._DesignParameter['nmoscap']['_XYCoordinates'][0][1] + self._DesignParameter['nmoscap']['_DesignObj']._DesignParameter['XVT']['_XYCoordinates'][0][1]) - (self._DesignParameter['nmoscap']['_DesignObj']._DesignParameter['XVT']['_YWidth'] // 2))]]]
			self._DesignParameter['NW'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['NWELL'][0], _Datatype=DesignParameters._LayerMapping['NWELL'][1], _Width=self._DesignParameter['pmoscap']['_DesignObj']._DesignParameter['NWELL']['_XWidth'])
			self._DesignParameter['NW']['_XYCoordinates'] = [[[(self._DesignParameter['vddrail']['_XYCoordinates'][0][0] + self._DesignParameter['vddrail']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0]), (((self._DesignParameter['vddrail']['_XYCoordinates'][0][1] + self._DesignParameter['vddrail']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) + (self._DesignParameter['vddrail']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // 2)) + drc._NwMinEnclosurePactive)], [(self._DesignParameter['vddrail']['_XYCoordinates'][0][0] + self._DesignParameter['vddrail']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0]), ((((self._DesignParameter['pmoscap']['_XYCoordinates'][0][1] + self._DesignParameter['pmoscap']['_DesignObj']._DesignParameter['N_poly']['_XYCoordinates'][0][1]) - (self._DesignParameter['pmoscap']['_DesignObj']._DesignParameter['N_poly']['_YWidth'] // 2)) // 2) + (((self._DesignParameter['nmoscap']['_XYCoordinates'][0][1] + self._DesignParameter['nmoscap']['_DesignObj']._DesignParameter['N_poly']['_XYCoordinates'][0][1]) + (self._DesignParameter['nmoscap']['_DesignObj']._DesignParameter['N_poly']['_YWidth'] // 2)) // 2))]]]
			self._DesignParameter['n_polyrouting'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _Width=(drc._CoMinWidth + (2 * drc._CoMinEnclosureByPOAtLeastTwoSide)))
			self._DesignParameter['n_polyrouting']['_XYCoordinates'] = [[[((self._DesignParameter['nmoscap']['_XYCoordinates'][0][0] + self._DesignParameter['nmoscap']['_DesignObj']._DesignParameter['N_poly']['_XYCoordinates'][0][0]) + (self._DesignParameter['nmoscap']['_DesignObj']._DesignParameter['N_poly']['_XWidth'] // 2)), ((((((self._DesignParameter['nmoscap']['_XYCoordinates'][0][1] + self._DesignParameter['nmoscap']['_DesignObj']._DesignParameter['N_poly']['_XYCoordinates'][0][1]) + (self._DesignParameter['nmoscap']['_DesignObj']._DesignParameter['N_poly']['_YWidth'] // 2)) // 2) + (((self._DesignParameter['pmoscap']['_XYCoordinates'][0][1] + self._DesignParameter['pmoscap']['_DesignObj']._DesignParameter['N_poly']['_XYCoordinates'][0][1]) - (self._DesignParameter['pmoscap']['_DesignObj']._DesignParameter['N_poly']['_YWidth'] // 2)) // 2)) - ((drc._CoMinWidth + (2 * drc._CoMinEnclosureByPOAtLeastTwoSide)) // 2)) - Poly_NW_edge_spacing)], [((self._DesignParameter['pmoscap']['_XYCoordinates'][0][0] + self._DesignParameter['pmoscap']['_DesignObj']._DesignParameter['DIFF_boundary_2']['_XYCoordinates'][0][0]) - (self._DesignParameter['pmoscap']['_DesignObj']._DesignParameter['DIFF_boundary_2']['_XWidth'] // 2)), ((((((self._DesignParameter['nmoscap']['_XYCoordinates'][0][1] + self._DesignParameter['nmoscap']['_DesignObj']._DesignParameter['N_poly']['_XYCoordinates'][0][1]) + (self._DesignParameter['nmoscap']['_DesignObj']._DesignParameter['N_poly']['_YWidth'] // 2)) // 2) + (((self._DesignParameter['pmoscap']['_XYCoordinates'][0][1] + self._DesignParameter['pmoscap']['_DesignObj']._DesignParameter['N_poly']['_XYCoordinates'][0][1]) - (self._DesignParameter['pmoscap']['_DesignObj']._DesignParameter['N_poly']['_YWidth'] // 2)) // 2)) - ((drc._CoMinWidth + (2 * drc._CoMinEnclosureByPOAtLeastTwoSide)) // 2)) - Poly_NW_edge_spacing)]]]
			self._DesignParameter['p_polyrouting'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _Width=(drc._CoMinWidth + (2 * drc._CoMinEnclosureByPOAtLeastTwoSide)))
			self._DesignParameter['p_polyrouting']['_XYCoordinates'] = [[[((self._DesignParameter['pmoscap']['_XYCoordinates'][0][0] + self._DesignParameter['pmoscap']['_DesignObj']._DesignParameter['N_poly']['_XYCoordinates'][0][0]) - (self._DesignParameter['pmoscap']['_DesignObj']._DesignParameter['N_poly']['_XWidth'] // 2)), ((((((self._DesignParameter['pmoscap']['_XYCoordinates'][0][1] + self._DesignParameter['pmoscap']['_DesignObj']._DesignParameter['N_poly']['_XYCoordinates'][0][1]) - (self._DesignParameter['pmoscap']['_DesignObj']._DesignParameter['N_poly']['_YWidth'] // 2)) // 2) + (((self._DesignParameter['nmoscap']['_XYCoordinates'][0][1] + self._DesignParameter['nmoscap']['_DesignObj']._DesignParameter['N_poly']['_XYCoordinates'][0][1]) + (self._DesignParameter['nmoscap']['_DesignObj']._DesignParameter['N_poly']['_YWidth'] // 2)) // 2)) + ((drc._CoMinWidth + (2 * drc._CoMinEnclosureByPOAtLeastTwoSide)) // 2)) + Poly_NW_edge_spacing)], [((self._DesignParameter['nmoscap']['_XYCoordinates'][0][0] + self._DesignParameter['nmoscap']['_DesignObj']._DesignParameter['DIFF_boundary_2']['_XYCoordinates'][0][0]) + (self._DesignParameter['nmoscap']['_DesignObj']._DesignParameter['DIFF_boundary_2']['_XWidth'] // 2)), ((((((self._DesignParameter['pmoscap']['_XYCoordinates'][0][1] + self._DesignParameter['pmoscap']['_DesignObj']._DesignParameter['N_poly']['_XYCoordinates'][0][1]) - (self._DesignParameter['pmoscap']['_DesignObj']._DesignParameter['N_poly']['_YWidth'] // 2)) // 2) + (((self._DesignParameter['nmoscap']['_XYCoordinates'][0][1] + self._DesignParameter['nmoscap']['_DesignObj']._DesignParameter['N_poly']['_XYCoordinates'][0][1]) + (self._DesignParameter['nmoscap']['_DesignObj']._DesignParameter['N_poly']['_YWidth'] // 2)) // 2)) + ((drc._CoMinWidth + (2 * drc._CoMinEnclosureByPOAtLeastTwoSide)) // 2)) + Poly_NW_edge_spacing)]]]

			self._DesignParameter['pmos_L'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=(drc._CoMinWidth + (2 * drc._CoMinEnclosureByOD)))
			self._DesignParameter['pmos_L']['_XYCoordinates'] = [[[(self._DesignParameter['pmoscap']['_XYCoordinates'][0][0] + self._DesignParameter['pmoscap']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0]), ((self._DesignParameter['vddrail']['_XYCoordinates'][0][1] + self._DesignParameter['vddrail']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) + (self._DesignParameter['vddrail']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // 2))], [(self._DesignParameter['pmoscap']['_XYCoordinates'][0][0] + self._DesignParameter['pmoscap']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0]), self._DesignParameter['n_polyrouting']['_XYCoordinates'][0][0][1]]]]
			self._DesignParameter['pmos_R'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=(drc._CoMinWidth + (2 * drc._CoMinEnclosureByOD)))
			self._DesignParameter['pmos_R']['_XYCoordinates'] = [[[(self._DesignParameter['pmoscap']['_XYCoordinates'][0][0] + self._DesignParameter['pmoscap']['_DesignObj']._DesignParameter['_Met1Layer_2']['_XYCoordinates'][0][0]), ((self._DesignParameter['pmoscap']['_XYCoordinates'][0][1] + self._DesignParameter['pmoscap']['_DesignObj']._DesignParameter['_Met1Layer_2']['_XYCoordinates'][0][1]) - (self._DesignParameter['pmoscap']['_DesignObj']._DesignParameter['_Met1Layer_2']['_YWidth'] // 2))], [(self._DesignParameter['pmoscap']['_XYCoordinates'][0][0] + self._DesignParameter['pmoscap']['_DesignObj']._DesignParameter['_Met1Layer_2']['_XYCoordinates'][0][0]), ((self._DesignParameter['vddrail']['_XYCoordinates'][0][1] + self._DesignParameter['vddrail']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) + (self._DesignParameter['vddrail']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // 2))]]]
			self._DesignParameter['nmos_L'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=(drc._CoMinWidth + (drc._CoMinEnclosureByOD * 2)))
			self._DesignParameter['nmos_L']['_XYCoordinates'] = [[[(self._DesignParameter['nmoscap']['_XYCoordinates'][0][0] + self._DesignParameter['nmoscap']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0]), ((self._DesignParameter['nmoscap']['_XYCoordinates'][0][1] + self._DesignParameter['nmoscap']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) + (self._DesignParameter['nmoscap']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // 2))], [(self._DesignParameter['nmoscap']['_XYCoordinates'][0][0] + self._DesignParameter['nmoscap']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0]), ((self._DesignParameter['vssrail']['_XYCoordinates'][0][1] + self._DesignParameter['vssrail']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) - (self._DesignParameter['vssrail']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // 2))]]]
			self._DesignParameter['nmos_R'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=(drc._CoMinWidth + (2 * drc._CoMinEnclosureByOD)))
			self._DesignParameter['nmos_R']['_XYCoordinates'] = [[[(self._DesignParameter['nmoscap']['_XYCoordinates'][0][0] + self._DesignParameter['nmoscap']['_DesignObj']._DesignParameter['_Met1Layer_2']['_XYCoordinates'][0][0]), ((self._DesignParameter['vssrail']['_XYCoordinates'][0][1] + self._DesignParameter['vssrail']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) - (self._DesignParameter['vssrail']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // 2))], [(self._DesignParameter['nmoscap']['_XYCoordinates'][0][0] + self._DesignParameter['nmoscap']['_DesignObj']._DesignParameter['_Met1Layer_2']['_XYCoordinates'][0][0]), self._DesignParameter['p_polyrouting']['_XYCoordinates'][0][0][1]]]]
			self._DesignParameter['VDD'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _XWidth=(self._DesignParameter['pmos_R']['_XYCoordinates'][0][0][0] - self._DesignParameter['pmos_L']['_XYCoordinates'][0][0][0]), _YWidth=self._DesignParameter['vddrail']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'])
			self._DesignParameter['VDD']['_XYCoordinates'] = [[(+ (self._DesignParameter['vddrail']['_XYCoordinates'][0][0] + self._DesignParameter['vddrail']['_DesignObj']._DesignParameter['_Met2Layer']['_XYCoordinates'][0][0])), (+ (self._DesignParameter['vddrail']['_XYCoordinates'][0][1] + self._DesignParameter['vddrail']['_DesignObj']._DesignParameter['_Met2Layer']['_XYCoordinates'][0][1]))]]
			self._DesignParameter['VSS'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _XWidth=(self._DesignParameter['nmos_R']['_XYCoordinates'][0][0][0] - self._DesignParameter['nmos_L']['_XYCoordinates'][0][0][0]), _YWidth=self._DesignParameter['vssrail']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'])
			self._DesignParameter['VSS']['_XYCoordinates'] = [[(+ self._DesignParameter['vssrail']['_XYCoordinates'][0][0]), (+ self._DesignParameter['vssrail']['_XYCoordinates'][0][1])]]

			self._DesignParameter['n_polyrouting2'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _XWidth=(self._DesignParameter['nmoscap']['_DesignObj']._DesignParameter['N_poly']['_XWidth'] // 5), _YWidth=(self._DesignParameter['n_polyrouting']['_XYCoordinates'][0][0][1] - ((self._DesignParameter['nmoscap']['_XYCoordinates'][0][1] + self._DesignParameter['nmoscap']['_DesignObj']._DesignParameter['N_poly']['_XYCoordinates'][0][1]))))
			self._DesignParameter['p_polyrouting2'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _XWidth=(self._DesignParameter['pmoscap']['_DesignObj']._DesignParameter['N_poly']['_XWidth'] // 5), _YWidth=(((self._DesignParameter['pmoscap']['_XYCoordinates'][0][1] + self._DesignParameter['pmoscap']['_DesignObj']._DesignParameter['N_poly']['_XYCoordinates'][0][1])) - self._DesignParameter['p_polyrouting']['_XYCoordinates'][0][0][1]))

			## for poly DRC
			if self._DesignParameter['n_polyrouting2']['_XWidth'] < drc._PolygateMinWidth :
				self._DesignParameter['n_polyrouting2']['_XWidth'] = drc._PolygateMinWidth
				self._DesignParameter['p_polyrouting2']['_XWidth'] = drc._PolygateMinWidth
			polyrouting2_x_offset = self._DesignParameter['n_polyrouting2']['_XWidth']

			self._DesignParameter['n_polyrouting2']['_XYCoordinates'] = [[(((self._DesignParameter['nmoscap']['_XYCoordinates'][0][0] + self._DesignParameter['nmoscap']['_DesignObj']._DesignParameter['N_poly']['_XYCoordinates'][0][0]) + (self._DesignParameter['nmoscap']['_DesignObj']._DesignParameter['N_poly']['_XWidth'] // 2)) - polyrouting2_x_offset/2), ((((self._DesignParameter['nmoscap']['_XYCoordinates'][0][1] + self._DesignParameter['nmoscap']['_DesignObj']._DesignParameter['N_poly']['_XYCoordinates'][0][1])) // 2) + (self._DesignParameter['n_polyrouting']['_XYCoordinates'][0][0][1] // 2))]]
			self._DesignParameter['p_polyrouting2']['_XYCoordinates'] = [[(((self._DesignParameter['pmoscap']['_XYCoordinates'][0][0] + self._DesignParameter['pmoscap']['_DesignObj']._DesignParameter['N_poly']['_XYCoordinates'][0][0]) - (self._DesignParameter['pmoscap']['_DesignObj']._DesignParameter['N_poly']['_XWidth'] // 2)) + polyrouting2_x_offset/2), ((((self._DesignParameter['pmoscap']['_XYCoordinates'][0][1] + self._DesignParameter['pmoscap']['_DesignObj']._DesignParameter['N_poly']['_XYCoordinates'][0][1])) // 2) + (self._DesignParameter['p_polyrouting']['_XYCoordinates'][0][0][1] // 2))]]

			self._DesignParameter['viaR'] = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_Name='viaRIn{}'.format(_Name)))[0]
			self._DesignParameter['viaR']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(**dict(_ViaPoly2Met1NumberOfCOX=gate2pwr_co_num, _ViaPoly2Met1NumberOfCOY=1))
			self._DesignParameter['viaR']['_XYCoordinates'] = [[(((self._DesignParameter['p_polyrouting']['_XYCoordinates'][0][1][0] - drc._Metal1MinEnclosureCO2) - (drc._CoMinWidth // 2)) - (((drc._CoMinWidth + drc._CoMinSpace2) * (gate2pwr_co_num - 1)) // 2)), self._DesignParameter['p_polyrouting']['_XYCoordinates'][0][0][1]]]
			self._DesignParameter['viaL'] = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_Name='viaLIn{}'.format(_Name)))[0]
			self._DesignParameter['viaL']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(**dict(_ViaPoly2Met1NumberOfCOX=gate2pwr_co_num, _ViaPoly2Met1NumberOfCOY=1))
			self._DesignParameter['viaL']['_XYCoordinates'] = [[(((self._DesignParameter['n_polyrouting']['_XYCoordinates'][0][1][0] + drc._Metal1MinEnclosureCO2) + (drc._CoMinWidth // 2)) + (((drc._CoMinWidth + drc._CoMinSpace) * (gate2pwr_co_num - 1)) // 2)), self._DesignParameter['n_polyrouting']['_XYCoordinates'][0][0][1]]]

			M1_span = (((self._DesignParameter['nmos_R']['_XYCoordinates'][0][0][0]) - (self._DesignParameter['nmos_R']['_Width'] / 2)) - (((self._DesignParameter['viaL']['_XYCoordinates'][0][0]) + self._DesignParameter['viaL']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0]) + (self._DesignParameter['viaL']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] / 2)))

			if M1_span < drc._Metal1MinSpace2 :
				raise NotImplementedError

			if Auto_Numpitch_flag == 1:
				Power_CO_Num = int(((self._DesignParameter['pmos_R']['_XYCoordinates'][0][0][0]) - self._DesignParameter['pmos_L']['_XYCoordinates'][0][0][0] + self._DesignParameter['pmos_L']['_Width']) // Power_CO_Pitch)
				self._DesignParameter['vssrail']['_DesignObj']._CalculateDesignParameter(**dict(NumPitch=Power_CO_Num, UnitPitch=Power_CO_Pitch, Met1YWidth=80, Met2YWidth=300, PpNpYWidth=180, isPbody=True, deleteViaAndMet1=False))
				self._DesignParameter['vddrail']['_DesignObj']._CalculateDesignParameter(**dict(NumPitch=Power_CO_Num, UnitPitch=Power_CO_Pitch, Met1YWidth=80, Met2YWidth=300, PpNpYWidth=180, isPbody=False, deleteViaAndMet1=False))


if __name__ == '__main__':
    from Private import Myinfo
    import DRCchecker_test2 as DRCchecker
    from generatorLib.IksuPack import PlaygroundBot
    import time

    My = Myinfo.USER(DesignParameters._Technology)
    Bot = PlaygroundBot.PGBot(token=My.BotToken, chat_id=My.ChatID)


    libname = 'FillCap_Gen'
    cellname = 'FilCap'
    _fileName = cellname + '.gds'

    ''' Input Parameters for Layout Object '''


    InputParams = dict(
		Cap_poly_x_length = 500,
		Cap_poly_nmos_y_width = 200,
		Cap_poly_pmos_y_width = 500,
		Cell_height = 1800,
		Power_CO_Pitch = 150,
		Power_CO_Num = None,
		vss_nmosgate_space = 58,
		vdd_pmosgate_space = 58,
		gate2pwr_co_num = 2,
		XVT = 'RVT'
    )

    Mode_DRCCheck = True  # True | False
    Num_DRCCheck = 100

    Checker = DRCchecker.DRCchecker(
        username=My.ID,
        password=My.PW,
        WorkDir=My.Dir_Work,
        DRCrunDir=My.Dir_DRCrun,
        GDSDir=My.Dir_GDS,
        libname=libname,
        cellname=cellname,
    )


    if Mode_DRCCheck:
        ErrCount = 0            # DRC error
        knownErrorCount = 0     # failed to generate design. NotImplementedError

        start_time = time.time()
        for ii in range(0, Num_DRCCheck):
            # if ii == 0:
            #     Bot.send2Bot(f'Start DRC checker...\nCellName: {cellname}\nTotal # of Run: {Num_DRCCheck}')

            forLoopCntMax = 10
            for iii in range(0, forLoopCntMax):
                try:
                    LayoutObjtmp = FillCapCell(_Name=cellname)

                    ''' ------------------------------- Random Parameters for Layout Object -------------------------------- '''
                    InputParams['Cap_poly_nmos_y_width'] = DRCchecker.RandomParam(start=200, stop=1000, step=20)
                    InputParams['Cap_poly_pmos_y_width'] = DRCchecker.RandomParam(start=200, stop=1000, step=20)
                    InputParams['Cap_poly_x_length'] = DRCchecker.RandomParam(start=200, stop=1000, step=20)
                    InputParams['Cell_height'] = (InputParams['Cap_poly_nmos_y_width'] + InputParams['Cap_poly_pmos_y_width']) + 1500
                    InputParams['Cell_height'] = LayoutObjtmp.calc_minHeight(**InputParams)
                    tmpNum = DRCchecker.RandomParam(start=1, stop=4, step=1)
                    if tmpNum == 1:
                        InputParams['XVT'] = 'SLVT'
                    elif tmpNum == 2:
                        InputParams['XVT'] = 'LVT'
                    elif tmpNum == 3:
                        InputParams['XVT'] = 'RVT'
                    elif tmpNum == 4:
                        InputParams['XVT'] = 'HVT'



                    print("   Last Layout Object's Input Parameters are   ".center(105, '='))
                    tmpStr = '\n'.join(f'{k} : {v}' for k, v in InputParams.items())
                    print(tmpStr)
                    print("".center(105, '='))

                    ''' ---------------------------------- Generate Layout Object -------------------------------------------'''
                    LayoutObj = FillCapCell(_Name=cellname)
                    LayoutObj._CalculateDesignParameter(**InputParams)
                    LayoutObj._UpdateDesignParameter2GDSStructure(_DesignParameterInDictionary=LayoutObj._DesignParameter)
                    with open(f'./{_fileName}', 'wb') as testStreamFile:
                        tmp = LayoutObj._CreateGDSStream(LayoutObj._DesignParameter['_GDSFile']['_GDSFile'])
                        tmp.write_binary_gds_stream(testStreamFile)
                except NotImplementedError:  # something known error !
                    print(f"forLoopCnt = {iii + 1}")
                    if iii + 1 == forLoopCntMax:
                        raise NotImplementedError
                else:
                    knownErrorCount = knownErrorCount + iii
                    # Bot.send2Bot(f"NotImplementedError...\nknownErrorCount = {knownErrorCount}")
                    break

            # end of for loop

            print('   Sending to FTP Server & StreamIn...   '.center(105, '#'))
            Checker.Upload2FTP()
            Checker.StreamIn(tech=DesignParameters._Technology)
            time.sleep(1.5)



    else:
        ''' ------------------------------------ Generate Layout Object ---------------------------------------------'''
        LayoutObj = FillCapCell(_Name=cellname)
        LayoutObj._CalculateDesignParameter(**InputParams)
        LayoutObj._UpdateDesignParameter2GDSStructure(_DesignParameterInDictionary=LayoutObj._DesignParameter)
        with open(f'./{_fileName}', 'wb') as testStreamFile:
            tmp = LayoutObj._CreateGDSStream(LayoutObj._DesignParameter['_GDSFile']['_GDSFile'])
            tmp.write_binary_gds_stream(testStreamFile)

        print('   Sending to FTP Server & StreamIn...   '.center(105, '#'))
        Checker.Upload2FTP()
        Checker.StreamIn(tech=DesignParameters._Technology)

    print('      Finished       '.center(105, '#'))


