import os
import pickle
os.chdir('t12p4-copia.py')
print(os.getcwd())

fh_carga = open('FicheroLista.txt','rb')
ListaCarga = pickle.load(fh_carga)
print(type(ListaCarga))
print(ListaCarga)
fh_carga.close()

