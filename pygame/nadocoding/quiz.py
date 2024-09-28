import pygame
import random
########################################################################
pygame.init() #초기화 (파이게임에서 반드시 필요)


#화면 크기 설정
screen_width = 480 # 가로 크기
screen_height = 640 # 세로 크기

screen = pygame.display.set_mode((screen_width, screen_height))

#화면 타이틀 설정
pygame.display.set_caption("QUIZ") #게임이름

#FPS
clock = pygame.time.Clock()

#배경
background = pygame.image.load("C:\\workspace\\99_python\\pygame\\background.png")

#캐릭터
character =  pygame.image.load("C:\\workspace\\99_python\\pygame\\character.png")
character_size = character.get_rect().size #이미지의 크기를 구해옴
character_width = character_size[0] #캐릭터의 가로 크기
character_height = character_size[1] #캐릭터의 세로 크기
character_x_pos = (screen_width / 2) - (character_width/2)  #화면 가로의 절반 크기에 해당하는 곳에 위치(가로)
character_y_pos = screen_height - character_height #화면 세로 크기 가장 아래에 해당하는 곳에 위치(세로)

#이동 위치
to_x = 0

character_speed = 0.6

#똥 만들기
ddong =  pygame.image.load("C:\\workspace\\99_python\\pygame\\enemy.png")
ddong_size = ddong.get_rect().size #이미지의 크기를 구해옴
ddong_width = ddong_size[0] #캐릭터의 가로 크기
ddong_height = ddong_size[1] #캐릭터의 세로 크기
ddong_x_pos = random.randint(0, screen_width -ddong_width)  #화면 가로의 절반 크기에 해당하는 곳에 위치(가로)
ddong_y_pos = 0 #화면 세로 크기 가장 아래에 해당하는 곳에 위치(세로)
ddong_speed =6

# 폰트 정의
game_font = pygame.font.Font(None, 40) #폰트 객체 생성(폰트, 크기)

# 총 시간
total_time = 30

# 시작 시간 정보
start_ticks = pygame.time.get_ticks() #현재 tick 을 받아옴

running = True

while running:
    dt=clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN: # 키가 눌러졌는지 확인
            if event.key == pygame.K_LEFT: # 캐릭터를 왼쪽으로
                to_x -= character_speed #to_x = to_x -5
            elif event.key == pygame.K_RIGHT: #캐릭터를 오른쪽으로
                to_x += character_speed

    if event.type == pygame.KEYUP :
        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            to_x = 0

    # 3. 게임 캐릭터의 위치 정의
    character_x_pos += to_x *dt

    #나가지 말도록
    if character_x_pos < 0 :
        character_x_pos=0
    
    elif character_x_pos> screen_width - character_width :
        character_x_pos = screen_width - character_width

    ddong_y_pos+= ddong_speed

    if ddong_y_pos > screen_height:
        ddong_y_pos = 0
        ddong_x_pos = random.randint(0, screen_width - ddong_width)

    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    ddong_rect = ddong.get_rect()
    ddong_rect.left = ddong_x_pos
    ddong_rect.top =ddong_y_pos

    if character_rect.colliderect(ddong_rect):
        print("충돌했어요")
        running = False

    screen.blit(background, (0,0))
    screen.blit(character, (character_x_pos, character_y_pos))
    screen.blit(ddong, (ddong_x_pos, ddong_y_pos))

    pygame.display.update()


pygame.quit()