import pygame, sys


pygame.init()


# Set colors.
BLACK = (0,     0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE  = (  0,   0, 255)


# Make window.
size = (800, 500)
screen = pygame.display.set_mode(size)


while True:
	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN and pygame.K_ESCAPE == event.key:
			sys.exit()
		elif event.type == pygame.QUIT:
			sys.exit()
	# Set background.
	screen.fill(WHITE)
	### >----- DRAW ZONE
	pygame.draw.line(screen, GREEN, [10, 110], [210, 300], 5)
	pygame.draw.rect(screen, BLACK, (100, 100, 80, 80))
	pygame.draw.circle(screen, BLACK, (300, 80), 32) 
	### -----< DRAW ZONE
	# Refresh screen.
	pygame.display.flip()