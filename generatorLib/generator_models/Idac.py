from generatorLib import StickDiagram
from generatorLib import DesignParameters
import copy
import math
from generatorLib import DRC
from generatorLib.generator_models import idec_cells_row
from generatorLib.generator_models import ViaMet22Met3
from generatorLib.generator_models import ViaMet52Met6

class IDAC(StickDiagram._StickDiagram):
	def __init__(self, _DesignParameter=None, _Name='EasyDebugModule'):
		if _DesignParameter != None:
			self._DesignParameter = _DesignParameter
		else:
			self._DesignParameter = dict(_Name=self._NameDeclaration(_Name=_Name), _GDSFile=self._GDSObjDeclaration(_GDSFile=None))
		self._DesignParameter['_Name']['Name'] = _Name

	def _CalculateDesignParameter(self, _X_NUM=10, _Y_NUM=4, _Y_NUM_L=2, W_pbias_pmos=830, W_pbias_pmos_L=660, _Idac_cell={'Cell_height': 2108, 'nf_aoi_out_pmos': 1, 'W_aoi_out_pmos': 1000, 'L_aoi_out_pmos': 30, 'aoi_out_pmos_y': 1000, 'aoi_XVT': 'RVT', 'nf_pbias_pmos': 2, 'L_pbias_pmos': 300, 'pbias_pmos_XVT': 'LVT', 'nf_AOI_mos': 1, 'W_AOI_pmos': 200, 'W_AOI_nmos': 200, 'L_AOI_mos': 30, 'VDD2aoi_pmos': 550, 'VSS2aoi_nmos': 350}, TIEL_flag=0):
	
		drc = DRC.DRC()
		_Name = self._DesignParameter['_Name']['_Name']
		
		# self._DesignParameter['Idac_row'] = self._SrefElementDeclaration(_DesignObj=idec_cells_row.Idac_cells_row(_Name='Idac_rowIn{}'.format(_Name)))[0]
		# self._DesignParameter['Idac_row']['_DesignObj']._CalculateDesignParameter(**dict(X_num=_X_NUM, **Idac_cell))

		if (_Y_NUM+_Y_NUM_L) == 1 :
			name = 'Row_0'
			name2 = 'Row_0{}'
			self._DesignParameter[name] = self._SrefElementDeclaration(_DesignObj=idec_cells_row.Idac_cells_row(_Name=name2.format(_Name)))[0]
			self._DesignParameter[name]['_DesignObj']._CalculateDesignParameter(**dict(X_num=_X_NUM, _W_pbias_pmos=W_pbias_pmos, Idac_cell=_Idac_cell))
			self._DesignParameter[name]['_XYCoordinates'] = [[0.0, 0.0]]

		else :
			for i in range(0,_Y_NUM) :
				name = 'Row_%d'%i
				name2 = 'Row_%d{}'%i
				self._DesignParameter[name] = self._SrefElementDeclaration(_DesignObj=idec_cells_row.Idac_cells_row(_Name=name2.format(_Name)))[0]
				self._DesignParameter[name]['_DesignObj']._CalculateDesignParameter(**dict(X_num=_X_NUM, _W_pbias_pmos=W_pbias_pmos, _Odd_row_flag=i%2, Idac_cell=_Idac_cell))

				if i%2==1 :
					self._DesignParameter[name]['_Reflect'] = [1, 0, 0]

				RYdistance = ((self._DesignParameter['Row_0']['_DesignObj']._DesignParameter['Idac_cells']['_DesignObj']._DesignParameter['VDD']['_XYCoordinates'][0][1]) - (self._DesignParameter['Row_0']['_DesignObj']._DesignParameter['Idac_cells']['_DesignObj']._DesignParameter['VSS']['_XYCoordinates'][0][1]))

				self._DesignParameter[name]['_XYCoordinates'] = [[0.0, -2*RYdistance*(i//2)]]
			for i in range(0,_Y_NUM_L) :
				name = 'Row_L_%d'%i
				name2 = 'Row_L_%d{}'%i
				self._DesignParameter[name] = self._SrefElementDeclaration(_DesignObj=idec_cells_row.Idac_cells_row(_Name=name2.format(_Name)))[0]
				self._DesignParameter[name]['_DesignObj']._CalculateDesignParameter(**dict(X_num=_X_NUM, _W_pbias_pmos=W_pbias_pmos_L, _Odd_row_flag=(_Y_NUM_L+i)%2, Idac_cell=_Idac_cell))

				if (i+_Y_NUM)%2==1 :
					self._DesignParameter[name]['_Reflect'] = [1, 0, 0]

				RYdistance = ((self._DesignParameter['Row_0']['_DesignObj']._DesignParameter['Idac_cells']['_DesignObj']._DesignParameter['VDD']['_XYCoordinates'][0][1]) - (self._DesignParameter['Row_0']['_DesignObj']._DesignParameter['Idac_cells']['_DesignObj']._DesignParameter['VSS']['_XYCoordinates'][0][1]))

				self._DesignParameter[name]['_XYCoordinates'] = [[0.0, -2*RYdistance*((i+_Y_NUM)//2)]]



		##pbias_global

		self._DesignParameter['pbias_m2_path_global'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1],
																					 _Width=self._DesignParameter['Row_0']['_DesignObj']._DesignParameter['Idac_cells']['_DesignObj']._DesignParameter['row2_rail']['_Width'])
		self._DesignParameter['pbias_via_global'] = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_Name='pbias_via_globalIn{}'.format(_Name)))[0]
		self._DesignParameter['pbias_via_global']['_DesignObj']._CalculateDesignParameterSameEnclosure(**dict(_ViaMet22Met3NumberOfCOX=7, _ViaMet22Met3NumberOfCOY=2))

		tmp = [[]]
		tmp2 = []
		for i in range(0, _Y_NUM+_Y_NUM_L):
			tmp.append([[(+ (((self._DesignParameter['Row_0']['_XYCoordinates'][0][0]) + self._DesignParameter['Row_0']['_DesignObj']._DesignParameter['Idac_cells']['_XYCoordinates'][0][0]) + self._DesignParameter['Row_0']['_DesignObj']._DesignParameter['Idac_cells']['_DesignObj']._DesignParameter['row2_rail']['_XYCoordinates'][0][1][0])),
						(+ (((self._DesignParameter['Row_0']['_XYCoordinates'][0][1]) + self._DesignParameter['Row_0']['_DesignObj']._DesignParameter['Idac_cells']['_XYCoordinates'][0][1]) + self._DesignParameter['Row_0']['_DesignObj']._DesignParameter['Idac_cells']['_DesignObj']._DesignParameter['row2_rail']['_XYCoordinates'][0][1][1]-2*RYdistance*(i//2)))],
						[((((self._DesignParameter['Row_0']['_XYCoordinates'][0][0]) + self._DesignParameter['Row_0']['_DesignObj']._DesignParameter['Idac_cells']['_XYCoordinates'][0][0]) + self._DesignParameter['Row_0']['_DesignObj']._DesignParameter['Idac_cells']['_DesignObj']._DesignParameter['row2_rail']['_XYCoordinates'][0][1][0]) + 1163),
						(((self._DesignParameter['Row_0']['_XYCoordinates'][0][1]) + self._DesignParameter['Row_0']['_DesignObj']._DesignParameter['Idac_cells']['_XYCoordinates'][0][1]) + self._DesignParameter['Row_0']['_DesignObj']._DesignParameter['Idac_cells']['_DesignObj']._DesignParameter['row2_rail']['_XYCoordinates'][0][1][1]-2*RYdistance*(i//2))]])
			tmp2.append([((((self._DesignParameter['Row_0']['_XYCoordinates'][0][0]) + self._DesignParameter['Row_0']['_DesignObj']._DesignParameter['Idac_cells']['_XYCoordinates'][0][0]) + self._DesignParameter['Row_0']['_DesignObj']._DesignParameter['Idac_cells']['_DesignObj']._DesignParameter['row2_rail']['_XYCoordinates'][0][1][0]) + 1163),
		 				(((self._DesignParameter['Row_0']['_XYCoordinates'][0][1]) + self._DesignParameter['Row_0']['_DesignObj']._DesignParameter['Idac_cells']['_XYCoordinates'][0][1]) + self._DesignParameter['Row_0']['_DesignObj']._DesignParameter['Idac_cells']['_DesignObj']._DesignParameter['row2_rail']['_XYCoordinates'][0][1][1] - 2 * RYdistance * (i // 2))])
		self._DesignParameter['pbias_m2_path_global']['_XYCoordinates'] = tmp
		self._DesignParameter['pbias_via_global']['_XYCoordinates'] = tmp2

		del tmp, tmp2

		self._DesignParameter['pbias_m3_path_global'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0], _Datatype=DesignParameters._LayerMapping['METAL3'][1], _Width=self._DesignParameter['pbias_via_global']['_DesignObj']._DesignParameter['_Met3Layer']['_XWidth'])
		self._DesignParameter['pbias_m3_path_global']['_XYCoordinates'] = [[[((self._DesignParameter['pbias_via_global']['_XYCoordinates'][3][0]) + self._DesignParameter['pbias_via_global']['_DesignObj']._DesignParameter['_Met3Layer']['_XYCoordinates'][0][0]),
																			 ((((self._DesignParameter['Row_0']['_XYCoordinates'][0][1]) + self._DesignParameter['Row_0']['_DesignObj']._DesignParameter['Idac_cells']['_XYCoordinates'][0][1]) + self._DesignParameter['Row_0']['_DesignObj']._DesignParameter['Idac_cells']['_DesignObj']._DesignParameter['VDD']['_XYCoordinates'][0][1]) + self._DesignParameter['Row_0']['_DesignObj']._DesignParameter['Idac_cells']['_DesignObj']._DesignParameter['VDD']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1])],
																			[((self._DesignParameter['pbias_via_global']['_XYCoordinates'][3][0]) + self._DesignParameter['pbias_via_global']['_DesignObj']._DesignParameter['_Met3Layer']['_XYCoordinates'][0][0]),
																			 (((((self._DesignParameter['Row_0']['_XYCoordinates'][0][1]) + self._DesignParameter['Row_0']['_DesignObj']._DesignParameter['Idac_cells']['_XYCoordinates'][0][1]) + self._DesignParameter['Row_0']['_DesignObj']._DesignParameter['Idac_cells']['_DesignObj']._DesignParameter['VDD']['_XYCoordinates'][0][1]) + self._DesignParameter['Row_0']['_DesignObj']._DesignParameter['Idac_cells']['_DesignObj']._DesignParameter['VDD']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) - ((_Y_NUM+_Y_NUM_L) * RYdistance))]]]

		self._DesignParameter['Row_m6_paths_global'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL6'][0], _Datatype=DesignParameters._LayerMapping['METAL6'][1],
																					 _Width=self._DesignParameter['Row_0']['_DesignObj']._DesignParameter['Idac_cells']['_DesignObj']._DesignParameter['row1_rail']['_Width'])

		self._DesignParameter['Row_via'] = self._SrefElementDeclaration(_DesignObj=ViaMet52Met6._ViaMet52Met6(_Name='Row_viaIn{}'.format(_Name)))[0]
		self._DesignParameter['Row_via']['_DesignObj']._CalculateViaMet52Met6DesignParameter(**dict(_ViaMet52Met6NumberOfCOX=1, _ViaMet52Met6NumberOfCOY=2, _MetalType={'METAL1': 'X', 'METAL2': 'X', 'METAL3': 'X', 'METAL4': 'X', 'METAL5': 'X', 'METAL6': 'X', 'METAL7': 'X', 'METAL8': 'Z', 'METAL9': 'Z'}))

		Row_m5_distance = self._DesignParameter['Row_via']['_DesignObj']._DesignParameter['_Met5Layer']['_XWidth'] + drc._MetalxMinSpace2 * 3

		tmp = [[]]
		for i in range (0, _Y_NUM+_Y_NUM_L+1):
			tmp.append([[(+ (((self._DesignParameter['Row_0']['_XYCoordinates'][0][0]) + self._DesignParameter['Row_0']['_DesignObj']._DesignParameter['Idac_cells']['_XYCoordinates'][-1][0]) + self._DesignParameter['Row_0']['_DesignObj']._DesignParameter['Idac_cells']['_DesignObj']._DesignParameter['row1_rail']['_XYCoordinates'][0][0][0])),
						(+ (((self._DesignParameter['Row_0']['_XYCoordinates'][0][1]) + self._DesignParameter['Row_0']['_DesignObj']._DesignParameter['Idac_cells']['_XYCoordinates'][-1][1]) + self._DesignParameter['Row_0']['_DesignObj']._DesignParameter['Idac_cells']['_DesignObj']._DesignParameter['row1_rail']['_XYCoordinates'][0][0][1]-i*RYdistance))],
						[((((self._DesignParameter['Row_0']['_XYCoordinates'][0][0]) + self._DesignParameter['Row_0']['_DesignObj']._DesignParameter['Idac_cells']['_XYCoordinates'][-1][0]) + self._DesignParameter['Row_0']['_DesignObj']._DesignParameter['Idac_cells']['_DesignObj']._DesignParameter['row1_rail']['_XYCoordinates'][0][0][0]) - 500 - (_Y_NUM+_Y_NUM_L+1)*Row_m5_distance),
						(((self._DesignParameter['Row_0']['_XYCoordinates'][0][1]) + self._DesignParameter['Row_0']['_DesignObj']._DesignParameter['Idac_cells']['_XYCoordinates'][-1][1]) + self._DesignParameter['Row_0']['_DesignObj']._DesignParameter['Idac_cells']['_DesignObj']._DesignParameter['row1_rail']['_XYCoordinates'][0][0][1]-i*RYdistance)]])
		self._DesignParameter['Row_m6_paths_global']['_XYCoordinates'] = tmp
		del tmp

		tmp = []
		for i in range (0, _Y_NUM+_Y_NUM_L+1):
			tmp.append([((self._DesignParameter['Row_m6_paths_global']['_XYCoordinates'][1][(- 1)][0]) + (i * Row_m5_distance)), (self._DesignParameter['Row_m6_paths_global']['_XYCoordinates'][-i-1][(-1)][1])])
			pin_name='Row_<%d>'%i
			self._DesignParameter[pin_name] = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL5PIN'][0], _Datatype=DesignParameters._LayerMapping['METAL5PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0], _XYCoordinates=[[0, 0]], _Mag=0.1, _Angle=270, _TEXT=pin_name)
			self._DesignParameter[pin_name]['_XYCoordinates'] = [[((self._DesignParameter['Row_m6_paths_global']['_XYCoordinates'][1][-1][0]) + ((_Y_NUM+_Y_NUM_L-i) * Row_m5_distance)), (self._DesignParameter['Row_m6_paths_global']['_XYCoordinates'][1][-1][1])]]
		self._DesignParameter['Row_via']['_XYCoordinates'] = tmp
		del tmp

		self._DesignParameter['Row_m5'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL5'][0], _Datatype=DesignParameters._LayerMapping['METAL5'][1], _Width=drc._MetalxMinWidth)
		tmp = [[]]
		for i in range (0, _Y_NUM+_Y_NUM_L+1):
			tmp.append([[(self._DesignParameter['Row_via']['_XYCoordinates'][i][0] + self._DesignParameter['Row_via']['_DesignObj']._DesignParameter['_Met5Layer']['_XYCoordinates'][0][0]),
						(self._DesignParameter['Row_m6_paths_global']['_XYCoordinates'][1][0][1])+self._DesignParameter['Row_via']['_DesignObj']._DesignParameter['_Met5Layer']['_YWidth']/2],
						[(self._DesignParameter['Row_via']['_XYCoordinates'][i][0] + self._DesignParameter['Row_via']['_DesignObj']._DesignParameter['_Met5Layer']['_XYCoordinates'][0][0]),
						(self._DesignParameter['Row_m6_paths_global']['_XYCoordinates'][(- 1)][0][1])-self._DesignParameter['Row_via']['_DesignObj']._DesignParameter['_Met5Layer']['_YWidth']/2]])
		self._DesignParameter['Row_m5']['_XYCoordinates'] = tmp
		del tmp

		self._DesignParameter['PBIAS'] = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3PIN'][0], _Datatype=DesignParameters._LayerMapping['METAL3PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0], _XYCoordinates=[[0, 0]], _Mag=0.1, _Angle=0, _TEXT='PBIAS')
		self._DesignParameter['PBIAS']['_XYCoordinates'] = [[(+ (self._DesignParameter['pbias_m3_path_global']['_XYCoordinates'][0][0][0])), (+ (self._DesignParameter['pbias_m3_path_global']['_XYCoordinates'][0][0][1]))]]

		for i in range (0, _X_NUM) :
			pin_name_col='Col_<%d>'%i
			self._DesignParameter[pin_name_col] = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL5PIN'][0], _Datatype=DesignParameters._LayerMapping['METAL5PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0], _XYCoordinates=[[0, 0]], _Mag=0.1, _Angle=0, _TEXT=pin_name_col)
			self._DesignParameter[pin_name_col]['_XYCoordinates'] = [[(+ (((self._DesignParameter['Row_0']['_XYCoordinates'][0][0]) + self._DesignParameter['Row_0']['_DesignObj']._DesignParameter['Idac_cells']['_XYCoordinates'][i][0]) + self._DesignParameter['Row_0']['_DesignObj']._DesignParameter['Idac_cells']['_DesignObj']._DesignParameter['col']['_XYCoordinates'][0][0][0])), (+ (((self._DesignParameter['Row_0']['_XYCoordinates'][0][1]) + self._DesignParameter['Row_0']['_DesignObj']._DesignParameter['Idac_cells']['_XYCoordinates'][i][1]) + self._DesignParameter['Row_0']['_DesignObj']._DesignParameter['Idac_cells']['_DesignObj']._DesignParameter['col']['_XYCoordinates'][0][0][1]))]]

		## For 1semicon design (Connects Last Row & First Col)
		if TIEL_flag == 1 :
			self._DesignParameter['TIEL_VIA5to6'] = self._SrefElementDeclaration(_DesignObj=ViaMet52Met6._ViaMet52Met6(_Name='TIEL_VIA5to6In{}'.format(_Name)))[0]
			self._DesignParameter['TIEL_VIA5to6']['_DesignObj']._CalculateViaMet52Met6DesignParameter(**dict(_ViaMet52Met6NumberOfCOX=1, _ViaMet52Met6NumberOfCOY=2, _MetalType={'METAL1': 'X', 'METAL2': 'X', 'METAL3': 'X', 'METAL4': 'X', 'METAL5': 'X', 'METAL6': 'X', 'METAL7': 'X', 'METAL8': 'Z', 'METAL9': 'Z'}))
			self._DesignParameter['TIEL_VIA5to6']['_XYCoordinates'] = [[(+ (((self._DesignParameter['Row_0']['_XYCoordinates'][0][0]) + self._DesignParameter['Row_0']['_DesignObj']._DesignParameter['Idac_cells']['_XYCoordinates'][(_X_NUM-1)][0]) + self._DesignParameter['Row_0']['_DesignObj']._DesignParameter['Idac_cells']['_DesignObj']._DesignParameter['col']['_XYCoordinates'][0][0][0])),
																		(self._DesignParameter['Row_via']['_XYCoordinates'][0][1])]]

