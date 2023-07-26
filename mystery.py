# Mystery One 
n = 1234567
def long(n):
    res=0
    while res**10 <=n:
        res=res+1
        n = n * 10
    return res
print(long(n))