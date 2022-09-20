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
																'nmos_guardring_co_left':1,'nmos_guardring_co_right':1, 'nmos_guardring_co_top':1, 'nmos_guardring_co_bot':1, 'nmos_guardring_height1':None, 'nmos_guardring_width1':None, 'nmos_guardring_width2':None, 'nmos_guardring_height2':None}}, \
										Common_param = {\
																'nmos_param':{'_NMOSNumberofGate':3, '_NMOSChannelWidth':5000, '_NMOSChannellength':1000, '_NMOSDummy':False, '_GateSpacing':None, '_SDWidth':None, '_XVT':'RVT', '_PCCrit':None},\
																'psubring_param':{'height':None, 'width':None, 'contact_bottom':2, 'contact_top':2, 'contact_left':2, 'contact_right':2}, \
																'R_drain':{'_ResWidth':800, '_ResLength':4628, '_CONUMX':None, '_CONUMY':1}, \
																'R_feedback':{'_ResWidth':800, '_ResLength':1068, '_CONUMX':None, '_CONUMY':1}, \
																'cap1_param':{'_XWidth':2763, '_YWidth':3000, '_NumofGates':10, 'NumOfCOX':None, 'NumOfCOY':None, 'Guardring':False, 'guardring_height':None, 'guardring_width':None, 'guardring_right':None, 'guardring_left':None, 'guardring_top':None, 'guardring_bot':None}, \
																'cap2_param':{'_XWidth':3459, '_YWidth':2997, '_NumofGates':12, 'NumOfCOX':None, 'NumOfCOY':None, 'Guardring':False, 'guardring_height':None, 'guardring_width':None, 'guardring_right':None, 'guardring_left':None, 'guardring_top':None, 'guardring_bot':None}}, \
								) :

		drc = DRC.DRC()
		_Name = self._DesignParameter['_Name']['_Name']
		MinSnapSpacing=drc._MinSnapSpacing
		_OriginXY=[[0,0]]

		if Folded_param['nset_param']['nmos_guardring_co_top'] != Common_param['psubring_param']['contact_top'] :
			raise NotImplementedError

		self._DesignParameter['Folded_Cascode_AMP']=self._SrefElementDeclaration(_DesignObj=Folded_Cascode_Amp._Folded_Cascode_Amp(_Name='Folded_Cascode_AMPIn{}'.format(_Name)))[0]
		self._DesignParameter['Folded_Cascode_AMP']['_DesignObj']._CalculateDesignParameter(**Folded_param)

		self._DesignParameter['Common_Source_AMP']=self._SrefElementDeclaration(_DesignObj=Common_Source_Amp._CalculateDesignParameter(_Name='Common_Source_AMPIn{}'.format(_Name)))[0]
		self._DesignParameter['Common_Source_AMP']['_DesignObj']._CalculateDesignParameter(**Common_param)
		self._DesignParameter['Common_Source_AMP']['_DesignObj']._DesignParameter['guardring']['_DesignObj']._DesignParameter['top']['_DesignObj']._DesignParameter['_COLayer']['_XYCoordinates']=[]

		self._DesignParameter['Folded_Cascode_AMP']['_XYCoordinates']=_OriginXY
		self._DesignParameter['Common_Source_AMP']['_XYCoordinates']=[[self.getXY('Folded_Cascode_AMP')[0][0], self.getXY('Folded_Cascode_AMP','pguardring1','top')[0][1]-self.getXY('Common_Source_AMP','guardring','top')[0][1]]]
