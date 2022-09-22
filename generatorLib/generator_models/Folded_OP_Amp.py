from generatorLib import StickDiagram
from generatorLib import DesignParameters
import copy
import math
from generatorLib import DRC
from generatorLib.generator_models import Folded_Cascode_Amp
from generatorLib.generator_models import Common_Source_Amp
from generatorLib.generator_models import ViaPoly2Met1
from generatorLib.generator_models import ViaMet12Met2
from generatorLib.generator_models import ViaMet22Met3
from generatorLib.generator_models import ViaMet32Met4
from generatorLib.generator_models import NSubRing
from generatorLib.generator_models import PSubRing
from generatorLib.generator_models import PbodyContact

class _Folded_OP_Amp(StickDiagram._StickDiagram):
	def __init__(self, _DesignParameter=None, _Name='Folded_OP_Amp'):
		super().__init__()
		if _DesignParameter != None:
			self._DesignParameter = _DesignParameter
		else:
			self._DesignParameter = dict(_Name=self._NameDeclaration(_Name=_Name), _GDSFile=self._GDSObjDeclaration(_GDSFile=None))
		self._DesignParameter['_Name']['Name'] = _Name


	def _CalculateDesignParameter(self, Folded_param = {\
													'pset_param':\
																{'pmos_pdn_single_sw_param':{'_PMOSNumberofGate':4, '_PMOSChannelWidth':2000, '_PMOSChannellength':30, '_PMOSDummy':True, '_GateSpacing':None, '_SDWidth':None, '_XVT':'LVT', '_PCCrit':None}, \
																'pmos_pdn_pair_sw_param':{'_PMOSNumberofGate':32, '_PMOSChannelWidth':250, '_PMOSChannellength':30, '_PMOSDummy':True, '_GateSpacing':None, '_SDWidth':None, '_XVT':'LVT', '_PCCrit':None}, \
																'pmos_current_pair1_param':{'_PMOSNumberofGate':8, '_PMOSChannelWidth':5000, '_PMOSChannellength':1000, '_PMOSDummy':False, '_GateSpacing':None, '_SDWidth':None, '_XVT':'LVT', '_PCCrit':None}, \
																'pmos_current_pair2_param':{'_PMOSNumberofGate':8, '_PMOSChannelWidth':5000, '_PMOSChannellength':1000, '_PMOSDummy':False, '_GateSpacing':None, '_SDWidth':None, '_XVT':'LVT', '_PCCrit':None},\
																'pmos_current_single_param':{'_PMOSNumberofGate':8, '_PMOSChannelWidth':5000, '_PMOSChannellength':1000, '_PMOSDummy':False, '_GateSpacing':None, '_SDWidth':None, '_XVT':'LVT', '_PCCrit':None},\
																'pmos_input_param':{'_PMOSNumberofGate':8, '_PMOSChannelWidth':5000, '_PMOSChannellength':1000, '_PMOSDummy':False, '_GateSpacing':None, '_SDWidth':None, '_XVT':'LVT', '_PCCrit':None}, \
																'pmos_guardring_co_left':1,'pmos_guardring_co_right':1, 'pmos_guardring_co_top':1, 'pmos_guardring_co_bot':2, 'pmos_guardring_height1':None, 'pmos_guardring_width1':None, 'pmos_guardring_width2':None, 'pmos_guardring_height2':None},\
													'nset_param':\
																{'nmos_pdn_sw_param':{'_NMOSNumberofGate':2, '_NMOSChannelWidth':2000, '_NMOSChannellength':30, '_NMOSDummy':True, '_GateSpacing':None, '_SDWidth':None, '_XVT':'RVT', '_PCCrit':None}, \
																'nmos_current_pair1_param':{'_NMOSNumberofGate':4, '_NMOSChannelWidth':5000, '_NMOSChannellength':1000, '_NMOSDummy':False, '_GateSpacing':None, '_SDWidth':None, '_XVT':'RVT', '_PCCrit':None}, \
																'nmos_current_pair2_param':{'_NMOSNumberofGate':4, '_NMOSChannelWidth':5000, '_NMOSChannellength':1000, '_NMOSDummy':False, '_GateSpacing':None, '_SDWidth':None, '_XVT':'RVT', '_PCCrit':None},\
																'nmos_current_single_param':{'_NMOSNumberofGate':4, '_NMOSChannelWidth':5000, '_NMOSChannellength':1000, '_NMOSDummy':False, '_GateSpacing':None, '_SDWidth':None, '_XVT':'RVT', '_PCCrit':None},\
																'nmos_input_param':{'_NMOSNumberofGate':8, '_NMOSChannelWidth':2500, '_NMOSChannellength':1000, '_NMOSDummy':False, '_GateSpacing':None, '_SDWidth':None, '_XVT':'RVT', '_PCCrit':None}, \
																'nmos_guardring_co_left':1,'nmos_guardring_co_right':1, 'nmos_guardring_co_top':2, 'nmos_guardring_co_bot':1, 'nmos_guardring_height1':None, 'nmos_guardring_width1':None, 'nmos_guardring_width2':None, 'nmos_guardring_height2':None}}, \
										Common_param = {\
																'nmos_param':{'_NMOSNumberofGate':3, '_NMOSChannelWidth':5000, '_NMOSChannellength':1000, '_NMOSDummy':False, '_GateSpacing':None, '_SDWidth':None, '_XVT':'RVT', '_PCCrit':None},\
																'psubring_param':{'height':None, 'width':None, 'contact_bottom':2, 'contact_top':2, 'contact_left':2, 'contact_right':2}, \
																'R_drain':{'_ResWidth':800, '_ResLength':4628, '_CONUMX':None, '_CONUMY':1}, \
																'R_feedback':{'_ResWidth':800, '_ResLength':1068, '_CONUMX':None, '_CONUMY':1}, \
																'cap1_param':{'_XWidth':2763, '_YWidth':3000, '_NumofGates':10, '_NumofOD':1, 'NumOfCOX':None, 'NumOfCOY':None, 'Guardring':False, 'guardring_height':None, 'guardring_width':None, 'guardring_right':None, 'guardring_left':None, 'guardring_top':None, 'guardring_bot':None}, \
																'cap2_param':{'_XWidth':3459, '_YWidth':2997, '_NumofGates':12, '_NumofOD':1, 'NumOfCOX':None, 'NumOfCOY':None, 'Guardring':False, 'guardring_height':None, 'guardring_width':None, 'guardring_right':None, 'guardring_left':None, 'guardring_top':None, 'guardring_bot':None}}, \
								) :

		drc = DRC.DRC()
		_Name = self._DesignParameter['_Name']['_Name']
		MinSnapSpacing=drc._MinSnapSpacing
		_OriginXY=[[0,0]]

		if Folded_param['nset_param']['nmos_guardring_co_top'] != Common_param['psubring_param']['contact_top'] :
			raise NotImplementedError

		self._DesignParameter['Folded_Cascode_AMP']=self._SrefElementDeclaration(_DesignObj=Folded_Cascode_Amp._Folded_Cascode_Amp(_Name='Folded_Cascode_AMPIn{}'.format(_Name)))[0]
		self._DesignParameter['Folded_Cascode_AMP']['_DesignObj']._CalculateDesignParameter(**Folded_param)

		self._DesignParameter['Common_Source_AMP']=self._SrefElementDeclaration(_DesignObj=Common_Source_Amp._Common_Source_Amp(_Name='Common_Source_AMPIn{}'.format(_Name)))[0]
		self._DesignParameter['Common_Source_AMP']['_DesignObj']._CalculateDesignParameter(**Common_param)
		self._DesignParameter['Common_Source_AMP']['_DesignObj']._DesignParameter['guardring']['_DesignObj']._DesignParameter['top']['_DesignObj']._DesignParameter['_COLayer']['_XYCoordinates']=[]

		self._DesignParameter['Folded_Cascode_AMP']['_XYCoordinates']=_OriginXY
		self._DesignParameter['Common_Source_AMP']['_XYCoordinates']=[[self.getXY('Folded_Cascode_AMP')[0][0], self.getXY('Folded_Cascode_AMP','pguardring1','top')[0][1]\
																	-(self._DesignParameter['Common_Source_AMP']['_DesignObj']._DesignParameter['guardring']['_XYCoordinates'][0][1]+self._DesignParameter['Common_Source_AMP']['_DesignObj']._DesignParameter['guardring']['_DesignObj']._DesignParameter['top']['_XYCoordinates'][0][1])]]

		viaXnum=int(((self._DesignParameter['Common_Source_AMP']['_DesignObj']._DesignParameter['via12_gate']['_XYCoordinates'][-1][0]-self._DesignParameter['Common_Source_AMP']['_DesignObj']._DesignParameter['via12_gate']['_XYCoordinates'][0][0])+self.getXWidth('Common_Source_AMP','via12_gate','_Met2Layer'))/(drc._VIAxMinWidth+drc._VIAxMinSpace))
		self._DesignParameter['via23_common']=self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_Name='via23_commonIn{}'.format(_Name)))[0]
		self._DesignParameter['via23_common']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureY(_ViaMet22Met3NumberOfCOX=viaXnum, _ViaMet22Met3NumberOfCOY=1)
		self._DesignParameter['via23_common']['_XYCoordinates']=[[self.getXY('Common_Source_AMP','nmos')[0][0], self.getXY('Common_Source_AMP','via12_gate')[-1][1]]]
		del viaXnum

		self._DesignParameter['m3_folded_common']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0],_Datatype=DesignParameters._LayerMapping['METAL3'][1], _XYCoordinates=[], _Width=None)
		self._DesignParameter['m3_folded_common']['_Width']=self._DesignParameter['Folded_Cascode_AMP']['_DesignObj']._DesignParameter['m3_vbp1_vbn1']['_Width']
		self._DesignParameter['m3_folded_common']['_XYCoordinates']=[[[self._DesignParameter['Folded_Cascode_AMP']['_XYCoordinates'][0][0]+self._DesignParameter['Folded_Cascode_AMP']['_DesignObj']._DesignParameter['m3_vbp1_vbn1']['_XYCoordinates'][0][0][0], self._DesignParameter['Folded_Cascode_AMP']['_XYCoordinates'][0][1]+self._DesignParameter['Folded_Cascode_AMP']['_DesignObj']._DesignParameter['m3_vbp1_vbn1']['_XYCoordinates'][0][0][1]], \
																		[self._DesignParameter['Folded_Cascode_AMP']['_XYCoordinates'][0][0]+self._DesignParameter['Folded_Cascode_AMP']['_DesignObj']._DesignParameter['m3_vbp1_vbn1']['_XYCoordinates'][0][0][0], self.getXY('via23_common')[0][1]]]]

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

		self._DesignParameter['VDD']['_XYCoordinates']=[[self.getXY('Folded_Cascode_AMP','nguardring2','bot')[0][0],self.getXY('Folded_Cascode_AMP','nguardring2','bot')[0][1]], self.getXY('Common_Source_AMP','R_drain','_Met1Layer')[0]]
		self._DesignParameter['VSS']['_XYCoordinates']=[[self.getXY('Folded_Cascode_AMP','pguardring1','top')[0][0],self.getXY('Folded_Cascode_AMP','pguardring1','top')[0][1]]]
		self._DesignParameter['VINM']['_XYCoordinates']=[[self._DesignParameter['Folded_Cascode_AMP']['_XYCoordinates'][0][0]+self._DesignParameter['Folded_Cascode_AMP']['_DesignObj']._DesignParameter['m3_gate_inputn']['_XYCoordinates'][0][0][0], self._DesignParameter['Folded_Cascode_AMP']['_XYCoordinates'][0][1]+(self._DesignParameter['Folded_Cascode_AMP']['_DesignObj']._DesignParameter['m3_gate_inputn']['_XYCoordinates'][0][0][1]+self._DesignParameter['Folded_Cascode_AMP']['_DesignObj']._DesignParameter['m3_gate_inputn']['_XYCoordinates'][0][1][1])/2]]
		self._DesignParameter['VINP']['_XYCoordinates']=[[self._DesignParameter['Folded_Cascode_AMP']['_XYCoordinates'][0][0]+self._DesignParameter['Folded_Cascode_AMP']['_DesignObj']._DesignParameter['m3_gate_inputp']['_XYCoordinates'][0][0][0], self._DesignParameter['Folded_Cascode_AMP']['_XYCoordinates'][0][1]+(self._DesignParameter['Folded_Cascode_AMP']['_DesignObj']._DesignParameter['m3_gate_inputp']['_XYCoordinates'][0][0][1]+self._DesignParameter['Folded_Cascode_AMP']['_DesignObj']._DesignParameter['m3_gate_inputp']['_XYCoordinates'][0][1][1])/2]]
		self._DesignParameter['vb1']['_XYCoordinates']=[[self._DesignParameter['Folded_Cascode_AMP']['_XYCoordinates'][0][0]+(self._DesignParameter['Folded_Cascode_AMP']['_DesignObj']._DesignParameter['m2_gate_vb1']['_XYCoordinates'][0][0][0]+self._DesignParameter['Folded_Cascode_AMP']['_DesignObj']._DesignParameter['m2_gate_vb1']['_XYCoordinates'][0][1][0])/2, self._DesignParameter['Folded_Cascode_AMP']['_XYCoordinates'][0][1]+self._DesignParameter['Folded_Cascode_AMP']['_DesignObj']._DesignParameter['m2_gate_vb1']['_XYCoordinates'][1][0][1]]]
		self._DesignParameter['vb2']['_XYCoordinates']=[[self._DesignParameter['Folded_Cascode_AMP']['_XYCoordinates'][0][0]+(self._DesignParameter['Folded_Cascode_AMP']['_DesignObj']._DesignParameter['m2_gate_vb2']['_XYCoordinates'][0][0][0]+self._DesignParameter['Folded_Cascode_AMP']['_DesignObj']._DesignParameter['m2_gate_vb2']['_XYCoordinates'][0][1][0])/2, self._DesignParameter['Folded_Cascode_AMP']['_XYCoordinates'][0][1]+self._DesignParameter['Folded_Cascode_AMP']['_DesignObj']._DesignParameter['m2_gate_vb2']['_XYCoordinates'][1][0][1]]]
		self._DesignParameter['vbp1']['_XYCoordinates']=[[self._DesignParameter['Folded_Cascode_AMP']['_XYCoordinates'][0][0]+(self._DesignParameter['Folded_Cascode_AMP']['_DesignObj']._DesignParameter['m2_gate_vbp1']['_XYCoordinates'][0][0][0]+self._DesignParameter['Folded_Cascode_AMP']['_DesignObj']._DesignParameter['m2_gate_vbp1']['_XYCoordinates'][0][1][0])/2, self._DesignParameter['Folded_Cascode_AMP']['_XYCoordinates'][0][1]+self._DesignParameter['Folded_Cascode_AMP']['_DesignObj']._DesignParameter['m2_gate_vbp1']['_XYCoordinates'][1][0][1]]]
		self._DesignParameter['vbp2']['_XYCoordinates']=[[self._DesignParameter['Folded_Cascode_AMP']['_XYCoordinates'][0][0]+(self._DesignParameter['Folded_Cascode_AMP']['_DesignObj']._DesignParameter['m2_gate_vbp2']['_XYCoordinates'][0][0][0]+self._DesignParameter['Folded_Cascode_AMP']['_DesignObj']._DesignParameter['m2_gate_vbp2']['_XYCoordinates'][0][1][0])/2, self._DesignParameter['Folded_Cascode_AMP']['_XYCoordinates'][0][1]+self._DesignParameter['Folded_Cascode_AMP']['_DesignObj']._DesignParameter['m2_gate_vbp2']['_XYCoordinates'][1][0][1]]]
		self._DesignParameter['vbn1']['_XYCoordinates']=[[self._DesignParameter['Folded_Cascode_AMP']['_XYCoordinates'][0][0]+(self._DesignParameter['Folded_Cascode_AMP']['_DesignObj']._DesignParameter['m2_gate_vbn1']['_XYCoordinates'][0][0][0]+self._DesignParameter['Folded_Cascode_AMP']['_DesignObj']._DesignParameter['m2_gate_vbn1']['_XYCoordinates'][0][1][0])/2, self._DesignParameter['Folded_Cascode_AMP']['_XYCoordinates'][0][1]+self._DesignParameter['Folded_Cascode_AMP']['_DesignObj']._DesignParameter['m2_gate_vbn1']['_XYCoordinates'][1][0][1]]]
		self._DesignParameter['vpdn']['_XYCoordinates']=[[self._DesignParameter['Folded_Cascode_AMP']['_XYCoordinates'][0][0]+(self._DesignParameter['Folded_Cascode_AMP']['_DesignObj']._DesignParameter['m4_pdn_single_sw']['_XYCoordinates'][0][0][0]+self._DesignParameter['Folded_Cascode_AMP']['_DesignObj']._DesignParameter['m4_pdn_single_sw']['_XYCoordinates'][0][1][0])/2, self._DesignParameter['Folded_Cascode_AMP']['_XYCoordinates'][0][1]+self._DesignParameter['Folded_Cascode_AMP']['_DesignObj']._DesignParameter['m4_pdn_single_sw']['_XYCoordinates'][0][0][1]]]
		self._DesignParameter['VOUT']['_XYCoordinates']=[self.getXY('Common_Source_AMP','via23_R_feedback')[0]]
