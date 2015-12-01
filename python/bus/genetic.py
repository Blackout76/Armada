from Data.data import *
from Genetic.ADN import *
from Genetic.Individu import *
from Genetic.Tools import *
from time import *
from math import *


score_objectif = 23333.0000001
population_size = 50000
iteration = 1
child_population_size = 70
parents_count_min = 2
parents_count_max = 2
selection_type = 'roulette' # alea / roulette 
adn_croisement_count = 1

links = generateLiaisons()
travels = generateTravels(links)
incomp = generateIncomp(travels)

print incomp

print len(travels[0].travelUncompatible)

timeStart = time()
adnBase = generateBasicADN(travels)
nbBus = 100
population = createPopulation(population_size, adnBase,nbBus)

evalPopulation(population,incomp)


for i in range(iteration):
	print 'Generation: ' + str(i)
	
	print '		Selection parents ...'
	populationParent = selectPopulationParents(selection_type,population,child_population_size,parents_count_min,parents_count_max)
	print '		Generation enfants ...'
	populationChild = generateChildren(incomp,populationParent,adn_croisement_count)
	print '		Construction nouvelle population ...'
	population = insertInPopulation(incomp,population,populationChild,population_size,score_objectif,nbBus)
	print 'Score:'
	print '		max: ' + str(population[population_size-1].score) 
	print '		min: ' + str(population[0].score) 
	if population[population_size-1].score == population[0].score and population[population_size-1].score == 539:
		print 'FOUNDDDDDDDDDDDDDDDDDDDDDDDDdd'
		break



total = 0
lines = []
for j in range(nbBus+1):
	print'###>'
	lines.append('###>')
	nbTrajetbus = 0
	for i in range(len(population[0].adn)):
		if population[0].adn[i] == j:
			print'	' + travels[i].toString()
			lines.append(travels[i].toString())
			nbTrajetbus += 1
	total += nbTrajetbus
	print 'Nb trajet totale pour le bus ' + str(j) +' : ' + str(nbTrajetbus)
	lines.append('Nb trajet totale pour le bus ' + str(j) +' : ' + str(nbTrajetbus))

lines.append('###>  Result   <###')
lines.append('Nb trajet totale:' + str(total))
print 'Nb trajet totale:' + str(total)
saveIndividu(lines)
#printPopulation(population)

print 'Results:'
print '		population size: ' + str(population_size)
print '		population children size: ' + str(child_population_size)
print '		selection: ' + selection_type
print '		count of croisement ADN: ' + str(adn_croisement_count)
print '		executed time: ' + str(round((time() - timeStart)*100)/100) + 's in ' + str(iteration) + ' generation'
print 'Score:'
print '		max: ' + str(population[population_size-1].score) 
print '		min: ' + str(population[0].score)
