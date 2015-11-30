from ADN import *

class Individu(object):
	def __init__(self, adn):
		self.score = 0
		self.adn = adn
	
	def toString(self):
		return str(self.score) + '>' + str(self.adn.genes)