import sys
from st2common.runners.base_action import Action
import ssl
import os
import paramiko
class MyAction(Action):
    def run(self,shell_param):
         #pwd = os.path.dirname(os.path.realpath('test.sh'))
        pwd = os.path.dirname(__file__)
        #print(pwd)
        dir_path=pwd+"/test.sh"
        #print(dir_path)
        #print(dir_path)
        user='ssadmin@vnext.nihilentanalytics.com'
        host='192.168.0.4' 
        password='C1sc0@12345!@#$%'
        command=dir_path
        #os.system('ssh ssadmin@192.168.0.4  bash < echo Hello World!)) >> D:/abhishek/Qsuper/call_to_pwss/code/copy.txt 2>&1')

        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        getdata=None
        client.connect('192.168.0.4', username='ssadmin', password='C1sc0@12345!@#$%')
        with open(dir_path, 'rb') as f:
            getdata = f.read()
            #print (getdata)
        getdata1=getdata.decode("utf-8")
        #print(getdata1)
        checkfile=getdata1.format(shell_param)
        print(checkfile)
        stdin, stdout, stderr = client.exec_command(checkfile)
        print(stdout)
        #print("############################")
        print(stderr)
        #print("******************************")
        print(stdin)
        #print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")



        for line in stdout:
            print (line.strip('\n'))

        client.close()