#!/usr/bin/python3 
#
# scan a 3D picture serie 
#

from datetime import datetime
from config import DEBUG, WINDOWS, DEVICEID, config
from send_info import SendFiles, SendMemFiles
from scan_set import ScanFileSet, ScanMemSet, ScanContMemSet
#from light_func import flash_light, light_3d
from light_3d import light_3d


SECTION='scan_3d'
NUMBER_PIC='number_pic'
NO_PICTURE = 4
DEBUG=True

scanpicture = config[SECTION]
no_picture = scanpicture.getint(NUMBER_PIC, 3)

#deviceid = config
start_time = datetime.now()
if DEBUG: print ("Starting 3D Scan", start_time.time(), " Antal:", no_picture)

#files = ScanMemSet(no_picture)
files = ScanContMemSet(no_picture, format='jpeg', flash=light_3d)
data={'scannerid':DEVICEID,"cmd":"scan3d"}
info={'billedinfo': str(no_picture) + " filer"}

result =SendMemFiles(files, file_type='jpg', params=data, info=None)
end_time = datetime.now()

if DEBUG: print ("End", end_time.time() )
print('Result:', result)
