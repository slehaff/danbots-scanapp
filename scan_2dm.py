#!/usr/bin/python3 
#
# scan a picture serie for stitching
#

from datetime import datetime
from config import DEBUG, WINDOWS, config
from send_info import SendFiles, SendMemFiles
from scan_set import ScanFileSet, ScanMemSet, ScanContMemSet
from light_func import flash_light

SCAN_PICTURE='scan_picture'
NUMBER_PIC='number_pic'
NO_PICTURE = 3
DEBUG=True

scanpicture = config[SCAN_PICTURE]
no_picture = scanpicture.getint(NUMBER_PIC, NO_PICTURE)
start_time = datetime.now()
if DEBUG: print ("Starting 2D Scan", start_time.time(), " Antal:", no_picture)

# init camera

# if not WINDOWS:
# 	print(" take pic")
# 	camera = PiCamera()
# 	camera.capture('mypic.jpg')

#files = ScanMemSet(no_picture)
files = ScanContMemSet(no_picture, format='png', flash=flash_light)
capture_time = datetime.now()
captime = (capture_time - start_time).total_seconds()

data={'scannerid':'654321',"cmd":"stitch"}
info={'billedinfo': str(no_picture) + " filer"}

result =SendMemFiles(files, file_type='png', params=data, info=None)
end_time = datetime.now()
time = (end_time - start_time).total_seconds()
if DEBUG: 
    print ("Capture time:", captime, "Billeder/sek:", no_picture/captime)
    sendtime=(end_time-capture_time).total_seconds()
    print ("Send time:", sendtime, "Billeder/sek:", no_picture/sendtime)
    print ("End", end_time.time(), "Tid:", time, "Billeder/sek:", no_picture/time)

print('Result:', result)


#lib.send_pic.SendFiles(filearr)
