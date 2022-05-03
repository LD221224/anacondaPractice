import numpy
import cv2

ff = numpy.fromfile(r'220503\pic\바다.jpg', numpy.uint8)
img = cv2.imdecode(ff, cv2.IMREAD_UNCHANGED)
img = cv2.resize(img, dsize=(0, 0), fx=1.0, fy=1.0, interpolation=cv2.INTER_LINEAR)


def onChange(pos):
    pass

# 트랙 윈도우 생성
cv2.namedWindow('Trackbar Windows')

# 트랙의 최솟값, 최댓값 설정
cv2.createTrackbar('sigma_s', 'Trackbar Windows', 0, 200, onChange)
cv2.createTrackbar('sigma_r', 'Trackbar Windows', 0, 100, onChange)

# 트랙의 기본 위치
cv2.setTrackbarPos('sigma_s', 'Trackbar Windows', 100)
cv2.setTrackbarPos('sigma_r', 'Trackbar Windows', 10)

while True:
    if cv2.waitKey(100) == ord('q'):
        break
    
    sigma_s_value = cv2.getTrackbarPos('sigma_s', 'Trackbar Windows')
    sigma_r_value = cv2.getTrackbarPos('sigma_r', 'Trackbar Windows') / 100.0
    
    print('sigma_s_value', sigma_s_value)
    print('sigma_r_value', sigma_r_value)
    
    cartoon_img = cv2.stylization(img, sigma_s=sigma_s_value, sigma_r=sigma_r_value)
    
    cv2.imshow('Trackbar Windows', cartoon_img)
    
cv2.destroyAllWindows()