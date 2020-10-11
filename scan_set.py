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

    def Pic1Setup():
        pass

    def ScanSet(self):
        self.cam.take_stream(self.f1)

my = Scanner()
my.ScanSet()
print("F1:", my.f1)
