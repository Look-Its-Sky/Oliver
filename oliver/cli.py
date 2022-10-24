import os
import platform

#CLI Interface
if platform.system() != "Linux":
    ans = input("You are running on " + platform.system() + ". \nThis OS may not support or function well with this script. \nIf you think this is a mistake then press enter to continue.")

while True:
    cmd = input("Oliver: ")
    
    #Help
    if cmd == "help":
        print("Use the keyword bash to access bash shell \n Or type an Oliver command")

    #Bash Shell
    elif cmd == "bash":
        while True:
            cmd = input("$ ")

            if cmd == "exit":
                break

            else:
                os.system(cmd.split("$")[0])
    
    elif cmd == "exit":
        print("See You Later!")
        exit()

    elif cmd == "clear":
        os.system("clear")

    #Regular Oliver Shell
    else:
        os.system("python3 ./interpeter.py " + cmd)