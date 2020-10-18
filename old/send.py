import requests
import os



def send_pic():

 

    # URL='http://192.168.0.33:8000/scan/upload'
    URL = 'http://samir-Nitro-AN515-53.local:8000/scan/upload'
    URL = 'http://live.danbots.com/api/sendpic'
    #URL = 'http://dxwin10.local:8000/api/sendpic'
 

    #path = os.path.join(os.path.join(os.path.dirname(os.path.abspath(__file__)),'static'),'device')

    #print(path)

 

    def sendfiles(file1, file2, file3, file4):
        #print ("sender filer")
        with open(file1, 'rb') as f1, open(file2, 'rb') as f2, open(file3, 'rb') as f3, open(file4, 'rb') as f4:
            try:
                #r = requests.post(URL, files={"Pic1": f1, "Pic2": f2, "Pic3": f3, "Pic4": f4 }, data={'scannerid':'654321', 'cmd':'tekst'})
                r = requests.post(URL, timeout=1, files={"Pic1": f1}, data={'scannerid':'654321', 'cmd':'tekst'})
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

 
    f1 = 'file1.png'
    f2 = 'file2.png'
    f3 = 'file3.png'
    f4 = 'file4.png'
    

    # f1 = os.path.join(path, 'tand1a.png')

    # f2 = os.path.join(path, 'tand1b.png')

    sendfiles(f1,f2,f3,f4)

    return


# send_pic()
