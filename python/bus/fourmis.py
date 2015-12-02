# import os, sys, copy
# lib_path = os.path.abspath(os.path.join('..', '..', '..', 'lib'))
# sys.path.append(lib_path)
import copy

from Data.data import *
from Fourmis.toolsFourmis import *

###########################################

links = generateLiaisons()
travels = generateTravels(links)

##############################################
#####             Debut ALGO	         #####
##############################################

nbIteration = 2
nbFourmis = 50


travels2 = generateTravels(links)
print "travels generer"
travels3 = listeChrono(travels2)
print "travels par ordre chrono"


# while len(travels3)!=0:

for iteration in xrange(0,nbIteration):

	travelIteration = generateTravels(links)
	print "travels total iteration generer"
	travelIterationIteration = listeChrono(travelIteration)
	print "travels total iteration chrono generer"

	for fourmis in xrange(0, nbFourmis):

		Tk = []
		travelTotal = generateTravels(links)
		print "travels total fourmis generer"
		travelFourmis = listeChrono(travelTotal)
		print "travels fourmis generer"

		choix = 0
		Tk.append(travelIterationIteration[choix])

		while len(travelFourmis) != 0:
			choixPrecedent = choix

			voisins = voisinsPossible(travelIterationIteration, choix)
			choix = choix + choisirVoisin(voisins)
			Tk.append(travelIterationIteration[choix])

			supprFourmis = choix-choixPrecedent

			for x in xrange(0,(supprFourmis)):
				del travelFourmis[x]
				pass
			len(travelFourmis)

			pass
		
		pass
	pass