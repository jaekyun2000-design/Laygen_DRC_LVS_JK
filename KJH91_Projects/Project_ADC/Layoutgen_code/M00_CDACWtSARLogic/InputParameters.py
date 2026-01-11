import json
''' Input Parameters for Layout Object '''
InputParams = dict(
    _NumofBit=6,
    _CDAC_Folding=False,  # None/True/False
    _Driver_CommonCentroidPlacementIfCDACFolded=False,  # 말 그대로 True이면 CommmonCentroid 배치가 됨.
    _Driver_DecimationIfDriverPlacedInCommonCentroid=False,
    _Driver_DecimationFactor=[2, 0, 0, 0, 0, 0, 0],  # [MSB, MSB-1 ... MSB-x]: 단 X<MSB  # 위 옵션 True시 작동; MSB부터 벡터로 작성; [3,2,2] 시 MSB0 -> 3:1, MSB1 -> 2:1, MSB2 -> 2:1, ... 1은 불가
    _SpaceBtwBootSWPosNeg=200,  # Fixed

    ## SAR Logic sizing
    _Test_distance=330,  # Fixed
    _Routing_width=50,  # Fixed
    _Routing_distance=80,  # Fixed

    _SARLogic_YWidthOfCLKSrc=100,  # Fixed (CLK spine)
    _SARLogic_SpaceBtwCLKSrcAndCLKSamp=100,  # Fixed (Dist. CLK spine and CLK_Samp)
    _SARLogic_YWidthOfCLKSamp=100,  # Fixed (CLK spine)

    _SARLogic_YWidthOfCompOut=100,  # Fixed
    _SARLogic_SpaceBtwCompOutAndCLKDout=100,  # Fixed
    _SARLogic_YWidthOfCLKDout=100,  # Fixed

    ## DFF Common
    _SARLogic_DFF_Pbody_NumCont=2,  # number (Fixed)
    _SARLogic_DFF_Nbody_NumCont=2,  # number (Fixed)
    _SARLogic_DFF_PMOSXvt2NMOSXvt=1150,  # number (Fixed)
    _SARLogic_DFF_XvtTop2Pbody=None,  # number/None(Minimum) (Fixed)
    _SARLogic_DFF_Xvtdown2Nbody=None,  # number/None(Minimum) (Fixed)

    ## Master Xgate1
    ## Xgate common

    ## Xgate NMOS
    _SARLogic_Mst_Xgate1_NMOS_NumberofGate=1,  # 1
    _SARLogic_Mst_Xgate1_NMOS_ChannelWidth=400,  # 400
    _SARLogic_Mst_Xgate1_NMOS_ChannelLength=30,  # 30
    _SARLogic_Mst_Xgate1_NMOS_XVT='SLVT',
    _SARLogic_Mst_Xgate1_NMOS_POGate_Comb_length=100,  # (Fixed)

    ## Xgate PMOS
    _SARLogic_Mst_Xgate1_PMOS_NumberofGate=1,  # 1
    _SARLogic_Mst_Xgate1_PMOS_ChannelWidth=800,  # 200
    _SARLogic_Mst_Xgate1_PMOS_ChannelLength=30,
    _SARLogic_Mst_Xgate1_PMOS_XVT='SLVT',
    _SARLogic_Mst_Xgate1_PMOS_POGate_Comb_length=100,  # (Fixed)

    ## Master Xgate2
    ## Xgate common

    ## Xgate NMOS
    _SARLogic_Mst_Xgate2_NMOS_NumberofGate=1,
    _SARLogic_Mst_Xgate2_NMOS_ChannelWidth=400,
    _SARLogic_Mst_Xgate2_NMOS_ChannelLength=30,
    _SARLogic_Mst_Xgate2_NMOS_XVT='SLVT',
    _SARLogic_Mst_Xgate2_NMOS_POGate_Comb_length=100,  # (Fixed)

    ## Xgate PMOS
    _SARLogic_Mst_Xgate2_PMOS_NumberofGate=1,
    _SARLogic_Mst_Xgate2_PMOS_ChannelWidth=800,
    _SARLogic_Mst_Xgate2_PMOS_ChannelLength=30,
    _SARLogic_Mst_Xgate2_PMOS_XVT='SLVT',
    _SARLogic_Mst_Xgate2_PMOS_POGate_Comb_length=100,  # (Fixed)

    ## Master Nor1
    ## Nor1 common

    ## NMOS
    ## NMOS common
    _SARLogic_Mst_Nor1_NMOS_XVT='SLVT',

    ## NMOSA
    _SARLogic_Mst_Nor1_NMOSA_NumberofGate=4,
    _SARLogic_Mst_Nor1_NMOSA_ChannelWidth=400,
    _SARLogic_Mst_Nor1_NMOSA_ChannelLength=30,
    _SARLogic_Mst_Nor1_NMOSA_POGate_Comb_length=100,  # (Fixed)

    ## NMOSB
    _SARLogic_Mst_Nor1_NMOSB_NumberofGate=4,
    _SARLogic_Mst_Nor1_NMOSB_ChannelWidth=400,
    _SARLogic_Mst_Nor1_NMOSB_ChannelLength=30,
    _SARLogic_Mst_Nor1_NMOSB_POGate_Comb_length=100,  # (Fixed)

    ## PMOS
    ## PMOS common
    _SARLogic_Mst_Nor1_PMOS_XVT='SLVT',

    ## PMOSA
    _SARLogic_Mst_Nor1_PMOSA_NumberofGate=8,
    _SARLogic_Mst_Nor1_PMOSA_ChannelWidth=800,
    _SARLogic_Mst_Nor1_PMOSA_ChannelLength=30,
    _SARLogic_Mst_Nor1_PMOSA_POGate_Comb_length=100,  # (Fixed)

    ## PMOSB
    _SARLogic_Mst_Nor1_PMOSB_NumberofGate=8,
    _SARLogic_Mst_Nor1_PMOSB_ChannelWidth=800,
    _SARLogic_Mst_Nor1_PMOSB_ChannelLength=30,
    _SARLogic_Mst_Nor1_PMOSB_POGate_Comb_length=100,  # (Fixed)

    ## Master Nor2
    ## Nor2 common

    ## NMOS
    ## NMOS common
    _SARLogic_Mst_Nor2_NMOS_XVT='SLVT',

    ## NMOSA
    _SARLogic_Mst_Nor2_NMOSA_NumberofGate=1,
    _SARLogic_Mst_Nor2_NMOSA_ChannelWidth=400,
    _SARLogic_Mst_Nor2_NMOSA_ChannelLength=30,
    _SARLogic_Mst_Nor2_NMOSA_POGate_Comb_length=100,  # (Fixed)

    ## NMOSB
    _SARLogic_Mst_Nor2_NMOSB_NumberofGate=1,
    _SARLogic_Mst_Nor2_NMOSB_ChannelWidth=400,
    _SARLogic_Mst_Nor2_NMOSB_ChannelLength=30,
    _SARLogic_Mst_Nor2_NMOSB_POGate_Comb_length=100,  # (Fixed)

    ## PMOS
    ## PMOS common
    _SARLogic_Mst_Nor2_PMOS_XVT='SLVT',

    ## PMOSA
    _SARLogic_Mst_Nor2_PMOSA_NumberofGate=2,
    _SARLogic_Mst_Nor2_PMOSA_ChannelWidth=800,
    _SARLogic_Mst_Nor2_PMOSA_ChannelLength=30,
    _SARLogic_Mst_Nor2_PMOSA_POGate_Comb_length=100,  # (Fixed)

    ## PMOSB
    _SARLogic_Mst_Nor2_PMOSB_NumberofGate=2,
    _SARLogic_Mst_Nor2_PMOSB_ChannelWidth=800,
    _SARLogic_Mst_Nor2_PMOSB_ChannelLength=30,
    _SARLogic_Mst_Nor2_PMOSB_POGate_Comb_length=100,  # (Fixed)

    ## Master Inv1 : Set pre-driver
    ## Inv1 common

    ## Inv1 NMOS
    _SARLogic_Mst_Inv1_NMOS_NumberofGate=1,
    _SARLogic_Mst_Inv1_NMOS_ChannelWidth=400,
    _SARLogic_Mst_Inv1_NMOS_ChannelLength=30,
    _SARLogic_Mst_Inv1_NMOS_XVT='SLVT',
    _SARLogic_Mst_Inv1_NMOS_POGate_Comb_length=100,  # (Fixed)

    ## Inv1 PMOS
    _SARLogic_Mst_Inv1_PMOS_NumberofGate=1,
    _SARLogic_Mst_Inv1_PMOS_ChannelWidth=800,
    _SARLogic_Mst_Inv1_PMOS_ChannelLength=30,
    _SARLogic_Mst_Inv1_PMOS_XVT='SLVT',
    _SARLogic_Mst_Inv1_PMOS_POGate_Comb_length=100,  # (Fixed)

    ## Master Inv2 : Set driver
    ## Inv2 common

    ## Inv2 NMOS
    _SARLogic_Mst_Inv2_NMOS_NumberofGate=2,
    _SARLogic_Mst_Inv2_NMOS_ChannelWidth=400,
    _SARLogic_Mst_Inv2_NMOS_ChannelLength=30,
    _SARLogic_Mst_Inv2_NMOS_XVT='SLVT',
    _SARLogic_Mst_Inv2_NMOS_POGate_Comb_length=100,  # (Fixed)

    ## Inv2 PMOS
    _SARLogic_Mst_Inv2_PMOS_NumberofGate=2,
    _SARLogic_Mst_Inv2_PMOS_ChannelWidth=800,
    _SARLogic_Mst_Inv2_PMOS_ChannelLength=30,
    _SARLogic_Mst_Inv2_PMOS_XVT='SLVT',
    _SARLogic_Mst_Inv2_PMOS_POGate_Comb_length=100,  # (Fixed)

    ## Master Inv3 : Clock driver
    ## Inv3 common

    ## Inv3 NMOS
    _SARLogic_Mst_Inv3_NMOS_NumberofGate=2,
    _SARLogic_Mst_Inv3_NMOS_ChannelWidth=400,
    _SARLogic_Mst_Inv3_NMOS_ChannelLength=30,
    _SARLogic_Mst_Inv3_NMOS_XVT='SLVT',
    _SARLogic_Mst_Inv3_NMOS_POGate_Comb_length=100,  # (Fixed)

    ## Inv3 PMOS
    _SARLogic_Mst_Inv3_PMOS_NumberofGate=2,
    _SARLogic_Mst_Inv3_PMOS_ChannelWidth=800,
    _SARLogic_Mst_Inv3_PMOS_ChannelLength=30,
    _SARLogic_Mst_Inv3_PMOS_XVT='SLVT',
    _SARLogic_Mst_Inv3_PMOS_POGate_Comb_length=100,  # (Fixed)

    ## Slave Xgate1
    ## Xgate common

    ## Xgate NMOS
    _SARLogic_Slv_Xgate1_NMOS_NumberofGate=3,
    _SARLogic_Slv_Xgate1_NMOS_ChannelWidth=400,
    _SARLogic_Slv_Xgate1_NMOS_ChannelLength=30,
    _SARLogic_Slv_Xgate1_NMOS_XVT='SLVT',
    _SARLogic_Slv_Xgate1_NMOS_POGate_Comb_length=100,  # (Fixed)

    ## Xgate PMOS
    _SARLogic_Slv_Xgate1_PMOS_NumberofGate=3,
    _SARLogic_Slv_Xgate1_PMOS_ChannelWidth=800,
    _SARLogic_Slv_Xgate1_PMOS_ChannelLength=30,
    _SARLogic_Slv_Xgate1_PMOS_XVT='SLVT',
    _SARLogic_Slv_Xgate1_PMOS_POGate_Comb_length=100,  # (Fixed)

    ## Slave Xgate2
    ## Xgate common

    ## Xgate NMOS
    _SARLogic_Slv_Xgate2_NMOS_NumberofGate=2,
    _SARLogic_Slv_Xgate2_NMOS_ChannelWidth=400,
    _SARLogic_Slv_Xgate2_NMOS_ChannelLength=30,
    _SARLogic_Slv_Xgate2_NMOS_XVT='SLVT',
    _SARLogic_Slv_Xgate2_NMOS_POGate_Comb_length=100,  # (Fixed)

    ## Xgate PMOS
    _SARLogic_Slv_Xgate2_PMOS_NumberofGate=2,
    _SARLogic_Slv_Xgate2_PMOS_ChannelWidth=800,
    _SARLogic_Slv_Xgate2_PMOS_ChannelLength=30,
    _SARLogic_Slv_Xgate2_PMOS_XVT='SLVT',
    _SARLogic_Slv_Xgate2_PMOS_POGate_Comb_length=100,  # (Fixed)

    ## Slave Nor1
    ## Nor1 common

    ## NMOS
    ## NMOS common
    _SARLogic_Slv_Nor1_NMOS_XVT='SLVT',

    ## NMOSA
    _SARLogic_Slv_Nor1_NMOSA_NumberofGate=6,
    _SARLogic_Slv_Nor1_NMOSA_ChannelWidth=400,
    _SARLogic_Slv_Nor1_NMOSA_ChannelLength=30,
    _SARLogic_Slv_Nor1_NMOSA_POGate_Comb_length=100,  # (Fixed)

    ## NMOSB
    _SARLogic_Slv_Nor1_NMOSB_NumberofGate=6,
    _SARLogic_Slv_Nor1_NMOSB_ChannelWidth=400,
    _SARLogic_Slv_Nor1_NMOSB_ChannelLength=30,
    _SARLogic_Slv_Nor1_NMOSB_POGate_Comb_length=100,  # (Fixed)

    ## PMOS
    ## PMOS common
    _SARLogic_Slv_Nor1_PMOS_XVT='SLVT',

    ## PMOSA
    _SARLogic_Slv_Nor1_PMOSA_NumberofGate=12,
    _SARLogic_Slv_Nor1_PMOSA_ChannelWidth=800,
    _SARLogic_Slv_Nor1_PMOSA_ChannelLength=30,
    _SARLogic_Slv_Nor1_PMOSA_POGate_Comb_length=100,  # (Fixed)

    ## PMOSB
    _SARLogic_Slv_Nor1_PMOSB_NumberofGate=12,
    _SARLogic_Slv_Nor1_PMOSB_ChannelWidth=800,
    _SARLogic_Slv_Nor1_PMOSB_ChannelLength=30,
    _SARLogic_Slv_Nor1_PMOSB_POGate_Comb_length=100,  # (Fixed)

    ## Slave Nor2
    ## Nor2 common

    ## NMOS
    ## NMOS common
    _SARLogic_Slv_Nor2_NMOS_XVT='SLVT',

    ## NMOSA
    _SARLogic_Slv_Nor2_NMOSA_NumberofGate=2,
    _SARLogic_Slv_Nor2_NMOSA_ChannelWidth=400,
    _SARLogic_Slv_Nor2_NMOSA_ChannelLength=30,
    _SARLogic_Slv_Nor2_NMOSA_POGate_Comb_length=100,  # (Fixed)

    ## NMOSB
    _SARLogic_Slv_Nor2_NMOSB_NumberofGate=2,
    _SARLogic_Slv_Nor2_NMOSB_ChannelWidth=400,
    _SARLogic_Slv_Nor2_NMOSB_ChannelLength=30,
    _SARLogic_Slv_Nor2_NMOSB_POGate_Comb_length=100,  # (Fixed)

    ## PMOS
    ## PMOS common
    _SARLogic_Slv_Nor2_PMOS_XVT='SLVT',

    ## PMOSA
    _SARLogic_Slv_Nor2_PMOSA_NumberofGate=4,
    _SARLogic_Slv_Nor2_PMOSA_ChannelWidth=800,
    _SARLogic_Slv_Nor2_PMOSA_ChannelLength=30,
    _SARLogic_Slv_Nor2_PMOSA_POGate_Comb_length=100,  # (Fixed)

    ## PMOSB
    _SARLogic_Slv_Nor2_PMOSB_NumberofGate=4,
    _SARLogic_Slv_Nor2_PMOSB_ChannelWidth=800,
    _SARLogic_Slv_Nor2_PMOSB_ChannelLength=30,
    _SARLogic_Slv_Nor2_PMOSB_POGate_Comb_length=100,  # (Fixed)

    ## Slave Inv1 : ReSet pre-driver
    ## Inv1 common

    ## Inv1 NMOS
    _SARLogic_Slv_Inv1_NMOS_NumberofGate=1,
    _SARLogic_Slv_Inv1_NMOS_ChannelWidth=400,
    _SARLogic_Slv_Inv1_NMOS_ChannelLength=30,
    _SARLogic_Slv_Inv1_NMOS_XVT='SLVT',
    _SARLogic_Slv_Inv1_NMOS_POGate_Comb_length=100,  # (Fixed)

    ## Inv1 PMOS
    _SARLogic_Slv_Inv1_PMOS_NumberofGate=1,
    _SARLogic_Slv_Inv1_PMOS_ChannelWidth=800,
    _SARLogic_Slv_Inv1_PMOS_ChannelLength=30,
    _SARLogic_Slv_Inv1_PMOS_XVT='SLVT',
    _SARLogic_Slv_Inv1_PMOS_POGate_Comb_length=100,  # (Fixed)

    ## Slave Inv2 : ReSet driver
    ## Inv2 common

    ## Inv2 NMOS
    _SARLogic_Slv_Inv2_NMOS_NumberofGate=2,
    _SARLogic_Slv_Inv2_NMOS_ChannelWidth=400,
    _SARLogic_Slv_Inv2_NMOS_ChannelLength=30,
    _SARLogic_Slv_Inv2_NMOS_XVT='SLVT',
    _SARLogic_Slv_Inv2_NMOS_POGate_Comb_length=100,  # (Fixed)

    ## Inv2 PMOS
    _SARLogic_Slv_Inv2_PMOS_NumberofGate=2,
    _SARLogic_Slv_Inv2_PMOS_ChannelWidth=800,
    _SARLogic_Slv_Inv2_PMOS_ChannelLength=30,
    _SARLogic_Slv_Inv2_PMOS_XVT='SLVT',
    _SARLogic_Slv_Inv2_PMOS_POGate_Comb_length=100,  # (Fixed)

    ## Slave Inv3 : Qb driver
    ## Inv3 common

    ## Inv3 NMOS
    _SARLogic_Slv_Inv3_NMOS_NumberofGate=4,
    _SARLogic_Slv_Inv3_NMOS_ChannelWidth=400,
    _SARLogic_Slv_Inv3_NMOS_ChannelLength=30,
    _SARLogic_Slv_Inv3_NMOS_XVT='SLVT',
    _SARLogic_Slv_Inv3_NMOS_POGate_Comb_length=100,  # (Fixed)

    ## Inv3 PMOS
    _SARLogic_Slv_Inv3_PMOS_NumberofGate=4,
    _SARLogic_Slv_Inv3_PMOS_ChannelWidth=800,
    _SARLogic_Slv_Inv3_PMOS_ChannelLength=30,
    _SARLogic_Slv_Inv3_PMOS_XVT='SLVT',
    _SARLogic_Slv_Inv3_PMOS_POGate_Comb_length=100,  # (Fixed)

    # Top Clock  Tree Size
    _SARLogic_CLKBufTreeTop_NumOfStage=4,
    _SARLogic_CLKBufTreeTop_CLKSampBuf_SizeByStage=[1, 1, 1, 1],
    _SARLogic_CLKBufTreeTop_CLKSrcBuf_SizeByStage=[1, 1, 1, 1],  # 스테이지에 따른 버퍼 사이즈(UnitBuffer의 배수로 각 스테이지의 크기가 결정 됨.)
    _SARLogic_CLKBufTreeTop_XOffSet=0,  # (8Bit DRC check:-79, 10Bit DRC Check:0, 12Bit:)

    ## Top CLK Buffer Tree Sizeq
    _SARLogic_CLKBufTreeTop_Inv_NMOS_ChannelWidth=400,  # Number
    _SARLogic_CLKBufTreeTop_Inv_NMOS_ChannelLength=30,  # Number
    _SARLogic_CLKBufTreeTop_Inv_NMOS_NumberofGate=1,  # Number
    _SARLogic_CLKBufTreeTop_Inv_NMOS_XVT='SLVT',  # 'XVT' ex)SLVT/LVT/RVT/HVT
    _SARLogic_CLKBufTreeTop_Inv_NMOS_POGate_Comb_length=100,  # None/Number #(Fixed)

    _SARLogic_CLKBufTreeTop_Inv_PMOS_ChannelWidth=800,  # Number
    _SARLogic_CLKBufTreeTop_Inv_PMOS_ChannelLength=30,  # Number
    _SARLogic_CLKBufTreeTop_Inv_PMOS_NumberofGate=1,  # Number
    _SARLogic_CLKBufTreeTop_Inv_PMOS_XVT='SLVT',  # 'XVT' ex)SLVT/LVT/RVT/HVT
    _SARLogic_CLKBufTreeTop_Inv_PMOS_POGate_Comb_length=100,  # None/Number #(Fixed)

    # Top CLK BufferPowerRail Size
    _SARLogic_CLKBufTreeTop_NMOS_Pbody_NumCont=2,  # (Fixed)
    _SARLogic_CLKBufTreeTop_NMOS_Pbody_XvtTop2Pbody=None,  # (Fixed)
    _SARLogic_CLKBufTreeTop_PMOS_Nbody_NumCont=2,  # (Fixed)
    _SARLogic_CLKBufTreeTop_PMOS_Nbody_Xvtdown2Nbody=None,  # (Fixed)
    _SARLogic_CLKBufTreeTop_PMOSXvt2NMOSXvt=446,  # (Fixed)

    # Bottom Clock  Tree Size
    _SARLogic_CLKBufTreeBot_NumOfStage=4,
    _SARLogic_CLKBufTreeBot_CompOutBuf_SizeByStage=[1, 1, 1, 1],
    _SARLogic_CLKBufTreeBot_CLKDoutBuf_SizeByStage=[1, 1, 1, 1],
    # 스테이지에 따른 버퍼 사이즈(UnitBuffer의 배수로 각 스테이지의 크기가 결정 됨.)
    _SARLogic_CLKBufTreeBot_XOffSet=0,  # (DRC check)

    ## Bottom CLK Buffer Tree Size
    _SARLogic_CLKBufTreeBot_Inv_NMOS_ChannelWidth=400,  # Number
    _SARLogic_CLKBufTreeBot_Inv_NMOS_ChannelLength=30,  # Number
    _SARLogic_CLKBufTreeBot_Inv_NMOS_NumberofGate=1,  # Number
    _SARLogic_CLKBufTreeBot_Inv_NMOS_XVT='SLVT',  # 'XVT' ex)SLVT/LVT/RVT/HVT
    _SARLogic_CLKBufTreeBot_Inv_NMOS_POGate_Comb_length=100,  # None/Number #(Fixed)

    _SARLogic_CLKBufTreeBot_Inv_PMOS_ChannelWidth=800,  # Number
    _SARLogic_CLKBufTreeBot_Inv_PMOS_ChannelLength=30,  # Number
    _SARLogic_CLKBufTreeBot_Inv_PMOS_NumberofGate=1,  # Number
    _SARLogic_CLKBufTreeBot_Inv_PMOS_XVT='SLVT',  # 'XVT' ex)SLVT/LVT/RVT/HVT
    _SARLogic_CLKBufTreeBot_Inv_PMOS_POGate_Comb_length=100,  # None/Number #(Fixed)

    # Bottom CLK Buffer PowerRail Size
    _SARLogic_CLKBufTreeBot_NMOS_Pbody_NumCont=2,  # (Fixed)
    _SARLogic_CLKBufTreeBot_NMOS_Pbody_XvtTop2Pbody=None,  # (Fixed)
    _SARLogic_CLKBufTreeBot_PMOS_Nbody_NumCont=2,  # (Fixed)
    _SARLogic_CLKBufTreeBot_PMOS_Nbody_Xvtdown2Nbody=None,  # (Fixed)
    _SARLogic_CLKBufTreeBot_PMOSXvt2NMOSXvt=446,  # (Fixed)

    #### CDAC Pre-Driver Sizing
    ## InvChain Common
    _CDACPreDriver_Pbody_NumCont=2,  # number #(Fixed)
    _CDACPreDriver_Nbody_NumCont=2,  # number #(Fixed)
    _CDACPreDriver_PMOSXvt2NMOSXvt=500,  # number #(Fixed)
    _CDACPreDriver_XvtTop2Pbody=None,  # number/None(Minimum) #(Fixed)
    _CDACPreDriver_Xvtdown2Nbody=None,  # number/None(Minimum) #(Fixed)

    ## Inverter Chain
    ## Inv1 common
    _CDACPreDriver_NumberofGate=[1, 1],  # Vector
    _CDACPreDriver_ChannelLength=30,  # Scalar
    _CDACPreDriver_XVT='SLVT',  # 'SLVT'

    ## Inv1 NMOS
    _CDACPreDriver_Inv_NMOS_ChannelWidth=400,  # Scalar
    _CDACPreDriver_Inv_NMOS_POGate_Comb_length=100,  # Scalar #(Fixed)

    ## Inv1 PMOS
    _CDACPreDriver_Inv_PMOS_ChannelWidth=800,  # Scalar
    _CDACPreDriver_Inv_PMOS_POGate_Comb_length=100,  # Scalar

    ## CLKDout(OutSamp) Inverter & AND Common Option
    _CLKDout_XVT_Common='SLVT',

    ## CLKDout(OutSamp) Inverter Size
    _CLKDout_Inv_NMOS_ChannelWidth=400,
    # Number (== _CLKDout_AND_NAND_NMOS_ChannelWidth,_CLKDout_AND_Inv_NMOS_ChannelWidth)
    _CLKDout_Inv_NMOS_ChannelLength=30,  # Number
    _CLKDout_Inv_NMOS_NumberofGate=1,  # Number
    _CLKDout_Inv_NMOS_POGate_Comb_length=100,  # None/Number

    _CLKDout_Inv_PMOS_ChannelWidth=800,
    # Number (== _CLKDout_AND_NAND_PMOS_ChannelWidth ,_CLKDout_AND_Inv_PMOS_ChannelWidth )
    _CLKDout_Inv_PMOS_ChannelLength=30,  # Number
    _CLKDout_Inv_PMOS_NumberofGate=1,  # Number
    _CLKDout_Inv_PMOS_POGate_Comb_length=100,  # None/Number

    ## CLKDout(OutSamp) AND Size
    _CLKDout_AND_NAND_NMOS_ChannelWidth=400,
    _CLKDout_AND_NAND_NMOS_ChannelLength=30,
    _CLKDout_AND_NAND_NMOS_NumberofGate=2,

    _CLKDout_AND_NAND_PMOS_ChannelWidth=800,
    _CLKDout_AND_NAND_PMOS_ChannelLength=30,
    _CLKDout_AND_NAND_PMOS_NumberofGate=1,

    _CLKDout_AND_Inv_NMOS_ChannelWidth=400,
    _CLKDout_AND_Inv_NMOS_ChannelLength=30,
    _CLKDout_AND_Inv_NMOS_NumberofGate=1,
    _CLKDout_AND_Inv_NMOS_POGate_Comb_length=100,

    _CLKDout_AND_Inv_PMOS_ChannelWidth=800,
    _CLKDout_AND_Inv_PMOS_ChannelLength=30,
    _CLKDout_AND_Inv_PMOS_NumberofGate=1,
    _CLKDout_AND_Inv_PMOS_POGate_Comb_length=100,

    ## StrongARM Latch
    _Comp_SALatch_CLKinputPMOSFinger1=6,  # random.randint(1, 15),  # 6
    _Comp_SALatch_CLKinputPMOSFinger2=6,  # random.randint(1, 15),  # 3
    _Comp_SALatch_PMOSFinger=6,  # random.randint(1, 15),  # 3
    _Comp_SALatch_PMOSChannelWidth=350,  # random.randrange(200, 1050, 2),  # 500
    _Comp_SALatch_DATAinputNMOSFinger=3,  # random.randint(3, 15),  # 12
    _Comp_SALatch_NMOSFinger=3,  # random.randint(1, 15),  # 2
    _Comp_SALatch_CLKinputNMOSFinger=3,  # random.randint(1, 15),  # 8
    _Comp_SALatch_NMOSChannelWidth=350,  # random.randrange(200, 1050, 2),  # 500
    _Comp_SALatch_CLKinputNMOSChannelWidth=350,  # random.randrange(200, 1050, 2),  # 800
    _Comp_SALatch_ChannelLength=30,  # random.randrange(30, 60, 2),  # 30
    _Comp_SALatch_Dummy=True,  # (Fixed)
    _Comp_SALatch_XVT='HVT',
    _Comp_SALatch_GuardringWidth=150,  # (Fixed)
    _Comp_SALatch_Guardring=True,  # (Fixed)
    _Comp_SALatch_SlicerGuardringWidth=150,  # (Fixed)
    _Comp_SALatch_SlicerGuardring=None,  # (Fixed)
    _Comp_SALatch_NumSupplyCOY=None,  # (Fixed)
    _Comp_SALatch_NumSupplyCOX=None,  # (Fixed)
    _Comp_SALatch_SupplyMet1XWidth=None,  # (Fixed)
    _Comp_SALatch_SupplyMet1YWidth=None,  # (Fixed)
    _Comp_SALatch_VDD2VSSHeight=None,  # (Fixed)
    _Comp_SALatch_NumVIAPoly2Met1COX=None,  # (Fixed)
    _Comp_SALatch_NumVIAPoly2Met1COY=None,  # (Fixed)
    _Comp_SALatch_NumVIAMet12COX=None,  # (Fixed)
    _Comp_SALatch_NumVIAMet12COY=None,  # (Fixed)
    _Comp_SALatch_PowerLine=False,  # (Fixed)

    ## StrongARMLatch Output Buffer Sizing
    # Inverter1
    _Comp_SAOutBuf_Inv1_NMOS_ChannelWidth=400,  # Number
    _Comp_SAOutBuf_Inv1_NMOS_ChannelLength=30,  # Number
    _Comp_SAOutBuf_Inv1_NMOS_NumberofGate=1,  # Number
    _Comp_SAOutBuf_Inv1_NMOS_XVT='SLVT',  # 'XVT' ex)SLVT/LVT/RVT/HVT
    _Comp_SAOutBuf_Inv1_NMOS_POGate_Comb_length=100,  # None/Number #(Fixed)

    _Comp_SAOutBuf_Inv1_PMOS_ChannelWidth=800,  # Number
    _Comp_SAOutBuf_Inv1_PMOS_ChannelLength=30,  # Number
    _Comp_SAOutBuf_Inv1_PMOS_NumberofGate=1,  # Number
    _Comp_SAOutBuf_Inv1_PMOS_XVT='SLVT',  # 'XVT' ex)SLVT/LVT/RVT/HVT
    _Comp_SAOutBuf_Inv1_PMOS_POGate_Comb_length=100,  # None/Number #(Fixed)

    # Inverter2
    _Comp_SAOutBuf_Inv2_NMOS_ChannelWidth=400,  # Number
    _Comp_SAOutBuf_Inv2_NMOS_ChannelLength=30,  # Number
    _Comp_SAOutBuf_Inv2_NMOS_NumberofGate=1,  # Number
    _Comp_SAOutBuf_Inv2_NMOS_XVT='SLVT',  # 'XVT' ex)SLVT/LVT/RVT/HVT
    _Comp_SAOutBuf_Inv2_NMOS_POGate_Comb_length=100,  # None/Number #(Fixed)

    _Comp_SAOutBuf_Inv2_PMOS_ChannelWidth=800,  # Number
    _Comp_SAOutBuf_Inv2_PMOS_ChannelLength=30,  # Number
    _Comp_SAOutBuf_Inv2_PMOS_NumberofGate=1,  # Number
    _Comp_SAOutBuf_Inv2_PMOS_XVT='SLVT',  # 'XVT' ex)SLVT/LVT/RVT/HVT
    _Comp_SAOutBuf_Inv2_PMOS_POGate_Comb_length=100,  # None/Number #(Fixed)

    ## SR Latch Size
    _Comp_SRLatch_NAND_NMOS_ChannelWidth=400,  # Number
    _Comp_SRLatch_NAND_NMOS_ChannelLength=30,  # Number
    _Comp_SRLatch_NAND_NMOS_NumberofGate=2,  # Number
    _Comp_SRLatch_NAND_NMOS_XVT='SLVT',  # 'XVT' ex)SLVT/LVT/RVT/HVT
    _Comp_SRLatch_NAND_NMOS_POGate_Comb_length=100,  # None/Number #(Fixed)

    _Comp_SRLatch_NAND_PMOS_ChannelWidth=800,  # Number
    _Comp_SRLatch_NAND_PMOS_ChannelLength=30,  # Number
    _Comp_SRLatch_NAND_PMOS_NumberofGate=1,  # Number
    _Comp_SRLatch_NAND_PMOS_XVT='SLVT',  # 'XVT' ex)SLVT/LVT/RVT/HVT
    _Comp_SRLatch_NAND_PMOS_POGate_Comb_length=100,  # None/Number #(Fixed)

    # CLK Input Logic Gates
    _Comp_CLKSamp_Inv_NMOS_ChannelWidth=400,
    _Comp_CLKSamp_Inv_NMOS_ChannelLength=30,
    _Comp_CLKSamp_Inv_NMOS_NumberofGate=1,
    _Comp_CLKSamp_Inv_NMOS_XVT='SLVT',
    _Comp_CLKSamp_Inv_NMOS_POGate_Comb_length=100,  # (Fixed)

    _Comp_CLKSamp_Inv_PMOS_ChannelWidth=800,
    _Comp_CLKSamp_Inv_PMOS_ChannelLength=30,
    _Comp_CLKSamp_Inv_PMOS_NumberofGate=1,
    _Comp_CLKSamp_Inv_PMOS_XVT='SLVT',
    _Comp_CLKSamp_Inv_PMOS_POGate_Comb_length=100,  # (Fixed)

    _Comp_CLKSrc_Inv_NMOS_ChannelWidth=400,
    _Comp_CLKSrc_Inv_NMOS_ChannelLength=30,
    _Comp_CLKSrc_Inv_NMOS_NumberofGate=1,
    _Comp_CLKSrc_Inv_NMOS_XVT='SLVT',
    _Comp_CLKSrc_Inv_NMOS_POGate_Comb_length=100,  # (Fixed)

    _Comp_CLKSrc_Inv_PMOS_ChannelWidth=800,
    _Comp_CLKSrc_Inv_PMOS_ChannelLength=30,
    _Comp_CLKSrc_Inv_PMOS_NumberofGate=1,
    _Comp_CLKSrc_Inv_PMOS_XVT='SLVT',
    _Comp_CLKSrc_Inv_PMOS_POGate_Comb_length=100,  # (Fixed)

    ## CLKSrc & CLKSample AND Gate
    _Comp_AND_NAND_NMOS_ChannelWidth=400,
    _Comp_AND_NAND_NMOS_ChannelLength=30,
    _Comp_AND_NAND_NMOS_NumberofGate=2,
    _Comp_AND_NAND_NMOS_XVT='SLVT',

    _Comp_AND_NAND_PMOS_ChannelWidth=800,
    _Comp_AND_NAND_PMOS_ChannelLength=30,
    _Comp_AND_NAND_PMOS_NumberofGate=1,
    _Comp_AND_NAND_PMOS_XVT='SLVT',

    _Comp_AND_Inv_NMOS_ChannelWidth=400,
    _Comp_AND_Inv_NMOS_ChannelLength=30,
    _Comp_AND_Inv_NMOS_NumberofGate=1,
    _Comp_AND_Inv_NMOS_XVT='SLVT',
    _Comp_AND_Inv_NMOS_POGate_Comb_length=100,  # (Fixed)

    _Comp_AND_Inv_PMOS_ChannelWidth=800,
    _Comp_AND_Inv_PMOS_ChannelLength=30,
    _Comp_AND_Inv_PMOS_NumberofGate=1,
    _Comp_AND_Inv_PMOS_XVT='SLVT',
    _Comp_AND_Inv_PMOS_POGate_Comb_length=100,  # (Fixed)

    ## CLK Buffer
    # Inverter1
    _Comp_CLKBuf_Inv1_NMOS_ChannelWidth=400,  # Number
    _Comp_CLKBuf_Inv1_NMOS_ChannelLength=30,  # Number
    _Comp_CLKBuf_Inv1_NMOS_NumberofGate=2,  # Number
    _Comp_CLKBuf_Inv1_NMOS_XVT='SLVT',  # 'XVT' ex)SLVT/LVT/RVT/HVT
    _Comp_CLKBuf_Inv1_NMOS_POGate_Comb_length=100,  # None/Number #(Fixed)

    _Comp_CLKBuf_Inv1_PMOS_ChannelWidth=800,  # Number
    _Comp_CLKBuf_Inv1_PMOS_ChannelLength=30,  # Number
    _Comp_CLKBuf_Inv1_PMOS_NumberofGate=2,  # Number
    _Comp_CLKBuf_Inv1_PMOS_XVT='SLVT',  # 'XVT' ex)SLVT/LVT/RVT/HVT
    _Comp_CLKBuf_Inv1_PMOS_POGate_Comb_length=100,  # None/Number #(Fixed)

    # Inverter2
    _Comp_CLKBuf_Inv2_NMOS_ChannelWidth=400,  # Number
    _Comp_CLKBuf_Inv2_NMOS_ChannelLength=30,  # Number
    _Comp_CLKBuf_Inv2_NMOS_NumberofGate=4,  # Number
    _Comp_CLKBuf_Inv2_NMOS_XVT='SLVT',  # 'XVT' ex)SLVT/LVT/RVT/HVT
    _Comp_CLKBuf_Inv2_NMOS_POGate_Comb_length=100,  # None/Number #(Fixed)

    _Comp_CLKBuf_Inv2_PMOS_ChannelWidth=800,  # Number
    _Comp_CLKBuf_Inv2_PMOS_ChannelLength=30,  # Number
    _Comp_CLKBuf_Inv2_PMOS_NumberofGate=4,  # Number
    _Comp_CLKBuf_Inv2_PMOS_XVT='SLVT',  # 'XVT' ex)SLVT/LVT/RVT/HVT
    _Comp_CLKBuf_Inv2_PMOS_POGate_Comb_length=100,  # None/Number #(Fixed)

    # PowerRail Placement
    _Comp_BufSR_NMOS_Pbody_NumCont=2,  # (Fixed)
    _Comp_BufSR_NMOS_Pbody_XvtTop2Pbody=600,  # (Fixed)
    _Comp_BufSR_PMOS_Nbody_NumCont=2,  # (Fixed)
    _Comp_BufSR_PMOS_Nbody_Xvtdown2Nbody=1000,  # (Fixed)
    _Comp_BufSR_PMOSXvt2NMOSXvt=1000,

    _Comp_CLKInLogic_NMOS_Pbody_Xvtdown2Pbody=1000,  # (Fixed)
    _Comp_CLKInLogic_PMOS_Nbody_NumCont=2,  # (Fixed)
    _Comp_CLKInLogic_PMOS_Nbody_Xvtdown2Nbody=1000,  # (Fixed)
    _Comp_CLKInLogic_PMOSXvt2NMOSXvt=1000,

    # Additional Buffer Between CLK_Sample Input of Comparator And Output of Tree Buffer
    ## InvChain Common
    _Buf_CLKSamp_Pbody_NumCont=2,  # number #(Fixed)
    _Buf_CLKSamp_Nbody_NumCont=2,  # number #(Fixed)
    _Buf_CLKSamp_PMOSXvt2NMOSXvt=500,  # number
    _Buf_CLKSamp_XvtTop2Pbody=None,  # number/None(Minimum) #(Fixed)
    _Buf_CLKSamp_Xvtdown2Nbody=None,  # number/None(Minimum) #(Fixed)

    ## Inverter Chain
    ## Inv1 common
    _Buf_CLKSamp_NumberofGate=[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],  # Vector
    _Buf_CLKSamp_ChannelLength=30,  # Scalar
    _Buf_CLKSamp_XVT='SLVT',  # 'SLVT'

    ## Inv1 NMOS
    _Buf_CLKSamp_Inv_NMOS_ChannelWidth=400,  # Scalar
    _Buf_CLKSamp_Inv_NMOS_POGate_Comb_length=100,  # Scalar #(Fixed)

    ## Inv1 PMOS
    _Buf_CLKSamp_Inv_PMOS_ChannelWidth=800,  # Scalar
    _Buf_CLKSamp_Inv_PMOS_POGate_Comb_length=100,  # Scalar #(Fixed)

    # Additional Buffer Between CLK_Source Input of Comparator And Output of Tree Buffer
    ## InvChain Common
    _Buf_CLKSrc_Pbody_NumCont=2,  # number #(Fixed)
    _Buf_CLKSrc_Nbody_NumCont=2,  # number #(Fixed)
    _Buf_CLKSrc_PMOSXvt2NMOSXvt=500,  # number
    _Buf_CLKSrc_XvtTop2Pbody=None,  # number/None(Minimum) #(Fixed)
    _Buf_CLKSrc_Xvtdown2Nbody=None,  # number/None(Minimum) #(Fixed)

    ## Inverter Chain
    ## Inv1 common
    _Buf_CLKSrc_NumberofGate=[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],  # Vector
    _Buf_CLKSrc_ChannelLength=30,  # Scalar
    _Buf_CLKSrc_XVT='SLVT',  # 'SLVT'

    ## Inv1 NMOS
    _Buf_CLKSrc_Inv_NMOS_ChannelWidth=400,  # Scalar
    _Buf_CLKSrc_Inv_NMOS_POGate_Comb_length=100,  # Scalar #(Fixed)

    ## Inv1 PMOS
    _Buf_CLKSrc_Inv_PMOS_ChannelWidth=800,  # Scalar
    _Buf_CLKSrc_Inv_PMOS_POGate_Comb_length=100,  # Scalar #(Fixed)

    # Additional Buffer Between Output of Comparator  And Input of Tree Buffer
    ## InvChain Common
    _Buf_CompOut_Pbody_NumCont=2,  # number #(Fixed)
    _Buf_CompOut_Nbody_NumCont=2,  # number #(Fixed)
    _Buf_CompOut_PMOSXvt2NMOSXvt=500,  # number
    _Buf_CompOut_XvtTop2Pbody=None,  # number/None(Minimum) #(Fixed)
    _Buf_CompOut_Xvtdown2Nbody=None,  # number/None(Minimum) #(Fixed)

    ## Inv1 common
    _Buf_CompOut_NumberofGate=[1, 1],  # Vector
    _Buf_CompOut_ChannelLength=30,  # Scalar
    _Buf_CompOut_XVT='SLVT',  # 'SLVT'

    ## Inv1 NMOS
    _Buf_CompOut_Inv_NMOS_ChannelWidth=400,  # Scalar
    _Buf_CompOut_Inv_NMOS_POGate_Comb_length=100,  # Scalar #(Fixed)

    ## Inv1 PMOS
    _Buf_CompOut_Inv_PMOS_ChannelWidth=800,  # Scalar
    _Buf_CompOut_Inv_PMOS_POGate_Comb_length=100,  # Scalar #(Fixed)

    # # Element CDAC
    _CDAC_LayoutOption=[5, 6],
    _CDAC_ShieldingLayer=4,  # Poly:0, M1:1, M2:2 ...
    _CDAC_MetalWidth=50,
    _CDAC_MetalLength=2920,  # (8bit size: 1414/ 10bit size: 2800/ 12bit size: 4200)
    _CDAC_MetalSpacing=50,

    # #Unit Cap
    _CDAC_NumOfElement=2,  # (매우 복잡..) Driver Common Centroid가 아니면 1// 맞으면 2

    # # Shielding & Top Connect node
    _CDAC_ConnectLength=400,
    _CDAC_ExtendLength=400,

    # # Dummy Cap Option
    _CDAC_DummyCap_TopBottomShort=None,
    # True => Top - Bottom Short, False -> Bottom = GND, None => Floating Bottom Node
    _CDAC_NumOfDummyCaps=10,  # Number of dummy cap(one side)

    # # CommonCentroid With Driving node
    _CDAC_CapArrayWDrivingNodeDistance=2000,  # DRC Rule
    _CDAC_DriveNodeDistance=279,  #
    _CDAC_YWidth_Bottom_Hrz=50,

    # Driver Sizing
    _Driver_SizeByBit=[1, 1, 1, 1, 1, 1],  # Drv.CCPlacement == False일때 사용됨.

    # Driver(Inverter) NMOS
    _Driver_NMOS_NumberofGate=1,  # number
    _Driver_NMOS_ChannelWidth=400,  # number (8bit size: 340/ 10bit size: 680/ 12bit size: 1020)
    _Driver_NMOS_Channellength=30,  # number
    _Driver_NMOS_XVT='SLVT',  # 'XVT' ex)SLVT LVT RVT HVT

    # Driver(Inverter) PMOS
    _Driver_PMOS_NumberofGate=1,  # number
    _Driver_PMOS_ChannelWidth=800,  # number (8bit size: 900/ 10bit size: 1800/ 12bit size: 2700)
    _Driver_PMOS_Channellength=30,  # number
    _Driver_PMOS_XVT='SLVT',  # 'XVT' ex)SLVT LVT RVT HVT

    #### Bootstrap Sampler
    # Tr1 and Tr2
    # Tr1
    _Samp_Tr1Tr2_Tr1_NMOSNumberofGate=1,  # number
    _Samp_Tr1Tr2_Tr1_NMOSChannelWidth=100,  # number
    _Samp_Tr1Tr2_Tr1_NMOSChannellength=30,  # number
    _Samp_Tr1Tr2_Tr1_GateSpacing=222,  # None/number
    _Samp_Tr1Tr2_Tr1_SDWidth=None,  # None/number
    _Samp_Tr1Tr2_Tr1_XVT='HVT',  # 'XVT' ex)SLVT LVT RVT HVT
    _Samp_Tr1Tr2_Tr1_PCCrit=True,  # None/True

    # Source_node_ViaM1M2
    _Samp_Tr1Tr2_Tr1_Source_Via_TF=False,  # True/False

    # Drain_node_ViaM1M2
    _Samp_Tr1Tr2_Tr1_Drain_Via_TF=False,  # True/False

    # POLY dummy setting
    _Samp_Tr1Tr2_Tr1_NMOSDummy=True,  # TF
    # if _PMOSDummy == True
    _Samp_Tr1Tr2_Tr1_NMOSDummy_length=None,  # None/Value
    _Samp_Tr1Tr2_Tr1_NMOSDummy_placement=None,  # None/'Up'/'Dn'/

    # Tr2
    _Samp_Tr1Tr2_Tr2_NMOSNumberofGate=2,  # number
    _Samp_Tr1Tr2_Tr2_NMOSChannelWidth=100,  # number
    _Samp_Tr1Tr2_Tr2_NMOSChannellength=30,  # number
    _Samp_Tr1Tr2_Tr2_GateSpacing=100,  # None/number
    _Samp_Tr1Tr2_Tr2_SDWidth=None,  # None/number
    _Samp_Tr1Tr2_Tr2_XVT='SLVT',  # 'XVT' ex)SLVT LVT RVT HVT
    _Samp_Tr1Tr2_Tr2_PCCrit=True,  # None/True

    # Source_node_ViaM1M2
    _Samp_Tr1Tr2_Tr2_Source_Via_TF=True,  # True/False

    # Drain_node_ViaM1M2
    _Samp_Tr1Tr2_Tr2_Drain_Via_TF=True,  # True/False

    # POLY dummy setting
    _Samp_Tr1Tr2_Tr2_NMOSDummy=True,  # TF
    # if _PMOSDummy == True
    _Samp_Tr1Tr2_Tr2_NMOSDummy_length=None,  # None/Value
    _Samp_Tr1Tr2_Tr2_NMOSDummy_placement=None,  # None/'Up'/'Dn'/

    # Input/Output node
    # INPUT node
    _Samp_Tr1Tr2_Inputnode_Metal_layer=6,  # number
    _Samp_Tr1Tr2_Inputnode_width=600,  # number

    # OUTPUT node
    _Samp_Tr1Tr2_Outputnode_Metal_layer=6,  # number
    _Samp_Tr1Tr2_Outputnode_width=600,  # number

    # Guardring
    # Pbody: number of contact
    # Nbody
    _Samp_Tr1Tr2_NwellWidth=850,  # number

    # Tr4
    _Samp_Tr4_NMOSNumberofGate=2,  # number
    _Samp_Tr4_NMOSChannelWidth=100,  # number
    _Samp_Tr4_NMOSChannellength=30,  # number
    _Samp_Tr4_GateSpacing=None,  # None/number
    _Samp_Tr4_SDWidth=None,  # None/number
    _Samp_Tr4_XVT='RVT',  # 'XVT' ex)SLVT LVT RVT HVT
    _Samp_Tr4_PCCrit=True,  # None/True

    # Source_node_ViaM1M2
    _Samp_Tr4_Source_Via_TF=True,  # True/False

    # Drain_node_ViaM1M2
    _Samp_Tr4_Drain_Via_TF=True,  # True/False

    # POLY dummy setting
    _Samp_Tr4_NMOSDummy=True,  # TF
    # if _PMOSDummy == True
    _Samp_Tr4_NMOSDummy_length=None,  # None/Value
    _Samp_Tr4_NMOSDummy_placement=None,  # None/'Up'/'Dn'/

    # Tr5 Tr7 Tr9
    # PMOS: Tr5
    _Samp_Tr5_PMOSNumberofGate=1,
    _Samp_Tr5_PMOSChannelWidth=200,  # ref=1000
    _Samp_Tr5_PMOSChannellength=30,
    _Samp_Tr5_GateSpacing=None,
    _Samp_Tr5_SDWidth=None,
    _Samp_Tr5_XVT='SLVT',
    _Samp_Tr5_PCCrit=None,

    # Source_node_ViaM1M2
    _Samp_Tr5_Source_Via_TF=True,

    # Drain_node_ViaM1M2
    _Samp_Tr5_Drain_Via_TF=True,

    # POLY dummy setting
    _Samp_Tr5_PMOSDummy=True,  # TF
    # if _PMOSDummy == True
    _Samp_Tr5_PMOSDummy_length=None,  # None/Value
    _Samp_Tr5_PMOSDummy_placement='Up',  # None/'Up'/'Dn'/

    # PMOS: Tr7
    _Samp_Tr7_PMOSNumberofGate=1,
    _Samp_Tr7_PMOSChannelWidth=200,
    _Samp_Tr7_PMOSChannellength=30,
    _Samp_Tr7_GateSpacing=None,
    _Samp_Tr7_SDWidth=None,
    _Samp_Tr7_XVT='SLVT',
    _Samp_Tr7_PCCrit=None,

    # Source_node_ViaM1M2
    _Samp_Tr7_Source_Via_TF=True,

    # Drain_node_ViaM1M2
    _Samp_Tr7_Drain_Via_TF=True,

    # POLY dummy setting
    _Samp_Tr7_PMOSDummy=True,  # TF
    # if _PMOSDummy == True
    _Samp_Tr7_PMOSDummy_length=None,  # None/Value
    _Samp_Tr7_PMOSDummy_placement='Up',  # None/'Up'/'Dn'/

    # PMOS: Tr9
    _Samp_Tr9_PMOSNumberofGate=1,
    _Samp_Tr9_PMOSChannelWidth=200,  # ref = 1000
    _Samp_Tr9_PMOSChannellength=30,
    _Samp_Tr9_GateSpacing=None,
    _Samp_Tr9_SDWidth=None,
    _Samp_Tr9_XVT='SLVT',
    _Samp_Tr9_PCCrit=None,

    # Source_node_ViaM1M2
    _Samp_Tr9_Source_Via_TF=True,

    # Drain_node_ViaM1M2
    _Samp_Tr9_Drain_Via_TF=True,

    # POLY dummy setting
    _Samp_Tr9_PMOSDummy=True,  # TF
    # if _PMOSDummy == True
    _Samp_Tr9_PMOSDummy_length=None,  # None/Value
    _Samp_Tr9_PMOSDummy_placement='Dn',  # None/'Up'/'Dn'/

    # Tr8
    _Samp_Tr8_NMOSNumberofGate=2,  # number (ref:4)
    _Samp_Tr8_NMOSChannelWidth=100,  # number (ref:500)
    _Samp_Tr8_NMOSChannellength=30,  # number (ref:30)
    _Samp_Tr8_GateSpacing=None,  # None/number
    _Samp_Tr8_SDWidth=None,  # None/number
    _Samp_Tr8_XVT='RVT',  # 'XVT' ex)SLVT LVT RVT HVT
    _Samp_Tr8_PCCrit=True,  # None/True

    # Source_node_ViaM1M2
    _Samp_Tr8_Source_Via_TF=True,  # True/False

    # Drain_node_ViaM1M2
    _Samp_Tr8_Drain_Via_TF=True,  # True/False

    # POLY dummy setting
    _Samp_Tr8_NMOSDummy=True,  # TF
    # if _PMOSDummy == True
    _Samp_Tr8_NMOSDummy_length=None,  # None/Value
    _Samp_Tr8_NMOSDummy_placement=None,  # None/'Up'/'Dn'/

    ## Tr6
    _Samp_Tr6_NMOSNumberofGate=2,  # number
    _Samp_Tr6_NMOSChannelWidth=100,  # number
    _Samp_Tr6_NMOSChannellength=30,  # number
    _Samp_Tr6_GateSpacing=None,  # None/number
    _Samp_Tr6_SDWidth=None,  # None/number
    _Samp_Tr6_XVT='SLVT',  # 'XVT' ex)SLVT LVT RVT HVT
    _Samp_Tr6_PCCrit=True,  # None/True

    # Tr6 Source_node_ViaM1M2
    _Samp_Tr6_Source_Via_TF=False,  # True/False

    # Tr6 Drain_node_ViaM1M2
    _Samp_Tr6_Drain_Via_TF=False,  # True/False

    # Tr6 POLY dummy setting
    _Samp_Tr6_NMOSDummy=True,  # TF
    # Tr6 if _PMOSDummy == True
    _Samp_Tr6_NMOSDummy_length=None,  # None/Value
    _Samp_Tr6_NMOSDummy_placement='Dn',  # None/'Up'/'Dn'/

    # Tr6 Vp node
    _Samp_Tr6_Vp_node_width=280,  # Number
    _Samp_Tr6_Vp_node_metal_Layer=3,  # number

    # Tr6 Guardring
    # Pbody: number of contact
    # Nbody
    _Samp_Tr6_NwellWidth=850,  # number

    # PMOS: Tr11
    _Samp_Tr11_PMOSNumberofGate=2,
    _Samp_Tr11_PMOSChannelWidth=200,
    _Samp_Tr11_PMOSChannellength=30,
    _Samp_Tr11_GateSpacing=None,
    _Samp_Tr11_SDWidth=None,
    _Samp_Tr11_XVT='SLVT',
    _Samp_Tr11_PCCrit=None,

    # Source_node_ViaM1M2
    _Samp_Tr11_Source_Via_TF=True,

    # Drain_node_ViaM1M2
    _Samp_Tr11_Drain_Via_TF=True,

    # POLY dummy setting
    _Samp_Tr11_PMOSDummy=True,  # TF
    # if _PMOSDummy == True
    _Samp_Tr11_PMOSDummy_length=None,  # None/Value
    _Samp_Tr11_PMOSDummy_placement='Up',  # None/'Up'/'Dn'/

    # Nbodyring(Guardring)
    _Samp_Tr11_Guardring_NumCont=3,  # number

    ## VddTieCell4
    # VddTieCell4 NMOS
    _Samp_Tie4N_NMOSNumberofGate=2,  # number
    _Samp_Tie4N_NMOSChannelWidth=100,  # number
    _Samp_Tie4N_NMOSChannellength=30,  # number
    _Samp_Tie4N_GateSpacing=None,  # None/number
    _Samp_Tie4N_SDWidth=None,  # None/number
    _Samp_Tie4N_XVT='SLVT',  # 'XVT' ex)SLVT LVT RVT HVT
    _Samp_Tie4N_PCCrit=True,  # None/True

    # VddTieCell4 Source_node_ViaM1M2
    _Samp_Tie4N_Source_Via_TF=True,  # True/False

    # VddTieCell4 Drain_node_ViaM1M2
    _Samp_Tie4N_Drain_Via_TF=False,  # True/False

    # POLY dummy setting
    _Samp_Tie4N_NMOSDummy=True,  # TF
    # if _PMOSDummy == True
    _Samp_Tie4N_NMOSDummy_length=None,  # None/Value
    _Samp_Tie4N_NMOSDummy_placement='Dn',  # None/'Up'/'Dn'/

    # VddTieCell4 PMOS
    _Samp_Tie4P_PMOSNumberofGate=2,  # number
    _Samp_Tie4P_PMOSChannelWidth=200,  # number
    _Samp_Tie4P_PMOSChannellength=30,  # number
    _Samp_Tie4P_GateSpacing=None,  # None/number
    _Samp_Tie4P_SDWidth=None,  # None/number
    _Samp_Tie4P_XVT='SLVT',  # 'XVT' ex)SLVT LVT RVT HVT
    _Samp_Tie4P_PCCrit=True,  # None/True

    # VddTieCell4 PMOS Source_node_ViaM1M2
    _Samp_Tie4P_Source_Via_TF=False,  # True/False

    # VddTieCell4 PMOS Drain_node_ViaM1M2
    _Samp_Tie4P_Drain_Via_TF=True,  # True/False

    # POLY dummy setting
    _Samp_Tie4P_PMOSDummy=True,  # TF
    # if _PMOSDummy == True
    _Samp_Tie4P_PMOSDummy_length=None,  # None/Value
    _Samp_Tie4P_PMOSDummy_placement='Up',  # None/'Up'/'Dn'/

    # VddTieCell4 Number of Body Contact
    _Samp_Tie4_NBodyCOX=15,
    _Samp_Tie4_NBodyCOY=3,
    _Samp_Tie4_PBodyCOX=15,
    _Samp_Tie4_PBodyCOY=3,

    ## VddTieCell8
    # VddTieCell8 NMOS
    _Samp_Tie8N_NMOSNumberofGate=2,  # number
    _Samp_Tie8N_NMOSChannelWidth=100,  # number
    _Samp_Tie8N_NMOSChannellength=30,  # number
    _Samp_Tie8N_GateSpacing=None,  # None/number
    _Samp_Tie8N_SDWidth=None,  # None/number
    _Samp_Tie8N_XVT='SLVT',  # 'XVT' ex)SLVT LVT RVT HVT
    _Samp_Tie8N_PCCrit=True,  # None/True

    # VddTieCell8 Source_node_ViaM1M2
    _Samp_Tie8N_Source_Via_TF=True,  # True/False

    # VddTieCell8 Drain_node_ViaM1M2
    _Samp_Tie8N_Drain_Via_TF=False,  # True/False

    # POLY dummy setting
    _Samp_Tie8N_NMOSDummy=True,  # TF
    # if _PMOSDummy == True
    _Samp_Tie8N_NMOSDummy_length=None,  # None/Value
    _Samp_Tie8N_NMOSDummy_placement='Dn',  # None/'Up'/'Dn'/

    # VddTieCell8 PMOS
    _Samp_Tie8P_PMOSNumberofGate=2,  # number
    _Samp_Tie8P_PMOSChannelWidth=200,  # number
    _Samp_Tie8P_PMOSChannellength=30,  # number
    _Samp_Tie8P_GateSpacing=None,  # None/number
    _Samp_Tie8P_SDWidth=None,  # None/number
    _Samp_Tie8P_XVT='SLVT',  # 'XVT' ex)SLVT LVT RVT HVT
    _Samp_Tie8P_PCCrit=True,  # None/True

    # VddTieCell8 PMOS Source_node_ViaM1M2
    _Samp_Tie8P_Source_Via_TF=False,  # True/False

    # VddTieCell8 PMOS Drain_node_ViaM1M2
    _Samp_Tie8P_Drain_Via_TF=True,  # True/False

    # POLY dummy setting
    _Samp_Tie8P_PMOSDummy=True,  # TF
    # if _PMOSDummy == True
    _Samp_Tie8P_PMOSDummy_length=None,  # None/Value
    _Samp_Tie8P_PMOSDummy_placement='Up',  # None/'Up'/'Dn'/

    # VddTieCell8 Number of Body Contact
    _Samp_Tie8_NBodyCOX=15,
    _Samp_Tie8_NBodyCOY=3,
    _Samp_Tie8_PBodyCOX=15,
    _Samp_Tie8_PBodyCOY=3,

    # Tr12
    _Samp_Tr12_NMOSNumberofGate=2,  # number
    _Samp_Tr12_NMOSChannelWidth=100,  # number
    _Samp_Tr12_NMOSChannellength=30,  # number
    _Samp_Tr12_GateSpacing=None,  # None/number
    _Samp_Tr12_SDWidth=None,  # None/number
    _Samp_Tr12_XVT='SLVT',  # 'XVT' ex)SLVT LVT RVT HVT
    _Samp_Tr12_PCCrit=True,  # None/True

    # Source_node_ViaM1M2
    _Samp_Tr12_Source_Via_TF=True,  # True/False

    # Drain_node_ViaM1M2
    _Samp_Tr12_Drain_Via_TF=True,  # True/False

    # POLY dummy setting
    _Samp_Tr12_NMOSDummy=True,  # TF
    # if _PMOSDummy == True
    _Samp_Tr12_NMOSDummy_length=None,  # None/Value
    _Samp_Tr12_NMOSDummy_placement=None,  # None/'Up'/'Dn'/

    # Tr3
    _Samp_Tr3_NMOSNumberofGate=2,  # number
    _Samp_Tr3_NMOSChannelWidth=100,  # number
    _Samp_Tr3_NMOSChannellength=30,  # number
    _Samp_Tr3_GateSpacing=None,  # None/number
    _Samp_Tr3_SDWidth=None,  # None/number
    _Samp_Tr3_XVT='RVT',  # 'XVT' ex)SLVT LVT RVT HVT
    _Samp_Tr3_PCCrit=True,  # None/True

    # Source_node_ViaM1M2
    _Samp_Tr3_Source_Via_TF=True,  # True/False

    # Drain_node_ViaM1M2
    _Samp_Tr3_Drain_Via_TF=True,  # True/False

    # POLY dummy setting
    _Samp_Tr3_NMOSDummy=True,  # TF
    # if _PMOSDummy == True
    _Samp_Tr3_NMOSDummy_length=None,  # None/Value
    _Samp_Tr3_NMOSDummy_placement=None,  # None/'Up'/'Dn'/

    # Tr10
    _Samp_Tr10_NMOSNumberofGate=2,  # number
    _Samp_Tr10_NMOSChannelWidth=100,  # number
    _Samp_Tr10_NMOSChannellength=30,  # number
    _Samp_Tr10_GateSpacing=None,  # None/number
    _Samp_Tr10_SDWidth=None,  # None/number
    _Samp_Tr10_XVT='RVT',  # 'XVT' ex)SLVT LVT RVT HVT
    _Samp_Tr10_PCCrit=True,  # None/True

    # Source_node_ViaM1M2
    _Samp_Tr10_Source_Via_TF=True,  # True/False

    # Drain_node_ViaM1M2
    _Samp_Tr10_Drain_Via_TF=True,  # True/False

    # POLY dummy setting
    _Samp_Tr10_NMOSDummy=True,  # TF
    # if _PMOSDummy == True
    _Samp_Tr10_NMOSDummy_length=None,  # None/Value
    _Samp_Tr10_NMOSDummy_placement=None,  # None/'Up'/'Dn'/

    # Tr12Tr3Tr10 Guardring
    _Samp_Tr12Tr3Tr10_Guardring_NumCont=3,  # Number

    # HDVNCAP_Array
    _Samp_HDVNCAP_Length=5000,  # 22u M
    _Samp_HDVNCAP_LayoutOption=[3, 4, 5, 6],
    _Samp_HDVNCAP_NumFigPair=25,  # 9.55u M == 94개
    _Samp_HDVNCAP_Array=3,  # number: 1xnumber
    _Samp_HDVNCAP_Cbot_Ctop_metalwidth=190,  # number
    # Total HDVNCapSize = 600fF

    ## BootStrapped Sampler CLKB Inverter
    _CLKBInv_NMOS_NumberofGate=32,
    _CLKBInv_NMOS_ChannelWidth=400,
    _CLKBInv_NMOS_ChannelLength=30,
    _CLKBInv_NMOS_XVT='SLVT',
    _CLKBInv_NMOS_POGate_Comb_length=None,

    _CLKBInv_PMOS_NumberofGate=32,
    _CLKBInv_Inv_PMOS_ChannelWidth=800,
    _CLKBInv_PMOS_ChannelLength=30,
    _CLKBInv_PMOS_XVT='SLVT',
    _CLKBInv_PMOS_POGate_Comb_length=None,

    _CLKBInv_Pbody_NumCont=2,
    _CLKBInv_XvtTop2Pbody=None,
    _CLKBInv_Nbody_NumCont=2,
    _CLKBInv_Xvtdown2Nbody=None,
    _CLKBInv_PMOSXvt2NMOSXvt=500,
)

with open("input.json", "w", encoding="utf-8") as json_file:
    json.dump(InputParams, json_file, ensure_ascii=False, indent=4)
print ('json file generation complete')