from SelectionRoulette import *
from Individu import *
from ADN import *
from Data.Travel import *
from random import *
from math import *

##############################################
#####          GENETIC FUNCTION         ######
##############################################
def evalPopulation(population,incomp):
	for i in range(len(population)):
		population[i].computeScore2(incomp)
		



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


def insertInPopulation(incomp,population,populationChild,populationSize,scoreObjectif,nbBus):
	newPopulation = []
	
	for i in range(len(populationChild)):
		newPopulation.append(mutate(populationChild[i],nbBus))
	# Eval the new population
	evalPopulation(newPopulation,incomp)
	# Compose the new population
	for i in range(len(population)):
		newPopulation.append(population[i])
	# Sort the new population>
	newPopulation.sort(key=lambda x: x.score, reverse=False)
	# Remove bad individu
	for i in range(len(newPopulation)-populationSize):
		del newPopulation[0]

	return newPopulation

def mutate(individu,nbBus):
	if (randint(0,10000)/10000) < 0.075:
		mutateIndex = randint(0,len(individu.adn)-1)
		individu.adn[mutateIndex] = randint(0,nbBus)
	return individu

def createPopulation(populationSize,travels,incomp):
	population = []
	print 'Initialisation population ...'
	for i in range(populationSize):
		population.append(createIndividu(travels))

	print 'Evaluation population initiale ... '
	evalPopulation(population,incomp)
	print 'Population initialised !'
	return population

def createIndividu(travels):
	travelsTMP = []
	for i in range(len(travels)):
		travelsTMP.append(i)
	gene = []
	for i in range(len(travels)):
		index = randint(0,len(travelsTMP)-1)
		gene.append(travelsTMP[index] )
		del travelsTMP[index]
	return Individu(gene)

def printPopulation(population):
	for i in range(len(population)):
		print population[i].toString()

def generateIncomp(travels):
	incomp = []
	for i in range(len(travels)):
		incomp.append([])
		error = False
		for j in range(len(travels)):
			if travels[j] in travels[i].travelUncompatible:
				incomp[i].append(j)
	return incomp
	

