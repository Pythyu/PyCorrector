from FileExplorer import *
import shutil

forbidden_keywords = ["import os","import sys","import subprocess", "from os", "from sys", "from subprocess"]


def CheckFile(filePath):
    file = open(filePath, "r", encoding='utf-8')
    txt = file.read()
    file.close()
    return any(keyword in txt for keyword in forbidden_keywords)

def QuarantineFolder(name, path,QuarantinePath):
    shutil.move(path,join(QuarantinePath, name))

def RecursiveTreeCheck(directory):
    for content in get_content(directory):
        if content[0] == "_" and content[1] == "_":
            continue
        path = join(directory, content)
        if isdir(path):
            RecursiveTreeCheck(path)
        elif "py" in splitext(content)[1]:
            if CheckFile(path):
                QuarantineFolder(directory.split("/")[-1], directory, "./Quarantine")
                break




#QuarantineFolder("loopStudent", "./studentFiles/loopStudent", "./Quarantine")
