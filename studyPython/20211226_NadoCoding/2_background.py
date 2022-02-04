# 1. 오락실 게임 만들기 - (2) 배경 만들기 연습
# https://youtu.be/Dkx8Pl6QKW0

import pygame

pygame.init()    # 초기화 (반드시 필요)

# 화면크기 설정
screen_width = 600      # 가로 크기
screen_height = 800     # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Cloud Practice Game")   # 게임 이름

# 배경 이미지 불러오기
background = pygame.image.load("E:/OneDrive/바탕 화면/dailyPractice/dailyPractice/studyPython/20211226_NadoCoding/background.png")

# 이벤트 루프 : 이것이 실행되어 있어야 창이 꺼지지 않음
running = True  # 게임이 진행중인가?
while running : 
    for event in pygame.event.get() :   # 어떤 이벤트가 발생했나?
        if event.type == pygame.QUIT :  # 창이 닫히는 이벤트가 발생하였는가?
            running = False             # 게임이 실행중이 아닌 이벤트 발생

    screen.blit(background, (0, 0))     # blit 을 통한 배경 그리기
    # screen.fill((0, 0, 255))              # RGB 값으로도 배경을 채울 수 있음 (참고)

    pygame.display.update()             # 게임 화면을 다시 그려줌 (pygame에서는 배경을 불러오기위해 필수로 써야함)

# pygame 종료처리
pygame.quit()