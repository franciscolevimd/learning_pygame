import random
import pygame

# Set colors.
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Set screen dimensions.
WIDTH = 900
HEIGHT = 600

# Others constants.
FPS = 60
TOTAL_METEORS = 50
INCREMENTAL_SCORE = 1
SHIP_POSITION_Y = 510
METEOR_POSITION_X = 880
METEOR_POSITION_Y = 450
LASER_POSITION_X = 45
LASER_POSITION_Y = 20
END_LASER_ROUTE = -10
LASER_DISPLACEMENT = 5
SHIP_SPRITE_NAME = "ship.png"
METEOR_SPRITE_NAME = "meteor.png"
LASER_SPRITE_NAME = "laser.png"


class Meteor(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(METEOR_SPRITE_NAME)
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()


class Ship(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(SHIP_SPRITE_NAME)
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()

    def update(self):
        mouse_pos = pygame.mouse.get_pos()
        self.rect.x = mouse_pos[0]
        self.rect.y = SHIP_POSITION_Y


class Laser(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(LASER_SPRITE_NAME)
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.y -= LASER_DISPLACEMENT


pygame.init()

# Make window.
screen_size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(screen_size)
clock = pygame.time.Clock()
game_over = False
score = 0

all_sprites = pygame.sprite.Group()
meteors = pygame.sprite.Group()
lasers = pygame.sprite.Group()

ship = Ship()
all_sprites.add(ship)

for i in range(TOTAL_METEORS):
    meteor = Meteor()
    meteor.rect.x = random.randrange(METEOR_POSITION_X)
    meteor.rect.y = random.randrange(METEOR_POSITION_Y)
    meteors.add(meteor)
    all_sprites.add(meteor)


while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN and pygame.K_ESCAPE == event.key:
            game_over = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            laser = Laser()
            laser.rect.x = ship.rect.x + LASER_POSITION_X
            laser.rect.y = ship.rect.y - LASER_POSITION_Y
            all_sprites.add(laser)
            lasers.add(laser)
    # >----- GAME LOGIC
    all_sprites.update()
    for laser in lasers:
        meteors_hit = pygame.sprite.spritecollide(laser, meteors, True)
        for meteor in meteors_hit:
            all_sprites.remove(laser)
            lasers.remove(laser)
            score += INCREMENTAL_SCORE
            print(score)
        if laser.rect.y < END_LASER_ROUTE:
            all_sprites.remove(laser)
            lasers.remove(laser)
    # -----< GAME LOGIC
    # Set background.
    screen.fill(WHITE)
    # >----- DRAW ZONE
    all_sprites.draw(screen)
    # -----< DRAW ZONE
    # Refresh screen.
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
