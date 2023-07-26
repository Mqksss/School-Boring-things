'LISTE SYMETRIQUE ?'

def symetrie():

    vrai = 0
    faux = 0

    liste = [1,2,3,4,4,3,2,1] 

    if liste == liste[::-1] :
        vrai = True
        print("La liste est symetrique")
    else:
        faux = False
        print("La liste n'est pas symetrique")

if __name__ == '__main__' :
    symetrie()