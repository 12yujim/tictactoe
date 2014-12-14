import pygame

class Board(object):
	def __init__(self):
		# initialize the boardstate
		self.top = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]
		# mid is initialized with 3 in the center row to indicate it cannot be played
		self.mid = [[0, 0, 0],[0, 3, 0],[0, 0, 0]]
		self.bot = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]
		self.board = [self.top, self.mid, self.bot]

	def update(self, (x, y, z), player):
		if self.board[z][y][x] == 0:
			self.board[z][y][x] = player
		else:
			raise Exception
		return self.check_win(player)

	def check_win(self, player):
		for x in range(3):
			for y in range(3):
				for z in range(3):
					if self.board[z][y][x] != player:
						continue
					for dx in [0, 1]:
						for dy in [0, 1]:
							for dz in [0, 1]:
								if dx == 0 and dy == 0 and dz == 0:
									continue
								newx = x + dx
								newy = y + dy
								newz = z + dz
								found = 1
								while (0 <= newx < 3) and (0 <= newy < 3) and (0 <= newz < 3):
									if self.board[newz][newy][newx] == player:
										found += 1
									else:
										break
									newx += dx
									newy += dy
									newz += dz
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
