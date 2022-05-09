from generatorLib import StickDiagram
from generatorLib import DesignParameters
import copy
import math
from generatorLib import DRC
from generatorLib.generator_models import Two2TwentyEight_MUX
from generatorLib.generator_models import RArray
from generatorLib.generator_models import ViaMet22Met3

class Rladder_wt_MUX(StickDiagram._StickDiagram):
	def __init__(self, _DesignParameter=None, _Name='Rladder_wt_MUX'):
		if _DesignParameter != None:
			self._DesignParameter = _DesignParameter
		else:
			self._DesignParameter = dict(_Name=self._NameDeclaration(_Name=_Name), _GDSFile=self._GDSObjDeclaration(_GDSFile=None))
		self._DesignParameter['_Name']['Name'] = _Name

	def _CalculateDesignParameter(self,Cell_height=1800,Num_of_Vref=25,UNITR_X_WIDTH=1500,UNITR_Y_LENGTH=1000,UNITR_CONT_X_NUM=None,UNITR_CONT_Y_NUM=1,Rladder_X_NUM=10,Rladder_Y_NUM=6,First_Vref_Point=4,VREF_STEP=2,MUX_INV_nmos_width=180,MUX_INV_finger=1,MUX_VDD2PMOS=410,MUX_gate_length=30,MUX_gate_spacing=100,MUX_XVT='\'RVT\'',MUX_nmos_y=375,MUX_cell_height=1800,MUX_TG_pmos_width=600,MUX_TG_nmos_width=300,MUX_TG_poly_y=760,MUX_nandin_y=860):
	
		drc = DRC.DRC()
		_Name = self._DesignParameter['_Name']['_Name']
		
		self._DesignParameter['R_ladder'] = self._SrefElementDeclaration(_DesignObj=RArray.RArray(_Name='R_ladderIn{}'.format(_Name)))[0]
		self._DesignParameter['R_ladder']['_DesignObj']._CalculateDesignParameter(**dict(R_X_width=UNITR_X_WIDTH, R_Y_length=UNITR_Y_LENGTH, CONT_X_num=UNITR_CONT_X_NUM, CONT_Y_num=UNITR_CONT_Y_NUM, NUMofX=Rladder_X_NUM, NUMofY=Rladder_Y_NUM, R_guard_flag=1, Vref_routing_flag=1, First_vref_point=First_Vref_Point, Vref_step=VREF_STEP, Vref_num=Num_of_Vref))
		self._DesignParameter['R_ladder']['_XYCoordinates'] = [[0.0, 0.0]]
		self._DesignParameter['MUX'] = self._SrefElementDeclaration(_DesignObj=Two2TwentyEight_MUX.Two2TwentyEight_MUX(_Name='MUXIn{}'.format(_Name)))[0]
		self._DesignParameter['MUX']['_DesignObj']._CalculateDesignParameter(**dict(INV_nmos_width=MUX_INV_nmos_width, INV_finger=MUX_INV_finger, VDD2PMOS=MUX_VDD2PMOS, gate_length=MUX_gate_length, gate_spacing=MUX_gate_spacing, XVT=MUX_XVT, NMOS_y=MUX_nmos_y, Cell_height=MUX_cell_height, TG_pmos_width=MUX_TG_pmos_width, TG_nmos_width=MUX_TG_nmos_width, TG_poly_y=MUX_TG_poly_y, NANDIN_y=MUX_nandin_y, INPUT_num=Num_of_Vref))
		self._DesignParameter['MUX']['_XYCoordinates'] = [[((((self._DesignParameter['R_ladder']['_XYCoordinates'][0][0] + self._DesignParameter['R_ladder']['_DesignObj']._DesignParameter['GuardRing']['_XYCoordinates'][0][0]) + self._DesignParameter['R_ladder']['_DesignObj']._DesignParameter['GuardRing']['_DesignObj']._DesignParameter['left']['_XYCoordinates'][0][0]) + self._DesignParameter['R_ladder']['_DesignObj']._DesignParameter['GuardRing']['_DesignObj']._DesignParameter['left']['_DesignObj']._DesignParameter['_PPLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['R_ladder']['_DesignObj']._DesignParameter['GuardRing']['_DesignObj']._DesignParameter['left']['_DesignObj']._DesignParameter['_PPLayer']['_XWidth'] / 2)),
														   (((((self._DesignParameter['R_ladder']['_XYCoordinates'][0][1] + self._DesignParameter['R_ladder']['_DesignObj']._DesignParameter['GuardRing']['_XYCoordinates'][0][1]) + self._DesignParameter['R_ladder']['_DesignObj']._DesignParameter['GuardRing']['_DesignObj']._DesignParameter['bot']['_XYCoordinates'][0][1]) + self._DesignParameter['R_ladder']['_DesignObj']._DesignParameter['GuardRing']['_DesignObj']._DesignParameter['bot']['_DesignObj']._DesignParameter['_PPLayer']['_XYCoordinates'][0][1]) - (self._DesignParameter['R_ladder']['_DesignObj']._DesignParameter['GuardRing']['_DesignObj']._DesignParameter['bot']['_DesignObj']._DesignParameter['_PPLayer']['_YWidth'] / 2)) - (Cell_height * 2))]]

		##MUX re-position(x position)
		if Num_of_Vref >= 7:
			for i in range (0,7) :
				tmpname1 = 'mux_module_%d' %i
				MUX_offset_tmp=drc.DRCVIAxMinSpace(2,1) + drc._VIAxMinWidth + drc._MetalxMinSpace2 -(self._DesignParameter['R_ladder']['_XYCoordinates'][0][0] + self._DesignParameter['R_ladder']['_DesignObj']._DesignParameter['_M3_vertical']['_XYCoordinates'][i+1][0][0]) + ((((self._DesignParameter['MUX']['_XYCoordinates'][0][0]) + self._DesignParameter['MUX']['_DesignObj']._DesignParameter['EightMUX_0']['_XYCoordinates'][0][0]) + self._DesignParameter['MUX']['_DesignObj']._DesignParameter['EightMUX_0']['_DesignObj']._DesignParameter[tmpname1]['_XYCoordinates'][0][0]) + self._DesignParameter['MUX']['_DesignObj']._DesignParameter['EightMUX_0']['_DesignObj']._DesignParameter[tmpname1]['_DesignObj']._DesignParameter['m3_boundary']['_XYCoordinates'][0][0])
				if i==0 :
					MUX_offset = MUX_offset_tmp
				elif MUX_offset < MUX_offset_tmp :
					MUX_offset = MUX_offset_tmp
		else :
			for i in range (0,Num_of_Vref) :
				tmpname1 = 'mux_module_%d' %i
				MUX_offset_tmp=drc.DRCVIAxMinSpace(2,1) + drc._VIAxMinWidth + drc._MetalxMinSpace2 -(self._DesignParameter['R_ladder']['_XYCoordinates'][0][0] + self._DesignParameter['R_ladder']['_DesignObj']._DesignParameter['_M3_vertical']['_XYCoordinates'][i+1][0][0]) + ((((self._DesignParameter['MUX']['_XYCoordinates'][0][0]) + self._DesignParameter['MUX']['_DesignObj']._DesignParameter['EightMUX_0']['_XYCoordinates'][0][0]) + self._DesignParameter['MUX']['_DesignObj']._DesignParameter['EightMUX_0']['_DesignObj']._DesignParameter[tmpname1]['_XYCoordinates'][0][0]) + self._DesignParameter['MUX']['_DesignObj']._DesignParameter['EightMUX_0']['_DesignObj']._DesignParameter[tmpname1]['_DesignObj']._DesignParameter['m3_boundary']['_XYCoordinates'][0][0])
				if i==0 :
					MUX_offset = MUX_offset_tmp
				elif MUX_offset < MUX_offset_tmp :
					MUX_offset = MUX_offset_tmp

		self._DesignParameter['MUX']['_XYCoordinates'] = [[((((self._DesignParameter['R_ladder']['_XYCoordinates'][0][0] + self._DesignParameter['R_ladder']['_DesignObj']._DesignParameter['GuardRing']['_XYCoordinates'][0][0]) + self._DesignParameter['R_ladder']['_DesignObj']._DesignParameter['GuardRing']['_DesignObj']._DesignParameter['left']['_XYCoordinates'][0][0]) + self._DesignParameter['R_ladder']['_DesignObj']._DesignParameter['GuardRing']['_DesignObj']._DesignParameter['left']['_DesignObj']._DesignParameter['_PPLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['R_ladder']['_DesignObj']._DesignParameter['GuardRing']['_DesignObj']._DesignParameter['left']['_DesignObj']._DesignParameter['_PPLayer']['_XWidth'] / 2) - MUX_offset),
														   (((((self._DesignParameter['R_ladder']['_XYCoordinates'][0][1] + self._DesignParameter['R_ladder']['_DesignObj']._DesignParameter['GuardRing']['_XYCoordinates'][0][1]) + self._DesignParameter['R_ladder']['_DesignObj']._DesignParameter['GuardRing']['_DesignObj']._DesignParameter['bot']['_XYCoordinates'][0][1]) + self._DesignParameter['R_ladder']['_DesignObj']._DesignParameter['GuardRing']['_DesignObj']._DesignParameter['bot']['_DesignObj']._DesignParameter['_PPLayer']['_XYCoordinates'][0][1]) - (self._DesignParameter['R_ladder']['_DesignObj']._DesignParameter['GuardRing']['_DesignObj']._DesignParameter['bot']['_DesignObj']._DesignParameter['_PPLayer']['_YWidth'] / 2)) - (Cell_height * 2))]]
		del tmpname1
		for i in range (0,Num_of_Vref) :

			name1 = 'Vref_%d_via_1'%i
			name1_1 = 'Vref_%d_via_1in{}'%i
			name2 = 'Vref_%d_via_2'%i
			name2_1 = 'Vref_%d_via_2in{}'%i

			pathname1 = 'Vref_%d_m2_1'%i
			pathname2 = 'Vref_%d_m3_1'%i
			module_num = i%7
			muxname = 'mux_module_%d'%module_num

			Eightmux_num = i // 7
			muxname2 = 'EightMUX_%d'%Eightmux_num

			self._DesignParameter[name1] = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_Name=name1_1.format(_Name)))[0]
			self._DesignParameter[name1]['_DesignObj']._CalculateDesignParameterSameEnclosure(**dict(_ViaMet22Met3NumberOfCOX=1, _ViaMet22Met3NumberOfCOY=1))
			self._DesignParameter[name1]['_XYCoordinates'] = [[(+ (self._DesignParameter['R_ladder']['_XYCoordinates'][0][0] + self._DesignParameter['R_ladder']['_DesignObj']._DesignParameter['_M3_vertical']['_XYCoordinates'][i+1][1][0])), (+ (self._DesignParameter['R_ladder']['_XYCoordinates'][0][1] + self._DesignParameter['R_ladder']['_DesignObj']._DesignParameter['_M3_vertical']['_XYCoordinates'][i+1][1][1]))]]

			self._DesignParameter[pathname1] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _Width=self._DesignParameter[name1]['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth'])
			self._DesignParameter[pathname1]['_XYCoordinates'] = [[[(+ (self._DesignParameter[name1]['_XYCoordinates'][0][0] + self._DesignParameter[name1]['_DesignObj']._DesignParameter['_Met3Layer']['_XYCoordinates'][0][0])),
																	(+ (self._DesignParameter[name1]['_XYCoordinates'][0][1] + self._DesignParameter[name1]['_DesignObj']._DesignParameter['_Met3Layer']['_XYCoordinates'][0][1]))],
																   [((self._DesignParameter['MUX']['_XYCoordinates'][0][0] + self._DesignParameter['MUX']['_DesignObj']._DesignParameter[muxname2]['_DesignObj']._DesignParameter[muxname]['_XYCoordinates'][0][0]) + self._DesignParameter['MUX']['_DesignObj']._DesignParameter[muxname2]['_DesignObj']._DesignParameter[muxname]['_DesignObj']._DesignParameter['Vref_in_m3_2']['_XYCoordinates'][0][0][0]),
																	(self._DesignParameter[name1]['_XYCoordinates'][0][1] + self._DesignParameter[name1]['_DesignObj']._DesignParameter['_Met3Layer']['_XYCoordinates'][0][1])]]]

			self._DesignParameter[name2] = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_Name=name2_1.format(_Name)))[0]
			self._DesignParameter[name2]['_DesignObj']._CalculateDesignParameterSameEnclosure(**dict(_ViaMet22Met3NumberOfCOX=1, _ViaMet22Met3NumberOfCOY=1))
			self._DesignParameter[name2]['_XYCoordinates'] = [[(+ self._DesignParameter[pathname1]['_XYCoordinates'][0][1][0]), (+ self._DesignParameter[pathname1]['_XYCoordinates'][0][1][1])]]

			self._DesignParameter[pathname2] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0], _Datatype=DesignParameters._LayerMapping['METAL3'][1], _Width=self._DesignParameter[name2]['_DesignObj']._DesignParameter['_Met3Layer']['_XWidth'])
			self._DesignParameter[pathname2]['_XYCoordinates'] = [[[(+ (self._DesignParameter[name2]['_XYCoordinates'][0][0] + self._DesignParameter[name2]['_DesignObj']._DesignParameter['_Met3Layer']['_XYCoordinates'][0][0])),
																	(+ (self._DesignParameter[name2]['_XYCoordinates'][0][1] + self._DesignParameter[name2]['_DesignObj']._DesignParameter['_Met3Layer']['_XYCoordinates'][0][1]))],
																   [(+ ((self._DesignParameter['MUX']['_XYCoordinates'][0][0] + self._DesignParameter['MUX']['_DesignObj']._DesignParameter[muxname2]['_DesignObj']._DesignParameter[muxname]['_XYCoordinates'][0][0]) + self._DesignParameter['MUX']['_DesignObj']._DesignParameter[muxname2]['_DesignObj']._DesignParameter[muxname]['_DesignObj']._DesignParameter['Vref_in_m3_2']['_XYCoordinates'][0][0][0])),
																	(+ ((self._DesignParameter['MUX']['_XYCoordinates'][0][1] + self._DesignParameter['MUX']['_DesignObj']._DesignParameter[muxname2]['_DesignObj']._DesignParameter[muxname]['_XYCoordinates'][0][1]) + self._DesignParameter['MUX']['_DesignObj']._DesignParameter[muxname2]['_DesignObj']._DesignParameter[muxname]['_DesignObj']._DesignParameter['Vref_in_m3_2']['_XYCoordinates'][0][0][1])
																	 -2*Cell_height*((Eightmux_num+1)//2)+(2*Cell_height-2*self._DesignParameter['MUX']['_DesignObj']._DesignParameter[muxname2]['_DesignObj']._DesignParameter[muxname]['_DesignObj']._DesignParameter['Vref_in_m3_2']['_XYCoordinates'][0][0][1])*(Eightmux_num%2))]]]

		if Num_of_Vref >= 7:
			if (self._DesignParameter['Vref_6_m2_1']['_XYCoordinates'][0][1][0]-self._DesignParameter['Vref_6_m2_1']['_XYCoordinates'][0][0][0]) >= 0 :
				raise NotImplementedError
		else :
			tmpname = 'Vref_%d_m2_1'%(Num_of_Vref-1)
			if (self._DesignParameter[tmpname]['_XYCoordinates'][0][1][0]-self._DesignParameter[tmpname]['_XYCoordinates'][0][0][0]) >= 0 :
				raise NotImplementedError
			del tmpname