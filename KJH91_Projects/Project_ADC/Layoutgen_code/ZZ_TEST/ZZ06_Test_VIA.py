############################################################################################################################################################ BASIC Modules
from KJH91_Projects.Project_ADC.Library_and_Engine import StickDiagram_KJH1, DesignParameters
from KJH91_Projects.Project_ADC.Library_and_Engine import DRC

import copy
import math
import numpy as np
import time

from KJH91_Projects.Project_ADC.Layoutgen_code.ZZ_TEST import ZZ04_Test_paramKJH4

from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A02_ViaStack_KJH3


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




		## Sref generation: ViaX
		## Define ViaX Parameter
		_Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH3._ViaStack._ParametersForDesignCalculation)
		_Caculation_Parameters['_Layer1'] = 1
		_Caculation_Parameters['_Layer2'] = 7
		_Caculation_Parameters['_COX'] = 100
		_Caculation_Parameters['_COY'] = 100

		## Sref ViaX declaration
		self._DesignParameter['Via_test'] = self._SrefElementDeclaration(_DesignObj=A02_ViaStack_KJH3._ViaStack(_DesignParameter=None, _Name='{}:Via_test'.format(_Name)))[0]

		## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin
		self._DesignParameter['Via_test']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)
		# self._DesignParameter['Via_test']['_DesignObj']._CalculateDesignParameterXmin(**_Caculation_Parameters)
		# self._DesignParameter['Via_test']['_DesignObj']._CalculateDesignParameterYmin(**_Caculation_Parameters)

		## Calculate Sref XYcoord
		tmpXY = []
		## initialized Sref coordinate
		self._DesignParameter['Via_test']['_XYCoordinates'] = [[0, 0]]






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
	cellname = 'VIA_Test56'
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