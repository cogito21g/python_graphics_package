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
