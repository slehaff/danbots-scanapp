#!/usr/bin/python3 
#
# scan a picture serie for stitching
#

from datetime import datetime
from config import DEBUG, WINDOWS, config
from send_info import SendFiles, SendMemFiles
from scan_set import ScanFileSet, ScanMemSet

SCAN_PICTURE='scan_picture'
NUMBER_PIC='number_pic'
NO_PICTURE = 3
DEBUG=True
	
if DEBUG: print ("Starting 2D Scan", datetime.now().time())

scanpicture = config[SCAN_PICTURE]
no_picture = scanpicture.getint(NUMBER_PIC, NO_PICTURE)

# init camera

# if not WINDOWS:
# 	print(" take pic")
# 	camera = PiCamera()
# 	camera.capture('mypic.jpg')

files = ScanMemSet(no_picture)
data={'scannerid':'654321',"cmd":"stitch"}
info={'billedinfo': str(no_picture) + " filer"}
result =SendMemFiles(files, params=data, info=None)
print('Result:', result)
if DEBUG: print ("Ending 2D Scan", datetime.now().time())

#lib.send_pic.SendFiles(filearr)
