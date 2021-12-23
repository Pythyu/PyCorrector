import zipfile
import os
import tarfile
from pyunpack import Archive



class Decompressor:
    def __init__(self, path, outpath):
        self.path = path
        self.outpath = outpath
        if not os.path.exists(self.outpath):
            os.makedirs(self.outpath)
        self.filename, self.file_extension = os.path.splitext(path)

    def extract(self):
        if "zip" in self.file_extension:
            self.zip_extract()
        elif "7z" in self.file_extension:
            self.zip7_extract()
        elif "tar.gz" in self.file_extension or "tgz" in self.file_extension or "gz" in self.file_extension:
            self.tar_extract()
        else:
            print("File at %s couldn't be extracted ! Be sure to use either Zip, Tar or 7z format for your compressed files" % (path))


    def zip_extract(self):
        with zipfile.ZipFile(self.path, 'r') as zip_ref:
            zip_ref.extractall("./%s" % (self.outpath))

    def tar_extract(self):
        my_tar = tarfile.open(self.path)
        my_tar.extractall("./%s" % (self.outpath))
        my_tar.close()

    def zip7_extract(self):
        Archive(self.path).extractall("./%s" % (self.outpath))
