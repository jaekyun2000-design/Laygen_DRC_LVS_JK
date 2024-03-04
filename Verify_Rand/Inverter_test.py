import StickDiagram
import DesignParameters
import copy
import DRC
import NMOSWithDummy_iksu
import PMOSWithDummy_iksu
import NbodyContact_iksu
import PbodyContact_iksu
import ViaPoly2Met1
import ViaMet12Met2
import ViaMet22Met3
import ViaMet32Met4
import math
import random

class _Inverter(StickDiagram._StickDiagram) :
	_ParametersForDesignCalculation = dict(_Finger = None, _ChannelWidth = None, _ChannelLength = None, _NPRatio = None,\
								  _VDD2VSSHeight = None, _Dummy = None, _NumSupplyCoX = None, _NumSupplyCoY = None, \
								  _SupplyMet1XWidth = None, _SupplyMet1YWidth = None, _NumViaPoly2Met1CoX = None, \
								  _NumViaPoly2Met1CoY = None, _NumViaPMOSMet12Met2CoX = None, \
								  _NumViaPMOSMet12Met2CoY = None, _NumViaNMOSMet12Met2CoX = None, _NumViaNMOSMet12Met2CoY = None, _XVT = None, _SupplyLine = None)


	def __init__(self, _DesignParameter = None, _Name = 'Inverter') :
		if _DesignParameter != None :
			self._DesignParameter = _DesignParameter

		else :
			self._DesignParameter = dict(_Name = self._NameDeclaration(_Name = _Name), _GDSFile = self._GDSObjDeclaration(_GDSFile=None))

	def _CalculateDesignParameter(self, _Finger = None, _ChannelWidth = None, _ChannelLength = None, _NPRatio = None,\
								  _VDD2VSSHeight = None, _Dummy = None, _NumSupplyCoX = None, _NumSupplyCoY = None, \
								  _SupplyMet1XWidth = None, _SupplyMet1YWidth = None, _NumViaPoly2Met1CoX = None, \
								  _NumViaPoly2Met1CoY = None, _NumViaPMOSMet12Met2CoX = None, _NumViaPMOSMet12Met2CoY = None, _NumViaNMOSMet12Met2CoX = None, _NumViaNMOSMet12Met2CoY = None, _XVT = None, _SupplyLine = None) :

		_DRCObj = DRC.DRC()
		_Name = self._DesignParameter['_Name']['_Name']
		MinSnapSpacing = _DRCObj._MinSnapSpacing

		#####################################_NMOS Generation######################################
		_NMOSinputs = copy.deepcopy(NMOSWithDummy_iksu._NMOS._ParametersForDesignCalculation)
		_NMOSinputs['_NMOSNumberofGate'] = _Finger
		_NMOSinputs['_NMOSChannelWidth'] = _ChannelWidth
		_NMOSinputs['_NMOSChannellength'] = _ChannelLength
		_NMOSinputs['_NMOSDummy'] = _Dummy
		_NMOSinputs['_XVT'] = _XVT

		self._DesignParameter['_NMOS'] = self._SrefElementDeclaration(_Reflect = [1,0,0], _Angle=0, _DesignObj = NMOSWithDummy_iksu._NMOS(_DesignParameter = None, \
																										   _Name = 'NMOSIn{}'.format(_Name)))[0]
		self._DesignParameter['_NMOS']['_DesignObj']._CalculateNMOSDesignParameter(**_NMOSinputs)


		#####################################_PMOS Generation######################################
		_PMOSinputs = copy.deepcopy(PMOSWithDummy_iksu._PMOS._ParametersForDesignCalculation)
		_PMOSinputs['_PMOSNumberofGate'] = _Finger
		_PMOSinputs['_PMOSChannelWidth'] = round(_ChannelWidth * _NPRatio)
		_PMOSinputs['_PMOSChannellength'] = _ChannelLength
		_PMOSinputs['_PMOSDummy'] = _Dummy
		_PMOSinputs['_XVT'] = _XVT

		self._DesignParameter['_PMOS'] = self._SrefElementDeclaration(_DesignObj = PMOSWithDummy_iksu._PMOS(_DesignParameter = None, \
																											_Name = 'PMOSIn{}'.format(_Name)))[0]
		self._DesignParameter['_PMOS']['_DesignObj']._CalculatePMOSDesignParameter(**_PMOSinputs)


		#####################################VDD Generation######################################
		_ContactNum = _NumSupplyCoX
		if _ContactNum == None:
			_ContactNum = int((self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_PPLayer']['_XWidth']) // (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2)) + 1
		if _ContactNum < 2 :
			_ContactNum = 2

		if _NumSupplyCoY is None :
			_NumSupplyCoY = 2

		_Nbodyinputs = copy.deepcopy(NbodyContact_iksu._NbodyContact._ParametersForDesignCalculation)
		_Nbodyinputs['_NumberOfNbodyCOX'] = _ContactNum
		_Nbodyinputs['_NumberOfNbodyCOY'] = _NumSupplyCoY
		_Nbodyinputs['_Met1XWidth'] = _SupplyMet1XWidth
		_Nbodyinputs['_Met1YWidth'] = _SupplyMet1YWidth

		self._DesignParameter['NbodyContact'] = self._SrefElementDeclaration(_DesignObj = NbodyContact_iksu._NbodyContact(_DesignParameter = None,\
																													 _Name = 'NbodyContactIn{}'.format(_Name)))[0]
		self._DesignParameter['NbodyContact']['_DesignObj']._CalculateNbodyContactDesignParameter(**_Nbodyinputs)


		#####################################VSS Generation######################################
		_Pbodyinputs = copy.deepcopy(PbodyContact_iksu._PbodyContact._ParametersForDesignCalculation)
		_Pbodyinputs['_NumberOfPbodyCOX'] = _ContactNum
		_Pbodyinputs['_NumberOfPbodyCOY'] = _NumSupplyCoY
		_Pbodyinputs['_Met1XWidth'] = _SupplyMet1XWidth
		_Pbodyinputs['_Met1YWidth'] = _SupplyMet1YWidth

		self._DesignParameter['PbodyContact'] = self._SrefElementDeclaration(_DesignObj = PbodyContact_iksu._PbodyContact(_DesignParameter = None, \
																													 _Name = 'PbodyContactIn{}'.format(_Name)))[0]
		self._DesignParameter['PbodyContact']['_DesignObj']._CalculatePbodyContactDesignParameter(**_Pbodyinputs)
		del _ContactNum

		#####################################VIA Generation for PMOS Output######################################
		_ViaNum = _NumViaPMOSMet12Met2CoY
		if _ViaNum == None :
			_ViaNum = int(self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace))
		if _ViaNum < 2 :
			_ViaNum = 2

		if _NumViaPMOSMet12Met2CoX == None :
			NumViaPMOSMet12Met2CoX = 1

		_VIAPMOSMet12 = copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation)
		_VIAPMOSMet12['_ViaMet12Met2NumberOfCOX'] = NumViaPMOSMet12Met2CoX
		_VIAPMOSMet12['_ViaMet12Met2NumberOfCOY'] = _ViaNum

		self._DesignParameter['_ViaMet12Met2OnPMOSOutput'] = self._SrefElementDeclaration(_DesignObj = ViaMet12Met2._ViaMet12Met2(_DesignParameter = None, \
																																  _Name = 'ViaMet12Met2OnPMOSOutputIn{}'.format(_Name)))[0]
		self._DesignParameter['_ViaMet12Met2OnPMOSOutput']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(**_VIAPMOSMet12)
		del _ViaNum


		#####################################VIA Generation for NMOS Output######################################
		_ViaNum = _NumViaNMOSMet12Met2CoY
		if _ViaNum == None:
			_ViaNum = int(self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace))
		if _ViaNum < 2 :
			_ViaNum = 2

		if _NumViaNMOSMet12Met2CoX == None:
			NumViaNMOSMet12Met2CoX = 1

		_VIANMOSMet12 = copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation)
		_VIANMOSMet12['_ViaMet12Met2NumberOfCOX'] = NumViaNMOSMet12Met2CoX
		_VIANMOSMet12['_ViaMet12Met2NumberOfCOY'] = _ViaNum

		self._DesignParameter['_ViaMet12Met2OnNMOSOutput'] = self._SrefElementDeclaration(_DesignObj = ViaMet12Met2._ViaMet12Met2(_DesignParameter = None, \
																																  _Name = 'ViaMet12Met2OnNMOSOutputIn{}'.format(_Name)))[0]
		self._DesignParameter['_ViaMet12Met2OnNMOSOutput']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(**_VIANMOSMet12)
		del _ViaNum


		self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] = self._DesignParameter['_ViaMet12Met2OnNMOSOutput']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
		self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] = self._DesignParameter['_ViaMet12Met2OnPMOSOutput']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']



		#####################################VIA Generation for PMOS Gate######################################
		_LenBtwPMOSGates = self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'][-1][0] - \
						   self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'][0][0]

		#####################################VIA Generation for NMOS Gate######################################
		_LenBtwNMOSGates = self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_XYCoordinateNMOSGateRouting']['_XYCoordinates'][-1][0] - \
						   self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_XYCoordinateNMOSGateRouting']['_XYCoordinates'][0][0]

		_LenBtwMOSGates = max(_LenBtwPMOSGates, _LenBtwNMOSGates)

		_VIAMOSPoly2Met1 = copy.deepcopy(ViaPoly2Met1._ViaPoly2Met1._ParametersForDesignCalculation)
		_tmpNumCOX = int(_LenBtwMOSGates // (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace))

		if _tmpNumCOX < 1:
			_tmpNumCOX = 1

		if _NumViaPoly2Met1CoX != None :
			_tmpNumCOX = _NumViaPoly2Met1CoX

		if _NumViaPoly2Met1CoY == None :
			_tmpNumCOY = 1
		else :
			_tmpNumCOY = _NumViaPoly2Met1CoY

		_VIAMOSPoly2Met1['_ViaPoly2Met1NumberOfCOX'] = _tmpNumCOX
		_VIAMOSPoly2Met1['_ViaPoly2Met1NumberOfCOY'] = _tmpNumCOY

		self._DesignParameter['_VIAMOSPoly2Met1'] = self._SrefElementDeclaration(_DesignObj = ViaPoly2Met1._ViaPoly2Met1(_DesignParameter = None, _Name = 'ViaPoly2Met1OnMOSGateIn{}'.format(_Name)))[0]
		self._DesignParameter['_VIAMOSPoly2Met1']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(**_VIAMOSPoly2Met1)
		del _tmpNumCOX
		del _tmpNumCOY

		#####################################Coordinates setting######################################
		_LengthSpaceBtwInputMet1 = 2 * _DRCObj._PolygateMinSpace2Co + _ChannelLength

		_LengthBtwPoly2Poly = 2 * _DRCObj._PolygateMinSpace2Co + _DRCObj._CoMinWidth
		_LengthPolyDummyEdge2OriginX = (int(_Finger // 2) + 1) * _LengthBtwPoly2Poly - _ChannelLength // 2 - (self._DesignParameter['_VIAMOSPoly2Met1']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']) // 2
		#_LengthPPolyDummyEdge2OriginX = (int(_Finger // 2) + 1) * _LengthBtwPoly2Poly - _ChannelLength // 2 - (self._DesignParameter['_VIAMOSPoly2Met1']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']) // 2



		self._DesignParameter['PbodyContact']['_XYCoordinates'] = [[0, 0]] ### PbodyContact Coordinate setting

		HeightofNMOS = self.FloorMinSnapSpacing(self._DesignParameter['PbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // 2 + max(self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'], self._DesignParameter['_ViaMet12Met2OnNMOSOutput']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']) // 2 + _DRCObj._Metal1DefaultSpace, MinSnapSpacing)

		self._DesignParameter['_NMOS']['_XYCoordinates'] = [[0, HeightofNMOS]]


		_VDD2VSSMinHeight = self.CeilMinSnapSpacing(self._DesignParameter['PbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // 2
		+ max(self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'], self._DesignParameter['_ViaMet12Met2OnNMOSOutput']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'])
		+ self._DesignParameter['NbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // 2
		+ max(self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'], self._DesignParameter['_ViaMet12Met2OnPMOSOutput']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']) +\
		2 * _DRCObj._Metal1DefaultSpace + self._DesignParameter['_VIAMOSPoly2Met1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] + 2 * _DRCObj._Metal1DefaultSpace + _DRCObj._Metal1MinSpace, MinSnapSpacing)


		if _VDD2VSSHeight == None :
			_VDD2VSSHeight = _VDD2VSSMinHeight

		else :
			if _VDD2VSSHeight < _VDD2VSSMinHeight :
				print("ERROR! VDD2VSSMinHeight =", _VDD2VSSMinHeight)
				raise NotImplementedError

		self._DesignParameter['_INVVDD2VSSMinHeight']= {'_Ignore': _VDD2VSSHeight, '_DesignParametertype': None, '_ElementName': None, '_XYCoordinates': None, '_Width': None, '_Layer': None, '_Datatype': None}

		self._DesignParameter['NbodyContact']['_XYCoordinates'] = [[0, _VDD2VSSHeight]]

		HeightofPMOS = self.CeilMinSnapSpacing(_VDD2VSSHeight - self._DesignParameter['NbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // 2 - max(self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'], self._DesignParameter['_ViaMet12Met2OnPMOSOutput']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']) // 2 - _DRCObj._Metal1DefaultSpace, MinSnapSpacing)

		self._DesignParameter['_PMOS']['_XYCoordinates'] = [[0, HeightofPMOS]] ### PODummyLayer -> POLayer

		tmpNMOSOutputRouting = []
		tmpPMOSOutputRouting = []

		for i in range(0, len(self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'])) :
			tmpPMOSOutputRouting.append([self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][i][0] + self._DesignParameter['_PMOS']['_XYCoordinates'][0][0], \
										 self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][i][1] + self._DesignParameter['_PMOS']['_XYCoordinates'][0][1]])
			tmpNMOSOutputRouting.append([self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][i][0] + self._DesignParameter['_NMOS']['_XYCoordinates'][0][0], \
										 self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][i][1] + self._DesignParameter['_NMOS']['_XYCoordinates'][0][1]])

		self._DesignParameter['_ViaMet12Met2OnPMOSOutput']['_XYCoordinates'] = tmpPMOSOutputRouting
		self._DesignParameter['_ViaMet12Met2OnNMOSOutput']['_XYCoordinates'] = tmpNMOSOutputRouting

		YCoordinateofNPoly = self._DesignParameter['_NMOS']['_XYCoordinates'][0][1] + max(self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'], self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_PODummyLayer']['_YWidth']) // 2
		YCoordinateofPPoly = self._DesignParameter['_PMOS']['_XYCoordinates'][0][1] - max(self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'], self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_PODummyLayer']['_YWidth']) // 2

		self._DesignParameter['_VIAMOSPoly2Met1']['_XYCoordinates'] = [[self._DesignParameter['_NMOS']['_XYCoordinates'][0][0], self.CeilMinSnapSpacing((YCoordinateofNPoly + YCoordinateofPPoly) // 2, MinSnapSpacing)]]

		###### 추가 230801
		self._DesignParameter['_AdditionalGateM1'] =  self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0],_Datatype=DesignParameters._LayerMapping['METAL1'][1], _XYCoordinates=[],_XWidth=None, _YWidth=None, _ElementName=None,)
		self._DesignParameter['_AdditionalGateM1']['_XWidth'] = self.CeilMinSnapSpacing(self._DesignParameter['_VIAMOSPoly2Met1']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] + 1, 2 * MinSnapSpacing)
		self._DesignParameter['_AdditionalGateM1']['_YWidth'] = self._DesignParameter['_VIAMOSPoly2Met1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']
		self._DesignParameter['_AdditionalGateM1']['_XYCoordinates'] = self._DesignParameter['_VIAMOSPoly2Met1']['_XYCoordinates']


		 #####################################VSS&VDD Met1 Routing######################################
		tmpNMOSSupplyRouting = []
		tmpPMOSSupplyRouting = []
		for i in range(0, len(self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'])) :
			tmpNMOSSupplyRouting.append([[self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][i][0] + self._DesignParameter['_NMOS']['_XYCoordinates'][0][0], self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][i][1] + self._DesignParameter['_NMOS']['_XYCoordinates'][0][1]], \
										 [self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][i][0] + self._DesignParameter['_NMOS']['_XYCoordinates'][0][0], self._DesignParameter['PbodyContact']['_XYCoordinates'][0][1]]])
			tmpPMOSSupplyRouting.append([[self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSSupplyRouting']['_XYCoordinates'][i][0] + self._DesignParameter['_PMOS']['_XYCoordinates'][0][0], self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSSupplyRouting']['_XYCoordinates'][i][1] + self._DesignParameter['_PMOS']['_XYCoordinates'][0][1]], \
										 [self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSSupplyRouting']['_XYCoordinates'][i][0] + self._DesignParameter['_PMOS']['_XYCoordinates'][0][0], self._DesignParameter['NbodyContact']['_XYCoordinates'][0][1]]])

		self._DesignParameter['_NMOSSupplyRouting'] = self._PathElementDeclaration(_Layer = DesignParameters._LayerMapping['METAL1'][0], _Datatype = DesignParameters._LayerMapping['METAL1'][1], _XYCoordinates = [], _Width = None)
		self._DesignParameter['_NMOSSupplyRouting']['_Width'] = self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
		self._DesignParameter['_NMOSSupplyRouting']['_XYCoordinates'] = tmpNMOSSupplyRouting

		self._DesignParameter['_PMOSSupplyRouting'] = self._PathElementDeclaration(_Layer = DesignParameters._LayerMapping['METAL1'][0], _Datatype = DesignParameters._LayerMapping['METAL1'][1], _XYCoordinates = [], _Width = None)
		self._DesignParameter['_PMOSSupplyRouting']['_Width'] = self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
		self._DesignParameter['_PMOSSupplyRouting']['_XYCoordinates'] = tmpPMOSSupplyRouting


		#####################################Input Met1 Routing######################################
		tmpInputRouting = []
		self._DesignParameter['_InputRouting'] = self._PathElementDeclaration(_Layer = DesignParameters._LayerMapping['METAL1'][0], _Datatype = DesignParameters._LayerMapping['METAL1'][1], _XYCoordinates = [], _Width = None)
		self._DesignParameter['_InputRouting']['_Width'] = _DRCObj._Metal1MinWidth

		if _Finger % 2 == 0 :
			for i in range(1, len(self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSSupplyRouting']['_XYCoordinates']) - 1) :
				tmpInputRouting.append([[self._DesignParameter['_PMOS']['_XYCoordinates'][0][0] + self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSSupplyRouting']['_XYCoordinates'][i][0], self._DesignParameter['_VIAMOSPoly2Met1']['_XYCoordinates'][0][1]], \
										  [self._DesignParameter['_NMOS']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][i][0], self._DesignParameter['_VIAMOSPoly2Met1']['_XYCoordinates'][0][1]]])

		elif _Finger % 2 != 0 :
			for i in range(1, len(self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSSupplyRouting']['_XYCoordinates'])) :
				tmpInputRouting.append([[self._DesignParameter['_PMOS']['_XYCoordinates'][0][0] + self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSSupplyRouting']['_XYCoordinates'][i][0], self._DesignParameter['_VIAMOSPoly2Met1']['_XYCoordinates'][0][1]], \
										  [self._DesignParameter['_NMOS']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][i][0], self._DesignParameter['_VIAMOSPoly2Met1']['_XYCoordinates'][0][1]]])

		if _Finger == 1 :
			tmpInputRouting =  [[[0, self._DesignParameter['_VIAMOSPoly2Met1']['_XYCoordinates'][0][1]], [0, self._DesignParameter['_VIAMOSPoly2Met1']['_XYCoordinates'][0][1]]]]

		if _Finger == 2 :
			tmpInputRouting = [[[0, self._DesignParameter['_VIAMOSPoly2Met1']['_XYCoordinates'][0][1]], [0, self._DesignParameter['_VIAMOSPoly2Met1']['_XYCoordinates'][0][1]]]]

		if _Finger == 3 :
			tmpInputRouting = [[[0, self._DesignParameter['_VIAMOSPoly2Met1']['_XYCoordinates'][0][1]], [0, self._DesignParameter['_VIAMOSPoly2Met1']['_XYCoordinates'][0][1]]]]


		self._DesignParameter['_InputRouting']['_XYCoordinates'] = tmpInputRouting


		#####################################Output Met2 Boundary&Routing######################################
		tmpOutputRouting = []

		self._DesignParameter['_OutputRouting'] = self._PathElementDeclaration(_Layer = DesignParameters._LayerMapping['METAL2'][0], _Datatype = DesignParameters._LayerMapping['METAL2'][1],  _XYCoordinates = [], _Width = None)
		self._DesignParameter['_OutputRouting']['_Width'] = _DRCObj._MetalxMinWidth

		if _Finger == 2 :
			tmpOutputRouting.append([[self._DesignParameter['_PMOS']['_XYCoordinates'][0][0] + self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][-1][0], self._DesignParameter['_PMOS']['_XYCoordinates'][0][1] + self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][-1][1]], \
									 [self._DesignParameter['_NMOS']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][-1][0], self._DesignParameter['_NMOS']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][-1][1]]])

		elif _Finger == 3 :
			tmpOutputRouting.append([[self._DesignParameter['_PMOS']['_XYCoordinates'][0][0] + self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][-1][0], self._DesignParameter['_PMOS']['_XYCoordinates'][0][1] + self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][-1][1]], \
									 [self._DesignParameter['_NMOS']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][-1][0], self._DesignParameter['_NMOS']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][-1][1]]])

		elif _Finger == 4 :
			tmpOutputRouting.append([[self._DesignParameter['_PMOS']['_XYCoordinates'][0][0] + self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][-1][0], self._DesignParameter['_PMOS']['_XYCoordinates'][0][1] + self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][-1][1]], \
									 [self._DesignParameter['_NMOS']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][-1][0], self._DesignParameter['_NMOS']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][-1][1]]])

		else :
			for i in range(0, int((len(self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates']) + 1) // 2)) :
				tmpOutputRouting.append([[self._DesignParameter['_PMOS']['_XYCoordinates'][0][0] + self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][2*i][0], self._DesignParameter['_PMOS']['_XYCoordinates'][0][1] + self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][2*i][1]], \
										 [self._DesignParameter['_NMOS']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][2*i][0], self._DesignParameter['_NMOS']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][2*i][1]]])


		self._DesignParameter['_OutputRouting']['_XYCoordinates'] = tmpOutputRouting

		self._DesignParameter['_Met2OnOutput'] = self._PathElementDeclaration(_Layer = DesignParameters._LayerMapping['METAL2'][0], _Datatype = DesignParameters._LayerMapping['METAL2'][1], _XYCoordinates = [], _Width = None)
		self._DesignParameter['_Met2OnOutput']['_Width'] = _DRCObj._MetalxMinWidth

		if _Finger != 2 :
			self._DesignParameter['_Met2OnOutput']['_XYCoordinates'] = [[[self._DesignParameter['_PMOS']['_XYCoordinates'][0][0] + self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][-1][0], \
																		  self._DesignParameter['_PMOS']['_XYCoordinates'][0][1] + self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][-1][1]], \
																		 [self._DesignParameter['_PMOS']['_XYCoordinates'][0][0] + self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][0][0], \
																		  self._DesignParameter['_PMOS']['_XYCoordinates'][0][1] + self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][0][1]]], \
																		 [[self._DesignParameter['_NMOS']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][-1][0], \
																		   self._DesignParameter['_NMOS']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][-1][1]], \
																		  [self._DesignParameter['_NMOS']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][0][0], \
																		   self._DesignParameter['_NMOS']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][0][1]]]]

		elif _Finger == 2 :
			self._DesignParameter['_Met2OnOutput']['_XYCoordinates'] = [[[self._DesignParameter['_PMOS']['_XYCoordinates'][0][0] + self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][0][0], \
																		  self._DesignParameter['_PMOS']['_XYCoordinates'][0][1] + self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][0][1]], \
																		 [self._DesignParameter['_PMOS']['_XYCoordinates'][0][0] + self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][-1][0]+self.CeilMinSnapSpacing(self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']/2, MinSnapSpacing), \
																		  self._DesignParameter['_PMOS']['_XYCoordinates'][0][1] + self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][0][1]]], \
																		 [[self._DesignParameter['_NMOS']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][0][0], \
																		   self._DesignParameter['_NMOS']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][0][1]], \
																		  [self._DesignParameter['_NMOS']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][-1][0]+self.CeilMinSnapSpacing(self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']/2, MinSnapSpacing), \
																		   self._DesignParameter['_NMOS']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][0][1]]]]


		if _Finger > 4 :
			_ViaMet12Met2forInput = copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation)
			_ViaMet12Met2forInput['_ViaMet12Met2NumberOfCOX'] = int((self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][2][0] - self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][0][0] - self._DesignParameter['_Met2OnOutput']['_Width'] - 2 * _DRCObj._MetalxMinEnclosureCO2 - 2 * _DRCObj._MetalxMinSpace) / (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace))
			_ViaMet12Met2forInput['_ViaMet12Met2NumberOfCOY'] = 1
			self._DesignParameter['_ViaMet12Met2forInput'] = self._SrefElementDeclaration(_DesignObj = ViaMet12Met2._ViaMet12Met2(_DesignParameter = None, _Name = 'ViaMet12Met2forInputIn{}'.format(_Name)))[0]
			self._DesignParameter['_ViaMet12Met2forInput']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureY(**_ViaMet12Met2forInput)
			tmp = []
			for i in range(0, (len(self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates']) + 1) // 2 - 1) :
				tmp.append([self._DesignParameter['_PMOS']['_XYCoordinates'][0][0] + self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][2*i+1][0], self._DesignParameter['_VIAMOSPoly2Met1']['_XYCoordinates'][0][1]])
			self._DesignParameter['_ViaMet12Met2forInput']['_XYCoordinates'] = tmp
			del tmp

			_ViaMet22Met3forInput = copy.deepcopy(ViaMet22Met3._ViaMet22Met3._ParametersForDesignCalculation)
			_ViaMet22Met3forInput['_ViaMet22Met3NumberOfCOX'] = int((self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][2][0] - self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][0][0] - self._DesignParameter['_Met2OnOutput']['_Width'] - 2 * _DRCObj._MetalxMinEnclosureCO2 - 2 * _DRCObj._MetalxMinSpace) / (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace))
			_ViaMet22Met3forInput['_ViaMet22Met3NumberOfCOY'] = 1
			self._DesignParameter['_ViaMet22Met3forInput'] = self._SrefElementDeclaration(_DesignObj = ViaMet22Met3._ViaMet22Met3(_DesignParameter = None, _Name = 'ViaMet22Met3forInputIn{}'.format(_Name)))[0]
			self._DesignParameter['_ViaMet22Met3forInput']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureY(**_ViaMet22Met3forInput)
			tmp = []
			for i in range(0, (len(self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates']) + 1) // 2 - 1) :
				tmp.append([self._DesignParameter['_PMOS']['_XYCoordinates'][0][0] + self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][2*i+1][0], self._DesignParameter['_VIAMOSPoly2Met1']['_XYCoordinates'][0][1]])
			self._DesignParameter['_ViaMet22Met3forInput']['_XYCoordinates'] = tmp
			del tmp

			self._DesignParameter['_Met3InRouting'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0], _Datatype=DesignParameters._LayerMapping['METAL3'][1], _XYCoordinates=[],_Width=None)
			self._DesignParameter['_Met3InRouting']['_Width'] = self.CeilMinSnapSpacing(self._DesignParameter['_ViaMet22Met3forInput']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth'], 2 * MinSnapSpacing)
			self._DesignParameter['_Met3InRouting']['_XYCoordinates'] = [[self._DesignParameter['_ViaMet22Met3forInput']['_XYCoordinates'][0], self._DesignParameter['_ViaMet22Met3forInput']['_XYCoordinates'][-1]]]



		#####################################Additional Poly Routing######################################
		self._DesignParameter['_AdditionalPolyOnPMOS'] = self._PathElementDeclaration(_Layer = DesignParameters._LayerMapping['POLY'][0], _Datatype = DesignParameters._LayerMapping['POLY'][1], \
																					  _XYCoordinates = [], _Width = None)
		self._DesignParameter['_AdditionalPolyOnNMOS'] = self._PathElementDeclaration(_Layer = DesignParameters._LayerMapping['POLY'][0], _Datatype = DesignParameters._LayerMapping['POLY'][1], \
																					  _XYCoordinates=[], _Width=None)
		# self._DesignParameter['_AdditionalPolyOnPMOS']['_Width'] = _DRCObj._PolygateMinWidth
		# self._DesignParameter['_AdditionalPolyOnNMOS']['_Width'] = _DRCObj._PolygateMinWidth
		self._DesignParameter['_AdditionalPolyOnPMOS']['_Width'] = _ChannelLength
		self._DesignParameter['_AdditionalPolyOnNMOS']['_Width'] = _ChannelLength


		tmpAdditionalPolyOnPMOS = []
		tmpAdditionalPolyOnNMOS = []

		for i in range(0, len(self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'])) :
			tmpAdditionalPolyOnPMOS.append([[self._DesignParameter['_PMOS']['_XYCoordinates'][0][0] + self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'][i][0], self._DesignParameter['_PMOS']['_XYCoordinates'][0][1] + self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'][i][1]], \
											  [self._DesignParameter['_PMOS']['_XYCoordinates'][0][0] + self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'][i][0], self._DesignParameter['_VIAMOSPoly2Met1']['_XYCoordinates'][0][1] - self.CeilMinSnapSpacing(self._DesignParameter['_VIAMOSPoly2Met1']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] // 2, _DRCObj._MinSnapSpacing)]])
			tmpAdditionalPolyOnNMOS.append([[self._DesignParameter['_NMOS']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_XYCoordinateNMOSGateRouting']['_XYCoordinates'][i][0], self._DesignParameter['_NMOS']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_XYCoordinateNMOSGateRouting']['_XYCoordinates'][i][1]], \
											  [self._DesignParameter['_NMOS']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_XYCoordinateNMOSGateRouting']['_XYCoordinates'][i][0], self._DesignParameter['_VIAMOSPoly2Met1']['_XYCoordinates'][0][1] + self.CeilMinSnapSpacing(self._DesignParameter['_VIAMOSPoly2Met1']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] // 2, _DRCObj._MinSnapSpacing)]])

		self._DesignParameter['_AdditionalPolyOnPMOS']['_XYCoordinates'] = tmpAdditionalPolyOnPMOS
		self._DesignParameter['_AdditionalPolyOnNMOS']['_XYCoordinates'] = tmpAdditionalPolyOnNMOS

		del tmpAdditionalPolyOnPMOS
		del tmpAdditionalPolyOnNMOS

		self._DesignParameter['_AdditionalPolyOnGate'] =  self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0],_Datatype=DesignParameters._LayerMapping['POLY'][1], _XYCoordinates=[],_XWidth=None, _YWidth=None, _ElementName=None,)
		self._DesignParameter['_AdditionalPolyOnGate']['_XWidth'] = self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'][-1][0] - self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'][0][0]
		self._DesignParameter['_AdditionalPolyOnGate']['_YWidth'] = self._DesignParameter['_VIAMOSPoly2Met1']['_DesignObj']._DesignParameter['_POLayer']['_YWidth']
		self._DesignParameter['_AdditionalPolyOnGate']['_XYCoordinates'] = self._DesignParameter['_VIAMOSPoly2Met1']['_XYCoordinates'] + self._DesignParameter['_VIAMOSPoly2Met1']['_XYCoordinates']

		if self.getXWidth('_NMOS','_Met1Layer') * self.getYWidth('_NMOS','_Met1Layer') < _DRCObj._Metal1MinArea :
			self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] = _DRCObj._Metal1MinArea // self.getXWidth('_NMOS','_Met1Layer') + 2*MinSnapSpacing

		if self.getXWidth('_PMOS','_Met1Layer') * self.getYWidth('_PMOS','_Met1Layer') < _DRCObj._Metal1MinArea :
			self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] = _DRCObj._Metal1MinArea // self.getXWidth('_PMOS','_Met1Layer') + 2*MinSnapSpacing


		#####################################NWELL&PP/NP Layer Generation & Coordinates#######################################
		self._DesignParameter['_NWLayer'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['NWELL'][0], _Datatype=DesignParameters._LayerMapping['NWELL'][1], _XYCoordinates=[], _Width=None)
		#if DesignParameters._Technology == '028nm' : self._DesignParameter['_NWLayer']['_Width'] = self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_SLVTLayer']['_XWidth'] + 2 * _DRCObj._NwMinSpacetoSLVT
		self._DesignParameter['_NWLayer']['_Width'] = self._DesignParameter['NbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] + 2 * _DRCObj._NwMinEnclosurePactive
		self._DesignParameter['_NWLayer']['_XYCoordinates'] = [[[self._DesignParameter['_PMOS']['_XYCoordinates'][0][0], self.CeilMinSnapSpacing(self._DesignParameter['NbodyContact']['_XYCoordinates'][0][1] + self._DesignParameter['NbodyContact']['_DesignObj']._DesignParameter['_NPLayer']['_YWidth'] // 2 + _DRCObj._NwMinEnclosurePactive2, MinSnapSpacing)], [self._DesignParameter['_PMOS']['_XYCoordinates'][0][0], self._DesignParameter['_PMOS']['_XYCoordinates'][0][1] - self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_PPLayer']['_YWidth'] // 2]]]

		if DesignParameters._Technology != '028nm' :
			self._DesignParameter['_PPLayer'] = self._PathElementDeclaration(_Layer = DesignParameters._LayerMapping['PIMP'][0],_Datatype = DesignParameters._LayerMapping['PIMP'][1], _XYCoordinates = [], _Width=None)
			self._DesignParameter['_PPLayer']['_Width'] = self._DesignParameter['_PMOS']['_DesignObj']._DesignParameter['_PPLayer']['_XWidth']
			self._DesignParameter['_PPLayer']['_XYCoordinates'] = [[self._DesignParameter['_PMOS']['_XYCoordinates'][0], [self._DesignParameter['_VIAMOSPoly2Met1']['_XYCoordinates'][0][0],
																															self.CeilMinSnapSpacing(self._DesignParameter['_VIAMOSPoly2Met1']['_XYCoordinates'][0][1], 2*MinSnapSpacing)]]]

			self._DesignParameter['_NPLayer'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['NIMP'][0], _Datatype=DesignParameters._LayerMapping['NIMP'][1], _XYCoordinates=[], _Width=None)
			self._DesignParameter['_NPLayer']['_Width'] = self._DesignParameter['_NMOS']['_DesignObj']._DesignParameter['_NPLayer']['_XWidth']
			self._DesignParameter['_NPLayer']['_XYCoordinates'] = [[self._DesignParameter['_NMOS']['_XYCoordinates'][0], [self._DesignParameter['_VIAMOSPoly2Met1']['_XYCoordinates'][0][0],
																															self.CeilMinSnapSpacing(self._DesignParameter['_VIAMOSPoly2Met1']['_XYCoordinates'][0][1], 2*MinSnapSpacing)]]]


			_SupplyRailYwidth = _DRCObj._CoMinWidth * _NumSupplyCoY + _DRCObj._CoMinSpace * _NumSupplyCoY
			self._DesignParameter['_AdditionalNWLayer'] = self._PathElementDeclaration(_Layer = DesignParameters._LayerMapping['NWELL'][0],_Datatype = DesignParameters._LayerMapping['NWELL'][1], _XYCoordinates = [], _Width=None)
			self._DesignParameter['_AdditionalNWLayer']['_Width'] = self._DesignParameter['NbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] + 2 * _DRCObj._NwMinEnclosurePactive2

			self._DesignParameter['_AdditionalNWLayer']['_XYCoordinates'] = [[[self._DesignParameter['_PMOS']['_XYCoordinates'][0][0], self.CeilMinSnapSpacing(self._DesignParameter['NbodyContact']['_XYCoordinates'][0][1] + self._DesignParameter['NbodyContact']['_DesignObj']._DesignParameter['_NPLayer']['_YWidth'] // 2 + _DRCObj._NwMinEnclosurePactive2, MinSnapSpacing)], \
																	[self._DesignParameter['_PMOS']['_XYCoordinates'][0][0], self.FloorMinSnapSpacing(self._DesignParameter['_PPLayer']['_XYCoordinates'][0][1][1], MinSnapSpacing)]]]




		#####################################Pin Generation & Coordinates#######################################
		self._DesignParameter['_VDDpin'] = self._TextElementDeclaration(_Layer = DesignParameters._LayerMapping['METAL1PIN'][0], _Datatype = DesignParameters._LayerMapping['METAL1PIN'][1], _Presentation = [0,1,2], _Reflect = [0,0,0], _XYCoordinates=[[0,0]], _Mag = 0.05, _Angle = 0, _TEXT = 'VDD')
		self._DesignParameter['_VSSpin'] = self._TextElementDeclaration(_Layer = DesignParameters._LayerMapping['METAL1PIN'][0], _Datatype = DesignParameters._LayerMapping['METAL1PIN'][1], _Presentation = [0,1,2], _Reflect = [0,0,0], _XYCoordinates=[[0,0]], _Mag = 0.05, _Angle = 0, _TEXT = 'VSS')
		self._DesignParameter['_Inputpin'] = self._TextElementDeclaration(_Layer = DesignParameters._LayerMapping['METAL1PIN'][0], _Datatype = DesignParameters._LayerMapping['METAL1PIN'][1], _Presentation = [0,1,2], _Reflect = [0,0,0], _XYCoordinates=[[0,0]], _Mag = 0.05, _Angle = 0, _TEXT = 'VIN')
		self._DesignParameter['_Outputpin'] = self._TextElementDeclaration(_Layer = DesignParameters._LayerMapping['METAL2PIN'][0], _Datatype = DesignParameters._LayerMapping['METAL2PIN'][1], _Presentation = [0,1,2], _Reflect = [0,0,0], _XYCoordinates=[[0,0]], _Mag = 0.05, _Angle = 0, _TEXT = 'VOUT')

		self._DesignParameter['_VDDpin']['_XYCoordinates'] = [[0, _VDD2VSSHeight]]
		self._DesignParameter['_VSSpin']['_XYCoordinates'] = [[0,0]]
		self._DesignParameter['_Inputpin']['_XYCoordinates'] = [[self.CeilMinSnapSpacing(round((self._DesignParameter['_InputRouting']['_XYCoordinates'][0][0][0] + \
					self._DesignParameter['_InputRouting']['_XYCoordinates'][0][1][0]) / 2), MinSnapSpacing), self.CeilMinSnapSpacing(round((self._DesignParameter['_InputRouting']['_XYCoordinates'][0][0][1] + \
					self._DesignParameter['_InputRouting']['_XYCoordinates'][0][1][1]) / 2), MinSnapSpacing)]]
		self._DesignParameter['_Outputpin']['_XYCoordinates'] = [[self.CeilMinSnapSpacing(round((self._DesignParameter['_OutputRouting']['_XYCoordinates'][0][0][0] + \
					self._DesignParameter['_OutputRouting']['_XYCoordinates'][0][1][0]) / 2), MinSnapSpacing), self.CeilMinSnapSpacing(round((self._DesignParameter['_OutputRouting']['_XYCoordinates'][0][0][1] + \
					self._DesignParameter['_OutputRouting']['_XYCoordinates'][0][1][1]) / 2), MinSnapSpacing)]]



		#####################################SupplyLine Generation & Coordinates#######################################
		if _SupplyLine == True :
			self._DesignParameter['_Met2LayerOnSupply'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _XYCoordinates=[], _XWidth=400, _YWidth=400)
			self._DesignParameter['_Met3LayerOnSupply'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0], _Datatype=DesignParameters._LayerMapping['METAL3'][1], _XYCoordinates=[], _XWidth=400, _YWidth=400)

			self._DesignParameter['_Met2LayerOnSupply']['_XWidth'] = self._DesignParameter['NbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
			self._DesignParameter['_Met2LayerOnSupply']['_YWidth'] = self._DesignParameter['NbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']
			self._DesignParameter['_Met3LayerOnSupply']['_XWidth'] = self._DesignParameter['NbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']
			self._DesignParameter['_Met3LayerOnSupply']['_YWidth'] = self._DesignParameter['NbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']

			self._DesignParameter['_Met2LayerOnSupply']['_XYCoordinates'] = self._DesignParameter['NbodyContact']['_XYCoordinates'] + self._DesignParameter['PbodyContact']['_XYCoordinates']
			self._DesignParameter['_Met3LayerOnSupply']['_XYCoordinates'] = self._DesignParameter['NbodyContact']['_XYCoordinates'] + self._DesignParameter['PbodyContact']['_XYCoordinates']

			_ViaNumSupplyX = int((self._DesignParameter['NbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] - 2 * _DRCObj._VIAxMinEnclosureByMetxTwoOppositeSide - _DRCObj._VIAxMinWidth) / (_DRCObj._VIAxMinSpace2 + _DRCObj._VIAxMinWidth)) + 1
			_ViaNumSupplyY = int((self._DesignParameter['NbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] - _DRCObj._VIAxMinWidth) / (_DRCObj._VIAxMinSpace2 + _DRCObj._VIAxMinWidth)) + 1


			if _ViaNumSupplyX <= 1:
				_ViaNumSupplyX = 1
				_ViaNumSupplyY = int((self._DesignParameter['NbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] - _DRCObj._VIAxMinWidth) / (_DRCObj._VIAxMinSpace + _DRCObj._VIAxMinWidth)) + 1
			if _ViaNumSupplyY <= 1:
				_ViaNumSupplyY = 1
				_ViaNumSupplyX = int((self._DesignParameter['NbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] - 2 * _DRCObj._VIAxMinEnclosureByMetxTwoOppositeSide - _DRCObj._VIAxMinWidth) / (_DRCObj._VIAxMinSpace + _DRCObj._VIAxMinWidth)) + 1


			_ViaVDDMet12Met2 = copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation)
			_ViaVDDMet12Met2['_ViaMet12Met2NumberOfCOX'] = _ViaNumSupplyX
			_ViaVDDMet12Met2['_ViaMet12Met2NumberOfCOY'] = _ViaNumSupplyY
			self._DesignParameter['_ViaMet12Met2OnSupply'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_DesignParameter=None, _Name='ViaMet12Met2OnSupplyIn{}'.format(_Name)))[0]
			self._DesignParameter['_ViaMet12Met2OnSupply']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureY(**_ViaVDDMet12Met2)
			self._DesignParameter['_ViaMet12Met2OnSupply']['_XYCoordinates'] = self._DesignParameter['NbodyContact']['_XYCoordinates'] + self._DesignParameter['PbodyContact']['_XYCoordinates']

			_ViaVDDMet22Met3 = copy.deepcopy(ViaMet22Met3._ViaMet22Met3._ParametersForDesignCalculation)
			_ViaVDDMet22Met3['_ViaMet22Met3NumberOfCOX'] = _ViaNumSupplyX
			_ViaVDDMet22Met3['_ViaMet22Met3NumberOfCOY'] = _ViaNumSupplyY
			self._DesignParameter['_ViaMet22Met3OnSupply'] = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_DesignParameter=None, _Name='ViaMet22Met3OnSupplyIn{}'.format(_Name)))[0]
			self._DesignParameter['_ViaMet22Met3OnSupply']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureY(**_ViaVDDMet22Met3)
			self._DesignParameter['_ViaMet22Met3OnSupply']['_XYCoordinates'] = self._DesignParameter['NbodyContact']['_XYCoordinates'] + self._DesignParameter['PbodyContact']['_XYCoordinates']

			if _Finger < 3 :
				raise NotImplementedError

if __name__ == '__main__':
	import ftplib

	for i in range(1, 2) :
		_Finger = 3#random.randint(5,16)
		_ChannelWidth = 200#random.randrange(700,1200,10)
		_ChannelLength = 60
		_NPRatio = 2
		_VDD2VSSHeight = None
		_Dummy = False
		_NumSupplyCoX = None
		_NumSupplyCoY = None
		_SupplyMet1XWidth = None
		_SupplyMet1YWidth = None
		_NumViaPoly2Met1CoX = None
		_NumViaPoly2Met1CoY = None
		_NumViaPMOSMet12Met2CoX = None
		_NumViaPMOSMet12Met2CoY = None
		_NumViaNMOSMet12Met2CoX = None
		_NumViaNMOSMet12Met2CoY = None
		_XVT = 'LVT'
		_SupplyLine = False


		# from Private import MyInfo
		# import DRCchecker
		libname = 'Inverter'
		cellname = 'Inverter'
		_fileName = cellname + '.gds'

		InputParams = dict(
		_Finger=_Finger,
		_ChannelWidth = _ChannelWidth,
		_ChannelLength = _ChannelLength,
		_NPRatio = _NPRatio,
		_VDD2VSSHeight = _VDD2VSSHeight,
		_Dummy = _Dummy,
		_NumSupplyCoX = _NumSupplyCoX,
		_NumSupplyCoY = _NumSupplyCoY,
		_SupplyMet1XWidth = _SupplyMet1XWidth,
		_SupplyMet1YWidth = _SupplyMet1YWidth,
		_NumViaPoly2Met1CoX = _NumViaPoly2Met1CoX,
		_NumViaPoly2Met1CoY = _NumViaPoly2Met1CoY,
		_NumViaPMOSMet12Met2CoX = _NumViaPMOSMet12Met2CoX,
		_NumViaPMOSMet12Met2CoY = _NumViaPMOSMet12Met2CoY,
		_NumViaNMOSMet12Met2CoX = _NumViaNMOSMet12Met2CoX,
		_NumViaNMOSMet12Met2CoY = _NumViaNMOSMet12Met2CoY,
		_XVT = _XVT,
		_SupplyLine = _SupplyLine
		)
		LayoutObj = _Inverter(_DesignParameter=None, _Name=cellname)
		LayoutObj._CalculateDesignParameter(**InputParams)
		LayoutObj._UpdateDesignParameter2GDSStructure(_DesignParameterInDictionary=LayoutObj._DesignParameter)
		testStreamFile = open('./{}'.format(_fileName), 'wb')
		tmp = LayoutObj._CreateGDSStream(LayoutObj._DesignParameter['_GDSFile']['_GDSFile'])
		tmp.write_binary_gds_stream(testStreamFile)
		testStreamFile.close()

		print('#############################      Sending to FTP Server...      #############################')

		# ftp = ftplib.FTP('141.223.29.62')
		# ftp.login('junung', 'chlwnsdnd1!')
		# ftp.cwd('/mnt/sdc/junung/OPUS/Samsung28n')
		# myfile = open('Inverter.gds', 'rb')
		# ftp.storbinary('STOR Inverter.gds', myfile)
		# myfile.close()
		# ftp.close()
		# My = MyInfo.USER(DesignParameters._Technology)
		# Checker = DRCchecker.DRCchecker(
		#     username=My.ID,
		#     password=My.PW,
		#     WorkDir=My.Dir_Work,
		#     DRCrunDir=My.Dir_DRCrun,
		#     libname=libname,
		#     cellname=cellname,
		#     GDSDir=My.Dir_GDS
		# )
		# Checker.Upload2FTP()
		# Checker.StreamIn(tech=DesignParameters._Technology)

		import ftplib

		# ftp = ftplib.FTP('141.223.29.62')
		# ftp.login('jicho0927', 'cho89140616!!')
		# ftp.cwd('/mnt/sdc/jicho0927/OPUS/SAMSUNG28n')
		# myfile = open('Inverter.gds', 'rb')
		# ftp.storbinary('STOR Inverter.gds', myfile)
		# myfile.close()
	#
	#     import DRCchecker
	#     a = DRCchecker.DRCchecker('jicho0927','cho89140616!!','/mnt/sdc/jicho0927/OPUS/SAMSUNG28n','/mnt/sdc/jicho0927/OPUS/SAMSUNG28n/DRC/run','Inverter','Inverter',None)
	#     a.DRCchecker()
	#
	# print ("DRC Clean!!!")


	#     import ftplib
	#
		ftp = ftplib.FTP('141.223.29.62')
		ftp.login('jicho0927', 'cho89140616!!')
		ftp.cwd('/mnt/sdc/jicho0927/OPUS/tsmc65n')
		myfile = open('Inverter.gds', 'rb')
		ftp.storbinary('STOR Inverter.gds', myfile)
		myfile.close()

	#     import DRCchecker
	#     a = DRCchecker.DRCchecker('jicho0927','cho89140616!!','/mnt/sdc/jicho0927/OPUS/tsmc65n','/mnt/sdc/jicho0927/OPUS/tsmc65n/DRC/run','Inverter','Inverter',None)
	#     a.DRCchecker()
	#
	# print ("DRC Clean!!!")

	#     import ftplib
	#
	#     ftp = ftplib.FTP('141.223.29.62')
	#     ftp.login('jicho0927', 'cho89140616!!')
	#     ftp.cwd('/mnt/sdc/jicho0927/OPUS/tsmc40n')
	#     myfile = open('Inverter.gds', 'rb')
	#     ftp.storbinary('STOR Inverter.gds', myfile)
	#     myfile.close()
	#
	#     import DRCchecker
	#     a = DRCchecker.DRCchecker('jicho0927','cho89140616!!','/mnt/sdc/jicho0927/OPUS/tsmc40n','/mnt/sdc/jicho0927/OPUS/tsmc40n/DRC/run','Inverter','Inverter',None)
	#     a.DRCchecker()
	#
	#
	# print ("DRC Clean!!!")

	#     import ftplib
	#
	#     ftp = ftplib.FTP('141.223.29.62')
	#     ftp.login('jicho0927', 'cho89140616!!')
	#     ftp.cwd('/mnt/sdc/jicho0927/OPUS/tsmc90n')
	#     myfile = open('Inverter.gds', 'rb')
	#     ftp.storbinary('STOR Inverter.gds', myfile)
	#     myfile.close()
	#
	#     import DRCchecker
	#     a = DRCchecker.DRCchecker('jicho0927','cho89140616!!','/mnt/sdc/jicho0927/OPUS/tsmc90n','/mnt/sdc/jicho0927/OPUS/tsmc90n/DRC/run','Inverter','Inverter',None)
	#     a.DRCchecker()
	#
	#
	# print ("DRC Clean!!!")