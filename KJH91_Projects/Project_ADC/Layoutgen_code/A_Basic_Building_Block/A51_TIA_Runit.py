from KJH91_Projects.Project_ADC.Library_and_Engine import StickDiagram_KJH1, DesignParameters
from KJH91_Projects.Project_ADC.Library_and_Engine import DRC_EGFET

import numpy as np
import copy
import math

from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A50_TIA_TG
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A50_opppcres_b

from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A02_ViaStack_KJH2_YCH

class _TIA_Runit_YCH(StickDiagram_KJH1._StickDiagram_KJH):

    ## Define input_parameters for Design calculation
    _ParametersForDesignCalculation = dict(

        #NMOS inverter
        _inv_NMOSNumberofGate	= None,
        _inv_NMOSChannelWidth	= None,
        _inv_NMOSChannellength	= None,
        _inv_NMOSGateSpacing		= None,
        _inv_NMOSSDWidth			= None,
        _inv_NMOSXVT				= None,
        _inv_NMOSPCCrit				= None,

        #Source_node_ViaM1M2
        _inv_NMOSSource_Via_TF = None,

        #Drain_node_ViaM1M2
        _inv_NMOSDrain_Via_TF = None,

        #POLY dummy setting
        _inv_NMOSDummy = None, #TF
            #if _NMOSDummy == True
        _inv_NMOSDummy_length = None, #None/Value
        _inv_NMOSDummy_placement = None, #None/Up/Dn/

        # PMOS inverter
        _inv_PMOSNumberofGate = None,
        _inv_PMOSChannelWidth = None,
        _inv_PMOSChannellength = None,
        _inv_PMOSGateSpacing = None,
        _inv_PMOSSDWidth = None,
        _inv_PMOSXVT = None,
        _inv_PMOSPCCrit = None,

            # Source_node_ViaM1M2
        _inv_PMOSSource_Via_TF = None,

            # Drain_node_ViaM1M2
        _inv_PMOSDrain_Via_TF = None,

            # POLY dummy setting
        _inv_PMOSDummy = None,  # TF
            # if _PMOSDummy == True
        _inv_PMOSDummy_length = None,  # None/Value
        _inv_PMOSDummy_placement = None,  # None/Up/Dn/

        # NMOS TG
        _tg_NMOSNumberofGate=None,
        _tg_NMOSChannelWidth=None,
        _tg_NMOSChannellength=None,
        _tg_NMOSGateSpacing	= None,
        _tg_NMOSSDWidth			= None,
        _tg_NMOSXVT				= None,
        _tg_NMOSPCCrit				= None,

        # Source_node_ViaM1M2
        _tg_NMOSSource_Via_TF = None,

        # Drain_node_ViaM1M2
        _tg_NMOSDrain_Via_TF = None,

        # POLY dummy setting
        _tg_NMOSDummy = None, # TF
        # if _NMOSDummy == True
        _tg_NMOSDummy_length = None, # None/Value
        _tg_NMOSDummy_placement = None, # None/Up/Dn/

        # PMOS TG
        _tg_PMOSNumberofGate = None,
        _tg_PMOSChannelWidth = None,
        _tg_PMOSChannellength = None,
        _tg_PMOSGateSpacing = None,
        _tg_PMOSSDWidth = None,
        _tg_PMOSXVT = None,
        _tg_PMOSPCCrit = None,

        # Source_node_ViaM1M2
        _tg_PMOSSource_Via_TF = None,

        # Drain_node_ViaM1M2
        _tg_PMOSDrain_Via_TF = None,

        # POLY dummy setting
        _tg_PMOSDummy = None,  # TF
        # if _PMOSDummy == True
        _tg_PMOSDummy_length = None,  # None/Value
        _tg_PMOSDummy_placement = None,  # None/Up/Dn/

        # 저항
        _ResWidth_Runit=1000,
        _ResLength_Runit=5850,
        _CONUMX_Runit=None,
        _CONUMY_Runit=None,
        _SeriesStripes_Runit=25,
        _ParallelStripes_Runit=1,
    )

    ## Initially Generated _DesignParameter

    def __init__(self, _DesignParameter=None, _Name=None):
        if _DesignParameter != None:
            self._DesignParameter = _DesignParameter
        else:
            self._DesignParameter = dict(
                _Name=self._NameDeclaration(_Name=_Name),
                _GDSFile=self._GDSObjDeclaration(_GDSFile=None),
                _XYcoordAsCent=dict(_XYcoordAsCent=0),
            )

     ## ################################################################################################################################################ _CalculateDesignParameter

    def _CalculateDesignParameter(self,

                                  # NMOS inverter
                                  _inv_NMOSNumberofGate=None,
                                  _inv_NMOSChannelWidth=None,
                                  _inv_NMOSChannellength=None,
                                  _inv_NMOSGateSpacing=None,
                                  _inv_NMOSSDWidth	= None,
                                  _inv_NMOSXVT			= None,
                                  _inv_NMOSPCCrit			= None,

                                  # Source_node_ViaM1M2
                                  _inv_NMOSSource_Via_TF= None,

                                  # Drain_node_ViaM1M2
                                  _inv_NMOSDrain_Via_TF= None,

                                  # POLY dummy setting
                                  _inv_NMOSDummy= None  , # TF
                                  # if _PMOSDummy == True
                                  _inv_NMOSDummy_length = None, # None/Value
                                  _inv_NMOSDummy_placement = None, # None/Up/Dn/

                                  # PMOS inverter
                                  _inv_PMOSNumberofGate=None,
                                  _inv_PMOSChannelWidth=None,
                                  _inv_PMOSChannellength=None,
                                  _inv_PMOSGateSpacing=None,
                                  _inv_PMOSSDWidth=None,
                                  _inv_PMOSXVT=None,
                                  _inv_PMOSPCCrit=None,

                                  # Source_node_ViaM1M2
                                  _inv_PMOSSource_Via_TF=None,

                                  # Drain_node_ViaM1M2
                                  _inv_PMOSDrain_Via_TF=None,

                                  # POLY dummy setting
                                  _inv_PMOSDummy=None,  # TF
                                  # if _PMOSDummy == True
                                  _inv_PMOSDummy_length=None,  # None/Value
                                  _inv_PMOSDummy_placement=None,  # None/Up/Dn/

                                  # NMOS tg
                                  _tg_NMOSNumberofGate=None,
                                  _tg_NMOSChannelWidth=None,
                                  _tg_NMOSChannellength=None,
                                  _tg_NMOSGateSpacing=None,
                                  _tg_NMOSSDWidth=None,
                                  _tg_NMOSXVT	= None,
                                  _tg_NMOSPCCrit		= None,

                                  # Source_node_ViaM1M2
                                  _tg_NMOSSource_Via_TF= None,

                                  # Drain_node_ViaM1M2
                                  _tg_NMOSDrain_Via_TF= None,

                                  # POLY dummy setting
                                  _tg_NMOSDummy= None  , # TF
                                  # if _PMOSDummy == True
                                  _tg_NMOSDummy_length = None, # None/Value
                                  _tg_NMOSDummy_placement = None, # None/Up/Dn/

                                  # PMOS inverter
                                  _tg_PMOSNumberofGate=None,
                                  _tg_PMOSChannelWidth=None,
                                  _tg_PMOSChannellength=None,
                                  _tg_PMOSGateSpacing=None,
                                  _tg_PMOSSDWidth=None,
                                  _tg_PMOSXVT=None,
                                  _tg_PMOSPCCrit=None,

                                  # Source_node_ViaM1M2
                                  _tg_PMOSSource_Via_TF=None,

                                  # Drain_node_ViaM1M2
                                  _tg_PMOSDrain_Via_TF=None,

                                  # POLY dummy setting
                                  _tg_PMOSDummy=None,  # TF
                                  # if _PMOSDummy == True
                                  _tg_PMOSDummy_length=None,  # None/Value
                                  _tg_PMOSDummy_placement=None,  # None/Up/Dn/

                                  # Resistor
                                  _ResWidth_Runit=1000,
                                  _ResLength_Runit=5850,
                                  _CONUMX_Runit=None,
                                  _CONUMY_Runit=None,
                                  _SeriesStripes_Runit=25,
                                  _ParallelStripes_Runit=1,

                                  ):

        ## ################################################################################################################################# Class_HEADER: Pre Defined Parameter Before Calculation
        # Load DRC library
        _DRCObj = DRC_EGFET.DRC()

        # Define _name
        _Name = self._DesignParameter['_Name']['_Name']


        ## ################################################################################################################################# Calculation_Start
        print('##############################')
        print('##     Calculation_Start    ##')
        print('##############################')



        ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_nmos_power_v2._NMOS_POWER._ParametersForDesignCalculation)
        _Caculation_Parameters = copy.deepcopy(A50_TIA_TG._TIA_TG_YCH._ParametersForDesignCalculation)
        ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
        _Caculation_Parameters['_inv_NMOSNumberofGate'] = _inv_NMOSNumberofGate
        _Caculation_Parameters['_inv_NMOSChannelWidth'] = _inv_NMOSChannelWidth
        _Caculation_Parameters['_inv_NMOSChannellength'] = _inv_NMOSChannellength
        _Caculation_Parameters['_inv_NMOSGateSpacing'] = _inv_NMOSGateSpacing
        _Caculation_Parameters['_inv_NMOSSDWidth'] = _inv_NMOSSDWidth
        _Caculation_Parameters['_inv_NMOSXVT'] = _inv_NMOSXVT
        _Caculation_Parameters['_inv_NMOSPCCrit'] = _inv_NMOSPCCrit
        _Caculation_Parameters['_inv_NMOSSource_Via_TF'] = _inv_NMOSSource_Via_TF
        _Caculation_Parameters['_inv_NMOSDrain_Via_TF'] = _inv_NMOSDrain_Via_TF
        _Caculation_Parameters['_inv_NMOSDummy'] = _inv_NMOSDummy
        _Caculation_Parameters['_inv_NMOSDummy_length'] = _inv_NMOSDummy_length
        _Caculation_Parameters['_inv_NMOSDummy_placement'] = _inv_NMOSDummy_placement

        _Caculation_Parameters['_inv_PMOSNumberofGate'] = _inv_PMOSNumberofGate
        _Caculation_Parameters['_inv_PMOSChannelWidth'] = _inv_PMOSChannelWidth
        _Caculation_Parameters['_inv_PMOSChannellength'] = _inv_PMOSChannellength
        _Caculation_Parameters['_inv_PMOSGateSpacing'] = _inv_PMOSGateSpacing
        _Caculation_Parameters['_inv_PMOSSDWidth'] = _inv_PMOSSDWidth
        _Caculation_Parameters['_inv_PMOSXVT'] = _inv_PMOSXVT
        _Caculation_Parameters['_inv_PMOSPCCrit'] = _inv_PMOSPCCrit
        _Caculation_Parameters['_inv_PMOSSource_Via_TF'] = _inv_PMOSSource_Via_TF
        _Caculation_Parameters['_inv_PMOSDrain_Via_TF'] = _inv_PMOSDrain_Via_TF
        _Caculation_Parameters['_inv_PMOSDummy'] = _inv_PMOSDummy
        _Caculation_Parameters['_inv_PMOSDummy_length'] = _inv_PMOSDummy_length
        _Caculation_Parameters['_inv_PMOSDummy_placement'] = _inv_PMOSDummy_placement

        _Caculation_Parameters['_tg_NMOSNumberofGate'] = _tg_NMOSNumberofGate
        _Caculation_Parameters['_tg_NMOSChannelWidth'] = _tg_NMOSChannelWidth
        _Caculation_Parameters['_tg_NMOSChannellength'] = _tg_NMOSChannellength
        _Caculation_Parameters['_tg_NMOSGateSpacing'] = _tg_NMOSGateSpacing
        _Caculation_Parameters['_tg_NMOSSDWidth'] = _tg_NMOSSDWidth
        _Caculation_Parameters['_tg_NMOSXVT'] = _tg_NMOSXVT
        _Caculation_Parameters['_tg_NMOSPCCrit'] = _tg_NMOSPCCrit
        _Caculation_Parameters['_tg_NMOSSource_Via_TF'] = _tg_NMOSSource_Via_TF
        _Caculation_Parameters['_tg_NMOSDrain_Via_TF'] = _tg_NMOSDrain_Via_TF
        _Caculation_Parameters['_tg_NMOSDummy'] = _tg_NMOSDummy
        _Caculation_Parameters['_tg_NMOSDummy_length'] = _tg_NMOSDummy_length
        _Caculation_Parameters['_tg_NMOSDummy_placement'] = _tg_NMOSDummy_placement

        _Caculation_Parameters['_tg_PMOSNumberofGate'] = _tg_PMOSNumberofGate
        _Caculation_Parameters['_tg_PMOSChannelWidth'] = _tg_PMOSChannelWidth
        _Caculation_Parameters['_tg_PMOSChannellength'] = _tg_PMOSChannellength
        _Caculation_Parameters['_tg_PMOSGateSpacing'] = _tg_PMOSGateSpacing
        _Caculation_Parameters['_tg_PMOSSDWidth'] = _tg_PMOSSDWidth
        _Caculation_Parameters['_tg_PMOSXVT'] = _tg_PMOSXVT
        _Caculation_Parameters['_tg_PMOSPCCrit'] = _tg_PMOSPCCrit
        _Caculation_Parameters['_tg_PMOSSource_Via_TF'] = _tg_PMOSSource_Via_TF
        _Caculation_Parameters['_tg_PMOSDrain_Via_TF'] = _tg_PMOSDrain_Via_TF
        _Caculation_Parameters['_tg_PMOSDummy'] = _tg_PMOSDummy
        _Caculation_Parameters['_tg_PMOSDummy_length'] = _tg_PMOSDummy_length
        _Caculation_Parameters['_tg_PMOSDummy_placement'] = _tg_PMOSDummy_placement

        ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_TG'] = self._SrefElementDeclaration(
            _DesignObj=A50_TIA_TG._TIA_TG_YCH(_DesignParameter=None, _Name='{}:SRF_TG'.format(_Name)))[0]

        ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_TG']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_TG']['_Angle'] = 0

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_TG']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_TG']['_XYCoordinates'] = [[0, 0]]


        ## SREF Generation Resistor0
        ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_nmos_power_v2._NMOS_POWER._ParametersForDesignCalculation)
        _Caculation_Parameters = copy.deepcopy(A50_opppcres_b._Opppcres_b_YCH._ParametersForDesignCalculation)
        _Caculation_Parameters['_ResWidth'] = _ResWidth_Runit
        _Caculation_Parameters['_ResLength'] = _ResLength_Runit
        _Caculation_Parameters['_CONUMX'] = _CONUMX_Runit
        _Caculation_Parameters['_CONUMY'] = _CONUMY_Runit
        _Caculation_Parameters['_SeriesStripes'] = _SeriesStripes_Runit
        _Caculation_Parameters['_ParallelStripes'] = _ParallelStripes_Runit

        ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_Res_Runit'] = self._SrefElementDeclaration(
            _DesignObj=A50_opppcres_b._Opppcres_b_YCH(_DesignParameter=None, _Name='{}:SRF_Res_Runit'.format(_Name)))[0]

        ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_Res_Runit']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Res_Runit']['_Angle'] = 0

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Res_Runit']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Res_Runit']['_XYCoordinates'] = [[0, 0]]

        tmpXY = []

        # Calculate
        # Target_coord
        tmp1 = self.get_param_KJH4('SRF_TG','BND_Metal3Layer_connect_Drain_tg')
        target_coord = tmp1[0][0][0]['_XY_down_left']
        # Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_Res_Runit')
        approaching_coord = tmp2[0][0]['_XY_down_left']
        # Sref coord
        tmp3 = self.get_param_KJH4('SRF_Res_Runit')
        Scoord = tmp3[0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        # Define
        self._DesignParameter['SRF_Res_Runit']['_XYCoordinates'] = tmpXY


        print('##############################')
        print('##     Calculation_End    ##')
        print('##############################')


## ########################################################################################################################################################## Start_Main
if __name__ == '__main__':

    from TIA_Proj_YCH.Library_and_Engine.Private import MyInfo_YCH
    from TIA_Proj_YCH.Library_and_Engine import DRCchecker_KJH0

    libname = 'Proj_A51_TIA_Runit_v2'
    cellname = 'A51_TIA_Runit'
    _fileName = cellname + '.gds'

    ''' Input Parameters for Layout Object '''
    InputParams = dict(
        # NMOS inverter
        _inv_NMOSNumberofGate=2,
        _inv_NMOSChannelWidth=500,
        _inv_NMOSChannellength=150,
        _inv_NMOSGateSpacing=None,
        _inv_NMOSSDWidth=None,
        _inv_NMOSXVT='EG',
        _inv_NMOSPCCrit	= None,

        # Source_node_ViaM1M2
        _inv_NMOSSource_Via_TF= True,

        # Drain_node_ViaM1M2
        _inv_NMOSDrain_Via_TF= True,

        # POLY dummy setting
        _inv_NMOSDummy= True  , # TF
        # if _PMOSDummy == True
        _inv_NMOSDummy_length = None, # None/Value
        _inv_NMOSDummy_placement = None, # None/Up/Dn/

        # PMOS inverter
        _inv_PMOSNumberofGate=2,
        _inv_PMOSChannelWidth=1000,
        _inv_PMOSChannellength=150,
        _inv_PMOSGateSpacing=None,
        _inv_PMOSSDWidth=None,
        _inv_PMOSXVT='EG',
        _inv_PMOSPCCrit=None,

        # Source_node_ViaM1M2
        _inv_PMOSSource_Via_TF=True,

        # Drain_node_ViaM1M2
        _inv_PMOSDrain_Via_TF=True,

        # POLY dummy setting
        _inv_PMOSDummy=True,  # TF
        # if _PMOSDummy == True
        _inv_PMOSDummy_length=None,  # None/Value
        _inv_PMOSDummy_placement=None,  # None/Up/Dn/

        # NMOS tg
        _tg_NMOSNumberofGate=100,
        _tg_NMOSChannelWidth=500,
        _tg_NMOSChannellength=150,
        _tg_NMOSGateSpacing=None,
        _tg_NMOSSDWidth=None,
        _tg_NMOSXVT	= 'EG',
        _tg_NMOSPCCrit		= None,

        # Source_node_ViaM1M2
        _tg_NMOSSource_Via_TF= True,

        # Drain_node_ViaM1M2
        _tg_NMOSDrain_Via_TF= True,

        # POLY dummy setting
        _tg_NMOSDummy= True  , # TF
        # if _PMOSDummy == True
        _tg_NMOSDummy_length = None, # None/Value
        _tg_NMOSDummy_placement = None, # None/Up/Dn/

        # PMOS inverter
        _tg_PMOSNumberofGate=100,
        _tg_PMOSChannelWidth=1000,
        _tg_PMOSChannellength=150,
        _tg_PMOSGateSpacing=None,
        _tg_PMOSSDWidth=None,
        _tg_PMOSXVT='EG',
        _tg_PMOSPCCrit=None,

        # Source_node_ViaM1M2
        _tg_PMOSSource_Via_TF=True,

        # Drain_node_ViaM1M2
        _tg_PMOSDrain_Via_TF=True,

        # POLY dummy setting
        _tg_PMOSDummy=True,  # TF
        # if _PMOSDummy == True
        _tg_PMOSDummy_length=None,  # None/Value
        _tg_PMOSDummy_placement=None,  # None/Up/Dn/

        # Resistor
        _ResWidth_Runit=1000,
        _ResLength_Runit=5850,
        _CONUMX_Runit=None,
        _CONUMY_Runit=None,
        _SeriesStripes_Runit=25,
        _ParallelStripes_Runit=1,

    )

    '''Mode_DRCCHECK '''
    Mode_DRCCheck = False
    Num_DRCCheck = 1

    for ii in range(0, Num_DRCCheck if Mode_DRCCheck else 1):
        if Mode_DRCCheck:
            ''' Input Parameters for Layout Object '''
        else:
            pass

    ''' Generate Layout Object '''
    LayoutObj = _TIA_Runit_YCH(_DesignParameter=None, _Name=cellname)
    LayoutObj._CalculateDesignParameter(**InputParams)
    LayoutObj._UpdateDesignParameter2GDSStructure(_DesignParameterInDictionary=LayoutObj._DesignParameter)
    testStreamFile = open('./{}'.format(_fileName), 'wb')
    tmp = LayoutObj._CreateGDSStream(LayoutObj._DesignParameter['_GDSFile']['_GDSFile'])
    tmp.write_binary_gds_stream(testStreamFile)
    testStreamFile.close()

    print('###############      Sending to FTP Server...      ##################')
    My = MyInfo_YCH.USER(DesignParameters._Technology)
    Checker = DRCchecker_KJH0.DRCchecker_KJH0(
        username=My.ID,
        password=My.PW,
        WorkDir=My.Dir_Work,
        DRCrunDir=My.Dir_DRCrun,
        libname=libname,
        cellname=cellname,
        GDSDir=My.Dir_GDS
    )
    # Checker.lib_deletion()
    Checker.cell_deletion()
    Checker.Upload2FTP()
    Checker.StreamIn(tech=DesignParameters._Technology)
    # Checker_KJH0.DRCchecker()
    print('#############################      Finished      ################################')
# end of 'main():' ---------------------------------------------------------------------------------------------