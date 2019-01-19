# -*- coding: utf-8 -*-
"""
Created on Sat Jan 19 20:20:54 2019
@author: Strong
"""
"""
1. [Programmatically generate video or animated GIF in Python?](https://stackoverflow.com/questions/753190/programmatically-generate-video-or-animated-gif-in-python)
2. CV2 影片
- [](https://stackoverflow.com/questions/9795601/python-jpeg-to-movie)
- [Python Code：图片和视频互相转换](https://blog.csdn.net/Errors_In_Life/article/details/72809580)
"""

import numpy as np
import os, cv2
import imageio

#%%

def MakeForderImgToGif(imgNameList = None, imgFolder = None):
#    print(imgFolder.rsplit('/',1))
    # name sort
    if (imgNameList is None) :
        assert (not imgFolder is None), "ERROR"
        imgNameList = np.array(os.listdir(imgFolder))
        imgNameList = imgNameList[np.argsort([int(na.split(".")[0]) for na in imgNameList ], axis = 0)]

    # 
    with imageio.get_writer(imgFolder + 'output.gif', mode = 'I') as writer:
        for filename in imgNameList:
            image = imageio.imread(imgFolder + "/" + filename)
            writer.append_data(image)
    return

def CleanGifFolder(imgFolder):
    imgNameList = np.array(os.listdir(imgFolder))
    for na in imgNameList:
        os.remove(imgFolder + "/" + na)
    os.removedirs(imgFolder)
    return

#%%
#if __name__ == "__main__":
#    print("1")