class ADN(object):
	def __init__(self, arg):
		self.genes = arg

	def toString(self):
		s = ''
		for i in range(len(self.genes)):
			s += str(self.genes[i])
		return s
		