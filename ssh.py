# -*- coding: UTF-8 -*-
import paramiko


class sshOpen:
    def __init__(self):
        pass
    def sshcon(self,taghost,tagport = 22,taguser = 'root',tagpassword = 'smnra000',tagcmd = 'ls -l'):
        self.ssh = paramiko.SSHClient()  #����SSH����
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())   #��Ҫ���ӵĻ�����ӵ�known_hosts�ļ���
        self.ssh.connect(hostname = taghost, port = tagport, username = taguser, password = tagpassword) #���ӷ�����
        self.stdin, self.stdout, self.stderr = self.ssh.exec_command(tagcmd) #ִ���������
        self.result = self.stdout.read()
        if not self.result:
            self.result = self.stderr.read()
        self.ssh.close()
        return self.result.decode()


def sshOpenFunc(taghost,tagport = 22,taguser = 'root',tagpassword = 'smnra000',tagcmd = 'ls -l'):
    ssh = paramiko.SSHClient()  #����SSH����
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())   #��Ҫ���ӵĻ�����ӵ�known_hosts�ļ���
    ssh.connect(hostname = taghost, port = tagport, username = taguser, password = tagpassword) #���ӷ�����
    #tagcmd = 'ls -l;ifconfig' #���������;����
    stdin, stdout, stderr = ssh.exec_command(tagcmd) #ִ���������
    result = stdout.read()
    if not result:
        result = stderr.read()
    ssh.close()
    #print(result.decode())
    return result.decode()
    
if __name__ == '__main__':
    print(sshOpenFunc('10.100.162.115',22,'richuser','richr00t',"netstat -an|awk '{print $4}' | grep ':21$'"))