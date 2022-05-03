import numpy
import cv2

# 얼굴, 눈을 찾기 위한 OpenCV 알고리즘이 적용된 파일 불러오기
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

ff = numpy.fromfile(r'220503\pic\얼굴.jpg', numpy.uint8)
img = cv2.imdecode(ff, cv2.IMREAD_UNCHANGED)
img = cv2.resize(img, dsize=(0, 0), fx=1.0, fy=1.0, interpolation=cv2.INTER_LINEAR)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, 1.2, 5)
for (x, y, w, h) in faces:
    # 얼굴 부분 자르기
    face_img = img[y: y + h, x: x + w]
    face_img = cv2.resize(face_img, dsize=(0, 0), fx=0.1, fy=0.1)
    face_img = cv2.resize(face_img, (w, h), interpolation=cv2.INTER_AREA)
    img[y: y + h, x: x + w] = face_img
        
cv2.imshow('face find', img)
cv2.waitKey(0)
cv2.destroyAllWindows()