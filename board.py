

class Board(object):
	def __init__(self):
		# initialize the boardstate
		self.top = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]
		# mid is initialized with 3 in the center row for ease
		self.mid = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]
		self.bot = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]

	def check_win(self):
		pass