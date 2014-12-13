import pygame

BLACK = (   0,   0,   0)
WHITE = ( 255, 255, 255)
GREEN = (   0, 255,   0)
RED   = ( 255,   0,   0)
FONT  = "monospace"

class Button:
	mouseOn = False

	def __init__(self, color, rect, content):
		self.color = color
		self.rect = pygame.Rect(rect)
		self.content = content
		self.rend = content_init.render(self.content, 1, BLACK)

	def draw(self):
		pygame.draw.rect(screen, self.color, self.rect, 2)
		textpos = self.rend.get_rect()
		textpos.center = self.rect.center
		screen.blit(self.rend, textpos)

# initialization
pygame.init()
size = (600, 400)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("3D Tic Tac Toe - Lillian Chen & Jim Yu")
clock = pygame.time.Clock()
running = True

# game states
BEGIN = 0
PLAY = 1
LEARN = 2
ABOUT = 3

state = BEGIN

while running:
	screen.fill(WHITE)
	
	# start screen
	if state == BEGIN:
		content_init = pygame.font.SysFont(FONT, 30)
		menu = [Button(BLACK, [225, 50, 150, 80], "Play"),
						Button(BLACK, [225, 150, 150, 80], "Learn"),
						Button(BLACK, [225, 250, 150, 80], "About")]

		for button in menu:
			button.draw()

		for event in pygame.event.get():
			if event.type == pygame.MOUSEBUTTONDOWN:
				for button in menu:
					if button.rect.collidepoint(event.pos):
						if button.content == "Play":
							state = PLAY
						if button.content == "About":
							state = ABOUT
						else:
							pass

	if state == PLAY:
		# draw the board
		xbase1 = 50
		xbase2 = 225
		xbase3 = 400
		for y in [125, 175, 225]:
			for i in range(3):
				add = i * 50
				pygame.draw.rect(screen, BLACK, [xbase1 + add, y, 50, 50], 2)
				if y == 175 and add == 50:
					pygame.draw.rect(screen, BLACK, [xbase2 + add, y, 50, 50])
				else:
					pygame.draw.rect(screen, BLACK, [xbase2 + add, y, 50, 50], 2)
				pygame.draw.rect(screen, BLACK, [xbase3 + add, y, 50, 50], 2)


	if state == ABOUT:
		pass
		
	pygame.display.flip()
	clock.tick(60)

pygame.quit()