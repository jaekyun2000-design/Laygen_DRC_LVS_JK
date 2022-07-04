from generatorLib import StickDiagram
from generatorLib import DesignParameters
import copy
import math
from generatorLib import DRC
from generatorLib.generator_models import NSET_Current_mirror
from generatorLib.generator_models import PSET_Current_Mirror

class EasyDebugModule(StickDiagram._StickDiagram):
	def __init__(self, _DesignParameter=None, _Name='EasyDebugModule'):
		if _DesignParameter != None:
			self._DesignParameter = _DesignParameter
		else:
			self._DesignParameter = dict(_Name=self._NameDeclaration(_Name=_Name), _GDSFile=self._GDSObjDeclaration(_GDSFile=None))
		self._DesignParameter['_Name']['Name'] = _Name

	def _CalculateDesignParameter_v1(self,nset_param={'nmos_stack_coarse_param': {'nmos1_width': 2000, 'nmos1_length': 500, 'nmos1_gate': 1, 'nmos1_dummy': False, 'nmos1_xvt': 'RVT', 'nmos1_pccrit': False, 'nmos2_width': 2000, 'nmos2_length': 30, 'nmos2_gate': 1, 'nmos2_dummy': False, 'nmos2_xvt': 'RVT', 'nmos2_pccrit': False, 'guardring_bot': 2, 'guardring_top': 2, 'guardring_left': 2, 'guardring_right': 2, 'guardring_width': None, 'guardring_height': None, 'diode_connect': True}, \
												   'nmos_stack_fine_param': {'nmos1_width': 500, 'nmos1_length': 500, 'nmos1_gate': 1, 'nmos1_dummy': False, 'nmos1_xvt': 'RVT', 'nmos1_pccrit': False, 'nmos2_width': 2000, 'nmos2_length': 30, 'nmos2_gate': 1, 'nmos2_dummy': False, 'nmos2_xvt': 'RVT', 'nmos2_pccrit': False, 'guardring_bot': 2, 'guardring_top': 2, 'guardring_left': 2, 'guardring_right': 2, 'guardring_width': None, 'guardring_height': None, 'diode_connect': True}, \
												   'nmos_stack_mirror_param': {'nmos1_width': 2000, 'nmos1_length': 500, 'nmos1_gate': 1, 'nmos1_dummy': False, 'nmos1_xvt': 'RVT', 'nmos1_pccrit': False, 'nmos2_width': 2000, 'nmos2_length': 30, 'nmos2_gate': 1, 'nmos2_dummy': False, 'nmos2_xvt': 'RVT', 'nmos2_pccrit': False, 'guardring_bot': 2, 'guardring_top': 2, 'guardring_left': 2, 'guardring_right': 2, 'guardring_width': None, 'guardring_height': None, 'diode_connect': False}, \
												   'guardring_width': None, 'guardring_height': None, 'coarse_num': 5, 'fine_num': 5, 'mirror_num': 1, 'Xnum': 5, 'Ynum': 5}):

		drc = DRC.DRC()
		_Name = self._DesignParameter['_Name']['_Name']
		_OriginXY=[[0,0]]

		self._DesignParameter['nset'] = self._SrefElementDeclaration(_DesignObj=NSET_Current_mirror.EasyDebugModule(_Name='nsetIn{}'.format(_Name)))[0]
		self._DesignParameter['nset']['_DesignObj']._CalculateDesignParameter_v1(**dict(**nset_param))

		self._DesignParameter['nset']['_XYCoordinates'] = _OriginXY

	def _CalculateDesignParameter_v2(self,pset_param={'pmos1_param': {'finger': 2, 'width': 1500, 'length': 100, 'dummy': True, 'xvt': 'LVT', 'pccrit': False, 'guardring_co_right': 3, 'guardring_co_left': 3, 'guardring_co_top': 4, 'guardring_co_bottom': 2}, 'pmos2_param': {'finger': 2, 'width': 1500, 'length': 100, 'dummy': True, 'xvt': 'LVT', 'pccrit': False, 'guardring_co_right': 3, 'guardring_co_left': 3, 'guardring_co_top': 4, 'guardring_co_bottom': 2}, \
												   'pmos3_param': {'finger': 2, 'width': 1500, 'length': 100, 'dummy': True, 'xvt': 'LVT', 'pccrit': 'False ', 'guardring_co_right': 3, 'guardring_co_left': 3, 'guardring_co_top': 4, 'guardring_co_bottom': 2}, 'pmos_cap_param': {'pmos_cap_gate':16,'pmos_cap_width':1500,'pmos_cap_length':100,'pmos_cap_dummy':False,'pmos_cap_xvt':'LVT','pmos_cap_pccrit':False,'pmos_sw1_gate':1,'pmos_sw1_width':1000,'pmos_sw1_length':30,'pmos_sw1_dummy':True,'pmos_sw1_xvt':'LVT','pmos_sw1_pccrit':True,'pmos_sw2_gate':1,'pmos_sw2_width':1000,'pmos_sw2_length':30,'pmos_sw2_dummy':True,'pmos_sw2_xvt':'LVT','pmos_sw2_pccrit':True,'guardring_co_bottom':4,'guardring_co_top':3,'guardring_co_left':3,'guardring_co_right':3,'guardring_width':None,'guardring_height':None}},\
								  	   nset_param={'nmos_stack_coarse_param': {'nmos1_width': 2000, 'nmos1_length': 500, 'nmos1_gate': 1, 'nmos1_dummy': False, 'nmos1_xvt': 'RVT', 'nmos1_pccrit': False, 'nmos2_width': 2000, 'nmos2_length': 30, 'nmos2_gate': 1, 'nmos2_dummy': False, 'nmos2_xvt': 'RVT', 'nmos2_pccrit': False, 'guardring_bot': 2, 'guardring_top': 2, 'guardring_left': 2, 'guardring_right': 2, 'guardring_width': None, 'guardring_height': None, 'diode_connect': True}, \
												   'nmos_stack_fine_param': {'nmos1_width': 500, 'nmos1_length': 500, 'nmos1_gate': 1, 'nmos1_dummy': False, 'nmos1_xvt': 'RVT', 'nmos1_pccrit': False, 'nmos2_width': 2000, 'nmos2_length': 30, 'nmos2_gate': 1, 'nmos2_dummy': False, 'nmos2_xvt': 'RVT', 'nmos2_pccrit': False, 'guardring_bot': 2, 'guardring_top': 2, 'guardring_left': 2, 'guardring_right': 2, 'guardring_width': None, 'guardring_height': None, 'diode_connect': True}, \
												   'nmos_stack_mirror_param': {'nmos1_width': 2000, 'nmos1_length': 500, 'nmos1_gate': 1, 'nmos1_dummy': False, 'nmos1_xvt': 'RVT', 'nmos1_pccrit': False, 'nmos2_width': 2000, 'nmos2_length': 30, 'nmos2_gate': 1, 'nmos2_dummy': False, 'nmos2_xvt': 'RVT', 'nmos2_pccrit': False, 'guardring_bot': 2, 'guardring_top': 2, 'guardring_left': 2, 'guardring_right': 2, 'guardring_width': None, 'guardring_height': None, 'diode_connect': False}, \
												   'nmos_single_sw_param':{'nmos_gate':2,'nmos_width':1000,'nmos_length':30,'nmos_dummy':True,'xvt':'SLVT','pccrit':True,'guardring_right':2,'guardring_left':2,'guardring_bot':2,'guardring_top':2,'guardring_width':None,'guardring_height':None},\
                                  				   'nmos_single_tail_param':{'nmos1_gate':1,'nmos1_width':2000,'nmos1_length':500,'nmos1_dummy':False,'nmos1_xvt':'RVT','nmos1_pccrit':False,'guardring_left':2,'guardring_right':2,'guardring_top':2,'guardring_bot':2,'guardring_width':None,'guardring_height':None},\
												   'guardring_width': None, 'guardring_height': None, 'coarse_num': 3, 'fine_num': 4, 'mirror_num': 1, 'Xnum': 3, 'Ynum': 4}):

		drc = DRC.DRC()
		_Name = self._DesignParameter['_Name']['_Name']
		
		self._DesignParameter['pset'] = self._SrefElementDeclaration(_DesignObj=PSET_Current_Mirror.EasyDebugModule(_Name='psetIn{}'.format(_Name)))[0]
		self._DesignParameter['pset']['_DesignObj']._CalculateDesignParameter(**dict(**pset_param))
		self._DesignParameter['pset']['_XYCoordinates'] = [[0, 0]]
		self._DesignParameter['nset'] = self._SrefElementDeclaration(_DesignObj=NSET_Current_mirror.EasyDebugModule(_Name='nsetIn{}'.format(_Name)))[0]
		self._DesignParameter['nset']['_DesignObj']._CalculateDesignParameter_v2(**dict(**nset_param))

		_Ycoordinate_nset=self._DesignParameter['pset']['_XYCoordinates'][0][1]+self._DesignParameter['pset']['_DesignObj']._DesignParameter['pmos2']['_XYCoordinates'][0][1]+self._DesignParameter['pset']['_DesignObj']._DesignParameter['pmos2']['_DesignObj']._DesignParameter['pguardring']['_XYCoordinates'][0][1]+self._DesignParameter['pset']['_DesignObj']._DesignParameter['pmos2']['_DesignObj']._DesignParameter['pguardring']['_DesignObj']._DesignParameter['bot']['_XYCoordinates'][0][1]-self._DesignParameter['pset']['_DesignObj']._DesignParameter['pmos2']['_DesignObj']._DesignParameter['pguardring']['_DesignObj']._DesignParameter['bot']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']/2-\
						  (self._DesignParameter['nset']['_DesignObj']._DesignParameter['nmos_sw']['_XYCoordinates'][0][1]+self._DesignParameter['nset']['_DesignObj']._DesignParameter['nmos_sw']['_DesignObj']._DesignParameter['guardring']['_XYCoordinates'][0][1]+self._DesignParameter['nset']['_DesignObj']._DesignParameter['nmos_sw']['_DesignObj']._DesignParameter['guardring']['_DesignObj']._DesignParameter['top']['_XYCoordinates'][0][1]+self._DesignParameter['nset']['_DesignObj']._DesignParameter['nmos_sw']['_DesignObj']._DesignParameter['guardring']['_DesignObj']._DesignParameter['top']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']/2)-drc._Metal1MinSpace3

		self._DesignParameter['nset']['_XYCoordinates'] = [[self._DesignParameter['pset']['_XYCoordinates'][0][0], _Ycoordinate_nset]]

