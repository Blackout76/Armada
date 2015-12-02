from random import *

class Roulette():
	def __init__(self,reverse):
		self.items = []
		self.reverse = reverse
		self.total = 0.0

	def addItem(self,item_id,item_score):
		if self.reverse:
			item_score = 1.0 / float(item_score) * 10000000.0
		self.items.append(RouletteItem(item_id,item_score))

	def load(self):
		self.total = 0.0;
		for i in range(len(self.items)):
			self.total += self.items[i].score;

		scorePrevious = 0
		for i in range(len(self.items)):
			self.items[i].score = scorePrevious + self.items[i].score
			scorePrevious = self.items[i].score

	def randomId(self):
		val = randint(0,int(self.total+1))
		for i in range(len(self.items)): 
			if val <= self.items[i].score:
				return self.items[i].id
		return 0

class RouletteItem():
	def __init__(self, item_id,item_score):
		self.id = item_id
		self.score = item_score
		