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
 - [Getting Started with Videos - Saving a Video](https://docs.opencv.org/3.1.0/dd/d43/tutorial_py_video_display.html)
 - [OpenCV 擷取網路攝影機串流影像，處理並寫入影片檔案教學 - G. T. Wang](https://blog.gtwang.org/programming/opencv-webcam-video-capture-and-file-write-tutorial/)
"""

import numpy as np
import os, cv2
import imageio

BOOL_CLEAN_TMP = True
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
    return (rows_n, cols_n)

def MakeForderImgToGif(imgNameList = None, imgFolder = None, outputFolder = "./", tmpFolder = "./TMP/", boolResize = False, cols_n = 800):
    """ """
#    print(imgFolder.rsplit('/',1))
    # name sort
    if (imgNameList is None) :
        assert (not imgFolder is None), "ERROR"
        imgNameList = np.array(os.listdir(imgFolder))
        imgNameList = imgNameList[np.argsort([int(na.split(".")[0]) for na in imgNameList ], axis = 0)]
        
    if boolResize:
        ResizeFolderImg(imgNameList, imgFolder, cols_n = 800, tmpFolder = tmpFolder);
        imgFolder = tmpFolder
    # 
    with imageio.get_writer(outputFolder + 'output.gif', mode = 'I') as writer:
        for filename in imgNameList:
            image = imageio.imread(imgFolder + filename)
            writer.append_data(image)
    if boolResize and BOOL_CLEAN_TMP:
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
def MakeForderImgToMP4(imgNameList, imgFolder, outputName = 'output.mp4', fps = 4.0, outputFolder = "./", tmpFolder = "./TMP/", boolResize = False, cols_n = 800):
    """ """
    if not outputName.rsplit(".", 1)[1] in ["mp4", "avi"]:
        outputName += ".mp4"
    rows, cols = 640, 480
    if boolResize:
        rows, cols = ResizeFolderImg(imgNameList, imgFolder, cols_n = 800, tmpFolder = tmpFolder)
        imgFolder = tmpFolder
    # 設置
    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'MJPG')
    out = cv2.VideoWriter(outputName, fourcc, fps, (cols, rows))
    # 紀錄
    for filename in imgNameList:
        img = cv2.imread(imgFolder + filename)
#        img = cv2.flip(img,0)
        out.write(img)
    # 釋放與清除
    out.release()
    if boolResize and BOOL_CLEAN_TMP:
        CleanGifFolder(tmpFolder)
    return
#%%
#if __name__ == "__main__":
#    print("1")