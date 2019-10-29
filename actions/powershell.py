import sys
import subprocess
from st2common.runners.base_action import Action
import ssl
import os
import codecs
import winrm
class MyAction(Action):
    def run(self):
        #p = subprocess.Popen(['powershell.exe', 'C:\\temp\\first.ps1'], stdout=sys.stdout)
        print('test')
        #dir_path = os.path.dirname(os.path.realpath("home"))
        #print(dir_path)
        pwd = os.path.dirname(__file__)
        print(pwd)
        dir_path=pwd+'Copy.ps1'
        print(dir_path)
        #newfile = dir_path.replace('.ps1', '.txt')
        print('--------------------------------------------')
        #print(newfile)
        getdata=None
        # with open("/opt/stackstorm/packs/shelscript/actions/Copy.ps1", 'rb') as f:
        #     getdata = f.read()
        #     print (getdata)
        # file1=codecs.open("/opt/stackstorm/packs/shelscript/actions/Copy.ps1",'r')
        # getdata = file1.readlines()
        # print (getdata)
        # for x in getdata:
        #    print(x.decode('utf-8'))
        f = codecs.open("/opt/stackstorm/packs/shelscript/actions/Copy.ps1", 'r', decode='utf-8')
        lines = f.readlines()
        print (lines)
        f.close()
        #s = winrm.Session('172.16.2.33', auth=('abhishekb@nihilentanalytics.com', 'M1cr7123'), transport='ntlm')
        #r = s.run_cmd('ipconfig', ['/all'])
       #r = s.run_ps(getdata)
        #print(r.std_out)
        #file1=open("/opt/stackstorm/packs/shelscript/actions/Copy.ps1","r")
        
        #file1=codecs.open(dir_path,'r')
        #file1 = codecs.open(dir_path, 'r',encoding=sys.getfilesystemencoding())
        #getdata = file1.read()
        #getdata = file1.read()
        #getdata=getdata.decode('base64', 'strict') 
        #lines[line_num] = text
        #f.close()
        # file1 = open(dir_path,"r") 
        #getdata=file1.read()
        print('--------------------------------------------')
        #print (getdata)
        
        print ('/////////////////////////////////////')
        # for root, dirs, files in os.walk("home"):
        #     for file in files:
        #         if file.endswith("."):
        #             print(os.path.join(root, file))  

        print ('/////////////////////////////////////')
        