import sys
import subprocess
from st2common.runners.base_action import Action
import ssl
import os

class MyAction(Action):
    def run(self):
        #p = subprocess.Popen(['powershell.exe', 'C:\\temp\\first.ps1'], stdout=sys.stdout)
        print('test')
        #dir_path = os.path.dirname(os.path.realpath("home"))
        #print(dir_path)
        pwd = os.path.dirname(__file__)
        print(pwd)
        dir_path=pwd+'/copy.ps1'
        print(dir_path)
        newfile = dir_path.replace('.ps1', '.txt')
        print('--------------------------------------------')
        print(newfile)
        file1 = open(newfile,"r") 
        getdata=file1.read()
        print('--------------------------------------------')
        print (getdata)
        print(dir_path)
        for x in os.listdir(pwd):
            print x
            # try:
            #     for y in os.listdir(x):
            #         print(y)
            # except Exception as e:
            #     return(False,e)
        print ('/////////////////////////////////////')
        # for root, dirs, files in os.walk("home"):
        #     for file in files:
        #         if file.endswith("."):
        #             print(os.path.join(root, file))  

        print ('/////////////////////////////////////')
        # dirpath = os.getcwd()
        # print("current directory is : " + dirpath)
        # foldername = os.path.basename(dirpath)
        # print("Directory name is : " + foldername)
        # dir_path = os.path.dirname(os.path.realpath('copy.ps1'))
        # print(dir_path)
        # dir_path=dir_path+'\copy.ps1'
        # newfile = dir_path.replace('.ps1', '.txt')
        # print('--------------------------------------------')
        # print(newfile)
        # file1 = open(newfile,"r") 
        # getdata=file1.read()
        # print('--------------------------------------------')
        # print (getdata)
        # print(dir_path)