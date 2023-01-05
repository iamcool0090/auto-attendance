# auto-attendance

NOTE : Installing dlib in face-recognition requires Windows 10 SDK and CMake to be preinstalled and in path



This is a Python program that uses facial recognition technology(face_recognition and cv2 (OpenCV) libraries to perform face recognition tasks) to register attendance for classes. The program takes in images of students' faces and stores their facial characteristics as face encodings. During attendance, the program compares the faces in a given image to the stored face encodings and, if a match is found, logs the student's attendance. The program also allows for a custom time table to be inputted, so that attendance can be taken for each class separately.

The program can do the following:

1. Load and store face encodings for a list of students in a JSON file called 'students.json'. This is done using the add_student() function, which takes in a student's name and the URL of an image containing the student's face, and stores the face encoding in the JSON file.

2. Given a video stream(project can overlap with IOT as this can also be run on Raspberry PI <subject to certain limitations>) of containing a face, compare the face to the stored face encodings in 'students.json' using the scan_att() function. If a match is found, the student's name is written to a text file called 'attendance/[current date]_[current class].txt', where [current date] is the current date and [current class] is the current class as determined by the current time.

3. Determine the current class based on the current time using the get_class() function and a time table stored in a JSON file called 'time_table.json'. The time table lists the class schedule for each day of the week.

  


The program also includes some additional code for capturing video from a camera and detecting faces in the video using a Haar cascade classifier, but these functions are currently commented out and not being used.
 
 
---------------------------------------------------USAGE-------------------------------------------------------------------

1.Register a student using add_student(name,url) [Note : the url must be local I have not yet integrated the requests module with it]

  Example : add_student('Racoon Dog','doraemon.jpg')


2.Accept attendance using scan_att(url) [Note : the url must be a local image I have not yet integrated web cam stream with it]
  Example : scan_att('nobita.jpg')
  It creates a file based on the day and time with the name [current date]_[current class].txt and adds the name of the       face it detected  
  
3.The timetable can be updated according to one's needs 



There are some major but simple functonalities to be added I will be adding them very soon


Praful M
BMSCE ISE PB 
