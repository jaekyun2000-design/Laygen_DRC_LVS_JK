from generatorLib import StickDiagram
from generatorLib import DesignParameters
import copy
import math
from generatorLib import DRC
from generatorLib.generator_models import idac_cell

class Idac_cells_row(StickDiagram._StickDiagram):
	def __init__(self, _DesignParameter=None, _Name='Idac_cells_row'):
		if _DesignParameter != None:
			self._DesignParameter = _DesignParameter
		else:
			self._DesignParameter = dict(_Name=self._NameDeclaration(_Name=_Name), _GDSFile=self._GDSObjDeclaration(_GDSFile=None))
		self._DesignParameter['_Name']['Name'] = _Name

	def _CalculateDesignParameter(self, X_num=10, _W_pbias_pmos=830, _Odd_row_flag=0, Idac_cell={'Cell_height':2108, 'nf_aoi_out_pmos':1, 'W_aoi_out_pmos':1000, 'L_aoi_out_pmos':30, 'aoi_out_pmos_y':1000, 'aoi_XVT':'RVT', 'nf_pbias_pmos':2,'L_pbias_pmos':300, 'pbias_pmos_XVT':'LVT', 'nf_AOI_mos':1, 'W_AOI_pmos':200, 'W_AOI_nmos':200, 'L_AOI_mos':30, 'VDD2aoi_pmos':58, 'VSS2aoi_nmos':90}):
	
		drc = DRC.DRC()
		_Name = self._DesignParameter['_Name']['_Name']
		
		self._DesignParameter['Idac_cells'] = self._SrefElementDeclaration(_DesignObj=idac_cell.Idac_cell(_Name='Idac_cellsIn{}'.format(_Name)))[0]
		self._DesignParameter['Idac_cells']['_DesignObj']._CalculateDesignParameter(**dict(W_pbias_pmos=_W_pbias_pmos, Odd_row_flag=_Odd_row_flag, **Idac_cell))
		_XYCoordinateofIdac = [[0,0]]


		# RYdistance = ((self._DesignParameter['Idac_cells']['_DesignObj']._DesignParameter['VDD']['_XYCoordinates'][0][1]) - (self._DesignParameter['Idac_cells']['_DesignObj']._DesignParameter['VSS']['_XYCoordinates'][0][1]))
		RXdistance = (((self._DesignParameter['Idac_cells']['_DesignObj']._DesignParameter['VDD']['_XYCoordinates'][0][0]) + self._DesignParameter['Idac_cells']['_DesignObj']._DesignParameter['VDD']['_DesignObj']._DesignParameter['_COLayer']['_XYCoordinates'][(- 1)][0]) - ((self._DesignParameter['Idac_cells']['_DesignObj']._DesignParameter['VDD']['_XYCoordinates'][0][0]) + self._DesignParameter['Idac_cells']['_DesignObj']._DesignParameter['VDD']['_DesignObj']._DesignParameter['_COLayer']['_XYCoordinates'][0][0]))

		tmp = []
		for i in range(0, X_num) :
				tmp.append([_XYCoordinateofIdac[0][0] - i * RXdistance,
							_XYCoordinateofIdac[0][1]])

		self._DesignParameter['Idac_cells']['_XYCoordinates'] = tmp

		del tmp