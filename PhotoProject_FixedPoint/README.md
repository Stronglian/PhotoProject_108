# 拍照點縮時 
##### - PhotoProject_FixedPoint - README.md

###### tags: `程式撰寫`

---

Probelm:
1. 凌晨應該接到晚上之後，白日到黑夜。
2. 清晨、黃昏之時，無法用時間排序。
3. 光亮排序，不知道該用什麼排，HSV 不甚理想，大概要反算白平衡。
4. **照片要重新照。**
5. 完全忘了怎麼排 sort 順序

---

# 參考資料
#### c1_makeGIF.py
1. [Programmatically generate video or animated GIF in Python?](https://stackoverflow.com/questions/753190/programmatically-generate-video-or-animated-gif-in-python)
2. CV2 影片
    - [Python JPEG to movie](https://stackoverflow.com/questions/9795601/python-jpeg-to-movie)
    - [Python Code：图片和视频互相转换](https://blog.csdn.net/Errors_In_Life/article/details/72809580)
     - [VideoWriter::VideoWriter - cv2](https://docs.opencv.org/2.4/modules/highgui/doc/reading_and_writing_images_and_video.html#videowriter-videowriter)
     - [Getting Started with Videos - Saving a Video](https://docs.opencv.org/3.1.0/dd/d43/tutorial_py_video_display.html)
     - [OpenCV 擷取網路攝影機串流影像，處理並寫入影片檔案教學 - G. T. Wang](https://blog.gtwang.org/programming/opencv-webcam-video-capture-and-file-write-tutorial/)


#### c2_readFileInfo.py
1. [python Exifread, PIL練習 抽出圖片元數據](https://self.jxtsai.info/2016/09/python-exifread-pil.html)
2.  python selet Directory
    - [【Python】利用tkFileDialog打开文件对话框](https://blog.csdn.net/churximi/article/details/61198438)
    - [Tkinter tkFileDialog module](https://pythonspot.com/tk-file-dialogs/)
    - [How to select a directory and store the location using tkinter in Python](https://stackoverflow.com/questions/11295917/how-to-select-a-directory-and-store-the-location-using-tkinter-in-python)
3. [Changing Colorspaces](https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_colorspaces/py_colorspaces.html)
    - [HSL和HSV色彩空間 - wiki](https://zh.wikipedia.org/wiki/HSL%E5%92%8CHSV%E8%89%B2%E5%BD%A9%E7%A9%BA%E9%97%B4)

#### c3_sortImgTime.py
1. [numpy.concatenate](https://docs.scipy.org/doc/numpy/reference/generated/numpy.concatenate.html)
2. [numpy.argsort](https://docs.scipy.org/doc/numpy-1.15.0/reference/generated/numpy.argsort.html)


#### other
- [從零開始學資料科學：Numpy 基礎入門](https://blog.techbridge.cc/2017/07/28/data-science-101-numpy-tutorial/)
- [6. Modules — Python 3.7.2 documentation](https://docs.python.org/3/tutorial/modules.html)
- [Python Tutorial 第二堂（3）函式、模組、類別與套件](http://www.codedata.com.tw/python/python-tutorial-the-2nd-class-3-function-module-class-package)
