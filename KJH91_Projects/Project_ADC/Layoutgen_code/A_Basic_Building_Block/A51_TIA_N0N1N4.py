from KJH91_Projects.Project_ADC.Library_and_Engine import StickDiagram_KJH1, DesignParameters
from KJH91_Projects.Project_ADC.Library_and_Engine import DRC_EGFET

import numpy as np
import copy
import math

# from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A02_ViaStack_KJH2
# from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A04_PmosWithDummy_KJH3_YCH_TIA
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A50_TIA_N0
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A50_TIA_N1
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A50_TIA_N4



## ########################################################################################################################################################## Class_HEADER
class _TIA_N0N1N4_YCH(StickDiagram_KJH1._StickDiagram_KJH):

    ## Define input_parameters for Design calculation
    _ParametersForDesignCalculation = dict(

        # NMOS
        _Tr0_NMOSNumberofGate=None,
        _Tr0_NMOSChannelWidth=None,
        _Tr0_NMOSChannellength=None,
        _Tr0_GateSpacing	= None,
        _Tr0_SDWidth			= None,
        _Tr0_XVT				= None,
        _Tr0_PCCrit				= None,

        # Source_node_ViaM1M2
        _Tr0_Source_Via_TF = None,

        # Drain_node_ViaM1M2
        _Tr0_Drain_Via_TF = None,

        # POLY dummy setting
        _Tr0_NMOSDummy = None, # TF
        # if _NMOSDummy == True
        _Tr0_NMOSDummy_length = None, # None/Value
        _Tr0_NMOSDummy_placement = None, # None/Up/Dn/

        # NMOS
        _Tr1_NMOSNumberofGate = None,
        _Tr1_NMOSChannelWidth = None,
        _Tr1_NMOSChannellength = None,
        _Tr1_GateSpacing = None,
        _Tr1_SDWidth = None,
        _Tr1_XVT = None,
        _Tr1_PCCrit = None,

            # Source_node_ViaM1M2
        _Tr1_Source_Via_TF = None,

            # Drain_node_ViaM1M2
        _Tr1_Drain_Via_TF = None,

            # POLY dummy setting
        _Tr1_NMOSDummy = None,  # TF
            # if _NMOSDummy == True
        _Tr1_NMOSDummy_length = None,  # None/Value
        _Tr1_NMOSDummy_placement = None,  # None/Up/Dn/

        # NMOS
        _Tr4_NMOSNumberofGate = None,
        _Tr4_NMOSChannelWidth = None,
        _Tr4_NMOSChannellength = None,
        _Tr4_GateSpacing = None,
        _Tr4_SDWidth = None,
        _Tr4_XVT = None,
        _Tr4_PCCrit = None,

            # Source_node_ViaM1M2
        _Tr4_Source_Via_TF = None,

            # Drain_node_ViaM1M2
        _Tr4_Drain_Via_TF = None,

            # POLY dummy setting
        _Tr4_NMOSDummy = None,  # TF
            # if _NMOSDummy == True
        _Tr4_NMOSDummy_length = None,  # None/Value
        _Tr4_NMOSDummy_placement = None  # None/Up/Dn/
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
                                  _Tr0_NMOSNumberofGate=None,
                                  _Tr0_NMOSChannelWidth=None,
                                  _Tr0_NMOSChannellength=None,
                                  _Tr0_GateSpacing=None,
                                  _Tr0_SDWidth	= None,
                                  _Tr0_XVT			= None,
                                  _Tr0_PCCrit			= None,

                                  # Source_node_ViaM1M2
                                  _Tr0_Source_Via_TF= None,

                                  # Drain_node_ViaM1M2
                                  _Tr0_Drain_Via_TF= None,

                                  # POLY dummy setting
                                  _Tr0_NMOSDummy= None  , # TF
                                  # if _PMOSDummy == True
                                  _Tr0_NMOSDummy_length = None, # None/Value
                                  _Tr0_NMOSDummy_placement = None, # None/Up/Dn/

                                  # NMOS
                                  _Tr1_NMOSNumberofGate=None,
                                  _Tr1_NMOSChannelWidth=None,
                                  _Tr1_NMOSChannellength=None,
                                  _Tr1_GateSpacing=None,
                                  _Tr1_SDWidth	= None,
                                  _Tr1_XVT			= None,
                                  _Tr1_PCCrit			= None,

                                  # Source_node_ViaM1M2
                                  _Tr1_Source_Via_TF= None,

                                  # Drain_node_ViaM1M2
                                  _Tr1_Drain_Via_TF= None,

                                  # POLY dummy setting
                                  _Tr1_NMOSDummy= None  , # TF
                                  # if _PMOSDummy == True
                                  _Tr1_NMOSDummy_length = None, # None/Value
                                  _Tr1_NMOSDummy_placement = None, # None/Up/Dn/

                                  # NMOS
                                  _Tr4_NMOSNumberofGate=None,
                                  _Tr4_NMOSChannelWidth=None,
                                  _Tr4_NMOSChannellength=None,
                                  _Tr4_GateSpacing=None,
                                  _Tr4_SDWidth	= None,
                                  _Tr4_XVT			= None,
                                  _Tr4_PCCrit			= None,

                                  # Source_node_ViaM1M2
                                  _Tr4_Source_Via_TF= None,

                                  # Drain_node_ViaM1M2
                                  _Tr4_Drain_Via_TF= None,

                                  # POLY dummy setting
                                  _Tr4_NMOSDummy= None  , # TF
                                  # if _PMOSDummy == True
                                  _Tr4_NMOSDummy_length = None, # None/Value
                                  _Tr4_NMOSDummy_placement = None, # None/Up/Dn/
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


        ## SREF Generation Tr4
        ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_nmos_power_v2._NMOS_POWER._ParametersForDesignCalculation)
        _Caculation_Parameters = copy.deepcopy(A50_TIA_N4._TIA_N4_YCH._ParametersForDesignCalculation)
                ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
        _Caculation_Parameters['_Tr4_NMOSNumberofGate']     = _Tr4_NMOSNumberofGate
        _Caculation_Parameters['_Tr4_NMOSChannelWidth']     = _Tr4_NMOSChannelWidth
        _Caculation_Parameters['_Tr4_NMOSChannellength']    = _Tr4_NMOSChannellength
        _Caculation_Parameters['_Tr4_GateSpacing']          = _Tr4_GateSpacing
        _Caculation_Parameters['_Tr4_SDWidth']              = _Tr4_SDWidth
        _Caculation_Parameters['_Tr4_XVT']                  = _Tr4_XVT
        _Caculation_Parameters['_Tr4_PCCrit']               = _Tr4_PCCrit
        _Caculation_Parameters['_Tr4_Source_Via_TF']        = _Tr4_Source_Via_TF
        _Caculation_Parameters['_Tr4_Drain_Via_TF']         = _Tr4_Drain_Via_TF
        _Caculation_Parameters['_Tr4_NMOSDummy']            = _Tr4_NMOSDummy
        _Caculation_Parameters['_Tr4_NMOSDummy_length']     = _Tr4_NMOSDummy_length
        _Caculation_Parameters['_Tr4_NMOSDummy_placement']  = _Tr4_NMOSDummy_placement

        ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_Nmos_Tr4'] = self._SrefElementDeclaration(_DesignObj=A50_TIA_N4._TIA_N4_YCH(_DesignParameter=None, _Name='{}:SRF_Nmos_Tr4'.format(_Name)))[0]

        ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_Nmos_Tr4']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Nmos_Tr4']['_Angle'] = 0

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Nmos_Tr4']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Nmos_Tr4']['_XYCoordinates'] = [[0, 0]]



        ## SREF Generation Tr0
        ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_nmos_power_v2._NMOS_POWER._ParametersForDesignCalculation)
        _Caculation_Parameters = copy.deepcopy(A50_TIA_N0._TIA_N0_YCH._ParametersForDesignCalculation)
        ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
        _Caculation_Parameters['_Tr0_NMOSNumberofGate'] = _Tr0_NMOSNumberofGate
        _Caculation_Parameters['_Tr0_NMOSChannelWidth'] = _Tr0_NMOSChannelWidth
        _Caculation_Parameters['_Tr0_NMOSChannellength'] = _Tr0_NMOSChannellength
        _Caculation_Parameters['_Tr0_GateSpacing'] = _Tr0_GateSpacing
        _Caculation_Parameters['_Tr0_SDWidth'] = _Tr0_SDWidth
        _Caculation_Parameters['_Tr0_XVT'] = _Tr0_XVT
        _Caculation_Parameters['_Tr0_PCCrit'] = _Tr0_PCCrit
        _Caculation_Parameters['_Tr0_Source_Via_TF'] = _Tr0_Source_Via_TF
        _Caculation_Parameters['_Tr0_Drain_Via_TF'] = _Tr0_Drain_Via_TF
        _Caculation_Parameters['_Tr0_NMOSDummy'] = _Tr0_NMOSDummy
        _Caculation_Parameters['_Tr0_NMOSDummy_length'] = _Tr0_NMOSDummy_length
        _Caculation_Parameters['_Tr0_NMOSDummy_placement'] = _Tr0_NMOSDummy_placement

        ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_Nmos_Tr0'] = self._SrefElementDeclaration(_DesignObj=A50_TIA_N0._TIA_N0_YCH(_DesignParameter=None,_Name='{}:SRF_Nmos_Tr0'.format(_Name)))[0]

        ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_Nmos_Tr0']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Nmos_Tr0']['_Angle'] = 0

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Nmos_Tr0']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Nmos_Tr0']['_XYCoordinates'] = [[0, 0]]

        tmpXY = []
        # Target_coord
        tmp1 = self.get_param_KJH4('SRF_Nmos_Tr4','SRF_Nmos','BND_POLayer')
        target_coord = tmp1[0][0][0][0]['_XY_left']
        # Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_Nmos_Tr0','SRF_Nmos','BND_POLayer')
        approaching_coord = tmp2[0][0][-1][0]['_XY_right']
        # Sref coord
        tmp3 = self.get_param_KJH4('SRF_Nmos_Tr0','SRF_Nmos','BND_POLayer')
        Scoord = tmp3[0][0][0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)

        if (_Tr4_GateSpacing == None):
            _Tr4_GateSpacing = _DRCObj._PolygateMinSpace2
            _Tr4_GatetoGate = 2 * _Tr4_GateSpacing + _Tr4_NMOSChannellength
        else :
            _Tr4_GatetoGate = 2 * _Tr4_GateSpacing + _Tr4_NMOSChannellength

        New_Scoord[0] = New_Scoord[0] - _Tr4_GatetoGate
        tmpXY.append(New_Scoord)
        # Define
        self._DesignParameter['SRF_Nmos_Tr0']['_XYCoordinates'] = tmpXY


        ## SREF Generation Tr1
        ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_nmos_power_v2._NMOS_POWER._ParametersForDesignCalculation)
        _Caculation_Parameters = copy.deepcopy(A50_TIA_N1._TIA_N1_YCH._ParametersForDesignCalculation)
        ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
        _Caculation_Parameters['_Tr1_NMOSNumberofGate'] = _Tr1_NMOSNumberofGate
        _Caculation_Parameters['_Tr1_NMOSChannelWidth'] = _Tr1_NMOSChannelWidth
        _Caculation_Parameters['_Tr1_NMOSChannellength'] = _Tr1_NMOSChannellength
        _Caculation_Parameters['_Tr1_GateSpacing'] = _Tr1_GateSpacing
        _Caculation_Parameters['_Tr1_SDWidth'] = _Tr1_SDWidth
        _Caculation_Parameters['_Tr1_XVT'] = _Tr1_XVT
        _Caculation_Parameters['_Tr1_PCCrit'] = _Tr1_PCCrit
        _Caculation_Parameters['_Tr1_Source_Via_TF'] = _Tr1_Source_Via_TF
        _Caculation_Parameters['_Tr1_Drain_Via_TF'] = _Tr1_Drain_Via_TF
        _Caculation_Parameters['_Tr1_NMOSDummy'] = _Tr1_NMOSDummy
        _Caculation_Parameters['_Tr1_NMOSDummy_length'] = _Tr1_NMOSDummy_length
        _Caculation_Parameters['_Tr1_NMOSDummy_placement'] = _Tr1_NMOSDummy_placement

        ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_Nmos_Tr1'] = self._SrefElementDeclaration(_DesignObj=A50_TIA_N1._TIA_N1_YCH(_DesignParameter=None,_Name='{}:SRF_Nmos_Tr1'.format(_Name)))[0]

        ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_Nmos_Tr1']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Nmos_Tr1']['_Angle'] = 0

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Nmos_Tr1']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Nmos_Tr1']['_XYCoordinates'] = [[0, 0]]


        tmpXY = []
        # Target_coord
        tmp1 = self.get_param_KJH4('SRF_Nmos_Tr4', 'SRF_Nmos', 'BND_POLayer')
        target_coord = tmp1[0][0][-1][0]['_XY_right']
        # Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_Nmos_Tr1', 'SRF_Nmos', 'BND_POLayer')
        approaching_coord = tmp2[0][0][0][0]['_XY_left']
        # Sref coord
        tmp3 = self.get_param_KJH4('SRF_Nmos_Tr1', 'SRF_Nmos', 'BND_POLayer')
        Scoord = tmp3[0][0][0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)


        if (_Tr4_GateSpacing == None):
            _Tr4_GateSpacing = _DRCObj._PolygateMinSpace2
            _Tr4_GatetoGate = 2 * _Tr4_GateSpacing + _Tr4_NMOSChannellength
        else :
            _Tr4_GatetoGate = 2 * _Tr4_GateSpacing + _Tr4_NMOSChannellength

        New_Scoord[0] = New_Scoord[0] + _Tr4_GatetoGate
        tmpXY.append(New_Scoord)
        # Define
        self._DesignParameter['SRF_Nmos_Tr1']['_XYCoordinates'] = tmpXY


        ## ################################################################################################################################# Calculation_End
        print('##############################')
        print('##     Calculation_End      ##')
        print('##############################')

## ########################################################################################################################################################## Start_Main
if __name__ == '__main__':
    from TIA_Proj_YCH.Library_and_Engine.Private import MyInfo_YCH
    from TIA_Proj_YCH.Library_and_Engine import DRCchecker_KJH0

    libname = 'Proj_A51_TIA_N0N1N4_v2'
    cellname = 'A51_TIA_N0N1N4'
    _fileName = cellname + '.gds'

    ''' Input Parameters for Layout Object '''
    InputParams = dict(
        # NMOS Tr0
        _Tr0_NMOSNumberofGate=15,
        _Tr0_NMOSChannelWidth=3000,
        _Tr0_NMOSChannellength=150,
        _Tr0_GateSpacing	= None,
        _Tr0_SDWidth			= None,
        _Tr0_XVT				= 'EG',
        _Tr0_PCCrit				= None,

        # Source_node_ViaM1M2
        _Tr0_Source_Via_TF = True,

        # Drain_node_ViaM1M2
        _Tr0_Drain_Via_TF = True,

        # POLY dummy setting
        _Tr0_NMOSDummy = True, # TF
        # if _PMOSDummy == True
        _Tr0_NMOSDummy_length = None, # None/Value
        _Tr0_NMOSDummy_placement = None, # None/'Up'/'Dn'/

        # NMOS Tr0
        _Tr1_NMOSNumberofGate=15,
        _Tr1_NMOSChannelWidth=3000,
        _Tr1_NMOSChannellength=150,
        _Tr1_GateSpacing	= None,
        _Tr1_SDWidth			= None,
        _Tr1_XVT				= 'EG',
        _Tr1_PCCrit				= None,

        # Source_node_ViaM1M2
        _Tr1_Source_Via_TF = True,

        # Drain_node_ViaM1M2
        _Tr1_Drain_Via_TF = True,

        # POLY dummy setting
        _Tr1_NMOSDummy = True, # TF
        # if _PMOSDummy == True
        _Tr1_NMOSDummy_length = None, # None/Value
        _Tr1_NMOSDummy_placement = None, # None/'Up'/'Dn'/

        # NMOS Tr0
        _Tr4_NMOSNumberofGate=8,
        _Tr4_NMOSChannelWidth=3000,
        _Tr4_NMOSChannellength=150,
        _Tr4_GateSpacing	= None,
        _Tr4_SDWidth			= None,
        _Tr4_XVT				= 'EG',
        _Tr4_PCCrit				= None,

        # Source_node_ViaM1M2
        _Tr4_Source_Via_TF = True,

        # Drain_node_ViaM1M2
        _Tr4_Drain_Via_TF = True,

        # POLY dummy setting
        _Tr4_NMOSDummy = True, # TF
        # if _PMOSDummy == True
        _Tr4_NMOSDummy_length = None, # None/Value
        _Tr4_NMOSDummy_placement = None, # None/'Up'/'Dn'/

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
    LayoutObj = _TIA_N0N1N4_YCH(_DesignParameter=None, _Name=cellname)
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