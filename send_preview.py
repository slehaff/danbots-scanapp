import requests 

URL = 'http://live.danbots.com/api/sendpic'
#URL = 'http://192.168.0.100:8000/api/sendpic'

def SendPreview(f1):
    f1.seek(0)
    try:
        r = requests.post(URL, timeout=1, files={'Pic1': ('pic1.jpg', f1) }, data={'scannerid':'654321', 'cmd':'tekst'})
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
        return False
    return True

