from generatorLib import StickDiagram
from generatorLib import DesignParameters
import copy
import math
from generatorLib import DRC
from generatorLib.generator_models import Two2eight_inputs_mux_ver2
from generatorLib.generator_models import ViaMet32Met4

class Two2TwentyEight_MUX(StickDiagram._StickDiagram):
	def __init__(self, _DesignParameter=None, _Name='Two2TwentyEight_MUX'):
		if _DesignParameter != None:
			self._DesignParameter = _DesignParameter
		else:
			self._DesignParameter = dict(_Name=self._NameDeclaration(_Name=_Name), _GDSFile=self._GDSObjDeclaration(_GDSFile=None))
		self._DesignParameter['_Name']['Name'] = _Name

	def _CalculateDesignParameter(self,INPUT_num=28,Cell_height=1800,INV_nmos_width= 180, INV_finger= 1, VDD2PMOS= 410, gate_length= 30, gate_spacing= 100, XVT= '\'RVT\'', NMOS_y= 375, TG_pmos_width= 600, TG_nmos_width= 300, TG_poly_y= 760, NANDIN_y= 860):
	
		drc = DRC.DRC()
		_Name = self._DesignParameter['_Name']['_Name']

		Num_of_8mux = (INPUT_num-1)//7 + 1

		if Num_of_8mux == 1 :
			name = 'EightMUX_0'
			name2 = 'EightMUX_0{}'
			self._DesignParameter[name] = self._SrefElementDeclaration(_DesignObj=Two2eight_inputs_mux_ver2._2to8inputs_mux(_Name=name2.format(_Name)))[0]
			self._DesignParameter[name]['_DesignObj']._CalculateDesignParameter(**dict(_INV_nmos_width=INV_nmos_width, _INV_finger=INV_finger, _VDD2PMOS=VDD2PMOS, _gate_length=gate_length, _gate_spacing=gate_spacing, _XVT=XVT, _NMOS_y=NMOS_y, _Cell_height=Cell_height,
																					   _TG_pmos_width=TG_pmos_width, _TG_nmos_width=TG_nmos_width, _TG_poly_y=TG_poly_y, _NANDIN_y=NANDIN_y, _Num_of_MUX_modules=INPUT_num, _Input_offset=0))
			self._DesignParameter[name]['_XYCoordinates'] = [[0.0, 0.0]]
			nameA = 'Ain_0'
			nameB = 'Bin_0'
			nameC = 'Cin_0'
			self._DesignParameter[nameA] = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2PIN'][0], _Datatype=DesignParameters._LayerMapping['METAL2PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0], _XYCoordinates=[[0, 0]], _Mag=0.1, _Angle=0, _TEXT=nameA)
			self._DesignParameter[nameB] = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2PIN'][0], _Datatype=DesignParameters._LayerMapping['METAL2PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0], _XYCoordinates=[[0, 0]], _Mag=0.1, _Angle=0, _TEXT=nameB)
			self._DesignParameter[nameC] = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2PIN'][0], _Datatype=DesignParameters._LayerMapping['METAL2PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0], _XYCoordinates=[[0, 0]], _Mag=0.1, _Angle=0, _TEXT=nameC)
			self._DesignParameter[nameA]['_XYCoordinates'] = [[(+ ((self._DesignParameter[name]['_XYCoordinates'][0][0]) + self._DesignParameter[name]['_DesignObj']._DesignParameter['inv_b_via1_2']['_XYCoordinates'][0][0])), (+ ((self._DesignParameter[name]['_XYCoordinates'][0][1]) + self._DesignParameter[name]['_DesignObj']._DesignParameter['inv_b_via1_2']['_XYCoordinates'][0][1]))]]
			self._DesignParameter[nameB]['_XYCoordinates'] = [[(+ ((self._DesignParameter[name]['_XYCoordinates'][0][0]) + self._DesignParameter[name]['_DesignObj']._DesignParameter['inv_a_via1_2']['_XYCoordinates'][0][0])), (+ ((self._DesignParameter[name]['_XYCoordinates'][0][1]) + self._DesignParameter[name]['_DesignObj']._DesignParameter['inv_a_via1_2']['_XYCoordinates'][0][1]))]]
			self._DesignParameter[nameC]['_XYCoordinates'] = [[(+ ((self._DesignParameter[name]['_XYCoordinates'][0][0]) + self._DesignParameter[name]['_DesignObj']._DesignParameter['inv_c_via1_2']['_XYCoordinates'][0][0])), (+ ((self._DesignParameter[name]['_XYCoordinates'][0][1]) + self._DesignParameter[name]['_DesignObj']._DesignParameter['inv_c_via1_2']['_XYCoordinates'][0][1]))]]


		else :
			for i in range(0,Num_of_8mux) :
				name = 'EightMUX_%d'%i
				name2 = 'EightMUX_%d{}'%i
				self._DesignParameter[name] = self._SrefElementDeclaration(_DesignObj=Two2eight_inputs_mux_ver2._2to8inputs_mux(_Name=name2.format(_Name)))[0]
				self._DesignParameter[name]['_DesignObj']._CalculateDesignParameter(**dict(_INV_nmos_width=INV_nmos_width, _INV_finger=INV_finger, _VDD2PMOS=VDD2PMOS, _gate_length=gate_length, _gate_spacing=gate_spacing, _XVT=XVT, _NMOS_y=NMOS_y, _Cell_height=Cell_height,
																						   _TG_pmos_width=TG_pmos_width, _TG_nmos_width=TG_nmos_width, _TG_poly_y=TG_poly_y, _NANDIN_y=NANDIN_y, _Num_of_MUX_modules=7, _Input_offset=i))
				if i%2==1 :
					self._DesignParameter[name]['_Reflect'] = [1, 0, 0]
				self._DesignParameter[name]['_XYCoordinates'] = [[0.0, -2*Cell_height*(i//2)]]

				nameA='Ain_%d'%i
				nameB='Bin_%d'%i
				nameC='Cin_%d'%i

				if i%2==0:
					self._DesignParameter[nameA] = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2PIN'][0], _Datatype=DesignParameters._LayerMapping['METAL2PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0], _XYCoordinates=[[0, 0]], _Mag=0.1, _Angle=0, _TEXT=nameA)
					self._DesignParameter[nameB] = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2PIN'][0], _Datatype=DesignParameters._LayerMapping['METAL2PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0], _XYCoordinates=[[0, 0]], _Mag=0.1, _Angle=0, _TEXT=nameB)
					self._DesignParameter[nameC] = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2PIN'][0], _Datatype=DesignParameters._LayerMapping['METAL2PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0], _XYCoordinates=[[0, 0]], _Mag=0.1, _Angle=0, _TEXT=nameC)
					self._DesignParameter[nameA]['_XYCoordinates'] = [[(+ ((self._DesignParameter[name]['_XYCoordinates'][0][0]) + self._DesignParameter[name]['_DesignObj']._DesignParameter['inv_b_via1_2']['_XYCoordinates'][0][0])), (+ ((self._DesignParameter[name]['_XYCoordinates'][0][1]) + self._DesignParameter[name]['_DesignObj']._DesignParameter['inv_b_via1_2']['_XYCoordinates'][0][1]))]]
					self._DesignParameter[nameB]['_XYCoordinates'] = [[(+ ((self._DesignParameter[name]['_XYCoordinates'][0][0]) + self._DesignParameter[name]['_DesignObj']._DesignParameter['inv_a_via1_2']['_XYCoordinates'][0][0])), (+ ((self._DesignParameter[name]['_XYCoordinates'][0][1]) + self._DesignParameter[name]['_DesignObj']._DesignParameter['inv_a_via1_2']['_XYCoordinates'][0][1]))]]
					self._DesignParameter[nameC]['_XYCoordinates'] = [[(+ ((self._DesignParameter[name]['_XYCoordinates'][0][0]) + self._DesignParameter[name]['_DesignObj']._DesignParameter['inv_c_via1_2']['_XYCoordinates'][0][0])), (+ ((self._DesignParameter[name]['_XYCoordinates'][0][1]) + self._DesignParameter[name]['_DesignObj']._DesignParameter['inv_c_via1_2']['_XYCoordinates'][0][1]))]]
				else :
					self._DesignParameter[nameA] = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2PIN'][0], _Datatype=DesignParameters._LayerMapping['METAL2PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0], _XYCoordinates=[[0, 0]], _Mag=0.1, _Angle=0, _TEXT=nameA)
					self._DesignParameter[nameB] = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2PIN'][0], _Datatype=DesignParameters._LayerMapping['METAL2PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0], _XYCoordinates=[[0, 0]], _Mag=0.1, _Angle=0, _TEXT=nameB)
					self._DesignParameter[nameC] = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2PIN'][0], _Datatype=DesignParameters._LayerMapping['METAL2PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0], _XYCoordinates=[[0, 0]], _Mag=0.1, _Angle=0, _TEXT=nameC)
					self._DesignParameter[nameA]['_XYCoordinates'] = [[(+ ((self._DesignParameter[name]['_XYCoordinates'][0][0]) + self._DesignParameter[name]['_DesignObj']._DesignParameter['inv_b_via1_2']['_XYCoordinates'][0][0])), (+ ((self._DesignParameter[name]['_XYCoordinates'][0][1]) - self._DesignParameter[name]['_DesignObj']._DesignParameter['inv_b_via1_2']['_XYCoordinates'][0][1]))]]
					self._DesignParameter[nameB]['_XYCoordinates'] = [[(+ ((self._DesignParameter[name]['_XYCoordinates'][0][0]) + self._DesignParameter[name]['_DesignObj']._DesignParameter['inv_a_via1_2']['_XYCoordinates'][0][0])), (+ ((self._DesignParameter[name]['_XYCoordinates'][0][1]) - self._DesignParameter[name]['_DesignObj']._DesignParameter['inv_a_via1_2']['_XYCoordinates'][0][1]))]]
					self._DesignParameter[nameC]['_XYCoordinates'] = [[(+ ((self._DesignParameter[name]['_XYCoordinates'][0][0]) + self._DesignParameter[name]['_DesignObj']._DesignParameter['inv_c_via1_2']['_XYCoordinates'][0][0])), (+ ((self._DesignParameter[name]['_XYCoordinates'][0][1]) - self._DesignParameter[name]['_DesignObj']._DesignParameter['inv_c_via1_2']['_XYCoordinates'][0][1]))]]

		# self._DesignParameter['EightMUX_1'] = self._SrefElementDeclaration(_DesignObj=Two2eight_inputs_mux_ver2._2to8inputs_mux(_Name='EightMUX_1In{}'.format(_Name)))[0]
		# self._DesignParameter['EightMUX_1']['_DesignObj']._CalculateDesignParameter(**dict(param_muxmodule,_Input_offset=1))
		# self._DesignParameter['EightMUX_1']['_XYCoordinates'] = [[0.0, 0.0]]
		# self._DesignParameter['EightMUX_1']['_Reflect'] = [1, 0, 0]
		# self._DesignParameter['EightMUX_2'] = self._SrefElementDeclaration(_DesignObj=Two2eight_inputs_mux_ver2._2to8inputs_mux(_Name='EightMUX_2In{}'.format(_Name)))[0]
		# self._DesignParameter['EightMUX_2']['_DesignObj']._CalculateDesignParameter(**dict(param_muxmodule,_Input_offset=2))
		# self._DesignParameter['EightMUX_2']['_XYCoordinates'] = [[0.0, (- 3600.0)]]
		# self._DesignParameter['EightMUX_3'] = self._SrefElementDeclaration(_DesignObj=Two2eight_inputs_mux_ver2._2to8inputs_mux(_Name='EightMUX_3In{}'.format(_Name)))[0]
		# self._DesignParameter['EightMUX_3']['_DesignObj']._CalculateDesignParameter(**dict(param_muxmodule,_Input_offset=3))
		# self._DesignParameter['EightMUX_3']['_XYCoordinates'] = [[0.0, (- 3600.0)]]
		# self._DesignParameter['EightMUX_3']['_Reflect'] = [1, 0, 0]
		#
		if Num_of_8mux > 1:
			self._DesignParameter['OUTCONNECT'] = self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_Name='OUTCONNECTIn{}'.format(_Name)))[0]
			self._DesignParameter['OUTCONNECT']['_DesignObj']._CalculateDesignParameterSameEnclosure(**dict(_ViaMet32Met4NumberOfCOX=1, _ViaMet32Met4NumberOfCOY=2))
			tmp = []
			for i in range(0,Num_of_8mux) :
				name11 = 'EightMUX_%d'%i
				for j in range (1,7) :
					name12 = 'mux_module_%d'%j
					tmp.append([((self._DesignParameter[name11]['_XYCoordinates'][0][0] + self._DesignParameter[name11]['_DesignObj']._DesignParameter[name12]['_XYCoordinates'][0][0]) + self._DesignParameter[name11]['_DesignObj']._DesignParameter[name12]['_DesignObj']._DesignParameter['INb_m1_4']['_XYCoordinates'][0][0][0])
								+ drc._VIAxMinWidth + 2 * max([drc._Metal1MinEnclosureVia3,drc._MetalxMinEnclosureVia3]) + drc._MetalxMinSpace2
								   , (self._DesignParameter['EightMUX_0']['_XYCoordinates'][0][1] + self._DesignParameter['EightMUX_0']['_DesignObj']._DesignParameter['OUT_line']['_XYCoordinates'][0][0][1]
								-2*Cell_height*((1+i)//2)+(2*Cell_height-2*self._DesignParameter['EightMUX_0']['_DesignObj']._DesignParameter['OUT_line']['_XYCoordinates'][0][0][1])*(i%2))])

			self._DesignParameter['OUTCONNECT']['_XYCoordinates'] = tmp
			del tmp

			tmp2 = [[]]
			self._DesignParameter['OUTconnect_m3'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0], _Datatype=DesignParameters._LayerMapping['METAL3'][1], _Width=self._DesignParameter['OUTCONNECT']['_DesignObj']._DesignParameter['_Met3Layer']['_XWidth'])
			for j in range (0,6) :
				tmp2.append([self._DesignParameter['OUTCONNECT']['_XYCoordinates'][j], self._DesignParameter['OUTCONNECT']['_XYCoordinates'][-6+j]])

			self._DesignParameter['OUTconnect_m3']['_XYCoordinates'] = tmp2
			del tmp2
	#self._DesignParameter['OUTconnect']['_XYCoordinates'] = [[][]]
