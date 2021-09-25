import pygame, sys, random


pygame.init()


# Set colors.
BLACK = (0,     0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE  = (  0,   0, 201)
PINK  = (255, 192, 203)

# Make window.
size = (800, 500)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
pygame.mouse.set_visible(0)

# Square coords.
coord_x = 10
coord_y = 10
# Speed
x_speed = 0
y_speed = 0


while True:
	
	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN and pygame.K_ESCAPE == event.key:
			sys.exit()
		elif event.type == pygame.QUIT:
			sys.exit()

		# Keyboard events.
		if event.type == pygame.KEYDOWN:
			if pygame.K_LEFT == event.key:
				x_speed = -3
			if pygame.K_RIGHT == event.key:
				x_speed = 3
			if pygame.K_UP == event.key:
				y_speed = -3
			if pygame.K_DOWN == event.key:
				y_speed = 3
		if event.type == pygame.KEYUP:
			if pygame.K_LEFT == event.key or pygame.K_RIGHT == event.key:
				x_speed = 0
			if pygame.K_UP == event.key or pygame.K_DOWN == event.key:
				y_speed = 0
	
	### >----- GAME LOGIC
	### -----< GAME LOGIC

	# Set background.
	screen.fill(WHITE)
	
	### >----- DRAW ZONE
	coord_x += x_speed
	coord_y += y_speed
	pygame.draw.rect(screen, RED, (coord_x, coord_y, 100, 100))
	### -----< DRAW ZONE
	
	# Refresh screen.
	pygame.display.flip()
	clock.tick(60)