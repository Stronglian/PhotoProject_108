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
 - [VideoWriter::VideoWriter - cv2](https://docs.opencv.org/2.4/modules/highgui/doc/reading_and_writing_images_and_video.html#videowriter-videowriter)
"""

import numpy as np
import os, cv2
import imageio

#%%

def ResizeFolderImg(imgNameList, imgFolder, cols_n = 800, tmpFolder = "./TMP/"):
    """ """
    if not os.path.isdir(tmpFolder):
        os.mkdir(tmpFolder)
    img = cv2.imread(imgFolder + imgNameList[0])
    rows, cols = img.shape[:2]
    rows_n = rows * cols_n // cols
    for filename in imgNameList:
        img = cv2.imread(imgFolder + filename)
        img = cv2.resize(img, (cols_n, rows_n))
        cv2.imwrite(tmpFolder + filename, img)
    del img
    return

def MakeForderImgToGif(imgNameList = None, imgFolder = None, outputFolder = "./", tmpFolder = "./TMP/", boolResize = False):
    """ """
#    print(imgFolder.rsplit('/',1))
    # name sort
    if (imgNameList is None) :
        assert (not imgFolder is None), "ERROR"
        imgNameList = np.array(os.listdir(imgFolder))
        imgNameList = imgNameList[np.argsort([int(na.split(".")[0]) for na in imgNameList ], axis = 0)]
        
    if boolResize:
        ResizeFolderImg(imgNameList, imgFolder, tmpFolder = tmpFolder)
        imgFolder = tmpFolder
    # 
    with imageio.get_writer(outputFolder + 'output.gif', mode = 'I') as writer:
        for filename in imgNameList:
            image = imageio.imread(imgFolder + filename)
            writer.append_data(image)
    if boolResize and False:
        CleanGifFolder(tmpFolder)
    return

def CleanGifFolder(imgFolder):
    """ """
    imgNameList = np.array(os.listdir(imgFolder))
    for na in imgNameList:
        os.remove(imgFolder + "/" + na)
    os.removedirs(imgFolder)
    return
#%%
def MakeForderImgToMP4(imgNameList, imgFolder, outputFolder = "./", tmpFolder = "./TMP/", boolResize = False):
    """ """
    if boolResize:
        ResizeFolderImg(imgNameList, imgFolder, tmpFolder = tmpFolder)
        imgFolder = tmpFolder
    
    return
#%%
#if __name__ == "__main__":
#    print("1")