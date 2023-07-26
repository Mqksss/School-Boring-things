'PALINDROMES'

def separation(mot, a, b, resultat):
    while a >= 0 and b < len(mot) and mot[a] == mot[b]:
        resultat.add(mot[a: b + 1])
        a = a - 1
        b = b + 1
 
def palindromes(s):
    resultat = set()
 
    for i in range(len(s)):
        separation(mot, i, i, resultat)
        separation(mot, i, i + 1, resultat)
    print(resultat, end='')
 
if __name__ == '__main__':
    mot = [1,2,3,3,2,1]
    palindromes(mot)