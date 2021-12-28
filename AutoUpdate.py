import subprocess
import time
import os
import sys

def do_execv():
    """Re-execute the current process.

    This must be called from the main thread, because certain platforms
    (OS X) don't allow execv to be called in a child thread very well.
    """
    args = sys.argv[:]
    print('Re-spawning %s' % ' '.join(args))
    args.insert(0, sys.executable)
    if sys.platform == 'win32':
        args = ['"%s"' % arg for arg in args]
        
    os.chdir(_startup_cwd)
    os.execv(sys.executable, args)

def CheckUpdate():
    try:
        print("AutoUpdate : check if a new version is available...\n")
        process = subprocess.Popen(["git", "pull"], stdout=subprocess.PIPE)
        print(str(process.communicate()[0]))
        print("\n#####################################\n")
        return True
    except Exception as e:
        print("An error occured while updating the application...\nReason :")
        print(e)
        return False
