#Cette fonction est la même que la fonction de recherche par dichotomie, cependant elle est recursive.

L = [2,4,4,4,5,5,11,13,18,21,23,45,54,57,59,64]

def dicho_recur(L,x,gauche,droite):
	if gauche <= droite :
		millieu = (((droite + gauche) + 1) // 2)
		if x > millieu:
			return dicho_recur(L,x,millieu,millieu - 1)
		elif x < millieu:
			return dicho_recur(L,x,millieu,millieu - 1)
		elif x not in L:
			return "L'element n'est pas dans la liste"
	return dicho_recur(L,x,gauche,droite)
print (dicho_recur(L,13,0,len(L)))

