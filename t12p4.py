import os
import shutil
nombreCarpeta = 't12p4-copia.py'

if os.path.exists(nombreCarpeta) == False:
    os.mkdir(nombreCarpeta)
os.chdir(nombreCarpeta)
print(os.getcwd())
fh = 'copia.txt'
fh = open('copia.txt',"w")
fh.writelines(["#","\n", "# Inicio de mi programa python","\n","#","\n","\n"])
fh.close()


fh = open('copia.txt',"a")
fh.writelines(["#","\n","# Fin de mi programa python","\n","#"])
fh.close()