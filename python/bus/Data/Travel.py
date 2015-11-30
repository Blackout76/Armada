class Travel(object):
	def __init__(self, lineName, startPoint, endPoint, dist):
		self.lineName = lineName
		self.dist = dist
		self.startPoint = startPoint;
		self.endPoint = endPoint;
		self.travelBefore = []
		self.travelAfter = []

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
	def isTravelCompatible(self,travel,addToList):
		# addToList = false if just return the value  /// addToList = true for return and put in list
		# -1 if travel can be do before self
		# 0  if travel is in the same time
		# 1  if travel can be do after self
		return 0

	def toString (self):
		return 'ligne:' + self.lineName + '   start:' + self.startPoint.name +'(' + self.startPoint.time.hour + ':' + self.startPoint.time.min + ')'+ '   end:' + self.endPoint.name +'(' + self.endPoint.time.hour + ':' + self.endPoint.time.min + ')'
	
class TravelPoint(object):
	def __init__(self,name,time):
		self.name = name
		self.time = time

class TravelTime(object):
	def __init__(self, timeSplit):
		self.hour = timeSplit[0]
		self.min = timeSplit[1]
		
class TravelLink(object):
	def __init__(self,dist,time):
		self.dist = dist
		self.time = time
	def toString (self):
		return 'dist:' + self.dist + '   time:' + self.time 