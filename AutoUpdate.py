import subprocess
import time
import os
import sys

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


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
        out = str(process.communicate()[0])
        print(out)
        if 'Already up to date' not in out:
            if "requirements.txt" in out:
                print("\n"+ bcolors.WARNING + "\/!\\ requirements.txt may have been modified \/!\\")
                print("We recommend using again " + bcolors.UNDERLINE + "python3 -m pip install -r requirements.txt" +bcolors.ENDC)
            print(bcolors.OKGREEN + "The update is complete \\o\/ : please restart the app to apply the update" + bcolors.ENDC)
            return False

        print("\n#####################################\n")
        return True
    except Exception as e:
        print("An error occured while updating the application...\nReason :")
        print(e)
        return False
