import pygame

pygame.init()


# Set colors.
BLACK = (0,     0,   0)
WHITE = (255, 255, 255)

# Make window.
screen_size = (800, 600)
screen = pygame.display.set_mode(screen_size)
clock = pygame.time.Clock()

game_over = False
player_width = 15
player_height = 90

# Player 1
player_1_x_coord = 50
player_1_y_coord = 300 - (player_height / 2)
player_1_y_speed = 0

# Player 2
player_2_x_coord = 750 - player_width
player_2_y_coord = 300 - (player_height / 2)
player_2_y_speed = 0

# Ball
ball_x = 400
ball_y = 300
ball_speed_x = 3
ball_speed_y = 3
ball_radius = 10


while not game_over:
	
	for event in pygame.event.get():		
		if event.type == pygame.QUIT:
			game_over = True
		elif event.type == pygame.KEYDOWN and pygame.K_ESCAPE == event.key:
			game_over = True
		elif event.type == pygame.KEYDOWN:
			# Player 1
			if pygame.K_w == event.key:
				player_1_y_speed = -3
			elif pygame.K_s == event.key:
				player_1_y_speed = 3
			# Player 2
			if pygame.K_UP == event.key:
				player_2_y_speed = -3
			elif pygame.K_DOWN == event.key:
				player_2_y_speed = 3
		elif event.type == pygame.KEYUP:
			# Player 1
			if pygame.K_w == event.key or pygame.K_s == event.key:
				player_1_y_speed = 0
			# Player 2
			elif pygame.K_UP == event.key or pygame.K_DOWN == event.key:
				player_2_y_speed = 0
		
	### >----- GAME LOGIC
	# Ball limits
	if ball_y > 590 or ball_y < 10:
		ball_speed_y *= -1
	# If the ball goes off right side...
	if ball_x > 800:
		ball_x = 400
		ball_y = 300
		# If the ball goes off the screen, reverse direction.
		ball_speed_x *= -1
		ball_speed_y *= -1

	# If the ball goes off left side...
	if ball_x < 0:
		ball_x = 400
		ball_y = 300
		# If the ball goes off the screen, reverse direction.
		ball_speed_x *= -1
		ball_speed_y *= -1

	# Players
	player_1_y_coord += player_1_y_speed
	player_2_y_coord += player_2_y_speed
	# Ball
	ball_x += ball_speed_x
	ball_y += ball_speed_y
	### -----< GAME LOGIC

	# Set background.
	screen.fill(BLACK)
	
	### >----- DRAW ZONE
	player_1 = pygame.draw.rect(screen, WHITE, (player_1_x_coord, player_1_y_coord, player_width, player_height))
	player_2 = pygame.draw.rect(screen, WHITE, (player_2_x_coord, player_2_y_coord, player_width, player_height))
	ball = pygame.draw.circle(screen, WHITE, (ball_x, ball_y), ball_radius)
	### -----< DRAW ZONE
	
	# Collisions
	if ball.colliderect(player_1) or ball.colliderect(player_2):
		ball_speed_x *= -1

	# Refresh screen.
	pygame.display.flip()
	clock.tick(60)

pygame.quit()