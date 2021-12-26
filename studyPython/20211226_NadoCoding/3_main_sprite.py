# 1. 오락실 게임 만들기 - (2) 배경 만들기 연습
# https://youtu.be/Dkx8Pl6QKW0

import pygame

pygame.init()    # 초기화 (반드시 필요)

# 화면크기 설정
screen_width = 600      # 배경 가로 크기
screen_height = 800     # 배경 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Cloud Practice Game")   # 게임 이름

# 배경 이미지 불러오기
background = pygame.image.load("E:/OneDrive/바탕 화면/dailyPractice/dailyPractice/studyPython/20211226_NadoCoding/background.png")

# 스프라이트 (캐릭터) 불러오기
character = pygame.image.load("E:/OneDrive/바탕 화면/dailyPractice/dailyPractice/studyPython/20211226_NadoCoding/character.png")
character_size = character.get_rect().size  # 사각형 이미지의 크기를 구해옴 (랙탱글)
character_width = character_size[0]         # 캐릭터의 가로 크기
character_height = character_size[1]        # 캐릭터의 세로 크기
character_x_pos = (screen_width - character_width) / 2           # (화면 가로 - 캐릭터 가로)의 절반 > 가운데 위치
character_y_pos = (screen_height - character_height)             # (화면 세로 - 캐릭터 세로)의 가장 아래 > 바닥 위치
# 좌표들이 4사분면처럼 그려지기 때문에 그려지는 기준점을 잘 설정 해 주어야 함

# 이벤트 루프 : 이것이 실행되어 있어야 창이 꺼지지 않음
running = True  # 게임이 진행중인가?
while running : 
    for event in pygame.event.get() :   # 어떤 이벤트가 발생했나?
        if event.type == pygame.QUIT :  # 창이 닫히는 이벤트가 발생하였는가?
            running = False             # 게임이 실행중이 아닌 이벤트 발생

    screen.blit(background, (0, 0))     # blit 을 통한 배경 그리기
    screen.blit(character, (character_x_pos, character_y_pos))     # blit 을 통한 배경 그리기

    pygame.display.update()             # 게임 화면을 다시 그려줌 (pygame에서는 배경을 불러오기위해 필수로 써야함)

# pygame 종료처리
pygame.quit()