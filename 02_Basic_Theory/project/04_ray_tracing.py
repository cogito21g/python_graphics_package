import numpy as np
from PIL import Image

# 이미지 크기 설정
width, height = 400, 400

# 이미지 배열 생성
image = np.zeros((height, width, 3), dtype=np.uint8)

# 구체의 중심과 반지름 설정
sphere_center = np.array([200, 200, 50])
sphere_radius = 50

# 빛의 색상 설정
light_color = np.array([255, 255, 255])

# 레이 트레이싱 계산
for y in range(height):
    for x in range(width):
        # 레이의 방향 설정
        ray_direction = np.array([x - sphere_center[0], y - sphere_center[1], 100])
        ray_direction = ray_direction / np.linalg.norm(ray_direction)

        # 구체와의 교차 여부 계산
        oc = np.array([x, y, 0]) - sphere_center
        b = 2 * np.dot(oc, ray_direction)
        c = np.dot(oc, oc) - sphere_radius * sphere_radius
        discriminant = b * b - 4 * c

        if discriminant > 0:
            # 교차점 계산
            t = (-b - np.sqrt(discriminant)) / 2
            if t > 0:
                hit_point = np.array([x, y, 0]) + t * ray_direction
                normal = (hit_point - sphere_center) / sphere_radius
                light_intensity = np.dot(normal, -ray_direction) * 255
                color = light_color * light_intensity / 255
                image[y, x] = np.clip(color, 0, 255)

# 이미지 생성 및 저장
img = Image.fromarray(image, 'RGB')
img.save('./result/ray_traced_image.png')
img.show()
