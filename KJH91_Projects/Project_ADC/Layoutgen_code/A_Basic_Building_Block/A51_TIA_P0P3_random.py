from KJH91_Projects.Project_ADC.Library_and_Engine import StickDiagram_KJH1, DesignParameters
from KJH91_Projects.Project_ADC.Library_and_Engine import DRC_EGFET

import numpy as np
import copy
import math

# from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A02_ViaStack_KJH2
# from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A04_PmosWithDummy_KJH3_YCH_TIA
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A50_TIA_P0_random
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A50_TIA_P3_random



## ########################################################################################################################################################## Class_HEADER
class _TIA_P0P3_YCH(StickDiagram_KJH1._StickDiagram_KJH):

    ## Define input_parameters for Design calculation
    _ParametersForDesignCalculation = dict(

        # PMOS
        _Tr0_PMOSNumberofGate=45,
        _Tr0_PMOSChannelWidth=6000,
        _Tr0_PMOSChannellength=150,
        _Tr0_GateSpacing	= None,
        _Tr0_SDWidth			= None,
        _Tr0_XVT				= 'EG',
        _Tr0_PCCrit				= None,

        # Source_node_ViaM1M2
        _Tr0_Source_Via_TF = True,

        # Drain_node_ViaM1M2
        _Tr0_Drain_Via_TF = True,

        # POLY dummy setting
        _Tr0_PMOSDummy = True, # TF
        # if _PMOSDummy == True
        _Tr0_PMOSDummy_length = None, # None/Value
        _Tr0_PMOSDummy_placement = None, # None/'Up'/'Dn'/

        #PMOS
        _Tr3_PMOSNumberofGate	= None,
        _Tr3_PMOSChannelWidth	= None,
        _Tr3_PMOSChannellength	= None,
        _Tr3_GateSpacing		= None,
        _Tr3_SDWidth			= None,
        _Tr3_XVT				= None,
        _Tr3_PCCrit				= None,

        #Source_node_ViaM1M2
        _Tr3_Source_Via_TF = None,

        #Drain_node_ViaM1M2
        _Tr3_Drain_Via_TF = None,

        #POLY dummy setting
        _Tr3_PMOSDummy = None, #TF
            #if _PMOSDummy == True
        _Tr3_PMOSDummy_length = None, #None/Value
        _Tr3_PMOSDummy_placement = None #None/Up/Dn/
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

                                  # PMOS
                                  _Tr0_PMOSNumberofGate=None,
                                  _Tr0_PMOSChannelWidth=None,
                                  _Tr0_PMOSChannellength=None,
                                  _Tr0_GateSpacing=None,
                                  _Tr0_SDWidth=None,
                                  _Tr0_XVT=None,
                                  _Tr0_PCCrit	= None,

                                  # Source_node_ViaM1M2
                                  _Tr0_Source_Via_TF= None,

                                  # Drain_node_ViaM1M2
                                  _Tr0_Drain_Via_TF= None,

                                  # POLY dummy setting
                                  _Tr0_PMOSDummy= None  , # TF
                                  # if _PMOSDummy == True
                                  _Tr0_PMOSDummy_length = None, # None/Value
                                  _Tr0_PMOSDummy_placement = None, # None/Up/Dn/

                                  # NMOS
                                  _Tr3_PMOSNumberofGate=None,
                                  _Tr3_PMOSChannelWidth=None,
                                  _Tr3_PMOSChannellength=None,
                                  _Tr3_GateSpacing=None,
                                  _Tr3_SDWidth	= None,
                                  _Tr3_XVT			= None,
                                  _Tr3_PCCrit			= None,

                                  # Source_node_ViaM1M2
                                  _Tr3_Source_Via_TF= None,

                                  # Drain_node_ViaM1M2
                                  _Tr3_Drain_Via_TF= None,

                                  # POLY dummy setting
                                  _Tr3_PMOSDummy= None  , # TF
                                  # if _PMOSDummy == True
                                  _Tr3_PMOSDummy_length = None, # None/Value
                                  _Tr3_PMOSDummy_placement = None, # None/Up/Dn/


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




        ## SREF Generation Tr0
        ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_nmos_power_v2._NMOS_POWER._ParametersForDesignCalculation)
        _Caculation_Parameters = copy.deepcopy(A50_TIA_P0_random._TIA_P0_YCH._ParametersForDesignCalculation)
        ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
        _Caculation_Parameters['_Tr0_PMOSNumberofGate'] = _Tr0_PMOSNumberofGate
        _Caculation_Parameters['_Tr0_PMOSChannelWidth'] = _Tr0_PMOSChannelWidth
        _Caculation_Parameters['_Tr0_PMOSChannellength'] = _Tr0_PMOSChannellength
        _Caculation_Parameters['_Tr0_GateSpacing'] = _Tr0_GateSpacing
        _Caculation_Parameters['_Tr0_SDWidth'] = _Tr0_SDWidth
        _Caculation_Parameters['_Tr0_XVT'] = _Tr0_XVT
        _Caculation_Parameters['_Tr0_PCCrit'] = _Tr0_PCCrit
        _Caculation_Parameters['_Tr0_Source_Via_TF'] = _Tr0_Source_Via_TF
        _Caculation_Parameters['_Tr0_Drain_Via_TF'] = _Tr0_Drain_Via_TF
        _Caculation_Parameters['_Tr0_PMOSDummy'] = _Tr0_PMOSDummy
        _Caculation_Parameters['_Tr0_PMOSDummy_length'] = _Tr0_PMOSDummy_length
        _Caculation_Parameters['_Tr0_PMOSDummy_placement'] = _Tr0_PMOSDummy_placement

        ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_Pmos_Tr0'] = self._SrefElementDeclaration(
            _DesignObj=A50_TIA_P0_random._TIA_P0_YCH(_DesignParameter=None, _Name='{}:SRF_Pmos_Tr0'.format(_Name)))[0]

        ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_Pmos_Tr0']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Pmos_Tr0']['_Angle'] = 0

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Pmos_Tr0']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Pmos_Tr0']['_XYCoordinates'] = [[0, 0]]

        ## SREF Generation Tr3
        ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_nmos_power_v2._NMOS_POWER._ParametersForDesignCalculation)
        _Caculation_Parameters = copy.deepcopy(A50_TIA_P3_random._TIA_P3_YCH._ParametersForDesignCalculation)
        ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
        _Caculation_Parameters['_Tr3_PMOSNumberofGate'] = _Tr3_PMOSNumberofGate
        _Caculation_Parameters['_Tr3_PMOSChannelWidth'] = _Tr3_PMOSChannelWidth
        _Caculation_Parameters['_Tr3_PMOSChannellength'] = _Tr3_PMOSChannellength
        _Caculation_Parameters['_Tr3_GateSpacing'] = _Tr3_GateSpacing
        _Caculation_Parameters['_Tr3_SDWidth'] = _Tr3_SDWidth
        _Caculation_Parameters['_Tr3_XVT'] = _Tr3_XVT
        _Caculation_Parameters['_Tr3_PCCrit'] = _Tr3_PCCrit
        _Caculation_Parameters['_Tr3_Source_Via_TF'] = _Tr3_Source_Via_TF
        _Caculation_Parameters['_Tr3_Drain_Via_TF'] = _Tr3_Drain_Via_TF
        _Caculation_Parameters['_Tr3_PMOSDummy'] = _Tr3_PMOSDummy
        _Caculation_Parameters['_Tr3_PMOSDummy_length'] = _Tr3_PMOSDummy_length
        _Caculation_Parameters['_Tr3_PMOSDummy_placement'] = _Tr3_PMOSDummy_placement

        ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_Pmos_Tr3'] = self._SrefElementDeclaration(
            _DesignObj=A50_TIA_P3_random._TIA_P3_YCH(_DesignParameter=None, _Name='{}:SRF_Pmos_Tr3'.format(_Name)))[0]

        ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_Pmos_Tr3']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Pmos_Tr3']['_Angle'] = 0

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Pmos_Tr3']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Pmos_Tr3']['_XYCoordinates'] = [[0, 0]]


        tmpXY = []
        # Target_coord
        tmp1 = self.get_param_KJH4('SRF_Pmos_Tr0','SRF_Pmos','BND_POLayer')
        target_coord = tmp1[0][0][0][0]['_XY_left']
        # Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_Pmos_Tr3','SRF_Pmos','BND_POLayer')
        approaching_coord = tmp2[0][0][-1][0]['_XY_right']
        # Sref coord
        tmp3 = self.get_param_KJH4('SRF_Pmos_Tr3','SRF_Pmos','BND_POLayer')
        Scoord = tmp3[0][0][0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)

        if (_Tr0_GateSpacing == None):
            _Tr0_GateSpacing = _DRCObj._PolygateMinSpace2
            _Tr0_GatetoGate = 2 * _Tr0_GateSpacing + _Tr0_PMOSChannellength
        else :
            _Tr0_GatetoGate = 2 * _Tr0_GateSpacing + _Tr0_PMOSChannellength

        New_Scoord[0] = New_Scoord[0] - _Tr0_GatetoGate
        tmpXY.append(New_Scoord)
        # Define
        self._DesignParameter['SRF_Pmos_Tr3']['_XYCoordinates'] = tmpXY


        # PP layer 연장 연결
        # Define Boundary_element
        self._DesignParameter['BND_PPLayer_Extension'] = self._BoundaryElementDeclaration(      _Layer=DesignParameters._LayerMapping['PIMP'][0],
                                                                                                _Datatype=DesignParameters._LayerMapping['PIMP'][1],
                                                                                                _XWidth=None,
                                                                                                _YWidth=None,
                                                                                                _XYCoordinates=[],
                )


        # Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('SRF_Pmos_Tr0','SRF_Pmos','BND_PPLayer')

        self._DesignParameter['BND_PPLayer_Extension']['_YWidth'] = tmp1[0][0][0][0]['_Ywidth']

        # Define Boundary_element _XWidth
        tmp1 = self.get_param_KJH4('SRF_Pmos_Tr0','SRF_Pmos','BND_PPLayer')
        tmp2 = self.get_param_KJH4('SRF_Pmos_Tr3','SRF_Pmos','BND_PPLayer')

        self._DesignParameter['BND_PPLayer_Extension']['_XWidth'] = abs(tmp1[0][0][0][0]['_XY_right'][0]-tmp2[0][0][0][0]['_XY_left'][0])

        # Define coord
        # Calculate Sref XYcoord
        tmpXY = []
        # initialized Sref coordinate
        self._DesignParameter['BND_PPLayer_Extension']['_XYCoordinates'] = [[0, 0]]

        # Calculate1
        # Target_coord
        tmp1 = self.get_param_KJH4('SRF_Pmos_Tr0','SRF_Pmos','BND_PPLayer')
        target_coord = tmp1[0][0][0][0]['_XY_up_right']
        # Approaching_coord
        tmp2 = self.get_param_KJH4('BND_PPLayer_Extension')
        approaching_coord = tmp2[0][0]['_XY_up_right']
        # Sref coord
        tmp3 = self.get_param_KJH4('BND_PPLayer_Extension')
        Scoord = tmp3[0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)

        self._DesignParameter['BND_PPLayer_Extension']['_XYCoordinates'] = tmpXY





## ########################################################################################################################################################## Start_Main
if __name__ == '__main__':

    from KJH91_Projects.Project_ADC.Library_and_Engine.Private import MyInfo_YCH
    from KJH91_Projects.Project_ADC.Library_and_Engine import DRCchecker_KJH0
    import random

    for _iter in range(10):
        libname = 'Proj_A51_TIA_P0P3_v{}'.format(_iter + 38)
        cellname = 'A51_TIA_P0P3'
        _fileName = cellname + '.gds'

        _TR0_3_PMOSChannelWidth = random.randrange(3000, 10000, 1000)

        ''' Input Parameters for Layout Object '''
        InputParams = dict(

            #PMOS
            _Tr0_PMOSNumberofGate= random.randrange(2, 10, 1),
            _Tr0_PMOSChannelWidth= _TR0_3_PMOSChannelWidth,
            _Tr0_PMOSChannellength= 150,
            _Tr0_GateSpacing	= None,
            _Tr0_SDWidth			= None,
            _Tr0_XVT				= 'EG',
            _Tr0_PCCrit				= None,

            # Source_node_ViaM1M2
            _Tr0_Source_Via_TF = True,

            # Drain_node_ViaM1M2
            _Tr0_Drain_Via_TF = True,

            # POLY dummy setting
            _Tr0_PMOSDummy = True, # TF
            # if _PMOSDummy == True
            _Tr0_PMOSDummy_length = None, # None/Value
            _Tr0_PMOSDummy_placement = None, # None/'Up'/'Dn'/

            # PMOS
            _Tr3_PMOSNumberofGate= random.randrange(2, 10, 1),
            _Tr3_PMOSChannelWidth=_TR0_3_PMOSChannelWidth,
            _Tr3_PMOSChannellength=150,
            _Tr3_GateSpacing	= None,
            _Tr3_SDWidth			= None,
            _Tr3_XVT				= 'EG',
            _Tr3_PCCrit				= None,

            # Source_node_ViaM1M2
            _Tr3_Source_Via_TF = True,

            # Drain_node_ViaM1M2
            _Tr3_Drain_Via_TF = True,

            # POLY dummy setting
            _Tr3_PMOSDummy = True, # TF
            # if _PMOSDummy == True
            _Tr3_PMOSDummy_length = None, # None/Value
            _Tr3_PMOSDummy_placement = None, # None/'Up'/'Dn'/

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
        LayoutObj = _TIA_P0P3_YCH(_DesignParameter=None, _Name=cellname)
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