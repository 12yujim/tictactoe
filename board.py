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
		self.board[z][x][y] = player
		return self.check_win(x, y, z, player)

	def check_win(self, x, y, z, player):
		# use modulo 3 for wrap around checking
		for directionx in [-1, 0, 1]:
			for directiony in [-1, 0, 1]:
				for directionz in [-1, 0, 1]:
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
