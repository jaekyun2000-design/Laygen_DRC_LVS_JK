from generatorLib import StickDiagram
from generatorLib import DesignParameters
import copy
import math
from generatorLib import DRC
from generatorLib.generator_models import PMOSWithDummy
from generatorLib.generator_models import NMOSWithDummy
from generatorLib.generator_models import ViaPoly2Met1
from generatorLib.generator_models import ViaMet12Met2
from generatorLib.generator_models import ViaMet22Met3
from generatorLib.generator_models import ViaMet32Met4
from generatorLib.generator_models import NSubRing
from generatorLib.generator_models import PSubRing
from generatorLib.generator_models import PbodyContact

class _Folded_Cascode_Amp(StickDiagram._StickDiagram):
	def __init__(self, _DesignParameter=None, _Name='Folded_Cascode_Amp'):
		super().__init__()
		if _DesignParameter != None:
			self._DesignParameter = _DesignParameter
		else:
			self._DesignParameter = dict(_Name=self._NameDeclaration(_Name=_Name), _GDSFile=self._GDSObjDeclaration(_GDSFile=None))
		self._DesignParameter['_Name']['Name'] = _Name

	def _CalculateDesignParameter(self, pset_param={'pmos_pdn_single_sw_param':{'_PMOSNumberofGate':4, '_PMOSChannelWidth':2000, '_PMOSChannellength':30, '_PMOSDummy':True, '_GateSpacing':None, '_SDWidth':None, '_XVT':'LVT', '_PCCrit':None}, \
														'pmos_pdn_pair_sw_param':{'_PMOSNumberofGate':32, '_PMOSChannelWidth':250, '_PMOSChannellength':30, '_PMOSDummy':True, '_GateSpacing':None, '_SDWidth':None, '_XVT':'LVT', '_PCCrit':None}, \
														'pmos_current_pair1_param':{'_PMOSNumberofGate':8, '_PMOSChannelWidth':5000, '_PMOSChannellength':1000, '_PMOSDummy':False, '_GateSpacing':None, '_SDWidth':None, '_XVT':'LVT', '_PCCrit':None}, \
														'pmos_current_pair2_param':{'_PMOSNumberofGate':8, '_PMOSChannelWidth':5000, '_PMOSChannellength':1000, '_PMOSDummy':False, '_GateSpacing':None, '_SDWidth':None, '_XVT':'LVT', '_PCCrit':None},\
														'pmos_current_single_param':{'_PMOSNumberofGate':8, '_PMOSChannelWidth':5000, '_PMOSChannellength':1000, '_PMOSDummy':False, '_GateSpacing':None, '_SDWidth':None, '_XVT':'LVT', '_PCCrit':None},\
														'pmos_input_param':{'_PMOSNumberofGate':8, '_PMOSChannelWidth':5000, '_PMOSChannellength':1000, '_PMOSDummy':False, '_GateSpacing':None, '_SDWidth':None, '_XVT':'LVT', '_PCCrit':None}, \
														'pmos_guardring_co_left':1,'pmos_guardring_co_right':1, 'pmos_guardring_co_top':1, 'pmos_guardring_co_bot':2, 'pmos_guardring_height1':None, 'pmos_guardring_width1':None, 'pmos_guardring_width2':None, 'pmos_guardring_height2':None},\
										nset_param={'nmos_pdn_sw_param':{'_NMOSNumberofGate':2, '_NMOSChannelWidth':2000, '_NMOSChannellength':30, '_NMOSDummy':True, '_GateSpacing':None, '_SDWidth':None, '_XVT':'RVT', '_PCCrit':None}, \
														'nmos_current_pair1_param':{'_NMOSNumberofGate':4, '_NMOSChannelWidth':5000, '_NMOSChannellength':1000, '_NMOSDummy':False, '_GateSpacing':None, '_SDWidth':None, '_XVT':'RVT', '_PCCrit':None}, \
														'nmos_current_pair2_param':{'_NMOSNumberofGate':4, '_NMOSChannelWidth':5000, '_NMOSChannellength':1000, '_NMOSDummy':False, '_GateSpacing':None, '_SDWidth':None, '_XVT':'RVT', '_PCCrit':None},\
														'nmos_current_single_param':{'_NMOSNumberofGate':4, '_NMOSChannelWidth':5000, '_NMOSChannellength':1000, '_NMOSDummy':False, '_GateSpacing':None, '_SDWidth':None, '_XVT':'RVT', '_PCCrit':None},\
														'nmos_input_param':{'_NMOSNumberofGate':8, '_NMOSChannelWidth':2500, '_NMOSChannellength':1000, '_NMOSDummy':False, '_GateSpacing':None, '_SDWidth':None, '_XVT':'RVT', '_PCCrit':None}, \
														'nmos_guardring_co_left':1,'nmos_guardring_co_right':1, 'nmos_guardring_co_top':1, 'nmos_guardring_co_bot':1, 'nmos_guardring_height1':None, 'nmos_guardring_width1':None, 'nmos_guardring_width2':None, 'nmos_guardring_height2':None}) :

		drc = DRC.DRC()
		_Name = self._DesignParameter['_Name']['_Name']
		MinSnapSpacing=drc._MinSnapSpacing
		_OriginXY=[[0,0]]


		#### Pset Generation ####
		self._DesignParameter['pmos_pdn_single_sw']=self._SrefElementDeclaration(_DesignObj=PMOSWithDummy._PMOS(_Name='pmos_pdn_single_swIn{}'.format(_Name)))[0]
		self._DesignParameter['pmos_pdn_single_sw']['_DesignObj']._CalculatePMOSDesignParameter(**dict(**pset_param['pmos_pdn_single_sw_param']))

		self._DesignParameter['pmos_pdn_pair_sw']=self._SrefElementDeclaration(_DesignObj=PMOSWithDummy._PMOS(_Name='pmos_pdn_pair_swIn{}'.format(_Name)))[0]
		self._DesignParameter['pmos_pdn_pair_sw']['_DesignObj']._CalculatePMOSDesignParameter(**dict(**pset_param['pmos_pdn_pair_sw_param']))

		self._DesignParameter['pmos_vb2']=self._SrefElementDeclaration(_DesignObj=PMOSWithDummy._PMOS(_Name='pmos_vb2In{}'.format(_Name)))[0]
		self._DesignParameter['pmos_vb2']['_DesignObj']._CalculatePMOSDesignParameter(**dict(**pset_param['pmos_current_single_param']))

		self._DesignParameter['pmos_vbp2']=self._SrefElementDeclaration(_DesignObj=PMOSWithDummy._PMOS(_Name='pmos_vbp2In{}'.format(_Name)))[0]
		self._DesignParameter['pmos_vbp2']['_DesignObj']._CalculatePMOSDesignParameter(**dict(**pset_param['pmos_current_pair2_param']))

		self._DesignParameter['pmos_vbp1']=self._SrefElementDeclaration(_DesignObj=PMOSWithDummy._PMOS(_Name='pmos_vbp1In{}'.format(_Name)))[0]
		self._DesignParameter['pmos_vbp1']['_DesignObj']._CalculatePMOSDesignParameter(**dict(**pset_param['pmos_current_pair1_param']))

		self._DesignParameter['pmos_input']=self._SrefElementDeclaration(_DesignObj=PMOSWithDummy._PMOS(_Name='pmos_inputIn{}'.format(_Name)))[0]
		self._DesignParameter['pmos_input']['_DesignObj']._CalculatePMOSDesignParameter(**dict(**pset_param['pmos_input_param']))

		_Lengthbtwmet1=self._DesignParameter['pmos_vbp2']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][1][0]-self._DesignParameter['pmos_vbp2']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0]

		self._DesignParameter['pmos_vbp2']['_XYCoordinates']=[[_OriginXY[0][0]-_Lengthbtwmet1*(len(self._DesignParameter['pmos_vbp2']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'])-1)/2-drc._Metal1MinSpace*5.2, _OriginXY[0][1]],\
															  [_OriginXY[0][0]+_Lengthbtwmet1*(len(self._DesignParameter['pmos_vbp2']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'])-1)/2+drc._Metal1MinSpace*5.2, _OriginXY[0][1]]]

		CoNumX=max(1,int(self.getXWidth('pmos_vbp2','_POLayer')/(drc._CoMinWidth+drc._CoMinSpace)-1))
		self._DesignParameter['gate_vbp2']=self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_Name='gate_vbp2In{}'.format(_Name)))[0]
		self._DesignParameter['gate_vbp2']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(_ViaPoly2Met1NumberOfCOX=CoNumX, _ViaPoly2Met1NumberOfCOY=1)
		tmp=[]
		for i in range(0, len(self._DesignParameter['pmos_vbp2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
			tmp.append([self._DesignParameter['pmos_vbp2']['_XYCoordinates'][0][0]+self._DesignParameter['pmos_vbp2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0], self._DesignParameter['pmos_vbp2']['_XYCoordinates'][0][1]+self.getYWidth('pmos_vbp2','_Met1Layer')/2+self.getYWidth('gate_vbp2','_Met1Layer')/2+drc._Metal1MinSpace2])
			tmp.append([self._DesignParameter['pmos_vbp2']['_XYCoordinates'][0][0]+self._DesignParameter['pmos_vbp2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0], self._DesignParameter['pmos_vbp2']['_XYCoordinates'][0][1]-self.getYWidth('pmos_vbp2','_Met1Layer')/2-self.getYWidth('gate_vbp2','_Met1Layer')/2-drc._Metal1MinSpace2])
			tmp.append([self._DesignParameter['pmos_vbp2']['_XYCoordinates'][1][0]+self._DesignParameter['pmos_vbp2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0], self._DesignParameter['pmos_vbp2']['_XYCoordinates'][1][1]+self.getYWidth('pmos_vbp2','_Met1Layer')/2+self.getYWidth('gate_vbp2','_Met1Layer')/2+drc._Metal1MinSpace2])
			tmp.append([self._DesignParameter['pmos_vbp2']['_XYCoordinates'][1][0]+self._DesignParameter['pmos_vbp2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0], self._DesignParameter['pmos_vbp2']['_XYCoordinates'][1][1]-self.getYWidth('pmos_vbp2','_Met1Layer')/2-self.getYWidth('gate_vbp2','_Met1Layer')/2-drc._Metal1MinSpace2])

		self._DesignParameter['gate_vbp2']['_XYCoordinates']=tmp
		del tmp

		ViaNumX=max(1,int(self.getXWidth('gate_vbp2','_Met1Layer')/(drc._VIAxMinWidth+drc._VIAxMinSpace)))
		self._DesignParameter['via12_gate_vbp2']=self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='via12_gate_vbp2In{}'.format(_Name)))[0]
		self._DesignParameter['via12_gate_vbp2']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureY(_ViaMet12Met2NumberOfCOX=ViaNumX, _ViaMet12Met2NumberOfCOY=1)
		tmp=[]
		for i in range(0, len(self._DesignParameter['pmos_vbp2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
			tmp.append([self._DesignParameter['pmos_vbp2']['_XYCoordinates'][0][0]+self._DesignParameter['pmos_vbp2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0], self._DesignParameter['pmos_vbp2']['_XYCoordinates'][0][1]+self.getYWidth('pmos_vbp2','_Met1Layer')/2+self.getYWidth('gate_vbp2','_Met1Layer')/2+drc._Metal1MinSpace2])
			tmp.append([self._DesignParameter['pmos_vbp2']['_XYCoordinates'][0][0]+self._DesignParameter['pmos_vbp2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0], self._DesignParameter['pmos_vbp2']['_XYCoordinates'][0][1]-self.getYWidth('pmos_vbp2','_Met1Layer')/2-self.getYWidth('gate_vbp2','_Met1Layer')/2-drc._Metal1MinSpace2])
			tmp.append([self._DesignParameter['pmos_vbp2']['_XYCoordinates'][1][0]+self._DesignParameter['pmos_vbp2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0], self._DesignParameter['pmos_vbp2']['_XYCoordinates'][1][1]+self.getYWidth('pmos_vbp2','_Met1Layer')/2+self.getYWidth('gate_vbp2','_Met1Layer')/2+drc._Metal1MinSpace2])
			tmp.append([self._DesignParameter['pmos_vbp2']['_XYCoordinates'][1][0]+self._DesignParameter['pmos_vbp2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0], self._DesignParameter['pmos_vbp2']['_XYCoordinates'][1][1]-self.getYWidth('pmos_vbp2','_Met1Layer')/2-self.getYWidth('gate_vbp2','_Met1Layer')/2-drc._Metal1MinSpace2])

		self._DesignParameter['via12_gate_vbp2']['_XYCoordinates']=tmp
		del tmp

		self._DesignParameter['pmos_pdn_pair_sw']['_XYCoordinates']=[[self.getXY('pmos_vbp2')[0][0], self.getXY('gate_vbp2')[0][1]+self.getYWidth('gate_vbp2','_Met1Layer')+3*drc._Metal1MinSpace+2*drc._Metal1MinWidth+drc._Metal1MinSpace2+self.getYWidth('pmos_pdn_pair_sw','_Met1Layer')/2],\
																	 [self.getXY('pmos_vbp2')[1][0], self.getXY('gate_vbp2')[0][1]+self.getYWidth('gate_vbp2','_Met1Layer')+3*drc._Metal1MinSpace+2*drc._Metal1MinWidth+drc._Metal1MinSpace2+self.getYWidth('pmos_pdn_pair_sw','_Met1Layer')/2]]

		NumofVia=max(2,int(self.getYWidth('pmos_pdn_pair_sw','_Met1Layer')/(drc._VIAxMinWidth+drc._VIAxMinSpace)))
		self._DesignParameter['via12_pdn_pair_sw']=self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='via12_pdn_pair_swIn{}'.format(_Name)))[0]
		self._DesignParameter['via12_pdn_pair_sw']['_DesignObj']._CalculateDesignParameterSameEnclosure(_ViaMet12Met2NumberOfCOX=1, _ViaMet12Met2NumberOfCOY=NumofVia)
		tmp=[]
		for i in range(0,len(self._DesignParameter['pmos_pdn_pair_sw']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'])):
			tmp.append([self._DesignParameter['pmos_pdn_pair_sw']['_XYCoordinates'][0][0]+self._DesignParameter['pmos_pdn_pair_sw']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][i][0], self._DesignParameter['pmos_pdn_pair_sw']['_XYCoordinates'][0][1]])
		self._DesignParameter['via12_pdn_pair_sw']['_XYCoordinates']=tmp
		del tmp
		self._DesignParameter['via12_1_pdn_pair_sw']=self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='via12_1_pdn_pair_swIn{}'.format(_Name)))[0]
		self._DesignParameter['via12_1_pdn_pair_sw']['_DesignObj']._CalculateDesignParameterSameEnclosure(_ViaMet12Met2NumberOfCOX=1, _ViaMet12Met2NumberOfCOY=NumofVia)
		tmp=[]
		for i in range(0,len(self._DesignParameter['pmos_pdn_pair_sw']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'])):
			tmp.append([-(self._DesignParameter['pmos_pdn_pair_sw']['_XYCoordinates'][0][0]+self._DesignParameter['pmos_pdn_pair_sw']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][i][0]), self._DesignParameter['pmos_pdn_pair_sw']['_XYCoordinates'][0][1]])
		self._DesignParameter['via12_1_pdn_pair_sw']['_XYCoordinates']=tmp
		del tmp
		del NumofVia

		self._DesignParameter['poly_gate_vbp2']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0],_Datatype=DesignParameters._LayerMapping['POLY'][1], _XYCoordinates=[], _Width=None)
		self._DesignParameter['poly_gate_vbp2']['_Width']=self.getXWidth('pmos_vbp2','_POLayer')
		tmp=[]
		for i in range(0, len(self._DesignParameter['pmos_vbp2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
			tmp.append([[self._DesignParameter['pmos_vbp2']['_XYCoordinates'][0][0]+self._DesignParameter['pmos_vbp2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0], self._DesignParameter['gate_vbp2']['_XYCoordinates'][0][1]+self.getYWidth('gate_vbp2','_POLayer')/2], \
						[self._DesignParameter['pmos_vbp2']['_XYCoordinates'][0][0]+self._DesignParameter['pmos_vbp2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0], self._DesignParameter['gate_vbp2']['_XYCoordinates'][1][1]-self.getYWidth('gate_vbp2','_POLayer')/2]])
			tmp.append([[self._DesignParameter['pmos_vbp2']['_XYCoordinates'][1][0]+self._DesignParameter['pmos_vbp2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0], self._DesignParameter['gate_vbp2']['_XYCoordinates'][0][1]+self.getYWidth('gate_vbp2','_POLayer')/2], \
						[self._DesignParameter['pmos_vbp2']['_XYCoordinates'][1][0]+self._DesignParameter['pmos_vbp2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0], self._DesignParameter['gate_vbp2']['_XYCoordinates'][1][1]-self.getYWidth('gate_vbp2','_POLayer')/2]])
		self._DesignParameter['poly_gate_vbp2']['_XYCoordinates']=tmp
		del tmp

		self._DesignParameter['met1_pdn_pair_sw_x']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0],_Datatype=DesignParameters._LayerMapping['METAL1'][1], _XYCoordinates=[], _Width=None)
		self._DesignParameter['met1_pdn_pair_sw_x']['_Width']=2*drc._Metal1MinWidth
		self._DesignParameter['met1_pdn_pair_sw_x']['_XYCoordinates']=[[[self._DesignParameter['pmos_pdn_pair_sw']['_XYCoordinates'][0][0]+self._DesignParameter['pmos_pdn_pair_sw']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0]-self.getXWidth('pmos_pdn_pair_sw','_Met1Layer')/2, self._DesignParameter['pmos_pdn_pair_sw']['_XYCoordinates'][0][1]-max(self.getYWidth('pmos_pdn_pair_sw', '_Met1Layer'),self.getYWidth('via12_pdn_pair_sw', '_Met1Layer'))/2-self.getWidth('met1_pdn_pair_sw_x')/2-drc._Metal1MinSpace2], \
																		[self._DesignParameter['pmos_pdn_pair_sw']['_XYCoordinates'][0][0]+self._DesignParameter['pmos_pdn_pair_sw']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][-1][0]+self.getXWidth('pmos_pdn_pair_sw','_Met1Layer')/2, self._DesignParameter['pmos_pdn_pair_sw']['_XYCoordinates'][0][1]-max(self.getYWidth('pmos_pdn_pair_sw', '_Met1Layer'),self.getYWidth('via12_pdn_pair_sw', '_Met1Layer'))/2-self.getWidth('met1_pdn_pair_sw_x')/2-drc._Metal1MinSpace2]], \
																	   [[-(self._DesignParameter['pmos_pdn_pair_sw']['_XYCoordinates'][0][0]+self._DesignParameter['pmos_pdn_pair_sw']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0]-self.getXWidth('pmos_pdn_pair_sw','_Met1Layer')/2), self._DesignParameter['pmos_pdn_pair_sw']['_XYCoordinates'][1][1]-max(self.getYWidth('pmos_pdn_pair_sw', '_Met1Layer'),self.getYWidth('via12_pdn_pair_sw', '_Met1Layer'))/2-self.getWidth('met1_pdn_pair_sw_x')/2-drc._Metal1MinSpace2], \
																		[-(self._DesignParameter['pmos_pdn_pair_sw']['_XYCoordinates'][0][0]+self._DesignParameter['pmos_pdn_pair_sw']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][-1][0]+self.getXWidth('pmos_pdn_pair_sw','_Met1Layer')/2), self._DesignParameter['pmos_pdn_pair_sw']['_XYCoordinates'][1][1]-max(self.getYWidth('pmos_pdn_pair_sw', '_Met1Layer'),self.getYWidth('via12_pdn_pair_sw', '_Met1Layer'))/2-self.getWidth('met1_pdn_pair_sw_x')/2-drc._Metal1MinSpace2]]]

		self._DesignParameter['met1_pdn_pair_sw_y']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0],_Datatype=DesignParameters._LayerMapping['METAL1'][1], _XYCoordinates=[], _Width=None)
		self._DesignParameter['met1_pdn_pair_sw_y']['_Width']=self.getXWidth('pmos_pdn_pair_sw','_Met1Layer')
		tmp=[]
		for i in range(0,len(self._DesignParameter['pmos_pdn_pair_sw']['_DesignObj']._DesignParameter['_XYCoordinatePMOSSupplyRouting']['_XYCoordinates'])):
			tmp.append([[self._DesignParameter['pmos_pdn_pair_sw']['_XYCoordinates'][0][0]+self._DesignParameter['pmos_pdn_pair_sw']['_DesignObj']._DesignParameter['_XYCoordinatePMOSSupplyRouting']['_XYCoordinates'][i][0], self._DesignParameter['pmos_pdn_pair_sw']['_XYCoordinates'][0][1]],\
						[self._DesignParameter['pmos_pdn_pair_sw']['_XYCoordinates'][0][0]+self._DesignParameter['pmos_pdn_pair_sw']['_DesignObj']._DesignParameter['_XYCoordinatePMOSSupplyRouting']['_XYCoordinates'][i][0], self._DesignParameter['met1_pdn_pair_sw_x']['_XYCoordinates'][0][0][1]]])
			tmp.append([[self._DesignParameter['pmos_pdn_pair_sw']['_XYCoordinates'][1][0]+self._DesignParameter['pmos_pdn_pair_sw']['_DesignObj']._DesignParameter['_XYCoordinatePMOSSupplyRouting']['_XYCoordinates'][i][0], self._DesignParameter['pmos_pdn_pair_sw']['_XYCoordinates'][1][1]],\
						[self._DesignParameter['pmos_pdn_pair_sw']['_XYCoordinates'][1][0]+self._DesignParameter['pmos_pdn_pair_sw']['_DesignObj']._DesignParameter['_XYCoordinatePMOSSupplyRouting']['_XYCoordinates'][i][0], self._DesignParameter['met1_pdn_pair_sw_x']['_XYCoordinates'][0][0][1]]])
		self._DesignParameter['met1_pdn_pair_sw_y']['_XYCoordinates']=tmp
		del tmp

		self._DesignParameter['gate_pdn_pair_sw']=self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_Name='gate_pdn_pair_swIn{}'.format(_Name)))[0]
		NumofCo=max(1,int((self._DesignParameter['pmos_pdn_pair_sw']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][-1][0]-self._DesignParameter['pmos_pdn_pair_sw']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]+self.getXWidth('pmos_pdn_pair_sw','_POLayer'))/(drc._CoMinWidth + drc._CoMinSpace)))
		self._DesignParameter['gate_pdn_pair_sw']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(_ViaPoly2Met1NumberOfCOX=NumofCo, _ViaPoly2Met1NumberOfCOY=1)
		self._DesignParameter['gate_pdn_pair_sw']['_XYCoordinates']=[[self._DesignParameter['pmos_pdn_pair_sw']['_XYCoordinates'][0][0], self._DesignParameter['pmos_pdn_pair_sw']['_XYCoordinates'][0][1]+max(self.getYWidth('pmos_pdn_pair_sw', '_Met1Layer'),self.getYWidth('via12_pdn_pair_sw', '_Met1Layer'))/2+self.getYWidth('gate_pdn_pair_sw','_Met1Layer')/2+drc._Metal1MinSpace2],\
																	 [self._DesignParameter['pmos_pdn_pair_sw']['_XYCoordinates'][1][0], self._DesignParameter['pmos_pdn_pair_sw']['_XYCoordinates'][0][1]+max(self.getYWidth('pmos_pdn_pair_sw', '_Met1Layer'),self.getYWidth('via12_pdn_pair_sw', '_Met1Layer'))/2+self.getYWidth('gate_pdn_pair_sw','_Met1Layer')/2+drc._Metal1MinSpace2]]
		del NumofCo

		self._DesignParameter['poly_pdn_pair_sw_x']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0],_Datatype=DesignParameters._LayerMapping['POLY'][1], _XYCoordinates=[], _Width=None)
		self._DesignParameter['poly_pdn_pair_sw_x']['_Width']=self.getYWidth('gate_pdn_pair_sw','_POLayer')
		self._DesignParameter['poly_pdn_pair_sw_x']['_XYCoordinates']=[[[self._DesignParameter['pmos_pdn_pair_sw']['_XYCoordinates'][0][0]+self._DesignParameter['pmos_pdn_pair_sw']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]-self.getXWidth('pmos_pdn_pair_sw','_POLayer')/2, self._DesignParameter['gate_pdn_pair_sw']['_XYCoordinates'][0][1]], \
																		[self._DesignParameter['pmos_pdn_pair_sw']['_XYCoordinates'][0][0]+self._DesignParameter['pmos_pdn_pair_sw']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][-1][0]+self.getXWidth('pmos_pdn_pair_sw','_POLayer')/2, self._DesignParameter['gate_pdn_pair_sw']['_XYCoordinates'][0][1]]],\
																	   [[-(self._DesignParameter['pmos_pdn_pair_sw']['_XYCoordinates'][0][0]+self._DesignParameter['pmos_pdn_pair_sw']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]-self.getXWidth('pmos_pdn_pair_sw','_POLayer')/2), self._DesignParameter['gate_pdn_pair_sw']['_XYCoordinates'][0][1]], \
																		[-(self._DesignParameter['pmos_pdn_pair_sw']['_XYCoordinates'][0][0]+self._DesignParameter['pmos_pdn_pair_sw']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][-1][0]+self.getXWidth('pmos_pdn_pair_sw','_POLayer')/2), self._DesignParameter['gate_pdn_pair_sw']['_XYCoordinates'][0][1]]]]

		self._DesignParameter['poly_pdn_pair_sw_y']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0],_Datatype=DesignParameters._LayerMapping['POLY'][1], _XYCoordinates=[], _Width=None)
		self._DesignParameter['poly_pdn_pair_sw_y']['_Width']=self.getXWidth('pmos_pdn_pair_sw','_POLayer')
		tmp=[]
		for i in range(0, len(self._DesignParameter['pmos_pdn_pair_sw']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
			tmp.append([[self._DesignParameter['pmos_pdn_pair_sw']['_XYCoordinates'][0][0]+self._DesignParameter['pmos_pdn_pair_sw']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0], self._DesignParameter['pmos_pdn_pair_sw']['_XYCoordinates'][0][1]], [self._DesignParameter['pmos_pdn_pair_sw']['_XYCoordinates'][0][0]+self._DesignParameter['pmos_pdn_pair_sw']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0], self._DesignParameter['gate_pdn_pair_sw']['_XYCoordinates'][0][1]+self.getYWidth('gate_pdn_pair_sw','_POLayer')/2]])
			tmp.append([[self._DesignParameter['pmos_pdn_pair_sw']['_XYCoordinates'][1][0]+self._DesignParameter['pmos_pdn_pair_sw']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0], self._DesignParameter['pmos_pdn_pair_sw']['_XYCoordinates'][0][1]], [self._DesignParameter['pmos_pdn_pair_sw']['_XYCoordinates'][1][0]+self._DesignParameter['pmos_pdn_pair_sw']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0], self._DesignParameter['gate_pdn_pair_sw']['_XYCoordinates'][0][1]+self.getYWidth('gate_pdn_pair_sw','_POLayer')/2]])
		self._DesignParameter['poly_pdn_pair_sw_y']['_XYCoordinates']=tmp
		del tmp

		CoNumX=max(1,int(self.getXWidth('pmos_vbp1','_POLayer')/(drc._CoMinWidth+drc._CoMinSpace)-1))
		self._DesignParameter['gate_vbp1']=self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_Name='gate_vbp1In{}'.format(_Name)))[0]
		self._DesignParameter['gate_vbp1']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(_ViaPoly2Met1NumberOfCOX=CoNumX, _ViaPoly2Met1NumberOfCOY=1)

		self._DesignParameter['pmos_vbp1']['_XYCoordinates']=[[self._DesignParameter['pmos_pdn_pair_sw']['_XYCoordinates'][0][0], self._DesignParameter['gate_pdn_pair_sw']['_XYCoordinates'][0][1]+self.getYWidth('gate_pdn_pair_sw','_Met1Layer')/2+self.getYWidth('pmos_vbp1','_POLayer')/2+self.getYWidth('gate_vbp1','_Met1Layer')/2+6*drc._Metal1MinSpace], \
															  [self._DesignParameter['pmos_pdn_pair_sw']['_XYCoordinates'][1][0], self._DesignParameter['gate_pdn_pair_sw']['_XYCoordinates'][0][1]+self.getYWidth('gate_pdn_pair_sw','_Met1Layer')/2+self.getYWidth('pmos_vbp1','_POLayer')/2+self.getYWidth('gate_vbp1','_Met1Layer')/2+6*drc._Metal1MinSpace]]

		tmp=[]
		for i in range(0, len(self._DesignParameter['pmos_vbp1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
			tmp.append([self._DesignParameter['pmos_vbp1']['_XYCoordinates'][0][0]+self._DesignParameter['pmos_vbp1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0], self._DesignParameter['pmos_vbp1']['_XYCoordinates'][0][1]+self.getYWidth('pmos_vbp1','_Met1Layer')/2+self.getYWidth('gate_vbp1','_Met1Layer')/2+drc._Metal1MinSpace2])
			tmp.append([self._DesignParameter['pmos_vbp1']['_XYCoordinates'][0][0]+self._DesignParameter['pmos_vbp1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0], self._DesignParameter['pmos_vbp1']['_XYCoordinates'][0][1]-self.getYWidth('pmos_vbp1','_Met1Layer')/2-self.getYWidth('gate_vbp1','_Met1Layer')/2-drc._Metal1MinSpace2])
			tmp.append([self._DesignParameter['pmos_vbp1']['_XYCoordinates'][1][0]+self._DesignParameter['pmos_vbp1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0], self._DesignParameter['pmos_vbp1']['_XYCoordinates'][1][1]+self.getYWidth('pmos_vbp1','_Met1Layer')/2+self.getYWidth('gate_vbp1','_Met1Layer')/2+drc._Metal1MinSpace2])
			tmp.append([self._DesignParameter['pmos_vbp1']['_XYCoordinates'][1][0]+self._DesignParameter['pmos_vbp1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0], self._DesignParameter['pmos_vbp1']['_XYCoordinates'][1][1]-self.getYWidth('pmos_vbp1','_Met1Layer')/2-self.getYWidth('gate_vbp1','_Met1Layer')/2-drc._Metal1MinSpace2])
		self._DesignParameter['gate_vbp1']['_XYCoordinates']=tmp
		del tmp

		self._DesignParameter['poly_gate_vbp1']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0],_Datatype=DesignParameters._LayerMapping['POLY'][1], _XYCoordinates=[], _Width=None)
		self._DesignParameter['poly_gate_vbp1']['_Width']=self.getXWidth('pmos_vbp1','_POLayer')
		tmp=[]
		for i in range(0, len(self._DesignParameter['pmos_vbp1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
			tmp.append([[self._DesignParameter['pmos_vbp1']['_XYCoordinates'][0][0]+self._DesignParameter['pmos_vbp1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0], self.getXY('gate_vbp1')[0][1]+self.getYWidth('gate_vbp1','_POLayer')/2], \
						[self._DesignParameter['pmos_vbp1']['_XYCoordinates'][0][0]+self._DesignParameter['pmos_vbp1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0], self.getXY('gate_vbp1')[1][1]-self.getYWidth('gate_vbp1','_POLayer')/2]])
			tmp.append([[self._DesignParameter['pmos_vbp1']['_XYCoordinates'][1][0]+self._DesignParameter['pmos_vbp1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0], self.getXY('gate_vbp1')[0][1]+self.getYWidth('gate_vbp1','_POLayer')/2], \
						[self._DesignParameter['pmos_vbp1']['_XYCoordinates'][1][0]+self._DesignParameter['pmos_vbp1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0], self.getXY('gate_vbp1')[1][1]-self.getYWidth('gate_vbp1','_POLayer')/2]])
		self._DesignParameter['poly_gate_vbp1']['_XYCoordinates']=tmp
		del tmp

		ViaNumX=max(1,int(self.getXWidth('gate_vbp1','_Met1Layer')/(drc._VIAxMinWidth+drc._VIAxMinSpace)))
		self._DesignParameter['via12_gate_vbp1']=self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='via12_gate_vbp1In{}'.format(_Name)))[0]
		self._DesignParameter['via12_gate_vbp1']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureY(_ViaMet12Met2NumberOfCOX=ViaNumX, _ViaMet12Met2NumberOfCOY=1)
		tmp=[]
		for i in range(0, len(self._DesignParameter['pmos_vbp1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
			tmp.append([self._DesignParameter['pmos_vbp1']['_XYCoordinates'][0][0]+self._DesignParameter['pmos_vbp1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0], self.getXY('gate_vbp1')[0][1]])
			tmp.append([self._DesignParameter['pmos_vbp1']['_XYCoordinates'][0][0]+self._DesignParameter['pmos_vbp1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0], self.getXY('gate_vbp1')[1][1]])
			tmp.append([self._DesignParameter['pmos_vbp1']['_XYCoordinates'][1][0]+self._DesignParameter['pmos_vbp1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0], self.getXY('gate_vbp1')[0][1]])
			tmp.append([self._DesignParameter['pmos_vbp1']['_XYCoordinates'][1][0]+self._DesignParameter['pmos_vbp1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0], self.getXY('gate_vbp1')[1][1]])

		self._DesignParameter['via12_gate_vbp1']['_XYCoordinates']=tmp
		del tmp

		self._DesignParameter['gate_pdn_single_sw']=self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_Name='gate_pdn_single_swIn{}'.format(_Name)))[0]
		self._DesignParameter['gate_pdn_single_sw']['_DesignObj']._CalculateViaPoly2Met1DesignParameterMinimumEnclosureX(_ViaPoly2Met1NumberOfCOX=1, _ViaPoly2Met1NumberOfCOY=2)

		XCoordinate_single_sw=self._DesignParameter['pmos_vbp2']['_XYCoordinates'][0][0]+self._DesignParameter['pmos_vbp2']['_DesignObj']._DesignParameter['_PPLayer']['_XYCoordinates'][0][0]-self.getXWidth('pmos_vbp2','_PPLayer')/2-(self._DesignParameter['pmos_pdn_single_sw']['_DesignObj']._DesignParameter['_PPLayer']['_XYCoordinates'][-1][0]+self.getXWidth('pmos_pdn_single_sw','_PPLayer')/2)-drc._PpMinSpace
		YCoordinate_gate_sw=self._DesignParameter['gate_vbp2']['_XYCoordinates'][-1][1]-self.getYWidth('gate_vbp2','_POLayer')/2+self.getYWidth('gate_pdn_single_sw','_POLayer')/2

		self._DesignParameter['pmos_pdn_single_sw']['_XYCoordinates']=[[XCoordinate_single_sw, YCoordinate_gate_sw+self.getYWidth('gate_pdn_single_sw','_Met1Layer')/2+self.getYWidth('pmos_pdn_single_sw','_Met1Layer')/2+3*drc._Metal1MinSpace]]
		tmp=[]
		for i in range(0, len(self._DesignParameter['pmos_pdn_single_sw']['_DesignObj']._DesignParameter['_XYCoordinatePMOSSupplyRouting']['_XYCoordinates'])):
			tmp.append([self._DesignParameter['pmos_pdn_single_sw']['_XYCoordinates'][0][0]+self._DesignParameter['pmos_pdn_single_sw']['_DesignObj']._DesignParameter['_XYCoordinatePMOSSupplyRouting']['_XYCoordinates'][i][0], YCoordinate_gate_sw])
		self._DesignParameter['gate_pdn_single_sw']['_XYCoordinates']=tmp
		del tmp

		self._DesignParameter['via12_pdn_single_sw']=self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='via12_pdn_single_swIn{}'.format(_Name)))[0]
		self._DesignParameter['via12_pdn_single_sw']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(_ViaMet12Met2NumberOfCOX=1, _ViaMet12Met2NumberOfCOY=2)
		self._DesignParameter['via12_pdn_single_sw']['_XYCoordinates']=self._DesignParameter['gate_pdn_single_sw']['_XYCoordinates']

		self._DesignParameter['via23_pdn_single_sw']=self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_Name='via23_pdn_single_swIn{}'.format(_Name)))[0]
		self._DesignParameter['via23_pdn_single_sw']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureX(_ViaMet22Met3NumberOfCOX=1, _ViaMet22Met3NumberOfCOY=2)
		self._DesignParameter['via23_pdn_single_sw']['_XYCoordinates']=self._DesignParameter['gate_pdn_single_sw']['_XYCoordinates']

		self._DesignParameter['via34_pdn_single_sw']=self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_Name='via34_pdn_single_swIn{}'.format(_Name)))[0]
		self._DesignParameter['via34_pdn_single_sw']['_DesignObj']._CalculateViaMet32Met4DesignParameterMinimumEnclosureX(_ViaMet32Met4NumberOfCOX=1, _ViaMet32Met4NumberOfCOY=2)
		self._DesignParameter['via34_pdn_single_sw']['_XYCoordinates']=self._DesignParameter['gate_pdn_single_sw']['_XYCoordinates']

		self._DesignParameter['poly_pdn_single_sw_x']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0],_Datatype=DesignParameters._LayerMapping['POLY'][1], _XYCoordinates=[], _Width=None)
		self._DesignParameter['poly_pdn_single_sw_x']['_Width']=self.getYWidth('gate_pdn_single_sw','_POLayer')
		self._DesignParameter['poly_pdn_single_sw_x']['_XYCoordinates']=[[self._DesignParameter['gate_pdn_single_sw']['_XYCoordinates'][0], self._DesignParameter['gate_pdn_single_sw']['_XYCoordinates'][-1]]]

		self._DesignParameter['poly_pdn_single_sw_y']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0],_Datatype=DesignParameters._LayerMapping['POLY'][1], _XYCoordinates=[], _Width=None)
		self._DesignParameter['poly_pdn_single_sw_y']['_Width']=self.getXWidth('pmos_pdn_single_sw','_POLayer')
		tmp=[]
		for i in range(0,len(self._DesignParameter['pmos_pdn_single_sw']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
			tmp.append([[self._DesignParameter['pmos_pdn_single_sw']['_XYCoordinates'][0][0]+self._DesignParameter['pmos_pdn_single_sw']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0], self._DesignParameter['pmos_pdn_single_sw']['_XYCoordinates'][0][1]], \
						[self._DesignParameter['pmos_pdn_single_sw']['_XYCoordinates'][0][0]+self._DesignParameter['pmos_pdn_single_sw']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0], self._DesignParameter['gate_pdn_single_sw']['_XYCoordinates'][0][1]]])
		self._DesignParameter['poly_pdn_single_sw_y']['_XYCoordinates']=tmp

		self._DesignParameter['pmos_vb2']['_XYCoordinates']=[[min(self._DesignParameter['pmos_pdn_single_sw']['_XYCoordinates'][0][0]+self._DesignParameter['pmos_pdn_single_sw']['_DesignObj']._DesignParameter['_PPLayer']['_XYCoordinates'][0][0]-self.getXWidth('pmos_pdn_single_sw','_PPLayer')/2-self.getXWidth('pmos_vb2','_PPLayer')/2-drc._PpMinSpace, self._DesignParameter['pmos_vbp1']['_XYCoordinates'][0][0]+self._DesignParameter['pmos_vbp1']['_DesignObj']._DesignParameter['_PPLayer']['_XYCoordinates'][0][0]-self.getXWidth('pmos_vbp1','_PPLayer')/2-self.getXWidth('pmos_input','_PPLayer')/2-drc._PpMinSpace), self._DesignParameter['pmos_vbp2']['_XYCoordinates'][0][1]]]
		self._DesignParameter['pmos_input']['_XYCoordinates']=[[self.getXY('pmos_vb2')[0][0], self.getXY('pmos_vbp1')[0][1]-self.getYWidth('pmos_vbp1','_POLayer')/2+self.getYWidth('pmos_input','_POLayer')/2], [self.getXY('pmos_vb2')[0][0], self.getXY('pmos_vbp1')[0][1]-self.getYWidth('pmos_vbp1','_POLayer')/2+self.getYWidth('pmos_input','_POLayer')/2+self.getYWidth('pmos_input','_Met1Layer')+19*drc._Metal1MinSpace]]

		self._DesignParameter['pmos_pdn_single_sw']['_XYCoordinates'].append([2*self._DesignParameter['pmos_vb2']['_XYCoordinates'][0][0]-self._DesignParameter['pmos_pdn_single_sw']['_XYCoordinates'][0][0], self._DesignParameter['pmos_pdn_single_sw']['_XYCoordinates'][0][1]])

		self._DesignParameter['gate_1_pdn_single_sw']=self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_Name='gate_1_pdn_single_swIn{}'.format(_Name)))[0]
		self._DesignParameter['gate_1_pdn_single_sw']['_DesignObj']._CalculateViaPoly2Met1DesignParameterMinimumEnclosureX(_ViaPoly2Met1NumberOfCOX=1, _ViaPoly2Met1NumberOfCOY=2)
		tmp=[]
		for i in range(0, len(self._DesignParameter['pmos_pdn_single_sw']['_DesignObj']._DesignParameter['_XYCoordinatePMOSSupplyRouting']['_XYCoordinates'])):
			tmp.append([2*self._DesignParameter['pmos_vb2']['_XYCoordinates'][0][0]-self._DesignParameter['gate_pdn_single_sw']['_XYCoordinates'][i][0], self._DesignParameter['gate_pdn_single_sw']['_XYCoordinates'][0][1]])
		self._DesignParameter['gate_1_pdn_single_sw']['_XYCoordinates']=tmp
		del tmp

		self._DesignParameter['via12_1_pdn_single_sw']=self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='via12_1_pdn_single_swIn{}'.format(_Name)))[0]
		self._DesignParameter['via12_1_pdn_single_sw']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(_ViaMet12Met2NumberOfCOX=1, _ViaMet12Met2NumberOfCOY=2)
		self._DesignParameter['via12_1_pdn_single_sw']['_XYCoordinates']=self._DesignParameter['gate_1_pdn_single_sw']['_XYCoordinates']

		self._DesignParameter['via23_1_pdn_single_sw']=self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_Name='via23_1_pdn_single_swIn{}'.format(_Name)))[0]
		self._DesignParameter['via23_1_pdn_single_sw']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureX(_ViaMet22Met3NumberOfCOX=1, _ViaMet22Met3NumberOfCOY=2)
		self._DesignParameter['via23_1_pdn_single_sw']['_XYCoordinates']=self._DesignParameter['via12_1_pdn_single_sw']['_XYCoordinates']

		self._DesignParameter['via34_1_pdn_single_sw']=self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_Name='via34_1_pdn_single_swIn{}'.format(_Name)))[0]
		self._DesignParameter['via34_1_pdn_single_sw']['_DesignObj']._CalculateViaMet32Met4DesignParameterMinimumEnclosureX(_ViaMet32Met4NumberOfCOX=1, _ViaMet32Met4NumberOfCOY=2)
		self._DesignParameter['via34_1_pdn_single_sw']['_XYCoordinates']=self._DesignParameter['via12_1_pdn_single_sw']['_XYCoordinates']

		self._DesignParameter['poly_1_pdn_single_sw_x']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0],_Datatype=DesignParameters._LayerMapping['POLY'][1], _XYCoordinates=[], _Width=None)
		self._DesignParameter['poly_1_pdn_single_sw_x']['_Width']=self.getYWidth('gate_pdn_single_sw','_POLayer')
		self._DesignParameter['poly_1_pdn_single_sw_x']['_XYCoordinates']=[[self._DesignParameter['gate_1_pdn_single_sw']['_XYCoordinates'][0], self._DesignParameter['gate_1_pdn_single_sw']['_XYCoordinates'][-1]]]

		self._DesignParameter['poly_1_pdn_single_sw_y']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0],_Datatype=DesignParameters._LayerMapping['POLY'][1], _XYCoordinates=[], _Width=None)
		self._DesignParameter['poly_1_pdn_single_sw_y']['_Width']=self.getXWidth('pmos_pdn_single_sw','_POLayer')
		tmp=[]
		for i in range(0,len(self._DesignParameter['pmos_pdn_single_sw']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
			tmp.append([[self._DesignParameter['pmos_pdn_single_sw']['_XYCoordinates'][1][0]+self._DesignParameter['pmos_pdn_single_sw']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0], self._DesignParameter['pmos_pdn_single_sw']['_XYCoordinates'][1][1]], \
						[self._DesignParameter['pmos_pdn_single_sw']['_XYCoordinates'][1][0]+self._DesignParameter['pmos_pdn_single_sw']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0], self._DesignParameter['gate_1_pdn_single_sw']['_XYCoordinates'][0][1]]])
		self._DesignParameter['poly_1_pdn_single_sw_y']['_XYCoordinates']=tmp
		del tmp

		CoNumX=max(1,int(self.getXWidth('pmos_input','_POLayer')/(drc._CoMinWidth+drc._CoMinSpace)-1))
		self._DesignParameter['gate_inputn']=self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_Name='gate_inputnIn{}'.format(_Name)))[0]
		self._DesignParameter['gate_inputn']['_DesignObj']._CalculateViaPoly2Met1DesignParameterMinimumEnclosureX(_ViaPoly2Met1NumberOfCOX=CoNumX, _ViaPoly2Met1NumberOfCOY=1)
		tmp=[]
		for i in range(0,len(self._DesignParameter['pmos_input']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
			tmp.append([self._DesignParameter['pmos_input']['_XYCoordinates'][0][0]+self._DesignParameter['pmos_input']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0],\
						self._DesignParameter['pmos_input']['_XYCoordinates'][0][1]+self.getYWidth('pmos_input','_Met1Layer')/2+self.getYWidth('gate_inputn','_Met1Layer')/2+drc._Metal1MinSpace2])
			tmp.append([self._DesignParameter['pmos_input']['_XYCoordinates'][0][0]+self._DesignParameter['pmos_input']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0],\
						self._DesignParameter['pmos_input']['_XYCoordinates'][0][1]-self.getYWidth('pmos_input','_POLayer')/2])
		self._DesignParameter['gate_inputn']['_XYCoordinates']=tmp
		del tmp

		self._DesignParameter['gate_inputp']=self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_Name='gate_inputpIn{}'.format(_Name)))[0]
		self._DesignParameter['gate_inputp']['_DesignObj']._CalculateViaPoly2Met1DesignParameterMinimumEnclosureX(_ViaPoly2Met1NumberOfCOX=CoNumX, _ViaPoly2Met1NumberOfCOY=1)
		tmp=[]
		for i in range(0,len(self._DesignParameter['pmos_input']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
			tmp.append([self._DesignParameter['pmos_input']['_XYCoordinates'][1][0]+self._DesignParameter['pmos_input']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0],\
						self._DesignParameter['pmos_input']['_XYCoordinates'][1][1]+self.getYWidth('pmos_input','_POLayer')/2])
			tmp.append([self._DesignParameter['pmos_input']['_XYCoordinates'][1][0]+self._DesignParameter['pmos_input']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0],\
						self._DesignParameter['pmos_input']['_XYCoordinates'][1][1]-self.getYWidth('pmos_input','_Met1Layer')/2-self.getYWidth('gate_inputp','_Met1Layer')/2-drc._Metal1MinSpace2])
		self._DesignParameter['gate_inputp']['_XYCoordinates']=tmp
		del tmp

		CoNumX=max(1,int(self.getXWidth('pmos_vb2','_POLayer')/(drc._CoMinWidth+drc._CoMinSpace)-1))
		self._DesignParameter['gate_vb2']=self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_Name='gate_vb2In{}'.format(_Name)))[0]
		self._DesignParameter['gate_vb2']['_DesignObj']._CalculateViaPoly2Met1DesignParameterMinimumEnclosureX(_ViaPoly2Met1NumberOfCOX=CoNumX, _ViaPoly2Met1NumberOfCOY=1)
		tmp=[]
		for i in range(0,len(self._DesignParameter['pmos_vb2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
			tmp.append([self._DesignParameter['pmos_vb2']['_XYCoordinates'][0][0]+self._DesignParameter['pmos_vb2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0],\
						self._DesignParameter['pmos_vb2']['_XYCoordinates'][0][1]+self.getYWidth('pmos_vb2','_Met1Layer')/2+self.getYWidth('gate_vb2','_Met1Layer')/2+drc._Metal1MinSpace2])
			tmp.append([self._DesignParameter['pmos_vb2']['_XYCoordinates'][0][0]+self._DesignParameter['pmos_vb2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0],\
						self._DesignParameter['pmos_vb2']['_XYCoordinates'][0][1]-self.getYWidth('pmos_vb2','_Met1Layer')/2-self.getYWidth('gate_vb2','_Met1Layer')/2-drc._Metal1MinSpace2])
		self._DesignParameter['gate_vb2']['_XYCoordinates']=tmp
		del tmp

		self._DesignParameter['poly_gate_vb2']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0],_Datatype=DesignParameters._LayerMapping['POLY'][1], _XYCoordinates=[], _Width=None)
		self._DesignParameter['poly_gate_vb2']['_Width']=self.getXWidth('pmos_vb2','_POLayer')
		tmp=[]
		for i in range(0, len(self._DesignParameter['pmos_vb2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
			tmp.append([[self._DesignParameter['pmos_vb2']['_XYCoordinates'][0][0]+self._DesignParameter['pmos_vb2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0], self.getXY('gate_vb2')[0][1]+self.getYWidth('gate_vb2','_POLayer')/2], \
						[self._DesignParameter['pmos_vb2']['_XYCoordinates'][0][0]+self._DesignParameter['pmos_vb2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0], self.getXY('gate_vb2')[-1][1]-self.getYWidth('gate_vb2','_POLayer')/2]])
		self._DesignParameter['poly_gate_vb2']['_XYCoordinates']=tmp
		del tmp

		ViaNumX=max(1,int(self.getXWidth('gate_inputn','_Met1Layer')/(drc._VIAxMinWidth+drc._VIAxMinSpace)))
		self._DesignParameter['via12_gate_inputn']=self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='via12_gate_inputnIn{}'.format(_Name)))[0]
		self._DesignParameter['via12_gate_inputn']['_DesignObj']._CalculateDesignParameterSameEnclosure( _ViaMet12Met2NumberOfCOX=ViaNumX, _ViaMet12Met2NumberOfCOY=1)
		tmp=[]
		for i in range(0, len(self._DesignParameter['pmos_input']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
			tmp.append([self._DesignParameter['pmos_input']['_XYCoordinates'][0][0]+self._DesignParameter['pmos_input']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0], self._DesignParameter['gate_inputn']['_XYCoordinates'][0][1]])
			tmp.append([self._DesignParameter['pmos_input']['_XYCoordinates'][0][0]+self._DesignParameter['pmos_input']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0], self._DesignParameter['gate_inputn']['_XYCoordinates'][-1][1]])
		self._DesignParameter['via12_gate_inputn']['_XYCoordinates']=tmp
		del tmp

		self._DesignParameter['via12_gate_inputp']=self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='via12_gate_inputpIn{}'.format(_Name)))[0]
		self._DesignParameter['via12_gate_inputp']['_DesignObj']._CalculateDesignParameterSameEnclosure( _ViaMet12Met2NumberOfCOX=ViaNumX, _ViaMet12Met2NumberOfCOY=1)
		tmp=[]
		for i in range(0, len(self._DesignParameter['pmos_input']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
			tmp.append([self._DesignParameter['pmos_input']['_XYCoordinates'][1][0]+self._DesignParameter['pmos_input']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0], self._DesignParameter['gate_inputp']['_XYCoordinates'][0][1]])
			tmp.append([self._DesignParameter['pmos_input']['_XYCoordinates'][1][0]+self._DesignParameter['pmos_input']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0], self._DesignParameter['gate_inputp']['_XYCoordinates'][-1][1]])
		self._DesignParameter['via12_gate_inputp']['_XYCoordinates']=tmp
		del tmp

		self._DesignParameter['m2_gate_inputn']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0],_Datatype=DesignParameters._LayerMapping['METAL2'][1], _XYCoordinates=[], _Width=None)
		self._DesignParameter['m2_gate_inputn']['_Width']=self._DesignParameter['via12_gate_inputn']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth']
		self._DesignParameter['m2_gate_inputn']['_XYCoordinates']=[[self._DesignParameter['via12_gate_inputn']['_XYCoordinates'][0], self._DesignParameter['via12_gate_inputn']['_XYCoordinates'][-2]], \
																   [self._DesignParameter['via12_gate_inputn']['_XYCoordinates'][1], self._DesignParameter['via12_gate_inputn']['_XYCoordinates'][-1]]]


		self._DesignParameter['m2_gate_inputp']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0],_Datatype=DesignParameters._LayerMapping['METAL2'][1], _XYCoordinates=[], _Width=None)
		self._DesignParameter['m2_gate_inputp']['_Width']=self._DesignParameter['via12_gate_inputp']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth']
		self._DesignParameter['m2_gate_inputp']['_XYCoordinates']=[[self._DesignParameter['via12_gate_inputp']['_XYCoordinates'][0], self._DesignParameter['via12_gate_inputp']['_XYCoordinates'][-2]], \
																   [self._DesignParameter['via12_gate_inputp']['_XYCoordinates'][1], self._DesignParameter['via12_gate_inputp']['_XYCoordinates'][-1]]]

		self._DesignParameter['via12_drain_inputn']=self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='via12_drain_inputnIn{}'.format(_Name)))[0]
		self._DesignParameter['via12_drain_inputn']['_DesignObj']._CalculateDesignParameterSameEnclosure( _ViaMet12Met2NumberOfCOX=1, _ViaMet12Met2NumberOfCOY=2)
		tmp=[]
		for i in range(0, len(self._DesignParameter['pmos_input']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'])):
			tmp.append([self._DesignParameter['pmos_input']['_XYCoordinates'][0][0]+self._DesignParameter['pmos_input']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][i][0], self._DesignParameter['pmos_input']['_XYCoordinates'][0][1]])
			tmp.append([self._DesignParameter['pmos_input']['_XYCoordinates'][0][0]+self._DesignParameter['pmos_input']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][i][0], self._DesignParameter['pmos_input']['_XYCoordinates'][0][1]])
		self._DesignParameter['via12_drain_inputn']['_XYCoordinates']=tmp
		del tmp

		self._DesignParameter['via12_drain_inputp']=self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='via12_drain_inputpIn{}'.format(_Name)))[0]
		self._DesignParameter['via12_drain_inputp']['_DesignObj']._CalculateDesignParameterSameEnclosure( _ViaMet12Met2NumberOfCOX=1, _ViaMet12Met2NumberOfCOY=2)
		tmp=[]
		for i in range(0, len(self._DesignParameter['pmos_input']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'])):
			tmp.append([self._DesignParameter['pmos_input']['_XYCoordinates'][1][0]+self._DesignParameter['pmos_input']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][i][0], self._DesignParameter['pmos_input']['_XYCoordinates'][1][1]])
			tmp.append([self._DesignParameter['pmos_input']['_XYCoordinates'][1][0]+self._DesignParameter['pmos_input']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][i][0], self._DesignParameter['pmos_input']['_XYCoordinates'][1][1]])
		self._DesignParameter['via12_drain_inputp']['_XYCoordinates']=tmp
		del tmp

		self._DesignParameter['m2_drain_input']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0],_Datatype=DesignParameters._LayerMapping['METAL2'][1], _XYCoordinates=[], _Width=None)
		self._DesignParameter['m2_drain_input']['_Width']=self._DesignParameter['via12_drain_inputn']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth']
		self._DesignParameter['m2_drain_input']['_XYCoordinates']=[[[self._DesignParameter['via12_drain_inputn']['_XYCoordinates'][0][0], self._DesignParameter['via12_drain_inputn']['_XYCoordinates'][0][1]], [self._DesignParameter['pmos_input']['_XYCoordinates'][0][0]+self._DesignParameter['pmos_input']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][-1][0], self._DesignParameter['via12_drain_inputn']['_XYCoordinates'][-1][1]]], \
																   [[self._DesignParameter['via12_drain_inputp']['_XYCoordinates'][0][0], self._DesignParameter['via12_drain_inputp']['_XYCoordinates'][0][1]], [self._DesignParameter['pmos_input']['_XYCoordinates'][0][0]+self._DesignParameter['pmos_input']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][-1][0], self._DesignParameter['via12_drain_inputp']['_XYCoordinates'][-1][1]]]]

		self._DesignParameter['poly_gate_input']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0],_Datatype=DesignParameters._LayerMapping['POLY'][1], _XYCoordinates=[], _Width=None)
		self._DesignParameter['poly_gate_input']['_Width']=self.getXWidth('pmos_input','_POLayer')
		tmp=[]
		for i in range(0,len(self._DesignParameter['pmos_input']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
			tmp.append([[self._DesignParameter['pmos_input']['_XYCoordinates'][0][0]+self._DesignParameter['pmos_input']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0], self._DesignParameter['gate_inputn']['_XYCoordinates'][1][1]-self.getYWidth('gate_inputn','_POLayer')/2],\
						[self._DesignParameter['pmos_input']['_XYCoordinates'][0][0]+self._DesignParameter['pmos_input']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0], self._DesignParameter['gate_inputn']['_XYCoordinates'][0][1]+self.getYWidth('gate_inputn','_POLayer')/2]])
			tmp.append([[self._DesignParameter['pmos_input']['_XYCoordinates'][1][0]+self._DesignParameter['pmos_input']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0], self._DesignParameter['gate_inputp']['_XYCoordinates'][0][1]+self.getYWidth('gate_inputp','_POLayer')/2],\
						[self._DesignParameter['pmos_input']['_XYCoordinates'][1][0]+self._DesignParameter['pmos_input']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0], self._DesignParameter['gate_inputp']['_XYCoordinates'][1][1]-self.getYWidth('gate_inputp','_POLayer')/2]])
		self._DesignParameter['poly_gate_input']['_XYCoordinates']=tmp
		del tmp

		self._DesignParameter['poly_vb2']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0],_Datatype=DesignParameters._LayerMapping['POLY'][1], _XYCoordinates=[], _Width=None)
		self._DesignParameter['poly_vb2']['_Width']=self.getXWidth('pmos_vb2','_POLayer')
		tmp=[]
		for i in range(0,len(self._DesignParameter['pmos_vb2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
			tmp.append([[self._DesignParameter['pmos_vb2']['_XYCoordinates'][0][0]+self._DesignParameter['pmos_vb2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0], self._DesignParameter['pmos_vb2']['_XYCoordinates'][0][1]+self.getYWidth('pmos_vb2','_POLayer')/2+self.getYWidth('gate_vb2','_POLayer')/2],\
						[self._DesignParameter['pmos_vb2']['_XYCoordinates'][0][0]+self._DesignParameter['pmos_vb2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0], self._DesignParameter['pmos_vb2']['_XYCoordinates'][0][1]-self.getYWidth('pmos_vb2','_POLayer')/2-self.getYWidth('gate_vb2','_POLayer')/2]])
		self._DesignParameter['poly_vb2']['_XYCoordinates']=tmp
		del tmp

		self._DesignParameter['pplayer_y']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['PIMP'][0],_Datatype=DesignParameters._LayerMapping['PIMP'][1], _XYCoordinates=[], _Width=None)
		self._DesignParameter['pplayer_y']['_Width']=min(self._DesignParameter['pmos_vb2']['_XYCoordinates'][0][0]+self.getXWidth('pmos_vb2','_PPLayer')/2,self._DesignParameter['pmos_input']['_XYCoordinates'][0][0]+self.getXWidth('pmos_input','_PPLayer')/2)-min(self._DesignParameter['pmos_pdn_single_sw']['_XYCoordinates'][1][0]-self.getXWidth('pmos_pdn_single_sw','_PPLayer')/2,self._DesignParameter['pmos_input']['_XYCoordinates'][0][0]-self.getXWidth('pmos_input','_PPLayer')/2)
		self._DesignParameter['pplayer_y']['_XYCoordinates']=[[[(min(self._DesignParameter['pmos_vb2']['_XYCoordinates'][0][0]+self.getXWidth('pmos_vb2','_PPLayer')/2,self._DesignParameter['pmos_input']['_XYCoordinates'][0][0]+self.getXWidth('pmos_input','_PPLayer')/2)+min(self._DesignParameter['pmos_pdn_single_sw']['_XYCoordinates'][1][0]-self.getXWidth('pmos_pdn_single_sw','_PPLayer')/2,self._DesignParameter['pmos_input']['_XYCoordinates'][0][0]-self.getXWidth('pmos_input','_PPLayer')/2))/2, self._DesignParameter['pmos_input']['_XYCoordinates'][1][1]+self.getYWidth('pmos_input','_PPLayer')/2],\
															  [(min(self._DesignParameter['pmos_vb2']['_XYCoordinates'][0][0]+self.getXWidth('pmos_vb2','_PPLayer')/2,self._DesignParameter['pmos_input']['_XYCoordinates'][0][0]+self.getXWidth('pmos_input','_PPLayer')/2)+min(self._DesignParameter['pmos_pdn_single_sw']['_XYCoordinates'][1][0]-self.getXWidth('pmos_pdn_single_sw','_PPLayer')/2,self._DesignParameter['pmos_input']['_XYCoordinates'][0][0]-self.getXWidth('pmos_input','_PPLayer')/2))/2, self._DesignParameter['pmos_vb2']['_XYCoordinates'][0][1]-self.getYWidth('pmos_vb2','_PPLayer')/2]]]

		self._DesignParameter['pplayer_x']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['PIMP'][0],_Datatype=DesignParameters._LayerMapping['PIMP'][1], _XYCoordinates=[], _Width=None)
		self._DesignParameter['pplayer_x']['_Width']=self._DesignParameter['pmos_vbp1']['_XYCoordinates'][0][1]+self.getYWidth('pmos_vbp1','_PPLayer')/2-min(self._DesignParameter['pmos_vbp2']['_XYCoordinates'][0][1]-self.getYWidth('pmos_vbp2','_PPLayer')/2, self._DesignParameter['pmos_pdn_single_sw']['_XYCoordinates'][0][1]-self.getYWidth('pmos_pdn_single_sw','_PPLayer')/2)
		self._DesignParameter['pplayer_x']['_XYCoordinates']=[[[min(self._DesignParameter['pmos_input']['_XYCoordinates'][0][0]-self.getXWidth('pmos_input','_PPLayer')/2, self._DesignParameter['pmos_pdn_single_sw']['_XYCoordinates'][1][0]-self.getXWidth('pmos_pdn_single_sw','_PPLayer')/2), (self._DesignParameter['pmos_vbp1']['_XYCoordinates'][0][1]+self.getYWidth('pmos_vbp1','_PPLayer')/2+min(self._DesignParameter['pmos_vbp2']['_XYCoordinates'][0][1]-self.getYWidth('pmos_vbp2','_PPLayer')/2, self._DesignParameter['pmos_pdn_single_sw']['_XYCoordinates'][0][1]-self.getYWidth('pmos_pdn_single_sw','_PPLayer')/2))/2],\
															  [max(self._DesignParameter['pmos_vbp2']['_XYCoordinates'][1][0]+self.getXWidth('pmos_vbp2','_PPLayer')/2, self._DesignParameter['pmos_vbp1']['_XYCoordinates'][1][0]+self.getXWidth('pmos_vbp1','_PPLayer')/2,self._DesignParameter['pmos_pdn_pair_sw']['_XYCoordinates'][1][0]+self.getXWidth('pmos_pdn_pair_sw','_PPLayer')/2), (self._DesignParameter['pmos_vbp1']['_XYCoordinates'][0][1]+self.getYWidth('pmos_vbp1','_PPLayer')/2+min(self._DesignParameter['pmos_vbp2']['_XYCoordinates'][0][1]-self.getYWidth('pmos_vbp2','_PPLayer')/2, self._DesignParameter['pmos_pdn_single_sw']['_XYCoordinates'][0][1]-self.getYWidth('pmos_pdn_single_sw','_PPLayer')/2))/2]]]

		self._DesignParameter['nguardring1']=self._SrefElementDeclaration(_DesignObj=NSubRing.NSubRing(_Name='nguardring1In{}'.format(_Name)))[0]
		self._DesignParameter['nguardring1']['_DesignObj']._CalculateDesignParameter(height=5000,width=3000,contact_bottom=pset_param['pmos_guardring_co_top'],contact_top=pset_param['pmos_guardring_co_top'],contact_left=pset_param['pmos_guardring_co_left'],contact_right=pset_param['pmos_guardring_co_top'])
		if pset_param['pmos_guardring_height1'] != None :
			nguardring_yheight1=pset_param['pmos_guardring_height1']
		elif pset_param['pmos_guardring_height1'] == None :
			nguardring_yheight1=(self._DesignParameter['gate_inputp']['_XYCoordinates'][0][1]+self.getYWidth('gate_inputp','_Met1Layer')/2+self.getYWidth('nguardring1','top','_Met1Layer')/2+drc._Metal1MinSpace3)-(self._DesignParameter['gate_vbp1']['_XYCoordinates'][0][1]+self.getYWidth('gate_vbp1','_Met1Layer')/2+self.getYWidth('nguardring1','top','_Met1Layer')/2+drc._Metal1MinSpace3)
		if pset_param['pmos_guardring_width1'] != None :
			nguardring_xwidth1=pset_param['pmos_guardring_width1']
		elif pset_param['pmos_guardring_width1'] == None :
			nguardring_xwidth1=max(self._DesignParameter['pmos_pdn_single_sw']['_XYCoordinates'][0][0]+self._DesignParameter['pmos_pdn_single_sw']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][-1][0]+self.getXWidth('pmos_pdn_single_sw','_Met1Layer')/2+self.getYWidth('nguardring1','top','_Met1Layer')/2+drc._Metal1MinSpace3, self._DesignParameter['pmos_input']['_XYCoordinates'][0][0]+self._DesignParameter['pmos_input']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][-1][0]+self.getXWidth('pmos_input','_Met1Layer')/2+self.getYWidth('nguardring1','top','_Met1Layer')/2+drc._Metal1MinSpace3)\
							   -min(self._DesignParameter['pmos_pdn_single_sw']['_XYCoordinates'][1][0]+self._DesignParameter['pmos_pdn_single_sw']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0]-self.getXWidth('pmos_pdn_single_sw','_Met1Layer')/2-self.getYWidth('nguardring1','top','_Met1Layer')/2-drc._Metal1MinSpace3,self._DesignParameter['pmos_input']['_XYCoordinates'][1][0]+self._DesignParameter['pmos_input']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0]-self.getXWidth('pmos_input','_Met1Layer')/2-self.getYWidth('nguardring1','top','_Met1Layer')/2-drc._Metal1MinSpace3)
		self._DesignParameter['nguardring1']['_DesignObj']._CalculateDesignParameter(height=nguardring_yheight1,width=nguardring_xwidth1,contact_bottom=pset_param['pmos_guardring_co_top'],contact_top=pset_param['pmos_guardring_co_top'],contact_left=pset_param['pmos_guardring_co_left'],contact_right=pset_param['pmos_guardring_co_top'])

		self._DesignParameter['nguardring1']['_XYCoordinates']=[[self._DesignParameter['pmos_input']['_XYCoordinates'][1][0], ((self._DesignParameter['gate_inputp']['_XYCoordinates'][0][1]+self.getYWidth('gate_inputp','_Met1Layer')/2+self.getYWidth('nguardring1','top','_Met1Layer')/2+drc._Metal1MinSpace3)+(self._DesignParameter['gate_vbp1']['_XYCoordinates'][0][1]+self.getYWidth('gate_vbp1','_Met1Layer')/2+self.getYWidth('nguardring1','top','_Met1Layer')/2+drc._Metal1MinSpace3))/2]]

		self._DesignParameter['nguardring2']=self._SrefElementDeclaration(_DesignObj=NSubRing.NSubRing(_Name='nguardring2In{}'.format(_Name)))[0]
		self._DesignParameter['nguardring2']['_DesignObj']._CalculateDesignParameter(height=5000,width=3000,contact_bottom=pset_param['pmos_guardring_co_bot'],contact_top=pset_param['pmos_guardring_co_top'],contact_left=pset_param['pmos_guardring_co_left'],contact_right=pset_param['pmos_guardring_co_top'])
		if pset_param['pmos_guardring_height2'] != None :
			nguardring_yheight2=pset_param['pmos_guardring_height2']
		elif pset_param['pmos_guardring_height2'] == None :
			nguardring_yheight2=(self._DesignParameter['gate_vbp1']['_XYCoordinates'][0][1]+self.getYWidth('gate_vbp1','_Met1Layer')/2+self.getYWidth('nguardring2','top','_Met1Layer')/2+drc._Metal1MinSpace3)-min(self._DesignParameter['gate_vbp2']['_XYCoordinates'][-1][1]-self.getYWidth('gate_vbp2','_Met1Layer')/2-self.getYWidth('nguardring2','bot','_Met1Layer')/2-drc._Metal1MinSpace3,self._DesignParameter['via12_pdn_single_sw']['_XYCoordinates'][0][1]-self.getYWidth('via12_pdn_single_sw','_Met1Layer')/2-self.getYWidth('nguardring2','bot','_Met1Layer')/2-drc._Metal1MinSpace3,self._DesignParameter['gate_vb2']['_XYCoordinates'][-1][1]-self.getYWidth('gate_vb2','_Met1Layer')/2-self.getYWidth('nguardring2','bot','_Met1Layer')/2-drc._Metal1MinSpace3)
		if pset_param['pmos_guardring_width2'] != None :
			nguardring_xwidth2=pset_param['pmos_guardring_width2']
		elif pset_param['pmos_guardring_width2'] == None :
			nguardring_xwidth2=max(self._DesignParameter['pmos_vbp1']['_XYCoordinates'][1][0]+self._DesignParameter['pmos_vbp1']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][-1][0]+self.getXWidth('pmos_vbp1','_Met1Layer')/2+self.getXWidth('nguardring2','right','_Met1Layer')/2+drc._Metal1MinSpace3, self._DesignParameter['pmos_vbp2']['_XYCoordinates'][1][0]+self._DesignParameter['pmos_vbp2']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][-1][0]+self.getXWidth('pmos_vbp2','_Met1Layer')/2+self.getXWidth('nguardring2','right','_Met1Layer')/2+drc._Metal1MinSpace3, self._DesignParameter['pmos_pdn_pair_sw']['_XYCoordinates'][1][0]+self._DesignParameter['pmos_pdn_pair_sw']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][-1][0]+self.getXWidth('pmos_pdn_pair_sw','_Met1Layer')/2+self.getXWidth('nguardring2','right','_Met1Layer')/2+drc._Metal1MinSpace3)\
							   -min(self._DesignParameter['pmos_pdn_single_sw']['_XYCoordinates'][1][0]+self._DesignParameter['pmos_pdn_single_sw']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0]-self.getXWidth('pmos_pdn_single_sw','_Met1Layer')/2-self.getXWidth('nguardring2','left','_Met1Layer')/2-drc._Metal1MinSpace3,self._DesignParameter['pmos_input']['_XYCoordinates'][0][0]+self._DesignParameter['pmos_input']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0]-self.getXWidth('pmos_input','_Met1Layer')/2-self.getXWidth('nguardring2','left','_Met1Layer')/2-drc._Metal1MinSpace3)
		self._DesignParameter['nguardring2']['_DesignObj']._CalculateDesignParameter(height=nguardring_yheight2,width=nguardring_xwidth2,contact_bottom=pset_param['pmos_guardring_co_bot'],contact_top=pset_param['pmos_guardring_co_top'],contact_left=pset_param['pmos_guardring_co_left'],contact_right=pset_param['pmos_guardring_co_right'])

		self._DesignParameter['nguardring2']['_XYCoordinates']=[[(max(self._DesignParameter['pmos_vbp1']['_XYCoordinates'][1][0]+self._DesignParameter['pmos_vbp1']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][-1][0]+self.getXWidth('pmos_vbp1','_Met1Layer')/2+self.getXWidth('nguardring2','right','_Met1Layer')/2+drc._Metal1MinSpace3, self._DesignParameter['pmos_vbp2']['_XYCoordinates'][1][0]+self._DesignParameter['pmos_vbp2']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][-1][0]+self.getXWidth('pmos_vbp2','_Met1Layer')/2+self.getXWidth('nguardring2','right','_Met1Layer')/2+drc._Metal1MinSpace3, self._DesignParameter['pmos_pdn_pair_sw']['_XYCoordinates'][1][0]+self._DesignParameter['pmos_pdn_pair_sw']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][-1][0]+self.getXWidth('pmos_pdn_pair_sw','_Met1Layer')/2+self.getXWidth('nguardring2','right','_Met1Layer')/2+drc._Metal1MinSpace3)\
																 +min(self._DesignParameter['pmos_pdn_single_sw']['_XYCoordinates'][1][0]+self._DesignParameter['pmos_pdn_single_sw']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0]-self.getXWidth('pmos_pdn_single_sw','_Met1Layer')/2-self.getXWidth('nguardring2','left','_Met1Layer')/2-drc._Metal1MinSpace3,self._DesignParameter['pmos_input']['_XYCoordinates'][0][0]+self._DesignParameter['pmos_input']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0]-self.getXWidth('pmos_input','_Met1Layer')/2-self.getXWidth('nguardring2','left','_Met1Layer')/2-drc._Metal1MinSpace3))/2, \
																 ((self._DesignParameter['gate_vbp1']['_XYCoordinates'][0][1]+self.getYWidth('gate_vbp1','_Met1Layer')/2+self.getYWidth('nguardring2','top','_Met1Layer')/2+drc._Metal1MinSpace3)+min(self._DesignParameter['gate_vbp2']['_XYCoordinates'][-1][1]-self.getYWidth('gate_vbp2','_Met1Layer')/2-self.getYWidth('nguardring2','bot','_Met1Layer')/2-drc._Metal1MinSpace3,self._DesignParameter['via12_pdn_single_sw']['_XYCoordinates'][0][1]-self.getYWidth('via12_pdn_single_sw','_Met1Layer')/2-self.getYWidth('nguardring2','bot','_Met1Layer')/2-drc._Metal1MinSpace3,self._DesignParameter['gate_vb2']['_XYCoordinates'][-1][1]-self.getYWidth('gate_vb2','_Met1Layer')/2-self.getYWidth('nguardring2','bot','_Met1Layer')/2-drc._Metal1MinSpace3))/2]]


		if self.getXWidth('pmos_pdn_pair_sw','_PODummyLayer')*self.getYWidth('pmos_pdn_pair_sw','_PODummyLayer'):
			self._DesignParameter['pmos_pdn_pair_sw']['_DesignObj']._DesignParameter['_PODummyLayer']['_YWidth']=int(drc._PODummyMinArea//self.getXWidth('pmos_pdn_pair_sw','_PODummyLayer'))+2*MinSnapSpacing


		#### Nset Generation ####
		self._DesignParameter['nmos_pdn_sw']=self._SrefElementDeclaration(_DesignObj=NMOSWithDummy._NMOS(_Name='nmos_pdn_pair_swIn{}'.format(_Name)))[0]
		self._DesignParameter['nmos_pdn_sw']['_DesignObj']._CalculateNMOSDesignParameter(**dict(**nset_param['nmos_pdn_sw_param']))

		self._DesignParameter['nmos_vb1']=self._SrefElementDeclaration(_DesignObj=NMOSWithDummy._NMOS(_Name='nmos_vb1In{}'.format(_Name)))[0]
		self._DesignParameter['nmos_vb1']['_DesignObj']._CalculateNMOSDesignParameter(**dict(**nset_param['nmos_current_single_param']))

		self._DesignParameter['nmos_vbn1']=self._SrefElementDeclaration(_DesignObj=NMOSWithDummy._NMOS(_Name='nmos_vbn1In{}'.format(_Name)))[0]
		self._DesignParameter['nmos_vbn1']['_DesignObj']._CalculateNMOSDesignParameter(**dict(**nset_param['nmos_current_pair1_param']))

		self._DesignParameter['nmos_input']=self._SrefElementDeclaration(_DesignObj=NMOSWithDummy._NMOS(_Name='nmos_inputIn{}'.format(_Name)))[0]
		self._DesignParameter['nmos_input']['_DesignObj']._CalculateNMOSDesignParameter(**dict(**nset_param['nmos_input_param']))

		self._DesignParameter['nmos_n0']=self._SrefElementDeclaration(_DesignObj=NMOSWithDummy._NMOS(_Name='nmos_n0In{}'.format(_Name)))[0]
		self._DesignParameter['nmos_n0']['_DesignObj']._CalculateNMOSDesignParameter(**dict(**nset_param['nmos_current_pair2_param']))

		self._DesignParameter['pguardring1']=self._SrefElementDeclaration(_DesignObj=PSubRing.PSubRing(_Name='pguardring1In{}'.format(_Name)))[0]
		self._DesignParameter['pguardring1']['_DesignObj']._CalculateDesignParameter(height=5000,width=3000,contact_bottom=nset_param['nmos_guardring_co_top'],contact_top=nset_param['nmos_guardring_co_top'],contact_left=nset_param['nmos_guardring_co_left'],contact_right=nset_param['nmos_guardring_co_top'])

		self._DesignParameter['pguardring2']=self._SrefElementDeclaration(_DesignObj=PSubRing.PSubRing(_Name='pguardring2In{}'.format(_Name)))[0]
		self._DesignParameter['pguardring2']['_DesignObj']._CalculateDesignParameter(height=5000,width=3000,contact_bottom=nset_param['nmos_guardring_co_bot'],contact_top=nset_param['nmos_guardring_co_bot'],contact_left=nset_param['nmos_guardring_co_bot'],contact_right=nset_param['nmos_guardring_co_right'])

		self._DesignParameter['gate_ninputn']=self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_Name='gate_ninputnIn{}'.format(_Name)))[0]
		CoNumX=max(1,int(self.getXWidth('nmos_input','_POLayer')/(drc._CoMinWidth+drc._CoMinSpace)-1))
		self._DesignParameter['gate_ninputn']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(_ViaPoly2Met1NumberOfCOX=CoNumX, _ViaPoly2Met1NumberOfCOY=1)
		self._DesignParameter['gate_ninputp']=self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_Name='gate_ninputpIn{}'.format(_Name)))[0]
		CoNumX=max(1,int(self.getXWidth('nmos_input','_POLayer')/(drc._CoMinWidth+drc._CoMinSpace)-1))
		self._DesignParameter['gate_ninputp']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(_ViaPoly2Met1NumberOfCOX=CoNumX, _ViaPoly2Met1NumberOfCOY=1)
		self._DesignParameter['gate_vbn1']=self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_Name='gate_vbn1In{}'.format(_Name)))[0]
		CoNumX=max(1,int(self.getXWidth('nmos_vbn1','_POLayer')/(drc._CoMinWidth+drc._CoMinSpace)-1))
		self._DesignParameter['gate_vbn1']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(_ViaPoly2Met1NumberOfCOX=CoNumX, _ViaPoly2Met1NumberOfCOY=1)
		self._DesignParameter['gate_vb1']=self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_Name='gate_vb1In{}'.format(_Name)))[0]
		CoNumX=max(1,int(self.getXWidth('nmos_vb1','_POLayer')/(drc._CoMinWidth+drc._CoMinSpace)-1))
		self._DesignParameter['gate_vb1']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(_ViaPoly2Met1NumberOfCOX=CoNumX, _ViaPoly2Met1NumberOfCOY=1)
		self._DesignParameter['gate_n0']=self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_Name='gate_n0In{}'.format(_Name)))[0]
		CoNumX=max(1,int(self.getXWidth('nmos_n0','_POLayer')/(drc._CoMinWidth+drc._CoMinSpace)-1))
		self._DesignParameter['gate_n0']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(_ViaPoly2Met1NumberOfCOX=CoNumX, _ViaPoly2Met1NumberOfCOY=1)

		self._DesignParameter['nmos_input']['_XYCoordinates']=[[self.getXY('pmos_input')[0][0], self.getXY('nguardring1','top')[0][1]+self.getYWidth('nguardring1','top','_Met1Layer')/2+self.getYWidth('pguardring1','bot','_Met1Layer')+drc._Metal1MinSpace3*2+self.getYWidth('nmos_input','_POLayer')/2+self.getYWidth('gate_ninputn','_Met1Layer')/2], [self.getXY('pmos_input')[0][0], self.getXY('nguardring1','top')[0][1]+self.getYWidth('nguardring1','top','_Met1Layer')*3/2+drc._Metal1MinSpace3*2+self.getYWidth('nmos_input','_POLayer')/2+self.getYWidth('gate_ninputn','_Met1Layer')/2+self.getYWidth('nmos_input','_Met1Layer')+19*drc._Metal1MinSpace]]
		self._DesignParameter['nmos_vb1']['_XYCoordinates']=[[self.getXY('nmos_input')[0][0], self.getXY('nmos_input')[1][1]+self.getYWidth('nmos_input','_Met1Layer')/2+self.getYWidth('nmos_vb1','_Met1Layer')/2+19*drc._Metal1MinSpace]]

		_Lengthbtwmet1=self._DesignParameter['nmos_vbn1']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][1][0]-self._DesignParameter['nmos_vbn1']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0]
		self._DesignParameter['nmos_vbn1']['_XYCoordinates']=[[_OriginXY[0][0]-_Lengthbtwmet1*(len(self._DesignParameter['nmos_vbn1']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'])-1)/2-drc._Metal1MinSpace*5.2, self.getXY('nguardring2','top')[0][1]+self.getYWidth('nguardring2','top','_ODLayer')/2+self.getYWidth('pguardring2','bot','_ODLayer')+drc._Metal1MinSpace3*2+self.getYWidth('nmos_vbn1','_POLayer')/2+self.getYWidth('gate_vbn1','_Met1Layer')/2], [_OriginXY[0][0]+_Lengthbtwmet1*(len(self._DesignParameter['nmos_vbn1']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'])-1)/2+drc._Metal1MinSpace*5.2, self.getXY('nguardring2','top')[0][1]+self.getYWidth('nguardring2','top','_ODLayer')/2+self.getYWidth('pguardring2','bot','_ODLayer')+drc._Metal1MinSpace3*2+self.getYWidth('nmos_vbn1','_POLayer')/2+self.getYWidth('gate_vbn1','_Met1Layer')/2]]
		self._DesignParameter['nmos_n0']['_XYCoordinates']=[[self._DesignParameter['nmos_vbn1']['_XYCoordinates'][0][0], self.getXY('nmos_vbn1')[0][1]+self.getYWidth('nmos_vbn1','_Met1Layer')/2+self.getYWidth('nmos_n0','_Met1Layer')/2+19*drc._Metal1MinSpace], [self._DesignParameter['nmos_vbn1']['_XYCoordinates'][1][0], self.getXY('nmos_vbn1')[0][1]+self.getYWidth('nmos_vbn1','_Met1Layer')/2+self.getYWidth('nmos_n0','_Met1Layer')/2+19*drc._Metal1MinSpace]]


		if (DesignParameters._Technology == 'SS28nm') and nset_param['nmos_pdn_sw_param']['_XVT'] in ('SLVT', 'LVT', 'RVT', 'HVT'):
			_nmos_pdn_sw_XVTLayer = '_' + nset_param['nmos_pdn_sw_param']['_XVT'] + 'Layer'
			_XVTLayerMappingName = nset_param['nmos_pdn_sw_param']['_XVT']
		elif (DesignParameters._Technology in ('TSMC65nm', 'SS65nm')) and nset_param['nmos_pdn_sw_param']['_XVT'] in ('LVT', 'HVT'):
			_nmos_pdn_sw_XVTLayer = '_N' + nset_param['nmos_pdn_sw_param']['_XVT'] + 'Layer'
			_XVTLayerMappingName = 'N' + nset_param['nmos_pdn_sw_param']['_XVT']
		elif (DesignParameters._Technology in ('TSMC65nm', 'SS65nm')) and (nset_param['nmos_pdn_sw_param']['_XVT'] == None):
			_nmos_pdn_sw_XVTLayer = None
			_XVTLayerMappingName = None

		elif DesignParameters._Technology in ('SS28nm', 'SS65nm', 'TSMC65nm'):
			raise NotImplementedError(f"Invalid '_XVT' argument({nset_param['nmos_pdn_sw_param']['_XVT']}) for {DesignParameters._Technology}")
		else:
			raise NotImplementedError(f"Not Yet Implemented in other technology : {DesignParameters._Technology}")


		if (DesignParameters._Technology == 'SS28nm') and nset_param['nmos_current_pair1_param']['_XVT'] in ('SLVT', 'LVT', 'RVT', 'HVT'):
			_nmos_vbn1_XVTLayer = '_' + nset_param['nmos_current_pair1_param']['_XVT'] + 'Layer'
			_XVTLayerMappingName = nset_param['nmos_current_pair1_param']['_XVT']
		elif (DesignParameters._Technology in ('TSMC65nm', 'SS65nm')) and nset_param['nmos_current_pair1_param']['_XVT'] in ('LVT', 'HVT'):
			_nmos_vbn1_XVTLayer = '_N' + nset_param['nmos_current_pair1_param']['_XVT'] + 'Layer'
			_XVTLayerMappingName = 'N' + nset_param['nmos_current_pair1_param']['_XVT']
		elif (DesignParameters._Technology in ('TSMC65nm', 'SS65nm')) and (nset_param['nmos_current_pair1_param']['_XVT'] == None):
			_nmos_vbn1_XVTLayer = None
			_XVTLayerMappingName = None

		elif DesignParameters._Technology in ('SS28nm', 'SS65nm', 'TSMC65nm'):
			raise NotImplementedError(f"Invalid '_XVT' argument({nset_param['nmos_current_pair1_param']['_XVT']}) for {DesignParameters._Technology}")
		else:
			raise NotImplementedError(f"Not Yet Implemented in other technology : {DesignParameters._Technology}")

		self._DesignParameter['nmos_pdn_sw']['_XYCoordinates']=[[min(self.getXY('nmos_vbn1','_Met1Layer')[0][0]-self._DesignParameter['nmos_pdn_sw']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][-1][0]-self._DesignParameter['nmos_pdn_sw']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']-drc._Metal1MinSpace3, self.getXY('nmos_vbn1')[0][0]-self.getXWidth('nmos_vbn1',_nmos_vbn1_XVTLayer)/2-self.getXWidth('nmos_pdn_sw',_nmos_pdn_sw_XVTLayer)/2-drc._XvtMinSpace), self._DesignParameter['nmos_vbn1']['_XYCoordinates'][0][1]]]


		tmp=[]
		for i in range(0, len(self._DesignParameter['nmos_vbn1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
			tmp.append([self.getXY('nmos_vbn1')[0][0]+self._DesignParameter['nmos_vbn1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0], self.getXY('nmos_vbn1')[0][1]+self.getYWidth('nmos_vbn1','_Met1Layer')/2+self.getYWidth('gate_vbn1','_Met1Layer')/2+drc._Metal1MinSpace2])
			tmp.append([self.getXY('nmos_vbn1')[0][0]+self._DesignParameter['nmos_vbn1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0], self.getXY('nmos_vbn1')[0][1]-self.getYWidth('nmos_vbn1','_Met1Layer')/2-self.getYWidth('gate_vbn1','_Met1Layer')/2-drc._Metal1MinSpace2])
			tmp.append([self.getXY('nmos_vbn1')[1][0]+self._DesignParameter['nmos_vbn1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0], self.getXY('nmos_vbn1')[1][1]+self.getYWidth('nmos_vbn1','_Met1Layer')/2+self.getYWidth('gate_vbn1','_Met1Layer')/2+drc._Metal1MinSpace2])
			tmp.append([self.getXY('nmos_vbn1')[1][0]+self._DesignParameter['nmos_vbn1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0], self.getXY('nmos_vbn1')[1][1]-self.getYWidth('nmos_vbn1','_Met1Layer')/2-self.getYWidth('gate_vbn1','_Met1Layer')/2-drc._Metal1MinSpace2])
		self._DesignParameter['gate_vbn1']['_XYCoordinates']=tmp
		del tmp

		tmp=[]
		for i in range(0, len(self._DesignParameter['nmos_vb1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
			tmp.append([self.getXY('nmos_vb1')[0][0]+self._DesignParameter['nmos_vb1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0], self.getXY('nmos_vb1')[0][1]+self.getYWidth('nmos_vb1','_Met1Layer')/2+self.getYWidth('gate_vb1','_Met1Layer')/2+drc._Metal1MinSpace2])
			tmp.append([self.getXY('nmos_vb1')[0][0]+self._DesignParameter['nmos_vb1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0], self.getXY('nmos_vb1')[0][1]-self.getYWidth('nmos_vb1','_Met1Layer')/2-self.getYWidth('gate_vb1','_Met1Layer')/2-drc._Metal1MinSpace2])
		self._DesignParameter['gate_vb1']['_XYCoordinates']=tmp
		del tmp

		tmp=[]
		for i in range(0, len(self._DesignParameter['nmos_n0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
			tmp.append([self.getXY('nmos_n0')[0][0]+self._DesignParameter['nmos_n0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0], self.getXY('nmos_n0')[0][1]+self.getYWidth('nmos_n0','_Met1Layer')/2+self.getYWidth('gate_n0','_Met1Layer')/2+drc._Metal1MinSpace2])
			tmp.append([self.getXY('nmos_n0')[0][0]+self._DesignParameter['nmos_n0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0], self.getXY('nmos_n0')[0][1]-self.getYWidth('nmos_n0','_Met1Layer')/2-self.getYWidth('gate_n0','_Met1Layer')/2-drc._Metal1MinSpace2])
			tmp.append([self.getXY('nmos_n0')[1][0]+self._DesignParameter['nmos_n0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0], self.getXY('nmos_n0')[1][1]+self.getYWidth('nmos_n0','_Met1Layer')/2+self.getYWidth('gate_n0','_Met1Layer')/2+drc._Metal1MinSpace2])
			tmp.append([self.getXY('nmos_n0')[1][0]+self._DesignParameter['nmos_n0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0], self.getXY('nmos_n0')[1][1]-self.getYWidth('nmos_n0','_Met1Layer')/2-self.getYWidth('gate_n0','_Met1Layer')/2-drc._Metal1MinSpace2])
		self._DesignParameter['gate_n0']['_XYCoordinates']=tmp
		del tmp

		tmp=[]
		for i in range(0, len(self._DesignParameter['nmos_input']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
			tmp.append([self.getXY('nmos_input')[0][0]+self._DesignParameter['nmos_input']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0], self.getXY('nmos_input')[0][1]+self.getYWidth('nmos_input','_Met1Layer')/2+self.getYWidth('gate_ninputp','_Met1Layer')/2+drc._Metal1MinSpace2])
			tmp.append([self.getXY('nmos_input')[0][0]+self._DesignParameter['nmos_input']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0], self.getXY('nmos_input')[0][1]-+self.getYWidth('nmos_input','_Met1Layer')/2-self.getYWidth('gate_ninputp','_Met1Layer')/2-drc._Metal1MinSpace2])
		self._DesignParameter['gate_ninputp']['_XYCoordinates']=tmp
		del tmp

		tmp=[]
		for i in range(0, len(self._DesignParameter['nmos_input']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
			tmp.append([self.getXY('nmos_input')[1][0]+self._DesignParameter['nmos_input']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0], self.getXY('nmos_input')[1][1]+self.getYWidth('nmos_input','_Met1Layer')/2+self.getYWidth('gate_ninputn','_Met1Layer')/2+drc._Metal1MinSpace2])
			tmp.append([self.getXY('nmos_input')[1][0]+self._DesignParameter['nmos_input']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0], self.getXY('nmos_input')[1][1]-self.getYWidth('nmos_input','_Met1Layer')/2-self.getYWidth('gate_ninputn','_Met1Layer')/2-drc._Metal1MinSpace2])
		self._DesignParameter['gate_ninputn']['_XYCoordinates']=tmp
		del tmp

		ViaNumX=max(1,int(self.getXWidth('gate_ninputn','_Met1Layer')/(drc._VIAxMinWidth+drc._VIAxMinSpace)))
		self._DesignParameter['via12_gate_ninputn']=self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='via12_gate_ninputnIn{}'.format(_Name)))[0]
		self._DesignParameter['via12_gate_ninputn']['_DesignObj']._CalculateDesignParameterSameEnclosure( _ViaMet12Met2NumberOfCOX=ViaNumX, _ViaMet12Met2NumberOfCOY=1)
		tmp=[]
		for i in range(0, len(self._DesignParameter['nmos_input']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
			tmp.append([self._DesignParameter['nmos_input']['_XYCoordinates'][0][0]+self._DesignParameter['nmos_input']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0], self._DesignParameter['gate_ninputn']['_XYCoordinates'][0][1]])
			tmp.append([self._DesignParameter['nmos_input']['_XYCoordinates'][0][0]+self._DesignParameter['nmos_input']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0], self._DesignParameter['gate_ninputn']['_XYCoordinates'][-1][1]])
		self._DesignParameter['via12_gate_ninputn']['_XYCoordinates']=tmp
		del tmp

		self._DesignParameter['via12_gate_ninputp']=self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='via12_gate_ninputpIn{}'.format(_Name)))[0]
		self._DesignParameter['via12_gate_ninputp']['_DesignObj']._CalculateDesignParameterSameEnclosure( _ViaMet12Met2NumberOfCOX=ViaNumX, _ViaMet12Met2NumberOfCOY=1)
		tmp=[]
		for i in range(0, len(self._DesignParameter['nmos_input']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
			tmp.append([self._DesignParameter['nmos_input']['_XYCoordinates'][1][0]+self._DesignParameter['nmos_input']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0], self._DesignParameter['gate_ninputp']['_XYCoordinates'][0][1]])
			tmp.append([self._DesignParameter['nmos_input']['_XYCoordinates'][1][0]+self._DesignParameter['nmos_input']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0], self._DesignParameter['gate_ninputp']['_XYCoordinates'][-1][1]])
		self._DesignParameter['via12_gate_ninputp']['_XYCoordinates']=tmp
		del tmp


		self._DesignParameter['m2_gate_ninputn']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0],_Datatype=DesignParameters._LayerMapping['METAL2'][1], _XYCoordinates=[], _Width=None)
		self._DesignParameter['m2_gate_ninputn']['_Width']=self._DesignParameter['via12_gate_ninputn']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth']
		self._DesignParameter['m2_gate_ninputn']['_XYCoordinates']=[[self._DesignParameter['via12_gate_ninputn']['_XYCoordinates'][0], self._DesignParameter['via12_gate_ninputn']['_XYCoordinates'][-2]], \
																   [self._DesignParameter['via12_gate_ninputn']['_XYCoordinates'][1], self._DesignParameter['via12_gate_ninputn']['_XYCoordinates'][-1]]]


		self._DesignParameter['m2_gate_ninputp']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0],_Datatype=DesignParameters._LayerMapping['METAL2'][1], _XYCoordinates=[], _Width=None)
		self._DesignParameter['m2_gate_ninputp']['_Width']=self._DesignParameter['via12_gate_ninputp']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth']
		self._DesignParameter['m2_gate_ninputp']['_XYCoordinates']=[[self._DesignParameter['via12_gate_ninputp']['_XYCoordinates'][0], self._DesignParameter['via12_gate_ninputp']['_XYCoordinates'][-2]], \
																   [self._DesignParameter['via12_gate_ninputp']['_XYCoordinates'][1], self._DesignParameter['via12_gate_ninputp']['_XYCoordinates'][-1]]]

		self._DesignParameter['via12_drain_ninputn']=self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='via12_drain_ninputnIn{}'.format(_Name)))[0]
		self._DesignParameter['via12_drain_ninputn']['_DesignObj']._CalculateDesignParameterSameEnclosure( _ViaMet12Met2NumberOfCOX=1, _ViaMet12Met2NumberOfCOY=2)
		tmp=[]
		for i in range(0, len(self._DesignParameter['nmos_input']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'])):
			tmp.append([self._DesignParameter['nmos_input']['_XYCoordinates'][0][0]+self._DesignParameter['nmos_input']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][i][0], self._DesignParameter['nmos_input']['_XYCoordinates'][0][1]])
			tmp.append([self._DesignParameter['nmos_input']['_XYCoordinates'][0][0]+self._DesignParameter['nmos_input']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][i][0], self._DesignParameter['nmos_input']['_XYCoordinates'][0][1]])
		self._DesignParameter['via12_drain_ninputn']['_XYCoordinates']=tmp
		del tmp

		self._DesignParameter['via12_drain_ninputp']=self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='via12_drain_ninputpIn{}'.format(_Name)))[0]
		self._DesignParameter['via12_drain_ninputp']['_DesignObj']._CalculateDesignParameterSameEnclosure( _ViaMet12Met2NumberOfCOX=1, _ViaMet12Met2NumberOfCOY=2)
		tmp=[]
		for i in range(0, len(self._DesignParameter['nmos_input']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'])):
			tmp.append([self._DesignParameter['nmos_input']['_XYCoordinates'][1][0]+self._DesignParameter['nmos_input']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][i][0], self._DesignParameter['nmos_input']['_XYCoordinates'][1][1]])
			tmp.append([self._DesignParameter['nmos_input']['_XYCoordinates'][1][0]+self._DesignParameter['nmos_input']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][i][0], self._DesignParameter['nmos_input']['_XYCoordinates'][1][1]])
		self._DesignParameter['via12_drain_ninputp']['_XYCoordinates']=tmp
		del tmp

		self._DesignParameter['m2_drain_ninput']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0],_Datatype=DesignParameters._LayerMapping['METAL2'][1], _XYCoordinates=[], _Width=None)
		self._DesignParameter['m2_drain_ninput']['_Width']=self._DesignParameter['via12_drain_ninputp']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth']
		self._DesignParameter['m2_drain_ninput']['_XYCoordinates']=[[self._DesignParameter['via12_drain_ninputn']['_XYCoordinates'][0], self._DesignParameter['via12_drain_ninputn']['_XYCoordinates'][-1]], \
																   [self._DesignParameter['via12_drain_ninputp']['_XYCoordinates'][0], self._DesignParameter['via12_drain_ninputp']['_XYCoordinates'][-1]]]

		self._DesignParameter['poly_nvb1']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0],_Datatype=DesignParameters._LayerMapping['POLY'][1], _XYCoordinates=[], _Width=self.getXWidth('nmos_vb1','_POLayer'))
		self._DesignParameter['poly_nn0']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0],_Datatype=DesignParameters._LayerMapping['POLY'][1], _XYCoordinates=[], _Width=self.getXWidth('nmos_n0','_POLayer'))
		self._DesignParameter['poly_nvbn1']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0],_Datatype=DesignParameters._LayerMapping['POLY'][1], _XYCoordinates=[], _Width=self.getXWidth('nmos_vbn1','_POLayer'))
		self._DesignParameter['poly_ninput']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0],_Datatype=DesignParameters._LayerMapping['POLY'][1], _XYCoordinates=[], _Width=self.getXWidth('nmos_input','_POLayer'))

		tmp=[]
		for i in range(0, len(self._DesignParameter['nmos_vb1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
			tmp.append([[self.getXY('nmos_vb1')[0][0]+self._DesignParameter['nmos_vb1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0], self.getXY('nmos_vb1')[0][1]+self.getYWidth('nmos_vb1','_POLayer')/2+self.getYWidth('gate_vb1','_POLayer')/2],\
						[self.getXY('nmos_vb1')[0][0]+self._DesignParameter['nmos_vb1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0], self.getXY('nmos_vb1')[0][1]-self.getYWidth('nmos_vb1','_POLayer')/2-self.getYWidth('gate_vb1','_POLayer')/2]])
		self._DesignParameter['poly_nvb1']['_XYCoordinates']=tmp
		del tmp

		tmp=[]
		for i in range(0, len(self._DesignParameter['nmos_vbn1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
			tmp.append([[self.getXY('nmos_vbn1')[0][0]+self._DesignParameter['nmos_vbn1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0], self.getXY('nmos_vbn1')[0][1]+self.getYWidth('nmos_vbn1','_POLayer')/2+self.getYWidth('gate_vbn1','_POLayer')/2],\
						[self.getXY('nmos_vbn1')[0][0]+self._DesignParameter['nmos_vbn1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0], self.getXY('nmos_vbn1')[0][1]-self.getYWidth('nmos_vbn1','_POLayer')/2-self.getYWidth('gate_vbn1','_POLayer')/2]])
			tmp.append([[self.getXY('nmos_vbn1')[1][0]+self._DesignParameter['nmos_vbn1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0], self.getXY('nmos_vbn1')[1][1]+self.getYWidth('nmos_vbn1','_POLayer')/2+self.getYWidth('gate_vbn1','_POLayer')/2],\
						[self.getXY('nmos_vbn1')[1][0]+self._DesignParameter['nmos_vbn1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0], self.getXY('nmos_vbn1')[1][1]-self.getYWidth('nmos_vbn1','_POLayer')/2-self.getYWidth('gate_vbn1','_POLayer')/2]])
		self._DesignParameter['poly_nvbn1']['_XYCoordinates']=tmp
		del tmp

		tmp=[]
		for i in range(0, len(self._DesignParameter['nmos_n0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
			tmp.append([[self.getXY('nmos_n0')[0][0]+self._DesignParameter['nmos_n0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0], self.getXY('nmos_n0')[0][1]+self.getYWidth('nmos_n0','_POLayer')/2+self.getYWidth('gate_n0','_POLayer')/2],\
						[self.getXY('nmos_n0')[0][0]+self._DesignParameter['nmos_n0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0], self.getXY('nmos_n0')[0][1]-self.getYWidth('nmos_n0','_POLayer')/2-self.getYWidth('gate_n0','_POLayer')/2]])
			tmp.append([[self.getXY('nmos_n0')[1][0]+self._DesignParameter['nmos_n0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0], self.getXY('nmos_n0')[1][1]+self.getYWidth('nmos_n0','_POLayer')/2+self.getYWidth('gate_n0','_POLayer')/2],\
						[self.getXY('nmos_n0')[1][0]+self._DesignParameter['nmos_n0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0], self.getXY('nmos_n0')[1][1]-self.getYWidth('nmos_n0','_POLayer')/2-self.getYWidth('gate_n0','_POLayer')/2]])
		self._DesignParameter['poly_nn0']['_XYCoordinates']=tmp
		del tmp

		tmp=[]
		for i in range(0, len(self._DesignParameter['nmos_input']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
			tmp.append([[self.getXY('nmos_input')[0][0]+self._DesignParameter['nmos_input']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0], self.getXY('gate_ninputn')[0][1]+self.getYWidth('gate_ninputn','_POLayer')/2],\
						[self.getXY('nmos_input')[0][0]+self._DesignParameter['nmos_input']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0], self.getXY('gate_ninputn')[1][1]-self.getYWidth('gate_ninputn','_POLayer')/2]])
			tmp.append([[self.getXY('nmos_input')[1][0]+self._DesignParameter['nmos_input']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0], self.getXY('gate_ninputp')[0][1]+self.getYWidth('gate_ninputp','_POLayer')/2],\
						[self.getXY('nmos_input')[1][0]+self._DesignParameter['nmos_input']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0], self.getXY('gate_ninputp')[1][1]-self.getYWidth('gate_ninputp','_POLayer')/2]])
		self._DesignParameter['poly_ninput']['_XYCoordinates']=tmp
		del tmp

		if nset_param['nmos_guardring_height1'] != None :
			pguardring_yheight1=nset_param['nmos_guardring_height1']
		elif nset_param['nmos_guardring_height1'] == None :
			pguardring_yheight1=(max(self._DesignParameter['gate_n0']['_XYCoordinates'][0][1]+self.getYWidth('gate_n0','_Met1Layer')/2, self._DesignParameter['gate_vb1']['_XYCoordinates'][0][1]+self.getYWidth('gate_vb1','_Met1Layer')/2)+self.getYWidth('pguardring1','top','_Met1Layer')/2+drc._Metal1MinSpace3)-(self._DesignParameter['gate_ninputp']['_XYCoordinates'][-1][1]-self.getYWidth('gate_ninputp','_Met1Layer')/2-self.getYWidth('pguardring1','top','_Met1Layer')/2-drc._Metal1MinSpace3)
		if nset_param['nmos_guardring_width1'] != None :
			pguardring_xwidth1=nset_param['nmos_guardring_width1']
		elif nset_param['nmos_guardring_width1'] == None :
			pguardring_xwidth1=max(self._DesignParameter['nmos_n0']['_XYCoordinates'][1][0]+self._DesignParameter['nmos_n0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][-1][0]+self.getXWidth('nmos_n0','_Met1Layer')/2+self.getXWidth('pguardring1','right','_Met1Layer')/2+drc._Metal1MinSpace3, self._DesignParameter['nmos_vbn1']['_XYCoordinates'][1][0]+self._DesignParameter['nmos_vbn1']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][-1][0]+self.getXWidth('nmos_vbn1','_Met1Layer')/2+self.getXWidth('pguardring1','right','_Met1Layer')/2+drc._Metal1MinSpace3)\
							   -min(self._DesignParameter['nmos_input']['_XYCoordinates'][0][0]+self._DesignParameter['nmos_input']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0]-self.getXWidth('nmos_input','_Met1Layer')/2-self.getXWidth('pguardring1','left','_Met1Layer')/2-drc._Metal1MinSpace3,self._DesignParameter['nmos_vb1']['_XYCoordinates'][0][0]+self._DesignParameter['nmos_vb1']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0]-self.getXWidth('nmos_vb1','_Met1Layer')/2-self.getXWidth('pguardring1','left','_Met1Layer')/2-drc._Metal1MinSpace3)
		self._DesignParameter['pguardring1']['_DesignObj']._CalculateDesignParameter(height=pguardring_yheight1,width=pguardring_xwidth1,contact_bottom=nset_param['nmos_guardring_co_bot'],contact_top=nset_param['nmos_guardring_co_top'],contact_left=nset_param['nmos_guardring_co_left'],contact_right=nset_param['nmos_guardring_co_right'])
		self._DesignParameter['pguardring1']['_XYCoordinates']=[[(max(self._DesignParameter['nmos_n0']['_XYCoordinates'][1][0]+self._DesignParameter['nmos_n0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][-1][0]+self.getXWidth('nmos_n0','_Met1Layer')/2+self.getXWidth('pguardring1','right','_Met1Layer')/2+drc._Metal1MinSpace3, self._DesignParameter['nmos_vbn1']['_XYCoordinates'][1][0]+self._DesignParameter['nmos_vbn1']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][-1][0]+self.getXWidth('nmos_vbn1','_Met1Layer')/2+self.getXWidth('pguardring1','right','_Met1Layer')/2+drc._Metal1MinSpace3)\
							   +min(self._DesignParameter['nmos_input']['_XYCoordinates'][0][0]+self._DesignParameter['nmos_input']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0]-self.getXWidth('nmos_input','_Met1Layer')/2-self.getXWidth('pguardring1','left','_Met1Layer')/2-drc._Metal1MinSpace3,self._DesignParameter['nmos_vb1']['_XYCoordinates'][0][0]+self._DesignParameter['nmos_vb1']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0]-self.getXWidth('nmos_vb1','_Met1Layer')/2-self.getXWidth('pguardring1','left','_Met1Layer')/2-drc._Metal1MinSpace3))/2, ((max(self._DesignParameter['gate_n0']['_XYCoordinates'][0][1]+self.getYWidth('gate_n0','_Met1Layer')/2, self._DesignParameter['gate_vb1']['_XYCoordinates'][0][1]+self.getYWidth('gate_vb1','_Met1Layer')/2)+self.getYWidth('pguardring1','top','_Met1Layer')/2+drc._Metal1MinSpace3)+(self._DesignParameter['gate_ninputp']['_XYCoordinates'][-1][1]-self.getYWidth('gate_ninputp','_Met1Layer')/2-self.getYWidth('pguardring1','top','_Met1Layer')/2-drc._Metal1MinSpace3))/2]]

		if self.getXY('nguardring2','left')[0][0] < self.getXY('pguardring1','left')[0][0]:
			left_x_guardring=self.getXY('nguardring2','left')[0][0]
		elif self.getXY('nguardring2','left')[0][0] >= self.getXY('pguardring1','left')[0][0]:
			left_x_guardring=self.getXY('pguardring1','left')[0][0]
		if self.getXY('nguardring2','right')[0][0] < self.getXY('pguardring1','right')[0][0]:
			right_x_guardring=self.getXY('pguardring1','right')[0][0]
		elif self.getXY('nguardring2','right')[0][0] >= self.getXY('pguardring1','right')[0][0]:
			right_x_guardring=self.getXY('nguardring2','right')[0][0]

		tmp_width_guardring=right_x_guardring-left_x_guardring
		tmp_x=(right_x_guardring+left_x_guardring)/2

		self._DesignParameter['pguardring1']['_DesignObj']._CalculateDesignParameter(height=pguardring_yheight1,width=tmp_width_guardring,contact_bottom=nset_param['nmos_guardring_co_bot'],contact_top=nset_param['nmos_guardring_co_top'],contact_left=nset_param['nmos_guardring_co_left'],contact_right=nset_param['nmos_guardring_co_right'])
		self._DesignParameter['pguardring1']['_XYCoordinates']=[[tmp_x, self._DesignParameter['pguardring1']['_XYCoordinates'][0][1]]]

		self._DesignParameter['nguardring2']['_DesignObj']._CalculateDesignParameter(height=nguardring_yheight2,width=tmp_width_guardring,contact_bottom=pset_param['pmos_guardring_co_bot'],contact_top=pset_param['pmos_guardring_co_top'],contact_left=pset_param['pmos_guardring_co_left'],contact_right=pset_param['pmos_guardring_co_right'])
		self._DesignParameter['nguardring2']['_XYCoordinates']=[[tmp_x, self._DesignParameter['nguardring2']['_XYCoordinates'][0][1]]]

		self._DesignParameter['nguardring1']['_DesignObj']._CalculateDesignParameter(height=nguardring_yheight1,width=self.getXY('nguardring1','right')[0][0]-left_x_guardring,contact_bottom=pset_param['pmos_guardring_co_top'],contact_top=pset_param['pmos_guardring_co_top'],contact_left=pset_param['pmos_guardring_co_left'],contact_right=pset_param['pmos_guardring_co_top'])
		self._DesignParameter['nguardring1']['_XYCoordinates']=[[(self.getXY('nguardring1','right')[0][0]+left_x_guardring)/2, self._DesignParameter['nguardring1']['_XYCoordinates'][0][1]]]

		self._DesignParameter['additional_od_left']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['DIFF'][0],_Datatype=DesignParameters._LayerMapping['DIFF'][1], _XYCoordinates=[], _Width=self.getXWidth('nguardring2','od_left'))
		self._DesignParameter['additional_od_left']['_XYCoordinates']=[[self.getXY('nguardring2','left')[0], self.getXY('nguardring1','left')[0]]]
		self._DesignParameter['additional_met1_left']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0],_Datatype=DesignParameters._LayerMapping['METAL1'][1], _XYCoordinates=[], _Width=self.getXWidth('nguardring2','met_left'))
		self._DesignParameter['additional_met1_left']['_XYCoordinates']=[[self.getXY('nguardring2','left')[0], self.getXY('nguardring1','left')[0]]]
		self._DesignParameter['additional_nw_left']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['NWELL'][0],_Datatype=DesignParameters._LayerMapping['NWELL'][1], _XYCoordinates=[], _Width=self.getXWidth('nguardring2','nw_left'))
		self._DesignParameter['additional_nw_left']['_XYCoordinates']=[[self.getXY('nguardring2','left')[0], self.getXY('nguardring1','left')[0]]]
		self._DesignParameter['additional_od_top']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['DIFF'][0],_Datatype=DesignParameters._LayerMapping['DIFF'][1], _XYCoordinates=[], _Width=self.getXWidth('nguardring1','od_right'))
		self._DesignParameter['additional_od_top']['_XYCoordinates']=[[[self.getXY('nguardring1','right')[0][0]-self.getXWidth('nguardring1','od_right')/2, self.getXY('nguardring2','od_top')[0][1]], [self.getXY('nguardring2','right')[0][0]+self.getXWidth('nguardring2','od_right')/2, self.getXY('nguardring2','od_top')[0][1]]]]
		self._DesignParameter['additional_od_right']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['DIFF'][0],_Datatype=DesignParameters._LayerMapping['DIFF'][1], _XYCoordinates=[], _Width=self.getXWidth('nguardring2','od_left'))
		self._DesignParameter['additional_od_right']['_XYCoordinates']=[[self.getXY('nguardring1','right')[0], [self.getXY('nguardring1','right')[0][0], self.getXY('nguardring2','top')[0][1]]]]

		self._DesignParameter['additional_nw1']=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['NWELL'][0],_Datatype=DesignParameters._LayerMapping['NWELL'][1], _XYCoordinates=[], _XWidth=None, _YWidth=None)
		self._DesignParameter['additional_nw1']['_XWidth']=(self.getXY('nguardring1','right')[0][0]+self.getXWidth('nguardring1','nw_right')/2)-(self.getXY('nguardring1','left')[0][0]-self.getXWidth('nguardring1','nw_left')/2)
		self._DesignParameter['additional_nw1']['_YWidth']=self.getXY('nguardring1','top')[0][1]-self.getXY('nguardring2','bot')[0][1]
		self._DesignParameter['additional_nw1']['_XYCoordinates']=[[((self.getXY('nguardring1','right')[0][0]+self.getXWidth('nguardring1','nw_right')/2)+(self.getXY('nguardring1','left')[0][0]-self.getXWidth('nguardring1','nw_left')/2))/2, (self.getXY('nguardring1','top')[0][1]+self.getXY('nguardring2','bot')[0][1])/2]]

		self._DesignParameter['additional_nw2']=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['NWELL'][0],_Datatype=DesignParameters._LayerMapping['NWELL'][1], _XYCoordinates=[], _XWidth=None, _YWidth=None)
		self._DesignParameter['additional_nw2']['_XWidth']=(self.getXY('nguardring2','right')[0][0]+self.getXWidth('nguardring2','nw_right')/2)-(self.getXY('nguardring2','left')[0][0]-self.getXWidth('nguardring2','nw_left')/2)
		self._DesignParameter['additional_nw2']['_YWidth']=self.getXY('additional_od_top')[0][0][1]-self.getXY('nguardring2','bot')[0][1]
		self._DesignParameter['additional_nw2']['_XYCoordinates']=[[((self.getXY('nguardring2','right')[0][0]+self.getXWidth('nguardring2','nw_right')/2)+(self.getXY('nguardring2','left')[0][0]-self.getXWidth('nguardring2','nw_left')/2))/2, (self.getXY('additional_od_top')[0][0][1]+self.getXY('nguardring2','bot')[0][1])/2]]

		self._DesignParameter['pguardring2']=self._SrefElementDeclaration(_DesignObj=PSubRing.PSubRing(_Name='pguardring2In{}'.format(_Name)))[0]
		self._DesignParameter['pguardring2']['_DesignObj']._CalculateDesignParameter(height=5000,width=3000,contact_bottom=nset_param['nmos_guardring_co_bot'],contact_top=nset_param['nmos_guardring_co_bot'],contact_left=nset_param['nmos_guardring_co_bot'],contact_right=nset_param['nmos_guardring_co_right'])

		if nset_param['nmos_guardring_height2'] != None :
			pguardring_yheight2=nset_param['nmos_guardring_height2']
		elif nset_param['nmos_guardring_height2'] == None :
			pguardring_yheight2=self.getXY('pguardring1','bot')[0][1]-(self.getXY('nguardring2','top')[0][1]+self.getYWidth('nguardring2','top','_Met1Layer')/2+self.getYWidth('pguardring2','bot','_Met1Layer')/2+drc._Metal1MinSpace3)
		if nset_param['nmos_guardring_width2'] != None :
			pguardring_xwidth2=nset_param['nmos_guardring_width2']
		elif nset_param['nmos_guardring_width2'] == None :
			pguardring_xwidth2=self.getXY('pguardring1','right')[0][0]-(self.getXY('nguardring1','right')[0][0]+self.getXWidth('nguardring1','right','_Met1Layer')/2+self.getXWidth('pguardring2','left','_Met1Layer')/2+drc._Metal1MinSpace3)

		self._DesignParameter['pguardring2']['_DesignObj']._CalculateDesignParameter(height=pguardring_yheight2,width=pguardring_xwidth2,contact_bottom=nset_param['nmos_guardring_co_bot'],contact_top=nset_param['nmos_guardring_co_bot'],contact_left=nset_param['nmos_guardring_co_bot'],contact_right=nset_param['nmos_guardring_co_right'])

		self._DesignParameter['pguardring2']['_XYCoordinates']=[[(self.getXY('pguardring1','right')[0][0]+(self.getXY('nguardring1','right')[0][0]+self.getXWidth('nguardring1','right','_Met1Layer')/2+self.getXWidth('pguardring2','left','_Met1Layer')/2+drc._Metal1MinSpace3))/2, (self.getXY('pguardring1','bot')[0][1]+(self.getXY('nguardring2','top')[0][1]+self.getYWidth('nguardring2','top','_Met1Layer')/2+self.getYWidth('pguardring2','bot','_Met1Layer')/2+drc._Metal1MinSpace3))/2]]

		self._DesignParameter['pguardring3']=self._SrefElementDeclaration(_DesignObj=PbodyContact._PbodyContact(_Name='pguardring3In{}'.format(_Name)))[0]
		_numofCoX=int((self.getXY('pguardring2','left')[0][0]+self.getXWidth('pguardring2','left','_Met1Layer')/2-self.getXY('pguardring1','left')[0][0]-self.getXWidth('pguardring1','left','_Met1Layer')/2)/(drc._CoMinSpace+drc._CoMinWidth))
		_numofCoY=nset_param['nmos_guardring_co_bot']
		self._DesignParameter['pguardring3']['_DesignObj']._CalculatePbodyContactDesignParameter(**dict(_NumberOfPbodyCOX=_numofCoX, _NumberOfPbodyCOY=_numofCoY, _Met1XWidth=None, _Met1YWidth=None))
		self._DesignParameter['pguardring3']['_XYCoordinates']=[[(self.getXY('pguardring1','left')[0][0]+self.getXY('pguardring2','left')[0][0])/2, self.getXY('pguardring2','top')[0][1]]]
		del _numofCoY
		del _numofCoX

		self._DesignParameter['AdditionalMet1']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0],_Datatype=DesignParameters._LayerMapping['METAL1'][1], _XYCoordinates=[], _Width=self.getYWidth('pguardring1','bot','_Met1Layer'))
		self._DesignParameter['AdditionalMet1']['_XYCoordinates']=[[[self.getXY('pguardring1','left')[0][0], self.getXY('pguardring1','bot')[0][1]], [self.getXY('pguardring2','left')[0][0], self.getXY('pguardring1','bot')[0][1]]]]
		self._DesignParameter['AdditionalOD']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['DIFF'][0],_Datatype=DesignParameters._LayerMapping['DIFF'][1], _XYCoordinates=[], _Width=self.getYWidth('pguardring1','bot','_ODLayer'))
		self._DesignParameter['AdditionalOD']['_XYCoordinates']=[[[self.getXY('pguardring1','left')[0][0], self.getXY('pguardring1','bot')[0][1]], [self.getXY('pguardring2','left')[0][0], self.getXY('pguardring1','bot')[0][1]]]]
		self._DesignParameter['AdditionalPP']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['PIMP'][0],_Datatype=DesignParameters._LayerMapping['PIMP'][1], _XYCoordinates=[], _Width=self.getYWidth('pguardring1','bot','_PPLayer'))
		self._DesignParameter['AdditionalPP']['_XYCoordinates']=[[[self.getXY('pguardring1','left')[0][0], self.getXY('pguardring1','bot')[0][1]], [self.getXY('pguardring2','left')[0][0]  , self.getXY('pguardring1','bot')[0][1]]]]

		self._DesignParameter['nguardring2']['_DesignObj']._DesignParameter['od_top']['_XYCoordinates']=[]
		self._DesignParameter['nguardring2']['_DesignObj']._DesignParameter['top']['_XYCoordinates']=[]
		self._DesignParameter['nguardring2']['_DesignObj']._DesignParameter['met_top']['_XYCoordinates']=[]

		self._DesignParameter['nguardring1']['_DesignObj']._DesignParameter['bot']['_XYCoordinates']=[]
		self._DesignParameter['nguardring1']['_DesignObj']._DesignParameter['od_bot']['_XYCoordinates']=[]
		self._DesignParameter['nguardring1']['_DesignObj']._DesignParameter['nw_bot']['_XYCoordinates']=[]
		self._DesignParameter['nguardring1']['_DesignObj']._DesignParameter['met_bot']['_XYCoordinates']=[]

		self._DesignParameter['pguardring1']['_DesignObj']._DesignParameter['od_bot']['_XYCoordinates']=[]
		self._DesignParameter['pguardring1']['_DesignObj']._DesignParameter['bot']['_XYCoordinates']=[]
		self._DesignParameter['pguardring1']['_DesignObj']._DesignParameter['met_bot']['_XYCoordinates']=[]
		self._DesignParameter['pguardring1']['_DesignObj']._DesignParameter['pw_bot']['_XYCoordinates']=[]

		self._DesignParameter['pguardring2']['_DesignObj']._DesignParameter['top']['_XYCoordinates']=[]
		self._DesignParameter['pguardring2']['_DesignObj']._DesignParameter['od_top']['_XYCoordinates']=[]
		self._DesignParameter['pguardring2']['_DesignObj']._DesignParameter['met_top']['_XYCoordinates']=[]
		self._DesignParameter['pguardring2']['_DesignObj']._DesignParameter['pw_top']['_XYCoordinates']=[]

		self._DesignParameter['pguardring2']['_DesignObj']._DesignParameter['bot']['_XYCoordinates']=[]
		self._DesignParameter['pguardring2']['_DesignObj']._DesignParameter['met_bot']['_XYCoordinates']=[]


		self._DesignParameter['via12_drain_vbp1']=self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='via12_drain_vbp1In{}'.format(_Name)))[0]
		self._DesignParameter['via12_drain_vbp1']['_DesignObj']._CalculateDesignParameterSameEnclosure( _ViaMet12Met2NumberOfCOX=1, _ViaMet12Met2NumberOfCOY=2)
		tmp=[]
		for i in range(0, len(self._DesignParameter['pmos_vbp1']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'])):
			tmp.append([self._DesignParameter['pmos_vbp1']['_XYCoordinates'][0][0]+self._DesignParameter['pmos_vbp1']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][i][0], self._DesignParameter['pmos_vbp1']['_XYCoordinates'][0][1]+self.getYWidth('via12_drain_vbp1','_Met2Layer')/2+drc._Metal1MinSpace3/2])
			tmp.append([-(self._DesignParameter['pmos_vbp1']['_XYCoordinates'][0][0]+self._DesignParameter['pmos_vbp1']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][i][0]), self._DesignParameter['pmos_vbp1']['_XYCoordinates'][0][1]+self.getYWidth('via12_drain_vbp1','_Met2Layer')/2+drc._Metal1MinSpace3/2])
		self._DesignParameter['via12_drain_vbp1']['_XYCoordinates']=tmp
		del tmp

		self._DesignParameter['via12_source_vbp1']=self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='via12_source_vbp1In{}'.format(_Name)))[0]
		self._DesignParameter['via12_source_vbp1']['_DesignObj']._CalculateDesignParameterSameEnclosure( _ViaMet12Met2NumberOfCOX=1, _ViaMet12Met2NumberOfCOY=2)
		tmp=[]
		for i in range(0, len(self._DesignParameter['pmos_vbp1']['_DesignObj']._DesignParameter['_XYCoordinatePMOSSupplyRouting']['_XYCoordinates'])):
			tmp.append([self._DesignParameter['pmos_vbp1']['_XYCoordinates'][0][0]+self._DesignParameter['pmos_vbp1']['_DesignObj']._DesignParameter['_XYCoordinatePMOSSupplyRouting']['_XYCoordinates'][i][0], self._DesignParameter['pmos_vbp1']['_XYCoordinates'][0][1]-self.getYWidth('via12_source_vbp1','_Met2Layer')/2-drc._Metal1MinSpace3/2])
			tmp.append([-(self._DesignParameter['pmos_vbp1']['_XYCoordinates'][0][0]+self._DesignParameter['pmos_vbp1']['_DesignObj']._DesignParameter['_XYCoordinatePMOSSupplyRouting']['_XYCoordinates'][i][0]), self._DesignParameter['pmos_vbp1']['_XYCoordinates'][0][1]-self.getYWidth('via12_source_vbp1','_Met2Layer')/2-drc._Metal1MinSpace3/2])
		self._DesignParameter['via12_source_vbp1']['_XYCoordinates']=tmp
		del tmp

		self._DesignParameter['m1_source_vbp2']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0],_Datatype=DesignParameters._LayerMapping['METAL1'][1], _XYCoordinates=[], _Width=None)
		self._DesignParameter['m1_source_vbp2']['_Width']=self.getXWidth('pmos_vbp2','_Met1Layer')
		tmp=[]
		for i in range(0,len(self._DesignParameter['pmos_vbp2']['_DesignObj']._DesignParameter['_XYCoordinatePMOSSupplyRouting']['_XYCoordinates'])):
			tmp.append([[self._DesignParameter['pmos_vbp2']['_XYCoordinates'][0][0]+self._DesignParameter['pmos_vbp2']['_DesignObj']._DesignParameter['_XYCoordinatePMOSSupplyRouting']['_XYCoordinates'][i][0], self._DesignParameter['pmos_vbp2']['_XYCoordinates'][0][1]+self._DesignParameter['pmos_vbp2']['_DesignObj']._DesignParameter['_XYCoordinatePMOSSupplyRouting']['_XYCoordinates'][i][1]], \
						[self._DesignParameter['pmos_vbp2']['_XYCoordinates'][0][0]+self._DesignParameter['pmos_vbp2']['_DesignObj']._DesignParameter['_XYCoordinatePMOSSupplyRouting']['_XYCoordinates'][i][0], self.getXY('nguardring2','bot')[0][1]]])
			tmp.append([[-(self._DesignParameter['pmos_vbp2']['_XYCoordinates'][0][0]+self._DesignParameter['pmos_vbp2']['_DesignObj']._DesignParameter['_XYCoordinatePMOSSupplyRouting']['_XYCoordinates'][i][0]), self._DesignParameter['pmos_vbp2']['_XYCoordinates'][0][1]+self._DesignParameter['pmos_vbp2']['_DesignObj']._DesignParameter['_XYCoordinatePMOSSupplyRouting']['_XYCoordinates'][i][1]], \
						[-(self._DesignParameter['pmos_vbp2']['_XYCoordinates'][0][0]+self._DesignParameter['pmos_vbp2']['_DesignObj']._DesignParameter['_XYCoordinatePMOSSupplyRouting']['_XYCoordinates'][i][0]), self.getXY('nguardring2','bot')[0][1]]])
		self._DesignParameter['m1_source_vbp2']['_XYCoordinates']=tmp
		del tmp

		self._DesignParameter['m1_drain_vbp2']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0],_Datatype=DesignParameters._LayerMapping['METAL1'][1], _XYCoordinates=[], _Width=None)
		self._DesignParameter['m1_drain_vbp2']['_Width']=self.getXWidth('pmos_vbp2','_Met1Layer')
		tmp=[]
		for i in range(0,len(self._DesignParameter['pmos_vbp2']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'])):
			tmp.append([[self._DesignParameter['pmos_vbp2']['_XYCoordinates'][0][0]+self._DesignParameter['pmos_vbp2']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][i][0], self._DesignParameter['pmos_vbp2']['_XYCoordinates'][0][1]+self._DesignParameter['pmos_vbp2']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][i][1]], \
						[self._DesignParameter['pmos_vbp2']['_XYCoordinates'][0][0]+self._DesignParameter['pmos_vbp2']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][i][0], self._DesignParameter['met1_pdn_pair_sw_x']['_XYCoordinates'][0][0][1]]])
			tmp.append([[-(self._DesignParameter['pmos_vbp2']['_XYCoordinates'][0][0]+self._DesignParameter['pmos_vbp2']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][i][0]), self._DesignParameter['pmos_vbp2']['_XYCoordinates'][0][1]+self._DesignParameter['pmos_vbp2']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][i][1]], \
						[-(self._DesignParameter['pmos_vbp2']['_XYCoordinates'][0][0]+self._DesignParameter['pmos_vbp2']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][i][0]), self._DesignParameter['met1_pdn_pair_sw_x']['_XYCoordinates'][0][0][1]]])
		self._DesignParameter['m1_drain_vbp2']['_XYCoordinates']=tmp
		del tmp

		self._DesignParameter['additional_met1_pdn_pair_sw_x']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0],_Datatype=DesignParameters._LayerMapping['METAL1'][1], _XYCoordinates=[], _Width=None)
		self._DesignParameter['additional_met1_pdn_pair_sw_x']['_Width']=self._DesignParameter['met1_pdn_pair_sw_x']['_Width']
		self._DesignParameter['additional_met1_pdn_pair_sw_x']['_XYCoordinates']=[[[self._DesignParameter['pmos_vbp2']['_XYCoordinates'][0][0]+self._DesignParameter['pmos_vbp2']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][0][0]-self._DesignParameter['m1_drain_vbp2']['_Width']/2, self._DesignParameter['met1_pdn_pair_sw_x']['_XYCoordinates'][0][0][1]], \
																				   [self._DesignParameter['pmos_vbp2']['_XYCoordinates'][0][0]+self._DesignParameter['pmos_vbp2']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][-1][0]+self._DesignParameter['m1_drain_vbp2']['_Width']/2, self._DesignParameter['met1_pdn_pair_sw_x']['_XYCoordinates'][0][0][1]]],\
																				  [[-(self._DesignParameter['pmos_vbp2']['_XYCoordinates'][0][0]+self._DesignParameter['pmos_vbp2']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][0][0]-self._DesignParameter['m1_drain_vbp2']['_Width']/2), self._DesignParameter['met1_pdn_pair_sw_x']['_XYCoordinates'][0][0][1]], \
																				   [-(self._DesignParameter['pmos_vbp2']['_XYCoordinates'][0][0]+self._DesignParameter['pmos_vbp2']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][-1][0]+self._DesignParameter['m1_drain_vbp2']['_Width']/2), self._DesignParameter['met1_pdn_pair_sw_x']['_XYCoordinates'][0][0][1]]]]

		self._DesignParameter['m1_vbp1_source_y']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0],_Datatype=DesignParameters._LayerMapping['METAL1'][1], _XYCoordinates=[], _Width=None)
		self._DesignParameter['m1_vbp1_source_y']['_Width']=self._DesignParameter['pmos_vbp1']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
		tmp=[]
		tmp.append([[self.getXY('pmos_vbp1','_XYCoordinatePMOSSupplyRouting')[0][0], self.getXY('pmos_vbp1','_XYCoordinatePMOSSupplyRouting')[0][1]], [self.getXY('pmos_vbp1','_XYCoordinatePMOSSupplyRouting')[0][0], self._DesignParameter['pmos_pdn_pair_sw']['_XYCoordinates'][0][1]]])
		tmp.append([[self._DesignParameter['pmos_vbp1']['_XYCoordinates'][0][0]+self._DesignParameter['pmos_vbp1']['_DesignObj']._DesignParameter['_XYCoordinatePMOSSupplyRouting']['_XYCoordinates'][-1][0], self.getXY('pmos_vbp1','_XYCoordinatePMOSSupplyRouting')[0][1]], [self._DesignParameter['pmos_vbp1']['_XYCoordinates'][0][0]+self._DesignParameter['pmos_vbp1']['_DesignObj']._DesignParameter['_XYCoordinatePMOSSupplyRouting']['_XYCoordinates'][-1][0], self._DesignParameter['pmos_pdn_pair_sw']['_XYCoordinates'][0][1]]])
		tmp.append([[-(self.getXY('pmos_vbp1','_XYCoordinatePMOSSupplyRouting')[0][0]), self.getXY('pmos_vbp1','_XYCoordinatePMOSSupplyRouting')[0][1]], [-(self.getXY('pmos_vbp1','_XYCoordinatePMOSSupplyRouting')[0][0]), self._DesignParameter['pmos_pdn_pair_sw']['_XYCoordinates'][0][1]]])
		tmp.append([[-(self._DesignParameter['pmos_vbp1']['_XYCoordinates'][0][0]+self._DesignParameter['pmos_vbp1']['_DesignObj']._DesignParameter['_XYCoordinatePMOSSupplyRouting']['_XYCoordinates'][-1][0]), self.getXY('pmos_vbp1','_XYCoordinatePMOSSupplyRouting')[0][1]], [-(self._DesignParameter['pmos_vbp1']['_XYCoordinates'][0][0]+self._DesignParameter['pmos_vbp1']['_DesignObj']._DesignParameter['_XYCoordinatePMOSSupplyRouting']['_XYCoordinates'][-1][0]), self._DesignParameter['pmos_pdn_pair_sw']['_XYCoordinates'][0][1]]])
		self._DesignParameter['m1_vbp1_source_y']['_XYCoordinates']=tmp
		del tmp

		self._DesignParameter['via12_vbp_source']=self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='via12_vbp_sourceIn{}'.format(_Name)))[0]
		self._DesignParameter['via12_vbp_source']['_DesignObj']._CalculateDesignParameterSameEnclosure( _ViaMet12Met2NumberOfCOX=1, _ViaMet12Met2NumberOfCOY=2)
		self._DesignParameter['via12_vbp_source']['_XYCoordinates']=[self._DesignParameter['m1_vbp1_source_y']['_XYCoordinates'][0][1], self._DesignParameter['m1_vbp1_source_y']['_XYCoordinates'][1][1], self._DesignParameter['m1_vbp1_source_y']['_XYCoordinates'][2][1], self._DesignParameter['m1_vbp1_source_y']['_XYCoordinates'][3][1]]

		self._DesignParameter['m2_vbp_pdn_pair']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0],_Datatype=DesignParameters._LayerMapping['METAL2'][1], _XYCoordinates=[], _Width=None)
		self._DesignParameter['m2_vbp_pdn_pair']['_Width']=self._DesignParameter['via12_vbp_source']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth']
		self._DesignParameter['m2_vbp_pdn_pair']['_XYCoordinates']=[[self._DesignParameter['via12_vbp_source']['_XYCoordinates'][0], self._DesignParameter['via12_vbp_source']['_XYCoordinates'][1]], [self._DesignParameter['via12_vbp_source']['_XYCoordinates'][2], self._DesignParameter['via12_vbp_source']['_XYCoordinates'][3]]]

		self._DesignParameter['m1_drain_pdn_single_sw']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0],_Datatype=DesignParameters._LayerMapping['METAL1'][1], _XYCoordinates=[], _Width=None)
		self._DesignParameter['m1_drain_pdn_single_sw']['_Width']=self.getXWidth('pmos_pdn_single_sw','_Met1Layer')
		tmp=[]
		for i in range(0,len(self._DesignParameter['pmos_pdn_single_sw']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'])):
			tmp.append([[self._DesignParameter['pmos_pdn_single_sw']['_XYCoordinates'][0][0]+self._DesignParameter['pmos_pdn_single_sw']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][i][0], self._DesignParameter['pmos_pdn_single_sw']['_XYCoordinates'][0][1]+self._DesignParameter['pmos_pdn_single_sw']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][i][1]], \
						[self._DesignParameter['pmos_pdn_single_sw']['_XYCoordinates'][0][0]+self._DesignParameter['pmos_pdn_single_sw']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][i][0], self.getXY('nguardring2','bot')[0][1]]])
			tmp.append([[self._DesignParameter['pmos_pdn_single_sw']['_XYCoordinates'][1][0]+self._DesignParameter['pmos_pdn_single_sw']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][i][0], self._DesignParameter['pmos_pdn_single_sw']['_XYCoordinates'][0][1]+self._DesignParameter['pmos_pdn_single_sw']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][i][1]], \
						[self._DesignParameter['pmos_pdn_single_sw']['_XYCoordinates'][1][0]+self._DesignParameter['pmos_pdn_single_sw']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][i][0], self.getXY('nguardring2','bot')[0][1]]])
		self._DesignParameter['m1_drain_pdn_single_sw']['_XYCoordinates']=tmp
		del tmp

		self._DesignParameter['via12_gate_vb2']=self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='via12_gate_vb2In{}'.format(_Name)))[0]
		ViaNumX=max(1,int(self.getXWidth('gate_vb2','_Met1Layer')/(drc._VIAxMinWidth+drc._VIAxMinSpace)))
		self._DesignParameter['via12_gate_vb2']['_DesignObj']._CalculateDesignParameterSameEnclosure( _ViaMet12Met2NumberOfCOX=ViaNumX, _ViaMet12Met2NumberOfCOY=1)
		tmp=[]
		for i in range(0, len(self._DesignParameter['pmos_vb2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
			tmp.append([self._DesignParameter['pmos_vb2']['_XYCoordinates'][0][0]+self._DesignParameter['pmos_vb2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0], self._DesignParameter['gate_vb2']['_XYCoordinates'][0][1]])
			tmp.append([self._DesignParameter['pmos_vb2']['_XYCoordinates'][0][0]+self._DesignParameter['pmos_vb2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0], self._DesignParameter['gate_vb2']['_XYCoordinates'][1][1]])
		self._DesignParameter['via12_gate_vb2']['_XYCoordinates']=tmp
		del tmp

		self._DesignParameter['via12_source_vb2']=self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='via12_source_vb2In{}'.format(_Name)))[0]
		self._DesignParameter['via12_source_vb2']['_DesignObj']._CalculateDesignParameterSameEnclosure( _ViaMet12Met2NumberOfCOX=1, _ViaMet12Met2NumberOfCOY=2)
		tmp=[]
		for i in range(0, len(self._DesignParameter['pmos_vb2']['_DesignObj']._DesignParameter['_XYCoordinatePMOSSupplyRouting']['_XYCoordinates'])):
			tmp.append([self._DesignParameter['pmos_vb2']['_XYCoordinates'][0][0]+self._DesignParameter['pmos_vb2']['_DesignObj']._DesignParameter['_XYCoordinatePMOSSupplyRouting']['_XYCoordinates'][i][0], self._DesignParameter['pmos_vb2']['_XYCoordinates'][0][1]+self._DesignParameter['pmos_vb2']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]+self._DesignParameter['pmos_vb2']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']/2-self._DesignParameter['via12_source_vb2']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']/2])
		self._DesignParameter['via12_source_vb2']['_XYCoordinates']=tmp
		del tmp

		self._DesignParameter['via12_source_pdn_single']=self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='via12_source_pdn_singleIn{}'.format(_Name)))[0]
		self._DesignParameter['via12_source_pdn_single']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX( _ViaMet12Met2NumberOfCOX=1, _ViaMet12Met2NumberOfCOY=2)
		tmp=[]
		for i in range(0, len(self._DesignParameter['pmos_pdn_single_sw']['_DesignObj']._DesignParameter['_XYCoordinatePMOSSupplyRouting']['_XYCoordinates'])):
			tmp.append([self._DesignParameter['pmos_pdn_single_sw']['_XYCoordinates'][0][0]+self._DesignParameter['pmos_pdn_single_sw']['_DesignObj']._DesignParameter['_XYCoordinatePMOSSupplyRouting']['_XYCoordinates'][i][0], self._DesignParameter['pmos_pdn_single_sw']['_XYCoordinates'][0][1]+self._DesignParameter['pmos_pdn_single_sw']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]-self._DesignParameter['pmos_pdn_single_sw']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']/2+self._DesignParameter['via12_source_pdn_single']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']/2])
			tmp.append([self._DesignParameter['pmos_pdn_single_sw']['_XYCoordinates'][1][0]+self._DesignParameter['pmos_pdn_single_sw']['_DesignObj']._DesignParameter['_XYCoordinatePMOSSupplyRouting']['_XYCoordinates'][i][0], self._DesignParameter['pmos_pdn_single_sw']['_XYCoordinates'][0][1]+self._DesignParameter['pmos_pdn_single_sw']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]-self._DesignParameter['pmos_pdn_single_sw']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']/2+self._DesignParameter['via12_source_pdn_single']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']/2])
		self._DesignParameter['via12_source_pdn_single']['_XYCoordinates']=tmp
		del tmp

		self._DesignParameter['via12_drain_vb2']=self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='via12_drain_vb2In{}'.format(_Name)))[0]
		self._DesignParameter['via12_drain_vb2']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX( _ViaMet12Met2NumberOfCOX=1, _ViaMet12Met2NumberOfCOY=2)
		tmp=[]
		for i in range(0, len(self._DesignParameter['pmos_vb2']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'])):
			tmp.append([self._DesignParameter['pmos_vb2']['_XYCoordinates'][0][0]+self._DesignParameter['pmos_vb2']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][i][0], self._DesignParameter['via12_source_pdn_single']['_XYCoordinates'][0][1]])
		self._DesignParameter['via12_drain_vb2']['_XYCoordinates']=tmp
		del tmp

		self._DesignParameter['m2_gate_vbp2']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0],_Datatype=DesignParameters._LayerMapping['METAL2'][1], _XYCoordinates=[], _Width=None)
		self._DesignParameter['m2_gate_vbp2']['_Width']=self._DesignParameter['via12_gate_vbp2']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth']
		self._DesignParameter['m2_gate_vbp2']['_XYCoordinates']=[[self._DesignParameter['via12_gate_vbp2']['_XYCoordinates'][0], self._DesignParameter['via12_gate_vbp2']['_XYCoordinates'][-2]], \
																 [self._DesignParameter['via12_gate_vbp2']['_XYCoordinates'][1], self._DesignParameter['via12_gate_vbp2']['_XYCoordinates'][-1]]]

		self._DesignParameter['m2_gate_vbp1']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0],_Datatype=DesignParameters._LayerMapping['METAL2'][1], _XYCoordinates=[], _Width=None)
		self._DesignParameter['m2_gate_vbp1']['_Width']=self._DesignParameter['via12_gate_vbp1']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth']
		self._DesignParameter['m2_gate_vbp1']['_XYCoordinates']=[[self._DesignParameter['via12_gate_vbp1']['_XYCoordinates'][0], self._DesignParameter['via12_gate_vbp1']['_XYCoordinates'][-2]],\
																 [self._DesignParameter['via12_gate_vbp1']['_XYCoordinates'][1], self._DesignParameter['via12_gate_vbp1']['_XYCoordinates'][-1]]]

		self._DesignParameter['m2_drain_vbp1']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0],_Datatype=DesignParameters._LayerMapping['METAL2'][1], _XYCoordinates=[], _Width=None)
		self._DesignParameter['m2_drain_vbp1']['_Width']=self._DesignParameter['via12_drain_vbp1']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth']
		self._DesignParameter['m2_drain_vbp1']['_XYCoordinates']=[[[self._DesignParameter['pmos_vbp1']['_XYCoordinates'][0][0]+self._DesignParameter['pmos_vbp1']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0], self._DesignParameter['via12_drain_vbp1']['_XYCoordinates'][0][1]], \
																   [self._DesignParameter['pmos_vbp1']['_XYCoordinates'][0][0]+self._DesignParameter['pmos_vbp1']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][-1][0], self._DesignParameter['via12_drain_vbp1']['_XYCoordinates'][0][1]]], \
																  [[self._DesignParameter['pmos_vbp1']['_XYCoordinates'][1][0]+self._DesignParameter['pmos_vbp1']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0], self._DesignParameter['via12_drain_vbp1']['_XYCoordinates'][-1][1]], \
																   [self._DesignParameter['pmos_vbp1']['_XYCoordinates'][1][0]+self._DesignParameter['pmos_vbp1']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][-1][0], self._DesignParameter['via12_drain_vbp1']['_XYCoordinates'][-1][1]]]]

		self._DesignParameter['m2_source_vbp1']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0],_Datatype=DesignParameters._LayerMapping['METAL2'][1], _XYCoordinates=[], _Width=None)
		self._DesignParameter['m2_source_vbp1']['_Width']=self._DesignParameter['via12_source_vbp1']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth']
		self._DesignParameter['m2_source_vbp1']['_XYCoordinates']=[[[self._DesignParameter['pmos_vbp1']['_XYCoordinates'][0][0]+self._DesignParameter['pmos_vbp1']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0], self._DesignParameter['via12_source_vbp1']['_XYCoordinates'][0][1]], \
																   [self._DesignParameter['pmos_vbp1']['_XYCoordinates'][0][0]+self._DesignParameter['pmos_vbp1']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][-1][0], self._DesignParameter['via12_source_vbp1']['_XYCoordinates'][0][1]]], \
																  [[self._DesignParameter['pmos_vbp1']['_XYCoordinates'][1][0]+self._DesignParameter['pmos_vbp1']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0], self._DesignParameter['via12_source_vbp1']['_XYCoordinates'][-1][1]], \
																   [self._DesignParameter['pmos_vbp1']['_XYCoordinates'][1][0]+self._DesignParameter['pmos_vbp1']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][-1][0], self._DesignParameter['via12_source_vbp1']['_XYCoordinates'][-1][1]]]]

		self._DesignParameter['m2_gate_vb2']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0],_Datatype=DesignParameters._LayerMapping['METAL2'][1], _XYCoordinates=[], _Width=None)
		self._DesignParameter['m2_gate_vb2']['_Width']=self._DesignParameter['via12_gate_vb2']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth']
		self._DesignParameter['m2_gate_vb2']['_XYCoordinates']=[[self._DesignParameter['via12_gate_vb2']['_XYCoordinates'][0], self._DesignParameter['via12_gate_vb2']['_XYCoordinates'][-2]],\
																[self._DesignParameter['via12_gate_vb2']['_XYCoordinates'][1], self._DesignParameter['via12_gate_vb2']['_XYCoordinates'][-1]]]

		self._DesignParameter['m2_source_vb2']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0],_Datatype=DesignParameters._LayerMapping['METAL2'][1], _XYCoordinates=[], _Width=None)
		self._DesignParameter['m2_source_vb2']['_Width']=self._DesignParameter['via12_source_vb2']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth']
		self._DesignParameter['m2_source_vb2']['_XYCoordinates']=[[self._DesignParameter['via12_source_vb2']['_XYCoordinates'][0], self._DesignParameter['via12_source_vb2']['_XYCoordinates'][-1]]]

		self._DesignParameter['m2_source_pdn_single']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0],_Datatype=DesignParameters._LayerMapping['METAL2'][1], _XYCoordinates=[], _Width=None)
		self._DesignParameter['m2_source_pdn_single']['_Width']=self._DesignParameter['via12_source_pdn_single']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth']
		self._DesignParameter['m2_source_pdn_single']['_XYCoordinates']=[[[self._DesignParameter['pmos_pdn_single_sw']['_XYCoordinates'][0][0]+self._DesignParameter['pmos_pdn_single_sw']['_DesignObj']._DesignParameter['_XYCoordinatePMOSSupplyRouting']['_XYCoordinates'][-1][0], self._DesignParameter['via12_source_pdn_single']['_XYCoordinates'][0][1]], \
																		  [self._DesignParameter['pmos_pdn_single_sw']['_XYCoordinates'][1][0]+self._DesignParameter['pmos_pdn_single_sw']['_DesignObj']._DesignParameter['_XYCoordinatePMOSSupplyRouting']['_XYCoordinates'][0][0], self._DesignParameter['via12_source_pdn_single']['_XYCoordinates'][0][1]]]]

		self._DesignParameter['via12_gate_vbn1']=self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='via12_gate_vbn1In{}'.format(_Name)))[0]
		ViaNumX=max(1,int(self.getXWidth('gate_vbn1','_Met1Layer')/(drc._VIAxMinWidth+drc._VIAxMinSpace)))
		self._DesignParameter['via12_gate_vbn1']['_DesignObj']._CalculateDesignParameterSameEnclosure( _ViaMet12Met2NumberOfCOX=ViaNumX, _ViaMet12Met2NumberOfCOY=1)
		tmp=[]
		for i in range(0, len(self._DesignParameter['nmos_vbn1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
			tmp.append([self._DesignParameter['nmos_vbn1']['_XYCoordinates'][0][0]+self._DesignParameter['nmos_vbn1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0], self._DesignParameter['gate_vbn1']['_XYCoordinates'][0][1]])
			tmp.append([-(self._DesignParameter['nmos_vbn1']['_XYCoordinates'][0][0]+self._DesignParameter['nmos_vbn1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0]), self._DesignParameter['gate_vbn1']['_XYCoordinates'][0][1]])
			tmp.append([self._DesignParameter['nmos_vbn1']['_XYCoordinates'][0][0]+self._DesignParameter['nmos_vbn1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0], self._DesignParameter['gate_vbn1']['_XYCoordinates'][1][1]])
			tmp.append([-(self._DesignParameter['nmos_vbn1']['_XYCoordinates'][0][0]+self._DesignParameter['nmos_vbn1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0]), self._DesignParameter['gate_vbn1']['_XYCoordinates'][1][1]])
		self._DesignParameter['via12_gate_vbn1']['_XYCoordinates']=tmp
		del tmp

		self._DesignParameter['m2_gate_vbn1']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0],_Datatype=DesignParameters._LayerMapping['METAL2'][1], _XYCoordinates=[], _Width=None)
		self._DesignParameter['m2_gate_vbn1']['_Width']=self._DesignParameter['via12_gate_vbn1']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth']
		self._DesignParameter['m2_gate_vbn1']['_XYCoordinates']=[[self._DesignParameter['via12_gate_vbn1']['_XYCoordinates'][0], self._DesignParameter['via12_gate_vbn1']['_XYCoordinates'][1]],\
																 [self._DesignParameter['via12_gate_vbn1']['_XYCoordinates'][2], self._DesignParameter['via12_gate_vbn1']['_XYCoordinates'][3]]]

		self._DesignParameter['via12_source_vbn1']=self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='via12_source_vbn1In{}'.format(_Name)))[0]
		self._DesignParameter['via12_source_vbn1']['_DesignObj']._CalculateDesignParameterSameEnclosure( _ViaMet12Met2NumberOfCOX=1, _ViaMet12Met2NumberOfCOY=2)
		tmp=[]
		for i in range(0, len(self._DesignParameter['nmos_vbn1']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'])):
			tmp.append([self._DesignParameter['nmos_vbn1']['_XYCoordinates'][0][0]+self._DesignParameter['nmos_vbn1']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][i][0], self._DesignParameter['nmos_vbn1']['_XYCoordinates'][0][1]-self.getYWidth('via12_source_vbn1','_Met2Layer')/2-drc._Metal1MinSpace3/2])
			tmp.append([-(self._DesignParameter['nmos_vbn1']['_XYCoordinates'][0][0]+self._DesignParameter['nmos_vbn1']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][i][0]), self._DesignParameter['nmos_vbn1']['_XYCoordinates'][0][1]-self.getYWidth('via12_source_vbn1','_Met2Layer')/2-drc._Metal1MinSpace3/2])
		self._DesignParameter['via12_source_vbn1']['_XYCoordinates']=tmp
		del tmp

		self._DesignParameter['via12_drain_vbn1']=self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='via12_drain_vbn1In{}'.format(_Name)))[0]
		self._DesignParameter['via12_drain_vbn1']['_DesignObj']._CalculateDesignParameterSameEnclosure( _ViaMet12Met2NumberOfCOX=1, _ViaMet12Met2NumberOfCOY=2)
		tmp=[]
		for i in range(0, len(self._DesignParameter['nmos_vbn1']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'])):
			tmp.append([self._DesignParameter['nmos_vbn1']['_XYCoordinates'][0][0]+self._DesignParameter['nmos_vbn1']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][i][0], self._DesignParameter['nmos_vbn1']['_XYCoordinates'][0][1]+self.getYWidth('via12_drain_vbn1','_Met2Layer')/2+drc._Metal1MinSpace3/2])
			tmp.append([-(self._DesignParameter['nmos_vbn1']['_XYCoordinates'][0][0]+self._DesignParameter['nmos_vbn1']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][i][0]), self._DesignParameter['nmos_vbn1']['_XYCoordinates'][0][1]+self.getYWidth('via12_drain_vbn1','_Met2Layer')/2+drc._Metal1MinSpace3/2])
		self._DesignParameter['via12_drain_vbn1']['_XYCoordinates']=tmp
		del tmp

		self._DesignParameter['via23_drain_vbn1_1']=self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_Name='via23_drain_vbn1_1{}'.format(_Name)))[0]
		self._DesignParameter['via23_drain_vbn1_1']['_DesignObj']._CalculateDesignParameterSameEnclosure( _ViaMet22Met3NumberOfCOX=1, _ViaMet22Met3NumberOfCOY=2)
		tmp=[]
		for i in range(0, len(self._DesignParameter['nmos_vbn1']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'])):
			tmp.append([-(self._DesignParameter['nmos_vbn1']['_XYCoordinates'][0][0]+self._DesignParameter['nmos_vbn1']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][i][0]), self._DesignParameter['via12_source_vbn1']['_XYCoordinates'][0][1]])
		self._DesignParameter['via23_drain_vbn1_1']['_XYCoordinates']=tmp
		del tmp

		self._DesignParameter['via34_drain_vbn1']=self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_Name='via34_drain_vbn1In{}'.format(_Name)))[0]
		self._DesignParameter['via34_drain_vbn1']['_DesignObj']._CalculateDesignParameterSameEnclosure( _ViaMet32Met4NumberOfCOX=1, _ViaMet32Met4NumberOfCOY=2)
		tmp=[]
		for i in range(0, len(self._DesignParameter['nmos_vbn1']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'])):
			tmp.append([-(self._DesignParameter['nmos_vbn1']['_XYCoordinates'][0][0]+self._DesignParameter['nmos_vbn1']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][i][0]), self._DesignParameter['via12_source_vbn1']['_XYCoordinates'][0][1]])
		self._DesignParameter['via34_drain_vbn1']['_XYCoordinates']=tmp
		del tmp


		self._DesignParameter['via12_gate_n0']=self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='via12_gate_n0In{}'.format(_Name)))[0]
		ViaNumX=max(1,int(self.getXWidth('gate_n0','_Met1Layer')/(drc._VIAxMinWidth+drc._VIAxMinSpace)))
		self._DesignParameter['via12_gate_n0']['_DesignObj']._CalculateDesignParameterSameEnclosure( _ViaMet12Met2NumberOfCOX=ViaNumX, _ViaMet12Met2NumberOfCOY=1)
		tmp=[]
		for i in range(0, len(self._DesignParameter['nmos_n0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
			tmp.append([self._DesignParameter['nmos_n0']['_XYCoordinates'][0][0]+self._DesignParameter['nmos_n0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0], self._DesignParameter['gate_n0']['_XYCoordinates'][0][1]])
			tmp.append([-(self._DesignParameter['nmos_n0']['_XYCoordinates'][0][0]+self._DesignParameter['nmos_n0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0]), self._DesignParameter['gate_n0']['_XYCoordinates'][0][1]])
			tmp.append([self._DesignParameter['nmos_n0']['_XYCoordinates'][0][0]+self._DesignParameter['nmos_n0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0], self._DesignParameter['gate_n0']['_XYCoordinates'][1][1]])
			tmp.append([-(self._DesignParameter['nmos_n0']['_XYCoordinates'][0][0]+self._DesignParameter['nmos_n0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0]), self._DesignParameter['gate_n0']['_XYCoordinates'][1][1]])
		self._DesignParameter['via12_gate_n0']['_XYCoordinates']=tmp
		del tmp

		self._DesignParameter['m2_gate_n0']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0],_Datatype=DesignParameters._LayerMapping['METAL2'][1], _XYCoordinates=[], _Width=None)
		self._DesignParameter['m2_gate_n0']['_Width']=self._DesignParameter['via12_gate_n0']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth']
		self._DesignParameter['m2_gate_n0']['_XYCoordinates']=[[self._DesignParameter['via12_gate_n0']['_XYCoordinates'][0], self._DesignParameter['via12_gate_n0']['_XYCoordinates'][1]],\
																 [self._DesignParameter['via12_gate_n0']['_XYCoordinates'][2], self._DesignParameter['via12_gate_n0']['_XYCoordinates'][3]]]

		self._DesignParameter['via12_drain_n0']=self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='via12_drain_n0In{}'.format(_Name)))[0]
		self._DesignParameter['via12_drain_n0']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX( _ViaMet12Met2NumberOfCOX=1, _ViaMet12Met2NumberOfCOY=2)
		tmp=[]
		for i in range(0, len(self._DesignParameter['nmos_n0']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'])):
			tmp.append([self._DesignParameter['nmos_n0']['_XYCoordinates'][0][0]+self._DesignParameter['nmos_n0']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][i][0], self._DesignParameter['via12_gate_n0']['_XYCoordinates'][-1][1]+self.getYWidth('via12_gate_n0','_Met2Layer')/2+self.getYWidth('via12_drain_n0','_Met2Layer')/2+drc._MetalxMinSpace5])
			tmp.append([-(self._DesignParameter['nmos_n0']['_XYCoordinates'][0][0]+self._DesignParameter['nmos_n0']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][i][0]), self._DesignParameter['via12_gate_n0']['_XYCoordinates'][-1][1]+self.getYWidth('via12_gate_n0','_Met2Layer')/2+self.getYWidth('via12_drain_n0','_Met2Layer')/2+drc._MetalxMinSpace5])
		self._DesignParameter['via12_drain_n0']['_XYCoordinates']=tmp
		del tmp

		self._DesignParameter['via12_source_n0']=self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='via12_source_n0In{}'.format(_Name)))[0]
		self._DesignParameter['via12_source_n0']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX( _ViaMet12Met2NumberOfCOX=1, _ViaMet12Met2NumberOfCOY=3)
		tmp=[]
		for i in range(0, len(self._DesignParameter['nmos_n0']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'])):
			tmp.append([self._DesignParameter['nmos_n0']['_XYCoordinates'][0][0]+self._DesignParameter['nmos_n0']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][i][0], self._DesignParameter['via12_gate_n0']['_XYCoordinates'][0][1]-self.getYWidth('via12_gate_n0','_Met2Layer')/2-self.getYWidth('via12_source_n0','_Met2Layer')/2-drc._MetalxMinSpace5])
			tmp.append([-(self._DesignParameter['nmos_n0']['_XYCoordinates'][0][0]+self._DesignParameter['nmos_n0']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][i][0]), self._DesignParameter['via12_gate_n0']['_XYCoordinates'][0][1]-self.getYWidth('via12_gate_n0','_Met2Layer')/2-self.getYWidth('via12_source_n0','_Met2Layer')/2-drc._MetalxMinSpace5])
		self._DesignParameter['via12_source_n0']['_XYCoordinates']=tmp
		del tmp

		self._DesignParameter['via12_n0_guardring1']=self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='via12_n0_guardring1In{}'.format(_Name)))[0]
		self._DesignParameter['via12_n0_guardring1']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX( _ViaMet12Met2NumberOfCOX=1, _ViaMet12Met2NumberOfCOY=3)
		self._DesignParameter['via12_n0_guardring1']['_XYCoordinates']=[[self.getXY('pguardring1','right')[0][0], self._DesignParameter['via12_source_n0']['_XYCoordinates'][0][1]]]

		self._DesignParameter['via12_gate_vb1']=self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='via12_gate_vb1In{}'.format(_Name)))[0]
		ViaNumX=max(1,int(self.getXWidth('gate_vb1','_Met1Layer')/(drc._VIAxMinWidth+drc._VIAxMinSpace)))
		self._DesignParameter['via12_gate_vb1']['_DesignObj']._CalculateDesignParameterSameEnclosure( _ViaMet12Met2NumberOfCOX=ViaNumX, _ViaMet12Met2NumberOfCOY=1)
		tmp=[]
		for i in range(0, len(self._DesignParameter['nmos_vb1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
			tmp.append([self._DesignParameter['nmos_vb1']['_XYCoordinates'][0][0]+self._DesignParameter['nmos_vb1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0], self._DesignParameter['gate_vb1']['_XYCoordinates'][0][1]])
			tmp.append([self._DesignParameter['nmos_vb1']['_XYCoordinates'][0][0]+self._DesignParameter['nmos_vb1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0], self._DesignParameter['gate_vb1']['_XYCoordinates'][1][1]])
		self._DesignParameter['via12_gate_vb1']['_XYCoordinates']=tmp
		del tmp

		self._DesignParameter['m2_gate_vb1']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0],_Datatype=DesignParameters._LayerMapping['METAL2'][1], _XYCoordinates=[], _Width=None)
		self._DesignParameter['m2_gate_vb1']['_Width']=self._DesignParameter['via12_gate_vb1']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth']
		self._DesignParameter['m2_gate_vb1']['_XYCoordinates']=[[self._DesignParameter['via12_gate_vb1']['_XYCoordinates'][0], self._DesignParameter['via12_gate_vb1']['_XYCoordinates'][-2]],\
																[self._DesignParameter['via12_gate_vb1']['_XYCoordinates'][1], self._DesignParameter['via12_gate_vb1']['_XYCoordinates'][-1]]]

		self._DesignParameter['m2_source_vbn1']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0],_Datatype=DesignParameters._LayerMapping['METAL2'][1], _XYCoordinates=[], _Width=None)
		self._DesignParameter['m2_source_vbn1']['_Width']=self._DesignParameter['via12_source_vbn1']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth']
		self._DesignParameter['m2_source_vbn1']['_XYCoordinates']=[[self._DesignParameter['via12_source_vbn1']['_XYCoordinates'][0], [self._DesignParameter['nmos_vbn1']['_XYCoordinates'][0][0]+self._DesignParameter['nmos_vbn1']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][-1][0], self._DesignParameter['via12_source_vbn1']['_XYCoordinates'][0][1]]],\
																[[self._DesignParameter['nmos_vbn1']['_XYCoordinates'][1][0]+self._DesignParameter['nmos_vbn1']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0], self._DesignParameter['via12_source_vbn1']['_XYCoordinates'][0][1]], self._DesignParameter['via12_source_vbn1']['_XYCoordinates'][1]]]

		self._DesignParameter['m2_drain_n0']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0],_Datatype=DesignParameters._LayerMapping['METAL2'][1], _XYCoordinates=[], _Width=None)
		self._DesignParameter['m2_drain_n0']['_Width']=self._DesignParameter['via12_drain_n0']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth']
		self._DesignParameter['m2_drain_n0']['_XYCoordinates']=[[[self._DesignParameter['nmos_n0']['_XYCoordinates'][0][0]+self._DesignParameter['nmos_n0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0], self._DesignParameter['via12_drain_n0']['_XYCoordinates'][0][1]], \
																   [self._DesignParameter['nmos_n0']['_XYCoordinates'][0][0]+self._DesignParameter['nmos_n0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][-1][0], self._DesignParameter['via12_drain_n0']['_XYCoordinates'][0][1]]], \
																  [[self._DesignParameter['nmos_n0']['_XYCoordinates'][1][0]+self._DesignParameter['nmos_n0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0], self._DesignParameter['via12_drain_n0']['_XYCoordinates'][-1][1]], \
																   [self._DesignParameter['nmos_n0']['_XYCoordinates'][1][0]+self._DesignParameter['nmos_n0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][-1][0], self._DesignParameter['via12_drain_n0']['_XYCoordinates'][-1][1]]]]

		self._DesignParameter['m2_source_n0']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0],_Datatype=DesignParameters._LayerMapping['METAL2'][1], _XYCoordinates=[], _Width=None)
		self._DesignParameter['m2_source_n0']['_Width']=self._DesignParameter['via12_source_n0']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth']
		self._DesignParameter['m2_source_n0']['_XYCoordinates']=[[[self.getXY('nmos_n0','_Met1Layer')[0][0], self._DesignParameter['via12_source_n0']['_XYCoordinates'][0][1]], [self.getXY('pguardring1','right')[0][0], self._DesignParameter['via12_source_n0']['_XYCoordinates'][0][1]]]]

		self._DesignParameter['m2_drain_vbn1']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0],_Datatype=DesignParameters._LayerMapping['METAL2'][1], _XYCoordinates=[], _Width=None)
		self._DesignParameter['m2_drain_vbn1']['_Width']=self._DesignParameter['via12_drain_vbn1']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth']
		self._DesignParameter['m2_drain_vbn1']['_XYCoordinates']=[[[self._DesignParameter['nmos_vbn1']['_XYCoordinates'][0][0]+self._DesignParameter['nmos_vbn1']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0], self._DesignParameter['via12_drain_vbn1']['_XYCoordinates'][0][1]], \
																   [self._DesignParameter['nmos_vbn1']['_XYCoordinates'][0][0]+self._DesignParameter['nmos_vbn1']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][-1][0], self._DesignParameter['via12_drain_vbn1']['_XYCoordinates'][0][1]]], \
																  [[self._DesignParameter['nmos_vbn1']['_XYCoordinates'][1][0]+self._DesignParameter['nmos_vbn1']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0], self._DesignParameter['via12_drain_vbn1']['_XYCoordinates'][-1][1]], \
																   [self._DesignParameter['nmos_vbn1']['_XYCoordinates'][1][0]+self._DesignParameter['nmos_vbn1']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][-1][0], self._DesignParameter['via12_drain_vbn1']['_XYCoordinates'][-1][1]]]]

		self._DesignParameter['via23_drain_vbp1']=self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_Name='via23_drain_vbp1In{}'.format(_Name)))[0]
		ViaNumY=max(2,int(self.getWidth('m2_drain_vbp1')/(drc._VIAxMinSpace+drc._VIAxMinWidth)))
		self._DesignParameter['via23_drain_vbp1']['_DesignObj']._CalculateDesignParameterSameEnclosure( _ViaMet22Met3NumberOfCOX=ViaNumY, _ViaMet22Met3NumberOfCOY=ViaNumY)
		self._DesignParameter['via23_drain_vbp1']['_XYCoordinates']=[[self._DesignParameter['pmos_vbp1']['_XYCoordinates'][0][0]+self._DesignParameter['pmos_vbp1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][-1][0], self._DesignParameter['m2_drain_vbp1']['_XYCoordinates'][0][0][1]], \
																	 [self._DesignParameter['pmos_vbp1']['_XYCoordinates'][1][0]+self._DesignParameter['pmos_vbp1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0], self._DesignParameter['m2_drain_vbp1']['_XYCoordinates'][0][0][1]]]

		self._DesignParameter['via23_gate_n0']=self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_Name='via23_gate_n0In{}'.format(_Name)))[0]
		ViaNumY=max(2,int(self.getWidth('m2_gate_n0')/(drc._VIAxMinSpace+drc._VIAxMinWidth)))
		self._DesignParameter['via23_gate_n0']['_DesignObj']._CalculateDesignParameterSameEnclosure( _ViaMet22Met3NumberOfCOX=ViaNumY, _ViaMet22Met3NumberOfCOY=1)
		self._DesignParameter['via23_gate_n0']['_XYCoordinates']=[[self._DesignParameter['via23_drain_vbp1']['_XYCoordinates'][0][0], self._DesignParameter['m2_gate_n0']['_XYCoordinates'][1][0][1]]] ##+self.getYWidth('via23_gate_n0','_Met2Layer')/2-self._DesignParameter['m2_gate_n0']['_Width']/2]]

		self._DesignParameter['via23_drain_vbn1']=self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_Name='via23_drain_vbn1In{}'.format(_Name)))[0]
		ViaNumY=max(2,int(self.getWidth('m2_drain_vbn1')/(drc._VIAxMinSpace+drc._VIAxMinWidth)))
		self._DesignParameter['via23_drain_vbn1']['_DesignObj']._CalculateDesignParameterSameEnclosure( _ViaMet22Met3NumberOfCOX=ViaNumY, _ViaMet22Met3NumberOfCOY=ViaNumY)
		self._DesignParameter['via23_drain_vbn1']['_XYCoordinates']=[[self._DesignParameter['via23_drain_vbp1']['_XYCoordinates'][0][0], self._DesignParameter['m2_drain_vbn1']['_XYCoordinates'][0][0][1]],\
																	 [self._DesignParameter['via23_drain_vbp1']['_XYCoordinates'][1][0], self._DesignParameter['m2_source_vbn1']['_XYCoordinates'][1][0][1]]]

		self._DesignParameter['m3_vbp1_n0']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0],_Datatype=DesignParameters._LayerMapping['METAL3'][1], _XYCoordinates=[], _Width=None)
		self._DesignParameter['m3_vbp1_n0']['_Width']=self._DesignParameter['via23_drain_vbp1']['_DesignObj']._DesignParameter['_Met3Layer']['_XWidth']
		self._DesignParameter['m3_vbp1_n0']['_XYCoordinates']=[[self._DesignParameter['via23_drain_vbp1']['_XYCoordinates'][0], self._DesignParameter['via23_gate_n0']['_XYCoordinates'][0]]]

		self._DesignParameter['m3_vbp1_vbn1']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0],_Datatype=DesignParameters._LayerMapping['METAL3'][1], _XYCoordinates=[], _Width=None)
		self._DesignParameter['m3_vbp1_vbn1']['_Width']=self._DesignParameter['via23_drain_vbp1']['_DesignObj']._DesignParameter['_Met3Layer']['_XWidth']
		self._DesignParameter['m3_vbp1_vbn1']['_XYCoordinates']=[[self._DesignParameter['via23_drain_vbp1']['_XYCoordinates'][1], self._DesignParameter['via23_drain_vbn1']['_XYCoordinates'][1]]]

		self._DesignParameter['via23_pdn_pair_sw']=self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_Name='via23_pdn_pair_swIn{}'.format(_Name)))[0]
		ViaNumY=max(2,int(self.getWidth('m2_vbp_pdn_pair')/(drc._VIAxMinSpace+drc._VIAxMinWidth)))
		self._DesignParameter['via23_pdn_pair_sw']['_DesignObj']._CalculateDesignParameterSameEnclosure( _ViaMet22Met3NumberOfCOX=ViaNumY, _ViaMet22Met3NumberOfCOY=ViaNumY)
		self._DesignParameter['via23_pdn_pair_sw']['_XYCoordinates']=[[self._DesignParameter['via23_drain_vbp1']['_XYCoordinates'][0][0]-self.getXWidth('via23_drain_vbp1','_Met3Layer')/2-self.getXWidth('via23_pdn_pair_sw','_Met3Layer')/2-drc._MetalxMinSpace3, self._DesignParameter['m2_vbp_pdn_pair']['_XYCoordinates'][0][0][1]],\
																	  [self._DesignParameter['via23_drain_vbp1']['_XYCoordinates'][1][0]+self.getXWidth('via23_drain_vbp1','_Met3Layer')/2+self.getXWidth('via23_pdn_pair_sw','_Met3Layer')/2+drc._MetalxMinSpace3, self._DesignParameter['m2_vbp_pdn_pair']['_XYCoordinates'][0][0][1]]]

		self._DesignParameter['m1_vb2_y']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0],_Datatype=DesignParameters._LayerMapping['METAL1'][1], _XYCoordinates=[], _Width=None)
		self._DesignParameter['m1_vb2_y']['_Width']=self.getXWidth('pmos_vb2','_Met1Layer')
		tmp=[]
		for i in range(0, len(self._DesignParameter['pmos_vb2']['_DesignObj']._DesignParameter['_XYCoordinatePMOSSupplyRouting']['_XYCoordinates'])):
			tmp.append([[self._DesignParameter['pmos_vb2']['_XYCoordinates'][0][0]+self._DesignParameter['pmos_vb2']['_DesignObj']._DesignParameter['_XYCoordinatePMOSSupplyRouting']['_XYCoordinates'][i][0], self._DesignParameter['pmos_vb2']['_XYCoordinates'][0][1]+self._DesignParameter['pmos_vb2']['_DesignObj']._DesignParameter['_XYCoordinatePMOSSupplyRouting']['_XYCoordinates'][i][1]], \
						[self._DesignParameter['pmos_vb2']['_XYCoordinates'][0][0]+self._DesignParameter['pmos_vb2']['_DesignObj']._DesignParameter['_XYCoordinatePMOSSupplyRouting']['_XYCoordinates'][i][0], self._DesignParameter['pmos_pdn_pair_sw']['_XYCoordinates'][0][1]]])
		self._DesignParameter['m1_vb2_y']['_XYCoordinates']=tmp
		del tmp

		self._DesignParameter['m1_input_y']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0],_Datatype=DesignParameters._LayerMapping['METAL1'][1], _XYCoordinates=[], _Width=None)
		self._DesignParameter['m1_input_y']['_Width']=self.getXWidth('pmos_input','_Met1Layer')
		tmp=[]
		for i in range(0, len(self._DesignParameter['pmos_input']['_DesignObj']._DesignParameter['_XYCoordinatePMOSSupplyRouting']['_XYCoordinates'])):
			tmp.append([[self._DesignParameter['pmos_input']['_XYCoordinates'][1][0]+self._DesignParameter['pmos_input']['_DesignObj']._DesignParameter['_XYCoordinatePMOSSupplyRouting']['_XYCoordinates'][i][0], self._DesignParameter['pmos_input']['_XYCoordinates'][1][1]+self._DesignParameter['pmos_input']['_DesignObj']._DesignParameter['_XYCoordinatePMOSSupplyRouting']['_XYCoordinates'][i][1]], \
						[self._DesignParameter['pmos_input']['_XYCoordinates'][1][0]+self._DesignParameter['pmos_input']['_DesignObj']._DesignParameter['_XYCoordinatePMOSSupplyRouting']['_XYCoordinates'][i][0], self._DesignParameter['pmos_pdn_pair_sw']['_XYCoordinates'][0][1]]])
		self._DesignParameter['m1_input_y']['_XYCoordinates']=tmp
		del tmp

		self._DesignParameter['m1_input_vb2_x']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0],_Datatype=DesignParameters._LayerMapping['METAL1'][1], _XYCoordinates=[], _Width=None)
		self._DesignParameter['m1_input_vb2_x']['_Width']=self.getXWidth('pmos_input','_Met1Layer')
		self._DesignParameter['m1_input_vb2_x']['_XYCoordinates']=[[[min(self._DesignParameter['m1_input_y']['_XYCoordinates'][0][0][0]-self._DesignParameter['m1_input_y']['_Width']/2, self._DesignParameter['m1_vb2_y']['_XYCoordinates'][0][0][0]-self._DesignParameter['m1_vb2_y']['_Width']/2), self._DesignParameter['pmos_pdn_pair_sw']['_XYCoordinates'][0][1]], \
																	[max(self._DesignParameter['m1_input_y']['_XYCoordinates'][-1][0][0]+self._DesignParameter['m1_input_y']['_Width']/2, self._DesignParameter['m1_vb2_y']['_XYCoordinates'][-1][0][0]+self._DesignParameter['m1_vb2_y']['_Width']/2), self._DesignParameter['pmos_pdn_pair_sw']['_XYCoordinates'][0][1]]]]

		self._DesignParameter['m1_vb1_y']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0],_Datatype=DesignParameters._LayerMapping['METAL1'][1], _XYCoordinates=[], _Width=None)
		self._DesignParameter['m1_vb1_y']['_Width']=self.getXWidth('nmos_vb1','_Met1Layer')
		tmp=[]
		for i in range(0, len(self._DesignParameter['nmos_vb1']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'])):
			tmp.append([[self._DesignParameter['nmos_vb1']['_XYCoordinates'][0][0]+self._DesignParameter['nmos_vb1']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][i][0], self._DesignParameter['nmos_vb1']['_XYCoordinates'][0][1]+self._DesignParameter['nmos_vb1']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][i][1]], \
						[self._DesignParameter['nmos_vb1']['_XYCoordinates'][0][0]+self._DesignParameter['nmos_vb1']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][i][0], (self._DesignParameter['gate_ninputn']['_XYCoordinates'][0][1]+self._DesignParameter['gate_vb1']['_XYCoordinates'][1][1])/2]])
		self._DesignParameter['m1_vb1_y']['_XYCoordinates']=tmp
		del tmp

		self._DesignParameter['m1_ninput_y']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0],_Datatype=DesignParameters._LayerMapping['METAL1'][1], _XYCoordinates=[], _Width=None)
		self._DesignParameter['m1_ninput_y']['_Width']=self.getXWidth('nmos_input','_Met1Layer')
		tmp=[]
		for i in range(0, len(self._DesignParameter['nmos_input']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'])):
			tmp.append([[self._DesignParameter['nmos_input']['_XYCoordinates'][0][0]+self._DesignParameter['nmos_input']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][i][0], self._DesignParameter['nmos_input']['_XYCoordinates'][0][1]+self._DesignParameter['nmos_input']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][i][1]], \
						[self._DesignParameter['nmos_input']['_XYCoordinates'][0][0]+self._DesignParameter['nmos_input']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][i][0], (self._DesignParameter['gate_ninputn']['_XYCoordinates'][0][1]+self._DesignParameter['gate_vb1']['_XYCoordinates'][1][1])/2]])
		self._DesignParameter['m1_ninput_y']['_XYCoordinates']=tmp
		del tmp

		self._DesignParameter['m1_ninput_vb1_x']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0],_Datatype=DesignParameters._LayerMapping['METAL1'][1], _XYCoordinates=[], _Width=None)
		self._DesignParameter['m1_ninput_vb1_x']['_Width']=self.getXWidth('nmos_input','_Met1Layer')
		self._DesignParameter['m1_ninput_vb1_x']['_XYCoordinates']=[[[min(self._DesignParameter['m1_ninput_y']['_XYCoordinates'][0][0][0]-self._DesignParameter['m1_ninput_y']['_Width']/2, self._DesignParameter['m1_vb1_y']['_XYCoordinates'][0][0][0]-self._DesignParameter['m1_vb1_y']['_Width']/2), (self._DesignParameter['gate_ninputn']['_XYCoordinates'][0][1]+self._DesignParameter['gate_vb1']['_XYCoordinates'][1][1])/2], \
																	[max(self._DesignParameter['m1_ninput_y']['_XYCoordinates'][-1][0][0]+self._DesignParameter['m1_ninput_y']['_Width']/2, self._DesignParameter['m1_vb1_y']['_XYCoordinates'][-1][0][0]+self._DesignParameter['m1_vb1_y']['_Width']/2), (self._DesignParameter['gate_ninputn']['_XYCoordinates'][0][1]+self._DesignParameter['gate_vb1']['_XYCoordinates'][1][1])/2]]]

		self._DesignParameter['m1_drain_vb1']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0],_Datatype=DesignParameters._LayerMapping['METAL1'][1], _XYCoordinates=[], _Width=None)
		self._DesignParameter['m1_drain_vb1']['_Width']=self.getXWidth('nmos_vb1','_Met1Layer')
		tmp=[]
		for i in range(0,len(self._DesignParameter['nmos_vb1']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'])):
			tmp.append([[self._DesignParameter['nmos_vb1']['_XYCoordinates'][0][0]+self._DesignParameter['nmos_vb1']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][i][0], self._DesignParameter['nmos_vb1']['_XYCoordinates'][0][1]+self._DesignParameter['nmos_vb1']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][i][1]], \
						[self._DesignParameter['nmos_vb1']['_XYCoordinates'][0][0]+self._DesignParameter['nmos_vb1']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][i][0], self.getXY('pguardring1','top')[0][1]]])
		self._DesignParameter['m1_drain_vb1']['_XYCoordinates']=tmp
		del tmp


		self._DesignParameter['via23_inputn']=self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_Name='via23_inputnIn{}'.format(_Name)))[0]
		self._DesignParameter['via23_inputn']['_DesignObj']._CalculateDesignParameterSameEnclosure( _ViaMet22Met3NumberOfCOX=2, _ViaMet22Met3NumberOfCOY=2)
		self._DesignParameter['via23_inputn']['_XYCoordinates']=[self._DesignParameter['m2_drain_input']['_XYCoordinates'][0][1]]

		self._DesignParameter['via23_inputp']=self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_Name='via23_inputpIn{}'.format(_Name)))[0]
		self._DesignParameter['via23_inputp']['_DesignObj']._CalculateDesignParameterSameEnclosure( _ViaMet22Met3NumberOfCOX=2, _ViaMet22Met3NumberOfCOY=2)
		self._DesignParameter['via23_inputp']['_XYCoordinates']=[self._DesignParameter['m2_drain_input']['_XYCoordinates'][1][1]]

		self._DesignParameter['via23_input_n0']=self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_Name='via23_input_n0In{}'.format(_Name)))[0]
		self._DesignParameter['via23_input_n0']['_DesignObj']._CalculateDesignParameterSameEnclosure( _ViaMet22Met3NumberOfCOX=2, _ViaMet22Met3NumberOfCOY=2)
		self._DesignParameter['via23_input_n0']['_XYCoordinates']=[[self._DesignParameter['via23_inputp']['_XYCoordinates'][0][0], self.CeilMinSnapSpacing((self._DesignParameter['via12_gate_vbn1']['_XYCoordinates'][0][1]+self._DesignParameter['via12_gate_n0']['_XYCoordinates'][-1][1])/2, MinSnapSpacing)], [self._DesignParameter['via23_inputn']['_XYCoordinates'][0][0], self.CeilMinSnapSpacing(max(self._DesignParameter['via12_gate_vbp1']['_XYCoordinates'][0][1], self._DesignParameter['via12_gate_inputn']['_XYCoordinates'][0][1])+self.getYWidth('via12_gate_vbp1','_Met2Layer')/2+self.getYWidth('via23_input_n0','_Met2Layer')/2+drc._MetalxMinSpace3, MinSnapSpacing)]]

		self._DesignParameter['m3_input']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0],_Datatype=DesignParameters._LayerMapping['METAL3'][1], _XYCoordinates=[], _Width=None)
		self._DesignParameter['m3_input']['_Width']=self.getXWidth('via23_inputp','_Met3Layer')
		self._DesignParameter['m3_input']['_XYCoordinates']=[[[self._DesignParameter['via23_inputn']['_XYCoordinates'][0][0], self._DesignParameter['via23_inputn']['_XYCoordinates'][0][1]], [self._DesignParameter['via23_input_n0']['_XYCoordinates'][1][0], self._DesignParameter['via23_input_n0']['_XYCoordinates'][1][1]]],\
															  [[self._DesignParameter['via23_inputp']['_XYCoordinates'][0][0], self._DesignParameter['via23_inputp']['_XYCoordinates'][0][1]], [self._DesignParameter['via23_input_n0']['_XYCoordinates'][0][0], self._DesignParameter['via23_input_n0']['_XYCoordinates'][0][1]]]]

		self._DesignParameter['via23_input_n0_2']=self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_Name='via23_input_n0_2In{}'.format(_Name)))[0]
		self._DesignParameter['via23_input_n0_2']['_DesignObj']._CalculateDesignParameterSameEnclosure( _ViaMet22Met3NumberOfCOX=2, _ViaMet22Met3NumberOfCOY=2)
		self._DesignParameter['via23_input_n0_2']['_XYCoordinates']=[[self._DesignParameter['via23_gate_n0']['_XYCoordinates'][0][0]-self.getXWidth('via23_gate_n0','_Met3Layer')/2-self.getXWidth('via23_input_n0_2','_Met3Layer')/2-drc._MetalxMinSpace3, self._DesignParameter['via23_input_n0']['_XYCoordinates'][1][1]], [self._DesignParameter['via23_drain_vbn1']['_XYCoordinates'][1][0]+self.getXWidth('via23_drain_vbn1','_Met3Layer')/2+self.getXWidth('via23_input_n0_2','_Met3Layer')/2+drc._MetalxMinSpace3, self._DesignParameter['via23_input_n0']['_XYCoordinates'][0][1]]]


		self._DesignParameter['m2_input_n0']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0],_Datatype=DesignParameters._LayerMapping['METAL2'][1], _XYCoordinates=[], _Width=None)
		self._DesignParameter['m2_input_n0']['_Width']=self.getYWidth('via23_input_n0_2','_Met2Layer')
		self._DesignParameter['m2_input_n0']['_XYCoordinates']=[[self._DesignParameter['via23_input_n0']['_XYCoordinates'][1], self._DesignParameter['via23_input_n0_2']['_XYCoordinates'][0]], \
																[self._DesignParameter['via23_input_n0']['_XYCoordinates'][0], self._DesignParameter['via23_input_n0_2']['_XYCoordinates'][1]]]

		self._DesignParameter['via23_drain_n0']=self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_Name='via23_drain_n0In{}'.format(_Name)))[0]
		self._DesignParameter['via23_drain_n0']['_DesignObj']._CalculateDesignParameterSameEnclosure( _ViaMet22Met3NumberOfCOX=2, _ViaMet22Met3NumberOfCOY=2)
		self._DesignParameter['via23_drain_n0']['_XYCoordinates']=[[self._DesignParameter['via23_input_n0_2']['_XYCoordinates'][0][0], self._DesignParameter['m2_drain_n0']['_XYCoordinates'][0][0][1]], [self._DesignParameter['via23_input_n0_2']['_XYCoordinates'][1][0], self._DesignParameter['m2_drain_n0']['_XYCoordinates'][0][0][1]]]

		self._DesignParameter['via23_ninputn']=self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_Name='via23_ninputnIn{}'.format(_Name)))[0]
		self._DesignParameter['via23_ninputn']['_DesignObj']._CalculateDesignParameterSameEnclosure( _ViaMet22Met3NumberOfCOX=2, _ViaMet22Met3NumberOfCOY=2)
		self._DesignParameter['via23_ninputn']['_XYCoordinates']=[[self.getXY('pguardring2','left')[0][0], self._DesignParameter['via12_drain_ninputn']['_XYCoordinates'][0][1]]]

		self._DesignParameter['via23_ninputp']=self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_Name='via23_ninputpIn{}'.format(_Name)))[0]
		self._DesignParameter['via23_ninputp']['_DesignObj']._CalculateDesignParameterSameEnclosure( _ViaMet22Met3NumberOfCOX=2, _ViaMet22Met3NumberOfCOY=2)
		self._DesignParameter['via23_ninputp']['_XYCoordinates']=[[self._DesignParameter['via23_ninputn']['_XYCoordinates'][0][0]+self.getXWidth('via23_ninputn','_Met3Layer')/2+self.getXWidth('via23_ninputp','_Met3Layer')/2+drc._MetalxMinSpace3, self._DesignParameter['via12_drain_ninputp']['_XYCoordinates'][0][1]]]

		self._DesignParameter['m2_ninput']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0],_Datatype=DesignParameters._LayerMapping['METAL2'][1], _XYCoordinates=[], _Width=None)
		self._DesignParameter['m2_ninput']['_Width']=self.getYWidth('via23_ninputp','_Met2Layer')
		self._DesignParameter['m2_ninput']['_XYCoordinates']=[[self._DesignParameter['via12_drain_ninputp']['_XYCoordinates'][-1], self._DesignParameter['via23_ninputp']['_XYCoordinates'][0]], \
															  [self._DesignParameter['via12_drain_ninputn']['_XYCoordinates'][-1], self._DesignParameter['via23_ninputn']['_XYCoordinates'][0]]]

		self._DesignParameter['via34_ninput_pdn_pair_sw']=self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_Name='via34_ninput_pdn_pair_swIn{}'.format(_Name)))[0]
		self._DesignParameter['via34_ninput_pdn_pair_sw']['_DesignObj']._CalculateDesignParameterSameEnclosure( _ViaMet32Met4NumberOfCOX=2, _ViaMet32Met4NumberOfCOY=2)
		self._DesignParameter['via34_ninput_pdn_pair_sw']['_XYCoordinates']=[[self._DesignParameter['via23_ninputn']['_XYCoordinates'][0][0], self._DesignParameter['via23_input_n0']['_XYCoordinates'][1][1]+self.getYWidth('via23_input_n0','_Met3Layer')/2+self.getYWidth('via34_ninput_pdn_pair_sw','_Met3Layer')/2+drc._MetalxMinSpace3], [self._DesignParameter['via23_ninputp']['_XYCoordinates'][0][0], self._DesignParameter['via23_input_n0']['_XYCoordinates'][0][1]+self.getYWidth('via23_input_n0','_Met2Layer')/2+self.getYWidth('via23_ninputp','_Met2Layer')/2+drc._MetalxMinSpace3]]

		self._DesignParameter['m3_ninput']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0],_Datatype=DesignParameters._LayerMapping['METAL3'][1], _XYCoordinates=[], _Width=None)
		self._DesignParameter['m3_ninput']['_Width']=self.getXWidth('via34_ninput_pdn_pair_sw','_Met3Layer')
		self._DesignParameter['m3_ninput']['_XYCoordinates']=[[[self._DesignParameter['via23_ninputn']['_XYCoordinates'][0][0], self._DesignParameter['via23_ninputn']['_XYCoordinates'][0][1]], [self._DesignParameter['via34_ninput_pdn_pair_sw']['_XYCoordinates'][0][0], self._DesignParameter['via34_ninput_pdn_pair_sw']['_XYCoordinates'][0][1]]],\
															  [[self._DesignParameter['via23_ninputp']['_XYCoordinates'][0][0], self._DesignParameter['via23_ninputp']['_XYCoordinates'][0][1]], [self._DesignParameter['via34_ninput_pdn_pair_sw']['_XYCoordinates'][1][0], self._DesignParameter['via34_ninput_pdn_pair_sw']['_XYCoordinates'][1][1]]]]

		self._DesignParameter['via34_ninput_pdn_pair_sw_2']=self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_Name='via34_ninput_pdn_pair_sw_2In{}'.format(_Name)))[0]
		self._DesignParameter['via34_ninput_pdn_pair_sw_2']['_DesignObj']._CalculateDesignParameterSameEnclosure( _ViaMet32Met4NumberOfCOX=2, _ViaMet32Met4NumberOfCOY=2)
		self._DesignParameter['via34_ninput_pdn_pair_sw_2']['_XYCoordinates']=[[self._DesignParameter['via23_input_n0_2']['_XYCoordinates'][0][0]-self.getXWidth('via23_input_n0_2','_Met3Layer')/2-self.getXWidth('via34_ninput_pdn_pair_sw_2','_Met3Layer')/2-drc._MetalxMinSpace3, self._DesignParameter['via34_ninput_pdn_pair_sw']['_XYCoordinates'][0][1]], [self._DesignParameter['via23_input_n0_2']['_XYCoordinates'][1][0]+self.getXWidth('via23_input_n0_2','_Met3Layer')/2+self.getXWidth('via34_ninput_pdn_pair_sw_2','_Met3Layer')/2+drc._MetalxMinSpace3, self._DesignParameter['via34_ninput_pdn_pair_sw']['_XYCoordinates'][1][1]]]

		self._DesignParameter['m4_ninput_pdn_pair_sw_2']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL4'][0],_Datatype=DesignParameters._LayerMapping['METAL4'][1], _XYCoordinates=[], _Width=None)
		self._DesignParameter['m4_ninput_pdn_pair_sw_2']['_Width']=self.getYWidth('via34_ninput_pdn_pair_sw_2','_Met4Layer')
		self._DesignParameter['m4_ninput_pdn_pair_sw_2']['_XYCoordinates']=[[self._DesignParameter['via34_ninput_pdn_pair_sw']['_XYCoordinates'][0], self._DesignParameter['via34_ninput_pdn_pair_sw_2']['_XYCoordinates'][0]], \
																			[self._DesignParameter['via34_ninput_pdn_pair_sw']['_XYCoordinates'][1], self._DesignParameter['via34_ninput_pdn_pair_sw_2']['_XYCoordinates'][1]]]

		self._DesignParameter['via23_pdn_pair_sw']['_XYCoordinates']=[[self._DesignParameter['via34_ninput_pdn_pair_sw_2']['_XYCoordinates'][0][0], self._DesignParameter['via23_pdn_pair_sw']['_XYCoordinates'][0][1]], [self._DesignParameter['via34_ninput_pdn_pair_sw_2']['_XYCoordinates'][1][0], self._DesignParameter['via23_pdn_pair_sw']['_XYCoordinates'][1][1]]]

		self._DesignParameter['via23_drain_pdn_pair_sw']=self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_Name='via23_drain_pdn_pair_swIn{}'.format(_Name)))[0]
		self._DesignParameter['via23_drain_pdn_pair_sw']['_DesignObj']._CalculateDesignParameterSameEnclosure( _ViaMet22Met3NumberOfCOX=2, _ViaMet22Met3NumberOfCOY=2)
		self._DesignParameter['via23_drain_pdn_pair_sw']['_XYCoordinates']=self._DesignParameter['via23_pdn_pair_sw']['_XYCoordinates']

		self._DesignParameter['m3_pdn_pair_sw']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0],_Datatype=DesignParameters._LayerMapping['METAL3'][1], _XYCoordinates=[], _Width=None)
		self._DesignParameter['m3_pdn_pair_sw']['_Width']=self.getXWidth('via23_drain_pdn_pair_sw','_Met3Layer')
		self._DesignParameter['m3_pdn_pair_sw']['_XYCoordinates']=[[[self._DesignParameter['via34_ninput_pdn_pair_sw_2']['_XYCoordinates'][0][0], self._DesignParameter['via34_ninput_pdn_pair_sw_2']['_XYCoordinates'][0][1]], [self._DesignParameter['via23_drain_pdn_pair_sw']['_XYCoordinates'][0][0], self._DesignParameter['via23_drain_pdn_pair_sw']['_XYCoordinates'][0][1]]],\
														  [[self._DesignParameter['via34_ninput_pdn_pair_sw_2']['_XYCoordinates'][1][0], self._DesignParameter['via34_ninput_pdn_pair_sw_2']['_XYCoordinates'][1][1]], [self._DesignParameter['via23_drain_pdn_pair_sw']['_XYCoordinates'][1][0], self._DesignParameter['via23_drain_pdn_pair_sw']['_XYCoordinates'][1][1]]]]

		self._DesignParameter['via23_inputn_vbn1']=self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_Name='via23_inputn_vbn1In{}'.format(_Name)))[0]
		self._DesignParameter['via23_inputn_vbn1']['_DesignObj']._CalculateDesignParameterSameEnclosure( _ViaMet22Met3NumberOfCOX=2, _ViaMet22Met3NumberOfCOY=2)
		self._DesignParameter['via23_inputn_vbn1']['_XYCoordinates']=[[self._DesignParameter['via23_input_n0_2']['_XYCoordinates'][0][0], self._DesignParameter['m2_source_vbn1']['_XYCoordinates'][0][0][1]]]

		self._DesignParameter['via23_inputp_vbn1']=self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_Name='via23_inputp_vbn1In{}'.format(_Name)))[0]
		self._DesignParameter['via23_inputp_vbn1']['_DesignObj']._CalculateDesignParameterSameEnclosure( _ViaMet22Met3NumberOfCOX=2, _ViaMet22Met3NumberOfCOY=2)
		self._DesignParameter['via23_inputp_vbn1']['_XYCoordinates']=[[self._DesignParameter['via23_input_n0_2']['_XYCoordinates'][1][0], self._DesignParameter['m2_drain_vbn1']['_XYCoordinates'][1][0][1]]]

		self._DesignParameter['m3_n0']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0],_Datatype=DesignParameters._LayerMapping['METAL3'][1], _XYCoordinates=[], _Width=None)
		self._DesignParameter['m3_n0']['_Width']=self.getXWidth('via23_gate_n0','_Met3Layer')
		self._DesignParameter['m3_n0']['_XYCoordinates']=[[[self._DesignParameter['via23_input_n0_2']['_XYCoordinates'][0][0], self._DesignParameter['via23_input_n0_2']['_XYCoordinates'][0][1]], [self._DesignParameter['via23_drain_n0']['_XYCoordinates'][0][0], self._DesignParameter['via23_drain_n0']['_XYCoordinates'][0][1]]],\
														  [[self._DesignParameter['via23_input_n0_2']['_XYCoordinates'][1][0], self._DesignParameter['via23_drain_n0']['_XYCoordinates'][1][1]], [self._DesignParameter['via23_drain_n0']['_XYCoordinates'][1][0], self._DesignParameter['via23_inputp_vbn1']['_XYCoordinates'][0][1]]]]

		NumCoX=max(2,int(self.getXWidth('gate_pdn_pair_sw','_Met1Layer')/(drc._VIAxMinSpace+drc._VIAxMinWidth)))
		self._DesignParameter['via12_gate_pdn']=self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='via12_gate_pdnIn{}'.format(_Name)))[0]
		self._DesignParameter['via12_gate_pdn']['_DesignObj']._CalculateDesignParameterSameEnclosure( _ViaMet12Met2NumberOfCOX=NumCoX, _ViaMet12Met2NumberOfCOY=1)
		self._DesignParameter['via12_gate_pdn']['_XYCoordinates']=[[self._DesignParameter['gate_pdn_pair_sw']['_XYCoordinates'][0][0], self._DesignParameter['gate_pdn_pair_sw']['_XYCoordinates'][0][1]+self.getYWidth('gate_pdn_pair_sw','_Met1Layer')/2-self.getYWidth('via12_gate_pdn','_Met1Layer')/2], \
																   [self._DesignParameter['gate_pdn_pair_sw']['_XYCoordinates'][1][0], self._DesignParameter['gate_pdn_pair_sw']['_XYCoordinates'][1][1]+self.getYWidth('gate_pdn_pair_sw','_Met1Layer')/2-self.getYWidth('via12_gate_pdn','_Met1Layer')/2]]

		self._DesignParameter['m2_gate_pdn']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0],_Datatype=DesignParameters._LayerMapping['METAL2'][1], _XYCoordinates=[], _Width=None)
		self._DesignParameter['m2_gate_pdn']['_Width']=self.getYWidth('via12_gate_pdn','_Met2Layer')
		self._DesignParameter['m2_gate_pdn']['_XYCoordinates']=[[self._DesignParameter['via12_gate_pdn']['_XYCoordinates'][0], self._DesignParameter['via12_gate_pdn']['_XYCoordinates'][1]]]

		self._DesignParameter['m2_drain_vbn1_pdn_sw']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0],_Datatype=DesignParameters._LayerMapping['METAL2'][1], _XYCoordinates=[], _Width=None)
		self._DesignParameter['m2_drain_vbn1_pdn_sw']['_Width']=self._DesignParameter['via12_drain_vbn1']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth']
		self._DesignParameter['m2_drain_vbn1_pdn_sw']['_XYCoordinates']=[[[self._DesignParameter['via12_drain_vbn1']['_XYCoordinates'][0][0], self._DesignParameter['via12_drain_vbn1']['_XYCoordinates'][0][1]], \
																		[self._DesignParameter['nmos_pdn_sw']['_XYCoordinates'][0][0]+self._DesignParameter['nmos_pdn_sw']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][-1][0], self._DesignParameter['via12_drain_vbn1']['_XYCoordinates'][0][1]]]]

		self._DesignParameter['m4_drain_vbn1_pdn_sw']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL4'][0],_Datatype=DesignParameters._LayerMapping['METAL4'][1], _XYCoordinates=[], _Width=None)
		self._DesignParameter['m4_drain_vbn1_pdn_sw']['_Width']=self._DesignParameter['via34_drain_vbn1']['_DesignObj']._DesignParameter['_Met4Layer']['_YWidth']
		self._DesignParameter['m4_drain_vbn1_pdn_sw']['_XYCoordinates']=[[[self._DesignParameter['via34_drain_vbn1']['_XYCoordinates'][0][0], self._DesignParameter['via34_drain_vbn1']['_XYCoordinates'][0][1]], \
																		[self._DesignParameter['nmos_pdn_sw']['_XYCoordinates'][0][0]+self._DesignParameter['nmos_pdn_sw']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0], self._DesignParameter['via34_drain_vbn1']['_XYCoordinates'][0][1]]]]

		self._DesignParameter['via12_vbn1_pdn_sw']=self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='via12_vbn1_pdn_swIn{}'.format(_Name)))[0]
		self._DesignParameter['via12_vbn1_pdn_sw']['_DesignObj']._CalculateDesignParameterSameEnclosure( _ViaMet12Met2NumberOfCOX=1, _ViaMet12Met2NumberOfCOY=2)
		self._DesignParameter['via12_vbn1_pdn_sw']['_XYCoordinates']=[[self._DesignParameter['nmos_pdn_sw']['_XYCoordinates'][0][0]+self._DesignParameter['nmos_pdn_sw']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0], self._DesignParameter['via34_drain_vbn1']['_XYCoordinates'][0][1]], \
																	  [self._DesignParameter['nmos_pdn_sw']['_XYCoordinates'][0][0]+self._DesignParameter['nmos_pdn_sw']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][-1][0], self._DesignParameter['via12_drain_vbn1']['_XYCoordinates'][0][1]]]

		self._DesignParameter['via23_vbn1_pdn_sw']=self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_Name='via23_vbn1_pdn_swIn{}'.format(_Name)))[0]
		self._DesignParameter['via23_vbn1_pdn_sw']['_DesignObj']._CalculateDesignParameterSameEnclosure( _ViaMet22Met3NumberOfCOX=1, _ViaMet22Met3NumberOfCOY=2)
		self._DesignParameter['via23_vbn1_pdn_sw']['_XYCoordinates']=[self._DesignParameter['via12_vbn1_pdn_sw']['_XYCoordinates'][0]]

		self._DesignParameter['via34_vbn1_pdn_sw']=self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_Name='via34_vbn1_pdn_swIn{}'.format(_Name)))[0]
		self._DesignParameter['via34_vbn1_pdn_sw']['_DesignObj']._CalculateDesignParameterSameEnclosure( _ViaMet32Met4NumberOfCOX=1, _ViaMet32Met4NumberOfCOY=2)
		self._DesignParameter['via34_vbn1_pdn_sw']['_XYCoordinates']=[self._DesignParameter['via12_vbn1_pdn_sw']['_XYCoordinates'][0]]

		self._DesignParameter['via34_pdn_single']=self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_Name='via34_pdn_singleIn{}'.format(_Name)))[0]
		self._DesignParameter['via34_pdn_single']['_DesignObj']._CalculateDesignParameterSameEnclosure( _ViaMet32Met4NumberOfCOX=2, _ViaMet32Met4NumberOfCOY=2)
		self._DesignParameter['via34_pdn_single']['_XYCoordinates']=[[self._DesignParameter['m3_ninput']['_XYCoordinates'][0][0][0]+self._DesignParameter['m3_ninput']['_Width']/2+self.getXWidth('via34_pdn_single','_Met3Layer')/2+drc._MetalxMinSpace3, self.getXY('via12_1_pdn_single_sw')[0][1]]]

		self._DesignParameter['m4_pdn_single_sw']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL4'][0],_Datatype=DesignParameters._LayerMapping['METAL4'][1], _XYCoordinates=[], _Width=None)
		self._DesignParameter['m4_pdn_single_sw']['_Width']=self.getYWidth('via34_pdn_single','_Met4Layer')
		self._DesignParameter['m4_pdn_single_sw']['_XYCoordinates']=[[self.getXY('via12_1_pdn_single_sw')[-1], [0, self.getXY('via12_1_pdn_single_sw')[-1][1]]]]

		self._DesignParameter['via34_pdn_single_1']=self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_Name='via34_pdn_single_1In{}'.format(_Name)))[0]
		self._DesignParameter['via34_pdn_single_1']['_DesignObj']._CalculateDesignParameterSameEnclosure( _ViaMet32Met4NumberOfCOX=2, _ViaMet32Met4NumberOfCOY=2)
		self._DesignParameter['via34_pdn_single_1']['_XYCoordinates']=[[0, self.getXY('via12_1_pdn_single_sw')[-1][1]]]

		self._DesignParameter['m3_pdn_single_sw_y']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0],_Datatype=DesignParameters._LayerMapping['METAL3'][1], _XYCoordinates=[], _Width=None)
		self._DesignParameter['m3_pdn_single_sw_y']['_Width']=self.getXWidth('via34_pdn_single_1','_Met3Layer')
		self._DesignParameter['m3_pdn_single_sw_y']['_XYCoordinates']=[[self.getXY('via34_pdn_single_1')[0], [self.getXY('via34_pdn_single_1')[0][0], self._DesignParameter['m2_gate_pdn']['_XYCoordinates'][0][0][1]]]]

		self._DesignParameter['via23_pdn_single_1']=self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_Name='via23_pdn_single_1In{}'.format(_Name)))[0]
		self._DesignParameter['via23_pdn_single_1']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureY( _ViaMet22Met3NumberOfCOX=2, _ViaMet22Met3NumberOfCOY=1)
		self._DesignParameter['via23_pdn_single_1']['_XYCoordinates']=[[0, self._DesignParameter['m2_gate_pdn']['_XYCoordinates'][0][0][1]]]

		numCoX=1
		self._DesignParameter['gate_nmos_pdn']=self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_Name='gate_nmos_pdnIn{}'.format(_Name)))[0]
		self._DesignParameter['gate_nmos_pdn']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(_ViaPoly2Met1NumberOfCOX=numCoX, _ViaPoly2Met1NumberOfCOY=1)
		self._DesignParameter['gate_nmos_pdn']['_XYCoordinates']=[[self._DesignParameter['nmos_pdn_sw']['_XYCoordinates'][0][0], self._DesignParameter['nmos_pdn_sw']['_XYCoordinates'][0][1]-self.getYWidth('nmos_pdn_sw','_Met1Layer')/2-self.getYWidth('gate_nmos_pdn','_Met1Layer')/2-drc._Metal1MinSpace2]]
		del numCoX

		self._DesignParameter['poly_nmos_pdn_y']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0],_Datatype=DesignParameters._LayerMapping['POLY'][1], _XYCoordinates=[], _Width=None)
		self._DesignParameter['poly_nmos_pdn_y']['_Width']=self.getXWidth('nmos_pdn_sw','_POLayer')
		self._DesignParameter['poly_nmos_pdn_y']['_XYCoordinates']=[[self.getXY('nmos_pdn_sw','_POLayer')[0], [self.getXY('nmos_pdn_sw','_POLayer')[0][0], self._DesignParameter['gate_nmos_pdn']['_XYCoordinates'][0][1]]],\
																  [self.getXY('nmos_pdn_sw','_POLayer')[1], [self.getXY('nmos_pdn_sw','_POLayer')[1][0], self._DesignParameter['gate_nmos_pdn']['_XYCoordinates'][0][1]]]]

		self._DesignParameter['poly_nmos_pdn_x']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0],_Datatype=DesignParameters._LayerMapping['POLY'][1], _XYCoordinates=[], _Width=None)
		self._DesignParameter['poly_nmos_pdn_x']['_Width']=self.getYWidth('gate_nmos_pdn','_POLayer')
		self._DesignParameter['poly_nmos_pdn_x']['_XYCoordinates']=[[[self.getXY('nmos_pdn_sw','_POLayer')[0][0]-self.getXWidth('nmos_pdn_sw','_POLayer')/2, self._DesignParameter['gate_nmos_pdn']['_XYCoordinates'][0][1]], [self.getXY('nmos_pdn_sw','_POLayer')[1][0]+self.getXWidth('nmos_pdn_sw','_POLayer')/2, self._DesignParameter['gate_nmos_pdn']['_XYCoordinates'][0][1]]]]

		self._DesignParameter['m3_pdn_single_sw']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0],_Datatype=DesignParameters._LayerMapping['METAL3'][1], _XYCoordinates=[], _Width=None)
		self._DesignParameter['m3_pdn_single_sw']['_Width']=self.getXWidth('via34_pdn_single','_Met3Layer')
		self._DesignParameter['m3_pdn_single_sw']['_XYCoordinates']=[[self._DesignParameter['via34_pdn_single']['_XYCoordinates'][0], [self._DesignParameter['via34_pdn_single']['_XYCoordinates'][0][0], self._DesignParameter['gate_nmos_pdn']['_XYCoordinates'][0][1]]]]

		self._DesignParameter['via23_pdn_single']=self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_Name='via23_pdn_singleIn{}'.format(_Name)))[0]
		self._DesignParameter['via23_pdn_single']['_DesignObj']._CalculateDesignParameterSameEnclosure(_ViaMet22Met3NumberOfCOX=2, _ViaMet22Met3NumberOfCOY=1)
		self._DesignParameter['via23_pdn_single']['_XYCoordinates']=[[self._DesignParameter['m3_pdn_single_sw']['_XYCoordinates'][0][0][0], self._DesignParameter['gate_nmos_pdn']['_XYCoordinates'][0][1]]]

		self._DesignParameter['via12_pdn_single']=self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='via12_pdn_singleIn{}'.format(_Name)))[0]
		self._DesignParameter['via12_pdn_single']['_DesignObj']._CalculateDesignParameterSameEnclosure(_ViaMet12Met2NumberOfCOX=2, _ViaMet12Met2NumberOfCOY=1)
		self._DesignParameter['via12_pdn_single']['_XYCoordinates']=self._DesignParameter['via23_pdn_single']['_XYCoordinates']

		self._DesignParameter['m1_pdn_single_sw']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0],_Datatype=DesignParameters._LayerMapping['METAL1'][1], _XYCoordinates=[], _Width=None)
		self._DesignParameter['m1_pdn_single_sw']['_Width']=self.getXWidth('gate_nmos_pdn','_Met1Layer')
		self._DesignParameter['m1_pdn_single_sw']['_XYCoordinates']=[[self._DesignParameter['gate_nmos_pdn']['_XYCoordinates'][0], [self._DesignParameter['via12_pdn_single']['_XYCoordinates'][0][0]-self.getXWidth('via12_pdn_single','_Met1Layer')/2, self._DesignParameter['gate_nmos_pdn']['_XYCoordinates'][0][1]]]]

		self._DesignParameter['m1_pdn_single_sw_vss_x']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0],_Datatype=DesignParameters._LayerMapping['METAL1'][1], _XYCoordinates=[], _Width=None)
		self._DesignParameter['m1_pdn_single_sw_vss_x']['_Width']=2*drc._Metal1MinSpace
		self._DesignParameter['m1_pdn_single_sw_vss_x']['_XYCoordinates']=[[[self.getXY('pguardring2','left')[0][0], self._DesignParameter['nmos_pdn_sw']['_XYCoordinates'][0][1]+self.getYWidth('nmos_pdn_sw','_Met1Layer')/2+self._DesignParameter['m1_pdn_single_sw_vss_x']['_Width']/2+drc._Metal1MinSpace2], \
																			[self._DesignParameter['nmos_pdn_sw']['_XYCoordinates'][0][0]+self._DesignParameter['nmos_pdn_sw']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][1][0], self._DesignParameter['nmos_pdn_sw']['_XYCoordinates'][0][1]+self.getYWidth('nmos_pdn_sw','_Met1Layer')/2+self._DesignParameter['m1_pdn_single_sw_vss_x']['_Width']/2+drc._Metal1MinSpace2]]]

		self._DesignParameter['m1_pdn_single_sw_vss_y']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0],_Datatype=DesignParameters._LayerMapping['METAL1'][1], _XYCoordinates=[], _Width=None)
		self._DesignParameter['m1_pdn_single_sw_vss_y']['_Width']=self.getXWidth('nmos_pdn_sw','_Met1Layer')
		self._DesignParameter['m1_pdn_single_sw_vss_y']['_XYCoordinates']=[[[self._DesignParameter['nmos_pdn_sw']['_XYCoordinates'][0][0]+self._DesignParameter['nmos_pdn_sw']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][1][0], self._DesignParameter['nmos_pdn_sw']['_XYCoordinates'][0][1]+self._DesignParameter['nmos_pdn_sw']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][1][1]], \
																			[self._DesignParameter['nmos_pdn_sw']['_XYCoordinates'][0][0]+self._DesignParameter['nmos_pdn_sw']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][1][0], self._DesignParameter['m1_pdn_single_sw_vss_x']['_XYCoordinates'][0][0][1]+self._DesignParameter['m1_pdn_single_sw_vss_x']['_Width']/2]]]

		self._DesignParameter['AdditionalPP']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['PIMP'][0],_Datatype=DesignParameters._LayerMapping['PIMP'][1], _XYCoordinates=[], _Width=None)
		self._DesignParameter['AdditionalPP']['_Width']=self.getYWidth('pguardring3','_PPLayer')
		self._DesignParameter['AdditionalPP']['_XYCoordinates']=[[[self.getXY('pguardring1','left')[0][0]-self.getXWidth('pguardring1','left','_PPLayer')/2, self.getXY('pguardring3')[0][1]], [self.getXY('pguardring2','left')[0][0]+self.getXWidth('pguardring2','left','_PPLayer')/2, self.getXY('pguardring3')[0][1]]]]


		self._DesignParameter['via23_gate_inputp']=self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_Name='via23_gate_inputpIn{}'.format(_Name)))[0]
		self._DesignParameter['via23_gate_inputp']['_DesignObj']._CalculateDesignParameterSameEnclosure(_ViaMet22Met3NumberOfCOX=2, _ViaMet22Met3NumberOfCOY=1)
		self._DesignParameter['via23_gate_inputp']['_XYCoordinates']=[[self._DesignParameter['pmos_input']['_XYCoordinates'][0][0]-self.getXWidth('via23_gate_inputp','_Met3Layer')/2-drc._MetalxMinSpace3, self._DesignParameter['m2_gate_inputp']['_XYCoordinates'][1][0][1]],\
																	  [self._DesignParameter['pmos_input']['_XYCoordinates'][0][0]-self.getXWidth('via23_gate_inputp','_Met3Layer')/2-drc._MetalxMinSpace3, self._DesignParameter['m2_gate_inputp']['_XYCoordinates'][0][0][1]],\
																	  [self._DesignParameter['nmos_input']['_XYCoordinates'][0][0]-self.getXWidth('via23_gate_inputp','_Met3Layer')/2-drc._MetalxMinSpace3, self._DesignParameter['m2_gate_ninputn']['_XYCoordinates'][1][0][1]],\
																	  [self._DesignParameter['nmos_input']['_XYCoordinates'][0][0]-self.getXWidth('via23_gate_inputp','_Met3Layer')/2-drc._MetalxMinSpace3, self._DesignParameter['m2_gate_ninputn']['_XYCoordinates'][0][0][1]]]

		self._DesignParameter['via23_gate_inputn']=self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_Name='via23_gate_inputnIn{}'.format(_Name)))[0]
		self._DesignParameter['via23_gate_inputn']['_DesignObj']._CalculateDesignParameterSameEnclosure(_ViaMet22Met3NumberOfCOX=2, _ViaMet22Met3NumberOfCOY=1)
		self._DesignParameter['via23_gate_inputn']['_XYCoordinates']=[[self._DesignParameter['pmos_input']['_XYCoordinates'][0][0]+self.getXWidth('via23_gate_inputn','_Met3Layer')/2+drc._MetalxMinSpace3, self._DesignParameter['m2_gate_inputn']['_XYCoordinates'][1][0][1]],\
																	  [self._DesignParameter['pmos_input']['_XYCoordinates'][0][0]+self.getXWidth('via23_gate_inputn','_Met3Layer')/2+drc._MetalxMinSpace3, self._DesignParameter['m2_gate_inputn']['_XYCoordinates'][0][0][1]],\
																	  [self._DesignParameter['nmos_input']['_XYCoordinates'][0][0]+self.getXWidth('via23_gate_inputn','_Met3Layer')/2+drc._MetalxMinSpace3, self._DesignParameter['m2_gate_ninputp']['_XYCoordinates'][1][0][1]],\
																	  [self._DesignParameter['nmos_input']['_XYCoordinates'][0][0]+self.getXWidth('via23_gate_inputn','_Met3Layer')/2+drc._MetalxMinSpace3, self._DesignParameter['m2_gate_ninputp']['_XYCoordinates'][0][0][1]]]

		self._DesignParameter['m3_gate_inputp']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0],_Datatype=DesignParameters._LayerMapping['METAL3'][1], _XYCoordinates=[], _Width=None)
		self._DesignParameter['m3_gate_inputp']['_Width']=self.getXWidth('via23_gate_inputp','_Met3Layer')
		self._DesignParameter['m3_gate_inputp']['_XYCoordinates']=[[self._DesignParameter['via23_gate_inputp']['_XYCoordinates'][0], self._DesignParameter['via23_gate_inputp']['_XYCoordinates'][-1]]]

		self._DesignParameter['m3_gate_inputn']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0],_Datatype=DesignParameters._LayerMapping['METAL3'][1], _XYCoordinates=[], _Width=None)
		self._DesignParameter['m3_gate_inputn']['_Width']=self.getXWidth('via23_gate_inputn','_Met3Layer')
		self._DesignParameter['m3_gate_inputn']['_XYCoordinates']=[[self._DesignParameter['via23_gate_inputn']['_XYCoordinates'][0], self._DesignParameter['via23_gate_inputn']['_XYCoordinates'][-1]]]

		self._DesignParameter['VSS'] = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1PIN'][0], _Datatype=DesignParameters._LayerMapping['METAL1PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0], _XYCoordinates=[], _Mag=0.2, _Angle=0, _TEXT='VSS')
		self._DesignParameter['VDD'] = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1PIN'][0], _Datatype=DesignParameters._LayerMapping['METAL1PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0], _XYCoordinates=[], _Mag=0.2, _Angle=0, _TEXT='VDD')

		self._DesignParameter['VINM'] = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3PIN'][0], _Datatype=DesignParameters._LayerMapping['METAL3PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0], _XYCoordinates=[], _Mag=0.2, _Angle=0, _TEXT='VINM')
		self._DesignParameter['VINP'] = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3PIN'][0], _Datatype=DesignParameters._LayerMapping['METAL3PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0], _XYCoordinates=[], _Mag=0.2, _Angle=0, _TEXT='VINP')
		self._DesignParameter['vb1'] = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2PIN'][0], _Datatype=DesignParameters._LayerMapping['METAL2PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0], _XYCoordinates=[], _Mag=0.2, _Angle=0, _TEXT='vb1')
		self._DesignParameter['vb2'] = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2PIN'][0], _Datatype=DesignParameters._LayerMapping['METAL2PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0], _XYCoordinates=[], _Mag=0.2, _Angle=0, _TEXT='vb2')
		self._DesignParameter['vbp1'] = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2PIN'][0], _Datatype=DesignParameters._LayerMapping['METAL2PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0], _XYCoordinates=[], _Mag=0.2, _Angle=0, _TEXT='vbp1')
		self._DesignParameter['vbp2'] = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2PIN'][0], _Datatype=DesignParameters._LayerMapping['METAL2PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0], _XYCoordinates=[], _Mag=0.2, _Angle=0, _TEXT='vbp2')
		self._DesignParameter['vbn1'] = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2PIN'][0], _Datatype=DesignParameters._LayerMapping['METAL2PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0], _XYCoordinates=[], _Mag=0.2, _Angle=0, _TEXT='vbn1')
		self._DesignParameter['vpdn'] = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL4PIN'][0], _Datatype=DesignParameters._LayerMapping['METAL4PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0], _XYCoordinates=[], _Mag=0.2, _Angle=0, _TEXT='vpdn')
		self._DesignParameter['VOUT'] = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3PIN'][0], _Datatype=DesignParameters._LayerMapping['METAL3PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0], _XYCoordinates=[], _Mag=0.2, _Angle=0, _TEXT='VOUT')

		self._DesignParameter['VDD']['_XYCoordinates']=[[self.getXY('nguardring2','bot')[0][0],self.getXY('nguardring2','bot')[0][1]]]
		self._DesignParameter['VSS']['_XYCoordinates']=[[self.getXY('pguardring1','top')[0][0],self.getXY('pguardring1','top')[0][1]]]
		self._DesignParameter['VINM']['_XYCoordinates']=[[self._DesignParameter['m3_gate_inputn']['_XYCoordinates'][0][0][0], (self._DesignParameter['m3_gate_inputn']['_XYCoordinates'][0][0][1]+self._DesignParameter['m3_gate_inputn']['_XYCoordinates'][0][1][1])/2]]
		self._DesignParameter['VINP']['_XYCoordinates']=[[self._DesignParameter['m3_gate_inputp']['_XYCoordinates'][0][0][0], (self._DesignParameter['m3_gate_inputp']['_XYCoordinates'][0][0][1]+self._DesignParameter['m3_gate_inputp']['_XYCoordinates'][0][1][1])/2]]
		self._DesignParameter['vb1']['_XYCoordinates']=[[(self._DesignParameter['m2_gate_vb1']['_XYCoordinates'][0][0][0]+self._DesignParameter['m2_gate_vb1']['_XYCoordinates'][0][1][0])/2, self._DesignParameter['m2_gate_vb1']['_XYCoordinates'][1][0][1]]]
		self._DesignParameter['vb2']['_XYCoordinates']=[[(self._DesignParameter['m2_gate_vb2']['_XYCoordinates'][0][0][0]+self._DesignParameter['m2_gate_vb2']['_XYCoordinates'][0][1][0])/2, self._DesignParameter['m2_gate_vb2']['_XYCoordinates'][1][0][1]]]
		self._DesignParameter['vbp1']['_XYCoordinates']=[[(self._DesignParameter['m2_gate_vbp1']['_XYCoordinates'][0][0][0]+self._DesignParameter['m2_gate_vbp1']['_XYCoordinates'][0][1][0])/2, self._DesignParameter['m2_gate_vbp1']['_XYCoordinates'][1][0][1]]]
		self._DesignParameter['vbp2']['_XYCoordinates']=[[(self._DesignParameter['m2_gate_vbp2']['_XYCoordinates'][0][0][0]+self._DesignParameter['m2_gate_vbp2']['_XYCoordinates'][0][1][0])/2, self._DesignParameter['m2_gate_vbp2']['_XYCoordinates'][1][0][1]]]
		self._DesignParameter['vbn1']['_XYCoordinates']=[[(self._DesignParameter['m2_gate_vbn1']['_XYCoordinates'][0][0][0]+self._DesignParameter['m2_gate_vbn1']['_XYCoordinates'][0][1][0])/2, self._DesignParameter['m2_gate_vbn1']['_XYCoordinates'][1][0][1]]]
		self._DesignParameter['vpdn']['_XYCoordinates']=[[(self._DesignParameter['m4_pdn_single_sw']['_XYCoordinates'][0][0][0]+self._DesignParameter['m4_pdn_single_sw']['_XYCoordinates'][0][1][0])/2, self._DesignParameter['m4_pdn_single_sw']['_XYCoordinates'][0][0][1]]]
		self._DesignParameter['VOUT']['_XYCoordinates']=[[self._DesignParameter['m3_vbp1_vbn1']['_XYCoordinates'][0][0][0], (self._DesignParameter['m3_vbp1_vbn1']['_XYCoordinates'][0][0][1]+self._DesignParameter['m3_vbp1_vbn1']['_XYCoordinates'][0][1][1])/2]]

		if pset_param['pmos_input_param']['_PMOSNumberofGate'] < 2 :
			raise NotImplementedError('The input gate finger shoulde be larger than 1.')

		if nset_param['nmos_input_param']['_NMOSNumberofGate'] < 2 :
			raise NotImplementedError('The input gate finger shoulde be larger than 1.')

		if pset_param['pmos_current_pair1_param']['_PMOSNumberofGate'] != pset_param['pmos_current_pair2_param']['_PMOSNumberofGate']:
			raise NotImplementedError('Gate finger of both of pmos current source pairs should be equal.')

		if nset_param['nmos_current_pair1_param']['_NMOSNumberofGate'] != nset_param['nmos_current_pair2_param']['_NMOSNumberofGate']:
			raise NotImplementedError('Gate finger of both of nmos current source pairs should be equal.')

		if (pset_param['pmos_current_pair1_param']['_PMOSChannelWidth'] == pset_param['pmos_current_pair2_param']['_PMOSChannelWidth'] == pset_param['pmos_input_param']['_PMOSChannelWidth'] == pset_param['pmos_current_single_param']['_PMOSChannelWidth']) == False :
			raise NotImplementedError('All channel width of pmos should be equal.')

		if (nset_param['nmos_current_pair1_param']['_NMOSChannelWidth'] == nset_param['nmos_current_pair2_param']['_NMOSChannelWidth'] == nset_param['nmos_current_single_param']['_NMOSChannelWidth']) == False:
			raise NotImplementedError('All channel width of nmos except for input pair should be equal.')

		if pset_param['pmos_current_pair1_param']['_PMOSNumberofGate'] <= nset_param['nmos_current_pair1_param']['_NMOSNumberofGate']:
			raise NotImplementedError('Gate finger of pmos current source should be larger than the one of nmos current source.')

		if nset_param['nmos_pdn_sw_param']['_NMOSNumberofGate'] != 2 :
			raise NotImplementedError('Gate finger of each nmos switch shoulde be 1.')

		if ((pset_param['pmos_current_pair1_param']['_PMOSChannelWidth'] < 1500) or (pset_param['pmos_current_pair2_param']['_PMOSChannelWidth'] < 1500) or (pset_param['pmos_current_single_param']['_PMOSChannelWidth'] < 1500) or (pset_param['pmos_input_param']['_PMOSChannelWidth'] < 1500)) == True :
			raise NotImplementedError('All channel width of pmos should be larger than 1500nm.')

		if ((nset_param['nmos_current_pair1_param']['_NMOSChannelWidth'] < 1500) or (nset_param['nmos_current_pair2_param']['_NMOSChannelWidth'] < 1500) or (nset_param['nmos_current_single_param']['_NMOSChannelWidth'] < 1500) or (nset_param['nmos_input_param']['_NMOSChannelWidth'] < 1500)) == True :
			raise NotImplementedError('All channel width of nmos should be larger than 1500nm.')

		if ((pset_param['pmos_current_pair1_param']['_PMOSChannellength'] < 150) or (pset_param['pmos_current_pair2_param']['_PMOSChannellength'] < 150) or (pset_param['pmos_current_single_param']['_PMOSChannellength'] < 150) or (pset_param['pmos_input_param']['_PMOSChannellength'] < 150)) == True :
			raise NotImplementedError('All channel length of pmos should be larger than 150nm.')

		if ((nset_param['nmos_current_pair1_param']['_NMOSChannellength'] < 150) or (nset_param['nmos_current_pair2_param']['_NMOSChannellength'] < 150) or (nset_param['nmos_current_single_param']['_NMOSChannellength'] < 150) or (nset_param['nmos_input_param']['_NMOSChannellength'] < 150)) == True :
			raise NotImplementedError('All channel length of nmos should be larger than 150nm.')

