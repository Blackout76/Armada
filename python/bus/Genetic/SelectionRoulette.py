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

		scorePrevious = 0
		for i in range(len(self.items)):
			if total > 0:
				self.items[i].score = scorePrevious + self.items[i].score * 100.0 / total
				scorePrevious = self.items[i].score
		self.items.sort(key=lambda x: x.score, reverse=False)


	def randomId(self):
		if self.items[0].score == self.items[len(self.items)-1].score:
			return self.items[randint(0,len(self.items)-1)].id
		else:
			val = randint(0,1000)/10.0
			for i in range(len(self.items)): 
				if val <= self.items[i].score:
					return self.items[i].id

			print'g,eeeeeeeeee' + str(val)
			return 0

class RouletteItem():
	def __init__(self, item_id,item_score):
		self.id = item_id
		self.score = item_score
		