import pygame
import random


# Set colors.
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Set screen dimensions.
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 600

# Others constants.
FPS = 60
METEOR_SPRITE_NAME = 'meteor.png'
SHIP_SPRITE_NAME = 'ship.png'
TOTAL_METEORS = 50


class Meteor(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(METEOR_SPRITE_NAME).convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.y += 1
        if self.rect.y > SCREEN_HEIGHT:
            self.rect.y = -10
            self.rect.x = random.randrange(SCREEN_WIDTH)


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


class Game(object):
    def __init__(self):
        self.score = 0
        self.meteors = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()
        for i in range(TOTAL_METEORS):
            meteor = Meteor()
            meteor.rect.x = random.randrange(SCREEN_WIDTH)
            meteor.rect.y = random.randrange(SCREEN_WIDTH)
            self.meteors.add(meteor)
            self.all_sprites.add(meteor)
        self.ship = Ship()
        self.all_sprites.add(self.ship)

    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            elif event.type == pygame.KEYDOWN and pygame.K_ESCAPE == event.key:
                return True
        return False

    def run_logic(self):
        self.all_sprites.update()
        meteors_hit = pygame.sprite.spritecollide(
            self.ship, self.meteors, True)
        for meteor in meteors_hit:
            self.score += 1
            print(self.score)

    def display_frame(self, screen):
        screen.fill(WHITE)
        self.all_sprites.draw(screen)
        pygame.display.flip()


def main():
    pygame.init()
    screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
    done = False
    clock = pygame.time.Clock()
    game = Game()
    while not done:
        done = game.process_events()
        game.run_logic()
        game.display_frame(screen)
        clock.tick(FPS)
    pygame.quit()


if __name__ == '__main__':
    main()
