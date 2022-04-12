'''
This script will remove the _builds directory and all of its contents.

On mac, this will also remove the built files and test output that is stored
in the user audio directory.

To run, use like 'python3 scripts/clean.py'.
'''

import os
import platform
import sys
import shutil
from pathlib import Path

# collect needed information
platform_name = platform.system()
platform_release = platform.release()
current_path = os.getcwd()
home_path = str(Path.home())
python_version = 'python3'  # expect python3
pv = sys.version  # captures the python version number (2 or 3)
if pv.startswith('2.'):
    python_version = 'python'

try:
    os.system('cls' if os.name == 'nt' else 'clear')

    cmd = "echo 'Removing _builds '"
    os.system(cmd)

    if(platform_name == 'Darwin'):
        print('CLEAN STATUS removing the _builds folder')
        dir_path = current_path + '/_builds'
        isdir = os.path.isdir(dir_path)
        if isdir == True:
            try:
                shutil.rmtree(dir_path)
            except OSError as e:
                print("Error: %s : %s" % (dir_path, e.strerror))
                sys.exit(1)

    elif(platform_name == 'Linux'):
        print('CLEAN STATUS removing the _builds folder')
        dir_path = current_path + '/_builds'
        isdir = os.path.isdir(dir_path)
        if isdir == True:
            try:
                shutil.rmtree(dir_path)
            except OSError as e:
                print("Error: %s : %s" % (dir_path, e.strerror))
                sys.exit(1)

    elif(platform_name == 'Windows'):
        print('CLEAN STATUS removing the _builds folder')
        dir_path = current_path + '/_builds'
        isdir = os.path.isdir(dir_path)
        if isdir == True:
            try:
                shutil.rmtree(dir_path)
            except OSError as e:
                print("Error: %s : %s" % (dir_path, e.strerror))
                sys.exit(1)

    else:
        raise ValueError(
            'Operating system not recognized by clean.py script.')

    cmd = "echo 'The _builds directory has been removed.'"
    os.system(cmd)
    sys.exit(0)

except OSError as e:
    print("Error: %s : %s" % (cmd, e.strerror))
    sys.exit(1)
