import pygame

BLACK = (   0,   0,   0)
WHITE = ( 255, 255, 255)
GREEN = (   0, 255,   0)
RED   = ( 255,   0,   0)

pygame.init()

size = (600, 400)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("3D Tic Tac Toe - Lily Chen - Jim Yu")

clock = pygame.time.Clock()

running = True

# game states
BEGIN = 0
PLAY = 1
LEARN = 2
ABOUT = 3

state = BEGIN

while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	screen.fill(WHITE)

	if state == BEGIN:
		# start screen
		myfont = pygame.font.SysFont("monospace", 40)
		play = myfont.render("Play", 1, BLACK)
		learn = myfont.render("Learn", 1, BLACK)
		about = myfont.render("About", 1, BLACK)
		pygame.draw.rect(screen, RED, [225, 50, 175, 90], 2)
		pygame.draw.rect(screen, RED, [225, 150, 175, 90], 2)
		pygame.draw.rect(screen, RED, [225, 250, 175, 90], 2)
		screen.blit(play, (263,75))
		screen.blit(learn, (250, 175))
		screen.blit(about, (250, 275))

	if state == PLAY:
		# draw the board
		xbase1 = 25
		xbase2 = 225
		xbase3 = 425
		for y in [100, 150, 200]:
			for i in range(3):
				add = i * 50
				pygame.draw.rect(screen, GREEN, [xbase1 + add, y, 50, 50], 2)
				if y == 150 and add == 50:
					pygame.draw.rect(screen, BLACK, [xbase2 + add, y, 50, 50])
				else:
					pygame.draw.rect(screen, GREEN, [xbase2 + add, y, 50, 50], 2)
				pygame.draw.rect(screen, GREEN, [xbase3 + add, y, 50, 50], 2)

	if state == ABOUT:
		pass
		
	pygame.display.flip()

	clock.tick(60)

pygame.quit()