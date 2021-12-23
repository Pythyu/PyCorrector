from os import listdir
from os.path import isfile, isdir, join, splitext
import glob

def get_content(directory):
    return [f for f in listdir(directory)]

def get_folders(directory):
    return [f for f in listdir(directory) if isdir(join(directory, f))]

def get_files(directory):
    return [f for f in listdir(directory) if isfile(join(directory, f))]

def get_files_with_extension(directory, extent):
    return [f for f in listdir(directory) if isfile(join(directory, f)) and extent in splitext(f)[1]]

def clean_folder_content(directory):
    files = glob.glob('%s/*' % (directory))
    for f in files:
        os.remove(f)
