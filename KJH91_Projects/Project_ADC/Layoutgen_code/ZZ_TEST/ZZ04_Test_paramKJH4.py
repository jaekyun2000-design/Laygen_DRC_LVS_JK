############################################################################################################################################################ BASIC Modules
from KJH91_Projects.Project_ADC.Library_and_Engine import StickDiagram_KJH1, DesignParameters
from KJH91_Projects.Project_ADC.Library_and_Engine import DRC

import copy
import time

from KJH91_Projects.Project_ADC.Layoutgen_code.ZZ_TEST import ZZ03_Test_paramKJH4


############################################################################################################################################################ Class_HEADER
class _BoundaryTest(StickDiagram_KJH1._StickDiagram_KJH):

	##########################################################################################################################^^^^^^^^^^^^^^^^^^^^^
	# Define input_parameters for Design calculation
	_ParametersForDesignCalculation = dict(

	)

	# Initially Defined design_parameter
	def __init__(self, _DesignParameter=None, _Name=None):
		if _DesignParameter != None:
			self._DesignParameter = _DesignParameter
		else:
			self._DesignParameter = dict(
				_Name=self._NameDeclaration(_Name=_Name),
				_GDSFile=self._GDSObjDeclaration(_GDSFile=None),
			)

	##########################################################################################################################^^^^^^^^^^^^^^^^^^^^^
	def _CalculateDesignParameter(self,

								  ):

		################################################################################################################################################## Class_HEADER: Pre Defined Parameter Before Calculation
		print('##     Pre Defined Parameter Before Calculation    ##')
		# Load DRC library
		_DRCobj = DRC.DRC()

		# Define _name
		_Name = self._DesignParameter['_Name']['_Name']

		############################################################################################################################################################ CALCULATION START
		print(            '#########################################################################################################')
		print(            '                                      Calculation Start                                                  ')
		print(            '#########################################################################################################')


		## SREF Generation
		## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_nmos_power_v2._NMOS_POWER._ParametersForDesignCalculation)
		_Caculation_Parameters = copy.deepcopy(ZZ03_Test_paramKJH4._BoundaryTest._ParametersForDesignCalculation)
		## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length

		## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
		self._DesignParameter['Sref_test'] = self._SrefElementDeclaration(_DesignObj=ZZ03_Test_paramKJH4._BoundaryTest(_DesignParameter=None, _Name='{}:Sref_test'.format(_Name)))[0]

		## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
		self._DesignParameter['Sref_test']['_Reflect'] = [0, 0, 0]

		## Define Sref Angle: ex)'_NMOS_POWER'
		self._DesignParameter['Sref_test']['_Angle'] = 90

		## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
		self._DesignParameter['Sref_test']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

		## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
		self._DesignParameter['Sref_test']['_XYCoordinates'] = [[21, 33]]





		# Define Boundary_element ex)METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
		self._DesignParameter['M3_test'] = self._BoundaryElementDeclaration(
			_Layer=DesignParameters._LayerMapping['METAL3'][0],
			_Datatype=DesignParameters._LayerMapping['METAL3'][1],
			_XWidth=None,
			_YWidth=None,
			_XYCoordinates=[],
		)

		# Define Boundary_element _YWidth
		self._DesignParameter['M3_test']['_YWidth'] = 27

		# Define Boundary_element _XWidth
		self._DesignParameter['M3_test']['_XWidth'] = 31

		# Define Boundary_element _XYCoordinates
		self._DesignParameter['M3_test']['_XYCoordinates'] = [[0, 0]]


		## Get_Scoord_v4.
		## Calculate Sref XYcoord
		tmpXY = []
		## initialized Sref coordinate
		self._DesignParameter['M3_test']['_XYCoordinates'] = [[0, 0]]
		## Calculate
		## Target_coord: _XY_type1
		tmp1 = self.get_param_KJH4('Sref_test','M1_HDVNCAP_test')
		target_coord = tmp1[0][1][0]['_XY_left']
		## Approaching_coord: _XY_type2
		tmp2 = self.get_param_KJH4('M3_test')
		approaching_coord = tmp2[0][0]['_XY_down_left']
		## Sref coord
		tmp3 = self.get_param_KJH4('M3_test')
		Scoord = tmp3[0][0]['_XY_origin']
		## Cal
		New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
		tmpXY.append(New_Scoord)
		## Define Coordinates
		self._DesignParameter['M3_test']['_XYCoordinates'] = tmpXY






		## Path_element Generation
		## Define Path_element ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
		self._DesignParameter['M1_path_test'] = self._PathElementDeclaration(
			_Layer=DesignParameters._LayerMapping['METAL1'][0],
			_Datatype=DesignParameters._LayerMapping['METAL1'][1],
			_XYCoordinates=[],
			_Width=None,
		)
		## Path Width
		self._DesignParameter['M1_path_test']['_Width'] = 52

		## P1--P2 coordiantes
		tmpXY = []
		## P1 calculation
		P1 = [200,100]
		## P2 calculation
		P2 = [200,151]
		## P1_P2
		P1_P2 = [P1, P2]
		tmpXY.append(P1_P2)

		## P3--P4 coordiantes
		## P3 calculation
		P3 = [200,151]
		## P4 calculation
		P4 = [402,151]
		## P1_P2
		P3_P4 = [P3, P4]
		tmpXY.append(P3_P4)

		## Define Coordinates
		self._DesignParameter['M1_path_test']['_XYCoordinates'] = tmpXY


		print(            '#########################################################################################################')
		print(            '                                      Calculation Start                                                  ')
		print(            '#########################################################################################################')

############################################################################################################################################################ START MAIN
if __name__ == '__main__':

	''' Check Time'''
	start_time = time.time()

	from KJH91_Projects.Project_ADC.Library_and_Engine.Private import MyInfo
	from KJH91_Projects.Project_ADC.Library_and_Engine import DRCchecker_KJH0

	libname = 'Lib_for_test'
	cellname = 'HDVNCAP_Test89'
	_fileName = cellname + '.gds'

	''' Input Parameters for Layout Object ''' ############################################################### ^^^^^^^^^^^^^^^^^^^^^
	InputParams = dict(


						)

	'''Mode_DRCCHECK '''
	Mode_DRCCheck = False
	Num_DRCCheck =1

	for ii in range(0, Num_DRCCheck if Mode_DRCCheck else 1):
		if Mode_DRCCheck:
			''' Input Parameters for Layout Object '''
		else:
			pass

	''' Generate Layout Object '''
	LayoutObj = _BoundaryTest(_DesignParameter=None, _Name=cellname)
	LayoutObj._CalculateDesignParameter(**InputParams)
	LayoutObj._UpdateDesignParameter2GDSStructure(_DesignParameterInDictionary=LayoutObj._DesignParameter)
	testStreamFile = open('./{}'.format(_fileName), 'wb')
	tmp = LayoutObj._CreateGDSStream(LayoutObj._DesignParameter['_GDSFile']['_GDSFile'])
	tmp.write_binary_gds_stream(testStreamFile)
	testStreamFile.close()

	print('###############      Sending to FTP Server...      ##################')
	My = MyInfo.USER(DesignParameters._Technology)
	Checker = DRCchecker_KJH0.DRCchecker_KJH0(
		username=My.ID,
		password=My.PW,
		WorkDir=My.Dir_Work,
		DRCrunDir=My.Dir_DRCrun,
		libname=libname,
		cellname=cellname,
		GDSDir=My.Dir_GDS
	)
	#Checker.lib_deletion()
	#Checker.cell_deletion()
	Checker.Upload2FTP()
	Checker.StreamIn(tech=DesignParameters._Technology)
	#Checker_KJH0.DRCchecker()

	''' Check Time'''
	elapsed_time = time.time() - start_time
	m, s = divmod(elapsed_time,60)
	h, m = divmod(m, 60)


	print ('#############################      Finished      ################################')
	# end of 'main():' ---------------------------------------------------------------------------------------------