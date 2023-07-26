'TRI SELECTIF'

#Cette fonction à pour but de trier une liste dans le sens croissant.

#On initialise la liste à trier :

L= [12,6,3,9,14,7,16]

def triselec(L):
    long = len(L)
    
    #La double boucle est caractéristique du tri de liste
    for number in range (long):
        min = number
        for k in range(number, long):
            #ici on parcours la liste en fonction du nombre output au dessus.
            if L[min] > L[k]:
                min = k
            else:
                pass
        #C'est ici que la liste est triée.
        var = L[number]
        L[number] = L[min]
        L[min] = var

    return L
print (triselec(L))