#!/usr/bin/python3 
from datetime import datetime 
import time 
#from scancam import scancamera
#from scan_set import Scanner
#from send_pic import SendFiles, Register
from io import BytesIO
from shutil import copyfileobj, copyfile
from picamera import PiCamera
#import config

SCAN_PICTURE='scan_picture'
#scanpicture = config[SCAN_PICTURE]
camera_init_time = 0.9
picture_interval_time = 0.0

# scansettings = config['scan']
# picturewidth = scansettings.getint('width',720)
# pictureheight = scansettings.getint("height", 480)

FOLDER = "/tmp/"
FILENAME = "file"
FILETYPE = ".png"
PATH = FOLDER + FILENAME

def take_pic(filename):
    """ filename decide the type of the file """
    camera.capture(filename, use_video_port=True, format='png')
    return True

def take_fd(format='jpeg'):
    fd = BytesIO()
    camera.capture(fd, format=format)
    return fd

def speed_fd(format='jpeg'):
    fd = BytesIO()
    camera.capture(fd, format=format, use_video_port=True)
    return fd

def ScanFileSet(antal=1):
    #time.sleep(1)
    i = 1
    filelist =[]
    while i<=antal:
        filename =PATH + str(i) + FILETYPE
        #camera.capture(filename, use_video_port=True)
        take_pic(filename)
        #filelist.append(filename)
        #time.sleep(picture_interval_time)
        i += 1
    return filelist

def ScanMemSet(antal=1, format='jpeg'):
    #time.sleep(camera_init_time)
    i = 1
    filelist =[]
    while i<=antal:
        #fd = take_fd(format=format)
        fd = speed_fd()
        filelist.append(fd)
        time.sleep(picture_interval_time)
        i += 1
    return filelist

def ScanContMemSet(antal=10, format='jpeg', flash=None):
    #time.sleep(camera_init_time)
    j = 1
    filelist = []
    stream = BytesIO()
    if flash : flash(j)
    for i in enumerate(camera.capture_continuous(stream, format=format, use_video_port=True)):
        j = j+1    
        if flash : flash(j)    
        stream.truncate()
        stream.seek(0)
        fd = BytesIO()
        copyfileobj(stream, fd)
        filelist.append(fd)
        stream.seek(0)
        stream.truncate(0)

        if j>antal:
            if flash : flash(0)
            break;
    return filelist


antal = 20
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
ScanFileSet(antal)
#ScanContMemSet(antal)
#camera.resolution = (picturewidth, pictureheight)

end_time= datetime.now()

time = (end_time-start_time).total_seconds()

print ("end", end_time, "length:", time,  "Billeder/sek:", antal/time)

