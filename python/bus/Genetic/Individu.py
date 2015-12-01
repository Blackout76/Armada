from ADN import *

class Individu(object):
	def __init__(self, adn):
		self.score = 0
		self.adn = adn
	
	def toString(self):
		return str(self.score) + '>' + str(self.adn.genes)
	
	def computeScore(self,travels,links):
		self.score = 0
		for i in range(len(self.adn)):
			error = False
			for j in range(len(self.adn)):
				if self.adn[i] == self.adn[j] and travels[j] in travels[i].travelUncompatible:
					error = True
			if not error:
				self.score += 1
	def computeScore2(self,incomp):
		self.score = 0
		for i in range(len(self.adn)):
			error = False
			for j in range (len(incomp[i])):
				if(self.adn[incomp[i][j]] == self.adn[i]):
					error = True
			if not error:
				self.score += 1
	