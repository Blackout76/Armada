from ADN import *

class Individu(object):
	def __init__(self, adn):
		self.score = 0
		self.adn = adn
	
	def toString(self):
		return str(self.score) + '>' + str(self.adn.genes)
	
	def computeScore(self,incomp,travels,links,nbBus):
		self.score = 0
		buslist = [[] for i in range(nbBus+1)]
		buslistUncompatibility = [[] for i in range(nbBus+1)]
		
		for i in range(len(self.adn)):
			buslist[self.adn[i]].append(i)
			buslistUncompatibility[self.adn[i]] += incomp[i]

		for busIndex in range(len(buslist)):
			inter = set(buslist[busIndex]) & set(buslistUncompatibility[busIndex])
			self.score += (len(buslist[busIndex]) - len(inter))
		


	def computeScore2(self,incomp,travels,links,nbBus):
		self.score = 0
		for i in range(len(self.adn)):
			error = False
			for j in range (len(incomp[i])):
				if(self.adn[incomp[i][j]] == self.adn[i]):
					error = True
					break
			if not error:
				self.score += 1
	