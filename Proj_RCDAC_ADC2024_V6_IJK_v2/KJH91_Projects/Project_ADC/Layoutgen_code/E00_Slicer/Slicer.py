import sys, os
sys.path.append(os.path.abspath(__file__))
sys.path.append(os.path.abspath("KJH91_Projects\\Project_ADC\\Layoutgen_code\\E00_Slicer"))
print(sys.path)
sys.path.append(os.path.abspath(sys.path[0]))

# print(os.path.realpath(__file__))
# print(os.path.abspath(__file__))
# print(os.getcwd())
# os.chdir(os.getcwd())

from Proj_RCDAC_ADC2024_V6_IJK_v2.KJH91_Projects.Project_ADC.Layoutgen_code.E00_Slicer import StickDiagram
from Proj_RCDAC_ADC2024_V6_IJK_v2.KJH91_Projects.Project_ADC.Layoutgen_code.E00_Slicer import DesignParameters
from Proj_RCDAC_ADC2024_V6_IJK_v2.KJH91_Projects.Project_ADC.Layoutgen_code.E00_Slicer import DRC
from Proj_RCDAC_ADC2024_V6_IJK_v2.KJH91_Projects.Project_ADC.Layoutgen_code.E00_Slicer import user_define_exceptions

from Proj_RCDAC_ADC2024_V6_IJK_v2.KJH91_Projects.Project_ADC.Layoutgen_code.E00_Slicer import NMOSWithDummy
from Proj_RCDAC_ADC2024_V6_IJK_v2.KJH91_Projects.Project_ADC.Layoutgen_code.E00_Slicer import PMOSWithDummy
from Proj_RCDAC_ADC2024_V6_IJK_v2.KJH91_Projects.Project_ADC.Layoutgen_code.E00_Slicer import NbodyContact
from Proj_RCDAC_ADC2024_V6_IJK_v2.KJH91_Projects.Project_ADC.Layoutgen_code.E00_Slicer import PbodyContact
from Proj_RCDAC_ADC2024_V6_IJK_v2.KJH91_Projects.Project_ADC.Layoutgen_code.E00_Slicer import ViaPoly2Met1
from Proj_RCDAC_ADC2024_V6_IJK_v2.KJH91_Projects.Project_ADC.Layoutgen_code.E00_Slicer import ViaMet12Met2
from Proj_RCDAC_ADC2024_V6_IJK_v2.KJH91_Projects.Project_ADC.Layoutgen_code.E00_Slicer import ViaMet22Met3
from Proj_RCDAC_ADC2024_V6_IJK_v2.KJH91_Projects.Project_ADC.Layoutgen_code.E00_Slicer import ViaMet32Met4
from Proj_RCDAC_ADC2024_V6_IJK_v2.KJH91_Projects.Project_ADC.Layoutgen_code.E00_Slicer import ViaMet42Met5
from Proj_RCDAC_ADC2024_V6_IJK_v2.KJH91_Projects.Project_ADC.Layoutgen_code.E00_Slicer import ViaMet52Met6
from Proj_RCDAC_ADC2024_V6_IJK_v2.KJH91_Projects.Project_ADC.Layoutgen_code.E00_Slicer import ViaMet62Met7
from Proj_RCDAC_ADC2024_V6_IJK_v2.KJH91_Projects.Project_ADC.Layoutgen_code.E00_Slicer import ContGeneration
from Proj_RCDAC_ADC2024_V6_IJK_v2.KJH91_Projects.Project_ADC.Layoutgen_code.E00_Slicer import PMOSSetofSlicer_test
from Proj_RCDAC_ADC2024_V6_IJK_v2.KJH91_Projects.Project_ADC.Layoutgen_code.E00_Slicer import NMOSSetofSlicer_test
from Proj_RCDAC_ADC2024_V6_IJK_v2.KJH91_Projects.Project_ADC.Layoutgen_code.E00_Slicer import psubring

import warnings
import copy
import random



import ftplib
import os

from ftplib import FTP
import base64


class _Slicer(StickDiagram._StickDiagram):


	_ParametersForDesignCalculation=dict(
		_CLKinputPMOSFinger1=None,  # 6
		_CLKinputPMOSFinger2=None,  # 3
		_PMOSFinger=None,  # 3
		_PMOSChannelWidth=None,  # 500
		_DATAinputNMOSFinger=None,  # 12
		_NMOSFinger=None,  # 2
		_CLKinputNMOSFinger=None,  # 8
		_NMOSChannelWidth=None,  # 500
		_CLKinputNMOSChannelWidth=None,  # 800
		_ChannelLength=None,  # 30
		_Dummy=True,
		_XVT=None,
		_GuardringWidth=None,
		_Guardring=True,
		_SlicerGuardringWidth=None,
		_SlicerGuardring=None,
		_NumSupplyCOY=None,
		_NumSupplyCOX=None,
		_SupplyMet1XWidth=None,
		_SupplyMet1YWidth=None,
		_VDD2VSSHeight=None,
		_NumVIAPoly2Met1COX=None,
		_NumVIAPoly2Met1COY=None,
		_NumVIAMet12COX=None,
		_NumVIAMet12COY=None,
		_PowerLine=False,)


	def __init__(self, _DesignParameter=None, _Name='E00_Slicer'):
		if _DesignParameter != None:
			self._DesignParameter = _DesignParameter
		else:
			self._DesignParameter = dict(_Name=self._NameDeclaration(_Name=_Name),
										 _GDSFile=self._GDSObjDeclaration(_GDSFile=None),
										_XYcoordAsCent = dict(_XYcoordAsCent=1)
										)


	def _CalculateDesignParameter(self,
								  _CLKinputPMOSFinger1=None,  # 6
								  _CLKinputPMOSFinger2=None,  # 3
								  _PMOSFinger=None,  # 3
								  _PMOSChannelWidth=None,  # 500
								  _DATAinputNMOSFinger=None,  # 12
								  _NMOSFinger=None,  # 2
								  _CLKinputNMOSFinger=None,  # 8
								  _NMOSChannelWidth=None,  # 500
								  _CLKinputNMOSChannelWidth=None,  # 800
								  _ChannelLength=None,  # 30
								  _Dummy=True,
								  _XVT=None,
								  _GuardringWidth=None,
								  _Guardring=True,
								  _SlicerGuardringWidth=None,
								  _SlicerGuardring=None,
								  _NumSupplyCOY=None,
								  _NumSupplyCOX=None,
								  _SupplyMet1XWidth=None,
								  _SupplyMet1YWidth=None,
								  _VDD2VSSHeight=None,
								  _NumVIAPoly2Met1COX=None,
								  _NumVIAPoly2Met1COY=None,
								  _NumVIAMet12COX=None,
								  _NumVIAMet12COY=None,
								  _PowerLine=False,
								 ):

			_DRCObj = DRC.DRC()
			_XYCoordinateOfPMOSSET = [[0, 0]]
			_XYCoordinateOfNMOSSET = [[0, 0]]
			MinSnapSpacing = _DRCObj._MinSnapSpacing
			_Name = self._DesignParameter['_Name']['_Name']
			_CLKinputPMOSFinger = _CLKinputPMOSFinger1 + _CLKinputPMOSFinger2





			##############################################################################################################################################################
			################################################################### PMOS SET Generation  #########################################################################
			##############################################################################################################################################################
			# PMOS SET Generation
			_PMOSSETinputs = copy.deepcopy(PMOSSetofSlicer_test._PMOSWithDummyOfSlicer._ParametersForDesignCalculation)
			_PMOSSETinputs['_CLKinputPMOSFinger1'] = _CLKinputPMOSFinger1
			_PMOSSETinputs['_CLKinputPMOSFinger2'] = _CLKinputPMOSFinger2
			_PMOSSETinputs['_PMOSFinger'] = _PMOSFinger
			_PMOSSETinputs['_PMOSChannelWidth'] = _PMOSChannelWidth
			_PMOSSETinputs['_ChannelLength'] = _ChannelLength
			_PMOSSETinputs['_Dummy'] = _Dummy
			_PMOSSETinputs['_XVT'] = _XVT
			_PMOSSETinputs['_GuardringWidth'] = _GuardringWidth
			_PMOSSETinputs['_Guardring'] = _Guardring
			self._DesignParameter['_PMOSSET'] = self._SrefElementDeclaration(_DesignObj=PMOSSetofSlicer_test._PMOSWithDummyOfSlicer(_DesignParameter=None, _Name='{}:PMOSSET'.format(_Name)))[0]
			self._DesignParameter['_PMOSSET']['_DesignObj']._CalculateDesignParameter(**_PMOSSETinputs)
			self._DesignParameter['_PMOSSET']['_XYCoordinates'] = [[0, 0+abs(self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['PMOS_bottomtmp']['_Ignore']) + _GuardringWidth +_DRCObj._NwMinSpacetoNactive]]

			##############################################################################################################################################################
			################################################################### NMOS SET Generation  #########################################################################
			##############################################################################################################################################################
			# NMOS SET Generation
			_NMOSSETinputs = copy.deepcopy(NMOSSetofSlicer_test._NMOSWithDummyOfSlicer._ParametersForDesignCalculation)
			_NMOSSETinputs['_DATAinputNMOSFinger'] = _DATAinputNMOSFinger
			_NMOSSETinputs['_NMOSFinger'] = _NMOSFinger
			_NMOSSETinputs['_CLKinputNMOSFinger'] = _CLKinputNMOSFinger
			_NMOSSETinputs['_NMOSChannelWidth'] = _NMOSChannelWidth
			_NMOSSETinputs['_CLKinputNMOSChannelWidth'] = _CLKinputNMOSChannelWidth
			_NMOSSETinputs['_ChannelLength'] = _ChannelLength
			_NMOSSETinputs['_Dummy'] = _Dummy
			_NMOSSETinputs['_XVT'] = _XVT
			_NMOSSETinputs['_GuardringWidth'] = _GuardringWidth
			_NMOSSETinputs['_Guardring'] = _Guardring

			self._DesignParameter['_NMOSSET'] = self._SrefElementDeclaration(_DesignObj=NMOSSetofSlicer_test._NMOSWithDummyOfSlicer(_DesignParameter=None, _Name='{}:NMOSSET'.format(_Name)))[0]
			self._DesignParameter['_NMOSSET']['_DesignObj']._CalculateDesignParameter(**_NMOSSETinputs)

			PMOS_toptmp=self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['PMOS_toptmp']['_Ignore']
			PMOS_bottomtmp=self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['PMOS_bottomtmp']['_Ignore']
			PMOS_righttmp=self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['PMOS_righttmp']['_Ignore']
			PMOS_lefttmp=self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['PMOS_lefttmp']['_Ignore']
			NMOS_toptmp=self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['NMOS_toptmp']['_Ignore']
			NMOS_bottomtmp=self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['NMOS_bottomtmp']['_Ignore']
			NMOS_righttmp=self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['NMOS_righttmp']['_Ignore']
			NMOS_lefttmp=self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['NMOS_lefttmp']['_Ignore']
			_NMOSGuardringY=self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_GuardringY']['_Ignore']

			NMOS_GuardringHeight = NMOS_toptmp - NMOS_bottomtmp
			tmp = self._DesignParameter['_PMOSSET']['_XYCoordinates'][0][1] + PMOS_bottomtmp
			self._DesignParameter['_NMOSSET']['_XYCoordinates'] = [[0, self.FloorMinSnapSpacing(tmp - (int(round(NMOS_GuardringHeight + 0.5)) // 2 + _NMOSGuardringY) - max(_DRCObj._Metal1DefaultSpace + _GuardringWidth, self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_Guardring']['_DesignObj']._DesignParameter['_NWLayer']['_Width'] // 2 + _GuardringWidth // 2 + _DRCObj._NwMinSpacetoNactive), MinSnapSpacing)]]



			#########################################################################################################################################
			############################################### Guardring Generation for E00_Slicer #########################################################
			#########################################################################################################################################
			print('x')
			_GuardRingMet1Space = _DRCObj._Metal1DefaultSpace##_DRCObj._PpMinExtensiononPactive2 * 2 + _DRCObj._PpMinSpace


			bottomtmp = self.CeilMinSnapSpacing(self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1] + NMOS_bottomtmp - max(_GuardringWidth//2 + _GuardRingMet1Space + _SlicerGuardringWidth//2, _GuardringWidth + 2 * _DRCObj._PpMinExtensiononPactive2 + _DRCObj._PpMinSpace), MinSnapSpacing)

			lefttmp = self.CeilMinSnapSpacing(min(self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][0] + NMOS_lefttmp - self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_Guardring']['_DesignObj']._DesignParameter['_PPLayer']['_Width'] // 2 - _SlicerGuardringWidth // 2 - _DRCObj._PpMinSpace - _DRCObj._PpMinExtensiononPactive2, \
												  self._DesignParameter['_PMOSSET']['_XYCoordinates'][0][0] + min(PMOS_lefttmp, NMOS_lefttmp) - _GuardringWidth//2 - _GuardRingMet1Space - _SlicerGuardringWidth//2,\
												  self._DesignParameter['_PMOSSET']['_XYCoordinates'][0][0] + min(PMOS_lefttmp, NMOS_lefttmp) - self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_Guardring']['_DesignObj']._DesignParameter['_NWLayer']['_Width'] // 2 - _SlicerGuardringWidth//2 - _DRCObj._NwMinSpacetoNactive), MinSnapSpacing)
			righttmp = self.CeilMinSnapSpacing(max(self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][0] + NMOS_righttmp + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_Guardring']['_DesignObj']._DesignParameter['_PPLayer']['_Width'] // 2 + _SlicerGuardringWidth // 2 + _DRCObj._PpMinSpace + _DRCObj._PpMinExtensiononPactive2,\
												   self._DesignParameter['_PMOSSET']['_XYCoordinates'][0][0] + max(PMOS_righttmp, NMOS_righttmp) + _GuardringWidth//2 + _GuardRingMet1Space + _SlicerGuardringWidth//2, \
												   self._DesignParameter['_PMOSSET']['_XYCoordinates'][0][0] + max(PMOS_righttmp, NMOS_righttmp) + self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_Guardring']['_DesignObj']._DesignParameter['_NWLayer']['_Width'] // 2 + _SlicerGuardringWidth//2 + _DRCObj._NwMinSpacetoNactive), MinSnapSpacing)

			_GuardringMet1Space2 = _DRCObj.DRCMETAL1MinSpace(self.CeilMinSnapSpacing(self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1] + NMOS_bottomtmp - bottomtmp + _SlicerGuardringWidth / 2 + _GuardringWidth / 2, MinSnapSpacing), PMOS_righttmp - PMOS_lefttmp + _GuardringWidth, _GuardringWidth)

			toptmp = self.CeilMinSnapSpacing(max(self._DesignParameter['_PMOSSET']['_XYCoordinates'][0][1] + PMOS_toptmp + _GuardringWidth / 2 + _GuardringMet1Space2 + _SlicerGuardringWidth / 2, self._DesignParameter['_PMOSSET']['_XYCoordinates'][0][1] + PMOS_toptmp + self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_Guardring']['_DesignObj']._DesignParameter['_NWLayer']['_Width'] // 2 + _SlicerGuardringWidth//2 + _DRCObj._NwMinSpacetoNactive), MinSnapSpacing)

			_GuardringCetPointX = self.CeilMinSnapSpacing((lefttmp + righttmp) / 2, MinSnapSpacing)
			_GuardringCetPointY = self.CeilMinSnapSpacing((toptmp + bottomtmp) / 2, MinSnapSpacing)
			_GuardringXWidth = self.CeilMinSnapSpacing((righttmp - lefttmp - _SlicerGuardringWidth), MinSnapSpacing)
			_GuardringYWidth = self.CeilMinSnapSpacing((toptmp - bottomtmp - _SlicerGuardringWidth), MinSnapSpacing)
			# if _GuardringXWidth % 2 == 1:
			#     _GuardringXWidth = _GuardringXWidth + 1
			# if _GuardringYWidth % 2 == 1:
			#     _GuardringYWidth = _GuardringYWidth + 1
			# if _GuardringCetPointX % 2 == 1 :
			#     _GuardringCetPointX = _GuardringCetPointX
			# if _GuardringCetPointY % 2 == 1 :
			#     _GuardringCetPointY = _GuardringCetPointY



			_NMOSSubringinputs = copy.deepcopy(psubring._PSubring._ParametersForDesignCalculation)
			_NMOSSubringinputs['_PType'] = True
			_NMOSSubringinputs['_XWidth'] = _GuardringXWidth
			_NMOSSubringinputs['_YWidth'] = _GuardringYWidth
			_NMOSSubringinputs['_Width'] = _SlicerGuardringWidth

			self._DesignParameter['_Guardring'] = self._SrefElementDeclaration(
				_DesignObj=psubring._PSubring(_DesignParameter=None, _Name='{}:Guardring'.format(_Name)))[0]
			self._DesignParameter['_Guardring']['_DesignObj']._CalculatePSubring(**_NMOSSubringinputs)

			self._DesignParameter['_Guardring']['_XYCoordinates'] = [[_GuardringCetPointX, _GuardringCetPointY]]


			################################################################ Guadring VSS Generation ########################################################################################
			self._DesignParameter['_GuardringVSS'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _XYCoordinates=[], _XWidth=400, _YWidth=400)
			self._DesignParameter['_GuardringVSS']['_XWidth'] = _GuardringXWidth + 2 * _SlicerGuardringWidth
			self._DesignParameter['_GuardringVSS']['_YWidth'] = self.CeilMinSnapSpacing((self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_Guardring']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_Guardring']['_DesignObj']._DesignParameter['_Met1Layerx']['_XYCoordinates'][1][1]) - (self._DesignParameter['_Guardring']['_XYCoordinates'][0][1] + self._DesignParameter['_Guardring']['_DesignObj']._DesignParameter['_Met1Layerx']['_XYCoordinates'][1][1]) + _GuardringWidth // 2 + _SlicerGuardringWidth // 2, 2 * MinSnapSpacing)
			self._DesignParameter['_GuardringVSS']['_XYCoordinates'] = [[0, self.CeilMinSnapSpacing(((self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_Guardring']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_Guardring']['_DesignObj']._DesignParameter['_Met1Layerx']['_XYCoordinates'][1][1] + _GuardringWidth // 2) + (self._DesignParameter['_Guardring']['_XYCoordinates'][0][1] + self._DesignParameter['_Guardring']['_DesignObj']._DesignParameter['_Met1Layerx']['_XYCoordinates'][1][1] - _SlicerGuardringWidth // 2)) // 2, MinSnapSpacing)]]
			print('x')

			_LengthbtwViaCentertoViaCenter = _DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace

			##################################################################################################################################################################################
			################################################################# NMOS VIA1 Generation ###########################################################################################
			##################################################################################################################################################################################
			## VIA1 Generation for Gate of Inner NMOS
			_VIAInnerNMOSGateMet12 = copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation)
			_tmpNumViaX = int(self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS3']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace))
			if _tmpNumViaX < 2:
				_tmpNumViaX = 2
			_VIAInnerNMOSGateMet12['_ViaMet12Met2NumberOfCOX'] = _tmpNumViaX
			_VIAInnerNMOSGateMet12['_ViaMet12Met2NumberOfCOY'] = 1


			self._DesignParameter['_ViaMet12Met2OnNMOSGate1'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_DesignParameter=None, _Name='{}:ViaMet12Met2OnInnerNMOSGate'.format(_Name)))[0]
			self._DesignParameter['_ViaMet12Met2OnNMOSGate1']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureY(**_VIAInnerNMOSGateMet12)
			self._DesignParameter['_ViaMet12Met2OnNMOSGate1']['_XYCoordinates'] = [[self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS3']['_XYCoordinates'][0][0],
																					self.CeilMinSnapSpacing(max(self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_Met2NMOS']['_XYCoordinates'][0][1][1] + _DRCObj._MetalxMinWidth + _DRCObj._MetalxMinSpace,
																				   self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS3']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1] + _LengthbtwViaCentertoViaCenter // 4), MinSnapSpacing)],
																				   [self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS4']['_XYCoordinates'][0][0],
																					self.CeilMinSnapSpacing(max(self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_Met2NMOS']['_XYCoordinates'][0][1][1] + _DRCObj._MetalxMinWidth + _DRCObj._MetalxMinSpace,
																					self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS3']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1] + _LengthbtwViaCentertoViaCenter // 4), MinSnapSpacing)]
																				  ]
			del _tmpNumViaX


			# if _NMOSChannelWidth < 400 :
			#     self._DesignParameter['_Metal1forGate2&3'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _XYCoordinates=[], _XWidth=400, _YWidth=400)
			#     self._DesignParameter['_Metal1forGate2&3']['_XWidth'] = max(self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS3']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'], self._DesignParameter['_ViaMet12Met2OnNMOSGate1']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'])
			#     self._DesignParameter['_Metal1forGate2&3']['_YWidth'] = self.CeilMinSnapSpacing(abs(self._DesignParameter['_ViaMet12Met2OnNMOSGate1']['_XYCoordinates'][0][1] + self._DesignParameter['_ViaMet12Met2OnNMOSGate1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // 2 - (self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS3']['_XYCoordinates'][0][1]\
			#                                                                         + self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1] - self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS3']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // 2)), MinSnapSpacing)
			#     self._DesignParameter['_Metal1forGate2&3']['_XYCoordinates'] = [[self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS3']['_XYCoordinates'][0][0],
			#                                                                      self.CeilMinSnapSpacing((self._DesignParameter['_ViaMet12Met2OnNMOSGate1']['_XYCoordinates'][0][1] + self._DesignParameter['_ViaMet12Met2OnNMOSGate1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // 2 + (self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS3']['_XYCoordinates'][0][1] \
			#                                                                     + self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1] - self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS3']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // 2)) // 2 - 1, MinSnapSpacing)],
			#                                                                        [self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS4']['_XYCoordinates'][0][0],
			#                                                                         self.CeilMinSnapSpacing((self._DesignParameter['_ViaMet12Met2OnNMOSGate1']['_XYCoordinates'][0][1] + self._DesignParameter['_ViaMet12Met2OnNMOSGate1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // 2 + (self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS3']['_XYCoordinates'][0][1] \
			#                                                                     + self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1] - self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS3']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // 2)) // 2 - 1, MinSnapSpacing)]
			#                                                                       ]




			# VIA1 Generation for Gate of Outer NMOS
			_VIAOuterNMOSGateMet12 = copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation)
			_tmpNumViaX = int(self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS5']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace))
			if _tmpNumViaX < 2:
				_tmpNumViaX = 2
			_VIAOuterNMOSGateMet12['_ViaMet12Met2NumberOfCOX'] = _tmpNumViaX
			_VIAOuterNMOSGateMet12['_ViaMet12Met2NumberOfCOY'] = 1
			self._DesignParameter['_ViaMet12Met2OnNMOSGate2'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_DesignParameter=None, _Name='{}:ViaMet12Met2OnOuterNMOSGate'.format(_Name)))[0]
			self._DesignParameter['_ViaMet12Met2OnNMOSGate2']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureY(**_VIAOuterNMOSGateMet12)
			self._DesignParameter['_ViaMet12Met2OnNMOSGate2']['_XYCoordinates'] = [[self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS5']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][0] ,
																					self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS5']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1]]
																				  ]
			if self._DesignParameter['_ViaMet12Met2OnNMOSGate2']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth'] * self._DesignParameter['_ViaMet12Met2OnNMOSGate2']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] < _DRCObj._MetalxMinArea:
				self._DesignParameter['_ViaMet12Met2OnNMOSGate2']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth'] = self.CeilMinSnapSpacing(_DRCObj._MetalxMinArea // self._DesignParameter['_ViaMet12Met2OnNMOSGate2']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'], 2 * MinSnapSpacing)


			del _tmpNumViaX
			print('x')

			## VIA1 Generation for Gate of Outer PMOS CLK
			_VIAOuterPMOSGateMet12 = copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation)
			_tmpNumViaX = int(self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_VIAPMOSPoly2Met1PMOS1']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace))
			if _tmpNumViaX < 2:
				_tmpNumViaX = 2

			_VIAOuterPMOSGateMet12['_ViaMet12Met2NumberOfCOX'] = _tmpNumViaX
			_VIAOuterPMOSGateMet12['_ViaMet12Met2NumberOfCOY'] = 1
			self._DesignParameter['_ViaMet12Met2OnPMOSGate2'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_DesignParameter=None, _Name='{}:ViaMet12Met2OnOuterPMOSGate'.format(_Name)))[0]
			self._DesignParameter['_ViaMet12Met2OnPMOSGate2']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureY(**_VIAOuterPMOSGateMet12)
			self._DesignParameter['_ViaMet12Met2OnPMOSGate2']['_XYCoordinates'] = [[self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_VIAPMOSPoly2Met1PMOS1']['_XYCoordinates'][0][0],  self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_VIAPMOSPoly2Met1PMOS1']['_XYCoordinates'][0][1] \
																					+ self._DesignParameter['_PMOSSET']['_XYCoordinates'][0][1]],
																				   [self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_VIAPMOSPoly2Met1PMOS2']['_XYCoordinates'][0][0], self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_VIAPMOSPoly2Met1PMOS2']['_XYCoordinates'][0][1] \
																					+ self._DesignParameter['_PMOSSET']['_XYCoordinates'][0][1]]]

			if self._DesignParameter['_ViaMet12Met2OnPMOSGate2']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth'] * self._DesignParameter['_ViaMet12Met2OnPMOSGate2']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] < _DRCObj._MetalxMinArea:
				self._DesignParameter['_ViaMet12Met2OnPMOSGate2']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth'] = self.CeilMinSnapSpacing(_DRCObj._MetalxMinArea // self._DesignParameter['_ViaMet12Met2OnPMOSGate2']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'], 2 * MinSnapSpacing)


			del _tmpNumViaX






			## VIA1 Generation for Gate of Inner PMOS
			_VIAInnerPMOSGateMet12 = copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation)
			_tmpNumViaX = int(self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_VIAPMOSPoly2Met1PMOS3']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace) - 1)
			if _tmpNumViaX < 2 :
				_tmpNumViaX = 2
			_VIAInnerPMOSGateMet12['_ViaMet12Met2NumberOfCOX'] = _tmpNumViaX
			_VIAInnerPMOSGateMet12['_ViaMet12Met2NumberOfCOY'] = 1
			self._DesignParameter['_ViaMet12Met2OnPMOSGate1'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_DesignParameter=None, _Name='{}:ViaMet12Met2OnInnerPMOSGate'.format(_Name)))[0]
			self._DesignParameter['_ViaMet12Met2OnPMOSGate1']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureY(**_VIAInnerPMOSGateMet12)
			self._DesignParameter['_ViaMet12Met2OnPMOSGate1']['_XYCoordinates'] = [[self._DesignParameter['_PMOSSET']['_XYCoordinates'][0][0] + self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_VIAPMOSPoly2Met1PMOS3']['_XYCoordinates'][0][0], self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_VIAPMOSPoly2Met1PMOS3']['_XYCoordinates'][0][1] +self._DesignParameter['_PMOSSET']['_XYCoordinates'][0][1]],
																				   [self._DesignParameter['_PMOSSET']['_XYCoordinates'][0][0] + self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_VIAPMOSPoly2Met1PMOS4']['_XYCoordinates'][0][0], self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_VIAPMOSPoly2Met1PMOS4']['_XYCoordinates'][0][1] +self._DesignParameter['_PMOSSET']['_XYCoordinates'][0][1]]
																				  ]

			del _tmpNumViaX


			self._DesignParameter['_Met1ForGates'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _XYCoordinates=[], _Width=400)
			self._DesignParameter['_Met1ForGates']['_Width'] = max(self._DesignParameter['_ViaMet12Met2OnNMOSGate1']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'], self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS3']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'])
			if _NMOSFinger != 1:
				self._DesignParameter['_Met1ForGates']['_XYCoordinates'] = [[[self._DesignParameter['_ViaMet12Met2OnNMOSGate1']['_XYCoordinates'][0][0], self.CeilMinSnapSpacing(self._DesignParameter['_ViaMet12Met2OnNMOSGate1']['_XYCoordinates'][0][1] + self._DesignParameter['_ViaMet12Met2OnNMOSGate1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // 2, MinSnapSpacing)], [self._DesignParameter['_ViaMet12Met2OnNMOSGate1']['_XYCoordinates'][0][0], self.CeilMinSnapSpacing(self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS3']['_XYCoordinates'][0][1] - self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS3']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // 2, MinSnapSpacing)]], \
																			[[self._DesignParameter['_ViaMet12Met2OnNMOSGate1']['_XYCoordinates'][1][0], self.CeilMinSnapSpacing(self._DesignParameter['_ViaMet12Met2OnNMOSGate1']['_XYCoordinates'][1][1] + self._DesignParameter['_ViaMet12Met2OnNMOSGate1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // 2, MinSnapSpacing)], [self._DesignParameter['_ViaMet12Met2OnNMOSGate1']['_XYCoordinates'][1][0], self.CeilMinSnapSpacing(self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS4']['_XYCoordinates'][0][1] - self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS4']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // 2, MinSnapSpacing)]]]
			else :
				self._DesignParameter['_Met1ForGates']['_XYCoordinates'] = [[[self._DesignParameter['_ViaMet12Met2OnNMOSGate1']['_XYCoordinates'][0][0], self.CeilMinSnapSpacing(self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS3']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS3']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // 2, MinSnapSpacing)], [self._DesignParameter['_ViaMet12Met2OnNMOSGate1']['_XYCoordinates'][0][0], self.CeilMinSnapSpacing(self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS3']['_XYCoordinates'][0][1] - self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS3']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // 2, MinSnapSpacing)]], \
																			[[self._DesignParameter['_ViaMet12Met2OnNMOSGate1']['_XYCoordinates'][1][0], self.CeilMinSnapSpacing(self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS4']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS4']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // 2, MinSnapSpacing)], [self._DesignParameter['_ViaMet12Met2OnNMOSGate1']['_XYCoordinates'][1][0], self.CeilMinSnapSpacing(self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS4']['_XYCoordinates'][0][1] - self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS4']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] // 2, MinSnapSpacing)]]]



			self._DesignParameter['_Met1ForNMOSGates5'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _XYCoordinates=[], _XWidth=400, _YWidth=400)
			self._DesignParameter['_Met1ForNMOSGates5']['_XWidth'] = max(self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS5']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'], self._DesignParameter['_ViaMet12Met2OnNMOSGate2']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'])
			self._DesignParameter['_Met1ForNMOSGates5']['_YWidth'] = max(self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS5']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'], self._DesignParameter['_ViaMet12Met2OnNMOSGate2']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'])
			self._DesignParameter['_Met1ForNMOSGates5']['_XYCoordinates'] = self._DesignParameter['_ViaMet12Met2OnNMOSGate2']['_XYCoordinates']

			self._DesignParameter['_Met1ForPMOSGates1'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _XYCoordinates=[], _XWidth=400, _YWidth=400)
			self._DesignParameter['_Met1ForPMOSGates1']['_XWidth'] = max(0, self._DesignParameter['_ViaMet12Met2OnPMOSGate2']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'])###max(self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_VIAPMOSPoly2Met1PMOS1']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'], self._DesignParameter['_ViaMet12Met2OnPMOSGate1']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'])
			self._DesignParameter['_Met1ForPMOSGates1']['_YWidth'] = max(self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_VIAPMOSPoly2Met1PMOS1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'], self._DesignParameter['_ViaMet12Met2OnPMOSGate2']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'])
			self._DesignParameter['_Met1ForPMOSGates1']['_XYCoordinates'] =  [[self._DesignParameter['_PMOSSET']['_XYCoordinates'][0][0] + self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_VIAPMOSPoly2Met1PMOS1']['_XYCoordinates'][0][0], self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_VIAPMOSPoly2Met1PMOS1']['_XYCoordinates'][0][1] +self._DesignParameter['_PMOSSET']['_XYCoordinates'][0][1]],
																			  [self._DesignParameter['_PMOSSET']['_XYCoordinates'][0][0] + self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_VIAPMOSPoly2Met1PMOS2']['_XYCoordinates'][0][0], self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_VIAPMOSPoly2Met1PMOS2']['_XYCoordinates'][0][1] +self._DesignParameter['_PMOSSET']['_XYCoordinates'][0][1]]
																				]

			self._DesignParameter['_Met1ForPMOSGates3'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _XYCoordinates=[], _XWidth=400, _YWidth=400)
			self._DesignParameter['_Met1ForPMOSGates3']['_XWidth'] = max(self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_VIAPMOSPoly2Met1PMOS3']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'], self._DesignParameter['_ViaMet12Met2OnPMOSGate1']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'])
			self._DesignParameter['_Met1ForPMOSGates3']['_YWidth'] = max(self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_VIAPMOSPoly2Met1PMOS3']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'], self._DesignParameter['_ViaMet12Met2OnPMOSGate1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'])
			self._DesignParameter['_Met1ForPMOSGates3']['_XYCoordinates'] = self._DesignParameter['_ViaMet12Met2OnPMOSGate1']['_XYCoordinates']



			## VIA2 Generation of Inner PMOS Drain and Inner NMOS Drain for PMOSSET, NMOSSET Connection
			_VIANMOSMet12 = copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation)

			_VIANMOSMet12['_ViaMet12Met2NumberOfCOX'] = 1

			_tmpNumY = int((_NMOSChannelWidth - 2 * _DRCObj._Metal1MinEnclosureVia12) // (_DRCObj._VIAxMinSpace + _DRCObj._VIAxMinWidth))
			if _tmpNumY < 1:
				_tmpNumY = 1

			_VIANMOSMet12['_ViaMet12Met2NumberOfCOY'] = _tmpNumY

			self._DesignParameter['_ViaMet12Met2OnNMOSOutput'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_DesignParameter=None, _Name='{}:ViaMet22Met3OnNMOSOutput'.format(_Name)))[0]
			self._DesignParameter['_ViaMet12Met2OnNMOSOutput']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(**_VIANMOSMet12)
			self._DesignParameter['_ViaMet12Met2OnNMOSOutput']['_XYCoordinates'] = [[self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_NMOS3']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_NMOS3']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][-1][0], self.CeilMinSnapSpacing(self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1] + _LengthbtwViaCentertoViaCenter // 4, MinSnapSpacing)],
																					[-(self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_NMOS3']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_NMOS3']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][-1][0]), self.CeilMinSnapSpacing(self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1] + _LengthbtwViaCentertoViaCenter // 4, MinSnapSpacing)]]


			_VIANMOSMet23 = copy.deepcopy(ViaMet22Met3._ViaMet22Met3._ParametersForDesignCalculation)

			_VIANMOSMet23['_ViaMet22Met3NumberOfCOX'] = 1

			_tmpNumY = int((_NMOSChannelWidth - 2 * _DRCObj._Metal1MinEnclosureVia12) // (_DRCObj._VIAxMinSpace + _DRCObj._VIAxMinWidth))
			if _tmpNumY < 1 :
				_tmpNumY = 1

			_VIANMOSMet23['_ViaMet22Met3NumberOfCOY'] = _tmpNumY


			self._DesignParameter['_ViaMet22Met3OnNMOSOutput'] = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_DesignParameter=None, _Name='{}:ViaMet12Met2OnNMOSOutput'.format(_Name)))[0]
			self._DesignParameter['_ViaMet22Met3OnNMOSOutput']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureX(**_VIANMOSMet23)
			self._DesignParameter['_ViaMet22Met3OnNMOSOutput']['_XYCoordinates'] = self._DesignParameter['_ViaMet12Met2OnNMOSOutput']['_XYCoordinates']


																				# [
																				#
																				#   [self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_NMOS3']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_NMOS3']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][-1][0],
																				#    self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1]],
																				#
																				#   [-(self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_NMOS3']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_NMOS3']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][-1][0]), \
																				#    self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1]
																				#   ]]

			if self._DesignParameter['_ViaMet22Met3OnNMOSOutput']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth'] * self._DesignParameter['_ViaMet22Met3OnNMOSOutput']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] < _DRCObj._MetalxMinArea :
				tmp1 = 2 * (self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_NMOS3']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0] - self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_NMOS3']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][0])
				tmp2 = tmp1 - self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_NMOS3']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] - 2 * _DRCObj._MetalxMinSpace2
				self._DesignParameter['_AdditionalMet2OnNMOSOutput'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _XYCoordinates=[], _XWidth=None, _YWidth=None)
				self._DesignParameter['_AdditionalMet2OnNMOSOutput']['_XWidth'] = tmp2
				self._DesignParameter['_AdditionalMet2OnNMOSOutput']['_YWidth'] = max(self.CeilMinSnapSpacing(_DRCObj._MetalxMinArea // tmp2, 2*MinSnapSpacing), self._DesignParameter['_ViaMet22Met3OnNMOSOutput']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'])
				self._DesignParameter['_AdditionalMet2OnNMOSOutput']['_XYCoordinates'] = [[self._DesignParameter['_ViaMet22Met3OnNMOSOutput']['_XYCoordinates'][0][0], self.CeilMinSnapSpacing(self._DesignParameter['_ViaMet22Met3OnNMOSOutput']['_XYCoordinates'][0][1] - self._DesignParameter['_AdditionalMet2OnNMOSOutput']['_YWidth'] // 2 + self._DesignParameter['_ViaMet22Met3OnNMOSOutput']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] // 2, MinSnapSpacing)], \
																						  [self._DesignParameter['_ViaMet22Met3OnNMOSOutput']['_XYCoordinates'][1][0], self.CeilMinSnapSpacing(self._DesignParameter['_ViaMet22Met3OnNMOSOutput']['_XYCoordinates'][1][1] - self._DesignParameter['_AdditionalMet2OnNMOSOutput']['_YWidth'] // 2 + self._DesignParameter['_ViaMet22Met3OnNMOSOutput']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] // 2, MinSnapSpacing)]]


			if self._DesignParameter['_ViaMet22Met3OnNMOSOutput']['_DesignObj']._DesignParameter['_Met3Layer']['_XWidth'] * self._DesignParameter['_ViaMet22Met3OnNMOSOutput']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth'] < _DRCObj._MetalxMinArea :
				self._DesignParameter['_ViaMet22Met3OnNMOSOutput']['_DesignObj']._DesignParameter['_Met3Layer']['_XWidth'] = self.CeilMinSnapSpacing(_DRCObj._MetalxMinArea // self._DesignParameter['_ViaMet22Met3OnNMOSOutput']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth'], 2*MinSnapSpacing)



			_VIAPMOSMet23 = copy.deepcopy(ViaMet22Met3._ViaMet22Met3._ParametersForDesignCalculation)
			_VIAPMOSMet23['_ViaMet22Met3NumberOfCOX'] = 1
			_tmpNumY = int(_PMOSChannelWidth // (_DRCObj._VIAxMinSpace + _DRCObj._VIAxMinWidth))
			if _tmpNumY < 2 :
				_tmpNumY = 2
			_VIAPMOSMet23['_ViaMet22Met3NumberOfCOY'] = _tmpNumY
			self._DesignParameter['_ViaMet22Met3OnPMOSOutput'] = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_DesignParameter=None, _Name='{}:ViaMet22Met3OnPMOSOutput'.format(_Name)))[0]
			self._DesignParameter['_ViaMet22Met3OnPMOSOutput']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureX(**_VIAPMOSMet23)
			self._DesignParameter['_ViaMet22Met3OnPMOSOutput']['_XYCoordinates'] = [[self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutput2']['_XYCoordinates'][_PMOSFinger // 2][0],
																				  self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutput2']['_XYCoordinates'][0][1] + self._DesignParameter['_PMOSSET']['_XYCoordinates'][0][1]], \
																					 [self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutput2']['_XYCoordinates'][_PMOSFinger // 2 + 1][0],
																				   self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutput2']['_XYCoordinates'][0][1] + self._DesignParameter['_PMOSSET']['_XYCoordinates'][0][1]]]

			if self._DesignParameter['_ViaMet22Met3OnPMOSOutput']['_DesignObj']._DesignParameter['_Met3Layer']['_XWidth'] * self._DesignParameter['_ViaMet22Met3OnPMOSOutput']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth'] < _DRCObj._MetalxMinArea :
				self._DesignParameter['_ViaMet22Met3OnPMOSOutput']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth'] = self.CeilMinSnapSpacing(_DRCObj._MetalxMinArea // self._DesignParameter['_ViaMet22Met3OnPMOSOutput']['_DesignObj']._DesignParameter['_Met3Layer']['_XWidth'], 2*MinSnapSpacing)



			# if self._DesignParameter['_ViaMet22Met3OnNMOSOutput']['_DesignObj']._DesignParameter['_Met3Layer']['_XWidth'] * self._DesignParameter['_ViaMet22Met3OnNMOSOutput']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth'] :
			#     self._DesignParameter['_AdditionalMet3forArea'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0], _Datatype=DesignParameters._LayerMapping['METAL3'][1], _XYCoordinates=[], _XWidth=400, _YWidth=400)
			#     self._DesignParameter['_AdditionalMet3forArea']['_XWidth'] = self._DesignParameter['_ViaMet22Met3OnNMOSOutput']['_DesignObj']._DesignParameter['_Met3Layer']['_XWidth']
			#     self._DesignParameter['_AdditionalMet3forArea']['_YWidth'] = self.CeilMinSnapSpacing(_DRCObj._MetalxMinArea // self._DesignParameter['_ViaMet22Met3OnNMOSOutput']['_DesignObj']._DesignParameter['_Met3Layer']['_XWidth'], 2 * MinSnapSpacing)
			#     self._DesignParameter['_AdditionalMet3forArea']['_XYCoordinates'] = [self._DesignParameter['_ViaMet22Met3OnPMOSOutput']['_XYCoordinates'][0], self._DesignParameter['_ViaMet22Met3OnPMOSOutput']['_XYCoordinates'][1]]



			## VIA3 Generation of Inner PMOS Drain and Inner NMOS Drain for PMOSSET, NMOSSET Connection
			_VIANMOSMet34 = copy.deepcopy(ViaMet32Met4._ViaMet32Met4._ParametersForDesignCalculation)

			_VIANMOSMet34['_ViaMet32Met4NumberOfCOX'] = 1

			_tmpNumY = int((_NMOSChannelWidth - 2 * _DRCObj._Metal1MinEnclosureVia12) // (_DRCObj._VIAxMinSpace + _DRCObj._VIAxMinWidth))
			if _tmpNumY < 2 :
				_tmpNumY = 2

			_VIANMOSMet34['_ViaMet32Met4NumberOfCOY'] = _tmpNumY


			self._DesignParameter['_ViaMet32Met4OnNMOSOutput'] = self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_DesignParameter=None, _Name='{}:ViaMet32Met4OnNMOSOutput'.format(_Name)))[0]
			self._DesignParameter['_ViaMet32Met4OnNMOSOutput']['_DesignObj']._CalculateViaMet32Met4DesignParameterMinimumEnclosureX(**_VIANMOSMet34)
			self._DesignParameter['_ViaMet32Met4OnNMOSOutput']['_XYCoordinates'] = [[self._DesignParameter['_ViaMet22Met3OnNMOSOutput']['_XYCoordinates'][0][0], self.CeilMinSnapSpacing(self._DesignParameter['_ViaMet22Met3OnNMOSOutput']['_XYCoordinates'][0][1] + _DRCObj._MetalxMinSpace // 2, MinSnapSpacing)],\
																					[self._DesignParameter['_ViaMet22Met3OnNMOSOutput']['_XYCoordinates'][1][0], self.CeilMinSnapSpacing(self._DesignParameter['_ViaMet22Met3OnNMOSOutput']['_XYCoordinates'][1][1] + _DRCObj._MetalxMinSpace // 2, MinSnapSpacing)]]

			if self._DesignParameter['_ViaMet32Met4OnNMOSOutput']['_DesignObj']._DesignParameter['_Met3Layer']['_XWidth'] * self._DesignParameter['_ViaMet32Met4OnNMOSOutput']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth'] < _DRCObj._MetalxMinArea :
				self._DesignParameter['_ViaMet32Met4OnNMOSOutput']['_DesignObj']._DesignParameter['_Met3Layer']['_XWidth'] = self.CeilMinSnapSpacing(_DRCObj._MetalxMinArea // self._DesignParameter['_ViaMet32Met4OnNMOSOutput']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth'], 2*MinSnapSpacing)


																				# [
																				#
																				#   [self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_NMOS3']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_NMOS3']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][-1][0],
																				#    self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1]],
																				#
																				#
																				#
																				#   [-(self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_NMOS3']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_NMOS3']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][-1][0]), \
																				#    self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1]
																				#   ]]
																				# #



			# if (self._DesignParameter['_ViaMet12Met2OnNMOSOutput']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth'] * self._DesignParameter['_ViaMet12Met2OnNMOSOutput']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] < _DRCObj._MetalxMinArea) :
			#
			#     _LengthNMOSSpaceBtwMet1 = _DRCObj.DRCPolygateMinSpace(_DRCObj._CoMinWidth + 2 * _DRCObj._PolygateMinSpace2Co) + _ChannelLength - _DRCObj._Metal1MinWidth
			#     _SpaceMet12Met1 = 2 * _LengthNMOSSpaceBtwMet1 + _DRCObj._Metal1MinWidth
			#
			#     self._DesignParameter['_Met2OnNMOS4forArea'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _XYCoordinates=[], _XWidth=400, _YWidth=400)
			#     self._DesignParameter['_Met2OnNMOS4forArea']['_XWidth'] = _SpaceMet12Met1 - 2 * _DRCObj._MetalxMinSpace2
			#     self._DesignParameter['_Met2OnNMOS4forArea']['_YWidth'] = self.CeilMinSnapSpacing(_DRCObj._MetalxMinArea // self._DesignParameter['_Met2OnNMOS4forArea']['_XWidth'], MinSnapSpacing)
			#     self._DesignParameter['_Met2OnNMOS4forArea']['_XYCoordinates'] = [[self._DesignParameter['_ViaMet12Met2OnNMOSOutput']['_XYCoordinates'][0][0], self.CeilMinSnapSpacing(self._DesignParameter['_ViaMet12Met2OnNMOSOutput']['_XYCoordinates'][0][1] - self._DesignParameter['_Met2OnNMOS4forArea']['_YWidth'] // 2 + self._DesignParameter['_ViaMet12Met2OnNMOSOutput']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] // 2, MinSnapSpacing)], \
			#                                                                       [self._DesignParameter['_ViaMet12Met2OnNMOSOutput']['_XYCoordinates'][1][0], self.CeilMinSnapSpacing(self._DesignParameter['_ViaMet12Met2OnNMOSOutput']['_XYCoordinates'][0][1] - self._DesignParameter['_Met2OnNMOS4forArea']['_YWidth'] // 2 + self._DesignParameter['_ViaMet12Met2OnNMOSOutput']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] // 2, MinSnapSpacing)]]
			#
			#     self._DesignParameter['_Met3OnNMOS4forArea'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0], _Datatype=DesignParameters._LayerMapping['METAL3'][1], _XYCoordinates=[], _XWidth=400, _YWidth=400)
			#     self._DesignParameter['_Met3OnNMOS4forArea']['_XWidth'] = _SpaceMet12Met1 - 2 * _DRCObj._MetalxMinSpace2
			#     self._DesignParameter['_Met3OnNMOS4forArea']['_YWidth'] = self.CeilMinSnapSpacing(_DRCObj._MetalxMinArea // self._DesignParameter['_Met2OnNMOS4forArea']['_XWidth'], MinSnapSpacing)
			#     self._DesignParameter['_Met3OnNMOS4forArea']['_XYCoordinates'] = self._DesignParameter['_Met2OnNMOS4forArea']['_XYCoordinates']












			_VIAPMOSMet34 = copy.deepcopy(ViaMet32Met4._ViaMet32Met4._ParametersForDesignCalculation)
			_VIAPMOSMet34['_ViaMet32Met4NumberOfCOX'] = 1
			_tmpNumY = int(_PMOSChannelWidth // (_DRCObj._VIAxMinSpace + _DRCObj._VIAxMinWidth))
			if _tmpNumY < 2 :
				_tmpNumY = 2
			_VIAPMOSMet34['_ViaMet32Met4NumberOfCOY'] = _tmpNumY
			self._DesignParameter['_ViaMet32Met4OnPMOSOutput'] = self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_DesignParameter=None, _Name='{}:ViaMet32Met4OnPMOSOutput'.format(_Name)))[0]
			self._DesignParameter['_ViaMet32Met4OnPMOSOutput']['_DesignObj']._CalculateViaMet32Met4DesignParameterMinimumEnclosureX(**_VIAPMOSMet34)
			self._DesignParameter['_ViaMet32Met4OnPMOSOutput']['_XYCoordinates'] = [[self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutput2']['_XYCoordinates'][_PMOSFinger // 2][0],
																				   self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutput2']['_XYCoordinates'][0][1]\
																				   + self._DesignParameter['_PMOSSET']['_XYCoordinates'][0][1]], \

																				   [self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutput2']['_XYCoordinates'][_PMOSFinger // 2 + 1][0],
																					self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutput2']['_XYCoordinates'][0][1] \
																					+ self._DesignParameter['_PMOSSET']['_XYCoordinates'][0][1]]
																				   ]








			## VIA2 Generation of Outer PMOS and NMOS for CLK routing Connection
			_VIAPMOSMet23CLKinput = copy.deepcopy(ViaMet22Met3._ViaMet22Met3._ParametersForDesignCalculation)
			_tmpNumViaX = int(self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_VIAPMOSPoly2Met1PMOS1']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace))
			if _tmpNumViaX < 2 :
				_tmpNumViaX = 2

			_VIAPMOSMet23CLKinput['_ViaMet22Met3NumberOfCOX'] = _tmpNumViaX
			_VIAPMOSMet23CLKinput['_ViaMet22Met3NumberOfCOY'] = 1

			self._DesignParameter['_ViaMet22Met3OnPMOSCLKInput'] = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_DesignParameter=None, _Name='{}:ViaMet22Met3OnPMOSCLKInput'.format(_Name)))[0]
			self._DesignParameter['_ViaMet22Met3OnPMOSCLKInput']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureY(**_VIAPMOSMet23CLKinput)
			self._DesignParameter['_ViaMet22Met3OnPMOSCLKInput']['_XYCoordinates'] = [[self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_VIAPMOSPoly2Met1PMOS1']['_XYCoordinates'][0][0]
																				   + self._DesignParameter['_PMOSSET']['_XYCoordinates'][0][0],
																				   self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_VIAPMOSPoly2Met1PMOS1']['_XYCoordinates'][0][1] \
																				   + self._DesignParameter['_PMOSSET']['_XYCoordinates'][0][1]],

																				  [self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_VIAPMOSPoly2Met1PMOS2']['_XYCoordinates'][0][0]
																				   + self._DesignParameter['_PMOSSET']['_XYCoordinates'][0][0],
																				   self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_VIAPMOSPoly2Met1PMOS2']['_XYCoordinates'][0][1] \
																				   + self._DesignParameter['_PMOSSET']['_XYCoordinates'][0][1]]]
			del _tmpNumViaX
			print('x')

			_VIANMOSMet23CLKinput = copy.deepcopy(ViaMet22Met3._ViaMet22Met3._ParametersForDesignCalculation)
			_tmpNumViaX = int(self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS5']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace))
			if _tmpNumViaX < 2:
				_tmpNumViaX = 2

			_VIANMOSMet23CLKinput['_ViaMet22Met3NumberOfCOX'] = _tmpNumViaX
			_VIANMOSMet23CLKinput['_ViaMet22Met3NumberOfCOY'] = 1

			self._DesignParameter['_ViaMet22Met3OnNMOSCLKInput'] = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_DesignParameter=None, _Name='{}:ViaMet22Met3OnNMOSCLKInput'.format(_Name)))[0]
			self._DesignParameter['_ViaMet22Met3OnNMOSCLKInput']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureY(**_VIANMOSMet23CLKinput)
			self._DesignParameter['_ViaMet22Met3OnNMOSCLKInput']['_XYCoordinates'] = [self._DesignParameter['_ViaMet12Met2OnNMOSGate2']['_XYCoordinates'][0]


																				 ]
			del _tmpNumViaX

			_LengthbtwViaCentertoViaCenter = _DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace
			_VIANMOSMet23input = copy.deepcopy(ViaMet22Met3._ViaMet22Met3._ParametersForDesignCalculation)

			if _DATAinputNMOSFinger > 1:
				_tmpNumViaX = int(self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS1']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace)) + 1
				if _tmpNumViaX < 2:
					_tmpNumViaX = 2

				_VIANMOSMet23input['_ViaMet22Met3NumberOfCOX'] = _tmpNumViaX
				_VIANMOSMet23input['_ViaMet22Met3NumberOfCOY'] = 1

				self._DesignParameter['_ViaMet22Met3OnNMOSInput'] = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_DesignParameter=None, _Name='{}:ViaMet22Met3OnNMOSInput'.format(_Name)))[0]
				self._DesignParameter['_ViaMet22Met3OnNMOSInput']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureY(**_VIANMOSMet23input)
				self._DesignParameter['_ViaMet22Met3OnNMOSInput']['_XYCoordinates'] = [[self.CeilMinSnapSpacing(self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS1']['_XYCoordinates'][0][0] - _DRCObj._MetalxMinSpace3 // 2, MinSnapSpacing), \
																					self.CeilMinSnapSpacing(self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_NMOS1']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnNMOSOutput1']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] // 2 + _LengthbtwViaCentertoViaCenter // 4 + _DRCObj._MetalxMinWidth // 2, MinSnapSpacing)],
																					[self.CeilMinSnapSpacing(self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS2']['_XYCoordinates'][0][0] + _DRCObj._MetalxMinSpace3 // 2, MinSnapSpacing), \
																					 self.CeilMinSnapSpacing(self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_NMOS1']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnNMOSOutput1']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] // 2 + _LengthbtwViaCentertoViaCenter // 4 + _DRCObj._MetalxMinWidth // 2, MinSnapSpacing)], \
																					   ]
				del _tmpNumViaX

			elif _DATAinputNMOSFinger == 1 :
				_VIANMOSMet23input['_ViaMet22Met3NumberOfCOX'] = 2
				_VIANMOSMet23input['_ViaMet22Met3NumberOfCOY'] = 1

				self._DesignParameter['_ViaMet22Met3OnNMOSInput'] = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_DesignParameter=None, _Name='{}:ViaMet22Met3OnNMOSInput'.format(_Name)))[0]
				self._DesignParameter['_ViaMet22Met3OnNMOSInput']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureY(**_VIANMOSMet23input)
				self._DesignParameter['_ViaMet22Met3OnNMOSInput']['_XYCoordinates'] = [[self.CeilMinSnapSpacing(self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS1']['_XYCoordinates'][0][0] - self._DesignParameter['_ViaMet22Met3OnNMOSInput']['_DesignObj']._DesignParameter['_Met3Layer']['_XWidth'] // 2, MinSnapSpacing), \
																					self.CeilMinSnapSpacing(self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_NMOS1']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnNMOSOutput1']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] // 2 + _LengthbtwViaCentertoViaCenter // 4 + _DRCObj._MetalxMinWidth // 2, MinSnapSpacing)],
																					[self.CeilMinSnapSpacing(self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS2']['_XYCoordinates'][0][0] + self._DesignParameter['_ViaMet22Met3OnNMOSInput']['_DesignObj']._DesignParameter['_Met3Layer']['_XWidth'] // 2, MinSnapSpacing), \
																					 self.CeilMinSnapSpacing(self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_NMOS1']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnNMOSOutput1']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] // 2 + _LengthbtwViaCentertoViaCenter // 4 + _DRCObj._MetalxMinWidth // 2, MinSnapSpacing)]
																					]





			del _VIANMOSMet23input



			print('x')

			#####################################################################################################################################################
			########################################################### PMOS Met2 Routing #######################################################################
			#####################################################################################################################################################

			########################################### CLK input PMOS1 Btw Drains Connection ############################################
			self._DesignParameter['_Met2PMOS1'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _XYCoordinates=[], _Width=400)
			self._DesignParameter['_Met2PMOS1']['_Width'] = _DRCObj._MetalxMinWidth
			# _LengthPMOSBtwMet1 = _DRCObj.DRCPolygateMinSpace(_DRCObj._CoMinWidth + 2 * _DRCObj._PolygateMinSpace2Co) + self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']

			if DesignParameters._Technology == '028nm':
				_LengthPMOSBtwMet1 = _DRCObj.DRCPolyMinSpace(_Width=_PMOSChannelWidth, _ParallelLength=_ChannelLength) + self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
			else:
				_LengthPMOSBtwMet1 = _DRCObj.DRCPolygateMinSpace(_DRCObj._CoMinWidth + 2 * _DRCObj._PolygateMinSpace2Co) + self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']


			if (_CLKinputPMOSFinger1 % 2) == 0:
				k = int(_CLKinputPMOSFinger1//2)
			elif (_CLKinputPMOSFinger1 % 2) == 1:
				k = int((float(_CLKinputPMOSFinger1)//float(2)) + 0.5)

			if (_CLKinputPMOSFinger1 % 2) == 1 and (_CLKinputPMOSFinger1 != 1):
				self._DesignParameter['_Met2PMOS1']['_XYCoordinates'] = [
																		 [
																		  [self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutput1']['_XYCoordinates'][0][0],
																		   self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutput1']['_XYCoordinates'][0][1]+self._DesignParameter['_PMOSSET']['_XYCoordinates'][0][1]],
																		  [self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutput1']['_XYCoordinates'][k-1][0],
																		   self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutput1']['_XYCoordinates'][0][1]+self._DesignParameter['_PMOSSET']['_XYCoordinates'][0][1]] # Right
																		 ],
																		 [
																		  [self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutput1']['_XYCoordinates'][-1][0],
																		   self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutput1']['_XYCoordinates'][-1][1] + self._DesignParameter['_PMOSSET']['_XYCoordinates'][0][1]],
																		  [self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutput1']['_XYCoordinates'][-1][0] - _LengthPMOSBtwMet1 * (_CLKinputPMOSFinger1 - 1),
																		   self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutput1']['_XYCoordinates'][-1][1] + self._DesignParameter['_PMOSSET']['_XYCoordinates'][0][1]] # Right
																		 ]
																		]
			elif (_CLKinputPMOSFinger1 % 2) == 1 and (_CLKinputPMOSFinger1 == 1):
				self._DesignParameter['_Met2PMOS1']['_XYCoordinates'] = [
																		 [
																		  [self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutput1']['_XYCoordinates'][-1][0],
																		   self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutput1']['_XYCoordinates'][-1][1] + self._DesignParameter['_PMOSSET']['_XYCoordinates'][0][1]],
																		  [self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutput1']['_XYCoordinates'][-1][0] - _LengthPMOSBtwMet1 * (_CLKinputPMOSFinger1 - 1),
																		   self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutput1']['_XYCoordinates'][-1][1] + self._DesignParameter['_PMOSSET']['_XYCoordinates'][0][1]] # Right
																		 ]
																		]

			elif (_CLKinputPMOSFinger1 % 2) == 0:
				self._DesignParameter['_Met2PMOS1']['_XYCoordinates'] = [
																		 [
																		  [self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutput1']['_XYCoordinates'][0][0],
																		   self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutput1']['_XYCoordinates'][0][1] + self._DesignParameter['_PMOSSET']['_XYCoordinates'][0][1]],
																		  [self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutput1']['_XYCoordinates'][0][0] + _LengthPMOSBtwMet1 * (_CLKinputPMOSFinger1-1) - _LengthPMOSBtwMet1,
																		   self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutput1']['_XYCoordinates'][0][1] + self._DesignParameter['_PMOSSET']['_XYCoordinates'][0][1]]  # CLK input Right PMOS Drain Connection
																		 ],
																		 [
																		  [self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutput1']['_XYCoordinates'][-1][0],
																		   self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutput1']['_XYCoordinates'][-1][1] + self._DesignParameter['_PMOSSET']['_XYCoordinates'][0][1]],
																		  [self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutput1']['_XYCoordinates'][-1][0] - _LengthPMOSBtwMet1 * (_CLKinputPMOSFinger1-1)+ _LengthPMOSBtwMet1,
																		   self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutput1']['_XYCoordinates'][-1][1] + self._DesignParameter['_PMOSSET']['_XYCoordinates'][0][1]]  # CLK input Left PMOS Drain Connection
																		 ]
																		]
			print('x')

			self._DesignParameter['_Met3PMOS1'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0], _Datatype=DesignParameters._LayerMapping['METAL3'][1], _XYCoordinates=[], _Width=400)
			self._DesignParameter['_Met3PMOS1']['_Width'] = _DRCObj._MetalxMinWidth
			# _LengthPMOSBtwMet1 = _DRCObj.DRCPolygateMinSpace(_DRCObj._CoMinWidth + 2 * _DRCObj._PolygateMinSpace2Co) + self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']

			if DesignParameters._Technology == '028nm':
				_LengthPMOSBtwMet1 = _DRCObj.DRCPolyMinSpace(_Width=_PMOSChannelWidth, _ParallelLength=_ChannelLength) + self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
			else:
				_LengthPMOSBtwMet1 = _DRCObj.DRCPolygateMinSpace(_DRCObj._CoMinWidth + 2 * _DRCObj._PolygateMinSpace2Co) + self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']

			if (_CLKinputPMOSFinger1 % 2) == 0:
				k = int(_CLKinputPMOSFinger1//2)
			elif (_CLKinputPMOSFinger1 % 2) == 1:
				k = int((float(_CLKinputPMOSFinger1)//float(2)) + 0.5)

			if ((_CLKinputPMOSFinger1 % 2) == 1) and (_CLKinputPMOSFinger1 != 1):
				self._DesignParameter['_Met3PMOS1']['_XYCoordinates'] = [
																		 [
																		  [self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutput1']['_XYCoordinates'][0][0],
																		   self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutput1']['_XYCoordinates'][0][1]+self._DesignParameter['_PMOSSET']['_XYCoordinates'][0][1]],
																		  [self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutput1']['_XYCoordinates'][k-1][0],
																		   self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutput1']['_XYCoordinates'][0][1]+self._DesignParameter['_PMOSSET']['_XYCoordinates'][0][1]] # Right
																		 ],
																		 [
																		  [self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutput1']['_XYCoordinates'][-1][0],
																		   self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutput1']['_XYCoordinates'][-1][1] + self._DesignParameter['_PMOSSET']['_XYCoordinates'][0][1]],
																		  [self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutput1']['_XYCoordinates'][-1][0] - _LengthPMOSBtwMet1 * (_CLKinputPMOSFinger1 - 1),
																		   self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutput1']['_XYCoordinates'][-1][1] + self._DesignParameter['_PMOSSET']['_XYCoordinates'][0][1]] # Right
																			]
																		]

			elif ((_CLKinputPMOSFinger1 % 2) == 1) and (_CLKinputPMOSFinger1 == 1):
				self._DesignParameter['_Met3PMOS1']['_XYCoordinates'] = [

																		 [
																		  [self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutput1']['_XYCoordinates'][-1][0],
																		   self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutput1']['_XYCoordinates'][-1][1] + self._DesignParameter['_PMOSSET']['_XYCoordinates'][0][1]],
																		  [self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutput1']['_XYCoordinates'][-1][0] - _LengthPMOSBtwMet1 * (_CLKinputPMOSFinger1 - 1),
																		   self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutput1']['_XYCoordinates'][-1][1] + self._DesignParameter['_PMOSSET']['_XYCoordinates'][0][1]] # Right
																		 ]
																		]

			elif (_CLKinputPMOSFinger1 % 2) == 0:
				self._DesignParameter['_Met3PMOS1']['_XYCoordinates'] = [
																		 [
																		  [self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutput1']['_XYCoordinates'][0][0],
																		   self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutput1']['_XYCoordinates'][0][1] + self._DesignParameter['_PMOSSET']['_XYCoordinates'][0][1]],
																		  [self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutput1']['_XYCoordinates'][0][0] + _LengthPMOSBtwMet1 * (_CLKinputPMOSFinger1-1) - _LengthPMOSBtwMet1,
																		   self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutput1']['_XYCoordinates'][0][1] + self._DesignParameter['_PMOSSET']['_XYCoordinates'][0][1]]  # CLK input Right PMOS Drain Connection
																		 ],
																		 [
																		  [self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutput1']['_XYCoordinates'][-1][0],
																		   self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutput1']['_XYCoordinates'][-1][1] + self._DesignParameter['_PMOSSET']['_XYCoordinates'][0][1]],
																		  [self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutput1']['_XYCoordinates'][-1][0] - _LengthPMOSBtwMet1 * (_CLKinputPMOSFinger1-1)+ _LengthPMOSBtwMet1,
																		   self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutput1']['_XYCoordinates'][-1][1] + self._DesignParameter['_PMOSSET']['_XYCoordinates'][0][1]]  # CLK input Left PMOS Drain Connection
																		 ]
																		]
			print('x')

			self._DesignParameter['_Met4PMOS1'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL4'][0], _Datatype=DesignParameters._LayerMapping['METAL4'][1], _XYCoordinates=[], _Width=400)
			self._DesignParameter['_Met4PMOS1']['_Width'] = _DRCObj._MetalxMinWidth
			# _LengthPMOSBtwMet1 = _DRCObj.DRCPolygateMinSpace(_DRCObj._CoMinWidth + 2 * _DRCObj._PolygateMinSpace2Co) + self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
			if DesignParameters._Technology == '028nm':
				_LengthPMOSBtwMet1 = _DRCObj.DRCPolyMinSpace(_Width=_PMOSChannelWidth, _ParallelLength=_ChannelLength) + self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
			else:
				_LengthPMOSBtwMet1 = _DRCObj.DRCPolygateMinSpace(_DRCObj._CoMinWidth + 2 * _DRCObj._PolygateMinSpace2Co) + self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_PMOS1']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']

			if (_CLKinputPMOSFinger1 % 2) == 0:
				k = int(_CLKinputPMOSFinger1 // 2)
			elif (_CLKinputPMOSFinger1 % 2) == 1:
				k = int((float(_CLKinputPMOSFinger1) // float(2)) + 0.5)

			if ((_CLKinputPMOSFinger1 % 2) == 1) and (_CLKinputPMOSFinger1 != 1):
				self._DesignParameter['_Met4PMOS1']['_XYCoordinates'] = [
					[
						[self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutput1'][
							 '_XYCoordinates'][0][0],
						 self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutput1'][
							 '_XYCoordinates'][0][1] + self._DesignParameter['_PMOSSET']['_XYCoordinates'][0][1]],
						[self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutput1'][
							 '_XYCoordinates'][k - 1][0],
						 self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutput1'][
							 '_XYCoordinates'][0][1] + self._DesignParameter['_PMOSSET']['_XYCoordinates'][0][1]]
						# Right
					],
					[
						[self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutput1'][
							 '_XYCoordinates'][-1][0],
						 self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutput1'][
							 '_XYCoordinates'][-1][1] + self._DesignParameter['_PMOSSET']['_XYCoordinates'][0][1]],
						[self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutput1'][
							 '_XYCoordinates'][-1][0] - _LengthPMOSBtwMet1 * (_CLKinputPMOSFinger1 - 1),
						 self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutput1'][
							 '_XYCoordinates'][-1][1] + self._DesignParameter['_PMOSSET']['_XYCoordinates'][0][1]]
						# Right
					]
				]
			elif ((_CLKinputPMOSFinger1 % 2) == 1) and (_CLKinputPMOSFinger1 == 1):
				self._DesignParameter['_Met4PMOS1']['_XYCoordinates'] = [
					[

					[
						[self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutput1'][
							 '_XYCoordinates'][-1][0],
						 self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutput1'][
							 '_XYCoordinates'][-1][1] + self._DesignParameter['_PMOSSET']['_XYCoordinates'][0][1]],
						[self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutput1'][
							 '_XYCoordinates'][-1][0] - _LengthPMOSBtwMet1 * (_CLKinputPMOSFinger1 - 1),
						 self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutput1'][
							 '_XYCoordinates'][-1][1] + self._DesignParameter['_PMOSSET']['_XYCoordinates'][0][1]]
						# Right
					]
				]]

			elif (_CLKinputPMOSFinger1 % 2) == 0:
				self._DesignParameter['_Met4PMOS1']['_XYCoordinates'] = [
																		 [
																		  [self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutput1']['_XYCoordinates'][0][0],
																		   self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutput1']['_XYCoordinates'][0][1] + self._DesignParameter['_PMOSSET']['_XYCoordinates'][0][1]],
																		  [self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutput1']['_XYCoordinates'][0][0] + _LengthPMOSBtwMet1 * (_CLKinputPMOSFinger1 - 1) - _LengthPMOSBtwMet1,
																		   self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutput1']['_XYCoordinates'][0][1] + self._DesignParameter['_PMOSSET']['_XYCoordinates'][0][1]]
						# CLK input Right PMOS Drain Connection
					],
					[
						[self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutput1']['_XYCoordinates'][-1][0],
						 self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutput1']['_XYCoordinates'][-1][1] + self._DesignParameter['_PMOSSET']['_XYCoordinates'][0][1]],
						[self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutput1']['_XYCoordinates'][-1][0] - _LengthPMOSBtwMet1 * (_CLKinputPMOSFinger1 - 1) + _LengthPMOSBtwMet1,
						 self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutput1']['_XYCoordinates'][-1][1] + self._DesignParameter['_PMOSSET']['_XYCoordinates'][0][1]]
						# CLK input Left PMOS Drain Connection
					]
				]
			print('x')


			################################################# Inner CLK input PMOS2 Drain --- Inner PMOS Drain Connection ###############################################
			self._DesignParameter['_Met2PMOS2'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _XYCoordinates=[], _Width=400)
			self._DesignParameter['_Met2PMOS2']['_Width'] = _DRCObj._MetalxMinWidth
			k = len(self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutput1']['_XYCoordinates'])
			j = len(self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutput2']['_XYCoordinates'])

			print('x')

			if (_CLKinputPMOSFinger2 % 2) == 1:
				self._DesignParameter['_Met2PMOS2']['_XYCoordinates'] = [
																		 [
																		  [self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutput1']['_XYCoordinates'][int((k//2)-1)][0] - _LengthPMOSBtwMet1 * (_CLKinputPMOSFinger2 - 1),
																		   self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutput1']['_XYCoordinates'][0][1] + self._DesignParameter['_PMOSSET']['_XYCoordinates'][0][1]],
																		  [self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutput2']['_XYCoordinates'][int((j // 2) - 1)][0],
																		   self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutput1']['_XYCoordinates'][0][1] + self._DesignParameter['_PMOSSET']['_XYCoordinates'][0][1]]
																		 ],
																		 [
																		  [self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutput1']['_XYCoordinates'][int((k // 2))][0] + _LengthPMOSBtwMet1 * (_CLKinputPMOSFinger2 - 1),
																		   self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutput1']['_XYCoordinates'][0][1] + self._DesignParameter['_PMOSSET']['_XYCoordinates'][0][1]],
																		  [self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutput2']['_XYCoordinates'][int((j // 2))][0],
																		   self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutput1']['_XYCoordinates'][0][1] + self._DesignParameter['_PMOSSET']['_XYCoordinates'][0][1]]
																		 ]
																		]
			elif (_CLKinputPMOSFinger2 % 2) == 0:
				self._DesignParameter['_Met2PMOS2']['_XYCoordinates'] = [
																		 [
																		  [self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutput1']['_XYCoordinates'][int((k//2)-1)][0] - _LengthPMOSBtwMet1 * (_CLKinputPMOSFinger2 - 2),
																		   self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutput1']['_XYCoordinates'][0][1] + self._DesignParameter['_PMOSSET']['_XYCoordinates'][0][1]],
																		  [self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutput2']['_XYCoordinates'][int((j//2)-1)][0],
																		   self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutput1']['_XYCoordinates'][0][1] + self._DesignParameter['_PMOSSET']['_XYCoordinates'][0][1]]
																		 ],
																		 [
																		  [self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutput1']['_XYCoordinates'][int((k//2))][0] + _LengthPMOSBtwMet1 * (_CLKinputPMOSFinger2 - 2),
																		   self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutput1']['_XYCoordinates'][0][1] + self._DesignParameter['_PMOSSET']['_XYCoordinates'][0][1]],
																		  [self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutput2']['_XYCoordinates'][int((j//2))][0],
																		   self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnPMOSOutput1']['_XYCoordinates'][0][1] + self._DesignParameter['_PMOSSET']['_XYCoordinates'][0][1]]
																		 ]
																		]


			######################################################################################################################################################################
			########################################################################### Met3 Routing #############################################################################
			######################################################################################################################################################################
			################################################ Met3 Routing Generation for CLK input PMOS2 --- Inner PMOS Connection ###############################################
			PMOS_bottomtmp = self._DesignParameter['_PMOSSET']['_XYCoordinates'][0][1] + self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['PMOS_bottomtmp']['_Ignore']
			NMOS_toptmp = self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['NMOS_toptmp']['_Ignore']

			self._DesignParameter['_Met4PNMOS'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL4'][0], _Datatype=DesignParameters._LayerMapping['METAL4'][1], _XYCoordinates=[], _Width=400)
			self._DesignParameter['_Met4PNMOS']['_Width'] = 2 * _DRCObj._MetalxMinWidth

			self._DesignParameter['_Met4PNMOS']['_XYCoordinates'] = [[[self._DesignParameter['_ViaMet32Met4OnPMOSOutput']['_XYCoordinates'][0][0], self.CeilMinSnapSpacing(self._DesignParameter['_ViaMet32Met4OnPMOSOutput']['_XYCoordinates'][0][1] + self._DesignParameter['_ViaMet32Met4OnPMOSOutput']['_DesignObj']._DesignParameter['_Met4Layer']['_YWidth'] // 2, MinSnapSpacing)],
																	  [self._DesignParameter['_ViaMet32Met4OnPMOSOutput']['_XYCoordinates'][0][0], self.CeilMinSnapSpacing((PMOS_bottomtmp + NMOS_toptmp) // 2, MinSnapSpacing)],
																	  [self._DesignParameter['_ViaMet32Met4OnNMOSOutput']['_XYCoordinates'][0][0], self.CeilMinSnapSpacing((PMOS_bottomtmp + NMOS_toptmp) // 2, MinSnapSpacing)],
																	  [self._DesignParameter['_ViaMet32Met4OnNMOSOutput']['_XYCoordinates'][0][0], self.CeilMinSnapSpacing(self._DesignParameter['_ViaMet32Met4OnNMOSOutput']['_XYCoordinates'][0][1] - self._DesignParameter['_ViaMet32Met4OnNMOSOutput']['_DesignObj']._DesignParameter['_Met4Layer']['_YWidth'] // 2, MinSnapSpacing)]],
																	[[self._DesignParameter['_ViaMet32Met4OnPMOSOutput']['_XYCoordinates'][1][0], self.CeilMinSnapSpacing(self._DesignParameter['_ViaMet32Met4OnPMOSOutput']['_XYCoordinates'][1][1] + self._DesignParameter['_ViaMet32Met4OnPMOSOutput']['_DesignObj']._DesignParameter['_Met4Layer']['_YWidth'] // 2, MinSnapSpacing)],
																	  [self._DesignParameter['_ViaMet32Met4OnPMOSOutput']['_XYCoordinates'][1][0], self.CeilMinSnapSpacing((PMOS_bottomtmp + NMOS_toptmp) // 2, MinSnapSpacing)],
																	  [self._DesignParameter['_ViaMet32Met4OnNMOSOutput']['_XYCoordinates'][1][0], self.CeilMinSnapSpacing((PMOS_bottomtmp + NMOS_toptmp) // 2, MinSnapSpacing)],
																	  [self._DesignParameter['_ViaMet32Met4OnNMOSOutput']['_XYCoordinates'][1][0], self.CeilMinSnapSpacing(self._DesignParameter['_ViaMet32Met4OnNMOSOutput']['_XYCoordinates'][1][1] - self._DesignParameter['_ViaMet32Met4OnNMOSOutput']['_DesignObj']._DesignParameter['_Met4Layer']['_YWidth'] // 2, MinSnapSpacing)]]]
			################################################ Met3 Routing Generation for CLK input // Outer PMOS1---PMOS2---NMOS5 ###############################################
			self._DesignParameter['_Met3CLKinput'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0], _Datatype=DesignParameters._LayerMapping['METAL3'][1], _XYCoordinates=[], _Width=400)
			self._DesignParameter['_Met3CLKinput']['_Width'] = 2 * _DRCObj._MetalxMinWidth
			self._DesignParameter['_Met3CLKinput']['_XYCoordinates'] = [[[self.CeilMinSnapSpacing(self._DesignParameter['_ViaMet22Met3OnPMOSCLKInput']['_XYCoordinates'][0][0] - self._DesignParameter['_ViaMet22Met3OnPMOSCLKInput']['_DesignObj']._DesignParameter['_Met3Layer']['_XWidth'] // 2, MinSnapSpacing), self.CeilMinSnapSpacing(self._DesignParameter['_ViaMet22Met3OnPMOSCLKInput']['_XYCoordinates'][0][1] - self._DesignParameter['_Met3CLKinput']['_Width'] // 2 + self._DesignParameter['_ViaMet22Met3OnPMOSCLKInput']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth'] // 2, MinSnapSpacing)],
																		 [self.CeilMinSnapSpacing(min(self._DesignParameter['_ViaMet22Met3OnPMOSOutput']['_XYCoordinates'][0][0], self._DesignParameter['_ViaMet22Met3OnNMOSOutput']['_XYCoordinates'][0][0]) - 4 * _DRCObj._MetalxMinSpace2, MinSnapSpacing), self.CeilMinSnapSpacing(self._DesignParameter['_ViaMet22Met3OnPMOSCLKInput']['_XYCoordinates'][0][1] - self._DesignParameter['_Met3CLKinput']['_Width'] // 2 + self._DesignParameter['_ViaMet22Met3OnPMOSCLKInput']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth'] // 2, MinSnapSpacing)]],
																		# [[self.CeilMinSnapSpacing(self._DesignParameter[
																		#                               '_ViaMet22Met3OnPMOSCLKInput'][
																		#                               '_XYCoordinates'][
																		#                               0][0] -
																		#                           self._DesignParameter[
																		#                               '_ViaMet22Met3OnPMOSCLKInput'][
																		#                               '_DesignObj']._DesignParameter[
																		#                               '_Met3Layer'][
																		#                               '_XWidth'] // 2,
																		#                           MinSnapSpacing),
																		#   self.CeilMinSnapSpacing(self._DesignParameter[
																		#                               '_ViaMet22Met3OnPMOSCLKInput'][
																		#                               '_XYCoordinates'][
																		#                               0][1] -
																		#                           self._DesignParameter[
																		#                               '_Met3CLKinput'][
																		#                               '_Width'] // 2 +
																		#                           self._DesignParameter[
																		#                               '_ViaMet22Met3OnPMOSCLKInput'][
																		#                               '_DesignObj']._DesignParameter[
																		#                               '_Met3Layer'][
																		#                               '_YWidth'] // 2,
																		#                           MinSnapSpacing)],
																		#  [self.CeilMinSnapSpacing(min(
																		#      self._DesignParameter[
																		#          '_ViaMet22Met3OnPMOSOutput'][
																		#          '_XYCoordinates'][0][0],
																		#      self._DesignParameter[
																		#          '_ViaMet22Met3OnNMOSOutput'][
																		#          '_XYCoordinates'][0][
																		#          0]) - 3 * _DRCObj._MetalxMinWidth - _DRCObj._MetalxMinSpace5,
																		#                           MinSnapSpacing),
																		#   self.CeilMinSnapSpacing(self._DesignParameter[
																		#                               '_ViaMet22Met3OnPMOSCLKInput'][
																		#                               '_XYCoordinates'][
																		#                               0][1] -
																		#                           self._DesignParameter[
																		#                               '_Met3CLKinput'][
																		#                               '_Width'] // 2 +
																		#                           self._DesignParameter[
																		#                               '_ViaMet22Met3OnPMOSCLKInput'][
																		#                               '_DesignObj']._DesignParameter[
																		#                               '_Met3Layer'][
																		#                               '_YWidth'] // 2,
																		#                           MinSnapSpacing)]],

																		[[self.CeilMinSnapSpacing(-(self._DesignParameter['_ViaMet22Met3OnPMOSCLKInput']['_XYCoordinates'][0][0] - self._DesignParameter['_ViaMet22Met3OnPMOSCLKInput']['_DesignObj']._DesignParameter['_Met3Layer']['_XWidth'] // 2), MinSnapSpacing), self.CeilMinSnapSpacing(self._DesignParameter['_ViaMet22Met3OnPMOSCLKInput']['_XYCoordinates'][0][1] - self._DesignParameter['_Met3CLKinput']['_Width'] // 2 + self._DesignParameter['_ViaMet22Met3OnPMOSCLKInput']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth'] // 2, MinSnapSpacing)],
																		 [self.CeilMinSnapSpacing(-(min(self._DesignParameter['_ViaMet22Met3OnPMOSOutput']['_XYCoordinates'][0][0], self._DesignParameter['_ViaMet22Met3OnNMOSOutput']['_XYCoordinates'][0][0]) - 4 * _DRCObj._MetalxMinSpace2), MinSnapSpacing), self.CeilMinSnapSpacing(self._DesignParameter['_ViaMet22Met3OnPMOSCLKInput']['_XYCoordinates'][0][1] - self._DesignParameter['_Met3CLKinput']['_Width'] // 2 + self._DesignParameter['_ViaMet22Met3OnPMOSCLKInput']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth'] // 2, MinSnapSpacing)]],
																		 # [[self.CeilMinSnapSpacing(-(
																		 #             self._DesignParameter[
																		 #                 '_ViaMet22Met3OnPMOSCLKInput'][
																		 #                 '_XYCoordinates'][0][0] -
																		 #             self._DesignParameter[
																		 #                 '_ViaMet22Met3OnPMOSCLKInput'][
																		 #                 '_DesignObj']._DesignParameter[
																		 #                 '_Met3Layer']['_XWidth'] // 2),
																		 #                           MinSnapSpacing),
																		 #   self.CeilMinSnapSpacing(
																		 #       self._DesignParameter[
																		 #           '_ViaMet22Met3OnPMOSCLKInput'][
																		 #           '_XYCoordinates'][0][1] -
																		 #       self._DesignParameter['_Met3CLKinput'][
																		 #           '_Width'] // 2 +
																		 #       self._DesignParameter[
																		 #           '_ViaMet22Met3OnPMOSCLKInput'][
																		 #           '_DesignObj']._DesignParameter[
																		 #           '_Met3Layer']['_YWidth'] // 2,
																		 #       MinSnapSpacing)],
																		 #  [self.CeilMinSnapSpacing(-(min(
																		 #      self._DesignParameter[
																		 #          '_ViaMet22Met3OnPMOSOutput'][
																		 #          '_XYCoordinates'][0][0],
																		 #      self._DesignParameter[
																		 #          '_ViaMet22Met3OnNMOSOutput'][
																		 #          '_XYCoordinates'][0][
																		 #          0]) - 3 * _DRCObj._MetalxMinWidth - _DRCObj._MetalxMinSpace5),
																		 #                           MinSnapSpacing),
																		 #   self.CeilMinSnapSpacing(
																		 #       self._DesignParameter[
																		 #           '_ViaMet22Met3OnPMOSCLKInput'][
																		 #           '_XYCoordinates'][0][1] -
																		 #       self._DesignParameter['_Met3CLKinput'][
																		 #           '_Width'] // 2 +
																		 #       self._DesignParameter[
																		 #           '_ViaMet22Met3OnPMOSCLKInput'][
																		 #           '_DesignObj']._DesignParameter[
																		 #           '_Met3Layer']['_YWidth'] // 2,
																		 #       MinSnapSpacing)]
																		 #
																		 # ],
																		# [[self.CeilMinSnapSpacing(min(self._DesignParameter['_ViaMet22Met3OnPMOSOutput']['_XYCoordinates'][0][0], self._DesignParameter['_ViaMet22Met3OnNMOSOutput']['_XYCoordinates'][0][0]) - 3 * _DRCObj._MetalxMinWidth - _DRCObj._MetalxMinSpace5, MinSnapSpacing), self.CeilMinSnapSpacing(self._DesignParameter['_ViaMet22Met3OnNMOSCLKInput']['_XYCoordinates'][0][1] + self._DesignParameter['_Met3CLKinput']['_Width'] // 2 - self._DesignParameter['_ViaMet22Met3OnPMOSCLKInput']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth'] // 2, MinSnapSpacing)],
																		#  [self.CeilMinSnapSpacing(-(min(self._DesignParameter['_ViaMet22Met3OnPMOSOutput']['_XYCoordinates'][0][0], self._DesignParameter['_ViaMet22Met3OnNMOSOutput']['_XYCoordinates'][0][0]) - 3 * _DRCObj._MetalxMinWidth - _DRCObj._MetalxMinSpace5), MinSnapSpacing), self.CeilMinSnapSpacing(self._DesignParameter['_ViaMet22Met3OnNMOSCLKInput']['_XYCoordinates'][0][1] + + self._DesignParameter['_Met3CLKinput']['_Width'] // 2 - self._DesignParameter['_ViaMet22Met3OnPMOSCLKInput']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth'] // 2, MinSnapSpacing)]]]
																		[[self.CeilMinSnapSpacing(min(self._DesignParameter['_ViaMet22Met3OnPMOSOutput']['_XYCoordinates'][0][0], self._DesignParameter['_ViaMet22Met3OnNMOSOutput']['_XYCoordinates'][0][0]) - 4 * _DRCObj._MetalxMinSpace2, MinSnapSpacing), self.CeilMinSnapSpacing(self._DesignParameter['_ViaMet22Met3OnNMOSCLKInput']['_XYCoordinates'][0][1] + self._DesignParameter['_Met3CLKinput']['_Width'] // 2 - self._DesignParameter['_ViaMet22Met3OnPMOSCLKInput']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth'] // 2, MinSnapSpacing)],
																		 [self.CeilMinSnapSpacing(-(min(self._DesignParameter['_ViaMet22Met3OnPMOSOutput']['_XYCoordinates'][0][0], self._DesignParameter['_ViaMet22Met3OnNMOSOutput']['_XYCoordinates'][0][0]) - 4 * _DRCObj._MetalxMinSpace2), MinSnapSpacing), self.CeilMinSnapSpacing(self._DesignParameter['_ViaMet22Met3OnNMOSCLKInput']['_XYCoordinates'][0][1] + + self._DesignParameter['_Met3CLKinput']['_Width'] // 2 - self._DesignParameter['_ViaMet22Met3OnPMOSCLKInput']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth'] // 2, MinSnapSpacing)]]]




			self._DesignParameter['_Met4CLKinput'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL4'][0], _Datatype=DesignParameters._LayerMapping['METAL4'][1], _XYCoordinates=[], _Width=400)
			self._DesignParameter['_Met4CLKinput']['_Width'] = 2 * _DRCObj._MetalxMinWidth
			self._DesignParameter['_Met4CLKinput']['_XYCoordinates'] = [[[min(self._DesignParameter['_ViaMet22Met3OnPMOSOutput']['_XYCoordinates'][0][0], self._DesignParameter['_ViaMet22Met3OnNMOSOutput']['_XYCoordinates'][0][0]) - 4 * _DRCObj._MetalxMinSpace2, self.CeilMinSnapSpacing(self._DesignParameter['_Met3CLKinput']['_XYCoordinates'][0][0][1] + self._DesignParameter['_Met3CLKinput']['_Width'] // 2, MinSnapSpacing)], [min(self._DesignParameter['_ViaMet22Met3OnPMOSOutput']['_XYCoordinates'][0][0], self._DesignParameter['_ViaMet22Met3OnNMOSOutput']['_XYCoordinates'][0][0]) - 4 * _DRCObj._MetalxMinSpace2, self.CeilMinSnapSpacing(self._DesignParameter['_Met3CLKinput']['_XYCoordinates'][2][0][1] - self._DesignParameter['_Met3CLKinput']['_Width'] // 2, MinSnapSpacing)]],
																		[[-(min(self._DesignParameter['_ViaMet22Met3OnPMOSOutput']['_XYCoordinates'][0][0], self._DesignParameter['_ViaMet22Met3OnNMOSOutput']['_XYCoordinates'][0][0]) - 4 * _DRCObj._MetalxMinSpace2), self.CeilMinSnapSpacing(self._DesignParameter['_Met3CLKinput']['_XYCoordinates'][0][0][1] + self._DesignParameter['_Met3CLKinput']['_Width'] // 2, MinSnapSpacing)], [-(min(self._DesignParameter['_ViaMet22Met3OnPMOSOutput']['_XYCoordinates'][0][0], self._DesignParameter['_ViaMet22Met3OnNMOSOutput']['_XYCoordinates'][0][0]) - 4 * _DRCObj._MetalxMinSpace2), self.CeilMinSnapSpacing(self._DesignParameter['_Met3CLKinput']['_XYCoordinates'][2][0][1] - self._DesignParameter['_Met3CLKinput']['_Width'] // 2, MinSnapSpacing)]]]

			# self._DesignParameter['_Met4CLKinput']['_XYCoordinates'] = [[[min(self._DesignParameter['_ViaMet22Met3OnPMOSOutput']['_XYCoordinates'][0][0], self._DesignParameter['_ViaMet22Met3OnNMOSOutput']['_XYCoordinates'][0][0]) - 3 * _DRCObj._MetalxMinWidth - _DRCObj._MetalxMinSpace5, self.CeilMinSnapSpacing(self._DesignParameter['_Met3CLKinput']['_XYCoordinates'][0][0][1] + self._DesignParameter['_Met3CLKinput']['_Width'] // 2, MinSnapSpacing)], [min(self._DesignParameter['_ViaMet22Met3OnPMOSOutput']['_XYCoordinates'][0][0], self._DesignParameter['_ViaMet22Met3OnNMOSOutput']['_XYCoordinates'][0][0]) - 3 * _DRCObj._MetalxMinWidth - _DRCObj._MetalxMinSpace5, self.CeilMinSnapSpacing(self._DesignParameter['_Met3CLKinput']['_XYCoordinates'][2][0][1] - self._DesignParameter['_Met3CLKinput']['_Width'] // 2, MinSnapSpacing)]],
			#                                                             [[-(min(self._DesignParameter['_ViaMet22Met3OnPMOSOutput']['_XYCoordinates'][0][0], self._DesignParameter['_ViaMet22Met3OnNMOSOutput']['_XYCoordinates'][0][0]) - 3 * _DRCObj._MetalxMinWidth  - _DRCObj._MetalxMinSpace5), self.CeilMinSnapSpacing(self._DesignParameter['_Met3CLKinput']['_XYCoordinates'][0][0][1] + self._DesignParameter['_Met3CLKinput']['_Width'] // 2, MinSnapSpacing)], [-(min(self._DesignParameter['_ViaMet22Met3OnPMOSOutput']['_XYCoordinates'][0][0], self._DesignParameter['_ViaMet22Met3OnNMOSOutput']['_XYCoordinates'][0][0]) - 3 * _DRCObj._MetalxMinWidth - _DRCObj._MetalxMinSpace5), self.CeilMinSnapSpacing(self._DesignParameter['_Met3CLKinput']['_XYCoordinates'][2][0][1] - self._DesignParameter['_Met3CLKinput']['_Width'] // 2, MinSnapSpacing)]]]



			_VIANMOSMet34inner = copy.deepcopy(ViaMet32Met4._ViaMet32Met4._ParametersForDesignCalculation)
			_tmpNumViaX = int(abs((self._DesignParameter['_Met4CLKinput']['_XYCoordinates'][1][1][0] - self._DesignParameter['_Met4CLKinput']['_XYCoordinates'][0][1][0] - self._DesignParameter['_Met4CLKinput']['_Width'] - 2 * _DRCObj._MetalxMinSpace2) // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace)))
			#_DRCObj._MetalxMinSpace21

			_VIANMOSMet34inner['_ViaMet32Met4NumberOfCOX'] = _tmpNumViaX
			_VIANMOSMet34inner['_ViaMet32Met4NumberOfCOY'] = 1

			self._DesignParameter['_ViaMet32Met4OnNMOSInner'] = self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_DesignParameter=None, _Name='{}:ViaMet32Met4OnNMOSInner'.format(_Name)))[0]
			self._DesignParameter['_ViaMet32Met4OnNMOSInner']['_DesignObj']._CalculateViaMet32Met4DesignParameterMinimumEnclosureY(**_VIANMOSMet34inner)
			self._DesignParameter['_ViaMet32Met4OnNMOSInner']['_XYCoordinates'] = [[0, self.CeilMinSnapSpacing(self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_NMOS1']['_XYCoordinates'][0][1] - self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnNMOSOutput1']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] // 2 - _LengthbtwViaCentertoViaCenter // 4 - _DRCObj._MetalxMinWidth // 2, MinSnapSpacing)]]

			del _tmpNumViaX

			_VIANMOSMet23inner = copy.deepcopy(ViaMet22Met3._ViaMet22Met3._ParametersForDesignCalculation)
			_tmpNumViaX = int(abs((self._DesignParameter['_Met4CLKinput']['_XYCoordinates'][1][1][0] - self._DesignParameter['_Met4CLKinput']['_XYCoordinates'][0][1][0] - self._DesignParameter['_Met4CLKinput']['_Width'] - 2 * _DRCObj._MetalxMinSpace2) // (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace)))
			#_DRCObj._MetalxMinSpace21

			_VIANMOSMet23inner['_ViaMet22Met3NumberOfCOX'] = _tmpNumViaX
			_VIANMOSMet23inner['_ViaMet22Met3NumberOfCOY'] = 1

			self._DesignParameter['_ViaMet22Met3OnNMOSInner'] = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_DesignParameter=None, _Name='{}:ViaMet22Met3OnNMOSInner'.format(_Name)))[0]
			self._DesignParameter['_ViaMet22Met3OnNMOSInner']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureY(**_VIANMOSMet23inner)
			self._DesignParameter['_ViaMet22Met3OnNMOSInner']['_XYCoordinates'] = [[0, self.CeilMinSnapSpacing(self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_NMOS1']['_XYCoordinates'][0][1] - self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnNMOSOutput1']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] // 2 - _LengthbtwViaCentertoViaCenter // 4 - _DRCObj._MetalxMinWidth // 2, MinSnapSpacing)]]



			_VIAMet32Met4OnforCLKRouting = copy.deepcopy(ViaMet32Met4._ViaMet32Met4._ParametersForDesignCalculation)
			_VIAMet32Met4OnforCLKRouting['_ViaMet32Met4NumberOfCOX'] = 1
			_VIAMet32Met4OnforCLKRouting['_ViaMet32Met4NumberOfCOY'] = 2

			self._DesignParameter['_VIAMet32Met4OnforCLKPNRouting'] = self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_DesignParameter=None, _Name='{}:VIAMet32Met3OnforPNRouting'.format(_Name)))[0]
			self._DesignParameter['_VIAMet32Met4OnforCLKPNRouting']['_DesignObj']._CalculateViaMet32Met4DesignParameterMinimumEnclosureX(**_VIAMet32Met4OnforCLKRouting)
			self._DesignParameter['_VIAMet32Met4OnforCLKPNRouting']['_XYCoordinates'] =  [[self._DesignParameter['_Met4CLKinput']['_XYCoordinates'][0][0][0], self.CeilMinSnapSpacing(self._DesignParameter['_Met4CLKinput']['_XYCoordinates'][0][0][1] - self._DesignParameter['_VIAMet32Met4OnforCLKPNRouting']['_DesignObj']._DesignParameter['_Met4Layer']['_YWidth'] // 2, MinSnapSpacing)], \
																						 [self._DesignParameter['_Met4CLKinput']['_XYCoordinates'][0][1][0], self.CeilMinSnapSpacing(self._DesignParameter['_Met4CLKinput']['_XYCoordinates'][0][1][1] + self._DesignParameter['_VIAMet32Met4OnforCLKPNRouting']['_DesignObj']._DesignParameter['_Met4Layer']['_YWidth'] // 2, MinSnapSpacing)], \
																						 [self._DesignParameter['_Met4CLKinput']['_XYCoordinates'][1][0][0], self.CeilMinSnapSpacing(self._DesignParameter['_Met4CLKinput']['_XYCoordinates'][1][0][1] - self._DesignParameter['_VIAMet32Met4OnforCLKPNRouting']['_DesignObj']._DesignParameter['_Met4Layer']['_YWidth'] // 2, MinSnapSpacing)], \
																						 [self._DesignParameter['_Met4CLKinput']['_XYCoordinates'][1][1][0], self.CeilMinSnapSpacing(self._DesignParameter['_Met4CLKinput']['_XYCoordinates'][1][1][1] + self._DesignParameter['_VIAMet32Met4OnforCLKPNRouting']['_DesignObj']._DesignParameter['_Met4Layer']['_YWidth'] // 2, MinSnapSpacing)]]





			print('x')


			########################################### Met2 Routing Generation for Inner PMOS Gate --- Inner NMOS Gate Connection (Cross-coupled) ##########################################
			self._DesignParameter['_ThickMet2PNMOSGate'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _XYCoordinates=[], _Width=400)
			if DesignParameters._Technology == '090nm' :
				self._DesignParameter['_ThickMet2PNMOSGate']['_Width'] = _DRCObj._MetalxMinWidth
			else :
				self._DesignParameter['_ThickMet2PNMOSGate']['_Width'] = 2 * _DRCObj._MetalxMinWidth
			if (_PMOSFinger < _NMOSFinger):
				self._DesignParameter['_ThickMet2PNMOSGate']['_XYCoordinates'] = [[self._DesignParameter['_ViaMet12Met2OnPMOSGate1']['_XYCoordinates'][0],
																				  [self._DesignParameter['_ViaMet12Met2OnPMOSGate1']['_XYCoordinates'][0][0], self.CeilMinSnapSpacing((self._DesignParameter['_ViaMet12Met2OnPMOSGate1']['_XYCoordinates'][0][1] + self._DesignParameter['_ViaMet12Met2OnNMOSGate1']['_XYCoordinates'][0][1]) // 2, MinSnapSpacing)], \
																				  [self._DesignParameter['_ViaMet12Met2OnNMOSGate1']['_XYCoordinates'][0][0], self.CeilMinSnapSpacing((self._DesignParameter['_ViaMet12Met2OnPMOSGate1']['_XYCoordinates'][0][1] + self._DesignParameter['_ViaMet12Met2OnNMOSGate1']['_XYCoordinates'][0][1]) // 2, MinSnapSpacing)], \
																				   self._DesignParameter['_ViaMet12Met2OnNMOSGate1']['_XYCoordinates'][0]],

																				  [self._DesignParameter['_ViaMet12Met2OnPMOSGate1']['_XYCoordinates'][1],
																				  [self._DesignParameter['_ViaMet12Met2OnPMOSGate1']['_XYCoordinates'][1][0], self.CeilMinSnapSpacing((self._DesignParameter['_ViaMet12Met2OnPMOSGate1']['_XYCoordinates'][1][1] + self._DesignParameter['_ViaMet12Met2OnNMOSGate1']['_XYCoordinates'][1][1]) // 2, MinSnapSpacing)], \
																				  [self._DesignParameter['_ViaMet12Met2OnNMOSGate1']['_XYCoordinates'][1][0], self.CeilMinSnapSpacing((self._DesignParameter['_ViaMet12Met2OnPMOSGate1']['_XYCoordinates'][1][1] + self._DesignParameter['_ViaMet12Met2OnNMOSGate1']['_XYCoordinates'][1][1]) // 2, MinSnapSpacing)], \
																				   self._DesignParameter['_ViaMet12Met2OnNMOSGate1']['_XYCoordinates'][1]]]


			elif (_PMOSFinger >= _NMOSFinger):
				self._DesignParameter['_ThickMet2PNMOSGate']['_XYCoordinates'] = [[self._DesignParameter['_ViaMet12Met2OnNMOSGate1']['_XYCoordinates'][0],
																				  [self._DesignParameter['_ViaMet12Met2OnNMOSGate1']['_XYCoordinates'][0][0], self.CeilMinSnapSpacing((self._DesignParameter['_ViaMet12Met2OnPMOSGate1']['_XYCoordinates'][0][1] + self._DesignParameter['_ViaMet12Met2OnNMOSGate1']['_XYCoordinates'][0][1]) // 2, MinSnapSpacing)], \
																				  [self._DesignParameter['_ViaMet12Met2OnPMOSGate1']['_XYCoordinates'][0][0], self.CeilMinSnapSpacing((self._DesignParameter['_ViaMet12Met2OnPMOSGate1']['_XYCoordinates'][0][1] + self._DesignParameter['_ViaMet12Met2OnNMOSGate1']['_XYCoordinates'][0][1]) // 2, MinSnapSpacing)], \
																				   self._DesignParameter['_ViaMet12Met2OnPMOSGate1']['_XYCoordinates'][0]],


																			 [self._DesignParameter['_ViaMet12Met2OnNMOSGate1']['_XYCoordinates'][1],
																			 [self._DesignParameter['_ViaMet12Met2OnNMOSGate1']['_XYCoordinates'][1][0], self.CeilMinSnapSpacing((self._DesignParameter['_ViaMet12Met2OnPMOSGate1']['_XYCoordinates'][1][1] + self._DesignParameter['_ViaMet12Met2OnNMOSGate1']['_XYCoordinates'][1][1]) // 2, MinSnapSpacing)],\
																			 [self._DesignParameter['_ViaMet12Met2OnPMOSGate1']['_XYCoordinates'][1][0], self.CeilMinSnapSpacing((self._DesignParameter['_ViaMet12Met2OnPMOSGate1']['_XYCoordinates'][1][1] + self._DesignParameter['_ViaMet12Met2OnNMOSGate1']['_XYCoordinates'][1][1]) // 2, MinSnapSpacing)],\
																			  self._DesignParameter['_ViaMet12Met2OnPMOSGate1']['_XYCoordinates'][1]]

																			]


			########################################### Met4 Routing Generation for CLK PMOS//NMOS Drain --- Inner PMOS//NMOS Drain Connection ##########################################
			self._DesignParameter['_Met4PNMOSDrain'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL4'][0], _Datatype=DesignParameters._LayerMapping['METAL4'][1], _XYCoordinates=[], _Width=400)
			self._DesignParameter['_Met4PNMOSDrain']['_Width'] = _DRCObj._MetalxMinWidth
			tmp = []
			for i in range(0, int(_CLKinputPMOSFinger1 + 1) // 2) :


				tmp.append([[self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet32Met4OnPMOSOutput1']['_XYCoordinates'][i][0], self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_PMOS1']['_XYCoordinates'][0][1] + self._DesignParameter['_PMOSSET']['_XYCoordinates'][0][1]], \
							[self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet32Met4OnPMOSOutput1']['_XYCoordinates'][i][0], self._DesignParameter['_ViaMet22Met3OnNMOSInput']['_XYCoordinates'][0][1]]])

				tmp.append([[-(self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet32Met4OnPMOSOutput1']['_XYCoordinates'][i][0]), self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_PMOS1']['_XYCoordinates'][0][1] + self._DesignParameter['_PMOSSET']['_XYCoordinates'][0][1]], \
							[-(self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet32Met4OnPMOSOutput1']['_XYCoordinates'][i][0]),  self._DesignParameter['_ViaMet22Met3OnNMOSInput']['_XYCoordinates'][0][1]]])


			self._DesignParameter['_Met4PNMOSDrain']['_XYCoordinates'] = tmp
			del tmp

			self._DesignParameter['_Met3PNMOSDrainRouting'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0], _Datatype=DesignParameters._LayerMapping['METAL3'][1], _XYCoordinates=[], _Width=400)
			self._DesignParameter['_Met3PNMOSDrainRouting']['_Width'] = _DRCObj._MetalxMinWidth
			tmp = []
			tmp.append([[self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet32Met4OnPMOSOutput1']['_XYCoordinates'][0][0], self._DesignParameter['_ViaMet22Met3OnNMOSInput']['_XYCoordinates'][0][1]], [self._DesignParameter['_ViaMet22Met3OnNMOSInput']['_XYCoordinates'][0][0], self._DesignParameter['_ViaMet22Met3OnNMOSInput']['_XYCoordinates'][0][1]]])
			tmp.append([[-(self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet32Met4OnPMOSOutput1']['_XYCoordinates'][0][0]), self._DesignParameter['_ViaMet22Met3OnNMOSInput']['_XYCoordinates'][0][1]], [-(self._DesignParameter['_ViaMet22Met3OnNMOSInput']['_XYCoordinates'][0][0]), self._DesignParameter['_ViaMet22Met3OnNMOSInput']['_XYCoordinates'][0][1]]])

			self._DesignParameter['_Met3PNMOSDrainRouting']['_XYCoordinates'] = tmp

			del tmp

			_ViaMet324PNMOSDrain = copy.deepcopy(ViaMet32Met4._ViaMet32Met4._ParametersForDesignCalculation)
			_ViaMet324PNMOSDrain['_ViaMet32Met4NumberOfCOX'] = 1
			_ViaMet324PNMOSDrain['_ViaMet32Met4NumberOfCOY'] = 2

			self._DesignParameter['_ViaMet324PNMOSDrain'] = self._SrefElementDeclaration(_DesignObj=ViaMet32Met4._ViaMet32Met4(_DesignParameter=None, _Name='{}:ViaMet324PNMOSDrain'.format(_Name)))[0]
			self._DesignParameter['_ViaMet324PNMOSDrain']['_DesignObj']._CalculateViaMet32Met4DesignParameterMinimumEnclosureX(**_ViaMet324PNMOSDrain)

			tmp = []

			for i in range(0, int(_CLKinputPMOSFinger1 + 1) // 2) :
				tmp.append([self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet32Met4OnPMOSOutput1']['_XYCoordinates'][i][0], self.CeilMinSnapSpacing(self._DesignParameter['_ViaMet22Met3OnNMOSInput']['_XYCoordinates'][0][1] + self._DesignParameter['_ViaMet324PNMOSDrain']['_DesignObj']._DesignParameter['_Met4Layer']['_YWidth'] // 2 - self._DesignParameter['_Met3PNMOSDrainRouting']['_Width'] // 2, MinSnapSpacing)])
				tmp.append([-(self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_ViaMet32Met4OnPMOSOutput1']['_XYCoordinates'][i][0]), self.CeilMinSnapSpacing(self._DesignParameter['_ViaMet22Met3OnNMOSInput']['_XYCoordinates'][0][1] + self._DesignParameter['_ViaMet324PNMOSDrain']['_DesignObj']._DesignParameter['_Met4Layer']['_YWidth'] // 2 - self._DesignParameter['_Met3PNMOSDrainRouting']['_Width'] // 2, MinSnapSpacing)])


			self._DesignParameter['_ViaMet324PNMOSDrain']['_XYCoordinates'] = tmp

			del tmp


			self._DesignParameter['_Met4NMOS5'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL4'][0], _Datatype=DesignParameters._LayerMapping['METAL4'][1], _XYCoordinates=[], _Width=400)

			if _DATAinputNMOSFinger > 1 :


				# if _CLKinputNMOSFinger % 4 != 2 :
				#     self._DesignParameter['_Met4NMOS5']['_Width'] =self.CeilMinSnapSpacing( 3 * _DRCObj._MetalxMinWidth + _DRCObj._MetalxMinWidth // 2, 2*MinSnapSpacing)
				#     self._DesignParameter['_Met4NMOS5']['_XYCoordinates'] = [[[self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][0], self.CeilMinSnapSpacing(self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_NMOS1']['_XYCoordinates'][0][1] - self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnNMOSOutput1']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] // 2 - _LengthbtwViaCentertoViaCenter // 4 - _DRCObj._MetalxMinWidth // 2, MinSnapSpacing)], [self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][0], self.CeilMinSnapSpacing(self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_NMOS5']['_XYCoordinates'][0][1] - self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_ViaMet32Met4OnNMOSOutput5']['_DesignObj']._DesignParameter['_Met4Layer']['_YWidth'] // 2, MinSnapSpacing)]]]
				# elif _CLKinputNMOSFinger % 4 == 2 :
				#     self._DesignParameter['_Met4NMOS5']['_Width'] = 2 * _DRCObj._MetalxMinWidth
				#     self._DesignParameter['_Met4NMOS5']['_XYCoordinates'] = [[[self.CeilMinSnapSpacing(self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][0] - _DRCObj._PolygateMinWidth - _DRCObj._PolygateMinSpace - _DRCObj._MetalxMinWidth // 2 - self._DesignParameter['_Met4NMOS5']['_Width'] // 2 + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_ViaMet32Met4OnNMOSOutput5']['_DesignObj']._DesignParameter['_Met4Layer']['_XWidth'] // 2, MinSnapSpacing), self.CeilMinSnapSpacing(self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_NMOS1']['_XYCoordinates'][0][1] - self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnNMOSOutput1']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] // 2 - _LengthbtwViaCentertoViaCenter // 4 - _DRCObj._MetalxMinWidth // 2, MinSnapSpacing)], \
				#                                                              [self.CeilMinSnapSpacing(self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][0] - _DRCObj._PolygateMinWidth - _DRCObj._PolygateMinSpace - _DRCObj._MetalxMinWidth // 2 - self._DesignParameter['_Met4NMOS5']['_Width'] // 2 + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_ViaMet32Met4OnNMOSOutput5']['_DesignObj']._DesignParameter['_Met4Layer']['_XWidth'] // 2, MinSnapSpacing), self.CeilMinSnapSpacing(self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_NMOS5']['_XYCoordinates'][0][1] - self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_ViaMet32Met4OnNMOSOutput5']['_DesignObj']._DesignParameter['_Met4Layer']['_YWidth'] // 2, MinSnapSpacing)]], \
				#                                                              [[self.CeilMinSnapSpacing(self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][0] + _DRCObj._PolygateMinWidth + _DRCObj._PolygateMinSpace + _DRCObj._MetalxMinWidth // 2 + self._DesignParameter['_Met4NMOS5']['_Width'] // 2 - self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_ViaMet32Met4OnNMOSOutput5']['_DesignObj']._DesignParameter['_Met4Layer']['_XWidth'] // 2, MinSnapSpacing), self.CeilMinSnapSpacing(self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_NMOS1']['_XYCoordinates'][0][1] - self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnNMOSOutput1']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] // 2 - _LengthbtwViaCentertoViaCenter // 4 - _DRCObj._MetalxMinWidth // 2, MinSnapSpacing)], \
				#                                                               [self.CeilMinSnapSpacing(self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][0] + _DRCObj._PolygateMinWidth + _DRCObj._PolygateMinSpace + _DRCObj._MetalxMinWidth // 2 + self._DesignParameter['_Met4NMOS5']['_Width'] // 2 - self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_ViaMet32Met4OnNMOSOutput5']['_DesignObj']._DesignParameter['_Met4Layer']['_XWidth'] // 2, MinSnapSpacing), self.CeilMinSnapSpacing(self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_NMOS5']['_XYCoordinates'][0][1] - self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_ViaMet32Met4OnNMOSOutput5']['_DesignObj']._DesignParameter['_Met4Layer']['_YWidth'] // 2, MinSnapSpacing)]]]

				if _CLKinputNMOSFinger != 1 :
					self._DesignParameter['_Met4NMOS5']['_Width'] = 4 * _DRCObj._MetalxMinWidth
					self._DesignParameter['_Met4NMOS5']['_XYCoordinates'] = [[[self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_NMOS5']['_XYCoordinates'][0][0], self._DesignParameter['_ViaMet32Met4OnNMOSInner']['_XYCoordinates'][0][1]], [self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_NMOS5']['_XYCoordinates'][0][0], self.CeilMinSnapSpacing(self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_NMOS5']['_XYCoordinates'][0][1] - self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_ViaMet32Met4OnNMOSOutput5']['_DesignObj']._DesignParameter['_Met4Layer']['_YWidth'] // 2, MinSnapSpacing)]]]


				elif _CLKinputNMOSFinger == 1 :
					self._DesignParameter['_Met4NMOS5']['_Width'] = self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_ViaMet32Met4OnNMOSOutput5']['_DesignObj']._DesignParameter['_Met4Layer']['_XWidth']
					self._DesignParameter['_Met4NMOS5']['_XYCoordinates'] = [[[self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_NMOS5']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_NMOS5']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][0][0], self._DesignParameter['_ViaMet32Met4OnNMOSInner']['_XYCoordinates'][0][1]], \
																			 [self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_NMOS5']['_XYCoordinates'][0][0] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_NMOS5']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][0][0], self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_NMOS5']['_XYCoordinates'][0][1]]]]

			elif _DATAinputNMOSFinger == 1:
				self._DesignParameter['_Met4NMOS5']['_Width'] = 2 * _DRCObj._MetalxMinWidth
				self._DesignParameter['_Met4NMOS5']['_XYCoordinates'] = [[[self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][0], self.CeilMinSnapSpacing(self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_NMOS1']['_XYCoordinates'][0][1] - self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnNMOSOutput1']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] // 2 - _LengthbtwViaCentertoViaCenter // 4 - _DRCObj._MetalxMinWidth // 2, MinSnapSpacing)], [self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][0], self.CeilMinSnapSpacing(self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_NMOS5']['_XYCoordinates'][0][1] - self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_ViaMet32Met4OnNMOSOutput5']['_DesignObj']._DesignParameter['_Met4Layer']['_YWidth'] // 2, MinSnapSpacing)]], \
																		 [[self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][0], self.CeilMinSnapSpacing(self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_NMOS1']['_XYCoordinates'][0][1] - self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_ViaMet12Met2OnNMOSOutput1']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] // 2 - _LengthbtwViaCentertoViaCenter // 4 - _DRCObj._MetalxMinWidth // 2, MinSnapSpacing)], [self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][0], self.CeilMinSnapSpacing(self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_NMOS5']['_XYCoordinates'][0][1] - self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_ViaMet32Met4OnNMOSOutput5']['_DesignObj']._DesignParameter['_Met4Layer']['_YWidth'] // 2, MinSnapSpacing)]]]


			# #####################################################################################################################################################
			# ############################################################# Pin Declaration #######################################################################
			# #####################################################################################################################################################
			# self._DesignParameter['_PinVDD'] = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1PIN'][0], _Datatype=DesignParameters._LayerMapping['METAL1PIN'][1], _Presentation = [0,1,2], _Reflect=[0,0,0], _XYCoordinates=[[0,0]], _Mag=0.1, _Angle=0, _TEXT='VDD')
			# self._DesignParameter['_PinVSS'] = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1PIN'][0], _Datatype=DesignParameters._LayerMapping['METAL1PIN'][1], _Presentation = [0,1,2], _Reflect=[0,0,0], _XYCoordinates=[[0,0]], _Mag=0.1, _Angle=0, _TEXT='VSS')
			# self._DesignParameter['_PinInputP'] = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1PIN'][0], _Datatype=DesignParameters._LayerMapping['METAL1PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0],_XYCoordinates=[[0, 0]], _Mag=0.1, _Angle=0, _TEXT='INp')
			# self._DesignParameter['_PinInputN'] = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1PIN'][0], _Datatype=DesignParameters._LayerMapping['METAL1PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0],_XYCoordinates=[[0, 0]], _Mag=0.1, _Angle=0, _TEXT='INn')
			# self._DesignParameter['_PinOutputP'] = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1PIN'][0], _Datatype=DesignParameters._LayerMapping['METAL1PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0],_XYCoordinates=[[0, 0]], _Mag=0.1, _Angle=0, _TEXT='SSp')
			# self._DesignParameter['_PinOutputN'] = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1PIN'][0], _Datatype=DesignParameters._LayerMapping['METAL1PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0],_XYCoordinates=[[0, 0]], _Mag=0.1, _Angle=0, _TEXT='SSn')
			# self._DesignParameter['_PinCLK'] = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1PIN'][0], _Datatype=DesignParameters._LayerMapping['METAL1PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0], _XYCoordinates=[[0, 0]], _Mag=0.1, _Angle=0, _TEXT='CLK')
            #
			# self._DesignParameter['_PinVDD']['_XYCoordinates'] = [[0, PMOS_toptmp+self._DesignParameter['_PMOSSET']['_XYCoordinates'][0][1]]]
			# self._DesignParameter['_PinVSS']['_XYCoordinates'] = [[0, NMOS_bottomtmp+self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1]]]
			# self._DesignParameter['_PinInputP']['_XYCoordinates'] = [[self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS1']['_XYCoordinates'][0][0],
			# 														  self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS1']['_XYCoordinates'][0][1]+self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1]]]
			# self._DesignParameter['_PinInputN']['_XYCoordinates'] = [[self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS2']['_XYCoordinates'][0][0],
			# 														  self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS2']['_XYCoordinates'][0][1]+self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1]]]
            #
			# self._DesignParameter['_PinOutputN']['_XYCoordinates'] = [self._DesignParameter['_ViaMet22Met3OnPMOSOutput']['_XYCoordinates'][0]]
			# self._DesignParameter['_PinOutputP']['_XYCoordinates'] = [self._DesignParameter['_ViaMet22Met3OnPMOSOutput']['_XYCoordinates'][1]]
			# self._DesignParameter['_PinCLK']['_XYCoordinates'] = [[self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS5']['_XYCoordinates'][0][0],
			# 													   self._DesignParameter['_NMOSSET']['_DesignObj']._DesignParameter['_VIANMOSPoly2Met1NMOS5']['_XYCoordinates'][0][1] + self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][1]],
			# 													  [self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_VIAPMOSPoly2Met1PMOS1']['_XYCoordinates'][0][0], self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_VIAPMOSPoly2Met1PMOS1']['_XYCoordinates'][0][1] + self._DesignParameter['_PMOSSET']['_XYCoordinates'][0][1]],
			# 													  [self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_VIAPMOSPoly2Met1PMOS2']['_XYCoordinates'][0][0], self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_VIAPMOSPoly2Met1PMOS2']['_XYCoordinates'][0][1] + self._DesignParameter['_PMOSSET']['_XYCoordinates'][0][1]],
			# 													 ]

			print('x221')
			pass



			if _PMOSFinger % 2 == 1 :
				_VIAPMOSMet23Routing = copy.deepcopy(ViaMet22Met3._ViaMet22Met3._ParametersForDesignCalculation)
				_VIAPMOSMet23Routing['_ViaMet22Met3NumberOfCOX'] = 1
				_VIAPMOSMet23Routing['_ViaMet22Met3NumberOfCOY'] = 2
				self._DesignParameter['_VIAPMOSMet23forRouting'] = self._SrefElementDeclaration( _DesignObj=ViaMet22Met3._ViaMet22Met3(_DesignParameter=None, _Name='{}:VIAPMOSMet23forRouting'.format(_Name)))[0]
				self._DesignParameter['_VIAPMOSMet23forRouting']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureY(**_VIAPMOSMet23Routing)
				self._DesignParameter['_VIAPMOSMet23forRouting']['_XYCoordinates'] = [[self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][0], self.CeilMinSnapSpacing((3 * self._DesignParameter['_ViaMet12Met2OnPMOSGate1']['_XYCoordinates'][0][1] + self._DesignParameter['_ViaMet12Met2OnNMOSGate1']['_XYCoordinates'][0][1]) // 4, MinSnapSpacing)]]

				self._DesignParameter['_CrossPMOSMet3Routing'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0], _Datatype=DesignParameters._LayerMapping['METAL3'][1], _XYCoordinates=[], _Width=400)
				self._DesignParameter['_CrossPMOSMet3Routing']['_Width'] = self.CeilMinSnapSpacing(1.5 * _DRCObj._MetalxMinWidth, 2*MinSnapSpacing)
				self._DesignParameter['_CrossPMOSMet3Routing']['_XYCoordinates'] = [[[self._DesignParameter['_ViaMet22Met3OnPMOSOutput']['_XYCoordinates'][0][0], self.CeilMinSnapSpacing((3 * self._DesignParameter['_ViaMet12Met2OnPMOSGate1']['_XYCoordinates'][0][1] + self._DesignParameter['_ViaMet12Met2OnNMOSGate1']['_XYCoordinates'][0][1]) // 4, MinSnapSpacing)], \
															 self._DesignParameter['_VIAPMOSMet23forRouting']['_XYCoordinates'][0]]]



				_VIAPMOSMet34Routing = copy.deepcopy(ViaMet32Met4._ViaMet32Met4._ParametersForDesignCalculation)
				_VIAPMOSMet34Routing['_ViaMet32Met4NumberOfCOX'] = 1
				_VIAPMOSMet34Routing['_ViaMet32Met4NumberOfCOY'] = 2
				self._DesignParameter['_VIAPMOSMet34forRouting'] = self._SrefElementDeclaration( _DesignObj=ViaMet32Met4._ViaMet32Met4(_DesignParameter=None, _Name='{}:VIAPMOSMet34forRouting'.format(_Name)))[0]
				self._DesignParameter['_VIAPMOSMet34forRouting']['_DesignObj']._CalculateViaMet32Met4DesignParameter(**_VIAPMOSMet34Routing)
				self._DesignParameter['_VIAPMOSMet34forRouting']['_XYCoordinates'] = [[self.CeilMinSnapSpacing(self._DesignParameter['_ViaMet22Met3OnPMOSOutput']['_XYCoordinates'][0][0] - self._DesignParameter['_VIAPMOSMet34forRouting']['_DesignObj']._DesignParameter['_Met4Layer']['_XWidth'] // 2 + _DRCObj._MetalxMinWidth, MinSnapSpacing), self.CeilMinSnapSpacing((3 * self._DesignParameter['_ViaMet12Met2OnPMOSGate1']['_XYCoordinates'][0][1] + self._DesignParameter['_ViaMet12Met2OnNMOSGate1']['_XYCoordinates'][0][1]) // 4, MinSnapSpacing)]]



				self._DesignParameter['_CrossPMOSMet2Routing'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _XYCoordinates=[], _Width=400)
				self._DesignParameter['_CrossPMOSMet2Routing']['_Width'] = self.CeilMinSnapSpacing(1.5 * _DRCObj._MetalxMinWidth, 2*MinSnapSpacing)
				self._DesignParameter['_CrossPMOSMet2Routing']['_XYCoordinates'] = [[[self._DesignParameter['_ViaMet12Met2OnPMOSGate1']['_XYCoordinates'][1][0],  self.CeilMinSnapSpacing((3 * self._DesignParameter['_ViaMet12Met2OnPMOSGate1']['_XYCoordinates'][0][1] + self._DesignParameter['_ViaMet12Met2OnNMOSGate1']['_XYCoordinates'][0][1]) // 4, MinSnapSpacing)], \
															 self._DesignParameter['_VIAPMOSMet23forRouting']['_XYCoordinates'][0]]]

				del _VIAPMOSMet23Routing


			elif _PMOSFinger == 2 :
				_VIAPMOSMet23Routing = copy.deepcopy(ViaMet22Met3._ViaMet22Met3._ParametersForDesignCalculation)
				_VIAPMOSMet23Routing['_ViaMet22Met3NumberOfCOX'] = 1
				_VIAPMOSMet23Routing['_ViaMet22Met3NumberOfCOY'] = 2
				self._DesignParameter['_VIAPMOSMet23forRouting'] = self._SrefElementDeclaration( _DesignObj=ViaMet22Met3._ViaMet22Met3(_DesignParameter=None, _Name='{}:VIAPMOSMet23forRouting'.format(_Name)))[0]
				self._DesignParameter['_VIAPMOSMet23forRouting']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureY(**_VIAPMOSMet23Routing)
				self._DesignParameter['_VIAPMOSMet23forRouting']['_XYCoordinates'] = [[self.CeilMinSnapSpacing(self._DesignParameter['_ViaMet22Met3OnPMOSOutput']['_XYCoordinates'][0][0] + self._DesignParameter['_VIAPMOSMet23forRouting']['_DesignObj']._DesignParameter['_Met3Layer']['_XWidth'] // 2, MinSnapSpacing),  self.CeilMinSnapSpacing((3 * self._DesignParameter['_ViaMet12Met2OnPMOSGate1']['_XYCoordinates'][0][1] + self._DesignParameter['_ViaMet12Met2OnNMOSGate1']['_XYCoordinates'][0][1]) // 4, MinSnapSpacing)]]

				_VIAPMOSMet34Routing = copy.deepcopy(ViaMet32Met4._ViaMet32Met4._ParametersForDesignCalculation)
				_VIAPMOSMet34Routing['_ViaMet32Met4NumberOfCOX'] = 1
				_VIAPMOSMet34Routing['_ViaMet32Met4NumberOfCOY'] = 2
				self._DesignParameter['_VIAPMOSMet34forRouting'] = self._SrefElementDeclaration( _DesignObj=ViaMet32Met4._ViaMet32Met4(_DesignParameter=None, _Name='{}:VIAPMOSMet34forRouting'.format(_Name)))[0]
				self._DesignParameter['_VIAPMOSMet34forRouting']['_DesignObj']._CalculateViaMet32Met4DesignParameterMinimumEnclosureY(**_VIAPMOSMet34Routing)
				self._DesignParameter['_VIAPMOSMet34forRouting']['_XYCoordinates'] = [[self.CeilMinSnapSpacing(self._DesignParameter['_ViaMet22Met3OnPMOSOutput']['_XYCoordinates'][0][0] + self._DesignParameter['_VIAPMOSMet23forRouting']['_DesignObj']._DesignParameter['_Met3Layer']['_XWidth'] // 2, MinSnapSpacing), self.CeilMinSnapSpacing((3 * self._DesignParameter['_ViaMet12Met2OnPMOSGate1']['_XYCoordinates'][0][1] + self._DesignParameter['_ViaMet12Met2OnNMOSGate1']['_XYCoordinates'][0][1]) // 4, MinSnapSpacing)]]





				self._DesignParameter['_CrossPMOSMet2Routing'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _XYCoordinates=[], _Width=400)
				self._DesignParameter['_CrossPMOSMet2Routing']['_Width'] = self.CeilMinSnapSpacing(1.5 * _DRCObj._MetalxMinWidth, 2*MinSnapSpacing)
				self._DesignParameter['_CrossPMOSMet2Routing']['_XYCoordinates'] = [[[self._DesignParameter['_ViaMet12Met2OnPMOSGate1']['_XYCoordinates'][1][0], self.CeilMinSnapSpacing((3 * self._DesignParameter['_ViaMet12Met2OnPMOSGate1']['_XYCoordinates'][0][1] + self._DesignParameter['_ViaMet12Met2OnNMOSGate1']['_XYCoordinates'][0][1]) // 4, MinSnapSpacing)], \
															 self._DesignParameter['_VIAPMOSMet23forRouting']['_XYCoordinates'][0]]]

				del _VIAPMOSMet23Routing


			else :
				_VIAPMOSMet23Routing = copy.deepcopy(ViaMet22Met3._ViaMet22Met3._ParametersForDesignCalculation)
				_VIAPMOSMet23Routing['_ViaMet22Met3NumberOfCOX'] = 1
				_VIAPMOSMet23Routing['_ViaMet22Met3NumberOfCOY'] = 2
				self._DesignParameter['_VIAPMOSMet23forRouting'] = self._SrefElementDeclaration( _DesignObj=ViaMet22Met3._ViaMet22Met3(_DesignParameter=None, _Name='{}:VIAPMOSMet23forRouting'.format(_Name)))[0]
				self._DesignParameter['_VIAPMOSMet23forRouting']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureY(**_VIAPMOSMet23Routing)
				self._DesignParameter['_VIAPMOSMet23forRouting']['_XYCoordinates'] = [[self.CeilMinSnapSpacing(self._DesignParameter['_ViaMet22Met3OnPMOSOutput']['_XYCoordinates'][0][0] + self._DesignParameter['_VIAPMOSMet23forRouting']['_DesignObj']._DesignParameter['_Met3Layer']['_XWidth'] // 2, MinSnapSpacing), self.CeilMinSnapSpacing((3 * self._DesignParameter['_ViaMet12Met2OnPMOSGate1']['_XYCoordinates'][0][1] + self._DesignParameter['_ViaMet12Met2OnNMOSGate1']['_XYCoordinates'][0][1]) // 4, MinSnapSpacing)]]

				_VIAPMOSMet34Routing = copy.deepcopy(ViaMet32Met4._ViaMet32Met4._ParametersForDesignCalculation)
				_VIAPMOSMet34Routing['_ViaMet32Met4NumberOfCOX'] = 1
				_VIAPMOSMet34Routing['_ViaMet32Met4NumberOfCOY'] = 2
				self._DesignParameter['_VIAPMOSMet34forRouting'] = self._SrefElementDeclaration( _DesignObj=ViaMet32Met4._ViaMet32Met4(_DesignParameter=None, _Name='{}:VIAPMOSMet34forRouting'.format(_Name)))[0]
				self._DesignParameter['_VIAPMOSMet34forRouting']['_DesignObj']._CalculateViaMet32Met4DesignParameterMinimumEnclosureY(**_VIAPMOSMet34Routing)
				self._DesignParameter['_VIAPMOSMet34forRouting']['_XYCoordinates'] = [[self.CeilMinSnapSpacing(self._DesignParameter['_ViaMet22Met3OnPMOSOutput']['_XYCoordinates'][0][0] + self._DesignParameter['_VIAPMOSMet23forRouting']['_DesignObj']._DesignParameter['_Met3Layer']['_XWidth'] // 2, MinSnapSpacing), self.CeilMinSnapSpacing((3 * self._DesignParameter['_ViaMet12Met2OnPMOSGate1']['_XYCoordinates'][0][1] + self._DesignParameter['_ViaMet12Met2OnNMOSGate1']['_XYCoordinates'][0][1]) // 4, MinSnapSpacing)]]




				self._DesignParameter['_CrossPMOSMet2Routing'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _XYCoordinates=[], _Width=400)
				self._DesignParameter['_CrossPMOSMet2Routing']['_Width'] = 2 * _DRCObj._MetalxMinWidth
				self._DesignParameter['_CrossPMOSMet2Routing']['_XYCoordinates'] = [[[self._DesignParameter['_ViaMet12Met2OnPMOSGate1']['_XYCoordinates'][1][0], self.CeilMinSnapSpacing((3 * self._DesignParameter['_ViaMet12Met2OnPMOSGate1']['_XYCoordinates'][0][1] + self._DesignParameter['_ViaMet12Met2OnNMOSGate1']['_XYCoordinates'][0][1]) // 4, MinSnapSpacing)], \
															 self._DesignParameter['_VIAPMOSMet23forRouting']['_XYCoordinates'][0]]]


				del _VIAPMOSMet23Routing




			if _NMOSFinger % 2 == 1 :
				_VIANMOSMet23Routing = copy.deepcopy(ViaMet22Met3._ViaMet22Met3._ParametersForDesignCalculation)
				_VIANMOSMet23Routing['_ViaMet22Met3NumberOfCOX'] = 1
				_VIANMOSMet23Routing['_ViaMet22Met3NumberOfCOY'] = 2
				self._DesignParameter['_VIANMOSMet23forRouting'] = self._SrefElementDeclaration( _DesignObj=ViaMet22Met3._ViaMet22Met3(_DesignParameter=None, _Name='{}:VIANMOSMet23forRouting'.format(_Name)))[0]
				self._DesignParameter['_VIANMOSMet23forRouting']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureY(**_VIANMOSMet23Routing)
				self._DesignParameter['_VIANMOSMet23forRouting']['_XYCoordinates'] = [[self._DesignParameter['_NMOSSET']['_XYCoordinates'][0][0], self.CeilMinSnapSpacing((self._DesignParameter['_ViaMet12Met2OnPMOSGate1']['_XYCoordinates'][0][1] + 3 * self._DesignParameter['_ViaMet12Met2OnNMOSGate1']['_XYCoordinates'][0][1]) // 4, MinSnapSpacing)]]

				self._DesignParameter['_CrossNMOSMet3Routing'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0], _Datatype=DesignParameters._LayerMapping['METAL3'][1], _XYCoordinates=[], _Width=400)
				self._DesignParameter['_CrossNMOSMet3Routing']['_Width'] = self.CeilMinSnapSpacing(1.5 * _DRCObj._MetalxMinWidth, 2*MinSnapSpacing)
				self._DesignParameter['_CrossNMOSMet3Routing']['_XYCoordinates'] = [[[self._DesignParameter['_ViaMet22Met3OnNMOSOutput']['_XYCoordinates'][1][0], self.CeilMinSnapSpacing((self._DesignParameter['_ViaMet12Met2OnPMOSGate1']['_XYCoordinates'][0][1] + 3 * self._DesignParameter['_ViaMet12Met2OnNMOSGate1']['_XYCoordinates'][0][1]) // 4, MinSnapSpacing)], \
															 self._DesignParameter['_VIANMOSMet23forRouting']['_XYCoordinates'][0]]]


				_VIANMOSMet34Routing = copy.deepcopy(ViaMet32Met4._ViaMet32Met4._ParametersForDesignCalculation)
				_VIANMOSMet34Routing['_ViaMet32Met4NumberOfCOX'] = 1
				_VIANMOSMet34Routing['_ViaMet32Met4NumberOfCOY'] = 2
				self._DesignParameter['_VIANMOSMet34forRouting'] = self._SrefElementDeclaration( _DesignObj=ViaMet32Met4._ViaMet32Met4(_DesignParameter=None, _Name='{}:VIANMOSMet34orRouting'.format(_Name)))[0]
				self._DesignParameter['_VIANMOSMet34forRouting']['_DesignObj']._CalculateViaMet32Met4DesignParameter(**_VIANMOSMet34Routing)
				self._DesignParameter['_VIANMOSMet34forRouting']['_XYCoordinates'] = [[self.CeilMinSnapSpacing(self._DesignParameter['_ViaMet22Met3OnNMOSOutput']['_XYCoordinates'][1][0] + self._DesignParameter['_VIANMOSMet34forRouting']['_DesignObj']._DesignParameter['_Met4Layer']['_XWidth'] // 2 - _DRCObj._MetalxMinWidth, MinSnapSpacing), self.CeilMinSnapSpacing((self._DesignParameter['_ViaMet12Met2OnPMOSGate1']['_XYCoordinates'][0][1] + 3 * self._DesignParameter['_ViaMet12Met2OnNMOSGate1']['_XYCoordinates'][0][1]) // 4, MinSnapSpacing)]]



				self._DesignParameter['_CrossNMOSMet2Routing'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _XYCoordinates=[], _Width=400)
				self._DesignParameter['_CrossNMOSMet2Routing']['_Width'] = self.CeilMinSnapSpacing(1.5 * _DRCObj._MetalxMinWidth, 2*MinSnapSpacing)
				self._DesignParameter['_CrossNMOSMet2Routing']['_XYCoordinates'] = [[[self._DesignParameter['_ViaMet12Met2OnNMOSGate1']['_XYCoordinates'][0][0], self.CeilMinSnapSpacing((self._DesignParameter['_ViaMet12Met2OnPMOSGate1']['_XYCoordinates'][0][1] + 3 * self._DesignParameter['_ViaMet12Met2OnNMOSGate1']['_XYCoordinates'][0][1]) // 4, MinSnapSpacing)], \
															 self._DesignParameter['_VIANMOSMet23forRouting']['_XYCoordinates'][0]]]

				del _VIANMOSMet23Routing


			elif _NMOSFinger == 2 :
				_VIANMOSMet23Routing = copy.deepcopy(ViaMet22Met3._ViaMet22Met3._ParametersForDesignCalculation)
				_VIANMOSMet23Routing['_ViaMet22Met3NumberOfCOX'] = 1
				_VIANMOSMet23Routing['_ViaMet22Met3NumberOfCOY'] = 2
				self._DesignParameter['_VIANMOSMet23forRouting'] = self._SrefElementDeclaration( _DesignObj=ViaMet22Met3._ViaMet22Met3(_DesignParameter=None, _Name='{}:VIANMOSMet23forRouting'.format(_Name)))[0]
				self._DesignParameter['_VIANMOSMet23forRouting']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureY(**_VIANMOSMet23Routing)
				self._DesignParameter['_VIANMOSMet23forRouting']['_XYCoordinates'] = [[self.CeilMinSnapSpacing(self._DesignParameter['_ViaMet22Met3OnNMOSOutput']['_XYCoordinates'][1][0] - self._DesignParameter['_VIAPMOSMet23forRouting']['_DesignObj']._DesignParameter['_Met3Layer']['_XWidth'] // 2, MinSnapSpacing), self.CeilMinSnapSpacing((self._DesignParameter['_ViaMet12Met2OnPMOSGate1']['_XYCoordinates'][0][1] + 3 * self._DesignParameter['_ViaMet12Met2OnNMOSGate1']['_XYCoordinates'][0][1]) // 4, MinSnapSpacing)]]


				_VIANMOSMet34Routing = copy.deepcopy(ViaMet32Met4._ViaMet32Met4._ParametersForDesignCalculation)
				_VIANMOSMet34Routing['_ViaMet32Met4NumberOfCOX'] = 1
				_VIANMOSMet34Routing['_ViaMet32Met4NumberOfCOY'] = 2
				self._DesignParameter['_VIANMOSMet34forRouting'] = self._SrefElementDeclaration( _DesignObj=ViaMet32Met4._ViaMet32Met4(_DesignParameter=None, _Name='{}:VIANMOSMet34orRouting'.format(_Name)))[0]
				self._DesignParameter['_VIANMOSMet34forRouting']['_DesignObj']._CalculateViaMet32Met4DesignParameterMinimumEnclosureY(**_VIANMOSMet34Routing)
				self._DesignParameter['_VIANMOSMet34forRouting']['_XYCoordinates'] = [[self.CeilMinSnapSpacing(self._DesignParameter['_ViaMet22Met3OnNMOSOutput']['_XYCoordinates'][1][0] - self._DesignParameter['_VIAPMOSMet23forRouting']['_DesignObj']._DesignParameter['_Met3Layer']['_XWidth'] // 2, MinSnapSpacing), self.CeilMinSnapSpacing((self._DesignParameter['_ViaMet12Met2OnPMOSGate1']['_XYCoordinates'][0][1] + 3 * self._DesignParameter['_ViaMet12Met2OnNMOSGate1']['_XYCoordinates'][0][1]) // 4, MinSnapSpacing)]]


				self._DesignParameter['_CrossNMOSMet2Routing'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _XYCoordinates=[], _Width=400)
				self._DesignParameter['_CrossNMOSMet2Routing']['_Width'] = self.CeilMinSnapSpacing(1.5 * _DRCObj._MetalxMinWidth, 2*MinSnapSpacing)
				self._DesignParameter['_CrossNMOSMet2Routing']['_XYCoordinates'] = [[[self._DesignParameter['_ViaMet12Met2OnNMOSGate1']['_XYCoordinates'][0][0], self.CeilMinSnapSpacing((self._DesignParameter['_ViaMet12Met2OnPMOSGate1']['_XYCoordinates'][0][1] + 3 * self._DesignParameter['_ViaMet12Met2OnNMOSGate1']['_XYCoordinates'][0][1]) // 4, MinSnapSpacing)], \
															 self._DesignParameter['_VIANMOSMet23forRouting']['_XYCoordinates'][0]]]

				del _VIANMOSMet23Routing


				self._DesignParameter['_CrossNMOSMet2Routing'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _XYCoordinates=[], _Width=400)
				self._DesignParameter['_CrossNMOSMet2Routing']['_Width'] = self.CeilMinSnapSpacing(1.5 * _DRCObj._MetalxMinWidth, 2*MinSnapSpacing)
				self._DesignParameter['_CrossNMOSMet2Routing']['_XYCoordinates'] = [[[self._DesignParameter['_ViaMet12Met2OnNMOSGate1']['_XYCoordinates'][0][0], self.CeilMinSnapSpacing((self._DesignParameter['_ViaMet12Met2OnPMOSGate1']['_XYCoordinates'][0][1] + 3 * self._DesignParameter['_ViaMet12Met2OnNMOSGate1']['_XYCoordinates'][0][1]) // 4, MinSnapSpacing)], \
															 self._DesignParameter['_VIANMOSMet23forRouting']['_XYCoordinates'][0]]]





			else :
				_VIANMOSMet23Routing = copy.deepcopy(ViaMet22Met3._ViaMet22Met3._ParametersForDesignCalculation)
				_VIANMOSMet23Routing['_ViaMet22Met3NumberOfCOX'] = 1
				_VIANMOSMet23Routing['_ViaMet22Met3NumberOfCOY'] = 2
				self._DesignParameter['_VIANMOSMet23forRouting'] = self._SrefElementDeclaration( _DesignObj=ViaMet22Met3._ViaMet22Met3(_DesignParameter=None, _Name='{}:VIANMOSMet23forRouting'.format(_Name)))[0]
				self._DesignParameter['_VIANMOSMet23forRouting']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureY(**_VIANMOSMet23Routing)
				self._DesignParameter['_VIANMOSMet23forRouting']['_XYCoordinates'] = [[self.CeilMinSnapSpacing(self._DesignParameter['_ViaMet22Met3OnNMOSOutput']['_XYCoordinates'][1][0] - self._DesignParameter['_VIAPMOSMet23forRouting']['_DesignObj']._DesignParameter['_Met3Layer']['_XWidth'] // 2, MinSnapSpacing), self.CeilMinSnapSpacing((self._DesignParameter['_ViaMet12Met2OnPMOSGate1']['_XYCoordinates'][0][1] + 3 * self._DesignParameter['_ViaMet12Met2OnNMOSGate1']['_XYCoordinates'][0][1]) // 4, MinSnapSpacing)]]

				_VIANMOSMet34Routing = copy.deepcopy(ViaMet32Met4._ViaMet32Met4._ParametersForDesignCalculation)
				_VIANMOSMet34Routing['_ViaMet32Met4NumberOfCOX'] = 1
				_VIANMOSMet34Routing['_ViaMet32Met4NumberOfCOY'] = 2
				self._DesignParameter['_VIANMOSMet34forRouting'] = self._SrefElementDeclaration( _DesignObj=ViaMet32Met4._ViaMet32Met4(_DesignParameter=None, _Name='{}:VIANMOSMet34orRouting'.format(_Name)))[0]
				self._DesignParameter['_VIANMOSMet34forRouting']['_DesignObj']._CalculateViaMet32Met4DesignParameterMinimumEnclosureY(**_VIANMOSMet34Routing)
				self._DesignParameter['_VIANMOSMet34forRouting']['_XYCoordinates'] = [[self.CeilMinSnapSpacing(self._DesignParameter['_ViaMet22Met3OnNMOSOutput']['_XYCoordinates'][1][0] - self._DesignParameter['_VIAPMOSMet23forRouting']['_DesignObj']._DesignParameter['_Met3Layer']['_XWidth'] // 2, MinSnapSpacing), self.CeilMinSnapSpacing((self._DesignParameter['_ViaMet12Met2OnPMOSGate1']['_XYCoordinates'][0][1] + 3 * self._DesignParameter['_ViaMet12Met2OnNMOSGate1']['_XYCoordinates'][0][1]) // 4, MinSnapSpacing)]]



				self._DesignParameter['_CrossNMOSMet2Routing'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _XYCoordinates=[], _Width=400)
				self._DesignParameter['_CrossNMOSMet2Routing']['_Width'] = 2 * _DRCObj._MetalxMinWidth
				self._DesignParameter['_CrossNMOSMet2Routing']['_XYCoordinates'] = [[[self._DesignParameter['_ViaMet12Met2OnNMOSGate1']['_XYCoordinates'][0][0], self.CeilMinSnapSpacing((self._DesignParameter['_ViaMet12Met2OnPMOSGate1']['_XYCoordinates'][0][1] + 3 * self._DesignParameter['_ViaMet12Met2OnNMOSGate1']['_XYCoordinates'][0][1]) // 4, MinSnapSpacing)], \
															 self._DesignParameter['_VIANMOSMet23forRouting']['_XYCoordinates'][0]]]


				del _VIANMOSMet23Routing


			self._DesignParameter['_AdditionalMet3Layer'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0], _Datatype=DesignParameters._LayerMapping['METAL3'][1], _XYCoordinates=[], _Width=400)
			self._DesignParameter['_AdditionalMet3Layer']['_Width'] = _DRCObj._MetalxMinWidth
			self._DesignParameter['_AdditionalMet3Layer']['_XYCoordinates'] = [[[self._DesignParameter['_ViaMet324PNMOSDrain']['_XYCoordinates'][0][0], self._DesignParameter['_ViaMet22Met3OnNMOSInput']['_XYCoordinates'][0][1]], \
																				[self._DesignParameter['_ViaMet324PNMOSDrain']['_XYCoordinates'][-2][0], self._DesignParameter['_ViaMet22Met3OnNMOSInput']['_XYCoordinates'][0][1]]], \
																			   [[self._DesignParameter['_ViaMet324PNMOSDrain']['_XYCoordinates'][1][0], self._DesignParameter['_ViaMet22Met3OnNMOSInput']['_XYCoordinates'][0][1]], \
																				[self._DesignParameter['_ViaMet324PNMOSDrain']['_XYCoordinates'][-1][0], self._DesignParameter['_ViaMet22Met3OnNMOSInput']['_XYCoordinates'][0][1]]]
																			   ]

			self._DesignParameter['_AdditionalMet3Layer2'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0], _Datatype=DesignParameters._LayerMapping['METAL3'][1], _XYCoordinates=[], _XWidth=400, _YWidth=400)
			self._DesignParameter['_AdditionalMet3Layer2']['_XWidth'] = self._DesignParameter['_ViaMet22Met3OnNMOSCLKInput']['_DesignObj']._DesignParameter['_Met3Layer']['_XWidth']
			self._DesignParameter['_AdditionalMet3Layer2']['_YWidth'] = self._DesignParameter['_Met3CLKinput']['_Width']
			self._DesignParameter['_AdditionalMet3Layer2']['_XYCoordinates'] = [[self._DesignParameter['_ViaMet22Met3OnNMOSCLKInput']['_XYCoordinates'][0][0], self.CeilMinSnapSpacing(self._DesignParameter['_ViaMet22Met3OnNMOSCLKInput']['_XYCoordinates'][0][1] + self._DesignParameter['_AdditionalMet3Layer2']['_YWidth'] // 2 - self._DesignParameter['_ViaMet22Met3OnNMOSCLKInput']['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth'] // 2, MinSnapSpacing)]]




			if _PowerLine == True :
				Ptoptmp = self._DesignParameter['_PMOSSET']['_XYCoordinates'][0][1] + self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_Guardring']['_XYCoordinates'][0][1] + self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_Guardring']['_DesignObj']._DesignParameter['_Met1Layerx']['_XYCoordinates'][0][1]
				Gtoptmp = self._DesignParameter['_Guardring']['_XYCoordinates'][0][1] + self._DesignParameter['_Guardring']['_DesignObj']._DesignParameter['_Met1Layerx']['_XYCoordinates'][1][1]

				self._DesignParameter['_SupplyLineMet2VSS'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _XYCoordinates=[], _XWidth=400, _YWidth=400)
				self._DesignParameter['_SupplyLineMet2VSS']['_XWidth'] = self._DesignParameter['_GuardringVSS']['_XWidth']
				self._DesignParameter['_SupplyLineMet2VSS']['_YWidth'] = self._DesignParameter['_GuardringVSS']['_YWidth']
				self._DesignParameter['_SupplyLineMet2VSS']['_XYCoordinates'] = self._DesignParameter['_GuardringVSS']['_XYCoordinates']

				self._DesignParameter['_SupplyLineMet3VSS'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0], _Datatype=DesignParameters._LayerMapping['METAL3'][1], _XYCoordinates=[], _XWidth=400, _YWidth=400)
				self._DesignParameter['_SupplyLineMet3VSS']['_XWidth'] = self._DesignParameter['_GuardringVSS']['_XWidth']
				self._DesignParameter['_SupplyLineMet3VSS']['_YWidth'] = self._DesignParameter['_GuardringVSS']['_YWidth']
				self._DesignParameter['_SupplyLineMet3VSS']['_XYCoordinates'] = self._DesignParameter['_GuardringVSS']['_XYCoordinates']


				_ViaNumVSSX12 = int((self._DesignParameter['_SupplyLineMet2VSS']['_XWidth'] - 2 * _DRCObj._VIAxMinEnclosureByMetxTwoOppositeSide - _DRCObj._VIAxMinWidth) / (_DRCObj._VIAxMinSpace2 + _DRCObj._VIAxMinWidth)) + 1
				_ViaNumVSSY12 = int((self._DesignParameter['_SupplyLineMet2VSS']['_YWidth'] - _DRCObj._VIAxMinWidth) / (_DRCObj._VIAxMinSpace2 + _DRCObj._VIAxMinWidth)) + 1
				_ViaNumVSSX23 = int((self._DesignParameter['_SupplyLineMet3VSS']['_XWidth'] - 2 * _DRCObj._VIAxMinEnclosureByMetxTwoOppositeSide - _DRCObj._VIAxMinWidth) / (_DRCObj._VIAxMinSpace2 + _DRCObj._VIAxMinWidth)) + 1
				_ViaNumVSSY23 = int((self._DesignParameter['_SupplyLineMet3VSS']['_YWidth'] - _DRCObj._VIAxMinWidth) / (_DRCObj._VIAxMinSpace2 + _DRCObj._VIAxMinWidth)) + 1


				if _ViaNumVSSX12 <= 1 :
					_ViaNumVSSX12 = 1
					_ViaNumVSSY12 = int((self._DesignParameter['_SupplyLineMet2VSS']['_YWidth'] - _DRCObj._VIAxMinWidth) / (_DRCObj._VIAxMinSpace + _DRCObj._VIAxMinWidth)) + 1

				if _ViaNumVSSY12 <= 1:
					_ViaNumVSSY12 = 1
					_ViaNumVSSX12 = int((self._DesignParameter['_SupplyLineMet2VSS']['_XWidth'] - 2 * _DRCObj._VIAxMinEnclosureByMetxTwoOppositeSide - _DRCObj._VIAxMinWidth) / (_DRCObj._VIAxMinSpace + _DRCObj._VIAxMinWidth)) + 1

				if _ViaNumVSSX23 <= 1 :
					_ViaNumVSSX23 = 1
					_ViaNumVSSY23 = int((self._DesignParameter['_SupplyLineMet3VSS']['_YWidth'] - _DRCObj._VIAxMinWidth) / (_DRCObj._VIAxMinSpace + _DRCObj._VIAxMinWidth)) + 1

				if _ViaNumVSSY23 <= 1:
					_ViaNumVSSY23 = 1
					_ViaNumVSSX23 = int((self._DesignParameter['_SupplyLineMet3VSS'][ '_XWidth'] - 2 * _DRCObj._VIAxMinEnclosureByMetxTwoOppositeSide - _DRCObj._VIAxMinWidth) / (_DRCObj._VIAxMinSpace + _DRCObj._VIAxMinWidth)) + 1



				_ViaVSSMet12Met2 = copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation)
				_ViaVSSMet12Met2['_ViaMet12Met2NumberOfCOX'] = _ViaNumVSSX12
				_ViaVSSMet12Met2['_ViaMet12Met2NumberOfCOY'] = _ViaNumVSSY12
				self._DesignParameter['_ViaMet12Met2VSS'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_DesignParameter=None, _Name = '{}:ViaMet12Met2VSS'.format(_Name)))[0]
				self._DesignParameter['_ViaMet12Met2VSS']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureY(**_ViaVSSMet12Met2)
				self._DesignParameter['_ViaMet12Met2VSS']['_XYCoordinates'] = self._DesignParameter['_SupplyLineMet2VSS']['_XYCoordinates']

				_ViaVSSMet22Met3 = copy.deepcopy(ViaMet22Met3._ViaMet22Met3._ParametersForDesignCalculation)
				_ViaVSSMet22Met3['_ViaMet22Met3NumberOfCOX'] = _ViaNumVSSX23
				_ViaVSSMet22Met3['_ViaMet22Met3NumberOfCOY'] = _ViaNumVSSY23
				self._DesignParameter['_ViaMet22Met3VSS'] = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_DesignParameter=None, _Name = '{}:ViaMet22Met3VSS'.format(_Name)))[0]
				self._DesignParameter['_ViaMet22Met3VSS']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureY(**_ViaVSSMet22Met3)
				self._DesignParameter['_ViaMet22Met3VSS']['_XYCoordinates'] = self._DesignParameter['_SupplyLineMet2VSS']['_XYCoordinates']




				_LengthofSupplyLine = self._DesignParameter['_PMOSSET']['_DesignObj']._DesignParameter['_Guardring']['_DesignObj']._DesignParameter['_Met1Layerx']['_XWidth']


				self._DesignParameter['_SupplyLineMet2VDD'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _XYCoordinates=[], _XWidth=400, _YWidth=400)
				self._DesignParameter['_SupplyLineMet2VDD']['_XWidth'] = _LengthofSupplyLine
				self._DesignParameter['_SupplyLineMet2VDD']['_YWidth'] = _GuardringWidth
				self._DesignParameter['_SupplyLineMet2VDD']['_XYCoordinates'] = [[self._DesignParameter['_GuardringVSS']['_XYCoordinates'][0][0], Ptoptmp]]

				self._DesignParameter['_SupplyLineMet3VDD'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0], _Datatype=DesignParameters._LayerMapping['METAL3'][1], _XYCoordinates=[], _XWidth=400, _YWidth=400)
				self._DesignParameter['_SupplyLineMet3VDD']['_XWidth'] = _LengthofSupplyLine
				self._DesignParameter['_SupplyLineMet3VDD']['_YWidth'] = _GuardringWidth
				self._DesignParameter['_SupplyLineMet3VDD']['_XYCoordinates'] = [[self._DesignParameter['_GuardringVSS']['_XYCoordinates'][0][0], Ptoptmp]]


				_ViaNumVDDX12 = int((_LengthofSupplyLine - 2 * _DRCObj._VIAxMinEnclosureByMetxTwoOppositeSide - _DRCObj._VIAxMinWidth) / (_DRCObj._VIAxMinSpace2 + _DRCObj._VIAxMinWidth)) + 1
				_ViaNumVDDX23 = int((_LengthofSupplyLine - 2 * _DRCObj._VIAxMinEnclosureByMetxTwoOppositeSide - _DRCObj._VIAxMinWidth) / (_DRCObj._VIAxMinSpace2 + _DRCObj._VIAxMinWidth)) + 1

				_ViaNumVDDY12 = int((_GuardringWidth - _DRCObj._VIAxMinWidth) / (_DRCObj._VIAxMinSpace2 + _DRCObj._VIAxMinWidth)) + 1
				_ViaNumVDDY23 = int((_GuardringWidth - _DRCObj._VIAxMinWidth) / (_DRCObj._VIAxMinSpace2 + _DRCObj._VIAxMinWidth)) + 1

				if _ViaNumVDDX12 <= 1:
					_ViaNumVDDX12 = 1
					_ViaNumVDDY12 = int((_GuardringWidth - _DRCObj._VIAxMinWidth) / (_DRCObj._VIAxMinSpace + _DRCObj._VIAxMinWidth)) + 1

				if _ViaNumVDDX23 <= 1:
					_ViaNumVDDX23 = 1
					_ViaNumVDDY23 = int((_GuardringWidth - _DRCObj._VIAxMinWidth) / (_DRCObj._VIAxMinSpace+ _DRCObj._VIAxMinWidth)) + 1


				if _ViaNumVDDY12 <= 1:
					_ViaNumVDDY12 = 1
					_ViaNumVDDX12 = int((_LengthofSupplyLine - 2 * _DRCObj._VIAxMinEnclosureByMetxTwoOppositeSide - _DRCObj._VIAxMinWidth) / (_DRCObj._VIAxMinSpace + _DRCObj._VIAxMinWidth)) + 1

				if _ViaNumVDDY23 <= 1:
					_ViaNumVDDY23 = 1
					_ViaNumVDDX23 = int((_LengthofSupplyLine  - 2 * _DRCObj._VIAxMinEnclosureByMetxTwoOppositeSide - _DRCObj._VIAxMinWidth) / (_DRCObj._VIAxMinSpace + _DRCObj._VIAxMinWidth)) + 1

				_ViaVDDMet12Met2 = copy.deepcopy(ViaMet12Met2._ViaMet12Met2._ParametersForDesignCalculation)
				_ViaVDDMet12Met2['_ViaMet12Met2NumberOfCOX'] = _ViaNumVDDX12
				_ViaVDDMet12Met2['_ViaMet12Met2NumberOfCOY'] = _ViaNumVDDY12
				self._DesignParameter['_ViaMet12Met2VDD'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_DesignParameter=None, _Name='{}:ViaMet12Met2VDD'.format(_Name)))[0]
				self._DesignParameter['_ViaMet12Met2VDD']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureY(**_ViaVDDMet12Met2)
				self._DesignParameter['_ViaMet12Met2VDD']['_XYCoordinates'] = [[self._DesignParameter['_PMOSSET']['_XYCoordinates'][0][0], Ptoptmp]]

				_ViaVDDMet22Met3 = copy.deepcopy(ViaMet22Met3._ViaMet22Met3._ParametersForDesignCalculation)
				_ViaVDDMet22Met3['_ViaMet22Met3NumberOfCOX'] = _ViaNumVDDX23
				_ViaVDDMet22Met3['_ViaMet22Met3NumberOfCOY'] = _ViaNumVDDY23
				self._DesignParameter['_ViaMet22Met3VDD'] = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_DesignParameter=None, _Name='{}:ViaMet22Met3VDD'.format(_Name)))[0]
				self._DesignParameter['_ViaMet22Met3VDD']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureY(**_ViaVDDMet22Met3)
				self._DesignParameter['_ViaMet22Met3VDD']['_XYCoordinates'] = [[self._DesignParameter['_PMOSSET']['_XYCoordinates'][0][0], Ptoptmp]]




			if _DATAinputNMOSFinger == 1 or _DATAinputNMOSFinger == 2:
				print("The input signal can be disturbed.")
				raise NotImplementedError





if __name__ == '__main__':

	for i in range(1,2) :
		_CLKinputPMOSFinger1 = 6#random.randint(1, 15)
		_CLKinputPMOSFinger2 = 3#random.randint(1, 15)
		_PMOSFinger = 3#random.randint(1, 15)
		_PMOSChannelWidth = 500#random.randrange(200, 1050, 2)
		_DATAinputNMOSFinger = 12#random.randint(3, 15)
		_NMOSFinger = 2#random.randint(1, 15)
		_CLKinputNMOSFinger = 8#random.randint(1, 15)
		_NMOSChannelWidth = 500#random.randrange(200, 1050, 2)
		_CLKinputNMOSChannelWidth = 800#random.randrange(200, 1050, 2)
		_ChannelLength = 30 #random.randrange(30, 60, 2)
		_Dummy = True
		_XVT = 'SLVT'
		_GuardringWidth = 200
		_Guardring = True
		_SlicerGuardringWidth = 200
		_SlicerGuardring = None
		_NumSupplyCOY = None
		_NumSupplyCOX = None
		_SupplyMet1XWidth = None
		_SupplyMet1YWidth = None
		_VDD2VSSHeight = None
		_NumVIAPoly2Met1COX = None
		_NumVIAPoly2Met1COY = None
		_NumVIAMet12COX = None
		_NumVIAMet12COY = None
		_PowerLine = False





		libname = 'E00_Slicer'
		cellname = 'E00_Slicer_v1'
		_fileName = cellname + '.gds'

		InputParams = dict(
			_CLKinputPMOSFinger1=6,  # random.randint(1, 15),  # 6
			_CLKinputPMOSFinger2=3,  # random.randint(1, 15),  # 3
			_PMOSFinger=3,  # random.randint(1, 15),  # 3
			_PMOSChannelWidth=500,  # random.randrange(200, 1050, 2),  # 500
			_DATAinputNMOSFinger=12,  # random.randint(3, 15),  # 12
			_NMOSFinger=2,  # random.randint(1, 15),  # 2
			_CLKinputNMOSFinger=8,  # random.randint(1, 15),  # 8
			_NMOSChannelWidth=500,  # random.randrange(200, 1050, 2),  # 500
			_CLKinputNMOSChannelWidth=800,  # random.randrange(200, 1050, 2),  # 800
			_ChannelLength=30,  # random.randrange(30, 60, 2),  # 30
			_Dummy=True,
			_XVT='SLVT',
			_GuardringWidth=200,
			_Guardring=True,
			_SlicerGuardringWidth=200,
			_SlicerGuardring=None,
			_NumSupplyCOY=None,
			_NumSupplyCOX=None,
			_SupplyMet1XWidth=None,
			_SupplyMet1YWidth=None,
			_VDD2VSSHeight=None,
			_NumVIAPoly2Met1COX=None,
			_NumVIAPoly2Met1COY=None,
			_NumVIAMet12COX=None,
			_NumVIAMet12COY=None,
			_PowerLine=False,
		)
		LayoutObj = _Slicer(_DesignParameter=None, _Name=cellname)
		LayoutObj._CalculateDesignParameter(**InputParams)
		LayoutObj._UpdateDesignParameter2GDSStructure(_DesignParameterInDictionary=LayoutObj._DesignParameter)
		testStreamFile = open('./{}'.format(_fileName), 'wb')
		tmp = LayoutObj._CreateGDSStream(LayoutObj._DesignParameter['_GDSFile']['_GDSFile'])
		tmp.write_binary_gds_stream(testStreamFile)
		testStreamFile.close()

		# print('#############################      Sending to FTP Server...      #############################')
		# My = MyInfo.USER(DesignParameters._Technology)
		# Checker = DRCchecker.DRCchecker(
		# 	username=My.ID,
		# 	password=My.PW,
		# 	WorkDir=My.Dir_Work,
		# 	DRCrunDir=My.Dir_DRCrun,
		# 	libname=libname,
		# 	cellname=cellname,
		# 	GDSDir=My.Dir_GDS
		# )
		# Checker.Upload2FTP()
		# Checker.StreamIn(tech=DesignParameters._Technology)


	#     import ftplib
	#
	#     ftp = ftplib.FTP('141.223.29.62')
	#     ftp.login('jicho0927', 'cho89140616!!')
	#     ftp.cwd('/mnt/sdc/jicho0927/OPUS/SAMSUNG28n')
	#     myfile = open('E00_Slicer.gds', 'rb')
	#     ftp.storbinary('STOR E00_Slicer.gds', myfile)
	#     myfile.close()
	#
	#     import DRCchecker
	#     a = DRCchecker.DRCchecker('jicho0927','cho89140616!!','/mnt/sdc/jicho0927/OPUS/SAMSUNG28n','/mnt/sdc/jicho0927/OPUS/SAMSUNG28n/DRC/run','E00_Slicer','E00_Slicer',None)
	#     a.DRCchecker()
	#
	# print ("DRC Clean!!!")

	#     import ftplib
	#
	#     ftp = ftplib.FTP(''141.223.29.62')
	#     ftp.login('jicho0927', 'cho89140616!!')
	#     ftp.cwd('/mnt/sdc/jicho0927/OPUS/tsmc40n')
	#     myfile = open('E00_Slicer.gds', 'rb')
	#     ftp.storbinary('STOR E00_Slicer.gds', myfile)
	#     myfile.close()
	#
	#     import DRCchecker
	#     a = DRCchecker.DRCchecker('jicho0927','cho89140616!!','/mnt/sdc/jicho0927/OPUS/tsmc40n','/mnt/sdc/jicho0927/OPUS/tsmc40n/DRC/run','E00_Slicer','E00_Slicer',None)
	#     a.DRCchecker()
	#
	#
	# print ("DRC Clean!!!")

	#     import ftplib
	#
	#     ftp = ftplib.FTP('141.223.29.62')
	#     ftp.login('jicho0927', 'cho89140616!!')
	#     ftp.cwd('/mnt/sdc/jicho0927/OPUS/tsmc65n')
	#     myfile = open('E00_Slicer.gds', 'rb')
	#     ftp.storbinary('STOR E00_Slicer.gds', myfile)
	#     myfile.close()
	#
	#     import DRCchecker
	#     a = DRCchecker.DRCchecker('jicho0927','cho89140616!!','/mnt/sdc/jicho0927/OPUS/tsmc65n','/mnt/sdc/jicho0927/OPUS/tsmc65n/DRC/run','E00_Slicer','E00_Slicer',None)
	#     a.DRCchecker()
	#
	# print ("DRC Clean!!!")


	#     import ftplib
	#
	#     ftp = ftplib.FTP('141.223.29.62')
	#     ftp.login('jicho0927', 'cho89140616!!')
	#     ftp.cwd('/mnt/sdc/jicho0927/OPUS/tsmc90n')
	#     myfile = open('E00_Slicer.gds', 'rb')
	#     ftp.storbinary('STOR E00_Slicer.gds', myfile)
	#     myfile.close()
	#
	#     import DRCchecker
	#     a = DRCchecker.DRCchecker('jicho0927','cho89140616!!','/mnt/sdc/jicho0927/OPUS/tsmc90n','/mnt/sdc/jicho0927/OPUS/tsmc90n/DRC/run','E00_Slicer','E00_Slicer',None)
	#     a.DRCchecker()
	#
	#
	# print ("DRC Clean!!!")