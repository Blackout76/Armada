def updateList(liste1, liste2):
	# la liste 1 a maj a partir de la liste 2 .... liste1 - liste2 si meme valeur
	copyL1 = copy.deepcopy(liste1)
	copyL2 = copy.deepcopy(liste2)

	for i in range(len(copyL2)):
		for j in range(len(copyL1)):
			if copyL2[i] == copyL1[j]:
				del copyL1[j]
				break
	return copyL1	