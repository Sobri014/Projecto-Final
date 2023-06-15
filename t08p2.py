from functools import reduce

import numpy as np
lista = []
def funcion1(a, b):
    for x in np.arange(a, b + 0.5, 0.5):
        lista.append(x)
        #print(x)
    return lista
funcion1(35.0,42.0)
print(lista)
def suma01(a):
    a = a +0.01
    return a
Lambda = map(suma01, lista)
print(str(list(Lambda)),"\n")
print(reduce(lambda a, b: a+b, lista))
print(reduce(lambda a, b:reduce(lambda a, b: a+b, lista)/len(lista) , lista))
def myFunc(x):
    if x-int(x) == 0.5:
        return False
    else:
        return True
num = filter(myFunc, lista)
for x in num:
    print(x)

