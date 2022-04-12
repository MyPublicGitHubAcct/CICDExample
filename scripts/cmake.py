'''
This script will run cmake. To run, on mac, just use 'python3 scripts/cmake.py', 
which will make both debug and release builds possible.

On Linux and Windows (which use Ninja), CMake needs to be run with awareness of which
types of builds the user would like to do.

Once cmake has run, a file will be written telling which build_type is to be used during
building and testing.

To use this file, call the command like 'python scripts/cmake.py d' or 
'python scripts/cmake.py' for debug or 'python scripts/cmake.py r' for release.
'''

import os
import platform
import sys

# collect needed information
platform_name = platform.system()
platform_release = platform.release()
current_path = os.getcwd()

# choose build type - if not entered, do Debug
try:
    bt = sys.argv[1]
except:
    bt = 'd'

if bt == 'r':
    build_type = 'Release'
else:
    build_type = 'Debug'

############################# run cmake #############################

try:
    os.system('cls' if os.name == 'nt' else 'clear')

    if(platform_name == 'Darwin'):
        try:
            cmd = 'cmake -H. -B _builds -G Xcode'
            os.system(cmd)
        except OSError as e:
            print("Error: %s : %s" % (cmd, e.strerror))

    elif(platform_name == 'Linux'):
        try:
            cmd = 'cmake -H. -B _builds -G "Ninja Multi-Config" -DCMAKE_CONFIGURATION_TYPES="' + build_type + \
                '" -DCMAKE_C_COMPILER:PATH="/usr/bin/clang" -DCMAKE_CXX_COMPILER:PATH="/usr/bin/clang++"'
            os.system(cmd)
        except OSError as e:
            print("Error: %s : %s" % (cmd, e.strerror))

    elif(platform_name == 'Windows'):
        try:
            cmd = 'cmake -B _builds -G "Ninja Multi-Config" -DCMAKE_CONFIGURATION_TYPES="' + build_type + \
                '" -DCMAKE_LINKER:PATH="C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\VC\Tools\Llvm\x64\bin\lld-link.exe"'
            os.system(cmd)
        except OSError as e:
            print("Error: %s : %s" % (cmd, e.strerror))

    else:
        cmd = 'echo There was a problem running cmake.'
        os.system(cmd)

    # write a file telling build_type to be used by other scripts
    f = open(current_path + '/_builds/cmakeprojecttype.txt', "w")
    f.write(build_type)
    f.close()

    print('Completed running CMake for ' + build_type + ' in ' +
          current_path + ' for ' + platform_name + ' ' + platform_release)
    sys.exit(0)

except OSError as e:
    print("Error: %s" % (e.strerror))
    sys.exit(1)
except Exception as e:
    print("Error: %s" % (e.strerror))
    sys.exit(1)
