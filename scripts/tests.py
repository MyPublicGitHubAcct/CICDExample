'''
This script will run unit tests for this project.
For this to work, both executables, the HelloWorld application *and* the
test application need to be built prior to this script being run.

To perform testing, use 'python3 scripts/tests.py'.
'''

import os
import platform
import sys
from pathlib import Path
from functions import logcmd


def run_tests(path):
    ''' script runner, takes current_path '''
    unit_test_file_paths = []
    for root, dir, files in os.walk(path):
        for file_name in files:
            if file_name == 'HelloWorld' + '_tests':
                unit_test_file_paths.append(os.path.join(
                    path, root, file_name))

    for cmd in unit_test_file_paths:
        try:
            os.system(cmd)
            logcmd(path, cmd)
        except OSError as e:
            print("Error: %s" % (e.strerror))
            sys.exit(1)


#################### collect needed information #####################
platform_name = platform.system()  # like Darwin, Linux, or Windows
platform_release = platform.release()  # like 19.6.0, etc.
current_path = os.getcwd()
home_path = str(Path.home())
python_version = 'python3'  # expect python3
pv = sys.version  # captures the python version number (2.x or 3.x)
if pv.startswith('2.'):
    python_version = 'python'

# Get the build type, which was defined when cmake was run.
try:
    f = open(current_path + '/_builds/cmakeprojecttype.txt', 'r')
    build_type = f.read()
except:
    build_type = 'Debug'
    raise Exception(
        'Something is wrong with project type. These tests should be run again a Debug build.')

########################### do the tests ############################
print('Testing is starting')
print("")

try:
    os.system('cls' if os.name == 'nt' else 'clear')

    # crawl the directory to find the tests file(s)
    if(platform_name == 'Darwin'):
        logcmd(current_path, 'Start Darwin Validation\n')
        run_tests(current_path)

    elif(platform_name == 'Linux'):
        logcmd(current_path, 'Start Linux Validation\n')
        run_tests(current_path)

    elif(platform_name == 'Windows'):
        logcmd(current_path, 'Start Windows Validation\n')
        run_tests(current_path)

    else:
        raise ValueError('Operating system not recognized by tests.py script.')

except OSError as e:
    print("Error: %s" % (e.strerror))
    sys.exit(1)
except Exception as e:
    print("Error: %s" % (e.strerror))
    sys.exit(1)
