from Data.data import *
from Genetic.ADN import *
from Genetic.Individu import *
from Genetic.Tools import *
from time import *
from math import *


score_objectif = 23333.0000001
population_size = 1
iteration = 1
child_population_size = 75
parents_count_min = 2
parents_count_max = 2
selection_type = 'roulette' # alea / roulette 
adn_croisement_count = 1

travels = generateTravels()
links = generateLiaisons()

for l in links:
	print l
print l


timeStart = time()
adnBase = generateBasicADN(travels)
nbBus = len(adnBase) / 2
population = createPopulation(population_size, adnBase,nbBus)


bus = []
for i in range(nbBus+1):
	bus.append(0)

for j in range(len(population)):
	for k in range(len(population[j].adn.genes)):
		bus[population[j].adn.genes[k]] += 1

for i in range(len(bus)):
	print 'Bus ' + str(i) + ' = ' + str(bus[i]*1.0/population_size)



# print'###################'

#for i in range(iteration):
	#evalPopulation(population,score_objectif)
	# populationParent = selectPopulationParents(selection_type,population,child_population_size,parents_count_min,parents_count_max)
	# populationChild = generateChildren(populationParent,adn_croisement_count)
	# population = insertInPopulation(population,populationChild,population_size,score_objectif)

#printPopulation(population)
"""
print 'Results:'
print '		population size: ' + str(population_size)
print '		population children size: ' + str(child_population_size)
print '		selection: ' + selection_type
print '		count of croisement ADN: ' + str(adn_croisement_count)
print '		executed time: ' + str(round((time() - timeStart)*100)/100) + 'ms in ' + str(iteration) + ' generation'
print 'Score:'
print '		min: ' + str(population[population_size-1].score) 
print '		max: ' + str(population[0].score) 
print '		best adn' + str(population[population_size-1].adn.genes)
"""