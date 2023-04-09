import cv2
# haarcascade_frontalface_default.xml
# https://github.com/opencv/opencv/tree/master/data/haarcascades
face_patterns = cv2.CascadeClassifier('Resources/haarcascades/haarcascade_frontalface_default.xml')
eyes_patterns = cv2.CascadeClassifier('Resources/haarcascades/haarcascade_eye.xml')
# leer imagen
sample_image = cv2.imread('Resources/lena.png')
gray = cv2.cvtColor(sample_image, cv2.COLOR_BGR2GRAY)
# Obtenga la cara reconocida 
faces = face_patterns.detectMultiScale(gray,scaleFactor=1.15,minNeighbors=5,minSize=(150, 150),maxSize=(500,500))
# Enmarca la cara reconocida
for (x, y, w, h) in faces:                          #ancho de color
    cv2.rectangle(sample_image, (x, y), (x+w, y+h), (0, 255, 0), 5)    
    eyes= eyes_patterns.detectMultiScale(sample_image[y:y+h,x:x+w],scaleFactor=1.15,minNeighbors=5,minSize=(10, 10),maxSize=(500,500))
    for (x1, y1, w1, h1) in eyes:                          #ancho de color
        cv2.rectangle(sample_image, (x1+x, y1+y), (x+x1+w1, y+y1+h1), (0, 0, 255), 5)
# Generar una nueva imagen para almacenar los resultados del reconocimiento
cv2.namedWindow("output", cv2.WINDOW_NORMAL)
cv2.imwrite('3_2.jpg', sample_image)
cv2.imshow("output", sample_image)
cv2.waitKey(0)