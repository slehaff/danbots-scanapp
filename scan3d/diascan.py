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
led1 = PWMLED(13) #pin 33
led2 = PWMLED(12) #pin 32
#led3 = PWMLED(13) #pin 33

def ledHon(led):
    if led == 0:
        return
    led.value =0.95
    # turn led on
    return

def ledLon(led):
    if led == 0:
        return
    led.value =0.05
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
    camera.resolution = (160, 160)
    camera.start_preview()
    time.sleep(1)
    return


def take(led,color, file):
    if led ==led1:
        ledLon(led)
    elif led == led2:
        ledHon(led)
    elif led == 0:
        ledLon(led)

    
    try:
        camera = picamera.PiCamera()
        camera.color_effects = color 
        camera.resolution = (160, 160)
        camera.capture(file)

    finally:
        camera.close()
    ledoff(led)
    return

def scan():
    take(led = led0, color= (128,128), file='file1.jpeg')
    take(led = led1, color= None, file='file2.jpeg')
    take(led = led2, color= (128,128), file='file3.jpeg')
    # take(led = led3, color= (128,128), file='file4.png')
    return


