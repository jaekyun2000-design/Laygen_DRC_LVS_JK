from generatorLib import StickDiagram
from generatorLib import DesignParameters
import copy
import math
from generatorLib import DRC
from generatorLib.generator_models import UNITR_wt_PIN
from generatorLib.generator_models import PSubRing

class RArray(StickDiagram._StickDiagram):
	def __init__(self, _DesignParameter=None, _Name='RArray'):
		if _DesignParameter != None:
			self._DesignParameter = _DesignParameter
		else:
			self._DesignParameter = dict(_Name=self._NameDeclaration(_Name=_Name), _GDSFile=self._GDSObjDeclaration(_GDSFile=None))
		self._DesignParameter['_Name']['Name'] = _Name

	def _CalculateDesignParameter(self,R_X_width=1500,CONT_X_num=None,CONT_Y_num=1,R_Y_length=1000,NUMofX=4,NUMofY=3,R_guard_flag=1):
	
		drc = DRC.DRC()
		_Name = self._DesignParameter['_Name']['_Name']

		##R array
		self._DesignParameter['Rref'] = self._SrefElementDeclaration(_DesignObj=UNITR_wt_PIN.UNITR_wt_PIN(_Name='RrefIn{}'.format(_Name)))[0]
		self._DesignParameter['Rref']['_DesignObj']._CalculateDesignParameter(**dict(R_X_WIDTH=R_X_width, CONT_X_NUM=CONT_X_num, CONT_Y_NUM=CONT_Y_num, R_Y_LENGTH=R_Y_length))

		_XYCoordinateofR = [[0,0]]

		if CONT_Y_num > 1:
			R_Y_SPACING = self._DesignParameter['Rref']['_DesignObj']._DesignParameter['upperpin']['_YWidth']
		else :
			R_Y_SPACING = drc._Metal1MinWidth * 3


		RYdistance = self._DesignParameter['Rref']['_DesignObj']._DesignParameter['upperpin']['_XYCoordinates'][0][1] - self._DesignParameter['Rref']['_DesignObj']._DesignParameter['lowerpin']['_XYCoordinates'][0][1]\
					 + R_Y_SPACING \
					 + self._DesignParameter['Rref']['_DesignObj']._DesignParameter['UNITR']['_DesignObj']._DesignParameter['OP_boundary_0']['_XWidth'] + drc._OPMinspace - self._DesignParameter['Rref']['_DesignObj']._DesignParameter['UNITR']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] \
					# drc._Metal1MinWidth * 3 ## when CONT_Y_NUM==1
					# self._DesignParameter['Rref']['_DesignObj']._DesignParameter['upperpin']['_YWidth'] \
					# (drc._PolyoverOPlayer - drc._CoMinSpace2OP - drc._CoMinWidth - drc._CoMinEnclosureByPO2) * 2 + drc._PolygateMinSpace2
		RXdistance = self._DesignParameter['Rref']['_DesignObj']._DesignParameter['UNITR']['_DesignObj']._DesignParameter['OP_boundary_0']['_XWidth'] + drc._OPMinspace

		tmp = []
		for i in range(0, NUMofX) :
			for j in range(0, NUMofY) :
				tmp.append([_XYCoordinateofR[0][0] - i * RXdistance,
							_XYCoordinateofR[0][1] - j * RYdistance])

		self._DesignParameter['Rref']['_XYCoordinates'] = tmp

		del tmp
		## PRES & PIMP big layer
		self._DesignParameter['PRES_boundary_0'] = self._BoundaryElementDeclaration(
			_Layer=DesignParameters._LayerMapping['PRES'][0], _Datatype=DesignParameters._LayerMapping['PRES'][1],
			_XWidth=self._DesignParameter['Rref']['_XYCoordinates'][0][0] - self._DesignParameter['Rref']['_XYCoordinates'][-1][0] \
					+ self._DesignParameter['Rref']['_DesignObj']._DesignParameter['UNITR']['_DesignObj']._DesignParameter['PRES_boundary_0']['_XWidth'],
			_YWidth=self._DesignParameter['Rref']['_XYCoordinates'][0][1] - self._DesignParameter['Rref']['_XYCoordinates'][-1][1] \
					+ self._DesignParameter['Rref']['_DesignObj']._DesignParameter['UNITR']['_DesignObj']._DesignParameter['PRES_boundary_0']['_YWidth'])
		self._DesignParameter['PRES_boundary_0']['_XYCoordinates'] = \
			[[(self._DesignParameter['Rref']['_XYCoordinates'][0][0] + self._DesignParameter['Rref']['_XYCoordinates'][-1][0])/2,
			  (self._DesignParameter['Rref']['_XYCoordinates'][0][1] + self._DesignParameter['Rref']['_XYCoordinates'][-1][1])/2]]

		self._DesignParameter['PIMP_boundary_0'] = self._BoundaryElementDeclaration(
			_Layer=DesignParameters._LayerMapping['PIMP'][0], _Datatype=DesignParameters._LayerMapping['PIMP'][1],
			_XWidth=self._DesignParameter['Rref']['_XYCoordinates'][0][0] - self._DesignParameter['Rref']['_XYCoordinates'][-1][0] \
					+ self._DesignParameter['Rref']['_DesignObj']._DesignParameter['UNITR']['_DesignObj']._DesignParameter['PRES_boundary_0']['_XWidth'],
			_YWidth=self._DesignParameter['Rref']['_XYCoordinates'][0][1] - self._DesignParameter['Rref']['_XYCoordinates'][-1][1] \
					+ self._DesignParameter['Rref']['_DesignObj']._DesignParameter['UNITR']['_DesignObj']._DesignParameter['PRES_boundary_0']['_YWidth'])
		self._DesignParameter['PIMP_boundary_0']['_XYCoordinates'] = \
			[[(self._DesignParameter['Rref']['_XYCoordinates'][0][0] + self._DesignParameter['Rref']['_XYCoordinates'][-1][0])/2,
			  (self._DesignParameter['Rref']['_XYCoordinates'][0][1] + self._DesignParameter['Rref']['_XYCoordinates'][-1][1])/2]]


		##M1 routing (horizontal)
		self._DesignParameter['M1horizontal1'] = self._BoundaryElementDeclaration(
			_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1],
			_XWidth=self._DesignParameter['Rref']['_DesignObj']._DesignParameter['UNITR']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] + RXdistance,
			_YWidth=drc._Metal1MinWidth * 3)  ## arbitrary

		self._DesignParameter['M1horizontal2'] = self._BoundaryElementDeclaration(
			_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1],
			_XWidth=self._DesignParameter['Rref']['_DesignObj']._DesignParameter['UNITR']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] + RXdistance,
			_YWidth=drc._Metal1MinWidth * 3)  ## arbitrary

		if CONT_Y_num > 1 :
			self._DesignParameter['M1horizontal1']['_YWidth'] = self._DesignParameter['Rref']['_DesignObj']._DesignParameter['UNITR']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']
			self._DesignParameter['M1horizontal2']['_YWidth'] = self._DesignParameter['Rref']['_DesignObj']._DesignParameter['UNITR']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']

		tmp1 = []
		tmp2 = []
		NUMofline1 = int((NUMofX-1)/2)
		NUMofline2 = int(NUMofX/2)

		for i in range(0, NUMofline1) :
			tmp1.append([(self._DesignParameter['Rref']['_XYCoordinates'][0][0] + self._DesignParameter['Rref']['_XYCoordinates'][NUMofY][0])/2 - (2*i+1) * RXdistance,
						self._DesignParameter['Rref']['_XYCoordinates'][0][1] + (self._DesignParameter['Rref']['_DesignObj']._DesignParameter['upperpin']['_XYCoordinates'][0][1]
																				 - self._DesignParameter['Rref']['_DesignObj']._DesignParameter['lowerpin']['_XYCoordinates'][0][1])/2])
		for i in range(0,NUMofline2) :
			tmp2.append([(self._DesignParameter['Rref']['_XYCoordinates'][0][0] + self._DesignParameter['Rref']['_XYCoordinates'][NUMofY][0])/2 - (2*i) * RXdistance,
						 self._DesignParameter['Rref']['_XYCoordinates'][NUMofY-1][1] - (self._DesignParameter['Rref']['_DesignObj']._DesignParameter['upperpin']['_XYCoordinates'][0][1]
																				 - self._DesignParameter['Rref']['_DesignObj']._DesignParameter['lowerpin']['_XYCoordinates'][0][1]) / 2])
		self._DesignParameter['M1horizontal1']['_XYCoordinates'] = tmp1
		self._DesignParameter['M1horizontal2']['_XYCoordinates'] = tmp2
		del tmp1
		del tmp2

		## M1 routing (vertical)
		self._DesignParameter['M1vertical'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1],
																			   _XWidth=self._DesignParameter['M1horizontal1']['_YWidth'], ## arbitrary
																			   _YWidth=RYdistance - (self._DesignParameter['Rref']['_DesignObj']._DesignParameter['upperpin']['_XYCoordinates'][0][1] - self._DesignParameter['Rref']['_DesignObj']._DesignParameter['lowerpin']['_XYCoordinates'][0][1]))
		self._DesignParameter['M1vertical2'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1],
																			   _XWidth=self._DesignParameter['Rref']['_DesignObj']._DesignParameter['UNITR']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'],
																			   _YWidth=self._DesignParameter['M1horizontal1']['_YWidth']) ## arbitrary

		_XYCoordinateofM1 = [[(self._DesignParameter['Rref']['_XYCoordinates'][0][0] + self._DesignParameter['Rref']['_XYCoordinates'][1][0])/2,
			  (self._DesignParameter['Rref']['_XYCoordinates'][0][1] + self._DesignParameter['Rref']['_XYCoordinates'][1][1])/2]]

		tmp = []
		tmp2 = []
		for i in range(0, NUMofX) :
			for j in range(0, NUMofY-1) :
				tmp.append([_XYCoordinateofM1[0][0] - i * RXdistance,
							_XYCoordinateofM1[0][1] - j * RYdistance])
				tmp2.append([_XYCoordinateofM1[0][0] - i * RXdistance,
							_XYCoordinateofM1[0][1] - j * RYdistance +
							(RYdistance - (self._DesignParameter['Rref']['_DesignObj']._DesignParameter['upperpin']['_XYCoordinates'][0][1] - self._DesignParameter['Rref']['_DesignObj']._DesignParameter['lowerpin']['_XYCoordinates'][0][1]))/2])
				tmp2.append([_XYCoordinateofM1[0][0] - i * RXdistance,
							_XYCoordinateofM1[0][1] - j * RYdistance -
							(RYdistance - (self._DesignParameter['Rref']['_DesignObj']._DesignParameter['upperpin']['_XYCoordinates'][0][1] - self._DesignParameter['Rref']['_DesignObj']._DesignParameter['lowerpin']['_XYCoordinates'][0][1]))/2])

		self._DesignParameter['M1vertical']['_XYCoordinates'] = tmp
		self._DesignParameter['M1vertical2']['_XYCoordinates'] = tmp2
		del tmp
		del tmp2

		##Resistor_guard
		if R_guard_flag == 1 :
			tmp = []
			self._DesignParameter['R_guard'] = self._SrefElementDeclaration(_DesignObj=UNITR_wt_PIN.UNITR_wt_PIN(_Name='R_guardIn{}'.format(_Name)))[0]
			self._DesignParameter['R_guard']['_DesignObj']._CalculateDesignParameter(**dict(R_X_WIDTH=R_X_width, CONT_X_NUM=CONT_X_num, CONT_Y_NUM=CONT_Y_num, R_Y_LENGTH=R_Y_length))
			for i in range(0, NUMofX+2) :
				for j in range(0, NUMofY+2) :
					if i == 0 or i == (NUMofX+1) or j == 0 or j == (NUMofY+1) :
						tmp.append([_XYCoordinateofR[0][0] + RXdistance - i * RXdistance,
									_XYCoordinateofR[0][1] + RYdistance - j * RYdistance])
			self._DesignParameter['R_guard']['_XYCoordinates'] = tmp

			## Metal1 guard routing (vertical)
			self._DesignParameter['M1_guard'] = self._BoundaryElementDeclaration(
				_Layer=DesignParameters._LayerMapping['METAL1'][0],
				_Datatype=DesignParameters._LayerMapping['METAL1'][1],
				_XWidth=self._DesignParameter['M1horizontal1']['_YWidth'],  ## arbitrary
				_YWidth=self._DesignParameter['R_guard']['_XYCoordinates'][0][1] -
						self._DesignParameter['R_guard']['_XYCoordinates'][NUMofY+1][1] +
						(self._DesignParameter['Rref']['_DesignObj']._DesignParameter['upperpin']['_XYCoordinates'][0][1] -
						self._DesignParameter['Rref']['_DesignObj']._DesignParameter['lowerpin']['_XYCoordinates'][0][1]))
			self._DesignParameter['M1_guard']['_XYCoordinates'] = [[self._DesignParameter['R_guard']['_XYCoordinates'][0][0],
				(self._DesignParameter['R_guard']['_XYCoordinates'][0][1] + self._DesignParameter['R_guard']['_XYCoordinates'][NUMofY+1][1])/2],
																   [self._DesignParameter['R_guard']['_XYCoordinates'][-1][0],
				(self._DesignParameter['R_guard']['_XYCoordinates'][-1][1] + self._DesignParameter['R_guard']['_XYCoordinates'][-NUMofY-2][1])/2]]

			## Metal1 guard routing (horizontal)
			self._DesignParameter['M1_guard_horizontal'] = self._BoundaryElementDeclaration(
				_Layer=DesignParameters._LayerMapping['METAL1'][0],
				_Datatype=DesignParameters._LayerMapping['METAL1'][1],
				_XWidth=self._DesignParameter['R_guard']['_XYCoordinates'][0][0] - self._DesignParameter['R_guard']['_XYCoordinates'][-NUMofY-2][0] + self._DesignParameter['Rref']['_DesignObj']._DesignParameter['UNITR']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'],
				_YWidth=self._DesignParameter['M1horizontal1']['_YWidth'])
			self._DesignParameter['M1_guard_horizontal']['_XYCoordinates'] = [[(self._DesignParameter['R_guard']['_XYCoordinates'][0][0] + self._DesignParameter['R_guard']['_XYCoordinates'][-NUMofY-2][0])/2,
																				self._DesignParameter['R_guard']['_XYCoordinates'][0][1]
																				+ (self._DesignParameter['Rref']['_DesignObj']._DesignParameter['upperpin']['_XYCoordinates'][0][1] - self._DesignParameter['Rref']['_DesignObj']._DesignParameter['lowerpin']['_XYCoordinates'][0][1]) / 2],
																			[(self._DesignParameter['R_guard']['_XYCoordinates'][0][0] + self._DesignParameter['R_guard']['_XYCoordinates'][-NUMofY-2][0])/2,
																				self._DesignParameter['R_guard']['_XYCoordinates'][0][1]
																				- (self._DesignParameter['Rref']['_DesignObj']._DesignParameter['upperpin']['_XYCoordinates'][0][1] - self._DesignParameter['Rref']['_DesignObj']._DesignParameter['lowerpin']['_XYCoordinates'][0][1]) / 2],
																			[(self._DesignParameter['R_guard']['_XYCoordinates'][0][0] + self._DesignParameter['R_guard']['_XYCoordinates'][-NUMofY - 2][0]) / 2,
																				 self._DesignParameter['R_guard']['_XYCoordinates'][-1][1]
																				 + (self._DesignParameter['Rref']['_DesignObj']._DesignParameter['upperpin']['_XYCoordinates'][0][1] - self._DesignParameter['Rref']['_DesignObj']._DesignParameter['lowerpin']['_XYCoordinates'][0][1]) / 2],
																			[(self._DesignParameter['R_guard']['_XYCoordinates'][0][0] + self._DesignParameter['R_guard']['_XYCoordinates'][-NUMofY - 2][0]) / 2,
																	 			self._DesignParameter['R_guard']['_XYCoordinates'][-1][1]
																				 - (self._DesignParameter['Rref']['_DesignObj']._DesignParameter['upperpin']['_XYCoordinates'][0][1] - self._DesignParameter['Rref']['_DesignObj']._DesignParameter['lowerpin']['_XYCoordinates'][0][1]) / 2],
																			]

			##Big PRES layer
			self._DesignParameter['PRES_boundary_1'] = self._BoundaryElementDeclaration(
				_Layer=DesignParameters._LayerMapping['PRES'][0], _Datatype=DesignParameters._LayerMapping['PRES'][1],
				_XWidth=self._DesignParameter['R_guard']['_XYCoordinates'][0][0] -
						self._DesignParameter['R_guard']['_XYCoordinates'][-1][0] \
						+ self._DesignParameter['R_guard']['_DesignObj']._DesignParameter['UNITR'][
							'_DesignObj']._DesignParameter['PRES_boundary_0']['_XWidth'],
				_YWidth=self._DesignParameter['R_guard']['_XYCoordinates'][0][1] -
						self._DesignParameter['R_guard']['_XYCoordinates'][-1][1] \
						+ self._DesignParameter['R_guard']['_DesignObj']._DesignParameter['UNITR'][
							'_DesignObj']._DesignParameter['PRES_boundary_0']['_YWidth'])
			self._DesignParameter['PRES_boundary_1']['_XYCoordinates'] = \
				[[(self._DesignParameter['R_guard']['_XYCoordinates'][0][0] +
				   self._DesignParameter['R_guard']['_XYCoordinates'][-1][0]) / 2,
				  (self._DesignParameter['R_guard']['_XYCoordinates'][0][1] +
				   self._DesignParameter['R_guard']['_XYCoordinates'][-1][1]) / 2]]
			##Big PIMP layer
			self._DesignParameter['PIMP_boundary_1'] = self._BoundaryElementDeclaration(
				_Layer=DesignParameters._LayerMapping['PIMP'][0], _Datatype=DesignParameters._LayerMapping['PIMP'][1],
				_XWidth=self._DesignParameter['R_guard']['_XYCoordinates'][0][0] -
						self._DesignParameter['R_guard']['_XYCoordinates'][-1][0] \
						+ self._DesignParameter['R_guard']['_DesignObj']._DesignParameter['UNITR'][
							'_DesignObj']._DesignParameter['PRES_boundary_0']['_XWidth'],
				_YWidth=self._DesignParameter['R_guard']['_XYCoordinates'][0][1] -
						self._DesignParameter['R_guard']['_XYCoordinates'][-1][1] \
						+ self._DesignParameter['R_guard']['_DesignObj']._DesignParameter['UNITR'][
							'_DesignObj']._DesignParameter['PRES_boundary_0']['_YWidth'])
			self._DesignParameter['PIMP_boundary_1']['_XYCoordinates'] = \
				[[(self._DesignParameter['R_guard']['_XYCoordinates'][0][0] +
				   self._DesignParameter['R_guard']['_XYCoordinates'][-1][0]) / 2,
				  (self._DesignParameter['R_guard']['_XYCoordinates'][0][1] +
				   self._DesignParameter['R_guard']['_XYCoordinates'][-1][1]) / 2]]
			del tmp

		## Guard_ring
		if R_guard_flag == 1 :
			Ring_contact = 3
			self._DesignParameter['GuardRing'] = self._SrefElementDeclaration(_DesignObj=PSubRing.PSubRing(_Name='GuardRingIn{}'.format(_Name)))[0]
			self._DesignParameter['GuardRing']['_DesignObj']._CalculateDesignParameter(**dict(height=self._DesignParameter['PIMP_boundary_1']['_YWidth'] + drc._PpMinSpace * 2 * 2
																									 + (drc._CoMinWidth+drc._CoMinSpace2) * (Ring_contact-1) + drc._CoMinWidth + drc._Metal1MinEnclosureCO2 * 2 + drc._PpMinExtensiononPactive2 * 2,
																							  width=self._DesignParameter['PIMP_boundary_1']['_XWidth'] + drc._PpMinSpace * 2 * 2
																							  		 + (drc._CoMinWidth+drc._CoMinSpace2) * (Ring_contact-1) + drc._CoMinWidth + drc._Metal1MinEnclosureCO2 * 2 + drc._PpMinExtensiononPactive2 * 2,
																							  contact=Ring_contact))
			self._DesignParameter['GuardRing']['_XYCoordinates'] = [self._DesignParameter['PIMP_boundary_1']['_XYCoordinates'][0]]

			self._DesignParameter['M1_guard_horizontal']['_XWidth'] = self._DesignParameter['PIMP_boundary_1']['_XWidth'] + drc._PpMinSpace * 2 * 2 \
																	+ (drc._CoMinWidth + drc._CoMinSpace2) * (Ring_contact-1) + drc._CoMinWidth + drc._Metal1MinEnclosureCO2 * 2 + drc._PpMinExtensiononPactive2 * 2

			self._DesignParameter['M1_guard']['_YWidth'] = self._DesignParameter['PIMP_boundary_1']['_YWidth'] + drc._PpMinSpace * 2 * 2 \
																	+ (drc._CoMinWidth + drc._CoMinSpace2) * (Ring_contact - 1) + drc._CoMinWidth + drc._Metal1MinEnclosureCO2 * 2 + drc._PpMinExtensiononPactive2 * 2

			##M1 vertical routing(Rguard2Ring)
			self._DesignParameter['M1_Res2Ring'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0],
																				_Datatype=DesignParameters._LayerMapping['METAL1'][1],
																				_Width=self._DesignParameter['M1horizontal1']['_YWidth'])
			tmp3 = [[]]
			for i in range(0, NUMofX) :
				tmp3.append([[self._DesignParameter['Rref']['_XYCoordinates'][0][0] - i * RXdistance,
							self._DesignParameter['Rref']['_XYCoordinates'][0][1] + RYdistance - (self._DesignParameter['Rref']['_DesignObj']._DesignParameter['upperpin']['_XYCoordinates'][0][1] - self._DesignParameter['Rref']['_DesignObj']._DesignParameter['lowerpin']['_XYCoordinates'][0][1]) / 2],
						   [self._DesignParameter['Rref']['_XYCoordinates'][0][0] - i * RXdistance,
							self._DesignParameter['Rref']['_XYCoordinates'][0][1] + RYdistance + self._DesignParameter['Rref']['_DesignObj']._DesignParameter['UNITR']['_DesignObj']._DesignParameter['PIMP_boundary_0']['_YWidth']/2 + drc._PpMinSpace * 2 + ((drc._CoMinWidth + drc._CoMinSpace2) * (Ring_contact - 1) + drc._CoMinWidth) / 2 + drc._Metal1MinEnclosureCO2 + drc._PpMinExtensiononPactive2]])
				tmp3.append([[self._DesignParameter['Rref']['_XYCoordinates'][0][0] - i * RXdistance,
							self._DesignParameter['Rref']['_XYCoordinates'][-1][1] - RYdistance + (self._DesignParameter['Rref']['_DesignObj']._DesignParameter['upperpin']['_XYCoordinates'][0][1] - self._DesignParameter['Rref']['_DesignObj']._DesignParameter['lowerpin']['_XYCoordinates'][0][1]) / 2],
						   [self._DesignParameter['Rref']['_XYCoordinates'][0][0] - i * RXdistance,
							self._DesignParameter['Rref']['_XYCoordinates'][-1][1] - RYdistance - (self._DesignParameter['Rref']['_DesignObj']._DesignParameter['UNITR']['_DesignObj']._DesignParameter['PIMP_boundary_0']['_YWidth']/2 + drc._PpMinSpace * 2 + ((drc._CoMinWidth + drc._CoMinSpace2) * (Ring_contact - 1) + drc._CoMinWidth) / 2 + drc._Metal1MinEnclosureCO2 + drc._PpMinExtensiononPactive2)]])

			self._DesignParameter['M1_Res2Ring']['_XYCoordinates'] = tmp3
			del tmp3

			## M1 horizontal routing(Rguard2Ring)

			self._DesignParameter['M1_Res2Ring_hor'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0],
																				_Datatype=DesignParameters._LayerMapping['METAL1'][1],
																				_Width=self._DesignParameter['M1horizontal1']['_YWidth'])
			tmp4 = [[]]

				##UNITR2Rguard
			tmp4.append([[self._DesignParameter['Rref']['_XYCoordinates'][0][0] - self._DesignParameter['Rref']['_DesignObj']._DesignParameter['upperpin']['_XWidth'] / 2,
						  self._DesignParameter['Rref']['_XYCoordinates'][0][1] + (self._DesignParameter['Rref']['_DesignObj']._DesignParameter['upperpin']['_XYCoordinates'][0][1] - self._DesignParameter['Rref']['_DesignObj']._DesignParameter['lowerpin']['_XYCoordinates'][0][1]) / 2],
						 [self._DesignParameter['Rref']['_XYCoordinates'][0][0] + RXdistance,
						  self._DesignParameter['Rref']['_XYCoordinates'][0][1] + (self._DesignParameter['Rref']['_DesignObj']._DesignParameter['upperpin']['_XYCoordinates'][0][1] - self._DesignParameter['Rref']['_DesignObj']._DesignParameter['lowerpin']['_XYCoordinates'][0][1]) / 2]])

			for j in range(0, NUMofY) :
				tmp4.append([[self._DesignParameter['Rref']['_XYCoordinates'][0][0] + RXdistance - self._DesignParameter['Rref']['_DesignObj']._DesignParameter['upperpin']['_XWidth']/2,
							self._DesignParameter['Rref']['_XYCoordinates'][0][1] - j * RYdistance + (self._DesignParameter['Rref']['_DesignObj']._DesignParameter['upperpin']['_XYCoordinates'][0][1] - self._DesignParameter['Rref']['_DesignObj']._DesignParameter['lowerpin']['_XYCoordinates'][0][1]) / 2],
						   [self._DesignParameter['Rref']['_XYCoordinates'][0][0] + RXdistance + self._DesignParameter['Rref']['_DesignObj']._DesignParameter['UNITR']['_DesignObj']._DesignParameter['PIMP_boundary_0']['_XWidth']/2 + drc._PpMinSpace * 2 + ((drc._CoMinWidth + drc._CoMinSpace2) * (Ring_contact - 1) + drc._CoMinWidth) / 2 + drc._Metal1MinEnclosureCO2 + drc._PpMinExtensiononPactive2,
							self._DesignParameter['Rref']['_XYCoordinates'][0][1] - j * RYdistance + (self._DesignParameter['Rref']['_DesignObj']._DesignParameter['upperpin']['_XYCoordinates'][0][1] - self._DesignParameter['Rref']['_DesignObj']._DesignParameter['lowerpin']['_XYCoordinates'][0][1]) / 2]])
				tmp4.append([[self._DesignParameter['Rref']['_XYCoordinates'][0][0] + RXdistance - self._DesignParameter['Rref']['_DesignObj']._DesignParameter['upperpin']['_XWidth']/2,
							self._DesignParameter['Rref']['_XYCoordinates'][0][1] - j * RYdistance - (self._DesignParameter['Rref']['_DesignObj']._DesignParameter['upperpin']['_XYCoordinates'][0][1] - self._DesignParameter['Rref']['_DesignObj']._DesignParameter['lowerpin']['_XYCoordinates'][0][1]) / 2],
						   [self._DesignParameter['Rref']['_XYCoordinates'][0][0] + RXdistance + self._DesignParameter['Rref']['_DesignObj']._DesignParameter['UNITR']['_DesignObj']._DesignParameter['PIMP_boundary_0']['_XWidth']/2 + drc._PpMinSpace * 2 + ((drc._CoMinWidth + drc._CoMinSpace2) * (Ring_contact - 1) + drc._CoMinWidth) / 2 + drc._Metal1MinEnclosureCO2 + drc._PpMinExtensiononPactive2,
							self._DesignParameter['Rref']['_XYCoordinates'][0][1] - j * RYdistance - (self._DesignParameter['Rref']['_DesignObj']._DesignParameter['upperpin']['_XYCoordinates'][0][1] - self._DesignParameter['Rref']['_DesignObj']._DesignParameter['lowerpin']['_XYCoordinates'][0][1]) / 2]])
				tmp4.append([[self._DesignParameter['Rref']['_XYCoordinates'][-1][0] - RXdistance + self._DesignParameter['Rref']['_DesignObj']._DesignParameter['upperpin']['_XWidth']/2,
							self._DesignParameter['Rref']['_XYCoordinates'][0][1] - j * RYdistance + (self._DesignParameter['Rref']['_DesignObj']._DesignParameter['upperpin']['_XYCoordinates'][0][1] - self._DesignParameter['Rref']['_DesignObj']._DesignParameter['lowerpin']['_XYCoordinates'][0][1]) / 2],
						   [self._DesignParameter['Rref']['_XYCoordinates'][-1][0] - RXdistance - (self._DesignParameter['Rref']['_DesignObj']._DesignParameter['UNITR']['_DesignObj']._DesignParameter['PIMP_boundary_0']['_XWidth']/2 + drc._PpMinSpace * 2 + ((drc._CoMinWidth + drc._CoMinSpace2) * (Ring_contact - 1) + drc._CoMinWidth) / 2 + drc._Metal1MinEnclosureCO2 + drc._PpMinExtensiononPactive2),
							self._DesignParameter['Rref']['_XYCoordinates'][0][1] - j * RYdistance + (self._DesignParameter['Rref']['_DesignObj']._DesignParameter['upperpin']['_XYCoordinates'][0][1] - self._DesignParameter['Rref']['_DesignObj']._DesignParameter['lowerpin']['_XYCoordinates'][0][1]) / 2]])
				tmp4.append([[self._DesignParameter['Rref']['_XYCoordinates'][-1][0] - RXdistance + self._DesignParameter['Rref']['_DesignObj']._DesignParameter['upperpin']['_XWidth']/2,
							self._DesignParameter['Rref']['_XYCoordinates'][0][1] - j * RYdistance - (self._DesignParameter['Rref']['_DesignObj']._DesignParameter['upperpin']['_XYCoordinates'][0][1] - self._DesignParameter['Rref']['_DesignObj']._DesignParameter['lowerpin']['_XYCoordinates'][0][1]) / 2],
						   [self._DesignParameter['Rref']['_XYCoordinates'][-1][0] - RXdistance - (self._DesignParameter['Rref']['_DesignObj']._DesignParameter['UNITR']['_DesignObj']._DesignParameter['PIMP_boundary_0']['_XWidth']/2 + drc._PpMinSpace * 2 + ((drc._CoMinWidth + drc._CoMinSpace2) * (Ring_contact - 1) + drc._CoMinWidth) / 2 + drc._Metal1MinEnclosureCO2 + drc._PpMinExtensiononPactive2),
							self._DesignParameter['Rref']['_XYCoordinates'][0][1] - j * RYdistance - (self._DesignParameter['Rref']['_DesignObj']._DesignParameter['upperpin']['_XYCoordinates'][0][1] - self._DesignParameter['Rref']['_DesignObj']._DesignParameter['lowerpin']['_XYCoordinates'][0][1]) / 2]])

			self._DesignParameter['M1_Res2Ring_hor']['_XYCoordinates'] = tmp4
			del tmp4
