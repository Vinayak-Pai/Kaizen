import paramiko

__author__ = 'vinayak'

hostname, username, password = '', ' ', ' '

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
try:
    ssh.connect(hostname=hostname, username=username, password=password)
    print("connected successfully!")
except Exception as e:
    print("Connection error", e)

'''
sftp.get(remotepath,localpath)
sftp.put(localpath,remotepath)
'''

sftp = ssh.open_sftp()
sftp.put(" ",
         " ")

sftp.close()
print("copied successfully!")

ssh.close()



