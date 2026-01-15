## Import Basic Modules
    ## Engine
#from KJH91_Projects.Project_ADC.Layoutgen_code.E00_Slicer import StickDiagram
from KJH91_Projects.Project_ADC.Library_and_Engine import StickDiagram_KJH1
from KJH91_Projects.Project_ADC.Layoutgen_code.E00_Slicer import DesignParameters
from KJH91_Projects.Project_ADC.Layoutgen_code.E00_Slicer import DRC

    ## Library
import copy
import time

    ## KJH91 Basic Building Blocks
from KJH91_Projects.Project_ADC.Layoutgen_code.E00_Slicer import Slicer
from KJH91_Projects.Project_ADC.Layoutgen_code.E02_Comparator_And_Fixed import E02_03_And_KJH0
from KJH91_Projects.Project_ADC.Layoutgen_code.E01_ComparatorWtLatch_Fixed import E01_04_SRLatch
from KJH91_Projects.Project_ADC.Layoutgen_code.E01_ComparatorWtLatch_Fixed import E01_01_Buffer
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A02_ViaStack_KJH3
from KJH91_Projects.Project_ADC.Layoutgen_code.E01_ComparatorWtLatch_Fixed import E01_00_Inverter

############################################################################################################################################################ Class_HEADER
class _StrongArmWtSRLatch(StickDiagram_KJH1._StickDiagram_KJH):

    # XYcoord as center coordination
    #_XYcoordAsCent = dict(_XYcoordAsCent=1)

    # Initially Defined design_parameter
    _ParametersForDesignCalculation = dict(
## StrongARM Latch
    # Common
    _SALatch_ChannelLength=30,  # random.randrange(30, 60, 2),  # 30
    _SALatch_XVT='HVT',

    # PMOS
    _SALatch_CLKinputPMOSFinger1=1,  #PMOS Reset Sw1 # random.randint(1, 15),  # 6
    _SALatch_CLKinputPMOSFinger2=1,  #PMOS Reset Sw2 # random.randint(1, 15),  # 3
    _SALatch_PMOSFinger=1,  		  #PMOS Latch	  # random.randint(1, 15),  # 3
    _SALatch_PMOSChannelWidth=1000,  #All PMOS width # random.randrange(200, 1050, 2),  # 500

    # NMOS
    _SALatch_DATAinputNMOSFinger=3,  #NMOS Input Tr # random.randint(3, 15),  # 12
    _SALatch_NMOSFinger=2,  		  #NMOS at Latch # random.randint(1, 15),  # 2
    _SALatch_CLKinputNMOSFinger=1,  #NMOS Tail # random.randint(1, 15),  # 8
    _SALatch_NMOSChannelWidth=330,  #Nmos width # random.randrange(200, 1050, 2),  # 500
    _SALatch_CLKinputNMOSChannelWidth=200,  # random.randrange(200, 1050, 2),  # 800

## StrongArmOutBuffer and SRLatch
    ## Common
        # XVT
        _SAOutBufAndSRLatch_XVT='SLVT',
        # Body
        _SAOutBufAndSRLatch_NMOS_Pbody_XvtTop2Pbody=None,  # Number/None(Minimum)
        _SAOutBufAndSRLatch_PMOS_Nbody_Xvtdown2Nbody=None,  # Number/None(Minimum)
        # Height
        _SAOutBufAndSRLatch_PMOSXvt2NMOSXvt=1800,  # number
    ## StronArm Output Buffer
        ## Inverter1
                #Nmos
            _SAOutBuf_Buf_Inv1_NMOS_NumberofGate          = 1,        # Number
            _SAOutBuf_Buf_Inv1_NMOS_ChannelWidth          = 400,      # Number
            _SAOutBuf_Buf_Inv1_NMOS_ChannelLength         = 30,       # Number
                #Pmos
            _SAOutBuf_Buf_Inv1_PMOS_NumberofGate          = 1,        # Number
            _SAOutBuf_Buf_Inv1_PMOS_ChannelWidth          = 800,      # Number
            _SAOutBuf_Buf_Inv1_PMOS_ChannelLength         = 30,       # Number
        ## Inverter2
                #Nmos
            _SAOutBuf_Buf_Inv2_NMOS_NumberofGate          = 1,        # Number
            _SAOutBuf_Buf_Inv2_NMOS_ChannelWidth          = 400,      # Number
            _SAOutBuf_Buf_Inv2_NMOS_ChannelLength         = 30,       # Number
                #Pmos
            _SAOutBuf_Buf_Inv2_PMOS_NumberofGate          = 1,        # Number
            _SAOutBuf_Buf_Inv2_PMOS_ChannelWidth          = 800,      # Number
            _SAOutBuf_Buf_Inv2_PMOS_ChannelLength         = 30,       # Number
    ## SRLatch
        ## Nand(Set,Rst same)
            # NmosA
            _SRLatch_Nand_NMOSA_NumberofGate=1,  # Number
            _SRLatch_Nand_NMOSA_ChannelWidth=100,  # Number
            _SRLatch_Nand_NMOSA_ChannelLength=30,  # Number
            # NMOSB
            _SRLatch_Nand_NMOSB_NumberofGate=2,  # Number
            _SRLatch_Nand_NMOSB_ChannelWidth=750,  # Number
            _SRLatch_Nand_NMOSB_ChannelLength=30,  # Number
            # PMOSA
            _SRLatch_Nand_PMOSA_NumberofGate=2,  # Number
            _SRLatch_Nand_PMOSA_ChannelWidth=100,  # Number
            _SRLatch_Nand_PMOSA_ChannelLength=30,  # Number
            # PMOSB
            _SRLatch_Nand_PMOSB_NumberofGate=1,  # Number
            _SRLatch_Nand_PMOSB_ChannelWidth=750,  # Number
            _SRLatch_Nand_PMOSB_ChannelLength=30,  # Number
# ## Comp clock Gen Logic: Clk_Samp Inv, Clk_Source Inv, AND Gate, CompClockBuff
    ## Common
        # XVT
        _CompClkLogic_XVT='SLVT',
        # Body
        _CompClkLogic_NMOS_Pbody_XvtTop2Pbody=None,  # Number/None(Minimum)
        _CompClkLogic_PMOS_Nbody_Xvtdown2Nbody=None,  # Number/None(Minimum)
        # Height
        _CompClkLogic_PMOSXvt2NMOSXvt=1800,  # number
    ## StronArm Output Buffer
        ## Inverter1(pre)
                #Nmos
            _CompClkLogic_Buf_Inv1_NMOS_NumberofGate          = 2,        # Number
            _CompClkLogic_Buf_Inv1_NMOS_ChannelWidth          = 400,      # Number
            _CompClkLogic_Buf_Inv1_NMOS_ChannelLength         = 30,       # Number
                #Pmos
            _CompClkLogic_Buf_Inv1_PMOS_NumberofGate          = 2,        # Number
            _CompClkLogic_Buf_Inv1_PMOS_ChannelWidth          = 800,      # Number
            _CompClkLogic_Buf_Inv1_PMOS_ChannelLength         = 30,       # Number
        ## Inverter2
                #Nmos
            _CompClkLogic_Buf_Inv2_NMOS_NumberofGate          = 4,        # Number
            _CompClkLogic_Buf_Inv2_NMOS_ChannelWidth          = 400,      # Number
            _CompClkLogic_Buf_Inv2_NMOS_ChannelLength         = 30,       # Number
                #Pmos
            _CompClkLogic_Buf_Inv2_PMOS_NumberofGate          = 4,        # Number
            _CompClkLogic_Buf_Inv2_PMOS_ChannelWidth          = 800,      # Number
            _CompClkLogic_Buf_Inv2_PMOS_ChannelLength         = 30,       # Number
    ## AND
        ## Nand
            # NmosA
            _CompClkLogic_Nand_NMOSA_NumberofGate=1,  # Number
            _CompClkLogic_Nand_NMOSA_ChannelWidth=100,  # Number
            _CompClkLogic_Nand_NMOSA_ChannelLength=30,  # Number
            # NMOSB
            _CompClkLogic_Nand_NMOSB_NumberofGate=2,  # Number
            _CompClkLogic_Nand_NMOSB_ChannelWidth=750,  # Number
            _CompClkLogic_Nand_NMOSB_ChannelLength=30,  # Number
            # PMOSA
            _CompClkLogic_Nand_PMOSA_NumberofGate=1,  # Number
            _CompClkLogic_Nand_PMOSA_ChannelWidth=300,  # Number
            _CompClkLogic_Nand_PMOSA_ChannelLength=30,  # Number
            # PMOSB
            _CompClkLogic_Nand_PMOSB_NumberofGate=3,  # Number
            _CompClkLogic_Nand_PMOSB_ChannelWidth=750,  # Number
            _CompClkLogic_Nand_PMOSB_ChannelLength=30,  # Number
        ## Inverter
            # Nmos
            _CompClkLogic_Inv_NMOS_NumberofGate=1,  # Number
            _CompClkLogic_Inv_NMOS_ChannelWidth=100,  # Number
            _CompClkLogic_Inv_NMOS_ChannelLength=30,  # Number
            # Pmos
            _CompClkLogic_Inv_PMOS_NumberofGate=1,  # Number
            _CompClkLogic_Inv_PMOS_ChannelWidth=200,  # Number
            _CompClkLogic_Inv_PMOS_ChannelLength=30,  # Number
    ## Clk_Source Inv
            #Nmos
        _CompClkLogic_ClkSrc_NMOS_NumberofGate          = 1,        # Number
        _CompClkLogic_ClkSrc_NMOS_ChannelWidth          = 400,      # Number
        _CompClkLogic_ClkSrc_NMOS_ChannelLength         = 30,       # Number
            #Pmos
        _CompClkLogic_ClkSrc_PMOS_NumberofGate          = 1,        # Number
        _CompClkLogic_ClkSrc_PMOS_ChannelWidth          = 800,      # Number
        _CompClkLogic_ClkSrc_PMOS_ChannelLength         = 30,       # Number
    ## Clk_Samp Inv
            #Nmos
        _CompClkLogic_ClkSmp_NMOS_NumberofGate          = 1,        # Number
        _CompClkLogic_ClkSmp_NMOS_ChannelWidth          = 400,      # Number
        _CompClkLogic_ClkSmp_NMOS_ChannelLength         = 30,       # Number
            #Pmos
        _CompClkLogic_ClkSmp_PMOS_NumberofGate          = 1,        # Number
        _CompClkLogic_ClkSmp_PMOS_ChannelWidth          = 800,      # Number
        _CompClkLogic_ClkSmp_PMOS_ChannelLength         = 30,       # Number
    )

    def __init__(self, _DesignParameter=None, _Name=None):
        if _DesignParameter != None:
            self._DesignParameter = _DesignParameter
        else:
            self._DesignParameter = dict(
                _Name=self._NameDeclaration(_Name=_Name),
                _GDSFile=self._GDSObjDeclaration(_GDSFile=None),
                _XYcoordAsCent=dict(_XYcoordAsCent=0),
            )

    ##########################################################################################################################^^^^^^^^^^^^^^^^^^^^^
    def _CalculateDesignParameter(self,
## StrongARM Latch
    # Common
    _SALatch_ChannelLength=30,  # random.randrange(30, 60, 2),  # 30
    _SALatch_XVT='HVT',

    # PMOS
    _SALatch_CLKinputPMOSFinger1=1,  #PMOS Reset Sw1 # random.randint(1, 15),  # 6
    _SALatch_CLKinputPMOSFinger2=1,  #PMOS Reset Sw2 # random.randint(1, 15),  # 3
    _SALatch_PMOSFinger=1,  		  #PMOS Latch	  # random.randint(1, 15),  # 3
    _SALatch_PMOSChannelWidth=1000,  #All PMOS width # random.randrange(200, 1050, 2),  # 500

    # NMOS
    _SALatch_DATAinputNMOSFinger=3,  #NMOS Input Tr # random.randint(3, 15),  # 12
    _SALatch_NMOSFinger=2,  		  #NMOS at Latch # random.randint(1, 15),  # 2
    _SALatch_CLKinputNMOSFinger=1,  #NMOS Tail # random.randint(1, 15),  # 8
    _SALatch_NMOSChannelWidth=330,  #Nmos width # random.randrange(200, 1050, 2),  # 500
    _SALatch_CLKinputNMOSChannelWidth=200,  # random.randrange(200, 1050, 2),  # 800

## StrongArmOutBuffer and SRLatch
    ## Common
        # XVT
        _SAOutBufAndSRLatch_XVT='SLVT',
        # Body
        _SAOutBufAndSRLatch_NMOS_Pbody_XvtTop2Pbody=None,  # Number/None(Minimum)
        _SAOutBufAndSRLatch_PMOS_Nbody_Xvtdown2Nbody=None,  # Number/None(Minimum)
        # Height
        _SAOutBufAndSRLatch_PMOSXvt2NMOSXvt=1800,  # number
    ## StronArm Output Buffer
        ## Inverter1
                #Nmos
            _SAOutBuf_Buf_Inv1_NMOS_NumberofGate          = 1,        # Number
            _SAOutBuf_Buf_Inv1_NMOS_ChannelWidth          = 400,      # Number
            _SAOutBuf_Buf_Inv1_NMOS_ChannelLength         = 30,       # Number
                #Pmos
            _SAOutBuf_Buf_Inv1_PMOS_NumberofGate          = 1,        # Number
            _SAOutBuf_Buf_Inv1_PMOS_ChannelWidth          = 800,      # Number
            _SAOutBuf_Buf_Inv1_PMOS_ChannelLength         = 30,       # Number
        ## Inverter2
                #Nmos
            _SAOutBuf_Buf_Inv2_NMOS_NumberofGate          = 1,        # Number
            _SAOutBuf_Buf_Inv2_NMOS_ChannelWidth          = 400,      # Number
            _SAOutBuf_Buf_Inv2_NMOS_ChannelLength         = 30,       # Number
                #Pmos
            _SAOutBuf_Buf_Inv2_PMOS_NumberofGate          = 1,        # Number
            _SAOutBuf_Buf_Inv2_PMOS_ChannelWidth          = 800,      # Number
            _SAOutBuf_Buf_Inv2_PMOS_ChannelLength         = 30,       # Number
    ## SRLatch
        ## Nand(Set,Rst same)
            # NmosA
            _SRLatch_Nand_NMOSA_NumberofGate=1,  # Number
            _SRLatch_Nand_NMOSA_ChannelWidth=100,  # Number
            _SRLatch_Nand_NMOSA_ChannelLength=30,  # Number
            # NMOSB
            _SRLatch_Nand_NMOSB_NumberofGate=2,  # Number
            _SRLatch_Nand_NMOSB_ChannelWidth=750,  # Number
            _SRLatch_Nand_NMOSB_ChannelLength=30,  # Number
            # PMOSA
            _SRLatch_Nand_PMOSA_NumberofGate=2,  # Number
            _SRLatch_Nand_PMOSA_ChannelWidth=100,  # Number
            _SRLatch_Nand_PMOSA_ChannelLength=30,  # Number
            # PMOSB
            _SRLatch_Nand_PMOSB_NumberofGate=1,  # Number
            _SRLatch_Nand_PMOSB_ChannelWidth=750,  # Number
            _SRLatch_Nand_PMOSB_ChannelLength=30,  # Number
# ## Comp clock Gen Logic: Clk_Samp Inv, Clk_Source Inv, AND Gate, CompClockBuff
    ## Common
        # XVT
        _CompClkLogic_XVT='SLVT',
        # Body
        _CompClkLogic_NMOS_Pbody_XvtTop2Pbody=None,  # Number/None(Minimum)
        _CompClkLogic_PMOS_Nbody_Xvtdown2Nbody=None,  # Number/None(Minimum)
        # Height
        _CompClkLogic_PMOSXvt2NMOSXvt=1800,  # number
    ## StronArm Output Buffer
        ## Inverter1(pre)
                #Nmos
            _CompClkLogic_Buf_Inv1_NMOS_NumberofGate          = 2,        # Number
            _CompClkLogic_Buf_Inv1_NMOS_ChannelWidth          = 400,      # Number
            _CompClkLogic_Buf_Inv1_NMOS_ChannelLength         = 30,       # Number
                #Pmos
            _CompClkLogic_Buf_Inv1_PMOS_NumberofGate          = 2,        # Number
            _CompClkLogic_Buf_Inv1_PMOS_ChannelWidth          = 800,      # Number
            _CompClkLogic_Buf_Inv1_PMOS_ChannelLength         = 30,       # Number
        ## Inverter2
                #Nmos
            _CompClkLogic_Buf_Inv2_NMOS_NumberofGate          = 4,        # Number
            _CompClkLogic_Buf_Inv2_NMOS_ChannelWidth          = 400,      # Number
            _CompClkLogic_Buf_Inv2_NMOS_ChannelLength         = 30,       # Number
                #Pmos
            _CompClkLogic_Buf_Inv2_PMOS_NumberofGate          = 4,        # Number
            _CompClkLogic_Buf_Inv2_PMOS_ChannelWidth          = 800,      # Number
            _CompClkLogic_Buf_Inv2_PMOS_ChannelLength         = 30,       # Number
    ## AND
        ## Nand
            # NmosA
            _CompClkLogic_Nand_NMOSA_NumberofGate=1,  # Number
            _CompClkLogic_Nand_NMOSA_ChannelWidth=100,  # Number
            _CompClkLogic_Nand_NMOSA_ChannelLength=30,  # Number
            # NMOSB
            _CompClkLogic_Nand_NMOSB_NumberofGate=2,  # Number
            _CompClkLogic_Nand_NMOSB_ChannelWidth=750,  # Number
            _CompClkLogic_Nand_NMOSB_ChannelLength=30,  # Number
            # PMOSA
            _CompClkLogic_Nand_PMOSA_NumberofGate=1,  # Number
            _CompClkLogic_Nand_PMOSA_ChannelWidth=300,  # Number
            _CompClkLogic_Nand_PMOSA_ChannelLength=30,  # Number
            # PMOSB
            _CompClkLogic_Nand_PMOSB_NumberofGate=3,  # Number
            _CompClkLogic_Nand_PMOSB_ChannelWidth=750,  # Number
            _CompClkLogic_Nand_PMOSB_ChannelLength=30,  # Number
        ## Inverter
            # Nmos
            _CompClkLogic_Inv_NMOS_NumberofGate=1,  # Number
            _CompClkLogic_Inv_NMOS_ChannelWidth=100,  # Number
            _CompClkLogic_Inv_NMOS_ChannelLength=30,  # Number
            # Pmos
            _CompClkLogic_Inv_PMOS_NumberofGate=1,  # Number
            _CompClkLogic_Inv_PMOS_ChannelWidth=200,  # Number
            _CompClkLogic_Inv_PMOS_ChannelLength=30,  # Number
    ## Clk_Source Inv
            #Nmos
        _CompClkLogic_ClkSrc_NMOS_NumberofGate          = 1,        # Number
        _CompClkLogic_ClkSrc_NMOS_ChannelWidth          = 400,      # Number
        _CompClkLogic_ClkSrc_NMOS_ChannelLength         = 30,       # Number
            #Pmos
        _CompClkLogic_ClkSrc_PMOS_NumberofGate          = 1,        # Number
        _CompClkLogic_ClkSrc_PMOS_ChannelWidth          = 800,      # Number
        _CompClkLogic_ClkSrc_PMOS_ChannelLength         = 30,       # Number
    ## Clk_Samp Inv
            #Nmos
        _CompClkLogic_ClkSmp_NMOS_NumberofGate          = 1,        # Number
        _CompClkLogic_ClkSmp_NMOS_ChannelWidth          = 400,      # Number
        _CompClkLogic_ClkSmp_NMOS_ChannelLength         = 30,       # Number
            #Pmos
        _CompClkLogic_ClkSmp_PMOS_NumberofGate          = 1,        # Number
        _CompClkLogic_ClkSmp_PMOS_ChannelWidth          = 800,      # Number
        _CompClkLogic_ClkSmp_PMOS_ChannelLength         = 30,       # Number
                                  ):


        ################################################################################################################################################## Class_HEADER: Pre Defined Parameter Before Calculation
        # Load DRC library
        _DRCobj = DRC.DRC()

        # Define _name
        _Name = self._DesignParameter['_Name']['_Name']
        # Predefined variable

        E01_05_StrongArmWtSRLatch_start_time = time.time()
        ## CALCULATION START
        print('##############################')
        print('##     Calculation_Start    ##')
        print('##############################')
        ##################################################################################################################################### Pre-Cal for BufX, Bufy, SR Latch. xvt2body
        ######################################################################################### Pre-Cal for BufX, Bufy, SR Latch. xvt2body: Buf Gen
        #################### Buffers Generation
        ########### SA Output Node X -> Buffer X Generation
        _Caculation_Parameters = copy.deepcopy(E01_01_Buffer._Buffer._ParametersForDesignCalculation)
        ## Buffer
            ## Common
                # XVT
        _Caculation_Parameters['_Buf_XVT'] = _SAOutBufAndSRLatch_XVT
                # Body
        _Caculation_Parameters['_Buf_NMOS_Pbody_XvtTop2Pbody'] = _SAOutBufAndSRLatch_NMOS_Pbody_XvtTop2Pbody
        _Caculation_Parameters['_Buf_PMOS_Nbody_Xvtdown2Nbody'] = _SAOutBufAndSRLatch_PMOS_Nbody_Xvtdown2Nbody
                # Height
        _Caculation_Parameters['_Buf_PMOSXvt2NMOSXvt'] = _SAOutBufAndSRLatch_PMOSXvt2NMOSXvt
            ## Inverter1
                # Nmos
        _Caculation_Parameters['_Buf_Inv1_NMOS_NumberofGate'] = _SAOutBuf_Buf_Inv1_NMOS_NumberofGate
        _Caculation_Parameters['_Buf_Inv1_NMOS_ChannelWidth'] = _SAOutBuf_Buf_Inv1_NMOS_ChannelWidth
        _Caculation_Parameters['_Buf_Inv1_NMOS_ChannelLength'] = _SAOutBuf_Buf_Inv1_NMOS_ChannelLength
                # Pmos
        _Caculation_Parameters['_Buf_Inv1_PMOS_NumberofGate'] = _SAOutBuf_Buf_Inv1_PMOS_NumberofGate
        _Caculation_Parameters['_Buf_Inv1_PMOS_ChannelWidth'] = _SAOutBuf_Buf_Inv1_PMOS_ChannelWidth
        _Caculation_Parameters['_Buf_Inv1_PMOS_ChannelLength'] = _SAOutBuf_Buf_Inv1_PMOS_ChannelLength
            ## Inverter2
                # Nmos
        _Caculation_Parameters['_Buf_Inv2_NMOS_NumberofGate'] = _SAOutBuf_Buf_Inv2_NMOS_NumberofGate
        _Caculation_Parameters['_Buf_Inv2_NMOS_ChannelWidth'] = _SAOutBuf_Buf_Inv2_NMOS_ChannelWidth
        _Caculation_Parameters['_Buf_Inv2_NMOS_ChannelLength'] = _SAOutBuf_Buf_Inv2_NMOS_ChannelLength
                # Pmos
        _Caculation_Parameters['_Buf_Inv2_PMOS_NumberofGate'] = _SAOutBuf_Buf_Inv2_PMOS_NumberofGate
        _Caculation_Parameters['_Buf_Inv2_PMOS_ChannelWidth'] = _SAOutBuf_Buf_Inv2_PMOS_ChannelWidth
        _Caculation_Parameters['_Buf_Inv2_PMOS_ChannelLength'] = _SAOutBuf_Buf_Inv2_PMOS_ChannelLength

        ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_BufferX'] = self._SrefElementDeclaration(_DesignObj=E01_01_Buffer._Buffer(_DesignParameter=None,_Name='{}:SRF_BufferX'.format(_Name)))[0]

        ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_BufferX']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_BufferX']['_Angle'] = 0

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_BufferX']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_BufferX']['_XYCoordinates'] = [[0, 0]]

        ######################################################################################### Pre-Cal for BufX, Bufy, SR Latch. xvt2body: SR Latch Gen
        ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ###
        ## NAND wt input 'R' SREF Generation
        ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_PMOS_power_v2._PMOS_POWER._ParametersForDesignCalculation)
        _Calculation_Parameters = copy.deepcopy(E01_04_SRLatch._SRLatch._ParametersForDesignCalculation)
        ## Define Calculation_Parameters ex) _Caculation_Parameters['_PMOSPOWER_PbodyContact_1_Length']  = _PMOSPOWER_PbodyContact_1_Length

        _Calculation_Parameters['_SRLatch_XVT'] = _SAOutBufAndSRLatch_XVT

        _Calculation_Parameters['_SRLatch_NMOSAB_Pbody_XvtTop2Pbody'] = _SAOutBufAndSRLatch_NMOS_Pbody_XvtTop2Pbody
        _Calculation_Parameters['_SRLatch_PMOSAB_Nbody_Xvtdown2Nbody'] = _SAOutBufAndSRLatch_PMOS_Nbody_Xvtdown2Nbody

        _Calculation_Parameters['_SRLatch_PMOSXvt2NMOSXvt'] = _SAOutBufAndSRLatch_PMOSXvt2NMOSXvt

        _Calculation_Parameters['_SRLatch_Nand_NMOSA_NumberofGate'] = _SRLatch_Nand_NMOSA_NumberofGate
        _Calculation_Parameters['_SRLatch_Nand_NMOSA_ChannelWidth'] = _SRLatch_Nand_NMOSA_ChannelWidth
        _Calculation_Parameters['_SRLatch_Nand_NMOSA_ChannelLength'] = _SRLatch_Nand_NMOSA_ChannelLength

        _Calculation_Parameters['_SRLatch_Nand_NMOSB_NumberofGate'] = _SRLatch_Nand_NMOSB_NumberofGate
        _Calculation_Parameters['_SRLatch_Nand_NMOSB_ChannelWidth'] = _SRLatch_Nand_NMOSB_ChannelWidth
        _Calculation_Parameters['_SRLatch_Nand_NMOSB_ChannelLength'] = _SRLatch_Nand_NMOSB_ChannelLength

        _Calculation_Parameters['_SRLatch_Nand_PMOSA_NumberofGate'] = _SRLatch_Nand_PMOSA_NumberofGate
        _Calculation_Parameters['_SRLatch_Nand_PMOSA_ChannelWidth'] = _SRLatch_Nand_PMOSA_ChannelWidth
        _Calculation_Parameters['_SRLatch_Nand_PMOSA_ChannelLength'] = _SRLatch_Nand_PMOSA_ChannelLength

        _Calculation_Parameters['_SRLatch_Nand_PMOSB_NumberofGate'] = _SRLatch_Nand_PMOSB_NumberofGate
        _Calculation_Parameters['_SRLatch_Nand_PMOSB_ChannelWidth'] = _SRLatch_Nand_PMOSB_ChannelWidth
        _Calculation_Parameters['_SRLatch_Nand_PMOSB_ChannelLength'] = _SRLatch_Nand_PMOSB_ChannelLength

        ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_SRLatch'] = self._SrefElementDeclaration(
            _DesignObj=E01_04_SRLatch._SRLatch(_DesignParameter=None, _Name='{}:SRF_SRLatch'.format(_Name)))[0]

        ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_SRLatch']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_SRLatch']['_Angle'] = 0

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_SRLatch']['_DesignObj']._CalculateDesignParameter(**_Calculation_Parameters)

        ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_SRLatch']['_XYCoordinates'] = [[0, 0]]

        ######################################################################################### Pre-Cal for BufX, Bufy, SR Latch. xvt2body: Cal Xvt2body
        tmp1 = self.get_param_KJH4('SRF_BufferX','SRF_Inverter1','SRF_NMOS','BND_{}Layer'.format(_SAOutBufAndSRLatch_XVT))
        tmp2 = self.get_param_KJH4('SRF_BufferX','SRF_Inverter1','SRF_Pbody','SRF_PbodyContactPhyLen','BND_Met1Layer')
        BufX_Xvttop2Pbody = abs(tmp1[0][0][0][0][0]['_XY_up'][1] - tmp2[0][0][0][0][0][0]['_XY_up'][1])
        tmp3 = self.get_param_KJH4('SRF_BufferX','SRF_Inverter1','SRF_PMOS','BND_{}Layer'.format(_SAOutBufAndSRLatch_XVT))
        tmp4 = self.get_param_KJH4('SRF_BufferX','SRF_Inverter1','SRF_Nbody','SRF_NbodyContactPhyLen','BND_Met1Layer')
        BufX_Xvtdown2Nbody = abs(tmp4[0][0][0][0][0][0]['_XY_down'][1] - tmp3[0][0][0][0][0]['_XY_down'][1])

        tmp5 = self.get_param_KJH4('SRF_SRLatch','SRF_NANDS','SRF_Pulldown','SRF_NMOSA','BND_{}Layer'.format(_SAOutBufAndSRLatch_XVT))
        tmp6 = self.get_param_KJH4('SRF_SRLatch','SRF_NANDS','SRF_Pbody','SRF_PbodyContactPhyLen','BND_Met1Layer')
        SRLatch_Xvttop2Pbody = abs(tmp5[0][0][0][0][0][0]['_XY_up'][1] - tmp6[0][0][0][0][0][0]['_XY_up'][1])
        tmp7 = self.get_param_KJH4('SRF_SRLatch','SRF_NANDS','SRF_Pullup','SRF_PMOSA','BND_{}Layer'.format(_SAOutBufAndSRLatch_XVT))
        tmp8 = self.get_param_KJH4('SRF_SRLatch','SRF_NANDS','SRF_Nbody','SRF_NbodyContactPhyLen','BND_Met1Layer')
        SRLatch_Xvtdown2Nbody = abs(tmp8[0][0][0][0][0][0]['_XY_down'][1] - tmp7[0][0][0][0][0][0]['_XY_down'][1])

        tmp1_Xvttop2Pbody = max(BufX_Xvttop2Pbody,SRLatch_Xvttop2Pbody)
        tmp1_Xvtdown2Nbody = max(BufX_Xvtdown2Nbody,SRLatch_Xvtdown2Nbody)

        #####################################################################################################################################
            ## SREF Generation
                ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_nmos_power_v2._NMOS_POWER._ParametersForDesignCalculation)
        _Calculation_Parameters = copy.deepcopy(Slicer._Slicer._ParametersForDesignCalculation)
                ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
        ## StrongARM Latch
            # Common
        _Calculation_Parameters['_ChannelLength']           = _SALatch_ChannelLength
        _Calculation_Parameters['_XVT']                     = _SALatch_XVT
            # PMOS
        _Calculation_Parameters['_CLKinputPMOSFinger1']     = _SALatch_CLKinputPMOSFinger1
        _Calculation_Parameters['_CLKinputPMOSFinger2']     = _SALatch_CLKinputPMOSFinger2
        _Calculation_Parameters['_PMOSFinger']              = _SALatch_PMOSFinger
        _Calculation_Parameters['_PMOSChannelWidth']        = _SALatch_PMOSChannelWidth
            # NMOS
        _Calculation_Parameters['_DATAinputNMOSFinger']     = _SALatch_DATAinputNMOSFinger
        _Calculation_Parameters['_NMOSFinger']              = _SALatch_NMOSFinger
        _Calculation_Parameters['_CLKinputNMOSFinger']      = _SALatch_CLKinputNMOSFinger
        _Calculation_Parameters['_NMOSChannelWidth']        = _SALatch_NMOSChannelWidth
        _Calculation_Parameters['_CLKinputNMOSChannelWidth']= _SALatch_CLKinputNMOSChannelWidth
            # Common(Fixed)
        _Calculation_Parameters['_Dummy']                   = True
        _Calculation_Parameters['_GuardringWidth']          = 400
        _Calculation_Parameters['_Guardring']               = True
        _Calculation_Parameters['_SlicerGuardringWidth']    = 400
        _Calculation_Parameters['_SlicerGuardring']         = None
        _Calculation_Parameters['_NumSupplyCOY']            = None
        _Calculation_Parameters['_NumSupplyCOX']            = None
        _Calculation_Parameters['_SupplyMet1XWidth']        = None
        _Calculation_Parameters['_SupplyMet1YWidth']        = None
        _Calculation_Parameters['_VDD2VSSHeight']           = None
        _Calculation_Parameters['_NumVIAPoly2Met1COX']      = None
        _Calculation_Parameters['_NumVIAPoly2Met1COY']      = None
        _Calculation_Parameters['_NumVIAMet12COX']          = None
        _Calculation_Parameters['_NumVIAMet12COY']          = None
        _Calculation_Parameters['_PowerLine']               = False

                ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_Slicer'] = self._SrefElementDeclaration(_DesignObj=Slicer._Slicer(_DesignParameter=None, _Name='{}:SRF_Slicer'.format(_Name)))[0]

                ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_Slicer']['_Reflect'] = [0, 0, 0]

                ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Slicer']['_Angle'] = 0

                ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Slicer']['_DesignObj']._CalculateDesignParameter(**_Calculation_Parameters)

                ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Slicer']['_XYCoordinates'] = [[0, 0]]

        #####################################################################################################################################
        ######## SAOutput 'X' Boundary Element Generation
            ## Boundary_element Generation
                ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_SAOutputNodeX_Hrz_M3'] = self._BoundaryElementDeclaration(
        _Layer=DesignParameters._LayerMapping['METAL3'][0],
        _Datatype=DesignParameters._LayerMapping['METAL3'][1],
        _XWidth=None,
        _YWidth=None,
        _XYCoordinates=[],
        )
                ## Define Boundary_element _YWidth
        BND_SAOutput_Hrz_M3_pathwidth = 50
        self._DesignParameter['BND_SAOutputNodeX_Hrz_M3']['_YWidth'] = BND_SAOutput_Hrz_M3_pathwidth

                ## Define Boundary_element _XWidth
        self._DesignParameter['SRF_Slicer']['_DesignObj']._DesignParameter['_VIAPMOSMet23forRouting']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_Slicer']['_DesignObj']._DesignParameter['_VIAPMOSMet23forRouting']['_Angle'] = 0

        tmp1 = self.get_param_KJH3('SRF_Slicer','_VIAPMOSMet23forRouting','_Met3Layer')
        self._DesignParameter['BND_SAOutputNodeX_Hrz_M3']['_XWidth'] = 10000

                ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_SAOutputNodeX_Hrz_M3']['_XYCoordinates'] = [[0, 0]]

                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## Calculate
                            ## Target_coord: _XY_type1
        target_coord = tmp1[0][0][0][0]['_XY_down_left']
                            ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_SAOutputNodeX_Hrz_M3')
        approaching_coord = tmp2[0][0]['_XY_up_left']
                            ## Sref coord
        tmp3 = self.get_param_KJH4('BND_SAOutputNodeX_Hrz_M3')
        Scoord = tmp3[0][0]['_XY_origin']
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                            ## Define coordinates
        self._DesignParameter['BND_SAOutputNodeX_Hrz_M3']['_XYCoordinates'] = tmpXY

        #####################################################################################################################################
        ######## SAOutput 'Y' Boundary Element Generation
            ## Boundary_element Generation
                ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_SAOutputNodeY_Hrz_M3'] = self._BoundaryElementDeclaration(
        _Layer=DesignParameters._LayerMapping['METAL3'][0],
        _Datatype=DesignParameters._LayerMapping['METAL3'][1],
        _XWidth=None,
        _YWidth=None,
        _XYCoordinates=[],
        )
                ## Define Boundary_element _YWidth
        self._DesignParameter['BND_SAOutputNodeY_Hrz_M3']['_YWidth'] = BND_SAOutput_Hrz_M3_pathwidth

                ## Define Boundary_element _XWidth
        self._DesignParameter['SRF_Slicer']['_DesignObj']._DesignParameter['_VIANMOSMet34forRouting']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_Slicer']['_DesignObj']._DesignParameter['_VIANMOSMet34forRouting']['_Angle'] = 0

        tmp1 = self.get_param_KJH3('SRF_Slicer','_VIANMOSMet34forRouting','_Met3Layer')
        # tmp2 = self.get_param_KJH4('SRF_SRLatch','SRF_InputS_ViaM1M3','SRF_ViaM1M2', 'BND_Met1Layer')
        # self._DesignParameter['BND_SAOutputNodeY_Hrz_M3']['_XWidth'] = abs(tmp1[0][0][0][0]['_XY_left'][0] - tmp2[0][0][0][0][0]['_XY_right'][0])
        self._DesignParameter['BND_SAOutputNodeY_Hrz_M3']['_XWidth'] = 10000
                ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_SAOutputNodeY_Hrz_M3']['_XYCoordinates'] = [[0, 0]]

                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## Calculate
                            ## Target_coord: _XY_type1
        target_coord = tmp1[0][0][0][0]['_XY_up_left']
                            ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_SAOutputNodeY_Hrz_M3')
        approaching_coord = tmp2[0][0]['_XY_down_left']
                            ## Sref coord
        tmp3 = self.get_param_KJH4('BND_SAOutputNodeY_Hrz_M3')
        Scoord = tmp3[0][0]['_XY_origin']
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                            ## Define coordinates
        self._DesignParameter['BND_SAOutputNodeY_Hrz_M3']['_XYCoordinates'] = tmpXY

        #####################################################################################################################################
        # save routing point
        SAOutputX_YcentCoord = self.get_param_KJH4('BND_SAOutputNodeX_Hrz_M3')[0][0]['_XY_cent'][1]
        SAOutputY_YcentCoord = self.get_param_KJH4('BND_SAOutputNodeY_Hrz_M3')[0][0]['_XY_cent'][1]

        #####################################################################################################################################
        #################### Buffers Generation
        ########### SA Output Node X -> Buffer X Generation
        _Caculation_Parameters = copy.deepcopy(E01_01_Buffer._Buffer._ParametersForDesignCalculation)
        ## Buffer
            ## Common
                # XVT
        _Caculation_Parameters['_Buf_XVT'] = _SAOutBufAndSRLatch_XVT
                # Body
        _Caculation_Parameters['_Buf_NMOS_Pbody_XvtTop2Pbody'] = tmp1_Xvttop2Pbody
        _Caculation_Parameters['_Buf_PMOS_Nbody_Xvtdown2Nbody'] = tmp1_Xvtdown2Nbody
                # Height
        _Caculation_Parameters['_Buf_PMOSXvt2NMOSXvt'] = _SAOutBufAndSRLatch_PMOSXvt2NMOSXvt
            ## Inverter1
                # Nmos
        _Caculation_Parameters['_Buf_Inv1_NMOS_NumberofGate'] = _SAOutBuf_Buf_Inv1_NMOS_NumberofGate
        _Caculation_Parameters['_Buf_Inv1_NMOS_ChannelWidth'] = _SAOutBuf_Buf_Inv1_NMOS_ChannelWidth
        _Caculation_Parameters['_Buf_Inv1_NMOS_ChannelLength'] = _SAOutBuf_Buf_Inv1_NMOS_ChannelLength
                # Pmos
        _Caculation_Parameters['_Buf_Inv1_PMOS_NumberofGate'] = _SAOutBuf_Buf_Inv1_PMOS_NumberofGate
        _Caculation_Parameters['_Buf_Inv1_PMOS_ChannelWidth'] = _SAOutBuf_Buf_Inv1_PMOS_ChannelWidth
        _Caculation_Parameters['_Buf_Inv1_PMOS_ChannelLength'] = _SAOutBuf_Buf_Inv1_PMOS_ChannelLength
            ## Inverter2
                # Nmos
        _Caculation_Parameters['_Buf_Inv2_NMOS_NumberofGate'] = _SAOutBuf_Buf_Inv2_NMOS_NumberofGate
        _Caculation_Parameters['_Buf_Inv2_NMOS_ChannelWidth'] = _SAOutBuf_Buf_Inv2_NMOS_ChannelWidth
        _Caculation_Parameters['_Buf_Inv2_NMOS_ChannelLength'] = _SAOutBuf_Buf_Inv2_NMOS_ChannelLength
                # Pmos
        _Caculation_Parameters['_Buf_Inv2_PMOS_NumberofGate'] = _SAOutBuf_Buf_Inv2_PMOS_NumberofGate
        _Caculation_Parameters['_Buf_Inv2_PMOS_ChannelWidth'] = _SAOutBuf_Buf_Inv2_PMOS_ChannelWidth
        _Caculation_Parameters['_Buf_Inv2_PMOS_ChannelLength'] = _SAOutBuf_Buf_Inv2_PMOS_ChannelLength

        ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_BufferX'] = self._SrefElementDeclaration(_DesignObj=E01_01_Buffer._Buffer(_DesignParameter=None,_Name='{}:SRF_BufferX'.format(_Name)))[0]

        ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_BufferX']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_BufferX']['_Angle'] = 0

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_BufferX']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_BufferX']['_XYCoordinates'] = [[0, 0]]

        tmpXY = []
        ## Target_coord: _XY_type1
        ##X
        self._DesignParameter['SRF_Slicer']['_DesignObj']._DesignParameter['_VIAPMOSMet23forRouting']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_Slicer']['_DesignObj']._DesignParameter['_VIAPMOSMet23forRouting']['_Angle'] = 0

        tmp1x = self.get_param_KJH3('SRF_Slicer', '_GuardringVSS')
        tmpy = int((SAOutputX_YcentCoord + SAOutputY_YcentCoord) / 2)
        target_coord = [tmp1x[0][0][0]['_XY_right'][0], tmpy]

        ## Approaching_coord: _XY_type2
        tmp2x = self.get_param_KJH4('SRF_BufferX', 'SRF_Inverter1', 'SRF_Pbody', 'SRF_PbodyContactPhyLen', 'BND_Met1Layer')
        tmp2y = self.get_param_KJH4('SRF_BufferX', 'SRF_Inverter1', 'BND_Input_Vtc_M1')
        approaching_coord = [tmp2x[0][0][0][0][0][0]['_XY_left'][0], tmp2y[0][0][0][0]['_XY_cent'][1]]

        ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_BufferX')
        Scoord = tmp3[0][0]['_XY_origin']

        SpaceBtwSAandBuffer = 500
        Scoord[0] = Scoord[0] + SpaceBtwSAandBuffer

        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define coordinates
        self._DesignParameter['SRF_BufferX']['_XYCoordinates'] = tmpXY

        #####################################################################################################################################

        ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ###
        ########### SA Output Node X -> Buffer X Generation
                ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_BufferY'] = self._SrefElementDeclaration(_DesignObj=E01_01_Buffer._Buffer(_DesignParameter=None, _Name='{}:SRF_BufferY'.format(_Name)))[0]

                ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_BufferY']['_Reflect'] = [0, 0, 0]

                ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_BufferY']['_Angle'] = 0

                ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_BufferY']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

                ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_BufferY']['_XYCoordinates'] = [[0, 0]]

        tmpXY=[]
                            ## Target_coord: _XY_type1
        tmp1_1 = self.get_param_KJH4('SRF_BufferX','SRF_Inverter2','SRF_NMOS', 'BND_PODummyLayer')
        tmp1_2 = self.get_param_KJH4('SRF_BufferX','SRF_Inverter2','SRF_PMOS', 'BND_PODummyLayer')
        target_coordx = max(tmp1_1[0][0][0][-1][0]['_XY_right'][0],tmp1_2[0][0][0][-1][0]['_XY_right'][0])
        tmp1_3 = self.get_param_KJH4('SRF_BufferX','SRF_Inverter2','SRF_PMOS', 'BND_{}Layer'.format(_SAOutBufAndSRLatch_XVT))
        target_coordy  = tmp1_3[0][0][0][0][0]['_XY_down'][1]
        target_coord = [target_coordx, target_coordy]
                            ## Approaching_coord: _XY_type2
        tmp2_1 = self.get_param_KJH4('SRF_BufferY','SRF_Inverter1','SRF_NMOS', 'BND_PODummyLayer')
        tmp2_2 = self.get_param_KJH4('SRF_BufferY','SRF_Inverter1','SRF_PMOS', 'BND_PODummyLayer')
        approaching_coordx = min(tmp2_1[0][0][0][0][0]['_XY_left'][0],tmp2_2[0][0][0][0][0]['_XY_left'][0])
        tmp1_3 = self.get_param_KJH4('SRF_BufferY','SRF_Inverter1','SRF_PMOS', 'BND_{}Layer'.format(_SAOutBufAndSRLatch_XVT))
        approaching_coordy = tmp1_3[0][0][0][0][0]['_XY_down'][1]
        approaching_coord = [approaching_coordx, approaching_coordy]
                            ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_BufferY')
        Scoord = tmp3[0][0]['_XY_origin']
        Scoord[0] = Scoord[0] + 96
        # Scoord[0] = Scoord[0] + 140
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                            ## Define coordinates
        self._DesignParameter['SRF_BufferY']['_XYCoordinates'] = tmpXY

        #####################################################################################################################################
        ##### SA Output X <-> Buffer X inverter1 input Routing
        ###### Update Via Ycoord for routing
        del(self._DesignParameter['SRF_BufferX']['_DesignObj']._DesignParameter['SRF_Inv1Input_ViaM1M2'])
        del(self._DesignParameter['SRF_BufferX']['_DesignObj']._DesignParameter['SRF_Inv1Out2Inv2In_ViaM1M2'])
        del(self._DesignParameter['SRF_BufferX']['_DesignObj']._DesignParameter['BND_Inv1Out2Inv2In_Hrz_M1'])
        del(self._DesignParameter['SRF_BufferX']['_DesignObj']._DesignParameter['BND_Inv1Out2Inv2In_Hrz_M2'])
        del(self._DesignParameter['SRF_BufferX']['_DesignObj']._DesignParameter['SRF_Inv2Output_ViaM1M3'])

        ##### SA Output Y <-> Buffer Y inverter1 input Routing
        ###### Update Via Ycoord for routing
        del(self._DesignParameter['SRF_BufferY']['_DesignObj']._DesignParameter['SRF_Inv1Input_ViaM1M2'])
        del(self._DesignParameter['SRF_BufferY']['_DesignObj']._DesignParameter['SRF_Inv1Out2Inv2In_ViaM1M2'])
        del(self._DesignParameter['SRF_BufferY']['_DesignObj']._DesignParameter['BND_Inv1Out2Inv2In_Hrz_M1'])
        del(self._DesignParameter['SRF_BufferY']['_DesignObj']._DesignParameter['BND_Inv1Out2Inv2In_Hrz_M2'])
        del(self._DesignParameter['SRF_BufferY']['_DesignObj']._DesignParameter['SRF_Inv2Output_ViaM1M3'])

        #####################################################################################################################################
        ### Update BND_SAOutputNodeX_Hrz_M3 Xwidth
        tmp1 = self.get_param_KJH4('SRF_BufferX','SRF_Inverter1', 'BND_Input_Vtc_M1')
        tmp2 = self.get_param_KJH3('SRF_Slicer','_VIAPMOSMet23forRouting','_Met3Layer')
        self._DesignParameter['BND_SAOutputNodeX_Hrz_M3']['_XWidth'] = abs(tmp1[0][0][0][0]['_XY_right'][0] - tmp2[0][0][0][0]['_XY_left'][0])

        tmp1 = self.get_param_KJH4('SRF_BufferY','SRF_Inverter1', 'BND_Input_Vtc_M1')
        tmp2 = self.get_param_KJH3('SRF_Slicer','_VIANMOSMet34forRouting','_Met3Layer')
        self._DesignParameter['BND_SAOutputNodeY_Hrz_M3']['_XWidth'] = abs(tmp1[0][0][0][0]['_XY_right'][0] - tmp2[0][0][0][0]['_XY_left'][0])

        #####################################################################################################################################
        ##### SA Output X <-> Buffer X Routing
        ## Sref generation: Input S ViaM1M3
        ## Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH3._ViaStack._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 1
        _Caculation_Parameters['_Layer2'] = 3
        _Caculation_Parameters['_COX'] = 2
        _Caculation_Parameters['_COY'] = 1

        ## Sref ViaX declaration
        self._DesignParameter['SRF_BufferXInput_ViaM1M3'] = self._SrefElementDeclaration(_DesignObj=A02_ViaStack_KJH3._ViaStack(_DesignParameter=None,_Name='{}:SRF_BufferXInput_ViaM1M3'.format(_Name)))[0]

        ## Define Sref Relection
        self._DesignParameter['SRF_BufferXInput_ViaM1M3']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle
        self._DesignParameter['SRF_BufferXInput_ViaM1M3']['_Angle'] = 0

        ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
        self._DesignParameter['SRF_BufferXInput_ViaM1M3']['_DesignObj']._CalculateDesignParameterYmin(
            **_Caculation_Parameters)

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['SRF_BufferXInput_ViaM1M3']['_XYCoordinates'] = [[0, 0]]
        ## Calculate
        ## Target_coord
        tmp = self.get_param_KJH4('BND_SAOutputNodeX_Hrz_M3')
        target_coord = tmp[0][0]['_XY_up_right']
        ## Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_BufferXInput_ViaM1M3', 'SRF_ViaM1M2', 'BND_Met1Layer')
        approaching_coord = tmp2[0][0][0][0]['_XY_up_right']
        ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_BufferXInput_ViaM1M3')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Calculate
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define
        self._DesignParameter['SRF_BufferXInput_ViaM1M3']['_XYCoordinates'] = tmpXY

        #####################################################################################################################################
        ######## Buffer X Inverter1 Out -> Inverter2 In Routing
        ## Sref generation: ViaX
            ## Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH3._ViaStack._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 1
        _Caculation_Parameters['_Layer2'] = 2
        _Caculation_Parameters['_COX'] = 2
        _Caculation_Parameters['_COY'] = 1

            ## Sref ViaX declaration
        self._DesignParameter['SRF_BufX_Inv1Out2Inv2In_ViaM1M2'] = self._SrefElementDeclaration(_DesignObj=A02_ViaStack_KJH3._ViaStack(_DesignParameter=None, _Name='{}:SRF_BufX_Inv1Out2Inv2In_ViaM1M2'.format(_Name)))[0]

            ## Define Sref Relection
        self._DesignParameter['SRF_BufX_Inv1Out2Inv2In_ViaM1M2']['_Reflect'] = [0, 0, 0]

            ## Define Sref Angle
        self._DesignParameter['SRF_BufX_Inv1Out2Inv2In_ViaM1M2']['_Angle'] = 0

            ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
        self._DesignParameter['SRF_BufX_Inv1Out2Inv2In_ViaM1M2']['_DesignObj']._CalculateDesignParameterYmin(**_Caculation_Parameters)

            ## Calculate Sref XYcoord
        tmpXY = []
                ## initialized Sref coordinate
        self._DesignParameter['SRF_BufX_Inv1Out2Inv2In_ViaM1M2']['_XYCoordinates'] = [[0, 0]]
                ## Calculate
                    ## Target_coord
        tmp1x = self.get_param_KJH4('SRF_BufferX','SRF_Inverter1','BND_Out_Vtc_M2')
        tmp1y = SAOutputX_YcentCoord
        target_coord = [tmp1x[0][0][0][0]['_XY_left'][0], tmp1y]
                    ## Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_BufX_Inv1Out2Inv2In_ViaM1M2','SRF_ViaM1M2','BND_Met2Layer')
        approaching_coord = tmp2[0][0][0][0]['_XY_left']
                    ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_BufX_Inv1Out2Inv2In_ViaM1M2')
        Scoord = tmp3[0][0]['_XY_origin']
                    ## Calculate
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                ## Define
        self._DesignParameter['SRF_BufX_Inv1Out2Inv2In_ViaM1M2']['_XYCoordinates'] = tmpXY

        #####################################################################################################################################
        ## BND_Inv1Out2Inv2In_Hrz_M1 generation
            ## Boundary_element Generation
                ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_BufX_Inv1Out2Inv2In_Hrz_M1'] = self._BoundaryElementDeclaration(
        _Layer=DesignParameters._LayerMapping['METAL1'][0],
        _Datatype=DesignParameters._LayerMapping['METAL1'][1],
        _XWidth=None,
        _YWidth=None,
        _XYCoordinates=[],
        )
                ## Define Boundary_element _YWidth
        self._DesignParameter['BND_BufX_Inv1Out2Inv2In_Hrz_M1']['_YWidth'] = 50

                ## Define Boundary_element _XWidth
        tmp1 = self.get_param_KJH4('SRF_BufX_Inv1Out2Inv2In_ViaM1M2','SRF_ViaM1M2','BND_Met1Layer')
        tmp2 = self.get_param_KJH4('SRF_BufferX','SRF_Inverter2','BND_Input_Vtc_M1')
        self._DesignParameter['BND_BufX_Inv1Out2Inv2In_Hrz_M1']['_XWidth'] = abs(tmp1[0][0][0][0]['_XY_left'][0] - tmp2[0][0][0][0]['_XY_right'][0])

                ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_BufX_Inv1Out2Inv2In_Hrz_M1']['_XYCoordinates'] = [[0, 0]]

                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## Calculate
                            ## Target_coord: _XY_type1
        tmp1 = self.get_param_KJH4('SRF_BufX_Inv1Out2Inv2In_ViaM1M2','SRF_ViaM1M2','BND_Met1Layer')
        target_coord = tmp1[0][0][0][0]['_XY_left']
                            ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_BufX_Inv1Out2Inv2In_Hrz_M1')
        approaching_coord = tmp2[0][0]['_XY_left']
                            ## Sref coord
        tmp3 = self.get_param_KJH4('BND_BufX_Inv1Out2Inv2In_Hrz_M1')
        Scoord = tmp3[0][0]['_XY_origin']
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                            ## Define coordinates
        self._DesignParameter['BND_BufX_Inv1Out2Inv2In_Hrz_M1']['_XYCoordinates'] = tmpXY

        #####################################################################################################################################
        ##### Buffer Y <-> SR Latch Input Routing
        ## Sref generation: Input S ViaM1M3
        ## Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH3._ViaStack._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 2
        _Caculation_Parameters['_Layer2'] = 3
        _Caculation_Parameters['_COX'] = 1
        _Caculation_Parameters['_COY'] = 2

        ## Sref ViaX declaration
        self._DesignParameter['SRF_BufXOutput2SRInput_ViaM2M3'] = self._SrefElementDeclaration(_DesignObj=A02_ViaStack_KJH3._ViaStack(_DesignParameter=None,_Name='{}:SRF_BufXOutput2SRInput_ViaM2M3'.format(_Name)))[0]

        ## Define Sref Relection
        self._DesignParameter['SRF_BufXOutput2SRInput_ViaM2M3']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle
        self._DesignParameter['SRF_BufXOutput2SRInput_ViaM2M3']['_Angle'] = 0

        ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
        self._DesignParameter['SRF_BufXOutput2SRInput_ViaM2M3']['_DesignObj']._CalculateDesignParameterXmin(**_Caculation_Parameters)

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['SRF_BufXOutput2SRInput_ViaM2M3']['_XYCoordinates'] = [[0, 0]]
        ## Calculate
        ## Target_coord
        tmp = self.get_param_KJH4('SRF_BufferX','SRF_Inverter2','BND_Out_Vtc_M2')
        target_coord = [tmp[0][0][0][0]['_XY_right'][0], SAOutputX_YcentCoord]
        ## Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_BufXOutput2SRInput_ViaM2M3', 'SRF_ViaM2M3', 'BND_Met2Layer')
        approaching_coord = tmp2[0][0][0][0]['_XY_down_right']
        ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_BufXOutput2SRInput_ViaM2M3')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Calculate
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define
        self._DesignParameter['SRF_BufXOutput2SRInput_ViaM2M3']['_XYCoordinates'] = tmpXY

        #####################################################################################################################################
        ##### SA Output Y <-> Buffer Y Routing
        ## Sref generation: Input S ViaM1M3
        ## Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH3._ViaStack._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 1
        _Caculation_Parameters['_Layer2'] = 3
        _Caculation_Parameters['_COX'] = 1
        _Caculation_Parameters['_COY'] = 2

        ## Sref ViaX declaration
        self._DesignParameter['SRF_BufferYInput_ViaM1M3'] = self._SrefElementDeclaration(
            _DesignObj=A02_ViaStack_KJH3._ViaStack(_DesignParameter=None,
                                                   _Name='{}:SRF_BufferYInput_ViaM1M3'.format(_Name)))[0]

        ## Define Sref Relection
        self._DesignParameter['SRF_BufferYInput_ViaM1M3']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle
        self._DesignParameter['SRF_BufferYInput_ViaM1M3']['_Angle'] = 0

        ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
        self._DesignParameter['SRF_BufferYInput_ViaM1M3']['_DesignObj']._CalculateDesignParameterXmin(
            **_Caculation_Parameters)

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['SRF_BufferYInput_ViaM1M3']['_XYCoordinates'] = [[0, 0]]
        ## Calculate
        ## Target_coord
        tmp = self.get_param_KJH4('BND_SAOutputNodeY_Hrz_M3')
        target_coord = tmp[0][0]['_XY_up_right']
        ## Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_BufferYInput_ViaM1M3', 'SRF_ViaM1M2', 'BND_Met1Layer')
        approaching_coord = tmp2[0][0][0][0]['_XY_up_right']
        ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_BufferYInput_ViaM1M3')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Calculate
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define
        self._DesignParameter['SRF_BufferYInput_ViaM1M3']['_XYCoordinates'] = tmpXY

        #####################################################################################################################################

        ######## Buffer Y Inverter1 Out -> Inverter2 In Routing
        ## Sref generation: ViaX
        ## Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH3._ViaStack._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 1
        _Caculation_Parameters['_Layer2'] = 2
        _Caculation_Parameters['_COX'] = 2
        _Caculation_Parameters['_COY'] = 1

        ## Sref ViaX declaration
        self._DesignParameter['SRF_BufY_Inv1Out2Inv2In_ViaM1M2'] = self._SrefElementDeclaration(
            _DesignObj=A02_ViaStack_KJH3._ViaStack(_DesignParameter=None,
                                                   _Name='{}:SRF_BufY_Inv1Out2Inv2In_ViaM1M2'.format(_Name)))[0]

        ## Define Sref Relection
        self._DesignParameter['SRF_BufY_Inv1Out2Inv2In_ViaM1M2']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle
        self._DesignParameter['SRF_BufY_Inv1Out2Inv2In_ViaM1M2']['_Angle'] = 0

        ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
        self._DesignParameter['SRF_BufY_Inv1Out2Inv2In_ViaM1M2']['_DesignObj']._CalculateDesignParameterYmin(**_Caculation_Parameters)

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['SRF_BufY_Inv1Out2Inv2In_ViaM1M2']['_XYCoordinates'] = [[0, 0]]
        ## Calculate
        ## Target_coord
        tmp1x = self.get_param_KJH4('SRF_BufferY', 'SRF_Inverter1', 'BND_Out_Vtc_M2')
        tmp1y = SAOutputY_YcentCoord
        target_coord = [tmp1x[0][0][0][0]['_XY_left'][0], tmp1y]
        ## Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_BufY_Inv1Out2Inv2In_ViaM1M2', 'SRF_ViaM1M2', 'BND_Met2Layer')
        approaching_coord = tmp2[0][0][0][0]['_XY_left']
        ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_BufY_Inv1Out2Inv2In_ViaM1M2')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Calculate
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define
        self._DesignParameter['SRF_BufY_Inv1Out2Inv2In_ViaM1M2']['_XYCoordinates'] = tmpXY
        #####################################################################################################################################
        ## BND_Inv1Out2Inv2In_Hrz_M1 generation
        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_BufY_Inv1Out2Inv2In_Hrz_M1'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1'][0],
            _Datatype=DesignParameters._LayerMapping['METAL1'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )
        ## Define Boundary_element _YWidth
        self._DesignParameter['BND_BufY_Inv1Out2Inv2In_Hrz_M1']['_YWidth'] = 50

        ## Define Boundary_element _XWidth
        tmp1 = self.get_param_KJH4('SRF_BufY_Inv1Out2Inv2In_ViaM1M2', 'SRF_ViaM1M2', 'BND_Met1Layer')
        tmp2 = self.get_param_KJH4('SRF_BufferY', 'SRF_Inverter2', 'BND_Input_Vtc_M1')
        self._DesignParameter['BND_BufY_Inv1Out2Inv2In_Hrz_M1']['_XWidth'] = abs(
            tmp1[0][0][0][0]['_XY_left'][0] - tmp2[0][0][0][0]['_XY_right'][0])

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_BufY_Inv1Out2Inv2In_Hrz_M1']['_XYCoordinates'] = [[0, 0]]

        ## Calculate Sref XYcoord
        tmpXY = []
        ## Calculate
        ## Target_coord: _XY_type1
        tmp1 = self.get_param_KJH4('SRF_BufY_Inv1Out2Inv2In_ViaM1M2', 'SRF_ViaM1M2', 'BND_Met1Layer')
        target_coord = tmp1[0][0][0][0]['_XY_left']
        ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_BufY_Inv1Out2Inv2In_Hrz_M1')
        approaching_coord = tmp2[0][0]['_XY_left']
        ## Sref coord
        tmp3 = self.get_param_KJH4('BND_BufY_Inv1Out2Inv2In_Hrz_M1')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define coordinates
        self._DesignParameter['BND_BufY_Inv1Out2Inv2In_Hrz_M1']['_XYCoordinates'] = tmpXY
        #####################################################################################################################################
        ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ###
        ## NAND wt input 'R' SREF Generation
        ## Copy Calculation_Parameters from low-level-block ex)copy.deepcopy(B16_PMOS_power_v2._PMOS_POWER._ParametersForDesignCalculation)
        _Calculation_Parameters = copy.deepcopy(E01_04_SRLatch._SRLatch._ParametersForDesignCalculation)
        ## Define Calculation_Parameters ex) _Caculation_Parameters['_PMOSPOWER_PbodyContact_1_Length']  = _PMOSPOWER_PbodyContact_1_Length

        _Calculation_Parameters['_SRLatch_XVT'] = _SAOutBufAndSRLatch_XVT

        _Calculation_Parameters['_SRLatch_NMOSAB_Pbody_XvtTop2Pbody'] = tmp1_Xvttop2Pbody
        _Calculation_Parameters['_SRLatch_PMOSAB_Nbody_Xvtdown2Nbody'] = tmp1_Xvtdown2Nbody

        _Calculation_Parameters['_SRLatch_PMOSXvt2NMOSXvt'] = _SAOutBufAndSRLatch_PMOSXvt2NMOSXvt

        _Calculation_Parameters['_SRLatch_Nand_NMOSA_NumberofGate'] = _SRLatch_Nand_NMOSA_NumberofGate
        _Calculation_Parameters['_SRLatch_Nand_NMOSA_ChannelWidth'] = _SRLatch_Nand_NMOSA_ChannelWidth
        _Calculation_Parameters['_SRLatch_Nand_NMOSA_ChannelLength'] = _SRLatch_Nand_NMOSA_ChannelLength

        _Calculation_Parameters['_SRLatch_Nand_NMOSB_NumberofGate'] = _SRLatch_Nand_NMOSB_NumberofGate
        _Calculation_Parameters['_SRLatch_Nand_NMOSB_ChannelWidth'] = _SRLatch_Nand_NMOSB_ChannelWidth
        _Calculation_Parameters['_SRLatch_Nand_NMOSB_ChannelLength'] = _SRLatch_Nand_NMOSB_ChannelLength

        _Calculation_Parameters['_SRLatch_Nand_PMOSA_NumberofGate'] = _SRLatch_Nand_PMOSA_NumberofGate
        _Calculation_Parameters['_SRLatch_Nand_PMOSA_ChannelWidth'] = _SRLatch_Nand_PMOSA_ChannelWidth
        _Calculation_Parameters['_SRLatch_Nand_PMOSA_ChannelLength'] = _SRLatch_Nand_PMOSA_ChannelLength

        _Calculation_Parameters['_SRLatch_Nand_PMOSB_NumberofGate'] = _SRLatch_Nand_PMOSB_NumberofGate
        _Calculation_Parameters['_SRLatch_Nand_PMOSB_ChannelWidth'] = _SRLatch_Nand_PMOSB_ChannelWidth
        _Calculation_Parameters['_SRLatch_Nand_PMOSB_ChannelLength'] = _SRLatch_Nand_PMOSB_ChannelLength

        ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_SRLatch'] = self._SrefElementDeclaration(
            _DesignObj=E01_04_SRLatch._SRLatch(_DesignParameter=None, _Name='{}:SRF_SRLatch'.format(_Name)))[0]

        ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_SRLatch']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_SRLatch']['_Angle'] = 0

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_SRLatch']['_DesignObj']._CalculateDesignParameter(**_Calculation_Parameters)

        ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_SRLatch']['_XYCoordinates'] = [[0, 0]]

        tmpXY = []
        ## Target_coord: _XY_type1
                            ## Target_coord: _XY_type1
        tmp1x1 = self.get_param_KJH4('SRF_BufferY','SRF_Inverter2','SRF_NMOS', 'BND_PODummyLayer')
        tmp1x2 = self.get_param_KJH4('SRF_BufferY','SRF_Inverter2','SRF_PMOS', 'BND_PODummyLayer')
        target_coordx = max(tmp1x1[0][0][0][-1][0]['_XY_right'][0],tmp1x2[0][0][0][-1][0]['_XY_right'][0])
        tmp1y = self.get_param_KJH4('SRF_BufferY','SRF_Inverter2','SRF_Pbody','SRF_PbodyContactPhyLen','BND_Met1Layer')
        target_coord = [target_coordx, tmp1y[0][0][0][0][0][0]['_XY_down'][1]]

        ## Approaching_coord: _XY_type2
        tmp2x1 = self.get_param_KJH4('SRF_SRLatch','SRF_NANDS', 'SRF_Pulldown', 'SRF_NMOSB', 'BND_PODummyLayer')
        tmp2x2 = self.get_param_KJH4('SRF_SRLatch','SRF_NANDS', 'SRF_Pullup', 'SRF_PMOSB', 'BND_PODummyLayer')
        approaching_coordx = min(tmp2x1[0][0][0][0][-1][0]['_XY_right'][0],tmp2x2[0][0][0][0][-1][0]['_XY_right'][0])
        tmp2y = self.get_param_KJH4('SRF_SRLatch','BND_M1_NMOS_PBody_SRLatch')
        approaching_coord = [approaching_coordx, tmp2y[0][0][0]['_XY_down'][1]]

        ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_SRLatch')
        Scoord = tmp3[0][0]['_XY_origin']
        Scoord[0] = Scoord[0] + 96
        # Scoord[0] = Scoord[0] + 140

        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define coordinates
        self._DesignParameter['SRF_SRLatch']['_XYCoordinates'] = tmpXY

        #####################################################################################################################################
        ## SRF_SRLatch - BND_InputS_Hrz_M3 길이 연장 & Y 위치 조정
        tmp1 = self.get_param_KJH4('SRF_SRLatch', 'BND_InputR_Hrz_M3')
        tmp2 = self.get_param_KJH4('SRF_BufferX', 'SRF_Inverter2', 'BND_Out_Vtc_M2')
        ExtendLength = tmp1[0][0][0]['_XY_left'][0] - tmp2[0][0][0][0]['_XY_left'][0]

        tmp3 = self.get_param_KJH4('SRF_BufXOutput2SRInput_ViaM2M3','SRF_ViaM2M3','BND_Met3Layer')
        tmp4 = self.get_param_KJH4('SRF_SRLatch','SRF_InputR_ViaM1M3','SRF_ViaM2M3','BND_Met3Layer')
        # YShiftAmount = SAOutputX_YcentCoord - tmp1[0][0][0]['_XY_cent'][1]
        YShiftAmount = abs(tmp3[0][0][0][0]['_XY_up'][1] - tmp4[0][0][0][0][0]['_XY_up'][1])
        self._DesignParameter['SRF_SRLatch']['_DesignObj']._DesignParameter['BND_InputR_Hrz_M3']['_XWidth'] = self._DesignParameter['SRF_SRLatch']['_DesignObj']._DesignParameter['BND_InputR_Hrz_M3']['_XWidth'] + ExtendLength
        self._DesignParameter['SRF_SRLatch']['_DesignObj']._DesignParameter['BND_InputR_Hrz_M3']['_XYCoordinates'][0][0] = self._DesignParameter['SRF_SRLatch']['_DesignObj']._DesignParameter['BND_InputR_Hrz_M3']['_XYCoordinates'][0][0] - ExtendLength
        self._DesignParameter['SRF_SRLatch']['_DesignObj']._DesignParameter['BND_InputR_Hrz_M3']['_XYCoordinates'][0][1] = self._DesignParameter['SRF_SRLatch']['_DesignObj']._DesignParameter['BND_InputR_Hrz_M3']['_XYCoordinates'][0][1] + YShiftAmount
        self._DesignParameter['SRF_SRLatch']['_DesignObj']._DesignParameter['SRF_InputR_ViaM1M3']['_XYCoordinates'][0][1] = self._DesignParameter['SRF_SRLatch']['_DesignObj']._DesignParameter['SRF_InputR_ViaM1M3']['_XYCoordinates'][0][1] + YShiftAmount

        ##################################################################################################################################### SRF_SRLatch - BND_InputS_Hrz_M3 길이 연장 & Y 위치 조정
        ## SRF_SRLatch - BND_InputS_Hrz_M3 길이 연장 & Y 위치 조정
        tmp1 = self.get_param_KJH4('SRF_SRLatch', 'BND_InputS_Hrz_M3')
        tmp2 = self.get_param_KJH4('SRF_BufferY', 'SRF_Inverter2', 'BND_Out_Vtc_M2')
        ExtendLength = tmp1[0][0][0]['_XY_left'][0] - tmp2[0][0][0][0]['_XY_left'][0]
        # YShiftAmount = SAOutputY_YcentCoord - tmp1[0][0][0]['_XY_cent'][1]
        YShiftAmount = -49
        self._DesignParameter['SRF_SRLatch']['_DesignObj']._DesignParameter['BND_InputS_Hrz_M3']['_XWidth'] = \
        self._DesignParameter['SRF_SRLatch']['_DesignObj']._DesignParameter['BND_InputS_Hrz_M3']['_XWidth'] + ExtendLength

        self._DesignParameter['SRF_SRLatch']['_DesignObj']._DesignParameter['BND_InputS_Hrz_M3']['_XYCoordinates'][0][0] = \
        self._DesignParameter['SRF_SRLatch']['_DesignObj']._DesignParameter['BND_InputS_Hrz_M3']['_XYCoordinates'][0][0] - ExtendLength

        self._DesignParameter['SRF_SRLatch']['_DesignObj']._DesignParameter['BND_InputS_Hrz_M3']['_XYCoordinates'][0][1] = \
        self._DesignParameter['SRF_SRLatch']['_DesignObj']._DesignParameter['BND_InputS_Hrz_M3']['_XYCoordinates'][0][1] + YShiftAmount

        self._DesignParameter['SRF_SRLatch']['_DesignObj']._DesignParameter['SRF_InputS_ViaM1M3']['_XYCoordinates'][0][1] = \
        self._DesignParameter['SRF_SRLatch']['_DesignObj']._DesignParameter['SRF_InputS_ViaM1M3']['_XYCoordinates'][0][1] + YShiftAmount
        ################################################################## SRF_SRLatch - BND_InputS_Hrz_M3 길이 연장 & Y 위치 조정 : Via Gen
        self._DesignParameter['SRF_BufYOutput2SRInput_ViaM2M3'] = copy.deepcopy(self._DesignParameter['SRF_BufXOutput2SRInput_ViaM2M3'])
        self.rename_srf_prefix(self._DesignParameter['SRF_BufYOutput2SRInput_ViaM2M3'], 'SRF_BufXOutput2SRInput_ViaM2M3', 'SRF_BufYOutput2SRInput_ViaM2M3')

                ## Get_Scoord_v4.
                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['SRF_BufYOutput2SRInput_ViaM2M3']['_XYCoordinates'] = [[0, 0]]
                        ## Calculate
                            ## Target_coord: _XY_type1
        tmp1 = self.get_param_KJH4('SRF_SRLatch','BND_InputS_Hrz_M3')
        target_coord = tmp1[0][0][0]['_XY_down_left']
                            ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('SRF_BufYOutput2SRInput_ViaM2M3','SRF_ViaM2M3','BND_Met3Layer')
        approaching_coord = tmp2[0][0][0][0]['_XY_down_left']
                            ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_BufYOutput2SRInput_ViaM2M3')
        Scoord = tmp3[0][0]['_XY_origin']
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                    ## Define Coordinates
        self._DesignParameter['SRF_BufYOutput2SRInput_ViaM2M3']['_XYCoordinates'] = tmpXY

        ##################################################################################################################################### To extract Xvt2Body
        ########### SA Output Node X -> Buffer X Generation
        _Caculation_Parameters = copy.deepcopy(E01_01_Buffer._Buffer._ParametersForDesignCalculation)
        ## Buffer
        ## Common
        # XVT
        _Caculation_Parameters['_Buf_XVT'] = _CompClkLogic_XVT
        # Body
        _Caculation_Parameters['_Buf_NMOS_Pbody_XvtTop2Pbody'] = _CompClkLogic_NMOS_Pbody_XvtTop2Pbody
        _Caculation_Parameters['_Buf_PMOS_Nbody_Xvtdown2Nbody'] = _CompClkLogic_PMOS_Nbody_Xvtdown2Nbody
        # Height
        _Caculation_Parameters['_Buf_PMOSXvt2NMOSXvt'] = _CompClkLogic_PMOSXvt2NMOSXvt
        ## Inverter1
        # Nmos
        _Caculation_Parameters['_Buf_Inv1_NMOS_NumberofGate'] = _CompClkLogic_Buf_Inv1_NMOS_NumberofGate
        _Caculation_Parameters['_Buf_Inv1_NMOS_ChannelWidth'] = _CompClkLogic_Buf_Inv1_NMOS_ChannelWidth
        _Caculation_Parameters['_Buf_Inv1_NMOS_ChannelLength'] = _CompClkLogic_Buf_Inv1_NMOS_ChannelLength
        # Pmos
        _Caculation_Parameters['_Buf_Inv1_PMOS_NumberofGate'] = _CompClkLogic_Buf_Inv1_PMOS_NumberofGate
        _Caculation_Parameters['_Buf_Inv1_PMOS_ChannelWidth'] = _CompClkLogic_Buf_Inv1_PMOS_ChannelWidth
        _Caculation_Parameters['_Buf_Inv1_PMOS_ChannelLength'] = _CompClkLogic_Buf_Inv1_PMOS_ChannelLength
        ## Inverter2
        # Nmos
        _Caculation_Parameters['_Buf_Inv2_NMOS_NumberofGate'] = _CompClkLogic_Buf_Inv2_NMOS_NumberofGate
        _Caculation_Parameters['_Buf_Inv2_NMOS_ChannelWidth'] = _CompClkLogic_Buf_Inv2_NMOS_ChannelWidth
        _Caculation_Parameters['_Buf_Inv2_NMOS_ChannelLength'] = _CompClkLogic_Buf_Inv2_NMOS_ChannelLength
        # Pmos
        _Caculation_Parameters['_Buf_Inv2_PMOS_NumberofGate'] = _CompClkLogic_Buf_Inv2_PMOS_NumberofGate
        _Caculation_Parameters['_Buf_Inv2_PMOS_ChannelWidth'] = _CompClkLogic_Buf_Inv2_PMOS_ChannelWidth
        _Caculation_Parameters['_Buf_Inv2_PMOS_ChannelLength'] = _CompClkLogic_Buf_Inv2_PMOS_ChannelLength

        ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_CLKBuffer'] = self._SrefElementDeclaration(_DesignObj=E01_01_Buffer._Buffer(_DesignParameter=None, _Name='{}:SRF_CLKBuffer'.format(_Name)))[0]

        ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_CLKBuffer']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_CLKBuffer']['_Angle'] = 180

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_CLKBuffer']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_CLKBuffer']['_XYCoordinates'] = [[0, 0]]

        ### AND Gate SREF Generation
        _Caculation_Parameters = copy.deepcopy(E02_03_And_KJH0._And._ParametersForDesignCalculation)
        _Caculation_Parameters['_And_XVT'] = _CompClkLogic_XVT

        _Caculation_Parameters['_And_PMOSXvt2NMOSXvt'] = _CompClkLogic_PMOSXvt2NMOSXvt

        _Caculation_Parameters['_And_Pbody_XvtTop2Pbody'] = _CompClkLogic_NMOS_Pbody_XvtTop2Pbody
        _Caculation_Parameters['_And_Nbody_Xvtdown2Nbody'] = _CompClkLogic_PMOS_Nbody_Xvtdown2Nbody

        _Caculation_Parameters['_Nand_NMOSA_NumberofGate'] = _CompClkLogic_Nand_NMOSA_NumberofGate
        _Caculation_Parameters['_Nand_NMOSA_ChannelWidth'] = _CompClkLogic_Nand_NMOSA_ChannelWidth
        _Caculation_Parameters['_Nand_NMOSA_ChannelLength'] = _CompClkLogic_Nand_NMOSA_ChannelLength

        _Caculation_Parameters['_Nand_NMOSB_NumberofGate'] = _CompClkLogic_Nand_NMOSB_NumberofGate
        _Caculation_Parameters['_Nand_NMOSB_ChannelWidth'] = _CompClkLogic_Nand_NMOSB_ChannelWidth
        _Caculation_Parameters['_Nand_NMOSB_ChannelLength'] = _CompClkLogic_Nand_NMOSB_ChannelLength

        _Caculation_Parameters['_Nand_PMOSA_NumberofGate'] = _CompClkLogic_Nand_PMOSA_NumberofGate
        _Caculation_Parameters['_Nand_PMOSA_ChannelWidth'] = _CompClkLogic_Nand_PMOSA_ChannelWidth
        _Caculation_Parameters['_Nand_PMOSA_ChannelLength'] = _CompClkLogic_Nand_PMOSA_ChannelLength

        _Caculation_Parameters['_Nand_PMOSB_NumberofGate'] = _CompClkLogic_Nand_PMOSB_NumberofGate
        _Caculation_Parameters['_Nand_PMOSB_ChannelWidth'] = _CompClkLogic_Nand_PMOSB_ChannelWidth
        _Caculation_Parameters['_Nand_PMOSB_ChannelLength'] = _CompClkLogic_Nand_PMOSB_ChannelLength

        _Caculation_Parameters['_Inv_NMOS_NumberofGate'] = _CompClkLogic_Inv_NMOS_NumberofGate
        _Caculation_Parameters['_Inv_NMOS_ChannelWidth'] = _CompClkLogic_Inv_NMOS_ChannelWidth
        _Caculation_Parameters['_Inv_NMOS_ChannelLength'] = _CompClkLogic_Inv_NMOS_ChannelLength

        _Caculation_Parameters['_Inv_PMOS_NumberofGate'] = _CompClkLogic_Inv_PMOS_NumberofGate
        _Caculation_Parameters['_Inv_PMOS_ChannelWidth'] = _CompClkLogic_Inv_PMOS_ChannelWidth
        _Caculation_Parameters['_Inv_PMOS_ChannelLength'] = _CompClkLogic_Inv_PMOS_ChannelLength

        ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_AND_CLKIn'] = self._SrefElementDeclaration(_DesignObj=E02_03_And_KJH0._And(_DesignParameter=None, _Name='{}:SRF_AND_CLKIn'.format(_Name)))[0]

        ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_AND_CLKIn']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_AND_CLKIn']['_Angle'] = 180

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_AND_CLKIn']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_AND_CLKIn']['_XYCoordinates'] = [[0, 0]]
        ## CLK Samp Inverter SREF Generation
        _Caculation_Parameters = copy.deepcopy(E01_00_Inverter._Inverter._ParametersForDesignCalculation)
        ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
        _Caculation_Parameters['_XVT'] = _CompClkLogic_XVT

        _Caculation_Parameters['_NMOS_NumberofGate'] = _CompClkLogic_ClkSrc_NMOS_NumberofGate
        _Caculation_Parameters['_NMOS_ChannelWidth'] = _CompClkLogic_ClkSrc_NMOS_ChannelWidth
        _Caculation_Parameters['_NMOS_ChannelLength'] = _CompClkLogic_ClkSrc_NMOS_ChannelLength

        _Caculation_Parameters['_PMOS_NumberofGate'] = _CompClkLogic_ClkSrc_PMOS_NumberofGate
        _Caculation_Parameters['_PMOS_ChannelWidth'] = _CompClkLogic_ClkSrc_PMOS_ChannelWidth
        _Caculation_Parameters['_PMOS_ChannelLength'] = _CompClkLogic_ClkSrc_PMOS_ChannelLength

        _Caculation_Parameters['_NMOS_Pbody_XvtTop2Pbody'] = _CompClkLogic_NMOS_Pbody_XvtTop2Pbody
        _Caculation_Parameters['_PMOS_Nbody_Xvtdown2Nbody'] = _CompClkLogic_PMOS_Nbody_Xvtdown2Nbody

        _Caculation_Parameters['_PMOSXvt2NMOSXvt'] = _CompClkLogic_PMOSXvt2NMOSXvt

        ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_Inv_CLKSrc'] = self._SrefElementDeclaration(
            _DesignObj=E01_00_Inverter._Inverter(_DesignParameter=None, _Name='{}:SRF_Inv_CLKSrc'.format(_Name)))[0]

        ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_Inv_CLKSrc']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Inv_CLKSrc']['_Angle'] = 180

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Inv_CLKSrc']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Inv_CLKSrc']['_XYCoordinates'] = [[0, 0]]
        ## CLK Src Inverter SREF Generation
        _Caculation_Parameters = copy.deepcopy(E01_00_Inverter._Inverter._ParametersForDesignCalculation)
        ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
        _Caculation_Parameters['_XVT'] = _CompClkLogic_XVT

        _Caculation_Parameters['_NMOS_NumberofGate'] = _CompClkLogic_ClkSmp_NMOS_NumberofGate
        _Caculation_Parameters['_NMOS_ChannelWidth'] = _CompClkLogic_ClkSmp_NMOS_ChannelWidth
        _Caculation_Parameters['_NMOS_ChannelLength'] = _CompClkLogic_ClkSmp_NMOS_ChannelLength

        _Caculation_Parameters['_PMOS_NumberofGate'] = _CompClkLogic_ClkSmp_PMOS_NumberofGate
        _Caculation_Parameters['_PMOS_ChannelWidth'] = _CompClkLogic_ClkSmp_PMOS_ChannelWidth
        _Caculation_Parameters['_PMOS_ChannelLength'] = _CompClkLogic_ClkSmp_PMOS_ChannelLength

        _Caculation_Parameters['_NMOS_Pbody_XvtTop2Pbody'] = _CompClkLogic_NMOS_Pbody_XvtTop2Pbody
        _Caculation_Parameters['_PMOS_Nbody_Xvtdown2Nbody'] = _CompClkLogic_PMOS_Nbody_Xvtdown2Nbody

        _Caculation_Parameters['_PMOSXvt2NMOSXvt'] = _CompClkLogic_PMOSXvt2NMOSXvt

        ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_Inv_CLKSamp'] = self._SrefElementDeclaration(
            _DesignObj=E01_00_Inverter._Inverter(_DesignParameter=None, _Name='{}:SRF_Inv_CLKSamp'.format(_Name)))[0]

        ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_Inv_CLKSamp']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Inv_CLKSamp']['_Angle'] = 180

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Inv_CLKSamp']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Inv_CLKSamp']['_XYCoordinates'] = [[0, 0]]
        ######################################################################################### Pre-Cal for BufX, Bufy, SR Latch. xvt2body: Cal Xvt2body
        tmp1_1 = self.get_param_KJH4('SRF_CLKBuffer','SRF_Inverter1','SRF_NMOS','BND_{}Layer'.format(_CompClkLogic_XVT))
        tmp2_1 = self.get_param_KJH4('SRF_CLKBuffer','SRF_Inverter1','SRF_Pbody','SRF_PbodyContactPhyLen','BND_Met1Layer')
        CLKBUf_Xvttop2Pbody = abs(tmp1_1[0][0][0][0][0]['_XY_up'][1] - tmp2_1[0][0][0][0][0][0]['_XY_up'][1])
        tmp3_1 = self.get_param_KJH4('SRF_CLKBuffer','SRF_Inverter1','SRF_PMOS','BND_{}Layer'.format(_CompClkLogic_XVT))
        tmp4_1 = self.get_param_KJH4('SRF_CLKBuffer','SRF_Inverter1','SRF_Nbody','SRF_NbodyContactPhyLen','BND_Met1Layer')
        CLKBUf_Xvtdown2Nbody = abs(tmp4_1[0][0][0][0][0][0]['_XY_down'][1] - tmp3_1[0][0][0][0][0]['_XY_down'][1])

        tmp1_2 = self.get_param_KJH4('SRF_AND_CLKIn','SRF_Inverter','SRF_NMOS','BND_{}Layer'.format(_CompClkLogic_XVT))
        tmp2_2 = self.get_param_KJH4('SRF_AND_CLKIn','SRF_Inverter','SRF_Pbody','SRF_PbodyContactPhyLen','BND_Met1Layer')
        And_Xvttop2Pbody = abs(tmp1_2[0][0][0][0][0]['_XY_up'][1] - tmp2_2[0][0][0][0][0][0]['_XY_up'][1])
        tmp3_2 = self.get_param_KJH4('SRF_AND_CLKIn','SRF_Inverter','SRF_PMOS','BND_{}Layer'.format(_CompClkLogic_XVT))
        tmp4_2 = self.get_param_KJH4('SRF_AND_CLKIn','SRF_Inverter','SRF_Nbody','SRF_NbodyContactPhyLen','BND_Met1Layer')
        And_Xvtdown2Nbody = abs(tmp4_2[0][0][0][0][0][0]['_XY_down'][1] - tmp3_2[0][0][0][0][0]['_XY_down'][1])

        tmp1_3 = self.get_param_KJH4('SRF_Inv_CLKSrc','SRF_NMOS','BND_{}Layer'.format(_CompClkLogic_XVT))
        tmp2_3 = self.get_param_KJH4('SRF_Inv_CLKSrc','SRF_Pbody','SRF_PbodyContactPhyLen','BND_Met1Layer')
        ScrInv_Xvttop2Pbody = abs(tmp1_3[0][0][0][0]['_XY_up'][1] - tmp2_3[0][0][0][0][0]['_XY_up'][1])
        tmp3_3 = self.get_param_KJH4('SRF_Inv_CLKSrc','SRF_PMOS','BND_{}Layer'.format(_CompClkLogic_XVT))
        tmp4_3 = self.get_param_KJH4('SRF_Inv_CLKSrc','SRF_Nbody','SRF_NbodyContactPhyLen','BND_Met1Layer')
        ScrInv_Xvtdown2Nbody = abs(tmp4_3[0][0][0][0][0]['_XY_down'][1] - tmp3_3[0][0][0][0]['_XY_down'][1])

        tmp1_4 = self.get_param_KJH4('SRF_Inv_CLKSamp','SRF_NMOS','BND_{}Layer'.format(_CompClkLogic_XVT))
        tmp2_4 = self.get_param_KJH4('SRF_Inv_CLKSamp','SRF_Pbody','SRF_PbodyContactPhyLen','BND_Met1Layer')
        SampInv_Xvttop2Pbody = abs(tmp1_4[0][0][0][0]['_XY_up'][1] - tmp2_4[0][0][0][0][0]['_XY_up'][1])
        tmp3_4 = self.get_param_KJH4('SRF_Inv_CLKSamp','SRF_PMOS','BND_{}Layer'.format(_CompClkLogic_XVT))
        tmp4_4 = self.get_param_KJH4('SRF_Inv_CLKSamp','SRF_Nbody','SRF_NbodyContactPhyLen','BND_Met1Layer')
        SampInv_Xvtdown2Nbody = abs(tmp4_4[0][0][0][0][0]['_XY_down'][1] - tmp3_4[0][0][0][0]['_XY_down'][1])

        tmp2_Xvttop2Pbody = max(CLKBUf_Xvttop2Pbody,And_Xvttop2Pbody,ScrInv_Xvttop2Pbody,SampInv_Xvttop2Pbody)
        tmp2_Xvtdown2Nbody = max(CLKBUf_Xvtdown2Nbody,And_Xvtdown2Nbody,ScrInv_Xvtdown2Nbody,SampInv_Xvtdown2Nbody)

        #####################################################################################################################################
        ################################################################################################################
        ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ###
        ### CLK(Samp/Source) Input Logic(CLK Buffer, AND, 2 Inverters)
        ## CLK Buffer Generation
        ########### SA Output Node X -> Buffer X Generation
        _Caculation_Parameters = copy.deepcopy(E01_01_Buffer._Buffer._ParametersForDesignCalculation)
        ## Buffer
            ## Common
                # XVT
        _Caculation_Parameters['_Buf_XVT'] = _CompClkLogic_XVT
                # Body
        _Caculation_Parameters['_Buf_NMOS_Pbody_XvtTop2Pbody'] = tmp2_Xvttop2Pbody
        _Caculation_Parameters['_Buf_PMOS_Nbody_Xvtdown2Nbody'] = tmp2_Xvtdown2Nbody
                # Height
        _Caculation_Parameters['_Buf_PMOSXvt2NMOSXvt'] = _CompClkLogic_PMOSXvt2NMOSXvt
            ## Inverter1
                # Nmos
        _Caculation_Parameters['_Buf_Inv1_NMOS_NumberofGate'] = _CompClkLogic_Buf_Inv1_NMOS_NumberofGate
        _Caculation_Parameters['_Buf_Inv1_NMOS_ChannelWidth'] = _CompClkLogic_Buf_Inv1_NMOS_ChannelWidth
        _Caculation_Parameters['_Buf_Inv1_NMOS_ChannelLength'] = _CompClkLogic_Buf_Inv1_NMOS_ChannelLength
                # Pmos
        _Caculation_Parameters['_Buf_Inv1_PMOS_NumberofGate'] = _CompClkLogic_Buf_Inv1_PMOS_NumberofGate
        _Caculation_Parameters['_Buf_Inv1_PMOS_ChannelWidth'] = _CompClkLogic_Buf_Inv1_PMOS_ChannelWidth
        _Caculation_Parameters['_Buf_Inv1_PMOS_ChannelLength'] = _CompClkLogic_Buf_Inv1_PMOS_ChannelLength
            ## Inverter2
                # Nmos
        _Caculation_Parameters['_Buf_Inv2_NMOS_NumberofGate'] = _CompClkLogic_Buf_Inv2_NMOS_NumberofGate
        _Caculation_Parameters['_Buf_Inv2_NMOS_ChannelWidth'] = _CompClkLogic_Buf_Inv2_NMOS_ChannelWidth
        _Caculation_Parameters['_Buf_Inv2_NMOS_ChannelLength'] = _CompClkLogic_Buf_Inv2_NMOS_ChannelLength
                # Pmos
        _Caculation_Parameters['_Buf_Inv2_PMOS_NumberofGate'] = _CompClkLogic_Buf_Inv2_PMOS_NumberofGate
        _Caculation_Parameters['_Buf_Inv2_PMOS_ChannelWidth'] = _CompClkLogic_Buf_Inv2_PMOS_ChannelWidth
        _Caculation_Parameters['_Buf_Inv2_PMOS_ChannelLength'] = _CompClkLogic_Buf_Inv2_PMOS_ChannelLength

        ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_CLKBuffer'] = self._SrefElementDeclaration(_DesignObj=E01_01_Buffer._Buffer(_DesignParameter=None,_Name='{}:SRF_CLKBuffer'.format(_Name)))[0]

        ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_CLKBuffer']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_CLKBuffer']['_Angle'] = 180

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_CLKBuffer']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_CLKBuffer']['_XYCoordinates'] = [[0, 0]]

                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## Calculate
                            ## Target_coord: _XY_type1
        tmp1 = self.get_param_KJH4('SRF_BufferX','SRF_Inverter1','SRF_Pbody','SRF_PbodyContactPhyLen','BND_Met1Layer')
        target_coord = tmp1[0][0][0][0][0][0]['_XY_down_left']
                            ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('SRF_CLKBuffer', 'SRF_Inverter2','SRF_Pbody','SRF_PbodyContactPhyLen','BND_Met1Layer')
        approaching_coord = tmp2[0][0][0][0][0][0]['_XY_up_right']
                            ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_CLKBuffer')
        Scoord = tmp3[0][0]['_XY_origin']
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                            ## Define coordinates
        self._DesignParameter['SRF_CLKBuffer']['_XYCoordinates'] = tmpXY

        #####################################################################################################################################
        ### AND Gate SREF Generation
        _Caculation_Parameters = copy.deepcopy(E02_03_And_KJH0._And._ParametersForDesignCalculation)
        _Caculation_Parameters['_And_XVT'] = _CompClkLogic_XVT

        _Caculation_Parameters['_And_PMOSXvt2NMOSXvt'] = _CompClkLogic_PMOSXvt2NMOSXvt

        _Caculation_Parameters['_And_Pbody_XvtTop2Pbody'] = tmp2_Xvttop2Pbody
        _Caculation_Parameters['_And_Nbody_Xvtdown2Nbody'] = tmp2_Xvtdown2Nbody

        _Caculation_Parameters['_Nand_NMOSA_NumberofGate'] = _CompClkLogic_Nand_NMOSA_NumberofGate
        _Caculation_Parameters['_Nand_NMOSA_ChannelWidth'] = _CompClkLogic_Nand_NMOSA_ChannelWidth
        _Caculation_Parameters['_Nand_NMOSA_ChannelLength'] = _CompClkLogic_Nand_NMOSA_ChannelLength

        _Caculation_Parameters['_Nand_NMOSB_NumberofGate'] = _CompClkLogic_Nand_NMOSB_NumberofGate
        _Caculation_Parameters['_Nand_NMOSB_ChannelWidth'] = _CompClkLogic_Nand_NMOSB_ChannelWidth
        _Caculation_Parameters['_Nand_NMOSB_ChannelLength'] = _CompClkLogic_Nand_NMOSB_ChannelLength

        _Caculation_Parameters['_Nand_PMOSA_NumberofGate'] = _CompClkLogic_Nand_PMOSA_NumberofGate
        _Caculation_Parameters['_Nand_PMOSA_ChannelWidth'] = _CompClkLogic_Nand_PMOSA_ChannelWidth
        _Caculation_Parameters['_Nand_PMOSA_ChannelLength'] = _CompClkLogic_Nand_PMOSA_ChannelLength

        _Caculation_Parameters['_Nand_PMOSB_NumberofGate'] = _CompClkLogic_Nand_PMOSB_NumberofGate
        _Caculation_Parameters['_Nand_PMOSB_ChannelWidth'] = _CompClkLogic_Nand_PMOSB_ChannelWidth
        _Caculation_Parameters['_Nand_PMOSB_ChannelLength'] = _CompClkLogic_Nand_PMOSB_ChannelLength

        _Caculation_Parameters['_Inv_NMOS_NumberofGate'] = _CompClkLogic_Inv_NMOS_NumberofGate
        _Caculation_Parameters['_Inv_NMOS_ChannelWidth'] = _CompClkLogic_Inv_NMOS_ChannelWidth
        _Caculation_Parameters['_Inv_NMOS_ChannelLength'] = _CompClkLogic_Inv_NMOS_ChannelLength

        _Caculation_Parameters['_Inv_PMOS_NumberofGate'] = _CompClkLogic_Inv_PMOS_NumberofGate
        _Caculation_Parameters['_Inv_PMOS_ChannelWidth'] = _CompClkLogic_Inv_PMOS_ChannelWidth
        _Caculation_Parameters['_Inv_PMOS_ChannelLength'] = _CompClkLogic_Inv_PMOS_ChannelLength

        ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_AND_CLKIn'] = self._SrefElementDeclaration(_DesignObj=E02_03_And_KJH0._And(_DesignParameter=None, _Name='{}:SRF_AND_CLKIn'.format(_Name)))[0]

        ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_AND_CLKIn']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_AND_CLKIn']['_Angle'] = 180

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_AND_CLKIn']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_AND_CLKIn']['_XYCoordinates'] = [[0, 0]]

                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## Calculate
        ## Target_coord: _XY_type1
        tmp1x1 = self.get_param_KJH4('SRF_CLKBuffer', 'SRF_Inverter1','SRF_NMOS', 'BND_PODummyLayer')
        tmp1x2 = self.get_param_KJH4('SRF_CLKBuffer', 'SRF_Inverter1','SRF_PMOS', 'BND_PODummyLayer')
        target_coordx = max(tmp1x1[0][0][0][0][0]['_XY_left'][0],tmp1x2[0][0][0][0][0]['_XY_left'][0])
        tmp1y = self.get_param_KJH4('SRF_CLKBuffer', 'SRF_Inverter1','SRF_Pbody','SRF_PbodyContactPhyLen','BND_Met1Layer')
        target_coord = [target_coordx, tmp1y[0][0][0][0][0][0]['_XY_up'][1]]
        ## Approaching_coord: _XY_type2
        tmp2x1 = self.get_param_KJH4('SRF_AND_CLKIn','SRF_Inverter', 'SRF_NMOS', 'BND_PODummyLayer')
        tmp2x2 = self.get_param_KJH4('SRF_AND_CLKIn','SRF_Inverter', 'SRF_PMOS', 'BND_PODummyLayer')
        approaching_coordx = min(tmp2x1[0][0][0][-1][0]['_XY_right'][0],tmp2x2[0][0][0][-1][0]['_XY_right'][0])
        tmp2y = self.get_param_KJH4('SRF_AND_CLKIn','SRF_Inverter', 'SRF_Pbody', 'SRF_PbodyContactPhyLen', 'BND_Met1Layer')
        approaching_coord = [approaching_coordx, tmp2y[0][0][0][0][0][0]['_XY_up'][1]]
                            ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_AND_CLKIn')
        Scoord = tmp3[0][0]['_XY_origin']
        Scoord[0] = Scoord[0] + 96
        # Scoord[0] = Scoord[0] + 140
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                            ## Define coordinates
        self._DesignParameter['SRF_AND_CLKIn']['_XYCoordinates'] = tmpXY

        #####################################################################################################################################
        ## CLK Samp Inverter SREF Generation
        _Caculation_Parameters = copy.deepcopy(E01_00_Inverter._Inverter._ParametersForDesignCalculation)
        ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
        _Caculation_Parameters['_XVT'] = _CompClkLogic_XVT

        _Caculation_Parameters['_NMOS_NumberofGate'] = _CompClkLogic_ClkSrc_NMOS_NumberofGate
        _Caculation_Parameters['_NMOS_ChannelWidth'] = _CompClkLogic_ClkSrc_NMOS_ChannelWidth
        _Caculation_Parameters['_NMOS_ChannelLength'] = _CompClkLogic_ClkSrc_NMOS_ChannelLength

        _Caculation_Parameters['_PMOS_NumberofGate'] = _CompClkLogic_ClkSrc_PMOS_NumberofGate
        _Caculation_Parameters['_PMOS_ChannelWidth'] = _CompClkLogic_ClkSrc_PMOS_ChannelWidth
        _Caculation_Parameters['_PMOS_ChannelLength'] = _CompClkLogic_ClkSrc_PMOS_ChannelLength

        _Caculation_Parameters['_NMOS_Pbody_XvtTop2Pbody'] = tmp2_Xvttop2Pbody
        _Caculation_Parameters['_PMOS_Nbody_Xvtdown2Nbody'] = tmp2_Xvtdown2Nbody

        _Caculation_Parameters['_PMOSXvt2NMOSXvt'] = _CompClkLogic_PMOSXvt2NMOSXvt

        ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_Inv_CLKSrc'] = self._SrefElementDeclaration(
            _DesignObj=E01_00_Inverter._Inverter(_DesignParameter=None, _Name='{}:SRF_Inv_CLKSrc'.format(_Name)))[0]

        ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_Inv_CLKSrc']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Inv_CLKSrc']['_Angle'] = 180

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Inv_CLKSrc']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Inv_CLKSrc']['_XYCoordinates'] = [[0, 0]]

                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## Calculate
        ## Target_coord: _XY_type1
        tmp1x1 = self.get_param_KJH4('SRF_AND_CLKIn','SRF_NAND','SRF_Pulldown', 'SRF_NMOSA', 'BND_PODummyLayer')
        tmp1x2 = self.get_param_KJH4('SRF_AND_CLKIn','SRF_NAND','SRF_Pullup', 'SRF_PMOSA', 'BND_PODummyLayer')
        target_coordx = max(tmp1x1[0][0][0][0][0][0]['_XY_left'][0],tmp1x2[0][0][0][0][0][0]['_XY_left'][0])
        tmp1y = self.get_param_KJH4('SRF_AND_CLKIn','SRF_Inverter', 'SRF_Pbody', 'SRF_PbodyContactPhyLen', 'BND_Met1Layer')
        target_coord = [target_coordx, tmp1y[0][0][0][0][0][0]['_XY_up'][1]]
        ## Approaching_coord: _XY_type2
        tmp2x1 = self.get_param_KJH4('SRF_Inv_CLKSrc', 'SRF_NMOS', 'BND_PODummyLayer')
        tmp2x2 = self.get_param_KJH4('SRF_Inv_CLKSrc', 'SRF_PMOS', 'BND_PODummyLayer')
        approaching_coordx = min(tmp2x1[0][0][-1][0]['_XY_right'][0],tmp2x2[0][0][-1][0]['_XY_right'][0])
        tmp2y = self.get_param_KJH4('SRF_Inv_CLKSrc', 'SRF_Pbody', 'SRF_PbodyContactPhyLen', 'BND_Met1Layer')
        approaching_coord = [approaching_coordx, tmp2y[0][0][0][0][0]['_XY_up'][1]]
                            ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_Inv_CLKSrc')
        Scoord = tmp3[0][0]['_XY_origin']
        Scoord[0] = Scoord[0] + 96
        # Scoord[0] = Scoord[0] + 140
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                            ## Define coordinates
        self._DesignParameter['SRF_Inv_CLKSrc']['_XYCoordinates'] = tmpXY


        #####################################################################################################################################
        ## CLK Src Inverter SREF Generation
        _Caculation_Parameters = copy.deepcopy(E01_00_Inverter._Inverter._ParametersForDesignCalculation)
        ## Define Calculation_Parameters ex) _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length
        _Caculation_Parameters['_XVT'] = _CompClkLogic_XVT

        _Caculation_Parameters['_NMOS_NumberofGate'] = _CompClkLogic_ClkSmp_NMOS_NumberofGate
        _Caculation_Parameters['_NMOS_ChannelWidth'] = _CompClkLogic_ClkSmp_NMOS_ChannelWidth
        _Caculation_Parameters['_NMOS_ChannelLength'] = _CompClkLogic_ClkSmp_NMOS_ChannelLength

        _Caculation_Parameters['_PMOS_NumberofGate'] = _CompClkLogic_ClkSmp_PMOS_NumberofGate
        _Caculation_Parameters['_PMOS_ChannelWidth'] = _CompClkLogic_ClkSmp_PMOS_ChannelWidth
        _Caculation_Parameters['_PMOS_ChannelLength'] = _CompClkLogic_ClkSmp_PMOS_ChannelLength

        _Caculation_Parameters['_NMOS_Pbody_XvtTop2Pbody'] = tmp2_Xvttop2Pbody
        _Caculation_Parameters['_PMOS_Nbody_Xvtdown2Nbody'] = tmp2_Xvtdown2Nbody

        _Caculation_Parameters['_PMOSXvt2NMOSXvt'] = _CompClkLogic_PMOSXvt2NMOSXvt

        ## Generate Sref: ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
        self._DesignParameter['SRF_Inv_CLKSamp'] = self._SrefElementDeclaration(
            _DesignObj=E01_00_Inverter._Inverter(_DesignParameter=None, _Name='{}:SRF_Inv_CLKSamp'.format(_Name)))[0]

        ## Define Sref Reflection: ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_Inv_CLKSamp']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Inv_CLKSamp']['_Angle'] = 180

        ## Calculate Sref Layer by using Calculation_Parameter: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Inv_CLKSamp']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        ## Define Sref _XYcoordinate: ex)'_NMOS_POWER'
        self._DesignParameter['SRF_Inv_CLKSamp']['_XYCoordinates'] = [[0, 0]]

        ## Calculate Sref XYcoord
        tmpXY = []
        ## Calculate
        ## Target_coord: _XY_type1
        # tmp1x = self.get_param_KJH4('SRF_Inv_CLKSrc', 'SRF_NMOS', 'BND_PODummyLayer')
        tmp1x1 = self.get_param_KJH4('SRF_Inv_CLKSrc','SRF_NMOS', 'BND_PODummyLayer')
        tmp1x2 = self.get_param_KJH4('SRF_Inv_CLKSrc','SRF_PMOS', 'BND_PODummyLayer')
        target_coordx = max(tmp1x1[0][0][0][0]['_XY_left'][0],tmp1x2[0][0][0][0]['_XY_left'][0])
        tmp1y = self.get_param_KJH4('SRF_Inv_CLKSrc', 'SRF_Pbody', 'SRF_PbodyContactPhyLen', 'BND_Met1Layer')
        target_coord = [target_coordx, tmp1y[0][0][0][0][0]['_XY_up'][1]]
        ## Approaching_coord: _XY_type2
        tmp2x1 = self.get_param_KJH4('SRF_Inv_CLKSamp', 'SRF_NMOS', 'BND_PODummyLayer')
        tmp2x2 = self.get_param_KJH4('SRF_Inv_CLKSamp', 'SRF_PMOS', 'BND_PODummyLayer')
        approaching_coordx = min(tmp2x1[0][0][-1][0]['_XY_right'][0],tmp2x2[0][0][-1][0]['_XY_right'][0])
        tmp2y = self.get_param_KJH4('SRF_Inv_CLKSamp', 'SRF_Pbody', 'SRF_PbodyContactPhyLen', 'BND_Met1Layer')
        approaching_coord = [approaching_coordx, tmp2y[0][0][0][0][0]['_XY_up'][1]]
        ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_Inv_CLKSamp')
        Scoord = tmp3[0][0]['_XY_origin']
        Scoord[0] = Scoord[0] + 96
        # Scoord[0] = Scoord[0] + 140
        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define coordinates
        self._DesignParameter['SRF_Inv_CLKSamp']['_XYCoordinates'] = tmpXY
        #####################################################################################################################################

        #### SRF Inv_CLKSamp_Input_ViaM1M4
        ## Sref generation: ViaX
            ## Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH3._ViaStack._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 1
        _Caculation_Parameters['_Layer2'] = 4
        _Caculation_Parameters['_COX'] = 1
        _Caculation_Parameters['_COY'] = 2

            ## Sref ViaX declaration
        self._DesignParameter['SRF_CLKSampInv_Input_ViaM1M4'] = self._SrefElementDeclaration(_DesignObj=A02_ViaStack_KJH3._ViaStack(_DesignParameter=None, _Name='{}:SRF_CLKSampInv_Input_ViaM1M4'.format(_Name)))[0]

            ## Define Sref Relection
        self._DesignParameter['SRF_CLKSampInv_Input_ViaM1M4']['_Reflect'] = [0, 0, 0]

            ## Define Sref Angle
        self._DesignParameter['SRF_CLKSampInv_Input_ViaM1M4']['_Angle'] = 0

            ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
        self._DesignParameter['SRF_CLKSampInv_Input_ViaM1M4']['_DesignObj']._CalculateDesignParameterXmin(**_Caculation_Parameters)

            ## Calculate Sref XYcoord
        tmpXY = []
                ## initialized Sref coordinate
        self._DesignParameter['SRF_CLKSampInv_Input_ViaM1M4']['_XYCoordinates'] = [[0, 0]]
                ## Calculate
                    ## Target_coord
        tmp1 = self.get_param_KJH4('SRF_Inv_CLKSamp','BND_Input_Vtc_M1')
        target_coord = tmp1[0][0][0]['_XY_left']
                    ## Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_CLKSampInv_Input_ViaM1M4','SRF_ViaM1M2','BND_Met1Layer')
        approaching_coord = tmp2[0][0][0][0]['_XY_right']
                    ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_CLKSampInv_Input_ViaM1M4')
        Scoord = tmp3[0][0]['_XY_origin']
                    ## Calculate
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                ## Define
        self._DesignParameter['SRF_CLKSampInv_Input_ViaM1M4']['_XYCoordinates'] = tmpXY
        #####################################################################################################################################

        #### CLK_Samp Inverter -> AND gate routing
        #### SRF Inv_CLKSrc_Input_ViaM1M4
        ## Sref generation: ViaX
            ## Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH3._ViaStack._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 1
        _Caculation_Parameters['_Layer2'] = 4
        _Caculation_Parameters['_COX'] = 1
        _Caculation_Parameters['_COY'] = 2

            ## Sref ViaX declaration
        self._DesignParameter['SRF_CLKSrcInv_Input_ViaM1M4'] = self._SrefElementDeclaration(_DesignObj=A02_ViaStack_KJH3._ViaStack(_DesignParameter=None, _Name='{}:SRF_CLKSrcInv_Input_ViaM1M4'.format(_Name)))[0]

            ## Define Sref Relection
        self._DesignParameter['SRF_CLKSrcInv_Input_ViaM1M4']['_Reflect'] = [0, 0, 0]

            ## Define Sref Angle
        self._DesignParameter['SRF_CLKSrcInv_Input_ViaM1M4']['_Angle'] = 0

            ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
        self._DesignParameter['SRF_CLKSrcInv_Input_ViaM1M4']['_DesignObj']._CalculateDesignParameterXmin(**_Caculation_Parameters)

            ## Calculate Sref XYcoord
        tmpXY = []
                ## initialized Sref coordinate
        self._DesignParameter['SRF_CLKSrcInv_Input_ViaM1M4']['_XYCoordinates'] = [[0, 0]]
                ## Calculate
                    ## Target_coord
        tmp1 = self.get_param_KJH4('SRF_Inv_CLKSrc','BND_Input_Vtc_M1')
        target_coord = tmp1[0][0][0]['_XY_left']
                    ## Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_CLKSrcInv_Input_ViaM1M4','SRF_ViaM1M2','BND_Met1Layer')
        approaching_coord = tmp2[0][0][0][0]['_XY_right']
                    ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_CLKSrcInv_Input_ViaM1M4')
        Scoord = tmp3[0][0]['_XY_origin']
                    ## Calculate
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                ## Define
        self._DesignParameter['SRF_CLKSrcInv_Input_ViaM1M4']['_XYCoordinates'] = tmpXY
        #####################################################################################################################################

        ###### CLK_Sample Inverter Output ViaM2M3
        ## Sref generation: ViaX
        ## Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH3._ViaStack._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 2
        _Caculation_Parameters['_Layer2'] = 3
        _Caculation_Parameters['_COX'] = 1
        _Caculation_Parameters['_COY'] = 2

        ## Sref ViaX declaration
        self._DesignParameter['SRF_CLKSampInvOut_ViaM2M3'] = self._SrefElementDeclaration(
            _DesignObj=A02_ViaStack_KJH3._ViaStack(_DesignParameter=None, _Name='{}:SRF_CLKSampInvOut_ViaM2M3'.format(_Name)))[0]

        ## Define Sref Relection
        self._DesignParameter['SRF_CLKSampInvOut_ViaM2M3']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle
        self._DesignParameter['SRF_CLKSampInvOut_ViaM2M3']['_Angle'] = 0

        ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
        self._DesignParameter['SRF_CLKSampInvOut_ViaM2M3']['_DesignObj']._CalculateDesignParameterXmin(**_Caculation_Parameters)

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['SRF_CLKSampInvOut_ViaM2M3']['_XYCoordinates'] = [[0, 0]]
        ## Calculate
        ## Target_coord
        tmp1x = self.get_param_KJH4('SRF_Inv_CLKSamp','BND_Out_Vtc_M2')
        tmp1y = self.get_param_KJH4('SRF_Inv_CLKSamp','SRF_PMOS', 'BND_Gate_Hrz_Mx')
        target_coord = [tmp1x[0][0][0]['_XY_right'][0], tmp1y[0][0][0][0]['_XY_down'][1]]
        ## Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_CLKSampInvOut_ViaM2M3','SRF_ViaM2M3','BND_Met3Layer')
        approaching_coord = tmp2[0][0][0][0]['_XY_down_left']
        ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_CLKSampInvOut_ViaM2M3')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Calculate
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define
        self._DesignParameter['SRF_CLKSampInvOut_ViaM2M3']['_XYCoordinates'] = tmpXY
        #####################################################################################################################################

        ###### CLK_Sample Inverter Output ViaM2M3
        ## Sref generation: ViaX
        ## Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH3._ViaStack._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 1
        _Caculation_Parameters['_Layer2'] = 3
        _Caculation_Parameters['_COX'] = 1
        _Caculation_Parameters['_COY'] = 2

        ## Sref ViaX declaration
        self._DesignParameter['SRF_ANDInCLKSamp_ViaM1M3'] = self._SrefElementDeclaration(
            _DesignObj=A02_ViaStack_KJH3._ViaStack(_DesignParameter=None, _Name='{}:SRF_ANDInCLKSamp_ViaM1M3'.format(_Name)))[0]

        ## Define Sref Relection
        self._DesignParameter['SRF_ANDInCLKSamp_ViaM1M3']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle
        self._DesignParameter['SRF_ANDInCLKSamp_ViaM1M3']['_Angle'] = 0

        ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
        self._DesignParameter['SRF_ANDInCLKSamp_ViaM1M3']['_DesignObj']._CalculateDesignParameterXmin(**_Caculation_Parameters)

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['SRF_ANDInCLKSamp_ViaM1M3']['_XYCoordinates'] = [[0, 0]]
        ## Calculate
        ## Target_coord
        tmp1x = self.get_param_KJH4('SRF_AND_CLKIn','SRF_NAND','BND_InputA_Vtc_M1')
        tmp1y = self.get_param_KJH4('SRF_CLKSampInvOut_ViaM2M3','SRF_ViaM2M3', 'BND_Met3Layer')
        target_coord = [tmp1x[0][0][0][0]['_XY_right'][0], tmp1y[0][0][0][0]['_XY_down'][1]]
        ## Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_ANDInCLKSamp_ViaM1M3','SRF_ViaM2M3','BND_Met3Layer')
        approaching_coord = tmp2[0][0][0][0]['_XY_down_left']
        ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_ANDInCLKSamp_ViaM1M3')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Calculate
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define
        self._DesignParameter['SRF_ANDInCLKSamp_ViaM1M3']['_XYCoordinates'] = tmpXY
        #####################################################################################################################################

        #### CLK_Samp Inverter -> AND gate routing
        #### BND_CLKSamp2AND_Hrz_M3
            ## Boundary_element Generation
                ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_CLKSamp2AND_Hrz_M3'] = self._BoundaryElementDeclaration(
        _Layer=DesignParameters._LayerMapping['METAL3'][0],
        _Datatype=DesignParameters._LayerMapping['METAL3'][1],
        _XWidth=None,
        _YWidth=None,
        _XYCoordinates=[],
        )
                ## Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('SRF_CLKSampInvOut_ViaM2M3','SRF_ViaM2M3', 'BND_Met3Layer')
        tmp2 = self.get_param_KJH4('SRF_ANDInCLKSamp_ViaM1M3','SRF_ViaM2M3', 'BND_Met3Layer')
        self._DesignParameter['BND_CLKSamp2AND_Hrz_M3']['_YWidth'] = 50

                ## Define Boundary_element _XWidth
        self._DesignParameter['BND_CLKSamp2AND_Hrz_M3']['_XWidth'] = abs(tmp1[0][0][0][0]['_XY_right'][0] - tmp2[0][0][0][0]['_XY_left'][0])

                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['BND_CLKSamp2AND_Hrz_M3']['_XYCoordinates'] = [[0, 0]]
                        ## Calculate
                            ## Target_coord: _XY_type1
        tmp1 = self.get_param_KJH4('SRF_CLKSampInvOut_ViaM2M3','SRF_ViaM2M3', 'BND_Met3Layer')
        target_coord = tmp1[0][0][0][0]['_XY_down_right']
                            ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_CLKSamp2AND_Hrz_M3')
        approaching_coord = tmp2[0][0]['_XY_down_right']
                            ## Sref coord
        tmp3 = self.get_param_KJH4('BND_CLKSamp2AND_Hrz_M3')
        Scoord = tmp3[0][0]['_XY_origin']
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                            ## Define coordinates
        self._DesignParameter['BND_CLKSamp2AND_Hrz_M3']['_XYCoordinates'] = tmpXY
        #####################################################################################################################################

        # pre-defined routing point(coordY)
        tmp = self.get_param_KJH4('SRF_CLKBuffer','SRF_Inverter1', 'BND_Input_Vtc_M1')
        upperroutepnty_CLKInLogic = max(int(tmp[0][0][0][0]['_XY_down'][1]*0.333 + tmp[0][0][0][0]['_XY_up'][1]*0.666),int(tmp[0][0][0][0]['_XY_down'][1]*0.666 + tmp[0][0][0][0]['_XY_up'][1]*0.333))
        # lowerroutepnty_CLKInLogic = min(int(tmp[0][0][0][0]['_XY_down'][1]*0.333 + tmp[0][0][0][0]['_XY_up'][1]*0.666),int(tmp[0][0][0][0]['_XY_down'][1]*0.666 + tmp[0][0][0][0]['_XY_up'][1]*0.333))

        #####################################################################################################################################

        #### CLK_Src Inverter -> AND gate routing
        ## Sref generation: ViaX
        ## Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH3._ViaStack._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 1
        _Caculation_Parameters['_Layer2'] = 2
        _Caculation_Parameters['_COX'] = 1
        _Caculation_Parameters['_COY'] = 2

        ## Sref ViaX declaration
        self._DesignParameter['SRF_CLKSrcOut2ANDIn_ViaM1M2'] = self._SrefElementDeclaration(
            _DesignObj=A02_ViaStack_KJH3._ViaStack(_DesignParameter=None, _Name='{}:SRF_CLKSrcOut2ANDIn_ViaM1M2'.format(_Name)))[0]

        ## Define Sref Relection
        self._DesignParameter['SRF_CLKSrcOut2ANDIn_ViaM1M2']['_Reflect'] = [0, 0, 0]

        ## Define Sref Angle
        self._DesignParameter['SRF_CLKSrcOut2ANDIn_ViaM1M2']['_Angle'] = 0

        ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
        self._DesignParameter['SRF_CLKSrcOut2ANDIn_ViaM1M2']['_DesignObj']._CalculateDesignParameterXmin(**_Caculation_Parameters)

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['SRF_CLKSrcOut2ANDIn_ViaM1M2']['_XYCoordinates'] = [[0, 0]]
        ## Calculate
        ## Target_coord
        # tmp1x_1 = self.get_param_KJH4('SRF_AND_CLKIn','SRF_NAND','BND_Out_Vtc_M2')
        # tmp1x_2 = self.get_param_KJH4('SRF_AND_CLKIn','SRF_NAND','BND_InputB_Vtc_M1')
        # tmp1x = int((tmp1x_1[0][0][0][0]['_XY_left'][0] + tmp1x_2[0][0][0][0]['_XY_right'][0])/2)
        tmp1x = self.get_param_KJH4('SRF_AND_CLKIn','SRF_NAND','BND_InputB_Vtc_M1')
        targetcoordx = tmp1x[0][0][0][0]['_XY_left'][0]
        tmp1y = upperroutepnty_CLKInLogic
        target_coord = [targetcoordx, tmp1y]
        ## Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_CLKSrcOut2ANDIn_ViaM1M2','SRF_ViaM1M2','BND_Met1Layer')
        approaching_coord = tmp2[0][0][0][0]['_XY_right']
        ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_CLKSrcOut2ANDIn_ViaM1M2')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Calculate
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define
        self._DesignParameter['SRF_CLKSrcOut2ANDIn_ViaM1M2']['_XYCoordinates'] = tmpXY
        #####################################################################################################################################

        #### CLK_Src Inverter -> AND gate routing
        #### BND_CLKSrcOut_Hrz_M2
            ## Boundary_element Generation
                ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_CLKSrcOut_Hrz_M2'] = self._BoundaryElementDeclaration(
        _Layer=DesignParameters._LayerMapping['METAL2'][0],
        _Datatype=DesignParameters._LayerMapping['METAL2'][1],
        _XWidth=None,
        _YWidth=None,
        _XYCoordinates=[],
        )
                ## Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('SRF_CLKSrcOut2ANDIn_ViaM1M2','SRF_ViaM1M2', 'BND_Met2Layer')
        tmp2 = self.get_param_KJH4('SRF_Inv_CLKSrc','BND_Out_Vtc_M2')
        self._DesignParameter['BND_CLKSrcOut_Hrz_M2']['_YWidth'] = 50

                ## Define Boundary_element _XWidth
        self._DesignParameter['BND_CLKSrcOut_Hrz_M2']['_XWidth'] = abs(tmp1[0][0][0][0]['_XY_left'][0] - tmp2[0][0][0]['_XY_left'][0])

                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['BND_CLKSrcOut_Hrz_M2']['_XYCoordinates'] = [[0, 0]]
                        ## Calculate
                            ## Target_coord: _XY_type1
        # tmp1 = self.get_param_KJH4('SRF_CLKSampInvOut_ViaM2M3','SRF_ViaM2M3', 'BND_Met3Layer')
        target_coord = tmp1[0][0][0][0]['_XY_up_left']
                            ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_CLKSrcOut_Hrz_M2')
        approaching_coord = tmp2[0][0]['_XY_up_left']
                            ## Sref coord
        tmp3 = self.get_param_KJH4('BND_CLKSrcOut_Hrz_M2')
        Scoord = tmp3[0][0]['_XY_origin']
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                            ## Define coordinates
        self._DesignParameter['BND_CLKSrcOut_Hrz_M2']['_XYCoordinates'] = tmpXY
        #####################################################################################################################################

        #### AND Output -> CLK Buffer Input
        #### BND_ANDIn_CLKSrc_Hrz_M1
            ## Boundary_element Generation
                ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_AND_Out_Hrz_M2'] = self._BoundaryElementDeclaration(
        _Layer=DesignParameters._LayerMapping['METAL2'][0],
        _Datatype=DesignParameters._LayerMapping['METAL2'][1],
        _XWidth=None,
        _YWidth=None,
        _XYCoordinates=[],
        )
                ## Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('SRF_CLKBuffer','SRF_Inv1Input_ViaM1M2', 'SRF_ViaM1M2', 'BND_Met2Layer')
        tmp2 = self.get_param_KJH4('SRF_AND_CLKIn','SRF_Inverter','BND_Out_Vtc_M2')
        self._DesignParameter['BND_AND_Out_Hrz_M2']['_YWidth'] = 50

                ## Define Boundary_element _XWidth
        self._DesignParameter['BND_AND_Out_Hrz_M2']['_XWidth'] = abs(tmp1[0][0][0][0][0]['_XY_right'][0] - tmp2[0][0][0][0]['_XY_left'][0])

                    ## Calculate Sref XYcoord
        tmpXY = []
                        ## initialized Sref coordinate
        self._DesignParameter['BND_AND_Out_Hrz_M2']['_XYCoordinates'] = [[0, 0]]
                        ## Calculate
                            ## Target_coord: _XY_type1
        # tmp1 = self.get_param_KJH4('SRF_CLKSampInvOut_ViaM2M3','SRF_ViaM2M3', 'BND_Met3Layer')
        target_coord = tmp1[0][0][0][0][0]['_XY_up_right']
                            ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_AND_Out_Hrz_M2')
        approaching_coord = tmp2[0][0]['_XY_down_left']
                            ## Sref coord
        tmp3 = self.get_param_KJH4('BND_AND_Out_Hrz_M2')
        Scoord = tmp3[0][0]['_XY_origin']
                            ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                            ## Define coordinates
        self._DesignParameter['BND_AND_Out_Hrz_M2']['_XYCoordinates'] = tmpXY
        #####################################################################################################################################

        # Calculate Power Rail Size
        tmp1 = self.get_param_KJH4('SRF_BufferX', 'SRF_Inverter1', 'SRF_Pbody', 'SRF_PbodyContactPhyLen','BND_Met1Layer')
        tmp2 = self.get_param_KJH4('SRF_BufferX', 'SRF_Inverter1', 'SRF_Nbody', 'SRF_NbodyContactPhyLen','BND_Met1Layer')
        SpaceBtwUpperRail = abs(tmp1[0][0][0][0][0][0]['_XY_up'][1] - tmp2[0][0][0][0][0][0]['_XY_up'][1])

        tmp3 =  self.get_param_KJH4('SRF_Inv_CLKSamp', 'SRF_Nbody', 'SRF_NbodyContactPhyLen','BND_Met1Layer')
        SpaceBtwLowerRail = abs(tmp1[0][0][0][0][0][0]['_XY_up'][1] - tmp3[0][0][0][0][0]['_XY_down'][1])
        #####################################################################################################################################

        ####### Metal 1 Layer Extension Pbody & Nbody
        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_Pbody_Hrz_M1'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1'][0],
            _Datatype=DesignParameters._LayerMapping['METAL1'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )
        ## Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('SRF_BufferX', 'SRF_Inverter1', 'SRF_Pbody', 'SRF_PbodyContactPhyLen','BND_Met1Layer')
        tmp2_1 = self.get_param_KJH4('SRF_Inv_CLKSamp', 'SRF_Pbody', 'SRF_PbodyContactPhyLen','BND_Met1Layer')
        tmp2_2 = self.get_param_KJH4('SRF_SRLatch', 'BND_M1_NMOS_PBody_SRLatch')
        tmp2 = max(tmp2_1[0][0][0][0][0]['_XY_left'][0], tmp2_2[0][0][0]['_XY_right'][0])
        self._DesignParameter['BND_Pbody_Hrz_M1']['_YWidth'] = max(tmp2_2[0][0][0]['_Ywidth'], tmp2_1[0][0][0][0][0]['_Ywidth'])

        ## Define Boundary_element _XWidth
        self._DesignParameter['BND_Pbody_Hrz_M1']['_XWidth'] = abs(tmp1[0][0][0][0][0][0]['_XY_left'][0] - tmp2)
        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_Pbody_Hrz_M1']['_XYCoordinates'] = [[0, 0]]

        ## Calculate Sref XYcoord
        tmpXY = []
        ## Calculate
        ## Target_coord: _XY_type1
        target_coord = tmp1[0][0][0][0][0][0]['_XY_up_left']
        ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_Pbody_Hrz_M1')
        approaching_coord = tmp2[0][0]['_XY_up_left']
        ## Sref coord
        tmp3 = self.get_param_KJH4('BND_Pbody_Hrz_M1')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)

        ScoordLower = copy.deepcopy(Scoord)
        ScoordLower[1] = ScoordLower[1] - SpaceBtwLowerRail
        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, ScoordLower)
        tmpXY.append(New_Scoord)

        ScoordUpper = copy.deepcopy(Scoord)
        ScoordUpper[1] = ScoordUpper[1] + SpaceBtwUpperRail
        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, ScoordUpper)
        tmpXY.append(New_Scoord)

        ## Define coordinates
        self._DesignParameter['BND_Pbody_Hrz_M1']['_XYCoordinates'] = tmpXY
        #####################################################################################################################################

        ####### RX Layer Extension On Pbody
        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_Pbody_Hrz_RX'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['DIFF'][0],
            _Datatype=DesignParameters._LayerMapping['DIFF'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )
        ## Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('SRF_BufferX', 'SRF_Inverter1', 'SRF_Pbody', 'SRF_PbodyContactPhyLen', 'BND_ODLayer')
        tmp2_1 = self.get_param_KJH4('SRF_Inv_CLKSamp', 'SRF_Pbody', 'SRF_PbodyContactPhyLen', 'BND_ODLayer')
        tmp2_2 = self.get_param_KJH4('SRF_SRLatch', 'BND_M1_NMOS_PBody_SRLatch')
        tmp2 = max(tmp2_1[0][0][0][0][0]['_XY_left'][0], tmp2_2[0][0][0]['_XY_right'][0])
        self._DesignParameter['BND_Pbody_Hrz_RX']['_YWidth'] = max(tmp2_2[0][0][0]['_Ywidth'],
                                                                   tmp2_1[0][0][0][0][0]['_Ywidth'])

        ## Define Boundary_element _XWidth
        self._DesignParameter['BND_Pbody_Hrz_RX']['_XWidth'] = abs(tmp1[0][0][0][0][0][0]['_XY_left'][0] - tmp2)
        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_Pbody_Hrz_RX']['_XYCoordinates'] = [[0, 0]]
        ## Calculate Sref XYcoord
        tmpXY = []
        ## Calculate
        ## Target_coord: _XY_type1
        target_coord = tmp1[0][0][0][0][0][0]['_XY_up_left']
        ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_Pbody_Hrz_RX')
        approaching_coord = tmp2[0][0]['_XY_up_left']
        ## Sref coord
        tmp3 = self.get_param_KJH4('BND_Pbody_Hrz_RX')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)

        ScoordLower = copy.deepcopy(Scoord)
        ScoordLower[1] = ScoordLower[1] - SpaceBtwLowerRail
        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, ScoordLower)
        tmpXY.append(New_Scoord)

        ScoordUpper = copy.deepcopy(Scoord)
        ScoordUpper[1] = ScoordUpper[1] + SpaceBtwUpperRail
        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, ScoordUpper)
        tmpXY.append(New_Scoord)

        ## Define coordinates
        self._DesignParameter['BND_Pbody_Hrz_RX']['_XYCoordinates'] = tmpXY
        #####################################################################################################################################

        ####### PP Layer Extension On Pbody
        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_Pbody_Hrz_PP'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['PIMP'][0],
            _Datatype=DesignParameters._LayerMapping['PIMP'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )
        ## Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('SRF_BufferX', 'SRF_Inverter1', 'SRF_Pbody', 'SRF_PbodyContactPhyLen','BND_PPLayer')
        tmp2_1 = self.get_param_KJH4('SRF_Inv_CLKSamp', 'SRF_Pbody', 'SRF_PbodyContactPhyLen','BND_PPLayer')
        tmp2_2 = self.get_param_KJH4('SRF_SRLatch', 'BND_PPLayer_NMOS_PBody_SRLatch')
        tmp2 = max(tmp2_1[0][0][0][0][0]['_XY_left'][0], tmp2_2[0][0][0]['_XY_right'][0])
        self._DesignParameter['BND_Pbody_Hrz_PP']['_YWidth'] = max(tmp2_2[0][0][0]['_Ywidth'], tmp2_1[0][0][0][0][0]['_Ywidth'])

        ## Define Boundary_element _XWidth
        self._DesignParameter['BND_Pbody_Hrz_PP']['_XWidth'] = abs(tmp1[0][0][0][0][0][0]['_XY_left'][0] - tmp2)
        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_Pbody_Hrz_PP']['_XYCoordinates'] = [[0, 0]]
        ## Calculate Sref XYcoord
        tmpXY = []
        ## Calculate
        ## Target_coord: _XY_type1
        target_coord = tmp1[0][0][0][0][0][0]['_XY_up_left']
        ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_Pbody_Hrz_PP')
        approaching_coord = tmp2[0][0]['_XY_up_left']
        ## Sref coord
        tmp3 = self.get_param_KJH4('BND_Pbody_Hrz_PP')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define coordinates
        self._DesignParameter['BND_Pbody_Hrz_PP']['_XYCoordinates'] = tmpXY
        #####################################################################################################################################

        ####### PP Layer Extension On PMOS
        #### PP Extension on PMOSs of CLKLogic
        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_PPOnCLKInLogic'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['PIMP'][0],
            _Datatype=DesignParameters._LayerMapping['PIMP'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )
        ## Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('SRF_CLKBuffer', 'SRF_Inverter2', 'SRF_PMOS', 'BND_PPLayer')
        tmp2 = self.get_param_KJH4('SRF_Inv_CLKSamp', 'SRF_PMOS', 'BND_PPLayer')
        self._DesignParameter['BND_PPOnCLKInLogic']['_YWidth'] = max(tmp1[0][0][0][0][0]['_Ywidth'], tmp2[0][0][0][0]['_Ywidth'])

        ## Define Boundary_element _XWidth
        self._DesignParameter['BND_PPOnCLKInLogic']['_XWidth'] = abs(
            tmp1[0][0][0][0][0]['_XY_right'][0] - tmp2[0][0][0][0]['_XY_left'][0])
        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_PPOnCLKInLogic']['_XYCoordinates'] = [[0, 0]]
        ## Calculate Sref XYcoord
        tmpXY = []
        ## Calculate
        ## Target_coord: _XY_type1
        target_coord = tmp1[0][0][0][0][0]['_XY_down_right']
        ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_PPOnCLKInLogic')
        approaching_coord = tmp2[0][0]['_XY_up_left']
        ## Sref coord
        tmp3 = self.get_param_KJH4('BND_PPOnCLKInLogic')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define coordinates
        self._DesignParameter['BND_PPOnCLKInLogic']['_XYCoordinates'] = tmpXY
        #####################################################################################################################################

        ####### PP Layer Extension On PMOS
        #### PP Extension on PMOSs of SRLatch & SA Output Buffer
        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_PPOnSRLatchAndBuffer'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['PIMP'][0],
            _Datatype=DesignParameters._LayerMapping['PIMP'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )
        ## Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('SRF_BufferX', 'SRF_Inverter1', 'SRF_PMOS', 'BND_PPLayer')
        tmp2 = self.get_param_KJH4('SRF_SRLatch', 'SRF_NANDR', 'SRF_Pullup', 'SRF_PMOSB', 'BND_PPLayer')
        self._DesignParameter['BND_PPOnSRLatchAndBuffer']['_YWidth'] = max(tmp1[0][0][0][0][0]['_Ywidth'], tmp2[0][0][0][0][0][0]['_Ywidth'])

        ## Define Boundary_element _XWidth
        self._DesignParameter['BND_PPOnSRLatchAndBuffer']['_XWidth'] = abs(
            tmp1[0][0][0][0][0]['_XY_left'][0] - tmp2[0][0][0][0][0][0]['_XY_right'][0])
        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_PPOnSRLatchAndBuffer']['_XYCoordinates'] = [[0, 0]]
        ## Calculate Sref XYcoord
        tmpXY = []
        ## Calculate
        ## Target_coord: _XY_type1
        target_coord = tmp1[0][0][0][0][0]['_XY_up_left']
        ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_PPOnSRLatchAndBuffer')
        approaching_coord = tmp2[0][0]['_XY_up_left']
        ## Sref coord
        tmp3 = self.get_param_KJH4('BND_PPOnSRLatchAndBuffer')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define coordinates
        self._DesignParameter['BND_PPOnSRLatchAndBuffer']['_XYCoordinates'] = tmpXY
        #####################################################################################################################################

        ####### XVT Layer Extension On MOSFET
        #### XVT Extension on PMOSs of SRLatch and SA Output Buffers
        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_XVTExten_PMOSOnSRLatchAndBuffer'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping[_SAOutBufAndSRLatch_XVT][0],
            _Datatype=DesignParameters._LayerMapping[_SAOutBufAndSRLatch_XVT][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )
        ## Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('SRF_BufferX', 'SRF_Inverter1', 'SRF_PMOS', 'BND_{}Layer'.format(_SAOutBufAndSRLatch_XVT))
        tmp2 = self.get_param_KJH4('SRF_SRLatch', 'SRF_NANDR', 'SRF_Pullup', 'SRF_PMOSB', 'BND_{}Layer'.format(_SAOutBufAndSRLatch_XVT))
        self._DesignParameter['BND_XVTExten_PMOSOnSRLatchAndBuffer']['_YWidth'] = max(tmp1[0][0][0][0][0]['_Ywidth'],
                                                                     tmp2[0][0][0][0][0][0]['_Ywidth'])

        ## Define Boundary_element _XWidth
        self._DesignParameter['BND_XVTExten_PMOSOnSRLatchAndBuffer']['_XWidth'] = abs(
            tmp1[0][0][0][0][0]['_XY_left'][0] - tmp2[0][0][0][0][0][0]['_XY_right'][0])
        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_XVTExten_PMOSOnSRLatchAndBuffer']['_XYCoordinates'] = [[0, 0]]
        ## Calculate Sref XYcoord
        tmpXY = []
        ## Calculate
        ## Target_coord: _XY_type1
        target_coord = tmp1[0][0][0][0][0]['_XY_down_left']
        ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_XVTExten_PMOSOnSRLatchAndBuffer')
        approaching_coord = tmp2[0][0]['_XY_down_left']
        ## Sref coord
        tmp3 = self.get_param_KJH4('BND_XVTExten_PMOSOnSRLatchAndBuffer')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define coordinates
        self._DesignParameter['BND_XVTExten_PMOSOnSRLatchAndBuffer']['_XYCoordinates'] = tmpXY
        #####################################################################################################################################

        ####### XVT Layer Extension On MOSFET
        #### XVT Extension on PMOSs of SRLatch and SA Output Buffers
        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_XVTExten_NMOSOnSRLatchAndBuffer'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping[_SAOutBufAndSRLatch_XVT][0],
            _Datatype=DesignParameters._LayerMapping[_SAOutBufAndSRLatch_XVT][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )
        ## Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('SRF_BufferX', 'SRF_Inverter1', 'SRF_NMOS', 'BND_{}Layer'.format(_SAOutBufAndSRLatch_XVT))
        tmp2 = self.get_param_KJH4('SRF_SRLatch', 'SRF_NANDR', 'SRF_Pulldown', 'SRF_NMOSB', 'BND_{}Layer'.format(_SAOutBufAndSRLatch_XVT))
        self._DesignParameter['BND_XVTExten_NMOSOnSRLatchAndBuffer']['_YWidth'] = max(tmp1[0][0][0][0][0]['_Ywidth'],tmp2[0][0][0][0][0][0]['_Ywidth'])

        ## Define Boundary_element _XWidth
        self._DesignParameter['BND_XVTExten_NMOSOnSRLatchAndBuffer']['_XWidth'] = abs(tmp1[0][0][0][0][0]['_XY_left'][0] - tmp2[0][0][0][0][0][0]['_XY_right'][0])
        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_XVTExten_NMOSOnSRLatchAndBuffer']['_XYCoordinates'] = [[0, 0]]
        ## Calculate Sref XYcoord
        tmpXY = []
        ## Calculate
        ## Target_coord: _XY_type1
        target_coord = tmp1[0][0][0][0][0]['_XY_up_left']
        ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_XVTExten_NMOSOnSRLatchAndBuffer')
        approaching_coord = tmp2[0][0]['_XY_up_left']
        ## Sref coord
        tmp3 = self.get_param_KJH4('BND_XVTExten_NMOSOnSRLatchAndBuffer')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define coordinates
        self._DesignParameter['BND_XVTExten_NMOSOnSRLatchAndBuffer']['_XYCoordinates'] = tmpXY
        #####################################################################################################################################

        ####### XVT Layer Extension On MOSFET
        #### XVT Extension on PMOSs of CLKLogic
        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_XVTExten_PMOSOnCLKInLogic'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping[_CompClkLogic_XVT][0],
            _Datatype=DesignParameters._LayerMapping[_CompClkLogic_XVT][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )
        ## Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('SRF_CLKBuffer', 'SRF_Inverter2', 'SRF_PMOS', 'BND_{}Layer'.format(_CompClkLogic_XVT))
        tmp2 = self.get_param_KJH4('SRF_Inv_CLKSamp', 'SRF_PMOS', 'BND_{}Layer'.format(_CompClkLogic_XVT))
        self._DesignParameter['BND_XVTExten_PMOSOnCLKInLogic']['_YWidth'] = max(tmp1[0][0][0][0][0]['_Ywidth'],tmp2[0][0][0][0]['_Ywidth'])

        ## Define Boundary_element _XWidth
        self._DesignParameter['BND_XVTExten_PMOSOnCLKInLogic']['_XWidth'] = abs(tmp1[0][0][0][0][0]['_XY_right'][0] - tmp2[0][0][0][0]['_XY_left'][0])
        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_XVTExten_PMOSOnCLKInLogic']['_XYCoordinates'] = [[0, 0]]
        ## Calculate Sref XYcoord
        tmpXY = []
        ## Calculate
        ## Target_coord: _XY_type1
        target_coord = tmp1[0][0][0][0][0]['_XY_down_right']
        ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_XVTExten_PMOSOnCLKInLogic')
        approaching_coord = tmp2[0][0]['_XY_up_left']
        ## Sref coord
        tmp3 = self.get_param_KJH4('BND_XVTExten_PMOSOnCLKInLogic')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define coordinates
        self._DesignParameter['BND_XVTExten_PMOSOnCLKInLogic']['_XYCoordinates'] = tmpXY
        #####################################################################################################################################

        #### XVT Extension on NMOSs of CLKLogic
        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_XVTExten_NMOSOnCLKInLogic'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping[_CompClkLogic_XVT][0],
            _Datatype=DesignParameters._LayerMapping[_CompClkLogic_XVT][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )
        ## Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('SRF_CLKBuffer', 'SRF_Inverter2', 'SRF_NMOS', 'BND_{}Layer'.format(_CompClkLogic_XVT))
        tmp2 = self.get_param_KJH4('SRF_Inv_CLKSamp', 'SRF_NMOS', 'BND_{}Layer'.format(_CompClkLogic_XVT))
        tmp3 = self.get_param_KJH4('SRF_AND_CLKIn','SRF_NAND','SRF_Pulldown','SRF_NMOSA','BND_{}Layer'.format(_CompClkLogic_XVT))
        tmp4 = self.get_param_KJH4('SRF_AND_CLKIn', 'SRF_NAND','SRF_Pulldown','SRF_NMOSB','BND_{}Layer'.format(_CompClkLogic_XVT))
        tmp5 = self.get_param_KJH4('SRF_AND_CLKIn', 'SRF_Inverter','SRF_NMOS','BND_{}Layer'.format(_CompClkLogic_XVT))
        self._DesignParameter['BND_XVTExten_NMOSOnCLKInLogic']['_YWidth'] = max(tmp1[0][0][0][0][0]['_Ywidth'],tmp2[0][0][0][0]['_Ywidth'],tmp3[0][0][0][0][0][0]['_Ywidth'],tmp4[0][0][0][0][0][0]['_Ywidth'],tmp5[0][0][0][0][0]['_Ywidth'])

        ## Define Boundary_element _XWidth
        self._DesignParameter['BND_XVTExten_NMOSOnCLKInLogic']['_XWidth'] = abs(tmp1[0][0][0][0][0]['_XY_right'][0] - tmp2[0][0][0][0]['_XY_left'][0])
        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_XVTExten_NMOSOnCLKInLogic']['_XYCoordinates'] = [[0, 0]]
        ## Calculate Sref XYcoord
        tmpXY = []
        ## Calculate
        ## Target_coord: _XY_type1
        target_coord = tmp1[0][0][0][0][0]['_XY_up_right']
        ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_XVTExten_NMOSOnCLKInLogic')
        approaching_coord = tmp2[0][0]['_XY_down_left']
        ## Sref coord
        tmp3 = self.get_param_KJH4('BND_XVTExten_NMOSOnCLKInLogic')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define coordinates
        self._DesignParameter['BND_XVTExten_NMOSOnCLKInLogic']['_XYCoordinates'] = tmpXY
        #####################################################################################################################################

        ####### NW Layer Extension On PMOS
        #### NW Extension on PMOSs of CLK Input logic
        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_NWellOnCLKInLogic'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['NWELL'][0],
            _Datatype=DesignParameters._LayerMapping['NWELL'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )
        ## Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('SRF_CLKBuffer', 'SRF_Inverter2', 'BND_PMOS_NellExten')
        tmp2 = self.get_param_KJH4('SRF_Inv_CLKSamp', 'BND_PMOS_NellExten')
        self._DesignParameter['BND_NWellOnCLKInLogic']['_YWidth'] = max(tmp1[0][0][0][0]['_Ywidth'], tmp2[0][0][0]['_Ywidth'])

        ## Define Boundary_element _XWidth
        tmp3 = self.get_param_KJH4('BND_Pbody_Hrz_RX')
        self._DesignParameter['BND_NWellOnCLKInLogic']['_XWidth'] = tmp3[0][0]['_Xwidth'] + 3*_DRCobj._NwMinEnclosureNactive + 30
        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_NWellOnCLKInLogic']['_XYCoordinates'] = [[0, 0]]
        ## Calculate Sref XYcoord
        tmpXY = []
        ## Calculate
        ## Target_coord: _XY_type1
        target_coord = tmp1[0][0][0][0]['_XY_down_right']
        ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_NWellOnCLKInLogic')
        approaching_coord = tmp2[0][0]['_XY_up_left']
        ## Sref coord
        tmp3 = self.get_param_KJH4('BND_NWellOnCLKInLogic')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define coordinates
        self._DesignParameter['BND_NWellOnCLKInLogic']['_XYCoordinates'] = tmpXY
        #####################################################################################################################################

        ####### NW Layer Extension On PMOS
        #### NW Extension on PMOSs of SRLatch & SA Output Buffer
        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_NWellOnSRLatchAndBuffer'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['NWELL'][0],
            _Datatype=DesignParameters._LayerMapping['NWELL'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )
        ## Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('SRF_BufferX', 'SRF_Inverter1', 'BND_PMOS_NellExten')
        tmp2 = self.get_param_KJH4('SRF_Inv_CLKSamp', 'BND_PMOS_NellExten')
        self._DesignParameter['BND_NWellOnSRLatchAndBuffer']['_YWidth'] = max(tmp1[0][0][0][0]['_Ywidth'], tmp2[0][0][0]['_Ywidth'])

        ## Define Boundary_element _XWidth
        tmp3 = self.get_param_KJH4('BND_NWellOnCLKInLogic')
        self._DesignParameter['BND_NWellOnSRLatchAndBuffer']['_XWidth'] = tmp3[0][0]['_Xwidth']

        ## Define Boundary_element _XYCoordinates
        self._DesignParameter['BND_NWellOnSRLatchAndBuffer']['_XYCoordinates'] = [[0, 0]]
        ## Calculate Sref XYcoord
        tmpXY = []
        ## Calculate
        ## Target_coord: _XY_type1
        target_coord = tmp1[0][0][0][0]['_XY_up_left']
        ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_NWellOnSRLatchAndBuffer')
        approaching_coord = tmp2[0][0]['_XY_up_left']
        ## Sref coord
        tmp3 = self.get_param_KJH4('BND_NWellOnSRLatchAndBuffer')
        Scoord = tmp3[0][0]['_XY_origin']
        ## Cal
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define coordinates
        self._DesignParameter['BND_NWellOnSRLatchAndBuffer']['_XYCoordinates'] = tmpXY
        #####################################################################################################################################

        ##### Slicer CLK Input Via M4 -> M6 Left & RightSide
        ## Sref generation: ViaX
            ## Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH3._ViaStack._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 4
        _Caculation_Parameters['_Layer2'] = 6
        _Caculation_Parameters['_COX'] = 1
        _Caculation_Parameters['_COY'] = 2

            ## Sref ViaX declaration
        self._DesignParameter['SRF_SlicerCLKInput_ViaM4M6'] = self._SrefElementDeclaration(_DesignObj=A02_ViaStack_KJH3._ViaStack(_DesignParameter=None, _Name='{}:SRF_CLKInput_ViaM4M6'.format(_Name)))[0]

            ## Define Sref Relection
        self._DesignParameter['SRF_SlicerCLKInput_ViaM4M6']['_Reflect'] = [0, 0, 0]

            ## Define Sref Angle
        self._DesignParameter['SRF_SlicerCLKInput_ViaM4M6']['_Angle'] = 0


            ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
        self._DesignParameter['SRF_SlicerCLKInput_ViaM4M6']['_DesignObj']._CalculateDesignParameterXmin(**_Caculation_Parameters)

            ## Calculate Sref XYcoord
        tmpXY = []
                ## initialized Sref coordinate
        self._DesignParameter['SRF_SlicerCLKInput_ViaM4M6']['_XYCoordinates'] = [[0, 0]]
                ## Calculate
                    ## Target_coord
        self._DesignParameter['SRF_Slicer']['_DesignObj']._DesignParameter['_VIAMet32Met4OnforCLKPNRouting']['_Reflect'] = [0, 0, 0]
        self._DesignParameter['SRF_Slicer']['_DesignObj']._DesignParameter['_VIAMet32Met4OnforCLKPNRouting']['_Angle'] = 0
        tmp1 = self.get_param_KJH3('SRF_Slicer','_VIAMet32Met4OnforCLKPNRouting')
        target_coord = tmp1[0][1][0]['_XY_cent']
                    ## Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_SlicerCLKInput_ViaM4M6','SRF_ViaM4M5','BND_Met4Layer')
        approaching_coord = tmp2[0][0][0][0]['_XY_cent']
                    ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_SlicerCLKInput_ViaM4M6')
        Scoord = tmp3[0][0]['_XY_origin']
                    ## Calculate1
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)

        ## Calculate2
        target_coord = tmp1[0][3][0]['_XY_cent']
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                ## Define
        self._DesignParameter['SRF_SlicerCLKInput_ViaM4M6']['_XYCoordinates'] = tmpXY
        #####################################################################################################################################

        ##### BND_SlicerCLKInput_Vtc_M6
        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_SlicerCLKInput_Vtc_M6'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL6'][0],
            _Datatype=DesignParameters._LayerMapping['METAL6'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )
        ## Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH3('SRF_Slicer','_GuardringVSS')
        tmp2 = self.get_param_KJH4('SRF_SlicerCLKInput_ViaM4M6','SRF_ViaM4M5','BND_Met4Layer')
        self._DesignParameter['BND_SlicerCLKInput_Vtc_M6']['_YWidth'] = abs(tmp1[0][0][0]['_XY_cent'][1] - tmp2[0][0][0][0]['_XY_up'][1])

        ## Define Boundary_element _XWidth
        self._DesignParameter['BND_SlicerCLKInput_Vtc_M6']['_XWidth'] = tmp2[0][0][0][0]['_Xwidth']

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['BND_SlicerCLKInput_Vtc_M6']['_XYCoordinates'] = [[0, 0]]
        ## Calculate1
        ## Target_coord: _XY_type1
        tmp1 = self.get_param_KJH4('SRF_SlicerCLKInput_ViaM4M6','SRF_ViaM4M5','BND_Met4Layer')
        target_coord = tmp1[0][0][0][0]['_XY_up_left']
        ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_SlicerCLKInput_Vtc_M6')
        approaching_coord = tmp2[0][0]['_XY_up_left']
        ## Sref coord
        tmp3 = self.get_param_KJH4('BND_SlicerCLKInput_Vtc_M6')
        Scoord = tmp3[0][0]['_XY_origin']
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Calculate2
        target_coord = tmp1[1][0][0][0]['_XY_up_left']
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define coordinates
        self._DesignParameter['BND_SlicerCLKInput_Vtc_M6']['_XYCoordinates'] = tmpXY
        #####################################################################################################################################

        ##### Slicer CLK Input Via M6 -> M5
        ## Sref generation: ViaX
            ## Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH3._ViaStack._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 5
        _Caculation_Parameters['_Layer2'] = 6
        _Caculation_Parameters['_COX'] = 2
        _Caculation_Parameters['_COY'] = 1

            ## Sref ViaX declaration
        self._DesignParameter['SRF_SlicerCLKInput_ViaM5M6'] = self._SrefElementDeclaration(_DesignObj=A02_ViaStack_KJH3._ViaStack(_DesignParameter=None, _Name='{}:SRF_SlicerCLKInput_ViaM5M6'.format(_Name)))[0]

            ## Define Sref Relection
        self._DesignParameter['SRF_SlicerCLKInput_ViaM5M6']['_Reflect'] = [0, 0, 0]

            ## Define Sref Angle
        self._DesignParameter['SRF_SlicerCLKInput_ViaM5M6']['_Angle'] = 0


            ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
        self._DesignParameter['SRF_SlicerCLKInput_ViaM5M6']['_DesignObj']._CalculateDesignParameterYmin(**_Caculation_Parameters)

            ## Calculate Sref XYcoord
        tmpXY = []
                ## initialized Sref coordinate
        self._DesignParameter['SRF_SlicerCLKInput_ViaM5M6']['_XYCoordinates'] = [[0, 0]]
                ## Calculate
                    ## Target_coord
        tmp1 = self.get_param_KJH4('BND_SlicerCLKInput_Vtc_M6')
        target_coord = tmp1[0][0]['_XY_down_left']
                    ## Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_SlicerCLKInput_ViaM5M6','SRF_ViaM5M6','BND_Met5Layer')
        approaching_coord = tmp2[0][0][0][0]['_XY_down_left']
                    ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_SlicerCLKInput_ViaM5M6')
        Scoord = tmp3[0][0]['_XY_origin']
                    ## Calculate1
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)

        ## Calculate2
        target_coord = tmp1[1][0]['_XY_down_right']
        approaching_coord = tmp2[0][0][0][0]['_XY_down_right']
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                ## Define
        self._DesignParameter['SRF_SlicerCLKInput_ViaM5M6']['_XYCoordinates'] = tmpXY
        #####################################################################################################################################

        ##### BND_SlicerCLKInput_Hrz_M5
        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_SlicerCLKInput_Hrz_M5'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL5'][0],
            _Datatype=DesignParameters._LayerMapping['METAL5'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )
        ## Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('SRF_SlicerCLKInput_ViaM5M6','SRF_ViaM5M6','BND_Met5Layer')
        self._DesignParameter['BND_SlicerCLKInput_Hrz_M5']['_YWidth'] = tmp1[0][0][0][0]['_Ywidth']

        ## Define Boundary_element _XWidth
        self._DesignParameter['BND_SlicerCLKInput_Hrz_M5']['_XWidth'] = abs(tmp1[0][0][0][0]['_XY_left'][0] - tmp1[1][0][0][0]['_XY_right'][0])

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['BND_SlicerCLKInput_Hrz_M5']['_XYCoordinates'] = [[0, 0]]
        ## Calculate1
        ## Target_coord: _XY_type1
        target_coord = tmp1[0][0][0][0]['_XY_down_left']
        ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_SlicerCLKInput_Hrz_M5')
        approaching_coord = tmp2[0][0]['_XY_down_left']
        ## Sref coord
        tmp3 = self.get_param_KJH4('BND_SlicerCLKInput_Hrz_M5')
        Scoord = tmp3[0][0]['_XY_origin']
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define coordinates
        self._DesignParameter['BND_SlicerCLKInput_Hrz_M5']['_XYCoordinates'] = tmpXY
        #####################################################################################################################################

        ##### Slicer CLK Input Via M5 -> M3
        ## Sref generation: ViaX
            ## Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH3._ViaStack._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] = 3
        _Caculation_Parameters['_Layer2'] = 5
        _Caculation_Parameters['_COX'] = 2
        _Caculation_Parameters['_COY'] = 1

            ## Sref ViaX declaration
        self._DesignParameter['SRF_SlicerCLKInput_ViaM3M5'] = self._SrefElementDeclaration(_DesignObj=A02_ViaStack_KJH3._ViaStack(_DesignParameter=None, _Name='{}:SRF_SlicerCLKInput_ViaM3M5'.format(_Name)))[0]

            ## Define Sref Relection
        self._DesignParameter['SRF_SlicerCLKInput_ViaM3M5']['_Reflect'] = [0, 0, 0]

            ## Define Sref Angle
        self._DesignParameter['SRF_SlicerCLKInput_ViaM3M5']['_Angle'] = 0


            ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
        self._DesignParameter['SRF_SlicerCLKInput_ViaM3M5']['_DesignObj']._CalculateDesignParameterYmin(**_Caculation_Parameters)

            ## Calculate Sref XYcoord
        tmpXY = []
                ## initialized Sref coordinate
        self._DesignParameter['SRF_SlicerCLKInput_ViaM3M5']['_XYCoordinates'] = [[0, 0]]
                ## Calculate
                    ## Target_coord
        tmp1 = self.get_param_KJH4('BND_SlicerCLKInput_Hrz_M5')
        target_coord = tmp1[0][0]['_XY_cent']
                    ## Approaching_coord
        tmp2 = self.get_param_KJH4('SRF_SlicerCLKInput_ViaM3M5','SRF_ViaM3M4','BND_Met3Layer')
        approaching_coord = tmp2[0][0][0][0]['_XY_cent']
                    ## Sref coord
        tmp3 = self.get_param_KJH4('SRF_SlicerCLKInput_ViaM3M5')
        Scoord = tmp3[0][0]['_XY_origin']
                    ## Calculate1
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
                ## Define
        self._DesignParameter['SRF_SlicerCLKInput_ViaM3M5']['_XYCoordinates'] = tmpXY
        #####################################################################################################################################

        ##### BND_SlicerCLKInput_Hrz_M3
        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_SlicerCLKInput_Hrz_M3'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3'][0],
            _Datatype=DesignParameters._LayerMapping['METAL3'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )
        ## Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('SRF_SlicerCLKInput_ViaM3M5','SRF_ViaM3M4','BND_Met3Layer')
        self._DesignParameter['BND_SlicerCLKInput_Hrz_M3']['_YWidth'] = tmp1[0][0][0][0]['_Ywidth']

        ## Define Boundary_element _XWidth
        tmp2 = self.get_param_KJH4('SRF_CLKBuffer','SRF_Inverter2','BND_Out_Vtc_M2')
        self._DesignParameter['BND_SlicerCLKInput_Hrz_M3']['_XWidth'] = abs(tmp1[0][0][0][0]['_XY_left'][0] - tmp2[0][0][0][0]['_XY_left'][0])

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['BND_SlicerCLKInput_Hrz_M3']['_XYCoordinates'] = [[0, 0]]
        ## Calculate1
        ## Target_coord: _XY_type1
        target_coord = tmp1[0][0][0][0]['_XY_down_left']
        ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_SlicerCLKInput_Hrz_M3')
        approaching_coord = tmp2[0][0]['_XY_down_left']
        ## Sref coord
        tmp3 = self.get_param_KJH4('BND_SlicerCLKInput_Hrz_M3')
        Scoord = tmp3[0][0]['_XY_origin']
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define coordinates
        self._DesignParameter['BND_SlicerCLKInput_Hrz_M3']['_XYCoordinates'] = tmpXY
        #####################################################################################################################################
        ##### BND_SlicerCLKInput_Hrz_M3
        ## Boundary_element Generation
        ## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['BND_SlicerCLKInput_Vtc_M3'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3'][0],
            _Datatype=DesignParameters._LayerMapping['METAL3'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )
        ## Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH4('BND_SlicerCLKInput_Hrz_M3')
        tmp2 = self.get_param_KJH4('SRF_CLKBuffer','SRF_Inv2Output_ViaM1M3','SRF_ViaM2M3','BND_Met3Layer')
        self._DesignParameter['BND_SlicerCLKInput_Vtc_M3']['_YWidth'] = tmp1[0][0]['_XY_up'][1] - tmp2[0][0][0][0][0]['_XY_down'][1]

        ## Define Boundary_element _XWidth
        tmp2 = self.get_param_KJH4('BND_SlicerCLKInput_Hrz_M3')
        self._DesignParameter['BND_SlicerCLKInput_Vtc_M3']['_XWidth'] = tmp2[0][0]['_Ywidth']

        ## Calculate Sref XYcoord
        tmpXY = []
        ## initialized Sref coordinate
        self._DesignParameter['BND_SlicerCLKInput_Vtc_M3']['_XYCoordinates'] = [[0, 0]]
        ## Calculate1
        ## Target_coord: _XY_type1
        target_coord = tmp1[0][0]['_XY_up_right']
        ## Approaching_coord: _XY_type2
        tmp2 = self.get_param_KJH4('BND_SlicerCLKInput_Vtc_M3')
        approaching_coord = tmp2[0][0]['_XY_up_right']
        ## Sref coord
        tmp3 = self.get_param_KJH4('BND_SlicerCLKInput_Vtc_M3')
        Scoord = tmp3[0][0]['_XY_origin']
        New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
        tmpXY.append(New_Scoord)
        ## Define coordinates
        self._DesignParameter['BND_SlicerCLKInput_Vtc_M3']['_XYCoordinates'] = tmpXY


        #####################################################################################################################################
        ## Body 공유로 인한 삭제 (삭제하지 않으면 CA가 겹쳐 DRC 발생 우려 있음.)
        del(self._DesignParameter['SRF_Inv_CLKSamp']['_DesignObj']._DesignParameter['SRF_Pbody'])
        del(self._DesignParameter['SRF_Inv_CLKSrc']['_DesignObj']._DesignParameter['SRF_Pbody'])
        del(self._DesignParameter['SRF_CLKBuffer']['_DesignObj']._DesignParameter['SRF_Inverter1']['_DesignObj']._DesignParameter['SRF_Pbody'])
        del(self._DesignParameter['SRF_CLKBuffer']['_DesignObj']._DesignParameter['SRF_Inverter2']['_DesignObj']._DesignParameter['SRF_Pbody'])
        del(self._DesignParameter['SRF_AND_CLKIn']['_DesignObj']._DesignParameter['SRF_NAND']['_DesignObj']._DesignParameter['SRF_Pbody'])
        del(self._DesignParameter['SRF_AND_CLKIn']['_DesignObj']._DesignParameter['SRF_Inverter']['_DesignObj']._DesignParameter['SRF_Pbody'])

        #####################################################################################################################################
        print('##############################')
        print('##     Calculation_End      ##')
        print('##############################')
        E01_05_StrongArmWtSRLatch_end_time = time.time()
        self.E01_05_StrongArmWtSRLatch_elapsed_time = E01_05_StrongArmWtSRLatch_end_time - E01_05_StrongArmWtSRLatch_start_time
        #####################################################################################################################################

############################################################################################################################################################ START MAIN
if __name__ == '__main__':

    ''' Check Time'''
    start_time = time.time()

    from KJH91_Projects.Project_ADC.Library_and_Engine.Private import MyInfo
    from KJH91_Projects.Project_ADC.Library_and_Engine import DRCchecker_KJH0

    libname = 'Proj_ZZ01_E01_05_StrongArmWtSRLatch_Fixed'
    cellname = 'E01_SALatchWtSRLatch'
    _fileName = cellname + '.gds'

    ''' Input Parameters for Layout Object ''' ############################################################### ^^^^^^^^^^^^^^^^^^^^^
    InputParams = dict(
## Comparator
    ## StrongARM Latch
        # Common
        _SALatch_ChannelLength=30,  # random.randrange(30, 60, 2),  # 30
        _SALatch_XVT='HVT',

        # PMOS
        _SALatch_CLKinputPMOSFinger1=1,  #PMOS Reset Sw1 # random.randint(1, 15),  # 6
        _SALatch_CLKinputPMOSFinger2=1,  #PMOS Reset Sw2 # random.randint(1, 15),  # 3
        _SALatch_PMOSFinger=1,  		  #PMOS Latch	  # random.randint(1, 15),  # 3
        _SALatch_PMOSChannelWidth=1000,  #All PMOS width # random.randrange(200, 1050, 2),  # 500

        # NMOS
        _SALatch_DATAinputNMOSFinger=3,  #NMOS Input Tr # random.randint(3, 15),  # 12
        _SALatch_NMOSFinger=2,  		  #NMOS at Latch # random.randint(1, 15),  # 2
        _SALatch_CLKinputNMOSFinger=1,  #NMOS Tail # random.randint(1, 15),  # 8
        _SALatch_NMOSChannelWidth=330,  #Nmos width # random.randrange(200, 1050, 2),  # 500
        _SALatch_CLKinputNMOSChannelWidth=200,  # random.randrange(200, 1050, 2),  # 800

    ## StrongArmOutBuffer and SRLatch
        ## Common
            # XVT
            _SAOutBufAndSRLatch_XVT='SLVT',
            # Body
            _SAOutBufAndSRLatch_NMOS_Pbody_XvtTop2Pbody=None,  # Number/None(Minimum)
            _SAOutBufAndSRLatch_PMOS_Nbody_Xvtdown2Nbody=None,  # Number/None(Minimum)
            # Height
            _SAOutBufAndSRLatch_PMOSXvt2NMOSXvt=1800,  # number
        ## StronArm Output Buffer
            ## Inverter1(pre)
                    #Nmos
                _SAOutBuf_Buf_Inv1_NMOS_NumberofGate          = 1,        # Number
                _SAOutBuf_Buf_Inv1_NMOS_ChannelWidth          = 400,      # Number
                _SAOutBuf_Buf_Inv1_NMOS_ChannelLength         = 30,       # Number
                    #Pmos
                _SAOutBuf_Buf_Inv1_PMOS_NumberofGate          = 1,        # Number
                _SAOutBuf_Buf_Inv1_PMOS_ChannelWidth          = 800,      # Number
                _SAOutBuf_Buf_Inv1_PMOS_ChannelLength         = 30,       # Number
            ## Inverter2
                    #Nmos
                _SAOutBuf_Buf_Inv2_NMOS_NumberofGate          = 2,        # Number
                _SAOutBuf_Buf_Inv2_NMOS_ChannelWidth          = 400,      # Number
                _SAOutBuf_Buf_Inv2_NMOS_ChannelLength         = 30,       # Number
                    #Pmos
                _SAOutBuf_Buf_Inv2_PMOS_NumberofGate          = 2,        # Number
                _SAOutBuf_Buf_Inv2_PMOS_ChannelWidth          = 800,      # Number
                _SAOutBuf_Buf_Inv2_PMOS_ChannelLength         = 30,       # Number
        ## SRLatch
            ## Nand(Set,Rst same)
                # NmosA
                _SRLatch_Nand_NMOSA_NumberofGate=1,  # Number
                _SRLatch_Nand_NMOSA_ChannelWidth=100,  # Number
                _SRLatch_Nand_NMOSA_ChannelLength=30,  # Number
                # NMOSB
                _SRLatch_Nand_NMOSB_NumberofGate=2,  # Number
                _SRLatch_Nand_NMOSB_ChannelWidth=750,  # Number
                _SRLatch_Nand_NMOSB_ChannelLength=30,  # Number
                # PMOSA
                _SRLatch_Nand_PMOSA_NumberofGate=2,  # Number
                _SRLatch_Nand_PMOSA_ChannelWidth=100,  # Number
                _SRLatch_Nand_PMOSA_ChannelLength=30,  # Number
                # PMOSB
                _SRLatch_Nand_PMOSB_NumberofGate=1,  # Number
                _SRLatch_Nand_PMOSB_ChannelWidth=750,  # Number
                _SRLatch_Nand_PMOSB_ChannelLength=30,  # Number

    ## Comp clock Gen Logic: Clk_Samp Inv, Clk_Source Inv, AND Gate, CompClockBuff
        ## Common
            # XVT
            _CompClkLogic_XVT='SLVT',
            # Body
            _CompClkLogic_NMOS_Pbody_XvtTop2Pbody=None,  # Number/None(Minimum)
            _CompClkLogic_PMOS_Nbody_Xvtdown2Nbody=None,  # Number/None(Minimum)
            # Height
            _CompClkLogic_PMOSXvt2NMOSXvt=1800,  # number
        ## StronArm Output Buffer
            ## Inverter1(pre)
                    #Nmos
                _CompClkLogic_Buf_Inv1_NMOS_NumberofGate          = 2,        # Number
                _CompClkLogic_Buf_Inv1_NMOS_ChannelWidth          = 400,      # Number
                _CompClkLogic_Buf_Inv1_NMOS_ChannelLength         = 30,       # Number
                    #Pmos
                _CompClkLogic_Buf_Inv1_PMOS_NumberofGate          = 2,        # Number
                _CompClkLogic_Buf_Inv1_PMOS_ChannelWidth          = 800,      # Number
                _CompClkLogic_Buf_Inv1_PMOS_ChannelLength         = 30,       # Number
            ## Inverter2
                    #Nmos
                _CompClkLogic_Buf_Inv2_NMOS_NumberofGate          = 4,        # Number
                _CompClkLogic_Buf_Inv2_NMOS_ChannelWidth          = 400,      # Number
                _CompClkLogic_Buf_Inv2_NMOS_ChannelLength         = 30,       # Number
                    #Pmos
                _CompClkLogic_Buf_Inv2_PMOS_NumberofGate          = 4,        # Number
                _CompClkLogic_Buf_Inv2_PMOS_ChannelWidth          = 800,      # Number
                _CompClkLogic_Buf_Inv2_PMOS_ChannelLength         = 30,       # Number
        ## AND
            ## Nand
                # NmosA
                _CompClkLogic_Nand_NMOSA_NumberofGate=1,  # Number
                _CompClkLogic_Nand_NMOSA_ChannelWidth=100,  # Number
                _CompClkLogic_Nand_NMOSA_ChannelLength=30,  # Number
                # NMOSB
                _CompClkLogic_Nand_NMOSB_NumberofGate=2,  # Number
                _CompClkLogic_Nand_NMOSB_ChannelWidth=750,  # Number
                _CompClkLogic_Nand_NMOSB_ChannelLength=30,  # Number
                # PMOSA
                _CompClkLogic_Nand_PMOSA_NumberofGate=1,  # Number
                _CompClkLogic_Nand_PMOSA_ChannelWidth=300,  # Number
                _CompClkLogic_Nand_PMOSA_ChannelLength=30,  # Number
                # PMOSB
                _CompClkLogic_Nand_PMOSB_NumberofGate=3,  # Number
                _CompClkLogic_Nand_PMOSB_ChannelWidth=750,  # Number
                _CompClkLogic_Nand_PMOSB_ChannelLength=30,  # Number
            ## Inverter
                # Nmos
                _CompClkLogic_Inv_NMOS_NumberofGate=1,  # Number
                _CompClkLogic_Inv_NMOS_ChannelWidth=100,  # Number
                _CompClkLogic_Inv_NMOS_ChannelLength=30,  # Number
                # Pmos
                _CompClkLogic_Inv_PMOS_NumberofGate=1,  # Number
                _CompClkLogic_Inv_PMOS_ChannelWidth=200,  # Number
                _CompClkLogic_Inv_PMOS_ChannelLength=30,  # Number

        ## Clk_Source Inv
                #Nmos
            _CompClkLogic_ClkSrc_NMOS_NumberofGate          = 1,        # Number
            _CompClkLogic_ClkSrc_NMOS_ChannelWidth          = 400,      # Number
            _CompClkLogic_ClkSrc_NMOS_ChannelLength         = 30,       # Number
                #Pmos
            _CompClkLogic_ClkSrc_PMOS_NumberofGate          = 1,        # Number
            _CompClkLogic_ClkSrc_PMOS_ChannelWidth          = 800,      # Number
            _CompClkLogic_ClkSrc_PMOS_ChannelLength         = 30,       # Number
        ## Clk_Samp Inv
                #Nmos
            _CompClkLogic_ClkSmp_NMOS_NumberofGate          = 1,        # Number
            _CompClkLogic_ClkSmp_NMOS_ChannelWidth          = 400,      # Number
            _CompClkLogic_ClkSmp_NMOS_ChannelLength         = 30,       # Number
                #Pmos
            _CompClkLogic_ClkSmp_PMOS_NumberofGate          = 1,        # Number
            _CompClkLogic_ClkSmp_PMOS_ChannelWidth          = 800,      # Number
            _CompClkLogic_ClkSmp_PMOS_ChannelLength         = 30,       # Number

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
    LayoutObj = _StrongArmWtSRLatch(_DesignParameter=None, _Name=cellname)
    LayoutObj._CalculateDesignParameter(**InputParams)
    LayoutObj._UpdateDesignParameter2GDSStructure(_DesignParameterInDictionary=LayoutObj._DesignParameter)
    testStreamFile = open('./{}'.format(_fileName), 'wb')
    tmp = LayoutObj._CreateGDSStream(LayoutObj._DesignParameter['_GDSFile']['_GDSFile'])
    tmp.write_binary_gds_stream(testStreamFile)
    testStreamFile.close()

    # TestObj = _StrongArmLatch(_DesignParameter=None, _Name=cellname)
    # TestObj._CalculateDesignParameter(**InputParams)
    # print(TestObj._DesignParameter)
    # print(TestObj._DesignParameter)
    # TestObj._UpdateDesignParameter2GDSStructure(_DesignParameterInDictionary={'_Name': {'_DesignParametertype': 5, '_Name': 'E01_SALatch_v0'},
    #  '_GDSFile': {'_DesignParametertype': 4, '_GDSFile': None}, 'BND_test':LayoutObj._DesignParameter.get('BND_test')})
    # testStreamFile = open('./{}'.format(_fileName), 'wb')
    # tmp = TestObj._CreateGDSStream(LayoutObj._DesignParameter['_GDSFile']['_GDSFile'])
    # tmp.write_binary_gds_stream(testStreamFile)
    # testStreamFile.close()

    ''' Check Time'''
    elapsed_time = time.time() - start_time
    m, s = divmod(elapsed_time,60)
    h, m = divmod(m, 60)

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

    print ('#############################      Finished      ################################')
    print('{} Hours   {} minutes   {} seconds'.format(h, m, s))

    # end of 'main():' ---------------------------------------------------------------------------------------------

