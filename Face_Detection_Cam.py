import cv2
# haarcascade_frontalface_default.xml
# https://github.com/opencv/opencv/tree/master/data/haarcascades
face_patterns = cv2.CascadeClassifier('Resources/haarcascades/haarcascade_frontalface_default.xml')
eyes_patterns = cv2.CascadeClassifier('Resources/haarcascades/haarcascade_eye.xml')

cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
while cap.isOpened():
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_patterns.detectMultiScale(gray,scaleFactor=1.15,minNeighbors=5,minSize=(150, 150),maxSize=(500,500))
    for (x, y, w, h) in faces:                          #ancho de color
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 5)    
        eyes= eyes_patterns.detectMultiScale(frame[y:y+h,x:x+w],scaleFactor=1.15,minNeighbors=5,minSize=(10, 10),maxSize=(500,500))
        for (x1, y1, w1, h1) in eyes:                          #ancho de color
            cv2.rectangle(frame, (x1+x, y1+y), (x+x1+w1, y+y1+h1), (0, 0, 255), 5)
    cv2.imshow("output", frame)
    c = cv2.waitKey(10)
    if c & 0xFF == ord('q'):
        break