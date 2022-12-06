import sys, os
from subprocess import call

valid_commands = ['-r', '--remove', '-a', '--add']

def printHelp():
    pass

if any(i in sys.argv[1] for i in valid_commands):

    path = sys.argv[2]
    
    '''use init.py as install script'''
    if any(ii in sys.argv[1] for ii in ['-a', '--add']):
        print("Process returned with code ", call(path + "/init.py"))

    '''use deinit.py as uninstall script'''
    if any(ii in sys.argv[1] for ii in ['-r', '--remove']):
        print("Process returned with code ", call(path + "/deinit.py"))

else:
    printHelp()

'''
file struct:
    <root>
    init.py -- for installing
    deinit.py -- for uninstalling
        resources:
            <whatever resources are referenced>
'''
