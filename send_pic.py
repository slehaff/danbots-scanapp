import requests 

HOST_URL = 'http://live.danbots.com/api/test'
URL = 'http://samir-Nitro-AN515-53.local:8000/scan/upload'
URL = 'http://live.danbots.com/api/sendpic'
URL = 'http://192.168.0.100:8000/api/sendpic'



def Register():
    try:
        r = requests.get(HOST_URL)
    except requests.exceptions.RequestException as e:
        print(e)
        return False     
    if r.status_code == requests.codes.ok:
        print('det gik godt')
        #print(r.text)
        pass
    else:
        print('Noget gik galt: ', r.status_code)
        print(r.text)
    return


def SendFiles(f1,f2,f3):
    #print ("sending files")
    #print (f1, f2, f3)  
    f1.seek(0)
    f2.seek(0)
    f3.seek(0)

    #with open(f1, 'rb') as f1, open(f2, 'rb') as f2, open(f3, 'rb') as f3:
    try:
        r = requests.post(URL, timeout=1, files={'Pic1': ('pic1.jpg', f1), 'Pic2': ('pic2.jpg',f2), 'Pic3': ('pic3.jpg', f3) }, data={'scannerid':'654321', 'cmd':'tekst'})
    except requests.exceptions.RequestException as e:
        print(e)
        return False
            
    if r.status_code == requests.codes.ok:
        #print('det gik godt')
        #print(r.text)
        pass
    else:
        print('Noget gik galt: ', r.status_code)
        print(r.text)
    return

 



    return True


