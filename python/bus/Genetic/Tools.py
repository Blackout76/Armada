from SelectionRoulette import *
from Individu import *
from ADN import *
from Data.Travel import *
from random import *
from math import *

##############################################
#####          GENETIC FUNCTION         ######
##############################################
def evalPopulation(travels,population,links):
	for i in range(len(population)):
		population[i].score = computeScore(travels,population[i],links)

def computeScore(travels,individu,links):
	score = 0
	for i in range(len(individu.adn)):
		error = False
		for j in range(len(individu.adn)):
			if individu.adn[i] == individu.adn[j] and travels[j] in travels[i].travelUncompatible:
				error = True
		if not error:
			score += 1
	return score

def selectPopulationParents(type,population,child_population_size,parents_count_min,parents_count_max):
	if type == 'alea':
		return selectPopulationParents_alea(type,population,child_population_size,parents_count_min,parents_count_max)
	if type == 'roulette':
		return selectPopulationParents_roulette(type,population,child_population_size,parents_count_min,parents_count_max)

def selectPopulationParents_roulette(type,population,child_population_size,parents_count_min,parents_count_max):
	parents = []
	roulette = Roulette()
	for i in range(len(population)):
		roulette.addItem(i,population[i].score)
	roulette.load()
	for i in range(child_population_size):
		parent_count = randint(parents_count_min,parents_count_max)
		couple = []
		while len(couple) != parent_count:
			parent = population[roulette.randomId()]
			if not parent in couple:
				couple.append(parent)
		parents.append(couple)

	return parents

def selectPopulationParents_alea(type,population,child_population_size,parents_count_min,parents_count_max):
	parents = []
	for i in range(child_population_size):
		# print 'couple:' + str(i)
		parent_count = randint(parents_count_min,parents_count_max)
		couple = []
		while len(couple) != parent_count:
			parent = population[randint(0,len(population)-1)]
			if not parent in couple:
				couple.append(parent)
				# print parent.toString()
		parents.append(couple)
	# print '######################'
	return parents

def generateChildren(populationParent,adnCroisementCount):
	children = []
	for i in range(len(populationParent)):
		croisementIndex = randint(1,len(populationParent[i][0].adn)-1)
		childGenes = []
		for j in range(len(populationParent[i][0].adn)):
			if j < croisementIndex :
				childGenes.append(populationParent[i][0].adn[j])
			else :
				childGenes.append(populationParent[i][1].adn[j])
		# print str(i) + '>>>' + str(childGenes) + '(' + str(croisementIndex) + ')'
		children.append(Individu(childGenes))
	return children

def createPopulation(populationSize,adnBase,nbBus):
	population = []
	for i in range(populationSize):
		population.append(createIndividu(adnBase,nbBus))
	return population

def insertInPopulation(travels,links,population,populationChild,populationSize,scoreObjectif,nbBus):
	newPopulation = []
	# Compose the new population
	for i in range(len(population)):
		newPopulation.append(mutate(population[i],nbBus))
	for i in range(len(populationChild)):
		newPopulation.append(mutate(populationChild[i],nbBus))
	# Eval the new population
	evalPopulation(travels,newPopulation,links)
	# Sort the new population>
	newPopulation.sort(key=lambda x: x.score, reverse=True)
	# Remove bad individu
	for i in range(len(newPopulation)-populationSize):
		del newPopulation[0]

	return newPopulation

def mutate(individu,nbBus):
	if (randint(0,10000)/10000) < 0.075:
		mutateIndex = randint(0,len(individu.adn)-1)
		individu.adn[mutateIndex] = randint(0,nbBus)
	return individu

def createIndividu(adnBase,nbBus):
	gene = []
	for i in range(len(adnBase)):
		gene.append(randint(0,nbBus))
	return Individu(gene)

def printPopulation(population):
	for i in range(len(population)):
		print population[i].toString()


def generateBasicADN(travels):
	adn = []
	for geneIndex in range(len(travels)):
		adn.append(travels[geneIndex])
	print 'Total genes:' + str(len(adn))
	return adn


