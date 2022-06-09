
from pathlib import Path
import os
from warnings import catch_warnings

class FileOperation:
    __filePath = Path
    def __init__(self, path):
        self.__filePath = Path(path)
    def setFilePath(self, path):
        self.__filePath = Path(path)
    def getImgCnt(self):
        filenum = 0
        try:
            os.listdir(self.__filePath)
        except Exception:
            os.makedirs(self.__filePath)
        for lists in os.listdir(self.__filePath):
            sub_path = os.path.join(str(self.__filePath), lists)
            print(sub_path)
            if os.path.isfile(sub_path):
                filenum = filenum+1
            elif os.path.isdir(sub_path):
                dirnum = dirnum+1
            filenum -= 2
            
        return filenum
    
