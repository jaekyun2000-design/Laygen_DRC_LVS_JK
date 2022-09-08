from generatorLib import StickDiagram
from generatorLib import DesignParameters
import copy
import math
from generatorLib import DRC
from generatorLib.generator_models import NMOSWithDummy
from generatorLib.generator_models import ViaPoly2Met1
from generatorLib.generator_models import PSubRing

class _NCap(StickDiagram._StickDiagram):
	_ParametersForDesignCalculation = dict(_XWidth=None, _YWidth=None, _NumofGates=None, NumOfCOX=None, NumOfCOY=None,
										   Guardring=True, guardring_height=None, guardring_width=None, guardring_right=None, guardring_left=None, guardring_top=None, guardring_bot=None)
	def __init__(self, _DesignParameter=None, _Name='NCap'):
		if _DesignParameter != None:
			self._DesignParameter = _DesignParameter
		else:
			self._DesignParameter = dict(
				_POLayer=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0],
														  _Datatype=DesignParameters._LayerMapping['POLY'][1],
														  _XYCoordinates=[], _XWidth=400, _YWidth=400),
				_ODLayer=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['DIFF'][0],
														  _Datatype=DesignParameters._LayerMapping['DIFF'][1],
														  _XYCoordinates=[], _XWidth=400, _YWidth=400),
				_Met1Layer1=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0],
															 _Datatype=DesignParameters._LayerMapping['METAL1'][1],
															 _XYCoordinates=[], _XWidth=400, _YWidth=400),
				_Met1Layer2=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0],
															 _Datatype=DesignParameters._LayerMapping['METAL1'][1],
															 _XYCoordinates=[], _XWidth=400, _YWidth=400),
				_COLayer=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['CONT'][0],
														  _Datatype=DesignParameters._LayerMapping['CONT'][1],
														  _XYCoordinates=[], _XWidth=400, _YWidth=400),
				_Name=self._NameDeclaration(_Name=_Name), _GDSFile=self._GDSObjDeclaration(_GDSFile=None),
				_XYCoordinateM1inPO=dict(_DesignParametertype=7, _XYCoordinates=[]),
				_XYCoordinateM1inOD=dict(_DesignParametertype=7, _XYCoordinates=[]))

		if _Name != None:
			self._DesignParameter['_Name']['Name'] = _Name

	# def _CalculateDesignParameter(self, length=2500, width=1000, Xnum=1, Ynum=4, Guardring=True, guardring_height=None, guardring_width=None, guardring_right=2, guardring_left=2, guardring_top=2, guardring_bot=2):
	#
	# 	drc = DRC.DRC()
	# 	_Name = self._DesignParameter['_Name']['_Name']
		# _OriginXY=[[0,0]]
		#
		# self._DesignParameter['nmos'] = self._SrefElementDeclaration(_DesignObj=NMOSWithDummy._NMOS(_Name='nmosIn{}'.format(_Name)))[0]
		# self._DesignParameter['nmos']['_DesignObj']._CalculateNMOSDesignParameter(**dict(_NMOSNumberofGate=Xnum, _NMOSChannelWidth=width, _NMOSChannellength=length, _NMOSDummy=False, _GateSpacing=drc._PolygateSpace_ncap, _SDWidth=drc._Metal1MinSpace21, _XVT='LVT', _PCCrit=False))
		# #self._DesignParameter['nmos']['_XYCoordinates'] = _OriginXY
		#
		# ########## To erase XVT Layer(LVT is set temporarily) ##########
		# _XVTLayer='_LVTLayer'
		# self._DesignParameter['nmos']['_DesignObj']._DesignParameter[_XVTLayer]['_XWidth']=0
		# self._DesignParameter['nmos']['_DesignObj']._DesignParameter[_XVTLayer]['_YWidth']=0
		#
		# Ydistance_od=self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth']+drc._OdSpace_ncap
		# tmp=[]
		# for i in range(0, Ynum):
		# 	tmp.append([_OriginXY[0][0], _OriginXY[0][1] - (Ynum-1)/2*Ydistance_od+i*Ydistance_od])
		#
		# self._DesignParameter['nmos']['_XYCoordinates'] = tmp
		# del tmp
		#
		# CoX=int((self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']-2*drc._Metal1MinEnclosureCO2)/(drc._CoMinSpace+drc._CoMinWidth))
		#
		# self._DesignParameter['via_poly_m1']=self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_Name='ViaPoly2Met1In{}'.format(_Name)))[0]
		# self._DesignParameter['via_poly_m1']['_DesignObj']._CalculateViaPoly2Met1DesignParameterMinimumEnclosureY(**dict(_ViaPoly2Met1NumberOfCOX=CoX, _ViaPoly2Met1NumberOfCOY=1))
		#
		# del CoX
		#
		# tmp=[]
		# for j in range(0, Ynum+1):
		# 	for i in range(0, Xnum):
		# 		tmp.append([self._DesignParameter['nmos']['_XYCoordinates'][0][0]+self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0], _OriginXY[0][1]-Ynum/2*Ydistance_od+Ydistance_od*j])
		#
		# self._DesignParameter['via_poly_m1']['_XYCoordinates']=tmp
		# del tmp
		#
		# self._DesignParameter['poly']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _Width=self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'])
		#
		# tmp=[]
		# for i in range(0, Xnum):
		# 	tmp.append([[self._DesignParameter['nmos']['_XYCoordinates'][0][0]+self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0], self._DesignParameter['via_poly_m1']['_XYCoordinates'][0][1]-self._DesignParameter['via_poly_m1']['_DesignObj']._DesignParameter['_POLayer']['_YWidth']/2], \
		# 				[self._DesignParameter['nmos']['_XYCoordinates'][0][0]+self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i][0], self._DesignParameter['via_poly_m1']['_XYCoordinates'][-1][1]+self._DesignParameter['via_poly_m1']['_DesignObj']._DesignParameter['_POLayer']['_YWidth']/2]])
		#
		# self._DesignParameter['poly']['_XYCoordinates']=tmp
		# del tmp
	def _CalculateNCapDesignParameter(self, _XWidth=1000, _YWidth=1000, _NumofGates=1, NumOfCOX=None, NumOfCOY=None, Guardring=True, guardring_height=None, guardring_width=None, guardring_right=2, guardring_left=2, guardring_top=2, guardring_bot=2):
		print('#########################################################################################################')
		print('                                    {}  ncap_b Calculation Start                                       '.format(self._DesignParameter['_Name']['_Name']))
		print('#########################################################################################################')

		_DRCObj = DRC.DRC()
		_Name = self._DesignParameter['_Name']['_Name']
		_XYCoordinatesofNcap = [[0, 0]]

		print('#############################     POLY Layer Calculation    ##############################################')
		_DRCgatemaxarea = 38661000 # not in DRC.py
		ODExtensionOnPO = (_DRCObj._OdMinSpace + _DRCObj._CoMinWidth + 2 * _DRCObj._CoMinEnclosureByPOAtLeastTwoSide) * 2 # 80 + 40 + 20

		self._DesignParameter['_POLayer']['_XWidth'] = _XWidth
		# min XWidth = 30nm
		if _XWidth < _DRCObj._PolygateMinWidth:
			raise NotImplementedError("Xwidth should be longer than 30nm")

		self._DesignParameter['_POLayer']['_YWidth'] = _YWidth + ODExtensionOnPO

		if _XWidth * _YWidth > _DRCgatemaxarea:
			raise NotImplementedError("poly max area should be less than 38.661um2")

		tmp = []
		for i in range(_NumofGates):
			tmp.append([_XYCoordinatesofNcap[0][0] + i * (self._DesignParameter['_POLayer']['_XWidth'] + ODExtensionOnPO // 2 + _DRCObj._PolygateMinSpace2OD), _XYCoordinatesofNcap[0][1]])
		self._DesignParameter['_POLayer']['_XYCoordinates'] = tmp
		del tmp

		print('#############################     OD Layer Calculation    ################################################')

		self._DesignParameter['_ODLayer']['_XWidth'] = _XWidth + ODExtensionOnPO
		self._DesignParameter['_ODLayer']['_YWidth'] = _YWidth
		# min YWidth = 80nm
		if _YWidth < _DRCObj._OdMinWidth:
			raise NotImplementedError("Ywidth should be longer than 80nm")

		self._DesignParameter['_ODLayer']['_XYCoordinates'] = self._DesignParameter['_POLayer']['_XYCoordinates']


		print('#############################     CONT Layer Calculation    ##############################################')
		self._DesignParameter['_COLayer']['_XWidth'] = _DRCObj._CoMinWidth
		self._DesignParameter['_COLayer']['_YWidth'] = _DRCObj._CoMinWidth

		_CONUMXOnPO = int(_DRCObj.DRCCOFillAtPoly2Met1(XWidth=_XWidth, YWidth=ODExtensionOnPO, NumOfCOX=NumOfCOX, NumOfCOY=NumOfCOY)[0])
		_CONUMYOnPO = 1
		_CONUMXOnOD = 1
		# CONUMYOnOD값이 정확하지 않다면 새로 결정(1.067um에서는 10개, 1.068um에선 11개 (1.068일떄 OD와 CO 사이의 거리는 0.014))
		_CONUMYOnOD = int(_DRCObj.DRCCOFillAtOD2Met1(XWidth = ODExtensionOnPO,  YWidth = _YWidth, NumOfCOX = NumOfCOX, NumOfCOY=NumOfCOY)[1])

		print("_CONUMXOnPO = %s\n", _CONUMXOnPO)
		print("_CONUMYOnOD = %s\n", _CONUMYOnOD)

		tmp_cont = []
		for k in range(_NumofGates):
			for i in range(_CONUMXOnPO):
				for j in range(_CONUMYOnPO):
					if (_CONUMXOnPO % 2 == 0):
						tmp_cont.append([_XYCoordinatesofNcap[0][0] - (_CONUMXOnPO // 2 - 0.5) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace)
									+ i * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace) + k * (self._DesignParameter['_POLayer']['_XWidth'] + ODExtensionOnPO // 2 + _DRCObj._PolygateMinSpace2OD),
									_XYCoordinatesofNcap[0][1] - self._DesignParameter['_POLayer']['_YWidth'] // 2 + _DRCObj._CoMinEnclosureByPOAtLeastTwoSide
																  + 0.5 * _DRCObj._CoMinWidth + j * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace)])
						tmp_cont.append([_XYCoordinatesofNcap[0][0] - (_CONUMXOnPO // 2 - 0.5) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace)
									+ i * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace) + k * (self._DesignParameter['_POLayer']['_XWidth'] + ODExtensionOnPO // 2 + _DRCObj._PolygateMinSpace2OD),
									_XYCoordinatesofNcap[0][1] + self._DesignParameter['_POLayer']['_YWidth'] // 2 - _DRCObj._CoMinEnclosureByPOAtLeastTwoSide
																  - 0.5 * _DRCObj._CoMinWidth - j * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace)])
					else:
						tmp_cont.append([_XYCoordinatesofNcap[0][0] - (_CONUMXOnPO // 2) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace)
									+ i * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace) + k * (self._DesignParameter['_POLayer']['_XWidth'] + ODExtensionOnPO // 2 + _DRCObj._PolygateMinSpace2OD),
									_XYCoordinatesofNcap[0][1] - self._DesignParameter['_POLayer']['_YWidth'] // 2 + _DRCObj._CoMinEnclosureByPOAtLeastTwoSide
																  + 0.5 * _DRCObj._CoMinWidth + j * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace)])
						tmp_cont.append([_XYCoordinatesofNcap[0][0] - (_CONUMXOnPO // 2) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace)
									+ i * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace) + k * (self._DesignParameter['_POLayer']['_XWidth'] + ODExtensionOnPO // 2 + _DRCObj._PolygateMinSpace2OD),
									_XYCoordinatesofNcap[0][1] + self._DesignParameter['_POLayer']['_YWidth'] // 2 - _DRCObj._CoMinEnclosureByPOAtLeastTwoSide
																  - 0.5 * _DRCObj._CoMinWidth - j * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace)])

			for i in range(_CONUMXOnOD):
				for j in range(_CONUMYOnOD):
					if (_CONUMYOnOD % 2 == 0):
						tmp_cont.append([_XYCoordinatesofNcap[0][0] - self._DesignParameter['_POLayer']['_XWidth'] // 2 - _DRCObj._CoMinSpace
									- 0.5 * _DRCObj._CoMinWidth + i * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace) + k * (self._DesignParameter['_POLayer']['_XWidth'] + ODExtensionOnPO // 2 + _DRCObj._PolygateMinSpace2OD),
									_XYCoordinatesofNcap[0][1] - (_CONUMYOnOD // 2 - 0.5) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace)
									+ j * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2)])
						tmp_cont.append([_XYCoordinatesofNcap[0][0] + self._DesignParameter['_POLayer']['_XWidth'] // 2 + _DRCObj._CoMinSpace
									+ 0.5 * _DRCObj._CoMinWidth - i * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace) + k * (self._DesignParameter['_POLayer']['_XWidth'] + ODExtensionOnPO // 2 + _DRCObj._PolygateMinSpace2OD),
									_XYCoordinatesofNcap[0][1] - (_CONUMYOnOD // 2 - 0.5) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace)
									+ j * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2)])
					else:
						tmp_cont.append([_XYCoordinatesofNcap[0][0] - self._DesignParameter['_POLayer']['_XWidth'] // 2 - _DRCObj._CoMinSpace
									- 0.5 * _DRCObj._CoMinWidth + i * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace) + k * (self._DesignParameter['_POLayer']['_XWidth'] + ODExtensionOnPO // 2 + _DRCObj._PolygateMinSpace2OD),
									_XYCoordinatesofNcap[0][1] - (_CONUMYOnOD // 2) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace)
									+ j * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2)])
						tmp_cont.append([_XYCoordinatesofNcap[0][0] + self._DesignParameter['_POLayer']['_XWidth'] // 2 + _DRCObj._CoMinSpace
									+ 0.5 * _DRCObj._CoMinWidth - i * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace) + k * (self._DesignParameter['_POLayer']['_XWidth'] + ODExtensionOnPO // 2 + _DRCObj._PolygateMinSpace2OD),
									_XYCoordinatesofNcap[0][1] - (_CONUMYOnOD // 2) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace)
									+ j * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2)])

		self._DesignParameter['_COLayer']['_XYCoordinates'] = tmp_cont
		del tmp_cont


		print('#########################     METAL1 in poly Coordinates Calculation    ####################################')
		tmp_m1poly = []
		for i in range(_NumofGates):
			tmp_m1poly.append([_XYCoordinatesofNcap[0][0] + i * (self._DesignParameter['_POLayer']['_XWidth'] + ODExtensionOnPO // 2 + _DRCObj._PolygateMinSpace2OD),
							   _XYCoordinatesofNcap[0][1] - self._DesignParameter['_POLayer']['_YWidth'] // 2 + _DRCObj._CoMinEnclosureByPOAtLeastTwoSide
							   + 0.5 * _DRCObj._CoMinWidth + (_CONUMYOnPO - 1) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2) // 2])
			tmp_m1poly.append([_XYCoordinatesofNcap[0][0] + i * (self._DesignParameter['_POLayer']['_XWidth'] + ODExtensionOnPO // 2 + _DRCObj._PolygateMinSpace2OD),
							   _XYCoordinatesofNcap[0][1] + self._DesignParameter['_POLayer']['_YWidth'] // 2 - _DRCObj._CoMinEnclosureByPOAtLeastTwoSide
							   - 0.5 * _DRCObj._CoMinWidth - (_CONUMYOnPO - 1) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2) // 2])

		self._DesignParameter['_XYCoordinateM1inPO']['_XYCoordinates'] = tmp_m1poly
		del tmp_m1poly


		print('#########################     METAL1 in OD Coordinates Calculation    ####################################')
		tmp_m1od = []
		for i in range(_NumofGates):
			tmp_m1od.append([_XYCoordinatesofNcap[0][0] - self._DesignParameter['_POLayer']['_XWidth'] // 2 - _DRCObj._CoMinSpace
								- 0.5 * _DRCObj._CoMinWidth - (_CONUMXOnOD - 1) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace) // 2
								+ i * (self._DesignParameter['_POLayer']['_XWidth'] + ODExtensionOnPO // 2 + _DRCObj._PolygateMinSpace2OD),
							   _XYCoordinatesofNcap[0][1]])
			tmp_m1od.append([_XYCoordinatesofNcap[0][0] + self._DesignParameter['_POLayer']['_XWidth'] // 2 + _DRCObj._CoMinSpace
								+ 0.5 * _DRCObj._CoMinWidth - (_CONUMXOnOD - 1) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace) // 2
								+ i * (self._DesignParameter['_POLayer']['_XWidth'] + ODExtensionOnPO // 2 + _DRCObj._PolygateMinSpace2OD),
							   _XYCoordinatesofNcap[0][1]])

		self._DesignParameter['_XYCoordinateM1inOD']['_XYCoordinates'] = tmp_m1od
		del tmp_m1od


		print('#############################     METAL1 Layer Calculation    ##############################################')
		self._DesignParameter['_Met1Layer1']['_XWidth'] = (_CONUMXOnPO - 1) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace) \
		                                                 + _DRCObj._CoMinWidth + _DRCObj._Metal1MinEnclosureCO2 * 2
		self._DesignParameter['_Met1Layer1']['_YWidth'] = (_CONUMYOnPO - 1) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2) \
		                                                 + _DRCObj._CoMinWidth + _DRCObj._Metal1MinEnclosureCO * 2
		self._DesignParameter['_Met1Layer1']['_XYCoordinates'] = self._DesignParameter['_XYCoordinateM1inPO']['_XYCoordinates']

		self._DesignParameter['_Met1Layer2']['_XWidth'] = (_CONUMXOnOD - 1) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace) \
		                                                 + _DRCObj._CoMinWidth + _DRCObj._Metal1MinEnclosureCO2 * 2
		self._DesignParameter['_Met1Layer2']['_YWidth'] = (_CONUMYOnOD - 1) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2) \
		                                                 + _DRCObj._CoMinWidth + _DRCObj._Metal1MinEnclosureCO * 2
		self._DesignParameter['_Met1Layer2']['_XYCoordinates'] = self._DesignParameter['_XYCoordinateM1inOD']['_XYCoordinates']


		# LVS만 수정하면 됨
		self._DesignParameter['LVSLayer']=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['LVS_dr4'][0],
																			_Datatype=DesignParameters._LayerMapping['LVS_dr4'][1],
																			_XWidth=self._DesignParameter['_ODLayer']['_XYCoordinates'][_NumofGates-1][0] - _XYCoordinatesofNcap[0][0] + self._DesignParameter['_ODLayer']['_XWidth'] + _DRCObj._CoMinEnclosureByPOAtLeastTwoSide * 2,
																			_YWidth=self._DesignParameter['_POLayer']['_YWidth'] + _DRCObj._CoMinEnclosureByPOAtLeastTwoSide * 2)
		self._DesignParameter['LVSLayer']['_XYCoordinates'] = [[_XYCoordinatesofNcap[0][0] + (self._DesignParameter['_POLayer']['_XYCoordinates'][_NumofGates-1][0] - _XYCoordinatesofNcap[0][0]) // 2,
															   _XYCoordinatesofNcap[0][1]]]



		self._DesignParameter['NWELL']=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['NWELL'][0], _Datatype=DesignParameters._LayerMapping['NWELL'][1],
																		_XWidth=self._DesignParameter['_POLayer']['_XYCoordinates'][_NumofGates-1][0] - _XYCoordinatesofNcap[0][0] + self._DesignParameter['_POLayer']['_XWidth'] + 2*_DRCObj._PolygateMinEnclosureByNcap,
																		_YWidth=self._DesignParameter['_ODLayer']['_YWidth']+2*_DRCObj._PolygateMinEnclosureByNcap)
		self._DesignParameter['NWELL']['_XYCoordinates'] = self._DesignParameter['LVSLayer']['_XYCoordinates']



		self._DesignParameter['NCAPLayer']=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['NCAP'][0], _Datatype=DesignParameters._LayerMapping['NCAP'][1],
																			_XWidth=self._DesignParameter['NWELL']['_XWidth'], _YWidth=self._DesignParameter['NWELL']['_YWidth'])
		self._DesignParameter['NCAPLayer']['_XYCoordinates'] = self._DesignParameter['LVSLayer']['_XYCoordinates']



		if Guardring == True :
			self._DesignParameter['guardring']=self._SrefElementDeclaration(_DesignObj=PSubRing.PSubRing(_Name='PSubRingIn{}'.format(_Name)))[0]
			self._DesignParameter['guardring']['_DesignObj']._CalculateDesignParameter(**dict(height=5000, width=3000, contact_bottom=guardring_left, contact_top=guardring_top, contact_left=guardring_left, contact_right=guardring_right))

			if guardring_width == None :
				guardring_Xwidth=self._DesignParameter['NCAPLayer']['_XWidth']+self._DesignParameter['guardring']['_DesignObj']._DesignParameter['right']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth']/2+self._DesignParameter['guardring']['_DesignObj']._DesignParameter['left']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth']/2+2*_DRCObj._NwMinSpacetoRX

			elif guardring_width != None :
				guardring_Xwidth=guardring_width

			if guardring_height == None :
				guardring_Yheight=self._DesignParameter['NCAPLayer']['_YWidth']+self._DesignParameter['guardring']['_DesignObj']._DesignParameter['top']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth']/2+self._DesignParameter['guardring']['_DesignObj']._DesignParameter['bot']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth']/2+2*_DRCObj._NwMinSpacetoRX

			elif guardring_height != None :
				guardring_Yheight=guardring_height

			self._DesignParameter['guardring']['_DesignObj']._CalculateDesignParameter(**dict(height=guardring_Yheight, width=guardring_Xwidth, contact_bottom=guardring_bot, contact_top=guardring_top, contact_left=guardring_left, contact_right=guardring_right))
			self._DesignParameter['guardring']['_XYCoordinates']=self._DesignParameter['NCAPLayer']['_XYCoordinates']

			if guardring_Xwidth < self._DesignParameter['NWELL']['_XWidth']+self._DesignParameter['guardring']['_DesignObj']._DesignParameter['right']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth']/2+self._DesignParameter['guardring']['_DesignObj']._DesignParameter['left']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth']/2+2*_DRCObj._NwMinSpacetoRX :
				raise NotImplementedError
			if guardring_Yheight < self._DesignParameter['NWELL']['_YWidth']+self._DesignParameter['guardring']['_DesignObj']._DesignParameter['top']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth']/2+self._DesignParameter['guardring']['_DesignObj']._DesignParameter['bot']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth']/2+2*_DRCObj._NwMinSpacetoRX :
				raise NotImplementedError