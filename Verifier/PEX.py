import paramiko
import ftplib
import os
import sys
import time
import DesignParameters

class PEX :
    '''
        Tech node 별로 제조사가 같아도 run rule file 이 다르다.
        Directory 를 나눠서 관리(서버상에서) 
        ex) /mnt/sdc/junung/PEX_run/TSMCxxn 로 설정하는 방식. 
        최소 1회 서버에서 manual 로 LVS / PEX run을 실행해야 한다.
    '''
    def __init__(self, username, password, WorkDir, PEXrunDir, libname, cellname, GDSDir, Vir_Connect) :
        self.server = '141.223.29.62'
        self.port = 22
        self.username = username
        self.password = password
        self.WorkDir = WorkDir
        self.PEXrunDir = PEXrunDir
        self.libname = libname
        self.cellname = cellname
        self.GDSDir = GDSDir if GDSDir != None else WorkDir
        self.Vir_Connect = Vir_Connect

    def PEXchecker(self) :
        if DesignParameters._Technology == '028nm' :
            PEXfile = '_calibre.run_'
            Techlib = 'cmos28lp'
        
        if DesignParameters._Technology == '045nm' :
            PEXfile = '_calibre.rcx_'
            Techlib = 'tsmcN45'

        if DesignParameters._Technology == '065nm' :
            PEXfile = '_calibre.rcx_'
            Techlib = 'tsmcN65'

        if DesignParameters._Technology == '090nm' :
            PEXfile = '_calibre.rcx_'
            Techlib = 'tsmcN90rf'

        print('   Connecting to Server by SSH...   '.center(105, '#'))
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(self.server, port=self.port, username=self.username, password=self.password)

        ##### Step 1 : Stream In/Out GDS file

        commandlines1 = "cd {0}; source setup.cshrc; strmin -library '{1}' -strmFile '{3}/{2}.gds' -attachTechFileOfLib '{4}' -logFile 'strmIn.log'"
        stdin, stdout, stderr = ssh.exec_command(commandlines1.format(self.WorkDir, self.libname, self.cellname, self.GDSDir, Techlib))
        result1 = stdout.read().decode('utf-8')
        print('print after commandlines1 : ')
        print(result1)
        if (result1.split()[-6]) != "'0'":
            raise Exception("Library name already Existing or XStream ERROR!!")

        if DesignParameters._Technology == '028nm' :
            commandlines2 = "cd {0}; source setup.cshrc; strmout -library '{1}' -strmFile '{3}/{2}.calibre.db' -topCell '{2}' -view layout -runDir '{3}' -logFile 'PIPO.LOG.{1}' -layerMap '/home/PDK/ss28nm/SEC_CDS/ln28lppdk/S00-V1.1.0.1_SEC2.0.6.2/oa/cmos28lp_tech_7U1x_2T8x_LB/cmos28lp_tech.layermap' -objectMap '/home/PDK/ss28nm/SEC_CDS/ln28lppdk/S00-V1.1.0.1_SEC2.0.6.2/oa/cmos28lp_tech_7U1x_2T8x_LB/cmos28lp_tech.objectmap' -case 'Preserve' -convertDot 'node' -noWarn '156 246 269 270 315 333'"
            stdin, stdout, stderr = ssh.exec_command(commandlines2.format(self.WorkDir, self.libname, self.cellname, self.PEXrunDir))
            result2 = stdout.read().decode('utf-8')
        if DesignParameters._Technology == '065nm' :
            commandlines2 = "cd {0}; strmout -library '{1}' -strmFile '{3}/{2}.calibre.db' -topCell '{2}' -view layout -runDir '{3}' -logFile 'PIPO.LOG.{1}' -layerMap '/home/PDK/tsmc65/tsmcN65/tsmcN65.layermap' -case 'Preserve' -convertDot 'node'"
            stdin, stdout, stderr = ssh.exec_command(commandlines2.format(self.WorkDir, self.libname, self.cellname, self.PEXrunDir))
            result2 = stdout.read().decode('utf-8')
        if DesignParameters._Technology == '045nm':
            commandlines2 = "cd {0}; strmout -library '{1}' -strmFile '{3}/{2}.calibre.db' -topCell '{2}' -view layout -runDir '{3}' -logFile 'PIPO.LOG.{1}' -layerMap '/home/PDK/tsmc40/tsmcN45/tsmcN45.layermap' -case 'Preserve' -convertDot 'node'"
            stdin, stdout, stderr = ssh.exec_command(commandlines2.format(self.WorkDir, self.libname, self.cellname, self.PEXrunDir))
            result2 = stdout.read().decode('utf-8')
        if DesignParameters._Technology == '090nm':
            commandlines2 = "cd {0}; strmout -library '{1}' -strmFile '{3}/{2}.calibre.db' -topCell '{2}' -view layout -runDir '{3}' -logFile 'PIPO.LOG.{1}' -layerMap '/home/PDK/tsmc90/tsmcN90rf/tsmcN90rf.layermap' -case 'Preserve' -convertDot 'node'"
            stdin, stdout, stderr = ssh.exec_command(commandlines2.format(self.WorkDir, self.libname, self.cellname, self.PEXrunDir))
            result2 = stdout.read().decode('utf-8')

        print(f'print after commandlines2 :')
        print(result2)
        if (result2.split()[-6]) != "'0'":
            raise Exception("XstreamOut ERROR")

        ##### Step 2 : Modifying lvs.cal file , you should extract schematic once before this procedure!!!!
        if DesignParameters._Technology == '028nm' :
            if self.Vir_Connect == True :
                commandlines3 = "cd {0}; sed -i '11s,.*,LAYOUT PATH  \"{0}/{1}.calibre.db\",' {2}; sed -i '12s,.*,LAYOUT PRIMARY \"{1}\",' {2}; sed -i '15s,.*,SOURCE PATH \"{0}/{1}.src.net\",' {2}; sed -i '16s,.*,SOURCE PRIMARY \"{1}\",' {2}; sed -i '19s,.*,MASK SVDB DIRECTORY \"svdb\" QUERY XRC IXF NXF SLPH,' {2}; sed -i '21s,.*,LVS REPORT \"{1}.lvs.report\",' {2}; sed -i '23s,.*,PEX NETLIST \"{0}/{1}.pex.netlist\" HSPICE 1 SOURCENAMES RCNAMED ,' {2}; sed -i '40s,.*,VIRTUAL CONNECT NAME ?,' {2}; sed -i '41s,.*,\
                    ,' {2}; sed -i '42s,.*,DRC ICSTATION YES,' {2}; sed -i '43s,.*,\
                        ,' {2}; sed -i '44s,.*,}},' {2}"
                stdin, stdout, stderr = ssh.exec_command(commandlines3.format(self.PEXrunDir, self.cellname, PEXfile, self.WorkDir))
                print(f'print after commandlines3 :')
                print(f"stdout: {stdout.read().decode('utf-8')}")
                print(f"stderr: {stderr.read().decode('utf-8')}")
            
            else :
                commandlines3 = "cd {0}; sed -i '11s,.*,LAYOUT PATH  \"{0}/{1}.calibre.db\",' {2}; sed -i '12s,.*,LAYOUT PRIMARY \"{1}\",' {2}; sed -i '15s,.*,SOURCE PATH \"{0}/{1}.src.net\",' {2}; sed -i '16s,.*,SOURCE PRIMARY \"{1}\",' {2}; sed -i '19s,.*,MASK SVDB DIRECTORY \"svdb\" QUERY XRC IXF NXF SLPH,' {2}; sed -i '21s,.*,LVS REPORT \"{1}.lvs.report\",' {2}; sed -i '23s,.*,PEX NETLIST \"{0}/{1}.pex.netlist\" HSPICE 1 SOURCENAMES RCNAMED ,' {2}; sed -i '40s,.*,\
                    ,' {2}; sed -i '41s,.*,DRC ICSTATION YES,' {2}; sed -i '42s,.*,\
                        ,' {2}; sed -i '43s,.*,}},' {2}"
                stdin, stdout, stderr = ssh.exec_command(commandlines3.format(self.PEXrunDir, self.cellname, PEXfile, self.WorkDir))
                print(f'print after commandlines3 :')
                print(f"stdout: {stdout.read().decode('utf-8')}")
                print(f"stderr: {stderr.read().decode('utf-8')}")

        if DesignParameters._Technology == '065nm' :
            if self.Vir_Connect == True :
                commandlines3 = "cd {0}; sed -i '11s,.*,LAYOUT PATH  \"{0}/{1}.calibre.db\",' {2}; sed -i '12s,.*,LAYOUT PRIMARY \"{1}\",' {2}; sed -i '15s,.*,SOURCE PATH \"{0}/{1}.src.net\",' {2}; sed -i '16s,.*,SOURCE PRIMARY \"{1}\",' {2}; sed -i '19s,.*,MASK SVDB DIRECTORY \"svdb\" QUERY XRC,' {2}; sed -i '21s,.*,LVS REPORT \"{1}.lvs.report\",' {2}; sed -i '23s,.*,PEX NETLIST \"{0}/{1}.pex.netlist\" HSPICE 1 SOURCENAMES ,' {2}; sed -i '40s,.*,VIRTUAL CONNECT NAME ?,' {2}; sed -i '41s,.*,\
                    ,' {2}; sed -i '42s,.*,DRC ICSTATION YES,' {2}; sed -i '43s,.*,\
                        ,' {2}; sed -i '44s,.*,}},' {2}"
                stdin, stdout, stderr = ssh.exec_command(commandlines3.format(self.PEXrunDir, self.cellname, PEXfile, self.WorkDir))
                print(f'print after commandlines3 :')
                print(f"stdout: {stdout.read().decode('utf-8')}")
                print(f"stderr: {stderr.read().decode('utf-8')}")
            
            else :
                commandlines3 = "cd {0}; sed -i '11s,.*,LAYOUT PATH  \"{0}/{1}.calibre.db\",' {2}; sed -i '12s,.*,LAYOUT PRIMARY \"{1}\",' {2}; sed -i '15s,.*,SOURCE PATH \"{0}/{1}.src.net\",' {2}; sed -i '16s,.*,SOURCE PRIMARY \"{1}\",' {2}; sed -i '19s,.*,MASK SVDB DIRECTORY \"svdb\" QUERY XRC,' {2}; sed -i '21s,.*,LVS REPORT \"{1}.lvs.report\",' {2}; sed -i '23s,.*,PEX NETLIST \"{0}/{1}.pex.netlist\" HSPICE 1 SOURCENAMES ,' {2}; sed -i '40s,.*,\
                    ,' {2}; sed -i '41s,.*,DRC ICSTATION YES,' {2}; sed -i '42s,.*,\
                        ,' {2}; sed -i '43s,.*,}},' {2}"
                stdin, stdout, stderr = ssh.exec_command(commandlines3.format(self.PEXrunDir, self.cellname, PEXfile, self.WorkDir))
                print(f'print after commandlines3 :')
                print(f"stdout: {stdout.read().decode('utf-8')}")
                print(f"stderr: {stderr.read().decode('utf-8')}")

        if DesignParameters._Technology == '090nm' : 
            if self.Vir_Connect == True :
                commandlines3 = "cd {0}; sed -i '9s,.*,LAYOUT PATH  \"{0}/{1}.calibre.db\",' {2}; sed -i '10s,.*,LAYOUT PRIMARY \"{1}\",' {2}; sed -i '13s,.*,SOURCE PATH \"{0}/{1}.src.net\",' {2}; sed -i '14s,.*,SOURCE PRIMARY \"{1}\",' {2}; sed -i '17s,.*,MASK SVDB DIRECTORY \"svdb\" QUERY XCALIBRE,' {2}; sed -i '19s,.*,LVS REPORT \"{1}.lvs.report\",' {2}; sed -i '21s,.*,PEX NETLIST \"{0}/{1}.pex.netlist\" HSPICE 1 SOURCENAMES ,' {2}; sed -i '37s,.*,VIRTUAL CONNECT NAME ?,' {2}; sed -i '38s,.*,\
                    ,' {2}; sed -i '39s,.*,DRC ICSTATION YES,' {2}; sed -i '40s,.*,\
                        ,' {2}"
                stdin, stdout, stderr = ssh.exec_command(commandlines3.format(self.PEXrunDir, self.cellname, PEXfile, self.WorkDir))
                print(f'print after commandlines3 :')
                print(f"stdout: {stdout.read().decode('utf-8')}")
                print(f"stderr: {stderr.read().decode('utf-8')}")
            
            else :
                commandlines3 = "cd {0}; sed -i '9s,.*,LAYOUT PATH  \"{0}/{1}.calibre.db\",' {2}; sed -i '12s,.*,LAYOUT PRIMARY \"{1}\",' {2}; sed -i '13s,.*,SOURCE PATH \"{0}/{1}.src.net\",' {2}; sed -i '14s,.*,SOURCE PRIMARY \"{1}\",' {2}; sed -i '17s,.*,MASK SVDB DIRECTORY \"svdb\" QUERY XCALIBRE,' {2}; sed -i '19s,.*,LVS REPORT \"{1}.lvs.report\",' {2}; sed -i '21s,.*,PEX NETLIST \"{0}/{1}.pex.netlist\" HSPICE 1 SOURCENAMES ,' {2}; sed -i '37s,.*,\
                    ,' {2}; sed -i '38s,.*,DRC ICSTATION YES,' {2}; sed -i '40s,.*,\
                        ,' {2}"
                stdin, stdout, stderr = ssh.exec_command(commandlines3.format(self.PEXrunDir, self.cellname, PEXfile, self.WorkDir))
                print(f'print after commandlines3 :')
                print(f"stdout: {stdout.read().decode('utf-8')}")
                print(f"stderr: {stderr.read().decode('utf-8')}")

        '''
            유의 : 45nm PEX 아직 62 server에서 지원 X. rules 파일 부재.
        if DesignParameters._Technology == '045nm' :
            if self.Vir_Connect == True :
                commandlines3 = "cd {0}; sed -i '11s,.*,LAYOUT PATH  \"{0}/{1}.calibre.db\",' {2}; sed -i '12s,.*,LAYOUT PRIMARY \"{1}\",' {2}; sed -i '15s,.*,SOURCE PATH \"{0}/{1}.src.net\",' {2}; sed -i '16s,.*,SOURCE PRIMARY \"{1}\",' {2}; sed -i '21s,.*,LVS REPORT \"{1}.lvs.report\",' {2}; sed -i '23s,.*,PEX NETLIST \"{0}/{1}.pex.netlist\" HSPICE 1 SOURCENAMES ,' {2}; sed -i '40s,.*,VIRTUAL CONNECT NAME ?,' {2}; sed -i '41s,.*,\n,' {2}; sed -i '42s,.*,DRC ICSTATION YES,' {2}; sed -i '43s,.*,\n,' {2}; sed -i '44s,.*,},' {2}"
                stdin, stdout, stderr = ssh.exec_command(commandlines3.format(self.PEXrunDir, self.cellname, PEXfile, self.WorkDir))
                print(f'print after commandlines3 :')
                print(f"stdout: {stdout.read().decode('utf-8')}")
                print(f"stderr: {stderr.read().decode('utf-8')}")
            
            else :
                commandlines3 = "cd {0}; sed -i '11s,.*,LAYOUT PATH  \"{0}/{1}.calibre.db\",' {2}; sed -i '12s,.*,LAYOUT PRIMARY \"{1}\",' {2}; sed -i '15s,.*,SOURCE PATH \"{0}/{1}.src.net\",' {2}; sed -i '16s,.*,SOURCE PRIMARY \"{1}\",' {2}; sed -i '21s,.*,LVS REPORT \"{1}.lvs.report\",' {2}; sed -i '23s,.*,PEX NETLIST \"{0}/{1}.pex.netlist\" HSPICE 1 SOURCENAMES ,' {2}; sed -i '40s,.*,\n,' {2}; sed -i '41s,.*,DRC ICSTATION YES,' {2}; sed -i '42s,.*,\n,' {2}; sed -i '43s,.*,},' {2}"
                stdin, stdout, stderr = ssh.exec_command(commandlines3.format(self.PEXrunDir, self.cellname, PEXfile, self.WorkDir))
                print(f'print after commandlines3 :')
                print(f"stdout: {stdout.read().decode('utf-8')}")
                print(f"stderr: {stderr.read().decode('utf-8')}")
        '''


        ##### Step 3 : Delete previous lvs report / pex report file

        commandlines33 = f"cd {self.PEXrunDir}; rm {self.cellname}.lvs.report; rm {self.cellname}.lvs.report.ext; rm {self.cellname}.pex.netlist; rm {self.cellname}.pex.netlist.pex; rm {self.cellname}.pex.netlist.{self.cellname}.pxi; cd {self.WorkDir}; rm {self.cellname}.sp"
        stdin, stdout, stderr = ssh.exec_command(commandlines33)
        print(f'print after commandlines33 :')
        print(f"stdout: {stdout.read().decode('utf-8')}")
        print(f"stderr: {stderr.read().decode('utf-8')}")

        ##### Step 4 : Running LVS / PEX..

        # commandlines41 = "cd {0}; source setup.cshrc; cd {1}; calibre -xact -3d -rcc -turbo -nowait {1}/{2}"
        # stdin, stdout, stderr = ssh.exec_command(commandlines41.format(self.WorkDir, self.PEXrunDir, PEXfile, self.cellname))
        # print(f"stdout: {stdout.read().decode('utf-8')}")
        # print(f"stderr: {stderr.read().decode('utf-8')}")
        if DesignParameters._Technology == '028nm' :
            commandlines4 = "cd {0}; source setup.cshrc; cd {1}; calibre -lvs -hier -spice {0}/{3}.sp -nowait -turbo {1}/{2}"
            stdin, stdout, stderr = ssh.exec_command(commandlines4.format(self.WorkDir, self.PEXrunDir, PEXfile, self.cellname))
            print(f"stdout: {stdout.read().decode('utf-8')}")
            print(f"stderr: {stderr.read().decode('utf-8')}")

            commandlines42 = "cd {0}; source setup.cshrc; cd {1}; calibre -xact -3d -rcc -turbo -nowait {1}/{2}"
            stdin, stdout, stderr = ssh.exec_command(commandlines42.format(self.WorkDir, self.PEXrunDir, PEXfile, self.cellname))
            print(f"stdout: {stdout.read().decode('utf-8')}")
            print(f"stderr: {stderr.read().decode('utf-8')}")

            commandlines43 = "cd {0}; source setup.cshrc; cd {1}; calibre -xact -fmt -all -nowait {1}/{2}"
            stdin, stdout, stderr = ssh.exec_command(commandlines43.format(self.WorkDir, self.PEXrunDir, PEXfile, self.cellname))
            print(f"stdout: {stdout.read().decode('utf-8')}")
            print(f"stderr: {stderr.read().decode('utf-8')}")

        if DesignParameters._Technology == '065nm' :
            commandlines4 = "cd {0}; cd {1}; calibre -lvs -hier -spice {0}/{3}.sp -nowait -turbo {1}/{2}"
            stdin, stdout, stderr = ssh.exec_command(commandlines4.format(self.WorkDir, self.PEXrunDir, PEXfile, self.cellname))
            print(f"stdout: {stdout.read().decode('utf-8')}")
            print(f"stderr: {stderr.read().decode('utf-8')}")

            commandlines42 = "cd {0}; cd {1}; calibre -xact -3d -rcc -turbo -nowait {1}/{2}"
            stdin, stdout, stderr = ssh.exec_command(commandlines42.format(self.WorkDir, self.PEXrunDir, PEXfile, self.cellname))
            print(f"stdout: {stdout.read().decode('utf-8')}")
            print(f"stderr: {stderr.read().decode('utf-8')}")

            commandlines43 = "cd {0}; cd {1}; calibre -xact -fmt -all -nowait {1}/{2}"
            stdin, stdout, stderr = ssh.exec_command(commandlines43.format(self.WorkDir, self.PEXrunDir, PEXfile, self.cellname))
            print(f"stdout: {stdout.read().decode('utf-8')}")
            print(f"stderr: {stderr.read().decode('utf-8')}")
        
        if DesignParameters._Technology == '090nm' :
            commandlines4 = "cd {0}; cd {1}; calibre -lvs -hier -spice {0}/{3}.sp -nowait -turbo {1}/{2}"
            stdin, stdout, stderr = ssh.exec_command(commandlines4.format(self.WorkDir, self.PEXrunDir, PEXfile, self.cellname))
            print(f"stdout: {stdout.read().decode('utf-8')}")
            print(f"stderr: {stderr.read().decode('utf-8')}")

            commandlines42 = "cd {0}; cd {1}; calibre -xrc -pdb -rcc -turbo -nowait {1}/{2}"
            stdin, stdout, stderr = ssh.exec_command(commandlines42.format(self.WorkDir, self.PEXrunDir, PEXfile, self.cellname))
            print(f"stdout: {stdout.read().decode('utf-8')}")
            print(f"stderr: {stderr.read().decode('utf-8')}")

            commandlines43 = "cd {0}; cd {1}; calibre -xrc -fmt -all -nowait {1}/{2}"
            stdin, stdout, stderr = ssh.exec_command(commandlines43.format(self.WorkDir, self.PEXrunDir, PEXfile, self.cellname))
            print(f"stdout: {stdout.read().decode('utf-8')}")
            print(f"stderr: {stderr.read().decode('utf-8')}")

        ##### Step 5 : Reading LVS report file..

        readfile = ssh.open_sftp()
        file = readfile.open('{0}/{1}.lvs.report'.format(self.PEXrunDir, self.cellname))
        print(f"Reading '{self.WorkDir}/{self.cellname}.lvs.report' for check LVS Error......")
        lines = file.readlines()
        line = lines[45]
        print(line)
        if 'INCORRECT' in line :
            raise Exception("LVS ERROR!!!")

        else:
            # commandlines5 = "cd {0}; rm -r {1}"
            # stdin, stdout, stderr = ssh.exec_command(commandlines5.format(self.WorkDir, self.libname))
            print('No LVS ERROR for this case')

        ##### Step 6 : Get pex netlist
        print('###### Gathering Parasitic Extracted Netlist from Server... ######')
        netlist = '{0}.pex.netlist'.format(self.cellname)
        ftp = ftplib.FTP(self.server)
        ftp.login(self.username, self.password)
        ftp.cwd(self.PEXrunDir)
        fd = open("./" + netlist, 'wb')
        ftp.retrbinary("RETR " + netlist, fd.write)
        fd.close()

        f = open(netlist,'r')
        lines = f.readlines()
        subckt_list = []
        i = 0
        for index,line in enumerate(lines) : 
            if '.subckt' in line :
                subckt_list.append(line)
                i = index
            if (index == i + 1) and '+' in line :
                subckt_list.append(line)
                i = i + 1

        l = subckt_list[0].split()
        l.pop(0)
        ckt_name = l[0]
        l[0] = 'x'+ l[0]
        l = " ".join(l)
        subckt_list[0] = l

        ll = subckt_list[-1].split()
        ll.append(ckt_name)
        ll = " ".join(ll)
        subckt_list [-1] = ll

        lines = lines + subckt_list
        new_lines = "".join(lines)
        f.close() 

        with open(netlist,'w') as f :
            f.write(new_lines)
            f.close()

        print('###### Uploading Parasitic Extracted Netlist to Server... ######')
        ftp = ftplib.FTP(self.server)
        ftp.login(self.username, self.password)
        ftp.cwd(self.PEXrunDir)
        fd = open("./" + netlist, 'rb')
        ftp.storbinary("STOR " + netlist, fd)
        fd.close()
        ftp.close()

        