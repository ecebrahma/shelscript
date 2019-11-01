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
        #print(pwd)
        dir_path=pwd+'Copy.ps1'
        #print(dir_path)
        #newfile = dir_path.replace('.ps1', '.txt')
        print('--------------------------------------------')
        #print(newfile)
        getdata=None
        with open("/opt/stackstorm/packs/shelscript/actions/file.ps1", 'rb') as f:
            getdata = f.read()
            print (getdata)

        getdata=getdata.replace("'\'", "")
       
        #s = winrm.Session('172.16.2.33', auth=('abhishekb@nihilentanalytics.com', 'M1cr7123'), transport='ntlm')
        s = winrm.Session('172.16.3.203', auth=('administrator@gso.internal', 'C1sc0@123'), transport='ntlm')
        print('--------------------------------------------')
        #r = s.run_cmd('ipconfig', ['/all'])
        r = s.run_ps(getdata,'HELLO', 'WORLD')
        print(r.std_out)

        print('--------------------------------------------')
        print('--------------------------------------------')
        #print (getdata)
        
        print ('/////////////////////////////////////')
         

        print ('/////////////////////////////////////')
        