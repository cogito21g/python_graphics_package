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
        rect1.x -= 1
    if keys[pygame.K_RIGHT]:
        rect1.x += 1
    if keys[pygame.K_UP]:
        rect1.y -= 1
    if keys[pygame.K_DOWN]:
        rect1.y += 1

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
