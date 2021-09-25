import pygame

pygame.init()


# Set colors.
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Make window.
screen_size = (800, 600)
screen = pygame.display.set_mode(screen_size)
clock = pygame.time.Clock()

game_over = False


while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN and pygame.K_ESCAPE == event.key:
            game_over = True
    ### >----- GAME LOGIC
    ### -----< GAME LOGIC
    # Set background.
    screen.fill(BLACK)
    ### >----- DRAW ZONE
    ### -----< DRAW ZONE
    # Collisions
    # Refresh screen.
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
