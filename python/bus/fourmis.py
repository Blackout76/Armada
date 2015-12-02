# import os, sys, copy
# lib_path = os.path.abspath(os.path.join('..', '..', '..', 'lib'))
# sys.path.append(lib_path)

import copy

from Data.data import *
from Fourmis.toolsFourmis import *

###########################################

links = generateLiaisons()
travels = generateTravels(links)

listeTrajets=[1,2,3,4,5,6,7,8,9]
print listeTrajets

listeTrajetEffectuer=[3,5,2,7]
print listeTrajetEffectuer

majTrajets = copy.deepcopy(listeTrajets)

majTrajets = updateList(majTrajets, listeTrajetEffectuer)

print majTrajets


##############################################
#####             Debut ALGO	         #####
##############################################

ListFake = [1,2,3]
ListTotal = copy.deepcopy(ListFake)
nbIteration = 2
nbFourmis = 500

while len(ListTotal)!=0:
	for iteration in xrange(1,nbIteration):
		for fourmis in xrange(1, nbFourmis):

			tabTF = []
			copyLT = copy.deepcopy(ListTotal)
			positionActuel = 0
			while len(copyLT)!=0:
				#fonction choix du chemin a faire, simulation :
				tabTF.append(copyLT[positionActuel])
				print tabTF
				copyLT = updateList(copyLT,tabTF)
				pass
			#print "iteration: " + str(iteration) + " fourmis: " + str(fourmis)
			pass
		pass
	ListTotal = updateList(ListTotal,tabTF)
	pass

print "liste total " 
print ListTotal



