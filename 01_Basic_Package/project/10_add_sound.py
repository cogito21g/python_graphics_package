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
pygame.mixer.music.load('./assets/background_music.mp3')
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
