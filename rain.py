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


radius = 2
coord_list = []
for i in range(60):
	x = random.randint(0, 800)
	y = random.randint(0, 500)
	coord_list.append([x, y])


while True:
	
	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN and pygame.K_ESCAPE == event.key:
			sys.exit()
		elif event.type == pygame.QUIT:
			sys.exit()
	
	### >----- GAME LOGIC
	### -----< GAME LOGIC

	# Set background.
	screen.fill(WHITE)
	
	### >----- DRAW ZONE
	for coord in coord_list:		
		pygame.draw.circle(screen, BLUE, coord, radius)
		coord[1] += 1
		if coord[1] > 500:
			coord[0] = random.randint(0, 800)
			coord[1] = 0
	### -----< DRAW ZONE
	
	# Refresh screen.
	pygame.display.flip()
	clock.tick(60)