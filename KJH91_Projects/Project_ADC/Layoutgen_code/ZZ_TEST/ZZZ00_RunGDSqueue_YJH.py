import time
from KJH91_Projects.Project_ADC.Library_and_Engine import DesignParameters


############################################################################################################################################################ START MAIN
def RunGDSqueue(libname, cellname, InputParams):
    if __name__ == '__main__':

        ''' Check Time'''
        start_time = time.time()

        from KJH91_Projects.Project_ADC.Library_and_Engine.Private import MyInfo_YJH
        from KJH91_Projects.Project_ADC.Library_and_Engine import DRCchecker_KJH0
        from KJH91_Projects.Project_ADC.Layoutgen_code.H02_CDACWDriver import H02_01_CDACWDriver_Fold1

        '''Mode_DRCCHECK '''
        Mode_DRCCheck = False
        Num_DRCCheck = 1

        for ii in range(0, Num_DRCCheck if Mode_DRCCheck else 1):
            if Mode_DRCCheck:
                ''' Input Parameters for Layout Object '''
            else:
                pass

        ''' Generate Layout Object '''
        ## Gen Object:
        LayoutObj = H02_01_CDACWDriver_Fold1._CDACWDriverFold1(_DesignParameter=None, _Name=cellname)
        LayoutObj._CalculateDesignParameter(**InputParams)
        LayoutObj._UpdateDesignParameter2GDSStructure(_DesignParameterInDictionary=LayoutObj._DesignParameter)
        testStreamFile = open('./{}'.format(_fileName), 'wb')
        tmp = LayoutObj._CreateGDSStream(LayoutObj._DesignParameter['_GDSFile']['_GDSFile'])
        tmp.write_binary_gds_stream(testStreamFile)
        testStreamFile.close()

        print('###############      Sending to FTP Server...      ##################')
        My = MyInfo_YJH.USER(DesignParameters._Technology)
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

        ''' Check Time'''
        elapsed_time = time.time() - start_time
        m, s = divmod(elapsed_time, 60)
        h, m = divmod(m, 60)

        print('#############################      Finished      ################################')



libname = 'Proj_ADC_H02_CDAC_Driver_v5'
cellname = 'H02_00_CDACWDriver_Fold1_3bit_4test'
_fileName = cellname + '.gds'
InputParams = dict(
    _NumOfBits=3,

    # # Element CDAC
    _CDAC_LayoutOption=[2,3,4,5,6],
    _CDAC_ShieldingLayer=1,  # Poly:0, M1:1, M2:2 ...
    _CDAC_MetalWidth=50,
    _CDAC_MetalLength=1414,
    _CDAC_MetalSpacing=50,

    # #Unit Cap
    _CDAC_NumOfElement=2,

    # # Shielding & Top Connect node
    _CDAC_ConnectLength=400,
    _CDAC_ExtendLength=400,

    # # CommonCentroid With Driving node
    _CDAC_CapArrayWDrivingNodeDistance=0,  # DRC Rule
    _CDAC_DriveNodeDistance=400,  #
    _CDAC_YWidth_Bottom_Hrz=50,

        # Driver(Inverter) NMOS
    _Driver_NMOS_NumberofGate = 1,  # number
    _Driver_NMOS_ChannelWidth = 340,  # number
    _Driver_NMOS_Channellength = 30,  # number
    _Driver_NMOS_GateSpacing = None,  # None/number
    _Driver_NMOS_SDWidth = None,  # None/number
    _Driver_NMOS_XVT = 'SLVT',  # 'XVT' ex)SLVT LVT RVT HVT
    _Driver_NMOS_PCCrit = None,  # None/True

        # Source_node_ViaM1M2
    _Driver_NMOS_Source_Via_TF = True,  # True/False

        # Drain_node_ViaM1M2
    _Driver_NMOS_Drain_Via_TF = None,  # True/False

        # POLY dummy setting
    _Driver_NMOS_Dummy = True,  # TF
        # if _PMOSDummy == True
    _Driver_NMOS_Dummy_length = None,  # None/Value
    _Driver_NMOS_Dummy_placement = None,  # None/'Up'/'Dn'/l

    # Driver(Inverter) PMOS
    _Driver_PMOS_NumberofGate = 1,  # number
    _Driver_PMOS_ChannelWidth=900,  # number
    _Driver_PMOS_Channellength=30,  # number
    _Driver_PMOS_GateSpacing=None,  # None/number
    _Driver_PMOS_SDWidth=None,  # None/number
    _Driver_PMOS_XVT='SLVT',  # 'XVT' ex)SLVT LVT RVT HVT
    _Driver_PMOS_PCCrit=None,  # None/True

    # Source_node_ViaM1M2
    _Driver_PMOS_Source_Via_TF=None,  # True/False

    # Drain_node_ViaM1M2
    _Driver_PMOS_Drain_Via_TF=None,  # True/False

    # POLY dummy setting
    _Driver_PMOS_Dummy=True,  # TF
    # if _PMOSDummy == True
    _Driver_PMOS_Dummy_length=None,  # None/Value
    _Driver_PMOS_Dummy_placement=None,  # None/'Up'/'Dn'/
)
RunGDSqueue(libname, cellname, InputParams)
# ============================================================================================================================================ #
# ============================================================================================================================================ #
libname1 = 'Proj_ADC_H02_CDAC_Driver_v5'
cellname1 = 'H02_00_CDACWDriver_Fold1_4bit_4test'
_fileName1 = cellname1 + '.gds'
InputParams1 = dict(
    _NumOfBits=4,

    # # Element CDAC
    _CDAC_LayoutOption=[2,3,4,5,6],
    _CDAC_ShieldingLayer=1,  # Poly:0, M1:1, M2:2 ...
    _CDAC_MetalWidth=50,
    _CDAC_MetalLength=1414,
    _CDAC_MetalSpacing=50,

    # #Unit Cap
    _CDAC_NumOfElement=2,

    # # Shielding & Top Connect node
    _CDAC_ConnectLength=400,
    _CDAC_ExtendLength=400,

    # # CommonCentroid With Driving node
    _CDAC_CapArrayWDrivingNodeDistance=0,  # DRC Rule
    _CDAC_DriveNodeDistance=400,  #
    _CDAC_YWidth_Bottom_Hrz=50,

        # Driver(Inverter) NMOS
    _Driver_NMOS_NumberofGate = 1,  # number
    _Driver_NMOS_ChannelWidth = 340,  # number
    _Driver_NMOS_Channellength = 30,  # number
    _Driver_NMOS_GateSpacing = None,  # None/number
    _Driver_NMOS_SDWidth = None,  # None/number
    _Driver_NMOS_XVT = 'SLVT',  # 'XVT' ex)SLVT LVT RVT HVT
    _Driver_NMOS_PCCrit = None,  # None/True

        # Source_node_ViaM1M2
    _Driver_NMOS_Source_Via_TF = True,  # True/False

        # Drain_node_ViaM1M2
    _Driver_NMOS_Drain_Via_TF = None,  # True/False

        # POLY dummy setting
    _Driver_NMOS_Dummy = True,  # TF
        # if _PMOSDummy == True
    _Driver_NMOS_Dummy_length = None,  # None/Value
    _Driver_NMOS_Dummy_placement = None,  # None/'Up'/'Dn'/l

    # Driver(Inverter) PMOS
    _Driver_PMOS_NumberofGate = 1,  # number
    _Driver_PMOS_ChannelWidth=900,  # number
    _Driver_PMOS_Channellength=30,  # number
    _Driver_PMOS_GateSpacing=None,  # None/number
    _Driver_PMOS_SDWidth=None,  # None/number
    _Driver_PMOS_XVT='SLVT',  # 'XVT' ex)SLVT LVT RVT HVT
    _Driver_PMOS_PCCrit=None,  # None/True

    # Source_node_ViaM1M2
    _Driver_PMOS_Source_Via_TF=None,  # True/False

    # Drain_node_ViaM1M2
    _Driver_PMOS_Drain_Via_TF=None,  # True/False

    # POLY dummy setting
    _Driver_PMOS_Dummy=True,  # TF
    # if _PMOSDummy == True
    _Driver_PMOS_Dummy_length=None,  # None/Value
    _Driver_PMOS_Dummy_placement=None,  # None/'Up'/'Dn'/
)
RunGDSqueue(libname1, cellname1, InputParams1)
# ============================================================================================================================================ #
# ============================================================================================================================================ #

libname2 = 'Proj_ADC_H02_CDAC_Driver_v4'
cellname2 = 'H02_00_CDACWDriver_Fold1_10bit_UCAP104fF'
_fileName2 = cellname2 + '.gds'
InputParams2 = dict(
    _NumOfBits=10,

    # # Element CDAC
    _CDAC_LayoutOption=[2,3,4,5,6],
    _CDAC_ShieldingLayer=1,  # Poly:0, M1:1, M2:2 ...
    _CDAC_MetalWidth=50,
    _CDAC_MetalLength=60000,
    _CDAC_MetalSpacing=50,

    # #Unit Cap
    _CDAC_NumOfElement=2,

    # # Shielding & Top Connect node
    _CDAC_ConnectLength=400,
    _CDAC_ExtendLength=400,

    # # CommonCentroid With Driving node
    _CDAC_CapArrayWDrivingNodeDistance=0,  # DRC Rule
    _CDAC_DriveNodeDistance=400,  #
    _CDAC_YWidth_Bottom_Hrz=50,

        # Driver(Inverter) NMOS
    _Driver_NMOS_NumberofGate = 1,  # number
    _Driver_NMOS_ChannelWidth = 340,  # number
    _Driver_NMOS_Channellength = 30,  # number
    _Driver_NMOS_GateSpacing = None,  # None/number
    _Driver_NMOS_SDWidth = None,  # None/number
    _Driver_NMOS_XVT = 'SLVT',  # 'XVT' ex)SLVT LVT RVT HVT
    _Driver_NMOS_PCCrit = None,  # None/True

        # Source_node_ViaM1M2
    _Driver_NMOS_Source_Via_TF = True,  # True/False

        # Drain_node_ViaM1M2
    _Driver_NMOS_Drain_Via_TF = None,  # True/False

        # POLY dummy setting
    _Driver_NMOS_Dummy = True,  # TF
        # if _PMOSDummy == True
    _Driver_NMOS_Dummy_length = None,  # None/Value
    _Driver_NMOS_Dummy_placement = None,  # None/'Up'/'Dn'/l

    # Driver(Inverter) PMOS
    _Driver_PMOS_NumberofGate = 1,  # number
    _Driver_PMOS_ChannelWidth=900,  # number
    _Driver_PMOS_Channellength=30,  # number
    _Driver_PMOS_GateSpacing=None,  # None/number
    _Driver_PMOS_SDWidth=None,  # None/number
    _Driver_PMOS_XVT='SLVT',  # 'XVT' ex)SLVT LVT RVT HVT
    _Driver_PMOS_PCCrit=None,  # None/True

    # Source_node_ViaM1M2
    _Driver_PMOS_Source_Via_TF=None,  # True/False

    # Drain_node_ViaM1M2
    _Driver_PMOS_Drain_Via_TF=None,  # True/False

    # POLY dummy setting
    _Driver_PMOS_Dummy=True,  # TF
    # if _PMOSDummy == True
    _Driver_PMOS_Dummy_length=None,  # None/Value
    _Driver_PMOS_Dummy_placement=None,  # None/'Up'/'Dn'/
)
RunGDSqueue(libname2, cellname2, InputParams2)

# ============================================================================================================================================ #
# ============================================================================================================================================ #
'''
libname3 = 'Proj_ADC_H02_CDAC_Driver_v4'
cellname3 = 'H02_00_CDACWDriver_Fold1_10bit_UCAP104fF'
_fileName3 = cellname3 + '.gds'
InputParams3 = dict(
    _NumOfBits=10,

    # # Element CDAC
    _CDAC_LayoutOption=[2,3,4,5,6],
    _CDAC_ShieldingLayer=1,  # Poly:0, M1:1, M2:2 ...
    _CDAC_MetalWidth=50,
    _CDAC_MetalLength=60000,
    _CDAC_MetalSpacing=50,

    # #Unit Cap
    _CDAC_NumOfElement=2,

    # # Shielding & Top Connect node
    _CDAC_ConnectLength=400,
    _CDAC_ExtendLength=400,

    # # CommonCentroid With Driving node
    _CDAC_CapArrayWDrivingNodeDistance=0,  # DRC Rule
    _CDAC_DriveNodeDistance=400,  #
    _CDAC_YWidth_Bottom_Hrz=50,

        # Driver(Inverter) NMOS
    _Driver_NMOS_NumberofGate = 1,  # number
    _Driver_NMOS_ChannelWidth = 340,  # number
    _Driver_NMOS_Channellength = 30,  # number
    _Driver_NMOS_GateSpacing = None,  # None/number
    _Driver_NMOS_SDWidth = None,  # None/number
    _Driver_NMOS_XVT = 'SLVT',  # 'XVT' ex)SLVT LVT RVT HVT
    _Driver_NMOS_PCCrit = None,  # None/True

        # Source_node_ViaM1M2
    _Driver_NMOS_Source_Via_TF = True,  # True/False

        # Drain_node_ViaM1M2
    _Driver_NMOS_Drain_Via_TF = None,  # True/False

        # POLY dummy setting
    _Driver_NMOS_Dummy = True,  # TF
        # if _PMOSDummy == True
    _Driver_NMOS_Dummy_length = None,  # None/Value
    _Driver_NMOS_Dummy_placement = None,  # None/'Up'/'Dn'/l

    # Driver(Inverter) PMOS
    _Driver_PMOS_NumberofGate = 1,  # number
    _Driver_PMOS_ChannelWidth=900,  # number
    _Driver_PMOS_Channellength=30,  # number
    _Driver_PMOS_GateSpacing=None,  # None/number
    _Driver_PMOS_SDWidth=None,  # None/number
    _Driver_PMOS_XVT='SLVT',  # 'XVT' ex)SLVT LVT RVT HVT
    _Driver_PMOS_PCCrit=None,  # None/True

    # Source_node_ViaM1M2
    _Driver_PMOS_Source_Via_TF=None,  # True/False

    # Drain_node_ViaM1M2
    _Driver_PMOS_Drain_Via_TF=None,  # True/False

    # POLY dummy setting
    _Driver_PMOS_Dummy=True,  # TF
    # if _PMOSDummy == True
    _Driver_PMOS_Dummy_length=None,  # None/Value
    _Driver_PMOS_Dummy_placement=None,  # None/'Up'/'Dn'/
)
RunGDSqueue(libname3, cellname3, InputParams3)
'''
# ============================================================================================================================================ #
# ============================================================================================================================================ #



# ============================================================================================================================================ #
# ============================================================================================================================================ #



# ============================================================================================================================================ #
# ============================================================================================================================================ #



# ============================================================================================================================================ #
# ============================================================================================================================================ #



# ============================================================================================================================================ #
# ============================================================================================================================================ #



# ============================================================================================================================================ #
# ============================================================================================================================================ #



# ============================================================================================================================================ #
# ============================================================================================================================================ #



# ============================================================================================================================================ #
# ============================================================================================================================================ #



# ============================================================================================================================================ #
# ============================================================================================================================================ #



# ============================================================================================================================================ #
# ============================================================================================================================================ #






