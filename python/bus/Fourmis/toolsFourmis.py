import copy
from random import randint
from Data.Travel import *
from time import *

# def updateList(liste1, liste2):
# 	# la liste 1 a maj a partir de la liste 2 .... liste1 - liste2 si meme valeur
# 	copyL1 = copy.deepcopy(liste1)
# 	copyL2 = copy.deepcopy(liste2)

# 	for i in range(len(copyL2)):
# 		for j in range(len(copyL1)):
# 			if copyL2[i] == copyL1[j]:
# 				del copyL1[j]
# 				break
# 	return copyL1	

def updateList(liste1, liste2):
	# la liste 1 a maj a partir de la liste 2 .... liste1 - liste2 si meme valeur
	print len(liste1)
	liste1 = list(set(liste1) - set(liste2))
	# for i in range(len(liste2)):
	# 	for j in range(len(liste1)):
	# 		if liste2[i] == liste1[j]:
	# 			del liste1[j]
	# 			break
	print len(liste1)

def listeChrono(liste):
	
	listeChro = list(liste)
	listeChro.sort(key = lambda x: x.startPoint.time.inMin(), reverse = False)

	return listeChro

# def voisinsPossible(liste, point):
# 	copyListe = liste
# 	pointActuel = copy.deepcopy(point)
# 	pointSuivant = copy.deepcopy(pointActuel) + 1

# 	sortir = 0

# 	listeVoisins =  []

# 	if pointActuel == 0:
# 		listeVoisins.append(liste[pointActuel])

# 		while copyListe[pointActuel].endPoint.time.inMin() > (copyListe[pointSuivant].startPoint.time.inMin() + 5) and sortir == 0:
# 			listeVoisins.append(liste[pointSuivant])
# 			pointSuivant = pointSuivant + 1
# 			if pointSuivant == 538 :
# 				sortir = 1

# 	else:
# 		while copyListe[pointActuel].endPoint.time.inMin() > (copyListe[pointSuivant].startPoint.time.inMin() + 5) and sortir == 0:
# 			pointSuivant = pointSuivant + 1
# 			if pointSuivant == 538 :
# 				sortir = 1

# 		listeVoisins.append(liste[pointSuivant])
# 		pointVoisin = copy.deepcopy(pointSuivant) + 1

# 		while copyListe[pointSuivant].endPoint.time.inMin() > (copyListe[pointVoisin].startPoint.time.inMin() + 5) and sortir == 0:
# 			listeVoisins.append(liste[pointVoisin])
# 			pointVoisin = pointVoisin + 1



# 			print pointVoisin



# 			if pointVoisin==538 :
# 				sortir = 1

# 	for x in xrange(0,len(listeVoisins)):
# 	 	print "Trajet" + str(x) + " " + str(listeVoisins[x].startPoint.time.hour) + ":" + str(listeVoisins[x].startPoint.time.min) + " " + str(listeVoisins[x].endPoint.time.hour) + ":" + str(listeVoisins[x].endPoint.time.min)
	 

# 	return listeVoisins


# def choisirVoisin(liste):

# 	copyListe = liste
# 	tailleL = len(copyListe)

# 	choix = randint(1, tailleL)

# 	return choix
# 	pass




# def pheromone(liste):

# 	copyListe = liste
# 	distanceTotal = 0

# 	for i in xrange(0,len(copyListe)):



# 		pass




# def chooseTravel(pointActuel, listeVoisins):
	
# 	pheromone=[]
# 	visibilite=[]
# 	total = 0

# 	for i in range(len(listeVoisins)):
# 		pheromone[i] = getPheromone()
# 		visibilite[i] = getVisibilite(pointActuel, listeVoisins[i])
# 		total = total + pheromone[i] * visibilite[i]

# 	probChoisir=[]
# 	probMax = 0
# 	choixVoisin = 0

# 	for i in range(len(listeVoisins)):
# 		probChoisir[i] = (pheromone[i] * visibilite[i]) / total 
		
# 		if probChoisir[i] > probMax:
# 			probMax=probChoisir[i]
# 			choixVoisin = i

# 	return choixVoisin



def move(travelStart, path, links):
	
	path.append(travelStart)
	voisins = travelStart.travelAfter
	voisins.sort(key = lambda x: x.startPoint.time.inMin(), reverse = False)
	realisable = []
	if len(voisins)>0:
		for v in voisins[0].travelUncompatible:
			if v.startPoint.time.inMin() >= voisins[0].startPoint.time.inMin() and v != voisins[0]:
				realisable.append(v)

	if len(realisable)>1:
		return move(choiceNextTravel(travelStart,realisable,links), path,links)
	else:
		return path

def choiceNextTravel(travelStart,travels,links):
	travel = travels[randint(1, len(travels)-1)] #OLIIIIIIIIIIIIIIIIIVER

	pheromone=[0 for x in travels]
 	visibilite=[0 for x in travels]
 	probChoisir=[0 for x in travels]
 	total = 0

 	for i in range(len(travels)):
 		pheromone[i] = travels[i].pheromones
		link = links.get(str(travelStart.endPoint.name + ':' + travels[i].startPoint.name))
 		visibilite[i] = 1.0 / (int(link.dist) + (((int(link.time)+5)/60.0)*25.0))
 		total += pheromone[i] * visibilite[i]

	probMax = 0
 	nextTravel = 0

 	if total == 0:
 		for i in range(len(visibilite)):
	 		if visibilite[i] > probMax:
	 			probMax=visibilite[i]
	 			nextTravel = travels[i]

	else:
		for i in range(len(probChoisir)):
	 		probChoisir[i] = (pheromone[i] * visibilite[i]) / total 
	 		if probChoisir[i] > probMax:
	 			probMax=probChoisir[i]
	 			nextTravel = travels[i]

 	return nextTravel

def computePath(path,links):
	scoreDist = 0
	scoreTime = 0
	lastTravelEndPointName = ''
	for travelIndex in range(len(path)):
		scoreDist += int(path[travelIndex].dist)
		scoreTime += int(path[travelIndex].endPoint.time.inMin()) - int(path[travelIndex].startPoint.time.inMin())
		if travelIndex == 0:
			#print links.get(str('T0' + ':' + path[travelIndex].startPoint.name)).dist
			scoreDist += int(links.get(str('T0' + ':' + path[travelIndex].startPoint.name)).dist)
			scoreTime += int(links.get(str('T0' + ':' + path[travelIndex].startPoint.name)).time)
			lastTravelEndPointName = path[travelIndex].endPoint.name
		else:
			scoreDist += int(links.get(str(lastTravelEndPointName + ':' + path[travelIndex].startPoint.name)).dist)
			scoreTime += int(links.get(str(lastTravelEndPointName + ':' + path[travelIndex].startPoint.name)).time) + 5
			lastTravelEndPointName = path[travelIndex].endPoint.name

		if travelIndex == len(path)-1:
			scoreDist += int(links.get(str(lastTravelEndPointName + ':' + 'T0')).dist)
			scoreTime += int(links.get(str(lastTravelEndPointName + ':' + 'T0')).time) + 5
	return [scoreTime,scoreDist]


def putPheromones(path,score):
	for p in path:
		p.pheromones += 1 / (score[1] + ((score[0]/60.0)*25))

def evapore(travels):
	for t in travels:
		t.pheromones *= 0.5

def actualiseTravels(travels,path):
	for pathTravel in path:
		for travel in travels:
			if pathTravel in travel.travelAfter:
				del travel.travelAfter[travel.travelAfter.index(pathTravel)]
			if pathTravel in travel.travelUncompatible:
				del travel.travelUncompatible[travel.travelUncompatible.index(pathTravel)]
	for pathTravel in path:
		del travels[travels.index(pathTravel)]




def addPathToBusList(busList,path):
	busTravel = []
	for pathTravel in path:
		lineName = pathTravel.lineName
		lineType = pathTravel.lineType
		lineNumber = pathTravel.lineNumber
		dist = pathTravel.dist
		startPoint = TravelPoint(pathTravel.startPoint.name,TravelTime([pathTravel.startPoint.time.hour,pathTravel.startPoint.time.min]))
		endPoint = TravelPoint(pathTravel.endPoint.name,TravelTime([pathTravel.endPoint.time.hour,pathTravel.endPoint.time.min]))

		busTravel.append(Travel(lineName, lineType, lineNumber, startPoint, endPoint, dist))
	busList.append(busTravel)


def saveBuslist(bus,links):
	print 'nb bus' + str(len(bus))

	lines=[]
	lineTest=[]
	countBus = 1

	for v in bus:
		stringline = 'bus'+ str(countBus)
		lineTest.append('bus'+ str(countBus))
		for travel in v:
			stringline += ',l'+str(travel.lineName)+':'+travel.lineType+':v'+str(travel.lineNumber)
			lineTest.append('	'+travel.toString())
		lines.append(stringline)
		countBus+=1


	jeVeuxUneDistance = 0
	for i in range(len(bus)):
		for j in range(len(bus[i])):
			if(j==0):
				jeVeuxUneDistance += int(links[(str(bus[i][0].startPoint.name) + ":T0")].dist)
			elif(j==len(bus[i])-1):
				jeVeuxUneDistance += int(links[(str(bus[i][len(bus[i])-1].endPoint.name) + ":T0")].dist)
			if(j!=0):
				jeVeuxUneDistance += int(links[(str(bus[i][j].startPoint.name) + ':' + str(bus[i][j-1].endPoint.name))].dist)
			jeVeuxUneDistance += int(bus[i][j].dist)		

	jeVeuxUnTemps = 0
	for i in range(len(bus)):
		depart = int(bus[i][0].startPoint.time.hour)*60 + int(bus[i][0].startPoint.time.min)
		arrive = int(bus[i][(len(bus[i])-1)].endPoint.time.hour)*60 + int(bus[i][(len(bus[i])-1)].endPoint.time.min)
		jeVeuxUnTemps += arrive - depart
		jeVeuxUnTemps += int(links[("T0:" + bus[i][0].startPoint.name)].time)
		jeVeuxUnTemps += int(links[("T0:" + bus[i][(len(bus[i])-1)].endPoint.name)].time)


	lines.insert(0,str(len(bus))+','+str(jeVeuxUnTemps)+','+str(jeVeuxUneDistance))	
	lines.insert(0,'#Bentoumi Feth-Allah, Bosch I Sais Jordi, Casol Nicolas, Jouet Jeremy, Leger Olivier, Menet Cedric')

	file = open('Data/Save/Fourmis/' + str(len(bus)) + '_Enforce_' + str(time()) +'.csv', 'w')
	for l in lines:
		file.write(l)
		file.write("\n")


	file = open('Data/Save/Fourmis/' + str(len(bus)) + '_EnforceTest_' + str(time()) +'.csv', 'w')
	for l in lineTest:
		file.write(l)
		file.write("\n")
	return