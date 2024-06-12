import cv2

# 이미지 로드
image = cv2.imread('./assets/image1.png')

# 이미지 표시
cv2.imshow('Loaded Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
