import pygame
pygame.init()

WIDTH = 852
HEIGHT = 480

pygame.display.set_caption('Intro game with python')
win = pygame.display.set_mode((WIDTH, HEIGHT))
player_walk_right = [
    pygame.image.load('assets/R1.png'),
    pygame.image.load('assets/R2.png'),
    pygame.image.load('assets/R3.png'),
    pygame.image.load('assets/R4.png'),
    pygame.image.load('assets/R5.png'),
    pygame.image.load('assets/R6.png'),
    pygame.image.load('assets/R7.png'),
    pygame.image.load('assets/R8.png'),
    pygame.image.load('assets/R9.png'),]

player_walk_left = [
    pygame.image.load('assets/L1.png'),
    pygame.image.load('assets/L2.png'),
    pygame.image.load('assets/L3.png'),
    pygame.image.load('assets/L4.png'),
    pygame.image.load('assets/L5.png'),
    pygame.image.load('assets/L6.png'),
    pygame.image.load('assets/L7.png'),
    pygame.image.load('assets/L8.png'),
    pygame.image.load('assets/L9.png'),]

background_image = pygame.image.load('assets/bg.jpg')
player_idle = pygame.image.load('assets/standing.png')

clock = pygame.time.Clock()

class Player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.is_jump = False
        self.jump_count = 5
        self.left = False
        self.right = False
        self.walk_count = 0
        self.standing = True

    def draw(self, win):
        if player.walk_count  + 1 >= 27:
            player.walk_count = 0

        if not self.standing:
            if player.left:
                win.blit(player_walk_left[player.walk_count // 3], (player.x,player.y))
                player.walk_count +=1
            elif player.right:
                win.blit(player_walk_right[player.walk_count // 3], (player.x,player.y))
                player.walk_count += 1
        else:
            if self.right:
                win.blit(player_walk_right[0],(self.x, self.y))
            else:
                win.blit(player_walk_left[0],(self.x, self.y))
            


    def move(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE]:
            if player.left:
                facing = -1
            else:
                facing = 1
            if len(bullets) < 3:
                bullets.append(Projectile(round(player.x + player.width // 2), round(player.y + player.height // 2), 6, (255,0,0), facing))
        
        if key[pygame.K_LEFT] and player.x > player.vel:
            player.x -= player.vel
            player.left = True
            player.right = False
            player.standing = False
        elif key[pygame.K_RIGHT] and player.x < WIDTH - player.width - player.vel:
            player.x += player.vel
            player.left = False
            player.right = True
            player.standing = False
        else:
            # player.left = False
            # player.right = False
            player.standing = True
            player.walk_count = 0
        if not player.is_jump:
            if key[pygame.K_UP]:
                player.is_jump = True
                player.left = False
                player.right = False
                player.walk_count = 0
        else:
            if player.jump_count >= -5:
                neg = 1
                player.height = 40
                if player.jump_count < 0:
                    neg = -1
                player.y -= (player.jump_count ** 2) * 0.5 * neg
                player.jump_count -= 1
            else:
                player.is_jump = False
                player.jump_count = 5
                # height = 32

        # end block move
class Projectile(object):
    def __init__(self,x,y,radius,color,facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 8 * facing

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)


player = Player(300,400,64,64)
run = True
bullets = []
bullet_mag = 3

def redraw_game_window():
    win.blit(background_image, (0,0))
    player.draw(win)
    for bullet in bullets:
        bullet.draw(win)
    player.move()
    pygame.display.update()

while run:
    for bullet in bullets:
        if bullet.x < WIDTH and bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))
    clock.tick(27)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    redraw_game_window()


