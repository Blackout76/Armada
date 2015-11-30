class Travel(object):
	def __init__(self, lineName, startPoint, endPoint, dist):
		self.bus = None
		self.lineName = lineName
		self.dist = dist
		self.startPoint = None;
		self.endPoint = None;
		print 'ligne:' + lineName + '   start:' + startPoint.name +'(' + startPoint.time.hour + ':' + startPoint.time.min + ')'+ '   end:' + endPoint.name +'(' + endPoint.time.hour + ':' + endPoint.time.min + ')'

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
