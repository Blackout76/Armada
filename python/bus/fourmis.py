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

# ListFake = [1,2,3]
# ListTotal = copy.deepcopy(ListFake)
# nbIteration = 2
# nbFourmis = 50

# while len(ListTotal)!=0:
# 	for iteration in xrange(0,nbIteration):
# 		for fourmis in xrange(0, nbFourmis):
# 			tabTF = []
# 			copyLT = copy.deepcopy(ListTotal)
# 			positionActuel = 0
# 			while len(copyLT)!=0:
# 				#fonction choix du chemin a faire, simulation :
# 				tabTF.append(copyLT[positionActuel])
# 				print tabTF
# 				copyLT = updateList(copyLT,tabTF)
# 				pass
# 			#print "iteration: " + str(iteration) + " fourmis: " + str(fourmis)
# 			pass
# 		pass
# 	ListTotal = updateList(ListTotal,tabTF)
# 	pass

# print "liste total " 
# print ListTotal

travels2 = generateTravels(links)
print len(travels2)
travels3 = listeChrono(travels2)
print len(travels3)
#print "pointActuel Heure fin: " + str(travels3[0].endPoint.time.inMin())
voisinsPossible(travels3, 0)