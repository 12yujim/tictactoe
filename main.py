import pygame

BLACK = (   0,   0,   0)
WHITE = ( 255, 255, 255)
GREEN = (   0, 255,   0)
RED   = ( 255,   0,   0)

pygame.init()

size = (800, 600)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("3D Tic Tac Toe - Lily Chen - Jim Yu")

clock = pygame.time.Clock()

running = True

while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	screen.fill(WHITE)

	pygame.display.flip()

	clock.tick(60)

pygame.quit()