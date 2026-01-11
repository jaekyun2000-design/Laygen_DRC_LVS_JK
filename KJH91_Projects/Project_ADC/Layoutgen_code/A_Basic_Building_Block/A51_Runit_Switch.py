from KJH91_Projects.Project_ADC.Library_and_Engine import StickDiagram_KJH1, DesignParameters
from KJH91_Projects.Project_ADC.Library_and_Engine import DRC_EGFET

import numpy as np
import copy
import math

# from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A02_ViaStack_KJH2
# from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A03_NmosWithDummy_KJH4_YCH_TIA
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A50_opppcres_b_portVia
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A50_TG_Switch




## ########################################################################################################################################################## Class_HEADER
class _Runit_Switch(StickDiagram_KJH1._StickDiagram_KJH):

    ## Define input_parameters for Design calculation
    _ParametersForDesignCalculation = dict(
        # Res
        _ResWidth=None,
        _ResLength=None,
        _CONUMX=None,
        _CONUMY=None,
        _SeriesStripes=None,
        _ParallelStripes=None,

        ### TG NMOS PMOS
        _TG_NumberofGate=None,  # number
        _TG_NMOSChannelWidth=None,  # number
        _TG_PMOSChannelWidth=None,
        _TG_Channellength=None,  # number
        _TG_XVT			= None, # 'XVT' ex)SLVT LVT RVT HVT EG
        _INV_NumberofGate=None,
        _NMOS_Pbody_NumCont=None,
        _PMOS_Nbody_NumCont=None,
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
                                  _ResWidth=None,
                                  _ResLength=None,
                                  _CONUMX=None,
                                  _CONUMY=None,
                                  _SeriesStripes=None,
                                  _ParallelStripes=None,

                                  ### TG NMOS PMOS
                                  _TG_NumberofGate=None,  # number
                                  _TG_NMOSChannelWidth=None,  # number
                                  _TG_PMOSChannelWidth=None,
                                  _TG_Channellength=None,  # number
                                  _TG_XVT			= None, # 'XVT' ex)SLVT LVT RVT HVT EG
                                  _INV_NumberofGate=None,
                                  _NMOS_Pbody_NumCont=None,
                                  _PMOS_Nbody_NumCont=None,

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
        _Caculation_Parameters = copy.deepcopy(A50_opppcres_b_portVia._Opppcres_b._ParametersForDesignCalculation)
        ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
        _Caculation_Parameters['_ResWidth'] = _ResWidth
        _Caculation_Parameters['_ResLength'] = _ResLength
        _Caculation_Parameters['_CONUMX'] = _CONUMX
        _Caculation_Parameters['_CONUMY'] = _CONUMY
        _Caculation_Parameters['_SeriesStripes'] = _SeriesStripes
        _Caculation_Parameters['_ParallelStripes'] = _ParallelStripes
        _Caculation_Parameters['_Port1Layer'] = 4
        _Caculation_Parameters['_Port2Layer'] = 3


        ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_Res'] = self._SrefElementDeclaration(
            _DesignObj=A50_opppcres_b_portVia._Opppcres_b(_DesignParameter=None, _Name='{}:SRF_Res'.format(_Name)))[0]

        ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_Res']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Res']['_Angle'] = 0

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Res']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Res']['_XYCoordinates'] = [[0, 0]]

        ## SREF Generation
        ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_nmos_power_v2._NMOS_POWER._ParametersForDesignCalculation)
        _Caculation_Parameters = copy.deepcopy(A50_TG_Switch._TG_Switch._ParametersForDesignCalculation)
        ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
        _Caculation_Parameters['_TG_NumberofGate'] = _TG_NumberofGate
        _Caculation_Parameters['_TG_NMOSChannelWidth'] = _TG_NMOSChannelWidth
        _Caculation_Parameters['_TG_PMOSChannelWidth'] = _TG_PMOSChannelWidth
        _Caculation_Parameters['_TG_Channellength'] = _TG_Channellength
        _Caculation_Parameters['_TG_XVT'] = _TG_XVT
        _Caculation_Parameters['_INV_NumberofGate'] = _INV_NumberofGate
        _Caculation_Parameters['_NMOS_Pbody_NumCont'] = _NMOS_Pbody_NumCont
        _Caculation_Parameters['_PMOS_Nbody_NumCont'] = _PMOS_Nbody_NumCont


        ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_TG_Switch'] = self._SrefElementDeclaration(
            _DesignObj=A50_TG_Switch._TG_Switch(_DesignParameter=None, _Name='{}:SRF_TG_Switch'.format(_Name)))[0]

        ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_TG_Switch']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_TG_Switch']['_Angle'] = 0

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_TG_Switch']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_TG_Switch']['_XYCoordinates'] = [[0, 0]]

        tmpXY = []
        tmp1 = self.get_param_KJH4('SRF_Res','_PPLayer')
        target_coord = tmp1[0][0][0]['_XY_right'] + [600,0]
        tmp2 = self.get_param_KJH4('SRF_TG_Switch','BND_NWell_Ext')
        approaching_coordx = tmp2[0][0][0]['_XY_left'][0]
        tmp21 = self.get_param_KJH4('SRF_TG_Switch','SRF_Nbody','SRF_NbodyContactPhyLen','BND_Met1Layer')
        tmp22 = self.get_param_KJH4('SRF_TG_Switch','SRF_Pbody','SRF_PbodyContactPhyLen','BND_Met1Layer')
        approaching_coordy = (tmp21[0][0][0][0][0]['_XY_up'][1] + tmp22[0][0][0][0][0]['_XY_down'][1])//2
        approaching_coord = [approaching_coordx, approaching_coordy]
        tmp3 = self.get_param_KJH4('SRF_TG_Switch')
        Scoord = tmp3[0][0]['_XY_origin']
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        # Define
        self._DesignParameter['SRF_TG_Switch']['_XYCoordinates'] = tmpXY

        ###### Res - TG Met3 connection
        # Define Boundary_element
        self._DesignParameter['BND_Met3Layer_Res_TG_Conn_1'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3'][0],
            _Datatype=DesignParameters._LayerMapping['METAL3'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        tmp11 = self.get_param_KJH4('SRF_TG_Switch','BND_Metal3Layer_Hrz_PortAB')
        tmp12 = self.get_param_KJH4('SRF_Res','SRF_OutputPort2_Via','SRF_ViaM2M3','BND_Met3Layer')
        # Define Boundary_element _YWidth
        self._DesignParameter['BND_Met3Layer_Res_TG_Conn_1']['_YWidth'] = tmp11[0][1][0]['_Ywidth']

        # Define Boundary_element _XWidth
        self._DesignParameter['BND_Met3Layer_Res_TG_Conn_1']['_XWidth'] = tmp11[0][1][0]['_XY_left'][0] - tmp12[0][0][0][0][0]['_XY_left'][0]

        # Calculate Sref XYcoord
        # initialize coordinate
        self._DesignParameter['BND_Met3Layer_Res_TG_Conn_1']['_XYCoordinates'] = [[0, 0]]
        tmpXY = []

        # Calculate
        # Target_coord
        target_coord = tmp11[0][1][0]['_XY_up_left']
        # Approaching_coord
        tmp3 = self.get_param_KJH4('BND_Met3Layer_Res_TG_Conn_1')
        approaching_coord = tmp3[0][0]['_XY_up_right']
        # Sref coord
        Scoord = tmp3[0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        # Define
        self._DesignParameter['BND_Met3Layer_Res_TG_Conn_1']['_XYCoordinates'] = tmpXY

        # Define Boundary_element
        self._DesignParameter['BND_Met3Layer_Res_TG_Conn_2'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3'][0],
            _Datatype=DesignParameters._LayerMapping['METAL3'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        # Define Boundary_element _YWidth
        self._DesignParameter['BND_Met3Layer_Res_TG_Conn_2']['_YWidth'] = abs(tmp12[0][0][0][0][0]['_XY_up_left'][1] - tmp11[0][1][0]['_XY_up_left'][1])

        # Define Boundary_element _XWidth
        self._DesignParameter['BND_Met3Layer_Res_TG_Conn_2']['_XWidth'] = tmp12[0][0][0][0][0]['_Xwidth']

        # Calculate Sref XYcoord
        # initialize coordinate
        self._DesignParameter['BND_Met3Layer_Res_TG_Conn_2']['_XYCoordinates'] = [[0, 0]]
        tmpXY = []

        # Calculate
        # Target_coord
        tmp2 = self.get_param_KJH4('BND_Met3Layer_Res_TG_Conn_1')
        if (tmp12[0][0][0][0][0]['_XY_up_left'][1] - tmp11[0][1][0]['_XY_up_left'][1]) > 0:
            target_coord = tmp2[0][0]['_XY_up_left']
        else:
            target_coord = tmp12[0][0][0][0][0]['_XY_up_left']

        # Approaching_coord
        tmp3 = self.get_param_KJH4('BND_Met3Layer_Res_TG_Conn_2')
        approaching_coord = tmp3[0][0]['_XY_down_left']
        # Sref coord
        Scoord = tmp3[0][0]['_XY_origin']
        # Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        # Define
        self._DesignParameter['BND_Met3Layer_Res_TG_Conn_2']['_XYCoordinates'] = tmpXY


## ########################################################################################################################################################## Start_Main
if __name__ == '__main__':

    from KJH91_Projects.Project_ADC.Library_and_Engine.Private import MyInfo_AJH
    from KJH91_Projects.Project_ADC.Library_and_Engine import DRCchecker_KJH0

    libname = 'Proj_A51_Runit_Switch'
    cellname = 'A51_Runit_Switch'
    _fileName = cellname + '.gds'

    ''' Input Parameters for Layout Object '''
    InputParams = dict(
        _ResWidth=160,
        _ResLength=1300,
        _CONUMX=None,
        _CONUMY=None,
        _SeriesStripes=50,
        _ParallelStripes=1,

        _TG_NumberofGate=100,  # number
        _TG_NMOSChannelWidth=500,  # number
        _TG_PMOSChannelWidth=1000,
        _TG_Channellength=150,  # number
        _TG_XVT			='EG', # 'XVT' ex)SLVT LVT RVT HVT EG
        _INV_NumberofGate       =2,
        _NMOS_Pbody_NumCont     =2,
        _PMOS_Nbody_NumCont     =2,
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
    LayoutObj = _Runit_Switch(_DesignParameter=None, _Name=cellname)
    LayoutObj._CalculateDesignParameter(**InputParams)
    LayoutObj._UpdateDesignParameter2GDSStructure(_DesignParameterInDictionary=LayoutObj._DesignParameter)
    testStreamFile = open('./{}'.format(_fileName), 'wb')
    tmp = LayoutObj._CreateGDSStream(LayoutObj._DesignParameter['_GDSFile']['_GDSFile'])
    tmp.write_binary_gds_stream(testStreamFile)
    testStreamFile.close()

    print('###############      Sending to FTP Server...      ##################')
    My = MyInfo_AJH.USER(DesignParameters._Technology)
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
