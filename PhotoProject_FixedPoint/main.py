# -*- coding: utf-8 -*-
"""
Created on Sat Jan 19 23:20:42 2019
@author: Strong
"""
"""
Probelm:
    1. 凌晨應該接到晚上之後
    2. 黃昏之時，無法用時間排序
    3. 光亮排序不知道該用什麼排，HSV 不甚理想，大概要反算白平衡
    
"""
import os, cv2
import numpy as np

from c1_makeGIF import *
from c2_readFileInfo import *
from c3_sortImgTime import *

if __name__ == "__main__":
    import time
    _start_time = time.time()
    # 讀取資料
    ## 設置目錄
    strSaveFolder = "./"
#    strDataFolder = SelectDirectory() #要避開中文、特殊符號
    strDataFolder = "E:/_Pictures/PHOTO_TMP/" 
    ## 讀取圖片資料 - 名稱、時間
    dictData = MakeInfoTable_time(strDataFolder)
    
    # 處理資料
    ## 依照時間排序照片
    arrImgName, argIdx = SortImgDataByTime(dictData, infoHeader = ["name", "hour", "minute", "light"])
#    print(arrImgName[argIdx])    
    ## 顯示
    for na in arrImgName[argIdx]:
        img = cv2.imread(strDataFolder + na)
        img = cv2.resize(img, (800, 600))
        cv2.imshow("SHOW", img)
        cv2.waitKey(50)
    cv2.destroyAllWindows()
    
    # 輸出資料
    ## 製作GIF # 檔案好大
    MakeForderImgToGif(arrImgName[argIdx], imgFolder = strDataFolder, boolResize = True)
    ## 製作MP4
    MakeForderImgToMP4(arrImgName[argIdx], imgFolder = strDataFolder, boolResize = True)
    
    _end_time = time.time()
    print("\n\nIt cost %.4f sec."%( _end_time - _start_time))