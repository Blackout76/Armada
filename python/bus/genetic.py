from Data.data import *
from Genetic.ADN import *
from Genetic.Individu import *
from Genetic.Tools import *
from time import *
from math import *
import sys

nbBus = 106
if len(sys.argv) > 1:
	nbBus = int(sys.argv[1])
	print "Bus number : " + int(sys.argv[1])

print 'Loading ... '
modePopViable = False
population_size = 50
iteration = 50000000
child_population_size = 20
parents_count_min = 2
parents_count_max = 8
selection_type = 'roulette' # alea / roulette 
adn_croisement_count_min = 1
adn_croisement_count_max = 150
countTryToProduceChild = 10

links = generateLiaisons()
travels = generateTravels(links)
incomp = generateIncomp(travels)

timeStart = time()
print 'Initialisation population 0 ... '
if modePopViable:
	population = createPopulation2(population_size,travels,nbBus)
else:
	population = createPopulation(population_size,travels,nbBus)
print 'Evaluation population 0 ... '
evalPopulation(population,incomp,travels,links,nbBus)

isValidPop = False
for i in range(iteration):
	print 'Generation: ' + str(i)
	
	print '		Selection parents ...'
	populationParent = selectPopulationParents(isValidPop,selection_type,population,child_population_size,parents_count_min,parents_count_max)
	print '		Generation enfants ...'
	populationChild = generateChildren(isValidPop,incomp,travels,links,nbBus,populationParent,adn_croisement_count_min,adn_croisement_count_max,countTryToProduceChild)
	print '		Construction nouvelle population ...'
	population = insertInPopulation(isValidPop,incomp,travels,links,population,populationChild,population_size,nbBus)
	print '		Score:'
	if isValidPop:
		print '			min: ' + str(population[population_size-1].scoreAdvancedToString())
		print '			max: ' + str(population[0].scoreAdvancedToString())
	else:
		print '			max: ' + str(population[population_size-1].score) 
		print '			min: ' + str(population[0].score) 
	if population[population_size-1].score == population[0].score and population[population_size-1].score == 539:
		if not isValidPop:
			evalPopulation(population,incomp,travels,links,nbBus)
			if i != 0 and not modePopViable:
				break
		if i % 2000 == 0 and i != 0:
			exportIndividu2(population[population_size-1].scoreBus,population[population_size-1],travels)
		isValidPop = True
	else:
		isValidPop = False


exportIndividu2(population[population_size-1].scoreBus,population[population_size-1],travels)

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
print '		executed time: ' + str(round((time() - timeStart)*100)/100) + 's in ' + str(iteration) + ' generation'
lines.append('		executed time: ' + str(round((time() - timeStart)*100)/100) + 's in ' + str(iteration) + ' generation')
print 'Score:'
lines.append('Score:')
print '		max: ' + str(population[population_size-1].score) + '	' + str(population[population_size-1].scoreTime) + '	'  + str(population[population_size-1].scoreDist) 
lines.append('		max: ' + str(population[population_size-1].score) + '	' + str(population[population_size-1].scoreTime) + '	'  + str(population[population_size-1].scoreDist) )
print '		min: ' + str(population[0].score) + '	Time: ' + str(population[0].scoreTime) + 'min	Dist:'  + str(population[0].scoreDist) 
lines.append('		min: ' + str(population[0].score) + '	Time: ' + str(population[0].scoreTime) + 'min	Dist'  + str(population[0].scoreDist))
saveIndividu('test_'+str(nbBus),lines)

