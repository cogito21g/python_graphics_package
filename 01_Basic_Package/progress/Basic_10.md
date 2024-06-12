좋습니다! 이제 8단계로 넘어가서 **OpenCV를 사용한 컴퓨터 비전**을 공부해보겠습니다. OpenCV(Open Source Computer Vision Library)는 이미지와 비디오 처리를 위한 강력한 라이브러리로, 다양한 컴퓨터 비전 작업을 수행할 수 있습니다.

### 8단계: OpenCV를 사용한 컴퓨터 비전

#### 이론
OpenCV는 다음과 같은 기능을 제공합니다:
- **이미지 및 비디오 처리**: 이미지 필터링, 변환, 색상 공간 변환 등의 기본 처리
- **객체 검출**: 얼굴, 눈, 차량 등 특정 객체를 이미지에서 검출
- **특징 검출 및 매칭**: 이미지에서 특징점을 검출하고 매칭
- **이미지 변환**: 회전, 확대/축소, 변형 등의 기하학적 변환

#### 설치
먼저 OpenCV를 설치해야 합니다. 아래 명령어를 사용하여 설치합니다.

```bash
pip install opencv-python
pip install opencv-python-headless
```

#### 실습 1: 이미지 로드 및 표시

##### 예제 코드: 이미지 로드 및 표시
아래 코드는 OpenCV를 사용하여 이미지를 로드하고 화면에 표시하는 예제입니다.

```python
import cv2

# 이미지 로드
image = cv2.imread('example_image.jpg')

# 이미지 표시
cv2.imshow('Loaded Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

##### 코드 설명
- `image = cv2.imread('example_image.jpg')`: 이미지를 로드합니다.
- `cv2.imshow('Loaded Image', image)`: 이미지를 화면에 표시합니다.
- `cv2.waitKey(0)`: 키 입력을 기다립니다.
- `cv2.destroyAllWindows()`: 모든 창을 닫습니다.

#### 실습 2: 이미지 처리

##### 예제 코드: 이미지 그레이스케일 변환
아래 코드는 이미지를 그레이스케일로 변환하는 예제입니다.

```python
import cv2

# 이미지 로드
image = cv2.imread('example_image.jpg')

# 그레이스케일 변환
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 이미지 저장
cv2.imwrite('gray_image.jpg', gray_image)

# 이미지 표시
cv2.imshow('Grayscale Image', gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

##### 코드 설명
- `gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)`: 이미지를 그레이스케일로 변환합니다.
- `cv2.imwrite('gray_image.jpg', gray_image)`: 그레이스케일 이미지를 저장합니다.

#### 실습 3: 얼굴 검출

##### 예제 코드: 얼굴 검출
아래 코드는 이미지를 사용하여 얼굴을 검출하는 예제입니다.

```python
import cv2

# 이미지 로드
image = cv2.imread('example_image.jpg')

# 그레이스케일 변환
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 얼굴 검출기 로드 (Haar Cascade 사용)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# 얼굴 검출
faces = face_cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

# 얼굴 위치에 사각형 그리기
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)

# 결과 이미지 저장
cv2.imwrite('faces_detected.jpg', image)

# 결과 이미지 표시
cv2.imshow('Faces Detected', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

##### 코드 설명
- `face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')`: Haar Cascade 얼굴 검출기를 로드합니다.
- `faces = face_cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))`: 그레이스케일 이미지에서 얼굴을 검출합니다.
- `cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)`: 검출된 얼굴 위치에 사각형을 그립니다.

#### 실습 과제
1. 위 예제 코드를 실행하여 이미지 로드, 그레이스케일 변환, 얼굴 검출을 해보세요.
2. 이미지를 다른 필터(예: Gaussian Blur)를 적용해보세요.
3. 동영상 파일에서 얼굴을 검출해보세요.
4. 다른 객체(예: 눈, 미소)를 검출해보세요.

아래는 Gaussian Blur를 적용하는 예제입니다.

```python
import cv2

# 이미지 로드
image = cv2.imread('example_image.jpg')

# Gaussian Blur 적용
blurred_image = cv2.GaussianBlur(image, (15, 15), 0)

# 이미지 저장
cv2.imwrite('blurred_image.jpg', blurred_image)

# 이미지 표시
cv2.imshow('Blurred Image', blurred_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

이제 OpenCV를 사용한 컴퓨터 비전의 기본 사용법을 익혔습니다. 궁금한 점이나 추가 설명이 필요하면 언제든지 질문해 주세요!