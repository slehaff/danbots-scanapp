import datetime
import time
#import scancam
from io import BytesIO
from config import DEBUG, WINDOWS

################
# this class implement a standard scan including controlling the LEDS
#
# this include 3 picture
# f1: normal
# f2: grayscale
# f3 solarized
#

camera = None 
def initcam():
    if not WINDOWS:
        from picamera import PiCamera
        camera = picamera()
    return

def take_pic(filename):
    if not WINDOWS:
        camera.capture(filename)
    return True


def ScanFileSet(antal=2):
    take_pic('file1.jpg')
    take_pic('file2.jpg')
    return ['file1.jpg','file2.jpg']

# class Scanner:
#     f1 = BytesIO()
#     f2 = BytesIO()
#     f3 = BytesIO()
#     cam = scancam.scancamera()
#     cam.set_scan_pic()

#     def Pic1Setup():
#         pass

#     def ScanSet(self):
#         self.cam.color_effects(None)
#         self.f1.seek(0)
#         self.cam.take_stream(self.f1)
#         self.cam.color_effects((127,127))
#         self.f2.seek(0)
#         self.cam.take_stream(self.f2)
#         self.f3.seek(0)
#         self.cam.take_stream(self.f3)

##my = Scanner()
#y.ScanSet()
#print("F1:", my.f1)

