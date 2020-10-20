#import datetime
#import time
from scancam import scancamera
from io import BytesIO

################
# this class implement a standard preview scan 
#

class Preview:
    f1 = BytesIO()
    cam = scancamera()
    #cam.set_scan_pic()

    def Pic1Setup():
        pass

    def Scan(self):
        self.f1.seek(0)
        self.f1.truncate()
        self.cam.capture_stream(self.f1)
