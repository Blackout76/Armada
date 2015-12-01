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

def generateChildren(incomp,populationParent,adnCroisementCount):
	children = []
	for i in range(len(populationParent)):
		valid = False
		childGenes = []
		while not valid:
			childGenes = []
			croisementIndex = randint(1,len(populationParent[i][0].adn)-1)
			for j in range(len(populationParent[i][0].adn)):
				if j < croisementIndex :
					childGenes.append(populationParent[i][0].adn[j])
				else :
					childGenes.append(populationParent[i][1].adn[j])
			# print str(i) + '>>>' + str(childGenes) + '(' + str(croisementIndex) + ')'
			valid = True
			#child = Individu(childGenes)
			#child.computeScore2(incomp)

			#if child.score >= populationParent[i][0].score or child.score >= populationParent[i][1].score:
			children.append(Individu(childGenes))
				#valid = True


	return children

def createPopulation(populationSize,adnBase,nbBus):
	population = []
	for i in range(populationSize):
		population.append(createIndividu(adnBase,nbBus))
	return population

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



def generateIncomp(travels):
	incomp = []
	for i in range(len(travels)):
		incomp.append([])
		error = False
		for j in range(len(travels)):
			if travels[j] in travels[i].travelUncompatible:
				incomp[i].append(j)
				
	return incomp
	

