import pygame
import board

BLACK = (   0,   0,   0)
WHITE = ( 255, 255, 255)
GREEN = (   0, 255,   0)
RED   = ( 255,   0,   0)
FONT  = "font/gameboy.ttf"

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
CHOOSE = 1
PLAY = 2
LEARN = 3
ABOUT = 4
END = 5

state = BEGIN

initialize()

while running:
	screen.fill(WHITE)
	
	# start screen
	if state == BEGIN:
		content_init = pygame.font.Font(FONT, 15)
		menu = [Button(BLACK, [225, 100, 150, 60], "Play"),
						Button(BLACK, [225, 175, 150, 60], "Learn"),
						Button(BLACK, [225, 250, 150, 60], "About")]

		for button in menu:
			button.draw()

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
			elif event.type == pygame.MOUSEBUTTONDOWN:
				for button in menu:
					if button.rect.collidepoint(event.pos):
						if button.content == "Play":
							state = CHOOSE
						if button.content == "About":
							state = ABOUT
						else:
							pass

	if state == CHOOSE:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_y:
					player = 1
					state = PLAY
				elif event.key == pygame.K_n:
					player = 2
					state = PLAY
		prompt = pygame.font.Font(FONT, 15)
		prompt_text = "Would you like to go first? y or n"
		label = prompt.render(prompt_text, 1, BLACK)
		label_pos = label.get_rect()
		label_pos.center = screen.get_rect().center
		screen.blit(label, label_pos)

	if state == PLAY:
		content_init = pygame.font.Font(None, 25)
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
								state = BEGIN
						elif player == 2:
							try:
								if gameboard.update(square.pos, 2):
									winner = 2
									state = END
								square.content = "O"
								player = 1
							except:
								state = BEGIN

		for square in squares:
			square.draw()
		pygame.draw.rect(screen, BLACK, [275, 175, 50, 50])
		playfont = pygame.font.Font(FONT, 15)
		if player == 1:
			turn = "turn: you"
		if player == 2:
			turn = "turn: computer"
		top = "top"
		middle = "middle"
		bottom = "bottom"
		turn_rend = playfont.render(turn, 1, BLACK)
		top_rend = playfont.render(top, 1, BLACK)
		mid_rend = playfont.render(middle, 1, BLACK)
		bot_rend = playfont.render(bottom, 1, BLACK)
		mid_pos = mid_rend.get_rect()
		mid_pos.centerx = screen.get_rect().centerx
		screen.blit(turn_rend, (50, 75))
		screen.blit(top_rend, (105, 300))
		screen.blit(mid_rend, (mid_pos.left, 300))
		screen.blit(bot_rend, (435, 300))

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
		winfont = pygame.font.Font(FONT, 20)
		replayfont = pygame.font.Font(FONT, 10)
		if winner == 1:
			the_win = "You win!"
		elif winner == 2:
			the_win = "You lose!"
		else:
			the_win = "It's a tie!"
		replay = "Press ENTER"
		label = winfont.render(the_win, 1, BLACK)
		label2 = replayfont.render(replay, 1, BLACK)
		label_pos = label.get_rect()
		label_pos.centerx = screen.get_rect().centerx
		label2_pos = label2.get_rect()
		label2_pos.centerx = screen.get_rect().centerx
		screen.blit(label, (label_pos.left, 175))
		screen.blit(label2, (label2_pos.left, 240))

	pygame.display.flip()
	clock.tick(60)

pygame.quit()