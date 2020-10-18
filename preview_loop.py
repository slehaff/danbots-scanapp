# Loop start utility in charge of sending live hhttp requests every second
import requests
import time
import datetime
from send_preview import SendPreview
from scan_preview import Preview

# url = 'http://192.168.0.33:8000/datetime'
# myobj = {'Mac': 'b8:27:eb:e3:0b:80'}
# i = 1
# while i == 1:
#     x = requests.post(url, data = myobj)
#     time.sleep(5)

#     print(x.text)

prev = Preview()
i=1
n= 100
print(datetime.datetime.now())
while i<n:
    prev.Scan()
    SendPreview(Preview.f1)
    time.sleep(0.1 )
    i +=1
    
print(datetime.datetime.now())
