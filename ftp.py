import user_setup
import ftplib
import paramiko


################ Privacy Information ################
server_ip = '141.223.29.62'
ftp_port = 21
ssh_port = 22
user = ''
pwd = ''

if user_setup._Technology == 'SS28nm':
    ftp_dir = '~/OPUS/ss28/gds'
    ssh_dir = '~/OPUS/ss28'
    tech_file = 'cmos28lp'
elif user_setup._Technology == 'TSMC65nm':
    ftp_dir = '~/OPUS/tsmc65/gds'
    ssh_dir = '~/OPUS/tsmc65'
    tech_file = 'tsmcN65'
else:
    raise NotImplemented

#####################################################

def upload_ftp(file, name, ip=server_ip, port=ftp_port, user=user, pwd=pwd, dir=ftp_dir):
    try:
        ftp_ = ftplib.FTP()
        ftp_.connect(ip, port)
        ftp_.login(user, pwd)
        ftp_.cwd(dir)
        ftp_.storbinary(f'STOR {name}', file)
        ftp_.close()
        return True, 'FTP upload success.'
    except:
        return False, 'FTP upload fail'

def stream(lib_name, file_name, file_path=ftp_dir, tech_file = tech_file, ip = server_ip, path=ssh_dir, user=user, pwd=pwd, port=ssh_port):
    try:
        ssh_ = paramiko.SSHClient()
        ssh_.set_missing_host_key_policy(paramiko.AutoAddPolicy)
        ssh_.connect(ip, port, user, pwd)

        command = f'cd {path}; source setup.cshrc; strmin -library {lib_name} -strmFile {file_path}/{file_name} -attachTechFileOfLib {tech_file} -logFile "autoStrmIn.log"'
        stdin, stdout, stderr = ssh_.exec_command(command)
        result = stdout.read().decode('utf-8')
        ssh_.close()
        if result.split()[-6] != "'0'":
            return False, 'Stream In Fail'
        else:
            return True, 'Stream In Sucess'
    except:
        return False, 'Stream In Fail'






