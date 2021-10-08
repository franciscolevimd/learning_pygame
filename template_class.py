import pygame


# Set colors.
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Set screen dimensions.
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 600

# Others constants.
FPS = 60


class Game(object):
    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            elif event.type == pygame.KEYDOWN and pygame.K_ESCAPE == event.key:
                return True
        return False

    def run_logic(self):
        pass

    def display_frame(self, screen):
        screen.fill(WHITE)
        pygame.display.flip()


def main():
    pygame.init()
    screen = pygame.display.set_mode([SCREEN_HEIGHT, SCREEN_WIDTH])
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
