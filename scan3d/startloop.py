# Loop start utility in charge of sending live hhttp requests every second
# Mac rpizero 10 = b8:27:eb:e3:0b:80
# Mac rpizero 12 =
import requests
import time
import send
import diascan

# url = 'http://192.168.0.33:8000/datetime'
# myobj = {'Mac': 'b8:27:eb:e3:0b:80'}
# i = 1
# while i == 1:
#     x = requests.post(url, data = myobj)
#     time.sleep(5)

#     print(x.text)

i=1
while i==1:
    diascan.scan()
    send.send_pic()
    time.sleep(.1)
