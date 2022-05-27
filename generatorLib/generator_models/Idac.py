from generatorLib import StickDiagram
from generatorLib import DesignParameters
import copy
import math
from generatorLib import DRC
from generatorLib.generator_models import idec_cells_row

class EasyDebugModule(StickDiagram._StickDiagram):
	def __init__(self, _DesignParameter=None, _Name='EasyDebugModule'):
		if _DesignParameter != None:
			self._DesignParameter = _DesignParameter
		else:
			self._DesignParameter = dict(_Name=self._NameDeclaration(_Name=_Name), _GDSFile=self._GDSObjDeclaration(_GDSFile=None))
		self._DesignParameter['_Name']['Name'] = _Name

	def _CalculateDesignParameter(self, _X_NUM=10, _Y_NUM=4, _Idac_cell={'Cell_height': 2108, 'nf_aoi_out_pmos': 1, 'W_aoi_out_pmos': 1000, 'L_aoi_out_pmos': 30, 'aoi_out_pmos_y': 1000, 'aoi_XVT': 'RVT', 'nf_pbias_pmos': 2, 'W_pbias_pmos': 830, 'L_pbias_pmos': 300, 'pbias_pmos_XVT': 'LVT', 'nf_AOI_mos': 1, 'W_AOI_pmos': 200, 'W_AOI_nmos': 200, 'L_AOI_mos': 30, 'VDD2aoi_pmos': 550, 'VSS2aoi_nmos': 350}):
	
		drc = DRC.DRC()
		_Name = self._DesignParameter['_Name']['_Name']
		
		# self._DesignParameter['Idac_row'] = self._SrefElementDeclaration(_DesignObj=idec_cells_row.Idac_cells_row(_Name='Idac_rowIn{}'.format(_Name)))[0]
		# self._DesignParameter['Idac_row']['_DesignObj']._CalculateDesignParameter(**dict(X_num=_X_NUM, **Idac_cell))

		if _Y_NUM == 1 :
			name = 'Row_0'
			name2 = 'Row_0{}'
			self._DesignParameter[name] = self._SrefElementDeclaration(_DesignObj=idec_cells_row.Idac_cells_row(_Name=name2.format(_Name)))[0]
			self._DesignParameter[name]['_DesignObj']._CalculateDesignParameter(**dict(X_num=_X_NUM, Idac_cell=_Idac_cell))
			self._DesignParameter[name]['_XYCoordinates'] = [[0.0, 0.0]]

		else :
			for i in range(0,_Y_NUM) :
				name = 'Row_%d'%i
				name2 = 'Row_%d{}'%i
				self._DesignParameter[name] = self._SrefElementDeclaration(_DesignObj=idec_cells_row.Idac_cells_row(_Name=name2.format(_Name)))[0]
				self._DesignParameter[name]['_DesignObj']._CalculateDesignParameter(**dict(X_num=_X_NUM, Idac_cell=_Idac_cell))

				if i%2==1 :
					self._DesignParameter[name]['_Reflect'] = [1, 0, 0]

				RYdistance = ((self._DesignParameter['Row_0']['_DesignObj']._DesignParameter['Idac_cells']['_DesignObj']._DesignParameter['VDD']['_XYCoordinates'][0][1]) - (self._DesignParameter['Row_0']['_DesignObj']._DesignParameter['Idac_cells']['_DesignObj']._DesignParameter['VSS']['_XYCoordinates'][0][1]))

				self._DesignParameter[name]['_XYCoordinates'] = [[0.0, -2*RYdistance*(i//2)]]

