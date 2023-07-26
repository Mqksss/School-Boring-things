L = [-1,-3,5,8,9,-6,2,3,7,89,-2,3,-45]
k = L[0]
def Partition(L,k):
    g = 0 
    d = (len(L) - 1)
    while (g < d):
        while (L[g] < k and g<= d):
            g = g + 1
        while (L[d] > k and d>= g):
            d = d - 1
        if (g < d):
            tmp = L[g]
            L[g] = L[d]
            L[d] = tmp
    tmp = L[g]
    L[g] = L[d]
    L[d] = tmp

    return L,k

def compv2(L,k):
    L,k = Partition(L,k)
    dr = (len(L)-1)
    for i in range (len(L)):
        res = []
        dr2 = dr -1
        if i > dr2:
            res.append(i+1)
        return L,res,dr2
print(compv2(L,k))