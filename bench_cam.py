from datetime import datetime
from time import sleep
from scancam import scancamera
#from scan_set import Scanner
from send_pic import SendFiles, Register
from io import BytesIO


print ("starting", datetime.now())


#scanner  = Scanner()
sleep(3)
cam = scancamera()
print ("Ready", datetime.now())

print("take one picture")
stream=BytesIO()
cam.resolution=(160,160)
cam.settings() 
#cam.capture_file('test2.jpg')
start=datetime.now()
cam.capture_stream(stream)
slut=datetime.now()
print("Time: ", (slut-start).total_seconds())
print("Stream length: ", stream.getbuffer().nbytes)

antal=10
i=0
while i<antal: 
    cam.capture_stream(stream) 
    i += 1
slut=datetime.now()
dif = slut - start
print("Pic/sec: ", antal/(slut-start).total_seconds())
exit(1)
print ("trans pr sek", antal/seconds)

antal=10
i=0
while i<antal: 
    cam.capture_stream() 
    SendFiles(scanner.f1,scanner.f2, scanner.f3)
    i += 1

