import os, sys, glob

if sys.argv[1] == "--fix-permissions":
    os.system("chmod +x modules/*")

for i in glob.glob("modules/"):
    if i == sys.argv[1]:
        ending = str(i).split('.')[1]

        if ending == '.py':
            os.system("python3 ", i)

        else:
            call(i)

    else:
        print("Command Not Found")