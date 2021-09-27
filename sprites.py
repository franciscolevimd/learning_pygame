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
METEOR_SPRITE_NAME = 'meteor.png'
SHIP_SPRITE_NAME = 'ship.png'


class Meteor(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(METEOR_SPRITE_NAME).convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.y += 1
        if self.rect.y > HEIGHT:
            self.rect.y = -10
            self.rect.x = random.randrange(WIDTH)


class Ship(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(SHIP_SPRITE_NAME).convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()

    def update(self):
        mouse_pos = pygame.mouse.get_pos()
        self.rect.x = mouse_pos[0]
        self.rect.y = mouse_pos[1]


pygame.init()

# Make window.
screen_size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(screen_size)
clock = pygame.time.Clock()
game_over = False
score = 0

meteors = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()

for i in range(TOTAL_METEORS):
    meteor = Meteor()
    meteor.rect.x = random.randrange(WIDTH)
    meteor.rect.y = random.randrange(HEIGHT)
    meteors.add(meteor)
    all_sprites.add(meteor)

ship = Ship()
all_sprites.add(ship)


while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN and pygame.K_ESCAPE == event.key:
            game_over = True
    # >----- GAME LOGIC
    all_sprites.update()
    meteors_hit = pygame.sprite.spritecollide(ship, meteors, True)
    for meteor in meteors_hit:
        score += INCREMENTAL_SCORE
        print(score)
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
