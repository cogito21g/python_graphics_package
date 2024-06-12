import numpy as np
from PIL import Image

# 이미지 크기 설정
width, height = 400, 400

# 이미지 배열 생성
image = np.zeros((height, width, 3), dtype=np.uint8)

# 삼각형의 정점 설정
triangle = np.array([[100, 100], [300, 100], [200, 300]])

# 삼각형의 색상 설정
triangle_color = np.array([255, 0, 0])

# 래스터화 계산
for y in range(height):
    for x in range(width):
        # 점이 삼각형 내부에 있는지 확인
        p = np.array([x, y])
        v0 = triangle[2] - triangle[0]
        v1 = triangle[1] - triangle[0]
        v2 = p - triangle[0]

        dot00 = np.dot(v0, v0)
        dot01 = np.dot(v0, v1)
        dot02 = np.dot(v0, v2)
        dot11 = np.dot(v1, v1)
        dot12 = np.dot(v1, v2)

        invDenom = 1 / (dot00 * dot11 - dot01 * dot01)
        u = (dot11 * dot02 - dot01 * dot12) * invDenom
        v = (dot00 * dot12 - dot01 * dot02) * invDenom

        if u >= 0 and v >= 0 and (u + v) < 1:
            image[y, x] = triangle_color

# 이미지 생성 및 저장
img = Image.fromarray(image, 'RGB')
img.save('./result/rasterized_image.png')
img.show()
