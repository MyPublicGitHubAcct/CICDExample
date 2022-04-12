
def logcmd(current_path, cmd):
    '''
    Creates and appends a file to log which tests were run.
    Used by tests.py.
    '''
    f2 = open(current_path + '/_builds/tests_run.txt', 'a')
    f2.write('\n' + cmd + '\n')
    f2.close()
