import pygame
import board
import bot
import bot2

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
		if self.mouseOn:
			self.rend = content_init.render(self.content, 1, WHITE)
			pygame.draw.rect(screen, self.color, self.rect)
		else:
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
	main_bot.board = gameboard
	assist_bot.board = gameboard

# game states
BEGIN = 0
CHOOSE = 1
PLAY = 2
LEARN = 3
ABOUT = 4
END = 5
LEARN_END = 6

stop_learning = 0

state = BEGIN

main_bot = bot2.Bot(2)
assist_bot = bot2.Bot(1)

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
			if button.rect.collidepoint(pygame.mouse.get_pos()):
				button.mouseOn = True
			else:
				button.mouseOn = False
			button.draw()

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_j:
					main_bot.display_progress()
			elif event.type == pygame.MOUSEBUTTONDOWN:
				for button in menu:
					if button.rect.collidepoint(event.pos):
						if button.content == "Play":
							state = CHOOSE
						if button.content == "About":
							state = ABOUT
						if button.content == "Learn":
							stop_learning = 0
							state = LEARN
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
		content_init = pygame.font.Font("font/gotham.otf", 20)

		if player == 2:
			try:
				comp_move = main_bot.make_move()
				if gameboard.update(comp_move, 2):
					winner = 2
					state = END
				for square in squares:
					if square.pos == comp_move:
						square.content = "O"
						player = 1
			except:
				pass

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
							pass

		for square in squares:
			square.draw()
		pygame.draw.rect(screen, BLACK, [275, 175, 50, 50])
		playfont = pygame.font.Font(FONT, 15)
		instr = "click on a tile"
		top = "top"
		middle = "middle"
		bottom = "bottom"
		instr_rend = playfont.render(instr, 1, BLACK)
		top_rend = playfont.render(top, 1, BLACK)
		mid_rend = playfont.render(middle, 1, BLACK)
		bot_rend = playfont.render(bottom, 1, BLACK)
		mid_pos = mid_rend.get_rect()
		mid_pos.centerx = screen.get_rect().centerx
		screen.blit(instr_rend, (50, 75))
		screen.blit(top_rend, (105, 300))
		screen.blit(mid_rend, (mid_pos.left, 300))
		screen.blit(bot_rend, (435, 300))

	if state == LEARN:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RETURN:
					stop_learning = 1
		learn_font = pygame.font.Font(FONT, 15)
		label = learn_font.render("LEARNING...", 1, BLACK)
		label_pos = label.get_rect()
		label_pos.center = screen.get_rect().center
		screen.blit(label, label_pos)
		if player == 1:
			try:
				comp1_move = assist_bot.make_move()
				if gameboard.update(comp1_move, 1):
					winner = 1
					state = LEARN_END
				for square in squares:
					if square.pos == comp1_move:
						square.content = "X"
						player = 2
			except:
				pass

		if player == 2:
			try:
				comp_move = main_bot.make_move()
				if gameboard.update(comp_move, 2):
					winner = 2
					state = LEARN_END
				for square in squares:
					if square.pos == comp_move:
						square.content = "O"
						player = 1
			except:
				pass

	if state == ABOUT:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RETURN:
					initialize()
					state = BEGIN
		aboutfont = pygame.font.Font("font/gotham.otf", 20)
		backfont = pygame.font.Font(FONT, 10)
		line1 = "3D Tic Tac Toe"
		line2 = "Lillian Chen & Jim Yu"
		line3 = "CS4701 - Bart Selman"
		line4 = "Cornell University"
		back = "Press ENTER"
		label1 = aboutfont.render(line1, 1, BLACK)
		label2 = aboutfont.render(line2, 1, BLACK)
		label3 = aboutfont.render(line3, 1, BLACK)
		label4 = aboutfont.render(line4, 1, BLACK)
		back_rend = backfont.render(back, 1, BLACK)
		back_pos = back_rend.get_rect()
		back_pos.centerx = screen.get_rect().centerx
		screen.blit(label1, (200, 125))
		screen.blit(label2, (200, 150))
		screen.blit(label3, (200, 175))
		screen.blit(label4, (200, 200))
		screen.blit(back_rend, (back_pos.left, 300))
	
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
			main_bot.update(-1)
			assist_bot.update(-1)
			the_win = "You win!"
		elif winner == 2:
			main_bot.update(1)
			assist_bot.update(-1)
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

	if state == LEARN_END:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RETURN:
					stop_learning = 1
		if stop_learning == 1:
			main_bot.learned = 1
			state = BEGIN
		else:
			state = LEARN
		learn_font = pygame.font.Font(FONT, 15)
		label = learn_font.render("LEARNING...", 1, BLACK)
		label_pos = label.get_rect()
		label_pos.center = screen.get_rect().center
		screen.blit(label, label_pos)
		if winner == 1:
			main_bot.update(-1)
			assist_bot.update(1)
		elif winner == 2:
			main_bot.update(1)
			assist_bot.update(-1)
		initialize()

	pygame.display.flip()
	clock.tick(60)

pygame.quit()