import pygame

pygame.init()


# Set colors.
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Make window.
screen_size = (720, 720)
screen = pygame.display.set_mode(screen_size)
clock = pygame.time.Clock()
pygame.mouse.set_visible(0)

game_over = False
background = pygame.image.load('background_2.png').convert()
character = pygame.image.load('ship.png').convert()
character.set_colorkey(BLACK)

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN and pygame.K_ESCAPE == event.key:
            game_over = True
    # >----- GAME LOGIC
    mouse_pos = pygame.mouse.get_pos()
    x = mouse_pos[0]
    y = mouse_pos[1]
    # -----< GAME LOGIC
    # Set background.
    screen.blit(background, [0, 0])
    screen.blit(character, [x, y])
    # Refresh screen.
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
