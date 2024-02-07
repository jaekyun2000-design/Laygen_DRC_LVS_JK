import StickDiagram
import DesignParameters
import copy
import DRC
import ViaPoly2Met1
import ViaMet12Met2
import ViaMet22Met3
import ViaMet32Met4
import ViaMet42Met5
import ViaMet52Met6
import ViaMet62Met7
import ftplib
import RB2

class _FullResistorBank(StickDiagram._StickDiagram) :
	_ParametersForDesignCalculation = dict(
											_XRBNum = None, _YRBNum = None,
											# _InverterFinger=None, _InverterChannelWidth=None, _InverterChannelLength=None, _InverterNPRatio=None, _InverterVDD2VSSHeight=None,
										   _TransmissionGateFinger = None, _TransmissionGateChannelWidth = None, _TransmissionGateChannelLength = None, _TransmissionGateNPRatio = None,
										   _TransmissionGateVDD2VSSHeight = None,
										   _PowerLine = False, _InputLine = False,
										   _ResistorWidth=None, _ResistorLength=None, _ResistorMetXCO=None,_ResistorMetYCO=None,
										   _PMOSSubringType=True, _PMOSSubringXWidth=None, _PMOSSubringYWidth=None,
										   _PMOSSubringWidth=None,
										   _NMOSSubringType=True, _NMOSSubringXWidth=None, _NMOSSubringYWidth=None,
										   _NMOSSubringWidth=None,
										   _TotalSubringType=True, _TotalSubringXWidth=None, _TotalSubringYWidth=None,
										   _TotalSubringWidth=None)

	def __init__(self, _DesignParameter=None, _Name='FullResistorBank'):
		if _DesignParameter != None:
			self._DesignParameter = _DesignParameter
		else:
			self._DesignParameter = dict(_Name=self._NameDeclaration(_Name=_Name),_GDSFile=self._GDSObjDeclaration(_GDSFile=None))

		if _Name == None:
			self._DesignParameter['_Name']['_Name'] = _Name

	def _CalculateFullResistorBank(self,
							   _XRBNum = None, _YRBNum = None,
							   _TransmissionGateFinger=None, _TransmissionGateChannelWidth=None,
							   _TransmissionGateChannelLength=None, _TransmissionGateNPRatio=None,
							   _TransmissionGateDummy=False, _TransmissionGateVDD2VSSHeight=None,
							   _TransmissionGateXVT=None,
							   _PowerLine = False, _InputLine = False,
							   _ResistorWidth=None, _ResistorLength=None, _ResistorMetXCO=None, _ResistorMetYCO=None,
							   _PMOSSubringType=True, _PMOSSubringXWidth=None, _PMOSSubringYWidth=None,
							   _PMOSSubringWidth=None,
							   _NMOSSubringType=True, _NMOSSubringXWidth=None, _NMOSSubringYWidth=None,
							   _NMOSSubringWidth=None,
							   _TotalSubringType=True, _TotalSubringXWidth=None, _TotalSubringYWidth=None,
							   _TotalSubringWidth=None):

		print ('#########################################################################################################')
		print ('                                {}  FullResistorBank Calculation Start                                       '.format(self._DesignParameter['_Name']['_Name']))
		print ('#########################################################################################################')

		_DRCObj = DRC.DRC()
		_Name = 'FullResistorBank'
		_MinSnapSpacing = _DRCObj._MinSnapSpacing

		print ('###############################      ResistorBank Generation     #########################################')

		if _TransmissionGateVDD2VSSHeight == None :
			det = 0
		else :
			det = 1

		while det != 2 :

			_ResistorBankinputs = copy.deepcopy(RB2._ResistorBank._ParametersForDesignCalculation)
			_ResistorBankinputs['_TransmissionGateFinger'] = _TransmissionGateFinger
			_ResistorBankinputs['_TransmissionGateChannelWidth'] = _TransmissionGateChannelWidth
			_ResistorBankinputs['_TransmissionGateChannelLength'] = _TransmissionGateChannelLength
			_ResistorBankinputs['_TransmissionGateNPRatio'] = _TransmissionGateNPRatio
			_ResistorBankinputs['_TransmissionGateDummy'] = _TransmissionGateDummy
			_ResistorBankinputs['_TransmissionGateVDD2VSSHeight'] = _TransmissionGateVDD2VSSHeight
			_ResistorBankinputs['_TransmissionGateXVT'] = _TransmissionGateXVT
			_ResistorBankinputs['_PowerLine'] = _PowerLine

			_ResistorBankinputs['_ResistorWidth'] = _ResistorWidth
			_ResistorBankinputs['_ResistorLength'] = _ResistorLength
			_ResistorBankinputs['_ResistorMetXCO'] = _ResistorMetXCO
			_ResistorBankinputs['_ResistorMetYCO'] = _ResistorMetYCO

			_ResistorBankinputs['_PMOSSubringType'] = _PMOSSubringType
			_ResistorBankinputs['_PMOSSubringXWidth'] = _PMOSSubringXWidth
			_ResistorBankinputs['_PMOSSubringYWidth'] = _PMOSSubringYWidth
			_ResistorBankinputs['_PMOSSubringWidth'] = _PMOSSubringWidth

			_ResistorBankinputs['_NMOSSubringType'] = _NMOSSubringType
			_ResistorBankinputs['_NMOSSubringXWidth'] = _NMOSSubringXWidth
			_ResistorBankinputs['_NMOSSubringYWidth'] = _NMOSSubringYWidth
			_ResistorBankinputs['_NMOSSubringWidth'] = _NMOSSubringWidth

			_ResistorBankinputs['_TotalSubringType'] = _TotalSubringType
			_ResistorBankinputs['_TotalSubringXWidth'] = _TotalSubringXWidth
			_ResistorBankinputs['_TotalSubringYWidth'] = _TotalSubringYWidth
			_ResistorBankinputs['_TotalSubringWidth'] = _TotalSubringWidth

			self._DesignParameter['_ResistorBank'] = self._SrefElementDeclaration(_DesignObj=RB2._ResistorBank(_DesignParameter=None,_Name='ResistorBankIn{}'.format(_Name)))[0]
			self._DesignParameter['_ResistorBank']['_DesignObj']._CalculateResistorBank(**_ResistorBankinputs)

			if _TransmissionGateVDD2VSSHeight == None :
				_TransmissionGateVDD2VSSHeight = self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_VDD2VSSMinHeight']['_Ignore']
				det += 1

			else :
				det += 1


		print ('#################################       Coordinates Settings      ########################################')
		_ResistorBankOrigin = [[0,0]]
		_ResistorSpaceX = (self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_TotalSubringRB']['_DesignObj']._DesignParameter['_Met1Layerx']['_XWidth'] -
															 self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_TotalSubringRB']['_DesignObj']._DesignParameter['_Met1Layerx']['_YWidth'])
		_ResistorSpaceY = (self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_TotalSubringRB']['_DesignObj']._DesignParameter['_Met1Layery']['_YWidth'] -
															 self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_TotalSubringRB']['_DesignObj']._DesignParameter['_Met1Layery']['_XWidth'])

		_GapbtwOriginX = _ResistorBankOrigin[0][0] + self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_Met5LayerInput']['_XYCoordinates'][0][1][0]
		_GapbtwOriginY = _ResistorBankOrigin[0][1] + (self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_TotalSubringRB']['_XYCoordinates'][0][1] +
													self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_TotalSubringRB']['_DesignObj']._DesignParameter['_Met1Layerx']['_XYCoordinates'][1][1])


		self._DesignParameter['_ResistorSpaceX']= {'_Ignore': _ResistorSpaceX, '_DesignParametertype': None, '_ElementName': None, '_XYCoordinates': None, '_Width': None, '_Layer': None, '_Datatype': None}
		self._DesignParameter['_ResistorSpaceY']= {'_Ignore': _ResistorSpaceY, '_DesignParametertype': None, '_ElementName': None, '_XYCoordinates': None, '_Width': None, '_Layer': None, '_Datatype': None}
		self._DesignParameter['_GapbtwOriginX']= {'_Ignore': _GapbtwOriginX, '_DesignParametertype': None, '_ElementName': None, '_XYCoordinates': None, '_Width': None, '_Layer': None, '_Datatype': None}
		self._DesignParameter['_GapbtwOriginY']= {'_Ignore': _GapbtwOriginY, '_DesignParametertype': None, '_ElementName': None, '_XYCoordinates': None, '_Width': None, '_Layer': None, '_Datatype': None}


		tmp = []
		for i in range (0, _XRBNum) :
			for j in range(0, _YRBNum) :
				tmp.append([_ResistorBankOrigin[0][0] + i * _ResistorSpaceX,
							_ResistorBankOrigin[0][1] + j * _ResistorSpaceY])

		self._DesignParameter['_ResistorBank']['_XYCoordinates'] = tmp
		del tmp


		print ('################################       Additional Path Settings      #####################################')
		self._DesignParameter['_Met4LayerVCM'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL4'][0], _Datatype=DesignParameters._LayerMapping['METAL4'][1],_XYCoordinates=[], _Width=100)
		self._DesignParameter['_Met4LayerVCM']['_Width'] = self.CeilMinSnapSpacing(int(self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_Met4LayerVCM']['_XWidth'] + \
														self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_ViaVCMMet32Met4']['_DesignObj']._DesignParameter['_Met4Layer']['_XWidth']), 2*_MinSnapSpacing)

		tmp = []

		for i in range (0, _XRBNum) :
			tmp.append([[_ResistorBankOrigin[0][0] + self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_Met4LayerVCM']['_XYCoordinates'][0][0] + i * _ResistorSpaceX,
							self.CeilMinSnapSpacing(_ResistorBankOrigin[0][1] + _GapbtwOriginY, 2*_MinSnapSpacing)],
							[_ResistorBankOrigin[0][0] + self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_Met4LayerVCM']['_XYCoordinates'][0][0] + i * _ResistorSpaceX,
							self.CeilMinSnapSpacing(_ResistorBankOrigin[0][1] + _GapbtwOriginY + (_YRBNum) * _ResistorSpaceY + _TotalSubringWidth / 2, 2*_MinSnapSpacing)]])

		self._DesignParameter['_Met4LayerVCM']['_XYCoordinates'] = tmp

		del tmp

		self._DesignParameter['_Met5LayerVCM'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL5'][0], _Datatype=DesignParameters._LayerMapping['METAL5'][1],_XYCoordinates=[], _Width=100)
		self._DesignParameter['_Met5LayerVCM']['_Width'] = self.CeilMinSnapSpacing((self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_TotalSubringRB']['_XYCoordinates'][0][1] +
															self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_TotalSubringRB']['_DesignObj']._DesignParameter['_Met1Layerx']['_XYCoordinates'][0][1])- \
														self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_ViaMet22Met3OnRes']['_XYCoordinates'][0][1], 2*_MinSnapSpacing)
		tmp = []
		for i in range (0, _YRBNum) :
			if i % 2 == 0 :
				tmp.append([[_ResistorBankOrigin[0][0] + _GapbtwOriginX ,
						self.FloorMinSnapSpacing(self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_ViaMet22Met3OnRes']['_XYCoordinates'][0][1] + self._DesignParameter['_Met5LayerVCM']['_Width'] / 2 + i * _ResistorSpaceY, 2*_MinSnapSpacing)],
						[_ResistorBankOrigin[0][0] + _GapbtwOriginX  + _XRBNum * _ResistorSpaceX,
						self.FloorMinSnapSpacing(self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_ViaMet22Met3OnRes']['_XYCoordinates'][0][1] + self._DesignParameter['_Met5LayerVCM']['_Width'] / 2 + i * _ResistorSpaceY, 2*_MinSnapSpacing)]])


		self._DesignParameter['_Met5LayerVCM']['_XYCoordinates'] = tmp

		del tmp

		_ViaVCMMet42Met5 = copy.deepcopy(ViaMet42Met5._ViaMet42Met5._ParametersForDesignCalculation)
		_ViaVCMMet42Met5['_ViaMet42Met5NumberOfCOX'] = int((self._DesignParameter['_Met4LayerVCM']['_Width'] - _DRCObj._VIAxMinWidth) // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace2)) + 1
		_ViaVCMMet42Met5['_ViaMet42Met5NumberOfCOY'] = int((self._DesignParameter['_Met5LayerVCM']['_Width'] - _DRCObj._VIAxMinWidth - _DRCObj._MetalxMinEnclosureCO2 * 2) // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace2)) + 1


		if _ViaVCMMet42Met5['_ViaMet42Met5NumberOfCOX'] <= 1 :
			_ViaVCMMet42Met5['_ViaMet42Met5NumberOfCOX'] = 1
			_ViaVCMMet42Met5['_ViaMet42Met5NumberOfCOY'] = int((self._DesignParameter['_Met5LayerVCM']['_Width'] - _DRCObj._VIAxMinWidth - _DRCObj._MetalxMinEnclosureCO2 * 2) // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace)) + 1

		if _ViaVCMMet42Met5['_ViaMet42Met5NumberOfCOY'] <= 1 :
			_ViaVCMMet42Met5['_ViaMet42Met5NumberOfCOY'] = 1
			_ViaVCMMet42Met5['_ViaMet42Met5NumberOfCOX'] = int((self._DesignParameter['_Met4LayerVCM']['_Width'] - _DRCObj._VIAxMinWidth) // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace)) + 1

		self._DesignParameter['_ViaMet42Met5OnVCM'] = self._SrefElementDeclaration(_DesignObj=ViaMet42Met5._ViaMet42Met5(_DesignParameter=None, _Name = 'ViaMet42Met5OnVCMIn{}'.format(_Name)))[0]
		self._DesignParameter['_ViaMet42Met5OnVCM']['_DesignObj']._CalculateViaMet42Met5DesignParameterMinimumEnclosureX(**_ViaVCMMet42Met5)

		tmp = []
		for i in range (0, _XRBNum) :
			for j in range (0, len(self._DesignParameter['_Met5LayerVCM']['_XYCoordinates'])) :
				tmp.append([self._DesignParameter['_Met4LayerVCM']['_XYCoordinates'][0][0][0] + i * _ResistorSpaceX,
							self._DesignParameter['_Met5LayerVCM']['_XYCoordinates'][j][0][1]])
		self._DesignParameter['_ViaMet42Met5OnVCM']['_XYCoordinates'] = tmp

		del tmp


		self._DesignParameter['_Met6LayerVCM'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL6'][0], _Datatype=DesignParameters._LayerMapping['METAL6'][1],_XYCoordinates=[], _Width=100)
		self._DesignParameter['_Met6LayerVCM']['_Width'] = self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_PMOSSubringRB']['_DesignObj']._DesignParameter['_Met1Layerx']['_XWidth'] -\
														 self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_PMOSSubringRB']['_DesignObj']._DesignParameter['_Met1Layery']['_XWidth'] * 2
		if DesignParameters._Technology != '090nm' :
			self._DesignParameter['_Met6LayerVCM']['_Width'] = self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_PMOSSubringRB']['_DesignObj']._DesignParameter['_Met1Layerx']['_XWidth'] -\
														 self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_PMOSSubringRB']['_DesignObj']._DesignParameter['_Met1Layery']['_XWidth'] * 2
		else :
			if self._DesignParameter['_Met6LayerVCM']['_Width'] >= 4500 :
			 self._DesignParameter['_Met6LayerVCM']['_Width'] = 4500

		tmp = []
		for i in range (0, _XRBNum) :
			if i % 4 == 0 or i % 4 == 3 :
				tmp.append([[self.CeilMinSnapSpacing(_ResistorBankOrigin[0][0] + min(self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_PMOSSubringRB']['_XYCoordinates'][0][0],
						self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_ViaMet52Met6OnRes']['_XYCoordinates'][0][0] -
						self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_ViaMet52Met6OnRes']['_DesignObj']._DesignParameter['_Met6Layer']['_XWidth'] / 2 -
						_DRCObj._MetalxMinSpace11 - self._DesignParameter['_Met6LayerVCM']['_Width'] / 2) + i * _ResistorSpaceX, 2*_MinSnapSpacing),
						self.CeilMinSnapSpacing(_ResistorBankOrigin[0][1] + _GapbtwOriginY, 2*_MinSnapSpacing)],
						[self.CeilMinSnapSpacing(_ResistorBankOrigin[0][0] + min(self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_PMOSSubringRB']['_XYCoordinates'][0][0],
						self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_ViaMet52Met6OnRes']['_XYCoordinates'][0][0] -
						self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_ViaMet52Met6OnRes']['_DesignObj']._DesignParameter['_Met6Layer']['_XWidth'] / 2 -
						_DRCObj._MetalxMinSpace11 - self._DesignParameter['_Met6LayerVCM']['_Width'] / 2) + i * _ResistorSpaceX , 2*_MinSnapSpacing),
						self.CeilMinSnapSpacing(_ResistorBankOrigin[0][1] + _GapbtwOriginY + _YRBNum * _ResistorSpaceY + _TotalSubringWidth / 2 , 2*_MinSnapSpacing)]])

		self._DesignParameter['_Met6LayerVCM']['_XYCoordinates'] = tmp

		del tmp
		######FFFFFF
		_ViaVCMMet52Met6 = copy.deepcopy(ViaMet52Met6._ViaMet52Met6._ParametersForDesignCalculation)
		_ViaVCMMet52Met6['_ViaMet52Met6NumberOfCOX'] = int((self._DesignParameter['_Met6LayerVCM']['_Width'] - _DRCObj._VIAxMinWidth) // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace2))
		_ViaVCMMet52Met6['_ViaMet52Met6NumberOfCOY'] = int((self._DesignParameter['_Met5LayerVCM']['_Width'] - _DRCObj._VIAxMinWidth - _DRCObj._MetalxMinEnclosureCO2 * 2) // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace2))

		if _ViaVCMMet52Met6['_ViaMet52Met6NumberOfCOX'] <= 1 :
			_ViaVCMMet52Met6['_ViaMet52Met6NumberOfCOX'] = 1
			_ViaVCMMet52Met6['_ViaMet52Met6NumberOfCOY'] = int((self._DesignParameter['_Met5LayerVCM']['_Width'] - _DRCObj._VIAxMinWidth - _DRCObj._MetalxMinEnclosureCO2 * 2) // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace))

		if _ViaVCMMet52Met6['_ViaMet52Met6NumberOfCOY'] <= 1 :
			_ViaVCMMet52Met6['_ViaMet52Met6NumberOfCOY'] = 1
			_ViaVCMMet52Met6['_ViaMet52Met6NumberOfCOX'] = int((self._DesignParameter['_Met6LayerVCM']['_Width'] - _DRCObj._VIAxMinWidth) // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace))

		self._DesignParameter['_ViaMet52Met6OnVCM'] = self._SrefElementDeclaration(_DesignObj=ViaMet52Met6._ViaMet52Met6(_DesignParameter=None, _Name = 'ViaMet52Met6OnVCMIn{}'.format(_Name)))[0]
		self._DesignParameter['_ViaMet52Met6OnVCM']['_DesignObj']._CalculateViaMet52Met6DesignParameterMinimumEnclosureX(**_ViaVCMMet52Met6)

		tmp = []
		for i in range (0, len(self._DesignParameter['_Met6LayerVCM']['_XYCoordinates'])) :
			for j in range (0, len(self._DesignParameter['_Met5LayerVCM']['_XYCoordinates'])) :
				tmp.append([self._DesignParameter['_Met6LayerVCM']['_XYCoordinates'][i][0][0],
							self._DesignParameter['_Met5LayerVCM']['_XYCoordinates'][j][0][1]])
		self._DesignParameter['_ViaMet52Met6OnVCM']['_XYCoordinates'] = tmp

		del tmp

		_Met7LayerVRXEA = int(((_YRBNum * _ResistorSpaceY) * 0.5) // (_DRCObj._MetalxMaxWidth // 2 + _DRCObj._MetalxMinSpace11))
		# Vrx width 조정
		_Met7DefWidth = _DRCObj._MetalxMaxWidth // 2
		if _Met7LayerVRXEA <= 1 :
			_Met7LayerVRXEA = 1


		self._DesignParameter['_Met6LayerVRX'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL6'][0], _Datatype=DesignParameters._LayerMapping['METAL6'][1],_XYCoordinates=[], _Width=100)
		self._DesignParameter['_Met6LayerVRX']['_Width'] = self.CeilMinSnapSpacing(self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_ViaMet52Met6OnRes']['_DesignObj']._DesignParameter['_Met6Layer']['_XWidth'], 2*_MinSnapSpacing)

		tmp = []
		for i in range(0, _XRBNum) :
			tmp.append([[self.CeilMinSnapSpacing(_ResistorBankOrigin[0][0] + self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_ViaMet52Met6OnRes']['_XYCoordinates'][0][0] + i * _ResistorSpaceX, 2*_MinSnapSpacing),
						_ResistorBankOrigin[0][1] + self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_ViaMet52Met6OnRes']['_XYCoordinates'][0][1]],
						[self.CeilMinSnapSpacing(_ResistorBankOrigin[0][0] + self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_ViaMet52Met6OnRes']['_XYCoordinates'][0][0] + i * _ResistorSpaceX, 2*_MinSnapSpacing),
						max(_ResistorBankOrigin[0][1] + self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_ViaMet52Met6OnRes']['_XYCoordinates'][0][1] + (_YRBNum - 1) * _ResistorSpaceY,
						self.CeilMinSnapSpacing(_ResistorBankOrigin[0][1] + _GapbtwOriginY + (_Met7LayerVRXEA) * ((_YRBNum * _ResistorSpaceY) // (_Met7LayerVRXEA + 1)) + (_Met7DefWidth - 2 * _DRCObj._MetalxMinSpace11) / 2 + 1, 2*_MinSnapSpacing))]])

		self._DesignParameter['_Met6LayerVRX']['_XYCoordinates'] = tmp

		del tmp


		# _Met7LayerVRXEA = int(((_YRBNum * _ResistorSpaceY) * 0.5) // (_DRCObj._MetalxMaxWidth // 2 + _DRCObj._MetalxMinSpace11))
		# _Met7DefWidth = _DRCObj._MetalxMaxWidth // 2
		# if _Met7LayerVRXEA <= 1 :
		#     _Met7LayerVRXEA = 1
		##
		self._DesignParameter['_Met7LayerVCM'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL7'][0], _Datatype=DesignParameters._LayerMapping['METAL7'][1], _XYCoordinates=[], _Width=100)
		self._DesignParameter['_Met7LayerVCM']['_Width'] = _Met7DefWidth - 2 * _DRCObj._MetalxMinSpace11


		tmp = []
		for i in range (0, _Met7LayerVRXEA) :
			# if i % 4 == 2 :
			#     continue
			# else :
				tmp.append([[_ResistorBankOrigin[0][0] + _GapbtwOriginX,
							self.CeilMinSnapSpacing(_ResistorBankOrigin[0][1] + _GapbtwOriginY + (i + 1) * ((_YRBNum * _ResistorSpaceY) // (_Met7LayerVRXEA + 1)), 2*_MinSnapSpacing)],
							[_ResistorBankOrigin[0][0] + _GapbtwOriginX + _XRBNum * _ResistorSpaceX,
							self.CeilMinSnapSpacing(_ResistorBankOrigin[0][1] + _GapbtwOriginY + (i + 1) * ((_YRBNum * _ResistorSpaceY) // (_Met7LayerVRXEA + 1)), 2*_MinSnapSpacing)]])


		self._DesignParameter['_Met7LayerVCM']['_XYCoordinates'] = tmp


		if _Met7LayerVRXEA != 1 :
			_SpacebtwVRX = (self._DesignParameter['_Met7LayerVCM']['_XYCoordinates'][1][0][1] - self._DesignParameter['_Met7LayerVCM']['_XYCoordinates'][0][0][1]) - \
						self._DesignParameter['_Met7LayerVCM']['_Width']

		else :
			_SpacebtwVRX = self._DesignParameter['_Met7LayerVCM']['_Width'] // 2 + _DRCObj._MetalxMinSpace11 * 2
		##

		self._DesignParameter['_Met7LayerVRX'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL7'][0], _Datatype=DesignParameters._LayerMapping['METAL7'][1],_XYCoordinates=[], _Width=100)
		self._DesignParameter['_Met7LayerVRX']['_Width'] = abs(_SpacebtwVRX - _DRCObj._MetalxMinSpace11 * 4)

		tmp = []
		if len(self._DesignParameter['_Met7LayerVCM']['_XYCoordinates']) > 1 :
			for i in range (0, len(self._DesignParameter['_Met7LayerVCM']['_XYCoordinates'])) :
				if i == 0 :
					continue

				if i == len(self._DesignParameter['_Met7LayerVCM']['_XYCoordinates']) - 1 :
					tmp.append([[_ResistorBankOrigin[0][0] + self._DesignParameter['_Met6LayerVCM']['_XYCoordinates'][0][0][0] - self._DesignParameter['_Met6LayerVCM']['_Width'] // 2,
							self.CeilMinSnapSpacing(_ResistorBankOrigin[0][1] + self._DesignParameter['_Met7LayerVCM']['_XYCoordinates'][i][0][1] -
							self._DesignParameter['_Met7LayerVCM']['_Width'] / 2 - _DRCObj._MetalxMinSpace11 * 2 - self._DesignParameter['_Met7LayerVRX']['_Width'] / 2, 2*_MinSnapSpacing)],
							[_ResistorBankOrigin[0][0] + _GapbtwOriginX + _XRBNum * _ResistorSpaceX,
							self.CeilMinSnapSpacing(_ResistorBankOrigin[0][1] + self._DesignParameter['_Met7LayerVCM']['_XYCoordinates'][i][0][1] -
							self._DesignParameter['_Met7LayerVCM']['_Width'] / 2 - _DRCObj._MetalxMinSpace11 * 2- self._DesignParameter['_Met7LayerVRX']['_Width'] / 2, 2*_MinSnapSpacing)]])

				## VCM 빈도 조정
				elif i % 4 != 3 :
					tmp.append([[_ResistorBankOrigin[0][0] + _GapbtwOriginX,
							self.CeilMinSnapSpacing(_ResistorBankOrigin[0][1] + self._DesignParameter['_Met7LayerVCM']['_XYCoordinates'][i][0][1] -
							self._DesignParameter['_Met7LayerVCM']['_Width'] / 2 - _DRCObj._MetalxMinSpace11 * 2 - self._DesignParameter['_Met7LayerVRX']['_Width'] / 2, 2*_MinSnapSpacing)],
							[_ResistorBankOrigin[0][0] + _GapbtwOriginX + _XRBNum * _ResistorSpaceX,
							self.CeilMinSnapSpacing(_ResistorBankOrigin[0][1] + self._DesignParameter['_Met7LayerVCM']['_XYCoordinates'][i][0][1] -
							self._DesignParameter['_Met7LayerVCM']['_Width'] / 2 - _DRCObj._MetalxMinSpace11 * 2- self._DesignParameter['_Met7LayerVRX']['_Width'] / 2, 2*_MinSnapSpacing)]])

		else :
			tmp.append([[_ResistorBankOrigin[0][0] + + self._DesignParameter['_Met6LayerVCM']['_XYCoordinates'][0][0][0] - self._DesignParameter['_Met6LayerVCM']['_Width'] // 2,
							self.CeilMinSnapSpacing(_ResistorBankOrigin[0][1] + self._DesignParameter['_Met7LayerVCM']['_XYCoordinates'][0][0][1] +
							self._DesignParameter['_Met7LayerVCM']['_Width'] / 2 + _DRCObj._MetalxMinSpace11 * 2 + self._DesignParameter['_Met7LayerVRX']['_Width'] / 2, 2*_MinSnapSpacing)],
							[_ResistorBankOrigin[0][0] + _GapbtwOriginX + _XRBNum * _ResistorSpaceX,
							self.CeilMinSnapSpacing(_ResistorBankOrigin[0][1] + self._DesignParameter['_Met7LayerVCM']['_XYCoordinates'][0][0][1] +
							self._DesignParameter['_Met7LayerVCM']['_Width'] / 2 + _DRCObj._MetalxMinSpace11 * 2 + self._DesignParameter['_Met7LayerVRX']['_Width'] / 2, 2*_MinSnapSpacing)]])
			tmp.append([[_ResistorBankOrigin[0][0] + + self._DesignParameter['_Met6LayerVCM']['_XYCoordinates'][0][0][0] - self._DesignParameter['_Met6LayerVCM']['_Width'] // 2,
							self.CeilMinSnapSpacing(_ResistorBankOrigin[0][1] + self._DesignParameter['_Met7LayerVCM']['_XYCoordinates'][0][0][1] -
							self._DesignParameter['_Met7LayerVCM']['_Width'] / 2 - _DRCObj._MetalxMinSpace11 * 2 - self._DesignParameter['_Met7LayerVRX']['_Width'] / 2, 2*_MinSnapSpacing)],
							[_ResistorBankOrigin[0][0] + _GapbtwOriginX + _XRBNum * _ResistorSpaceX,
							self.CeilMinSnapSpacing(_ResistorBankOrigin[0][1] + self._DesignParameter['_Met7LayerVCM']['_XYCoordinates'][0][0][1] -
							self._DesignParameter['_Met7LayerVCM']['_Width'] / 2 - _DRCObj._MetalxMinSpace11 * 2- self._DesignParameter['_Met7LayerVRX']['_Width'] / 2, 2*_MinSnapSpacing)]])


		self._DesignParameter['_Met7LayerVRX']['_XYCoordinates'] = tmp

		del tmp

		_ViaVRXMet62Met7 = copy.deepcopy(ViaMet62Met7._ViaMet62Met7._ParametersForDesignCalculation)
		_ViaVRXMet62Met7['_ViaMet62Met7NumberOfCOX'] = int((self._DesignParameter['_Met6LayerVRX']['_Width'] - _DRCObj._VIAxMinWidth) // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace2))+1
		_ViaVRXMet62Met7['_ViaMet62Met7NumberOfCOY'] = int((self._DesignParameter['_Met7LayerVRX']['_Width']- _DRCObj._VIAxMinWidth - _DRCObj._MetalxMinEnclosureCO2 * 2) // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace2))+1

		if _ViaVRXMet62Met7['_ViaMet62Met7NumberOfCOX'] <= 1 :
			_ViaVRXMet62Met7['_ViaMet62Met7NumberOfCOX'] = 1
			_ViaVRXMet62Met7['_ViaMet62Met7NumberOfCOY'] = int((self._DesignParameter['_Met7LayerVRX']['_Width']- _DRCObj._VIAxMinWidth - _DRCObj._MetalxMinEnclosureCO2 * 2) // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace))+1

		if _ViaVRXMet62Met7['_ViaMet62Met7NumberOfCOY'] <= 1 :
			_ViaVRXMet62Met7['_ViaMet62Met7NumberOfCOY'] = 1
			_ViaVRXMet62Met7['_ViaMet62Met7NumberOfCOX'] = int((self._DesignParameter['_Met6LayerVRX']['_Width'] - _DRCObj._VIAxMinWidth) // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace))+1


		self._DesignParameter['_ViaMet62Met7OnVRX'] = self._SrefElementDeclaration(_DesignObj=ViaMet62Met7._ViaMet62Met7(_DesignParameter=None, _Name = 'ViaMet62Met7OnVRXIn{}'.format(_Name)))[0]
		self._DesignParameter['_ViaMet62Met7OnVRX']['_DesignObj']._CalculateViaMet62Met7DesignParameterMinimumEnclosureX(**_ViaVRXMet62Met7)

		tmp = []
		for i in range (0, len(self._DesignParameter['_Met6LayerVRX']['_XYCoordinates'])) :
			for j in range (0, len(self._DesignParameter['_Met7LayerVRX']['_XYCoordinates'])) :
				tmp.append([self._DesignParameter['_Met6LayerVRX']['_XYCoordinates'][i][0][0],
							self._DesignParameter['_Met7LayerVRX']['_XYCoordinates'][j][0][1]])
		self._DesignParameter['_ViaMet62Met7OnVRX']['_XYCoordinates'] = tmp

		del tmp

		# self._DesignParameter['_Met7LayerVCM']['_XYCoordinates'] = [[[_ResistorBankOrigin[0][0] + _GapbtwOriginX,
		#                                                             _ResistorBankOrigin[0][1] + _GapbtwOriginY + _ResistorSpaceY // 2 + _DRCObj._MetalxMinSpace11 + self._DesignParameter['_Met7LayerVCM']['_Width'] // 2],
		#                                                             [_ResistorBankOrigin[0][0] + _GapbtwOriginX + _XRBNum * _ResistorSpaceX,
		#                                                             _ResistorBankOrigin[0][1] + _GapbtwOriginY + _ResistorSpaceY // 2 + _DRCObj._MetalxMinSpace11 + self._DesignParameter['_Met7LayerVCM']['_Width'] // 2]],
		#                                                             [[_ResistorBankOrigin[0][0] + _GapbtwOriginX,
		#                                                             _ResistorBankOrigin[0][1] + _GapbtwOriginY + _YRBNum * _ResistorSpaceY
		#                                                             - (_ResistorSpaceY // 2 + _DRCObj._MetalxMinSpace11 + self._DesignParameter['_Met7LayerVCM']['_Width'] // 2)],
		#                                                             [_ResistorBankOrigin[0][0] + _GapbtwOriginX + _XRBNum * _ResistorSpaceX,
		#                                                             _ResistorBankOrigin[0][1] + _GapbtwOriginY + _YRBNum * _ResistorSpaceY
		#                                                             - (_ResistorSpaceY // 2 + _DRCObj._MetalxMinSpace11 + self._DesignParameter['_Met7LayerVCM']['_Width'] // 2)]]]

		_ViaVCMMet62Met7 = copy.deepcopy(ViaMet62Met7._ViaMet62Met7._ParametersForDesignCalculation)
		_ViaVCMMet62Met7['_ViaMet62Met7NumberOfCOX'] = int((self._DesignParameter['_Met6LayerVCM']['_Width'] - _DRCObj._VIAxMinWidth - 2 * _DRCObj._MetalxMinEnclosureCO2) // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace2))
		_ViaVCMMet62Met7['_ViaMet62Met7NumberOfCOY'] = int((self._DesignParameter['_Met7LayerVCM']['_Width'] - _DRCObj._VIAxMinWidth) // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace2))
		if _ViaVCMMet62Met7['_ViaMet62Met7NumberOfCOX'] <= 1 :
			_ViaVCMMet62Met7['_ViaMet62Met7NumberOfCOX'] = 1
			_ViaVCMMet62Met7['_ViaMet62Met7NumberOfCOY'] = int((self._DesignParameter['_Met7LayerVCM']['_Width'] - _DRCObj._VIAxMinWidth) // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace))
		if _ViaVCMMet62Met7['_ViaMet62Met7NumberOfCOY'] <= 1 :
			_ViaVCMMet62Met7['_ViaMet62Met7NumberOfCOY'] = 1
			_ViaVCMMet62Met7['_ViaMet62Met7NumberOfCOX'] = int((self._DesignParameter['_Met6LayerVCM']['_Width'] - _DRCObj._VIAxMinWidth - 2 * _DRCObj._MetalxMinEnclosureCO2) // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace))


		self._DesignParameter['_ViaMet62Met7OnVCM'] = self._SrefElementDeclaration(_DesignObj=ViaMet62Met7._ViaMet62Met7(_DesignParameter=None, _Name = 'ViaMet62Met7OnVCMIn{}'.format(_Name)))[0]
		self._DesignParameter['_ViaMet62Met7OnVCM']['_DesignObj']._CalculateViaMet62Met7DesignParameterMinimumEnclosureY(**_ViaVCMMet62Met7)

		tmp = []
		for i in range (0, len(self._DesignParameter['_Met6LayerVCM']['_XYCoordinates'])) :
			for j in range (0, len(self._DesignParameter['_Met7LayerVCM']['_XYCoordinates'])) :
				tmp.append([self._DesignParameter['_Met6LayerVCM']['_XYCoordinates'][i][0][0],
							self._DesignParameter['_Met7LayerVCM']['_XYCoordinates'][j][0][1]])
		self._DesignParameter['_ViaMet62Met7OnVCM']['_XYCoordinates'] = tmp

		del tmp

		# _TopBotleft = ((_YRBNum * _ResistorSpaceY) - (self._DesignParameter['_Met7LayerVRX']['_XYCoordinates'][-1][0][1] - self._DesignParameter['_Met7LayerVRX']['_XYCoordinates'][0][0][1]) - \
		#     self._DesignParameter['_Met7LayerVRX']['_Width'] - 4 * _DRCObj._MetalxMinSpace11 - self._DesignParameter['_Met7LayerVCM']['_Width'] * 2) // 2

		_TopBotleft = abs(_GapbtwOriginY) + self._DesignParameter['_Met7LayerVCM']['_XYCoordinates'][0][0][1] - self._DesignParameter['_Met7LayerVCM']['_Width'] // 2 - _DRCObj._MetalxMinSpace11

		if _PowerLine == True :
			self._DesignParameter['_Met3LayerVDD'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0], _Datatype=DesignParameters._LayerMapping['METAL3'][1],_XYCoordinates=[], _Width=100)
			self._DesignParameter['_Met3LayerVDD']['_Width'] = self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_Met2LayerVDD']['_YWidth']

			tmp = []

			for i in range (0, _YRBNum) :
				tmp.append([[_ResistorBankOrigin[0][0] + (self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_PMOSSubringRB']['_XYCoordinates'][0][0] -
							self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_PMOSSubringRB']['_DesignObj']._DesignParameter['_Met1Layerx']['_XWidth'] // 2),
							_ResistorBankOrigin[0][1] + self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_PMOSSubringRB']['_XYCoordinates'][0][1] +
							self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_PMOSSubringRB']['_DesignObj']._DesignParameter['_Met1Layerx']['_XYCoordinates'][0][1] +
							i * _ResistorSpaceY],
							[_ResistorBankOrigin[0][0] + (self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_PMOSSubringRB']['_XYCoordinates'][0][0] -
							self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_PMOSSubringRB']['_DesignObj']._DesignParameter['_Met1Layerx']['_XWidth'] // 2) +
							_XRBNum * _ResistorSpaceX,
							_ResistorBankOrigin[0][1] + self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_PMOSSubringRB']['_XYCoordinates'][0][1] +
							self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_PMOSSubringRB']['_DesignObj']._DesignParameter['_Met1Layerx']['_XYCoordinates'][0][1] +
							i * _ResistorSpaceY]])

			self._DesignParameter['_Met3LayerVDD']['_XYCoordinates'] = tmp

			del tmp

			self._DesignParameter['_Met4LayerVDD'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL4'][0], _Datatype=DesignParameters._LayerMapping['METAL4'][1], _XYCoordinates=[], _Width=100)
			self._DesignParameter['_Met4LayerVDD']['_Width'] = self._DesignParameter['_Met3LayerVDD']['_Width'] * 2
			tmp = []

			for i in range (0, _XRBNum + 1) :
				if i % 2 == 1 :
					tmp.append([[_ResistorBankOrigin[0][0] + _GapbtwOriginX + self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_TotalSubringRB']['_DesignObj']._DesignParameter['_Met1Layery']['_XWidth'] // 2 + i * _ResistorSpaceX,
								_ResistorBankOrigin[0][1] + _GapbtwOriginY],
								[_ResistorBankOrigin[0][0] + _GapbtwOriginX + self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_TotalSubringRB']['_DesignObj']._DesignParameter['_Met1Layery']['_XWidth'] // 2 + i * _ResistorSpaceX,
								_ResistorBankOrigin[0][1] + _GapbtwOriginY + _ResistorSpaceY * _YRBNum]])

			self._DesignParameter['_Met4LayerVDD']['_XYCoordinates'] = tmp

			del tmp

			_ViaVDDMet32Met4 = copy.deepcopy(ViaMet32Met4._ViaMet32Met4._ParametersForDesignCalculation)
			_ViaVDDMet32Met4['_ViaMet32Met4NumberOfCOX'] = int((self._DesignParameter['_Met4LayerVDD']['_Width'] - _DRCObj._VIAxMinWidth) // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace2)) + 1
			_ViaVDDMet32Met4['_ViaMet32Met4NumberOfCOY'] = int((self._DesignParameter['_Met3LayerVDD']['_Width'] - _DRCObj._VIAxMinWidth - _DRCObj._MetalxMinEnclosureCO2 * 2) // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace2)) + 1

			if _ViaVDDMet32Met4['_ViaMet32Met4NumberOfCOX'] <= 1 :
				_ViaVDDMet32Met4['_ViaMet32Met4NumberOfCOX'] = 1
				_ViaVDDMet32Met4['_ViaMet32Met4NumberOfCOY'] = int((self._DesignParameter['_Met3LayerVDD']['_Width'] - _DRCObj._VIAxMinWidth - _DRCObj._MetalxMinEnclosureCO2 * 2) // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace)) + 1

			if _ViaVDDMet32Met4['_ViaMet32Met4NumberOfCOY'] <= 1 :
				_ViaVDDMet32Met4['_ViaMet32Met4NumberOfCOY'] = 1
				_ViaVDDMet32Met4['_ViaMet32Met4NumberOfCOX'] = int((self._DesignParameter['_Met4LayerVDD']['_Width'] - _DRCObj._VIAxMinWidth) // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace)) + 1

			self._DesignParameter['_ViaMet32Met4OnVDD'] = self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_DesignParameter=None, _Name = 'ViaMet32Met4OnVDDIn{}'.format(_Name)))[0]
			self._DesignParameter['_ViaMet32Met4OnVDD']['_DesignObj']._CalculateViaMet32Met4DesignParameterMinimumEnclosureX(**_ViaVDDMet32Met4)

			tmp = []
			for i in range (0, len(self._DesignParameter['_Met4LayerVDD']['_XYCoordinates'])) :
				for j in range (0, len(self._DesignParameter['_Met3LayerVDD']['_XYCoordinates'])) :
					tmp.append([self._DesignParameter['_Met4LayerVDD']['_XYCoordinates'][i][0][0],
								self._DesignParameter['_Met3LayerVDD']['_XYCoordinates'][j][0][1]])
			self._DesignParameter['_ViaMet32Met4OnVDD']['_XYCoordinates'] = tmp

			del tmp

			if self._DesignParameter['_ViaMet32Met4OnVDD']['_DesignObj']._DesignParameter['_Met4Layer']['_XWidth'] > self._DesignParameter['_Met4LayerVDD']['_Width'] :
				self._DesignParameter['_Met4LayerVDD']['_Width'] = self._DesignParameter['_ViaMet32Met4OnVDD']['_DesignObj']._DesignParameter['_Met4Layer']['_XWidth']


			if (_XRBNum >= 3) :
				self._DesignParameter['_Met5LayerVDD'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL5'][0], _Datatype=DesignParameters._LayerMapping['METAL5'][1], _XYCoordinates=[], _Width=100)
				self._DesignParameter['_Met5LayerVDD']['_Width'] = self._DesignParameter['_Met5LayerVCM']['_Width']


				tmp = []
				if (_YRBNum != 1) :
					for i in range (0, _YRBNum) :
						if i % 4 == 3 :
							tmp.append([[_ResistorBankOrigin[0][0] + _GapbtwOriginX + self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_TotalSubringRB']['_DesignObj']._DesignParameter['_Met1Layery']['_XWidth'] // 2 -
								self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_TotalSubringRB']['_DesignObj']._DesignParameter['_Met1Layery']['_XWidth'] * 2,
								self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_ViaMet22Met3OnRes']['_XYCoordinates'][0][1] + self._DesignParameter['_Met5LayerVCM']['_Width'] // 2 + i * _ResistorSpaceY],
								[_ResistorBankOrigin[0][0] + _GapbtwOriginX  + _XRBNum * _ResistorSpaceX - self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_TotalSubringRB']['_DesignObj']._DesignParameter['_Met1Layery']['_XWidth'] // 2 +
								self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_TotalSubringRB']['_DesignObj']._DesignParameter['_Met1Layery']['_XWidth'] * 2,
								self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_ViaMet22Met3OnRes']['_XYCoordinates'][0][1] + self._DesignParameter['_Met5LayerVCM']['_Width'] // 2 + i * _ResistorSpaceY]])

				else :
					tmp.append([[_ResistorBankOrigin[0][0] + _GapbtwOriginX + self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_TotalSubringRB']['_DesignObj']._DesignParameter['_Met1Layery']['_XWidth'] // 2 -
								self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_TotalSubringRB']['_DesignObj']._DesignParameter['_Met1Layery']['_XWidth'] * 2
								- _DRCObj._MetalxMinSpace11 * (3 - _XRBNum) - self._DesignParameter['_Met6LayerVCM']['_Width'] * (3 - _XRBNum),
								self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_ViaMet22Met3OnRes']['_XYCoordinates'][0][1] + self._DesignParameter['_Met5LayerVCM']['_Width'] // 2],
								[_ResistorBankOrigin[0][0] + _GapbtwOriginX  + _XRBNum * _ResistorSpaceX - self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_TotalSubringRB']['_DesignObj']._DesignParameter['_Met1Layery']['_XWidth'] // 2 +
								self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_TotalSubringRB']['_DesignObj']._DesignParameter['_Met1Layery']['_XWidth'] * 2,
								self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_ViaMet22Met3OnRes']['_XYCoordinates'][0][1] + self._DesignParameter['_Met5LayerVCM']['_Width'] // 2]])


				self._DesignParameter['_Met5LayerVDD']['_XYCoordinates'] = tmp

				del tmp

				_ViaVDDMet42Met5 = copy.deepcopy(ViaMet42Met5._ViaMet42Met5._ParametersForDesignCalculation)
				_ViaVDDMet42Met5['_ViaMet42Met5NumberOfCOX'] = int((self._DesignParameter['_Met4LayerVDD']['_Width'] - _DRCObj._VIAxMinWidth) // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace2)) + 1
				_ViaVDDMet42Met5['_ViaMet42Met5NumberOfCOY'] = int((self._DesignParameter['_Met5LayerVDD']['_Width'] - _DRCObj._VIAxMinWidth - 2 * _DRCObj._MetalxMinEnclosureCO2) // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace2)) + 1
				if _ViaVDDMet42Met5['_ViaMet42Met5NumberOfCOX'] <= 1 :
					_ViaVDDMet42Met5['_ViaMet42Met5NumberOfCOX'] = 1
					_ViaVDDMet42Met5['_ViaMet42Met5NumberOfCOY'] = int((self._DesignParameter['_Met5LayerVDD']['_Width'] - _DRCObj._VIAxMinWidth - 2 * _DRCObj._MetalxMinEnclosureCO2) // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace)) + 1
				if _ViaVDDMet42Met5['_ViaMet42Met5NumberOfCOY'] <= 1 :
					_ViaVDDMet42Met5['_ViaMet42Met5NumberOfCOY'] = 1
					_ViaVDDMet42Met5['_ViaMet42Met5NumberOfCOX'] = int((self._DesignParameter['_Met4LayerVDD']['_Width'] - _DRCObj._VIAxMinWidth) // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace)) + 1

				self._DesignParameter['_ViaMet42Met5OnVDD'] = self._SrefElementDeclaration(_DesignObj=ViaMet42Met5._ViaMet42Met5(_DesignParameter=None, _Name = 'ViaMet42Met5OnVDDIn{}'.format(_Name)))[0]
				self._DesignParameter['_ViaMet42Met5OnVDD']['_DesignObj']._CalculateViaMet42Met5DesignParameterMinimumEnclosureX(**_ViaVDDMet42Met5)

				tmp = []
				for i in range (0, len(self._DesignParameter['_Met4LayerVDD']['_XYCoordinates'])) :
					for j in range (0, len(self._DesignParameter['_Met5LayerVDD']['_XYCoordinates'])) :
						tmp.append([self._DesignParameter['_Met4LayerVDD']['_XYCoordinates'][i][0][0],
									self._DesignParameter['_Met5LayerVDD']['_XYCoordinates'][j][0][1]])

				self._DesignParameter['_ViaMet42Met5OnVDD']['_XYCoordinates'] = tmp

				del tmp


				self._DesignParameter['_Met6LayerVDD'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL6'][0], _Datatype=DesignParameters._LayerMapping['METAL6'][1],_XYCoordinates=[], _Width=100)
				self._DesignParameter['_Met6LayerVDD']['_Width'] = self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_PMOSSubringRB']['_DesignObj']._DesignParameter['_Met1Layerx']['_XWidth'] -\
																self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_PMOSSubringRB']['_DesignObj']._DesignParameter['_Met1Layery']['_XWidth'] * 2

				tmp = []
				for i in range (0, _XRBNum) :
					if i % 4 == 2 :
						tmp.append([[_ResistorBankOrigin[0][0] + min(self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_PMOSSubringRB']['_XYCoordinates'][0][0],
								self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_ViaMet52Met6OnRes']['_XYCoordinates'][0][0] -
								self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_ViaMet52Met6OnRes']['_DesignObj']._DesignParameter['_Met6Layer']['_XWidth'] // 2 -
								_DRCObj._MetalxMinSpace11 - self._DesignParameter['_Met6LayerVCM']['_Width'] // 2) + i * _ResistorSpaceX,
								_ResistorBankOrigin[0][1] + _GapbtwOriginY],
								[_ResistorBankOrigin[0][0] + min(self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_PMOSSubringRB']['_XYCoordinates'][0][0],
								self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_ViaMet52Met6OnRes']['_XYCoordinates'][0][0] -
								self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_ViaMet52Met6OnRes']['_DesignObj']._DesignParameter['_Met6Layer']['_XWidth'] // 2 -
								_DRCObj._MetalxMinSpace11 - self._DesignParameter['_Met6LayerVCM']['_Width'] // 2) + i * _ResistorSpaceX,
								_ResistorBankOrigin[0][1] + _GapbtwOriginY + _YRBNum * _ResistorSpaceY]])

				self._DesignParameter['_Met6LayerVDD']['_XYCoordinates'] = tmp

				del tmp


				_ViaVDDMet52Met6 = copy.deepcopy(ViaMet52Met6._ViaMet52Met6._ParametersForDesignCalculation)
				_ViaVDDMet52Met6['_ViaMet52Met6NumberOfCOX'] = int((self._DesignParameter['_Met6LayerVDD']['_Width'] - _DRCObj._VIAxMinWidth) // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace2)) + 1
				_ViaVDDMet52Met6['_ViaMet52Met6NumberOfCOY'] = int((self._DesignParameter['_Met5LayerVDD']['_Width'] - _DRCObj._VIAxMinWidth - 2 * _DRCObj._MetalxMinEnclosureCO2) // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace2)) + 1
				if _ViaVDDMet52Met6['_ViaMet52Met6NumberOfCOX'] <= 1 :
					_ViaVDDMet52Met6['_ViaMet52Met6NumberOfCOX'] = 1
					_ViaVDDMet52Met6['_ViaMet52Met6NumberOfCOY'] = int((self._DesignParameter['_Met5LayerVDD']['_Width'] - _DRCObj._VIAxMinWidth - 2 * _DRCObj._MetalxMinEnclosureCO2) // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace)) + 1
				if _ViaVDDMet52Met6['_ViaMet52Met6NumberOfCOY'] <= 1 :
					_ViaVDDMet52Met6['_ViaMet52Met6NumberOfCOY'] = 1
					_ViaVDDMet52Met6['_ViaMet52Met6NumberOfCOX'] = int((self._DesignParameter['_Met6LayerVDD']['_Width'] - _DRCObj._VIAxMinWidth) // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace)) + 1

				self._DesignParameter['_ViaMet52Met6OnVDD'] = self._SrefElementDeclaration(_DesignObj=ViaMet52Met6._ViaMet52Met6(_DesignParameter=None, _Name = 'ViaMet52Met6OnVDDIn{}'.format(_Name)))[0]
				self._DesignParameter['_ViaMet52Met6OnVDD']['_DesignObj']._CalculateViaMet52Met6DesignParameterMinimumEnclosureX(**_ViaVDDMet52Met6)

				tmp = []
				for i in range (0, len(self._DesignParameter['_Met6LayerVDD']['_XYCoordinates'])) :
					for j in range (0, len(self._DesignParameter['_Met5LayerVDD']['_XYCoordinates'])) :
						tmp.append([self._DesignParameter['_Met6LayerVDD']['_XYCoordinates'][i][0][0],
									self._DesignParameter['_Met5LayerVDD']['_XYCoordinates'][j][0][1]])

				self._DesignParameter['_ViaMet52Met6OnVDD']['_XYCoordinates'] = tmp

				del tmp

				# self._DesignParameter['_Met7LayerVDD'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL7'][0], _Datatype=DesignParameters._LayerMapping['METAL7'][1], _XYCoordinates=[], _Width=100)
				# self._DesignParameter['_Met7LayerVDD']['_Width'] = _ResistorSpaceY // 2
				# self._DesignParameter['_Met7LayerVDD']['_XYCoordinates'] = [[[_ResistorBankOrigin[0][0] + _GapbtwOriginX,
				#                                                             _ResistorBankOrigin[0][1] + _GapbtwOriginY + _YRBNum * _ResistorSpaceY - self._DesignParameter['_Met7LayerVDD']['_Width'] // 2],
				#                                                             [_ResistorBankOrigin[0][0] + _GapbtwOriginX + _XRBNum * _ResistorSpaceX ,
				#                                                             _ResistorBankOrigin[0][1] + _GapbtwOriginY + _YRBNum * _ResistorSpaceY - self._DesignParameter['_Met7LayerVDD']['_Width'] // 2]]]

				self._DesignParameter['_Met7LayerVDD'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL7'][0], _Datatype=DesignParameters._LayerMapping['METAL7'][1], _XYCoordinates=[], _Width=100)
				self._DesignParameter['_Met7LayerVDD']['_Width'] = (_TopBotleft - _DRCObj._MetalxMinSpace11 * 2) // 2
				if self._DesignParameter['_Met7LayerVDD']['_Width'] % 2 == 1 :
					self._DesignParameter['_Met7LayerVDD']['_Width'] -= 1
				self._DesignParameter['_Met7LayerVDD']['_XYCoordinates'] = [[[_ResistorBankOrigin[0][0] + _GapbtwOriginX,
																			_ResistorBankOrigin[0][1] + _GapbtwOriginY + _YRBNum * _ResistorSpaceY - self._DesignParameter['_Met7LayerVDD']['_Width'] // 2],
																			[_ResistorBankOrigin[0][0] + _GapbtwOriginX + _XRBNum * _ResistorSpaceX ,
																			_ResistorBankOrigin[0][1] + _GapbtwOriginY + _YRBNum * _ResistorSpaceY - self._DesignParameter['_Met7LayerVDD']['_Width'] // 2]],
																			[[_ResistorBankOrigin[0][0] + _GapbtwOriginX,
																			_ResistorBankOrigin[0][1] + _GapbtwOriginY + self._DesignParameter['_Met7LayerVDD']['_Width'] * 1.5 + _DRCObj._MetalxMinSpace11 * 2],
																			[_ResistorBankOrigin[0][0] + _GapbtwOriginX + _XRBNum * _ResistorSpaceX,
																			_ResistorBankOrigin[0][1] + _GapbtwOriginY + self._DesignParameter['_Met7LayerVDD']['_Width'] * 1.5 + _DRCObj._MetalxMinSpace11 * 2]]]

				self._DesignParameter['_Met7LayerVDD2'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL7'][0], _Datatype=DesignParameters._LayerMapping['METAL7'][1], _XYCoordinates=[], _Width=100)
				self._DesignParameter['_Met7LayerVDD2']['_Width'] = (_SpacebtwVRX - _DRCObj._MetalxMinSpace11 * 3) // 2
				if self._DesignParameter['_Met7LayerVDD2']['_Width'] % 2 == 1 :
					self._DesignParameter['_Met7LayerVDD2']['_Width'] -= 1
				## VDD Power 빈도 조정
				tmp = []
				for i in range (0, len(self._DesignParameter['_Met7LayerVCM']['_XYCoordinates'])) :
					if i != len(self._DesignParameter['_Met7LayerVCM']['_XYCoordinates']) - 1 and i % 4 == 3 :
						tmp.append([[_ResistorBankOrigin[0][0] + _GapbtwOriginX,
							_ResistorBankOrigin[0][1] + self._DesignParameter['_Met7LayerVCM']['_XYCoordinates'][i][0][1] -
							self._DesignParameter['_Met7LayerVCM']['_Width'] // 2 - _DRCObj._MetalxMinSpace11 - self._DesignParameter['_Met7LayerVDD2']['_Width'] // 2],
							[_ResistorBankOrigin[0][0] + _GapbtwOriginX + _XRBNum * _ResistorSpaceX,
							_ResistorBankOrigin[0][1] + self._DesignParameter['_Met7LayerVCM']['_XYCoordinates'][i][0][1] -
							self._DesignParameter['_Met7LayerVCM']['_Width'] // 2 - _DRCObj._MetalxMinSpace11 - self._DesignParameter['_Met7LayerVDD2']['_Width'] // 2]])

				self._DesignParameter['_Met7LayerVDD2']['_XYCoordinates'] = tmp

				del tmp



				_ViaVDDMet62Met7 = copy.deepcopy(ViaMet62Met7._ViaMet62Met7._ParametersForDesignCalculation)
				_ViaVDDMet62Met7['_ViaMet62Met7NumberOfCOX'] = int((self._DesignParameter['_Met6LayerVDD']['_Width'] - _DRCObj._VIAxMinWidth) // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace2)) + 1
				_ViaVDDMet62Met7['_ViaMet62Met7NumberOfCOY'] = int((self._DesignParameter['_Met7LayerVDD']['_Width'] - _DRCObj._VIAxMinWidth - _DRCObj._MetalxMinEnclosureCO2 * 2) // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace2)) + 1

				if _ViaVDDMet62Met7['_ViaMet62Met7NumberOfCOX'] <= 1 :
					_ViaVDDMet62Met7['_ViaMet62Met7NumberOfCOX'] = 1
					_ViaVDDMet62Met7['_ViaMet62Met7NumberOfCOY'] = int((self._DesignParameter['_Met7LayerVDD']['_Width'] - _DRCObj._VIAxMinWidth - _DRCObj._MetalxMinEnclosureCO2 * 2) // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace)) + 1

				if _ViaVDDMet62Met7['_ViaMet62Met7NumberOfCOY'] <= 1 :
					_ViaVDDMet62Met7['_ViaMet62Met7NumberOfCOY'] = 1
					_ViaVDDMet62Met7['_ViaMet62Met7NumberOfCOX'] = int((self._DesignParameter['_Met6LayerVDD']['_Width'] - _DRCObj._VIAxMinWidth) // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace)) + 1

				self._DesignParameter['_ViaMet62Met7OnVDD'] = self._SrefElementDeclaration(_DesignObj=ViaMet62Met7._ViaMet62Met7(_DesignParameter=None, _Name = 'ViaMet62Met7OnVDDIn{}'.format(_Name)))[0]
				self._DesignParameter['_ViaMet62Met7OnVDD']['_DesignObj']._CalculateViaMet62Met7DesignParameterMinimumEnclosureX(**_ViaVDDMet62Met7)

				tmp = []
				for i in range (0, len(self._DesignParameter['_Met6LayerVDD']['_XYCoordinates'])) :
					for j in range (0, len(self._DesignParameter['_Met7LayerVDD']['_XYCoordinates'])) :
						tmp.append([self._DesignParameter['_Met6LayerVDD']['_XYCoordinates'][i][0][0],
									self._DesignParameter['_Met7LayerVDD']['_XYCoordinates'][j][0][1]])

				self._DesignParameter['_ViaMet62Met7OnVDD']['_XYCoordinates'] = tmp

				del tmp


				_ViaVDDMet62Met72 = copy.deepcopy(ViaMet62Met7._ViaMet62Met7._ParametersForDesignCalculation)
				_ViaVDDMet62Met72['_ViaMet62Met7NumberOfCOX'] = int((self._DesignParameter['_Met6LayerVDD']['_Width'] - _DRCObj._VIAxMinWidth) // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace2)) + 1
				_ViaVDDMet62Met72['_ViaMet62Met7NumberOfCOY'] = int((self._DesignParameter['_Met7LayerVDD2']['_Width'] - _DRCObj._VIAxMinWidth - _DRCObj._MetalxMinEnclosureCO2 * 2) // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace2)) + 1

				if _ViaVDDMet62Met72['_ViaMet62Met7NumberOfCOX'] <= 1 :
					_ViaVDDMet62Met72['_ViaMet62Met7NumberOfCOX'] = 1
					_ViaVDDMet62Met72['_ViaMet62Met7NumberOfCOY'] = int((self._DesignParameter['_Met7LayerVDD2']['_Width'] - _DRCObj._VIAxMinWidth - _DRCObj._MetalxMinEnclosureCO2 * 2) // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace)) + 1

				if _ViaVDDMet62Met72['_ViaMet62Met7NumberOfCOY'] <= 1 :
					_ViaVDDMet62Met72['_ViaMet62Met7NumberOfCOY'] = 1
					_ViaVDDMet62Met72['_ViaMet62Met7NumberOfCOX'] = int((self._DesignParameter['_Met6LayerVDD']['_Width'] - _DRCObj._VIAxMinWidth) // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace)) + 1

				self._DesignParameter['_ViaMet62Met7OnVDD2'] = self._SrefElementDeclaration(_DesignObj=ViaMet62Met7._ViaMet62Met7(_DesignParameter=None, _Name = 'ViaMet62Met7OnVDD2In{}'.format(_Name)))[0]
				self._DesignParameter['_ViaMet62Met7OnVDD2']['_DesignObj']._CalculateViaMet62Met7DesignParameterMinimumEnclosureX(**_ViaVDDMet62Met72)

				tmp = []
				for i in range (0, len(self._DesignParameter['_Met6LayerVDD']['_XYCoordinates'])) :
					for j in range (0, len(self._DesignParameter['_Met7LayerVDD2']['_XYCoordinates'])) :
						tmp.append([self._DesignParameter['_Met6LayerVDD']['_XYCoordinates'][i][0][0],
									self._DesignParameter['_Met7LayerVDD2']['_XYCoordinates'][j][0][1]])

				self._DesignParameter['_ViaMet62Met7OnVDD2']['_XYCoordinates'] = tmp

				del tmp

			else : ## for case where X_axis resistor number under 3, didn't consider input line

				self._DesignParameter['_Met5LayerVDD'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL5'][0], _Datatype=DesignParameters._LayerMapping['METAL5'][1], _XYCoordinates=[], _Width=100)
				self._DesignParameter['_Met5LayerVDD']['_Width'] = self._DesignParameter['_Met5LayerVCM']['_Width']

				tmp = []
				if (_YRBNum != 1) :
					for i in range (0, _YRBNum) :
						if i % 4 == 3 :
							tmp.append([[_ResistorBankOrigin[0][0] + _GapbtwOriginX + self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_TotalSubringRB']['_DesignObj']._DesignParameter['_Met1Layery']['_XWidth'] // 2 -
								self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_TotalSubringRB']['_DesignObj']._DesignParameter['_Met1Layery']['_XWidth'] * 2
								- _DRCObj._MetalxMinSpace11 * (3 - _XRBNum) - self._DesignParameter['_Met6LayerVCM']['_Width'] * (3 - _XRBNum),
								self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_ViaMet22Met3OnRes']['_XYCoordinates'][0][1] + self._DesignParameter['_Met5LayerVCM']['_Width'] // 2 + i * _ResistorSpaceY],
								[_ResistorBankOrigin[0][0] + _GapbtwOriginX  + _XRBNum * _ResistorSpaceX - self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_TotalSubringRB']['_DesignObj']._DesignParameter['_Met1Layery']['_XWidth'] // 2 +
								self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_TotalSubringRB']['_DesignObj']._DesignParameter['_Met1Layery']['_XWidth'] * 2,
								self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_ViaMet22Met3OnRes']['_XYCoordinates'][0][1] + self._DesignParameter['_Met5LayerVCM']['_Width'] // 2 + i * _ResistorSpaceY]])

				else :
					tmp.append([[_ResistorBankOrigin[0][0] + _GapbtwOriginX + self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_TotalSubringRB']['_DesignObj']._DesignParameter['_Met1Layery']['_XWidth'] // 2 -
								self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_TotalSubringRB']['_DesignObj']._DesignParameter['_Met1Layery']['_XWidth'] * 2
								- _DRCObj._MetalxMinSpace11 * (3 - _XRBNum) - self._DesignParameter['_Met6LayerVCM']['_Width'] * (3 - _XRBNum),
								self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_ViaMet22Met3OnRes']['_XYCoordinates'][0][1] + self._DesignParameter['_Met5LayerVCM']['_Width'] // 2],
								[_ResistorBankOrigin[0][0] + _GapbtwOriginX  + _XRBNum * _ResistorSpaceX - self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_TotalSubringRB']['_DesignObj']._DesignParameter['_Met1Layery']['_XWidth'] // 2 +
								self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_TotalSubringRB']['_DesignObj']._DesignParameter['_Met1Layery']['_XWidth'] * 2,
								self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_ViaMet22Met3OnRes']['_XYCoordinates'][0][1] + self._DesignParameter['_Met5LayerVCM']['_Width'] // 2]])


				self._DesignParameter['_Met5LayerVDD']['_XYCoordinates'] = tmp

				del tmp

				_ViaVDDMet42Met5 = copy.deepcopy(ViaMet42Met5._ViaMet42Met5._ParametersForDesignCalculation)
				_ViaVDDMet42Met5['_ViaMet42Met5NumberOfCOX'] = int((self._DesignParameter['_Met4LayerVDD']['_Width'] - _DRCObj._VIAxMinWidth) // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace2)) + 1
				_ViaVDDMet42Met5['_ViaMet42Met5NumberOfCOY'] = int((self._DesignParameter['_Met5LayerVDD']['_Width'] - _DRCObj._VIAxMinWidth - 2 * _DRCObj._MetalxMinEnclosureCO2) // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace2)) + 1
				if _ViaVDDMet42Met5['_ViaMet42Met5NumberOfCOX'] <= 1 :
					_ViaVDDMet42Met5['_ViaMet42Met5NumberOfCOX'] = 1
					_ViaVDDMet42Met5['_ViaMet42Met5NumberOfCOY'] = int((self._DesignParameter['_Met5LayerVDD']['_Width'] - _DRCObj._VIAxMinWidth - 2 * _DRCObj._MetalxMinEnclosureCO2) // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace)) + 1
				if _ViaVDDMet42Met5['_ViaMet42Met5NumberOfCOY'] <= 1 :
					_ViaVDDMet42Met5['_ViaMet42Met5NumberOfCOY'] = 1
					_ViaVDDMet42Met5['_ViaMet42Met5NumberOfCOX'] = int((self._DesignParameter['_Met4LayerVDD']['_Width'] - _DRCObj._VIAxMinWidth) // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace)) + 1

				self._DesignParameter['_ViaMet42Met5OnVDD'] = self._SrefElementDeclaration(_DesignObj=ViaMet42Met5._ViaMet42Met5(_DesignParameter=None, _Name = 'ViaMet42Met5OnVDDIn{}'.format(_Name)))[0]
				self._DesignParameter['_ViaMet42Met5OnVDD']['_DesignObj']._CalculateViaMet42Met5DesignParameterMinimumEnclosureX(**_ViaVDDMet42Met5)

				tmp = []
				for i in range (0, len(self._DesignParameter['_Met4LayerVDD']['_XYCoordinates'])) :
					for j in range (0, len(self._DesignParameter['_Met5LayerVDD']['_XYCoordinates'])) :
						tmp.append([self._DesignParameter['_Met4LayerVDD']['_XYCoordinates'][i][0][0],
									self._DesignParameter['_Met5LayerVDD']['_XYCoordinates'][j][0][1]])

				self._DesignParameter['_ViaMet42Met5OnVDD']['_XYCoordinates'] = tmp

				del tmp


				self._DesignParameter['_Met6LayerVDD'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL6'][0], _Datatype=DesignParameters._LayerMapping['METAL6'][1],_XYCoordinates=[], _Width=100)
				self._DesignParameter['_Met6LayerVDD']['_Width'] = self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_PMOSSubringRB']['_DesignObj']._DesignParameter['_Met1Layerx']['_XWidth'] -\
																self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_PMOSSubringRB']['_DesignObj']._DesignParameter['_Met1Layery']['_XWidth'] * 2

				tmp = []

				tmp.append([[_ResistorBankOrigin[0][0] + _GapbtwOriginX
					- _DRCObj._MetalxMinSpace11 - self._DesignParameter['_Met6LayerVCM']['_Width'] // 2,
					_ResistorBankOrigin[0][1] + _GapbtwOriginY],
					[_ResistorBankOrigin[0][0] + _GapbtwOriginX
					- _DRCObj._MetalxMinSpace11 - self._DesignParameter['_Met6LayerVCM']['_Width'] // 2,
					_ResistorBankOrigin[0][1] + _GapbtwOriginY + _YRBNum * _ResistorSpaceY]])

				self._DesignParameter['_Met6LayerVDD']['_XYCoordinates'] = tmp

				del tmp


				_ViaVDDMet52Met6 = copy.deepcopy(ViaMet52Met6._ViaMet52Met6._ParametersForDesignCalculation)
				_ViaVDDMet52Met6['_ViaMet52Met6NumberOfCOX'] = int((self._DesignParameter['_Met6LayerVDD']['_Width'] - _DRCObj._VIAxMinWidth) // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace2)) + 1
				_ViaVDDMet52Met6['_ViaMet52Met6NumberOfCOY'] = int((self._DesignParameter['_Met5LayerVDD']['_Width'] - _DRCObj._VIAxMinWidth - 2 * _DRCObj._MetalxMinEnclosureCO2) // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace2)) + 1
				if _ViaVDDMet52Met6['_ViaMet52Met6NumberOfCOX'] <= 1 :
					_ViaVDDMet52Met6['_ViaMet52Met6NumberOfCOX'] = 1
					_ViaVDDMet52Met6['_ViaMet52Met6NumberOfCOY'] = int((self._DesignParameter['_Met5LayerVDD']['_Width'] - _DRCObj._VIAxMinWidth - 2 * _DRCObj._MetalxMinEnclosureCO2) // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace)) + 1
				if _ViaVDDMet52Met6['_ViaMet52Met6NumberOfCOY'] <= 1 :
					_ViaVDDMet52Met6['_ViaMet52Met6NumberOfCOY'] = 1
					_ViaVDDMet52Met6['_ViaMet52Met6NumberOfCOX'] = int((self._DesignParameter['_Met6LayerVDD']['_Width'] - _DRCObj._VIAxMinWidth) // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace)) + 1

				self._DesignParameter['_ViaMet52Met6OnVDD'] = self._SrefElementDeclaration(_DesignObj=ViaMet52Met6._ViaMet52Met6(_DesignParameter=None, _Name = 'ViaMet52Met6OnVDDIn{}'.format(_Name)))[0]
				self._DesignParameter['_ViaMet52Met6OnVDD']['_DesignObj']._CalculateViaMet52Met6DesignParameterMinimumEnclosureX(**_ViaVDDMet52Met6)

				tmp = []
				for i in range (0, len(self._DesignParameter['_Met6LayerVDD']['_XYCoordinates'])) :
					for j in range (0, len(self._DesignParameter['_Met5LayerVDD']['_XYCoordinates'])) :
						tmp.append([self._DesignParameter['_Met6LayerVDD']['_XYCoordinates'][i][0][0],
									self._DesignParameter['_Met5LayerVDD']['_XYCoordinates'][j][0][1]])

				self._DesignParameter['_ViaMet52Met6OnVDD']['_XYCoordinates'] = tmp

				del tmp

				# self._DesignParameter['_Met7LayerVDD'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL7'][0], _Datatype=DesignParameters._LayerMapping['METAL7'][1], _XYCoordinates=[], _Width=100)
				# self._DesignParameter['_Met7LayerVDD']['_Width'] = _ResistorSpaceY // 2
				# self._DesignParameter['_Met7LayerVDD']['_XYCoordinates'] = [[[_ResistorBankOrigin[0][0] + _GapbtwOriginX,
				#                                                             _ResistorBankOrigin[0][1] + _GapbtwOriginY + _YRBNum * _ResistorSpaceY - self._DesignParameter['_Met7LayerVDD']['_Width'] // 2],
				#                                                             [_ResistorBankOrigin[0][0] + _GapbtwOriginX + _XRBNum * _ResistorSpaceX ,
				#                                                             _ResistorBankOrigin[0][1] + _GapbtwOriginY + _YRBNum * _ResistorSpaceY - self._DesignParameter['_Met7LayerVDD']['_Width'] // 2]]]

				self._DesignParameter['_Met7LayerVDD'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL7'][0], _Datatype=DesignParameters._LayerMapping['METAL7'][1], _XYCoordinates=[], _Width=100)
				self._DesignParameter['_Met7LayerVDD']['_Width'] = (_TopBotleft - _DRCObj._MetalxMinSpace11 * 2) // 2
				if self._DesignParameter['_Met7LayerVDD']['_Width'] % 2 == 1 :
					self._DesignParameter['_Met7LayerVDD']['_Width'] -= 1
				self._DesignParameter['_Met7LayerVDD']['_XYCoordinates'] = [[[_ResistorBankOrigin[0][0] + _GapbtwOriginX
																			 - _DRCObj._MetalxMinSpace11 * (3 - _XRBNum) - self._DesignParameter['_Met6LayerVCM']['_Width'] * (3 - _XRBNum),
																			_ResistorBankOrigin[0][1] + _GapbtwOriginY + _YRBNum * _ResistorSpaceY - self._DesignParameter['_Met7LayerVDD']['_Width'] // 2],
																			[_ResistorBankOrigin[0][0] + _GapbtwOriginX + _XRBNum * _ResistorSpaceX ,
																			_ResistorBankOrigin[0][1] + _GapbtwOriginY + _YRBNum * _ResistorSpaceY - self._DesignParameter['_Met7LayerVDD']['_Width'] // 2]],
																			[[_ResistorBankOrigin[0][0] + _GapbtwOriginX
																			 - _DRCObj._MetalxMinSpace11 * (3 - _XRBNum) - self._DesignParameter['_Met6LayerVCM']['_Width'] * (3 - _XRBNum),
																			_ResistorBankOrigin[0][1] + _GapbtwOriginY + self._DesignParameter['_Met7LayerVDD']['_Width'] * 1.5 + _DRCObj._MetalxMinSpace11 * 2],
																			[_ResistorBankOrigin[0][0] + _GapbtwOriginX + _XRBNum * _ResistorSpaceX,
																			_ResistorBankOrigin[0][1] + _GapbtwOriginY + self._DesignParameter['_Met7LayerVDD']['_Width'] * 1.5 + _DRCObj._MetalxMinSpace11 * 2]]]

				self._DesignParameter['_Met7LayerVDD2'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL7'][0], _Datatype=DesignParameters._LayerMapping['METAL7'][1], _XYCoordinates=[], _Width=100)
				self._DesignParameter['_Met7LayerVDD2']['_Width'] = (_SpacebtwVRX - _DRCObj._MetalxMinSpace11 * 3) // 2
				if self._DesignParameter['_Met7LayerVDD2']['_Width'] % 2 == 1 :
					self._DesignParameter['_Met7LayerVDD2']['_Width'] -= 1
				## VDD Power 빈도 조정
				tmp = []
				for i in range (0, len(self._DesignParameter['_Met7LayerVCM']['_XYCoordinates'])) :
					if i != len(self._DesignParameter['_Met7LayerVCM']['_XYCoordinates']) - 1 and i % 4 == 3 :
						tmp.append([[_ResistorBankOrigin[0][0] + _GapbtwOriginX
						 - _DRCObj._MetalxMinSpace11 * (3 - _XRBNum) - self._DesignParameter['_Met6LayerVCM']['_Width'] * (3 - _XRBNum),
							_ResistorBankOrigin[0][1] + self._DesignParameter['_Met7LayerVCM']['_XYCoordinates'][i][0][1] -
							self._DesignParameter['_Met7LayerVCM']['_Width'] // 2 - _DRCObj._MetalxMinSpace11 - self._DesignParameter['_Met7LayerVDD2']['_Width'] // 2],
							[_ResistorBankOrigin[0][0] + _GapbtwOriginX + _XRBNum * _ResistorSpaceX,
							_ResistorBankOrigin[0][1] + self._DesignParameter['_Met7LayerVCM']['_XYCoordinates'][i][0][1] -
							self._DesignParameter['_Met7LayerVCM']['_Width'] // 2 - _DRCObj._MetalxMinSpace11 - self._DesignParameter['_Met7LayerVDD2']['_Width'] // 2]])

				self._DesignParameter['_Met7LayerVDD2']['_XYCoordinates'] = tmp

				del tmp



				_ViaVDDMet62Met7 = copy.deepcopy(ViaMet62Met7._ViaMet62Met7._ParametersForDesignCalculation)
				_ViaVDDMet62Met7['_ViaMet62Met7NumberOfCOX'] = int((self._DesignParameter['_Met6LayerVDD']['_Width'] - _DRCObj._VIAxMinWidth) // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace2)) + 1
				_ViaVDDMet62Met7['_ViaMet62Met7NumberOfCOY'] = int((self._DesignParameter['_Met7LayerVDD']['_Width'] - _DRCObj._VIAxMinWidth - _DRCObj._MetalxMinEnclosureCO2 * 2) // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace2)) + 1

				if _ViaVDDMet62Met7['_ViaMet62Met7NumberOfCOX'] <= 1 :
					_ViaVDDMet62Met7['_ViaMet62Met7NumberOfCOX'] = 1
					_ViaVDDMet62Met7['_ViaMet62Met7NumberOfCOY'] = int((self._DesignParameter['_Met7LayerVDD']['_Width'] - _DRCObj._VIAxMinWidth - _DRCObj._MetalxMinEnclosureCO2 * 2) // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace)) + 1

				if _ViaVDDMet62Met7['_ViaMet62Met7NumberOfCOY'] <= 1 :
					_ViaVDDMet62Met7['_ViaMet62Met7NumberOfCOY'] = 1
					_ViaVDDMet62Met7['_ViaMet62Met7NumberOfCOX'] = int((self._DesignParameter['_Met6LayerVDD']['_Width'] - _DRCObj._VIAxMinWidth) // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace)) + 1

				self._DesignParameter['_ViaMet62Met7OnVDD'] = self._SrefElementDeclaration(_DesignObj=ViaMet62Met7._ViaMet62Met7(_DesignParameter=None, _Name = 'ViaMet62Met7OnVDDIn{}'.format(_Name)))[0]
				self._DesignParameter['_ViaMet62Met7OnVDD']['_DesignObj']._CalculateViaMet62Met7DesignParameterMinimumEnclosureX(**_ViaVDDMet62Met7)

				tmp = []
				for i in range (0, len(self._DesignParameter['_Met6LayerVDD']['_XYCoordinates'])) :
					for j in range (0, len(self._DesignParameter['_Met7LayerVDD']['_XYCoordinates'])) :
						tmp.append([self._DesignParameter['_Met6LayerVDD']['_XYCoordinates'][i][0][0],
									self._DesignParameter['_Met7LayerVDD']['_XYCoordinates'][j][0][1]])

				self._DesignParameter['_ViaMet62Met7OnVDD']['_XYCoordinates'] = tmp

				del tmp


				_ViaVDDMet62Met72 = copy.deepcopy(ViaMet62Met7._ViaMet62Met7._ParametersForDesignCalculation)
				_ViaVDDMet62Met72['_ViaMet62Met7NumberOfCOX'] = int((self._DesignParameter['_Met6LayerVDD']['_Width'] - _DRCObj._VIAxMinWidth) // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace2)) + 1
				_ViaVDDMet62Met72['_ViaMet62Met7NumberOfCOY'] = int((self._DesignParameter['_Met7LayerVDD2']['_Width'] - _DRCObj._VIAxMinWidth - _DRCObj._MetalxMinEnclosureCO2 * 2) // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace2)) + 1

				if _ViaVDDMet62Met72['_ViaMet62Met7NumberOfCOX'] <= 1 :
					_ViaVDDMet62Met72['_ViaMet62Met7NumberOfCOX'] = 1
					_ViaVDDMet62Met72['_ViaMet62Met7NumberOfCOY'] = int((self._DesignParameter['_Met7LayerVDD2']['_Width'] - _DRCObj._VIAxMinWidth - _DRCObj._MetalxMinEnclosureCO2 * 2) // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace)) + 1

				if _ViaVDDMet62Met72['_ViaMet62Met7NumberOfCOY'] <= 1 :
					_ViaVDDMet62Met72['_ViaMet62Met7NumberOfCOY'] = 1
					_ViaVDDMet62Met72['_ViaMet62Met7NumberOfCOX'] = int((self._DesignParameter['_Met6LayerVDD']['_Width'] - _DRCObj._VIAxMinWidth) // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace)) + 1

				self._DesignParameter['_ViaMet62Met7OnVDD2'] = self._SrefElementDeclaration(_DesignObj=ViaMet62Met7._ViaMet62Met7(_DesignParameter=None, _Name = 'ViaMet62Met7OnVDD2In{}'.format(_Name)))[0]
				self._DesignParameter['_ViaMet62Met7OnVDD2']['_DesignObj']._CalculateViaMet62Met7DesignParameterMinimumEnclosureX(**_ViaVDDMet62Met72)

				tmp = []
				for i in range (0, len(self._DesignParameter['_Met6LayerVDD']['_XYCoordinates'])) :
					for j in range (0, len(self._DesignParameter['_Met7LayerVDD2']['_XYCoordinates'])) :
						tmp.append([self._DesignParameter['_Met6LayerVDD']['_XYCoordinates'][i][0][0],
									self._DesignParameter['_Met7LayerVDD2']['_XYCoordinates'][j][0][1]])

				self._DesignParameter['_ViaMet62Met7OnVDD2']['_XYCoordinates'] = tmp

				del tmp








			self._DesignParameter['_Met2LayerVSS'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1],_XYCoordinates=[], _Width=100)
			self._DesignParameter['_Met2LayerVSS']['_Width'] = self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_TotalSubringRB']['_DesignObj']._DesignParameter['_Met1Layery']['_XWidth']

			tmp = []
			for i in range (0, _XRBNum + 1) :
				#if i % 2 == 0 :
				tmp.append([[_ResistorBankOrigin[0][0] + _GapbtwOriginX + i * _ResistorSpaceX, _ResistorBankOrigin[0][1] + _GapbtwOriginY - self._DesignParameter['_Met2LayerVSS']['_Width'] // 2],
								[_ResistorBankOrigin[0][0] + _GapbtwOriginX + i * _ResistorSpaceX, _ResistorBankOrigin[0][1] + _GapbtwOriginY + _YRBNum * _ResistorSpaceY + self._DesignParameter['_Met2LayerVSS']['_Width'] * 1.5]])

			self._DesignParameter['_Met2LayerVSS']['_XYCoordinates'] = tmp

			del tmp

			# [[[_ResistorBankOrigin[0][0] + _GapbtwOriginX - self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_TotalSubringRB']['_DesignObj']._DesignParameter['_Met1Layery']['_XWidth'] // 2,
			#                                                         _ResistorBankOrigin[0][1] + _GapbtwOriginY - self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_TotalSubringRB']['_DesignObj']._DesignParameter['_Met1Layery']['_XWidth'] // 2],
			#                                                         [_ResistorBankOrigin[0][0] + _GapbtwOriginX - self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_TotalSubringRB']['_DesignObj']._DesignParameter['_Met1Layery']['_XWidth'] // 2,
			#                                                         _ResistorBankOrigin[0][1] + _GapbtwOriginY + self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_TotalSubringRB']['_DesignObj']._DesignParameter['_Met1Layery']['_XWidth'] // 2 + _YRBNum * _ResistorSpaceY]],
			#                                                         [[_ResistorBankOrigin[0][0] + _GapbtwOriginX + self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_TotalSubringRB']['_DesignObj']._DesignParameter['_Met1Layery']['_XWidth'] // 2 + _XRBNum * _ResistorSpaceX,
			#                                                         _ResistorBankOrigin[0][1] + _GapbtwOriginY - self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_TotalSubringRB']['_DesignObj']._DesignParameter['_Met1Layery']['_XWidth'] // 2],
			#                                                         [_ResistorBankOrigin[0][0] + _GapbtwOriginX + self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_TotalSubringRB']['_DesignObj']._DesignParameter['_Met1Layery']['_XWidth'] // 2 + _XRBNum * _ResistorSpaceX,
			#                                                         _ResistorBankOrigin[0][1] + _GapbtwOriginY + self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_TotalSubringRB']['_DesignObj']._DesignParameter['_Met1Layery']['_XWidth'] // 2 + _YRBNum * _ResistorSpaceY]]]


			_ViaVSSMet12Met2 = copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation)
			_ViaVSSMet12Met2['_ViaMet12Met2NumberOfCOX'] = int((self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_TotalSubringRB']['_DesignObj']._DesignParameter['_Met1Layery']['_XWidth'] - _DRCObj._VIAxMinWidth) // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace2)) + 1
			_ViaVSSMet12Met2['_ViaMet12Met2NumberOfCOY'] = int((_ResistorSpaceY * _YRBNum - _DRCObj._VIAxMinWidth - _DRCObj._MetalxMinEnclosureCO2 * 2) // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace2)) + 1

			if _ViaVSSMet12Met2['_ViaMet12Met2NumberOfCOX'] <= 1 :
				_ViaVSSMet12Met2['_ViaMet12Met2NumberOfCOX'] = 1
				_ViaVSSMet12Met2['_ViaMet12Met2NumberOfCOY'] = int((_ResistorSpaceY * _YRBNum - _DRCObj._VIAxMinWidth - _DRCObj._MetalxMinEnclosureCO2 * 2) // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace)) + 1

			if _ViaVSSMet12Met2['_ViaMet12Met2NumberOfCOY'] <= 1 :
				_ViaVSSMet12Met2['_ViaMet12Met2NumberOfCOY'] = 1
				_ViaVSSMet12Met2['_ViaMet12Met2NumberOfCOX'] = int((self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_TotalSubringRB']['_DesignObj']._DesignParameter['_Met1Layery']['_XWidth'] - _DRCObj._VIAxMinWidth) // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace)) + 1


			self._DesignParameter['_ViaMet12Met2OnVSS'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_DesignParameter=None, _Name = 'ViaMet12Met2OnVSSIn{}'.format(_Name)))[0]
			self._DesignParameter['_ViaMet12Met2OnVSS']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(**_ViaVSSMet12Met2)

			tmp = []
			for i in range (0, len(self._DesignParameter['_Met2LayerVSS']['_XYCoordinates'])) :
					tmp.append([_ResistorBankOrigin[0][0] + _GapbtwOriginX + i * _ResistorSpaceX,
								_ResistorBankOrigin[0][1] + _GapbtwOriginY + self._DesignParameter['_ViaMet12Met2OnVSS']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // 2])
			self._DesignParameter['_ViaMet12Met2OnVSS']['_XYCoordinates'] = tmp

			del tmp



			self._DesignParameter['_Met3LayerVSS'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0], _Datatype=DesignParameters._LayerMapping['METAL3'][1],_XYCoordinates=[], _Width=100)
			self._DesignParameter['_Met3LayerVSS']['_Width'] = self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_TotalSubringRB']['_DesignObj']._DesignParameter['_Met1Layery']['_XWidth'] * 2

			tmp = []
			for i in range (0, _YRBNum + 1) :
				tmp.append([[_ResistorBankOrigin[0][0] + _GapbtwOriginX - self._DesignParameter['_Met2LayerVSS']['_Width'] // 2,
							_ResistorBankOrigin[0][1] + _GapbtwOriginY + i * _ResistorSpaceY + self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_TotalSubringRB']['_DesignObj']._DesignParameter['_Met1Layery']['_XWidth'] // 2],
							[_ResistorBankOrigin[0][0] + _GapbtwOriginX - self._DesignParameter['_Met2LayerVSS']['_Width'] // 2 + _XRBNum * _ResistorSpaceX + self._DesignParameter['_Met2LayerVSS']['_Width'],
							_ResistorBankOrigin[0][1] + _GapbtwOriginY + i * _ResistorSpaceY + self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_TotalSubringRB']['_DesignObj']._DesignParameter['_Met1Layery']['_XWidth'] // 2]])

			self._DesignParameter['_Met3LayerVSS']['_XYCoordinates'] = tmp

			del tmp

			_ViaVSSMet22Met3 = copy.deepcopy(ViaMet22Met3._ViaMet22Met3._ParametersForDesignCalculation)
			_ViaVSSMet22Met3['_ViaMet22Met3NumberOfCOX'] = int((self._DesignParameter['_Met2LayerVSS']['_Width'] - 2 * _DRCObj._MetalxMinEnclosureCO2 - _DRCObj._VIAxMinWidth)// (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace2)) + 1
			_ViaVSSMet22Met3['_ViaMet22Met3NumberOfCOY'] = int((self._DesignParameter['_Met3LayerVSS']['_Width'] - _DRCObj._VIAxMinWidth) // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace2)) + 1
			if _ViaVSSMet22Met3['_ViaMet22Met3NumberOfCOX'] <= 1 :
				_ViaVSSMet22Met3['_ViaMet22Met3NumberOfCOX'] = 1
				_ViaVSSMet22Met3['_ViaMet22Met3NumberOfCOY'] = int((self._DesignParameter['_Met3LayerVSS']['_Width'] - _DRCObj._VIAxMinWidth) // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace)) + 1
			if _ViaVSSMet22Met3['_ViaMet22Met3NumberOfCOY'] <= 1 :
				_ViaVSSMet22Met3['_ViaMet22Met3NumberOfCOY'] = 1
				_ViaVSSMet22Met3['_ViaMet22Met3NumberOfCOX'] = int((self._DesignParameter['_Met2LayerVSS']['_Width'] - 2 * _DRCObj._MetalxMinEnclosureCO2 - _DRCObj._VIAxMinWidth)// (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace)) + 1

			self._DesignParameter['_ViaMet22Met3OnVSS'] = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_DesignParameter=None, _Name = 'ViaMet22Met3OnVSSIn{}'.format(_Name)))[0]
			self._DesignParameter['_ViaMet22Met3OnVSS']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureY(**_ViaVSSMet22Met3)

			tmp = []
			for i in range (0, len(self._DesignParameter['_Met2LayerVSS']['_XYCoordinates'])) :
				for j in range (0, len(self._DesignParameter['_Met3LayerVSS']['_XYCoordinates'])) :
					tmp.append([self._DesignParameter['_Met2LayerVSS']['_XYCoordinates'][i][0][0],
								self._DesignParameter['_Met3LayerVSS']['_XYCoordinates'][j][0][1]])

			self._DesignParameter['_ViaMet22Met3OnVSS']['_XYCoordinates'] = tmp

			del tmp

			self._DesignParameter['_Met4LayerVSS'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL4'][0], _Datatype=DesignParameters._LayerMapping['METAL4'][1], _XYCoordinates=[], _Width=100)
			self._DesignParameter['_Met4LayerVSS']['_Width'] = self._DesignParameter['_Met2LayerVSS']['_Width'] * 2

			tmp = []
			for i in range (0, _XRBNum + 1) :
				if i % 2 == 0 :
					tmp.append([[_ResistorBankOrigin[0][0] + _GapbtwOriginX + self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_TotalSubringRB']['_DesignObj']._DesignParameter['_Met1Layery']['_XWidth'] // 2 + i * _ResistorSpaceX,
								_ResistorBankOrigin[0][1] + _GapbtwOriginY - self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_TotalSubringRB']['_DesignObj']._DesignParameter['_Met1Layery']['_XWidth'] // 2],
								[_ResistorBankOrigin[0][0] + _GapbtwOriginX + self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_TotalSubringRB']['_DesignObj']._DesignParameter['_Met1Layery']['_XWidth'] // 2 + i * _ResistorSpaceX,
								_ResistorBankOrigin[0][1] + _GapbtwOriginY + _YRBNum * _ResistorSpaceY + self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_TotalSubringRB']['_DesignObj']._DesignParameter['_Met1Layery']['_XWidth'] * 1.5]])

			self._DesignParameter['_Met4LayerVSS']['_XYCoordinates'] = tmp

			_ViaVSSMet32Met4 = copy.deepcopy(ViaMet32Met4._ViaMet32Met4._ParametersForDesignCalculation)
			_ViaVSSMet32Met4['_ViaMet32Met4NumberOfCOX'] = int((self._DesignParameter['_Met4LayerVSS']['_Width'] - _DRCObj._VIAxMinWidth - _DRCObj._MetalxMinEnclosureCO2 * 2) // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace2)) + 1
			_ViaVSSMet32Met4['_ViaMet32Met4NumberOfCOY'] = int((self._DesignParameter['_Met3LayerVSS']['_Width'] - _DRCObj._VIAxMinWidth) // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace2)) + 1

			if _ViaVSSMet32Met4['_ViaMet32Met4NumberOfCOX'] <= 1 :
				_ViaVSSMet32Met4['_ViaMet32Met4NumberOfCOX'] = 1
				_ViaVSSMet32Met4['_ViaMet32Met4NumberOfCOY'] = int((self._DesignParameter['_Met3LayerVSS']['_Width'] - _DRCObj._VIAxMinWidth) // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace)) + 1

			if _ViaVSSMet32Met4['_ViaMet32Met4NumberOfCOY'] <= 1 :
				_ViaVSSMet32Met4['_ViaMet32Met4NumberOfCOY'] = 1
				_ViaVSSMet32Met4['_ViaMet32Met4NumberOfCOX'] = int((self._DesignParameter['_Met4LayerVSS']['_Width'] - _DRCObj._VIAxMinWidth - _DRCObj._MetalxMinEnclosureCO2 * 2) // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace)) + 1

			self._DesignParameter['_ViaMet32Met4OnVSS'] = self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_DesignParameter=None, _Name = 'ViaMet32Met4OnVSSIn{}'.format(_Name)))[0]
			self._DesignParameter['_ViaMet32Met4OnVSS']['_DesignObj']._CalculateViaMet32Met4DesignParameterMinimumEnclosureY(**_ViaVSSMet32Met4)

			tmp = []
			for i in range (0, len(self._DesignParameter['_Met4LayerVSS']['_XYCoordinates'])) :
				for j in range (0, len(self._DesignParameter['_Met3LayerVSS']['_XYCoordinates'])) :
					tmp.append([self._DesignParameter['_Met4LayerVSS']['_XYCoordinates'][i][0][0],
								self._DesignParameter['_Met3LayerVSS']['_XYCoordinates'][j][0][1]])

			self._DesignParameter['_ViaMet32Met4OnVSS']['_XYCoordinates'] = tmp

			del tmp

			if self._DesignParameter['_ViaMet32Met4OnVSS']['_DesignObj']._DesignParameter['_Met4Layer']['_XWidth'] > self._DesignParameter['_Met4LayerVSS']['_Width'] :
				self._DesignParameter['_Met4LayerVSS']['_Width'] = self._DesignParameter['_ViaMet32Met4OnVSS']['_DesignObj']._DesignParameter['_Met4Layer']['_XWidth']


			if (_XRBNum >= 2) :
				self._DesignParameter['_Met5LayerVSS'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL5'][0], _Datatype=DesignParameters._LayerMapping['METAL5'][1], _XYCoordinates=[], _Width=100)
				self._DesignParameter['_Met5LayerVSS']['_Width'] = self._DesignParameter['_Met5LayerVCM']['_Width']


				tmp = []
				if (_YRBNum != 1) :
					for i in range (0, _YRBNum) :
						if i % 4 == 1 :
							tmp.append([[_ResistorBankOrigin[0][0] + _GapbtwOriginX + self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_TotalSubringRB']['_DesignObj']._DesignParameter['_Met1Layery']['_XWidth'] // 2 -
								self._DesignParameter['_Met4LayerVSS']['_Width'],
								self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_ViaMet22Met3OnRes']['_XYCoordinates'][0][1] + self._DesignParameter['_Met5LayerVCM']['_Width'] // 2 + i * _ResistorSpaceY],
								[_ResistorBankOrigin[0][0] + _GapbtwOriginX  + _XRBNum * _ResistorSpaceX - self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_TotalSubringRB']['_DesignObj']._DesignParameter['_Met1Layery']['_XWidth'] // 2 +
								self._DesignParameter['_Met4LayerVSS']['_Width'],
								self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_ViaMet22Met3OnRes']['_XYCoordinates'][0][1] + self._DesignParameter['_Met5LayerVCM']['_Width'] // 2 + i * _ResistorSpaceY]])

				else :
					tmp.append([[_ResistorBankOrigin[0][0] + _GapbtwOriginX + self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_TotalSubringRB']['_DesignObj']._DesignParameter['_Met1Layery']['_XWidth'] // 2 -
								self._DesignParameter['_Met4LayerVSS']['_Width']
								 - _DRCObj._MetalxMinSpace11 * (3 - _XRBNum) - self._DesignParameter['_Met6LayerVCM']['_Width'] * (3 - _XRBNum),
								self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_ViaMet22Met3OnRes']['_XYCoordinates'][0][1] + self._DesignParameter['_Met5LayerVCM']['_Width'] // 2],
								[_ResistorBankOrigin[0][0] + _GapbtwOriginX  + _XRBNum * _ResistorSpaceX - self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_TotalSubringRB']['_DesignObj']._DesignParameter['_Met1Layery']['_XWidth'] // 2 +
								self._DesignParameter['_Met4LayerVSS']['_Width'],
								self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_ViaMet22Met3OnRes']['_XYCoordinates'][0][1] + self._DesignParameter['_Met5LayerVCM']['_Width'] // 2]])


				self._DesignParameter['_Met5LayerVSS']['_XYCoordinates'] = tmp

				del tmp


				_ViaVSSMet42Met5 = copy.deepcopy(ViaMet42Met5._ViaMet42Met5._ParametersForDesignCalculation)
				_ViaVSSMet42Met5['_ViaMet42Met5NumberOfCOX'] = int((self._DesignParameter['_Met4LayerVSS']['_Width'] - _DRCObj._VIAxMinWidth) // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace2)) + 1
				_ViaVSSMet42Met5['_ViaMet42Met5NumberOfCOY'] = int((self._DesignParameter['_Met5LayerVSS']['_Width'] - _DRCObj._VIAxMinWidth - _DRCObj._MetalxMinEnclosureCO2 * 2) // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace2)) + 1

				if _ViaVSSMet42Met5['_ViaMet42Met5NumberOfCOX'] <= 1 :
					_ViaVSSMet42Met5['_ViaMet42Met5NumberOfCOX'] = 1
					_ViaVSSMet42Met5['_ViaMet42Met5NumberOfCOY'] = int((self._DesignParameter['_Met5LayerVSS']['_Width'] - _DRCObj._VIAxMinWidth - _DRCObj._MetalxMinEnclosureCO2 * 2) // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace)) + 1

				if _ViaVSSMet42Met5['_ViaMet42Met5NumberOfCOY'] <= 1 :
					_ViaVSSMet42Met5['_ViaMet42Met5NumberOfCOY'] = 1
					_ViaVSSMet42Met5['_ViaMet42Met5NumberOfCOX'] = int((self._DesignParameter['_Met4LayerVSS']['_Width'] - _DRCObj._VIAxMinWidth) // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace)) + 1

				self._DesignParameter['_ViaMet42Met5OnVSS'] = self._SrefElementDeclaration(_DesignObj=ViaMet42Met5._ViaMet42Met5(_DesignParameter=None, _Name = 'ViaMet42Met5OnVSSIn{}'.format(_Name)))[0]
				self._DesignParameter['_ViaMet42Met5OnVSS']['_DesignObj']._CalculateViaMet42Met5DesignParameterMinimumEnclosureX(**_ViaVSSMet42Met5)

				tmp = []
				for i in range (0, len(self._DesignParameter['_Met4LayerVSS']['_XYCoordinates'])) :
					for j in range (0, len(self._DesignParameter['_Met5LayerVSS']['_XYCoordinates'])) :
						tmp.append([self._DesignParameter['_Met4LayerVSS']['_XYCoordinates'][i][0][0],
									self._DesignParameter['_Met5LayerVSS']['_XYCoordinates'][j][0][1]])

				self._DesignParameter['_ViaMet42Met5OnVSS']['_XYCoordinates'] = tmp

				del tmp



				self._DesignParameter['_Met6LayerVSS'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL6'][0], _Datatype=DesignParameters._LayerMapping['METAL6'][1],_XYCoordinates=[], _Width=100)
				self._DesignParameter['_Met6LayerVSS']['_Width'] = self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_PMOSSubringRB']['_DesignObj']._DesignParameter['_Met1Layerx']['_XWidth'] -\
																self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_PMOSSubringRB']['_DesignObj']._DesignParameter['_Met1Layery']['_XWidth'] * 2

				tmp = []
				for i in range (0, _XRBNum) :
					if i % 4 == 1 :
						tmp.append([[_ResistorBankOrigin[0][0] + min(self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_PMOSSubringRB']['_XYCoordinates'][0][0],
								self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_ViaMet52Met6OnRes']['_XYCoordinates'][0][0] -
								self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_ViaMet52Met6OnRes']['_DesignObj']._DesignParameter['_Met6Layer']['_XWidth'] // 2 -
								_DRCObj._MetalxMinSpace11 - self._DesignParameter['_Met6LayerVCM']['_Width'] // 2) + i * _ResistorSpaceX,
								_ResistorBankOrigin[0][1] + _GapbtwOriginY],
								[_ResistorBankOrigin[0][0] + min(self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_PMOSSubringRB']['_XYCoordinates'][0][0],
								self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_ViaMet52Met6OnRes']['_XYCoordinates'][0][0] -
								self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_ViaMet52Met6OnRes']['_DesignObj']._DesignParameter['_Met6Layer']['_XWidth'] // 2 -
								_DRCObj._MetalxMinSpace11 - self._DesignParameter['_Met6LayerVCM']['_Width'] // 2) + i * _ResistorSpaceX,
								_ResistorBankOrigin[0][1] + _GapbtwOriginY + _YRBNum * _ResistorSpaceY]])

				self._DesignParameter['_Met6LayerVSS']['_XYCoordinates'] = tmp

				del tmp



				_ViaVSSMet52Met6 = copy.deepcopy(ViaMet52Met6._ViaMet52Met6._ParametersForDesignCalculation)
				_ViaVSSMet52Met6['_ViaMet52Met6NumberOfCOX'] = int((self._DesignParameter['_Met6LayerVSS']['_Width'] - _DRCObj._VIAxMinWidth) // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace2)) + 1
				_ViaVSSMet52Met6['_ViaMet52Met6NumberOfCOY'] = int((self._DesignParameter['_Met5LayerVSS']['_Width'] - _DRCObj._VIAxMinWidth - _DRCObj._MetalxMinEnclosureCO2 * 2) // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace2)) + 1
				if _ViaVSSMet52Met6['_ViaMet52Met6NumberOfCOX'] <= 1 :
					_ViaVSSMet52Met6['_ViaMet52Met6NumberOfCOX'] = 1
					_ViaVSSMet52Met6['_ViaMet52Met6NumberOfCOY'] = int((self._DesignParameter['_Met5LayerVSS']['_Width'] - _DRCObj._VIAxMinWidth - _DRCObj._MetalxMinEnclosureCO2 * 2) // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace)) + 1

				if _ViaVSSMet52Met6['_ViaMet52Met6NumberOfCOY'] <= 1 :
					_ViaVSSMet52Met6['_ViaMet52Met6NumberOfCOY'] = 1
					_ViaVSSMet52Met6['_ViaMet52Met6NumberOfCOX'] = int((self._DesignParameter['_Met6LayerVSS']['_Width'] - _DRCObj._VIAxMinWidth) // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace)) + 1

				self._DesignParameter['_ViaMet52Met6OnVSS'] = self._SrefElementDeclaration(_DesignObj=ViaMet52Met6._ViaMet52Met6(_DesignParameter=None, _Name = 'ViaMet52Met6OnVSSIn{}'.format(_Name)))[0]
				self._DesignParameter['_ViaMet52Met6OnVSS']['_DesignObj']._CalculateViaMet52Met6DesignParameterMinimumEnclosureX(**_ViaVSSMet52Met6)

				tmp = []
				for i in range (0, len(self._DesignParameter['_Met6LayerVSS']['_XYCoordinates'])) :
					for j in range (0, len(self._DesignParameter['_Met5LayerVSS']['_XYCoordinates'])) :
						tmp.append([self._DesignParameter['_Met6LayerVSS']['_XYCoordinates'][i][0][0],
									self._DesignParameter['_Met5LayerVSS']['_XYCoordinates'][j][0][1]])

				self._DesignParameter['_ViaMet52Met6OnVSS']['_XYCoordinates'] = tmp

				del tmp


				# self._DesignParameter['_Met7LayerVSS'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL7'][0], _Datatype=DesignParameters._LayerMapping['METAL7'][1], _XYCoordinates=[], _Width=100)
				# self._DesignParameter['_Met7LayerVSS']['_Width'] = _ResistorSpaceY// 2
				# self._DesignParameter['_Met7LayerVSS']['_XYCoordinates'] = [[[_ResistorBankOrigin[0][0] + _GapbtwOriginX,
				#                                                             _ResistorBankOrigin[0][1] + _GapbtwOriginY + self._DesignParameter['_Met7LayerVSS']['_Width'] // 2],
				#                                                             [_ResistorBankOrigin[0][0] + _GapbtwOriginX + _XRBNum * _ResistorSpaceX ,
				#                                                             _ResistorBankOrigin[0][1] + _GapbtwOriginY + self._DesignParameter['_Met7LayerVSS']['_Width'] // 2]]]

				self._DesignParameter['_Met7LayerVSS'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL7'][0], _Datatype=DesignParameters._LayerMapping['METAL7'][1], _XYCoordinates=[], _Width=100)
				self._DesignParameter['_Met7LayerVSS']['_Width'] = (_TopBotleft - _DRCObj._MetalxMinSpace11 * 2) // 2
				if self._DesignParameter['_Met7LayerVSS']['_Width'] % 2 == 1 :
					self._DesignParameter['_Met7LayerVSS']['_Width'] -= 1
				self._DesignParameter['_Met7LayerVSS']['_XYCoordinates'] = [[[_ResistorBankOrigin[0][0] + _GapbtwOriginX,
																			_ResistorBankOrigin[0][1] + _GapbtwOriginY + self._DesignParameter['_Met7LayerVSS']['_Width'] // 2],
																			[_ResistorBankOrigin[0][0] + _GapbtwOriginX + _XRBNum * _ResistorSpaceX ,
																			_ResistorBankOrigin[0][1] + _GapbtwOriginY + self._DesignParameter['_Met7LayerVSS']['_Width'] // 2]],
																			[[_ResistorBankOrigin[0][0] + _GapbtwOriginX,
																			_ResistorBankOrigin[0][1] + _GapbtwOriginY + _YRBNum * _ResistorSpaceY - self._DesignParameter['_Met7LayerVSS']['_Width'] * 1.5 - _DRCObj._MetalxMinSpace11 * 2],
																			[_ResistorBankOrigin[0][0] + _GapbtwOriginX + _XRBNum * _ResistorSpaceX,
																			_ResistorBankOrigin[0][1] + _GapbtwOriginY + _YRBNum * _ResistorSpaceY - self._DesignParameter['_Met7LayerVSS']['_Width'] * 1.5 - _DRCObj._MetalxMinSpace11 * 2]]]


				self._DesignParameter['_Met7LayerVSS2'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL7'][0], _Datatype=DesignParameters._LayerMapping['METAL7'][1], _XYCoordinates=[], _Width=100)
				self._DesignParameter['_Met7LayerVSS2']['_Width'] = (_SpacebtwVRX - _DRCObj._MetalxMinSpace11 * 3) // 2
				if self._DesignParameter['_Met7LayerVSS2']['_Width'] % 2 == 1 :
					self._DesignParameter['_Met7LayerVSS2']['_Width'] -= 1
				## VDD Power 빈도 조정
				tmp = []
				for i in range (0, len(self._DesignParameter['_Met7LayerVCM']['_XYCoordinates'])) :
					if i != len(self._DesignParameter['_Met7LayerVCM']['_XYCoordinates']) - 1 and i % 4 == 3 :
						tmp.append([[_ResistorBankOrigin[0][0] + _GapbtwOriginX,
							_ResistorBankOrigin[0][1] + self._DesignParameter['_Met7LayerVCM']['_XYCoordinates'][i][0][1] -
							self._DesignParameter['_Met7LayerVCM']['_Width'] // 2 - _DRCObj._MetalxMinSpace11 * 2 - self._DesignParameter['_Met7LayerVSS2']['_Width'] * 1.5],
							[_ResistorBankOrigin[0][0] + _GapbtwOriginX + _XRBNum * _ResistorSpaceX,
							_ResistorBankOrigin[0][1] + self._DesignParameter['_Met7LayerVCM']['_XYCoordinates'][i][0][1] -
							self._DesignParameter['_Met7LayerVCM']['_Width'] // 2 - _DRCObj._MetalxMinSpace11 * 2 - self._DesignParameter['_Met7LayerVSS2']['_Width'] * 1.5]])

				self._DesignParameter['_Met7LayerVSS2']['_XYCoordinates'] = tmp

				del tmp

				_ViaVSSMet62Met7 = copy.deepcopy(ViaMet62Met7._ViaMet62Met7._ParametersForDesignCalculation)
				_ViaVSSMet62Met7['_ViaMet62Met7NumberOfCOX'] = int((self._DesignParameter['_Met6LayerVSS']['_Width'] - _DRCObj._VIAxMinWidth) // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace2)) + 1
				_ViaVSSMet62Met7['_ViaMet62Met7NumberOfCOY'] = int((self._DesignParameter['_Met7LayerVSS']['_Width'] - _DRCObj._VIAxMinWidth - _DRCObj._MetalxMinEnclosureCO2 * 2) // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace2)) + 1

				if _ViaVSSMet62Met7['_ViaMet62Met7NumberOfCOX'] <= 1 :
					_ViaVSSMet62Met7['_ViaMet62Met7NumberOfCOX'] = 1
					_ViaVSSMet62Met7['_ViaMet62Met7NumberOfCOY'] = int((self._DesignParameter['_Met7LayerVSS']['_Width'] - _DRCObj._VIAxMinWidth - _DRCObj._MetalxMinEnclosureCO2 * 2) // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace)) + 1

				if _ViaVSSMet62Met7['_ViaMet62Met7NumberOfCOY'] <= 1 :
					_ViaVSSMet62Met7['_ViaMet62Met7NumberOfCOY'] = 1
					_ViaVSSMet62Met7['_ViaMet62Met7NumberOfCOX'] = int((self._DesignParameter['_Met6LayerVSS']['_Width'] - _DRCObj._VIAxMinWidth) // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace)) + 1

				self._DesignParameter['_ViaMet62Met7OnVSS'] = self._SrefElementDeclaration(_DesignObj=ViaMet62Met7._ViaMet62Met7(_DesignParameter=None, _Name = 'ViaMet62Met7OnVSSIn{}'.format(_Name)))[0]
				self._DesignParameter['_ViaMet62Met7OnVSS']['_DesignObj']._CalculateViaMet62Met7DesignParameterMinimumEnclosureX(**_ViaVSSMet62Met7)

				tmp = []
				for i in range (0, len(self._DesignParameter['_Met6LayerVSS']['_XYCoordinates'])) :
					for j in range (0, len(self._DesignParameter['_Met7LayerVSS']['_XYCoordinates'])) :
						tmp.append([self._DesignParameter['_Met6LayerVSS']['_XYCoordinates'][i][0][0],
									self._DesignParameter['_Met7LayerVSS']['_XYCoordinates'][j][0][1]])

				self._DesignParameter['_ViaMet62Met7OnVSS']['_XYCoordinates'] = tmp

				del tmp


				_ViaVSSMet62Met72 = copy.deepcopy(ViaMet62Met7._ViaMet62Met7._ParametersForDesignCalculation)
				_ViaVSSMet62Met72['_ViaMet62Met7NumberOfCOX'] = int((self._DesignParameter['_Met6LayerVSS']['_Width'] - _DRCObj._VIAxMinWidth) // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace2)) + 1
				_ViaVSSMet62Met72['_ViaMet62Met7NumberOfCOY'] = int((self._DesignParameter['_Met7LayerVSS2']['_Width'] - _DRCObj._VIAxMinWidth - _DRCObj._MetalxMinEnclosureCO2 * 2) // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace2)) + 1

				if _ViaVSSMet62Met72['_ViaMet62Met7NumberOfCOX'] <= 1 :
					_ViaVSSMet62Met72['_ViaMet62Met7NumberOfCOX'] = 1
					_ViaVSSMet62Met72['_ViaMet62Met7NumberOfCOY'] = int((self._DesignParameter['_Met7LayerVSS2']['_Width'] - _DRCObj._VIAxMinWidth - _DRCObj._MetalxMinEnclosureCO2 * 2) // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace)) + 1

				if _ViaVSSMet62Met72['_ViaMet62Met7NumberOfCOY'] <= 1 :
					_ViaVSSMet62Met72['_ViaMet62Met7NumberOfCOY'] = 1
					_ViaVSSMet62Met72['_ViaMet62Met7NumberOfCOX'] = int((self._DesignParameter['_Met6LayerVSS']['_Width'] - _DRCObj._VIAxMinWidth) // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace)) + 1

				self._DesignParameter['_ViaMet62Met7OnVSS2'] = self._SrefElementDeclaration(_DesignObj=ViaMet62Met7._ViaMet62Met7(_DesignParameter=None, _Name = 'ViaMet62Met7OnVSS2In{}'.format(_Name)))[0]
				self._DesignParameter['_ViaMet62Met7OnVSS2']['_DesignObj']._CalculateViaMet62Met7DesignParameterMinimumEnclosureX(**_ViaVSSMet62Met72)

				tmp = []
				for i in range (0, len(self._DesignParameter['_Met6LayerVSS']['_XYCoordinates'])) :
					for j in range (0, len(self._DesignParameter['_Met7LayerVSS2']['_XYCoordinates'])) :
						tmp.append([self._DesignParameter['_Met6LayerVSS']['_XYCoordinates'][i][0][0],
									self._DesignParameter['_Met7LayerVSS2']['_XYCoordinates'][j][0][1]])

				self._DesignParameter['_ViaMet62Met7OnVSS2']['_XYCoordinates'] = tmp

				del tmp

			else :
				self._DesignParameter['_Met5LayerVSS'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL5'][0], _Datatype=DesignParameters._LayerMapping['METAL5'][1], _XYCoordinates=[], _Width=100)
				self._DesignParameter['_Met5LayerVSS']['_Width'] = self._DesignParameter['_Met5LayerVCM']['_Width']


				tmp = []
				if (_YRBNum != 1) :
					for i in range (0, _YRBNum) :
						if i % 4 == 1 :
							tmp.append([[_ResistorBankOrigin[0][0] + _GapbtwOriginX + self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_TotalSubringRB']['_DesignObj']._DesignParameter['_Met1Layery']['_XWidth'] // 2 -
								self._DesignParameter['_Met4LayerVSS']['_Width']
								 - _DRCObj._MetalxMinSpace11 * (3 - _XRBNum) - self._DesignParameter['_Met6LayerVCM']['_Width'] * (3 - _XRBNum),
								self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_ViaMet22Met3OnRes']['_XYCoordinates'][0][1] + self._DesignParameter['_Met5LayerVCM']['_Width'] // 2 + i * _ResistorSpaceY],
								[_ResistorBankOrigin[0][0] + _GapbtwOriginX  + _XRBNum * _ResistorSpaceX - self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_TotalSubringRB']['_DesignObj']._DesignParameter['_Met1Layery']['_XWidth'] // 2 +
								self._DesignParameter['_Met4LayerVSS']['_Width'],
								self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_ViaMet22Met3OnRes']['_XYCoordinates'][0][1] + self._DesignParameter['_Met5LayerVCM']['_Width'] // 2 + i * _ResistorSpaceY]])

				else :
					tmp.append([[_ResistorBankOrigin[0][0] + _GapbtwOriginX + self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_TotalSubringRB']['_DesignObj']._DesignParameter['_Met1Layery']['_XWidth'] // 2 -
								self._DesignParameter['_Met4LayerVSS']['_Width']
								 - _DRCObj._MetalxMinSpace11 * (3 - _XRBNum) - self._DesignParameter['_Met6LayerVCM']['_Width'] * (3 - _XRBNum),
								self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_ViaMet22Met3OnRes']['_XYCoordinates'][0][1] + self._DesignParameter['_Met5LayerVCM']['_Width'] // 2],
								[_ResistorBankOrigin[0][0] + _GapbtwOriginX  + _XRBNum * _ResistorSpaceX - self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_TotalSubringRB']['_DesignObj']._DesignParameter['_Met1Layery']['_XWidth'] // 2 +
								self._DesignParameter['_Met4LayerVSS']['_Width'],
								self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_ViaMet22Met3OnRes']['_XYCoordinates'][0][1] + self._DesignParameter['_Met5LayerVCM']['_Width'] // 2]])

				self._DesignParameter['_Met5LayerVSS']['_XYCoordinates'] = tmp

				del tmp


				_ViaVSSMet42Met5 = copy.deepcopy(ViaMet42Met5._ViaMet42Met5._ParametersForDesignCalculation)
				_ViaVSSMet42Met5['_ViaMet42Met5NumberOfCOX'] = int((self._DesignParameter['_Met4LayerVSS']['_Width'] - _DRCObj._VIAxMinWidth) // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace2)) + 1
				_ViaVSSMet42Met5['_ViaMet42Met5NumberOfCOY'] = int((self._DesignParameter['_Met5LayerVSS']['_Width'] - _DRCObj._VIAxMinWidth - _DRCObj._MetalxMinEnclosureCO2 * 2) // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace2)) + 1

				if _ViaVSSMet42Met5['_ViaMet42Met5NumberOfCOX'] <= 1 :
					_ViaVSSMet42Met5['_ViaMet42Met5NumberOfCOX'] = 1
					_ViaVSSMet42Met5['_ViaMet42Met5NumberOfCOY'] = int((self._DesignParameter['_Met5LayerVSS']['_Width'] - _DRCObj._VIAxMinWidth - _DRCObj._MetalxMinEnclosureCO2 * 2) // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace)) + 1

				if _ViaVSSMet42Met5['_ViaMet42Met5NumberOfCOY'] <= 1 :
					_ViaVSSMet42Met5['_ViaMet42Met5NumberOfCOY'] = 1
					_ViaVSSMet42Met5['_ViaMet42Met5NumberOfCOX'] = int((self._DesignParameter['_Met4LayerVSS']['_Width'] - _DRCObj._VIAxMinWidth) // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace)) + 1

				self._DesignParameter['_ViaMet42Met5OnVSS'] = self._SrefElementDeclaration(_DesignObj=ViaMet42Met5._ViaMet42Met5(_DesignParameter=None, _Name = 'ViaMet42Met5OnVSSIn{}'.format(_Name)))[0]
				self._DesignParameter['_ViaMet42Met5OnVSS']['_DesignObj']._CalculateViaMet42Met5DesignParameterMinimumEnclosureX(**_ViaVSSMet42Met5)

				tmp = []
				for i in range (0, len(self._DesignParameter['_Met4LayerVSS']['_XYCoordinates'])) :
					for j in range (0, len(self._DesignParameter['_Met5LayerVSS']['_XYCoordinates'])) :
						tmp.append([self._DesignParameter['_Met4LayerVSS']['_XYCoordinates'][i][0][0],
									self._DesignParameter['_Met5LayerVSS']['_XYCoordinates'][j][0][1]])

				self._DesignParameter['_ViaMet42Met5OnVSS']['_XYCoordinates'] = tmp

				del tmp



				self._DesignParameter['_Met6LayerVSS'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL6'][0], _Datatype=DesignParameters._LayerMapping['METAL6'][1],_XYCoordinates=[], _Width=100)
				self._DesignParameter['_Met6LayerVSS']['_Width'] = self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_PMOSSubringRB']['_DesignObj']._DesignParameter['_Met1Layerx']['_XWidth'] -\
																self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_PMOSSubringRB']['_DesignObj']._DesignParameter['_Met1Layery']['_XWidth'] * 2

				tmp = []

				tmp.append([[_ResistorBankOrigin[0][0] + _GapbtwOriginX
					- _DRCObj._MetalxMinSpace11 * 2 - self._DesignParameter['_Met6LayerVCM']['_Width'] * 1.5,
					_ResistorBankOrigin[0][1] + _GapbtwOriginY],
					[_ResistorBankOrigin[0][0] + _GapbtwOriginX
					- _DRCObj._MetalxMinSpace11 * 2 - self._DesignParameter['_Met6LayerVCM']['_Width'] * 1.5,
					_ResistorBankOrigin[0][1] + _GapbtwOriginY + _YRBNum * _ResistorSpaceY]])

				self._DesignParameter['_Met6LayerVSS']['_XYCoordinates'] = tmp

				del tmp



				_ViaVSSMet52Met6 = copy.deepcopy(ViaMet52Met6._ViaMet52Met6._ParametersForDesignCalculation)
				_ViaVSSMet52Met6['_ViaMet52Met6NumberOfCOX'] = int((self._DesignParameter['_Met6LayerVSS']['_Width'] - _DRCObj._VIAxMinWidth) // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace2)) + 1
				_ViaVSSMet52Met6['_ViaMet52Met6NumberOfCOY'] = int((self._DesignParameter['_Met5LayerVSS']['_Width'] - _DRCObj._VIAxMinWidth - _DRCObj._MetalxMinEnclosureCO2 * 2) // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace2)) + 1
				if _ViaVSSMet52Met6['_ViaMet52Met6NumberOfCOX'] <= 1 :
					_ViaVSSMet52Met6['_ViaMet52Met6NumberOfCOX'] = 1
					_ViaVSSMet52Met6['_ViaMet52Met6NumberOfCOY'] = int((self._DesignParameter['_Met5LayerVSS']['_Width'] - _DRCObj._VIAxMinWidth - _DRCObj._MetalxMinEnclosureCO2 * 2) // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace)) + 1

				if _ViaVSSMet52Met6['_ViaMet52Met6NumberOfCOY'] <= 1 :
					_ViaVSSMet52Met6['_ViaMet52Met6NumberOfCOY'] = 1
					_ViaVSSMet52Met6['_ViaMet52Met6NumberOfCOX'] = int((self._DesignParameter['_Met6LayerVSS']['_Width'] - _DRCObj._VIAxMinWidth) // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace)) + 1

				self._DesignParameter['_ViaMet52Met6OnVSS'] = self._SrefElementDeclaration(_DesignObj=ViaMet52Met6._ViaMet52Met6(_DesignParameter=None, _Name = 'ViaMet52Met6OnVSSIn{}'.format(_Name)))[0]
				self._DesignParameter['_ViaMet52Met6OnVSS']['_DesignObj']._CalculateViaMet52Met6DesignParameterMinimumEnclosureX(**_ViaVSSMet52Met6)

				tmp = []
				for i in range (0, len(self._DesignParameter['_Met6LayerVSS']['_XYCoordinates'])) :
					for j in range (0, len(self._DesignParameter['_Met5LayerVSS']['_XYCoordinates'])) :
						tmp.append([self._DesignParameter['_Met6LayerVSS']['_XYCoordinates'][i][0][0],
									self._DesignParameter['_Met5LayerVSS']['_XYCoordinates'][j][0][1]])

				self._DesignParameter['_ViaMet52Met6OnVSS']['_XYCoordinates'] = tmp

				del tmp


				# self._DesignParameter['_Met7LayerVSS'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL7'][0], _Datatype=DesignParameters._LayerMapping['METAL7'][1], _XYCoordinates=[], _Width=100)
				# self._DesignParameter['_Met7LayerVSS']['_Width'] = _ResistorSpaceY// 2
				# self._DesignParameter['_Met7LayerVSS']['_XYCoordinates'] = [[[_ResistorBankOrigin[0][0] + _GapbtwOriginX,
				#                                                             _ResistorBankOrigin[0][1] + _GapbtwOriginY + self._DesignParameter['_Met7LayerVSS']['_Width'] // 2],
				#                                                             [_ResistorBankOrigin[0][0] + _GapbtwOriginX + _XRBNum * _ResistorSpaceX ,
				#                                                             _ResistorBankOrigin[0][1] + _GapbtwOriginY + self._DesignParameter['_Met7LayerVSS']['_Width'] // 2]]]

				self._DesignParameter['_Met7LayerVSS'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL7'][0], _Datatype=DesignParameters._LayerMapping['METAL7'][1], _XYCoordinates=[], _Width=100)
				self._DesignParameter['_Met7LayerVSS']['_Width'] = (_TopBotleft - _DRCObj._MetalxMinSpace11 * 2) // 2
				if self._DesignParameter['_Met7LayerVSS']['_Width'] % 2 == 1 :
					self._DesignParameter['_Met7LayerVSS']['_Width'] -= 1
				self._DesignParameter['_Met7LayerVSS']['_XYCoordinates'] = [[[_ResistorBankOrigin[0][0] + _GapbtwOriginX
																			- _DRCObj._MetalxMinSpace11 * (3 - _XRBNum) - self._DesignParameter['_Met6LayerVCM']['_Width'] * (3 - _XRBNum),
																			_ResistorBankOrigin[0][1] + _GapbtwOriginY + self._DesignParameter['_Met7LayerVSS']['_Width'] // 2],
																			[_ResistorBankOrigin[0][0] + _GapbtwOriginX + _XRBNum * _ResistorSpaceX ,
																			_ResistorBankOrigin[0][1] + _GapbtwOriginY + self._DesignParameter['_Met7LayerVSS']['_Width'] // 2]],
																			[[_ResistorBankOrigin[0][0] + _GapbtwOriginX
																			- _DRCObj._MetalxMinSpace11 * (3 - _XRBNum) - self._DesignParameter['_Met6LayerVCM']['_Width'] * (3 - _XRBNum),
																			_ResistorBankOrigin[0][1] + _GapbtwOriginY + _YRBNum * _ResistorSpaceY - self._DesignParameter['_Met7LayerVSS']['_Width'] * 1.5 - _DRCObj._MetalxMinSpace11 * 2],
																			[_ResistorBankOrigin[0][0] + _GapbtwOriginX + _XRBNum * _ResistorSpaceX,
																			_ResistorBankOrigin[0][1] + _GapbtwOriginY + _YRBNum * _ResistorSpaceY - self._DesignParameter['_Met7LayerVSS']['_Width'] * 1.5 - _DRCObj._MetalxMinSpace11 * 2]]]


				self._DesignParameter['_Met7LayerVSS2'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL7'][0], _Datatype=DesignParameters._LayerMapping['METAL7'][1], _XYCoordinates=[], _Width=100)
				self._DesignParameter['_Met7LayerVSS2']['_Width'] = (_SpacebtwVRX - _DRCObj._MetalxMinSpace11 * 3) // 2
				if self._DesignParameter['_Met7LayerVSS2']['_Width'] % 2 == 1 :
					self._DesignParameter['_Met7LayerVSS2']['_Width'] -= 1
				tmp = []
				## VSS Power 빈도 조정
				for i in range (0, len(self._DesignParameter['_Met7LayerVCM']['_XYCoordinates'])) :
					if i != len(self._DesignParameter['_Met7LayerVCM']['_XYCoordinates']) - 1 and i % 4 == 3 :
						tmp.append([[_ResistorBankOrigin[0][0] + _GapbtwOriginX
							- _DRCObj._MetalxMinSpace11 * (3 - _XRBNum) - self._DesignParameter['_Met6LayerVCM']['_Width'] * (3 - _XRBNum),
							_ResistorBankOrigin[0][1] + self._DesignParameter['_Met7LayerVCM']['_XYCoordinates'][i][0][1] -
							self._DesignParameter['_Met7LayerVCM']['_Width'] // 2 - _DRCObj._MetalxMinSpace11 * 2 - self._DesignParameter['_Met7LayerVSS2']['_Width'] * 1.5],
							[_ResistorBankOrigin[0][0] + _GapbtwOriginX + _XRBNum * _ResistorSpaceX,
							_ResistorBankOrigin[0][1] + self._DesignParameter['_Met7LayerVCM']['_XYCoordinates'][i][0][1] -
							self._DesignParameter['_Met7LayerVCM']['_Width'] // 2 - _DRCObj._MetalxMinSpace11 * 2 - self._DesignParameter['_Met7LayerVSS2']['_Width'] * 1.5]])

				self._DesignParameter['_Met7LayerVSS2']['_XYCoordinates'] = tmp

				del tmp

				_ViaVSSMet62Met7 = copy.deepcopy(ViaMet62Met7._ViaMet62Met7._ParametersForDesignCalculation)
				_ViaVSSMet62Met7['_ViaMet62Met7NumberOfCOX'] = int((self._DesignParameter['_Met6LayerVSS']['_Width'] - _DRCObj._VIAxMinWidth) // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace2)) + 1
				_ViaVSSMet62Met7['_ViaMet62Met7NumberOfCOY'] = int((self._DesignParameter['_Met7LayerVSS']['_Width'] - _DRCObj._VIAxMinWidth - _DRCObj._MetalxMinEnclosureCO2 * 2) // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace2)) + 1

				if _ViaVSSMet62Met7['_ViaMet62Met7NumberOfCOX'] <= 1 :
					_ViaVSSMet62Met7['_ViaMet62Met7NumberOfCOX'] = 1
					_ViaVSSMet62Met7['_ViaMet62Met7NumberOfCOY'] = int((self._DesignParameter['_Met7LayerVSS']['_Width'] - _DRCObj._VIAxMinWidth - _DRCObj._MetalxMinEnclosureCO2 * 2) // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace)) + 1

				if _ViaVSSMet62Met7['_ViaMet62Met7NumberOfCOY'] <= 1 :
					_ViaVSSMet62Met7['_ViaMet62Met7NumberOfCOY'] = 1
					_ViaVSSMet62Met7['_ViaMet62Met7NumberOfCOX'] = int((self._DesignParameter['_Met6LayerVSS']['_Width'] - _DRCObj._VIAxMinWidth) // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace)) + 1

				self._DesignParameter['_ViaMet62Met7OnVSS'] = self._SrefElementDeclaration(_DesignObj=ViaMet62Met7._ViaMet62Met7(_DesignParameter=None, _Name = 'ViaMet62Met7OnVSSIn{}'.format(_Name)))[0]
				self._DesignParameter['_ViaMet62Met7OnVSS']['_DesignObj']._CalculateViaMet62Met7DesignParameterMinimumEnclosureX(**_ViaVSSMet62Met7)

				tmp = []
				for i in range (0, len(self._DesignParameter['_Met6LayerVSS']['_XYCoordinates'])) :
					for j in range (0, len(self._DesignParameter['_Met7LayerVSS']['_XYCoordinates'])) :
						tmp.append([self._DesignParameter['_Met6LayerVSS']['_XYCoordinates'][i][0][0],
									self._DesignParameter['_Met7LayerVSS']['_XYCoordinates'][j][0][1]])

				self._DesignParameter['_ViaMet62Met7OnVSS']['_XYCoordinates'] = tmp

				del tmp


				_ViaVSSMet62Met72 = copy.deepcopy(ViaMet62Met7._ViaMet62Met7._ParametersForDesignCalculation)
				_ViaVSSMet62Met72['_ViaMet62Met7NumberOfCOX'] = int((self._DesignParameter['_Met6LayerVSS']['_Width'] - _DRCObj._VIAxMinWidth) // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace2)) + 1
				_ViaVSSMet62Met72['_ViaMet62Met7NumberOfCOY'] = int((self._DesignParameter['_Met7LayerVSS2']['_Width'] - _DRCObj._VIAxMinWidth - _DRCObj._MetalxMinEnclosureCO2 * 2) // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace2)) + 1

				if _ViaVSSMet62Met72['_ViaMet62Met7NumberOfCOX'] <= 1 :
					_ViaVSSMet62Met72['_ViaMet62Met7NumberOfCOX'] = 1
					_ViaVSSMet62Met72['_ViaMet62Met7NumberOfCOY'] = int((self._DesignParameter['_Met7LayerVSS2']['_Width'] - _DRCObj._VIAxMinWidth - _DRCObj._MetalxMinEnclosureCO2 * 2) // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace)) + 1

				if _ViaVSSMet62Met72['_ViaMet62Met7NumberOfCOY'] <= 1 :
					_ViaVSSMet62Met72['_ViaMet62Met7NumberOfCOY'] = 1
					_ViaVSSMet62Met72['_ViaMet62Met7NumberOfCOX'] = int((self._DesignParameter['_Met6LayerVSS']['_Width'] - _DRCObj._VIAxMinWidth) // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace)) + 1

				self._DesignParameter['_ViaMet62Met7OnVSS2'] = self._SrefElementDeclaration(_DesignObj=ViaMet62Met7._ViaMet62Met7(_DesignParameter=None, _Name = 'ViaMet62Met7OnVSS2In{}'.format(_Name)))[0]
				self._DesignParameter['_ViaMet62Met7OnVSS2']['_DesignObj']._CalculateViaMet62Met7DesignParameterMinimumEnclosureX(**_ViaVSSMet62Met72)

				tmp = []
				for i in range (0, len(self._DesignParameter['_Met6LayerVSS']['_XYCoordinates'])) :
					for j in range (0, len(self._DesignParameter['_Met7LayerVSS2']['_XYCoordinates'])) :
						tmp.append([self._DesignParameter['_Met6LayerVSS']['_XYCoordinates'][i][0][0],
									self._DesignParameter['_Met7LayerVSS2']['_XYCoordinates'][j][0][1]])

				self._DesignParameter['_ViaMet62Met7OnVSS2']['_XYCoordinates'] = tmp

				del tmp





			# self._DesignParameter['_Met4LayerVSS2'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL4'][0], _Datatype=DesignParameters._LayerMapping['METAL4'][1],_XYCoordinates=[], _Width=100)
			# self._DesignParameter['_Met4LayerVSS2']['_Width'] = self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_Met4LayerVSS2']['_XWidth']

			# tmp = []
			# for i in range (0, _XRBNum) :
			#     tmp.append([[_ResistorBankOrigin[0][0] + self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_Met4LayerVSS2']['_XYCoordinates'][0][0] + i * _ResistorSpaceX,
			#                 _ResistorBankOrigin[0][1] - _ResistorSpaceY],
			#                 [_ResistorBankOrigin[0][0] + self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_Met4LayerVSS2']['_XYCoordinates'][0][0] + i * _ResistorSpaceX,
			#                 _ResistorBankOrigin[0][1] + _YRBNum * _ResistorSpaceY]])

			# self._DesignParameter['_Met4LayerVSS2']['_XYCoordinates'] = tmp

			# del tmp



		## TransmissionGate Pin Declaration
		if _InputLine == False :
			for i in range (0, _XRBNum) :
				for j in range (0, _YRBNum) :
					for k in range (0, 2) : ## for nmos 0 and pmos 1
						if k == 0 :
							self._DesignParameter['_S<{0}>pin'.format(i + _XRBNum * j)] = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL5PIN'][0], _Datatype=DesignParameters._LayerMapping['METAL5PIN'][1],
							_Presentation=[0,1,2], _Reflect=[0,0,0],
							_XYCoordinates=[[_ResistorBankOrigin[0][0] + self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_Met5LayerInput']['_XYCoordinates'][1][1][0] +
											i * _ResistorSpaceX,
											_ResistorBankOrigin[0][1] + self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_Met5LayerInput']['_XYCoordinates'][1][1][1] +
											j * _ResistorSpaceY]],
							_Mag = 0.5, _Angle=0, _TEXT='S<{0}>'.format(i + _XRBNum * j))

						else :
							self._DesignParameter['_SB<{0}>pin'.format(i + _XRBNum * j)] = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL5PIN'][0], _Datatype=DesignParameters._LayerMapping['METAL5PIN'][1],
							_Presentation=[0,1,2], _Reflect=[0,0,0],
							_XYCoordinates=[[_ResistorBankOrigin[0][0] + self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_Met5LayerInput']['_XYCoordinates'][0][1][0] +
											i * _ResistorSpaceX,
											_ResistorBankOrigin[0][1] + self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_Met5LayerInput']['_XYCoordinates'][0][1][1] +
											j * _ResistorSpaceY]],
							_Mag = 0.5, _Angle=0, _TEXT='SB<{0}>'.format(i + _XRBNum * j))

		if _InputLine == True :
			for i in range (0, _XRBNum) :
				for j in range (0, _YRBNum) :
					for k in range (0, 2) : ## for nmos 0 and pmos 1
						if k == 0 :
							self._DesignParameter['_S<{0}>'.format(i + _XRBNum * j)] = dict(_DesignParametertype = 7 ,
							_XYCoordinates=[[_ResistorBankOrigin[0][0] + self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_Met5LayerInput']['_XYCoordinates'][1][1][0] +
											i * _ResistorSpaceX,
											_ResistorBankOrigin[0][1] + self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_Met5LayerInput']['_XYCoordinates'][1][1][1] +
											j * _ResistorSpaceY]])

						else :
							self._DesignParameter['_SB<{0}>'.format(i + _XRBNum * j)] = dict(_DesignParametertype = 7,
							_XYCoordinates=[[_ResistorBankOrigin[0][0] + self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_Met5LayerInput']['_XYCoordinates'][0][1][0] +
											i * _ResistorSpaceX,
											_ResistorBankOrigin[0][1] + self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_Met5LayerInput']['_XYCoordinates'][0][1][1] +
											j * _ResistorSpaceY]])

		tmp = []
		for i in range (len(self._DesignParameter['_Met7LayerVRX']['_XYCoordinates'])) :
			tmp.append([(self._DesignParameter['_Met7LayerVRX']['_XYCoordinates'][i][1][0] - abs(self._DesignParameter['_Met7LayerVRX']['_XYCoordinates'][i][0][0])) // 2,
										self._DesignParameter['_Met7LayerVRX']['_XYCoordinates'][i][0][1]])


		self._DesignParameter['_VRXpin'] = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL7PIN'][0], _Datatype=DesignParameters._LayerMapping['METAL7PIN'][1],
						_Presentation=[0,1,2], _Reflect=[0,0,0],
						_XYCoordinates=tmp,
						_Mag = 0.5, _Angle=0, _TEXT='VRX')

		del tmp
		if _PowerLine == True :
			tmp = []
			for i in range (len(self._DesignParameter['_Met7LayerVDD']['_XYCoordinates'])) :
				tmp.append([(self._DesignParameter['_Met7LayerVDD']['_XYCoordinates'][i][1][0] -  abs(self._DesignParameter['_Met7LayerVDD']['_XYCoordinates'][i][0][0])) // 2,
											self._DesignParameter['_Met7LayerVDD']['_XYCoordinates'][i][0][1]])

			for i in range (len(self._DesignParameter['_Met7LayerVDD2']['_XYCoordinates'])) :
				tmp.append([(self._DesignParameter['_Met7LayerVDD2']['_XYCoordinates'][i][1][0] - abs(self._DesignParameter['_Met7LayerVDD2']['_XYCoordinates'][i][0][0])) // 2,
											self._DesignParameter['_Met7LayerVDD2']['_XYCoordinates'][i][0][1]])

			self._DesignParameter['_VDDpin'] = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL7PIN'][0], _Datatype=DesignParameters._LayerMapping['METAL7PIN'][1],
							_Presentation=[0,1,2], _Reflect=[0,0,0],
							_XYCoordinates=tmp,
							_Mag = 0.5, _Angle=0, _TEXT='VDD')

			del tmp

			tmp = []
			for i in range (len(self._DesignParameter['_Met7LayerVSS']['_XYCoordinates'])) :
				tmp.append([(self._DesignParameter['_Met7LayerVSS']['_XYCoordinates'][i][1][0] - abs(self._DesignParameter['_Met7LayerVSS']['_XYCoordinates'][i][0][0])) // 2,
											self._DesignParameter['_Met7LayerVSS']['_XYCoordinates'][i][0][1]])

			for i in range (len(self._DesignParameter['_Met7LayerVSS2']['_XYCoordinates'])) :
				tmp.append([(self._DesignParameter['_Met7LayerVSS2']['_XYCoordinates'][i][1][0] - abs(self._DesignParameter['_Met7LayerVSS2']['_XYCoordinates'][i][0][0])) // 2,
											self._DesignParameter['_Met7LayerVSS2']['_XYCoordinates'][i][0][1]])

			self._DesignParameter['_VSSpin'] = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL7PIN'][0], _Datatype=DesignParameters._LayerMapping['METAL7PIN'][1],
							_Presentation=[0,1,2], _Reflect=[0,0,0],
							_XYCoordinates=tmp,
							_Mag = 0.5, _Angle=0, _TEXT='VSS')

			del tmp

		else :
			tmp = []
			for i in range (0, _XRBNum) :
				for j in range (0, _YRBNum) :
					tmp.append([_ResistorBankOrigin[0][0] + self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_PMOSSubringRB']['_XYCoordinates'][0][0] + self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_PMOSSubringRB']['_DesignObj']._DesignParameter['_Met1Layerx']['_XYCoordinates'][0][0] +
											i * _ResistorSpaceX,
								_ResistorBankOrigin[0][1] + self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_PMOSSubringRB']['_XYCoordinates'][0][1] + self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_PMOSSubringRB']['_DesignObj']._DesignParameter['_Met1Layerx']['_XYCoordinates'][0][1] +
											j * _ResistorSpaceY])

			self._DesignParameter['_VDDpin'] = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1PIN'][0], _Datatype=DesignParameters._LayerMapping['METAL1PIN'][1],
							_Presentation=[0,1,2], _Reflect=[0,0,0],
							_XYCoordinates=tmp,
							_Mag = 0.5, _Angle=0, _TEXT='VDD')

			del tmp

			tmp = []
			for i in range (0, _XRBNum) :
				for j in range (0, _YRBNum) :
					tmp.append([_ResistorBankOrigin[0][0] + self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_NMOSSubringRB']['_XYCoordinates'][0][0] + self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_NMOSSubringRB']['_DesignObj']._DesignParameter['_Met1Layerx']['_XYCoordinates'][0][0] +
											i * _ResistorSpaceX,
								_ResistorBankOrigin[0][1] + self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_NMOSSubringRB']['_XYCoordinates'][0][1] + self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_NMOSSubringRB']['_DesignObj']._DesignParameter['_Met1Layerx']['_XYCoordinates'][0][1] +
											j * _ResistorSpaceY])

			self._DesignParameter['_VSSpin'] = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1PIN'][0], _Datatype=DesignParameters._LayerMapping['METAL1PIN'][1],
							_Presentation=[0,1,2], _Reflect=[0,0,0],
							_XYCoordinates=tmp,
							_Mag = 0.5, _Angle=0, _TEXT='VSS')

			del tmp

		tmp = []
		for i in range (len(self._DesignParameter['_Met7LayerVCM']['_XYCoordinates'])) :
			tmp.append([(self._DesignParameter['_Met7LayerVCM']['_XYCoordinates'][i][1][0] - abs(self._DesignParameter['_Met7LayerVCM']['_XYCoordinates'][i][0][0])) // 2,
										self._DesignParameter['_Met7LayerVCM']['_XYCoordinates'][i][0][1]])

		self._DesignParameter['_VCMpin'] = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL7PIN'][0], _Datatype=DesignParameters._LayerMapping['METAL7PIN'][1],
						_Presentation=[0,1,2], _Reflect=[0,0,0],
						_XYCoordinates=tmp,
						_Mag = 0.5, _Angle=0, _TEXT='VCM')

		del tmp



		##Path for inputs for other transmission gate and pin declaration


		if _InputLine == True :
			self._DesignParameter['_Met5LayerInput'] = self._PathElementDeclaration(
				_Layer = DesignParameters._LayerMapping['METAL5'][0], _Datatype=DesignParameters._LayerMapping['METAL5'][1],
				_XYCoordinates=[], _Width=100)

			self._DesignParameter['_Met5LayerInput']['_Width'] = self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSControlTG']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth']

			tmp = []
			_TotalInputnum = (_XRBNum * _YRBNum * 2) - 1
			for i in range (0, _YRBNum) :
				for j in range (0, 2) : ## for nmos and pmos
					for k in range (0, _XRBNum) :
						if j == 0 : ## nmos settings
							tmp.append([[_ResistorBankOrigin[0][0] + _GapbtwOriginX - _TotalSubringWidth // 2 - _DRCObj._MetalxMinSpace5 - (_DRCObj._VIAxMinSpaceFor3neighboring + self._DesignParameter['_Met5LayerInput']['_Width']) * (2 * _XRBNum*(_YRBNum - i) - k - 1),
										self._DesignParameter['_S<{0}>'.format(_XRBNum * i + k)]['_XYCoordinates'][0][1] + k * _DRCObj._MetalxMinSpace + k * self._DesignParameter['_Met5LayerInput']['_Width']],
										[self._DesignParameter['_S<{0}>'.format(_XRBNum * i + k)]['_XYCoordinates'][0][0],
										self._DesignParameter['_S<{0}>'.format(_XRBNum * i + k)]['_XYCoordinates'][0][1] + k * _DRCObj._MetalxMinSpace + k * self._DesignParameter['_Met5LayerInput']['_Width']]])

							tmp.append([[self._DesignParameter['_S<{0}>'.format(_XRBNum * i + k)]['_XYCoordinates'][0][0],
										self._DesignParameter['_S<{0}>'.format(_XRBNum * i + k)]['_XYCoordinates'][0][1] + k * _DRCObj._MetalxMinSpace + k * self._DesignParameter['_Met5LayerInput']['_Width'] + self._DesignParameter['_Met5LayerInput']['_Width'] // 2],
										[self._DesignParameter['_S<{0}>'.format(_XRBNum * i + k)]['_XYCoordinates'][0][0],
										self._DesignParameter['_S<{0}>'.format(_XRBNum * i + k)]['_XYCoordinates'][0][1] - self._DesignParameter['_Met5LayerInput']['_Width'] // 2]])

		#                     self._DesignParameter['_S<{0}>pin'.format((i+1) * _XRBNum - k - 1)] = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2PIN'][0], _Datatype=DesignParameters._LayerMapping['METAL2PIN'][1], _Presentation=[0,1,2], _Reflect=[0,0,0],
		#                                                                 _XYCoordinates=[[_ResistorBankOrigin[0][0] + self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_TotalSubringRB']['_XYCoordinates'][0][0] -
		#                                 (self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_TotalSubringRB']['_DesignObj']._DesignParameter['_Met1Layerx']['_XWidth'] // 2 + _DRCObj._MetalxMinSpace +
		#                                 self._DesignParameter['_Met5LayerInput']['_Width'] // 2 +
		#                                 (_DRCObj._MetalxMinSpace + self._DesignParameter['_Met5LayerInput']['_Width']) * (_TotalInputnum - (i * _YRBNum + j * _XRBNum + k))),
		#                                 _ResistorBankOrigin[0][1] +
		#                                 self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_TotalSubringRB']['_DesignObj']._DesignParameter['_Met1Layery']['_YWidth'] * _YRBNum]], _Mag=0.1, _Angle=90, _TEXT = 'S<{0}>'.format((i+1) * _XRBNum - k - 1))


		#                     tmp.append([[_ResistorBankOrigin[0][0] + self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_TotalSubringRB']['_XYCoordinates'][0][0] -
		#                                 (self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_TotalSubringRB']['_DesignObj']._DesignParameter['_Met1Layerx']['_XWidth'] // 2 + _DRCObj._MetalxMinSpace +
		#                                 self._DesignParameter['_Met5LayerInput']['_Width'] +
		#                                 (_DRCObj._MetalxMinSpace + self._DesignParameter['_Met5LayerInput']['_Width']) * (_TotalInputnum - (i * _YRBNum + j * _XRBNum + k))),
		#                                 _ResistorBankOrigin[0][1] +
		#                                 self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaMet12Met2OnNMOSControlTG']['_XYCoordinates'][0][1] +
		#                                 (_DRCObj._MetalxMinSpace + self._DesignParameter['_Met5LayerInput']['_Width']) * (k) +
		#                                 _ResistorSpaceY * i],
		#                                 [_ResistorBankOrigin[0][0] +
		#                                 self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaMet12Met2OnNMOSControlTG']['_XYCoordinates'][0][0] +
		#                                 _ResistorSpaceX * k,
		#                                 _ResistorBankOrigin[0][1] +
		#                                 self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaMet12Met2OnNMOSControlTG']['_XYCoordinates'][0][1] +
		#                                 (_DRCObj._MetalxMinSpace + self._DesignParameter['_Met5LayerInput']['_Width']) * (k) +
		#                                 _ResistorSpaceY * i]
		#                                 ])

		#                     tmp.append([[_ResistorBankOrigin[0][0] +
		#                                 self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaMet12Met2OnNMOSControlTG']['_XYCoordinates'][0][0] +
		#                                 _ResistorSpaceX * k,
		#                                 _ResistorBankOrigin[0][1] +
		#                                 self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaMet12Met2OnNMOSControlTG']['_XYCoordinates'][0][1] +
		#                                 self._DesignParameter['_Met5LayerInput']['_Width'] // 2 +
		#                                 (_DRCObj._MetalxMinSpace + self._DesignParameter['_Met5LayerInput']['_Width']) * (k) +
		#                                 _ResistorSpaceY * i],
		#                                 [_ResistorBankOrigin[0][0] +
		#                                 self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaMet12Met2OnNMOSControlTG']['_XYCoordinates'][0][0] +
		#                                 _ResistorSpaceX * k,
		#                                 _ResistorBankOrigin[0][1] +
		#                                 self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaMet12Met2OnNMOSControlTG']['_XYCoordinates'][0][1] +
		#                                 _ResistorSpaceY * i]
		#                                 ])


						else : ##pmos settings
							##1st connection
							tmp.append([[_ResistorBankOrigin[0][0] + _GapbtwOriginX - _TotalSubringWidth // 2 - _DRCObj._MetalxMinSpace5 - (_DRCObj._VIAxMinSpaceFor3neighboring + self._DesignParameter['_Met5LayerInput']['_Width']) * (2*_XRBNum*(_YRBNum - i - 1) + k),
										self._DesignParameter['_SB<{0}>'.format(_XRBNum * i + k)]['_XYCoordinates'][0][1] - k * _DRCObj._MetalxMinSpace - k * self._DesignParameter['_Met5LayerInput']['_Width']],
										[self._DesignParameter['_SB<{0}>'.format(_XRBNum * i + k)]['_XYCoordinates'][0][0],
										self._DesignParameter['_SB<{0}>'.format(_XRBNum * i + k)]['_XYCoordinates'][0][1] - k * _DRCObj._MetalxMinSpace - k * self._DesignParameter['_Met5LayerInput']['_Width']]])

							tmp.append([[self._DesignParameter['_SB<{0}>'.format(_XRBNum * i + k)]['_XYCoordinates'][0][0],
										self._DesignParameter['_SB<{0}>'.format(_XRBNum * i + k)]['_XYCoordinates'][0][1] - k * _DRCObj._MetalxMinSpace - k * self._DesignParameter['_Met5LayerInput']['_Width'] - self._DesignParameter['_Met5LayerInput']['_Width'] // 2],
										[self._DesignParameter['_SB<{0}>'.format(_XRBNum * i + k)]['_XYCoordinates'][0][0],
										self._DesignParameter['_SB<{0}>'.format(_XRBNum * i + k)]['_XYCoordinates'][0][1] + self._DesignParameter['_Met5LayerInput']['_Width'] // 2]])

		#                     self._DesignParameter['_SB<{0}>pin'.format(i * _XRBNum + k)] = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2PIN'][0], _Datatype=DesignParameters._LayerMapping['METAL2PIN'][1], _Presentation=[0,1,2], _Reflect=[0,0,0],
		#                                                                 _XYCoordinates=[[_ResistorBankOrigin[0][0] + self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_TotalSubringRB']['_XYCoordinates'][0][0] -
		#                                 (self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_TotalSubringRB']['_DesignObj']._DesignParameter['_Met1Layerx']['_XWidth'] // 2 + _DRCObj._MetalxMinSpace +
		#                                 self._DesignParameter['_Met5LayerInput']['_Width'] // 2 +
		#                                 (_DRCObj._MetalxMinSpace + self._DesignParameter['_Met5LayerInput']['_Width']) * (_TotalInputnum - (i * _YRBNum + j * _XRBNum + k))),
		#                                 _ResistorBankOrigin[0][1] +
		#                                 self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_TotalSubringRB']['_DesignObj']._DesignParameter['_Met1Layery']['_YWidth'] * _YRBNum]], _Mag=0.1, _Angle=90, _TEXT = 'SB<{0}>'.format(i * _XRBNum + k))


		#                     ##second connection
		#                     tmp.append([[_ResistorBankOrigin[0][0] + self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_TotalSubringRB']['_XYCoordinates'][0][0] -
		#                                 (self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_TotalSubringRB']['_DesignObj']._DesignParameter['_Met1Layerx']['_XWidth'] // 2 + _DRCObj._MetalxMinSpace +
		#                                 self._DesignParameter['_Met5LayerInput']['_Width'] +
		#                                 (_DRCObj._MetalxMinSpace + self._DesignParameter['_Met5LayerInput']['_Width']) * (_TotalInputnum - (i * _YRBNum + j * _XRBNum + k))),
		#                                 _ResistorBankOrigin[0][1] +
		#                                 self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSControlTG']['_XYCoordinates'][0][1] -
		#                                 (_DRCObj._MetalxMinSpace + self._DesignParameter['_Met5LayerInput']['_Width']) * (_XRBNum - k - 1) +
		#                                 _ResistorSpaceY * i],
		#                                 [_ResistorBankOrigin[0][0] +
		#                                 self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSControlTG']['_XYCoordinates'][0][0] +
		#                                 _ResistorSpaceX * (_XRBNum - k - 1),
		#                                 _ResistorBankOrigin[0][1] +
		#                                 self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSControlTG']['_XYCoordinates'][0][1] -
		#                                 (_DRCObj._MetalxMinSpace + self._DesignParameter['_Met5LayerInput']['_Width']) * (_XRBNum - k - 1) +
		#                                 _ResistorSpaceY * i]
		#                                 ])

		#                     ##third connection
		#                     tmp.append([[_ResistorBankOrigin[0][0] +
		#                                 self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSControlTG']['_XYCoordinates'][0][0] +
		#                                 _ResistorSpaceX * (_XRBNum - k - 1),
		#                                 _ResistorBankOrigin[0][1] +
		#                                 self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSControlTG']['_XYCoordinates'][0][1] -
		#                                 self._DesignParameter['_Met5LayerInput']['_Width'] // 2 -
		#                                 (_DRCObj._MetalxMinSpace + self._DesignParameter['_Met5LayerInput']['_Width']) * (_XRBNum - k - 1) +
		#                                 _ResistorSpaceY * i],
		#                                 [_ResistorBankOrigin[0][0] +
		#                                 self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSControlTG']['_XYCoordinates'][0][0] +
		#                                 _ResistorSpaceX * (_XRBNum - k - 1),
		#                                 _ResistorBankOrigin[0][1] +
		#                                 self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSControlTG']['_XYCoordinates'][0][1] +
		#                                 _ResistorSpaceY * i]
		#                                 ])


			self._DesignParameter['_Met5LayerInput']['_XYCoordinates'] = tmp
			del tmp

			_ViaInputRoutingMet52Met6 = copy.deepcopy(ViaMet52Met6._ViaMet52Met6._ParametersForDesignCalculation)
			_ViaInputRoutingMet52Met6['_ViaMet52Met6NumberOfCOX'] = 1
			_ViaInputRoutingMet52Met6['_ViaMet52Met6NumberOfCOY'] = 2


			self._DesignParameter['_ViaMet52Met6InputRouting'] = self._SrefElementDeclaration(_DesignObj=ViaMet52Met6._ViaMet52Met6(_DesignParameter=None, _Name = 'ViaMet52Met6InputRoutingIn{}'.format(_Name)))[0]
			self._DesignParameter['_ViaMet52Met6InputRouting']['_DesignObj']._CalculateViaMet52Met6DesignParameterMinimumEnclosureX(**_ViaInputRoutingMet52Met6)

			tmp = []
			for i in range (0, _XRBNum) :
				for j in range (0, _YRBNum) :
					for k in range (0, 2) :
						if k == 0 : ## nmos
							tmp.append([_ResistorBankOrigin[0][0] + _GapbtwOriginX - _TotalSubringWidth // 2 - _DRCObj._MetalxMinSpace5 - (_DRCObj._VIAxMinSpaceFor3neighboring + self._DesignParameter['_Met5LayerInput']['_Width']) * (2 * _XRBNum*(_YRBNum - j) - i - 1)
										- self._DesignParameter['_ViaMet52Met6InputRouting']['_DesignObj']._DesignParameter['_Met5Layer']['_XWidth'] // 2,
										self._DesignParameter['_S<{0}>'.format(_XRBNum * j + i)]['_XYCoordinates'][0][1] + i * _DRCObj._MetalxMinSpace + i * self._DesignParameter['_Met5LayerInput']['_Width'] +
										self._DesignParameter['_ViaMet52Met6InputRouting']['_DesignObj']._DesignParameter['_Met5Layer']['_YWidth'] // 2 - self._DesignParameter['_ViaMet52Met6InputRouting']['_DesignObj']._DesignParameter['_Met5Layer']['_XWidth'] // 2])

						if k == 1 : ## pmos
							tmp.append([_ResistorBankOrigin[0][0] + _GapbtwOriginX - _TotalSubringWidth // 2 - _DRCObj._MetalxMinSpace5 - (_DRCObj._VIAxMinSpaceFor3neighboring + self._DesignParameter['_Met5LayerInput']['_Width']) * (2*_XRBNum*(_YRBNum - j - 1) + i)
										- self._DesignParameter['_ViaMet52Met6InputRouting']['_DesignObj']._DesignParameter['_Met5Layer']['_XWidth'] // 2,
										self._DesignParameter['_SB<{0}>'.format(_XRBNum * j + i)]['_XYCoordinates'][0][1] - i * _DRCObj._MetalxMinSpace - i * self._DesignParameter['_Met5LayerInput']['_Width'] +
										self._DesignParameter['_ViaMet52Met6InputRouting']['_DesignObj']._DesignParameter['_Met5Layer']['_YWidth'] // 2 - self._DesignParameter['_ViaMet52Met6InputRouting']['_DesignObj']._DesignParameter['_Met5Layer']['_XWidth'] // 2])




			self._DesignParameter['_ViaMet52Met6InputRouting']['_XYCoordinates'] = tmp

			del tmp

			self._DesignParameter['_Met6LayerInput'] = self._PathElementDeclaration(
				_Layer = DesignParameters._LayerMapping['METAL6'][0], _Datatype=DesignParameters._LayerMapping['METAL6'][1],
				_XYCoordinates=[], _Width=100)

			self._DesignParameter['_Met6LayerInput']['_Width'] = self._DesignParameter['_ResistorBank']['_DesignObj']._DesignParameter['_TransmissionGateRB']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSControlTG']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth']

			tmp = []
			for i in range (0, _XRBNum) :
				for j in range (0, _YRBNum) :
					for k in range (0,2) :
						if k == 0 :
							tmp.append([[_ResistorBankOrigin[0][0] + _GapbtwOriginX - _TotalSubringWidth // 2 - _DRCObj._MetalxMinSpace5 - (_DRCObj._VIAxMinSpaceFor3neighboring + self._DesignParameter['_Met5LayerInput']['_Width']) * (2 * _XRBNum*(_YRBNum - j) - i - 1) -
									self._DesignParameter['_Met6LayerInput']['_Width'] // 2,
									self._DesignParameter['_S<{0}>'.format(_XRBNum * j + i)]['_XYCoordinates'][0][1] + i * _DRCObj._MetalxMinSpace + i * self._DesignParameter['_Met5LayerInput']['_Width']],
									[_ResistorBankOrigin[0][0] + _GapbtwOriginX - _TotalSubringWidth // 2 - _DRCObj._MetalxMinSpace5 - (_DRCObj._VIAxMinSpaceFor3neighboring + self._DesignParameter['_Met5LayerInput']['_Width']) * (2 * _XRBNum*(_YRBNum - j) - i - 1) -
									self._DesignParameter['_Met6LayerInput']['_Width'] // 2,
									_ResistorBankOrigin[0][1] + _GapbtwOriginY + _YRBNum * _ResistorSpaceY]])

						else :
							tmp.append([[_ResistorBankOrigin[0][0] + _GapbtwOriginX - _TotalSubringWidth // 2 - _DRCObj._MetalxMinSpace5 - (_DRCObj._VIAxMinSpaceFor3neighboring + self._DesignParameter['_Met5LayerInput']['_Width']) * (2*_XRBNum*(_YRBNum - j - 1) + i) -
										self._DesignParameter['_Met6LayerInput']['_Width'] // 2,
										self._DesignParameter['_SB<{0}>'.format(_XRBNum * j + i)]['_XYCoordinates'][0][1] - i * _DRCObj._MetalxMinSpace - i * self._DesignParameter['_Met5LayerInput']['_Width']],
										[_ResistorBankOrigin[0][0] + _GapbtwOriginX - _TotalSubringWidth // 2 - _DRCObj._MetalxMinSpace5 - (_DRCObj._VIAxMinSpaceFor3neighboring + self._DesignParameter['_Met5LayerInput']['_Width']) * (2*_XRBNum*(_YRBNum - j - 1) + i) -
										self._DesignParameter['_Met6LayerInput']['_Width'] // 2,
										_ResistorBankOrigin[0][1] + _GapbtwOriginY + _YRBNum * _ResistorSpaceY]])


			self._DesignParameter['_Met6LayerInput']['_XYCoordinates'] = tmp

			del tmp

			for i in range (0, _XRBNum) :
				for j in range (0, _YRBNum) :
					for k in range (0, 2) : ## for nmos 0 and pmos 1
						if k == 0 :
							self._DesignParameter['_S<{0}>pin'.format(i + _XRBNum * j)] = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL6PIN'][0], _Datatype=DesignParameters._LayerMapping['METAL6PIN'][1],
							_Presentation=[0,1,2], _Reflect=[0,0,0],
							_XYCoordinates=[[_ResistorBankOrigin[0][0] + _GapbtwOriginX - _TotalSubringWidth // 2 - _DRCObj._MetalxMinSpace5 - (_DRCObj._VIAxMinSpaceFor3neighboring + self._DesignParameter['_Met5LayerInput']['_Width']) * (2 * _XRBNum*(_YRBNum - j) - i - 1) -
											self._DesignParameter['_Met6LayerInput']['_Width'] // 2,
											_ResistorBankOrigin[0][1] + _GapbtwOriginY + _YRBNum * _ResistorSpaceY]],
							_Mag = 0.02, _Angle=0, _TEXT='S<{0}>'.format(i + _XRBNum * j))

						else :
							self._DesignParameter['_SB<{0}>pin'.format(i + _XRBNum * j)] = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL6PIN'][0], _Datatype=DesignParameters._LayerMapping['METAL6PIN'][1],
							_Presentation=[0,1,2], _Reflect=[0,0,0],
							_XYCoordinates=[[_ResistorBankOrigin[0][0] + _GapbtwOriginX - _TotalSubringWidth // 2 - _DRCObj._MetalxMinSpace5 - (_DRCObj._VIAxMinSpaceFor3neighboring + self._DesignParameter['_Met5LayerInput']['_Width']) * (2*_XRBNum*(_YRBNum - j - 1) + i) -
										self._DesignParameter['_Met6LayerInput']['_Width'] // 2,
										_ResistorBankOrigin[0][1] + _GapbtwOriginY + _YRBNum * _ResistorSpaceY]],
							_Mag = 0.02, _Angle=0, _TEXT='SB<{0}>'.format(i + _XRBNum * j))










if __name__ == '__main__' :
	import random
	import DRCchecker
	import time
	start = time.time()

	# for tries in range (0, 100) :
	#     i = random.randint(4,50)
	#     j = random.randint(4,80)
	#     k = random.randint(2,15)
	#     l = random.randint(1250, 4000)
	#     m = random.randint(170,200)
	#     n = random.randint(500,2000)
	#     o = random.randint(200,500)
	#     if m % 2 == 1 :
	#         m += 1
	#     print ("@@@@@@@@@@@@@@@@@@", i, j, k,l,m,n,o)

	## 65nm : 500nm min width (60), 28nm : 200nm min width (30), 40nm : 350nm min width(40),  90nm (100nm channel length) : 700nm min width
	## 65nm : pmos maximum width 1.5um

	for _ in range (0, 1) :
		_XRBNum = 4
		_YRBNum = 8

		_TransmissionGateFinger = 2
		_TransmissionGateChannelWidth = 200 ##200nm ~ 500nm range
		_TransmissionGateChannelLength = 60
		_TransmissionGateNPRatio = 2  ##Default = 2
		_TransmissionGateDummy = True     #T/F?
		_TransmissionGateVDD2VSSHeight = None ## FIXED
		_TransmissionGateXVT = 'SLVT'     #T/F?

		_PowerLine = True # T/F?
		_InputLine = True

		_ResistorWidth = 1250
		_ResistorLength = 1234    ## minimum : 400 1234
		_ResistorMetXCO = None
		_ResistorMetYCO = 2

		_PMOSSubringType = False ## FIXED
		_PMOSSubringXWidth = None ## FIXED
		_PMOSSubringYWidth = None ## FIXED
		_PMOSSubringWidth = 170 ## def : 170, 170~200

		_NMOSSubringType = True ## FIXED
		_NMOSSubringXWidth = None ## FIXED
		_NMOSSubringYWidth = None ## FIXED
		_NMOSSubringWidth = _PMOSSubringWidth

		_TotalSubringType = True ## FIXED
		_TotalSubringXWidth = None ## FIXED
		_TotalSubringYWidth = None ## FIXED
		_TotalSubringWidth = _PMOSSubringWidth

		FullResistorBankObj = _FullResistorBank(_DesignParameter=None, _Name='FullResistorBank')
		#print ("A!!")
		FullResistorBankObj._CalculateFullResistorBank(
								#  _InverterFinger=_InverterFinger, _InverterChannelWidth=_InverterChannelWidth, _InverterChannelLength=_InverterChannelLength, _InverterNPRatio=_InverterNPRatio, _InverterDummy = _InverterDummy,
								# _InverterVDD2VSSHeight=_InverterVDD2VSSHeight, _InverterSLVT = _InverterSLVT,
								# _InverterNumSupplyCOX = None, _InverterNumSupplyCOY = None,
								# _InverterSupplyMet1XWidth = None, _InverterSupplMet1YWidth = None, _InverterNumVIAPoly2Met1COX = None, _InverterNumVIAPoly2Met1COY = None,
								# _InverterNumVIAMet12COX = None, _InverterNumVIAMet12COY = None,
									_XRBNum=_XRBNum, _YRBNum=_YRBNum,
								_TransmissionGateFinger =_TransmissionGateFinger, _TransmissionGateChannelWidth = _TransmissionGateChannelWidth, _TransmissionGateChannelLength = _TransmissionGateChannelLength, _TransmissionGateNPRatio =_TransmissionGateNPRatio,
								_TransmissionGateDummy = _TransmissionGateDummy , _TransmissionGateVDD2VSSHeight = _TransmissionGateVDD2VSSHeight, _TransmissionGateXVT = _TransmissionGateXVT,
								_PowerLine = _PowerLine, _InputLine = _InputLine,
								# _TransmissionGateNumSupplyCOX = None, _TransmissionGateNumSupplyCOY = None, _TransmissionGateSupplyMet1XWidth = None, _TransmissionGateSupplyMet1YWidth = None,
								# _TransmissionGateNumVIAPoly2Met1COX = None, _TransmissionGateNumVIAPoly2Met1COY = None, _TransmissionGateNumVIAMet12COX = None, _TransmissionGateNumVIAMet12COY = None,
								_ResistorWidth=_ResistorWidth, _ResistorLength=_ResistorLength, _ResistorMetXCO = _ResistorMetXCO, _ResistorMetYCO = _ResistorMetYCO,
									_PMOSSubringType=_PMOSSubringType, _PMOSSubringXWidth=_PMOSSubringXWidth, _PMOSSubringYWidth=_PMOSSubringYWidth,_PMOSSubringWidth=_PMOSSubringWidth,
									_NMOSSubringType=_NMOSSubringType, _NMOSSubringXWidth=_NMOSSubringXWidth, _NMOSSubringYWidth=_NMOSSubringYWidth,_NMOSSubringWidth=_NMOSSubringWidth,
									_TotalSubringType=_TotalSubringType, _TotalSubringXWidth=_TotalSubringXWidth, _TotalSubringYWidth=_TotalSubringYWidth,_TotalSubringWidth=_TotalSubringWidth)


		FullResistorBankObj._UpdateDesignParameter2GDSStructure(_DesignParameterInDictionary=FullResistorBankObj._DesignParameter)
		_fileName = 'FullResistorBank.gds'
		testStreamFile = open('./{}'.format(_fileName), 'wb')

		tmp = FullResistorBankObj._CreateGDSStream(FullResistorBankObj._DesignParameter['_GDSFile']['_GDSFile'])

		tmp.write_binary_gds_stream(testStreamFile)

		testStreamFile.close()

		print ('###############      Sending to FTP Server...      ##################')


		ftp = ftplib.FTP('141.223.29.62')
		ftp.login('junung', 'chlwnsdnd1!')
		# ftp.cwd('/mnt/sdc/junung/OPUS/Samsung28n')
		ftp.cwd('/mnt/sdc/junung/OPUS/TSMC65n')
		#ftp.cwd('/mnt/sdc/junung/OPUS/TSMC40n')
		#ftp.cwd('/mnt/sdc/junung/OPUS/TSMC90n')
		myfile = open('FullResistorBank.gds', 'rb')
		ftp.storbinary('STOR FullResistorBank.gds', myfile)
		myfile.close()
		ftp.close()

		# _Checker = DRCchecker.DRCchecker('junung','chlwnsdnd1!','/mnt/sdc/junung/OPUS/TSMC90n','/mnt/sdc/junung/OPUS/TSMC90n/DRC/DRC_run','FRBtst','FullResistorBank')
		# _Checker.DRCchecker()

	# ftp = ftplib.FTP('141.223.22.156')
	# ftp.login('jicho0927', 'cho89140616!!')
	# ftp.cwd('/mnt/sdc/jicho0927/OPUS/SAMSUNG28n')
	# myfile = open('FullResistorBank.gds', 'rb')
	# ftp.storbinary('STOR FullResistorBank.gds', myfile)
	# myfile.close()
	# ftp.close()

#     print ('###############      DRC checking... {}/100      ##################'.format(tries + 1))

#     import DRCchecker
#     a = DRCchecker.DRCchecker('junung','chlwnsdnd1!','/mnt/sdc/junung/OPUS/Samsung28n','/mnt/sdc/junung/OPUS/Samsung28n/DRC/run','FRB_tst','FullResistorBank')
#     a.DRCchecker()

# print ("DRCclean!!")
