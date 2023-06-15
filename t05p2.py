ListaTeam = []
def FuncionEquipo(Equipo,Jugadores):
    Lista = []
    for x in range(Jugadores):
        Lista.append(x)
    return Lista

def Representar(Lista):
    print( "Madrid: " + str(Lista))

ListaTeam = FuncionEquipo("Madrid: ", 5)

Representar(ListaTeam)