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

	def draw(self):
		self.rend = content_init.render(self.content, 1, BLACK)
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
player = 1

# draw the board
squares = []
for y in [125, 175, 225]:
	for i in range(3):
		add = i * 50
		squares.append(Button(BLACK, [50 + add, y, 50, 50], ""))
		if y == 175 and add == 50:
			pass
		else:
			squares.append(Button(BLACK, [225 + add, y, 50, 50], ""))
		squares.append(Button(BLACK, [400 + add, y, 50, 50], ""))

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
			if event.type == pygame.QUIT:
				running = False
			elif event.type == pygame.MOUSEBUTTONDOWN:
				for button in menu:
					if button.rect.collidepoint(event.pos):
						if button.content == "Play":
							state = PLAY
						if button.content == "About":
							state = ABOUT
						else:
							pass

	if state == PLAY:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
			if event.type == pygame.MOUSEBUTTONDOWN:
				for square in squares:
					if square.rect.collidepoint(event.pos):
						if player == 1:
							square.content = "X"
							player = 2
						elif player == 2:
							square.content = "O"
							player = 1

		for square in squares:
			square.draw()
		pygame.draw.rect(screen, BLACK, [275, 175, 50, 50])

	if state == ABOUT:
		pass
		
	pygame.display.flip()
	clock.tick(60)

pygame.quit()