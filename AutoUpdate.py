import subprocess
import time

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
