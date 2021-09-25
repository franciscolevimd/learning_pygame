import pygame

pygame.init()


# Set colors.
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Make window.
screen_size = (750, 236)
screen = pygame.display.set_mode(screen_size)
clock = pygame.time.Clock()

game_over = False
background = pygame.image.load('background.png').convert()


while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN and pygame.K_ESCAPE == event.key:
            game_over = True
    # Set background.
    screen.blit(background, [0, 0])
    # Refresh screen.
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
