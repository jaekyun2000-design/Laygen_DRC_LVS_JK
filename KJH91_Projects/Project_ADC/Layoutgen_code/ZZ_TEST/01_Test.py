############################################################################################################################################################ BASIC Modules
from KJH91_Projects.Project_ADC.Library_and_Engine import StickDiagram_KJH1, DesignParameters
from KJH91_Projects.Project_ADC.Library_and_Engine import DRC

import copy
import math
import numpy as np
import time

from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A01_Boundary_Element_KJH

############################################################################################################################################################ Class_HEADER
class _BoundaryTest(StickDiagram_KJH1._StickDiagram_KJH):

    ##########################################################################################################################^^^^^^^^^^^^^^^^^^^^^
    # Define input_parameters for Design calculation
    _ParametersForDesignCalculation = dict(
		_Layermapping=None,
		_XWidth=None,
		_YWidth=None,
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

								  _Layermapping = None,
								  _XWidth = None,
								  _YWidth = None,

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



            ## ################################################################################################################### Gen nmos input Tr
            # Define Calculation_Parameters
        _Caculation_Parameters = copy.deepcopy(A01_Boundary_Element_KJH._Boundary_Element_KJH._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layermapping'] = _Layermapping
        _Caculation_Parameters['_XWidth'] 		= _XWidth
        _Caculation_Parameters['_YWidth'] 		= _YWidth

            # Generate Sref
        self._DesignParameter['_Input_p'] = self._SrefElementDeclaration(_DesignObj=A01_Boundary_Element_KJH._Boundary_Element_KJH(_DesignParameter=None, _Name='{}:_Input_p'.format(_Name)))[0]

            # Define Sref Relection
        self._DesignParameter['_Input_p']['_Reflect'] = [0, 0, 0]

            # Define Sref Angle
        self._DesignParameter['_Input_p']['_Angle'] = 0

            # Calculate Sref Layer by using Calculation_Parameter
        self._DesignParameter['_Input_p']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

            # Define Sref _XYcoordinate
        self._DesignParameter['_Input_p']['_XYCoordinates'] = [[0,0]]


############################################################################################################################################################ START MAIN
if __name__ == '__main__':

	''' Check Time'''
	start_time = time.time()

	from KJH91_Projects.Project_ADC.Library_and_Engine.Private import MyInfo
	from KJH91_Projects.Project_ADC.Library_and_Engine import DRCchecker_KJH0

	libname = 'Lib_for_test'
	cellname = 'Test3'
	_fileName = cellname + '.gds'

	''' Input Parameters for Layout Object ''' ############################################################### ^^^^^^^^^^^^^^^^^^^^^
	InputParams = dict(
		_Layermapping = 'METAL2',
		_XWidth = 19,
		_YWidth = 22,
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
	Checker.lib_deletion()
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