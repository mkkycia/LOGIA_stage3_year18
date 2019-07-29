from math import *

def dzielniki(a,b):
    a = ceil(sqrt(a))
    b = floor(sqrt(b))
    pierwsze = [x for x in range(3,b+1,2)]
    i = 0
    d = 3
    while d * d <= b:
        for j in range(d, b//d+1):
            if j * d in pierwsze:
                pierwsze.remove(j*d)
        i += 1
        d = pierwsze[i]
    print(pierwsze)
    pierwsze.insert(0,2)
    i = 0
    j = len(pierwsze)-1
    while i < j:
        s = (i+j)//2
        if pierwsze[s] < a:
            i=s+1
        else:
            j = s
    return len(pierwsze)-i
