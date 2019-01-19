# -*- coding: utf-8 -*-
"""
Created on Sun Jan 20 00:59:27 2019
@author: Strong
"""
"""
1. [numpy.concatenate](https://docs.scipy.org/doc/numpy/reference/generated/numpy.concatenate.html)
2. [numpy.argsort](https://docs.scipy.org/doc/numpy-1.15.0/reference/generated/numpy.argsort.html)
"""
import numpy as np
from c2_readFileInfo import *

def SortImgDataByTime(dictData, infoHeader = ["name", "hour", "minute"]):
    # 檔名
    arrImgName = np.array(list(dictData.keys()))
    # TO ARRAY
    for i, na in enumerate(arrImgName):
#        tmp = np.array([[dictData[na]["hour"], dictData[na]["minute"]]], dtype = np.int8)
        tmp = np.array([[dictData[na][label] for label in infoHeader[1:]]], dtype = np.int8)
        if i == 0: 
            arrTime = tmp.copy()
        else:
            arrTime = np.concatenate((arrTime, tmp), axis = 0)
    # SORT
    argIdx = arrTime.argsort(axis = 0)
    return arrImgName, argIdx[:, 0]

#    # 轉製作成 LIST - 檔名、時、分
#    infoHeader = ["name", "hour", "minute"]
#    arrImgName = np.array(list(dictData.keys()))
#    
#    for i, na in enumerate(arrImgName):
##        print(i, na)
##        tmp = np.array([[int(dictData[na]["hour"]), int(dictData[na]["minute"])]])
##        tmp = (int(dictData[na]["hour"]), int(dictData[na]["minute"]))
#        tmp = np.array([[dictData[na]["hour"], dictData[na]["minute"]]], dtype = np.int8)
#        if i == 0: 
#            arrTime = tmp.copy()
#        else:
#            arrTime = np.concatenate((arrTime, tmp), axis = 0)
##    arrTime1 = np.array(arrTime, dtype=[('hour', '<i4'), ('minute', '<i4')])
#    # 排序 早0-
#    tmp = arrTime.argsort(axis = 0)
#    print(arrTime[tmp[:, 0]])
    
# 排序 - 光亮
def SortImgDataByLight(dictData, infoHeader = ["name", "light"]):
    # 檔名
    arrImgName = np.array(list(dictData.keys()))
    # 
    arrlight = np.array([dictData[na]['light'] for na in arrImgName])
    
    argIdx = arrlight.argsort(axis = 0)
    return arrImgName, argIdx

if __name__ == "__main__":
    # 讀取設置
#    strDataFolder = SelectDirectory()
    strDataFolder = "E:/_Pictures/PHOTO_TMP/"
    dictData = MakeInfoTable_light(strDataFolder)
    
    arrImgName, argIdx = SortImgDataByLight(dictData)
    print(arrImgName[argIdx])    
    
    
    # 排序 早6-
    
    