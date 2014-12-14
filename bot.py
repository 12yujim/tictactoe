import pygame
import random

class Bot:
	def __init__(self, x=0, y=0, z=0):
		self.x = x
		self.y = y
		self.z = z

	# right now finds random empty tile
	def move(self, Board):
		for x in range(3):
			for y in range(3):
				for z in range(3):
					comp_x = random.randint(0,2)
					comp_y = random.randint(0,2)
					comp_z = random.randint(0,2)
					if Board.board[comp_z][comp_y][comp_x] == 0:
						self.x = comp_x
						self.y = comp_y
						self.z = comp_z