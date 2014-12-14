import pygame
import board

BLACK = (   0,   0,   0)
WHITE = ( 255, 255, 255)
GREEN = (   0, 255,   0)
RED   = ( 255,   0,   0)
FONT  = "monospace"

class Button:
	mouseOn = False

	def __init__(self, color, rect, content, pos=None):
		self.color = color
		self.rect = pygame.Rect(rect)
		self.content = content
		self.pos = pos

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

def initialize():
	global squares
	global gameboard
	global winner
	global player
	# draw the board
	squares = []
	for y in range(3):
		y_coord = 125 + (y * 50)
		for x in range(3):
			x_coord = x * 50
			squares.append(Button(BLACK, [50 + x_coord, y_coord, 50, 50], "", (x, y, 0)))
			if y_coord == 175 and x_coord == 50:
				pass
			else:
				squares.append(Button(BLACK, [225 + x_coord, y_coord, 50, 50], "", (x, y, 1)))
			squares.append(Button(BLACK, [400 + x_coord, y_coord, 50, 50], "", (x, y, 2)))
	# initialize the gameboard
	gameboard = board.Board()
	winner = 0
	player = 1

# game states
BEGIN = 0
PLAY = 1
LEARN = 2
ABOUT = 3
END = 4

state = BEGIN

initialize()

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
							try:
								if gameboard.update(square.pos, 1):
									winner = 1
									state = END
								square.content = "X"
								player = 2
							except:
								pass
						elif player == 2:
							try:
								if gameboard.update(square.pos, 2):
									winner = 2
									state = END
								square.content = "O"
								player = 1
							except:
								pass

		for square in squares:
			square.draw()
		pygame.draw.rect(screen, BLACK, [275, 175, 50, 50])

	if state == ABOUT:
		pass
	
	if state == END:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RETURN:
					initialize()
					state = BEGIN
		winfont = pygame.font.SysFont(FONT, 50)
		replayfont = pygame.font.SysFont(FONT, 30)
		the_win = "Player %s wins!" % winner
		replay = "Press ENTER"
		label = winfont.render(the_win, 1, BLACK)
		label2 = replayfont.render(replay, 1, BLACK)
		screen.blit(label, (100,150))
		screen.blit(label2, (175, 250))

	pygame.display.flip()
	clock.tick(60)

pygame.quit()