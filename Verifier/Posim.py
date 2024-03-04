import paramiko
import ftplib
import os
import sys
import time
import DesignParameters

'''
    You should create schematic for post-layout simulation, and have a netlist on your server to run automatic posim.
'''

class POSIM :
    def __init__(self, username, password, WorkDir, OceanDir, OceanScript, SimDir, modelDir, Corner, PEXnetlist, resultfile) :
        self.server = '141.223.29.62'
        self.port = 22
        self.username = username
        self.password = password
        self.WorkDir = WorkDir
        self.OceanDir = OceanDir
        self.OceanScript = OceanScript
        self.SimDir = SimDir
        self.modelDir = modelDir
        self.Corner = Corner
        self.PEXnetlist = PEXnetlist
        self.resultfile = resultfile

    def Posimchecker(self) :
        print('   Connecting to Server by SSH...   '.center(105, '#'))
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(self.server, port=self.port, username=self.username, password=self.password)

        ##### Step 1 : Stream In/Out GDS file
        if DesignParameters._Technology == '028nm' :

            # commandlines0 = "cd {0}; sed -i '2s,.*,design(  \"{2}/netlist/netlist\"),' {1}; sed -i '3s,.*,resultsDir( \"{2}\" ),' {1}; sed -i '4s,.*,path(  \"{6}\"),' {1}; sed -i '9s,.*,    \"{5}\",' {1};" # ocean file modification
            commandlines0 = "cd {0}; sed -i '3s,.*,resultsDir( \"{2}\" ),' {1}; sed -i '4s,.*,path(  \"{6}\"),' {1}; sed -i '9s,.*,    \"{5}\",' {1};" # ocean file modification
            stdin, stdout, stderr = ssh.exec_command(commandlines0.format(self.OceanDir, self.OceanScript, self.SimDir, self.modelDir, self.Corner, self.PEXnetlist, self.WorkDir))
            print(f'print after commandlines0 :')
            print(f"stdout: {stdout.read().decode('utf-8')}")
            print(f"stderr: {stderr.read().decode('utf-8')}")

            # commandlines01 = "cd {0}; sed -i \"6s,.*,    \'(@{3}@ @{4}@),\" {1};"
            # print (commandlines01.format(self.OceanDir, self.OceanScript, self.SimDir, self.modelDir, self.Corner, self.PEXnetlist, self.WorkDir))
            # stdin, stdout, stderr = ssh.exec_command(commandlines01.format(self.OceanDir, self.OceanScript, self.SimDir, self.modelDir, self.Corner, self.PEXnetlist, self.WorkDir))
            # print(f'print after commandlines01 :')
            # print(f"stdout: {stdout.read().decode('utf-8')}")
            # print(f"stderr: {stderr.read().decode('utf-8')}")

            commandlines02 = "cd {0}; sed -i \'s/@/\"/g\' {1};"
            print (commandlines02.format(self.OceanDir, self.OceanScript, self.SimDir, self.modelDir, self.Corner, self.PEXnetlist, self.WorkDir))
            stdin, stdout, stderr = ssh.exec_command(commandlines02.format(self.OceanDir, self.OceanScript, self.SimDir, self.modelDir, self.Corner, self.PEXnetlist, self.WorkDir))
            print(f'print after commandlines02 :')
            print(f"stdout: {stdout.read().decode('utf-8')}")
            print(f"stderr: {stderr.read().decode('utf-8')}")


            commandlines1 = "cd {0}; source setup.cshrc; cd {1}; ocean -nograph -restore {2}" # ocean script execution
            stdin, stdout, stderr = ssh.exec_command(commandlines1.format(self.WorkDir, self.OceanDir, self.OceanScript))
            result2 = stdout.read().decode('utf-8')

            commandlines2 = "cd {0}; cat {1};"
            stdin, stdout, stderr = ssh.exec_command(commandlines2.format(self.OceanDir, self.resultfile))
            print(f"stdout: {stdout.read().decode('utf-8')}")
            print(f"stderr: {stderr.read().decode('utf-8')}")


if __name__ == '__main__' :

    ### Testing resistor bank ###
    import matplotlib.pyplot as plt
    import ftplib
    import numpy as np

    _HomeDirectory = os.getcwd()

    # bank_num = 32
    # for tst in range (1,bank_num + 1) : ## tst equals to turn-on resistor banks
    #     net_lst = ['V7 (VCM 0) vsource dc=VCM type=d\n', 
    #             'V6 (VDD 0) vsource dc=1.1 type=dc\n',
    #             'V8 (VRX 0) vsource dc=Vterm type=dc\n',
    #             'V4 (VSS 0) vsource dc=0 type=dc\n']
    #     for on in range (0, tst) : ## on means turned-on banks
    #         net_lst.append('V0\<{0}\> (S\<{0}\> 0) vsource dc=1.1 type=dc\n'.format(on))
    #         net_lst.append('V2\<{0}\> (SB\<{0}\> 0) vsource dc=0 type=dc\n'.format(on))
    #     for off in range (tst, bank_num) :
    #         net_lst.append('V1\<{0}\> (S\<{0}\> 0) vsource dc=0 type=dc\n'.format(off))
    #         net_lst.append('V3\<{0}\> (SB\<{0}\> 0) vsource dc=1.1 type=dc\n'.format(off))

    #     net_str = ''.join(net_lst)
    #     with open(_HomeDirectory + "/Netlist/netlist", 'w') as sch :
    #         sch.write(net_str)
    #     sch.close()
    #     ftp = ftplib.FTP('141.223.29.62')
    #     ftp.login('junung', 'chlwnsdnd1!')
    #     ftp.cwd('/mnt/sdc/junung/simulation/FullResistorBank_posim/spectre/schematic/netlist/')
    #     myfile = open('./Netlist/netlist', 'rb')
    #     ftp.storbinary('STOR netlist', myfile)
    #     myfile.close()
    #     ftp.close()

    #     POSIM('junung','chlwnsdnd1!','/mnt/sdc/junung/OPUS/Samsung28n', '/mnt/sdc/junung/OPUS/Samsung28n/Ocean_script','Res_Ocean.ocn','/mnt/sdc/junung/simulation/FullResistorBank_posim/spectre/schematic','/mnt/sdc/junung/OPUS/Samsung28n/lib_spectre/LN28LPP_Spectre.lib', 'ss', '/mnt/sdc/junung/PEX_run/Samsung28n/Generated_pex/RX_core.pex.netlist', 'Resresult.txt').Posimchecker()

    # ftp = ftplib.FTP('141.223.29.62')
    # ftp.login('junung', 'chlwnsdnd1!')
    # ftp.cwd('/mnt/sdc/junung/OPUS/Samsung28n/Ocean_script/')
    # fd = open('./Netlist/Resresult.txt', 'wb')
    # ftp.retrbinary('RETR Resresult.txt', fd.write)
    # fd.close()
    # ftp.close()

    # # resistance1 = []
    # # with open(_HomeDirectory + "/Netlist/Resresult.txt", 'r') as res :
    # #     result = res.readlines()
    # #     for line in result :
    # #         line = line.split(' ')
    # #         print (line)
    # #         resistance1.append(float(line[-2]))
    # # print (resistance1)

    # bank_num = 32
    # for tst in range (1,bank_num + 1) : ## tst equals to turn-on resistor banks
    #     net_lst = ['V7 (VCM 0) vsource dc=VCM type=d\n', 
    #             'V6 (VDD 0) vsource dc=1.1 type=dc\n',
    #             'V8 (VRX 0) vsource dc=Vterm type=dc\n',
    #             'V4 (VSS 0) vsource dc=0 type=dc\n']
    #     for on in range (0, tst) : ## on means turned-on banks
    #         net_lst.append('V0\<{0}\> (S\<{0}\> 0) vsource dc=1.1 type=dc\n'.format(on))
    #         net_lst.append('V2\<{0}\> (SB\<{0}\> 0) vsource dc=0 type=dc\n'.format(on))
    #     for off in range (tst, bank_num) :
    #         net_lst.append('V1\<{0}\> (S\<{0}\> 0) vsource dc=0 type=dc\n'.format(off))
    #         net_lst.append('V3\<{0}\> (SB\<{0}\> 0) vsource dc=1.1 type=dc\n'.format(off))

    #     net_str = ''.join(net_lst)
    #     with open(_HomeDirectory + "/Netlist/netlist", 'w') as sch :
    #         sch.write(net_str)
    #     sch.close()
    #     ftp = ftplib.FTP('141.223.29.62')
    #     ftp.login('junung', 'chlwnsdnd1!')
    #     ftp.cwd('/mnt/sdc/junung/simulation/FullResistorBank_posim/spectre/schematic/netlist/')
    #     myfile = open('./Netlist/netlist', 'rb')
    #     ftp.storbinary('STOR netlist', myfile)
    #     myfile.close()
    #     ftp.close()

    #     POSIM('junung','chlwnsdnd1!','/mnt/sdc/junung/OPUS/Samsung28n', '/mnt/sdc/junung/OPUS/Samsung28n/Ocean_script','Res_Ocean.ocn','/mnt/sdc/junung/simulation/FullResistorBank_posim/spectre/schematic','/mnt/sdc/junung/OPUS/Samsung28n/lib_spectre/LN28LPP_Spectre.lib', 'nn', '/mnt/sdc/junung/PEX_run/Samsung28n/Manual_pex/RX_core_quad.pex.netlist', 'Resresult.txt').Posimchecker()

    # ftp = ftplib.FTP('141.223.29.62')
    # ftp.login('junung', 'chlwnsdnd1!')
    # ftp.cwd('/mnt/sdc/junung/OPUS/Samsung28n/Ocean_script/')
    # fd = open('./Netlist/Resresult.txt', 'wb')
    # ftp.retrbinary('RETR Resresult.txt', fd.write)
    # fd.close()
    # ftp.close()

    # resistance2 = []
    # with open(_HomeDirectory + "/Netlist/Resresult.txt", 'r') as res :
    #     result = res.readlines()
    #     for line in result :
    #         line = line.split(' ')
    #         print (line)
    #         resistance2.append(float(line[-2]))
    # print (resistance2)

    resistance1 = []
    with open(_HomeDirectory + "/Netlist/Resresult.txt", 'r') as res :
        result = res.readlines()
        for line in result[0:32] :
            line = line.split(' ')
            # print (line)
            resistance1.append(float(line[-2]))
    print (resistance1)

    resistance2 = []
    with open(_HomeDirectory + "/Netlist/Resresult.txt", 'r') as res :
        result = res.readlines()
        for line in result[32:64] :
            line = line.split(' ')
            # print (line)
            resistance2.append(float(line[-2]))
    print (resistance2)

    resistance3 = []
    with open(_HomeDirectory + "/Netlist/Resresult.txt", 'r') as res :
        result = res.readlines()
        for line in result[64:96] :
            line = line.split(' ')
            # print (line)
            resistance3.append(float(line[-2]))
    print (resistance3)

    resistance4 = []
    with open(_HomeDirectory + "/Netlist/Resresult.txt", 'r') as res :
        result = res.readlines()
        for line in result[96:128] :
            line = line.split(' ')
            # print (line)
            resistance4.append(float(line[-2]))
    print (resistance4)

    resistance5 = []
    with open(_HomeDirectory + "/Netlist/Resresult.txt", 'r') as res :
        result = res.readlines()
        for line in result[128:160] :
            line = line.split(' ')
            # print (line)
            resistance5.append(float(line[-2]))
    print (resistance5)

    real_res = [900.90, 455.93, 312.82, 240.29, 196.53, 166.90, 146.02, 130.07, 117.55, 107.60,
                99.54, 92.92, 87.21, 82.38, 78.22, 74.56, 71.26, 68.34, 65.72, 63.39,
                61.9, 59.82, 57.55, 55.96, 54.44, 53.05, 51.78, 50.55, 49.72, 48.73,
                47.71, 46.83]

    plt.figure(1)
    plt.rcParams["figure.autolayout"] = True
    plt.rcParams.update({'font.size' : 25, 'font.weight' : 'bold', 'axes.titlesize' : 30, 'axes.titleweight' : 'bold'})
    resistance1 = np.array(resistance1)
    pt1 = plt.plot(resistance1,'bo', label = 'Generated Resistor Bank (ss, 0.9VDD)', ms = 10)
    plt.xticks(np.arange(len(resistance1)), np.arange(1, len(resistance1) + 1))
    for i in range (len(resistance1)) :
        height = resistance1[i]
        plt.text(i , height + 5.25, '%.1f' %height, ha = 'center', va = 'bottom', size = 12, color = 'blue')
    # plt.title("Resistance per turned-on Resistor Bank")
    # plt.legend()
    # plt.xlabel('Number of Turned-On Resistor Bank')
    # plt.ylabel('Resistance (Ohm)')
    # plt.figure(2)
    resistance2 = np.array(resistance2)
    plt.plot(resistance2,'ro', label = 'Manually Made Resistor Bank (ss, 0.9VDD)', marker = 'x', ms = 10, mew = 3)
    plt.xticks(np.arange(len(resistance2)), np.arange(1, len(resistance2) + 1))
    for i in range (len(resistance2)) :
        height = resistance2[i]
        plt.text(i, height + 20.25, '%.1f' %height, ha = 'center', va = 'bottom', size = 12, color = 'red')
    resistance3 = np.array(resistance3) 
    pt1 = plt.plot(resistance3,'ro', label = 'Generated Resistor Bank (ff, 1.1VDD)', ms = 10, color = 'green')
    plt.xticks(np.arange(len(resistance3)), np.arange(1, len(resistance3) + 1)) 
    for i in range (len(resistance3)) :
        height = resistance3[i]
        plt.text(i , height - 25.25, '%.1f' %height, ha = 'center', va = 'bottom', size = 12, color = 'green')
    resistance4 = np.array(resistance4)
    plt.plot(resistance4,'ro', label = 'Manually Made Resistor Bank (ff, 1.1VDD)', marker = 'x', ms = 10, mew = 3, color = 'brown')
    plt.xticks(np.arange(len(resistance4)), np.arange(1, len(resistance4) + 1))
    for i in range (len(resistance4)) :
        height = resistance4[i]
        plt.text(i, height - 40.25, '%.1f' %height, ha = 'center', va = 'bottom', size = 12, color = 'brown')
    plt.title("Resistance per turned-on Resistor Bank (Post-Layout Simulation)")
    plt.legend(frameon = False)
    plt.xlabel('Number of Turned-On Resistor Bank', fontdict={'weight': 'bold', 'size': 30})
    plt.ylabel('Resistance (Ohm)', fontdict={'weight': 'bold', 'size': 30})
    plt.yticks(np.arange(0, 900, 50))
    plt.grid(True)
    plt.figure(2)
    plt.rcParams["figure.autolayout"] = True
    plt.rcParams.update({'font.size' : 25, 'font.weight' : 'bold', 'axes.titlesize' : 30, 'axes.titleweight' : 'bold'})
    resistance5 = np.array(resistance5)
    resistance5 = resistance5 + 18
    pt1 = plt.plot(resistance5,'bo', label = 'Generated Resistor Bank (nn, 1.1VDD) + On Chip Metal Path Resistance (18Ohm)')
    plt.xticks(np.arange(len(resistance5)), np.arange(1, len(resistance1) + 1))
    # for i in range (0,1) :
    #     height = resistance1[i]
    #     plt.text(i , height - 20.25, '%.1f' %height, ha = 'center', va = 'bottom', size = 12, color = 'blue')
    # for i in range (1,4) :
    #     height = resistance1[i]
    #     plt.text(i , height + 5.25, '%.1f' %height, ha = 'center', va = 'bottom', size = 12, color = 'blue')
    for i in range (len(resistance5)) :
        height = resistance5[i]
        plt.text(i , height - 20.25, '%.1f' %height, ha = 'center', va = 'bottom', size = 12, color = 'blue')
    real_res = np.array(real_res)
    plt.plot(real_res,'go', label = 'On-Chip Measurement')
    plt.xticks(np.arange(len(real_res)), np.arange(1, len(real_res) + 1))
    # for i in range (0,1) :
    #     height = real_res[i]
    #     plt.text(i, height + 5.25, '%.1f' %height, ha = 'center', va = 'bottom', size = 12, color = 'green')
    # for i in range (1,4) :
    #     height = real_res[i]
    #     plt.text(i , height - 20.25, '%.1f' %height, ha = 'center', va = 'bottom', size = 12, color = 'green')
    for i in range (len(real_res)) :
        height = real_res[i]
        plt.text(i, height + 5.25, '%.1f' %height, ha = 'center', va = 'bottom', size = 12, color = 'green')
    plt.title("Resistance per turned-on Resistor Bank (Post-Layout Simulation vs. Measurement)")
    plt.legend(frameon = False)
    plt.xlabel('Number of Turned-On Resistor Bank', fontdict={'weight': 'bold', 'size': 30})
    plt.ylabel('Resistance (Ohm)', fontdict={'weight': 'bold', 'size': 30})
    plt.yticks(np.arange(0, 900, 50))
    plt.grid(True)
    plt.show()


    # plt.figure(1)
    # plt.rcParams["figure.autolayout"] = True
    # plt.plot(resistance1, linestyle = ['-', '--', '-.', ':'][3], c = 'red', alpha = 0.50, linewidth = 5 - 8 * 3 / 32, label = 'Generated Bank')
    # plt.plot(resistance2, linestyle = ['-', '--', '-.', ':'][1], c = 'blue', alpha = 0.50, linewidth = 5 - 8 * 1 / 32, label = 'Manual Bank')
    # plt.title("Resistance per turned-on Resistor Bank")
    # plt.legend()
    # plt.xlabel('Number of Turned-On Resistor Bank')
    # plt.ylabel('Resistance (Ohm)')
    # plt.show()