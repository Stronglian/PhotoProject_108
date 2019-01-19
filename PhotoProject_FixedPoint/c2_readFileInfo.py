# -*- coding: utf-8 -*-
"""
Created on Sat Jan 19 20:54:33 2019
@author: Strong
"""
"""
1. [](https://self.jxtsai.info/2016/09/python-exifread-pil.html)
2.  python selet Directory
- [【Python】利用tkFileDialog打开文件对话框](https://blog.csdn.net/churximi/article/details/61198438)
- [Tkinter tkFileDialog module](https://pythonspot.com/tk-file-dialogs/)
- [How to select a directory and store the location using tkinter in Python](https://stackoverflow.com/questions/11295917/how-to-select-a-directory-and-store-the-location-using-tkinter-in-python)
"""

import os, cv2
import numpy as np

from PIL import Image
from PIL.ExifTags import TAGS #, GPSTAGS

def TimeStringToDict(inputString):
    """ format: yyyy:mm:dd hh:mm:ss """
    dictOutput = {}
    tmp = inputString.split(':')
    dictOutput["year"] = tmp[0]
    dictOutput["month"] = tmp[1]
    dictOutput["day"], dictOutput["hour"] = tmp[2].split(" ")
    dictOutput["minute"] = tmp[3]
    dictOutput["second"] = tmp[4]
    
    return dictOutput

def ReadImgTime(imgPath):
    img = Image.open(imgPath)
    info = img._getexif()
    for tag, value in info.items():
        if tag == 36867: #DateTimeOriginal
            timeDict = TimeStringToDict(value)
            break
    return timeDict

from tkinter import Tk, filedialog
def SelectDirectory():
    """ 選擇目錄 """
    root = Tk()
    root.withdraw()
    folder_selected = filedialog.askdirectory()
    return folder_selected + "/"

def MakeInfoTable_time(strFolderPath):
    dictOutput = {}
    arrImgnameList = os.listdir(strFolderPath)
    for na in arrImgnameList:
        dictOutput[na] = ReadImgTime(strFolderPath + na)
    return dictOutput

#imgFolder = 
#imgNameList = np.array(os.listdir(imgFolder))
#
##
##img = Image.open(imgFolder + imgNameList[0])
###print(img) #傳回印出該檔案的基本資料，如模式，大小，記憶體所在位置
##info = img._getexif()
##for tag, value in info.items():
##    key = TAGS.get(tag, tag)
##    if tag in [306, 36867]: # DateTime, DateTimeOriginal
##        print(key ,value)
##        print(TimeStringToDict(value))
#
#print(ReadImgTime(imgFolder + imgNameList[0]))

# 這不夠算
def CalImgLight(imgPath):
    img = cv2.imread(imgPath)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    
    return np.average(img[:, :, 2]) #V

def MakeInfoTable_light(strFolderPath):
    dictOutput = {}
    arrImgnameList = os.listdir(strFolderPath)
    for na in arrImgnameList:
        dictOutput[na] = ReadImgTime(strFolderPath + na)
        dictOutput[na]['light'] = CalImgLight(strFolderPath + na)
    return dictOutput
    
if __name__ == "__main__":
    import time
    _start_time = time.time()
    
    strDataFolder = SelectDirectory()
    dictData = MakeInfoTable_light(strDataFolder)
    
    
    _end_time = time.time()
    print("It cost %.4f sec."%( _end_time - _start_time))