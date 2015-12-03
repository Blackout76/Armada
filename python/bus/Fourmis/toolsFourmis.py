import copy
from random import randint

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

	for i in range(len(liste2)):
		for j in range(len(liste1)):
			if liste2[i] == liste1[j]:
				del liste1[j]
				break

def listeChrono(liste):
	copyListe = liste
	tailleL = len(copyListe)
	listeChro = []

	for i in xrange(0,tailleL):

		tailleCopy = len(copyListe)
		heureMin= 0
		
		for j in xrange(0,tailleCopy):
			if copyListe[heureMin].startPoint.time.inMin() > copyListe[j].startPoint.time.inMin():
				heureMin = j
				pass
			pass
		listeChro.append(copyListe[heureMin])
		updateList(copyListe,listeChro)
		pass

	# for x in xrange(0,len(listeChro)):
	# 	print "Trajet" + str(x) + " " + str(listeChro[x].startPoint.time.hour) + ":" + str(listeChro[x].startPoint.time.min)
	# 	pass

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
			if v.startPoint.time.inMin() >= voisins[0].startPoint.time.inMin():
				realisable.append(v)

	if len(realisable)>0:
		return move(choiceNextTravel(travelStart,realisable,links), path,links)
	else:
		return path

def choiceNextTravel(travelStart,travels,links):

	travel = travels[randint(0, len(travels)-1)]

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



