#!/usr/bin/python3 
#
# scan a set of pictures to files and send to server
#

import os
from datetime import datetime
from config import DEBUG, WINDOWS, config
from send_info import SendFiles
from scan_set import ScanFileSet

SCAN_PICTURE='scan_picture'
NUMBER_PIC='number_pic'
NO_PICTURE = 3
DEBUG=True
	
if DEBUG: print ("Starting 2D Scan", datetime.now().time())

scanpicture = config[SCAN_PICTURE]
no_picture = scanpicture.getint(NUMBER_PIC, NO_PICTURE)

# scan
start_time = datetime.now()
files = ScanFileSet(no_picture)
cap_time = datetime.now()

# send 
data={'scannerid':'654321',"cmd":"stitch"}
info={'billedinfo': str(no_picture) + " filer"}
result =SendFiles(files, params=data, info=None)
send_time = datetime.now()
captime = (cap_time - start_time).total_seconds()
print ("capture time: ", captime, "pic/sec:", no_picture/captime)
print('Result:', result)
if DEBUG: print ("Ending 2D Scan", datetime.now().time())
print ("Removing Files in /tmp")
for f in files:
    os.remove(f)
