Python을 사용하여 그래픽스를 공부하는 것은 매우 흥미로운 주제입니다. Python에는 그래픽스를 다루기 위한 다양한 라이브러리와 도구가 있습니다. 다음은 Python 그래픽스를 공부하는 데 도움이 되는 주요 라이브러리와 간단한 예제입니다:

1. **Matplotlib**: 2D 그래픽스를 위한 가장 널리 사용되는 라이브러리 중 하나입니다. 간단한 플롯부터 복잡한 그래프까지 다양한 그래픽스를 그릴 수 있습니다.
2. **Pygame**: 게임 개발과 같은 상호작용형 그래픽스를 위한 라이브러리입니다.
3. **Turtle**: Python의 기본 모듈로 간단한 그림을 그리는 데 사용됩니다. 주로 교육용으로 사용됩니다.
4. **Pillow**: 이미지 처리를 위한 라이브러리로, 기존 이미지를 조작하거나 새 이미지를 생성할 수 있습니다.
5. **OpenCV**: 컴퓨터 비전 라이브러리로, 이미지 및 비디오 처리를 위한 강력한 도구를 제공합니다.

각 라이브러리에 대한 간단한 예제를 소개하겠습니다.

### Matplotlib 예제
```python
import matplotlib.pyplot as plt
import numpy as np

# 데이터 생성
x = np.linspace(0, 10, 100)
y = np.sin(x)

# 그래프 생성
plt.plot(x, y)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Sine Wave')
plt.show()
```

### Pygame 예제
```python
import pygame
import sys

# 초기화
pygame.init()

# 화면 설정
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Pygame Example')

# 색상 정의
black = (0, 0, 0)
white = (255, 255, 255)

# 메인 루프
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 화면 색상 채우기
    screen.fill(black)

    # 원 그리기
    pygame.draw.circle(screen, white, (320, 240), 50)

    # 화면 업데이트
    pygame.display.flip()

# 종료
pygame.quit()
sys.exit()
```

### Turtle 예제
```python
import turtle

# 캔버스 설정
screen = turtle.Screen()
screen.bgcolor("white")

# 거북이 객체 생성
t = turtle.Turtle()
t.shape("turtle")
t.color("blue")

# 사각형 그리기
for _ in range(4):
    t.forward(100)
    t.right(90)

# 종료
turtle.done()
```

### Pillow 예제
```python
from PIL import Image, ImageDraw

# 새 이미지 생성
image = Image.new('RGB', (200, 200), 'white')
draw = ImageDraw.Draw(image)

# 사각형 그리기
draw.rectangle([50, 50, 150, 150], outline='blue', width=5)

# 이미지 저장
image.save('rectangle.png')
```

### OpenCV 예제
```python
import cv2

# 이미지 로드
image = cv2.imread('example.jpg')

# 그레이스케일 변환
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 이미지 표시
cv2.imshow('Grayscale Image', gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

위 예제들은 각 라이브러리의 기본적인 사용법을 소개합니다. 이들을 기반으로 더 복잡한 그래픽스를 만들어 나가면 됩니다. 추가로, 각 라이브러리의 공식 문서와 튜토리얼을 참고하여 더욱 깊이 있는 학습을 할 수 있습니다.