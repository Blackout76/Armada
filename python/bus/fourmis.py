# import os, sys, copy
# lib_path = os.path.abspath(os.path.join('..', '..', '..', 'lib'))
# sys.path.append(lib_path)
import copy

from Data.data import *
from Fourmis.toolsFourmis import *

###########################################

#links = generateLiaisons()
#travels = generateTravels(links)

##############################################
#####             Debut ALGO	         #####
##############################################
busList = []
nbIteration = 5
nbFourmis = 2

links = generateLiaisons()
print "links generer"
travels = generateTravels(links)
travels.sort(key = lambda x: x.startPoint.time.inMin(), reverse = False)
print "travels generer"
# travels2 = listeChrono(travels)
print "travels par ordre chrono"

while len(travels) != 0:
	for x in range(len(travels)):
		travels[x].pheromones = 0

	for j in range(nbIteration):

		for i in range(nbFourmis):
			path =[]
			premierVoyage = travels[0].travelUncompatible

			if (len(premierVoyage) != 0):
				choix = randint(0, len(premierVoyage)-1)
				path = move(travels[choix], [],links)
			else:
				path = move(travels[0], [],links)

			score = computePath(path,links)
			putPheromones(path,score)


		evapore(travels)

	addPathToBusList(busList,path)
	actualiseTravels(travels,path)

	print len(travels)

saveBuslist(busList,links)
