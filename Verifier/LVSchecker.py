import paramiko
import ftplib
import os
import sys
import time
import DesignParameters

'''
    LVS checker 
    you should convert schematic into netlist (.src.net) first via CDL
    Vir_Connect option specifies LVS options to use connect all nets by name or not
'''

class LVStest :
    def __init__(self, username, password, WorkDir, LVSrunDir, libname, cellname, GDSDir, Netname, Nettopname, Vir_Connect) :
        self.server = '141.223.24.53'
        self.port = 22
        self.username = username
        self.password = password
        self.WorkDir = WorkDir
        self.LVSrunDir = LVSrunDir
        self.libname = libname
        self.cellname = cellname
        self.GDSDir = GDSDir if GDSDir != None else WorkDir
        self.Netname = Netname
        self.Nettopname = Nettopname
        self.Vir_Connect = Vir_Connect


    def LVSchecker(self) :

        '''
            This routine should be performed after modifying spice netlist file...
        '''

        if DesignParameters._Technology == '028nm' :
            LVSfile = '_ln28lpp.lvs.cal_'
            Techlib = 'cmos28lp'
        
        if DesignParameters._Technology == '045nm' :
            LVSfile = '_calibre.lvs_'
            Techlib = 'tsmcN45'

        if DesignParameters._Technology == '065nm' :
            LVSfile = '_calibre.lvs_'
            Techlib = 'tsmcN65'

        if DesignParameters._Technology == '090nm' :
            LVSfile = '_calibre.lvs_'
            Techlib = 'tsmcN90rf'

        print('   Connecting to Server by SSH...   '.center(105, '#'))
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(self.server, port=self.port, username=self.username, password=self.password)

        ##### Step 1 : Stream In/Out GDS file

        if DesignParameters._Technology == '028nm' :
            commandlines1 = "cd {0}; source setup.cshrc; strmin -library '{1}' -strmFile '{3}/{2}.gds' -attachTechFileOfLib '{4}' -logFile 'strmIn.log'"
            stdin, stdout, stderr = ssh.exec_command(commandlines1.format(self.WorkDir, self.libname, self.cellname, self.GDSDir, Techlib))
            result1 = stdout.read().decode('utf-8')
            print('print after commandlines1 : ')
            print(result1)
            if (result1.split()[-6]) != "'0'":
                raise Exception("Library name already Existing or XStream ERROR!!")
        
        if DesignParameters._Technology != '028nm' :
            commandlines1 = "cd {0}; strmin -library '{1}' -strmFile '{3}/{2}.gds' -attachTechFileOfLib '{4}' -logFile 'strmIn.log'"
            stdin, stdout, stderr = ssh.exec_command(commandlines1.format(self.WorkDir, self.libname, self.cellname, self.GDSDir, Techlib))
            result1 = stdout.read().decode('utf-8')
            print('print after commandlines1 : ')
            print(result1)
            if (result1.split()[-6]) != "'0'":
                raise Exception("Library name already Existing or XStream ERROR!!")

        if DesignParameters._Technology == '028nm' :
            commandlines2 = "cd {0}; source setup.cshrc; strmout -library '{1}' -strmFile '{3}/{2}.calibre.db' -topCell '{2}' -view layout -runDir '{3}' -logFile 'PIPO.LOG.{1}' -layerMap '/home/PDK/ss28nm/SEC_CDS/ln28lppdk/S00-V1.1.0.1_SEC2.0.6.2/oa/cmos28lp_tech_7U1x_2T8x_LB/cmos28lp_tech.layermap' -objectMap '/home/PDK/ss28nm/SEC_CDS/ln28lppdk/S00-V1.1.0.1_SEC2.0.6.2/oa/cmos28lp_tech_7U1x_2T8x_LB/cmos28lp_tech.objectmap' -case 'Preserve' -convertDot 'node' -noWarn '156 246 269 270 315 333'"
            stdin, stdout, stderr = ssh.exec_command(commandlines2.format(self.WorkDir, self.libname, self.cellname, self.LVSrunDir))
            result2 = stdout.read().decode('utf-8')
        if DesignParameters._Technology == '065nm' :
            commandlines2 = "cd {0}; strmout -library '{1}' -strmFile '{3}/{2}.calibre.db' -topCell '{2}' -view layout -runDir '{3}' -logFile 'PIPO.LOG.{1}' -layerMap '/home/PDK/tsmc65/tsmcN65/tsmcN65.layermap' -case 'Preserve' -convertDot 'node'"
            stdin, stdout, stderr = ssh.exec_command(commandlines2.format(self.WorkDir, self.libname, self.cellname, self.LVSrunDir))
            result2 = stdout.read().decode('utf-8')
        if DesignParameters._Technology == '045nm':
            commandlines2 = "cd {0}; strmout -library '{1}' -strmFile '{3}/{2}.calibre.db' -topCell '{2}' -view layout -runDir '{3}' -logFile 'PIPO.LOG.{1}' -layerMap '/home/PDK/tsmc40/tsmcN45/tsmcN45.layermap' -case 'Preserve' -convertDot 'node'"
            stdin, stdout, stderr = ssh.exec_command(commandlines2.format(self.WorkDir, self.libname, self.cellname, self.LVSrunDir))
            result2 = stdout.read().decode('utf-8')
        if DesignParameters._Technology == '090nm':
            commandlines2 = "cd {0}; strmout -library '{1}' -strmFile '{3}/{2}.calibre.db' -topCell '{2}' -view layout -runDir '{3}' -logFile 'PIPO.LOG.{1}' -layerMap '/home/PDK/tsmc90/tsmcN90rf/tsmcN90rf.layermap' -case 'Preserve' -convertDot 'node'"
            stdin, stdout, stderr = ssh.exec_command(commandlines2.format(self.WorkDir, self.libname, self.cellname, self.LVSrunDir))
            result2 = stdout.read().decode('utf-8')

        print(f'print after commandlines2 :')
        print(result2)
        if (result2.split()[-6]) != "'0'":
            raise Exception("XstreamOut ERROR")

        ##### Step 2 : Modifying lvs.cal file , you should extract schematic once before this procedure!!!!

        if DesignParameters._Technology == '028nm' :
            if self.Vir_Connect == True :
                commandlines3 = "cd {0}; sed -i '11s|.*|LAYOUT PATH  \"{0}/{1}.calibre.db\"|' {2}; sed -i '12s|.*|LAYOUT PRIMARY \"{1}\"|' {2}; sed -i '15s|.*|SOURCE PATH \"{0}/{4}.src.net\"|' {2}; sed -i '16s|.*|SOURCE PRIMARY \"{5}\"|' {2}; sed -i '21s|.*|LVS REPORT \"{1}.lvs.report\"|' {2}; sed -i '42s|.*|VIRTUAL CONNECT REPORT MAXIMUM ALL|' {2}; sed -i '43s|.*|VIRTUAL CONNECT NAME ?|' {2}; sed -i '44s|.*|\
                    |' {2}; sed -i '45s|.*|LVS EXECUTE ERC YES|' {2}; sed -i '46s|.*|ERC RESULTS DATABASE \"{1}.erc.results\" |' {2}; sed -i '47s|.*|ERC SUMMARY REPORT \"{1}.erc.summary\" REPLACE HIER|' {2}; sed -i '48s|.*|ERC CELL NAME YES CELL SPACE XFORM|' {2}; sed -i '49s|.*|ERC MAXIMUM RESULTS 1000|' {2}; sed -i '50s|.*|ERC MAXIMUM VERTEX 4096|' {2}; sed -i '51s|.*|\
                        |' {2}; sed -i '52s|.*|DRC ICSTATION YES|' {2}; sed -i '53s|.*|\
                            |' {2}; sed -i '54s|.*|}}|' {2}"
                stdin, stdout, stderr = ssh.exec_command(commandlines3.format(self.LVSrunDir, self.cellname, LVSfile, self.WorkDir, self.Netname, self.Nettopname))
                print(f'print after commandlines3 :')
                print(f"stdout: {stdout.read().decode('utf-8')}")
                print(f"stderr: {stderr.read().decode('utf-8')}")
            
            else :
                commandlines3 = "cd {0}; sed -i '11s|.*|LAYOUT PATH  \"{0}/{1}.calibre.db\"|' {2}; sed -i '12s|.*|LAYOUT PRIMARY \"{1}\"|' {2}; sed -i '15s|.*|SOURCE PATH \"{0}/{4}.src.net\"|' {2}; sed -i '16s|.*|SOURCE PRIMARY \"{5}\"|' {2}; sed -i '21s|.*|LVS REPORT \"{1}.lvs.report\"|' {2}; sed -i '42s|.*|VIRTUAL CONNECT REPORT MAXIMUM ALL|' {2}; sed -i '43s|.*|\
                    |' {2}; sed -i '44s|.*|LVS EXECUTE ERC YES|' {2}; sed -i '45s|.*|ERC RESULTS DATABASE \"{1}.erc.results\" |' {2}; sed -i '46s|.*|ERC SUMMARY REPORT \"{1}.erc.summary\" REPLACE HIER|' {2}; sed -i '47s|.*|ERC CELL NAME YES CELL SPACE XFORM|' {2}; sed -i '48s|.*|ERC MAXIMUM RESULTS 1000|' {2}; sed -i '49s|.*|ERC MAXIMUM VERTEX 4096|' {2}; sed -i '50s|.*|\
                        |' {2}; sed -i '51s|.*|DRC ICSTATION YES|' {2}; sed -i '52s|.*|\
                            |' {2}; sed -i '53s|.*|}}|' {2}; sed -i '54s|.*|\
                                |' {2}"
                stdin, stdout, stderr = ssh.exec_command(commandlines3.format(self.LVSrunDir, self.cellname, LVSfile, self.WorkDir, self.Netname, self.Nettopname))
                print(f'print after commandlines3 :')
                print(f"stdout: {stdout.read().decode('utf-8')}")
                print(f"stderr: {stderr.read().decode('utf-8')}")

        if DesignParameters._Technology == '065nm' or DesignParameters._Technology == '045nm' :
            if self.Vir_Connect == True :
                commandlines3 = "cd {0}; sed -i '11s|.*|LAYOUT PATH  \"{0}/{1}.calibre.db\"|' {2}; sed -i '12s|.*|LAYOUT PRIMARY \"{1}\"|' {2}; sed -i '15s|.*|SOURCE PATH \"{0}/{4}.src.net\"|' {2}; sed -i '16s|.*|SOURCE PRIMARY \"{5}\"|' {2}; sed -i '21s|.*|LVS REPORT \"{1}.lvs.report\"|' {2}; sed -i '42s|.*|VIRTUAL CONNECT REPORT MAXIMUM ALL|' {2}; sed -i '43s|.*|VIRTUAL CONNECT NAME ?|' {2}; sed -i '44s|.*|\
                    |' {2}; sed -i '45s|.*|LVS EXECUTE ERC YES|' {2}; sed -i '46s|.*|ERC RESULTS DATABASE \"{1}.erc.results\" |' {2}; sed -i '47s|.*|ERC SUMMARY REPORT \"{1}.erc.summary\" REPLACE HIER|' {2}; sed -i '48s|.*|ERC CELL NAME YES CELL SPACE XFORM|' {2}; sed -i '49s|.*|ERC MAXIMUM RESULTS 1000|' {2}; sed -i '50s|.*|ERC MAXIMUM VERTEX 4096|' {2}; sed -i '51s|.*|\
                    |' {2}; sed -i '52s|.*|DRC ICSTATION YES|' {2}; sed -i '53s|.*|\
                        |' {2}; sed -i '54s|.*|}}|' {2}"
                stdin, stdout, stderr = ssh.exec_command(commandlines3.format(self.LVSrunDir, self.cellname, LVSfile, self.WorkDir, self.Netname, self.Nettopname))
                print(f'print after commandlines3 :')
                print(f"stdout: {stdout.read().decode('utf-8')}")
                print(f"stderr: {stderr.read().decode('utf-8')}")
            
            else :
                commandlines3 = "cd {0}; sed -i '11s|.*|LAYOUT PATH  \"{0}/{1}.calibre.db\"|' {2}; sed -i '12s|.*|LAYOUT PRIMARY \"{1}\"|' {2}; sed -i '15s|.*|SOURCE PATH \"{0}/{4}.src.net\"|' {2}; sed -i '16s|.*|SOURCE PRIMARY \"{5}\"|' {2}; sed -i '21s|.*|LVS REPORT \"{1}.lvs.report\"|' {2}; sed -i '42s|.*|VIRTUAL CONNECT REPORT MAXIMUM ALL|' {2}; sed -i '43s|.*|\
                    |' {2}; sed -i '44s|.*|LVS EXECUTE ERC YES|' {2}; sed -i '45s|.*|ERC RESULTS DATABASE \"{1}.erc.results\" |' {2}; sed -i '46s|.*|ERC SUMMARY REPORT \"{1}.erc.summary\" REPLACE HIER|' {2}; sed -i '47s|.*|ERC CELL NAME YES CELL SPACE XFORM|' {2}; sed -i '48s|.*|ERC MAXIMUM RESULTS 1000|' {2}; sed -i '49s|.*|ERC MAXIMUM VERTEX 4096|' {2}; sed -i '50s|.*|\
                        |' {2}; sed -i '51s|.*|DRC ICSTATION YES|' {2}; sed -i '52s|.*|\
                            |' {2}; sed -i '53s|.*|}}|' {2}; sed -i '54s|.*|\
                                |' {2}"
                stdin, stdout, stderr = ssh.exec_command(commandlines3.format(self.LVSrunDir, self.cellname, LVSfile, self.WorkDir, self.Netname, self.Nettopname))
                print(f'print after commandlines3 :')
                print(f"stdout: {stdout.read().decode('utf-8')}")
                print(f"stderr: {stderr.read().decode('utf-8')}")

        if DesignParameters._Technology == '090nm' :
            if self.Vir_Connect == True :
                commandlines3 = "cd {0}; sed -i '9s|.*|LAYOUT PATH  \"{0}/{1}.calibre.db\"|' {2}; sed -i '10s|.*|LAYOUT PRIMARY \"{1}\"|' {2}; sed -i '13s|.*|SOURCE PATH \"{0}/{4}.src.net\"|' {2}; sed -i '14s|.*|SOURCE PRIMARY \"{5}\"|' {2}; sed -i '19s|.*|LVS REPORT \"{1}.lvs.report\"|' {2}; sed -i '38s|.*|VIRTUAL CONNECT COLON NO|' {2}; sed -i '39s|.*|VIRTUAL CONNECT REPORT NO|' {2}; sed -i '40s|.*|VIRTUAL CONNECT NAME ?|' {2}; sed -i '41s|.*|\
                    |' {2}; sed -i '42s|.*|LVS EXECUTE ERC YES|' {2}; sed -i '43s|.*|ERC RESULTS DATABASE \"{1}.erc.results\" |' {2}; sed -i '44s|.*|ERC SUMMARY REPORT \"{1}.erc.summary\" REPLACE HIER|' {2}; sed -i '45s|.*|ERC CELL NAME YES CELL SPACE XFORM|' {2}; sed -i '46s|.*|ERC MAXIMUM RESULTS 1000|' {2}; sed -i '47s|.*|ERC MAXIMUM VERTEX 4096|' {2}; sed -i '51s|.*|\
                    |' {2}; sed -i '49s|.*|DRC ICSTATION YES|' {2}; sed -i '50s|.*|\
                        |' {2}; sed -i '51s|.*|\
                        |' {2};"
                stdin, stdout, stderr = ssh.exec_command(commandlines3.format(self.LVSrunDir, self.cellname, LVSfile, self.WorkDir, self.Netname, self.Nettopname))
                print(f'print after commandlines3 :')
                print(f"stdout: {stdout.read().decode('utf-8')}")
                print(f"stderr: {stderr.read().decode('utf-8')}")

            else :
                commandlines3 = "cd {0}; sed -i '9s|.*|LAYOUT PATH  \"{0}/{1}.calibre.db\"|' {2}; sed -i '10s|.*|LAYOUT PRIMARY \"{1}\"|' {2}; sed -i '13s|.*|SOURCE PATH \"{0}/{4}.src.net\"|' {2}; sed -i '14s|.*|SOURCE PRIMARY \"{5}\"|' {2}; sed -i '19s|.*|LVS REPORT \"{1}.lvs.report\"|' {2}; sed -i '38s|.*|VIRTUAL CONNECT COLON NO|' {2}; sed -i '39s|.*|VIRTUAL CONNECT REPORT NO|' {2}; sed -i '41s|.*|\
                    |' {2}; sed -i '42s|.*|LVS EXECUTE ERC YES|' {2}; sed -i '43s|.*|ERC RESULTS DATABASE \"{1}.erc.results\" |' {2}; sed -i '44s|.*|ERC SUMMARY REPORT \"{1}.erc.summary\" REPLACE HIER|' {2}; sed -i '45s|.*|ERC CELL NAME YES CELL SPACE XFORM|' {2}; sed -i '46s|.*|ERC MAXIMUM RESULTS 1000|' {2}; sed -i '47s|.*|ERC MAXIMUM VERTEX 4096|' {2}; sed -i '51s|.*|\
                    |' {2}; sed -i '49s|.*|DRC ICSTATION YES|' {2}; sed -i '50s|.*|\
                        |' {2}; sed -i '51s|.*|\
                        |' {2};"
                stdin, stdout, stderr = ssh.exec_command(commandlines3.format(self.LVSrunDir, self.cellname, LVSfile, self.WorkDir, self.Netname, self.Nettopname))
                print(f'print after commandlines3 :')
                print(f"stdout: {stdout.read().decode('utf-8')}")
                print(f"stderr: {stderr.read().decode('utf-8')}")
        ##### Step 3 : Delete previous lvs report file

        commandlines33 = f"cd {self.LVSrunDir}; rm {self.cellname}.lvs.report; rm {self.cellname}.erc.results; rm {self.cellname}.erc.summary; cd {self.WorkDir}; rm {self.cellname}.sp"
        stdin, stdout, stderr = ssh.exec_command(commandlines33)
        print(f'print after commandlines33 :')
        print(f"stdout: {stdout.read().decode('utf-8')}")
        print(f"stderr: {stderr.read().decode('utf-8')}")

        ##### Step 4 : Running LVS..

        if DesignParameters._Technology == '028nm' :
            commandlines4 = "cd {0}; source setup.cshrc; cd {1}; calibre -spice {0}/{3}.sp -turbo -lvs -hier -nowait {1}/{2}"
            stdin, stdout, stderr = ssh.exec_command(commandlines4.format(self.WorkDir, self.LVSrunDir, LVSfile, self.cellname))
            print(f"stdout: {stdout.read().decode('utf-8')}")
            print(f"stderr: {stderr.read().decode('utf-8')}")

        if DesignParameters._Technology != '028nm' :
            commandlines4 = "cd {0}; cd {1}; calibre -spice {0}/{3}.sp -turbo -lvs -hier -nowait {1}/{2}"
            stdin, stdout, stderr = ssh.exec_command(commandlines4.format(self.WorkDir, self.LVSrunDir, LVSfile, self.cellname))
            print(f"stdout: {stdout.read().decode('utf-8')}")
            print(f"stderr: {stderr.read().decode('utf-8')}")

        ##### Step 5 : Reading LVS report file..

        readfile = ssh.open_sftp()
        file = readfile.open('{0}/{1}.lvs.report'.format(self.LVSrunDir, self.cellname))
        print(f"Reading '{self.WorkDir}/{self.cellname}.lvs.report' for check LVS Error......")
        for line in (file.readlines()[43:48]): 
            print(line)
            if 'INCORRECT' in line :
                raise Exception("LVS ERROR!!!")
        # print(line)
        # if 'INCORRECT' in line :
        #     raise Exception("LVS ERROR!!!")

            else:
                commandlines5 = "cd {0}; rm -rf {1}"
                stdin, stdout, stderr = ssh.exec_command(commandlines5.format(self.WorkDir, self.libname))
                print('No LVS ERROR for this case')