from ADN import *
from Individu import *
from Tools import *
from time import *
from math import *

score_objectif = 23333.0000001
population_size = 100
iteration = 50
child_population_size = 75
parents_count_min = 2
parents_count_max = 2
selection_type = 'roulette' # alea / roulette 
adn_croisement_count = 1

timeStart = time()
population = createPopulation(population_size)
# print'###################'

for i in range(iteration):
	evalPopulation(population,score_objectif)
	populationParent = selectPopulationParents(selection_type,population,child_population_size,parents_count_min,parents_count_max)
	populationChild = generateChildren(populationParent,adn_croisement_count)
	population = insertInPopulation(population,populationChild,population_size,score_objectif)

printPopulation(population)

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
