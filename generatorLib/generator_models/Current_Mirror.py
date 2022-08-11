from generatorLib import StickDiagram
from generatorLib import DesignParameters
import copy
import math
from generatorLib import DRC
from generatorLib.generator_models import NSET_Current_mirror
from generatorLib.generator_models import PSET_Current_Mirror
from generatorLib.generator_models import ViaMet42Met5

class _Current_Mirror(StickDiagram._StickDiagram):
	def __init__(self, _DesignParameter=None, _Name='Current_Mirror'):
		if _DesignParameter != None:
			self._DesignParameter = _DesignParameter
		else:
			self._DesignParameter = dict(_Name=self._NameDeclaration(_Name=_Name), _GDSFile=self._GDSObjDeclaration(_GDSFile=None))
		self._DesignParameter['_Name']['Name'] = _Name

	def _CalculateDesignParameter_v1(self,nset_param={'nmos_stack_coarse_param': {'nmos1_width': 2000, 'nmos1_length': 500, 'nmos1_dummy': False, 'nmos1_xvt': 'RVT', 'nmos1_pccrit': False, 'nmos2_width': 2000, 'nmos2_length': 30, 'nmos2_dummy': False, 'nmos2_xvt': 'RVT', 'nmos2_pccrit': False, 'guardring_bot': 2, 'guardring_top': 2, 'guardring_left': 2, 'guardring_right': 2, 'guardring_width': None, 'guardring_height': None}, \
													  'nmos_stack_fine_param': {'nmos1_width': 500, 'nmos1_length': 500,  'nmos1_dummy': False, 'nmos1_xvt': 'RVT', 'nmos1_pccrit': False, 'nmos2_width': 2000, 'nmos2_length': 30, 'nmos2_dummy': False, 'nmos2_xvt': 'RVT', 'nmos2_pccrit': False, 'guardring_bot': 2, 'guardring_top': 2, 'guardring_left': 2, 'guardring_right': 2, 'guardring_width': None, 'guardring_height': None}, \
												      'nmos_stack_mirror_param': {'nmos1_width': 2000, 'nmos1_length': 500, 'nmos1_dummy': False, 'nmos1_xvt': 'RVT', 'nmos1_pccrit': False, 'nmos2_width': 2000, 'nmos2_length': 30, 'nmos2_dummy': False, 'nmos2_xvt': 'RVT', 'nmos2_pccrit': False, 'guardring_bot': 2, 'guardring_top': 2, 'guardring_left': 2, 'guardring_right': 2, 'guardring_width': None, 'guardring_height': None}, \
												      'guardring_width':None, 'guardring_height':None,'coarse_num': 5, 'fine_num': 5, 'mirror_num': 1, 'Xnum': 5, 'Ynum': 3}):

		drc = DRC.DRC()
		_Name = self._DesignParameter['_Name']['_Name']
		_OriginXY=[[0,0]]

		self._DesignParameter['nset'] = self._SrefElementDeclaration(_DesignObj=NSET_Current_mirror._NSET_Current_Mirror(_Name='nsetIn{}'.format(_Name)))[0]
		self._DesignParameter['nset']['_DesignObj']._CalculateDesignParameter_v1(**dict(**nset_param))

		self._DesignParameter['nset']['_XYCoordinates'] = _OriginXY

		self._DesignParameter['vss'] = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1PIN'][0], _Datatype=DesignParameters._LayerMapping['METAL1PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0], _XYCoordinates=[], _Mag=0.2, _Angle=0, _TEXT='vss')
		self._DesignParameter['Iin'] = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL4PIN'][0], _Datatype=DesignParameters._LayerMapping['METAL4PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0], _XYCoordinates=[], _Mag=0.1, _Angle=0, _TEXT='Iin')
		self._DesignParameter['Iout'] = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1PIN'][0], _Datatype=DesignParameters._LayerMapping['METAL1PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0], _XYCoordinates=[], _Mag=0.1, _Angle=0, _TEXT='Iout')
		self._DesignParameter['SI_coarse'] = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL4PIN'][0], _Datatype=DesignParameters._LayerMapping['METAL4PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0], _XYCoordinates=[], _Mag=0.1, _Angle=0, _TEXT='SI_coarse')
		self._DesignParameter['SI_fine'] = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL4PIN'][0], _Datatype=DesignParameters._LayerMapping['METAL4PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0], _XYCoordinates=[], _Mag=0.1, _Angle=0, _TEXT='SI_fine')
		self._DesignParameter['SI_mirror'] = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL4PIN'][0], _Datatype=DesignParameters._LayerMapping['METAL4PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0], _XYCoordinates=[], _Mag=0.1, _Angle=0, _TEXT='SI_mirror')

		self._DesignParameter['vss']['_XYCoordinates']=self.getXY('nset','nmos_coarse','guardring','top')
		self._DesignParameter['Iin']['_XYCoordinates']=self.getXY('nset','Via_m3_m4')
		tmp=[]
		for i in range(0,len(self._DesignParameter['nset']['_DesignObj']._DesignParameter['nmos_mirror']['_XYCoordinates'])):
			tmp.append([self._DesignParameter['nset']['_XYCoordinates'][0][0]+self._DesignParameter['nset']['_DesignObj']._DesignParameter['nmos_mirror']['_XYCoordinates'][i][0]+self._DesignParameter['nset']['_DesignObj']._DesignParameter['nmos_mirror']['_DesignObj']._DesignParameter['nmos2']['_XYCoordinates'][0][0]+self._DesignParameter['nset']['_DesignObj']._DesignParameter['nmos_mirror']['_DesignObj']._DesignParameter['nmos2']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][-1][0],\
						self._DesignParameter['nset']['_XYCoordinates'][0][1]+self._DesignParameter['nset']['_DesignObj']._DesignParameter['nmos_mirror']['_XYCoordinates'][i][1]+self._DesignParameter['nset']['_DesignObj']._DesignParameter['nmos_mirror']['_DesignObj']._DesignParameter['nmos2']['_XYCoordinates'][0][1]+self._DesignParameter['nset']['_DesignObj']._DesignParameter['nmos_mirror']['_DesignObj']._DesignParameter['nmos2']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][-1][1]])
		self._DesignParameter['Iout']['_XYCoordinates']=tmp
		tmp=[]
		for i in range(0,len(self._DesignParameter['nset']['_DesignObj']._DesignParameter['nmos_coarse']['_XYCoordinates'])):
			tmp.append([self._DesignParameter['nset']['_XYCoordinates'][0][0]+self._DesignParameter['nset']['_DesignObj']._DesignParameter['nmos_coarse']['_XYCoordinates'][i][0]+self._DesignParameter['nset']['_DesignObj']._DesignParameter['nmos_coarse']['_DesignObj']._DesignParameter['via_m1_m2_nmos2']['_XYCoordinates'][0][0],\
						self._DesignParameter['nset']['_XYCoordinates'][0][1]+self._DesignParameter['nset']['_DesignObj']._DesignParameter['nmos_coarse']['_XYCoordinates'][i][1]+self._DesignParameter['nset']['_DesignObj']._DesignParameter['nmos_coarse']['_DesignObj']._DesignParameter['via_m1_m2_nmos2']['_XYCoordinates'][0][1]])
		self._DesignParameter['SI_coarse']['_XYCoordinates']=tmp
		tmp=[]
		for i in range(0,len(self._DesignParameter['nset']['_DesignObj']._DesignParameter['nmos_fine']['_XYCoordinates'])):
			tmp.append([self._DesignParameter['nset']['_XYCoordinates'][0][0]+self._DesignParameter['nset']['_DesignObj']._DesignParameter['nmos_fine']['_XYCoordinates'][i][0]+self._DesignParameter['nset']['_DesignObj']._DesignParameter['nmos_fine']['_DesignObj']._DesignParameter['via_m1_m2_nmos2']['_XYCoordinates'][0][0],\
						self._DesignParameter['nset']['_XYCoordinates'][0][1]+self._DesignParameter['nset']['_DesignObj']._DesignParameter['nmos_fine']['_XYCoordinates'][i][1]+self._DesignParameter['nset']['_DesignObj']._DesignParameter['nmos_fine']['_DesignObj']._DesignParameter['via_m1_m2_nmos2']['_XYCoordinates'][0][1]])
		self._DesignParameter['SI_fine']['_XYCoordinates']=tmp
		tmp=[]
		for i in range(0,len(self._DesignParameter['nset']['_DesignObj']._DesignParameter['nmos_mirror']['_XYCoordinates'])):
			tmp.append([self._DesignParameter['nset']['_XYCoordinates'][0][0]+self._DesignParameter['nset']['_DesignObj']._DesignParameter['nmos_mirror']['_XYCoordinates'][i][0]+self._DesignParameter['nset']['_DesignObj']._DesignParameter['nmos_mirror']['_DesignObj']._DesignParameter['via_m1_m2_nmos2']['_XYCoordinates'][0][0],\
						self._DesignParameter['nset']['_XYCoordinates'][0][1]+self._DesignParameter['nset']['_DesignObj']._DesignParameter['nmos_mirror']['_XYCoordinates'][i][1]+self._DesignParameter['nset']['_DesignObj']._DesignParameter['nmos_mirror']['_DesignObj']._DesignParameter['via_m1_m2_nmos2']['_XYCoordinates'][0][1]])
		self._DesignParameter['SI_mirror']['_XYCoordinates']=tmp
		del tmp

	# def _CalculateDesignParameter_v2(self,pset_param={'pmos1_param': {'finger': 2, 'width': 1500, 'length': 100, 'dummy': True, 'xvt': 'LVT', 'pccrit': False, 'guardring_co_right': 3, 'guardring_co_left': 3, 'guardring_co_top': 4, 'guardring_co_bottom': 2,'guardring_width':None,'guardring_height':None}, 'pmos2_param': {'finger': 2, 'width': 1500, 'length': 100, 'dummy': True, 'xvt': 'LVT', 'pccrit': False, 'guardring_co_right': 3, 'guardring_co_left': 3, 'guardring_co_top': 4, 'guardring_co_bottom': 2,'guardring_width':None,'guardring_height':None}, \
	# 											   'pmos3_param': {'finger': 2, 'width': 1500, 'length': 100, 'dummy': True, 'xvt': 'LVT', 'pccrit': False, 'guardring_co_right': 3, 'guardring_co_left': 3, 'guardring_co_top': 4, 'guardring_co_bottom': 2,'guardring_width':None,'guardring_height':None}, 'pmos_cap_param': {'pmos_cap_gate':16,'pmos_cap_width':1500,'pmos_cap_length':100,'pmos_cap_dummy':False,'pmos_cap_xvt':'LVT','pmos_cap_pccrit':False,'pmos_sw1_gate':1,'pmos_sw1_width':1000,'pmos_sw1_length':30,'pmos_sw1_dummy':True,'pmos_sw1_xvt':'LVT','pmos_sw1_pccrit':True,'pmos_sw2_gate':1,'pmos_sw2_width':1000,'pmos_sw2_length':30,'pmos_sw2_dummy':True,'pmos_sw2_xvt':'LVT','pmos_sw2_pccrit':True,'guardring_co_bottom':4,'guardring_co_top':3,'guardring_co_left':3,'guardring_co_right':3,'guardring_width':None,'guardring_height':None,'guardring_width':None,'guardring_height':None}},\
	# 							  	   nset_param={'nmos_stack_coarse_param': {'nmos1_width': 2000, 'nmos1_length': 500, 'nmos1_gate': 1, 'nmos1_dummy': False, 'nmos1_xvt': 'RVT', 'nmos1_pccrit': False, 'nmos2_width': 2000, 'nmos2_length': 30, 'nmos2_gate': 1, 'nmos2_dummy': False, 'nmos2_xvt': 'RVT', 'nmos2_pccrit': False, 'guardring_bot': 2, 'guardring_top': 2, 'guardring_left': 2, 'guardring_right': 2, 'guardring_width': None, 'guardring_height': None, 'diode_connect': True}, \
	# 											   'nmos_stack_fine_param': {'nmos1_width': 500, 'nmos1_length': 500, 'nmos1_gate': 1, 'nmos1_dummy': False, 'nmos1_xvt': 'RVT', 'nmos1_pccrit': False, 'nmos2_width': 2000, 'nmos2_length': 30, 'nmos2_gate': 1, 'nmos2_dummy': False, 'nmos2_xvt': 'RVT', 'nmos2_pccrit': False, 'guardring_bot': 2, 'guardring_top': 2, 'guardring_left': 2, 'guardring_right': 2, 'guardring_width': None, 'guardring_height': None, 'diode_connect': True}, \
	# 											   'nmos_stack_mirror_param': {'nmos1_width': 2000, 'nmos1_length': 500, 'nmos1_gate': 1, 'nmos1_dummy': False, 'nmos1_xvt': 'RVT', 'nmos1_pccrit': False, 'nmos2_width': 2000, 'nmos2_length': 30, 'nmos2_gate': 1, 'nmos2_dummy': False, 'nmos2_xvt': 'RVT', 'nmos2_pccrit': False, 'guardring_bot': 2, 'guardring_top': 2, 'guardring_left': 2, 'guardring_right': 2, 'guardring_width': None, 'guardring_height': None, 'diode_connect': False}, \
	# 											   'nmos_single_sw_param':{'nmos_gate':2,'nmos_width':1000,'nmos_length':30,'nmos_dummy':True,'xvt':'SLVT','pccrit':True,'guardring_right':2,'guardring_left':2,'guardring_bot':2,'guardring_top':2,'guardring_width':None,'guardring_height':None},\
    #                               				   'nmos_single_tail_param':{'nmos1_gate':1,'nmos1_width':2000,'nmos1_length':500,'nmos1_dummy':False,'nmos1_xvt':'RVT','nmos1_pccrit':False,'guardring_left':2,'guardring_right':2,'guardring_top':2,'guardring_bot':2,'guardring_width':None,'guardring_height':None},\
	# 											   'guardring_width': None, 'guardring_height': None, 'mirror_num2':4, 'coarse_num': 4, 'fine_num': 3, 'mirror_num': 1, 'Xnum': 3, 'Ynum':4}):
	#
	# 	drc = DRC.DRC()
	# 	_Name = self._DesignParameter['_Name']['_Name']
	#
	# 	self._DesignParameter['pset'] = self._SrefElementDeclaration(_DesignObj=PSET_Current_Mirror._PSET_Current_Mirror(_Name='psetIn{}'.format(_Name)))[0]
	# 	self._DesignParameter['pset']['_DesignObj']._CalculateDesignParameter(**dict(**pset_param))
	# 	self._DesignParameter['pset']['_XYCoordinates'] = [[0, 0]]
	# 	self._DesignParameter['nset'] = self._SrefElementDeclaration(_DesignObj=NSET_Current_mirror._NSET_Current_Mirror(_Name='nsetIn{}'.format(_Name)))[0]
	# 	self._DesignParameter['nset']['_DesignObj']._CalculateDesignParameter_v2(**dict(**nset_param))
	#
	# 	_Ycoordinate_nset=self._DesignParameter['pset']['_XYCoordinates'][0][1]+self._DesignParameter['pset']['_DesignObj']._DesignParameter['pmos2']['_XYCoordinates'][0][1]+self._DesignParameter['pset']['_DesignObj']._DesignParameter['pmos2']['_DesignObj']._DesignParameter['pguardring']['_XYCoordinates'][0][1]+self._DesignParameter['pset']['_DesignObj']._DesignParameter['pmos2']['_DesignObj']._DesignParameter['pguardring']['_DesignObj']._DesignParameter['bot']['_XYCoordinates'][0][1]-self._DesignParameter['pset']['_DesignObj']._DesignParameter['pmos2']['_DesignObj']._DesignParameter['pguardring']['_DesignObj']._DesignParameter['bot']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']/2-\
	# 					  (self._DesignParameter['nset']['_DesignObj']._DesignParameter['nmos_sw']['_XYCoordinates'][0][1]+self._DesignParameter['nset']['_DesignObj']._DesignParameter['nmos_sw']['_DesignObj']._DesignParameter['guardring']['_XYCoordinates'][0][1]+self._DesignParameter['nset']['_DesignObj']._DesignParameter['nmos_sw']['_DesignObj']._DesignParameter['guardring']['_DesignObj']._DesignParameter['top']['_XYCoordinates'][0][1]+self._DesignParameter['nset']['_DesignObj']._DesignParameter['nmos_sw']['_DesignObj']._DesignParameter['guardring']['_DesignObj']._DesignParameter['top']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']/2)-drc._Metal1MinSpace3
	#
	# 	self._DesignParameter['nset']['_XYCoordinates'] = [[self._DesignParameter['pset']['_XYCoordinates'][0][0], _Ycoordinate_nset]]
	#
	# 	self._DesignParameter['m4_pnrouting_x']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL4'][0], _Datatype=DesignParameters._LayerMapping['METAL4'][1], _Width=self.getWidth('nset','m4_mirror2_sw_x'))
	# 	self._DesignParameter['m4_pnrouting_x']['_XYCoordinates']=[[[self.getXY('nset','nmos_sw','via_m1_m4_drain')[0][0], self.getXY('nset','nmos_sw','via_m1_m4_drain')[0][1]], [self.getXY('pset','pmos1','via_m1_m4')[0][0], self.getXY('nset','nmos_sw','via_m1_m4_drain')[0][1]]],\
	# 															 [[self.getXY('nset','nmos_sw')[-1][0]+self._DesignParameter['nset']['_DesignObj']._DesignParameter['nmos_sw']['_DesignObj']._DesignParameter['via_m1_m4_drain']['_XYCoordinates'][0][0], self.getXY('nset','nmos_sw','via_m1_m4_drain')[0][1]], [self.getXY('pset','pmos3','via_m1_m4')[0][0], self.getXY('nset','nmos_sw','via_m1_m4_drain')[0][1]]]]
	#
	# 	self._DesignParameter['m5_pnrouting_y']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL5'][0], _Datatype=DesignParameters._LayerMapping['METAL5'][1], _Width=self.getXWidth('pset','via_m2_m5_drain_pmos3','ViaMet42Met5','_Met5Layer'))
	# 	self._DesignParameter['m5_pnrouting_y']['_XYCoordinates']=[[self.getXY('pset','via_m2_m5_drain_pmos1')[0], [self.getXY('pset','pmos1','via_m1_m4')[0][0], self.getXY('nset','nmos_sw','via_m1_m4_drain')[0][1]]],\
	# 															 [[self.getXY('nset','nmos_sw')[-1][0]+self._DesignParameter['nset']['_DesignObj']._DesignParameter['nmos_sw']['_DesignObj']._DesignParameter['via_m1_m4_drain']['_XYCoordinates'][0][0], self.getXY('nset','nmos_sw','via_m1_m4_drain')[0][1]], \
	# 															  [self.getXY('pset','pmos3','via_m1_m4')[0][0], self.getXY('nset','nmos_sw','via_m1_m4_drain')[0][1]]]]
	#
	# 	self._DesignParameter['m5_routing_y']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL5'][0], _Datatype=DesignParameters._LayerMapping['METAL5'][1], _Width=2*drc._MetalxMinWidth)
	# 	tmp=[]
	# 	tmp.append([self.getXY('pset','via_m2_m5_sw1')[0], [self.getXY('pset','via_m2_m5_sw1')[0][0], self._DesignParameter['nset']['_XYCoordinates'][0][1]+self._DesignParameter['nset']['_DesignObj']._DesignParameter['m4_connect_x']['_XYCoordinates'][0][0][1]]])
	# 	tmp.append([self.getXY('pset','Via_m3_m4_pmos_sw')[0], [self.getXY('pset','Via_m3_m4_pmos_sw')[0][0], self.getXY('nset','via_m1_m4_mirror')[0][1]]])
	# 	self._DesignParameter['m5_routing_y']['_XYCoordinates']=tmp
	# 	del tmp
	#
	# 	self._DesignParameter['via_m4_m5_routing']=self._SrefElementDeclaration(_DesignObj=ViaMet42Met5._ViaMet42Met5(_Name='via_m4_m5_routingIn{}'.format(_Name)))[0]
	# 	self._DesignParameter['via_m4_m5_routing']['_DesignObj']._CalculateViaMet42Met5DesignParameterMinimumEnclosureX(**dict(_ViaMet42Met5NumberOfCOX=2, _ViaMet42Met5NumberOfCOY=2))
	# 	self._DesignParameter['via_m4_m5_routing']['_XYCoordinates'] = [[self._DesignParameter['m5_routing_y']['_XYCoordinates'][0][0][0], self._DesignParameter['nset']['_XYCoordinates'][0][1]+self._DesignParameter['nset']['_DesignObj']._DesignParameter['m4_connect_x']['_XYCoordinates'][0][0][1]]]

