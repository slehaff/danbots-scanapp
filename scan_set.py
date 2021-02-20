import datetime
import time
#import scancam
from io import BytesIO
from config import DEBUG, WINDOWS, config

################
# this class implement a standard picture scan 
#
# this include 3 picture
# f1: normal
# f2: grayscale
# f3 solarized
#
SCAN_PICTURE='scan_picture'
scanpicture = config[SCAN_PICTURE]
camera_init_time = scanpicture.getfloat('camera_init_time', 12)
picture_interval_time = scanpicture.getfloat('picture_interval_time', 5)

FOLDER = "/tmp/"
FILENAME = "file"
FILETYPE = ".jpg"

if not WINDOWS:
    from picamera import PiCamera  # pylint: disable=unresolved-import
    camera = PiCamera()
else:
    FOLDER = 'data/'

def take_pic(filename):
    if not WINDOWS:
        camera.capture(filename)
    return True

def take_fd():
    if not WINDOWS:
        fd = BytesIO()
        camera.capture(fd, format='jpeg')
    return fd

def ScanFileSet(antal=2):
    time.sleep(camera_init_time)
    i = 1
    filelist =[]
    while i<=antal:
        filename =FOLDER + FILENAME + str(i) + FILETYPE
        if not WINDOWS: take_pic(filename)
        filelist.append(filename)
        time.sleep(picture_interval_time)
        i += 1
    return filelist

def ScanMemSet(antal=1):
    time.sleep(camera_init_time)
    i = 1
    filelist =[]
    while i<=antal:
        #print (datetime.datetime.now().time())
        if not WINDOWS: 
            fd = take_fd()
        filelist.append(fd)
        time.sleep(picture_interval_time)
        i += 1
    #print (datetime.datetime.now().time())
    return filelist

# class Scanner:
#     f1 = BytesIO()
#     f2 = BytesIO()
#     f3 = BytesIO()
#     cam = scancam.scancamera()
#     cam.set_scan_pic()

#     def Pic1Setup():
#         pass

#     def ScanSet(self):
#         self.cam.color_effects(None)
#         self.f1.seek(0)
#         self.cam.take_stream(self.f1)
#         self.cam.color_effects((127,127))
#         self.f2.seek(0)
#         self.cam.take_stream(self.f2)
#         self.f3.seek(0)
#         self.cam.take_stream(self.f3)

##my = Scanner()
#y.ScanSet()
#print("F1:", my.f1)

