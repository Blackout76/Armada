from SelectionRoulette import *
from Individu import *
from ADN import *
from Data.Travel import *
from random import *
from math import *
import thread

##############################################
#####          GENETIC FUNCTION         ######
##############################################
def evalPopulation(population,incomp,travels,links,nbBus):
	for i in range(len(population)):
		population[i].computeScore(incomp,travels,links,nbBus)
		
def selectPopulationParents(isValidPop,type,population,child_population_size,parents_count_min,parents_count_max):
	if type == 'alea':
		return selectPopulationParents_alea(isValidPop,population,child_population_size,parents_count_min,parents_count_max)
	if type == 'roulette':
		return selectPopulationParents_roulette(isValidPop,population,child_population_size,parents_count_min,parents_count_max)

def selectPopulationParents_roulette(isValidPop,population,child_population_size,parents_count_min,parents_count_max):
	parents = []
	roulette = Roulette(isValidPop)
	for i in range(len(population)):
		if isValidPop:
			roulette.addItem(i,population[i].scoreTotal)
		else:
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

def selectPopulationParents_alea(isValidPop,population,child_population_size,parents_count_min,parents_count_max):
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

def generateChildren(isValidPop,incomp,travels,links,nbBus,populationParent,adnCroisementCount_min,adnCroisementCount_max,countTryToProduceChild):
	children = []
	for i in range(len(populationParent)):
		isValidChild = True
		countTry = 0
		child = generateChild(isValidPop,i,incomp,travels,links,nbBus,populationParent,adnCroisementCount_min,adnCroisementCount_max)
		if isValidPop and child.scoreTotal == 0:
			isValidChild = False

		if isValidPop:
			while not isValidChild and countTry < countTryToProduceChild:
				child = generateChild(isValidPop,i,incomp,travels,links,nbBus,populationParent,adnCroisementCount_min,adnCroisementCount_max)
				if isValidPop and child.scoreTotal == 0:
					isValidChild = False
					countTry +=1
				else:
					isValidChild = True
		if isValidChild:
			children.append(child)

	return children
def generateChild(isValidPop,indexParent,incomp,travels,links,nbBus,populationParent,adnCroisementCount_min,adnCroisementCount_max):
	childGenes = []
	if not isValidPop:
		croisementIndex = randint(1,len(populationParent[indexParent][0].adn)-2)
		childGenes = populationParent[indexParent][0].adn[:croisementIndex] + populationParent[indexParent][1].adn[-(len(populationParent[indexParent][1].adn)-croisementIndex):]
	else:
		indexParentSelected = randint(0,len(populationParent[indexParent])-1)
		indexParentSelected2 = randint(0,len(set(populationParent[indexParent]) - set([int(indexParentSelected)]))-1)
		childGenes = list(populationParent[indexParent][indexParentSelected].adn)

		for i in range(randint(adnCroisementCount_min,adnCroisementCount_max)):
			croisementIndex = randint(0,len(populationParent[indexParent][0].adn)-1)
			childGenes[croisementIndex] = populationParent[indexParent][indexParentSelected2].adn[croisementIndex]

	child = Individu(childGenes)
	if isValidPop:
		child.computeScore(incomp,travels,links,nbBus)
	return child

def insertInPopulation(isValidPop,incomp,travels,links,population,populationChild,populationSize,nbBus):
	newPopulation = []
	
	for i in range(len(populationChild)):
		newPopulation.append(mutate(populationChild[i],nbBus))
	# Eval the new population
	if not isValidPop:
		evalPopulation(newPopulation,incomp,travels,links,nbBus)
	# Compose the new population
	for i in range(len(population)):
		newPopulation.append(population[i])
	# Sort the new population>
	if isValidPop:
		newPopulation.sort(key=lambda x: x.scoreTotal, reverse=True)
	else:
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

def createPopulation2(populationSize,travels,nbBus):
	population = []
	for i in range(populationSize):
		population.append(createIndividu2(travels,nbBus))
	return population


def createPopulation(populationSize,travels,nbBus):
	population = []
	for i in range(populationSize):
		population.append(createIndividu(travels,nbBus))
	return population

def createIndividu(travels,nbBus):
	gene = []
	for i in range(len(travels)):
		gene.append(randint(0,nbBus-1))
	return Individu(gene)
def createIndividu2(travels,nbBus):
	idBus = []
	gene = []
	for i in range(len(travels)):
		idBus.append(i)
	for i in range(len(travels)):
		val = randint(0,len(idBus)-1)
		gene.append(idBus[val])
		del idBus[val]
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



def generateIncomp(travels):
	incomp = []
	for i in range(len(travels)):
		incomp.append([])
		error = False
		for j in range(len(travels)):
			if travels[j] in travels[i].travelUncompatible:
				incomp[i].append(j)
				
	return incomp
	

