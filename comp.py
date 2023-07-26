
L = [1,3,19,8,5,2,9]

def comp(L):
    compt = 0
    for i in range (len(L)):
        res = []
        if i+1 > (L[0]+1):
            res.append(i)
            compt = compt+1
    return res
print(comp(L))