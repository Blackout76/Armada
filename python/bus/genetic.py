from Data.data import *
from Genetic.ADN import *
from Genetic.Individu import *
from Genetic.Tools import *
from time import *
from math import *
import sys

nbBus = 100
if len(sys.argv) > 1:
	nbBus = int(sys.argv[1])
	print "Bus number : " + int(sys.argv[1])

score_objectif = 23333.0000001
population_size = 50
iteration = 50000000
child_population_size = 20
parents_count_min = 2
parents_count_max = 2
selection_type = 'roulette' # alea / roulette 
adn_croisement_count = 5

links = generateLiaisons()
travels = generateTravels(links)
incomp = generateIncomp(travels)


#print incomp
#print len(travels[0].travelUncompatible)




while nbBus > 0:
	timeStart = time()
	adnBase = generateBasicADN(travels)
	population = createPopulation(population_size, adnBase,nbBus)

	evalPopulation(population,incomp,travels,links,nbBus)


	for i in range(iteration):
		print 'Generation: ' + str(i)
		
		print '		Selection parents ...'
		populationParent = selectPopulationParents(selection_type,population,child_population_size,parents_count_min,parents_count_max)
		print '		Generation enfants ...'
		populationChild = generateChildren(incomp,populationParent,adn_croisement_count)
		print '		Construction nouvelle population ...'
		population = insertInPopulation(incomp,travels,links,population,populationChild,population_size,score_objectif,nbBus)
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
	print '		max: ' + str(population[population_size-1].score) 
	lines.append('		max: ' + str(population[population_size-1].score))
	print '		min: ' + str(population[0].score)
	lines.append('		min: ' + str(population[0].score))
	saveIndividu(nbBus,lines)
	nbBus -= 1
