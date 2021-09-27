import random
import pygame

# Set colors.
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


class Meteor(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('meteor.png').convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()


class Ship(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('ship.png').convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()


pygame.init()

# Make window.
screen_size = (900, 600)
screen = pygame.display.set_mode(screen_size)
clock = pygame.time.Clock()
game_over = False
score = 0

meteors = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()

for i in range(50):
    meteor = Meteor()
    meteor.rect.x = random.randrange(900)
    meteor.rect.y = random.randrange(600)
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
    mouse_pos = pygame.mouse.get_pos()
    ship.rect.x = mouse_pos[0]
    ship.rect.y = mouse_pos[1]
    meteors_hit = pygame.sprite.spritecollide(ship, meteors, True)
    for meteor in meteors_hit:
        score += 1
        print(score)
    # -----< GAME LOGIC
    # Set background.
    screen.fill(WHITE)
    # >----- DRAW ZONE
    all_sprites.draw(screen)
    # -----< DRAW ZONE
    # Refresh screen.
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
