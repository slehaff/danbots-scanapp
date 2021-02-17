#!/usr/bin/python3 
#
# scan a picture serie for stitching
#

#import os
#import time
from datetime import datetime
#import configparser	
#import requests
#import signal

#import config
from config import DEBUG, WINDOWS, config
from send_info import SendFiles
from scan_set import ScanFileSet
#from io import BytesIO

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

# 	f1 = BytesIO()
# 	camera.capture(f1,format='jpeg')
# 	camera.capture('test.jpg')

# filearr=[]
# filearr.append('file1.jpg')
# filearr.append('file2.jpg')
#print ("arr",filearr)

files = ScanFileSet(no_picture)
print ("Files:", files)
data={'scannerid':'654321',"cmd":"stitch"}
info={'billedinfo': str(no_picture) + " filer"}
result =SendFiles(files, params=data, info=None)
print('Result:', result)
if DEBUG: print ("Ending 2D Scan", datetime.now().time())

#lib.send_pic.SendFiles(filearr)



