# 1. 오락실 게임 만들기 - (5) FPS (Frame per Second)
# https://youtu.be/Dkx8Pl6QKW0

import pygame

pygame.init()    # 초기화 (반드시 필요)

# 화면크기 설정
screen_width = 600      # 배경 가로 크기
screen_height = 800     # 배경 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Cloud Practice Game")   # 게임 이름

# FPS
clock = pygame.time.Clock()


# 배경 이미지 불러오기
background = pygame.image.load("E:/OneDrive/바탕 화면/dailyPractice/dailyPractice/studyPython/20211226_NadoCoding/background.png")

# 스프라이트 (캐릭터) 불러오기
character = pygame.image.load("E:/OneDrive/바탕 화면/dailyPractice/dailyPractice/studyPython/20211226_NadoCoding/character.png")
character_size = character.get_rect().size  # 사각형 이미지의 크기를 구해옴 (랙탱글)
character_width = character_size[0]         # 캐릭터의 가로 크기
character_height = character_size[1]        # 캐릭터의 세로 크기
character_x_pos = (screen_width - character_width) / 2           # (화면 가로 - 캐릭터 가로)의 절반 > 가운데 위치
character_y_pos = (screen_height - character_height)             # (화면 세로 - 캐릭터 세로)의 가장 아래 > 바닥 위치


# 이동할 좌표 지정
to_x = 0
to_y = 0

# 이동 속도
character_speed = 0.6


# 이벤트 루프 : 이것이 실행되어 있어야 창이 꺼지지 않음
running = True  # 게임이 진행중인가?
while running : 
    dt = clock.tick(30)                 # 게임 화면의 초당 프레임 수를 설정해줌
    print("fps : " + str(clock.get_fps()))
    
    # 프레임이 한 10 정도 되면 캐릭터의 이동 속도에 영향을 줌!
    # 캐릭터가 1초 동안에 100 만큼 이동을 해야 하는 상황
    # 10 fps : 1초 동안에 10번 동작 : 1 번에 10 만큼 이동 > 10 * 10 = 100
    # 20 fps : 1초 동안에 20번 동작 : 1 번에 5 만큼 이동 > 5 * 20 = 100
    
    
    for event in pygame.event.get() :   # 어떤 이벤트가 발생했나?
        if event.type == pygame.QUIT :  # 창이 닫히는 이벤트가 발생하였는가?
            running = False             # 게임이 실행중이 아닌 이벤트 발생

        if event.type == pygame.KEYDOWN :       # 키보드가 눌러졌는지 확인
            if event.key == pygame.K_LEFT :     # 캐릭터를 왼쪽으로
                to_x -= character_speed
            if event.key == pygame.K_RIGHT :    # 캐릭터를 오른쪽으로
                to_x += character_speed     
            if event.key == pygame.K_UP :       # 캐릭터를 위로
                to_y -= character_speed
            if event.key == pygame.K_DOWN :     # 캐릭터를 아래로
                to_y += character_speed

        if event.type == pygame.KEYUP :         # 방향키를 떼면 멈추는 이벤트
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT :
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN :
                to_y = 0

    character_x_pos += to_x * dt
    character_y_pos += to_y * dt

    # (가로 경계값 처리) 화면 바깥으로 벗어나지 않도록 조정
    if character_x_pos < 0 :
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width :
        character_x_pos = screen_width - character_width
    
    # (세로 경계값 처리) 화면 바깥으로 벗어나지 않도록 조정
    if character_y_pos < 0 :
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height :
        character_y_pos = screen_height - character_height

    screen.blit(background, (0, 0))     # blit 을 통한 배경 그리기
    screen.blit(character, (character_x_pos, character_y_pos))     # blit 을 통한 배경 그리기

    pygame.display.update()             # 게임 화면을 다시 그려줌 (pygame에서는 배경을 불러오기위해 필수로 써야함)

# pygame 종료처리
pygame.quit()