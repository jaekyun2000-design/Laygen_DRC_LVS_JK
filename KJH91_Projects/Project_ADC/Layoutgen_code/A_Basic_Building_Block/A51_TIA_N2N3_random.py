from KJH91_Projects.Project_ADC.Library_and_Engine import StickDiagram_KJH1, DesignParameters
from KJH91_Projects.Project_ADC.Library_and_Engine import DRC_EGFET

import numpy as np
import copy
import math

# from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A02_ViaStack_KJH2
# from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A03_NmosWithDummy_KJH4_YCH_TIA
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A50_TIA_N2_random
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A50_TIA_N3_random





## ########################################################################################################################################################## Class_HEADER
class _TIA_N2N3_YCH(StickDiagram_KJH1._StickDiagram_KJH):

    ## Define input_parameters for Design calculation
    _ParametersForDesignCalculation = dict(

        # NMOS
        _Tr2_NMOSNumberofGate=45,
        _Tr2_NMOSChannelWidth=6000,
        _Tr2_NMOSChannellength=150,
        _Tr2_GateSpacing	= None,
        _Tr2_SDWidth			= None,
        _Tr2_XVT				= 'EG',
        _Tr2_PCCrit				= None,

        # Source_node_ViaM1M2
        _Tr2_Source_Via_TF = True,

        # Drain_node_ViaM1M2
        _Tr2_Drain_Via_TF = True,

        # POLY dummy setting
        _Tr2_NMOSDummy = True, # TF
        # if _PMOSDummy == True
        _Tr2_NMOSDummy_length = None, # None/Value
        _Tr2_NMOSDummy_placement = None, # None/'Up'/'Dn'/

        #NMOS
        _Tr3_NMOSNumberofGate	= None,
        _Tr3_NMOSChannelWidth	= None,
        _Tr3_NMOSChannellength	= None,
        _Tr3_GateSpacing		= None,
        _Tr3_SDWidth			= None,
        _Tr3_XVT				= None,
        _Tr3_PCCrit				= None,

        #Source_node_ViaM1M2
        _Tr3_Source_Via_TF = None,

        #Drain_node_ViaM1M2
        _Tr3_Drain_Via_TF = None,

        #POLY dummy setting
        _Tr3_NMOSDummy = None, #TF
            #if _PMOSDummy == True
        _Tr3_NMOSDummy_length = None, #None/Value
        _Tr3_NMOSDummy_placement = None #None/Up/Dn/
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

                                  # NMOS
                                  _Tr2_NMOSNumberofGate=None,
                                  _Tr2_NMOSChannelWidth=None,
                                  _Tr2_NMOSChannellength=None,
                                  _Tr2_GateSpacing=None,
                                  _Tr2_SDWidth=None,
                                  _Tr2_XVT=None,
                                  _Tr2_PCCrit	= None,

                                  # Source_node_ViaM1M2
                                  _Tr2_Source_Via_TF= None,

                                  # Drain_node_ViaM1M2
                                  _Tr2_Drain_Via_TF= None,

                                  # POLY dummy setting
                                  _Tr2_NMOSDummy= None  , # TF
                                  # if _PMOSDummy == True
                                  _Tr2_NMOSDummy_length = None, # None/Value
                                  _Tr2_NMOSDummy_placement = None, # None/Up/Dn/

                                  # NMOS
                                  _Tr3_NMOSNumberofGate=None,
                                  _Tr3_NMOSChannelWidth=None,
                                  _Tr3_NMOSChannellength=None,
                                  _Tr3_GateSpacing=None,
                                  _Tr3_SDWidth	= None,
                                  _Tr3_XVT			= None,
                                  _Tr3_PCCrit			= None,

                                  # Source_node_ViaM1M2
                                  _Tr3_Source_Via_TF= None,

                                  # Drain_node_ViaM1M2
                                  _Tr3_Drain_Via_TF= None,

                                  # POLY dummy setting
                                  _Tr3_NMOSDummy= None  , # TF
                                  # if _PMOSDummy == True
                                  _Tr3_NMOSDummy_length = None, # None/Value
                                  _Tr3_NMOSDummy_placement = None, # None/Up/Dn/


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


        ## SREF Generation Tr2
        ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_nmos_power_v2._NMOS_POWER._ParametersForDesignCalculation)
        _Caculation_Parameters = copy.deepcopy(A50_TIA_N2_random._TIA_N2_YCH._ParametersForDesignCalculation)
        ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
        _Caculation_Parameters['_Tr2_NMOSNumberofGate'] = _Tr2_NMOSNumberofGate
        _Caculation_Parameters['_Tr2_NMOSChannelWidth'] = _Tr2_NMOSChannelWidth
        _Caculation_Parameters['_Tr2_NMOSChannellength'] = _Tr2_NMOSChannellength
        _Caculation_Parameters['_Tr2_GateSpacing'] = _Tr2_GateSpacing
        _Caculation_Parameters['_Tr2_SDWidth'] = _Tr2_SDWidth
        _Caculation_Parameters['_Tr2_XVT'] = _Tr2_XVT
        _Caculation_Parameters['_Tr2_PCCrit'] = _Tr2_PCCrit
        _Caculation_Parameters['_Tr2_Source_Via_TF'] = _Tr2_Source_Via_TF
        _Caculation_Parameters['_Tr2_Drain_Via_TF'] = _Tr2_Drain_Via_TF
        _Caculation_Parameters['_Tr2_NMOSDummy'] = _Tr2_NMOSDummy
        _Caculation_Parameters['_Tr2_NMOSDummy_length'] = _Tr2_NMOSDummy_length
        _Caculation_Parameters['_Tr2_NMOSDummy_placement'] = _Tr2_NMOSDummy_placement

        ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_Nmos_Tr2'] = self._SrefElementDeclaration(
            _DesignObj=A50_TIA_N2_random._TIA_N2_YCH(_DesignParameter=None, _Name='{}:SRF_Nmos_Tr2'.format(_Name)))[0]

        ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_Nmos_Tr2']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Nmos_Tr2']['_Angle'] = 0

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Nmos_Tr2']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Nmos_Tr2']['_XYCoordinates'] = [[0, 0]]

        ## SREF Generation Tr3
        ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_nmos_power_v2._NMOS_POWER._ParametersForDesignCalculation)
        _Caculation_Parameters = copy.deepcopy(A50_TIA_N3_random._TIA_N3_YCH._ParametersForDesignCalculation)
        ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
        _Caculation_Parameters['_Tr3_NMOSNumberofGate'] = _Tr3_NMOSNumberofGate
        _Caculation_Parameters['_Tr3_NMOSChannelWidth'] = _Tr3_NMOSChannelWidth
        _Caculation_Parameters['_Tr3_NMOSChannellength'] = _Tr3_NMOSChannellength
        _Caculation_Parameters['_Tr3_GateSpacing'] = _Tr3_GateSpacing
        _Caculation_Parameters['_Tr3_SDWidth'] = _Tr3_SDWidth
        _Caculation_Parameters['_Tr3_XVT'] = _Tr3_XVT
        _Caculation_Parameters['_Tr3_PCCrit'] = _Tr3_PCCrit
        _Caculation_Parameters['_Tr3_Source_Via_TF'] = _Tr3_Source_Via_TF
        _Caculation_Parameters['_Tr3_Drain_Via_TF'] = _Tr3_Drain_Via_TF
        _Caculation_Parameters['_Tr3_NMOSDummy'] = _Tr3_NMOSDummy
        _Caculation_Parameters['_Tr3_NMOSDummy_length'] = _Tr3_NMOSDummy_length
        _Caculation_Parameters['_Tr3_NMOSDummy_placement'] = _Tr3_NMOSDummy_placement

        ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_Nmos_Tr3'] = self._SrefElementDeclaration(
            _DesignObj=A50_TIA_N3_random._TIA_N3_YCH(_DesignParameter=None, _Name='{}:SRF_Nmos_Tr3'.format(_Name)))[0]

        ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_Nmos_Tr3']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Nmos_Tr3']['_Angle'] = 0

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Nmos_Tr3']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Nmos_Tr3']['_XYCoordinates'] = [[0, 0]]

        tmpXY = []
        # Target_coord
        tmp1 = self.get_param_KJH4('SRF_Nmos_Tr2', 'SRF_Nmos', 'BND_POLayer')
        target_coord = tmp1[0][0][-1][0]['_XY_right']
        # Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_Nmos_Tr3', 'SRF_Nmos', 'BND_POLayer')
        approaching_coord = tmp2[0][0][0][0]['_XY_left']
        # Sref coord
        tmp3 = self.get_param_KJH4('SRF_Nmos_Tr3', 'SRF_Nmos', 'BND_POLayer')
        Scoord = tmp3[0][0][0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)

        if (_Tr2_GateSpacing == None):
            _Tr2_GateSpacing = _DRCObj._PolygateMinSpace2
            _Tr2_GatetoGate = 2 * _Tr2_GateSpacing + _Tr2_NMOSChannellength
        else:
            _Tr2_GatetoGate = 2 * _Tr2_GateSpacing + _Tr2_NMOSChannellength

        New_Scoord[0] = New_Scoord[0] + _Tr2_GatetoGate
        tmpXY.append(New_Scoord)
        # Define
        self._DesignParameter['SRF_Nmos_Tr3']['_XYCoordinates'] = tmpXY






## ########################################################################################################################################################## Start_Main
if __name__ == '__main__':

    from KJH91_Projects.Project_ADC.Library_and_Engine.Private import MyInfo_YCH
    from KJH91_Projects.Project_ADC.Library_and_Engine import DRCchecker_KJH0
    import random

    for _iter in range(10):
        libname = 'Proj_A51_TIA_N2N3_v{}'.format(_iter + 1)
        cellname = 'A51_TIA_N2N3'
        _fileName = cellname + '.gds'

        _TR2_3_PMOSChannelWidth = random.randrange(3000, 10000, 1000)

        ''' Input Parameters for Layout Object '''
        InputParams = dict(

            #NMOS
            _Tr2_NMOSNumberofGate=random.randrange(2, 10, 1),
            _Tr2_NMOSChannelWidth=_TR2_3_PMOSChannelWidth,
            _Tr2_NMOSChannellength=150,
            _Tr2_GateSpacing	= None,
            _Tr2_SDWidth			= None,
            _Tr2_XVT				= 'EG',
            _Tr2_PCCrit				= None,

            # Source_node_ViaM1M2
            _Tr2_Source_Via_TF = True,

            # Drain_node_ViaM1M2
            _Tr2_Drain_Via_TF = True,

            # POLY dummy setting
            _Tr2_NMOSDummy = True, # TF
            # if _PMOSDummy == True
            _Tr2_NMOSDummy_length = None, # None/Value
            _Tr2_NMOSDummy_placement = None, # None/'Up'/'Dn'/

            # NMOS
            _Tr3_NMOSNumberofGate=random.randrange(2, 10, 1),
            _Tr3_NMOSChannelWidth=_TR2_3_PMOSChannelWidth,
            _Tr3_NMOSChannellength=150,
            _Tr3_GateSpacing	= None,
            _Tr3_SDWidth			= None,
            _Tr3_XVT				= 'EG',
            _Tr3_PCCrit				= None,

            # Source_node_ViaM1M2
            _Tr3_Source_Via_TF = True,

            # Drain_node_ViaM1M2
            _Tr3_Drain_Via_TF = True,

            # POLY dummy setting
            _Tr3_NMOSDummy = True, # TF
            # if _PMOSDummy == True
            _Tr3_NMOSDummy_length = None, # None/Value
            _Tr3_NMOSDummy_placement = None, # None/'Up'/'Dn'/

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
        LayoutObj = _TIA_N2N3_YCH(_DesignParameter=None, _Name=cellname)
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
        #Checker.lib_deletion()
        Checker.cell_deletion()
        Checker.Upload2FTP()
        Checker.StreamIn(tech=DesignParameters._Technology)
        # Checker_KJH0.DRCchecker()
        print('#############################      Finished      ################################')
    # end of 'main():' ---------------------------------------------------------------------------------------------
