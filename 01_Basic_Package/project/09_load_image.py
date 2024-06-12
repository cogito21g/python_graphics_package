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
image = pygame.image.load('./assets/image1.png')

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
