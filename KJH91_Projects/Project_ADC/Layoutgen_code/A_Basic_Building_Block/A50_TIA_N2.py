from KJH91_Projects.Project_ADC.Library_and_Engine import StickDiagram_KJH1, DesignParameters
from KJH91_Projects.Project_ADC.Library_and_Engine import DRC_EGFET

import numpy as np
import copy
import math

from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A02_ViaStack_KJH2
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A03_NmosWithDummy_KJH4_YCH_TIA
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A02_ViaStack_KJH2_YCH

## ########################################################################################################################################################## Class_HEADER
class _TIA_N2_YCH(StickDiagram_KJH1._StickDiagram_KJH):

    ## Define input_parameters for Design calculation
    _ParametersForDesignCalculation = dict(

        #NMOS
        _Tr2_NMOSNumberofGate	= None,
        _Tr2_NMOSChannelWidth	= None,
        _Tr2_NMOSChannellength	= None,
        _Tr2_GateSpacing		= None,
        _Tr2_SDWidth			= None,
        _Tr2_XVT				= None,
        _Tr2_PCCrit				= None,

        #Source_node_ViaM1M2
        _Tr2_Source_Via_TF = None,

        #Drain_node_ViaM1M2
        _Tr2_Drain_Via_TF = None,

        #POLY dummy setting
        _Tr2_NMOSDummy = None, #TF
            #if _NMOSDummy == True
        _Tr2_NMOSDummy_length = None, #None/Value
        _Tr2_NMOSDummy_placement = None #None/Up/Dn/
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
                                  _Tr2_GateSpacing	= None,
                                  _Tr2_SDWidth			= None,
                                  _Tr2_XVT				= None,
                                  _Tr2_PCCrit				= None,

                                  # Source_node_ViaM1M2
                                  _Tr2_Source_Via_TF = None,

                                  # Drain_node_ViaM1M2
                                  _Tr2_Drain_Via_TF = None,

                                  # POLY dummy setting
                                  _Tr2_NMOSDummy = None, # TF
                                  # if _PMOSDummy == True
                                  _Tr2_NMOSDummy_length = None, # None/Value
                                  _Tr2_NMOSDummy_placement = None, # None/Up/Dn/

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

        ## SREF Generation

            ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_nmos_power_v2._NMOS_POWER._ParametersForDesignCalculation)
        _Caculation_Parameters = copy.deepcopy(A03_NmosWithDummy_KJH4_YCH_TIA._NmosWithDummy_KJH3._ParametersForDesignCalculation)
        ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
        _Caculation_Parameters['_NMOSNumberofGate'] = _Tr2_NMOSNumberofGate
        _Caculation_Parameters['_NMOSChannelWidth'] = _Tr2_NMOSChannelWidth
        _Caculation_Parameters['_NMOSChannellength'] = _Tr2_NMOSChannellength
        _Caculation_Parameters['_GateSpacing'] = _Tr2_GateSpacing
        _Caculation_Parameters['_SDWidth'] = _Tr2_SDWidth
        _Caculation_Parameters['_XVT'] = _Tr2_XVT
        _Caculation_Parameters['_PCCrit'] = _Tr2_PCCrit
        _Caculation_Parameters['_Source_Via_TF'] = _Tr2_Source_Via_TF
        _Caculation_Parameters['_Drain_Via_TF'] = _Tr2_Drain_Via_TF
        _Caculation_Parameters['_NMOSDummy'] = _Tr2_NMOSDummy
        _Caculation_Parameters['_NMOSDummy_length'] = _Tr2_NMOSDummy_length
        _Caculation_Parameters['_NMOSDummy_placement'] = _Tr2_NMOSDummy_placement

        ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_Nmos'] = self._SrefElementDeclaration(
            _DesignObj=A03_NmosWithDummy_KJH4_YCH_TIA._NmosWithDummy_KJH3(_DesignParameter=None,_Name='{}:SRF_Nmos'.format(_Name)))[0]

        ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_Nmos']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Nmos']['_Angle'] = 0

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Nmos']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Nmos']['_XYCoordinates'] = [[0, 0]]

        ## ################################################################################################################### POLY_Layer_Gate
        # Define Boundary_element
        self._DesignParameter['BND_POLayer_Hrz_Gate'] = self._BoundaryElementDeclaration(
                                                                                            _Layer=DesignParameters._LayerMapping['POLY'][0],
                                                                                            _Datatype=DesignParameters._LayerMapping['POLY'][1],
                                                                                            _XWidth=None,
                                                                                            _YWidth=None,
                                                                                            _XYCoordinates=[],
        )

        # Define Boundary_element _YWidth
        self._DesignParameter['BND_POLayer_Hrz_Gate']['_YWidth'] = 71

        # Define Boundary_element _XWidth
        tmp = self.get_param_KJH4('SRF_Nmos', 'BND_POLayer')

        self._DesignParameter['BND_POLayer_Hrz_Gate']['_XWidth'] = abs(tmp[0][-1][0]['_XY_right'][0] - tmp[0][0][0]['_XY_left'][0])

        # Calculate Sref XYcoord
        # initialize coordinate
        self._DesignParameter['BND_POLayer_Hrz_Gate']['_XYCoordinates'] = [[0, 0]]
        tmpXY = []

        # Calculate
        # Target_coord
        tmp1 = self.get_param_KJH4('SRF_Nmos', 'BND_POLayer')
        target_coord = tmp1[0][0][0]['_XY_down_left']
        # Approaching_coord
        tmp2 = self.get_param_KJH4('BND_POLayer_Hrz_Gate')
        approaching_coord = tmp2[0][0]['_XY_up_left']
        # Sref coord
        tmp3 = self.get_param_KJH4('BND_POLayer_Hrz_Gate')
        Scoord = tmp3[0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        # Define
        self._DesignParameter['BND_POLayer_Hrz_Gate']['_XYCoordinates'] = tmpXY


## ################################################################################################################### Metal1_Drain_connect
        # Define Boundary_element
        self._DesignParameter['BND_Met1Layer_Drain_connect'] = self._BoundaryElementDeclaration(
                                                                                                _Layer=DesignParameters._LayerMapping['METAL1'][0],
                                                                                                _Datatype=DesignParameters._LayerMapping['METAL1'][1],
                                                                                                _XWidth=None,
                                                                                                _YWidth=None,
                                                                                                _XYCoordinates=[],
        )

        # Define Boundary_element _YWidth
        self._DesignParameter['BND_Met1Layer_Drain_connect']['_YWidth'] = 142

        # Define Boundary_element _XWidth
        tmp1 = self.get_param_KJH4('SRF_Nmos', 'BND_Met1Layer_Drain')
        tmp2 = self.get_param_KJH4('BND_POLayer_Hrz_Gate')
        self._DesignParameter['BND_Met1Layer_Drain_connect']['_XWidth'] = abs(tmp1[0][-1][0]['_XY_right'][0]-tmp2[0][0]['_XY_left'][0])

        # Calculate Sref XYcoord
        # initialize coordinate
        self._DesignParameter['BND_Met1Layer_Drain_connect']['_XYCoordinates'] = [[0, 0]]

        tmpXY = []

        # Calculate
        # Target_coord
        tmp1 = self.get_param_KJH4('BND_POLayer_Hrz_Gate')
        target_coord = tmp1[0][0]['_XY_up_left']
        # Approaching_coord
        tmp2 = self.get_param_KJH4('BND_Met1Layer_Drain_connect')
        approaching_coord = tmp2[0][0]['_XY_up_left']
        # Sref coord
        tmp3 = self.get_param_KJH4('BND_Met1Layer_Drain_connect')
        Scoord = tmp3[0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        # Define
        self._DesignParameter['BND_Met1Layer_Drain_connect']['_XYCoordinates'] = tmpXY

## ################################################################################################################### Metal1_Drain_extension
        # Define Boundary_element
        self._DesignParameter['BND_Met1Layer_Drain_extension'] = self._BoundaryElementDeclaration(
                                                                                                _Layer=DesignParameters._LayerMapping['METAL1'][0],
                                                                                                _Datatype=DesignParameters._LayerMapping['METAL1'][1],
                                                                                                _XWidth=None,
                                                                                                _YWidth=None,
                                                                                                _XYCoordinates=[],
        )

        # Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('SRF_Nmos', 'BND_Met1Layer_Drain')
        tmp2 = self.get_param_KJH4('BND_Met1Layer_Drain_connect')
        self._DesignParameter['BND_Met1Layer_Drain_extension']['_YWidth'] = abs(tmp1[0][0][0]['_XY_cent'][1] - tmp2[0][0]['_XY_down'][1])

        # Define Boundary_element _XWidth
        tmp1 = self.get_param_KJH4('SRF_Nmos', 'BND_Met1Layer_Drain')
        self._DesignParameter['BND_Met1Layer_Drain_extension']['_XWidth'] = tmp1[0][0][0]['_Xwidth']

        # Calculate Sref XYcoord
        # initialize coordinate
        self._DesignParameter['BND_Met1Layer_Drain_extension']['_XYCoordinates'] = [[0, 0]]

        tmpXY = []
        Draincount = self.get_param_KJH4('SRF_Nmos', 'BND_Met1Layer_Drain')

        for i in range(0, len(Draincount[0])):
            # Calculate
            # Target_coord
            tmp1 = self.get_param_KJH4('SRF_Nmos', 'BND_Met1Layer_Drain')
            target_coord = tmp1[0][i][0]['_XY_cent']
            # Approaching_coord
            tmp2 = self.get_param_KJH4('BND_Met1Layer_Drain_extension')
            approaching_coord = tmp2[0][0]['_XY_up']
            # Sref coord
            tmp3 = self.get_param_KJH4('BND_Met1Layer_Drain_extension')
            Scoord = tmp3[0][0]['_XY_origin']
            # Cal
            New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
            tmpXY.append(New_Scoord)

        # Define
        self._DesignParameter['BND_Met1Layer_Drain_extension']['_XYCoordinates'] = tmpXY

## ################################################################################################################### POLY_Metal1 CA
## ################################################################################################################### _Gate_ViaM0M1
        # Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH2_YCH._ViaStack_KJH2._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 0
        _Caculation_Parameters['_Layer2'] = 1
        _Caculation_Parameters['_COX'] = None
        _Caculation_Parameters['_COY'] = None

        # Sref ViaX declaration
        self._DesignParameter['SRF_Gate_ViaM0M1'] = self._SrefElementDeclaration(
            _DesignObj=A02_ViaStack_KJH2_YCH._ViaStack_KJH2(_DesignParameter=None,_Name='{}:SRF_Gate_ViaM0M1'.format(_Name)))[0]

        # Define Sref Relection
        self._DesignParameter['SRF_Gate_ViaM0M1']['_Reflect'] = [0, 0, 0]

        # Define Sref Angle
        self._DesignParameter['SRF_Gate_ViaM0M1']['_Angle'] = 0

        # Calculate _COY
        _Caculation_Parameters['_COY'] = 1

        # Calculate _COX
        # Calculate Number of V1
        tmp = self.get_param_KJH4('BND_POLayer_Hrz_Gate')
        M1_Xwidth = tmp[0][0]['_Xwidth']
        Num_V1 = int((M1_Xwidth - 2 * 4) / (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace)) + 0
        # Define Num of V1
        if Num_V1 < 2:
            _Caculation_Parameters['_COX'] = 2
        else:
            _Caculation_Parameters['_COX'] = Num_V1


        # Generate Metal(x), Metal(x+1) and C0(Viax) layer
        self._DesignParameter['SRF_Gate_ViaM0M1']['_DesignObj']._CalculateDesignParameterXmin(**_Caculation_Parameters)

        # Calculate Sref XYcoord
        tmpXY = []
        # initialized Sref coordinate
        self._DesignParameter['SRF_Gate_ViaM0M1']['_XYCoordinates'] = [[0, 0]]


        # For num of M1 in Nmos

        tmpXY = []

        # Calculate
        # Target_coord
        tmp1 = self.get_param_KJH4('BND_POLayer_Hrz_Gate')
        target_coord = tmp1[0][0]['_XY_cent']
        # Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_Gate_ViaM0M1', 'SRF_ViaM0M1', 'BND_POLayer')
        approaching_coord = tmp2[0][0][0][0]['_XY_cent']
        # Sref coord
        tmp3 = self.get_param_KJH4('SRF_Gate_ViaM0M1')
        Scoord = tmp3[0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)


        self._DesignParameter['SRF_Gate_ViaM0M1']['_XYCoordinates'] = tmpXY

        ## ################################################################################################################### gate Metal1 extension
        # Define Boundary_element
        self._DesignParameter['BND_Metal1Layer_Connect_Gate_extension'] = self._BoundaryElementDeclaration(
                                                                                                        _Layer=DesignParameters._LayerMapping['METAL1'][0],
                                                                                                        _Datatype=DesignParameters._LayerMapping['METAL1'][1],
                                                                                                        _XWidth=None,
                                                                                                        _YWidth=None,
                                                                                                        _XYCoordinates=[],
        )

        tmp1 = self.get_param_KJH4('BND_Met1Layer_Drain_connect')
        tmp2 = self.get_param_KJH4('SRF_Gate_ViaM0M1', 'SRF_ViaM0M1', 'BND_Met1Layer')

        # Define Boundary_element _YWidth
        self._DesignParameter['BND_Metal1Layer_Connect_Gate_extension']['_YWidth'] = abs(tmp2[0][0][0][0]['_XY_up'][1] - tmp1[0][0]['_XY_down'][1])

        # Define Boundary_element _XWidth
        self._DesignParameter['BND_Metal1Layer_Connect_Gate_extension']['_XWidth'] = tmp1[0][0]['_Xwidth']

        # Calculate Sref XYcoord
        # initialize coordinate
        self._DesignParameter['BND_Metal1Layer_Connect_Gate_extension']['_XYCoordinates'] = [[0, 0]]
        tmpXY = []

        # Calculate
        # Target_coord
        tmp1 = self.get_param_KJH4('BND_Met1Layer_Drain_connect')
        target_coord = tmp1[0][0]['_XY_down_left']
        # Approaching_coord
        tmp2 = self.get_param_KJH4('BND_Metal1Layer_Connect_Gate_extension')
        approaching_coord = tmp2[0][0]['_XY_down_left']
        # Sref coord
        tmp3 = self.get_param_KJH4('BND_Metal1Layer_Connect_Gate_extension')
        Scoord = tmp3[0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        # Define
        self._DesignParameter['BND_Metal1Layer_Connect_Gate_extension']['_XYCoordinates'] = tmpXY




## ########################################################################################################################################################## Start_Main
if __name__ == '__main__':

    from TIA_Proj_YCH.Library_and_Engine.Private import MyInfo_YCH
    from TIA_Proj_YCH.Library_and_Engine import DRCchecker_KJH0

    libname = 'Proj_A50_TIA_N2_v4'
    cellname = 'A50_TIA_N2'
    _fileName = cellname + '.gds'

    ''' Input Parameters for Layout Object '''
    InputParams = dict(

        #NMOS Tr0
        _Tr2_NMOSNumberofGate	= 5,
        _Tr2_NMOSChannelWidth	= 3000,
        _Tr2_NMOSChannellength	= 150,
        _Tr2_GateSpacing		= None,
        _Tr2_SDWidth			= None,
        _Tr2_XVT				= 'EG',
        _Tr2_PCCrit				= None,

        #Source_node_ViaM1M2
        _Tr2_Source_Via_TF = True,

        #Drain_node_ViaM1M2
        _Tr2_Drain_Via_TF = True,

        #POLY dummy setting
        _Tr2_NMOSDummy = True, #TF
            #if _PMOSDummy == True
        _Tr2_NMOSDummy_length = None, #None/Value
        _Tr2_NMOSDummy_placement = None, #None/'Up'/'Dn'/


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
    LayoutObj = _TIA_N2_YCH(_DesignParameter=None, _Name=cellname)
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

