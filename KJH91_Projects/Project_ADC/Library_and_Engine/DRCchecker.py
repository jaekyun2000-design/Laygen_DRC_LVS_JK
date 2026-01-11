import ftplib
import random
import paramiko
from . import DesignParameters

'''
    This is Beta Version For auto DRC checker.
    Before you start, write your skill code at your directory.
    # File name of this skill code should be 'Skillcode.il'
    # copy and paste of this file at /mnt/sdc/junung/OPUS/Samsung28n . (Not Working for now)
    This now works only at server 141.223.22.156
    Write down every parameters as string, for example : '/mnt/sdc/username/...'
    DO NOT WRITE DOWN SLASH (/) AT THE END OF YOUR DIRECTORY!!!
    Make sure to write down Dir1 as your working directory of cadence virtuoso.
    Also do not use library name that already exists in your directory.
    
    Usage : Make an instance for this class, and use the function 'DRCchecker'

    2021-08-06 Junung
'''


class DRCchecker:
    def __init__(self, username, password, WorkDir, DRCrunDir, libname, cellname, GDSDir=None):
        #self.server = '141.223.29.62'
        self.server = '141.223.24.54'
        #self.server = '141.223.22.174'
        #self.port = 22
        self.port = 1450
        self.username = username
        self.password = password
        self.WorkDir = WorkDir
        self.DRCrunDir = DRCrunDir
        self.libname = libname
        self.cellname = cellname
        self.GDSDir = GDSDir if GDSDir != None else WorkDir


    def DRCchecker(self):
        
        if DesignParameters._Technology == '028nm' :
            DRCfile = '_cmos28lp.drc.cal_'
            Techlib = 'cmos28lp'
        if DesignParameters._Technology == '065nm' :
            DRCfile = '_calibre.drc_'
            Techlib = 'tsmcN65'
        if DesignParameters._Technology == '045nm' :
            DRCfile = '_calibre.drc_'
            Techlib = 'tsmcN45'
        if DesignParameters._Technology == '090nm':
            DRCfile = '_calibre.drc_'
            Techlib = 'tsmcN90rf'

        print('   Connecting to Server by SSH...   '.center(105, '#'))
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(self.server, port=self.port, username=self.username, password=self.password)


        commandlines1 = "cd {0}; source setup.cshrc; strmin -library '{1}' -strmFile '{3}/{2}.gds' -attachTechFileOfLib '{4}' -logFile 'strmIn.log'"
        stdin, stdout, stderr = ssh.exec_command(commandlines1.format(self.WorkDir, self.libname, self.cellname, self.GDSDir, Techlib))
        result1 = stdout.read().decode('utf-8')
        print('print after commandlines1 : ')
        print(result1)
        if (result1.split()[-6]) != "'0'":
            raise Exception("Library name already Existing or XStream ERROR!!")

        if DesignParameters._Technology == '028nm' :
            #commandlines2 = "cd {0}; source setup.cshrc; strmout -library '{1}' -strmFile '{3}/{2}.calibre.db' -topCell '{2}' -view layout -runDir '{3}' -logFile 'PIPO.LOG.{1}' -layerMap '/home/PDK/ss28nm/SEC_CDS/ln28lppdk/S00-V1.1.0.1_SEC2.0.6.2/oa/cmos28lp_tech_7U1x_2T8x_LB/cmos28lp_tech.layermap' -objectMap '/home/PDK/ss28nm/SEC_CDS/ln28lppdk/S00-V1.1.0.1_SEC2.0.6.2/oa/cmos28lp_tech_7U1x_2T8x_LB/cmos28lp_tech.objectmap' -case 'Preserve' -convertDot 'node' -noWarn '156 246 269 270 315 333'"
            commandlines2 = "cd {0}; source setup.cshrc; strmout -library '{1}' -strmFile '{3}/{2}.calibre.db' -topCell '{2}' -view layout -runDir '{3}' -logFile 'PIPO.LOG.{1}' -layerMap '/tools/PDK/ss28lpp/device/oa/cmos28lp_tech_7U1x_2T8x_LB/cmos28lp_tech.layermap' -objectMap '/tools/PDK/ss28lpp/device/oa/cmos28lp_tech_7U1x_2T8x_LB/cmos28lp_tech.objectmap' -case 'Preserve' -convertDot 'node' -noWarn '156 246 269 270 315 333'"
            stdin, stdout, stderr = ssh.exec_command(commandlines2.format(self.WorkDir, self.libname, self.cellname, self.DRCrunDir))
            result2 = stdout.read().decode('utf-8')
        if DesignParameters._Technology == '065nm' :
            commandlines2 = "cd {0}; strmout -library '{1}' -strmFile '{3}/{2}.calibre.db' -topCell '{2}' -view layout -runDir '{3}' -logFile 'PIPO.LOG.{1}' -layerMap '/home/PDK/tsmc65/tsmcN65/tsmcN65.layermap' -case 'Preserve' -convertDot 'node'"
            stdin, stdout, stderr = ssh.exec_command(commandlines2.format(self.WorkDir, self.libname, self.cellname, self.DRCrunDir))
            result2 = stdout.read().decode('utf-8')
        if DesignParameters._Technology == '045nm':
            commandlines2 = "cd {0}; strmout -library '{1}' -strmFile '{3}/{2}.calibre.db' -topCell '{2}' -view layout -runDir '{3}' -logFile 'PIPO.LOG.{1}' -layerMap '/home/PDK/tsmc40/tsmcN45/tsmcN45.layermap' -case 'Preserve' -convertDot 'node'"
            stdin, stdout, stderr = ssh.exec_command(commandlines2.format(self.WorkDir, self.libname, self.cellname, self.DRCrunDir))
            result2 = stdout.read().decode('utf-8')
        if DesignParameters._Technology == '090nm':
            commandlines2 = "cd {0}; strmout -library '{1}' -strmFile '{3}/{2}.calibre.db' -topCell '{2}' -view layout -runDir '{3}' -logFile 'PIPO.LOG.{1}' -layerMap '/home/PDK/tsmc90/tsmcN90rf/tsmcN90rf.layermap' -case 'Preserve' -convertDot 'node'"
            stdin, stdout, stderr = ssh.exec_command(commandlines2.format(self.WorkDir, self.libname, self.cellname, self.DRCrunDir))
            result2 = stdout.read().decode('utf-8')


        print(f'print after commandlines2 :')
        print(result2)
        if (result2.split()[-6]) != "'0'":
            raise Exception("XstreamOut ERROR")
        
        commandlines3 = "cd {0}; sed -i '9s,.*,LAYOUT PATH  \"{0}/{1}.calibre.db\",' {2}; sed -i '10s,.*,LAYOUT PRIMARY \"{1}\",' {2}; sed -i '13s,.*,DRC RESULTS DATABASE \"{1}.drc.results\" ASCII,' {2}; sed -i '18s,.*,DRC SUMMARY REPORT \"{1}.drc.summary\" REPLACE HIER,' {2}"
        stdin, stdout, stderr = ssh.exec_command(commandlines3.format(self.DRCrunDir, self.cellname, DRCfile))
        print(f'print after commandlines3 :')
        print(f"stdout: {stdout.read().decode('utf-8')}")
        print(f"stderr: {stderr.read().decode('utf-8')}")

        commandlines33 = f"cd {self.WorkDir}; rm -rf {self.cellname}.drc.summary"        # delete previous summary file
        stdin, stdout, stderr = ssh.exec_command(commandlines33)
        print(f'print after commandlines33 :')
        print(f"stdout: {stdout.read().decode('utf-8')}")
        print(f"stderr: {stderr.read().decode('utf-8')}")

        #commandlines4 = "cd {0}; calibre -drc -hier -turbo -turbo_litho -nowait {1}/{2}"
        commandlines4 = "cd {0}; source setup.cshrc; calibre -drc -hier -turbo -turbo_litho -nowait {1}/{2}"
        #commandlines4 = "cd {0}; source setup.cshrc; calibre -drc -hier -turbo -turbo_litho -nowait ./DRC/DRC_run/{2}"
        stdin, stdout, stderr = ssh.exec_command(commandlines4.format(self.WorkDir, self.DRCrunDir, DRCfile))
        stdout.read()

        readfile = ssh.open_sftp()
        file = readfile.open('{0}/{1}.drc.summary'.format(self.WorkDir, self.cellname))
        print(f"Reading '{self.WorkDir}/{self.cellname}.drc.summary' for check DRC Error......")
        if DesignParameters._Technology == '028nm' :
            for line in (file.readlines()[-2:-1]):        # 'TOTAL DRC Results Generated:   656 (656)\n'
                print(line)
                if line.split()[4] != '0':
                    raise Exception("DRC ERROR!!!")

                else:
                    # commandlines5 = "cd {0}; sed -i '1s,.*,ddDeleteLocal(ddGetObj(\"{1}\" \"\" \"\" \"\")),' Skillcode.il"
                    # stdin, stdout, stderr = ssh.exec_command(commandlines5.format(self.WorkDir, self.libname))
                    # print (''.join(stdout.read()))
                    # commandlines6 = "cd {0}; source setup.cshrc; virtuoso -nograph -restore Skillcode.il"
                    # stdin, stdout, stderr = ssh.exec_command(commandlines6.format(self.WorkDir))
                    commandlines5 = "cd {0}; rm -r {1}"
                    stdin, stdout, stderr = ssh.exec_command(commandlines5.format(self.WorkDir, self.libname))
                    print('No DRC ERROR for this case, deleting library...')
        
        if DesignParameters._Technology == '065nm' :
            line = (file.readlines()[-1])        # 'TOTAL DRC Results Generated:   656 (656)\n'
            print(line)
            if line.split()[4] != '0':
                raise Exception("DRC ERROR!!!")

        if DesignParameters._Technology == '045nm':
            line = (file.readlines()[-1])  # 'TOTAL DRC Results Generated:   656 (656)\n'
            print(line)
            if line.split()[4] != '0':
                raise Exception("DRC ERROR!!!")

        if DesignParameters._Technology == '090nm':
            line = (file.readlines()[-1])  # 'TOTAL DRC Results Generated:   656 (656)\n'
            print(line)
            if line.split()[4] != '0':
                raise Exception("DRC ERROR!!!")

            else:
                # commandlines5 = "cd {0}; sed -i '1s,.*,ddDeleteLocal(ddGetObj(\"{1}\" \"\" \"\" \"\")),' Skillcode.il"
                # stdin, stdout, stderr = ssh.exec_command(commandlines5.format(self.WorkDir, self.libname))
                # print (''.join(stdout.read()))
                # commandlines6 = "cd {0}; source setup.cshrc; virtuoso -nograph -restore Skillcode.il"
                # stdin, stdout, stderr = ssh.exec_command(commandlines6.format(self.WorkDir))
                commandlines5 = "cd {0}; rm -r {1}"
                stdin, stdout, stderr = ssh.exec_command(commandlines5.format(self.WorkDir, self.libname))
                print('No DRC ERROR for this case, deleting library...')

        ssh.close()
        print(''.center(105, '#'))


    # def DRCchecker_PrintInputParams(self, InputParams:dict):
    #
    #     try:
    #         self.DRCchecker()
    #     except Exception as e:
    #         print('Error Occurred', e)
    #         print("=============================   Last Layout Object's Input Parameters are   =============================")
    #         for key, value in InputParams.items():
    #             print(f'{key} : {value}')
    #         print("=========================================================================================================")
    #         raise Exception("Something ERROR with DRCchecker !!!")
    #     else:
    #         print("=============================   Last Layout Object's Input Parameters are   =============================")
    #         for key, value in InputParams.items():
    #             print(f'{key} : {value}')
    #         print("=========================================================================================================")


    def Upload2FTP(self):
        """
        Upload GDS file to Working Directory
        """
        filename = self.cellname + '.gds'

        print('   Uploading GDS file...   '.center(105, '#'))
        ftp = ftplib.FTP()
        ftp.connect(host=self.server, port=1451)
        ftp.login(self.username, self.password)
        ftp.cwd(self.GDSDir)
        myFile = open('./{}'.format(filename), 'rb')
        #myFile = open('./gdsfile/{}'.format(filename), 'rb')
        ftp.storbinary('STOR ' + filename, myFile)
        myFile.close()
        ftp.quit()
        print(''.center(105, '#'))


    def StreamIn(self, tech:str = '028nm'):
        """
        Only StreamIn

        :param tech:  '028nm' | '065nm'
        """

        print('   Connecting to Server by SSH...   '.center(105, '#'))
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=self.server, port=self.port, username=self.username, password=self.password)

        if tech in ('028nm', None):
            TechFile = 'cmos28lp'
        elif tech == '065nm':
            TechFile = 'tsmcN65'
        elif tech == '045nm' :
            TechFile = 'tsmcN45'
        elif tech == '090nm' :
            TechFile = 'tsmcN90rf'

        else:
            raise NotImplemented
        filename = self.cellname + '.gds'
        commandlines1 = "cd {0}; source setup.cshrc; strmin -library '{1}' -strmFile '{2}/{3}' -attachTechFileOfLib {4} -logFile 'strmIn.log'"
        stdin, stdout, stderr = ssh.exec_command(commandlines1.format(self.WorkDir, self.libname, self.GDSDir, filename, TechFile))
        result1 = stdout.read().decode('utf-8')

        print('   Stream In   '.center(105, '-'))
        print(result1)
        if (result1.split()[-6]) != "'0'":          # Example of result1's Last Line : INFO (XSTRM-234): Translation completed. '0' error(s) and '125' warning(s) found.
            raise Exception("Library name already Existing or XStream ERROR!!")

        ssh.close()
        print(''.center(105, '#'))


def RandomParam(start: int, stop: int, step: int = 1) -> int:
    """
        return random integer number 'N' between 'start' and 'stop', ( start <= N <= stop )

    :raises: (stop - start) should be a multiples of 'step' for uniform distribution
    """
    assert (stop - start) % step == 0

    tmp = random.randint(start, stop + (step - 1))
    N = (tmp // step) * step

    return N
