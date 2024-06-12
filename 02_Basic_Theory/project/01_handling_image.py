import numpy as np
from PIL import Image

# 10x10 픽셀의 빈 이미지 생성
image = np.zeros((100, 100, 3), dtype=np.uint8)

# 픽셀 색상 설정 (빨강)
image[5, 5] = [255, 0, 0]

# 이미지 생성 및 저장
img = Image.fromarray(image, 'RGB')
img.save('./result/pixel_image.png')
img.show()
