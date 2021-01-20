from datetime import datetime
from scan_diff_set import Scanner
#from send_pic import SendFiles, Register


print ("starting", datetime.now())

scanner  = Scanner()

print ("Ready", datetime.now())

scanner.ScanSet()

print ("Ready", datetime.now())
