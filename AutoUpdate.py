import subprocess
import time
import os
import sys
import socket
import shutil

def isConnected():
    try:
        # connect to the host -- tells us if the host is actually
        # reachable
        sock = socket.create_connection(("www.google.com", 80))
        if sock is not None:
            sock.close
        return True
    except OSError:
        pass
    return False

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

def config_update_saving():
    shutil.copy("./config.yaml","./tmp/config.yaml")

def config_update_restore():
    os.remove("./tmp/config.yaml")

def CheckUpdate():
    if not isConnected():
        print(bcolors.WARNING + "couldn't connect to internet... AutoUpdate Aborted...")
        return True
    try:
        config_update_saving()
        print(bcolors.OKCYAN + "AutoUpdate : check if a new version is available...\n" + bcolors.ENDC)
        p1 = subprocess.Popen(["git", "restore", "."], stdout=subprocess.PIPE)
        process = subprocess.Popen(["git", "pull"], stdout=subprocess.PIPE)
        out = str(process.communicate()[0])
        print(out)
        if 'Already up to date' not in out:
            if "config.yaml" in out:
                print("\n"+ bcolors.WARNING + "/!\\ config.yaml may have been modified /!\\")
                print("We saved the previous file at ./tmp/config.yaml !")
                print(bcolors.FAIL + " Be sure to re-edit the current config.yaml to your need to not lose any data since ./tmp/config.yaml will be deleted at the next start" + bcolors.ENDC)
            else:
                config_update_restore()
            if "requirements.txt" in out:
                print("\n"+ bcolors.WARNING + "/!\\ requirements.txt may have been modified /!\\")
                print("We recommend using again " + bcolors.UNDERLINE + "python3 -m pip install -r requirements.txt" +bcolors.ENDC)
            print(bcolors.OKGREEN + "The update is complete \\o/ : please restart the app to apply the update" + bcolors.ENDC)
            return False

        config_update_restore()
        print("\n#####################################\n")
        return True
    except Exception as e:
        print(bcolors.FAIL + "An error occured while updating the application...\nReason :")
        print(e)
        print(bcolors.ENDC)
        return False
