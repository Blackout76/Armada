from ADN import *

class Individu(object):
	def __init__(self, adn):
		self.score = 0
		self.scoreDist = 0
		self.scoreTime = 0
		self.scoreTotal = 0
		self.scoreBus = 0
		self.scoreBusChaine = 0
		self.adn = adn
		self.adnScore = [0 for x in adn]
		self.timeStart = 0
		self.timeEnd = 0
	
	def toString(self):
		return str(self.score) + '>' + str(self.adn.genes)
	def scoreAdvancedToString(self):
		return 'NB bus:' + str(self.scoreBus) + '	Score:'+ str(int(self.scoreTotal)) +'	Time: ' + str(self.scoreTime) + 'min	Dist:'  + str(self.scoreDist)  

	def computeScore(self,incomp,travels,links,nbBus):
		self.score = 0
		buslist = [[] for i in range(len(travels))]
		buslistTravels = [[] for i in range(len(travels))]
		buslistUncompatibility = [[] for i in range(len(travels))]

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
		self.scoreBus = 0
		self.scoreBusChaine = 0
		if self.score == len(travels) :
			for busTravels in buslistTravels:
				if len(busTravels) > 0:
					if self.scoreBusChaine < len(busTravels):
						self.scoreBusChaine = len(busTravels)
					self.scoreBus +=1
					busTravels.sort(key=lambda x: int(x.startPoint.time.hour) * 60 + int(x.startPoint.time.min), reverse=False)
					lastTravelEndPointName = ''
					self.timeStart = 0
					self.timeEnd = 0
					for travelIndex in range(len(busTravels)):
						self.scoreDist += int(busTravels[travelIndex].dist)
						if travelIndex == 0:
							#print links.get(str('T0' + ':' + busTravels[travelIndex].startPoint.name)).dist
							self.scoreDist += int(links.get(str('T0' + ':' + busTravels[travelIndex].startPoint.name)).dist)
							self.scoreTime += int(links.get(str('T0' + ':' + busTravels[travelIndex].startPoint.name)).time)
							self.timeStart = busTravels[travelIndex].startPoint.time.inMin()
							if len(busTravels) == 1:
								self.timeEnd = busTravels[travelIndex].endPoint.time.inMin()

							lastTravelEndPointName = busTravels[travelIndex].endPoint.name
						else:
							self.scoreDist += int(links.get(str(lastTravelEndPointName + ':' + busTravels[travelIndex].startPoint.name)).dist)
							lastTravelEndPointName = busTravels[travelIndex].endPoint.name
							self.timeEnd = busTravels[travelIndex].endPoint.time.inMin()

						if travelIndex == len(busTravels)-1:
							self.scoreDist += int(links.get(str(lastTravelEndPointName + ':' + 'T0')).dist)
							self.scoreTime += int(links.get(str(lastTravelEndPointName + ':' + 'T0')).time)

					self.scoreTime += int(self.timeEnd - self.timeStart)
			#self.scoreTotal = (float(self.scoreTime*25.0/60.0) + self.scoreDist) / (self.scoreBusChaine)
			#self.scoreTotal = (float(self.scoreTime*25.0/60.0) + self.scoreDist)
			if self.scoreBus > 0:
				self.scoreTotal = ((self.scoreTime*25.0/60.0) + self.scoreDist) / ((1.0/self.scoreBus)*100.0)
			else:
				self.scoreTotal = (float(self.scoreTime*25.0/60.0) + self.scoreDist)


			#print 'SCORE : ' + str(self.scoreTotal)

	def computeScoreNEW(self,incomp,travels,links,nbBus):
		self.score = 0
		busID = []
		for i in range(len(self.adn)):
			if not self.adn[i] in busID:
				busID.append(self.adn[i])

		buslist = [[] for i in range(len(busID))]
		buslistTravels = [[] for i in range(len(busID))]
		buslistUncompatibility = [[] for i in range(len(busID))]

		for i in range(len(self.adn)):
			buslist[busID.index(self.adn[i])].append(i)
			buslistTravels[busID.index(self.adn[i])].append(travels[i])
			buslistUncompatibility[busID.index(self.adn[i])] += incomp[i]


		for busIndex in range(len(buslist)):
			inter = set(buslist[busIndex]) & set(buslistUncompatibility[busIndex])
			self.score += (len(buslist[busIndex]) - len(inter))

		#IF SOLUTION AVAIBLE
		self.scoreDist = 0
		self.scoreTime = 0
		self.scoreBus = 0
		self.scoreBusChaine = 0
		if self.score == len(travels) :
			for busTravels in buslistTravels:
				if len(busTravels) > 0:
					if self.scoreBusChaine < len(busTravels):
						self.scoreBusChaine = len(busTravels)
					self.scoreBus +=1
					busTravels.sort(key=lambda x: int(x.startPoint.time.hour) * 60 + int(x.startPoint.time.min), reverse=False)
					lastTravelEndPointName = ''
					self.timeStart = 0
					self.timeEnd = 0
					for travelIndex in range(len(busTravels)):
						self.scoreDist += int(busTravels[travelIndex].dist)
						if travelIndex == 0:
							#print links.get(str('T0' + ':' + busTravels[travelIndex].startPoint.name)).dist
							self.scoreDist += int(links.get(str('T0' + ':' + busTravels[travelIndex].startPoint.name)).dist)
							self.scoreTime += int(links.get(str('T0' + ':' + busTravels[travelIndex].startPoint.name)).time)
							self.timeStart = busTravels[travelIndex].startPoint.time.inMin()
							if len(busTravels) == 1:
								self.timeEnd = busTravels[travelIndex].endPoint.time.inMin()

							lastTravelEndPointName = busTravels[travelIndex].endPoint.name
						else:
							self.scoreDist += int(links.get(str(lastTravelEndPointName + ':' + busTravels[travelIndex].startPoint.name)).dist)
							lastTravelEndPointName = busTravels[travelIndex].endPoint.name
							self.timeEnd = busTravels[travelIndex].endPoint.time.inMin()

						if travelIndex == len(busTravels)-1:
							self.scoreDist += int(links.get(str(lastTravelEndPointName + ':' + 'T0')).dist)
							self.scoreTime += int(links.get(str(lastTravelEndPointName + ':' + 'T0')).time)

					self.scoreTime += int(self.timeEnd - self.timeStart)
			#self.scoreTotal = (float(self.scoreTime*25.0/60.0) + self.scoreDist) / (self.scoreBusChaine)
			#self.scoreTotal = (float(self.scoreTime*25.0/60.0) + self.scoreDist)
			if self.scoreBus > 0:
				self.scoreTotal = ((self.scoreTime*25.0/60.0) + self.scoreDist) / ((1.0/self.scoreBus)*100.0)
			else:
				self.scoreTotal = (float(self.scoreTime*25.0/60.0) + self.scoreDist)


			#print 'SCORE : ' + str(self.scoreTotal)

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
	