import datetime
import time
import scancam
from io import BytesIO

antal_billeder = 10
start = datetime.datetime.now()
print ("Starting", start)


mycam = scancam.scancamera()
print("default settings")
mycam.settings()
mycam.set_scan_pic()
mycam.settings()
#mycam.start_preview()
time.sleep(5)



#mycam.stop_preview()

i = 0
while i<antal_billeder:
    #time.sleep(5)    
    my_stream = BytesIO()
    #mycam.take_stream(my_stream)

    #print("take picture", datetime.datetime.now())
 
    mycam.take_stream(my_stream)
    #mycam.take_file('test.png')
    #print("taken", datetime.datetime.now())
    #mycam.settings()
    #print("done - exposure", mycam.info())
    i += 1

slut = datetime.datetime.now()
print ("slutter", slut)
mycam.settings()

dif = slut - start
print (dif)

seconds = dif.total_seconds()

print ("Billeder pr sek", antal_billeder/seconds)
