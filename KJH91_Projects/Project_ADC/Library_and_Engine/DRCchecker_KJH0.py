import paramiko
from . import DRCchecker

'''
	
	
	
'''


class DRCchecker_KJH0(DRCchecker.DRCchecker):

	def cell_deletion(self):
	
		print('   Connecting to Server by SSH...   '.center(105, '#'))
		ssh = paramiko.SSHClient()
		ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		ssh.connect(hostname=self.server, port=self.port, username=self.username, password=self.password)

		#filename = self.cellname + '.gds'
		
		#commandlines1 = "cd {0}; cd {1}; find. -name'*{2}*' -delete"
		commandlines1 = "cd {0}; cd {1}; rm -rf ./{2}*"
		stdin, stdout, stderr = ssh.exec_command(commandlines1.format(self.WorkDir, self.libname, self.cellname,))
		
		
		ssh.close()
		print(''.center(105, '#'))
	
	def lib_deletion(self):
	
		print('   Connecting to Server by SSH...   '.center(105, '#'))
		ssh = paramiko.SSHClient()
		ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		ssh.connect(hostname=self.server, port=self.port, username=self.username, password=self.password)

		#
		filename = self.cellname + '.gds'
		
		commandlines1 = "cd {0}; rm -rf ./{1};"
		stdin, stdout, stderr = ssh.exec_command(commandlines1.format(self.WorkDir, self.libname,))
		
		
		ssh.close()
		print(''.center(105, '#'))
		