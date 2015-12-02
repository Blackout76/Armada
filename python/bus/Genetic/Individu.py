from ADN import *

class Individu(object):
	def __init__(self, adn):
		self.score = 0
		self.scoreDist = 0
		self.scoreTime = 0
		self.adn = adn
	
	def toString(self):
		return str(self.score) + '>' + str(self.adn.genes)
	
	def computeScore(self,incomp,travels,links,nbBus):
		self.score = 0
		buslist = [[] for i in range(nbBus+1)]
		buslistTravels = [[] for i in range(nbBus+1)]
		buslistUncompatibility = [[] for i in range(nbBus+1)]
		
		for i in range(len(self.adn)):
			buslist[self.adn[i]].append(i)
			buslistTravels[self.adn[i]].append(travels[i])
			buslistUncompatibility[self.adn[i]] += incomp[i]


		for busIndex in range(len(buslist)):
			inter = set(buslist[busIndex]) & set(buslistUncompatibility[busIndex])
			self.score += (len(buslist[busIndex]) - len(inter))


		#IF SOLUTION AVAIBLE
		self.scoreDist = 0
		self.scoreTime = 0
		if self.score == len(travels):
			for busTravels in buslistTravels:
				busTravels.sort(key=lambda x: int(x.startPoint.time.hour) * 60 + int(x.startPoint.time.min), reverse=False)
				lastTravelEndPointName = ''
				for travelIndex in range(len(busTravels)):
					if travelIndex == 0:
						self.scoreDist += int(links.get('T0' + ':' + str(busTravels[travelIndex].startPoint.name)).dist)
						self.scoreTime += int(links.get('T0' + ':' + str(busTravels[travelIndex].startPoint.name)).time)
						lastTravelEndPointName = busTravels[travelIndex].endPoint.name
					else:
						self.scoreDist += int(links.get(str(lastTravelEndPointName) + ':' + str(busTravels[travelIndex].startPoint.name)).dist)
						self.scoreTime += int(links.get(str(lastTravelEndPointName) + ':' + str(busTravels[travelIndex].startPoint.name)).time)
						lastTravelEndPointName = busTravels[travelIndex].endPoint.name

					if travelIndex == len(busTravels):
						self.scoreDist += int(links.get(str(lastTravelEndPointName) + ':' + 'T0').dist)
						self.scoreTime += int(links.get(str(lastTravelEndPointName) + ':' + 'T0').time)





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
	