import pygame

class Bot:
	def __init__(self):
		pass

	# returns (x,y,x) corresponding to tile bot makes move on
	# right now takes the first empty square it finds
	def move(self, Board):
		for x in range(3):
			for y in range(3):
				for z in range(3):
					if Board.board[z][y][x] == 0:
						then (x,y,z)