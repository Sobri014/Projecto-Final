
import numpy as np
temp = 36.5
lista = []
lista2 = []
h = bool
def funcion1(a, b):
    for x in np.arange(a, b + 0.5, 0.5):
        lista.append(x)
        #print(x)
    return lista
funcion1lambda = lambda lista2, x: lista2.append(x)
funcion1lambda(lista2, 10)
print(lista2)
funcion1(35.0, 42.0)

def funcion3(d):
    s = 0
    while s < len(d):
        if d[s] == temp:
            d[s] = "36.5*"
        s = s +1
    #print(d)
funcion3(lista)
funcionlambda = lambda x: x == temp
print(funcionlambda(36.5))
#print("Apartado e:")
def funcion4(e,T, z):

    s = 0
    while s < len(e):
        z = bool
        if e[s] == temp:
            z = true
            return z
            break
        else:
            return z
        s = s + 1
    #print(e)
funcion4(lista, temp, h)
if h:
    pass #print("encontrado")continue
else:
    pass