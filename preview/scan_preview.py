#import datetime
#import time
import .scancam
from io import BytesIO

################
# this class implement a standard preview scan 
#

class Preview:
    f1 = BytesIO()
    cam = scancam.scancamera()
    #cam.set_scan_pic()

    def Pic1Setup():
        pass

    def Scan(self):
        self.f1.seek(0)
        self.cam.capture_stream(self.f1)
