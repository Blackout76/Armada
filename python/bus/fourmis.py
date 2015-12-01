import os, sys, copy
lib_path = os.path.abspath(os.path.join('..', '..', '..', 'lib'))
sys.path.append(lib_path)
from Data.data import *

links = generateLiaisons()
travels = generateTravels(links)	

#show travels
#for t in travels:
#	print t.toString()

#show links
#print links
#get a links
#print 'Link : ' + str('T22' + ':' + 'T23') +' >>>  time:  ' + links.get('T22:T23').time + '   dist: ' + links.get('T22:T23').dist


#for tu in travels[0].travelUncompatible:
#	print tu.toString()


listeTrajets=[1,2,3,4,5,6,7,8,9]
print listeTrajets

listeTrajetEffectuer=[3,5,2,7]
print listeTrajetEffectuer

majTrajets = copy.deepcopy(listeTrajets)


for i in range(len(listeTrajetEffectuer)):
	for j in range(len(majTrajets)):
		if listeTrajetEffectuer[i] == majTrajets[j]:
			del majTrajets[j]
			break
print majTrajets