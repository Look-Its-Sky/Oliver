import os

#Copying
try:
    os.system("cp ../../oliver/ ../../oliver_backup/")
    
except:
    print("Exception Occurred \n Copying Stopped \n Stopping Execution")
    exit()

else:
    print("Backup Complete")