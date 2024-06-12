### 4. 컴퓨터 그래픽스 알고리즘

#### 4.1 레이 트레이싱
**이론**:
- **레이 트레이싱의 개념**: 레이 트레이싱은 빛의 경로를 추적하여 사실적인 이미지를 생성하는 렌더링 기법입니다. 광선이 물체에 반사되고 굴절되며, 이 과정에서 색상, 그림자, 반사 등을 계산하여 이미지를 만듭니다.
- **장점**: 매우 사실적인 이미지를 생성할 수 있습니다.
- **단점**: 계산량이 많아 렌더링 시간이 오래 걸릴 수 있습니다.

**실습**:
Python을 사용하여 간단한 레이 트레이싱을 구현해보겠습니다.

```python
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
img.save('ray_traced_image.png')
img.show()
```

이 코드는 간단한 레이 트레이싱 알고리즘을 사용

하여 구체의 이미지를 생성합니다.

#### 4.2 래스터화
**이론**:
- **래스터화의 개념**: 래스터화는 3D 모델의 폴리곤을 2D 화면의 픽셀로 변환하는 과정입니다. 각 픽셀은 해당하는 폴리곤의 색상을 가지며, 이를 통해 3D 모델을 2D 이미지로 표현합니다.
- **장점**: 계산 속도가 빠르며, 실시간 그래픽스에 적합합니다.
- **단점**: 매우 복잡한 광원 효과를 표현하기 어려울 수 있습니다.

**실습**:
Python을 사용하여 간단한 래스터화 알고리즘을 구현해보겠습니다.

```python
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
img.save('rasterized_image.png')
img.show()
```

이 코드는 간단한 래스터화 알고리즘을 사용하여 삼각형의 이미지를 생성합니다.
