import os, sys, copy
lib_path = os.path.abspath(os.path.join('..', '..', '..', 'lib'))
sys.path.append(lib_path)
from Data.data import *



def updateList(liste1, liste2):
	# la liste 1 a maj a partir de la liste 2 .... liste1 - liste2 si meme valeur
	copyL1 = copy.deepcopy(liste1)
	copyL2 = copy.deepcopy(liste2)

	for i in range(len(copyL2)):
		for j in range(len(copyL1)):
			if copyL2[i] == copyL1[j]:
				del copyL1[j]
				break
	return copyL1	

links = generateLiaisons()
travels = generateTravels(links)


listeTrajets=[1,2,3,4,5,6,7,8,9]
print listeTrajets

listeTrajetEffectuer=[3,5,2,7]
print listeTrajetEffectuer

majTrajets = copy.deepcopy(listeTrajets)

majTrajets = updateList(majTrajets, listeTrajetEffectuer)

print majTrajets




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
