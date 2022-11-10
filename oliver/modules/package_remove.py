import sys, os
from subprocess import call

if not sys.argv[1]:
    #note: should prob print help
    print("Invalid Package Path")
    exit()

path = sys.argv[1]
print("Process returned with code " + call(path + "/deinit.py"))