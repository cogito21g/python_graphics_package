import cv2

# 이미지 로드
image = cv2.imread('./assets/image1.png')

# 그레이스케일 변환
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 이미지 저장
cv2.imwrite('./assets/gray_image.png', gray_image)

# 이미지 표시
cv2.imshow('Grayscale Image', gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
