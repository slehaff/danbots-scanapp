import datetime
import time
#import scancam
from io import BytesIO, open
from shutil import copyfileobj, copyfile
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
    """ filename decide the type of the file """
    if not WINDOWS:
        camera.capture(filename)
    return True

def take_fd(format='jpeg'):
    if not WINDOWS:
        fd = BytesIO()
        camera.capture(fd, format=format)
    return fd

def speed_fd():
    if not WINDOWS:
        fd = BytesIO()
        camera.capture(fd, format='jpeg', use_video_port=True)
    return fd

def ScanFileSet(antal=1):
    time.sleep(camera_init_time)
    i = 1
    filelist =[]
    while i<=antal:
        filename =FOLDER + FILENAME + str(i) + FILETYPE
        take_pic(filename)
        filelist.append(filename)
        time.sleep(picture_interval_time)
        i += 1
    return filelist

def ScanMemSet(antal=1, format='jpeg'):
    time.sleep(camera_init_time)
    i = 1
    filelist =[]
    while i<=antal:
        if not WINDOWS: 
            #fd = take_fd(format=format)
            fd = speed_fd()
        filelist.append(fd)
        time.sleep(picture_interval_time)
        i += 1
    return filelist

def ScanContMemSet(antal=10, format='jpeg', flash=None):
    time.sleep(camera_init_time)
    j = 1
    filelist = []
    stream = BytesIO()
    #if flash : flash(j)
    for i in enumerate(camera.capture_continuous(stream, format='jpeg', use_video_port=True)):
        j = j+1    
        #if flash : flash(j)    
        stream.truncate()
        stream.seek(0)
        fd = BytesIO()
        copyfileobj(stream, fd)
        filelist.append(fd)
        stream.seek(0)
        stream.truncate(0)

        if j>antal:
            #if flash : flash(0)
            break;
    return filelist
