import numpy as np
temp = 36.5
lista=[]
#print(type(lista))
for x in np.arange(35.0, 42.5, 0.5):
#    print(x)
    lista.append(x)
#print(lista)
#print("Apartados D:" + "\n")
i = 0
while i < len(lista):

    if lista[i] == temp:
        lista[i] = "36.5*"
    else:
     pass#print(str(lista[i]))
    i = i + 1
print(lista)




