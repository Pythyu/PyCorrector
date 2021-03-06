from os import listdir
import shutil
from os.path import isfile, isdir, join, splitext
import glob

def underscore_format(string):
    return string.split("_")[0]


def get_content(directory):
    """
    Get all content of the specified directory
    """
    return [f for f in listdir(directory)]

def get_folders(directory):
    """
    Get all folders in the specified directory
    """
    return [f for f in listdir(directory) if isdir(join(directory, f))]

def get_files(directory):
    """
    Get all files in the specified directory
    """
    return [f for f in listdir(directory) if isfile(join(directory, f))]

def get_files_with_extension(directory, extent):
    """
    Get all files with a specific extension in the specified directory
    """
    return [f for f in listdir(directory) if isfile(join(directory, f)) and extent in splitext(f)[1]]

def clean_folder_content(directory):
    """
    Remove all non-hidden files from the specified directory
    """
    files = glob.glob('%s/*' % (directory))
    for f in files:
        shutil.rmtree(f)
