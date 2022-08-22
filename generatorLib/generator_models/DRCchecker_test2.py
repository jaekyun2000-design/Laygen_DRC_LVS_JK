import ftplib
import random
import paramiko
import sys
from generatorLib import DesignParameters

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
        self.server = '141.223.29.62'
        self.port = 22
        self.username = username
        self.password = password
        self.WorkDir = WorkDir
        self.DRCrunDir = DRCrunDir
        self.libname = libname
        self.cellname = cellname
        self.GDSDir = GDSDir if GDSDir != None else WorkDir


    def DRCchecker(self):

        if DesignParameters._Technology == 'SS28nm' :
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


        # commandlines1 = "cd {0}; source setup.cshrc; strmin -library '{1}' -strmFile '{3}/{2}.gds' -attachTechFileOfLib '{4}' -logFile 'strmIn.log'"
        # print(f"commandlines1: {commandlines1.format(self.WorkDir, self.libname, self.cellname, self.GDSDir, Techlib)}")
        # stdin, stdout, stderr = ssh.exec_command(commandlines1.format(self.WorkDir, self.libname, self.cellname, self.GDSDir, Techlib))
        # result1 = stdout.read().decode('utf-8')
        # print('print after commandlines1 : ')
        # print(result1)
        # if (result1.split()[-6]) != "'0'":
        #     raise Exception("Library name already Existing or XStream ERROR!!")

        if DesignParameters._Technology == 'SS28nm' :
            commandlines2 = "cd {0}; source setup.cshrc; strmout -library '{1}' -strmFile '{3}/{2}.calibre.db' -topCell '{2}' -view layout -runDir '{3}' -logFile 'PIPO.LOG.{1}' -layerMap '/home/PDK/ss28nm/SEC_CDS/ln28lppdk/S00-V1.1.0.1_SEC2.0.6.2/oa/cmos28lp_tech_7U1x_2T8x_LB/cmos28lp_tech.layermap' -objectMap '/home/PDK/ss28nm/SEC_CDS/ln28lppdk/S00-V1.1.0.1_SEC2.0.6.2/oa/cmos28lp_tech_7U1x_2T8x_LB/cmos28lp_tech.objectmap' -case 'Preserve' -convertDot 'node' -noWarn '156 246 269 270 315 333'"
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

        ''' drc run directory에 rule file ? 존재해야힘/ DRCfile... '''
        # commandlines3 = "cd {0}; sed -i '9s,.*,LAYOUT PATH  \"{0}/{1}.calibre.db\",' {2}; sed -i '10s,.*,LAYOUT PRIMARY \"{1}\",' {2}; sed -i '13s,.*,DRC RESULTS DATABASE \"{1}.drc.results\" ASCII,' {2}; sed -i '18s,.*,DRC SUMMARY REPORT \"{1}.drc.summary\" REPLACE HIER,' {2}"
        commandlines3 = "cd {0}; sed -i '9s,.*,LAYOUT PATH  \"{1}.calibre.db\",' {2}; sed -i '10s,.*,LAYOUT PRIMARY \"{1}\",' {2}; sed -i '13s,.*,DRC RESULTS DATABASE \"{1}.drc.results\" ASCII,' {2}; sed -i '18s,.*,DRC SUMMARY REPORT \"{1}.drc.summary\" REPLACE HIER,' {2}"
        stdin, stdout, stderr = ssh.exec_command(commandlines3.format(self.DRCrunDir, self.cellname, DRCfile))
        print(f'print after commandlines3 :')
        print(f"stdout: {stdout.read().decode('utf-8')}")
        print(f"stderr: {stderr.read().decode('utf-8')}")

        #commandlines33 = f"cd {self.WorkDir}; rm {self.cellname}.drc.summary"        # delete previous summary file
        commandlines33 = f"cd {self.DRCrunDir}; rm {self.cellname}.drc.summary"        # delete previous summary file
        stdin, stdout, stderr = ssh.exec_command(commandlines33)
        print(f'print after commandlines33 :')
        print(f"stdout: {stdout.read().decode('utf-8')}")
        print(f"stderr: {stderr.read().decode('utf-8')}")

        # commandlines4 = "cd {0}; source setup.cshrc; calibre -drc -hier -turbo -turbo_litho -nowait {1}/{2}"
        commandlines4 = "cd {0}; source setup.cshrc; calibre -drc -hier -nowait {1}/{2}"
        stdin, stdout, stderr = ssh.exec_command(commandlines4.format(self.WorkDir, self.DRCrunDir, DRCfile))
        # stdin, __, stderr = ssh.exec_command(commandlines4.format(self.WorkDir, self.DRCrunDir, DRCfile))
        print(f'print after commandlines4 :')
        # stdout.read().decode('utf8')        # 24s 1:53s no print
        # stdout.read().decode('utf-8')         # 1:58s
        # stdout.read()                           # 2:04s no print

        while 1:
            lines = stdout.readlines(1000000)              # 21s 17s
            if not lines:
                break
            for line in lines:
                print(line, end="")
                # print(line)

        # for line in iter(stdout.readline, ""):              # 1:01s print
        #     print(line, end="")

        readfile = ssh.open_sftp()
        # file = readfile.open('{0}/{1}.drc.summary'.format(self.WorkDir, self.cellname))
        file = readfile.open('{0}/{1}.drc.summary'.format(self.DRCrunDir, self.cellname))
        print(f"Reading '{self.WorkDir}/{self.cellname}.drc.summary' for check DRC Error......")
        if DesignParameters._Technology == 'SS28nm' :
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
        ftp = ftplib.FTP(self.server)
        ftp.login(self.username, self.password)
        ftp.cwd(self.GDSDir)
        myFile = open(filename, 'rb')
        ftp.storbinary('STOR ' + filename, myFile)
        myFile.close()
        ftp.quit()
        print(''.center(105, '#'))


    def StreamIn(self, tech:str = 'SS28nm'):
        """
        Only StreamIn

        :param tech:  'SS28nm' | '065nm'
        """

        print('   Connecting to Server by SSH...   '.center(105, '#'))
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=self.server, port=self.port, username=self.username, password=self.password)
        print('SSH Connected...')

        if tech in ('SS28nm', None):
            TechFile = 'cmos28lp'
        elif tech == 'SS65nm':
            TechFile = 'lf6s'
        elif tech == 'TSMC65nm':
            TechFile = 'tsmcN65'
        else:
            raise NotImplemented

        if tech in ('SS28nm', None):
            CommandLine_ChangeDir = f"cd {self.WorkDir}; source setup.cshrc;"
        elif tech == 'SS65nm':
            CommandLine_ChangeDir = f"s65;"
        else:
            raise NotImplemented
        CommandLine_StreamIn = f"strmin -library '{self.libname}' -strmFile '{self.GDSDir}/{self.cellname}.gds' -attachTechFileOfLib {TechFile} -logFile 'strmIn.log'"
        commandlines1 = CommandLine_ChangeDir + CommandLine_StreamIn
        commandlines1 = commandlines1 + " -noDetectVias"                # Option. To identify Via Objects' Names (For Debugging) | option 활성화하면 streamIn 속도 조금 느려짐.
        print(f"commandline1: {commandlines1}")
        stdin, stdout, stderr = ssh.exec_command(commandlines1)         # 이전 라이브러리 존재하면 streamin 느려짐. 없을때 0.5 ~ 1s, 있을떄 3 ~ 6s


        ''' prev code '''
        # result1 = stdout.read().decode('utf-8')
        #
        # print('   Stream In   '.center(105, '-'))
        # print(result1)
        # if (result1.split()[-6]) != "'0'":          # Example of result1's Last Line : INFO (XSTRM-234): Translation completed. '0' error(s) and '125' warning(s) found.
        #     raise Exception("Library name already Existing or XStream ERROR!!")
        ''' modified code '''
        while 1:
            lines = stdout.readlines(1000000)              #
            if not lines:
                break
            for line in lines:
                print(line, end="")
        if (line.split()[-6]) != "'0'":          # Example of result1's Last Line : INFO (XSTRM-234): Translation completed. '0' error(s) and '125' warning(s) found.
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
