from Data.data import *
from Genetic.ADN import *
from Genetic.Individu import *
from Genetic.Tools import *
from time import *
from math import *
import sys

nbBus = 200
if len(sys.argv) > 1:
	nbBus = int(sys.argv[1])
	print "Bus number : " + int(sys.argv[1])

population_size = 50
iteration = 50000000
child_population_size = 20
parents_count_min = 2
parents_count_max = 2
selection_type = 'roulette' # alea / roulette 
adn_croisement_count = 1

links = generateLiaisons()
travels = generateTravels(links)
incomp = generateIncomp(travels)


#while nbBus > 0:
timeStart = time()
population = createPopulation(population_size,travels,nbBus)

evalPopulation(population,incomp,travels,links,nbBus)

isValidPop = False
for i in range(iteration):
	print 'Generation: ' + str(i)
	
	print '		Selection parents ...'
	populationParent = selectPopulationParents(isValidPop,selection_type,population,child_population_size,parents_count_min,parents_count_max)
	print '		Generation enfants ...'
	populationChild = generateChildren(isValidPop,incomp,travels,links,nbBus,populationParent,adn_croisement_count)
	print '		Construction nouvelle population ...'
	population = insertInPopulation(isValidPop,incomp,travels,links,population,populationChild,population_size,nbBus)
	print '		Score:'
	print '			max: ' + str(population[population_size-1].score) + '	Time: ' + str(population[population_size-1].scoreTime) + 'min	Dist:'  + str(population[population_size-1].scoreDist)  
	print '			min: ' + str(population[0].score) + '	Time: ' + str(population[0].scoreTime) + 'min	Dist:'  + str(population[0].scoreDist)  
	if population[population_size-1].score == population[0].score and population[population_size-1].score == 539 and not isValidPop:
		break
		evalPopulation(population,incomp,travels,links,nbBus)
		isValidPop = True
		print 'aloooooooooooooooooo'
	else:
		isValidPop = False


exportIndividu(nbBus,population[population_size-1],travels)

total = 0
lines = []
for j in range(nbBus+1):
	#print'###>'
	lines.append('###>')
	nbTrajetbus = 0
	for i in range(len(population[0].adn)):
		if population[0].adn[i] == j:
			#print'	' + travels[i].toString()
			lines.append(travels[i].toString())
			nbTrajetbus += 1
	total += nbTrajetbus
	#print 'Nb trajet totale pour le bus ' + str(j) +' : ' + str(nbTrajetbus)
	lines.append('Nb trajet totale pour le bus ' + str(j) +' : ' + str(nbTrajetbus))

lines.append('###>  Result   <###')
lines.append('Nb trajet totale:' + str(total))
print 'Nb trajet totale:' + str(total)
#printPopulation(population)

print 'Results:'
print '		population size: ' + str(population_size)
lines.append('		population size: ' + str(population_size))
print '		population children size: ' + str(child_population_size)
lines.append('		population children size: ' + str(child_population_size))
print '		selection: ' + selection_type
lines.append('		selection: ' + selection_type)
print '		count of croisement ADN: ' + str(adn_croisement_count)
lines.append('		count of croisement ADN: ' + str(adn_croisement_count))
print '		executed time: ' + str(round((time() - timeStart)*100)/100) + 's in ' + str(iteration) + ' generation'
lines.append('		executed time: ' + str(round((time() - timeStart)*100)/100) + 's in ' + str(iteration) + ' generation')
print 'Score:'
lines.append('Score:')
print '		max: ' + str(population[population_size-1].score) + '	' + str(population[population_size-1].scoreTime) + '	'  + str(population[population_size-1].scoreDist) 
lines.append('		max: ' + str(population[population_size-1].score) + '	' + str(population[population_size-1].scoreTime) + '	'  + str(population[population_size-1].scoreDist) )
print '		min: ' + str(population[0].score) + '	Time: ' + str(population[0].scoreTime) + 'min	Dist:'  + str(population[0].scoreDist) 
lines.append('		min: ' + str(population[0].score) + '	Time: ' + str(population[0].scoreTime) + 'min	Dist'  + str(population[0].scoreDist))
saveIndividu('test_'+str(nbBus),lines)
#nbBus -= 5
