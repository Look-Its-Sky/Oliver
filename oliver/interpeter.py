import os
from os import path
import sys

def checkandexec(cmd):
    f = open("modules.txt", "r")

    #Only Supports Python3
    for x in f:
        if x.find(str("|" + cmd + "|")) != -1: #looks for parameter in modules.txt
            os.system("python3 " + x.split("| ")[1])#Found Line Executing Path
            f.close()
            exit()
    print("Command Not Found")

#Gives Everything execute permissions when the program is started with --fix-permissions
if sys.argv[1] == "--fix-permissions":
    os.system("chmod -R +x ./modules/")

#Otherwise it checks for the command
else:
    checkandexec(str(sys.argv[1]))