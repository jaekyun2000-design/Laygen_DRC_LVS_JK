def makeRBankCellSche(word, param):
    _ResistorWidth = param.get('_ResistorWidth')
    _ResistorLength = param.get('_ResistorLength')
    _TransmissionGateFinger = param.get('_TransmissionGateFinger')
    _TransmissionGateChannelWidth = param.get('_TransmissionGateChannelWidth')
    _TransmissionGateChannelLength = param.get('_TransmissionGateChannelLength')
    _TransmissionGateNPRatio = param.get('_TransmissionGateNPRatio')

    # Define pccrit layer creation
    if _TransmissionGateChannelLength == 30 or _TransmissionGateChannelLength == 34:
        _pccrit = 1
    else:
        _pccrit = 0

    _ResistorWidth = float(_ResistorWidth / 1000)
    _ResistorLength = float(_ResistorLength / 1000)
    _TGPMOSWidth = float(_TransmissionGateFinger * _TransmissionGateChannelWidth * _TransmissionGateNPRatio / 1000)
    _TGNMOSWidth = float(_TransmissionGateFinger * _TransmissionGateChannelWidth / 1000)
    _TGChannelLength = float(_TransmissionGateChannelLength / 1000)

    with open(f'ResistorBankCell{word}.src.net', 'w') as f:
        f.write('.INCLUDE  /home/PDK/ss28nm/SEC_CDS/ln28lppdk/S00-V1.1.0.1_SEC2.0.6.2/oa/cmos28lp/.resources/devices.cdl\n')
        f.write('.SUBCKT ResistorBankCell S SB VCM VDD VRX VSS\n')
        f.write(f'RR20 VRX net13 $SUB=VSS $[opppcres] r=0.725156k w={_ResistorWidth}u l={_ResistorLength}u pbar=1 s=1 bp=3 ncr=2\n')
        f.write(f'MN20 net13 S VCM VSS slvtnfet w={_TGNMOSWidth}u l={_TGChannelLength}u nf={_TransmissionGateFinger}.0 pccrit={_pccrit} plorient=1 ngcon=1 p_la=0u ptwell=0\n')
        f.write(f'MP20 net13 SB VCM VDD slvtpfet w={_TGPMOSWidth}u l={_TGChannelLength}u nf={_TransmissionGateFinger}.0 pccrit={_pccrit} plorient=1 ngcon=1 p_la=0u ptwell=0\n')
        f.write('.ENDS\n')
    pass

def makeRBankSche(word, param):
    _XRBNum = param.get('_XRBNum')
    _YRBNum = param.get('_YRBNum')
    _ResistorWidth = param.get('_ResistorWidth')
    _ResistorLength = param.get('_ResistorLength')
    _TransmissionGateFinger = param.get('_TransmissionGateFinger')
    _TransmissionGateChannelWidth = param.get('_TransmissionGateChannelWidth')
    _TransmissionGateChannelLength = param.get('_TransmissionGateChannelLength')
    _TransmissionGateNPRatio = param.get('_TransmissionGateNPRatio')

    # Define pccrit layer creation
    if _TransmissionGateChannelLength == 30 or _TransmissionGateChannelLength == 34:
        _pccrit = 1
    else:
        _pccrit = 0

    _ResistorWidth = float(_ResistorWidth / 1000)
    _ResistorLength = float(_ResistorLength / 1000)
    _TGPMOSWidth = float(_TransmissionGateFinger * _TransmissionGateChannelWidth * _TransmissionGateNPRatio / 1000)
    _TGNMOSWidth = float(_TransmissionGateFinger * _TransmissionGateChannelWidth / 1000)
    _TGChannelLength = float(_TransmissionGateChannelLength / 1000)

    sel_lst = []
    for i in range(_XRBNum * _YRBNum):
        sel_lst.append(f'S<{i}> SB<{i}>')
    sel_lst = ' '.join(sel_lst)

    with open(f'ResistorBank{word}.src.net', 'w') as f:
        f.write('.INCLUDE  /home/PDK/ss28nm/SEC_CDS/ln28lppdk/S00-V1.1.0.1_SEC2.0.6.2/oa/cmos28lp/.resources/devices.cdl\n')
        f.write('.SUBCKT ResistorBankCell S SB VCM VDD VRX VSS\n')
        f.write(f'RR20 VRX net13 $SUB=VSS $[opppcres] r=0.725156k w={_ResistorWidth}u l={_ResistorLength}u pbar=1 s=1 bp=3 ncr=2\n')
        f.write(f'MN20 net13 S VCM VSS slvtnfet w={_TGNMOSWidth}u l={_TGChannelLength}u nf={_TransmissionGateFinger}.0 pccrit={_pccrit} plorient=1 ngcon=1 p_la=0u ptwell=0\n')
        f.write(f'MP20 net13 SB VCM VDD slvtpfet w={_TGPMOSWidth}u l={_TGChannelLength}u nf={_TransmissionGateFinger}.0 pccrit={_pccrit} plorient=1 ngcon=1 p_la=0u ptwell=0\n')
        f.write('.ENDS\n')
        f.write(f'.SUBCKT ResistorBank {sel_lst} VCM VDD VRX VSS\n')
        for i in range(_XRBNum * _YRBNum):
            f.write(f'XIR<{i}> S<{i}> SB<{i}> VCM VDD VRX VSS / ResistorBankCell\n')
        f.write('.ENDS\n')
    pass

def makeRXSche(word, param):
    _XRBNum = param.get('_XRBNum')
    _YRBNum = param.get('_YRBNum')
    _ResistorWidth = param.get('_ResistorWidth')
    _ResistorLength = param.get('_ResistorLength')
    _TransmissionGateFinger = param.get('_TransmissionGateFinger')
    _TransmissionGateChannelWidth = param.get('_TransmissionGateChannelWidth')
    _TransmissionGateChannelLength = param.get('_TransmissionGateChannelLength')
    _TransmissionGateNPRatio = param.get('_TransmissionGateNPRatio')

    if _TransmissionGateChannelLength == 30 or _TransmissionGateChannelLength == 34:
        _RBpccrit = 1
    else:
        _RBpccrit = 0

    _ResistorWidth = float(_ResistorWidth / 1000)
    _ResistorLength = float(_ResistorLength / 1000)
    _TGPMOSWidth = float(_TransmissionGateFinger * _TransmissionGateChannelWidth * _TransmissionGateNPRatio / 1000)
    _TGNMOSWidth = float(_TransmissionGateFinger * _TransmissionGateChannelWidth / 1000)
    _TGChannelLength = float(_TransmissionGateChannelLength / 1000)

    sel_lst = []
    for i in range(_XRBNum * _YRBNum):
        sel_lst.append(f'S<{i}> SB<{i}>')
    sel_lst = ' '.join(sel_lst)

    _SRRandWidth = param.get('_SRRandWidth')
    _SRNPRatio = param.get('_SRNPRatio')
    _SRFinger1 = param.get('_SRFinger1')
    _SRFinger2 = param.get('_SRFinger2')
    _SRFinger3 = param.get('_SRFinger3')
    _SRFinger4 = param.get('_SRFinger4')
    _SRChannelLength = param.get('_SRChannelLength')

    # Define pccrit layer creation
    if _SRChannelLength == 30 or _SRChannelLength == 34:
        _SRpccrit = 1
    else:
        _SRpccrit = 0

    # Define total finger width (for SS28nm tech)
    _SRnmos1width = float(_SRRandWidth * _SRFinger1 / 1000)
    _SRnmos2width = float(_SRRandWidth * _SRFinger2 / 1000)
    _SRnmos3width = float(_SRRandWidth * _SRFinger3 / 1000)
    _SRnmos4width = float(_SRRandWidth * _SRFinger4 / 1000)
    _SRpmos1width = float(_SRRandWidth * _SRFinger1 * _SRNPRatio / 1000)
    _SRpmos2width = float(_SRRandWidth * _SRFinger2 * _SRNPRatio / 1000)
    _SRpmos3width = float(_SRRandWidth * _SRFinger3 * _SRNPRatio / 1000)
    _SRpmos4width = float(_SRRandWidth * _SRFinger4 * _SRNPRatio / 1000)

    # Define channel length (for SS28nm tech)
    _SRchannellength = float(_SRChannelLength / 1000)

    _SLCLKinputPMOSFinger1 = param.get('_SLCLKinputPMOSFinger1')
    _SLCLKinputPMOSFinger2 = param.get('_SLCLKinputPMOSFinger2')
    _SLPMOSFinger = param.get('_SLPMOSFinger')
    _SLPMOSChannelWidth = param.get('_SLPMOSChannelWidth')
    _SLNMOSFinger = param.get('_SLNMOSFinger')
    _SLDATAinputNMOSFinger = param.get('_SLDATAinputNMOSFinger')
    _SLNMOSChannelWidth = param.get('_SLNMOSChannelWidth')
    _SLCLKinputNMOSFinger = param.get('_SLCLKinputNMOSFinger')
    _SLCLKinputNMOSChannelWidth = param.get('_SLCLKinputNMOSChannelWidth')
    _SLChannelLength = param.get('_SLChannelLength')

    # Define netlist parameter for SS28nm
    if _SLChannelLength == 30 or _SLChannelLength == 34:
        _SLpccrit = 1
    else:
        _SLpccrit = 0

    _SLnmoswidth = float(_SLNMOSChannelWidth * _SLNMOSFinger / 1000)
    _SLdatainputnmoswidth = float(_SLNMOSChannelWidth * _SLDATAinputNMOSFinger / 1000)
    _SLclkinputnmoswidth = float(_SLCLKinputNMOSChannelWidth * _SLCLKinputNMOSFinger / 1000)

    _SLclkinputpmoswidth1 = float(_SLPMOSChannelWidth * _SLCLKinputPMOSFinger1 / 1000)
    _SLclkinputpmoswidth2 = float(_SLPMOSChannelWidth * _SLCLKinputPMOSFinger2 / 1000)
    _SLpmoswidth = float(_SLPMOSChannelWidth * _SLPMOSFinger / 1000)
    _SLchannellength = float(_SLChannelLength / 1000)

    _InvChannelWidth = param.get('_InvChannelWidth')
    _InvChannelLength = param.get('_InvChannelLength')
    _InvFinger = param.get('_InvFinger')
    _InvNPRatio = param.get('_InvNPRatio')

    if _InvChannelLength == 30 or _InvChannelLength == 34:
        _Invpccrit = 1
    else:
        _Invpccrit = 0

    _Invnmoswidth = float(_InvChannelWidth * _InvFinger / 1000)
    _Invpmoswidth = float(_InvChannelWidth * _InvFinger * _InvNPRatio / 1000)
    _Invchannellength = float(_InvChannelLength / 1000)

    _N = param.get('_N')
    interleaving = []
    for i in range(_N):
        interleaving.append(f'CK<{i}> OUT<{i}> OUTb<{i}>')
    interleaving = ' '.join(interleaving)

    with open(f'Receiver{word}.src.net', 'w') as f:
        f.write('.INCLUDE  /home/PDK/ss28nm/SEC_CDS/ln28lppdk/S00-V1.1.0.1_SEC2.0.6.2/oa/cmos28lp/.resources/devices.cdl\n')
        f.write('.GLOBAL VDD VSS\n')
        f.write('.SUBCKT StrongArmLatch CLK INn INp SSn SSp VDD VSS\n')
        f.write(
            f'MP5 net085 CLK VDD VDD slvtpfet w={_SLclkinputpmoswidth1}u l={_SLchannellength}u nf={_SLCLKinputPMOSFinger1}.0 pccrit={_SLpccrit} plorient=1 ngcon=1 p_la=0u ptwell=0\n')
        f.write(
            f'MP4 SSp CLK VDD VDD slvtpfet w={_SLclkinputpmoswidth2}u l={_SLchannellength}u nf={_SLCLKinputPMOSFinger2}.0 pccrit={_SLpccrit} plorient=1 ngcon=1 p_la=0u ptwell=0\n')
        f.write(
            f'MP3 net088 CLK VDD VDD slvtpfet w={_SLclkinputpmoswidth1}u l={_SLchannellength}u nf={_SLCLKinputPMOSFinger1}.0 pccrit={_SLpccrit} plorient=1 ngcon=1 p_la=0u ptwell=0\n')
        f.write(
            f'MP2 SSn CLK VDD VDD slvtpfet w={_SLclkinputpmoswidth2}u l={_SLchannellength}u nf={_SLCLKinputPMOSFinger2}.0 pccrit={_SLpccrit} plorient=1 ngcon=1 p_la=0u ptwell=0\n')
        f.write(
            f'MP1 SSn SSp VDD VDD slvtpfet w={_SLpmoswidth}u l={_SLchannellength}u nf={_SLPMOSFinger}.0 pccrit={_SLpccrit} plorient=1 ngcon=1 p_la=0u ptwell=0\n')
        f.write(
            f'MP0 SSp SSn VDD VDD slvtpfet w={_SLpmoswidth}u l={_SLchannellength}u nf={_SLPMOSFinger}.0 pccrit={_SLpccrit} plorient=1 ngcon=1 p_la=0u ptwell=0\n')
        f.write(
            f'MN7 net085 INn net083 VSS slvtnfet w={_SLdatainputnmoswidth}u l={_SLchannellength}u nf={_SLDATAinputNMOSFinger}.0 pccrit={_SLpccrit} plorient=1 ngcon=1 p_la=0u ptwell=0\n')
        f.write(
            f'MN2 net088 INp net083 VSS slvtnfet w={_SLdatainputnmoswidth}u l={_SLchannellength}u nf={_SLDATAinputNMOSFinger}.0 pccrit={_SLpccrit} plorient=1 ngcon=1 p_la=0u ptwell=0\n')
        f.write(
            f'MN4 SSp SSn net085 VSS slvtnfet w={_SLnmoswidth}u l={_SLchannellength}u nf={_SLNMOSFinger}.0 pccrit={_SLpccrit} plorient=1 ngcon=1 p_la=0u ptwell=0\n')
        f.write(
            f'MN3 SSn SSp net088 VSS slvtnfet w={_SLnmoswidth}u l={_SLchannellength}u nf={_SLNMOSFinger}.0 pccrit={_SLpccrit} plorient=1 ngcon=1 p_la=0u ptwell=0\n')
        f.write(
            f'MN1 net083 CLK VSS VSS slvtnfet w={_SLclkinputnmoswidth}u l={_SLchannellength}u nf={_SLCLKinputNMOSFinger}.0 pccrit={_SLpccrit} plorient=1 ngcon=1 p_la=0u ptwell=0\n')
        f.write('.ENDS\n')
        f.write('.SUBCKT CLK_drv_inv IN OUT VDD VSS\n')
        f.write(
            f'MN10 OUT IN VSS VSS slvtnfet w={_Invnmoswidth}u l={_Invchannellength}u nf={_InvFinger}.0 pccrit={_Invpccrit} plorient=1 ngcon=1 p_la=0u ptwell=0\n'
        )
        f.write(
            f'MP10 OUT IN VDD VDD slvtpfet w={_Invpmoswidth}u l={_Invchannellength}u nf={_InvFinger}.0 pccrit={_Invpccrit} plorient=1 ngcon=1 p_la=0u ptwell=0\n'
        )
        f.write('.ENDS\n')
        f.write('.SUBCKT ResistorBankCell S SB VCM VDD VRX VSS\n')
        f.write(
            f'RR20 VRX net13 $SUB=VSS $[opppcres] r=0.725156k w={_ResistorWidth}u l={_ResistorLength}u pbar=1 s=1 bp=3 ncr=2\n')
        f.write(
            f'MN20 net13 S VCM VSS slvtnfet w={_TGNMOSWidth}u l={_TGChannelLength}u nf={_TransmissionGateFinger}.0 pccrit={_RBpccrit} plorient=1 ngcon=1 p_la=0u ptwell=0\n')
        f.write(
            f'MP20 net13 SB VCM VDD slvtpfet w={_TGPMOSWidth}u l={_TGChannelLength}u nf={_TransmissionGateFinger}.0 pccrit={_RBpccrit} plorient=1 ngcon=1 p_la=0u ptwell=0\n')
        f.write('.ENDS\n')
        f.write(f'.SUBCKT ResistorBank {sel_lst} VCM VDD VRX VSS\n')
        for i in range(_XRBNum * _YRBNum):
            f.write(f'XIR<{i}> S<{i}> SB<{i}> VCM VDD VRX VSS / ResistorBankCell\n')
        f.write('.ENDS\n')
        f.write('.SUBCKT Inv IN OUT VDD VSS\n')
        f.write(
            f'MN30 OUT IN VSS VSS slvtnfet w={_SRnmos2width}u l={_SRchannellength}u nf={_SRFinger2}.0 pccrit={_SRpccrit} plorient=1 ngcon=1 p_la=0u ptwell=0\n')
        f.write(
            f'MP30 OUT IN VDD VDD slvtpfet w={_SRpmos2width}u l={_SRchannellength}u nf={_SRFinger2}.0 pccrit={_SRpccrit} plorient=1 ngcon=1 p_la=0u ptwell=0\n')
        f.write('.ENDS\n')
        f.write('.SUBCKT SRLatch IN INb OUT OUTb VDD VSS\n')
        f.write(
            f'MN45 OUTb net26 VSS VSS slvtnfet w={_SRnmos1width}u l={_SRchannellength}u nf={_SRFinger1}.0 pccrit={_SRpccrit} plorient=1 ngcon=1 p_la=0u ptwell=0\n')
        f.write(
            f'MN48 net38 OUTb VSS VSS slvtnfet w={_SRnmos4width}u l={_SRchannellength}u nf={_SRFinger4}.0 pccrit={_SRpccrit} plorient=1 ngcon=1 p_la=0u ptwell=0\n')
        f.write(
            f'MN46 OUTb IN net37 VSS slvtnfet w={_SRnmos3width}u l={_SRchannellength}u nf={_SRFinger3}.0 pccrit={_SRpccrit} plorient=1 ngcon=1 p_la=0u ptwell=0\n')
        f.write(
            f'MN42 OUT net10 VSS VSS slvtnfet w={_SRnmos1width}u l={_SRchannellength}u nf={_SRFinger1}.0 pccrit={_SRpccrit} plorient=1 ngcon=1 p_la=0u ptwell=0\n')
        f.write(
            f'MN47 net37 OUT VSS VSS slvtnfet w={_SRnmos4width}u l={_SRchannellength}u nf={_SRFinger4}.0 pccrit={_SRpccrit} plorient=1 ngcon=1 p_la=0u ptwell=0\n')
        f.write(
            f'MN40 OUT INb net38 VSS slvtnfet w={_SRnmos3width}u l={_SRchannellength}u nf={_SRFinger3}.0 pccrit={_SRpccrit} plorient=1 ngcon=1 p_la=0u ptwell=0\n')
        f.write(
            f'MP45 OUT INb VDD VDD slvtpfet w={_SRpmos1width}u l={_SRchannellength}u nf={_SRFinger1}.0 pccrit={_SRpccrit} plorient=1 ngcon=1 p_la=0u ptwell=0\n')
        f.write(
            f'MP44 OUTb IN VDD VDD slvtpfet w={_SRpmos1width}u l={_SRchannellength}u nf={_SRFinger1}.0 pccrit={_SRpccrit} plorient=1 ngcon=1 p_la=0u ptwell=0\n')
        f.write(
            f'MP43 net33 OUT VDD VDD slvtpfet w={_SRpmos4width}u l={_SRchannellength}u nf={_SRFinger4}.0 pccrit={_SRpccrit} plorient=1 ngcon=1 p_la=0u ptwell=0\n')
        f.write(
            f'MP42 OUTb net26 net33 VDD slvtpfet w={_SRpmos3width}u l={_SRchannellength}u nf={_SRFinger3}.0 pccrit={_SRpccrit} plorient=1 ngcon=1 p_la=0u ptwell=0\n')
        f.write(
            f'MP41 net35 OUTb VDD VDD slvtpfet w={_SRpmos4width}u l={_SRchannellength}u nf={_SRFinger4}.0 pccrit={_SRpccrit} plorient=1 ngcon=1 p_la=0u ptwell=0\n')
        f.write(
            f'MP40 OUT net10 net35 VDD slvtpfet w={_SRpmos3width}u l={_SRchannellength}u nf={_SRFinger3}.0 pccrit={_SRpccrit} plorient=1 ngcon=1 p_la=0u ptwell=0\n')
        f.write('XI49 IN net10 VDD VSS / Inv\n')
        f.write('XI46 INb net26 VDD VSS / Inv\n')
        f.write('.ENDS\n')
        f.write(f'.SUBCKT Receiver {interleaving} {sel_lst} VCM VDD VRX VSS Vref\n')
        for i in range(_N):
            f.write(f'XISA<{i}> CLK<{i}> Vref VRX ssp<{i}> ssn<{i}> VDD VSS / StrongArmLatch\n')
        for i in range(_N):
            f.write(f'XIInv<{i}> CK<{i}> CLK<{i}> VDD VSS / CLK_drv_inv\n')
        for i in range(_N):
            f.write(f'XISR<{i}> ssn<{i}> ssp<{i}> OUT<{i}> OUTb<{i}> VDD VSS / SRLatch\n')
        f.write(f'XI58 {sel_lst} VCM VDD VRX VSS / ResistorBank\n')
        f.write('.ENDS\n')
    pass

def makeSRLatchSche(word, param):
    _RandWidth = param.get('_RandWidth')
    _NPRatio = param.get('_NPRatio')
    _Finger1 = param.get('_Finger1')
    _Finger2 = param.get('_Finger2')
    _Finger3 = param.get('_Finger3')
    _Finger4 = param.get('_Finger4')
    _ChannelLength = param.get('_ChannelLength')

    # Define pccrit layer creation
    if _ChannelLength == 30 or _ChannelLength == 34:
        _pccrit = 1
    else:
        _pccrit = 0

    # Define total finger width (for SS28nm tech)
    _nmos1width = float(_RandWidth * _Finger1 / 1000)
    _nmos2width = float(_RandWidth * _Finger2 / 1000)
    _nmos3width = float(_RandWidth * _Finger3 / 1000)
    _nmos4width = float(_RandWidth * _Finger4 / 1000)
    _pmos1width = float(_RandWidth * _Finger1 * _NPRatio / 1000)
    _pmos2width = float(_RandWidth * _Finger2 * _NPRatio / 1000)
    _pmos3width = float(_RandWidth * _Finger3 * _NPRatio / 1000)
    _pmos4width = float(_RandWidth * _Finger4 * _NPRatio / 1000)

    # Define channel length (for SS28nm tech)
    _channellength = float(_ChannelLength / 1000)

    # write netlist for SR latch
    with open(f'SRLatch{word}.src.net', 'w') as f:
        f.write('.INCLUDE  /home/PDK/ss28nm/SEC_CDS/ln28lppdk/S00-V1.1.0.1_SEC2.0.6.2/oa/cmos28lp/.resources/devices.cdl\n')
        f.write('.SUBCKT Inv IN OUT VDD VSS\n')
        f.write(f'MN30 OUT IN VSS VSS slvtnfet w={_nmos2width}u l={_channellength}u nf={_Finger2}.0 pccrit={_pccrit} plorient=1 ngcon=1 p_la=0u ptwell=0\n')
        f.write(f'MP30 OUT IN VDD VDD slvtpfet w={_pmos2width}u l={_channellength}u nf={_Finger2}.0 pccrit={_pccrit} plorient=1 ngcon=1 p_la=0u ptwell=0\n')
        f.write('.ENDS\n')
        f.write('.SUBCKT SRLatch IN INb OUT OUTb VDD VSS\n')
        f.write(f'MN45 OUTb net26 VSS VSS slvtnfet w={_nmos1width}u l={_channellength}u nf={_Finger1}.0 pccrit={_pccrit} plorient=1 ngcon=1 p_la=0u ptwell=0\n')
        f.write(f'MN48 net38 OUTb VSS VSS slvtnfet w={_nmos4width}u l={_channellength}u nf={_Finger4}.0 pccrit={_pccrit} plorient=1 ngcon=1 p_la=0u ptwell=0\n')
        f.write(f'MN46 OUTb IN net37 VSS slvtnfet w={_nmos3width}u l={_channellength}u nf={_Finger3}.0 pccrit={_pccrit} plorient=1 ngcon=1 p_la=0u ptwell=0\n')
        f.write(f'MN42 OUT net10 VSS VSS slvtnfet w={_nmos1width}u l={_channellength}u nf={_Finger1}.0 pccrit={_pccrit} plorient=1 ngcon=1 p_la=0u ptwell=0\n')
        f.write(f'MN47 net37 OUT VSS VSS slvtnfet w={_nmos4width}u l={_channellength}u nf={_Finger4}.0 pccrit={_pccrit} plorient=1 ngcon=1 p_la=0u ptwell=0\n')
        f.write(f'MN40 OUT INb net38 VSS slvtnfet w={_nmos3width}u l={_channellength}u nf={_Finger3}.0 pccrit={_pccrit} plorient=1 ngcon=1 p_la=0u ptwell=0\n')
        f.write(f'MP45 OUT INb VDD VDD slvtpfet w={_pmos1width}u l={_channellength}u nf={_Finger1}.0 pccrit={_pccrit} plorient=1 ngcon=1 p_la=0u ptwell=0\n')
        f.write(f'MP44 OUTb IN VDD VDD slvtpfet w={_pmos1width}u l={_channellength}u nf={_Finger1}.0 pccrit={_pccrit} plorient=1 ngcon=1 p_la=0u ptwell=0\n')
        f.write(f'MP43 net33 OUT VDD VDD slvtpfet w={_pmos4width}u l={_channellength}u nf={_Finger4}.0 pccrit={_pccrit} plorient=1 ngcon=1 p_la=0u ptwell=0\n')
        f.write(f'MP42 OUTb net26 net33 VDD slvtpfet w={_pmos3width}u l={_channellength}u nf={_Finger3}.0 pccrit={_pccrit} plorient=1 ngcon=1 p_la=0u ptwell=0\n')
        f.write(f'MP41 net35 OUTb VDD VDD slvtpfet w={_pmos4width}u l={_channellength}u nf={_Finger4}.0 pccrit={_pccrit} plorient=1 ngcon=1 p_la=0u ptwell=0\n')
        f.write(f'MP40 OUT net10 net35 VDD slvtpfet w={_pmos3width}u l={_channellength}u nf={_Finger3}.0 pccrit={_pccrit} plorient=1 ngcon=1 p_la=0u ptwell=0\n')
        f.write('XI49 IN net10 VDD VSS / Inv\n')
        f.write('XI46 INb net26 VDD VSS / Inv\n')
        f.write('.ENDS\n')

    return None

def makeSALatchSche(word, param):
    _CLKinputPMOSFinger1 = param.get('_CLKinputPMOSFinger1')
    _CLKinputPMOSFinger2 = param.get('_CLKinputPMOSFinger2')
    _PMOSFinger = param.get('_PMOSFinger')
    _PMOSChannelWidth = param.get('_PMOSChannelWidth')
    _DATAinputNMOSFinger = param.get('_DATAinputNMOSFinger')
    _NMOSFinger = param.get('_NMOSFinger')
    _CLKinputNMOSFinger = param.get('_CLKinputNMOSFinger')
    _NMOSChannelWidth = param.get('_NMOSChannelWidth')
    _CLKinputNMOSChannelWidth = param.get('_CLKinputNMOSChannelWidth')
    _ChannelLength = param.get('_ChannelLength')

    # Define pccrit layer creation
    if _ChannelLength == 30 or _ChannelLength == 34:
        _pccrit = 1
    else:
        _pccrit = 0

    # Define total finger width (for SS28nm tech)
    _nmoswidth = float(_NMOSChannelWidth * _NMOSFinger / 1000)
    _datainputnmoswidth = float(_NMOSChannelWidth * _DATAinputNMOSFinger / 1000)
    _clkinputnmoswidth = float(_CLKinputNMOSChannelWidth * _CLKinputNMOSFinger / 1000)

    _clkinputpmoswidth1 = float(_PMOSChannelWidth * _CLKinputPMOSFinger1 / 1000)
    _clkinputpmoswidth2 = float(_PMOSChannelWidth * _CLKinputPMOSFinger2 / 1000)
    _pmoswidth = float(_PMOSChannelWidth * _PMOSFinger / 1000)

    # Define channel length (for SS28nm tech)
    _channellength = float(_ChannelLength / 1000)

    # write netlist for SA latch
    with open(f'SALatch{word}.src.net', 'w') as f:
        f.write('.INCLUDE  /home/PDK/ss28nm/SEC_CDS/ln28lppdk/S00-V1.1.0.1_SEC2.0.6.2/oa/cmos28lp/.resources/devices.cdl\n')
        f.write('.SUBCKT SALatch CLK INn INp SSn SSp VDD VSS\n')
        f.write(f'MP5 net085 CLK VDD VDD slvtpfet w={_clkinputpmoswidth1}u l={_channellength}u nf={_CLKinputPMOSFinger1}.0 pccrit={_pccrit} plorient=1 ngcon=1 p_la=0u ptwell=0\n')
        f.write(f'MP4 SSp CLK VDD VDD slvtpfet w={_clkinputpmoswidth2}u l={_channellength}u nf={_CLKinputPMOSFinger2}.0 pccrit={_pccrit} plorient=1 ngcon=1 p_la=0u ptwell=0\n')
        f.write(f'MP3 net088 CLK VDD VDD slvtpfet w={_clkinputpmoswidth1}u l={_channellength}u nf={_CLKinputPMOSFinger1}.0 pccrit={_pccrit} plorient=1 ngcon=1 p_la=0u ptwell=0\n')
        f.write(f'MP2 SSn CLK VDD VDD slvtpfet w={_clkinputpmoswidth2}u l={_channellength}u nf={_CLKinputPMOSFinger2}.0 pccrit={_pccrit} plorient=1 ngcon=1 p_la=0u ptwell=0\n')
        f.write(f'MP1 SSn SSp VDD VDD slvtpfet w={_pmoswidth}u l={_channellength}u nf={_PMOSFinger}.0 pccrit={_pccrit} plorient=1 ngcon=1 p_la=0u ptwell=0\n')
        f.write(f'MP0 SSp SSn VDD VDD slvtpfet w={_pmoswidth}u l={_channellength}u nf={_PMOSFinger}.0 pccrit={_pccrit} plorient=1 ngcon=1 p_la=0u ptwell=0\n')
        f.write(f'MN7 net085 INn net083 VSS slvtnfet w={_datainputnmoswidth}u l={_channellength}u nf={_DATAinputNMOSFinger}.0 pccrit={_pccrit} plorient=1 ngcon=1 p_la=0u ptwell=0\n')
        f.write(f'MN2 net088 INp net083 VSS slvtnfet w={_datainputnmoswidth}u l={_channellength}u nf={_DATAinputNMOSFinger}.0 pccrit={_pccrit} plorient=1 ngcon=1 p_la=0u ptwell=0\n')
        f.write(f'MN4 SSp SSn net085 VSS slvtnfet w={_nmoswidth}u l={_channellength}u nf={_NMOSFinger}.0 pccrit={_pccrit} plorient=1 ngcon=1 p_la=0u ptwell=0\n')
        f.write(f'MN3 SSn SSp net088 VSS slvtnfet w={_nmoswidth}u l={_channellength}u nf={_NMOSFinger}.0 pccrit={_pccrit} plorient=1 ngcon=1 p_la=0u ptwell=0\n')
        f.write(f'MN1 net083 CLK VSS VSS slvtnfet w={_clkinputnmoswidth}u l={_channellength}u nf={_CLKinputNMOSFinger}.0 pccrit={_pccrit} plorient=1 ngcon=1 p_la=0u ptwell=0\n')
        f.write('.ENDS\n')

    return None

def makeINVSche(word, param):
    n_width = param.get('n_width')
    p_width = param.get('p_width')
    length = param.get('length')
    ngate = param.get('ngate')
    pgate = param.get('pgate')

    nw = n_width*ngate/1000
    pw = p_width*pgate/1000
    len = length/1000

    with open(f'inverter{word}.src.net', 'w') as f:
        f.write('.INCLUDE  /home/PDK/ss28nm/SEC_CDS/ln28lppdk/S00-V1.1.0.1_SEC2.0.6.2/oa/cmos28lp/.resources/devices.cdl\n')
        f.write('.PARAM\n')
        f.write('.SUBCKT inverter VDD VIN VOUT VSS\n')
        f.write(f'MN0 VOUT VIN VSS VSS slvtnfet w={nw}u l={len}u nf={ngate}.0 pccrit=0 plorient=1 ngcon=1 p_la=0u ptwell=0\n')
        # f.write(f'MN0 VOUT VIN VSS VSS slvtnfet w=1.2u l=0.08u nf=2.0 pccrit=0 plorient=1 ngcon=1 p_la=0u ptwell=0\n')
        f.write(f'MP0 VOUT VIN VDD VDD slvtpfet w={pw}u l={len}u nf={pgate}.0 pccrit=0 plorient=1 ngcon=1 p_la=0u ptwell=0\n')
        # f.write(f'MP0 VOUT VIN VDD VDD slvtpfet w=4.0u l=0.08u nf=4.0 pccrit=0 plorient=1 ngcon=1 p_la=0u ptwell=0\n')
        f.write('.ENDS')

    return None
