class Travel(object):
	def __init__(self, lineName, lineType, lineNumber, startPoint, endPoint, dist):
		self.lineName = lineName
		self.lineType = lineType
		self.lineNumber = lineNumber
		self.dist = dist
		self.startPoint = startPoint;
		self.endPoint = endPoint;
		self.travelBefore = []
		self.travelAfter = []
		self.travelUncompatible = []
		self.pheromones = 0

	def addTravelBefore(self,travel):
		if not travel in self.travelBefore:
			self.travelBefore.append(travel)
			return true
		return false

	def addTravelAfter(self,travel):
		if not travel in self.travelAfter:
			self.travelAfter.append(travel)
			return true
		return false

	def isTravelCompatible(self,travel,addToList,links):
		# addToList = false if just return the value  /// addToList = true for return and put in list
		# -1 if travel can be do before self 		ex: self.travelBefore.append(travel)
		# 0  if travel is in the same time
		# 1  if travel can be do after self 		ex: self.travelAfter.append(travel)

		if int(self.endPoint.time.hour)*60 + int(self.endPoint.time.min)+ int(links.get(self.endPoint.name+':'+travel.startPoint.name).time)+5 < (int(travel.startPoint.time.hour)*60 + int(travel.startPoint.time.min)) : 
			if addToList:
				self.travelAfter.append(travel)
			return 1
		elif int(self.startPoint.time.hour)*60 + int(self.startPoint.time.min) > (int(travel.endPoint.time.hour)*60 + int(travel.endPoint.time.min)) +int(links.get(travel.endPoint.name+':'+self.startPoint.name).time)+5 : 
			if addToList:
				self.travelBefore.append(travel)
			return -1
		else :
			if addToList:
				self.travelUncompatible.append(travel)
			return 0

	def toString (self):
		return 'ligne(' + str(self.lineType) +'):' + self.lineName + '   start:' + self.startPoint.name +'(' + self.startPoint.time.hour + ':' + self.startPoint.time.min + ')'+ '   end:' + self.endPoint.name +'(' + self.endPoint.time.hour + ':' + self.endPoint.time.min + ')'
	
class TravelPoint(object):
	def __init__(self,name,time):
		self.name = name
		self.time = time

class TravelTime(object):
	def __init__(self, timeSplit):
		self.hour = timeSplit[0]
		self.min = timeSplit[1]
	def inMin(self):
		return int(self.hour) * 60 + int(self.min)
		
class TravelLink(object):
	def __init__(self,dist,time):
		self.dist = dist
		self.time = time
	def toString (self):
		return 'dist:' + self.dist + '   time:' + self.time 