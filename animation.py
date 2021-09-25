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
clock = pygame.time.Clock()

# Square position.
cord_x = 400
cord_y = 200

# square speed.
speed_x = 3
speed_y = 3


while True:
	
	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN and pygame.K_ESCAPE == event.key:
			sys.exit()
		elif event.type == pygame.QUIT:
			sys.exit()
	
	### >----- GAME LOGIC
	if cord_x > 720 or cord_x < 0:
		speed_x *= -1
	if cord_y > 420 or cord_y < 0:
		speed_y *= -1
	cord_x += speed_x
	cord_y += speed_y
	### -----< GAME LOGIC

	# Set background.
	screen.fill(WHITE)
	
	### >----- DRAW ZONE
	pygame.draw.rect(screen, RED, (cord_x, cord_y, 80, 80))
	### -----< DRAW ZONE
	
	# Refresh screen.
	pygame.display.flip()
	clock.tick(60)