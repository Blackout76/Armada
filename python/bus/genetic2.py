from Data.data import *
from Genetic.ADN import *
from Genetic.Individu import *
from Genetic.Tools_genetic import *
from time import *
from math import *


score_objectif = 23333.0000001
population_size = 100
iteration = 50000
child_population_size = 45
parents_count_min = 2
parents_count_max = 2
selection_type = 'roulette' # alea / roulette 
adn_croisement_count = 1

print 'loading ...'
links = generateLiaisons()
travels = generateTravels(links)
incomp = generateIncomp(travels)
print travels[33].lineType
print travels[33].lineNumber
print travels[53].lineType
print travels[53].lineNumber

#print incomp
#print len(travels[0].travelUncompatible)

timeStart = time()
population = createPopulation(population_size, travels,incomp)


# print'###################'

evalPopulation(population,incomp)

for i in range(iteration):
	print 'Generation: ' + str(i)
	
	print '		Selection parents ...'
	populationParent = selectPopulationParents(selection_type,population,child_population_size,parents_count_min,parents_count_max)
	print '		Generation enfants ...'
	populationChild = generateChildren(populationParent,adn_croisement_count)
	print '		Construction nouvelle population ...'
	population = insertInPopulation(incomp,population,populationChild,population_size,score_objectif,nbBus)
	print 'Score:'
	print '		min: ' + str(population[population_size-1].score) 
	print '		max: ' + str(population[0].score) 

#printPopulation(population)

print 'Results:'
print '		population size: ' + str(population_size)
print '		population children size: ' + str(child_population_size)
print '		selection: ' + selection_type
print '		count of croisement ADN: ' + str(adn_croisement_count)
print '		executed time: ' + str(round((time() - timeStart)*100)/100) + 's in ' + str(iteration) + ' generation'
print 'Score:'
print '		min: ' + str(population[population_size-1].score) 
print '		max: ' + str(population[0].score)
