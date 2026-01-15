import os
from asyncore import write
from KJH91_Projects.Project_ADC.Layoutgen_code.A_Basic_Building_Block import A53_TIA_2stageamp


# def makeRBankCellSche(word, param):
#     _ResistorWidth = param.get('_ResistorWidth')
#     _ResistorLength = param.get('_ResistorLength')
#     _TransmissionGateFinger = param.get('_TransmissionGateFinger')
#     _TransmissionGateChannelWidth = param.get('_TransmissionGateChannelWidth')
#     _TransmissionGateChannelLength = param.get('_TransmissionGateChannelLength')
#     _TransmissionGateNPRatio = param.get('_TransmissionGateNPRatio')
#
#     # Define pccrit layer creation
#     if _TransmissionGateChannelLength == 30 or _TransmissionGateChannelLength == 34:
#         _pccrit = 1
#     else:
#         _pccrit = 0
#
#     _ResistorWidth = float(_ResistorWidth / 1000)
#     _ResistorLength = float(_ResistorLength / 1000)
#     _TGPMOSWidth = float(_TransmissionGateFinger * _TransmissionGateChannelWidth * _TransmissionGateNPRatio / 1000)
#     _TGNMOSWidth = float(_TransmissionGateFinger * _TransmissionGateChannelWidth / 1000)
#     _TGChannelLength = float(_TransmissionGateChannelLength / 1000)
#
#     if not os.path.exists('./ResistorBankCell'):
#         os.makedirs('./ResistorBankCell')
#     with open(f'ResistorBankCell{word}.src.net', 'w') as f:
#         f.write('.INCLUDE  /home/PDK/ss28nm/SEC_CDS/ln28lppdk/S00-V1.1.0.1_SEC2.0.6.2/oa/cmos28lp/.resources/devices.cdl\n')
#         f.write('.SUBCKT ResistorBankCell S SB VCM VDD VRX VSS\n')
#         f.write(f'RR20 VRX net13 $SUB=VSS $[opppcres] r=0.725156k w={_ResistorWidth}u l={_ResistorLength}u pbar=1 s=1 bp=3 ncr=2\n')
#         f.write(f'MN20 net13 S VCM VSS slvtnfet w={_TGNMOSWidth}u l={_TGChannelLength}u nf={_TransmissionGateFinger}.0 pccrit={_pccrit} plorient=1 ngcon=1 p_la=0u ptwell=0\n')
#         f.write(f'MP20 net13 SB VCM VDD slvtpfet w={_TGPMOSWidth}u l={_TGChannelLength}u nf={_TransmissionGateFinger}.0 pccrit={_pccrit} plorient=1 ngcon=1 p_la=0u ptwell=0\n')
#         f.write('.ENDS\n')
#     pass
#
# def makeRBankSche(word, param):
#     _XRBNum = param.get('_XRBNum')
#     _YRBNum = param.get('_YRBNum')
#     _ResistorWidth = param.get('_ResistorWidth')
#     _ResistorLength = param.get('_ResistorLength')
#     _TransmissionGateFinger = param.get('_TransmissionGateFinger')
#     _TransmissionGateChannelWidth = param.get('_TransmissionGateChannelWidth')
#     _TransmissionGateChannelLength = param.get('_TransmissionGateChannelLength')
#     _TransmissionGateNPRatio = param.get('_TransmissionGateNPRatio')
#
#     # Define pccrit layer creation
#     if _TransmissionGateChannelLength == 30 or _TransmissionGateChannelLength == 34:
#         _pccrit = 1
#     else:
#         _pccrit = 0
#
#     _ResistorWidth = float(_ResistorWidth / 1000)
#     _ResistorLength = float(_ResistorLength / 1000)
#     _TGPMOSWidth = float(_TransmissionGateFinger * _TransmissionGateChannelWidth * _TransmissionGateNPRatio / 1000)
#     _TGNMOSWidth = float(_TransmissionGateFinger * _TransmissionGateChannelWidth / 1000)
#     _TGChannelLength = float(_TransmissionGateChannelLength / 1000)
#
#     sel_lst = []
#     for i in range(_XRBNum * _YRBNum):
#         sel_lst.append(f'S<{i}> SB<{i}>')
#     sel_lst = ' '.join(sel_lst)
#
#     if not os.path.exists('./ResistorBank'):
#         os.makedirs('./ResistorBank')
#     with open(f'ResistorBank{word}.src.net', 'w') as f:
#         f.write('.INCLUDE  /home/PDK/ss28nm/SEC_CDS/ln28lppdk/S00-V1.1.0.1_SEC2.0.6.2/oa/cmos28lp/.resources/devices.cdl\n')
#         f.write('.SUBCKT ResistorBankCell S SB VCM VDD VRX VSS\n')
#         f.write(f'RR20 VRX net13 $SUB=VSS $[opppcres] r=0.725156k w={_ResistorWidth}u l={_ResistorLength}u pbar=1 s=1 bp=3 ncr=2\n')
#         f.write(f'MN20 net13 S VCM VSS slvtnfet w={_TGNMOSWidth}u l={_TGChannelLength}u nf={_TransmissionGateFinger}.0 pccrit={_pccrit} plorient=1 ngcon=1 p_la=0u ptwell=0\n')
#         f.write(f'MP20 net13 SB VCM VDD slvtpfet w={_TGPMOSWidth}u l={_TGChannelLength}u nf={_TransmissionGateFinger}.0 pccrit={_pccrit} plorient=1 ngcon=1 p_la=0u ptwell=0\n')
#         f.write('.ENDS\n')
#         f.write(f'.SUBCKT ResistorBank {sel_lst} VCM VDD VRX VSS\n')
#         for i in range(_XRBNum * _YRBNum):
#             f.write(f'XIR<{i}> S<{i}> SB<{i}> VCM VDD VRX VSS / ResistorBankCell\n')
#         f.write('.ENDS\n')
#     pass
#
# def makeRXSche(word, param):
#     _XRBNum = param.get('_XRBNum')
#     _YRBNum = param.get('_YRBNum')
#     _ResistorWidth = param.get('_ResistorWidth')
#     _ResistorLength = param.get('_ResistorLength')
#     _TransmissionGateFinger = param.get('_TransmissionGateFinger')
#     _TransmissionGateChannelWidth = param.get('_TransmissionGateChannelWidth')
#     _TransmissionGateChannelLength = param.get('_TransmissionGateChannelLength')
#     _TransmissionGateNPRatio = param.get('_TransmissionGateNPRatio')
#
#     if _TransmissionGateChannelLength == 30 or _TransmissionGateChannelLength == 34:
#         _RBpccrit = 1
#     else:
#         _RBpccrit = 0
#
#     _ResistorWidth = float(_ResistorWidth / 1000)
#     _ResistorLength = float(_ResistorLength / 1000)
#     _TGPMOSWidth = float(_TransmissionGateFinger * _TransmissionGateChannelWidth * _TransmissionGateNPRatio / 1000)
#     _TGNMOSWidth = float(_TransmissionGateFinger * _TransmissionGateChannelWidth / 1000)
#     _TGChannelLength = float(_TransmissionGateChannelLength / 1000)
#
#     sel_lst = []
#     for i in range(_XRBNum * _YRBNum):
#         sel_lst.append(f'S<{i}> SB<{i}>')
#     sel_lst = ' '.join(sel_lst)
#
#     _SRRandWidth = param.get('_SRRandWidth')
#     _SRNPRatio = param.get('_SRNPRatio')
#     _SRFinger1 = param.get('_SRFinger1')
#     _SRFinger2 = param.get('_SRFinger2')
#     _SRFinger3 = param.get('_SRFinger3')
#     _SRFinger4 = param.get('_SRFinger4')
#     _SRChannelLength = param.get('_SRChannelLength')
#
#     # Define pccrit layer creation
#     if _SRChannelLength == 30 or _SRChannelLength == 34:
#         _SRpccrit = 1
#     else:
#         _SRpccrit = 0
#
#     # Define total finger width (for SS28nm tech)
#     _SRnmos1width = float(_SRRandWidth * _SRFinger1 / 1000)
#     _SRnmos2width = float(_SRRandWidth * _SRFinger2 / 1000)
#     _SRnmos3width = float(_SRRandWidth * _SRFinger3 / 1000)
#     _SRnmos4width = float(_SRRandWidth * _SRFinger4 / 1000)
#     _SRpmos1width = float(_SRRandWidth * _SRFinger1 * _SRNPRatio / 1000)
#     _SRpmos2width = float(_SRRandWidth * _SRFinger2 * _SRNPRatio / 1000)
#     _SRpmos3width = float(_SRRandWidth * _SRFinger3 * _SRNPRatio / 1000)
#     _SRpmos4width = float(_SRRandWidth * _SRFinger4 * _SRNPRatio / 1000)
#
#     # Define channel length (for SS28nm tech)
#     _SRchannellength = float(_SRChannelLength / 1000)
#
#     _SLCLKinputPMOSFinger1 = param.get('_SLCLKinputPMOSFinger1')
#     _SLCLKinputPMOSFinger2 = param.get('_SLCLKinputPMOSFinger2')
#     _SLPMOSFinger = param.get('_SLPMOSFinger')
#     _SLPMOSChannelWidth = param.get('_SLPMOSChannelWidth')
#     _SLNMOSFinger = param.get('_SLNMOSFinger')
#     _SLDATAinputNMOSFinger = param.get('_SLDATAinputNMOSFinger')
#     _SLNMOSChannelWidth = param.get('_SLNMOSChannelWidth')
#     _SLCLKinputNMOSFinger = param.get('_SLCLKinputNMOSFinger')
#     _SLCLKinputNMOSChannelWidth = param.get('_SLCLKinputNMOSChannelWidth')
#     _SLChannelLength = param.get('_SLChannelLength')
#
#     # Define netlist parameter for SS28nm
#     if _SLChannelLength == 30 or _SLChannelLength == 34:
#         _SLpccrit = 1
#     else:
#         _SLpccrit = 0
#
#     _SLnmoswidth = float(_SLNMOSChannelWidth * _SLNMOSFinger / 1000)
#     _SLdatainputnmoswidth = float(_SLNMOSChannelWidth * _SLDATAinputNMOSFinger / 1000)
#     _SLclkinputnmoswidth = float(_SLCLKinputNMOSChannelWidth * _SLCLKinputNMOSFinger / 1000)
#
#     _SLclkinputpmoswidth1 = float(_SLPMOSChannelWidth * _SLCLKinputPMOSFinger1 / 1000)
#     _SLclkinputpmoswidth2 = float(_SLPMOSChannelWidth * _SLCLKinputPMOSFinger2 / 1000)
#     _SLpmoswidth = float(_SLPMOSChannelWidth * _SLPMOSFinger / 1000)
#     _SLchannellength = float(_SLChannelLength / 1000)
#
#     _InvChannelWidth = param.get('_InvChannelWidth')
#     _InvChannelLength = param.get('_InvChannelLength')
#     _InvFinger = param.get('_InvFinger')
#     _InvNPRatio = param.get('_InvNPRatio')
#
#     if _InvChannelLength == 30 or _InvChannelLength == 34:
#         _Invpccrit = 1
#     else:
#         _Invpccrit = 0
#
#     _Invnmoswidth = float(_InvChannelWidth * _InvFinger / 1000)
#     _Invpmoswidth = float(_InvChannelWidth * _InvFinger * _InvNPRatio / 1000)
#     _Invchannellength = float(_InvChannelLength / 1000)
#
#     _N = param.get('_N')
#     interleaving = []
#     for i in range(_N):
#         interleaving.append(f'CK<{i}> OUT<{i}> OUTb<{i}>')
#     interleaving = ' '.join(interleaving)
#
#     if not os.path.exists('./Receiver'):
#         os.makedirs('./Receiver')
#     with open(f'Receiver{word}.src.net', 'w') as f:
#         f.write('.INCLUDE  /home/PDK/ss28nm/SEC_CDS/ln28lppdk/S00-V1.1.0.1_SEC2.0.6.2/oa/cmos28lp/.resources/devices.cdl\n')
#         f.write('.GLOBAL VDD VSS\n')
#         f.write('.SUBCKT StrongArmLatch CLK INn INp SSn SSp VDD VSS\n')
#         f.write(
#             f'MP5 net085 CLK VDD VDD slvtpfet w={_SLclkinputpmoswidth1}u l={_SLchannellength}u nf={_SLCLKinputPMOSFinger1}.0 pccrit={_SLpccrit} plorient=1 ngcon=1 p_la=0u ptwell=0\n')
#         f.write(
#             f'MP4 SSp CLK VDD VDD slvtpfet w={_SLclkinputpmoswidth2}u l={_SLchannellength}u nf={_SLCLKinputPMOSFinger2}.0 pccrit={_SLpccrit} plorient=1 ngcon=1 p_la=0u ptwell=0\n')
#         f.write(
#             f'MP3 net088 CLK VDD VDD slvtpfet w={_SLclkinputpmoswidth1}u l={_SLchannellength}u nf={_SLCLKinputPMOSFinger1}.0 pccrit={_SLpccrit} plorient=1 ngcon=1 p_la=0u ptwell=0\n')
#         f.write(
#             f'MP2 SSn CLK VDD VDD slvtpfet w={_SLclkinputpmoswidth2}u l={_SLchannellength}u nf={_SLCLKinputPMOSFinger2}.0 pccrit={_SLpccrit} plorient=1 ngcon=1 p_la=0u ptwell=0\n')
#         f.write(
#             f'MP1 SSn SSp VDD VDD slvtpfet w={_SLpmoswidth}u l={_SLchannellength}u nf={_SLPMOSFinger}.0 pccrit={_SLpccrit} plorient=1 ngcon=1 p_la=0u ptwell=0\n')
#         f.write(
#             f'MP0 SSp SSn VDD VDD slvtpfet w={_SLpmoswidth}u l={_SLchannellength}u nf={_SLPMOSFinger}.0 pccrit={_SLpccrit} plorient=1 ngcon=1 p_la=0u ptwell=0\n')
#         f.write(
#             f'MN7 net085 INn net083 VSS slvtnfet w={_SLdatainputnmoswidth}u l={_SLchannellength}u nf={_SLDATAinputNMOSFinger}.0 pccrit={_SLpccrit} plorient=1 ngcon=1 p_la=0u ptwell=0\n')
#         f.write(
#             f'MN2 net088 INp net083 VSS slvtnfet w={_SLdatainputnmoswidth}u l={_SLchannellength}u nf={_SLDATAinputNMOSFinger}.0 pccrit={_SLpccrit} plorient=1 ngcon=1 p_la=0u ptwell=0\n')
#         f.write(
#             f'MN4 SSp SSn net085 VSS slvtnfet w={_SLnmoswidth}u l={_SLchannellength}u nf={_SLNMOSFinger}.0 pccrit={_SLpccrit} plorient=1 ngcon=1 p_la=0u ptwell=0\n')
#         f.write(
#             f'MN3 SSn SSp net088 VSS slvtnfet w={_SLnmoswidth}u l={_SLchannellength}u nf={_SLNMOSFinger}.0 pccrit={_SLpccrit} plorient=1 ngcon=1 p_la=0u ptwell=0\n')
#         f.write(
#             f'MN1 net083 CLK VSS VSS slvtnfet w={_SLclkinputnmoswidth}u l={_SLchannellength}u nf={_SLCLKinputNMOSFinger}.0 pccrit={_SLpccrit} plorient=1 ngcon=1 p_la=0u ptwell=0\n')
#         f.write('.ENDS\n')
#         f.write('.SUBCKT CLK_drv_inv IN OUT VDD VSS\n')
#         f.write(
#             f'MN10 OUT IN VSS VSS slvtnfet w={_Invnmoswidth}u l={_Invchannellength}u nf={_InvFinger}.0 pccrit={_Invpccrit} plorient=1 ngcon=1 p_la=0u ptwell=0\n'
#         )
#         f.write(
#             f'MP10 OUT IN VDD VDD slvtpfet w={_Invpmoswidth}u l={_Invchannellength}u nf={_InvFinger}.0 pccrit={_Invpccrit} plorient=1 ngcon=1 p_la=0u ptwell=0\n'
#         )
#         f.write('.ENDS\n')
#         f.write('.SUBCKT ResistorBankCell S SB VCM VDD VRX VSS\n')
#         f.write(
#             f'RR20 VRX net13 $SUB=VSS $[opppcres] r=0.725156k w={_ResistorWidth}u l={_ResistorLength}u pbar=1 s=1 bp=3 ncr=2\n')
#         f.write(
#             f'MN20 net13 S VCM VSS slvtnfet w={_TGNMOSWidth}u l={_TGChannelLength}u nf={_TransmissionGateFinger}.0 pccrit={_RBpccrit} plorient=1 ngcon=1 p_la=0u ptwell=0\n')
#         f.write(
#             f'MP20 net13 SB VCM VDD slvtpfet w={_TGPMOSWidth}u l={_TGChannelLength}u nf={_TransmissionGateFinger}.0 pccrit={_RBpccrit} plorient=1 ngcon=1 p_la=0u ptwell=0\n')
#         f.write('.ENDS\n')
#         f.write(f'.SUBCKT ResistorBank {sel_lst} VCM VDD VRX VSS\n')
#         for i in range(_XRBNum * _YRBNum):
#             f.write(f'XIR<{i}> S<{i}> SB<{i}> VCM VDD VRX VSS / ResistorBankCell\n')
#         f.write('.ENDS\n')
#         f.write('.SUBCKT Inv IN OUT VDD VSS\n')
#         f.write(
#             f'MN30 OUT IN VSS VSS slvtnfet w={_SRnmos2width}u l={_SRchannellength}u nf={_SRFinger2}.0 pccrit={_SRpccrit} plorient=1 ngcon=1 p_la=0u ptwell=0\n')
#         f.write(
#             f'MP30 OUT IN VDD VDD slvtpfet w={_SRpmos2width}u l={_SRchannellength}u nf={_SRFinger2}.0 pccrit={_SRpccrit} plorient=1 ngcon=1 p_la=0u ptwell=0\n')
#         f.write('.ENDS\n')
#         f.write('.SUBCKT SRLatch IN INb OUT OUTb VDD VSS\n')
#         f.write(
#             f'MN45 OUTb net26 VSS VSS slvtnfet w={_SRnmos1width}u l={_SRchannellength}u nf={_SRFinger1}.0 pccrit={_SRpccrit} plorient=1 ngcon=1 p_la=0u ptwell=0\n')
#         f.write(
#             f'MN48 net38 OUTb VSS VSS slvtnfet w={_SRnmos4width}u l={_SRchannellength}u nf={_SRFinger4}.0 pccrit={_SRpccrit} plorient=1 ngcon=1 p_la=0u ptwell=0\n')
#         f.write(
#             f'MN46 OUTb IN net37 VSS slvtnfet w={_SRnmos3width}u l={_SRchannellength}u nf={_SRFinger3}.0 pccrit={_SRpccrit} plorient=1 ngcon=1 p_la=0u ptwell=0\n')
#         f.write(
#             f'MN42 OUT net10 VSS VSS slvtnfet w={_SRnmos1width}u l={_SRchannellength}u nf={_SRFinger1}.0 pccrit={_SRpccrit} plorient=1 ngcon=1 p_la=0u ptwell=0\n')
#         f.write(
#             f'MN47 net37 OUT VSS VSS slvtnfet w={_SRnmos4width}u l={_SRchannellength}u nf={_SRFinger4}.0 pccrit={_SRpccrit} plorient=1 ngcon=1 p_la=0u ptwell=0\n')
#         f.write(
#             f'MN40 OUT INb net38 VSS slvtnfet w={_SRnmos3width}u l={_SRchannellength}u nf={_SRFinger3}.0 pccrit={_SRpccrit} plorient=1 ngcon=1 p_la=0u ptwell=0\n')
#         f.write(
#             f'MP45 OUT INb VDD VDD slvtpfet w={_SRpmos1width}u l={_SRchannellength}u nf={_SRFinger1}.0 pccrit={_SRpccrit} plorient=1 ngcon=1 p_la=0u ptwell=0\n')
#         f.write(
#             f'MP44 OUTb IN VDD VDD slvtpfet w={_SRpmos1width}u l={_SRchannellength}u nf={_SRFinger1}.0 pccrit={_SRpccrit} plorient=1 ngcon=1 p_la=0u ptwell=0\n')
#         f.write(
#             f'MP43 net33 OUT VDD VDD slvtpfet w={_SRpmos4width}u l={_SRchannellength}u nf={_SRFinger4}.0 pccrit={_SRpccrit} plorient=1 ngcon=1 p_la=0u ptwell=0\n')
#         f.write(
#             f'MP42 OUTb net26 net33 VDD slvtpfet w={_SRpmos3width}u l={_SRchannellength}u nf={_SRFinger3}.0 pccrit={_SRpccrit} plorient=1 ngcon=1 p_la=0u ptwell=0\n')
#         f.write(
#             f'MP41 net35 OUTb VDD VDD slvtpfet w={_SRpmos4width}u l={_SRchannellength}u nf={_SRFinger4}.0 pccrit={_SRpccrit} plorient=1 ngcon=1 p_la=0u ptwell=0\n')
#         f.write(
#             f'MP40 OUT net10 net35 VDD slvtpfet w={_SRpmos3width}u l={_SRchannellength}u nf={_SRFinger3}.0 pccrit={_SRpccrit} plorient=1 ngcon=1 p_la=0u ptwell=0\n')
#         f.write('XI49 IN net10 VDD VSS / Inv\n')
#         f.write('XI46 INb net26 VDD VSS / Inv\n')
#         f.write('.ENDS\n')
#         f.write(f'.SUBCKT Receiver {interleaving} {sel_lst} VCM VDD VRX VSS Vref\n')
#         for i in range(_N):
#             f.write(f'XISA<{i}> CLK<{i}> Vref VRX ssp<{i}> ssn<{i}> VDD VSS / StrongArmLatch\n')
#         for i in range(_N):
#             f.write(f'XIInv<{i}> CK<{i}> CLK<{i}> VDD VSS / CLK_drv_inv\n')
#         for i in range(_N):
#             f.write(f'XISR<{i}> ssn<{i}> ssp<{i}> OUT<{i}> OUTb<{i}> VDD VSS / SRLatch\n')
#         f.write(f'XI58 {sel_lst} VCM VDD VRX VSS / ResistorBank\n')
#         f.write('.ENDS\n')
#     pass
#
# def makeSRLatchSche(word, param):
#     _RandWidth = param.get('_RandWidth')
#     _NPRatio = param.get('_NPRatio')
#     _Finger1 = param.get('_Finger1')
#     _Finger2 = param.get('_Finger2')
#     _Finger3 = param.get('_Finger3')
#     _Finger4 = param.get('_Finger4')
#     _ChannelLength = param.get('_ChannelLength')
#
#     # Define pccrit layer creation
#     if _ChannelLength == 30 or _ChannelLength == 34:
#         _pccrit = 1
#     else:
#         _pccrit = 0
#
#     # Define total finger width (for SS28nm tech)
#     _nmos1width = float(_RandWidth * _Finger1 / 1000)
#     _nmos2width = float(_RandWidth * _Finger2 / 1000)
#     _nmos3width = float(_RandWidth * _Finger3 / 1000)
#     _nmos4width = float(_RandWidth * _Finger4 / 1000)
#     _pmos1width = float(_RandWidth * _Finger1 * _NPRatio / 1000)
#     _pmos2width = float(_RandWidth * _Finger2 * _NPRatio / 1000)
#     _pmos3width = float(_RandWidth * _Finger3 * _NPRatio / 1000)
#     _pmos4width = float(_RandWidth * _Finger4 * _NPRatio / 1000)
#
#     # Define channel length (for SS28nm tech)
#     _channellength = float(_ChannelLength / 1000)
#
#     # write netlist for SR latch
#     if not os.path.exists('./SRLatch'):
#         os.makedirs('./SRLatch')
#     with open(f'SRLatch{word}.src.net', 'w') as f:
#         f.write('.INCLUDE  /home/PDK/ss28nm/SEC_CDS/ln28lppdk/S00-V1.1.0.1_SEC2.0.6.2/oa/cmos28lp/.resources/devices.cdl\n')
#         f.write('.SUBCKT Inv IN OUT VDD VSS\n')
#         f.write(f'MN30 OUT IN VSS VSS slvtnfet w={_nmos2width}u l={_channellength}u nf={_Finger2}.0 pccrit={_pccrit} plorient=1 ngcon=1 p_la=0u ptwell=0\n')
#         f.write(f'MP30 OUT IN VDD VDD slvtpfet w={_pmos2width}u l={_channellength}u nf={_Finger2}.0 pccrit={_pccrit} plorient=1 ngcon=1 p_la=0u ptwell=0\n')
#         f.write('.ENDS\n')
#         f.write('.SUBCKT SRLatch IN INb OUT OUTb VDD VSS\n')
#         f.write(f'MN45 OUTb net26 VSS VSS slvtnfet w={_nmos1width}u l={_channellength}u nf={_Finger1}.0 pccrit={_pccrit} plorient=1 ngcon=1 p_la=0u ptwell=0\n')
#         f.write(f'MN48 net38 OUTb VSS VSS slvtnfet w={_nmos4width}u l={_channellength}u nf={_Finger4}.0 pccrit={_pccrit} plorient=1 ngcon=1 p_la=0u ptwell=0\n')
#         f.write(f'MN46 OUTb IN net37 VSS slvtnfet w={_nmos3width}u l={_channellength}u nf={_Finger3}.0 pccrit={_pccrit} plorient=1 ngcon=1 p_la=0u ptwell=0\n')
#         f.write(f'MN42 OUT net10 VSS VSS slvtnfet w={_nmos1width}u l={_channellength}u nf={_Finger1}.0 pccrit={_pccrit} plorient=1 ngcon=1 p_la=0u ptwell=0\n')
#         f.write(f'MN47 net37 OUT VSS VSS slvtnfet w={_nmos4width}u l={_channellength}u nf={_Finger4}.0 pccrit={_pccrit} plorient=1 ngcon=1 p_la=0u ptwell=0\n')
#         f.write(f'MN40 OUT INb net38 VSS slvtnfet w={_nmos3width}u l={_channellength}u nf={_Finger3}.0 pccrit={_pccrit} plorient=1 ngcon=1 p_la=0u ptwell=0\n')
#         f.write(f'MP45 OUT INb VDD VDD slvtpfet w={_pmos1width}u l={_channellength}u nf={_Finger1}.0 pccrit={_pccrit} plorient=1 ngcon=1 p_la=0u ptwell=0\n')
#         f.write(f'MP44 OUTb IN VDD VDD slvtpfet w={_pmos1width}u l={_channellength}u nf={_Finger1}.0 pccrit={_pccrit} plorient=1 ngcon=1 p_la=0u ptwell=0\n')
#         f.write(f'MP43 net33 OUT VDD VDD slvtpfet w={_pmos4width}u l={_channellength}u nf={_Finger4}.0 pccrit={_pccrit} plorient=1 ngcon=1 p_la=0u ptwell=0\n')
#         f.write(f'MP42 OUTb net26 net33 VDD slvtpfet w={_pmos3width}u l={_channellength}u nf={_Finger3}.0 pccrit={_pccrit} plorient=1 ngcon=1 p_la=0u ptwell=0\n')
#         f.write(f'MP41 net35 OUTb VDD VDD slvtpfet w={_pmos4width}u l={_channellength}u nf={_Finger4}.0 pccrit={_pccrit} plorient=1 ngcon=1 p_la=0u ptwell=0\n')
#         f.write(f'MP40 OUT net10 net35 VDD slvtpfet w={_pmos3width}u l={_channellength}u nf={_Finger3}.0 pccrit={_pccrit} plorient=1 ngcon=1 p_la=0u ptwell=0\n')
#         f.write('XI49 IN net10 VDD VSS / Inv\n')
#         f.write('XI46 INb net26 VDD VSS / Inv\n')
#         f.write('.ENDS\n')
#
#     return None
#
# def makeSALatchSche(word, param):
#     _CLKinputPMOSFinger1 = param.get('_CLKinputPMOSFinger1')
#     _CLKinputPMOSFinger2 = param.get('_CLKinputPMOSFinger2')
#     _PMOSFinger = param.get('_PMOSFinger')
#     _PMOSChannelWidth = param.get('_PMOSChannelWidth')
#     _DATAinputNMOSFinger = param.get('_DATAinputNMOSFinger')
#     _NMOSFinger = param.get('_NMOSFinger')
#     _CLKinputNMOSFinger = param.get('_CLKinputNMOSFinger')
#     _NMOSChannelWidth = param.get('_NMOSChannelWidth')
#     _CLKinputNMOSChannelWidth = param.get('_CLKinputNMOSChannelWidth')
#     _ChannelLength = param.get('_ChannelLength')
#
#     # Define pccrit layer creation
#     if _ChannelLength == 30 or _ChannelLength == 34:
#         _pccrit = 1
#     else:
#         _pccrit = 0
#
#     # Define total finger width (for SS28nm tech)
#     _nmoswidth = float(_NMOSChannelWidth * _NMOSFinger / 1000)
#     _datainputnmoswidth = float(_NMOSChannelWidth * _DATAinputNMOSFinger / 1000)
#     _clkinputnmoswidth = float(_CLKinputNMOSChannelWidth * _CLKinputNMOSFinger / 1000)
#
#     _clkinputpmoswidth1 = float(_PMOSChannelWidth * _CLKinputPMOSFinger1 / 1000)
#     _clkinputpmoswidth2 = float(_PMOSChannelWidth * _CLKinputPMOSFinger2 / 1000)
#     _pmoswidth = float(_PMOSChannelWidth * _PMOSFinger / 1000)
#
#     # Define channel length (for SS28nm tech)
#     _channellength = float(_ChannelLength / 1000)
#
#     # write netlist for SA latch
#     if not os.path.exists('./SALatch'):
#         os.makedirs('./SALatch')
#     with open(f'SALatch{word}.src.net', 'w') as f:
#         f.write('.INCLUDE  /home/PDK/ss28nm/SEC_CDS/ln28lppdk/S00-V1.1.0.1_SEC2.0.6.2/oa/cmos28lp/.resources/devices.cdl\n')
#         f.write('.SUBCKT SALatch CLK INn INp SSn SSp VDD VSS\n')
#         f.write(f'MP5 net085 CLK VDD VDD slvtpfet w={_clkinputpmoswidth1}u l={_channellength}u nf={_CLKinputPMOSFinger1}.0 pccrit={_pccrit} plorient=1 ngcon=1 p_la=0u ptwell=0\n')
#         f.write(f'MP4 SSp CLK VDD VDD slvtpfet w={_clkinputpmoswidth2}u l={_channellength}u nf={_CLKinputPMOSFinger2}.0 pccrit={_pccrit} plorient=1 ngcon=1 p_la=0u ptwell=0\n')
#         f.write(f'MP3 net088 CLK VDD VDD slvtpfet w={_clkinputpmoswidth1}u l={_channellength}u nf={_CLKinputPMOSFinger1}.0 pccrit={_pccrit} plorient=1 ngcon=1 p_la=0u ptwell=0\n')
#         f.write(f'MP2 SSn CLK VDD VDD slvtpfet w={_clkinputpmoswidth2}u l={_channellength}u nf={_CLKinputPMOSFinger2}.0 pccrit={_pccrit} plorient=1 ngcon=1 p_la=0u ptwell=0\n')
#         f.write(f'MP1 SSn SSp VDD VDD slvtpfet w={_pmoswidth}u l={_channellength}u nf={_PMOSFinger}.0 pccrit={_pccrit} plorient=1 ngcon=1 p_la=0u ptwell=0\n')
#         f.write(f'MP0 SSp SSn VDD VDD slvtpfet w={_pmoswidth}u l={_channellength}u nf={_PMOSFinger}.0 pccrit={_pccrit} plorient=1 ngcon=1 p_la=0u ptwell=0\n')
#         f.write(f'MN7 net085 INn net083 VSS slvtnfet w={_datainputnmoswidth}u l={_channellength}u nf={_DATAinputNMOSFinger}.0 pccrit={_pccrit} plorient=1 ngcon=1 p_la=0u ptwell=0\n')
#         f.write(f'MN2 net088 INp net083 VSS slvtnfet w={_datainputnmoswidth}u l={_channellength}u nf={_DATAinputNMOSFinger}.0 pccrit={_pccrit} plorient=1 ngcon=1 p_la=0u ptwell=0\n')
#         f.write(f'MN4 SSp SSn net085 VSS slvtnfet w={_nmoswidth}u l={_channellength}u nf={_NMOSFinger}.0 pccrit={_pccrit} plorient=1 ngcon=1 p_la=0u ptwell=0\n')
#         f.write(f'MN3 SSn SSp net088 VSS slvtnfet w={_nmoswidth}u l={_channellength}u nf={_NMOSFinger}.0 pccrit={_pccrit} plorient=1 ngcon=1 p_la=0u ptwell=0\n')
#         f.write(f'MN1 net083 CLK VSS VSS slvtnfet w={_clkinputnmoswidth}u l={_channellength}u nf={_CLKinputNMOSFinger}.0 pccrit={_pccrit} plorient=1 ngcon=1 p_la=0u ptwell=0\n')
#         f.write('.ENDS\n')
#
#     return None
#
# def makeINVSche(word, param):
#     n_width = param.get('n_width')
#     p_width = param.get('p_width')
#     n_length = param.get('n_length')
#     p_length = param.get('p_length')
#     n_gate = param.get('n_gate')
#     p_gate = param.get('p_gate')
#
#     nw = n_width * n_gate / 1000
#     pw = p_width * p_gate / 1000
#     n_len = n_length/1000
#     p_len = p_length/1000
#
#     if not os.path.exists('./inverter'):
#         os.makedirs('./inverter')
#     with open(f'./inverter/inverter{word}.src.net', 'w') as f:
#         f.write('.INCLUDE /home/PDK/ss28nm/SEC_CDS/ln28lppdk/S00-V1.1.0.1_SEC2.0.6.2/oa/cmos28lp/.resources/devices.cdl\n')
#         f.write('.PARAM\n')
#         f.write('.SUBCKT inverter VDD VIN VOUT VSS\n')
#         f.write(f'MN0 VOUT VIN VSS VSS slvtnfet w={nw}u l={n_len}u nf={n_gate}.0 pccrit=0 plorient=1 ngcon=1 p_la=0u ptwell=0\n')
#         f.write(f'MP0 VOUT VIN VDD VDD slvtpfet w={pw}u l={p_len}u nf={p_gate}.0 pccrit=0 plorient=1 ngcon=1 p_la=0u ptwell=0\n')
#         f.write('.ENDS')
#
#     return None
#
#
# def makeCTLESche(word, param):
#     RL_Width = param.get('RL_Width')
#     RL_Length = param.get('RL_Length')
#
#     W1_num_finger = param.get('W1_num_finger')
#     W1_finger_width = param.get('W1_finger_width')
#     W2_num_finger = param.get('W2_num_finger')
#     W2_finger_width = param.get('W2_finger_width')
#
#     RS_Width = param.get('RS_Width')
#     RS_Length = param.get('RS_Length')
#     CS_Width = param.get('CS_Width')
#     CS_Length = param.get('CS_Length')
#
#     W1_num_finger_float = float(W1_num_finger)
#     W1_total_width = W1_num_finger_float * W1_finger_width / 1000
#     W2_num_finger_float = float(W2_num_finger)
#     W2_total_width = W2_num_finger_float * W2_finger_width / 1000
#
#     RL_Width = RL_Width / 1000
#     RL_Length = RL_Length / 1000
#
#     RS_Width = RS_Width / 1000
#     RS_Length = RS_Length / 1000
#
#     CS_Width = CS_Width / 1000
#     CS_Length = CS_Length / 1000
#
#     if not os.path.exists('./CTLE'):
#         os.makedirs('./CTLE')
#
#     with open(f'./CTLE/CTLE{word}.src.net', 'w') as f:
#         f.write('************************************************************************\n')
#         f.write('* auCdl Netlist:\n')
#         f.write('* \n')
#         f.write('* Library Name:  song\n')
#         f.write(f'* Top Cell Name: 2023_12_CTLE_Schematic_Layout\n')
#         f.write('* View Name:     schematic\n')
#         f.write(f'* Netlisted on:  Mar  4 12:00:39 2025\n')
#         f.write('************************************************************************\n\n')
#         f.write(
#             '.INCLUDE /home/PDK/ss28nm/SEC_CDS/ln28lppdk/S00-V1.1.0.1_SEC2.0.6.2/oa/cmos28lp/.resources/devices.cdl\n')
#         f.write('*.EQUATION\n')
#         f.write('*.SCALE METER\n')
#         f.write('*.MEGA\n')
#         f.write('.PARAM\n')
#         f.write('************************************************************************\n')
#         f.write('* Library Name: song\n')
#         f.write('* Cell Name:    2023_12_CTLE_Schematic_Layout\n')
#         f.write('* View Name:    schematic\n')
#         f.write('************************************************************************\n\n')
#         f.write('.SUBCKT CTLE IDS VDD VSS Vinn Vinp Voutn Voutp\n')
#         f.write('*.PININFO IDS:B VDD:B VSS:B Vinn:B Vinp:B Voutn:B Voutp:B\n')
#         f.write(
#             f'MN5 net1 IDS VSS VSS slvtnfet w={W2_total_width}u l=0.03u nf={W2_num_finger}.0 pccrit=1 plorient=1 ngcon=1 p_la=0u ptwell=0\n')
#         f.write(
#             f'MN9 Voutp Vinn net6 VSS slvtnfet w={W1_total_width}u l=0.03u nf={W1_num_finger}.0 pccrit=1 plorient=1 ngcon=1 p_la=0u ptwell=0\n')
#         f.write(
#             f'MN6 net6 IDS VSS VSS slvtnfet w={W2_total_width}u l=0.03u nf={W2_num_finger}.0 pccrit=1 plorient=1 ngcon=1 p_la=0u ptwell=0\n')
#         f.write(
#             f'MN7 IDS IDS VSS VSS slvtnfet w={W2_total_width}u l=0.03u nf={W2_num_finger}.0 pccrit=1 plorient=1 ngcon=1 p_la=0u ptwell=0\n')
#         f.write(
#             f'MN8 Voutn Vinp net1 VSS slvtnfet w={W1_total_width}u l=0.03u nf={W1_num_finger}.0 pccrit=1 plorient=1 ngcon=1 p_la=0u ptwell=0\n')
#         f.write(f'RR5 Voutn VDD $SUB=VSS $[opppcres] w={RL_Width}u l={RL_Length}u pbar=1 s=1 bp=3 ncr=2\n')
#         f.write(f'RR4 Voutp VDD $SUB=VSS $[opppcres] w={RL_Width}u l={RL_Length}u pbar=1 s=1 bp=3 ncr=2\n')
#         f.write(f'RR3 net6 net1 $SUB=VSS $[opppcres] w={RS_Width}u l={RS_Length}u pbar=1 s=1 bp=3 ncr=2\n')
#         f.write(f'CC1 net6 net1 $[vncap] $SUB=VSS l={CS_Length}u w={CS_Width}u botlev=19 toplev=44 sizedup=1\n')
#         f.write(f'CC0 net1 net6 $[vncap] $SUB=VSS l={CS_Length}u w={CS_Width}u botlev=19 toplev=44 sizedup=1\n')
#         f.write('.ENDS\n')
#
#     print(f'CTLE Netlist 생성 완료: ./CTLE/CTLE{word}.src.net')
#     return None




# import os
# from datetime import datetime
#
# def makevpnpSche(word, param):
#     w = param.get('W')  # 단위는 나노미터로 가정 (예: 2500 -> 2.5u로 변환됨)
#     if w is None:
#         raise ValueError("param 딕셔너리에 'w' 값이 필요합니다.")
#
#     # 단위를 마이크로미터로 변환
#     wu = float(w) / 1000
#     lu = wu  # w == l 조건
#
#     # 현재 날짜와 시간
#     timestamp = datetime.now().strftime("%b %d %H:%M:%S %Y")
#
#     # 저장 디렉토리 생성
#     if not os.path.exists('./vpnp'):
#         os.makedirs('./vpnp')
#
#     # 파일 생성
#     with open(f'./vpnp/{word}.scs', 'w') as f:
#         # f.write(f"// Generated for: spectre\n")
#         # f.write(f"// Generated on: {timestamp}\n")
#         # f.write(f"// Design library name: Proj_BGR_B01_KSH\n")
#         # f.write(f"// Design cell name: {word}\n")
#         # f.write(f"// Design view name: schematic\n")
#         # f.write("simulator lang=spectre\n")
#         # f.write("global 0\n")
#         # #f.write('include "/mnt/sda/2023_DISU402/DISU40210/OPUS/Modelfiles/LNR28LPP_Spectre_S00-V1.4.6.2/LNR28LPP_Spectre_passive.lib" section=typical\n\n')
#         f.write('.INCLUDE /home/PDK/ss28nm/SEC_CDS/ln28lppdk/S00-V1.1.0.1_SEC2.0.6.2/oa/cmos28lp/.resources/devices.cdl\n')
#         #
#         # f.write(f"// Library name: Proj_BGR_B01_KSH\n")
#         # f.write(f"// Cell name: {word}\n")
#         # f.write(f"// View name: schematic\n")
#         # f.write(f"QP0 (C B E) vpnp nf=1 nrep=1 w={wu}u l={lu}u\n")
#         # f.write("simulatorOptions options reltol=1e-3 vabstol=1e-6 iabstol=1e-12 temp=27 \\\n")
#         # f.write("    tnom=25 scalem=1.0 scale=1.0 gmin=1e-12 rforce=1 maxnotes=5 maxwarns=5 \\\n")
#         # f.write("    digits=5 cols=80 pivrel=1e-3 sensfile=\"../psf/sens.output\" \\\n")
#         # f.write("    checklimitdest=psf \n")
#         # f.write("modelParameter info what=models where=rawfile\n")
#         # f.write("element info what=inst where=rawfile\n")
#         # f.write("outputParameter info what=output where=rawfile\n")
#         # f.write("designParamVals info what=parameters where=rawfile\n")
#         # f.write("primitives info what=primitives where=rawfile\n")
#         # f.write("subckts info what=subckts where=rawfile\n")
#         # f.write("saveOptions options save=allpub\n")
#
#         f.write(
#             '.INCLUDE /home/PDK/ss28nm/SEC_CDS/ln28lppdk/S00-V1.1.0.1_SEC2.0.6.2/oa/cmos28lp/.resources/devices.cdl\n')
#         f.write('.PARAM\n')
#         f.write(f"QP0 (C B E) vpnp nf=1 nrep=1 w={wu}u l={lu}u\n")
#
#         f.write('.ENDS')
#     return None




import os
from datetime import datetime

# def makevpnpSche(word, param):
#     w = param.get('W')
#     if w is None:
#         raise ValueError("param 딕셔너리에 'w' 값이 필요합니다.")
#
#     wu = float(w) / 1000  # 단위 변환: nm → um
#
#     now_str = datetime.now().strftime("%b %d %H:%M:%S %Y")
#
#     if not os.path.exists('./Verify_Rand_beginner_JH/vpnp'):
#         os.makedirs('./Verify_Rand_beginner_JH/vpnp')
#
#     with open(f'./Verify_Rand_beginner_JH/vpnp/vpnp{word}.src.net', 'w') as f:
#         f.write("************************************************************************\n")
#         f.write("* auCdl Netlist:\n")
#         f.write("* \n")
#         f.write("* Library Name:  Proj_BGR_B01_KSH\n")
#         f.write(f"* Top Cell Name: vpnp\n")
#         f.write("* View Name:     schematic\n")
#         f.write(f"* Netlisted on:  {now_str}\n")
#         f.write("************************************************************************\n\n")
#
#         # f.write(".INCLUDE  /tools/PDK/ss28lpp_rf/Device/LNR28LPP_CDS_S00-V1.4.6.1/CDS/oa/cmos28lp/.il/devices.cdl\n")
#         f.write(
#             '.INCLUDE /home/PDK/ss28nm/SEC_CDS/ln28lppdk/S00-V1.1.0.1_SEC2.0.6.2/oa/cmos28lp/.resources/devices.cdl\n')
#         f.write("*.EQUATION\n")
#         f.write("*.SCALE METER\n")
#         f.write("*.MEGA\n")
#         f.write(".PARAM\n\n\n")
#
#         f.write("************************************************************************\n")
#         f.write("* Library Name: Proj_BGR_B01_KSH\n")
#         f.write(f"* Cell Name:    vpnp\n")
#         f.write("* View Name:    schematic\n")
#         f.write("************************************************************************\n\n")
#
#         f.write(f".SUBCKT vpnp B C E\n")
#         f.write("*.PININFO B:B C:B E:B\n")
#         f.write(f"QQP0 C B E vpnp nf=1 nrep=1 w={wu:.4f}u l={wu:.4f}u\n")
#         f.write(".ENDS\n")
#
#     return None



# def makeopampSche(word, param):
#     finger_N1 = param.get('finger_N1')
#     finger_N2 = param.get('finger_N2')
#     finger_P1 = param.get('finger_P1')
#     finger_P5 = param.get('finger_P5')
#     finger_N5 = param.get('finger_N5')
#     finger_N4 = param.get('finger_N4')
#     finger_P3 = param.get('finger_P3')
#     finger_P4 = param.get('finger_P4')
#     W_N = 700
#     L =param.get('L')
#     Dummy = True
#     XVT = 'RVT'
#     W_P = 700
#     Guad_via = 2
#     res_compensation_W = param.get('res_compensation_W')
#     res_compensation_L = param.get('res_compensation_L')
#     res_compensation_series = param.get('res_compensation_series')
#     NumofGate_res_com = param.get('NumofGate_res_com')
#     NumofRX_res_com = param.get('NumofRX_res_com')
#     L_cap = param.get('L_cap')
#     W_cap = param.get('W_cap')
#     B00_amp_v2 = B00_amp_v4_using_gui.B00_amp_v2(_DesignParameter=None, _Name='opamp')
#     B00_amp_v2_param = B00_amp_v2._CalculateDesignParameter(finger_N1=finger_N1, finger_N2=finger_N2, finger_P1=finger_P1,  finger_P5=finger_P5, finger_N5=finger_N5, finger_N4=finger_N4, finger_P3=finger_P3,finger_P4=finger_P4,W_N=W_N,L=L,Dummy=Dummy,XVT=XVT,W_P=W_P,Guad_via=Guad_via,res_compensation_W=res_compensation_W,res_compensation_L=res_compensation_L,res_compensation_series=res_compensation_series,NumofGate_res_com=NumofGate_res_com,NumofRX_res_com=NumofRX_res_com,L_cap=L_cap,W_cap=W_cap )
#     finger_N_Dummy1,finger_N_Dummy2,finger_P_Dummy1,finger_P_Dummy2  = B00_amp_v2_param
#     # if w is None:
#     #     raise ValueError("param 딕셔너리에 'w' 값이 필요합니다.")
#
#     W_N = float(W_N) / 1000  # 단위 변환: nm → um
#     L = float(L) / 1000
#     W_P = float(W_P) / 1000
#     L_cap = float(L_cap) / 1000
#     W_cap = float(W_cap) / 1000
#     res_compensation_W = float(res_compensation_W) / 1000
#     res_compensation_L = float(res_compensation_L) / 1000
    # fingerA = ((((finger_P1 + finger_P5) - finger_N2) - finger_N5) + 1)
    # fingerB = ((finger_N4 - finger_N5) + 1)
    # fingerC = (((((finger_P1 + finger_P3) + finger_P4) + 2) - finger_N2) - finger_N5)
    # finger_N_Dummy2 = max(2, fingerA, fingerB, fingerC)
    # finger_P_Dummy1 = ((((finger_N2 + finger_N5) - finger_P1) - finger_P5) + finger_N_Dummy2)
    # finger_N_Dummy1 = ((finger_N_Dummy2 + finger_N5) - finger_N4)
    # finger_P_Dummy2 = ((((((finger_N2 + finger_N5) + finger_N_Dummy2) - finger_P1) - finger_P3) - finger_P4) - 1)


    # if (finger_P_Dummy2 + finger_P1) % 2 == 1 and finger_P3 % 2 == 1:
    #     finger_P3 +=1
    #
    # if (finger_P_Dummy2 + finger_P1) % 2 == 0 and finger_P3 % 2 == 0:
    #     finger_P3 +=1

    # now_str = datetime.now().strftime("%b %d %H:%M:%S %Y")
    # if not os.path.exists('./Verify_Rand_beginner_JH/opamp'):
    #     os.makedirs('./Verify_Rand_beginner_JH/opamp')
    # if L == 30/1000:
    #     pccrit =1
    # else:
    #     pccrit = 0
    # with open(f'./Verify_Rand_beginner_JH/opamp/opamp{word}.src.net', 'w') as f:
    #     f.write("************************************************************************\n")
    #     f.write("* auCdl Netlist:\n")
    #     f.write("* \n")
    #     f.write("* Library Name:  Laygen_AMP\n")
    #     f.write(f"* Top Cell Name: opamp\n")
    #     f.write("* View Name:     schematic\n")
    #     f.write(f"* Netlisted on:  {now_str}\n")
    #     f.write("************************************************************************\n\n")
    #
    #     # f.write(".INCLUDE  /tools/PDK/ss28lpp_rf/Device/LNR28LPP_CDS_S00-V1.4.6.1/CDS/oa/cmos28lp/.il/devices.cdl\n")
    #     f.write('.INCLUDE /home/PDK/ss28nm/SEC_CDS/ln28lppdk/S00-V1.1.0.1_SEC2.0.6.2/oa/cmos28lp/.resources/devices.cdl\n')
    #     f.write("*.EQUATION\n")
    #     f.write("*.SCALE METER\n")
    #     f.write("*.MEGA\n")
    #     f.write(".PARAM\n\n\n")
    #
    #     f.write("************************************************************************\n")
    #     f.write("* Library Name: Laygen_AMP\n")
    #     f.write(f"* Cell Name:    opamp\n")
    #     f.write("* View Name:    schematic\n")
    #     f.write("************************************************************************\n\n")
    #
    #     f.write(f".SUBCKT opamp VDD VINn VINp VOUT VSS\n")
    #     f.write("*.PININFO VDD:B VINn:B VINp:B VOUT:B VSS:B\n")
    #     f.write(f"MN1 net6 net1 VSS VSS nfet w={finger_N1*W_N:.4f}u l={L:.4f}u nf={finger_N1:.4f} pccrit={pccrit} plorient=1 ngcon=1 p_la=0u ptwell=0\n")
    #     f.write(f"MN5 VOUT net1 VSS VSS nfet w={finger_N5*W_N:.4f}u l={L:.4f}u nf={finger_N5:.4f} pccrit={pccrit} plorient=1 ngcon=1 p_la=0u ptwell=0\n")
    #     f.write(f"MN3 net2 VINp net6 VSS nfet w={finger_N2*W_N:.4f}u l={L:.4f}u nf={finger_N2:.4f} pccrit={pccrit} plorient=1 ngcon=1 p_la=0u ptwell=0\n")
    #     f.write(f"MN2 net5 VINn net6 VSS nfet w={finger_N2*W_N:.4f}u l={L:.4f}u nf={finger_N2:.4f} pccrit={pccrit} plorient=1 ngcon=1 p_la=0u ptwell=0\n")
    #     f.write(f"MN_Dummy VSS VSS VSS VSS nfet w={(finger_N_Dummy1+finger_N_Dummy2)*W_N:.4f}u l={L:.4f}u nf={(finger_N_Dummy1+finger_N_Dummy2):.4f} pccrit={pccrit} plorient=1 ngcon=1 p_la=0u ptwell=0\n")
    #     f.write(f"MN4 net1 net1 VSS VSS nfet w={finger_N4*W_N:.4f}u l={L:.4f}u nf={finger_N4:.4f} pccrit={pccrit} plorient=1 ngcon=1 p_la=0u ptwell=0\n")
    #     f.write(f"MP1 net5 net5 VDD VDD pfet w={finger_P1*W_P:.4f}u l={L:.4f}u nf={finger_P1:.4f} pccrit={pccrit} plorient=1 ngcon=1 p_la=0u ptwell=0\n")
    #     f.write(f"MP4 net1 net1 net3 VDD pfet w={finger_P4*W_P:.4f}u l={L:.4f}u nf={finger_P4:.4f} pccrit={pccrit} plorient=1 ngcon=1 p_la=0u ptwell=0\n")
    #     f.write(f"MP2 net2 net5 VDD VDD pfet w={finger_P1*W_P:.4f}u l={L:.4f}u nf={finger_P1:.4f} pccrit={pccrit} plorient=1 ngcon=1 p_la=0u ptwell=0\n")
    #     f.write(f"MP_Dummy VDD VDD VDD VDD pfet w={(finger_N1+finger_P_Dummy1+finger_P_Dummy2)*W_P:.4f}u l={L:.4f}u nf={(finger_N1+finger_P_Dummy1+finger_P_Dummy2):.4f} pccrit={pccrit} plorient=1 ngcon=1 p_la=0u ptwell=0\n")
    #     f.write(f"MP3 net3 net3 VDD VDD pfet w={finger_P3*W_P:.4f}u l={L:.4f}u nf={finger_P3:.4f} pccrit={pccrit} plorient=1 ngcon=1 p_la=0u ptwell=0\n")
    #     f.write(f"MP5 VOUT net2 VDD VDD pfet w={finger_P5*W_P:.4f}u l={L:.4f}u nf={finger_P5:.4f} pccrit={pccrit} plorient=1 ngcon=1 p_la=0u ptwell=0\n")
    #     f.write(f"CC2 net2 net4 $[ncap] $SUB=VSS l={L_cap:.4f}u w={W_cap:.4f}u nf={NumofGate_res_com:.4f} nrep={NumofRX_res_com:.4f}\n")
    #     f.write(f"RR1 VOUT net4 $SUB=VSS $[opppcres] r=3.039k w={res_compensation_W:.4f}u l={res_compensation_L:.4f}u pbar=1 s={res_compensation_series:.4f} bp=3 ncr=1\n")
    #     f.write(".ENDS\n")
    #
    # return None

# def make_2stageampSche(word, param):
#     finger_P0=param.get('_Tr0_PMOSNumberofGate')
#     width_P0=param.get('_Tr0_PMOSChannelWidth')
#     finger_P1 = param.get('_Tr1_PMOSNumberofGate')
#     width_P1 = param.get('_Tr1_PMOSChannelWidth')
#     finger_P2 = param.get('_Tr2_PMOSNumberofGate')
#     width_P2 = param.get('_Tr2_PMOSChannelWidth')
#     finger_P3 = param.get('_Tr3_PMOSNumberofGate')
#     width_P3 = param.get('_Tr3_PMOSChannelWidth')
#     finger_P4 = param.get('_Tr4_PMOSNumberofGate')
#     width_P4 = param.get('_Tr4_PMOSChannelWidth')
#     finger_N0 = param.get('_Tr0_NMOSNumberofGate')
#     width_N0 = param.get('_Tr0_NMOSChannelWidth')
#     finger_N1 = param.get('_Tr1_NMOSNumberofGate')
#     width_N1 = param.get('_Tr1_NMOSChannelWidth')
#     finger_N2 = param.get('_Tr2_NMOSNumberofGate')
#     width_N2 = param.get('_Tr2_NMOSChannelWidth')
#     finger_N3 = param.get('_Tr3_NMOSNumberofGate')
#     width_N3 = param.get('_Tr3_NMOSChannelWidth')
#     finger_N4 = param.get('_Tr4_NMOSNumberofGate')
#     width_N4 = param.get('_Tr4_NMOSChannelWidth')
#     width_res0 = param.get('_ResWidth_res0')
#     length_res0 = param.get('_ResLength_res0')
#     width_res1 = param.get('_ResWidth_res1')
#     length_res1 = param.get('_ResLength_res1')
#     finger_cap0 = param.get('_NumFigPair_cap0')
#     length_cap0 = param.get('_Length_cap0')
#     finger_cap1 = param.get('_NumFigPair_cap1')
#     length_cap1 = param.get('_Length_cap1')
#     CAP0_LayoutOption = param.get('_LayoutOption_cap0')
#     CAP1_LayoutOption = param.get('_LayoutOption_cap1')
#     lev_mapping = {  # cmos28lp Spectre manual
#         1: 15,
#         2: 17,
#         3: 19,
#         4: 21,
#         5: 31,
#         6: 44,
#         7: 46
#     }
#     min_num_cap0 = min(CAP0_LayoutOption)
#     max_num_cap0 = max(CAP0_LayoutOption)
#     botlev_cap0 = lev_mapping.get(min_num_cap0, None)  # 낮은 메탈 값 매핑
#     toplev_cap0 = lev_mapping.get(max_num_cap0, None)  # 높은 메탈 값 매핑
#     min_num_cap1 = min(CAP1_LayoutOption)
#     max_num_cap1 = max(CAP1_LayoutOption)
#     botlev_cap1 = lev_mapping.get(min_num_cap1, None)  # 낮은 메탈 값 매핑
#     toplev_cap1 = lev_mapping.get(max_num_cap1, None)  # 높은 메탈 값 매핑
#
#     now_str = datetime.now().strftime("%b %d %H:%M:%S %Y")
#     if not os.path.exists(rf'C:\Users\KJB\PycharmProjects\LayGenGUI\generatorLib\generator_models\Verify_Rand_beginner_JH\_2stageamp'):
#         os.makedirs(rf'C:\Users\KJB\PycharmProjects\LayGenGUI\generatorLib\generator_models\Verify_Rand_beginner_JH\_2stageamp')
#
#     with open(rf'C:\Users\KJB\PycharmProjects\LayGenGUI\generatorLib\generator_models\Verify_Rand_beginner_JH\_2stageamp\_2stageamp{word}.src.net', 'w') as f:
#         f.write("************************************************************************\n")
#         f.write("* auCdl Netlist:\n")
#         f.write("* \n")
#         f.write(f"* Library Name:  _2stageamp_{word}\n")
#         f.write(f"* Top Cell Name: _2stageamp\n")
#         f.write("* View Name:     schematic\n")
#         f.write(f"* Netlisted on:  {now_str}\n")
#         f.write("************************************************************************\n\n")
#
#         f.write(".INCLUDE  /tools/PDK/ss28lpp_rf/Device/LNR28LPP_CDS_S00-V1.4.6.1/CDS/oa/cmos28lp/.il/devices.cdl\n")
#         # f.write('.INCLUDE /home/PDK/ss28nm/SEC_CDS/ln28lppdk/S00-V1.1.0.1_SEC2.0.6.2/oa/cmos28lp/.resources/devices.cdl\n')
#         f.write("*.EQUATION\n")
#         f.write("*.SCALE METER\n")
#         f.write("*.MEGA\n")
#         f.write(".PARAM\n\n\n\n")
#
#         f.write("************************************************************************\n")
#         f.write(f"* Library Name: 2satgeamp_{word}\n")
#         f.write(f"* Cell Name:    _2stageamp\n")
#         f.write("* View Name:    schematic\n")
#         f.write("************************************************************************\n\n")
#
#         f.write(f".SUBCKT _2stageamp VBN VBP VDD VINN VINP VOUT VSS\n")
#         f.write("*.PININFO VBN:B VBP:B VDD:B VINN:B VINP:B VOUT:B VSS:B\n")
#         f.write(f"MN11 VBP VBP VBN VSS egnfet w={(finger_N3*width_N3)/1000:.4f}u l=0.15u nf={finger_N3:.4f} pccrit=0 plorient=1 ngcon=1 p_la=0u ptwell=0\n")
#         f.write(f"MN9 VBN VBN VSS VSS egnfet w={(finger_N2*width_N2)/1000:.4f}u l=0.15u nf={finger_N2:.4f} pccrit=0 plorient=1 ngcon=1 p_la=0u ptwell=0\n")
#         f.write(f"MN0 net6 net6 VSS VSS egnfet w={(finger_N0*width_N0)/1000:.4f}u l=0.15u nf={finger_N0:.4f} pccrit=0 plorient=1 ngcon=1 p_la=0u ptwell=0\n")
#         f.write(f"MN1 VOUT1 net6 VSS VSS egnfet w={(finger_N1*width_N1)/1000:.4f}u l=0.15u nf={finger_N1:.4f} pccrit=0 plorient=1 ngcon=1 p_la=0u ptwell=0\n")
#         f.write(f"MN33 VOUT VOUT1 VSS VSS egnfet w={(finger_N4*width_N4)/1000:.4f}u l=0.15u nf={finger_N4:.4f} pccrit=0 plorient=1 ngcon=1 p_la=0u ptwell=0\n")
#         f.write(f"RR0 net10 VOUT1 $SUB=VSS $[opppcres] r=0.926k w={(width_res1)/1000:.4f}u l={(length_res1)/1000:.4f}u pbar=1 s=1 bp=3 ncr=1\n")
#         f.write(f"RR6 net10 VOUT1 $SUB=VSS $[opppcres] r=0.926k w={(width_res0)/1000:.4f}u l={(length_res0)/1000:.4f}u pbar=1 s=1 bp=3 ncr=1\n")
#         f.write(f"CC0 VOUT net10 $[hdvncap] $SUB=VSS l={(length_cap1)/1000:.4f}u w={(finger_cap1-1)*0.2+0.35:.4f}u botlev={botlev_cap1} toplev={toplev_cap1}\n")
#         f.write(f"CC2 VOUT net10 $[hdvncap] $SUB=VSS l={(length_cap0)/1000:.4f}u w={(finger_cap0-1)*0.2+0.35:.4f}u botlev={botlev_cap0} toplev={toplev_cap0}\n")
#         f.write(f"MP2 net38 VBP VDD VDD egpfet w={(finger_P0*width_P0)/1000:.4f}u l=0.15u nf={finger_P0:.4f} pccrit=0 plorient=1 ngcon=1 p_la=0u ptwell=0\n")
#         f.write(f"MP7 VBP VBP VDD VDD egpfet w={(finger_P3*width_P3)/1000:.4f}u l=0.15u nf={finger_P3:.4f} pccrit=0 plorient=1 ngcon=1 p_la=0u ptwell=0\n")
#         f.write(f"MP0 net6 VINN net38 VDD egpfet w={(finger_P1*width_P1)/1000:.4f}u l=0.15u nf={finger_P1:.4f} pccrit=0 plorient=1 ngcon=1 p_la=0u ptwell=0\n")
#         f.write(f"MP1 VOUT1 VINP net38 VDD egpfet w={(finger_P2*width_P2)/1000:.4f}u l=0.15u nf={finger_P2:.4f} pccrit=0 plorient=1 ngcon=1 p_la=0u ptwell=0\n")
#         f.write(f"MP14 VOUT VBP VDD VDD egpfet w={(finger_P4*width_P4)/1000:.4f}u l=0.15u nf={finger_P4:.4f} pccrit=0 plorient=1 ngcon=1 p_la=0u ptwell=0\n")
#         f.write(".ENDS\n")
#     return None

def makeTIASche(word, param):
    # 1st_amp
    _op1_P0_finger = param.get('_op1_Tr0_PMOSNumberofGate')
    _op1_P0_width = param.get('_op1_Tr0_PMOSChannelWidth')
    _op1_P1_finger = param.get('_op1_Tr1_PMOSNumberofGate')
    _op1_P1_width = param.get('_op1_Tr1_PMOSChannelWidth')
    _op1_P2_finger = param.get('_op1_Tr2_PMOSNumberofGate')
    _op1_P2_width = param.get('_op1_Tr2_PMOSChannelWidth')
    _op1_P3_finger = param.get('_op1_Tr3_PMOSNumberofGate')
    _op1_P3_width = param.get('_op1_Tr3_PMOSChannelWidth')
    _op1_P4_finger = param.get('_op1_Tr4_PMOSNumberofGate')
    _op1_P4_width = param.get('_op1_Tr4_PMOSChannelWidth')
    _op1_N0_finger = param.get('_op1_Tr0_NMOSNumberofGate')
    _op1_N0_width = param.get('_op1_Tr0_NMOSChannelWidth')
    _op1_N1_finger = param.get('_op1_Tr1_NMOSNumberofGate')
    _op1_N1_width = param.get('_op1_Tr1_NMOSChannelWidth')
    _op1_N2_finger = param.get('_op1_Tr2_NMOSNumberofGate')
    _op1_N2_width = param.get('_op1_Tr2_NMOSChannelWidth')
    _op1_N3_finger = param.get('_op1_Tr3_NMOSNumberofGate')
    _op1_N3_width = param.get('_op1_Tr3_NMOSChannelWidth')
    _op1_N4_finger = param.get('_op1_Tr4_NMOSNumberofGate')
    _op1_N4_width = param.get('_op1_Tr4_NMOSChannelWidth')
    _op1_res0_width = param.get('_op1_ResWidth_res0')
    _op1_res0_length = param.get('_op1_ResLength_res0')
    _op1_res1_width = param.get('_op1_ResWidth_res1')
    _op1_res1_length = param.get('_op1_ResLength_res1')
    _op1_cap0_finger = param.get('_op1_NumFigPair_cap0')
    _op1_cap0_length = param.get('_op1_Length_cap0')
    _op1_cap1_finger = param.get('_op1_NumFigPair_cap1')
    _op1_cap1_length = param.get('_op1_Length_cap1')
    _op1_cap0_LayoutOption = param.get('_op1_LayoutOption_cap0')
    _op1_cap1_LayoutOption = param.get('_op1_LayoutOption_cap1')
    lev_mapping = {  # cmos28lp Spectre manual
        1: 15,
        2: 17,
        3: 19,
        4: 21,
        5: 31,
        6: 44,
        7: 46
    }
    _op1_cap0_min_num = min(_op1_cap0_LayoutOption)
    _op1_cap0_max_num = max(_op1_cap0_LayoutOption)
    _op1_cap0_botlev = lev_mapping.get(_op1_cap0_min_num, None)  # 낮은 메탈 값 매핑
    _op1_cap0_toplev = lev_mapping.get(_op1_cap0_max_num, None)  # 높은 메탈 값 매핑
    _op1_cap1_min_num = min(_op1_cap1_LayoutOption)
    _op1_cap1_max_num = max(_op1_cap1_LayoutOption)
    _op1_cap1_botlev = lev_mapping.get(_op1_cap1_min_num, None)  # 낮은 메탈 값 매핑
    _op1_cap1_toplev = lev_mapping.get(_op1_cap1_max_num, None)  # 높은 메탈 값 매핑

    # 2nd_amp
    _op2_P0_finger = param.get('_op2_Tr0_PMOSNumberofGate')
    _op2_P0_width = param.get('_op2_Tr0_PMOSChannelWidth')
    _op2_P1_finger = param.get('_op2_Tr1_PMOSNumberofGate')
    _op2_P1_width = param.get('_op2_Tr1_PMOSChannelWidth')
    _op2_P2_finger = param.get('_op2_Tr2_PMOSNumberofGate')
    _op2_P2_width = param.get('_op2_Tr2_PMOSChannelWidth')
    _op2_P3_finger = param.get('_op2_Tr3_PMOSNumberofGate')
    _op2_P3_width = param.get('_op2_Tr3_PMOSChannelWidth')
    _op2_P4_finger = param.get('_op2_Tr4_PMOSNumberofGate')
    _op2_P4_width = param.get('_op2_Tr4_PMOSChannelWidth')
    _op2_N0_finger = param.get('_op2_Tr0_NMOSNumberofGate')
    _op2_N0_width = param.get('_op2_Tr0_NMOSChannelWidth')
    _op2_N1_finger = param.get('_op2_Tr1_NMOSNumberofGate')
    _op2_N1_width = param.get('_op2_Tr1_NMOSChannelWidth')
    _op2_N2_finger = param.get('_op2_Tr2_NMOSNumberofGate')
    _op2_N2_width = param.get('_op2_Tr2_NMOSChannelWidth')
    _op2_N3_finger = param.get('_op2_Tr3_NMOSNumberofGate')
    _op2_N3_width = param.get('_op2_Tr3_NMOSChannelWidth')
    _op2_N4_finger = param.get('_op2_Tr4_NMOSNumberofGate')
    _op2_N4_width = param.get('_op2_Tr4_NMOSChannelWidth')
    _op2_res0_width = param.get('_op2_ResWidth_res0')
    _op2_res0_length = param.get('_op2_ResLength_res0')
    _op2_res1_width = param.get('_op2_ResWidth_res1')
    _op2_res1_length = param.get('_op2_ResLength_res1')
    _op2_cap0_finger = param.get('_op2_NumFigPair_cap0')
    _op2_cap0_length = param.get('_op2_Length_cap0')
    _op2_cap1_finger = param.get('_op2_NumFigPair_cap1')
    _op2_cap1_length = param.get('_op2_Length_cap1')
    _op2_cap0_LayoutOption = param.get('_op2_LayoutOption_cap0')
    _op2_cap1_LayoutOption = param.get('_op2_LayoutOption_cap1')

    _op2_cap0_min_num = min(_op2_cap0_LayoutOption)
    _op2_cap0_max_num = max(_op2_cap0_LayoutOption)
    _op2_cap0_botlev = lev_mapping.get(_op2_cap0_min_num, None)  # 낮은 메탈 값 매핑
    _op2_cap0_toplev = lev_mapping.get(_op2_cap0_max_num, None)  # 높은 메탈 값 매핑
    _op2_cap1_min_num = min(_op2_cap1_LayoutOption)
    _op2_cap1_max_num = max(_op2_cap1_LayoutOption)
    _op2_cap1_botlev = lev_mapping.get(_op2_cap1_min_num, None)  # 낮은 메탈 값 매핑
    _op2_cap1_toplev = lev_mapping.get(_op2_cap1_max_num, None)  # 높은 메탈 값 매핑

    # RESA
    _ResWidth_resA = param.get('_ResWidth_resA')
    _ResLength_resA = param.get('_ResLength_resA')
    _SeriesStripes_resA = param.get('_SeriesStripes_resA')
    _ParallelStripes_resA = param.get('_ParallelStripes_resA')


    ### 2nd Feedback
    # Res_2nd
    _ResWidth_2nd = param.get('_ResWidth_2nd')
    _ResLength_2nd = param.get('_ResLength_2nd')
    _SeriesStripes_2nd = param.get('_SeriesStripes_2nd')
    _ParallelStripes_2nd = param.get('_ParallelStripes_2nd')

    # Cap_2nd
    _Length_2nd = param.get('_Length_2nd')
    _LayoutOption_2nd = param.get('_LayoutOption_2nd')
    min_num_2nd = min(_LayoutOption_2nd)
    max_num_2nd = max(_LayoutOption_2nd)
    botlev_2nd = lev_mapping.get(min_num_2nd, None)  # 낮은 메탈 값 매핑
    toplev_2nd = lev_mapping.get(max_num_2nd, None)  # 높은 메탈 값 매핑
    _NumFigPair_2nd = param.get('_NumFigPair_2nd')

    ## 1st Feedback
    # Parallel Res
    _Par_ResWidth = param.get('_Par_ResWidth')
    _Par_ResLength = param.get('_Par_ResLength')
    _Par_SeriesStripes = param.get('_Par_SeriesStripes')
    _Par_ParallelStripes = param.get('_Par_ParallelStripes')

    # Series Res
    _Ser_ResWidth = param.get('_Ser_ResWidth')
    _Ser_ResLength = param.get('_Ser_ResLength')
    _Ser_SeriesStripes = param.get('_Ser_SeriesStripes')
    _Ser_ParallelStripes = param.get('_Ser_ParallelStripes')

    ### TG NMOS PMOS
    _TG_NumberofGate = param.get('_TG_NumberofGate')
    _TG_NMOSChannelWidth = param.get('_TG_NMOSChannelWidth')
    _TG_PMOSChannelWidth = param.get('_TG_PMOSChannelWidth')
    _TG_Channellength = param.get('_TG_Channellength')
    _INV_NumberofGate = param.get('_INV_NumberofGate')

    # Cap_lst
    _Length_1st = param.get('_Length_1st')
    _LayoutOption_1st = param.get('_LayoutOption_1st')
    min_num_1st = min(_LayoutOption_1st)
    max_num_1st = max(_LayoutOption_1st)
    botlev_1st = lev_mapping.get(min_num_1st, None)  # 낮은 메탈 값 매핑
    toplev_1st = lev_mapping.get(max_num_1st, None)  # 높은 메탈 값 매핑
    _NumFigPair_1st = param.get('_NumFigPair_1st')

    _Parallel_Stack = param.get('_Parallel_Stack')





    now_str = datetime.now().strftime("%b %d %H:%M:%S %Y")
    if not os.path.exists(
            rf'C:\Users\KJB\PycharmProjects\LayGenGUI\generatorLib\generator_models\Verify_Rand_beginner_JH\TIA'):
        os.makedirs(
            rf'C:\Users\KJB\PycharmProjects\LayGenGUI\generatorLib\generator_models\Verify_Rand_beginner_JH\TIA')

    with open(
            rf'C:\Users\KJB\PycharmProjects\LayGenGUI\generatorLib\generator_models\Verify_Rand_beginner_JH\TIA\TIA{word}.src.net',
            'w') as f:
        f.write("************************************************************************\n")
        f.write("* auCdl Netlist:\n")
        f.write("* \n")
        f.write(f"* Library Name:  Generator_test2\n")
        f.write(f"* Top Cell Name: A01_TIA_Core_YJH_02\n")
        f.write("* View Name:     schematic\n")
        f.write(f"* Netlisted on:  {now_str}\n")
        f.write("************************************************************************\n\n")

        f.write(".INCLUDE  /tools/PDK/ss28lpp_rf/Device/LNR28LPP_CDS_S00-V1.4.6.1/CDS/oa/cmos28lp/.il/devices.cdl\n")
        # f.write('.INCLUDE /home/PDK/ss28nm/SEC_CDS/ln28lppdk/S00-V1.1.0.1_SEC2.0.6.2/oa/cmos28lp/.resources/devices.cdl\n')
        f.write("*.EQUATION\n")
        f.write("*.SCALE METER\n")
        f.write("*.MEGA\n")
        f.write(".PARAM\n\n\n\n")

        f.write("************************************************************************\n")
        f.write(f"* Library Name: Proj_ADC2024_00_2stageTIA_YJH\n")
        f.write(f"* Cell Name:    A06_INV_Size1_YJH_01_fin2\n")
        f.write("* View Name:    schematic\n")
        f.write("************************************************************************\n\n")

        f.write(f".SUBCKT A06_INV_Size1_YJH_01_fin2 IN OUT VDD VSS\n")
        f.write("*.PININFO IN:B OUT:B VDD:B VSS:B\n")
        f.write(
            f"MN2 OUT IN VSS VSS egnfet w=1u l=0.15u nf={_INV_NumberofGate:.4f} pccrit=0 plorient=1 ngcon=1 p_la=0u ptwell=0\n")
        f.write(
            f"MP0 OUT IN VDD VDD egpfet w=2u l=0.15u nf={_INV_NumberofGate:.4f} pccrit=0 plorient=1 ngcon=1 p_la=0u ptwell=0\n")
        f.write(".ENDS\n\n")


        f.write("************************************************************************\n")
        f.write(f"* Library Name: Generator_test\n")
        f.write(f"* Cell Name:    A06_TG_Ron20ohm_YJH\n")
        f.write("* View Name:    schematic\n")
        f.write("************************************************************************\n\n")

        f.write(f".SUBCKT A06_TG_Ron20ohm_YJH PASS PortA PortB VDD VSS\n")
        f.write("*.PININFO PASS:B PortA:B PortB:B VDD:B VSS:B\n")
        f.write(
            f"MP0 PortA PASSB PortB VDD egpfet w={(_TG_PMOSChannelWidth*_TG_NumberofGate)/1000:.4f}u l={(_TG_Channellength)/1000:.4f}u nf={_TG_NumberofGate:.4f} pccrit=0 plorient=1 ngcon=1 p_la=0u ptwell=0\n")
        f.write(
            f"MN2 PortA PASS PortB VSS egnfet w={(_TG_NMOSChannelWidth*_TG_NumberofGate)/1000:.4f}u l={(_TG_Channellength)/1000:.4f}u nf={_TG_NumberofGate:.4f} pccrit=0 plorient=1 ngcon=1 p_la=0u ptwell=0\n")
        f.write(
            f"XI3<0> PASS PASSB VDD VSS / A06_INV_Size1_YJH_01_fin2\n")
        f.write(".ENDS\n\n")

        f.write("************************************************************************\n")
        f.write(f"* Library Name: Generator_test2\n")
        f.write(f"* Cell Name:    A05_RParallel_RUnit\n")
        f.write("* View Name:    schematic\n")
        f.write("************************************************************************\n\n")

        f.write(f".SUBCKT A05_RParallel_RUnit PASS PortA PortB VDD VSS\n")
        f.write("*.PININFO PASS:B PortA:B PortB:B VDD:B VSS:B\n")
        f.write(
            f"XI2 PASS net4 PortB VDD VSS / A06_TG_Ron20ohm_YJH\n")
        f.write(
            f"RR8 net4 PortA $SUB=VSS $[opppcres] r=0.926k w={(_Par_ResWidth) / 1000:.4f}u l={(_Par_ResLength) / 1000:.4f}u pbar=1 s={_Par_SeriesStripes:.4f} bp=3 ncr=1\n")
        f.write(".ENDS\n\n")

        f.write("************************************************************************\n")
        f.write(f"* Library Name: Generator_test2\n")
        f.write(f"* Cell Name:    A06_TG_Ron20ohm_YJH_schematic\n")
        f.write("* View Name:    schematic\n")
        f.write("************************************************************************\n\n")

        f.write(f".SUBCKT A06_TG_Ron20ohm_YJH_schematic PASS PortA PortB VDD VSS\n")
        f.write("*.PININFO PASS:B PortA:B PortB:B VDD:B VSS:B\n")
        f.write(
            f"MN2 PortA PASS PortB VSS egnfet w={(_TG_NMOSChannelWidth*_TG_NumberofGate) / 1000:.4f}u l={(_TG_Channellength) / 1000:.4f}u nf={_TG_NumberofGate:.4f} pccrit=0 plorient=1 ngcon=1 p_la=0u ptwell=0\n")
        f.write(
            f"MP0 PortA PASSB PortB VDD egpfet w={(_TG_PMOSChannelWidth*_TG_NumberofGate) / 1000:.4f}u l={(_TG_Channellength) / 1000:.4f}u nf={_TG_NumberofGate:.4f} pccrit=0 plorient=1 ngcon=1 p_la=0u ptwell=0\n")
        f.write(
            f"XI3<0> PASS PASSB VDD VSS / A06_INV_Size1_YJH_01_fin2\n")
        f.write(".ENDS\n\n")

        f.write("************************************************************************\n")
        f.write(f"* Library Name: Generator_test2\n")
        f.write(f"* Cell Name:    A03_FBNetwork\n")
        f.write("* View Name:    schematic\n")
        f.write("************************************************************************\n\n")

        gain_pins = [f"Ctrl_TIGainP<{k}>" for k in range(_Parallel_Stack)]
        f.write(f".SUBCKT A03_FBNetwork Ctrl_CFB Ctrl_TIGainA "+" ".join(gain_pins)+" PortA PortB VDD VSS\n")
        # f.write(f".SUBCKT A03_FBNetwork Ctrl_CFB Ctrl_TIGainA Ctrl_TIGainP<0> Ctrl_TIGainP<1> Ctrl_TIGainP<2> Ctrl_TIGainP<3> PortA PortB VDD VSS\n")
        f.write("*.PININFO Ctrl_CFB:B Ctrl_TIGainA:B Ctrl_TIGainP<0>:B Ctrl_TIGainP<1>:B\n")
        f.write("*.PININFO Ctrl_TIGainP<2>:B Ctrl_TIGainP<3>:B PortA:B PortB:B VDD:B VSS:B\n")
        f.write(
            f"CC26 net73 PortA $[hdvncap] $SUB=VSS l={(_Length_1st) / 1000:.4f}u w={(_NumFigPair_1st - 1) * 0.2 + 0.35:.4f}u botlev={botlev_1st} toplev={toplev_1st}\n")
        f.write(
            f"CC31 net73 PortA $[hdvncap] $SUB=VSS l={(_Length_1st) / 1000:.4f}u w={(_NumFigPair_1st - 1) * 0.2 + 0.35:.4f}u botlev={botlev_1st} toplev={toplev_1st}\n")
        f.write(
            f"CC32 PortB PortA $[hdvncap] $SUB=VSS l={(_Length_1st) / 1000:.4f}u w={(_NumFigPair_1st - 1) * 0.2 + 0.35:.4f}u botlev={botlev_1st} toplev={toplev_1st}\n")
        f.write(
            f"CC33 PortB PortA $[hdvncap] $SUB=VSS l={(_Length_1st) / 1000:.4f}u w={(_NumFigPair_1st - 1) * 0.2 + 0.35:.4f}u botlev={botlev_1st} toplev={toplev_1st}\n")
        for i in range(0,_Parallel_Stack):
            f.write(
                f"XI2{i} Ctrl_TIGainP<{i}> PortB rdac VDD VSS / A05_RParallel_RUnit\n")
        # f.write(
        #     f"XI0 Ctrl_TIGainP<3> PortB rdac VDD VSS / A05_RParallel_RUnit\n")
        # f.write(
        #     f"XI21 Ctrl_TIGainP<0> PortB rdac VDD VSS / A05_RParallel_RUnit\n")
        # f.write(
        #     f"XI18 Ctrl_TIGainP<1> PortB rdac VDD VSS / A05_RParallel_RUnit\n")
        # f.write(
        #     f"XI19 Ctrl_TIGainP<2> PortB rdac VDD VSS / A05_RParallel_RUnit\n")
        f.write(
            f"RR17 rdac PortA $SUB=VSS $[opppcres] r=0.926k w={(_Ser_ResWidth) / 1000:.4f}u l={(_Ser_ResLength) / 1000:.4f}u pbar=1 s={_Ser_SeriesStripes:.4f} bp=3 ncr=1\n")
        f.write(
            f"XI17 Ctrl_TIGainA PortA rdac VDD VSS / A06_TG_Ron20ohm_YJH_schematic\n")
        f.write(
            f"XI16 Ctrl_CFB net73 PortB VDD VSS / A06_TG_Ron20ohm_YJH_schematic\n")
        f.write(".ENDS\n\n")

        f.write("************************************************************************\n")
        f.write(f"* Library Name: Generator_test2\n")
        f.write(f"* Cell Name:    A02_TwoStageAmp\n")
        f.write("* View Name:    schematic\n")
        f.write("************************************************************************\n\n")

        f.write(f".SUBCKT A02_TwoStageAmp VBN VBP VDD VINN VINP VOUT VSS\n")
        f.write("*.PININFO VBN:B VBP:B VDD:B VINN:B VINP:B VOUT:B VSS:B\n")
        f.write(
            f"MN33 VOUT VOUT1 VSS VSS egnfet w={(_op1_N4_finger * _op1_N4_width) / 1000:.4f}u l=0.15u nf={_op1_N4_finger:.4f} pccrit=0 plorient=1 ngcon=1 p_la=0u ptwell=0\n")
        f.write(
            f"MN1 VOUT1 net36 VSS VSS egnfet w={(_op1_N1_finger * _op1_N1_width) / 1000:.4f}u l=0.15u nf={_op1_N1_finger:.4f} pccrit=0 plorient=1 ngcon=1 p_la=0u ptwell=0\n")
        f.write(
            f"MN0 net36 net36 VSS VSS egnfet w={(_op1_N0_finger * _op1_N0_width) / 1000:.4f}u l=0.15u nf={_op1_N0_finger:.4f} pccrit=0 plorient=1 ngcon=1 p_la=0u ptwell=0\n")
        f.write(
            f"MN9 VBN VBN VSS VSS egnfet w={(_op1_N2_finger * _op1_N2_width) / 1000:.4f}u l=0.15u nf={_op1_N2_finger:.4f} pccrit=0 plorient=1 ngcon=1 p_la=0u ptwell=0\n")
        f.write(
            f"MN11 VBP VBP VBN VSS egnfet w={(_op1_N3_finger * _op1_N3_width) / 1000:.4f}u l=0.15u nf={_op1_N3_finger:.4f} pccrit=0 plorient=1 ngcon=1 p_la=0u ptwell=0\n")
        f.write(
            f"RR1 net37 VOUT1 $SUB=VSS $[opppcres] r=0.926k w={(_op1_res0_width) / 1000:.4f}u l={(_op1_res0_length) / 1000:.4f}u pbar=1 s=1 bp=3 ncr=1\n")
        f.write(
            f"RR9 net37 VOUT1 $SUB=VSS $[opppcres] r=0.926k w={(_op1_res1_width) / 1000:.4f}u l={(_op1_res1_length) / 1000:.4f}u pbar=1 s=1 bp=3 ncr=1\n")
        f.write(
            f"CC2 VOUT net37 $[hdvncap] $SUB=VSS l={(_op1_cap0_length) / 1000:.4f}u w={(_op1_cap0_finger - 1) * 0.2 + 0.35:.4f}u botlev={_op1_cap0_botlev} toplev={_op1_cap0_toplev}\n")
        f.write(
            f"CC1 VOUT net37 $[hdvncap] $SUB=VSS l={(_op1_cap1_length) / 1000:.4f}u w={(_op1_cap1_finger - 1) * 0.2 + 0.35:.4f}u botlev={_op1_cap1_botlev} toplev={_op1_cap1_toplev}\n")
        f.write(
            f"MP14 VOUT VBP VDD VDD egpfet w={(_op1_P4_finger * _op1_P4_width) / 1000:.4f}u l=0.15u nf={_op1_P4_finger:.4f} pccrit=0 plorient=1 ngcon=1 p_la=0u ptwell=0\n")
        f.write(
            f"MP1 VOUT1 VINP net38 VDD egpfet w={(_op1_P2_finger * _op1_P2_width) / 1000:.4f}u l=0.15u nf={_op1_P2_finger:.4f} pccrit=0 plorient=1 ngcon=1 p_la=0u ptwell=0\n")
        f.write(
            f"MP0 net36 VINN net38 VDD egpfet w={(_op1_P1_finger * _op1_P1_width) / 1000:.4f}u l=0.15u nf={_op1_P1_finger:.4f} pccrit=0 plorient=1 ngcon=1 p_la=0u ptwell=0\n")
        f.write(
            f"MP7 VBP VBP VDD VDD egpfet w={(_op1_P3_finger * _op1_P3_width) / 1000:.4f}u l=0.15u nf={_op1_P3_finger:.4f} pccrit=0 plorient=1 ngcon=1 p_la=0u ptwell=0\n")
        f.write(
            f"MP2 net38 VBP VDD VDD egpfet w={(_op1_P0_finger * _op1_P0_width) / 1000:.4f}u l=0.15u nf={_op1_P0_finger:.4f} pccrit=0 plorient=1 ngcon=1 p_la=0u ptwell=0\n")
        f.write(".ENDS\n\n")

        f.write("************************************************************************\n")
        f.write(f"* Library Name: Generator_test2\n")
        f.write(f"* Cell Name:    TIA\n")
        f.write("* View Name:    schematic\n")
        f.write("************************************************************************\n\n")
        gain_pins_reverse = [f"Ctrl_TIGainP<{k}>" for k in range(_Parallel_Stack-1,-1,-1)]
        f.write(f".SUBCKT TIA Ctrl_CFB Ctrl_TIGainA "+" ".join(gain_pins)+" IIN VDD VOCM VOUT VREF_TIA VSS\n")
        # f.write(f".SUBCKT TIA Ctrl_CFB Ctrl_TIGainA Ctrl_TIGainP<3> Ctrl_TIGainP<2> Ctrl_TIGainP<1> Ctrl_TIGainP<0> IIN VDD VOCM VOUT VREF_TIA VSS\n")
        f.write("*.PININFO Ctrl_CFB:B Ctrl_TIGainA:B Ctrl_TIGainP<3>:B Ctrl_TIGainP<2>:B\n")
        f.write("*.PININFO Ctrl_TIGainP<1>:B Ctrl_TIGainP<0>:B IIN:B VDD:B VOCM:B VOUT:B\n")
        f.write("*.PININFO VREF_TIA:B VSS:B\n")
        f.write(
            f"RR13 VOUT net28 $SUB=VSS $[opppcres] r=0.926k w={(_ResWidth_2nd) / 1000:.4f}u l={(_ResLength_2nd) / 1000:.4f}u pbar={_ParallelStripes_2nd:.4f} s={_SeriesStripes_2nd:.4f} bp=3 ncr=1\n")
        f.write(
            f"RR0 net28 TIStageOutput $SUB=VSS $[opppcres] r=0.926k w={(_ResWidth_resA) / 1000:.4f}u l={(_ResLength_resA) / 1000:.4f}u pbar={_ParallelStripes_resA:.4f} s={_SeriesStripes_resA:.4f} bp=3 ncr=1\n")

        f.write(
            f"XI66 Ctrl_CFB Ctrl_TIGainA "+" ".join(gain_pins)+" IIN TIStageOutput VDD VSS / A03_FBNetwork\n")
        # f.write(
            # f"XI66 Ctrl_CFB Ctrl_TIGainA Ctrl_TIGainP<0> Ctrl_TIGainP<1> Ctrl_TIGainP<2> Ctrl_TIGainP<3> IIN TIStageOutput VDD VSS / A03_FBNetwork\n")
        f.write(
            f"CC32 VOUT net28 $[hdvncap] $SUB=VSS l={(_Length_2nd) / 1000:.4f}u w={(_NumFigPair_2nd - 1) * 0.2 + 0.35:.4f}u botlev={botlev_2nd} toplev={toplev_2nd}\n")
        f.write(
            f"CC31 VOUT net28 $[hdvncap] $SUB=VSS l={(_Length_2nd) / 1000:.4f}u w={(_NumFigPair_2nd - 1) * 0.2 + 0.35:.4f}u botlev={botlev_2nd} toplev={toplev_2nd}\n")
        f.write(
            f"CC30 VOUT net28 $[hdvncap] $SUB=VSS l={(_Length_2nd) / 1000:.4f}u w={(_NumFigPair_2nd - 1) * 0.2 + 0.35:.4f}u botlev={botlev_2nd} toplev={toplev_2nd}\n")
        f.write(
            f"CC29 VOUT net28 $[hdvncap] $SUB=VSS l={(_Length_2nd) / 1000:.4f}u w={(_NumFigPair_2nd - 1) * 0.2 + 0.35:.4f}u botlev={botlev_2nd} toplev={toplev_2nd}\n")
        f.write(
            f"CC28 VOUT net28 $[hdvncap] $SUB=VSS l={(_Length_2nd) / 1000:.4f}u w={(_NumFigPair_2nd - 1) * 0.2 + 0.35:.4f}u botlev={botlev_2nd} toplev={toplev_2nd}\n")
        f.write(
            f"CC20 VOUT net28 $[hdvncap] $SUB=VSS l={(_Length_2nd) / 1000:.4f}u w={(_NumFigPair_2nd - 1) * 0.2 + 0.35:.4f}u botlev={botlev_2nd} toplev={toplev_2nd}\n")
        f.write(
            f"XI77 net26 net11 VDD net28 VOCM VOUT VSS / A02_TwoStageAmp\n")
        f.write(
            f"XI12 net6 net1 VDD VREF_TIA IIN TIStageOutput VSS / A02_TwoStageAmp\n")
        f.write(".ENDS")
    return None




# def makeBGRSche(word, param):
#     pnp_stack = param.get('pnp_stack')
#     finger_N1 = param.get('finger_N1')
#     finger_N2 = param.get('finger_N2')
#     finger_P1 = param.get('finger_P1')
#     finger_P5 = param.get('finger_P5')
#     finger_N5 = param.get('finger_N5')
#     finger_N4 = param.get('finger_N4')
#     finger_P3 = param.get('finger_P3')
#     finger_P4 = param.get('finger_P4')
#     finger_P6 = param.get('finger_P6')
#     finger_P7 = param.get('finger_P7')
#     finger_P8 = param.get('finger_P8')
#     finger_P9 = param.get('finger_P9')
#     finger_P10 = param.get('finger_P10')
#     finger_N6 = param.get('finger_N6')
#     finger_N7 = param.get('finger_N7')
#     pnp_mid_num = param.get('pnp_mid_num')
#     W_N1 = param.get('W_N1')
#     W_N3 = param.get('W_N3')
#     L1 =param.get('L1')
#     L2 = param.get('L2')
#     L3 = param.get('L3')
#     Dummy = True
#     XVT = 'RVT'
#     W_P1 = param.get('W_P1')
#     W_P2 = param.get('W_P2')
#     W_P3 = param.get('W_P3')
#
#     Guad_via = 2
#     W_res1 = param.get('W_res1')
#     W_res2 = param.get('W_res2')
#     W_res3 = param.get('W_res3')
#     L_res1 = param.get('L_res1')
#     L_res2 = param.get('L_res2')
#     L_Res3 = param.get('L_Res3')
#     series_res1 = param.get('series_res1')
#     Gate_cap = param.get('Gate_cap')
#     RX_cap = param.get('RX_cap')
#     series_res2 = param.get('series_res2')
#     series_res3 = param.get('series_res3')
#     W_pnp = 2000
#     L_cap = param.get('L_cap')
#     W_cap = param.get('W_cap')
#
#     B00_amp_v2 = B00_amp_v4_using_gui.B00_amp_v2(_DesignParameter=None, _Name='opamp')
#     B00_amp_v2_param = B00_amp_v2._CalculateDesignParameter(finger_N1=finger_N1, finger_N2=finger_N2, finger_P1=finger_P1,  finger_P5=finger_P5, finger_N5=finger_N5, finger_N4=finger_N4, finger_P3=finger_P3,finger_P4=finger_P4,W_N=W_N1,L=L1,Dummy=Dummy,XVT=XVT,W_P=W_P1,Guad_via=Guad_via,res_compensation_W=W_res1,res_compensation_L=L_res1,res_compensation_series=series_res1,NumofGate_res_com=Gate_cap,NumofRX_res_com=RX_cap,L_cap=L_cap,W_cap=W_cap )
#     finger_N_Dummy1,finger_N_Dummy2,finger_P_Dummy1,finger_P_Dummy2  = B00_amp_v2_param
#
#     W_N1 = float(W_N1) / 1000  # 단위 변환: nm → um
#     L1 = float(L1) / 1000
#     L2 = float(L2) / 1000
#     L3 = float(L3) / 1000
#     W_P1 = float(W_P1) / 1000
#     W_P2 = float(W_P2) / 1000
#     W_P3 = float(W_P3) / 1000
#     W_N3 = float(W_N3) / 1000
#     L_cap = float(L_cap) / 1000
#     W_cap = float(W_cap) / 1000
#     W_res1 = float(W_res1) / 1000
#     W_res2 = float(W_res2) / 1000
#     W_res3 = float(W_res3) / 1000
#     L_res1 = float(L_res1) / 1000
#     L_res2 = float(L_res2) / 1000
#     L_res3 = float(L_Res3) / 1000
#     W_pnp = float(W_pnp) / 1000
#
#
#
#     # if (finger_P_Dummy2 + finger_P1) % 2 == 1 and finger_P3 % 2 == 1:
#     #     finger_P3 +=1
#     #
#     # if (finger_P_Dummy2 + finger_P1) % 2 == 0 and finger_P3 % 2 == 0:
#     #     finger_P3 +=1
#
#     now_str = datetime.now().strftime("%b %d %H:%M:%S %Y")
#     if not os.path.exists('./Verify_Rand_beginner_JH/BGR'):
#         os.makedirs('./Verify_Rand_beginner_JH/BGR')
#     if L1 == 30/1000:
#         pccrit1 =1
#     else:
#         pccrit1 = 0
#     if L2 == 30/1000:
#         pccrit2 =1
#     else:
#         pccrit2 = 0
#     if L3 == 30/1000:
#         pccrit3 =1
#     else:
#         pccrit3 = 0
#     with open(f'./Verify_Rand_beginner_JH/BGR/BGR{word}.src.net', 'w') as f:
#         f.write("************************************************************************\n")
#         f.write("* auCdl Netlist:\n")
#         f.write("* \n")
#         f.write("* Library Name:  Laygen_AMP\n")
#         f.write(f"* Top Cell Name: BGR\n")
#         f.write("* View Name:     schematic\n")
#         f.write(f"* Netlisted on:  {now_str}\n")
#         f.write("************************************************************************\n\n")
#
#         # f.write(".INCLUDE  /tools/PDK/ss28lpp_rf/Device/LNR28LPP_CDS_S00-V1.4.6.1/CDS/oa/cmos28lp/.il/devices.cdl\n")
#         f.write('.INCLUDE /home/PDK/ss28nm/SEC_CDS/ln28lppdk/S00-V1.1.0.1_SEC2.0.6.2/oa/cmos28lp/.resources/devices.cdl\n')
#         f.write("*.EQUATION\n")
#         f.write("*.SCALE METER\n")
#         f.write("*.MEGA\n")
#         f.write(".PARAM\n\n\n")
#
#         f.write("************************************************************************\n")
#         f.write("* Library Name: Laygen_AMP\n")
#         f.write(f"* Cell Name:    opamp\n")
#         f.write("* View Name:    schematic\n")
#         f.write("************************************************************************\n\n")

    #     f.write(f".SUBCKT opamp VDD VINn VINp VOUT VSS\n")
    #     f.write("*.PININFO VDD:B VINn:B VINp:B VOUT:B VSS:B\n")
    #     f.write(f"MN1 net6 net1 VSS VSS nfet w={finger_N1*W_N1:.4f}u l={L1:.4f}u nf={finger_N1:.4f} pccrit={pccrit1} plorient=1 ngcon=1 p_la=0u ptwell=0\n")
    #     f.write(f"MN5 VOUT net1 VSS VSS nfet w={finger_N5*W_N1:.4f}u l={L1:.4f}u nf={finger_N5:.4f} pccrit={pccrit1} plorient=1 ngcon=1 p_la=0u ptwell=0\n")
    #     f.write(f"MN3 net2 VINp net6 VSS nfet w={finger_N2*W_N1:.4f}u l={L1:.4f}u nf={finger_N2:.4f} pccrit={pccrit1} plorient=1 ngcon=1 p_la=0u ptwell=0\n")
    #     f.write(f"MN2 net5 VINn net6 VSS nfet w={finger_N2*W_N1:.4f}u l={L1:.4f}u nf={finger_N2:.4f} pccrit={pccrit1} plorient=1 ngcon=1 p_la=0u ptwell=0\n")
    #     f.write(f"MN_Dummy VSS VSS VSS VSS nfet w={(finger_N_Dummy1+finger_N_Dummy2)*W_N1:.4f}u l={L1:.4f}u nf={(finger_N_Dummy1+finger_N_Dummy2):.4f} pccrit={pccrit1} plorient=1 ngcon=1 p_la=0u ptwell=0\n")
    #     f.write(f"MN4 net1 net1 VSS VSS nfet w={finger_N4*W_N1:.4f}u l={L1:.4f}u nf={finger_N4:.4f} pccrit={pccrit1} plorient=1 ngcon=1 p_la=0u ptwell=0\n")
    #     f.write(f"MP1 net5 net5 VDD VDD pfet w={finger_P1*W_P1:.4f}u l={L1:.4f}u nf={finger_P1:.4f} pccrit={pccrit1} plorient=1 ngcon=1 p_la=0u ptwell=0\n")
    #     f.write(f"MP4 net1 net1 net3 VDD pfet w={finger_P4*W_P1:.4f}u l={L1:.4f}u nf={finger_P4:.4f} pccrit={pccrit1} plorient=1 ngcon=1 p_la=0u ptwell=0\n")
    #     f.write(f"MP2 net2 net5 VDD VDD pfet w={finger_P1*W_P1:.4f}u l={L1:.4f}u nf={finger_P1:.4f} pccrit={pccrit1} plorient=1 ngcon=1 p_la=0u ptwell=0\n")
    #     f.write(f"MP_Dummy VDD VDD VDD VDD pfet w={(finger_N1+finger_P_Dummy1+finger_P_Dummy2)*W_P1:.4f}u l={L1:.4f}u nf={(finger_N1+finger_P_Dummy1+finger_P_Dummy2):.4f} pccrit={pccrit1} plorient=1 ngcon=1 p_la=0u ptwell=0\n")
    #     f.write(f"MP3 net3 net3 VDD VDD pfet w={finger_P3*W_P1:.4f}u l={L1:.4f}u nf={finger_P3:.4f} pccrit={pccrit1} plorient=1 ngcon=1 p_la=0u ptwell=0\n")
    #     f.write(f"MP5 VOUT net2 VDD VDD pfet w={finger_P5*W_P1:.4f}u l={L1:.4f}u nf={finger_P5:.4f} pccrit={pccrit1} plorient=1 ngcon=1 p_la=0u ptwell=0\n")
    #     f.write(f"CC2 net2 net4 $[ncap] $SUB=VSS l={L_cap:.4f}u w={W_cap:.4f}u nf={Gate_cap:.4f} nrep={RX_cap:.4f}\n")
    #     f.write(f"RR1 VOUT net4 $SUB=VSS $[opppcres] r=3.039k w={W_res1:.4f}u l={L_res1:.4f}u pbar=1 s={series_res1:.4f} bp=3 ncr=1\n")
    #     f.write(".ENDS\n")
    #
    #     f.write("************************************************************************\n")
    #     f.write("* Library Name: Laygen_BGR\n")
    #     f.write(f"* Cell Name:    BGR\n")
    #     f.write("* View Name:    schematic\n")
    #     f.write("************************************************************************\n\n")
    #
    #     f.write(".SUBCKT BGR VDD VSS Vref\n")
    #     f.write("*.PININFO VDD:B VSS:B Vref:B\n")
    #     f.write('XI40 VDD net1 net5 OUT VSS / opamp\n')
    #     f.write(f'QQP0 VSS VSS net1 vpnp nf=1 nrep=1 w={W_pnp:.4f}u l={W_pnp:.4f}u\n')
    #     f.write(f'QQP2 VSS VSS net2 vpnp nf=1 nrep=1 w={W_pnp:.4f}u l={W_pnp:.4f}u\n')
    #     if pnp_stack==0:
    #         f.write(f'QQP1<0> VSS VSS net6 vpnp nf=1 nrep=1 w={W_pnp:.4f}u l={W_pnp:.4f}u\n')
    #         f.write(f'QQP1<1> VSS VSS net6 vpnp nf=1 nrep=1 w={W_pnp:.4f}u l={W_pnp:.4f}u\n')
    #         f.write(f'QQP1<2> VSS VSS net6 vpnp nf=1 nrep=1 w={W_pnp:.4f}u l={W_pnp:.4f}u\n')
    #         f.write(f'QQP1<3> VSS VSS net6 vpnp nf=1 nrep=1 w={W_pnp:.4f}u l={W_pnp:.4f}u\n')
    #         f.write(f'QQP1<4> VSS VSS net6 vpnp nf=1 nrep=1 w={W_pnp:.4f}u l={W_pnp:.4f}u\n')
    #         f.write(f'QQP1<5> VSS VSS net6 vpnp nf=1 nrep=1 w={W_pnp:.4f}u l={W_pnp:.4f}u\n')
    #         f.write(f'QQP1<6> VSS VSS net6 vpnp nf=1 nrep=1 w={W_pnp:.4f}u l={W_pnp:.4f}u\n')
    #     if pnp_stack == 1:
    #         for i in range(0,pnp_mid_num):
    #             f.write(f'QQP1<{i}> VSS VSS net6 vpnp nf=1 nrep=1 w={W_pnp:.4f}u l={W_pnp:.4f}u\n')
    #         if pnp_mid_num %2 == 1:
    #             f.write(f"QQP3 VSS VSS VSS vpnp nf=1 nrep=1 w={W_pnp:.4f}u l={W_pnp:.4f}u\n") #수정 필요+파라미터 업데이트
    #     f.write(f'MP8 Vref OUT VDD VDD pfet w={W_P2*finger_P8:.4f}u l={L2:.4f}u nf={finger_P8:.4f} pccrit={pccrit2} plorient=1 ngcon=1 p_la=0u ptwell=0\n')
    #     f.write(f'MP7 net5 OUT VDD VDD pfet w={W_P2*finger_P7:.4f}u l={L2:.4f}u nf={finger_P7:.4f} pccrit={pccrit2} plorient=1 ngcon=1 p_la=0u ptwell=0\n')
    #     f.write(f'MP6 net1 OUT VDD VDD pfet w={W_P2*finger_P6:.4f}u l={L2:.4f}u nf={finger_P6:.4f} pccrit={pccrit2} plorient=1 ngcon=1 p_la=0u ptwell=0\n')
    #     f.write(f'MP9 net4 net4 net3 VDD pfet w={W_P3*finger_P9:.4f}u l={L3:.4f}u nf={finger_P9:.4f} pccrit={pccrit3} plorient=1 ngcon=1 p_la=0u ptwell=0\n')
    #     f.write(f'MP10 net3 net3 VDD VDD pfet w={W_P3*finger_P10:.4f}u l={L3:.4f}u nf={finger_P10:.4f} pccrit={pccrit3} plorient=1 ngcon=1 p_la=0u ptwell=0\n')
    #     f.write(f'RR3 net5 net6 $SUB=VSS $[opppcres] r=10.052k w={W_res3:.4f}u l={L_res3:.4f}u pbar=1 s={series_res3:.4f} bp=3 ncr=1\n')
    #     f.write(f'RR2 Vref net2 $SUB=VSS $[opppcres] r=88.819k w={W_res2:.4f}u l={L_res2:.4f}u pbar=1 s={series_res2:.4f} bp=3 ncr=1\n')
    #     f.write(f'MN6 OUT net4 VSS VSS nfet w={W_N3*finger_N6:.4f}u l={L3:.4f}u nf={finger_N6:.4f} pccrit={pccrit3} plorient=1 ngcon=1 p_la=0u ptwell=0\n')
    #     f.write(f'MN7 net4 Vref VSS VSS nfet w={W_N3*finger_N7:.4f}u l={L3:.4f}u nf={finger_N7:.4f} pccrit={pccrit3} plorient=1 ngcon=1 p_la=0u ptwell=0\n')
    #     f.write(".ENDS\n")
    # return None