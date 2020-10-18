# Loop start utility in charge of sending live hhttp requests every second
import requests
import time
import datetime
from send_preview import SendPreview
from scan_preview import Preview

# initialize

sleeptime = 0.25    # 4 pic pr seconds
runtime = 5 * 60 * / sleeptime    # minutes

prev = Preview()
i=1
print("Starting preview loop: ", datetime.datetime.now())
while i<runtime:
    prev.Scan()
    print ("stream length: ", prev.f1.getbuffer().nbytes )
    SendPreview(prev.f1)
    time.sleep(sleeptime)
    i +=1
    
print("Ending previewloop", datetime.datetime.now())
