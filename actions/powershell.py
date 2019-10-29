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
        #file1=open(dir_path,"r") 
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
        #Open the file back and read the contents
        f=open(dir_path, "r")
        if f.mode == 'r': 
            contents =f.read()
            print contents
        #or, readlines reads the individual line into a list
        fl =f.readlines()
        for x in fl:
            print x
        

        print ('/////////////////////////////////////')
        