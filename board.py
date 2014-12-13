import pygame

class Board(object):
	def __init__(self):
		# initialize the boardstate
		self.top = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]
		# mid is initialized with 3 in the center row for ease
		self.mid = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]
		self.bot = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]
		self.board = [self.top, self.mid, self.bot]

	def update(self, x, y, z, player):
		if self.board[z][x][y] == 0:
			self.board[z][x][y] = player
		else:
			raise Exception
		return self.check_win(x, y, z, player)

	def check_win(self, x, y, z, player):
		# use modulo 3 for wrap around checking
		for directionx in [0, 1]:
			for directiony in [0, 1]:
				for directionz in [0, 1]:
					newx = (x + directionx) % 3
					newy = (y + directiony) % 3
					newz = (z + directionz) % 3
					found = 1
					while x != newx or y != newy or z != newz:
						if self.board[newz][newx][newy] == player:
							found += 1
						newx = (newx + directionx) % 3
						newy = (newy + directiony) % 3
						newz = (newz + directionz) % 3
					if found >= 3:
						return True
		return False

	# returns the board_state in a string representation
	def board_state(self):
		state = ''
		for board in self.board:
			for row in board:
				for col in row:
					state += str(col)
		return state

	# returns the availables moves in a list of (x, y, z) tuples
	def moves_avail(self):
		avail = []
		for z in [0, 1, 2]:
			for x in [0, 1, 2]:
				for y in [0, 1, 2]:
					if self.board[z][x][y] == 0:
						avail.append((x, y, z))
		return avail

	# returns the longest path each player has in a list [player1, player2]
	# ex. if player 1 has 2 in a row while player 2 has only has 1, this function returns [2, 1]
	def close_win(self):
		pass
