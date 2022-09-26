from generatorLib import StickDiagram
from generatorLib import DesignParameters
import copy
import random
import math
from generatorLib import DRC
from generatorLib.generator_models import NMOSWithDummy
from generatorLib.generator_models import opppcres_b
from generatorLib.generator_models import NCAP
from generatorLib.generator_models import PbodyContact
from generatorLib.generator_models import ViaPoly2Met1
from generatorLib.generator_models import ViaMet12Met2
from generatorLib.generator_models import ViaMet22Met3


class _SummerBottom(StickDiagram._StickDiagram):
	_ParametersForDesignCalculation = dict(_NMOSNumberofGate1=None, _NMOSChannelWidth1=None, _NMOSChannellength1=None,
										   _NMOSDummy1=True, _GateSpacing1=None, _SDWidth1=None, _XVT=None, _PCCrit=None,
										   _NMOSNumberofGate2=None, _NMOSChannelWidth2=None, _NMOSChannellength2=None,
										   _NMOSDummy2=True, _GateSpacing2=None, _SDWidth2=None,
										   _NMOSNumberofGate3=None, _NMOSChannelWidth3=None, _NMOSChannellength3=None,
										   _NMOSDummy3=True, _GateSpacing3=None, _SDWidth3=None,
										   _NMOSNumberofGate4=None, _NMOSChannelWidth4=None, _NMOSChannellength4=None,
										   _NMOSDummy4=True, _GateSpacing4=None, _SDWidth4=None,
										   _ResWidth=None, _ResLength=None, _CONUMX=None,_CONUMY=None,
										   _XWidth=1000, _YWidth=1000, _NumofGates=1, NumOfCOX=None, NumOfCOY=None,
										   Guardring=True, guardring_height=None, guardring_width=None, guardring_right=2, guardring_left=2, guardring_top=2, guardring_bot=2,
										   _NumberOfPbodyCOX=None, _NumberOfPbodyCOY=None, _Met1XWidth=None, _Met1YWidth=None,
										   _ViaPoly2Met1NumberOfCOX=None, _ViaPoly2Met1NumberOfCOY=None,
										   _ViaMet12Met2NumberOfCOX=None, _ViaMet12Met2NumberOfCOY=None,
										   _ViaMet22Met3NumberOfCOX=None, _ViaMet22Met3NumberOfCOY=None,
										   _NumofOD=None, _ViaPoly2Met1NumberOfCOX_CAP=None, _ViaPoly2Met1NumberOfCOY_CAP=1)

	def __init__(self, _DesignParameter=None, _Name='SummerBottom'):
		if _DesignParameter != None:
			self._DesignParameter = _DesignParameter
		else:
			self._DesignParameter = dict(_Name=self._NameDeclaration(_Name=_Name), _GDSFile=self._GDSObjDeclaration(_GDSFile=None))

		if _Name != None:
			self._DesignParameter['_Name']['Name'] = _Name

	def _CalculateSummerBottomDesignParameter(self, _NMOSNumberofGate1=14, _NMOSChannelWidth1=500, _NMOSChannellength1=30, # NMOSWithDummy
											  _NMOSDummy1=False, _GateSpacing1=None, _SDWidth1=None, _XVT='LVT', _PCCrit=None,
											  _NMOSNumberofGate2=8, _NMOSChannelWidth2=None,_NMOSChannellength2=None,
											  _NMOSDummy2=True, _GateSpacing2=None, _SDWidth2=None,
											  _NMOSNumberofGate3=4, _NMOSChannelWidth3=None, _NMOSChannellength3=None,
											  _NMOSDummy3=False, _GateSpacing3=None, _SDWidth3=None,
											  _NMOSNumberofGate4=7, _NMOSChannelWidth4=None, _NMOSChannellength4=None,
											  _NMOSDummy4=True, _GateSpacing4=None, _SDWidth4=None,
											  _ResWidth=938, _ResLength=580, _CONUMX=None,_CONUMY=1, # opppcres_b
											  _XWidth=838, _YWidth=1874, _NumofGates=1, NumOfCOX=None, NumOfCOY=None,
											  Guardring=False, guardring_height=None, guardring_width=None, guardring_right=3, guardring_left=3, guardring_top=3, guardring_bot=3,
											  _NumberOfPbodyCOX=None, _NumberOfPbodyCOY=3, _Met1XWidth=None, _Met1YWidth=None, # PbodyContact
											  _ViaPoly2Met1NumberOfCOX=None, _ViaPoly2Met1NumberOfCOY=None, # ViaPoly2Met1
											  _ViaMet12Met2NumberOfCOX=None, _ViaMet12Met2NumberOfCOY=None, # ViaMet12Met2
											  _ViaMet22Met3NumberOfCOX=None, _ViaMet22Met3NumberOfCOY=None, # ViaMet22Met3
											  _NumofOD=1, _ViaPoly2Met1NumberOfCOX_CAP=None, _ViaPoly2Met1NumberOfCOY_CAP=1
											  ):
		print('#########################################################################################################')
		print('                                    {}  SummerBottom Calculation Start                                       '.format(self._DesignParameter['_Name']['_Name']))
		print('#########################################################################################################')

		_DRCObj = DRC.DRC()
		_Name = self._DesignParameter['_Name']['_Name']
		_XYCoordinatesofNMOS = [[0,-(_NMOSChannelWidth1 + 2 * _DRCObj.DRCPolygateMinExtensionOnOD(_NMOSChannellength1)+_DRCObj._OPlayeroverPoly)]]
		_MinSnapSpacing = _DRCObj._MinSnapSpacing


		##################################### NMOS1 generation #####################################
		NMOS1inputs = copy.deepcopy(NMOSWithDummy._NMOS._ParametersForDesignCalculation)
		NMOS1inputs['_NMOSNumberofGate'] = _NMOSNumberofGate1
		NMOS1inputs['_NMOSChannelWidth'] = _NMOSChannelWidth1
		NMOS1inputs['_NMOSChannellength'] = _NMOSChannellength1
		NMOS1inputs['_NMOSDummy'] = _NMOSDummy1
		NMOS1inputs['_GateSpacing'] = _GateSpacing1
		NMOS1inputs['_SDWidth'] = _SDWidth1
		NMOS1inputs['_XVT'] = _XVT
		NMOS1inputs['_PCCrit'] = _PCCrit

		self._DesignParameter['_NMOS1'] = self._SrefElementDeclaration(_Reflect = [1,0,0], _Angle=0, _DesignObj=NMOSWithDummy._NMOS(_Name='NMOS1In{}'.format(_Name)))[0]
		self._DesignParameter['_NMOS1']['_DesignObj']._CalculateNMOSDesignParameter(**NMOS1inputs)
		self._DesignParameter['_NMOS1']['_XYCoordinates'] = _XYCoordinatesofNMOS



		##################################### NMOS2 generation #####################################
		NMOS2inputs = copy.deepcopy(NMOSWithDummy._NMOS._ParametersForDesignCalculation)
		NMOS2inputs['_NMOSNumberofGate'] = _NMOSNumberofGate2
		NMOS2inputs['_NMOSDummy'] = _NMOSDummy2
		NMOS2inputs['_GateSpacing'] = _GateSpacing2
		NMOS2inputs['_SDWidth'] = _SDWidth2
		NMOS2inputs['_XVT'] = _XVT
		NMOS2inputs['_PCCrit'] = _PCCrit

		if _NMOSChannelWidth2 == None:
			NMOS2inputs['_NMOSChannelWidth'] = _NMOSChannelWidth1
		else:
			NMOS2inputs['_NMOSChannelWidth'] = _NMOSChannelWidth2

		if _NMOSChannellength2 == None:
			NMOS2inputs['_NMOSChannellength'] = _NMOSChannellength1
		else:
			NMOS2inputs['_NMOSChannellength'] = _NMOSChannellength2

		self._DesignParameter['_NMOS2'] = self._SrefElementDeclaration(_Reflect = [1,0,0], _Angle=0, _DesignObj=NMOSWithDummy._NMOS(_Name='NMOS2In{}'.format(_Name)))[0]
		self._DesignParameter['_NMOS2']['_DesignObj']._CalculateNMOSDesignParameter(**NMOS2inputs)

		if _NMOSNumberofGate1 % 2 == 0:
			_spacebtwnmos1 = (_NMOSNumberofGate1 // 2 + 0.5) * (_DRCObj._PolygateMinSpace + _DRCObj._PolygateMinWidth + (NMOS1inputs['_NMOSChannellength'] - _DRCObj._PolygateMinWidth))
		else:
			_spacebtwnmos1 = (_NMOSNumberofGate1 // 2 + 1) * (_DRCObj._PolygateMinSpace + _DRCObj._PolygateMinWidth + (NMOS1inputs['_NMOSChannellength'] - _DRCObj._PolygateMinWidth))

		if _NMOSNumberofGate2 % 2 == 0:
			_spacebtwnmos2 = (_NMOSNumberofGate2 // 2 + 0.5) * (_DRCObj._PolygateMinSpace + _DRCObj._PolygateMinWidth + (NMOS2inputs['_NMOSChannellength'] - _DRCObj._PolygateMinWidth))
		else:
			_spacebtwnmos2 = (_NMOSNumberofGate2 // 2 + 1) * (_DRCObj._PolygateMinSpace + _DRCObj._PolygateMinWidth + (NMOS2inputs['_NMOSChannellength'] - _DRCObj._PolygateMinWidth))

		self._DesignParameter['_NMOS2']['_XYCoordinates'] = [[_XYCoordinatesofNMOS[0][0] - _spacebtwnmos1 - _spacebtwnmos2 - (abs(NMOS1inputs['_NMOSChannellength'] - NMOS2inputs['_NMOSChannellength'])) // 2, _XYCoordinatesofNMOS[0][1]],
															[_XYCoordinatesofNMOS[0][0] + _spacebtwnmos1 + _spacebtwnmos2 + (abs(NMOS1inputs['_NMOSChannellength'] - NMOS2inputs['_NMOSChannellength'])) // 2, _XYCoordinatesofNMOS[0][1]]]



		##################################### NMOS3 generation #####################################
		NMOS3inputs = copy.deepcopy(NMOSWithDummy._NMOS._ParametersForDesignCalculation)
		NMOS3inputs['_NMOSNumberofGate'] = _NMOSNumberofGate3
		NMOS3inputs['_NMOSDummy'] = _NMOSDummy3
		NMOS3inputs['_GateSpacing'] = _GateSpacing3
		NMOS3inputs['_SDWidth'] = _SDWidth3
		NMOS3inputs['_XVT'] = _XVT
		NMOS3inputs['_PCCrit'] = _PCCrit

		if _NMOSChannelWidth3 == None:
			NMOS3inputs['_NMOSChannelWidth'] = _NMOSChannelWidth1
		else:
			NMOS3inputs['_NMOSChannelWidth'] = _NMOSChannelWidth3

		if _NMOSChannellength3 == None:
			NMOS3inputs['_NMOSChannellength'] = _NMOSChannellength1
		else:
			NMOS3inputs['_NMOSChannellength'] = _NMOSChannellength3

		self._DesignParameter['_NMOS3'] = self._SrefElementDeclaration(_Reflect = [1,0,0], _Angle=0, _DesignObj=NMOSWithDummy._NMOS(_Name='NMOS3In{}'.format(_Name)))[0]
		self._DesignParameter['_NMOS3']['_DesignObj']._CalculateNMOSDesignParameter(**NMOS3inputs)
		if _NMOSNumberofGate3 % 2 == 0:
			_spacebtwnmos3 = (_NMOSNumberofGate3 // 2 + 0.5) * (_DRCObj._PolygateMinSpace + _DRCObj._PolygateMinWidth + (NMOS3inputs['_NMOSChannellength'] - _DRCObj._PolygateMinWidth))
		else:
			_spacebtwnmos3 = (_NMOSNumberofGate3 // 2 + 1) * (_DRCObj._PolygateMinSpace + _DRCObj._PolygateMinWidth + (NMOS3inputs['_NMOSChannellength'] - _DRCObj._PolygateMinWidth))
		self._DesignParameter['_NMOS3']['_XYCoordinates'] = [[self._DesignParameter['_NMOS2']['_XYCoordinates'][0][0] - _spacebtwnmos2 - _spacebtwnmos3 - (abs(NMOS2inputs['_NMOSChannellength'] - NMOS3inputs['_NMOSChannellength'])) // 2, _XYCoordinatesofNMOS[0][1]],
															 [self._DesignParameter['_NMOS2']['_XYCoordinates'][1][0] + _spacebtwnmos2 + _spacebtwnmos3 + (abs(NMOS2inputs['_NMOSChannellength'] - NMOS3inputs['_NMOSChannellength'])) // 2, _XYCoordinatesofNMOS[0][1]]]



		##################################### NMOS4 generation #####################################
		NMOS4inputs = copy.deepcopy(NMOSWithDummy._NMOS._ParametersForDesignCalculation)
		NMOS4inputs['_NMOSNumberofGate'] = _NMOSNumberofGate4
		NMOS4inputs['_NMOSDummy'] = _NMOSDummy4
		NMOS4inputs['_GateSpacing'] = _GateSpacing4
		NMOS4inputs['_SDWidth'] = _SDWidth4
		NMOS4inputs['_XVT'] = _XVT
		NMOS4inputs['_PCCrit'] = _PCCrit

		if _NMOSChannelWidth4 == None:
			NMOS4inputs['_NMOSChannelWidth'] = _NMOSChannelWidth1
		else:
			NMOS4inputs['_NMOSChannelWidth'] = _NMOSChannelWidth4

		if _NMOSChannellength4 == None:
			NMOS4inputs['_NMOSChannellength'] = _NMOSChannellength1
		else:
			NMOS4inputs['_NMOSChannellength'] = _NMOSChannellength4

		self._DesignParameter['_NMOS4'] = self._SrefElementDeclaration(_Reflect = [1,0,0], _Angle=0, _DesignObj=NMOSWithDummy._NMOS(_Name='NMOS4In{}'.format(_Name)))[0]
		self._DesignParameter['_NMOS4']['_DesignObj']._CalculateNMOSDesignParameter(**NMOS4inputs)
		if _NMOSNumberofGate4 % 2 == 0:
			_spacebtwnmos4 = (_NMOSNumberofGate4 // 2 + 0.5) * (_DRCObj._PolygateMinSpace + _DRCObj._PolygateMinWidth + (NMOS4inputs['_NMOSChannellength'] - _DRCObj._PolygateMinWidth))
		else:
			_spacebtwnmos4 = (_NMOSNumberofGate4 // 2 + 1) * (_DRCObj._PolygateMinSpace + _DRCObj._PolygateMinWidth + (NMOS4inputs['_NMOSChannellength'] - _DRCObj._PolygateMinWidth))
		self._DesignParameter['_NMOS4']['_XYCoordinates'] = [[self._DesignParameter['_NMOS3']['_XYCoordinates'][0][0] - _spacebtwnmos3 - _spacebtwnmos4 - (abs(NMOS3inputs['_NMOSChannellength'] - NMOS4inputs['_NMOSChannellength'])) // 2, _XYCoordinatesofNMOS[0][1]],
															 [self._DesignParameter['_NMOS3']['_XYCoordinates'][1][0] + _spacebtwnmos3 + _spacebtwnmos4 + (abs(NMOS3inputs['_NMOSChannellength'] - NMOS4inputs['_NMOSChannellength'])) // 2, _XYCoordinatesofNMOS[0][1]]]


		self._DesignParameter['_XVTLayer'] = self._BoundaryElementDeclaration(
			_Layer=DesignParameters._LayerMapping[_XVT][0],
			_Datatype=DesignParameters._LayerMapping[_XVT][1],
			_XWidth=self._DesignParameter['_NMOS4']['_XYCoordinates'][1][0] - self._DesignParameter['_NMOS4']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOS4']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth'] + 2 * _DRCObj._XvtMinEnclosureOfODX,
			_YWidth=max(self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth'],
						self._DesignParameter['_NMOS2']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth'],
						self._DesignParameter['_NMOS3']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth'],
						self._DesignParameter['_NMOS4']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth']) + 2 * _DRCObj._XvtMinEnclosureOfODY,
			_XYCoordinates=_XYCoordinatesofNMOS)



		################################# PbodyContact1 generation #################################
		Pbodyinputs = copy.deepcopy(PbodyContact._PbodyContact._ParametersForDesignCalculation)
		Pbodyinputs['_NumberOfPbodyCOX'] = _NumberOfPbodyCOX
		Pbodyinputs['_NumberOfPbodyCOY'] = _NumberOfPbodyCOY
		Pbodyinputs['_Met1XWidth'] = _Met1XWidth
		Pbodyinputs['_Met1YWidth'] = _Met1YWidth

		self._DesignParameter['_PbodyContact1'] = self._SrefElementDeclaration(_DesignObj=PbodyContact._PbodyContact(_Name='PbodyContact1In{}'.format(_Name)))[0]
		self._DesignParameter['_PbodyContact1']['_DesignObj']._CalculatePbodyContactDesignParameter(**dict(_NumberOfPbodyCOX = int(((_XYCoordinatesofNMOS[0][0] - self._DesignParameter['_NMOS4']['_XYCoordinates'][0][0] + _spacebtwnmos4 + NMOS4inputs['_NMOSChannellength']) // (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace)) * 2),
																										  _NumberOfPbodyCOY = _NumberOfPbodyCOY, _Met1XWidth = _Met1XWidth, _Met1YWidth = _Met1YWidth))
		# self._DesignParameter['_PbodyContact1']['_XYCoordinates'] = [[_XYCoordinatesofNMOS[0][0],
		# 															_XYCoordinatesofNMOS[0][1] - _NMOSChannelWidth1 // 2 - _DRCObj._PolygateMinExtensionOnOD - _DRCObj._Metal1MinWidth - _DRCObj._PolylayeroverOd - self._DesignParameter['_PbodyContact1']['_DesignObj']._DesignParameter['_PPLayer']['_YWidth'] // 2]]



		################################### Resistor generation ###################################
		Resinputs = copy.deepcopy(opppcres_b._Opppcres._ParametersForDesignCalculation)
		Resinputs['_ResWidth'] = _ResWidth # poly Ywidth(b.o. rotate 90)
		Resinputs['_ResLength'] = _ResLength # OP Xwidth(b.o. rotate 90)
		Resinputs['_CONUMX'] = _CONUMX
		Resinputs['_CONUMY'] = _CONUMY

		self._DesignParameter['_Resistor'] = self._SrefElementDeclaration(_Reflect = [1,0,0], _Angle=90, _DesignObj=opppcres_b._Opppcres(_Name='Opppcres_bIn{}'.format(_Name)))[0]
		self._DesignParameter['_Resistor']['_DesignObj']._CalculateOpppcresDesignParameter(**Resinputs)
		# self._DesignParameter['_Resistor']['_XYCoordinates'] = [[self._DesignParameter['_PbodyContact']['_XYCoordinates'][0][0],
		# 														 self._DesignParameter['_PbodyContact']['_XYCoordinates'][0][1] - self._DesignParameter['_PbodyContact']['_DesignObj']._DesignParameter['_PPLayer']['_YWidth'] // 2 - _DRCObj._PpMinSpacetoPRES - _DRCObj._PRESlayeroverPoly - _ResWidth // 2]]



		##################################### NCAP generation #####################################
		NCAPinputs = copy.deepcopy(NCAP._NCap._ParametersForDesignCalculation)
		NCAPinputs['_XWidth'] = _XWidth
		NCAPinputs['_YWidth'] = _YWidth
		NCAPinputs['_NumofGates'] = _NumofGates
		NCAPinputs['NumOfCOX'] = NumOfCOX
		NCAPinputs['NumOfCOY'] = NumOfCOY
		NCAPinputs['Guardring'] = Guardring
		NCAPinputs['guardring_height'] = guardring_height
		NCAPinputs['guardring_width'] = guardring_width
		NCAPinputs['guardring_right'] = guardring_right
		NCAPinputs['guardring_left'] = guardring_left
		NCAPinputs['guardring_top'] = guardring_top
		NCAPinputs['guardring_bot'] = guardring_bot
		NCAPinputs['_NumofOD'] = _NumofOD
		NCAPinputs['_ViaPoly2Met1NumberOfCOX'] = _ViaPoly2Met1NumberOfCOX_CAP
		NCAPinputs['_ViaPoly2Met1NumberOfCOY'] = _ViaPoly2Met1NumberOfCOY_CAP


		self._DesignParameter['_NCAP'] = self._SrefElementDeclaration(_Reflect = [1,0,0], _Angle=90, _DesignObj=NCAP._NCap(_Name='NCAPIn{}'.format(_Name)))[0]
		self._DesignParameter['_NCAP']['_DesignObj']._CalculateNCapDesignParameter(**NCAPinputs)
		# self._DesignParameter['_NCAP']['_XYCoordinates'] = [[_XYCoordinatesofNMOS[0][0] - self._DesignParameter['_Resistor']['_DesignObj']._DesignParameter['_PRESLayer']['_YWidth'] // 2
		# 													 - _DRCObj._PolygateMinEnclosureByNcap - _YWidth // 2,
		# 													 self._DesignParameter['_PbodyContact1']['_XYCoordinates'][0][1] - self._DesignParameter['_PbodyContact1']['_DesignObj']._DesignParameter['_PPLayer']['_YWidth'] // 2 - self._DesignParameter['_NCAP']['_DesignObj']._DesignParameter['NWELL']['_XWidth'] // 2],
		# 													[_XYCoordinatesofNMOS[0][0] + self._DesignParameter['_Resistor']['_DesignObj']._DesignParameter['_PRESLayer']['_YWidth'] // 2
		# 													 + _DRCObj._PolygateMinEnclosureByNcap + _YWidth // 2,
		# 													 self._DesignParameter['_PbodyContact1']['_XYCoordinates'][0][1] - self._DesignParameter['_PbodyContact1']['_DesignObj']._DesignParameter['_PPLayer']['_YWidth'] // 2 - self._DesignParameter['_NCAP']['_DesignObj']._DesignParameter['NWELL']['_XWidth'] // 2]]

		# self._DesignParameter['_Resistor']['_XYCoordinates'] = [[_XYCoordinatesofNMOS[0][0], self._DesignParameter['_NCAP']['_XYCoordinates'][0][1]]]


		self._DesignParameter['_PbodyContact1']['_DesignObj']._CalculatePbodyContactDesignParameter(**dict(_NumberOfPbodyCOX=max(int(((_XYCoordinatesofNMOS[0][0] - self._DesignParameter['_NMOS4']['_XYCoordinates'][0][0] + _spacebtwnmos4 + _NMOSChannellength1) // (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace)) * 2),
																																 int((self._DesignParameter['_Resistor']['_DesignObj']._DesignParameter['_PRESLayer']['_YWidth'] + self._DesignParameter['_NCAP']['_DesignObj']._DesignParameter['NWELL']['_YWidth'] * 2) // (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace))),
																										   _NumberOfPbodyCOY=_NumberOfPbodyCOY, _Met1XWidth=_Met1XWidth, _Met1YWidth=_Met1YWidth))

		self._DesignParameter['_PbodyContact1']['_DesignObj']._DesignParameter['_PPLayer']['_YWidth'] = self._DesignParameter['_PbodyContact1']['_DesignObj']._DesignParameter['_PPLayer']['_YWidth'] + _DRCObj._PpMinEnclosureOfPactiveY * 2

		self._DesignParameter['_PbodyContact1']['_XYCoordinates'] = [[_XYCoordinatesofNMOS[0][0],
																	_XYCoordinatesofNMOS[0][1] - _NMOSChannelWidth1 // 2 - _DRCObj._PolygateMinExtensionOnOD - _DRCObj._Metal1MinWidth - _DRCObj._PolylayeroverOd - self._DesignParameter['_PbodyContact1']['_DesignObj']._DesignParameter['_PPLayer']['_YWidth'] // 2]]

		self._DesignParameter['_NCAP']['_XYCoordinates'] = [[_XYCoordinatesofNMOS[0][0] - self._DesignParameter['_Resistor']['_DesignObj']._DesignParameter['_PRESLayer']['_YWidth'] // 2
															 - _DRCObj._PolygateMinEnclosureByNcap - _YWidth // 2,
															 self._DesignParameter['_PbodyContact1']['_XYCoordinates'][0][1] - self._DesignParameter['_PbodyContact1']['_DesignObj']._DesignParameter['_PPLayer']['_YWidth'] // 2 - self._DesignParameter['_NCAP']['_DesignObj']._DesignParameter['NWELL']['_XWidth'] // 2],
															[_XYCoordinatesofNMOS[0][0] + self._DesignParameter['_Resistor']['_DesignObj']._DesignParameter['_PRESLayer']['_YWidth'] // 2
															 + _DRCObj._PolygateMinEnclosureByNcap + _YWidth // 2,
															 self._DesignParameter['_PbodyContact1']['_XYCoordinates'][0][1] - self._DesignParameter['_PbodyContact1']['_DesignObj']._DesignParameter['_PPLayer']['_YWidth'] // 2 - self._DesignParameter['_NCAP']['_DesignObj']._DesignParameter['NWELL']['_XWidth'] // 2]]

		self._DesignParameter['_Resistor']['_XYCoordinates'] = [[_XYCoordinatesofNMOS[0][0], self._DesignParameter['_NCAP']['_XYCoordinates'][0][1]]]



		################################# PbodyContact2 generation #################################
		self._DesignParameter['_PbodyContact2'] = self._SrefElementDeclaration(_DesignObj=PbodyContact._PbodyContact(_Name='PbodyContact2In{}'.format(_Name)))[0]
		self._DesignParameter['_PbodyContact2']['_DesignObj']._CalculatePbodyContactDesignParameter(**dict(_NumberOfPbodyCOX=max(int(((_XYCoordinatesofNMOS[0][0] - self._DesignParameter['_NMOS4']['_XYCoordinates'][0][0] + _spacebtwnmos4 + _NMOSChannellength1) // (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace)) * 2),
																																 int((self._DesignParameter['_Resistor']['_DesignObj']._DesignParameter['_PRESLayer']['_YWidth'] + self._DesignParameter['_NCAP']['_DesignObj']._DesignParameter['NWELL']['_YWidth'] * 2) // (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace))),
																										   _NumberOfPbodyCOY=_NumberOfPbodyCOY, _Met1XWidth=_Met1XWidth, _Met1YWidth=_Met1YWidth))
		self._DesignParameter['_PbodyContact2']['_XYCoordinates'] = [[_XYCoordinatesofNMOS[0][0],
																	  self._DesignParameter['_NCAP']['_XYCoordinates'][0][1] - self._DesignParameter['_NCAP']['_DesignObj']._DesignParameter['NWELL']['_XWidth'] // 2 - self._DesignParameter['_PbodyContact1']['_DesignObj']._DesignParameter['_PPLayer']['_YWidth'] // 2]]

		self._DesignParameter['_PbodyContact2']['_DesignObj']._DesignParameter['_PPLayer']['_XWidth'] = self._DesignParameter['_PbodyContact1']['_DesignObj']._DesignParameter['_PPLayer']['_XWidth']
		self._DesignParameter['_PbodyContact2']['_DesignObj']._DesignParameter['_PPLayer']['_YWidth'] = self._DesignParameter['_PbodyContact1']['_DesignObj']._DesignParameter['_PPLayer']['_YWidth']



		################################# Supply Routing #################################
		self._DesignParameter['_NMOS1toSupplyRouting'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0],
																					  _Datatype=DesignParameters._LayerMapping['METAL1'][1],
																					  _Width=self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth'] - (_DRCObj._CoMinEnclosureByOD - _DRCObj._Metal1MinEnclosureCO) * 2)
		self._DesignParameter['_NMOS1toSupplyRouting']['_XYCoordinates'] = [[self._DesignParameter['_NMOS1']['_XYCoordinates'][0], [self._DesignParameter['_NMOS1']['_XYCoordinates'][0][0], self._DesignParameter['_PbodyContact1']['_XYCoordinates'][0][1]]]]


		self._DesignParameter['_NMOS4toSupplyRouting'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0],
																					  _Datatype=DesignParameters._LayerMapping['METAL1'][1],
																					  _Width=self._DesignParameter['_NMOS4']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth'] - (_DRCObj._CoMinEnclosureByOD - _DRCObj._Metal1MinEnclosureCO) * 2)
		self._DesignParameter['_NMOS4toSupplyRouting']['_XYCoordinates'] = [[self._DesignParameter['_NMOS4']['_XYCoordinates'][0], [self._DesignParameter['_NMOS4']['_XYCoordinates'][0][0], self._DesignParameter['_PbodyContact1']['_XYCoordinates'][0][1]]],
																			[self._DesignParameter['_NMOS4']['_XYCoordinates'][1], [self._DesignParameter['_NMOS4']['_XYCoordinates'][1][0], self._DesignParameter['_PbodyContact1']['_XYCoordinates'][0][1]]]]


		self._DesignParameter['_NCAPtoSupplyRouting'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0],
																					  _Datatype=DesignParameters._LayerMapping['METAL1'][1],
																					  _Width=self._DesignParameter['_NCAP']['_DesignObj']._DesignParameter['NWELL']['_XWidth'] // 3)
		self._DesignParameter['_NCAPtoSupplyRouting']['_XYCoordinates'] = [[[self._DesignParameter['_NCAP']['_XYCoordinates'][0][0], self._DesignParameter['_PbodyContact1']['_XYCoordinates'][0][1]], [self._DesignParameter['_NCAP']['_XYCoordinates'][0][0], self._DesignParameter['_PbodyContact2']['_XYCoordinates'][0][1]]],
																		   [[self._DesignParameter['_NCAP']['_XYCoordinates'][1][0], self._DesignParameter['_PbodyContact1']['_XYCoordinates'][0][1]], [self._DesignParameter['_NCAP']['_XYCoordinates'][1][0], self._DesignParameter['_PbodyContact2']['_XYCoordinates'][0][1]]]]



		################################# Via generation for NMOS1 Polygate #################################
		_LenBtwNMOS1Gates = self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_XYCoordinateNMOSGateRouting']['_XYCoordinates'][-1][0] \
						   - self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_XYCoordinateNMOSGateRouting']['_XYCoordinates'][0][0]

		_VIANMOS1Poly2Met1 = copy.deepcopy(ViaPoly2Met1._ViaPoly2Met1._ParametersForDesignCalculation)
		_tmpNumCOX1 = int((_LenBtwNMOS1Gates + NMOS1inputs['_NMOSChannellength']) // (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace))

		if _tmpNumCOX1 < 1:
			_tmpNumCOX1 = 1

		if _ViaPoly2Met1NumberOfCOX != None:
			_tmpNumCOX1 = _ViaPoly2Met1NumberOfCOX

		if _ViaPoly2Met1NumberOfCOY == None:
			_tmpNumCOY1 = 1
		else:
			_tmpNumCOY1 = _ViaPoly2Met1NumberOfCOY


		_VIANMOS1Poly2Met1['_ViaPoly2Met1NumberOfCOX'] = _tmpNumCOX1
		_VIANMOS1Poly2Met1['_ViaPoly2Met1NumberOfCOY'] = _tmpNumCOY1

		self._DesignParameter['_VIANMOS1Poly2Met1'] = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_DesignParameter=None, _Name='ViaPoly2Met1OnNMOSGate1In{}'.format(_Name)))[0]
		self._DesignParameter['_VIANMOS1Poly2Met1']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(**_VIANMOS1Poly2Met1)


		self._DesignParameter['_VIANMOS1Poly2Met1']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] = _LenBtwNMOS1Gates + NMOS1inputs['_NMOSChannellength']
		self._DesignParameter['_VIANMOS1Poly2Met1']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] = _LenBtwNMOS1Gates + NMOS1inputs['_NMOSChannellength']
		self._DesignParameter['_VIANMOS1Poly2Met1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] = self._DesignParameter['_VIANMOS1Poly2Met1']['_DesignObj']._DesignParameter['_POLayer']['_YWidth']

		YCoordinateofNPoly1 = self._DesignParameter['_NMOS1']['_XYCoordinates'][0][1]\
							 - max(self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'], self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_PODummyLayer']['_YWidth']) // 2 \
							 - self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_POLayerPINDrawing']['_YWidth'] // 2
		self._DesignParameter['_VIANMOS1Poly2Met1']['_XYCoordinates'] = [[self._DesignParameter['_NMOS1']['_XYCoordinates'][0][0], YCoordinateofNPoly1]]


		################################# Via generation for NMOS2 Polygate #################################
		# Poly 2 Met1
		_LenBtwNMOS2Gates = self._DesignParameter['_NMOS2']['_DesignObj']._DesignParameter['_XYCoordinateNMOSGateRouting']['_XYCoordinates'][-1][0] \
						   - self._DesignParameter['_NMOS2']['_DesignObj']._DesignParameter['_XYCoordinateNMOSGateRouting']['_XYCoordinates'][0][0]

		_VIANMOS2Poly2Met1 = copy.deepcopy(ViaPoly2Met1._ViaPoly2Met1._ParametersForDesignCalculation)
		_tmpNumCOX2 = int((_LenBtwNMOS2Gates + NMOS2inputs['_NMOSChannellength']) // (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace))

		if _tmpNumCOX2 < 1:
			_tmpNumCOX2 = 1

		if _ViaPoly2Met1NumberOfCOX != None:
			_tmpNumCOX2 = _ViaPoly2Met1NumberOfCOX

		if _ViaPoly2Met1NumberOfCOY == None:
			_tmpNumCOY2 = 1
		else:
			_tmpNumCOY2 = _ViaPoly2Met1NumberOfCOY


		_VIANMOS2Poly2Met1['_ViaPoly2Met1NumberOfCOX'] = _tmpNumCOX2
		_VIANMOS2Poly2Met1['_ViaPoly2Met1NumberOfCOY'] = _tmpNumCOY2

		self._DesignParameter['_VIANMOS2Poly2Met1'] = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_DesignParameter=None, _Name='ViaPoly2Met1OnNMOSGate2In{}'.format(_Name)))[0]
		self._DesignParameter['_VIANMOS2Poly2Met1']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(**_VIANMOS2Poly2Met1)


		self._DesignParameter['_VIANMOS2Poly2Met1']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] = _LenBtwNMOS2Gates + NMOS2inputs['_NMOSChannellength']
		self._DesignParameter['_VIANMOS2Poly2Met1']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] = _LenBtwNMOS2Gates + NMOS2inputs['_NMOSChannellength']
		self._DesignParameter['_VIANMOS2Poly2Met1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] = self._DesignParameter['_VIANMOS2Poly2Met1']['_DesignObj']._DesignParameter['_POLayer']['_YWidth']

		YCoordinateofNPoly2 = self._DesignParameter['_NMOS2']['_XYCoordinates'][0][1]\
							 - max(self._DesignParameter['_NMOS2']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'], self._DesignParameter['_NMOS2']['_DesignObj']._DesignParameter['_PODummyLayer']['_YWidth']) // 2 \
							 - self._DesignParameter['_NMOS2']['_DesignObj']._DesignParameter['_POLayerPINDrawing']['_YWidth'] // 2
		self._DesignParameter['_VIANMOS2Poly2Met1']['_XYCoordinates'] = [[self._DesignParameter['_NMOS2']['_XYCoordinates'][0][0], YCoordinateofNPoly2],
																		 [self._DesignParameter['_NMOS2']['_XYCoordinates'][1][0], YCoordinateofNPoly2]]

		del _tmpNumCOX2, _tmpNumCOY2

		# Met1 2 Met2
		_VIANMOS2Met12Met2 = copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation)
		# _tmpNumCOX2 = _VIANMOS2Poly2Met1['_ViaPoly2Met1NumberOfCOX'] - 2
		_tmpNumCOX2 = 2

		if _tmpNumCOX2 < 1:
			_tmpNumCOX2 = 1

		if _ViaMet12Met2NumberOfCOX != None:
			_tmpNumCOX2 = _ViaMet12Met2NumberOfCOX

		if _ViaMet12Met2NumberOfCOY == None:
			_tmpNumCOY2 = 1
		else:
			_tmpNumCOY2 = _ViaMet12Met2NumberOfCOY


		_VIANMOS2Met12Met2['_ViaMet12Met2NumberOfCOX'] = _tmpNumCOX2
		_VIANMOS2Met12Met2['_ViaMet12Met2NumberOfCOY'] = _tmpNumCOY2

		self._DesignParameter['_VIANMOS2Met12Met2'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_DesignParameter=None, _Name='ViaMet12Met2OnNMOSGate2In{}'.format(_Name)))[0]
		self._DesignParameter['_VIANMOS2Met12Met2']['_DesignObj']._CalculateViaMet12Met2DesignParameter(**_VIANMOS2Met12Met2)

		self._DesignParameter['_VIANMOS2Met12Met2']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] = self._DesignParameter['_VIANMOS2Poly2Met1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']
		self._DesignParameter['_VIANMOS2Met12Met2']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] = self._DesignParameter['_VIANMOS2Poly2Met1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']

		self._DesignParameter['_VIANMOS2Met12Met2']['_XYCoordinates'] = [[self._DesignParameter['_NMOS2']['_XYCoordinates'][0][0], YCoordinateofNPoly2],
																		 [self._DesignParameter['_NMOS2']['_XYCoordinates'][1][0], YCoordinateofNPoly2]]

		del _tmpNumCOX2, _tmpNumCOY2

		# Met2 2 Met3
		_VIANMOS2Met22Met3 = copy.deepcopy(ViaMet22Met3._ViaMet22Met3._ParametersForDesignCalculation)
		# _tmpNumCOX2 = _VIANMOS2Poly2Met1['_ViaPoly2Met1NumberOfCOX'] - 2
		_tmpNumCOX2 = 2

		if _tmpNumCOX2 < 1:
			_tmpNumCOX2 = 1

		if _ViaMet22Met3NumberOfCOX != None:
			_tmpNumCOX2 = _ViaMet22Met3NumberOfCOX

		if _ViaMet22Met3NumberOfCOY == None:
			_tmpNumCOY2 = 1
		else:
			_tmpNumCOY2 = _ViaMet22Met3NumberOfCOY


		_VIANMOS2Met22Met3['_ViaMet22Met3NumberOfCOX'] = _tmpNumCOX2
		_VIANMOS2Met22Met3['_ViaMet22Met3NumberOfCOY'] = _tmpNumCOY2

		self._DesignParameter['_VIANMOS2Met22Met3'] = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_DesignParameter=None, _Name='ViaMet22Met3OnNMOSGate2In{}'.format(_Name)))[0]
		self._DesignParameter['_VIANMOS2Met22Met3']['_DesignObj']._CalculateViaMet22Met3DesignParameter(**_VIANMOS2Met22Met3)

		self._DesignParameter['_VIANMOS2Met22Met3']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] = self._DesignParameter['_VIANMOS2Poly2Met1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']
		self._DesignParameter['_VIANMOS2Met22Met3']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth'] = self._DesignParameter['_VIANMOS2Poly2Met1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']

		self._DesignParameter['_VIANMOS2Met22Met3']['_XYCoordinates'] = [[self._DesignParameter['_NMOS2']['_XYCoordinates'][0][0], YCoordinateofNPoly2],
																		 [self._DesignParameter['_NMOS2']['_XYCoordinates'][1][0], YCoordinateofNPoly2]]

		del _tmpNumCOX2, _tmpNumCOY2


		################################# Via generation for NMOS3 Polygate #################################
		# Poly 2 Met1
		_LenBtwNMOS3Gates = self._DesignParameter['_NMOS3']['_DesignObj']._DesignParameter['_XYCoordinateNMOSGateRouting']['_XYCoordinates'][-1][0] \
						   - self._DesignParameter['_NMOS3']['_DesignObj']._DesignParameter['_XYCoordinateNMOSGateRouting']['_XYCoordinates'][0][0]

		_VIANMOS3Poly2Met1 = copy.deepcopy(ViaPoly2Met1._ViaPoly2Met1._ParametersForDesignCalculation)
		_tmpNumCOX3 = int((_LenBtwNMOS3Gates + NMOS3inputs['_NMOSChannellength']) // (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace))

		if _tmpNumCOX3 < 1:
			_tmpNumCOX3 = 1

		if _ViaPoly2Met1NumberOfCOX != None:
			_tmpNumCOX3 = _ViaPoly2Met1NumberOfCOX

		if _ViaPoly2Met1NumberOfCOY == None:
			_tmpNumCOY3 = 1
		else:
			_tmpNumCOY3 = _ViaPoly2Met1NumberOfCOY


		_VIANMOS3Poly2Met1['_ViaPoly2Met1NumberOfCOX'] = _tmpNumCOX3
		_VIANMOS3Poly2Met1['_ViaPoly2Met1NumberOfCOY'] = _tmpNumCOY3

		self._DesignParameter['_VIANMOS3Poly2Met1'] = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_DesignParameter=None, _Name='ViaPoly2Met1OnNMOSGate3In{}'.format(_Name)))[0]
		self._DesignParameter['_VIANMOS3Poly2Met1']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(**_VIANMOS3Poly2Met1)


		self._DesignParameter['_VIANMOS3Poly2Met1']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] = _LenBtwNMOS3Gates + NMOS3inputs['_NMOSChannellength']
		self._DesignParameter['_VIANMOS3Poly2Met1']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] = _LenBtwNMOS3Gates + NMOS3inputs['_NMOSChannellength']
		self._DesignParameter['_VIANMOS3Poly2Met1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] = self._DesignParameter['_VIANMOS3Poly2Met1']['_DesignObj']._DesignParameter['_POLayer']['_YWidth']

		YCoordinateofNPoly3 = self._DesignParameter['_NMOS3']['_XYCoordinates'][0][1]\
							 - max(self._DesignParameter['_NMOS3']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'], self._DesignParameter['_NMOS3']['_DesignObj']._DesignParameter['_PODummyLayer']['_YWidth']) // 2 \
							 - self._DesignParameter['_NMOS3']['_DesignObj']._DesignParameter['_POLayerPINDrawing']['_YWidth'] // 2
		self._DesignParameter['_VIANMOS3Poly2Met1']['_XYCoordinates'] = [[self._DesignParameter['_NMOS3']['_XYCoordinates'][0][0], YCoordinateofNPoly3],
																		 [self._DesignParameter['_NMOS3']['_XYCoordinates'][1][0], YCoordinateofNPoly3]]

		del _tmpNumCOX3, _tmpNumCOY3

		# Met1 2 Met2
		_VIANMOS3Met12Met2 = copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation)
		# _tmpNumCOX3 = _VIANMOS3Poly2Met1['_ViaPoly2Met1NumberOfCOX'] - 2
		_tmpNumCOX3 = 2

		if _tmpNumCOX3 < 1:
			_tmpNumCOX3 = 1

		if _ViaMet12Met2NumberOfCOX != None:
			_tmpNumCOX3 = _ViaMet12Met2NumberOfCOX

		if _ViaMet12Met2NumberOfCOY == None:
			_tmpNumCOY3 = 1
		else:
			_tmpNumCOY3 = _ViaMet12Met2NumberOfCOY

		_VIANMOS3Met12Met2['_ViaMet12Met2NumberOfCOX'] = _tmpNumCOX3
		_VIANMOS3Met12Met2['_ViaMet12Met2NumberOfCOY'] = _tmpNumCOY3

		self._DesignParameter['_VIANMOS3Met12Met2'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_DesignParameter=None, _Name='ViaMet12Met2OnNMOSGate3In{}'.format(_Name)))[0]
		self._DesignParameter['_VIANMOS3Met12Met2']['_DesignObj']._CalculateViaMet12Met2DesignParameter(**_VIANMOS3Met12Met2)

		self._DesignParameter['_VIANMOS3Met12Met2']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] = self._DesignParameter['_VIANMOS3Poly2Met1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']
		self._DesignParameter['_VIANMOS3Met12Met2']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] = self._DesignParameter['_VIANMOS3Poly2Met1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']

		self._DesignParameter['_VIANMOS3Met12Met2']['_XYCoordinates'] = [[self._DesignParameter['_NMOS3']['_XYCoordinates'][0][0], YCoordinateofNPoly3],
																		 [self._DesignParameter['_NMOS3']['_XYCoordinates'][1][0], YCoordinateofNPoly3]]

		del _tmpNumCOX3, _tmpNumCOY3

		# Met2 2 Met3
		_VIANMOS3Met22Met3 = copy.deepcopy(ViaMet22Met3._ViaMet22Met3._ParametersForDesignCalculation)
		# _tmpNumCOX2 = _VIANMOS2Poly2Met1['_ViaPoly2Met1NumberOfCOX'] - 2
		_tmpNumCOX3 = 2

		if _tmpNumCOX3 < 1:
			_tmpNumCOX3 = 1

		if _ViaMet22Met3NumberOfCOX != None:
			_tmpNumCOX3 = _ViaMet22Met3NumberOfCOX

		if _ViaMet22Met3NumberOfCOY == None:
			_tmpNumCOY3 = 1
		else:
			_tmpNumCOY3 = _ViaMet22Met3NumberOfCOY


		_VIANMOS3Met22Met3['_ViaMet22Met3NumberOfCOX'] = _tmpNumCOX3
		_VIANMOS3Met22Met3['_ViaMet22Met3NumberOfCOY'] = _tmpNumCOY3

		self._DesignParameter['_VIANMOS3Met22Met3'] = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_DesignParameter=None, _Name='ViaMet22Met3OnNMOSGate3In{}'.format(_Name)))[0]
		self._DesignParameter['_VIANMOS3Met22Met3']['_DesignObj']._CalculateViaMet22Met3DesignParameter(**_VIANMOS3Met22Met3)

		self._DesignParameter['_VIANMOS3Met22Met3']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] = self._DesignParameter['_VIANMOS2Poly2Met1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']
		self._DesignParameter['_VIANMOS3Met22Met3']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth'] = self._DesignParameter['_VIANMOS2Poly2Met1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']

		self._DesignParameter['_VIANMOS3Met22Met3']['_XYCoordinates'] = [[self._DesignParameter['_NMOS3']['_XYCoordinates'][0][0], YCoordinateofNPoly3],
																		 [self._DesignParameter['_NMOS3']['_XYCoordinates'][1][0], YCoordinateofNPoly3]]

		del _tmpNumCOX3, _tmpNumCOY3


		################################# Via generation for NMOS4 Polygate #################################
		_LenBtwNMOS4Gates = self._DesignParameter['_NMOS4']['_DesignObj']._DesignParameter['_XYCoordinateNMOSGateRouting']['_XYCoordinates'][-1][0] \
						   - self._DesignParameter['_NMOS4']['_DesignObj']._DesignParameter['_XYCoordinateNMOSGateRouting']['_XYCoordinates'][0][0]

		_VIANMOS4Poly2Met1 = copy.deepcopy(ViaPoly2Met1._ViaPoly2Met1._ParametersForDesignCalculation)
		_tmpNumCOX4 = int((_LenBtwNMOS4Gates + NMOS4inputs['_NMOSChannellength']) // (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace))

		if _tmpNumCOX4 < 1:
			_tmpNumCOX4 = 1

		if _ViaPoly2Met1NumberOfCOX != None:
			_tmpNumCOX4 = _ViaPoly2Met1NumberOfCOX

		if _ViaPoly2Met1NumberOfCOY == None:
			_tmpNumCOY4 = 1
		else:
			_tmpNumCOY4 = _ViaPoly2Met1NumberOfCOY


		_VIANMOS4Poly2Met1['_ViaPoly2Met1NumberOfCOX'] = _tmpNumCOX4
		_VIANMOS4Poly2Met1['_ViaPoly2Met1NumberOfCOY'] = _tmpNumCOY4

		self._DesignParameter['_VIANMOS4Poly2Met1'] = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_DesignParameter=None, _Name='ViaPoly2Met1OnNMOSGate4In{}'.format(_Name)))[0]
		self._DesignParameter['_VIANMOS4Poly2Met1']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(**_VIANMOS4Poly2Met1)


		self._DesignParameter['_VIANMOS4Poly2Met1']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] = _LenBtwNMOS4Gates + NMOS4inputs['_NMOSChannellength']
		self._DesignParameter['_VIANMOS4Poly2Met1']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] = _LenBtwNMOS4Gates + NMOS4inputs['_NMOSChannellength']
		self._DesignParameter['_VIANMOS4Poly2Met1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] = self._DesignParameter['_VIANMOS4Poly2Met1']['_DesignObj']._DesignParameter['_POLayer']['_YWidth']

		YCoordinateofNPoly4 = self._DesignParameter['_NMOS4']['_XYCoordinates'][0][1]\
							 - max(self._DesignParameter['_NMOS4']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'], self._DesignParameter['_NMOS4']['_DesignObj']._DesignParameter['_PODummyLayer']['_YWidth']) // 2 \
							 - self._DesignParameter['_NMOS4']['_DesignObj']._DesignParameter['_POLayerPINDrawing']['_YWidth'] // 2
		self._DesignParameter['_VIANMOS4Poly2Met1']['_XYCoordinates'] = [[self._DesignParameter['_NMOS4']['_XYCoordinates'][0][0], YCoordinateofNPoly4],
																		 [self._DesignParameter['_NMOS4']['_XYCoordinates'][1][0], YCoordinateofNPoly4]]



		################################# Additional PolyGate Routing #################################
		# extends polygate
		self._DesignParameter['_ExtendPolyOnNMOS1'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0],
																					   _Datatype=DesignParameters._LayerMapping['POLY'][1],
																					   _Width=NMOS1inputs['_NMOSChannellength'])
		tmppolyn1 = []
		for i in range(_NMOSNumberofGate1):
			tmppolyn1.append([[_XYCoordinatesofNMOS[0][0] - self._DesignParameter['_NMOS1']['_XYCoordinates'][0][0] - self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0], _XYCoordinatesofNMOS[0][1]],
							  [_XYCoordinatesofNMOS[0][0] - self._DesignParameter['_NMOS1']['_XYCoordinates'][0][0] - self._DesignParameter['_NMOS1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0], self._DesignParameter['_VIANMOS1Poly2Met1']['_XYCoordinates'][0][1]]])

		self._DesignParameter['_ExtendPolyOnNMOS1']['_XYCoordinates'] = tmppolyn1

		self._DesignParameter['_ExtendPolyOnNMOS2'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0],
																				   _Datatype=DesignParameters._LayerMapping['POLY'][1],
																				   _Width=NMOS2inputs['_NMOSChannellength'])
		tmppolyn2 = []
		for i in range(_NMOSNumberofGate2):
			tmppolyn2.append([[_XYCoordinatesofNMOS[0][0] - self._DesignParameter['_NMOS2']['_XYCoordinates'][0][0] - self._DesignParameter['_NMOS2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0], _XYCoordinatesofNMOS[0][1]],
							  [_XYCoordinatesofNMOS[0][0] - self._DesignParameter['_NMOS2']['_XYCoordinates'][0][0] - self._DesignParameter['_NMOS2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0], self._DesignParameter['_VIANMOS2Poly2Met1']['_XYCoordinates'][0][1]]])
			tmppolyn2.append([[_XYCoordinatesofNMOS[0][0] + self._DesignParameter['_NMOS2']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOS2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0], _XYCoordinatesofNMOS[0][1]],
							  [_XYCoordinatesofNMOS[0][0] + self._DesignParameter['_NMOS2']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOS2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0], self._DesignParameter['_VIANMOS2Poly2Met1']['_XYCoordinates'][0][1]]])

		self._DesignParameter['_ExtendPolyOnNMOS2']['_XYCoordinates'] = tmppolyn2

		self._DesignParameter['_ExtendPolyOnNMOS3'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0],
																				   _Datatype=DesignParameters._LayerMapping['POLY'][1],
																				   _Width=NMOS3inputs['_NMOSChannellength'])
		tmppolyn3 = []
		for i in range(_NMOSNumberofGate3):
			tmppolyn3.append([[_XYCoordinatesofNMOS[0][0] - self._DesignParameter['_NMOS3']['_XYCoordinates'][0][0] - self._DesignParameter['_NMOS3']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0], _XYCoordinatesofNMOS[0][1]],
							  [_XYCoordinatesofNMOS[0][0] - self._DesignParameter['_NMOS3']['_XYCoordinates'][0][0] - self._DesignParameter['_NMOS3']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0], self._DesignParameter['_VIANMOS3Poly2Met1']['_XYCoordinates'][0][1]]])
			tmppolyn3.append([[_XYCoordinatesofNMOS[0][0] + self._DesignParameter['_NMOS3']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOS3']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0], _XYCoordinatesofNMOS[0][1]],
							  [_XYCoordinatesofNMOS[0][0] + self._DesignParameter['_NMOS3']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOS3']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0], self._DesignParameter['_VIANMOS3Poly2Met1']['_XYCoordinates'][0][1]]])

		self._DesignParameter['_ExtendPolyOnNMOS3']['_XYCoordinates'] = tmppolyn3

		self._DesignParameter['_ExtendPolyOnNMOS4'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0],
																				   _Datatype=DesignParameters._LayerMapping['POLY'][1],
																				   _Width=NMOS4inputs['_NMOSChannellength'])
		tmppolyn4 = []
		for i in range(_NMOSNumberofGate4):
			tmppolyn4.append([[_XYCoordinatesofNMOS[0][0] - self._DesignParameter['_NMOS4']['_XYCoordinates'][0][0] - self._DesignParameter['_NMOS4']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0], _XYCoordinatesofNMOS[0][1]],
							  [_XYCoordinatesofNMOS[0][0] - self._DesignParameter['_NMOS4']['_XYCoordinates'][0][0] - self._DesignParameter['_NMOS4']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0], self._DesignParameter['_VIANMOS4Poly2Met1']['_XYCoordinates'][0][1]]])
			tmppolyn4.append([[_XYCoordinatesofNMOS[0][0] + self._DesignParameter['_NMOS4']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOS4']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0], _XYCoordinatesofNMOS[0][1]],
							  [_XYCoordinatesofNMOS[0][0] + self._DesignParameter['_NMOS4']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOS4']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0], self._DesignParameter['_VIANMOS4Poly2Met1']['_XYCoordinates'][0][1]]])

		self._DesignParameter['_ExtendPolyOnNMOS4']['_XYCoordinates'] = tmppolyn4

		# NMOS2
		self._DesignParameter['_AdditionalPolyOnNMOS2'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _XYCoordinates=[], _Width=NMOS2inputs['_NMOSChannellength'])
		Mov2NMOS2XCoordinates = _XYCoordinatesofNMOS[0][0] + self._DesignParameter['_NMOS2']['_XYCoordinates'][0][0]

		self._DesignParameter['_AdditionalPolyOnNMOS2']['_XYCoordinates'] = [[[self._DesignParameter['_NMOS2']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][-1][0] - Mov2NMOS2XCoordinates, self._DesignParameter['_NMOS2']['_XYCoordinates'][-1][1]],
																			 [self._DesignParameter['_NMOS2']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][-1][0] - Mov2NMOS2XCoordinates, self._DesignParameter['_VIANMOS2Poly2Met1']['_XYCoordinates'][0][1]],
																			 [self._DesignParameter['_NMOS2']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][0] - Mov2NMOS2XCoordinates, self._DesignParameter['_VIANMOS2Poly2Met1']['_XYCoordinates'][0][1]],
																			 [self._DesignParameter['_NMOS2']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][0] - Mov2NMOS2XCoordinates, self._DesignParameter['_NMOS2']['_XYCoordinates'][0][1]]],
																			[[self._DesignParameter['_NMOS2']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][-1][0] + Mov2NMOS2XCoordinates, self._DesignParameter['_NMOS2']['_XYCoordinates'][-1][1]],
																			 [self._DesignParameter['_NMOS2']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][-1][0] + Mov2NMOS2XCoordinates, self._DesignParameter['_VIANMOS2Poly2Met1']['_XYCoordinates'][0][1]],
																			 [self._DesignParameter['_NMOS2']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][0] + Mov2NMOS2XCoordinates, self._DesignParameter['_VIANMOS2Poly2Met1']['_XYCoordinates'][0][1]],
																			 [self._DesignParameter['_NMOS2']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][0] + Mov2NMOS2XCoordinates, self._DesignParameter['_NMOS2']['_XYCoordinates'][0][1]]]]

		self._DesignParameter['_AdditionalPOBoundaryOnNMOS2'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0],
																								 _Datatype=DesignParameters._LayerMapping['POLY'][1],
																								 _XWidth=self._DesignParameter['_NMOS2']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][-1][0] - self._DesignParameter['_NMOS2']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][0] + NMOS2inputs['_NMOSChannellength'],
																								 _YWidth=self._DesignParameter['_VIANMOS2Poly2Met1']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'],
																								 _XYCoordinates=[[-Mov2NMOS2XCoordinates, self._DesignParameter['_VIANMOS2Poly2Met1']['_XYCoordinates'][0][1]],
																												 [Mov2NMOS2XCoordinates, self._DesignParameter['_VIANMOS2Poly2Met1']['_XYCoordinates'][0][1]]])

		#NMOS3
		self._DesignParameter['_AdditionalPolyOnNMOS3'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _XYCoordinates=[], _Width=NMOS4inputs['_NMOSChannellength'])
		Mov2NMOS3XCoordinates = _XYCoordinatesofNMOS[0][0] + self._DesignParameter['_NMOS3']['_XYCoordinates'][0][0]
		Mov2NMOS4XCoordinates = _XYCoordinatesofNMOS[0][0] + self._DesignParameter['_NMOS4']['_XYCoordinates'][0][0]

		self._DesignParameter['_AdditionalPolyOnNMOS3']['_XYCoordinates'] = [[[-self._DesignParameter['_NMOS4']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][1][0] - Mov2NMOS4XCoordinates, self._DesignParameter['_NMOS3']['_XYCoordinates'][0][1]],
																			  [-self._DesignParameter['_NMOS4']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][1][0] - Mov2NMOS4XCoordinates, self._DesignParameter['_VIANMOS3Poly2Met1']['_XYCoordinates'][0][1]],
																			  [self._DesignParameter['_NMOS3']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0] - Mov2NMOS3XCoordinates, self._DesignParameter['_VIANMOS3Poly2Met1']['_XYCoordinates'][0][1]]], #right side
																			  [[-self._DesignParameter['_NMOS4']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][-2][0] + Mov2NMOS4XCoordinates, self._DesignParameter['_NMOS3']['_XYCoordinates'][0][1]],
																			  [-self._DesignParameter['_NMOS4']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][-2][0] + Mov2NMOS4XCoordinates, self._DesignParameter['_VIANMOS3Poly2Met1']['_XYCoordinates'][0][1]],
																			  [self._DesignParameter['_NMOS3']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][-1][0] + Mov2NMOS3XCoordinates, self._DesignParameter['_VIANMOS3Poly2Met1']['_XYCoordinates'][0][1]]]] #left side

		self._DesignParameter['_AdditionalPOBoundaryOnNMOS3'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0],
																								 _Datatype=DesignParameters._LayerMapping['POLY'][1],
																								 _XWidth=int(self._DesignParameter['_AdditionalPolyOnNMOS3']['_XYCoordinates'][0][0][0] - self._DesignParameter['_AdditionalPolyOnNMOS3']['_XYCoordinates'][0][2][0]) + NMOS3inputs['_NMOSChannellength'] // 2 + NMOS4inputs['_NMOSChannellength'] // 2,
																								 _YWidth=self._DesignParameter['_VIANMOS3Poly2Met1']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'])
		# 여기부터
		self._DesignParameter['_AdditionalPOBoundaryOnNMOS3']['_XYCoordinates'] = [[self._DesignParameter['_AdditionalPolyOnNMOS3']['_XYCoordinates'][0][0][0] - self._DesignParameter['_AdditionalPOBoundaryOnNMOS3']['_XWidth'] // 2 + NMOS4inputs['_NMOSChannellength'] // 2, self._DesignParameter['_VIANMOS3Poly2Met1']['_XYCoordinates'][0][1]],
																				   [-(self._DesignParameter['_AdditionalPolyOnNMOS3']['_XYCoordinates'][0][0][0] - self._DesignParameter['_AdditionalPOBoundaryOnNMOS3']['_XWidth'] // 2 + NMOS4inputs['_NMOSChannellength'] // 2), self._DesignParameter['_VIANMOS3Poly2Met1']['_XYCoordinates'][0][1]]]

		# NMOS4
		self._DesignParameter['_AdditionalPolyOnNMOS4'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _XYCoordinates=[], _Width=NMOS4inputs['_NMOSChannellength'])


		self._DesignParameter['_AdditionalPolyOnNMOS4']['_XYCoordinates'] = [[[-self._DesignParameter['_NMOS4']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][0] - Mov2NMOS4XCoordinates, self._DesignParameter['_NMOS4']['_XYCoordinates'][0][1]],
																			  [-self._DesignParameter['_NMOS4']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][0] - Mov2NMOS4XCoordinates, self._DesignParameter['_VIANMOS4Poly2Met1']['_XYCoordinates'][0][1]],
																			  [self._DesignParameter['_NMOS4']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0] - Mov2NMOS4XCoordinates, self._DesignParameter['_VIANMOS4Poly2Met1']['_XYCoordinates'][0][1]],
																			  [self._DesignParameter['_NMOS4']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0] - Mov2NMOS4XCoordinates, self._DesignParameter['_NMOS4']['_XYCoordinates'][0][1]]], #right side
																			  [[-self._DesignParameter['_NMOS4']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][-1][0] + Mov2NMOS4XCoordinates, self._DesignParameter['_NMOS4']['_XYCoordinates'][0][1]],
																			  [-self._DesignParameter['_NMOS4']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][-1][0] + Mov2NMOS4XCoordinates, self._DesignParameter['_VIANMOS4Poly2Met1']['_XYCoordinates'][0][1]],
																			  [self._DesignParameter['_NMOS4']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][-1][0] + Mov2NMOS4XCoordinates, self._DesignParameter['_VIANMOS4Poly2Met1']['_XYCoordinates'][0][1]],
																			  [self._DesignParameter['_NMOS4']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][-1][0] + Mov2NMOS4XCoordinates, self._DesignParameter['_NMOS4']['_XYCoordinates'][0][1]]]] #left side

		self._DesignParameter['_AdditionalPOBoundaryOnNMOS4'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0],
																								 _Datatype=DesignParameters._LayerMapping['POLY'][1],
																								 _XWidth=int(self._DesignParameter['_AdditionalPolyOnNMOS4']['_XYCoordinates'][0][0][0] - self._DesignParameter['_AdditionalPolyOnNMOS4']['_XYCoordinates'][0][2][0]) + NMOS4inputs['_NMOSChannellength'],
																								 _YWidth=self._DesignParameter['_VIANMOS4Poly2Met1']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'],
																								 _XYCoordinates=[[(self._DesignParameter['_AdditionalPolyOnNMOS4']['_XYCoordinates'][0][0][0] + self._DesignParameter['_AdditionalPolyOnNMOS4']['_XYCoordinates'][0][2][0]) // 2, self._DesignParameter['_VIANMOS4Poly2Met1']['_XYCoordinates'][0][1]],
																												 [-(self._DesignParameter['_AdditionalPolyOnNMOS4']['_XYCoordinates'][0][0][0] + self._DesignParameter['_AdditionalPolyOnNMOS4']['_XYCoordinates'][0][2][0]) // 2, self._DesignParameter['_VIANMOS4Poly2Met1']['_XYCoordinates'][0][1]]])



		################################# NMOS2 Output Via Generation #################################
		_ViaNum = _ViaMet12Met2NumberOfCOY
		if _ViaNum == None:
			_ViaNum = int(self._DesignParameter['_NMOS2']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace))
		if _ViaNum < 2:
			_ViaNum = 2

		if _ViaMet12Met2NumberOfCOX == None:
			_ViaMet12Met2NumberOfCOX = 1

		_VIANMOS2OutputMet12Met2 = copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation)
		_VIANMOS2OutputMet12Met2['_ViaMet12Met2NumberOfCOX'] = _ViaMet12Met2NumberOfCOX
		_VIANMOS2OutputMet12Met2['_ViaMet12Met2NumberOfCOY'] = _ViaNum

		self._DesignParameter['_VIANMOS2OutputMet12Met2'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_DesignParameter=None, _Name='ViaMet12Met2OnNMOS2OutputIn{}'.format(_Name)))[0]
		self._DesignParameter['_VIANMOS2OutputMet12Met2']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(**_VIANMOS2OutputMet12Met2)
		del _ViaNum

		self._DesignParameter['_VIANMOS2OutputMet12Met2']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] = self._DesignParameter['_NMOS2']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']

		tmpNMOS2OutputRouting = []
		for i in range(len(self._DesignParameter['_NMOS2']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'])):
			tmpNMOS2OutputRouting.append([self._DesignParameter['_NMOS2']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][i][0] + self._DesignParameter['_NMOS2']['_XYCoordinates'][0][0], # leftside
										 self._DesignParameter['_NMOS2']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][i][1] + self._DesignParameter['_NMOS2']['_XYCoordinates'][0][1]])
			tmpNMOS2OutputRouting.append([-self._DesignParameter['_NMOS2']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][i][0] - self._DesignParameter['_NMOS2']['_XYCoordinates'][0][0], # right side
										  self._DesignParameter['_NMOS2']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][i][1] + self._DesignParameter['_NMOS2']['_XYCoordinates'][0][1]])

		self._DesignParameter['_VIANMOS2OutputMet12Met2']['_XYCoordinates'] = tmpNMOS2OutputRouting

		################################# NMOS3 Output Via Generation #################################
		_ViaNum = _ViaMet12Met2NumberOfCOY
		if _ViaNum == None:
			_ViaNum = int(self._DesignParameter['_NMOS3']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace))
		if _ViaNum < 2:
			_ViaNum = 2

		if _ViaMet12Met2NumberOfCOX == None:
			_ViaMet12Met2NumberOfCOX = 1

		_VIANMOS3OutputMet12Met2 = copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation)
		_VIANMOS3OutputMet12Met2['_ViaMet12Met2NumberOfCOX'] = _ViaMet12Met2NumberOfCOX
		_VIANMOS3OutputMet12Met2['_ViaMet12Met2NumberOfCOY'] = _ViaNum

		self._DesignParameter['_VIANMOS3OutputMet12Met2'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_DesignParameter=None, _Name='ViaMet12Met2OnNMOS3OutputIn{}'.format(_Name)))[0]
		self._DesignParameter['_VIANMOS3OutputMet12Met2']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(**_VIANMOS3OutputMet12Met2)
		del _ViaNum

		self._DesignParameter['_VIANMOS3OutputMet12Met2']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] = self._DesignParameter['_NMOS3']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']

		tmpNMOS3OutputRouting = []
		for i in range(len(self._DesignParameter['_NMOS3']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'])):
			tmpNMOS3OutputRouting.append([-self._DesignParameter['_NMOS3']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][i][0] + self._DesignParameter['_NMOS3']['_XYCoordinates'][0][0],
										 -self._DesignParameter['_NMOS3']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][i][1] + self._DesignParameter['_NMOS3']['_XYCoordinates'][0][1]])
			tmpNMOS3OutputRouting.append([self._DesignParameter['_NMOS3']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][i][0] - self._DesignParameter['_NMOS3']['_XYCoordinates'][0][0],
										  -self._DesignParameter['_NMOS3']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][i][1] + self._DesignParameter['_NMOS3']['_XYCoordinates'][0][1]])

		self._DesignParameter['_VIANMOS3OutputMet12Met2']['_XYCoordinates'] = tmpNMOS3OutputRouting


		################################# NCAP Via Generation #################################
		_ViaNum = _ViaMet12Met2NumberOfCOY
		if _ViaNum == None:
			_ViaNum = int(self._DesignParameter['_NCAP']['_DesignObj']._DesignParameter['Viapoly2Met1H']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace)) // 2
		if _ViaNum < 2:
			_ViaNum = 2

		if _ViaMet12Met2NumberOfCOX == None:
			_ViaMet12Met2NumberOfCOX = 1

		_VIANCAPMet12Met2 = copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation)
		_VIANCAPMet12Met2['_ViaMet12Met2NumberOfCOX'] = _ViaMet12Met2NumberOfCOX
		_VIANCAPMet12Met2['_ViaMet12Met2NumberOfCOY'] = _ViaNum

		self._DesignParameter['_VIANCAPMet12Met2'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_DesignParameter=None, _Name='ViaMet12Met2OnNCAPIn{}'.format(_Name)))[0]
		self._DesignParameter['_VIANCAPMet12Met2']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(**_VIANCAPMet12Met2)
		del _ViaNum

		self._DesignParameter['_VIANCAPMet12Met2']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] = self._DesignParameter['_NCAP']['_DesignObj']._DesignParameter['Viapoly2Met1H']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']

		tmpNCAPRouting = []
		tmpNCAPRouting.append([self._DesignParameter['_NCAP']['_DesignObj']._DesignParameter['Viapoly2Met1H']['_XYCoordinates'][0][1] + self._DesignParameter['_NCAP']['_XYCoordinates'][0][0],
								self._DesignParameter['_NCAP']['_DesignObj']._DesignParameter['Viapoly2Met1H']['_XYCoordinates'][0][0] + self._DesignParameter['_NCAP']['_XYCoordinates'][0][1]]) # left NCAP left side
		tmpNCAPRouting.append([-self._DesignParameter['_NCAP']['_DesignObj']._DesignParameter['Viapoly2Met1H']['_XYCoordinates'][0][1] + self._DesignParameter['_NCAP']['_XYCoordinates'][1][0],
								self._DesignParameter['_NCAP']['_DesignObj']._DesignParameter['Viapoly2Met1H']['_XYCoordinates'][0][0] + self._DesignParameter['_NCAP']['_XYCoordinates'][1][1]]) # right NCAP right side
		tmpNCAPRouting.append([self._DesignParameter['_NCAP']['_DesignObj']._DesignParameter['Viapoly2Met1H']['_XYCoordinates'][0][1] - self._DesignParameter['_NCAP']['_XYCoordinates'][0][0],
								self._DesignParameter['_NCAP']['_DesignObj']._DesignParameter['Viapoly2Met1H']['_XYCoordinates'][0][0] + self._DesignParameter['_NCAP']['_XYCoordinates'][0][1]]) # right NCAP left side
		tmpNCAPRouting.append([-self._DesignParameter['_NCAP']['_DesignObj']._DesignParameter['Viapoly2Met1H']['_XYCoordinates'][0][1] - self._DesignParameter['_NCAP']['_XYCoordinates'][1][0],
								self._DesignParameter['_NCAP']['_DesignObj']._DesignParameter['Viapoly2Met1H']['_XYCoordinates'][0][0] + self._DesignParameter['_NCAP']['_XYCoordinates'][1][1]]) # left NCAP right side

		self._DesignParameter['_VIANCAPMet12Met2']['_XYCoordinates'] = tmpNCAPRouting



		################################# Met2 Routing #################################
		self._DesignParameter['_Met2Routing'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0],
																				   _Datatype=DesignParameters._LayerMapping['METAL2'][1],
																				   _Width=_DRCObj._Metal1MinWidth)
		self._DesignParameter['_Met2Routing']['_XYCoordinates'] = [[[self._DesignParameter['_VIANMOS2OutputMet12Met2']['_XYCoordinates'][-1][0], self._DesignParameter['_NMOS2']['_XYCoordinates'][0][1]], #right side
																	[self._DesignParameter['_VIANMOS3OutputMet12Met2']['_XYCoordinates'][-1][0], self._DesignParameter['_NMOS3']['_XYCoordinates'][0][1]]],
																   [[-self._DesignParameter['_VIANMOS2OutputMet12Met2']['_XYCoordinates'][-1][0], self._DesignParameter['_NMOS2']['_XYCoordinates'][0][1]], #left side
																	[-self._DesignParameter['_VIANMOS3OutputMet12Met2']['_XYCoordinates'][-1][0], self._DesignParameter['_NMOS3']['_XYCoordinates'][0][1]]],
																   [[self._DesignParameter['_VIANMOS2OutputMet12Met2']['_XYCoordinates'][-2][0], self._DesignParameter['_NMOS2']['_XYCoordinates'][0][1]],
																	[self._DesignParameter['_VIANMOS2OutputMet12Met2']['_XYCoordinates'][-2][0], self._DesignParameter['_NCAP']['_XYCoordinates'][0][1] - self._DesignParameter['_VIANCAPMet12Met2']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] // 2]],
																   [[-self._DesignParameter['_VIANMOS2OutputMet12Met2']['_XYCoordinates'][-2][0], self._DesignParameter['_NMOS2']['_XYCoordinates'][0][1]],
																	[-self._DesignParameter['_VIANMOS2OutputMet12Met2']['_XYCoordinates'][-2][0], self._DesignParameter['_NCAP']['_XYCoordinates'][0][1] - self._DesignParameter['_VIANCAPMet12Met2']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] // 2]]]

		# resistor routing
		self._DesignParameter['_Met2RoutingOnRes'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0],
																			 _Datatype=DesignParameters._LayerMapping['METAL2'][1],
																			 _Width=self._DesignParameter['_VIANCAPMet12Met2']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'])

		self._DesignParameter['_Met2RoutingOnRes']['_XYCoordinates'] = [[self._DesignParameter['_VIANCAPMet12Met2']['_XYCoordinates'][0], self._DesignParameter['_VIANCAPMet12Met2']['_XYCoordinates'][3]],
																		[self._DesignParameter['_VIANCAPMet12Met2']['_XYCoordinates'][1], self._DesignParameter['_VIANCAPMet12Met2']['_XYCoordinates'][2]],
																		[self._DesignParameter['_VIANCAPMet12Met2']['_XYCoordinates'][3],[self._DesignParameter['_Met2Routing']['_XYCoordinates'][1][0][0],self._DesignParameter['_VIANCAPMet12Met2']['_XYCoordinates'][3][1]]],
																		[self._DesignParameter['_VIANCAPMet12Met2']['_XYCoordinates'][2],[self._DesignParameter['_Met2Routing']['_XYCoordinates'][0][0][0],self._DesignParameter['_VIANCAPMet12Met2']['_XYCoordinates'][2][1]]]]


		################################# Met3 Routing #################################
		self._DesignParameter['_Met3Routing'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0],
																			 _Datatype=DesignParameters._LayerMapping['METAL3'][1],
																			 _Width=_DRCObj._Metal1MinWidth)

		self._DesignParameter['_Met3Routing']['_XYCoordinates'] = [[self._DesignParameter['_VIANMOS2Met22Met3']['_XYCoordinates'][0], self._DesignParameter['_VIANMOS2Met22Met3']['_XYCoordinates'][1]],
																   [self._DesignParameter['_VIANMOS3Met22Met3']['_XYCoordinates'][0], [self._DesignParameter['_VIANMOS3Met22Met3']['_XYCoordinates'][0][0], self._DesignParameter['_PbodyContact1']['_XYCoordinates'][0][1]],
																	[self._DesignParameter['_VIANMOS3Met22Met3']['_XYCoordinates'][1][0], self._DesignParameter['_PbodyContact1']['_XYCoordinates'][0][1]], self._DesignParameter['_VIANMOS3Met22Met3']['_XYCoordinates'][1]]]





################################# DRC Check #################################
if __name__ == '__main__':
	# for i in range(0,100):
	# 	length=random.randrange(30,48,2)
	# 	_NMOSNumberofGate1 = random.randint(2,23)
	# 	_NMOSChannelWidth1 = random.randrange(300,500,2)
	# 	_NMOSChannellength1 = length
	# 	_NMOSNumberofGate2 = random.randit(6,40)n
	# 	_NMOSChannellength2 = length
	# 	_NMOSNumberofGate3 = random.randint(2,40)
	# 	_NMOSChannellength3 = length
	# 	_NMOSNumberofGate4 = random.randint(2,40)
	# 	_NMOSChannellength4 = length
		_NMOSNumberofGate1 = 14		# change
		_NMOSChannelWidth1 = 500	# change
		_NMOSChannellength1 = 30	# change
		_NMOSNumberofGate2 = 8	# change
		_NMOSChannellength2 = None	# change
		_NMOSNumberofGate3 = 4	# change
		_NMOSChannellength3 = None	# change
		_NMOSNumberofGate4 = 7	# change
		_NMOSChannellength4 = None	# change
		# _NMOSNumberofGate1 = 12		# change
		# _NMOSChannelWidth1 = 476	# change
		# _NMOSChannellength1 = 36	# change
		# _NMOSNumberofGate2 = 5	# change
		# _NMOSChannellength2 = 36	# change
		# _NMOSNumberofGate3 = 8	# change
		# _NMOSChannellength3 = 36	# change
		# _NMOSNumberofGate4 = 18	# change
		# _NMOSChannellength4 = 36	# change
		_NMOSDummy1 = False
		_GateSpacing1 = None
		_SDWidth1 = None
		_XVT = 'LVT'
		_PCCrit = None
		_NMOSChannelWidth2 = None
		_NMOSDummy2 = True
		_GateSpacing2 = None
		_SDWidth2 = None
		_NMOSChannelWidth3 = None
		_NMOSDummy3 = False
		_GateSpacing3 = None
		_SDWidth3 = None
		_NMOSChannelWidth4 = None
		_NMOSDummy4 = True
		_GateSpacing4 = None
		_SDWidth4 = None
		_ResWidth = 938
		_ResLength = 580
		_CONUMX = None
		_CONUMY = 1  # opppcres_b
		_XWidth = 838
		_YWidth = 1874
		_NumofGates = 1
		NumOfCOX = None
		NumOfCOY = None
		Guardring = False
		guardring_height = None
		guardring_width = None
		guardring_right = 3
		guardring_left = 3
		guardring_top = 3
		guardring_bot = 3
		_NumberOfPbodyCOX = None
		_NumberOfPbodyCOY = 3
		_Met1XWidth = None
		_Met1YWidth = None  # PbodyContact
		_ViaPoly2Met1NumberOfCOX = None
		_ViaPoly2Met1NumberOfCOY = None  # ViaPoly2Met1
		_ViaMet12Met2NumberOfCOX = None
		_ViaMet12Met2NumberOfCOY = None  # ViaMet12Met2
		_ViaMet22Met3NumberOfCOX = None
		_ViaMet22Met3NumberOfCOY = None
		_NumofOD = 1
		_ViaPoly2Met1NumberOfCOX_CAP = None
		_ViaPoly2Met1NumberOfCOY_CAP = 1

		print('_NMOSNumberofGate1=',_NMOSNumberofGate1)
		print('_NMOSChannelWidth1=',_NMOSChannelWidth1)
		print('_NMOSChannellength1=',_NMOSChannellength1)
		print('_NMOSNumberofGate2=',_NMOSNumberofGate2)
		print('_NMOSChannellength2=',_NMOSChannellength2)
		print('_NMOSNumberofGate3=',_NMOSNumberofGate3)
		print('_NMOSChannellength3=',_NMOSChannellength3)
		print('_NMOSNumberofGate4=',_NMOSNumberofGate4)
		print('_NMOSChannellength4=',_NMOSChannellength4)


		DesignParameters._Technology = 'SS28nm'
		TopObj = _SummerBottom(_DesignParameter=None, _Name='_SummerBottom')
		TopObj._CalculateSummerBottomDesignParameter(_NMOSNumberofGate1=_NMOSNumberofGate1, _NMOSChannelWidth1=_NMOSChannelWidth1, _NMOSChannellength1=_NMOSChannellength1,
														_NMOSDummy1=_NMOSDummy1, _GateSpacing1=_GateSpacing1, _SDWidth1=_SDWidth1, _XVT=_XVT, _PCCrit=_PCCrit,
														_NMOSNumberofGate2=_NMOSNumberofGate2, _NMOSChannelWidth2=_NMOSChannelWidth2, _NMOSChannellength2=_NMOSChannellength2,
														_NMOSDummy2=_NMOSDummy2, _GateSpacing2=_GateSpacing2, _SDWidth2=_SDWidth2,
														_NMOSNumberofGate3=_NMOSNumberofGate3, _NMOSChannelWidth3=_NMOSChannelWidth3, _NMOSChannellength3=_NMOSChannellength3,
														_NMOSDummy3=_NMOSDummy3, _GateSpacing3=_GateSpacing3, _SDWidth3=_SDWidth3,
														_NMOSNumberofGate4=_NMOSNumberofGate4, _NMOSChannelWidth4=_NMOSChannelWidth4, _NMOSChannellength4=_NMOSChannellength4,
														_NMOSDummy4=_NMOSDummy4, _GateSpacing4=_GateSpacing4, _SDWidth4=_SDWidth4,
														_ResWidth=_ResWidth, _ResLength=_ResLength, _CONUMX=_CONUMX,_CONUMY=_CONUMY,
														_XWidth=_XWidth, _YWidth=_YWidth, _NumofGates=_NumofGates, NumOfCOX=NumOfCOX, NumOfCOY=NumOfCOY,
														Guardring=Guardring, guardring_height=guardring_height, guardring_width=guardring_width,
														guardring_right=guardring_right, guardring_left=guardring_left, guardring_top=guardring_top, guardring_bot=guardring_bot,
														_NumberOfPbodyCOX=_NumberOfPbodyCOX, _NumberOfPbodyCOY=_NumberOfPbodyCOY, _Met1XWidth=_Met1XWidth, _Met1YWidth=_Met1YWidth,
														_ViaPoly2Met1NumberOfCOX=_ViaPoly2Met1NumberOfCOX, _ViaPoly2Met1NumberOfCOY=_ViaPoly2Met1NumberOfCOY,
														_ViaMet12Met2NumberOfCOX=_ViaMet12Met2NumberOfCOX, _ViaMet12Met2NumberOfCOY=_ViaMet12Met2NumberOfCOY,
														_ViaMet22Met3NumberOfCOX=_ViaMet22Met3NumberOfCOX, _ViaMet22Met3NumberOfCOY=_ViaMet22Met3NumberOfCOY,
													 	_NumofOD = _NumofOD, _ViaPoly2Met1NumberOfCOX_CAP = _ViaPoly2Met1NumberOfCOX_CAP, _ViaPoly2Met1NumberOfCOY_CAP = _ViaPoly2Met1NumberOfCOY_CAP)
		TopObj._UpdateDesignParameter2GDSStructure(_DesignParameterInDictionary=TopObj._DesignParameter)
		testStreamFile = open('./_SummerBottom.gds', 'wb')
		tmp = TopObj._CreateGDSStream(TopObj._DesignParameter['_GDSFile']['_GDSFile'])
		tmp.write_binary_gds_stream(testStreamFile)
		testStreamFile.close()

		print('#############################      Sending to FTP Server...      ##############################')

		import ftplib

		ftp = ftplib.FTP('141.223.29.62')
		ftp.login('smlim96', 'min753531')
		ftp.cwd('/mnt/sdc/smlim96/OPUS/ss28')
		myfile = open('_SummerBottom.gds', 'rb')
		ftp.storbinary('STOR _SummerBottom.gds', myfile)
		myfile.close()

		import DRCchecker
		a = DRCchecker.DRCchecker('smlim96','min753531','/mnt/sdc/smlim96/OPUS/ss28','/mnt/sdc/smlim96/OPUS/ss28/DRC/run','_SummerBottom','_SummerBottom',None)
		a.DRCchecker()

		print ("DRC Clean!!!")