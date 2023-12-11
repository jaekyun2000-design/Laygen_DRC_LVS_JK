from generatorLib import StickDiagram
from generatorLib import DesignParameters
import copy
import math
import winsound
from generatorLib import DRC
from generatorLib.generator_models import Three2TwentyEight_MUX
from generatorLib.generator_models import RArray
from generatorLib.generator_models import ViaMet22Met3

class Reference_Voltage_Generator(StickDiagram._StickDiagram):
	def __init__(self, _DesignParameter=None, _Name='Reference_Voltage_Generator'):
		if _DesignParameter != None:
			self._DesignParameter = _DesignParameter
		else:
			self._DesignParameter = dict(_Name=self._NameDeclaration(_Name=_Name), _GDSFile=self._GDSObjDeclaration(_GDSFile=None))
		self._DesignParameter['_Name']['Name'] = _Name

	def _CalculateDesignParameter(self,Num_of_Vref=25,UNITR_X_WIDTH=1500,UNITR_Y_LENGTH=1000,UNITR_CONT_X_NUM=None,UNITR_CONT_Y_NUM=1,Rladder_X_NUM=10,Rladder_Y_NUM=6,First_Vref_Point=4,VREF_STEP=2,MUX_INV_nmos_width=200,MUX_INV_finger=1,MUX_VDD2PMOS=380,MUX_gate_length=30,MUX_gate_spacing=100,MUX_XVT='RVT',MUX_nmos_y=420,MUX_cell_height=2000,MUX_TG_pmos_width=600,MUX_TG_nmos_width=300,MUX_TG_poly_y=800,MUX_TG_finger=3,MUX_nandin_y=900):
	
		drc = DRC.DRC()
		_Name = self._DesignParameter['_Name']['_Name']
		
		self._DesignParameter['R_ladder'] = self._SrefElementDeclaration(_DesignObj=RArray.RArray(_Name='R_ladderIn{}'.format(_Name)))[0]
		self._DesignParameter['R_ladder']['_DesignObj']._CalculateDesignParameter(**dict(R_X_width=UNITR_X_WIDTH, R_Y_length=UNITR_Y_LENGTH, CONT_X_num=UNITR_CONT_X_NUM, CONT_Y_num=UNITR_CONT_Y_NUM, NUMofX=Rladder_X_NUM, NUMofY=Rladder_Y_NUM, R_guard_flag=1, Vref_routing_flag=1, First_vref_point=First_Vref_Point, Vref_step=VREF_STEP, Vref_num=Num_of_Vref))
		self._DesignParameter['R_ladder']['_XYCoordinates'] = [[0.0, 0.0]]
		self._DesignParameter['MUX'] = self._SrefElementDeclaration(_DesignObj=Three2TwentyEight_MUX.Three2TwentyEight_MUX(_Name='MUXIn{}'.format(_Name)))[0]
		self._DesignParameter['MUX']['_DesignObj']._CalculateDesignParameter(**dict(INV_nmos_width=MUX_INV_nmos_width, INV_finger=MUX_INV_finger, VDD2PMOS=MUX_VDD2PMOS, gate_length=MUX_gate_length, gate_spacing=MUX_gate_spacing, XVT=MUX_XVT, NMOS_y=MUX_nmos_y, Cell_height=MUX_cell_height, TG_pmos_width=MUX_TG_pmos_width, TG_nmos_width=MUX_TG_nmos_width, TG_poly_y=MUX_TG_poly_y, TG_finger=MUX_TG_finger, NANDIN_y=MUX_nandin_y, INPUT_num=Num_of_Vref))
		self._DesignParameter['MUX']['_XYCoordinates'] = [[((((self._DesignParameter['R_ladder']['_XYCoordinates'][0][0] + self._DesignParameter['R_ladder']['_DesignObj']._DesignParameter['GuardRing']['_XYCoordinates'][0][0]) + self._DesignParameter['R_ladder']['_DesignObj']._DesignParameter['GuardRing']['_DesignObj']._DesignParameter['left']['_XYCoordinates'][0][0]) + self._DesignParameter['R_ladder']['_DesignObj']._DesignParameter['GuardRing']['_DesignObj']._DesignParameter['left']['_DesignObj']._DesignParameter['_PPLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['R_ladder']['_DesignObj']._DesignParameter['GuardRing']['_DesignObj']._DesignParameter['left']['_DesignObj']._DesignParameter['_PPLayer']['_XWidth'] / 2)),
														   (((((self._DesignParameter['R_ladder']['_XYCoordinates'][0][1] + self._DesignParameter['R_ladder']['_DesignObj']._DesignParameter['GuardRing']['_XYCoordinates'][0][1]) + self._DesignParameter['R_ladder']['_DesignObj']._DesignParameter['GuardRing']['_DesignObj']._DesignParameter['bot']['_XYCoordinates'][0][1]) + self._DesignParameter['R_ladder']['_DesignObj']._DesignParameter['GuardRing']['_DesignObj']._DesignParameter['bot']['_DesignObj']._DesignParameter['_PPLayer']['_XYCoordinates'][0][1]) - (self._DesignParameter['R_ladder']['_DesignObj']._DesignParameter['GuardRing']['_DesignObj']._DesignParameter['bot']['_DesignObj']._DesignParameter['_PPLayer']['_YWidth'] / 2)) - (MUX_cell_height * 2))]]

		##MUX re-position(x position)
		if Num_of_Vref >= 7:
			for i in range (0,7) :
				tmpname1 = 'mux_module_%d' %i
				MUX_offset_tmp=2*self._DesignParameter['R_ladder']['_DesignObj']._DesignParameter['_M3_vertical']['_Width'] + 2*drc._MetalxMinSpace21 - (self._DesignParameter['R_ladder']['_XYCoordinates'][0][0] + self._DesignParameter['R_ladder']['_DesignObj']._DesignParameter['_M3_vertical']['_XYCoordinates'][i+1][0][0]) + ((((self._DesignParameter['MUX']['_XYCoordinates'][0][0]) + self._DesignParameter['MUX']['_DesignObj']._DesignParameter['EightMUX_0']['_XYCoordinates'][0][0]) + self._DesignParameter['MUX']['_DesignObj']._DesignParameter['EightMUX_0']['_DesignObj']._DesignParameter[tmpname1]['_XYCoordinates'][0][0]) + self._DesignParameter['MUX']['_DesignObj']._DesignParameter['EightMUX_0']['_DesignObj']._DesignParameter[tmpname1]['_DesignObj']._DesignParameter['m3_boundary']['_XYCoordinates'][0][0])
				if i==0 :
					MUX_offset = MUX_offset_tmp
				elif MUX_offset < MUX_offset_tmp :
					MUX_offset = MUX_offset_tmp
		else :
			for i in range (0,Num_of_Vref) :
				tmpname1 = 'mux_module_%d' %i
				MUX_offset_tmp=2*self._DesignParameter['R_ladder']['_DesignObj']._DesignParameter['_M3_vertical']['_Width'] + 2*drc._MetalxMinSpace21 -(self._DesignParameter['R_ladder']['_XYCoordinates'][0][0] + self._DesignParameter['R_ladder']['_DesignObj']._DesignParameter['_M3_vertical']['_XYCoordinates'][i+1][0][0]) + ((((self._DesignParameter['MUX']['_XYCoordinates'][0][0]) + self._DesignParameter['MUX']['_DesignObj']._DesignParameter['EightMUX_0']['_XYCoordinates'][0][0]) + self._DesignParameter['MUX']['_DesignObj']._DesignParameter['EightMUX_0']['_DesignObj']._DesignParameter[tmpname1]['_XYCoordinates'][0][0]) + self._DesignParameter['MUX']['_DesignObj']._DesignParameter['EightMUX_0']['_DesignObj']._DesignParameter[tmpname1]['_DesignObj']._DesignParameter['m3_boundary']['_XYCoordinates'][0][0])
				if i==0 :
					MUX_offset = MUX_offset_tmp
				elif MUX_offset < MUX_offset_tmp :
					MUX_offset = MUX_offset_tmp

		self._DesignParameter['MUX']['_XYCoordinates'] = [[((((self._DesignParameter['R_ladder']['_XYCoordinates'][0][0] + self._DesignParameter['R_ladder']['_DesignObj']._DesignParameter['GuardRing']['_XYCoordinates'][0][0]) + self._DesignParameter['R_ladder']['_DesignObj']._DesignParameter['GuardRing']['_DesignObj']._DesignParameter['left']['_XYCoordinates'][0][0]) + self._DesignParameter['R_ladder']['_DesignObj']._DesignParameter['GuardRing']['_DesignObj']._DesignParameter['left']['_DesignObj']._DesignParameter['_PPLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['R_ladder']['_DesignObj']._DesignParameter['GuardRing']['_DesignObj']._DesignParameter['left']['_DesignObj']._DesignParameter['_PPLayer']['_XWidth'] / 2) - MUX_offset),
														   (((((self._DesignParameter['R_ladder']['_XYCoordinates'][0][1] + self._DesignParameter['R_ladder']['_DesignObj']._DesignParameter['GuardRing']['_XYCoordinates'][0][1]) + self._DesignParameter['R_ladder']['_DesignObj']._DesignParameter['GuardRing']['_DesignObj']._DesignParameter['bot']['_XYCoordinates'][0][1]) + self._DesignParameter['R_ladder']['_DesignObj']._DesignParameter['GuardRing']['_DesignObj']._DesignParameter['bot']['_DesignObj']._DesignParameter['_PPLayer']['_XYCoordinates'][0][1]) - (self._DesignParameter['R_ladder']['_DesignObj']._DesignParameter['GuardRing']['_DesignObj']._DesignParameter['bot']['_DesignObj']._DesignParameter['_PPLayer']['_YWidth'] / 2)) - (MUX_cell_height * 2))]]
		del tmpname1
		for i in range (0,Num_of_Vref) :

			name1 = 'Vref_%d_via_1'%i
			name1_1 = 'Vref_%d_via_1in{}'%i
			name2 = 'Vref_%d_via_2'%i
			name2_1 = 'Vref_%d_via_2in{}'%i

			pathname1 = 'Vref_%d_m2_1'%i
			pathname2 = 'Vref_%d_m3_1'%i
			module_num = i%7
			muxname = 'mux_module_%d'%module_num

			Eightmux_num = i // 7
			muxname2 = 'EightMUX_%d'%Eightmux_num

			self._DesignParameter[name1] = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_Name=name1_1.format(_Name)))[0]
			self._DesignParameter[name1]['_DesignObj']._CalculateDesignParameterSameEnclosure(**dict(_ViaMet22Met3NumberOfCOX=1, _ViaMet22Met3NumberOfCOY=1))
			self._DesignParameter[name1]['_XYCoordinates'] = [[(+ (self._DesignParameter['R_ladder']['_XYCoordinates'][0][0] + self._DesignParameter['R_ladder']['_DesignObj']._DesignParameter['_M3_vertical']['_XYCoordinates'][i+1][1][0])), (+ (self._DesignParameter['R_ladder']['_XYCoordinates'][0][1] + self._DesignParameter['R_ladder']['_DesignObj']._DesignParameter['_M3_vertical']['_XYCoordinates'][i+1][1][1]))]]

			self._DesignParameter[pathname1] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _Width=self._DesignParameter[name1]['_DesignObj']._DesignParameter['_Met3Layer']['_YWidth'])
			self._DesignParameter[pathname1]['_XYCoordinates'] = [[[(+ (self._DesignParameter[name1]['_XYCoordinates'][0][0] + self._DesignParameter[name1]['_DesignObj']._DesignParameter['_Met3Layer']['_XYCoordinates'][0][0])),
																	(+ (self._DesignParameter[name1]['_XYCoordinates'][0][1] + self._DesignParameter[name1]['_DesignObj']._DesignParameter['_Met3Layer']['_XYCoordinates'][0][1]))],
																   [((self._DesignParameter['MUX']['_XYCoordinates'][0][0] + self._DesignParameter['MUX']['_DesignObj']._DesignParameter[muxname2]['_DesignObj']._DesignParameter[muxname]['_XYCoordinates'][0][0]) + self._DesignParameter['MUX']['_DesignObj']._DesignParameter[muxname2]['_DesignObj']._DesignParameter[muxname]['_DesignObj']._DesignParameter['Vref_in_m3_2']['_XYCoordinates'][0][0][0]),
																	(self._DesignParameter[name1]['_XYCoordinates'][0][1] + self._DesignParameter[name1]['_DesignObj']._DesignParameter['_Met3Layer']['_XYCoordinates'][0][1])]]]

			self._DesignParameter[name2] = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_Name=name2_1.format(_Name)))[0]
			self._DesignParameter[name2]['_DesignObj']._CalculateDesignParameterSameEnclosure(**dict(_ViaMet22Met3NumberOfCOX=1, _ViaMet22Met3NumberOfCOY=1))
			self._DesignParameter[name2]['_XYCoordinates'] = [[(+ self._DesignParameter[pathname1]['_XYCoordinates'][0][1][0]), (+ self._DesignParameter[pathname1]['_XYCoordinates'][0][1][1])]]

			self._DesignParameter[pathname2] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0], _Datatype=DesignParameters._LayerMapping['METAL3'][1], _Width=self._DesignParameter[name2]['_DesignObj']._DesignParameter['_Met3Layer']['_XWidth'])
			self._DesignParameter[pathname2]['_XYCoordinates'] = [[[(+ (self._DesignParameter[name2]['_XYCoordinates'][0][0] + self._DesignParameter[name2]['_DesignObj']._DesignParameter['_Met3Layer']['_XYCoordinates'][0][0])),
																	(+ (self._DesignParameter[name2]['_XYCoordinates'][0][1] + self._DesignParameter[name2]['_DesignObj']._DesignParameter['_Met3Layer']['_XYCoordinates'][0][1]))],
																   [(+ ((self._DesignParameter['MUX']['_XYCoordinates'][0][0] + self._DesignParameter['MUX']['_DesignObj']._DesignParameter[muxname2]['_DesignObj']._DesignParameter[muxname]['_XYCoordinates'][0][0]) + self._DesignParameter['MUX']['_DesignObj']._DesignParameter[muxname2]['_DesignObj']._DesignParameter[muxname]['_DesignObj']._DesignParameter['Vref_in_m3_2']['_XYCoordinates'][0][0][0])),
																	(+ ((self._DesignParameter['MUX']['_XYCoordinates'][0][1] + self._DesignParameter['MUX']['_DesignObj']._DesignParameter[muxname2]['_DesignObj']._DesignParameter[muxname]['_XYCoordinates'][0][1]) + self._DesignParameter['MUX']['_DesignObj']._DesignParameter[muxname2]['_DesignObj']._DesignParameter[muxname]['_DesignObj']._DesignParameter['Vref_in_m3_2']['_XYCoordinates'][0][0][1])
																	 -2*MUX_cell_height*((Eightmux_num+1)//2)+(2*MUX_cell_height-2*self._DesignParameter['MUX']['_DesignObj']._DesignParameter[muxname2]['_DesignObj']._DesignParameter[muxname]['_DesignObj']._DesignParameter['Vref_in_m3_2']['_XYCoordinates'][0][0][1])*(Eightmux_num%2))]]]

		if Num_of_Vref >= 7:
			if (self._DesignParameter['Vref_6_m2_1']['_XYCoordinates'][0][1][0]-self._DesignParameter['Vref_6_m2_1']['_XYCoordinates'][0][0][0]) >= 0 :
				raise NotImplementedError
		else :
			tmpname = 'Vref_%d_m2_1'%(Num_of_Vref-1)
			if (self._DesignParameter[tmpname]['_XYCoordinates'][0][1][0]-self._DesignParameter[tmpname]['_XYCoordinates'][0][0][0]) >= 0 :
				raise NotImplementedError
			del tmpname

if __name__ == '__main__':
    from Private import Myinfo
    import DRCchecker_test2 as DRCchecker
    from generatorLib.IksuPack import PlaygroundBot
    import time


    My = Myinfo.USER(DesignParameters._Technology)
    # Bot = PlaygroundBot.PGBot(token=My.BotToken, chat_id=My.ChatID)


    libname = 'DEMO_ReferenceVoltageGenerator'
    cellname = 'RVG'
    _fileName = cellname + '.gds'

    ''' Input Parameters for Layout Object '''

    InputParams = dict(
      Num_of_Vref=25,
      UNITR_X_WIDTH=1500,
      UNITR_Y_LENGTH=1000,
      UNITR_CONT_X_NUM=None,
      UNITR_CONT_Y_NUM=1,
      Rladder_X_NUM=10,
      Rladder_Y_NUM=6,
      First_Vref_Point=4,
      VREF_STEP=2,
      MUX_INV_nmos_width=200,
      MUX_INV_finger=1,
      MUX_VDD2PMOS=380,
      MUX_gate_length=30,
      MUX_gate_spacing=100,
      MUX_XVT='RVT',
      MUX_nmos_y=420,
      MUX_cell_height=2000,
      MUX_TG_pmos_width=600,
      MUX_TG_nmos_width=300,
      MUX_TG_poly_y=800,
      MUX_TG_finger=3,
      MUX_nandin_y=900
    )

    Mode_DRCCheck = True  # True | False
    Num_DRCCheck = 30

    Checker = DRCchecker.DRCchecker(
        username=My.ID,
        password=My.PW,
        WorkDir=My.Dir_Work,
        DRCrunDir=My.Dir_DRCrun,
        GDSDir=My.Dir_GDS,
        libname=libname,
        cellname=cellname,
    )

    if Mode_DRCCheck:
        ErrCount = 0            # DRC error
        knownErrorCount = 0     # failed to generate design. NotImplementedError

        start_time = time.time()
        for ii in range(0, Num_DRCCheck):

            forLoopCntMax = 30
            for iii in range(0, forLoopCntMax):
                try:
                    ''' ------------------------------- Random Parameters for Layout Object -------------------------------- '''
                    # # default setup
                    # InputParams['Num_of_Vref'] = DRCchecker.RandomParam(start=4, stop=16, step=2)
                    # InputParams['UNITR_X_WIDTH'] = DRCchecker.RandomParam(start=1400, stop=2000, step=100)
                    # InputParams['UNITR_Y_LENGTH'] = DRCchecker.RandomParam(start=1000, stop=1600, step=100)
                    #
                    # InputParams['Rladder_X_NUM'] = DRCchecker.RandomParam(start=16, stop=24, step=2)
                    # InputParams['Rladder_Y_NUM'] = DRCchecker.RandomParam(start=8, stop=12, step=2)
                    # InputParams['First_Vref_Point'] = DRCchecker.RandomParam(start=8, stop=20, step=1)
                    # InputParams['VREF_STEP'] = DRCchecker.RandomParam(start=3, stop=6, step=1)

                    #
                    InputParams['Num_of_Vref'] = DRCchecker.RandomParam(start=4, stop=16, step=2)
                    InputParams['UNITR_X_WIDTH'] = DRCchecker.RandomParam(start=1400, stop=2000, step=100)
                    InputParams['UNITR_Y_LENGTH'] = DRCchecker.RandomParam(start=1000, stop=1600, step=100)

                    InputParams['Rladder_X_NUM'] = DRCchecker.RandomParam(start=8, stop=24, step=2)
                    InputParams['Rladder_Y_NUM'] = DRCchecker.RandomParam(start=8, stop=12, step=2)
                    InputParams['First_Vref_Point'] = DRCchecker.RandomParam(start=8, stop=20, step=1)
                    InputParams['VREF_STEP'] = DRCchecker.RandomParam(start=3, stop=6, step=1)

                    tmpNum = DRCchecker.RandomParam(start=1, stop=4, step=1)
                    if tmpNum == 1:
                        InputParams['MUX_XVT'] = 'SLVT'
                    elif tmpNum == 2:
                        InputParams['MUX_XVT'] = 'LVT'
                    elif tmpNum == 3:
                        InputParams['MUX_XVT'] = 'RVT'
                    elif tmpNum == 4:
                        InputParams['MUX_XVT'] = 'HVT'

                    print("   Last Layout Object's Input Parameters are   ".center(105, '='))
                    tmpStr = '\n'.join(f'{k} : {v}' for k, v in InputParams.items())
                    print(tmpStr)
                    print("".center(105, '='))

                    ''' ---------------------------------- Generate Layout Object -------------------------------------------'''
                    LayoutObj = Reference_Voltage_Generator(_Name=cellname)
                    LayoutObj._CalculateDesignParameter(**InputParams)
                    LayoutObj._UpdateDesignParameter2GDSStructure(_DesignParameterInDictionary=LayoutObj._DesignParameter)
                    testStreamFile = open('./{}'.format(_fileName), 'wb')
                    tmp = LayoutObj._CreateGDSStream(LayoutObj._DesignParameter['_GDSFile']['_GDSFile'])
                    tmp.write_binary_gds_stream(testStreamFile)
                    testStreamFile.close()
                except NotImplementedError:  # something known error !
                    print(f"forLoopCnt = {iii + 1}")
                    if iii + 1 == forLoopCntMax:
                        raise NotImplementedError
                else:
                    knownErrorCount = knownErrorCount + iii
                    break
            # end of for loop

            print('   Sending to FTP Server & StreamIn...   '.center(105, '#'))
            Checker.Upload2FTP()
            Checker.StreamIn(tech=DesignParameters._Technology)
            print(f"i={ii+1}")
            winsound.Beep(1000, 500)
            time.sleep(3)

    else:
        ''' ------------------------------------ Generate Layout Object ---------------------------------------------'''
        LayoutObj = Reference_Voltage_Generator(_Name=cellname)
        LayoutObj._CalculateDesignParameter(**InputParams)
        LayoutObj._UpdateDesignParameter2GDSStructure(_DesignParameterInDictionary=LayoutObj._DesignParameter)
        testStreamFile = open('./{}'.format(_fileName), 'wb')
        tmp = LayoutObj._CreateGDSStream(LayoutObj._DesignParameter['_GDSFile']['_GDSFile'])
        tmp.write_binary_gds_stream(testStreamFile)
        testStreamFile.close()

        print('   Sending to FTP Server & StreamIn...   '.center(105, '#'))
        Checker.Upload2FTP()
        Checker.StreamIn(tech=DesignParameters._Technology)

    print('      Finished       '.center(105, '#'))
