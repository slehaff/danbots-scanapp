from datetime import datetime
from scan_set import Scanner
from send_pic import SendFiles, Register


print ("starting", datetime.now())

scanner  = Scanner()

print ("Ready", datetime.now())

scanner.ScanSet()
print ("F1:", scanner.f1.getbuffer().nbytes )

start=datetime.now()
antal=10
i=0
while i<antal: 
    scanner.ScanSet() 
    SendFiles(scanner.f1,scanner.f2, scanner.f3)
    i += 1

slut=datetime.now()

dif = slut - start
print (dif)

seconds = dif.total_seconds()

print ("trans pr sek", antal/seconds)

