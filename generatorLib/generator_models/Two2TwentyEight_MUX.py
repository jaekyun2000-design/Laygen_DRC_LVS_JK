from generatorLib import StickDiagram
from generatorLib import DesignParameters
import copy
import math
from generatorLib import DRC
from generatorLib.generator_models import Two2eight_inputs_mux_ver2

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

		for i in range(0,Num_of_8mux) :
			name = 'EightMUX_%d'%i
			name2 = 'EightMUX_%d{}'%i
			self._DesignParameter[name] = self._SrefElementDeclaration(_DesignObj=Two2eight_inputs_mux_ver2._2to8inputs_mux(_Name=name2.format(_Name)))[0]
			self._DesignParameter[name]['_DesignObj']._CalculateDesignParameter(**dict(_INV_nmos_width=INV_nmos_width, _INV_finger=INV_finger, _VDD2PMOS=VDD2PMOS, _gate_length=gate_length, _gate_spacing=gate_spacing, _XVT=XVT, _NMOS_y=NMOS_y, _Cell_height=Cell_height,
																					   _TG_pmos_width=TG_pmos_width, _TG_nmos_width=TG_nmos_width, _TG_poly_y=TG_poly_y, _NANDIN_y=NANDIN_y, _Num_of_MUX_modules=7, _Input_offset=i))
			if i%2==1 :
				self._DesignParameter[name]['_Reflect'] = [1, 0, 0]
			self._DesignParameter[name]['_XYCoordinates'] = [[0.0, -2*Cell_height*(i//2)]]



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