import requests
import os



def send_pic():

 

    # URL='http://192.168.0.33:8000/scan/upload'
    URL = 'http://SAL.local:8000/scan/upload'

 

    path = os.path.join(os.path.join(os.path.dirname(os.path.abspath(__file__)),'static'),'device')

    print(path)

 

    def sendfiles(file1,file2, file3):

        with open(file1, 'rb') as f1, open(file2, 'rb') as f2, open(file3, 'rb') as f3:

            r = requests.post(URL, files={"Pic1": f1, "Pic2": f2, "Pic3": f3 }, data={'scannerid':'654321', 'cmd':'tekst'})

        

        if r.status_code == requests.codes.ok:

            print('det gik godt')

            print(r.text)

        else:

            print('Noget gik galt: ', r.status_code)

            print(r.text)

 

        return

 
    f1 = 'file1.jpeg'
    f2 = 'file2.jpeg'
    f3 = 'file3.jpeg'
    #f4 = 'file4.png'
    

    # f1 = os.path.join(path, 'tand1a.png')

    # f2 = os.path.join(path, 'tand1b.png')

    sendfiles(f1,f2,f3)

    return


# send_pic()
