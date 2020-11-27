def syracuse(n):
    """ Retourne la liste des valeurs de la suite en partant de n jusqu'à 1 """
    li=[]
    while n>1:
        if n%2==0:
            n= n/2
        else:
            n=n*3 +1
        li.append(n)
    return li
print(syracuse(3))

question 2.6:
def grand_vol(n_max):
    m = 0
    g = 0
    for i in range(2, n_max):
           a =tempsVol(i)
           if len(a) >  g:
               g = len(a)
               m = i
    return m
print(grand_vol(10000))


question 2.7