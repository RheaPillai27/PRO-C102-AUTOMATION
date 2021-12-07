import cv2 
import dropbox
import time 
import random


start_time=time.time()

def take_SnapShot():
    number = random.randint(0,100)
    #initiazling cv2 
    videoCaptureObject=cv2.VideoCapture(0)
    result=True
    while(result):
        ret,frame = videoCaptureObject.read()
        #cv2.iamwrite() is used to save an image to any storage device
        img_name = "img" + str(number) + ".png"
        cv2.iamwrite(img_name,frame)
        start_time=time.time
        result=False

    return img_name 
    print ("SnapShot taken")
    videoCaptureObject.release()
    cv2.destroyAllWindows()

    

def upload_file(img_name):
    access_token = "sl.A7xu99otL-hk4BqLOhXyo0LfwJJ4mCYHjou9GH-8f3p6vzUai1L-RlZfIlmB8D0kZ4ridz6VEHo2wma7vBhDjc6xzOs2K2P_rV38gFm0yNmxYfXjAluaktUpLdX9b5yEfESvalcSgjf9"
    file =img_name
    file_from = file
    file_to="/testFolder/"+(img_name)
    dbx = dropbox.Dropbox(access_token)

    with open(file_from, 'rb') as f:
        dbx.files_upload(f.read(), file_to,mode=dropbox.files.WriteMode.overwrite)
        print("file uploaded")


def main():
    while(True):
        if ((time.time() - start_time) >= 5):
            name = take_snapshot()
            upload_file(name)

main()