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

nbIteration = 1
nbFourmis = 10
links = generateLiaisons()
print "links generer"
travels = generateTravels(links)
print "travels generer"
travels2 = listeChrono(travels)
print "travels par ordre chrono"


while len(travels2) != 0:

 	for x in range(len(travels2)):
 		travels2[x].pheromones = 0

	for j in range(nbIteration):
		for i in range(nbFourmis):
			print '--------------- Iteration: ' + str(j) + ' Fourmis: ' + str(i) + ' ----------------------'
			path =[]
			premierVoyage = travels2[0].travelUncompatible

			#if (premierVoyage != 0):
			if (len(premierVoyage) != 0):
				choix = randint(0, len(premierVoyage)-1)
				path = move(travels2[choix], [travels2[0]],links)
			else:
				path = move(travels2[0], [travels2[0]],links)

			score = computePath(path,links)
			putPheromones(path,score)

			for t in path:
				print t.toString() + '   pheromones:' + str(t.pheromones)

		evapore(travels2)

	updateList(travels2, path)
	print len(travels2)







# while len(travels3)!=0:

# for iteration in xrange(0,nbIteration):

# 	travelIteration = generateTravels(links)
# 	print "travels total iteration generer"
# 	travelIterationIteration = listeChrono(travelIteration)
# 	print "travels total iteration chrono generer"

# 	for fourmis in xrange(0, nbFourmis):

# 		Tk = []
# 		travelTotal = generateTravels(links)
# 		print "travels total fourmis generer"
# 		travelFourmis = listeChrono(travelTotal)
# 		print "travels fourmis generer"

# 		choix = 0
# 		Tk.append(travelIterationIteration[choix])

# 		while len(travelFourmis) != 0:
# 			choixPrecedent = choix

# 			voisins = voisinsPossible(travelIterationIteration, choix)
# 			choix = choix + choisirVoisin(voisins)
# 			Tk.append(travelIterationIteration[choix])

# 			supprFourmis = choix-choixPrecedent

# 			for x in xrange(0,(supprFourmis)):
# 				del travelFourmis[x]
# 				pass
# 			len(travelFourmis)

# 			pass
		
# 		pass
# 	pass