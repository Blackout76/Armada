from Roulette import *
from Individu import *
from ADN import *
from random import *
from math import *

def evalPopulation(population,scoreObjectif):
	for i in range(len(population)):
		population[i].score = abs(scoreObjectif - int(population[i].adn.toString(), 2))

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
		croisementIndex = randint(1,len(populationParent[i][0].adn.genes)-1)
		childGenes = []
		for j in range(len(populationParent[i][0].adn.genes)):
			if j < croisementIndex :
				childGenes.append(populationParent[i][0].adn.genes[j])
			else :
				childGenes.append(populationParent[i][1].adn.genes[j])
		# print str(i) + '>>>' + str(childGenes) + '(' + str(croisementIndex) + ')'
		children.append(Individu(ADN(childGenes)))
	return children

def createPopulation(populationSize):
	population = []
	for i in range(populationSize):
		population.append(createIndividu())
	return population
def insertInPopulation(population,populationChild,populationSize,scoreObjectif):
	newPopulation = []
	# Compose the new population
	for i in range(len(population)):
		newPopulation.append(mutate(population[i]))
	for i in range(len(populationChild)):
		newPopulation.append(mutate(populationChild[i]))
	# Eval the new population
	evalPopulation(newPopulation,scoreObjectif)
	# Sort the new population
	newPopulation.sort(key=lambda x: x.score, reverse=True)
	# Remove bad individu
	for i in range(len(newPopulation)-populationSize):
		del newPopulation[0]

	return newPopulation

def mutate(individu):
	if (randint(0,10000)/10000) < 0.075:
		mutateIndex = randint(0,len(individu.adn.genes)-1)
		individu.adn.genes[mutateIndex] = randint(0,1)
	return individu

def createIndividu():
	gene = []
	for i in range(16):
		gene.append(randint(0,1))
	return Individu(ADN(gene))

def printPopulation(population):
	for i in range(len(population)):
		print population[i].toString()
