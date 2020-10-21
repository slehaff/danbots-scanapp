# Loop start utility in charge of sending live hhttp requests every second
import requests
import time
import datetime
from send_preview import SendPreview
from scan_preview import Preview

# initialize

def save_stream (f1, filename):
    f1.seek(0)
    f2 = open (filename, "bw")
    f2.write(f1.read(-1))
    f2.close()

sleeptime = 0.05    # 4 pic pr seconds
runtime = 5 * 60.0  / sleeptime    # minutes

prev = Preview()
prev.cam.resolution=(160,160)
#adjust camera
time.sleep(2)
i=1
print("Starting preview loop: ", datetime.datetime.now())
while i<runtime:
    prev.Scan()
    #print ("stream length: ", prev.f1.getbuffer().nbytes )
    #save_stream(prev.f1,str(i)+".jpg")
    SendPreview(prev.f1)
    time.sleep(sleeptime)
    i +=1
    
print("Ending previewloop", datetime.datetime.now())
