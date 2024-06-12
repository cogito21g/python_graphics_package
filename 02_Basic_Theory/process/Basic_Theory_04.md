### 2. 2D 그래픽스

#### 2.1 벡터 그래픽스
**이론**:
- **벡터 그래픽스의 개념**: 벡터 그래픽스는 점, 선, 곡선 등 기하학적 도형을 수학적으로 정의하여 이미지를 표현합니다. 이는 확대/축소해도 해상도가 떨어지지 않으며, 크기와 무관하게 동일한 품질을 유지합니다. 주로 SVG (Scalable Vector Graphics) 형식으로 저장됩니다.
- **주요 포맷**: SVG (Scalable Vector Graphics), AI (Adobe Illustrator), EPS (Encapsulated PostScript)
- **사용 사례**: 로고, 아이콘, 일러스트레이션 등
- **장점**: 벡터 그래픽스는 확대해도 해상도가 떨어지지 않으며, 파일 크기가 작고 수정이 용이합니다.

**벡터 그래픽스의 장점**:
1. **확장성**: 벡터 이미지는 크기에 상관없이 동일한 품질을 유지합니다.
2. **파일 크기**: 복잡한 이미지도 비교적 작은 파일 크기를 유지할 수 있습니다.
3. **편집 용이성**: 개별 요소를 독립적으로 조작할 수 있어 수정이 용이합니다.

**실습**:
간단한 SVG 파일을 생성하고, 이를 편집해보겠습니다.

```xml
<svg width="200" height="200" xmlns="http://www.w3.org/2000/svg">
  <!-- 빨간색 원 -->
  <circle cx="100" cy="100" r="80" stroke="black" stroke-width="3" fill="red" />
  <!-- 파란색 사각형 -->
  <rect x="50" y="50" width="100" height="100" stroke="black" stroke-width="3" fill="blue" />
</svg>
```

이 코드는 200x200 픽셀 크기의 SVG 이미지를 생성하고, 중앙에 빨간색 원과 파란색 사각형을 그립니다. 이 SVG 파일을 브라우저에서 열면 벡터 그래픽의 특성을 확인할 수 있습니다.

#### 2.2 래스터 그래픽스
**이론**:
- **래스터 그래픽스의 개념**: 래스터 그래픽스는 픽셀의 그리드로 이미지를 표현합니다. 각 픽셀은 고유의 색상을 가지며, 이미지의 전체 해상도는 픽셀 수로 결정됩니다. 이미지를 확대할 경우 해상도가 떨어질 수 있습니다.
- **주요 포맷**: JPEG, PNG, GIF, BMP
- **사용 사례**: 사진, 복잡한 이미지, 텍스처
- **장점**: 래스터 그래픽스는 복잡한 색상 변화를 표현하는 데 적합하며, 사진과 같은 이미지를 잘 표현할 수 있습니다.

**래스터 그래픽스의 장점**:
1. **세밀한 표현**: 색상 변화와 디테일한 표현이 가능하여 사진과 같은 이미지를 잘 나타냅니다.
2. **광범위한 지원**: 대부분의 디지털 디바이스와 소프트웨어에서 널리 사용됩니다.

**실습**:
Python과 PIL (Pillow) 라이브러리를 사용하여 래스터 이미지를 편집해보겠습니다.

1. **이미지 열기 및 보기**:
```python
from PIL import Image

# 이미지 열기
img = Image.open('example_image.jpg')

# 이미지 표시
img.show()
```

2. **이미지 크기 조절**:
```python
# 이미지 크기 조절
resized_img = img.resize((100, 100))

# 이미지 저장 및 표시
resized_img.save('resized_image.jpg')
resized_img.show()
```

3. **이미지 필터 적용**:
```python
from PIL import ImageFilter

# 블러 필터 적용
blurred_img = img.filter(ImageFilter.BLUR)

# 이미지 저장 및 표시
blurred_img.save('blurred_image.jpg')
blurred_img.show()
```

이 코드는 이미지를 열고, 크기를 조절하고, 블러 필터를 적용하는 방법을 보여줍니다.
