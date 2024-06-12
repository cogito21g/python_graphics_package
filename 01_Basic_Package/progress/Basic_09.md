좋습니다! 이제 7단계로 넘어가서 **Pillow를 사용한 이미지 처리**를 공부해보겠습니다. Pillow는 Python Imaging Library (PIL)의 후속 프로젝트로, 이미지 조작을 위한 다양한 기능을 제공합니다.

### 7단계: Pillow를 사용한 이미지 처리

#### 이론
Pillow 라이브러리는 다음과 같은 기능을 제공합니다:
- **이미지 로드 및 저장**: 이미지를 파일에서 로드하고, 파일로 저장하는 기능
- **이미지 조작**: 크기 조정, 자르기, 회전, 색상 변환 등의 이미지 조작 기능
- **그리기**: 이미지 위에 텍스트나 도형을 그리는 기능

#### 설치
먼저 Pillow를 설치해야 합니다. 아래 명령어를 사용하여 설치합니다.

```bash
pip install pillow
```

#### 실습 1: 이미지 로드 및 저장

##### 예제 코드: 이미지 로드 및 저장
아래 코드는 이미지를 로드하고, 새로운 파일로 저장하는 예제입니다.

```python
from PIL import Image

# 이미지 로드
image = Image.open('example_image.jpg')

# 이미지 정보 출력
print(image.format)
print(image.size)
print(image.mode)

# 이미지 저장
image.save('saved_image.png')
```

##### 코드 설명
- `image = Image.open('example_image.jpg')`: 이미지를 로드합니다.
- `print(image.format)`: 이미지 포맷을 출력합니다.
- `print(image.size)`: 이미지 크기를 출력합니다.
- `print(image.mode)`: 이미지 모드를 출력합니다.
- `image.save('saved_image.png')`: 이미지를 새로운 파일로 저장합니다.

#### 실습 2: 이미지 조작

##### 예제 코드: 이미지 크기 조정, 자르기, 회전
아래 코드는 이미지를 크기 조정, 자르기, 회전하는 예제입니다.

```python
from PIL import Image

# 이미지 로드
image = Image.open('example_image.jpg')

# 이미지 크기 조정
resized_image = image.resize((200, 200))
resized_image.save('resized_image.png')

# 이미지 자르기
cropped_image = image.crop((100, 100, 400, 400))
cropped_image.save('cropped_image.png')

# 이미지 회전
rotated_image = image.rotate(45)
rotated_image.save('rotated_image.png')
```

##### 코드 설명
- `resized_image = image.resize((200, 200))`: 이미지를 200x200 크기로 조정합니다.
- `cropped_image = image.crop((100, 100, 400, 400))`: 이미지를 (100, 100)에서 (400, 400)까지 자릅니다.
- `rotated_image = image.rotate(45)`: 이미지를 45도 회전합니다.

#### 실습 3: 이미지에 텍스트 및 도형 그리기

##### 예제 코드: 텍스트 및 도형 그리기
아래 코드는 이미지 위에 텍스트와 도형을 그리는 예제입니다.

```python
from PIL import Image, ImageDraw, ImageFont

# 이미지 로드
image = Image.open('example_image.jpg')
draw = ImageDraw.Draw(image)

# 폰트 설정 (TrueType 폰트 파일 경로 필요)
font = ImageFont.truetype("arial.ttf", 40)

# 텍스트 그리기
draw.text((100, 100), "Hello, Pillow!", fill="white", font=font)

# 사각형 그리기
draw.rectangle((200, 200, 300, 300), outline="red", width=5)

# 이미지 저장
image.save('drawn_image.png')
```

##### 코드 설명
- `draw = ImageDraw.Draw(image)`: 이미지 위에 그리기 위한 객체를 생성합니다.
- `font = ImageFont.truetype("arial.ttf", 40)`: 폰트를 설정합니다 (TrueType 폰트 파일이 필요합니다).
- `draw.text((100, 100), "Hello, Pillow!", fill="white", font=font)`: 텍스트를 그립니다.
- `draw.rectangle((200, 200, 300, 300), outline="red", width=5)`: 사각형을 그립니다.

#### 실습 과제
1. 위 예제 코드를 실행하여 이미지 로드, 저장, 조작, 그리기 작업을 해보세요.
2. 이미지를 흑백으로 변환해보세요.
3. 이미지를 다른 형식(예: JPEG, PNG)으로 저장해보세요.
4. 이미지 위에 원이나 선을 그려보세요.

아래는 이미지를 흑백으로 변환하는 예제입니다.

```python
from PIL import Image

# 이미지 로드
image = Image.open('example_image.jpg')

# 흑백 변환
gray_image = image.convert('L')
gray_image.save('gray_image.png')
```

이제 Pillow를 사용한 이미지 처리의 기본 사용법을 익혔습니다. 다음 단계에서는 OpenCV를 사용한 컴퓨터 비전을 배워보겠습니다. 