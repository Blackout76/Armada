from random import *

class Roulette():
	def __init__(self):
		self.items = []

	def addItem(self,item_id,item_score):
		self.items.append(RouletteItem(item_id,item_score))

	def load(self):
		total = 0.0;
		for i in range(len(self.items)):
			total = total + (1.0 / self.items[i].score);
			self.items[i].score = 1.0 / self.items[i].score
		for i in range(len(self.items)):
			if total > 0:
				self.items[i].score = self.items[i].score * 100.0 / total
		self.items.sort(key=lambda x: x.score, reverse=True)


	def randomId(self):
		val = randint(0,1000)/10.0
		for i in range(len(self.items)): 
			if val >= self.items[i].score:
				return self.items[i].id
		return 0;

class RouletteItem():
	def __init__(self, item_id,item_score):
		self.id = item_id
		self.score = item_score
		