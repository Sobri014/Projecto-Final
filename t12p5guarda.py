import os
import pickle


class ListaTemperatura():
    def __init__(self):
        self.temperatura = []
    def add(self):
        print("Introduzca un numero:")
        num = float(input())
        if num > 35.0 and num < 42.0:
            self.temperatura.append(num)
LT = []
LT = ListaTemperatura()
LT.add()
LT.add()
LT.add()
LT.add()
LT.add()
LT.add()
LT.add()
print(LT.temperatura)
os.chdir('t12p4-copia.py')
fh = 'FicheroLista.txt'
fh = open('FicheroLista.txt','wb')
pickle.dump(LT.temperatura, fh)
fh.close()
