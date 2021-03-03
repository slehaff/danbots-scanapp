#!/usr/bin/python3 
#
# scan a 3D picture serie 
#

from datetime import datetime
from config import DEBUG, WINDOWS, DEVICEID, config
from send_info import SendFiles, SendMemFiles
from scan_set import ScanFileSet, ScanMemSet, ScanContMemSet, start_cam, stop_cam
#from light_func import flash_light, light_3d
from light_3d import light_3d
#from scan3d.led_control import light_3d

SECTION='scan_3d'
NUMBER_PIC='number_pic'
DEBUG=True

scanpicture = config[SECTION]
no_picture = scanpicture.getint(NUMBER_PIC, 3)

start_time = datetime.now()
if DEBUG: print ("Starting 3D Scan", start_time.time(), " Antal:", no_picture)

start_cam(1.0)
files = ScanContMemSet(no_picture, format='jpeg', flash=light_3d)
data={'scannerid':DEVICEID,"cmd":"scan3d"}
info={'billedinfo': str(no_picture) + " filer"}

result =SendMemFiles(files, file_type='jpg', params=data, info=None)
end_time = datetime.now()

if DEBUG: print ("End", end_time.time() )
print('Result:', result)

if __name__ == "__main__":
    Print("Vi kører script")
    start_time = datetime.now()
    print ("Starting 3D Scan", start_time.time(), " Antal:", no_picture)
