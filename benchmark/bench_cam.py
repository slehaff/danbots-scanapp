#!/usr/bin/python3 
from datetime import datetime 
import time 
from io import BytesIO
from shutil import copyfileobj, copyfile
from picamera import PiCamera

SCAN_PICTURE='scan_picture'
#scanpicture = config[SCAN_PICTURE]
camera_init_time = 0.9
picture_interval_time = 0.0

FOLDER = "/tmp/"
FILENAME = "file"
FILETYPE = ".jpg"
PATH = FOLDER + FILENAME
def dummy_flash(i):
    return
    
def take_pic(filename):
    """ filename decide the type of the file """
    #camera.capture(filename, use_video_port=True, format='png')
    camera.capture(filename, use_video_port=True)
    return True

def take_fd(format='jpeg'):
    fd = BytesIO()
    camera.capture(fd, format=format)
    return fd

def speed_fd(format='jpeg'):
    fd = BytesIO()
    camera.capture(fd, format=format, use_video_port=True)
    return fd

def ScanFileSet(antal):
    i = 1
    filelist =[]
    while i<=antal:
        filename =PATH + str(i) + FILETYPE
        #camera.capture(filename)
        take_pic(filename)
        #filelist.append(filename)
        #time.sleep(picture_interval_time)
        i += 1
    return filelist

def ScanMemSet(antal=1, format='jpeg'):
    i = 1
    filelist =[]
    while i<=antal:
        fd = BytesIO()
        camera.capture(fd, format=format, use_video_port=True)

        #fd = take_fd(format=format)
        #fd = speed_fd()
        #filelist.append(fd)
        #time.sleep(picture_interval_time)
        i += 1
    return filelist

def ScanSeqFile(antal):
    i = 1
    filelist =[]
    while i<=antal:
        filename =PATH + str(i) + FILETYPE
        #take_pic(filename)
        filelist.append(filename)
        #time.sleep(picture_interval_time)
        i += 1
    camera.capture_sequence(filelist, use_video_port=True)
    return filelist


def ScanContMemSet(antal, format='jpeg', flash=None):
    j = 1
    filelist = []
    stream = BytesIO()
    if flash : flash(j)
    #for i in enumerate(camera.capture_continuous(stream, format=format, use_video_port=True)):
    for foo in camera.capture_continuous(stream, format=format, use_video_port=True):
        j = j+1    
        if flash : flash(j)    
        stream.truncate()
        stream.seek(0)
        fd = BytesIO()
        copyfileobj(stream, fd)
        filelist.append(fd)
        stream.seek(0)
        #stream.truncate(0)
        if j>antal:
            if flash : flash(0)
            break;
    return filelist

antal = 500
print("starting")
camera=PiCamera()
time.sleep(1)
print("ISO:", camera.iso)
print("Analog gain:", camera.analog_gain)
print("Digital gain:", camera.digital_gain)
print("Exposure speed:",camera.exposure_speed)
print("Shutter speed:",camera.shutter_speed)
print("Frame Rate:", camera.framerate)
start_time = datetime.now()
#ScanFileSet(antal)
#ScanSeqFile(antal)

#ScanMemSet(antal)
result = ScanContMemSet(antal, flash=dummy_flash)
#camera.resolution = (picturewidth, pictureheight)

end_time= datetime.now()
timelap = (end_time-start_time).total_seconds()
print ("end", end_time, "length:", timelap,  "Billeder/sek:", antal/timelap)

time.sleep(30)
