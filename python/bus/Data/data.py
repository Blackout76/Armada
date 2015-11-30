from Travel import *

##############################################
#####      GENERATION TRAVELS LINKS     ######
##############################################
def generateTravels():
	file = open('Data/horaires.csv', 'r')
	data = file.readlines()
	travels = []
	currentLine = None
	currentTerminus = []
	currentDist = None
	for line in data:
		line = line[:-1]
		if "ligne" in line:
			if len(currentTerminus) >0:
				travelsLine = generateTravelsOfLine(currentLine,currentTerminus,currentDist)
				for geneIndex in range(len(travelsLine)):
					travels.append(travelsLine[geneIndex])
			currentTerminus = []
			currentDist = None
			# print "New line:" + str(currentLine)
			currentLine = line.split(' ')[1]
		elif "T" in line:
			currentTerminus.append(line)
		else:
			currentDist = line

	travelsLine = generateTravelsOfLine(currentLine,currentTerminus,currentDist)
	for geneIndex in range(len(travelsLine)):
		travels.append(travelsLine[geneIndex])

	# Init travels to have before and after travels
	generateLinksTravels(travels)
	return travels

def generateTravelsOfLine(nameline,terminus,dist):
	travels = []
	travelCount = 0;
	terminusDecoded = []
	distDecoded = dist.split(',')

	for i in range(len(terminus)):
		#save split terminus
		terminusDecoded.append(terminus[i].split(','))
		#save max travel
		if len(terminusDecoded[len(terminusDecoded)-1]) > travelCount :
			travelCount = len(terminusDecoded[len(terminusDecoded)-1])
	travelCount -= 1

	for i in range(travelCount):
		terminusIndexStart=0
		terminusIndexEnd=len(terminusDecoded)-1
		#Find terminus index of start
		while i+1 >= len(terminusDecoded[terminusIndexStart]) or terminusDecoded[terminusIndexStart][i+1] is "": 
			terminusIndexStart += 1
		#Find terminus index of end
		while i+1 >= len(terminusDecoded[terminusIndexEnd]) or terminusDecoded[terminusIndexEnd][i+1] is "": 
			terminusIndexEnd -= 1

		startPoint = TravelPoint( terminusDecoded[terminusIndexStart][0], TravelTime(terminusDecoded[terminusIndexStart][i+1].split(':')) )
		endPoint = TravelPoint( terminusDecoded[terminusIndexEnd][0], TravelTime(terminusDecoded[terminusIndexEnd][i+1].split(':'))  )
		travels.append(Travel(nameline,startPoint,endPoint,distDecoded[i+1]))
	return travels

def generateLinksTravels(travels):
	for travel in travels:
		for travelTMP in travels:
			if not travel == travelTMP:
				travel.isTravelCompatible(travelTMP,True)

def generateLiaisons():
	file = open('Data/terminus.csv', 'r')
	fileDist = open('Data/dist_terminus.csv', 'r')
	data = file.readlines()
	dataDist = fileDist.readlines()
	terminusName = []
	links = []
	for i in range(len(data)):
		if not data[i] == "":
			if i==0:
				terminusName = data[i][:-1].split(',')
			else:
				line = data[i][:-1].split(',')
				lineDist = dataDist[i][:-1].split(',')
				for j in range(len(line)-1):
					links.append(dict({'linkName' : str(terminusName[j+1]+':'+line[0]),'link': TravelLink(lineDist[j+1],line[j+1])}))
	return links