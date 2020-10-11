# Old diascan file

import io
import socket
import struct
import time
import picamera
from gpiozero import PWMLED
from time import sleep
from picamera import PiCamera

led0 = 0 # no led selected, background lighting

#led1 = PWMLED(18) #pin 12
#led2 = PWMLED(12) #pin 32
#led3 = PWMLED(13) #pin 33



def ledon(led):
    if led == 0:
        return
    led.value =0.8
    # turn led on
    return

def ledoff(led):
    if led ==0:
        return
    led.value = 0
    # turn led off
    return


def warmup():
    camera = PiCamera()
    camera.resolution = (170, 170)
    camera.start_preview()
    #time.sleep(1)
    return


def take(color, file):
    #ledon(led)
    try:
        camera = picamera.PiCamera()
        camera.color_effects = color 
        camera.resolution = (170, 170)
        camera.capture(file)

    finally:
        camera.close()
    #ledoff(led)
    return

def scan():
    take(color= (128,128), file='file1.png')
    #take(color= None, file='file2.png')
    #take(color= (128,128), file='file3.png')
    #take(color= (128,128), file='file4.png')
    return


