'CONCATENATION'


def concatenation(listedonnee):

    listedonnee = [12, 81, 23, 4, 10, 56]
    liste2 = []
    liste3 = []
    temp = []
    resultat = []

    for i in listedonnee:
        if len(str(i)) == 1:
            liste2.append(i % 10)
            liste3.append(i % 10)
    for i in listedonnee:
        defi = listedonnee.index(i)
        temp.append(liste2[defi] + liste3[defi])
    for i in listedonnee:
        if liste2.count(max(liste2)) >= 2:
            k = temp.index(max(temp))
            resultat.append(listedonnee[k])
            temp[k] = 0
            liste2[k] = 0
        else :
            m = liste2.index(max(liste2))
            resultat.append(listedonnee[m])
            temp[m] = 0
            liste2[m] = 0
    print(resultat)
