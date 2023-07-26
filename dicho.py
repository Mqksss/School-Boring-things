#Cette fonction a pour but de trouver l'index du chiffre recherché dans la liste par recherche dichotomique

L = [2,4,4,4,5,5,11,13,18,21,23,45,54,57,59,64]

def dicho(L,x):
	#On définie la droite et la gauche.
	droite = len(L) - 1
	gauche = 0

	while gauche <= droite:
		#Ici on recherche le millieu de la liste.
		millieu = (((droite + gauche) + 1) // 2)
		if x > millieu:
			#Ici on a "si le nombre recherché est plus grand que le millieu, on le cherchera à droite."
			gauche = millieu + 1
		elif x < millieu:
			#Ici on a "si le nombre recherché est plus petit que le millieu, on le cherchera à gauche."
			droite = millieu - 1
		elif x not in L:
			return "L'element n'est pas dans la liste"
		else:
			return L.index(x)
	return -1
print (dicho(L,13))