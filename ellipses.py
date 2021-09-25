import pygame, sys


pygame.init()


# Set colors.
BLACK = (0,     0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE  = (  0,   0, 255)
PINK  = (255, 192, 203)


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
	for x in range(100, 760, 150):
		pygame.draw.ellipse(screen, BLACK, [x, 200, 65, 45])
		pygame.draw.ellipse(screen, BLACK, [x + 53, 180, 45, 45])
		pygame.draw.ellipse(screen, BLACK, [x - 40, 185, 45, 45])
	### -----< DRAW ZONE
	# Refresh screen.
	pygame.display.flip()