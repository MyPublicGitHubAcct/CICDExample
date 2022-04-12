'''
This script will build this project. CMake must have already been run.
This script takes an (optional) argument - either 'd' for Debug or 'r' for Release.
If this is run without an argument, a Debug build will be done.

To run, use like 'python3 scripts/build.py d'.
'''

import os
import platform
import sys

# collect needed information
platform_name = platform.system()
platform_release = platform.release()
current_path = os.getcwd()

try:
    f = open(current_path + "/_builds/cmakeprojecttype.txt", "r")
    build_type = f.read()
except:
    build_type = 'Debug'
    raise Exception(
        'Something is wrong with project type. Running tests expecting Debug.')

# define requested build type - if not entered, do Debug
try:
    bt = sys.argv[1]
except:
    bt = 'd'

if bt == 'r':
    requested_build_type = 'Release'
else:
    requested_build_type = 'Debug'

########################### do the builds ###########################
try:
    os.system('cls' if os.name == 'nt' else 'clear')

    print('Building (' + requested_build_type + ') all build files in ' + current_path +
          ' for ' + platform_name + " " + platform_release)

    if(platform_name == 'Darwin'):
        try:
            cmd = 'cmake --build _builds --config ' + requested_build_type
            os.system(cmd)
        except OSError as e:
            print("Error: %s : %s" % (cmd, e.strerror))
            sys.exit(1)

    elif(platform_name == 'Linux'):
        try:
            if build_type == requested_build_type:
                cmd = 'cmake --build _builds'
                os.system(cmd)
            else:
                raise ValueError(
                    'Build type requested does not match what CMake built.')
        except OSError as e:
            print("Error: %s : %s" % (cmd, e.strerror))
            sys.exit(1)

    elif(platform_name == 'Windows'):
        try:
            if build_type == requested_build_type:
                cmd = 'cmake --build _builds'
                os.system(cmd)
            else:
                raise ValueError(
                    'Build type requested does not match what CMake built.')
        except OSError as e:
            print("Error: %s : %s" % (cmd, e.strerror))
            sys.exit(1)
    else:
        raise ValueError('Operating system not recognized by build script.')

    print('Building has completed.')
    sys.exit(0)

except OSError as e:
    print("Error: %s" % (e.strerror))
    sys.exit(1)
except Exception as e:
    print("Error: %s" % (e.strerror))
    sys.exit(1)
