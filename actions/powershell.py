import sys
import subprocess
from st2common.runners.base_action import Action
import ssl
import os
import codecs
class MyAction(Action):
    def run(self):
        #p = subprocess.Popen(['powershell.exe', 'C:\\temp\\first.ps1'], stdout=sys.stdout)
        print('test')
        #dir_path = os.path.dirname(os.path.realpath("home"))
        #print(dir_path)
        pwd = os.path.dirname(__file__)
        print(pwd)
        dir_path=pwd+'/Copy.ps1'
        print(dir_path)
        #newfile = dir_path.replace('.ps1', '.txt')
        print('--------------------------------------------')
        #print(newfile)
        file1=codecs.utf_8_decode(dir_path.encode('utf8'))
        file1=codecs.open(file1)
        #file1 = codecs.open(dir_path, 'r',encoding=sys.getfilesystemencoding())
        #getdata = file1.read()
        getdata = file1.read()
        #getdata=getdata.decode('base64', 'strict') 
        #lines[line_num] = text
        #f.close()
        # file1 = open(dir_path,"r") 
        #getdata=file1.read()
        print('--------------------------------------------')
        print (getdata)
        
        print ('/////////////////////////////////////')
        # for root, dirs, files in os.walk("home"):
        #     for file in files:
        #         if file.endswith("."):
        #             print(os.path.join(root, file))  

        print ('/////////////////////////////////////')
        