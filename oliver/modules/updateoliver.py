import os

#Asks if any third party modules are installed
while True:
    ismergeneeded = input("Does the modules.txt have any third party modules referenced? (y/n)")

    if ismergeneeded != "y" or ismergeneeded != "n":
        print("Invalid input")

    else:
        break

#TODO: Implement Merging
if ismergeneeded == "y":
    print("Not Supported Yet....")

#No Merge Update
if ismergeneeded == "n":
    print("Making Backups......")

    #Copying
    try:
        os.system("cp ../../oliver/ ../../oliver_backup/")
    
    except:
        print("Exception Occurred \n Copying Stopped \n Stopping Execution")
        exit()

    else:
        print("Backup Complete")