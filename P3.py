def doblar_valor(numero):
    numero *= 2

n = 10
doblar_valor(n)
print(n)

def doblar_valores(numeros):
    for i,n in enumerate(numeros):
        numeros[i] *= 2

ns = [10,50,100]
doblar_valores(ns)
print(ns)

def doblar_valor(numero):
    return numero * 2

n = 10
n = doblar_valor(n)
print(n)

def doblar_valores(numeros):
    for i,n in enumerate(numeros):
        numeros[i] *= 2

ns = [10,50,100]
doblar_valores(ns[:])  # Una copia al vuelo de una lista con [:]
print(ns)