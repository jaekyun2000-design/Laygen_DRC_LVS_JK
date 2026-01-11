tmp4_1 = target_coordx
tmp4_2 = self.get_param_KJH4('SRF_C02_04_Guardring', 'BND_Deepnwell')[0][0][0]['_XY_right'][0]
tmp5_1 = self.get_param_KJH4('SRF_C05_02_Pin', 'SRF_Guardring', 'BND_Deepnwell')[0][0][0][0]['_XY_left'][0]
tmp5_2 = approaching_coordx
C02C05MinSpace = _DRCobj._T3toT3minspace - abs(tmp4_1 - tmp4_2) - abs(tmp5_1 - tmp5_2)
New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
C02C05space = 1300
New_Scoord[0] = New_Scoord[0] + max(C02C05MinSpace, C02C05space)
tmpXY.append(New_Scoord)
## Define Coordinates
self._DesignParameter['SRF_C05_02_Pin']['_XYCoordinates'] = tmpXY





#기존 입력
InputParams = dict(

    # Tr1 and Tr2
    # Tr1
    _Tr1Tr2_Tr1_NMOSNumberofGate=12,  # number
    _Tr1Tr2_Tr1_NMOSChannelWidth=1000,  # number
    _Tr1Tr2_Tr1_NMOSChannellength=30,  # number
    _Tr1Tr2_Tr1_GateSpacing=222,  # None/number
    _Tr1Tr2_Tr1_SDWidth=None,  # None/number
    _Tr1Tr2_Tr1_XVT='SLVT',  # 'XVT' ex)SLVT LVT RVT HVT
    _Tr1Tr2_Tr1_PCCrit=True,  # None/True

    # Source_node_ViaM1M2
    _Tr1Tr2_Tr1_Source_Via_TF=False,  # True/False

    # Drain_node_ViaM1M2
    _Tr1Tr2_Tr1_Drain_Via_TF=False,  # True/False

    # POLY dummy setting
    _Tr1Tr2_Tr1_NMOSDummy=True,  # TF
    # if _PMOSDummy == True
    _Tr1Tr2_Tr1_NMOSDummy_length=None,  # None/Value
    _Tr1Tr2_Tr1_NMOSDummy_placement=None,  # None/'Up'/'Dn'/

    # Tr2
    _Tr1Tr2_Tr2_NMOSNumberofGate=5,  # number
    _Tr1Tr2_Tr2_NMOSChannelWidth=1000,  # number
    _Tr1Tr2_Tr2_NMOSChannellength=30,  # number
    _Tr1Tr2_Tr2_GateSpacing=222,  # None/number
    _Tr1Tr2_Tr2_SDWidth=None,  # None/number
    _Tr1Tr2_Tr2_XVT='SLVT',  # 'XVT' ex)SLVT LVT RVT HVT
    _Tr1Tr2_Tr2_PCCrit=True,  # None/True

    # Source_node_ViaM1M2
    _Tr1Tr2_Tr2_Source_Via_TF=False,  # True/False

    # Drain_node_ViaM1M2
    _Tr1Tr2_Tr2_Drain_Via_TF=False,  # True/False

    # POLY dummy setting
    _Tr1Tr2_Tr2_NMOSDummy=True,  # TF
    # if _PMOSDummy == True
    _Tr1Tr2_Tr2_NMOSDummy_length=None,  # None/Value
    _Tr1Tr2_Tr2_NMOSDummy_placement=None,  # None/'Up'/'Dn'/

    # Input/Output node
    # INPUT node
    _Tr1Tr2_Inputnode_Metal_layer=6,  # number
    _Tr1Tr2_Inputnode_width=600,  # number

    # OUTPUT node
    _Tr1Tr2_Outputnode_Metal_layer=6,  # number
    _Tr1Tr2_Outputnode_width=600,  # number

    # Guardring
    # Pbody: number of contact
    # Nbody
    _Tr1Tr2_NwellWidth=850,  # number

    # Tr4
    _Tr4_NMOSNumberofGate=4,  # number
    _Tr4_NMOSChannelWidth=500,  # number
    _Tr4_NMOSChannellength=30,  # number
    _Tr4_GateSpacing=None,  # None/number
    _Tr4_SDWidth=None,  # None/number
    _Tr4_XVT='SLVT',  # 'XVT' ex)SLVT LVT RVT HVT
    _Tr4_PCCrit=True,  # None/True

    # Source_node_ViaM1M2
    _Tr4_Source_Via_TF=True,  # True/False

    # Drain_node_ViaM1M2
    _Tr4_Drain_Via_TF=True,  # True/False

    # POLY dummy setting
    _Tr4_NMOSDummy=True,  # TF
    # if _PMOSDummy == True
    _Tr4_NMOSDummy_length=None,  # None/Value
    _Tr4_NMOSDummy_placement=None,  # None/'Up'/'Dn'/

    # Tr5 Tr7 Tr9
    # PMOS: Tr5
    _Tr5_PMOSNumberofGate=2,
    _Tr5_PMOSChannelWidth=1000,  # ref=1000
    _Tr5_PMOSChannellength=30,
    _Tr5_GateSpacing=None,
    _Tr5_SDWidth=None,
    _Tr5_XVT='SLVT',
    _Tr5_PCCrit=None,

    # Source_node_ViaM1M2
    _Tr5_Source_Via_TF=True,

    # Drain_node_ViaM1M2
    _Tr5_Drain_Via_TF=True,

    # POLY dummy setting
    _Tr5_PMOSDummy=True,  # TF
    # if _PMOSDummy == True
    _Tr5_PMOSDummy_length=None,  # None/Value
    _Tr5_PMOSDummy_placement=None,  # None/'Up'/'Dn'/

    # PMOS: Tr7
    _Tr7_PMOSNumberofGate=4,
    _Tr7_PMOSChannelWidth=1000,
    _Tr7_PMOSChannellength=30,
    _Tr7_GateSpacing=None,
    _Tr7_SDWidth=None,
    _Tr7_XVT='SLVT',
    _Tr7_PCCrit=None,

    # Source_node_ViaM1M2
    _Tr7_Source_Via_TF=True,

    # Drain_node_ViaM1M2
    _Tr7_Drain_Via_TF=True,

    # POLY dummy setting
    _Tr7_PMOSDummy=True,  # TF
    # if _PMOSDummy == True
    _Tr7_PMOSDummy_length=None,  # None/Value
    _Tr7_PMOSDummy_placement=None,  # None/'Up'/'Dn'/

    # PMOS: Tr9
    _Tr9_PMOSNumberofGate=8,
    _Tr9_PMOSChannelWidth=1000,  # ref = 1000
    _Tr9_PMOSChannellength=30,
    _Tr9_GateSpacing=None,
    _Tr9_SDWidth=None,
    _Tr9_XVT='SLVT',
    _Tr9_PCCrit=None,

    # Source_node_ViaM1M2
    _Tr9_Source_Via_TF=True,

    # Drain_node_ViaM1M2
    _Tr9_Drain_Via_TF=True,

    # POLY dummy setting
    _Tr9_PMOSDummy=True,  # TF
    # if _PMOSDummy == True
    _Tr9_PMOSDummy_length=None,  # None/Value
    _Tr9_PMOSDummy_placement=None,  # None/'Up'/'Dn'/

    # Tr8
    _Tr8_NMOSNumberofGate=10,  # number (ref:4)
    _Tr8_NMOSChannelWidth=500,  # number (ref:500)
    _Tr8_NMOSChannellength=30,  # number (ref:30)
    _Tr8_GateSpacing=None,  # None/number
    _Tr8_SDWidth=None,  # None/number
    _Tr8_XVT='SLVT',  # 'XVT' ex)SLVT LVT RVT HVT
    _Tr8_PCCrit=True,  # None/True

    # Source_node_ViaM1M2
    _Tr8_Source_Via_TF=True,  # True/False

    # Drain_node_ViaM1M2
    _Tr8_Drain_Via_TF=True,  # True/False

    # POLY dummy setting
    _Tr8_NMOSDummy=True,  # TF
    # if _PMOSDummy == True
    _Tr8_NMOSDummy_length=None,  # None/Value
    _Tr8_NMOSDummy_placement=None,  # None/'Up'/'Dn'/

    ## Tr6
    _Tr6_NMOSNumberofGate=4,  # number
    _Tr6_NMOSChannelWidth=500,  # number
    _Tr6_NMOSChannellength=30,  # number
    _Tr6_GateSpacing=100,  # None/number
    _Tr6_SDWidth=None,  # None/number
    _Tr6_XVT='SLVT',  # 'XVT' ex)SLVT LVT RVT HVT
    _Tr6_PCCrit=True,  # None/True

    # Tr6 Source_node_ViaM1M2
    _Tr6_Source_Via_TF=False,  # True/False

    # Tr6 Drain_node_ViaM1M2
    _Tr6_Drain_Via_TF=False,  # True/False

    # Tr6 POLY dummy setting
    _Tr6_NMOSDummy=True,  # TF
    # Tr6 if _PMOSDummy == True
    _Tr6_NMOSDummy_length=None,  # None/Value
    _Tr6_NMOSDummy_placement=None,  # None/'Up'/'Dn'/

    # Tr6 Vp node
    _Tr6_Vp_node_width=280,  # Number
    _Tr6_Vp_node_metal_Layer=4,  # number

    # Tr6 Guardring
    # Pbody: number of contact
    # Nbody
    _Tr6_NwellWidth=850,  # number

    # PMOS: Tr11
    _Tr11_PMOSNumberofGate=4,
    _Tr11_PMOSChannelWidth=1000,
    _Tr11_PMOSChannellength=30,
    _Tr11_GateSpacing=100,
    _Tr11_SDWidth=None,
    _Tr11_XVT='SLVT',
    _Tr11_PCCrit=None,

    # Source_node_ViaM1M2
    _Tr11_Source_Via_TF=True,

    # Drain_node_ViaM1M2
    _Tr11_Drain_Via_TF=True,

    # POLY dummy setting
    _Tr11_PMOSDummy=True,  # TF
    # if _PMOSDummy == True
    _Tr11_PMOSDummy_length=None,  # None/Value
    _Tr11_PMOSDummy_placement=None,  # None/'Up'/'Dn'/

    # Nbodyring(Guardring)
    _Tr11_Guardring_NumCont=3,  # number

    ## VddTieCell4
    # VddTieCell4 NMOS
    _Tie4N_NMOSNumberofGate=4,  # number
    _Tie4N_NMOSChannelWidth=250,  # number
    _Tie4N_NMOSChannellength=30,  # number
    _Tie4N_GateSpacing=100,  # None/number
    _Tie4N_SDWidth=None,  # None/number
    _Tie4N_XVT='SLVT',  # 'XVT' ex)SLVT LVT RVT HVT
    _Tie4N_PCCrit=True,  # None/True

    # VddTieCell4 Source_node_ViaM1M2
    _Tie4N_Source_Via_TF=False,  # True/False

    # VddTieCell4 Drain_node_ViaM1M2
    _Tie4N_Drain_Via_TF=False,  # True/False

    # POLY dummy setting
    _Tie4N_NMOSDummy=True,  # TF
    # if _PMOSDummy == True
    _Tie4N_NMOSDummy_length=400,  # None/Value
    _Tie4N_NMOSDummy_placement=None,  # None/'Up'/'Dn'/

    # VddTieCell4 PMOS
    _Tie4P_PMOSNumberofGate=4,  # number
    _Tie4P_PMOSChannelWidth=500,  # number
    _Tie4P_PMOSChannellength=30,  # number
    _Tie4P_GateSpacing=100,  # None/number
    _Tie4P_SDWidth=None,  # None/number
    _Tie4P_XVT='SLVT',  # 'XVT' ex)SLVT LVT RVT HVT
    _Tie4P_PCCrit=True,  # None/True

    # VddTieCell4 PMOS Source_node_ViaM1M2
    _Tie4P_Source_Via_TF=False,  # True/False

    # VddTieCell4 PMOS Drain_node_ViaM1M2
    _Tie4P_Drain_Via_TF=True,  # True/False

    # POLY dummy setting
    _Tie4P_PMOSDummy=True,  # TF
    # if _PMOSDummy == True
    _Tie4P_PMOSDummy_length=None,  # None/Value
    _Tie4P_PMOSDummy_placement=None,  # None/'Up'/'Dn'/

    # VddTieCell4 Number of Body Contact
    _Tie4_NBodyCOX=10,
    _Tie4_NBodyCOY=2,
    _Tie4_PBodyCOX=10,
    _Tie4_PBodyCOY=2,

    ## VddTieCell8
    # VddTieCell8 NMOS
    _Tie8N_NMOSNumberofGate=4,  # number
    _Tie8N_NMOSChannelWidth=250,  # number
    _Tie8N_NMOSChannellength=30,  # number
    _Tie8N_GateSpacing=100,  # None/number
    _Tie8N_SDWidth=None,  # None/number
    _Tie8N_XVT='SLVT',  # 'XVT' ex)SLVT LVT RVT HVT
    _Tie8N_PCCrit=True,  # None/True

    # VddTieCell8 Source_node_ViaM1M2
    _Tie8N_Source_Via_TF=False,  # True/False

    # VddTieCell8 Drain_node_ViaM1M2
    _Tie8N_Drain_Via_TF=False,  # True/False

    # POLY dummy setting
    _Tie8N_NMOSDummy=True,  # TF
    # if _PMOSDummy == True
    _Tie8N_NMOSDummy_length=400,  # None/Value
    _Tie8N_NMOSDummy_placement=None,  # None/'Up'/'Dn'/

    # VddTieCell8 PMOS
    _Tie8P_PMOSNumberofGate=4,  # number
    _Tie8P_PMOSChannelWidth=500,  # number
    _Tie8P_PMOSChannellength=30,  # number
    _Tie8P_GateSpacing=100,  # None/number
    _Tie8P_SDWidth=None,  # None/number
    _Tie8P_XVT='SLVT',  # 'XVT' ex)SLVT LVT RVT HVT
    _Tie8P_PCCrit=True,  # None/True

    # VddTieCell8 PMOS Source_node_ViaM1M2
    _Tie8P_Source_Via_TF=False,  # True/False

    # VddTieCell8 PMOS Drain_node_ViaM1M2
    _Tie8P_Drain_Via_TF=True,  # True/False

    # POLY dummy setting
    _Tie8P_PMOSDummy=True,  # TF
    # if _PMOSDummy == True
    _Tie8P_PMOSDummy_length=None,  # None/Value
    _Tie8P_PMOSDummy_placement=None,  # None/'Up'/'Dn'/

    # VddTieCell8 Number of Body Contact
    _Tie8_NBodyCOX=10,
    _Tie8_NBodyCOY=2,
    _Tie8_PBodyCOX=10,
    _Tie8_PBodyCOY=2,

    # Tr12
    _Tr12_NMOSNumberofGate=4,  # number
    _Tr12_NMOSChannelWidth=500,  # number
    _Tr12_NMOSChannellength=30,  # number
    _Tr12_GateSpacing=None,  # None/number
    _Tr12_SDWidth=None,  # None/number
    _Tr12_XVT='SLVT',  # 'XVT' ex)SLVT LVT RVT HVT
    _Tr12_PCCrit=True,  # None/True

    # Source_node_ViaM1M2
    _Tr12_Source_Via_TF=True,  # True/False

    # Drain_node_ViaM1M2
    _Tr12_Drain_Via_TF=True,  # True/False

    # POLY dummy setting
    _Tr12_NMOSDummy=True,  # TF
    # if _PMOSDummy == True
    _Tr12_NMOSDummy_length=None,  # None/Value
    _Tr12_NMOSDummy_placement=None,  # None/'Up'/'Dn'/

    # Tr3
    _Tr3_NMOSNumberofGate=4,  # number
    _Tr3_NMOSChannelWidth=500,  # number
    _Tr3_NMOSChannellength=30,  # number
    _Tr3_GateSpacing=None,  # None/number
    _Tr3_SDWidth=None,  # None/number
    _Tr3_XVT='SLVT',  # 'XVT' ex)SLVT LVT RVT HVT
    _Tr3_PCCrit=True,  # None/True

    # Source_node_ViaM1M2
    _Tr3_Source_Via_TF=True,  # True/False

    # Drain_node_ViaM1M2
    _Tr3_Drain_Via_TF=True,  # True/False

    # POLY dummy setting
    _Tr3_NMOSDummy=True,  # TF
    # if _PMOSDummy == True
    _Tr3_NMOSDummy_length=None,  # None/Value
    _Tr3_NMOSDummy_placement=None,  # None/'Up'/'Dn'/

    # Tr10
    _Tr10_NMOSNumberofGate=4,  # number
    _Tr10_NMOSChannelWidth=500,  # number
    _Tr10_NMOSChannellength=30,  # number
    _Tr10_GateSpacing=None,  # None/number
    _Tr10_SDWidth=None,  # None/number
    _Tr10_XVT='SLVT',  # 'XVT' ex)SLVT LVT RVT HVT
    _Tr10_PCCrit=True,  # None/True

    # Source_node_ViaM1M2
    _Tr10_Source_Via_TF=True,  # True/False

    # Drain_node_ViaM1M2
    _Tr10_Drain_Via_TF=True,  # True/False

    # POLY dummy setting
    _Tr10_NMOSDummy=True,  # TF
    # if _PMOSDummy == True
    _Tr10_NMOSDummy_length=None,  # None/Value
    _Tr10_NMOSDummy_placement=None,  # None/'Up'/'Dn'/

    # Tr12Tr3Tr10 Guardring
    _Tr12Tr3Tr10_Guardring_NumCont=3,  # Number

)


#ref design 입력
InputParams = dict(

    # Tr1 and Tr2
    # Tr1
    _Tr1Tr2_Tr1_NMOSNumberofGate=12,  # number
    _Tr1Tr2_Tr1_NMOSChannelWidth=1000,  # number
    _Tr1Tr2_Tr1_NMOSChannellength=30,  # number
    _Tr1Tr2_Tr1_GateSpacing=222,  # None/number
    _Tr1Tr2_Tr1_SDWidth=None,  # None/number
    _Tr1Tr2_Tr1_XVT='SLVT',  # 'XVT' ex)SLVT LVT RVT HVT
    _Tr1Tr2_Tr1_PCCrit=True,  # None/True

    # Source_node_ViaM1M2
    _Tr1Tr2_Tr1_Source_Via_TF=False,  # True/False

    # Drain_node_ViaM1M2
    _Tr1Tr2_Tr1_Drain_Via_TF=False,  # True/False

    # POLY dummy setting
    _Tr1Tr2_Tr1_NMOSDummy=True,  # TF
    # if _PMOSDummy == True
    _Tr1Tr2_Tr1_NMOSDummy_length=None,  # None/Value
    _Tr1Tr2_Tr1_NMOSDummy_placement=None,  # None/'Up'/'Dn'/

    # Tr2
    _Tr1Tr2_Tr2_NMOSNumberofGate=5,  # number
    _Tr1Tr2_Tr2_NMOSChannelWidth=1000,  # number
    _Tr1Tr2_Tr2_NMOSChannellength=30,  # number
    _Tr1Tr2_Tr2_GateSpacing=100,  # None/number
    _Tr1Tr2_Tr2_SDWidth=None,  # None/number
    _Tr1Tr2_Tr2_XVT='SLVT',  # 'XVT' ex)SLVT LVT RVT HVT
    _Tr1Tr2_Tr2_PCCrit=True,  # None/True

    # Source_node_ViaM1M2
    _Tr1Tr2_Tr2_Source_Via_TF=False,  # True/False

    # Drain_node_ViaM1M2
    _Tr1Tr2_Tr2_Drain_Via_TF=False,  # True/False

    # POLY dummy setting
    _Tr1Tr2_Tr2_NMOSDummy=True,  # TF
    # if _PMOSDummy == True
    _Tr1Tr2_Tr2_NMOSDummy_length=None,  # None/Value
    _Tr1Tr2_Tr2_NMOSDummy_placement=None,  # None/'Up'/'Dn'/

    # Input/Output node
    # INPUT node
    _Tr1Tr2_Inputnode_Metal_layer=6,  # number
    _Tr1Tr2_Inputnode_width=600,  # number

    # OUTPUT node
    _Tr1Tr2_Outputnode_Metal_layer=6,  # number
    _Tr1Tr2_Outputnode_width=600,  # number

    # Guardring
    # Pbody: number of contact
    # Nbody
    _Tr1Tr2_NwellWidth=850,  # number

    # Tr4
    _Tr4_NMOSNumberofGate=4,  # number
    _Tr4_NMOSChannelWidth=500,  # number
    _Tr4_NMOSChannellength=30,  # number
    _Tr4_GateSpacing=None,  # None/number
    _Tr4_SDWidth=None,  # None/number
    _Tr4_XVT='SLVT',  # 'XVT' ex)SLVT LVT RVT HVT
    _Tr4_PCCrit=True,  # None/True

    # Source_node_ViaM1M2
    _Tr4_Source_Via_TF=True,  # True/False

    # Drain_node_ViaM1M2
    _Tr4_Drain_Via_TF=True,  # True/False

    # POLY dummy setting
    _Tr4_NMOSDummy=True,  # TF
    # if _PMOSDummy == True
    _Tr4_NMOSDummy_length=None,  # None/Value
    _Tr4_NMOSDummy_placement=None,  # None/'Up'/'Dn'/

    # Tr5 Tr7 Tr9
    # PMOS: Tr5
    _Tr5_PMOSNumberofGate=2,
    _Tr5_PMOSChannelWidth=1000,  # ref=1000
    _Tr5_PMOSChannellength=30,
    _Tr5_GateSpacing=100,
    _Tr5_SDWidth=None,
    _Tr5_XVT='SLVT',
    _Tr5_PCCrit=None,

    # Source_node_ViaM1M2
    _Tr5_Source_Via_TF=True,

    # Drain_node_ViaM1M2
    _Tr5_Drain_Via_TF=True,

    # POLY dummy setting
    _Tr5_PMOSDummy=True,  # TF
    # if _PMOSDummy == True
    _Tr5_PMOSDummy_length=None,  # None/Value
    _Tr5_PMOSDummy_placement=None,  # None/'Up'/'Dn'/

    # PMOS: Tr7
    _Tr7_PMOSNumberofGate=4,
    _Tr7_PMOSChannelWidth=1000,
    _Tr7_PMOSChannellength=30,
    _Tr7_GateSpacing=100,
    _Tr7_SDWidth=None,
    _Tr7_XVT='SLVT',
    _Tr7_PCCrit=None,

    # Source_node_ViaM1M2
    _Tr7_Source_Via_TF=True,

    # Drain_node_ViaM1M2
    _Tr7_Drain_Via_TF=True,

    # POLY dummy setting
    _Tr7_PMOSDummy=True,  # TF
    # if _PMOSDummy == True
    _Tr7_PMOSDummy_length=None,  # None/Value
    _Tr7_PMOSDummy_placement=None,  # None/'Up'/'Dn'/

    # PMOS: Tr9
    _Tr9_PMOSNumberofGate=8,
    _Tr9_PMOSChannelWidth=1000,  # ref = 1000
    _Tr9_PMOSChannellength=30,
    _Tr9_GateSpacing=100,
    _Tr9_SDWidth=None,
    _Tr9_XVT='SLVT',
    _Tr9_PCCrit=None,

    # Source_node_ViaM1M2
    _Tr9_Source_Via_TF=True,

    # Drain_node_ViaM1M2
    _Tr9_Drain_Via_TF=True,

    # POLY dummy setting
    _Tr9_PMOSDummy=True,  # TF
    # if _PMOSDummy == True
    _Tr9_PMOSDummy_length=None,  # None/Value
    _Tr9_PMOSDummy_placement=None,  # None/'Up'/'Dn'/

    # Tr8
    _Tr8_NMOSNumberofGate=12,  # number (ref:4)
    _Tr8_NMOSChannelWidth=500,  # number (ref:500)
    _Tr8_NMOSChannellength=30,  # number (ref:30)
    _Tr8_GateSpacing=None,  # None/number
    _Tr8_SDWidth=None,  # None/number
    _Tr8_XVT='SLVT',  # 'XVT' ex)SLVT LVT RVT HVT
    _Tr8_PCCrit=True,  # None/True

    # Source_node_ViaM1M2
    _Tr8_Source_Via_TF=True,  # True/False

    # Drain_node_ViaM1M2
    _Tr8_Drain_Via_TF=True,  # True/False

    # POLY dummy setting
    _Tr8_NMOSDummy=True,  # TF
    # if _PMOSDummy == True
    _Tr8_NMOSDummy_length=None,  # None/Value
    _Tr8_NMOSDummy_placement=None,  # None/'Up'/'Dn'/

    ## Tr6
    _Tr6_NMOSNumberofGate=6,  # number
    _Tr6_NMOSChannelWidth=1000,  # number
    _Tr6_NMOSChannellength=30,  # number
    _Tr6_GateSpacing=None,  # None/number
    _Tr6_SDWidth=None,  # None/number
    _Tr6_XVT='SLVT',  # 'XVT' ex)SLVT LVT RVT HVT
    _Tr6_PCCrit=True,  # None/True

    # Tr6 Source_node_ViaM1M2
    _Tr6_Source_Via_TF=False,  # True/False

    # Tr6 Drain_node_ViaM1M2
    _Tr6_Drain_Via_TF=False,  # True/False

    # Tr6 POLY dummy setting
    _Tr6_NMOSDummy=True,  # TF
    # Tr6 if _PMOSDummy == True
    _Tr6_NMOSDummy_length=None,  # None/Value
    _Tr6_NMOSDummy_placement=None,  # None/'Up'/'Dn'/

    # Tr6 Vp node
    _Tr6_Vp_node_width=280,  # Number
    _Tr6_Vp_node_metal_Layer=3,  # number

    # Tr6 Guardring
    # Pbody: number of contact
    # Nbody
    _Tr6_NwellWidth=850,  # number

    # PMOS: Tr11
    _Tr11_PMOSNumberofGate=8,
    _Tr11_PMOSChannelWidth=500,
    _Tr11_PMOSChannellength=30,
    _Tr11_GateSpacing=100,
    _Tr11_SDWidth=None,
    _Tr11_XVT='SLVT',
    _Tr11_PCCrit=None,

    # Source_node_ViaM1M2
    _Tr11_Source_Via_TF=True,

    # Drain_node_ViaM1M2
    _Tr11_Drain_Via_TF=True,

    # POLY dummy setting
    _Tr11_PMOSDummy=True,  # TF
    # if _PMOSDummy == True
    _Tr11_PMOSDummy_length=None,  # None/Value
    _Tr11_PMOSDummy_placement=None,  # None/'Up'/'Dn'/

    # Nbodyring(Guardring)
    _Tr11_Guardring_NumCont=3,  # number

    ## VddTieCell4
    # VddTieCell4 NMOS
    _Tie4N_NMOSNumberofGate=4,  # number
    _Tie4N_NMOSChannelWidth=250,  # number
    _Tie4N_NMOSChannellength=30,  # number
    _Tie4N_GateSpacing=100,  # None/number
    _Tie4N_SDWidth=None,  # None/number
    _Tie4N_XVT='SLVT',  # 'XVT' ex)SLVT LVT RVT HVT
    _Tie4N_PCCrit=True,  # None/True

    # VddTieCell4 Source_node_ViaM1M2
    _Tie4N_Source_Via_TF=False,  # True/False

    # VddTieCell4 Drain_node_ViaM1M2
    _Tie4N_Drain_Via_TF=False,  # True/False

    # POLY dummy setting
    _Tie4N_NMOSDummy=True,  # TF
    # if _PMOSDummy == True
    _Tie4N_NMOSDummy_length=400,  # None/Value
    _Tie4N_NMOSDummy_placement=None,  # None/'Up'/'Dn'/

    # VddTieCell4 PMOS
    _Tie4P_PMOSNumberofGate=4,  # number
    _Tie4P_PMOSChannelWidth=500,  # number
    _Tie4P_PMOSChannellength=30,  # number
    _Tie4P_GateSpacing=100,  # None/number
    _Tie4P_SDWidth=None,  # None/number
    _Tie4P_XVT='SLVT',  # 'XVT' ex)SLVT LVT RVT HVT
    _Tie4P_PCCrit=True,  # None/True

    # VddTieCell4 PMOS Source_node_ViaM1M2
    _Tie4P_Source_Via_TF=False,  # True/False

    # VddTieCell4 PMOS Drain_node_ViaM1M2
    _Tie4P_Drain_Via_TF=True,  # True/False

    # POLY dummy setting
    _Tie4P_PMOSDummy=True,  # TF
    # if _PMOSDummy == True
    _Tie4P_PMOSDummy_length=None,  # None/Value
    _Tie4P_PMOSDummy_placement=None,  # None/'Up'/'Dn'/

    # VddTieCell4 Number of Body Contact
    _Tie4_NBodyCOX=10,
    _Tie4_NBodyCOY=2,
    _Tie4_PBodyCOX=10,
    _Tie4_PBodyCOY=2,

    ## VddTieCell8
    # VddTieCell8 NMOS
    _Tie8N_NMOSNumberofGate=4,  # number
    _Tie8N_NMOSChannelWidth=250,  # number
    _Tie8N_NMOSChannellength=30,  # number
    _Tie8N_GateSpacing=100,  # None/number
    _Tie8N_SDWidth=None,  # None/number
    _Tie8N_XVT='SLVT',  # 'XVT' ex)SLVT LVT RVT HVT
    _Tie8N_PCCrit=True,  # None/True

    # VddTieCell8 Source_node_ViaM1M2
    _Tie8N_Source_Via_TF=False,  # True/False

    # VddTieCell8 Drain_node_ViaM1M2
    _Tie8N_Drain_Via_TF=False,  # True/False

    # POLY dummy setting
    _Tie8N_NMOSDummy=True,  # TF
    # if _PMOSDummy == True
    _Tie8N_NMOSDummy_length=400,  # None/Value
    _Tie8N_NMOSDummy_placement=None,  # None/'Up'/'Dn'/

    # VddTieCell8 PMOS
    _Tie8P_PMOSNumberofGate=4,  # number
    _Tie8P_PMOSChannelWidth=500,  # number
    _Tie8P_PMOSChannellength=30,  # number
    _Tie8P_GateSpacing=100,  # None/number
    _Tie8P_SDWidth=None,  # None/number
    _Tie8P_XVT='SLVT',  # 'XVT' ex)SLVT LVT RVT HVT
    _Tie8P_PCCrit=True,  # None/True

    # VddTieCell8 PMOS Source_node_ViaM1M2
    _Tie8P_Source_Via_TF=False,  # True/False

    # VddTieCell8 PMOS Drain_node_ViaM1M2
    _Tie8P_Drain_Via_TF=True,  # True/False

    # POLY dummy setting
    _Tie8P_PMOSDummy=True,  # TF
    # if _PMOSDummy == True
    _Tie8P_PMOSDummy_length=None,  # None/Value
    _Tie8P_PMOSDummy_placement=None,  # None/'Up'/'Dn'/

    # VddTieCell8 Number of Body Contact
    _Tie8_NBodyCOX=10,
    _Tie8_NBodyCOY=2,
    _Tie8_PBodyCOX=10,
    _Tie8_PBodyCOY=2,

    # Tr12
    _Tr12_NMOSNumberofGate=4,  # number
    _Tr12_NMOSChannelWidth=1000,  # number
    _Tr12_NMOSChannellength=30,  # number
    _Tr12_GateSpacing=None,  # None/number
    _Tr12_SDWidth=None,  # None/number
    _Tr12_XVT='SLVT',  # 'XVT' ex)SLVT LVT RVT HVT
    _Tr12_PCCrit=True,  # None/True

    # Source_node_ViaM1M2
    _Tr12_Source_Via_TF=True,  # True/False

    # Drain_node_ViaM1M2
    _Tr12_Drain_Via_TF=True,  # True/False

    # POLY dummy setting
    _Tr12_NMOSDummy=True,  # TF
    # if _PMOSDummy == True
    _Tr12_NMOSDummy_length=None,  # None/Value
    _Tr12_NMOSDummy_placement=None,  # None/'Up'/'Dn'/

    # Tr3
    _Tr3_NMOSNumberofGate=4,  # number
    _Tr3_NMOSChannelWidth=500,  # number
    _Tr3_NMOSChannellength=30,  # number
    _Tr3_GateSpacing=None,  # None/number
    _Tr3_SDWidth=None,  # None/number
    _Tr3_XVT='SLVT',  # 'XVT' ex)SLVT LVT RVT HVT
    _Tr3_PCCrit=True,  # None/True

    # Source_node_ViaM1M2
    _Tr3_Source_Via_TF=True,  # True/False

    # Drain_node_ViaM1M2
    _Tr3_Drain_Via_TF=True,  # True/False

    # POLY dummy setting
    _Tr3_NMOSDummy=True,  # TF
    # if _PMOSDummy == True
    _Tr3_NMOSDummy_length=None,  # None/Value
    _Tr3_NMOSDummy_placement=None,  # None/'Up'/'Dn'/

    # Tr10
    _Tr10_NMOSNumberofGate=8,  # number
    _Tr10_NMOSChannelWidth=1000,  # number
    _Tr10_NMOSChannellength=30,  # number
    _Tr10_GateSpacing=None,  # None/number
    _Tr10_SDWidth=None,  # None/number
    _Tr10_XVT='SLVT',  # 'XVT' ex)SLVT LVT RVT HVT
    _Tr10_PCCrit=True,  # None/True

    # Source_node_ViaM1M2
    _Tr10_Source_Via_TF=True,  # True/False

    # Drain_node_ViaM1M2
    _Tr10_Drain_Via_TF=True,  # True/False

    # POLY dummy setting
    _Tr10_NMOSDummy=True,  # TF
    # if _PMOSDummy == True
    _Tr10_NMOSDummy_length=None,  # None/Value
    _Tr10_NMOSDummy_placement=None,  # None/'Up'/'Dn'/

    # Tr12Tr3Tr10 Guardring
    _Tr12Tr3Tr10_Guardring_NumCont=3,  # Number

)









# Ctop M5 Hrz Route Boundary (HDVNCap 상단) Generetion
## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
self._DesignParameter['BND_CtopNode_Hrz_M5'] = self._BoundaryElementDeclaration(
    _Layer=DesignParameters._LayerMapping['METAL5'][0],
    _Datatype=DesignParameters._LayerMapping['METAL5'][1],
    _XWidth=None,
    _YWidth=None,
    _XYCoordinates=[],
)

## Define Boundary_element _YWidth
CtopNode_Hrz_M5_PathWidth = 1000
self._DesignParameter['BND_CtopNode_Hrz_M5']['_YWidth'] = CtopNode_Hrz_M5_PathWidth

## Define Boundary_element _XWidth
tmp1 = self.get_param_KJH4('BND_Ctop_Vtc_M5')
tmp2 = self.get_param_KJH4('SRF_HDVNCAP', 'SRF_Array', 'BND_Ctop_METAL{}'.format(_HDVNCAP_LayoutOption[-1]))
tmp3_1 = abs(tmp2[0][0][-1][0]['_XY_right'][0] - tmp1[0][0]['_XY_left'][0])
tmp3_2 = abs(tmp2[0][0][-1][0]['_XY_right'][0] - tmp2[0][0][0][0]['_XY_left'][0])
self._DesignParameter['BND_CtopNode_Hrz_M5']['_XWidth'] = max(tmp3_1, tmp3_2)

## Calculate Sref XYcoord
tmpXY = []
## initialized Sref coordinate
self._DesignParameter['BND_CtopNode_Hrz_M5']['_XYCoordinates'] = [[0, 0]]
## Calculate
## Target_coord: _XY_type1
target_coord = [tmp2[0][0][-1][0]['_XY_left'][0], tmp1[0][0]['_XY_down'][1]]
## Approaching_coord: _XY_type2
tmp5 = self.get_param_KJH4('BND_CtopNode_Hrz_M5')
approaching_coord = tmp5[0][0]['_XY_down_left']
## Sref coord
Scoord = tmp5[0][0]['_XY_origin']
## Cal
New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
tmpXY.append(New_Scoord)
## Define coordinates
self._DesignParameter['BND_CtopNode_Hrz_M5']['_XYCoordinates'] = tmpXY










# HDVNCap <-> BND_CtopNode_Hrz_M5 routing
## Boundary_element Generation
## Generate Boundary_element: ex)LayerName: METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
self._DesignParameter['BND_CtopHDVNCap_Vtc_M7'] = self._BoundaryElementDeclaration(
    _Layer=DesignParameters._LayerMapping['METAL7'][0],
    _Datatype=DesignParameters._LayerMapping['METAL7'][1],
    _XWidth=None,
    _YWidth=None,
    _XYCoordinates=[],
)

## Define Boundary_element _YWidth
tmp1_1 = self.get_param_KJH4('SRF_HDVNCAP', 'SRF_Array', 'BND_CTot_METAL{}'.format(_HDVNCAP_LayoutOption[-1]))
tmp1_2 = self.get_param_KJH4('BND_CtopNode_Hrz_M5')
self._DesignParameter['BND_CtopHDVNCap_Vtc_M7']['_YWidth'] = abs(tmp1_2[0][0]['_XY_up'][1] - tmp1_1[0][0][0][0]['_XY_down'][1])

## Define Boundary_element _XWidth
self._DesignParameter['BND_CtopHDVNCap_Vtc_M7']['_XWidth'] = _HDVNCAP_Cbot_Ctop_metalwidth

## initialized Sref coordinate
self._DesignParameter['BND_CtopHDVNCap_Vtc_M7']['_XYCoordinates'] = [[0, 0]]

## Calculate Sref XYcoord
tmpXY = []
for i in range(int(_HDVNCAP_Array / 2)):
    ## Target_coord: _XY_type1
    tmp2_1 = tmp1_1[0][0][i][0]['_XY_left'][0]
    tmp2_2 = tmp1_2[0][0]['_XY_up'][1]
    target_coord = [tmp2_1, tmp2_2]
    ## Approaching_coord: _XY_type2
    tmp3 = self.get_param_KJH4('BND_CtopHDVNCap_Vtc_M7')
    approaching_coord = tmp3[0][0]['_XY_up_left']
    ## Sref coord
    Scoord = tmp3[0][0]['_XY_origin']
    ## Cal
    New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
    tmpXY.append(New_Scoord)

## Define coordinates
self._DesignParameter['BND_CtopHDVNCap_Vtc_M7']['_XYCoordinates'] = tmpXY





## BND_CbotHDVNCap_vtc_M7 <-> HDVNCAP Via SREF generation
## Sref generation: ViaX
## Define ViaX Parameter
_Caculation_Parameters = copy.deepcopy(A02_ViaStack_KJH2._ViaStack_KJH2._ParametersForDesignCalculation)
_Caculation_Parameters['_Layer1'] = 4
_Caculation_Parameters['_Layer2'] = 7
_Caculation_Parameters['_COX'] = None
_Caculation_Parameters['_COY'] = None

## Sref ViaX declaration
self._DesignParameter['SRF_HDVNCapCtopHrzPath_ViaM4M7'] = self._SrefElementDeclaration(
    _DesignObj=A02_ViaStack_KJH2._ViaStack_KJH2(
        _DesignParameter=None,
        _Name='{}:SRF_HDVNCapCtopHrzPath_ViaM4M7'.format(_Name)))[0]

## Define Sref Relection
self._DesignParameter['SRF_HDVNCapCtopHrzPath_ViaM4M7']['_Reflect'] = [0, 0, 0]

## Define Sref Angle
self._DesignParameter['SRF_HDVNCapCtopHrzPath_ViaM4M7']['_Angle'] = 0

## initialized Sref coordinate
self._DesignParameter['SRF_HDVNCapCtopHrzPath_ViaM4M7']['_XYCoordinates'] = [[0, 0]]

tmp1 = self.get_param_KJH4('BND_CtopNode_Hrz_M5')
tmp2 = self.get_param_KJH4('BND_CtopHDVNCap_Vtc_M7')

## Calculate Sref XYcoord
tmpXY = []
for i in range(int(_HDVNCAP_Array / 2)):
    ## Calcuate Overlapped XYcoord
    Ovlpcoord = self.get_ovlp_KJH2(tmp1[0][0], tmp2[i][0])

    ## Calcuate _COX and _COY:  None or 'MinEnclosureX' or 'MinEnclosureY'
    _COX, _COY = self._CalculateNumViaByXYWidth(Ovlpcoord[0]['_Xwidth'], Ovlpcoord[0]['_Ywidth'], 'MinEnclosureY')

    ## Define _COX and _COY
    _Caculation_Parameters['_COX'] = _COX
    _Caculation_Parameters['_COY'] = _COY

    ## Generate Metal(x), Metal(x+1) and C0(Viax) layer:  Option: _CalculateDesignParameter, _CalculateDesignParameterXmin, _CalculateDesignParameterYmin, _CalculateDesignParameterXYsame
    self._DesignParameter['SRF_HDVNCapCtopHrzPath_ViaM4M7']['_DesignObj']._CalculateDesignParameterYmin(
        **_Caculation_Parameters)

    ## Calculate
    ## Target_coord
    target_coord = [tmp2[i][0]['_XY_cent'][0], tmp1[0][0]['_XY_cent'][1]]
    ## Approaching_coord
    tmp3 = self.get_param_KJH4('SRF_HDVNCapCtopHrzPath_ViaM4M7', 'SRF_ViaM6M7', 'BND_Met7Layer')
    approaching_coord = tmp3[0][0][0][0]['_XY_cent']
    ## Sref coord
    tmp4 = self.get_param_KJH4('SRF_HDVNCapCtopHrzPath_ViaM4M7')
    Scoord = tmp4[0][0]['_XY_origin']
    ## Calculate
    New_Scoord = self.get_Scoord_KJH4(target_coord, approaching_coord, Scoord)
    tmpXY.append(New_Scoord)

## Define
self._DesignParameter['SRF_HDVNCapCtopHrzPath_ViaM4M7']['_XYCoordinates'] = tmpXY