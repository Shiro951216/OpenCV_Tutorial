import cv2

# #Read Image
# img = cv2.imread("Resources/leadale.jpg")
# #Display
# cv2.imshow("Besto Waifu", img)
# cv2.waitKey(0)
#
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cap.set(3, 640)
cap.set(4, 480)
cap.set(10, 100)

while cap.isOpened():
  ret, frame = cap.read()
  cv2.imshow('Shiro_P', frame)
  key = cv2.waitKey(1)
  if key & 0xFF == ord('a'):
    cv2.imwrite("test.jpg", frame)
  if key & 0xFF == ord('q'):
    break
cap.release()
cv2.destroyAllWindows()