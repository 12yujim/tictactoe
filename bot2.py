import pygame
import random


class SpecialList(object):
	# list that orders elements of the form (a, b, c), ranked by a
	# elements with larger rank go first
	def __init__(self):
		self.order = []

	def add(self, elem):
		rank = elem[0]
		i = 0
		for (prev_rank, dc, dc2) in self.order:
			if prev_rank < rank:
				break
			i += 1
		self.order.insert(i, elem)

	def get_first(self):
		return self.order[0][1:]

	def get_rand(self):
		ind = random.randint(0, len(self.order) - 1)
		return self.order[ind][1:]

class Bot(object):
	def __init__(self, player):
		self.player = player
		self.scores = {}
		self.prev_states = []
		self.bot_type = 0
		self.board = None
		self.learned = 0

	def make_move(self):
		# we want to look at all available moves
		# keep track of previous states to update at the end
		# assign score as a function of the position in the list and final score
		# earlier moves get punished/rewarded less for loss/win
		# during learning phase, pick moves regardless of score in order to get a
		# good distribution
		after = SpecialList()
		loss = []
		for move in self.board.moves_avail():
			new_state, win = self.board.shallow_update(move, self.player)
			if self.learned:
				if win:
					self.prev_states.append(new_state)
					return move
				loss_state, other_win = self.check_next(move)
				if other_win:
					loss.append((new_state, move))
			try:
				rank = self.scores[new_state]
			except:
				rank = 0
			after.add((rank, move, new_state))
		if len(loss) > 0:
			loss_state, move = loss[0]
			self.prev_states.append(loss_state)
			return move
		if self.bot_type == 0:
			next_info = after.get_rand()
		else:
			next_info = after.get_first()
		move = next_info[0]
		new_state = next_info[1]
		self.prev_states.append(new_state)
		return move

	def check_next(self, move):
		if self.player == 1:
			test_player = 2
		else:
			test_player = 1
		test_state, test_win = self.board.shallow_update(move, test_player)
		return test_state, test_win


	def update(self, outcome):
		# go through previous moves and assign value based on win or loss
		# outcome is -1 if loss, +1 if win
		i = 1.0
		for state in self.prev_states:
			try:
				self.scores[state] += ((i/(len(self.prev_states) + 1)) * outcome)
			except:
				self.scores[state] = ((i/(len(self.prev_states) + 1)) * outcome)
			i += 1.0
		self.prev_states = []

	def display_progress(self):
		print 'PROGRESS'
		print 'scores', self.scores
		for key in self.scores:
			print key, self.scores[key]