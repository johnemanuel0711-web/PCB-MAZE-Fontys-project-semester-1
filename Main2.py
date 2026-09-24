import pygame
pygame.init()
WIDTH=1280
HEIGHT=720
MOVE_SPEED=3.5
PLAYER_RADIUS=5

NEON_GREEN=(20,255,145)
BACKGROUND=(3,18,14)
WALL_GREEN=(0,185,110)
PORT_WHITE=(255,255,255)

screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("PCB MAZE")

clock=pygame.time.Clock()
game_over_font=pygame.font.SysFont("consolas",60,bold=True)
title_font=pygame.font.SysFont("consolas",28,bold=True)
ui_font=pygame.font.SysFont("consolas",18)

player_position=pygame.Vector2(150,535)
player_trail=[]

UP=pygame.Vector2(0,-1)
DOWN=pygame.Vector2(0,1)
LEFT=pygame.Vector2(-1,0)
RIGHT=pygame.Vector2(1,0)

direction=RIGHT
game_over=False
game_won=False
game_started=False
current_level=1
play_area=pygame.Rect(140,60,1100,640)
start_port=pygame.Rect(140,485,35,100)
exit_port=pygame.Rect(1205,170,35,110)

level_1_blocks = [
    pygame.Rect(240, 90, 360, 55),
    pygame.Rect(240, 145, 120, 210),
    pygame.Rect(400, 145, 200, 45),
    pygame.Rect(400, 190, 55, 280),
    pygame.Rect(455, 315, 145, 170),

    pygame.Rect(650, 60, 70, 170),
    pygame.Rect(650,250,70,310),

    pygame.Rect(770, 80, 340, 120),
    pygame.Rect(770, 225, 340, 100),

    pygame.Rect(770, 380, 250, 120),
    pygame.Rect(1050,370,70,160),
    pygame.Rect(1120, 460, 80, 70),
    pygame.Rect(760, 560, 480, 140),
    pygame.Rect(300, 500, 120, 200),
    pygame.Rect(1130,280,110,60),
    pygame.Rect(600, 470, 60,170)
]
level_2_blocks = [
    
    pygame.Rect(300,60,60,490),
    pygame.Rect(470,210,60,490),
    pygame.Rect(640,60,60,490),
    pygame.Rect(810,210,60,490),
    pygame.Rect(980,60,60,490),
    pygame.Rect(1130,300,50,400),

    
    pygame.Rect(360,500,80,24),
    pygame.Rect(390,420,80,24),
    pygame.Rect(360,340,80,24),
    pygame.Rect(390,260,80,24),

   
    pygame.Rect(530,260,80,24),
    pygame.Rect(560,340,80,24),
    pygame.Rect(530,420,80,24),
    pygame.Rect(560,500,80,24),

    
    pygame.Rect(700,500,80,24),
    pygame.Rect(730,420,80,24),
    pygame.Rect(700,340,80,24),
    pygame.Rect(730,260,80,24),

   
    pygame.Rect(870,260,80,24),
    pygame.Rect(900,340,80,24),
    pygame.Rect(870,420,80,24),
    pygame.Rect(900,500,80,24),

   
    pygame.Rect(1040,500,60,24),
    pygame.Rect(1070,420,60,24),
    pygame.Rect(1040,340,60,24)


]
level_3_blocks = [
    
    pygame.Rect(240,90,360,55),
    pygame.Rect(240,145,120,210),
    pygame.Rect(400,145,200,45),
    pygame.Rect(400,190,55,280),
    pygame.Rect(455,315,145,170),
    pygame.Rect(300,500,120,200),
    pygame.Rect(600,470,60,170),

  
    pygame.Rect(650,60,70,170),
    pygame.Rect(650,260,70,300),

  
    pygame.Rect(770,60,60,440),
    pygame.Rect(930,230,60,470),
    pygame.Rect(1090,60,60,440),

   
    pygame.Rect(830,430,65,24),
    pygame.Rect(865,350,65,24),
    pygame.Rect(830,270,65,24),

    
    pygame.Rect(990,270,65,24),
    pygame.Rect(1025,350,65,24),
    pygame.Rect(990,430,65,24),
    pygame.Rect(140,450,90,25),
    pygame.Rect(200,390,200,25),
    pygame.Rect(1150,420,55,25),
    pygame.Rect(1185,330,55,25)
]
pcb_blocks=level_1_blocks


grid_surface=pygame.Surface((WIDTH,HEIGHT))
grid_surface.fill(BACKGROUND)

for x in range(play_area.left,play_area.right,20):
    for y in range(play_area.top,play_area.bottom,20):
        pygame.draw.circle(grid_surface,(8,42,30),(x,y),1)

grid_surface=grid_surface.convert()
player_glow=pygame.Surface((40,40),pygame.SRCALPHA)
pygame.draw.circle(player_glow,(20,255,145,25),(20,20),18)
pygame.draw.circle(player_glow,(20,255,145,55),(20,20),11)
running=True

while running:
    clock.tick(60)
    pygame.display.set_caption(f"PCB MAZE | FPS: {clock.get_fps():.0f}")

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        if event.type==pygame.KEYDOWN:
            if event.key in (
                pygame.K_w, pygame.K_UP,
                pygame.K_s, pygame.K_DOWN,
                pygame.K_a, pygame.K_LEFT,
                pygame.K_d, pygame.K_RIGHT
            ):
                game_started=True
            if event.key in (pygame.K_w,pygame.K_UP):
                direction=UP
            elif event.key in (pygame.K_s,pygame.K_DOWN):
                direction=DOWN
            elif event.key in (pygame.K_a,pygame.K_LEFT):
                direction=LEFT
            elif event.key in (pygame.K_d,pygame.K_RIGHT):
                direction=RIGHT
            elif event.key==pygame.K_r and (game_over or game_won):
                player_position=pygame.Vector2(150,535)
                player_trail=[]
                direction=RIGHT
                game_over=False
                game_won=False
                game_started=False
            elif event.key==pygame.K_n and game_won:
                current_level+=1

                if current_level>3:
                    current_level=1

                if current_level==1:
                    pcb_blocks=level_1_blocks
                elif current_level==2:
                    pcb_blocks=level_2_blocks
                elif current_level==3:
                    pcb_blocks=level_3_blocks

                player_position=pygame.Vector2(150,535)
                player_trail=[]
                direction=RIGHT
                game_over=False
                game_won=False
                game_started=False
    if game_started and not game_over and not game_won:
        player_position+=direction*MOVE_SPEED
        player_trail.append(player_position.copy())
        for trail_point in player_trail[:-4]:
              if player_position.distance_to(trail_point)<PLAYER_RADIUS+3:
                    game_over=True
    if (
        player_position.x - PLAYER_RADIUS <= play_area.left
        or player_position.x + PLAYER_RADIUS >= play_area.right
        or player_position.y - PLAYER_RADIUS <= play_area.top
        or player_position.y + PLAYER_RADIUS >= play_area.bottom
    ):
        game_over = True
    player_hitbox = pygame.Rect(
    player_position.x - PLAYER_RADIUS,
    player_position.y - PLAYER_RADIUS,
    PLAYER_RADIUS * 2,
    PLAYER_RADIUS * 2
    )
    if not game_over and player_hitbox.colliderect(exit_port):
        game_won=True
    for block in pcb_blocks:
        if player_hitbox.colliderect(block):
            game_over = True

    screen.blit(grid_surface,(0,0))
    title_text=title_font.render("PCB MAZE",True,NEON_GREEN)
    screen.blit(title_text,(140,15))
    level_text=title_font.render(f"LEVEL {current_level}/3",True,PORT_WHITE)
    screen.blit(level_text,level_text.get_rect(topright=(1240,15)))

    pygame.draw.rect(screen,NEON_GREEN,play_area,4)
    pygame.draw.rect(screen,PORT_WHITE,start_port)
    pygame.draw.rect(screen,PORT_WHITE,exit_port)

    for block in pcb_blocks:
        pygame.draw.rect(screen,(5,55,38),block)
        pygame.draw.rect(screen,WALL_GREEN,block,2)
    if len(player_trail)>1:
          trail_points=[(int(point.x),int(point.y))for point in player_trail]
          pygame.draw.lines(screen,(5,55,35),False,trail_points,9)
          pygame.draw.lines(screen,(10,110,65),False,trail_points,5)
          pygame.draw.lines(screen,NEON_GREEN,False,trail_points,3)
    screen.blit(player_glow,(int(player_position.x)-20,int(player_position.y)-20))
    pygame.draw.circle(
        screen,
        NEON_GREEN,
        (
            int(player_position.x),
            int(player_position.y)
        ),
        PLAYER_RADIUS
    )
    if game_over or game_won:
        result_panel=pygame.Rect(0,0,600,180)
        result_panel.center=(WIDTH//2,HEIGHT//2+20)
        pygame.draw.rect(screen,(3,25,18),result_panel)
        pygame.draw.rect(screen,NEON_GREEN,result_panel,2)
    if game_over:
        game_over_text=game_over_font.render("L0S3R",True,NEON_GREEN)
        screen.blit(game_over_text,game_over_text.get_rect(center=(WIDTH//2,HEIGHT//2)))
    if game_won:
        if current_level==3:
            message="SYSTEM HACKED"
        else:
            message="ACCESS GRANTED"

        win_text=game_over_font.render(message,True,PORT_WHITE)
        screen.blit(win_text,win_text.get_rect(center=(WIDTH//2,HEIGHT//2)))
    if game_over or game_won:
        if game_won and current_level==3:
            hint="N: BACK TO LEVEL 1   |   R: REPLAY LEVEL"
        elif game_won:
            hint="N: NEXT LEVEL   |   R: REPLAY LEVEL"
        else:
            hint="R: REPLAY LEVEL"

        restart_text=ui_font.render(hint,True,PORT_WHITE)
        screen.blit(restart_text,restart_text.get_rect(center=(WIDTH//2,HEIGHT//2+55)))
    pygame.display.flip()
pygame.quit()

