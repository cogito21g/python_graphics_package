좋습니다! 이제 5단계로 넘어가서 **Pygame 심화**를 공부해보겠습니다. 이 단계에서는 Pygame을 사용하여 이미지를 로드하고 표시하며, 소리를 추가하고, 충돌 감지를 구현하는 방법을 배웁니다.

### 5단계: Pygame 심화

#### 이론
1. **이미지 로드 및 표시**: 외부 이미지를 게임 화면에 로드하고 표시하는 방법
2. **소리 추가**: 배경 음악이나 효과음을 게임에 추가하는 방법
3. **충돌 감지**: 객체 간의 충돌을 감지하여 게임 로직에 반영하는 방법

#### 실습 1: 이미지 로드 및 표시

##### 예제 코드: 이미지 로드 및 표시
아래 코드는 Pygame을 사용하여 이미지를 로드하고 화면에 표시하는 예제입니다.

```python
import pygame
import sys

# Pygame 초기화
pygame.init()

# 스크린 설정
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Image Load Example')

# 색상 정의
black = (0, 0, 0)

# 이미지 로드
image = pygame.image.load('example_image.png')

# 메인 루프
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 화면 색상 채우기
    screen.fill(black)

    # 이미지 그리기
    screen.blit(image, (100, 100))

    # 화면 업데이트
    pygame.display.flip()

# 종료
pygame.quit()
sys.exit()
```

##### 코드 설명
- `image = pygame.image.load('example_image.png')`: 이미지를 로드합니다. `example_image.png` 파일 경로를 실제 이미지 파일 경로로 대체해야 합니다.
- `screen.blit(image, (100, 100))`: 이미지를 화면에 그립니다. (100, 100)은 이미지가 그려질 좌표입니다.

#### 실습 2: 소리 추가

##### 예제 코드: 소리 추가
아래 코드는 Pygame을 사용하여 배경 음악을 추가하는 예제입니다.

```python
import pygame
import sys

# Pygame 초기화
pygame.init()

# 스크린 설정
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Sound Example')

# 색상 정의
black = (0, 0, 0)

# 배경 음악 로드 및 재생
pygame.mixer.music.load('background_music.mp3')
pygame.mixer.music.play(-1)  # 무한 반복 재생

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
pygame.mixer.music.stop()
pygame.quit()
sys.exit()
```

##### 코드 설명
- `pygame.mixer.music.load('background_music.mp3')`: 배경 음악 파일을 로드합니다. `background_music.mp3` 파일 경로를 실제 음악 파일 경로로 대체해야 합니다.
- `pygame.mixer.music.play(-1)`: 배경 음악을 무한 반복 재생합니다.
- `pygame.mixer.music.stop()`: 프로그램 종료 시 배경 음악을 정지합니다.

#### 실습 3: 충돌 감지

##### 예제 코드: 충돌 감지
아래 코드는 Pygame을 사용하여 두 개의 사각형 객체 간의 충돌을 감지하는 예제입니다.

```python
import pygame
import sys

# Pygame 초기화
pygame.init()

# 스크린 설정
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Collision Detection Example')

# 색상 정의
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)

# 사각형 정의
rect1 = pygame.Rect(150, 100, 100, 50)
rect2 = pygame.Rect(300, 200, 100, 50)

# 메인 루프
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 키보드 입력 처리
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        rect1.x -= 5
    if keys[pygame.K_RIGHT]:
        rect1.x += 5
    if keys[pygame.K_UP]:
        rect1.y -= 5
    if keys[pygame.K_DOWN]:
        rect1.y += 5

    # 충돌 감지
    if rect1.colliderect(rect2):
        color = red
    else:
        color = blue

    # 화면 색상 채우기
    screen.fill(black)

    # 사각형 그리기
    pygame.draw.rect(screen, color, rect1)
    pygame.draw.rect(screen, blue, rect2)

    # 화면 업데이트
    pygame.display.flip()

# 종료
pygame.quit()
sys.exit()
```

##### 코드 설명
- `rect1 = pygame.Rect(150, 100, 100, 50)`: 첫 번째 사각형 객체를 정의합니다.
- `rect2 = pygame.Rect(300, 200, 100, 50)`: 두 번째 사각형 객체를 정의합니다.
- `keys = pygame.key.get_pressed()`: 키보드 입력을 처리합니다.
- `if rect1.colliderect(rect2)`: 두 사각형 객체 간의 충돌을 감지합니다.
- 충돌 시 색상을 빨간색으로 변경하고, 그렇지 않으면 파란색으로 설정합니다.

#### 실습 과제
1. 위 코드를 실행하여 이미지를 로드하고 표시하며, 배경 음악을 추가하고, 사각형 객체 간의 충돌을 감지하는지 확인해보세요.
2. 이미지 대신 다른 이미지를 로드하고 위치를 변경해보세요.
3. 다른 소리를 추가해보세요 (예: 효과음).
4. 충돌 감지 예제에서 사각형 대신 다른 도형이나 이미지를 사용해보세요.

이제 Pygame 심화 단계의 실습을 마치고 나면, 상호작용형 그래픽스를 더 잘 이해하게 될 것입니다. 다음 단계에서는 Turtle 그래픽스를 사용한 간단한 도형 그리기를 배워보겠습니다. 궁금한 점이나 추가 설명이 필요하면 언제든지 질문해 주세요!