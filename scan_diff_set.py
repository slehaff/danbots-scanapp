import datetime
import time
import scancam
from io import BytesIO

################
# this class implement a standard scan including controlling the LEDS
#
# this include 3 picture
# f1: normal
# f2: grayscale
# f3 solarized
#


class Scanner:
    f1 = BytesIO()
    f2 = BytesIO()
    f3 = BytesIO()
    cam = scancam.scancamera()
    cam.set_scan_pic()

    def Pic1Setup():
        pass

    def ScanSet(self):
        #self.cam.color_effects(None)
        self.cam.color_effects((127,127))
        time.sleep(5)
        self.cam.exposure_mode('off')
        print("Klar til første billede")
        self.cam.capture_file("fil1.jpg")
        
        print("pause")
        time.sleep(5)
        print("Klar til andet billede")
        self.cam.capture_file("fil2.jpg")
        print("pause")
        time.sleep(5)
        self.cam.capture_file("fil3.jpg")


