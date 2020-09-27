import pygame
pygame.init()

WIDTH = 800
HEIGHT = 800

pygame.display.set_caption('Intro game with python')
win = pygame.display.set_mode((WIDTH, HEIGHT))

x = 400
y = 700

width = 40
height = 60
vel = 10
is_jump = False
jump_count = 10

run = True

while run:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    #block move
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT] and x > vel:
        x -= vel
    if key[pygame.K_RIGHT] and x < 800 - width - vel:
        x += vel
    if not is_jump:
        if key[pygame.K_UP] and y > vel:
            y -= vel
        if key[pygame.K_DOWN] and y < 800 - height - vel:
            y += vel
        if key[pygame.K_SPACE]:
            is_jump = True
    else:
        if jump_count >= -10:
            neg = 1
            height = 40
            if jump_count < 0:
                neg = -1

            y -= (jump_count ** 2) * 0.5 * neg
            jump_count -= 1
        else:
            is_jump = False
            jump_count = 10
            height = 60

    #end block move
    win.fill((0,0,0))
    pygame.draw.rect(win, (255,0,0), (x,y,width,height))
    pygame.display.update()