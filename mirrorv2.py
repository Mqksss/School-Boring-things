def mirroir(a,k):
    #resul : résultat
    #r : reste
    #nbr : nbrchoisi
    
    resul = 0
    nbr = a
    while nbr > 0:
        
        r = nbr % 10 ** k
        nbr = nbr // 10 ** k
        resul = r + resul * 10
        
    return resul

print("Votre nombre mirroir est :", mirroir(5434567898,2))