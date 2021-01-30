#
# send pictures to server 
#
	
import requests
from config import DEBUG, APISERVER

APIURL = APISERVER + "sendpic"
HTTP_TIMEOUT=10

def SendFiles (files, info=None, params=None):
    if DEBUG: print("SendFiles:", files, info, params)
    files_spec=None
    data_spec={}
    info_spec=None
    if type(files) is list:
        files_spec=[]
        for f in files:
            files_spec.append(('Picture', (f, open(f,'rb'))))
    else:
        files_spec=[('Picture', (files, open(files,'rb')))]
    
    if params is not None:
        data_spec = params
    
    if info is not None:
        data_spec = { **data_spec, "info": info}
    if DEBUG:
        print('Data', data_spec)
        print ("filespec", files_spec)
    try:
        r = requests.post(APIURL, timeout=HTTP_TIMEOUT, files=files_spec, data=data_spec)
    except requests.exceptions.RequestException as e:
        print(e)
        return False
            
    if r.status_code == requests.codes.ok:
        if DEBUG:
            print('det gik godt')
            print(r.text)
        return True
    else:
        print('Noget gik galt: ', r.status_code)
        print(r.text)
    return False
    
# def SendFiles2(f1,f2,f3):
#     #print ("sending files")
#     #print (f1, f2, f3)  
#     f1.seek(0)
#     f2.seek(0)
#     f3.seek(0)

#     #with open(f1, 'rb') as f1, open(f2, 'rb') as f2, open(f3, 'rb') as f3:
#     try:
#         r = requests.post(URL, timeout=1, files={'Pic1': ('pic1.jpg', f1), 'Pic2': ('pic2.jpg',f2), 'Pic3': ('pic3.jpg', f3) }, data={'scannerid':'654321', 'cmd':'tekst'})
#     except requests.exceptions.RequestException as e:
#         print(e)
#         return False
            
#     if r.status_code == requests.codes.ok:
#         #print('det gik godt')
#         #print(r.text)
#         pass
#     else:
#         print('Noget gik galt: ', r.status_code)
#         print(r.text)
#     return
