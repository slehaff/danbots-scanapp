#!/usr/bin/python3 
#
# scan a picture serie for performancetest and stitching
#

from datetime import datetime
from config import DEBUG, WINDOWS, DEVICEID, config
from send_info import SendFiles, SendMemFiles
from scan_set import ScanFileSet, ScanMemSet, ScanContMemSet
from light_func import flash_light

SCAN_PICTURE='scan_picture'
NUMBER_PIC='number_pic'
DEBUG=True

scanpicture = config[SCAN_PICTURE]
no_picture = scanpicture.getint(NUMBER_PIC, 3)

start_time = datetime.now()
if DEBUG: print ("Starting 2D Scan", start_time.time(), " Antal:", no_picture)

files = ScanContMemSet(no_picture, format='jpeg', flash=flash_light)
capture_time = datetime.now()
captime = (capture_time - start_time).total_seconds()

data={'scannerid': DEVICEID, "cmd": "stitch"}
info={'billedinfo': str(no_picture) + " filer"}

result =SendMemFiles(files, file_type='jpg', params=data, info=info)
end_time = datetime.now()
time = (end_time - start_time).total_seconds()

if DEBUG: 
    print ("Capture time:", captime, "Billeder/sek:", no_picture/captime)
    sendtime=(end_time-capture_time).total_seconds()
    print ("Send time:", sendtime, "Billeder/sek:", no_picture/sendtime)
    print ("End", end_time.time(), "Tid:", time, "Billeder/sek:", no_picture/time)

print('Result:', result)
