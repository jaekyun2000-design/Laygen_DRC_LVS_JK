from generatorLib import StickDiagram
from generatorLib import DesignParameters
import copy
import math
from generatorLib import DRC
from generatorLib.generator_models import pmos_cap_current_mirror
from generatorLib.generator_models import pmos_current_mirror
from generatorLib.generator_models import ViaStack
from generatorLib.generator_models import ViaMet32Met4


class _PSET_Current_Mirror(StickDiagram._StickDiagram):
	def __init__(self, _DesignParameter=None, _Name='PSET_Current_Mirror'):
		if _DesignParameter != None:
			self._DesignParameter = _DesignParameter
		else:
			self._DesignParameter = dict(_Name=self._NameDeclaration(_Name=_Name), _GDSFile=self._GDSObjDeclaration(_GDSFile=None))
		self._DesignParameter['_Name']['Name'] = _Name

	def _CalculateDesignParameter(self,pmos1_param={'finger': 2, 'width': 1500, 'length': 100, 'dummy': True, 'xvt': 'LVT', 'pccrit': False, 'guardring_co_right': 3, 'guardring_co_left': 3, 'guardring_co_top': 4, 'guardring_co_bottom': 2,'guardring_width':None,'guardring_height':None},\
								  pmos2_param={'finger': 2, 'width': 1500, 'length': 100, 'dummy': True, 'xvt': 'LVT', 'pccrit': False, 'guardring_co_right': 3, 'guardring_co_left': 3, 'guardring_co_top': 4, 'guardring_co_bottom': 2,'guardring_width':None,'guardring_height':None},\
								  pmos3_param={'finger': 2, 'width': 1500, 'length': 100, 'dummy': True, 'xvt': 'LVT', 'pccrit': 'False ', 'guardring_co_right': 3, 'guardring_co_left': 3, 'guardring_co_top': 4, 'guardring_co_bottom': 2,'guardring_width':None,'guardring_height':None},\
								  pmos_cap_param={'pmos_cap_gate':16,'pmos_cap_width':1500,'pmos_cap_length':100,'pmos_cap_dummy':False,'pmos_cap_xvt':'LVT','pmos_cap_pccrit':False,'pmos_sw1_gate':1,'pmos_sw1_width':1000,'pmos_sw1_length':30,'pmos_sw1_dummy':True,'pmos_sw1_xvt':'LVT','pmos_sw1_pccrit':True,'pmos_sw2_gate':1,'pmos_sw2_width':1000,'pmos_sw2_length':30,'pmos_sw2_dummy':True,'pmos_sw2_xvt':'LVT','pmos_sw2_pccrit':True,'guardring_co_bottom':4,'guardring_co_top':3,'guardring_co_left':3,'guardring_co_right':3,'guardring_width':None,'guardring_height':None,'guardring_width':None,'guardring_height':None}):

		drc = DRC.DRC()
		_Name = self._DesignParameter['_Name']['_Name']

		self._DesignParameter['pmos2'] = self._SrefElementDeclaration(_DesignObj=pmos_current_mirror._pmos_current_mirror(_Name='pmos2In{}'.format(_Name)))[0]
		self._DesignParameter['pmos2']['_DesignObj']._CalculateDesignParameter(**dict(**pmos2_param))
		self._DesignParameter['pmos2']['_XYCoordinates'] = [[0, 0]]
		self._DesignParameter['pmos1'] = self._SrefElementDeclaration(_DesignObj=pmos_current_mirror._pmos_current_mirror(_Name='pmos1In{}'.format(_Name)))[0]
		self._DesignParameter['pmos1']['_DesignObj']._CalculateDesignParameter(**dict(**pmos1_param))
		self._DesignParameter['pmos1']['_XYCoordinates'] = [[(((self._DesignParameter['pmos2']['_XYCoordinates'][0][0] + self._DesignParameter['pmos2']['_DesignObj']._DesignParameter['pguardring']['_XYCoordinates'][0][0]) + self._DesignParameter['pmos2']['_DesignObj']._DesignParameter['pguardring']['_DesignObj']._DesignParameter['left']['_XYCoordinates'][0][0]) - (self._DesignParameter['pmos1']['_DesignObj']._DesignParameter['pguardring']['_XYCoordinates'][0][0] + self._DesignParameter['pmos1']['_DesignObj']._DesignParameter['pguardring']['_DesignObj']._DesignParameter['right']['_XYCoordinates'][0][0])), (((self._DesignParameter['pmos2']['_XYCoordinates'][0][1] + self._DesignParameter['pmos2']['_DesignObj']._DesignParameter['pguardring']['_XYCoordinates'][0][1]) + self._DesignParameter['pmos2']['_DesignObj']._DesignParameter['pguardring']['_DesignObj']._DesignParameter['top']['_XYCoordinates'][0][1]) - (self._DesignParameter['pmos1']['_DesignObj']._DesignParameter['pguardring']['_XYCoordinates'][0][1] + self._DesignParameter['pmos1']['_DesignObj']._DesignParameter['pguardring']['_DesignObj']._DesignParameter['top']['_XYCoordinates'][0][1]))]]
		self._DesignParameter['pmos3'] = self._SrefElementDeclaration(_DesignObj=pmos_current_mirror._pmos_current_mirror(_Name='pmos3In{}'.format(_Name)))[0]
		self._DesignParameter['pmos3']['_DesignObj']._CalculateDesignParameter(**dict(**pmos3_param))
		self._DesignParameter['pmos3']['_XYCoordinates'] = [[(((self._DesignParameter['pmos2']['_XYCoordinates'][0][0] + self._DesignParameter['pmos2']['_DesignObj']._DesignParameter['pguardring']['_XYCoordinates'][0][0]) + self._DesignParameter['pmos2']['_DesignObj']._DesignParameter['pguardring']['_DesignObj']._DesignParameter['right']['_XYCoordinates'][0][0]) - (self._DesignParameter['pmos3']['_DesignObj']._DesignParameter['pguardring']['_XYCoordinates'][0][0] + self._DesignParameter['pmos3']['_DesignObj']._DesignParameter['pguardring']['_DesignObj']._DesignParameter['left']['_XYCoordinates'][0][0])), (((self._DesignParameter['pmos2']['_XYCoordinates'][0][1] + self._DesignParameter['pmos2']['_DesignObj']._DesignParameter['pguardring']['_XYCoordinates'][0][1]) + self._DesignParameter['pmos2']['_DesignObj']._DesignParameter['pguardring']['_DesignObj']._DesignParameter['top']['_XYCoordinates'][0][1]) - (self._DesignParameter['pmos3']['_DesignObj']._DesignParameter['pguardring']['_XYCoordinates'][0][1] + self._DesignParameter['pmos3']['_DesignObj']._DesignParameter['pguardring']['_DesignObj']._DesignParameter['top']['_XYCoordinates'][0][1]))]]
		self._DesignParameter['pmos_cap'] = self._SrefElementDeclaration(_DesignObj=pmos_cap_current_mirror._pmos_cap_current_mirror(_Name='pmos_capIn{}'.format(_Name)))[0]
		self._DesignParameter['pmos_cap']['_DesignObj']._CalculateDesignParameter(**dict(**pmos_cap_param))

		x_offset=self._DesignParameter['pmos_cap']['_DesignObj']._DesignParameter['guardring']['_XYCoordinates'][0][0]+(self._DesignParameter['pmos_cap']['_DesignObj']._DesignParameter['guardring']['_DesignObj']._DesignParameter['right']['_XYCoordinates'][0][0]+self._DesignParameter['pmos_cap']['_DesignObj']._DesignParameter['guardring']['_DesignObj']._DesignParameter['left']['_XYCoordinates'][0][0])/2
		self._DesignParameter['pmos_cap']['_XYCoordinates'] = [[self._DesignParameter['pmos2']['_XYCoordinates'][0][0]-x_offset, self._DesignParameter['pmos2']['_XYCoordinates'][0][1]+self._DesignParameter['pmos2']['_DesignObj']._DesignParameter['pguardring']['_XYCoordinates'][0][1]+self._DesignParameter['pmos2']['_DesignObj']._DesignParameter['pguardring']['_DesignObj']._DesignParameter['top']['_XYCoordinates'][0][1]+(self._DesignParameter['pmos_cap']['_DesignObj']._DesignParameter['pmos_cap']['_XYCoordinates'][0][1]-(self._DesignParameter['pmos_cap']['_DesignObj']._DesignParameter['guardring']['_XYCoordinates'][0][1]+self._DesignParameter['pmos_cap']['_DesignObj']._DesignParameter['guardring']['_DesignObj']._DesignParameter['bot']['_XYCoordinates'][0][1]))]]

		#### Constraints ####
		if (pmos1_param['guardring_co_top']==pmos2_param['guardring_co_top']==pmos3_param['guardring_co_top']==pmos_cap_param['guardring_co_bottom']) != True :
			raise NotImplementedError
		if (pmos1_param['guardring_co_bottom']==pmos2_param['guardring_co_bottom']==pmos3_param['guardring_co_bottom']) != True :
			raise NotImplementedError
		if (pmos1_param['guardring_co_right']==pmos2_param['guardring_co_left']) != True :
			raise NotImplementedError
		if (pmos2_param['guardring_co_right']==pmos3_param['guardring_co_left']) != True :
			raise NotImplementedError

		self._DesignParameter['pmos_cap']['_DesignObj']._DesignParameter['guardring']['_DesignObj']._DesignParameter['bot']['_DesignObj']._DesignParameter['_COLayer']['_XYCoordinates']=[]


		via_num = max(2, max(1, (1 + int((((self._DesignParameter['pmos1']['_DesignObj']._DesignParameter['pmos']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] - drc._VIAxMinSpace) - (2 * drc._VIAxMinEnclosureByMetx)) / (drc._VIAxMinWidth + drc._VIAxMinSpace))))))
		self._DesignParameter['via_m2_m5_drain_pmos1'] = self._SrefElementDeclaration(_DesignObj=ViaStack._ViaStack(_Name='via_m2_m5_drain_pmos1In{}'.format(_Name)))[0]
		self._DesignParameter['via_m2_m5_drain_pmos1']['_DesignObj']._CalculateStackMinimumEnclosureY(**dict(COX=1, COY=via_num, start_layer=2,end_layer=5))

		XYList=[]
		for i in range(0,len(self._DesignParameter['pmos1']['_DesignObj']._DesignParameter['pmos']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'])):
			XYList.append(self.getXY('pmos1','pmos','_XYCoordinatePMOSOutputRouting')[i])
		self._DesignParameter['via_m2_m5_drain_pmos1']['_XYCoordinates'] = XYList

		del XYList

		via_num = max(2, max(1, (1 + int((((self._DesignParameter['pmos3']['_DesignObj']._DesignParameter['pmos']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] - drc._VIAxMinSpace) - (2 * drc._VIAxMinEnclosureByMetx)) / (drc._VIAxMinWidth + drc._VIAxMinSpace))))))
		self._DesignParameter['via_m2_m5_drain_pmos3'] = self._SrefElementDeclaration(_DesignObj=ViaStack._ViaStack(_Name='via_m2_m5_drain_pmos3In{}'.format(_Name)))[0]
		self._DesignParameter['via_m2_m5_drain_pmos3']['_DesignObj']._CalculateStackMinimumEnclosureY(**dict(COX=1, COY=via_num, start_layer=2,end_layer=5))

		XYList=[]
		for i in range(0,len(self._DesignParameter['pmos3']['_DesignObj']._DesignParameter['pmos']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'])):
			XYList.append(self.getXY('pmos3','pmos','_XYCoordinatePMOSOutputRouting')[i])
		self._DesignParameter['via_m2_m5_drain_pmos3']['_XYCoordinates'] = XYList

		del XYList

		self._DesignParameter['pmos2']['_DesignObj']._DesignParameter['via_m1_m2_drain']['_XYCoordinates']=[]
		#self._DesignParameter['pmos2']['_DesignObj']._DesignParameter['m2_output_x']['_XYCoordinates']=[]

		self._DesignParameter['m1_pmos2_y']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=None)
		self._DesignParameter['m1_pmos2_y']['_Width']=self.getXWidth('pmos2','pmos','_Met1Layer')

		tmp=[]
		for i in range(0,len(self.getXY('pmos2','pmos','_XYCoordinatePMOSOutputRouting'))):
			tmp.append([self.getXY('pmos2','pmos','_XYCoordinatePMOSOutputRouting')[i], [self.getXY('pmos2','pmos','_XYCoordinatePMOSOutputRouting')[i][0], self.getXY('pmos2','via_gate')[0][1]]])
		self._DesignParameter['m1_pmos2_y']['_XYCoordinates']=tmp
		del tmp

		self._DesignParameter['m1_pmos2_x']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=None)
		self._DesignParameter['m1_pmos2_x']['_Width']=self.getYWidth('pmos2','via_gate','_Met1Layer')
		self._DesignParameter['m1_pmos2_x']['_XYCoordinates']=[[[self.getXY('pmos2','pmos','_XYCoordinatePMOSOutputRouting')[0][0]-self.getXWidth('pmos2','pmos','_Met1Layer')/2, self.getXY('pmos2','via_gate')[0][1]], [self.getXY('pmos2','pmos','_XYCoordinatePMOSOutputRouting')[-1][0]+self.getXWidth('pmos2','pmos','_Met1Layer')/2, self.getXY('pmos2','via_gate')[0][1]]]]

		self._DesignParameter['m4_gate_routing']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL4'][0], _Datatype=DesignParameters._LayerMapping['METAL4'][1], _Width=self.getYWidth('pmos1','via_m1_m4','ViaMet32Met4','_Met4Layer'))
		self._DesignParameter['m4_gate_routing']['_XYCoordinates']=[[self.getXY('pmos1','via_m1_m4')[0], self.getXY('pmos3','via_m1_m4')[0]]]

		self._DesignParameter['via_m2_m5_sw1'] = self._SrefElementDeclaration(_DesignObj=ViaStack._ViaStack(_Name='via_m2_m5_sw1In{}'.format(_Name)))[0]
		self._DesignParameter['via_m2_m5_sw1']['_DesignObj']._CalculateStackMinimumEnclosureX(**dict(COX=2, COY=2, start_layer=2, end_layer=5))
		self._DesignParameter['via_m2_m5_sw1']['_XYCoordinates'] = [[((self._DesignParameter['pmos2']['_XYCoordinates'][0][0] + self._DesignParameter['pmos2']['_DesignObj']._DesignParameter['pguardring']['_XYCoordinates'][0][0]) + self._DesignParameter['pmos2']['_DesignObj']._DesignParameter['pguardring']['_DesignObj']._DesignParameter['left']['_XYCoordinates'][0][0]), (self._DesignParameter['pmos_cap']['_XYCoordinates'][0][1] + self._DesignParameter['pmos_cap']['_DesignObj']._DesignParameter['via_source_sw1']['_XYCoordinates'][0][1])]]
		self._DesignParameter['m2_sw1_source'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _Width=drc._MetalxMinWidth)
		self._DesignParameter['m2_sw1_source']['_XYCoordinates'] = [[[(self._DesignParameter['pmos_cap']['_XYCoordinates'][0][0] + self._DesignParameter['pmos_cap']['_DesignObj']._DesignParameter['via_source_sw1']['_XYCoordinates'][(- 1)][0]), (self._DesignParameter['pmos_cap']['_XYCoordinates'][0][1] + self._DesignParameter['pmos_cap']['_DesignObj']._DesignParameter['via_source_sw1']['_XYCoordinates'][(- 1)][1])], [(+ self._DesignParameter['via_m2_m5_sw1']['_XYCoordinates'][0][0]), (+ self._DesignParameter['via_m2_m5_sw1']['_XYCoordinates'][0][1])]]]
		self._DesignParameter['via_m3_m4_sw2'] = self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_Name='via_m3_m4_sw2In{}'.format(_Name)))[0]
		self._DesignParameter['via_m3_m4_sw2']['_DesignObj']._CalculateViaMet32Met4DesignParameterMinimumEnclosureX(**dict(_ViaMet32Met4NumberOfCOX=2, _ViaMet32Met4NumberOfCOY=2))
		self._DesignParameter['via_m3_m4_sw2']['_XYCoordinates'] = [[(self._DesignParameter['pmos2']['_XYCoordinates'][0][0] + self._DesignParameter['pmos2']['_DesignObj']._DesignParameter['pguardring']['_XYCoordinates'][0][0] + self._DesignParameter['pmos2']['_DesignObj']._DesignParameter['pguardring']['_DesignObj']._DesignParameter['right']['_XYCoordinates'][0][0]), (self._DesignParameter['pmos_cap']['_XYCoordinates'][0][1] + self._DesignParameter['pmos_cap']['_DesignObj']._DesignParameter['via_drain_sw2']['_XYCoordinates'][0][1])]]
		self._DesignParameter['m4_sw2_drain'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL4'][0], _Datatype=DesignParameters._LayerMapping['METAL4'][1], _Width=drc._MetalxMinWidth)
		self._DesignParameter['m4_sw2_drain']['_XYCoordinates'] = [[[(self._DesignParameter['pmos_cap']['_XYCoordinates'][0][0] + self._DesignParameter['pmos_cap']['_DesignObj']._DesignParameter['via_drain_sw2']['_XYCoordinates'][(- 1)][0]), (self._DesignParameter['pmos_cap']['_XYCoordinates'][0][1] + self._DesignParameter['pmos_cap']['_DesignObj']._DesignParameter['via_drain_sw2']['_XYCoordinates'][(- 1)][1])], [self._DesignParameter['via_m3_m4_sw2']['_XYCoordinates'][0][0], (self._DesignParameter['pmos_cap']['_XYCoordinates'][0][1] + self._DesignParameter['pmos_cap']['_DesignObj']._DesignParameter['via_drain_sw2']['_XYCoordinates'][0][1])]]]
		self._DesignParameter['m3_sw2_pmos2'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0], _Datatype=DesignParameters._LayerMapping['METAL3'][1], _Width=(drc._MetalxMinWidth * 2))
		self._DesignParameter['m3_sw2_pmos2']['_XYCoordinates'] = [[[(+ self._DesignParameter['via_m3_m4_sw2']['_XYCoordinates'][0][0]), (+ self._DesignParameter['via_m3_m4_sw2']['_XYCoordinates'][0][1])], [(+ self._DesignParameter['via_m3_m4_sw2']['_XYCoordinates'][0][0]), (+ (self._DesignParameter['pmos2']['_XYCoordinates'][0][1] + self._DesignParameter['pmos2']['_DesignObj']._DesignParameter['via_m1_m4']['_XYCoordinates'][0][1]))]]]
		self._DesignParameter['m4_sw_input'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL4'][0], _Datatype=DesignParameters._LayerMapping['METAL4'][1], _Width=drc._MetalxMinWidth)
		self._DesignParameter['m4_sw_input']['_XYCoordinates'] = [[[(+ (self._DesignParameter['pmos_cap']['_XYCoordinates'][0][0] + self._DesignParameter['pmos_cap']['_DesignObj']._DesignParameter['via_m1_m4_sw2']['_XYCoordinates'][0][0])), (+ (self._DesignParameter['pmos_cap']['_XYCoordinates'][0][1] + self._DesignParameter['pmos_cap']['_DesignObj']._DesignParameter['via_m1_m4_sw2']['_XYCoordinates'][0][1]))], [((((self._DesignParameter['pmos_cap']['_XYCoordinates'][0][0] + self._DesignParameter['pmos_cap']['_DesignObj']._DesignParameter['pmos_sw2']['_XYCoordinates'][0][0]) + self._DesignParameter['pmos_cap']['_DesignObj']._DesignParameter['pmos_sw2']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][0]) + ((self._DesignParameter['pmos_cap']['_XYCoordinates'][0][0] + self._DesignParameter['pmos_cap']['_DesignObj']._DesignParameter['pmos_sw1']['_XYCoordinates'][0][0]) + self._DesignParameter['pmos_cap']['_DesignObj']._DesignParameter['pmos_sw1']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][(- 1)][0])) / 2), (self._DesignParameter['pmos_cap']['_XYCoordinates'][0][1] + self._DesignParameter['pmos_cap']['_DesignObj']._DesignParameter['via_m1_m4_sw2']['_XYCoordinates'][0][1])], [((((self._DesignParameter['pmos_cap']['_XYCoordinates'][0][0] + self._DesignParameter['pmos_cap']['_DesignObj']._DesignParameter['pmos_sw1']['_XYCoordinates'][0][0]) + self._DesignParameter['pmos_cap']['_DesignObj']._DesignParameter['pmos_sw1']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][(- 1)][0]) + ((self._DesignParameter['pmos_cap']['_XYCoordinates'][0][0] + self._DesignParameter['pmos_cap']['_DesignObj']._DesignParameter['pmos_sw2']['_XYCoordinates'][0][0]) + self._DesignParameter['pmos_cap']['_DesignObj']._DesignParameter['pmos_sw2']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][0])) / 2), (self._DesignParameter['pmos_cap']['_XYCoordinates'][0][1] + self._DesignParameter['pmos_cap']['_DesignObj']._DesignParameter['via_m1_m4_sw1']['_XYCoordinates'][0][1])], [(+ (self._DesignParameter['pmos_cap']['_XYCoordinates'][0][0] + self._DesignParameter['pmos_cap']['_DesignObj']._DesignParameter['via_m1_m4_sw1']['_XYCoordinates'][0][0])), (+ (self._DesignParameter['pmos_cap']['_XYCoordinates'][0][1] + self._DesignParameter['pmos_cap']['_DesignObj']._DesignParameter['via_m1_m4_sw1']['_XYCoordinates'][0][1]))]]]
		self._DesignParameter['Via_m3_m4_pmos_sw']=self._SrefElementDeclaration(_DesignObj=ViaStack._ViaStack(_Name='Via_m3_m4_pmos_swIn{}'.format(_Name)))[0]
		self._DesignParameter['Via_m3_m4_pmos_sw']['_DesignObj']._CalculateStackMinimumEnclosureY(**dict(COX=2, COY=1, start_layer=3, end_layer=5))
		self._DesignParameter['Via_m3_m4_pmos_sw']['_XYCoordinates']=[[self._DesignParameter['m3_sw2_pmos2']['_XYCoordinates'][0][0][0], self._DesignParameter['m4_gate_routing']['_XYCoordinates'][0][0][1]]]