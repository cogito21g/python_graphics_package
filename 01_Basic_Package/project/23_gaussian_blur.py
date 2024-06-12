import cv2

# 이미지 로드
image = cv2.imread('./assets/image2.png')

# Gaussian Blur 적용
blurred_image = cv2.GaussianBlur(image, (15, 15), 0)

# 이미지 저장
cv2.imwrite('./assets/blurred_image.png', blurred_image)

# 이미지 표시
cv2.imshow('Blurred Image', blurred_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
