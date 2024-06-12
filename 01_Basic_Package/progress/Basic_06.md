좋습니다! 이제 4단계로 넘어가서 **Pygame**을 사용한 상호작용형 그래픽스를 공부해보겠습니다. Pygame은 주로 게임 개발에 사용되는 라이브러리로, 그래픽스와 소리를 쉽게 다룰 수 있게 해줍니다.

### 4단계: Pygame 기본 사용법

#### 이론
Pygame은 게임 개발을 위한 Python 라이브러리로, 기본적인 구성 요소는 다음과 같습니다:
- **스크린 (Screen)**: 게임이 그려지는 창
- **이벤트 루프 (Event Loop)**: 사용자의 입력을 처리하고, 게임 상태를 업데이트하며, 화면을 다시 그리는 반복 루프
- **색상 (Colors)**: 화면에 그릴 색상
- **도형 (Shapes)**: 화면에 그릴 다양한 도형

#### 실습: Pygame 기본 사용법

##### Pygame 설치
먼저, Pygame을 설치해야 합니다. 아래 명령어를 사용하여 설치합니다.

```bash
pip install pygame
```

##### 예제 코드: 간단한 Pygame 창 열기
아래 코드는 간단한 Pygame 창을 열고, 창을 닫을 때까지 실행되는 기본적인 이벤트 루프를 포함합니다.

```python
import pygame
import sys

# Pygame 초기화
pygame.init()

# 스크린 설정
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

    # 화면 업데이트
    pygame.display.flip()

# 종료
pygame.quit()
sys.exit()
```

##### 코드 설명
- `pygame.init()`: Pygame을 초기화합니다.
- `pygame.display.set_mode((640, 480))`: 640x480 크기의 스크린을 생성합니다.
- `pygame.display.set_caption('Pygame Example')`: 창의 제목을 설정합니다.
- `while running`: 메인 루프입니다. 창이 닫힐 때까지 반복됩니다.
- `for event in pygame.event.get()`: 이벤트를 처리합니다.
- `if event.type == pygame.QUIT`: 창을 닫는 이벤트가 발생하면 루프를 종료합니다.
- `screen.fill(black)`: 화면을 검은색으로 채웁니다.
- `pygame.display.flip()`: 화면을 업데이트합니다.
- `pygame.quit()`: Pygame을 종료합니다.
- `sys.exit()`: 프로그램을 종료합니다.

#### 실습 과제
1. 위 코드를 실행하여 Pygame 창이 열리는지 확인해보세요.
2. 화면에 간단한 도형을 그려보세요 (예: 원, 사각형).

##### 예제 코드: 도형 그리기
아래 코드는 화면에 원과 사각형을 그리는 예제입니다.

```python
import pygame
import sys

# Pygame 초기화
pygame.init()

# 스크린 설정
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Pygame Example')

# 색상 정의
black = (0, 0, 0)
white = (255, 255, 255)
blue = (0, 0, 255)

# 메인 루프
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 화면 색상 채우기
    screen.fill(black)

    # 도형 그리기
    pygame.draw.circle(screen, white, (320, 240), 50)  # 원
    pygame.draw.rect(screen, blue, (150, 100, 100, 50))  # 사각형

    # 화면 업데이트
    pygame.display.flip()

# 종료
pygame.quit()
sys.exit()
```

##### 코드 설명
- `pygame.draw.circle(screen, white, (320, 240), 50)`: 화면에 흰색 원을 그립니다. 원의 중심 좌표는 (320, 240)이고, 반지름은 50입니다.
- `pygame.draw.rect(screen, blue, (150, 100, 100, 50))`: 화면에 파란색 사각형을 그립니다. 사각형의 좌상단 좌표는 (150, 100)이고, 크기는 100x50입니다.

이제 Pygame의 기본 사용법을 익혔습니다. 다음 단계에서는 Pygame을 심화 학습하여 이미지 로드, 소리 추가, 충돌 감지 등을 배워보겠습니다.