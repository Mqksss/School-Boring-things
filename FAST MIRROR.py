'FAST MIRROR ALGORITHM'

def mirroir(a):

#J'ai essayé mon code avec plus de 200000 digits, le temps de calcul se situe aux alentours des 45 sec.
#Par la suite j'ai essayé avec 1 million de digits, le temps de calcul était de 12 minutes.
#(A noter que tous les tests on été réalisés avec mon ordinateur personnel)

    #resul : résultat
    #r : reste
    #nbr : nbrchoisi
    
    resul = 0
    nbr = a
    while nbr > 0:
        
        r = nbr % 10
        nbr = nbr // 10
        resul = r + resul * 10
        
    return resul


