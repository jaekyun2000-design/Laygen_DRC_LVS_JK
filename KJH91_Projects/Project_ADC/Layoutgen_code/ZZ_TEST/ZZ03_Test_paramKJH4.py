############################################################################################################################################################ BASIC Modules
from KJH91_Projects.Project_ADC.Library_and_Engine import StickDiagram_KJH1, DesignParameters
from KJH91_Projects.Project_ADC.Library_and_Engine import DRC

import copy
import math
import numpy as np
import time



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


		# Define Boundary_element ex)METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
		self._DesignParameter['M1_HDVNCAP_test'] = self._BoundaryElementDeclaration(
			_Layer=DesignParameters._LayerMapping['M1_HDVNCAP'][0],
			_Datatype=DesignParameters._LayerMapping['M1_HDVNCAP'][1],
			_XWidth=None,
			_YWidth=None,
			_XYCoordinates=[],
		)

		# Define Boundary_element _YWidth
		self._DesignParameter['M1_HDVNCAP_test']['_YWidth'] = 21

		# Define Boundary_element _XWidth
		self._DesignParameter['M1_HDVNCAP_test']['_XWidth'] = 19

		# Define Boundary_element _XYCoordinates
		self._DesignParameter['M1_HDVNCAP_test']['_XYCoordinates'] = [[0, 0],[300,500]]





		# Define Boundary_element ex)METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
		self._DesignParameter['M2_test'] = self._BoundaryElementDeclaration(
			_Layer=DesignParameters._LayerMapping['METAL2'][0],
			_Datatype=DesignParameters._LayerMapping['METAL2'][1],
			_XWidth=None,
			_YWidth=None,
			_XYCoordinates=[],
		)

		# Define Boundary_element _YWidth
		self._DesignParameter['M2_test']['_YWidth'] = 11

		# Define Boundary_element _XWidth
		self._DesignParameter['M2_test']['_XWidth'] = 7

		# Define Boundary_element _XYCoordinates
		self._DesignParameter['M2_test']['_XYCoordinates'] = [[0, 0]]


		## Get_Scoord_v4.
		## Calculate Sref XYcoord
		tmpXY = []
		## initialized Sref coordinate
		self._DesignParameter['M2_test']['_XYCoordinates'] = [[0, 0]]
		## Calculate
		## Target_coord: _XY_type1
		tmp1 = self.get_param_KJH4('M1_HDVNCAP_test')
		target_coord = tmp1[0][0]['_XY_up']
		## Approaching_coord: _XY_type2
		tmp2 = self.get_param_KJH4('M2_test')
		approaching_coord = tmp2[0][0]['_XY_down_left']
		## Sref coord
		tmp3 = self.get_param_KJH4('M2_test')
		Scoord = tmp3[0][0]['_XY_origin']
		## Cal
		New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
		tmpXY.append(New_Scoord)
		## Define Coordinates
		self._DesignParameter['M2_test']['_XYCoordinates'] = tmpXY

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
	cellname = 'HDVNCAP_Test91'
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