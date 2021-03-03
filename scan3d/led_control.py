# Old diascan file

import io
import socket
import struct
import time
#import picamera
from gpiozero import PWMLED
from time import sleep
#from picamera import PiCamera

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
        led.value = 0.99
    else
        led.value = 0.0
        return
    
    return



def flash_led(val):
    FLASH_IO=13
    led = PWMLED(FLASH_IO)
    if val:
        led.value = 0.99
    else
        led.value = 0.0
    return

def dias_led(val):
    FLASH_IO=12
    led = PWMLED(FLASH_IO)
    if val:
        led.value = 0.99
    else
        led.value = 0.0
    return

#tryk knap gpio 4


def take(led,color, file):
    if led ==led1:
        ledLon(led)
    elif led == led2:
        ledHon(led)
    elif led == 0:
        ledLon(led)
  
    # try:
    #     camera = picamera.PiCamera()
    #     camera.color_effects = color 
    #     camera.resolution = (160, 160)
    #     camera.capture(file)

    # finally:
    #     camera.close()
    #ledoff(led)
    return


def light_3d(picturenumber):
    if picturenumber == 0:
        print ("turn off flash")
        ledoff(led)
    elif picturenumber == 1:
        take(led = led0, color= (128,128), file='file1.jpeg')
    elif picturenumber == 2:
        take(led = led1, color= None, file='file2.jpeg')
    elif picturenumber == 3:
        take(led = led2, color= (128,128), file='file3.jpeg')
    else:
        ledoff(led)

    return True


# def warmup():
#     camera = PiCamera()
#     camera.resolution = (160, 160)
#     camera.start_preview()
#     time.sleep(1)
#     return


# def scan():
#     take(led = led0, color= (128,128), file='file1.jpeg')
#     take(led = led1, color= None, file='file2.jpeg')
#     take(led = led2, color= (128,128), file='file3.jpeg')
#     # take(led = led3, color= (128,128), file='file4.png')
#     return


