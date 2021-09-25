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
	for x in range(100, 700, 100):
		pygame.draw.rect(screen, BLACK, (x, 230, 50, 50))
		pygame.draw.line(screen, BLACK, (x, 10), (x, 110), 3)
	### -----< DRAW ZONE
	# Refresh screen.
	pygame.display.flip()