import datetime
import time
import scancam
from io import BytesIO



mycam = scancam.scancamera()
#print("default settings")
#mycam.settings()
mycam.set_scan_pic()
mycam.settings()
mycam.start_preview()
time.sleep(5)



#mycam.stop_preview()

antal_billeder = 10
start = datetime.datetime.now()
i = 0
while i<antal_billeder:
    #my_stream = BytesIO()
    #mycam.take_stream(my_stream)
    mycam.take_file('test.png')
    i += 1
slut = datetime.datetime.now()
print ("Starting", start)
print ("slutter", slut)
mycam.settings()

dif = slut - start
print (dif)

seconds = dif.total_seconds()

print ("Billeder pr sek", antal_billeder/seconds)
#print (my_stream.getbuffer().nbytes)
