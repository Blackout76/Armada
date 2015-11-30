class Travel(object):
	def __init__(self, lineName, startPoint, endPoint, dist):
		self.lineName = lineName
		self.dist = dist
		self.startPoint = startPoint;
		self.endPoint = endPoint;
		self.travelBefore = []
		self.travelAfter = []
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