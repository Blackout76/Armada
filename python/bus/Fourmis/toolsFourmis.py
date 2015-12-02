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
	copyL1 = liste1
	copyL2 = liste2

	for i in range(len(copyL2)):
		for j in range(len(copyL1)):
			if copyL2[i] == copyL1[j]:
				del copyL1[j]
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

def voisinsPossible(liste, point):
	copyListe = liste
	pointActuel = copy.deepcopy(point)
	pointSuivant = copy.deepcopy(pointActuel) + 1

	sortir = 0

	listeVoisins =  []

	if pointActuel == 0:
		listeVoisins.append(liste[pointActuel])

		while copyListe[pointActuel].endPoint.time.inMin() > (copyListe[pointSuivant].startPoint.time.inMin() + 5):
			listeVoisins.append(liste[pointSuivant])
			pointSuivant = pointSuivant + 1
			if pointSuivant == 538 :
				break

	else:
		while copyListe[pointActuel].endPoint.time.inMin() > (copyListe[pointSuivant].startPoint.time.inMin() + 5):
			pointSuivant = pointSuivant + 1
			if pointSuivant == 538 :
				break

		listeVoisins.append(liste[pointSuivant])
		pointVoisin = copy.deepcopy(pointSuivant) + 1

		while copyListe[pointSuivant].endPoint.time.inMin() > (copyListe[pointVoisin].startPoint.time.inMin() + 5):
			listeVoisins.append(liste[pointVoisin])
			pointVoisin = pointVoisin + 1
			print pointVoisin
			if pointVoisin==538 :
				break

	for x in xrange(0,len(listeVoisins)):
		print "Trajet" + str(x) + " " + str(listeVoisins[x].startPoint.time.hour) + ":" + str(listeVoisins[x].startPoint.time.min) + " " + str(listeVoisins[x].endPoint.time.hour) + ":" + str(listeVoisins[x].endPoint.time.min)
	 

	return listeVoisins


def choisirVoisin(liste):

	copyListe = liste
	tailleL = len(copyListe)

	choix = randint(0, tailleL)

	return choix
	pass




def pheromone(liste):

	copyListe = liste
	distanceTotal = 0

	for i in xrange(0,len(copyListe)):



		pass




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










