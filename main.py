import face_recognition
import cv2
import numpy as np
import glob
import json
import os
from datetime import datetime
#video_capture = cv2.VideoCapture(0)
#face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')


#images to load
now = datetime.now()


timings = ['08:00', '08:55', '09:50', '10:45', '11:15', '12:10', '13:05', '14:00', '14:55', '15:50', '16:45']

with open('time_table.json') as f:
        time_table = json.load(f)


def get_class(timings):
    now = datetime.now()
    time = now.strftime('%H:%M')
    hours, minutes = map(int, time.split(':'))
    day = now.strftime('%A').lower()
    time_table_arr = time_table[day].split(',')
    time_in_seconds = hours * 3600 + minutes * 60


    for i, t in enumerate(timings):
        hours, minutes = map(int, t.split(':'))
        t_in_seconds = hours * 3600 + minutes * 60
      

        if time_in_seconds <= t_in_seconds:
            return time_table_arr[i-1]




def add_student(name,url):

    

    img = face_recognition.load_image_file(url)
    encoding = face_recognition.face_encodings(img)[0]
    
    
    with open('students.json') as f:
        data = json.load(f)

    print(encoding)
    data['students'].append({
        'name': name,
        'encoding': encoding.tolist()
    })


    with open('students.json', 'w') as f:
        json.dump(data, f)


    return encoding





def scan_att(url):

    try:
        os.mkdir("attendance")
    except:
        pass
    

    i = 0

    
    with open('students.json') as f:
        data = json.load(f)
    
    img1 = face_recognition.load_image_file(url)
    get_curr_encoding = face_recognition.face_encodings(img1)[0]
    get_curr_enc = get_curr_encoding.tolist()
    

    for i in range(len(data['students'])):
        if(face_recognition.compare_faces([np.array(data['students'][i]['encoding'])],np.array(get_curr_enc))[0]):
            print("Found match")
            os.system("echo " + data['students'][i]['name'] + ", >> attendance/" + now.strftime('%d_%m_%y') + "_" + get_class(timings) + ".txt")
            return 0    

        else:
            pass


