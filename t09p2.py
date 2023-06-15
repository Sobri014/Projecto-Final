lista = []
num = 35.5


def genera_temp():
    num = 35.5
    while True:
        yield num
        num += 0.5
def escribe_algo(num):
    def generando():
        return"Generando lista"
    def Final():
        return "Ha superado el límite de 42.0"
    if num == 42.0:
        return print(Final())
    else:
        return print(generando())


for i in genera_temp():


    if i < 42.5:
        escribe_algo(i)
        lista.append(i)
    else:
        break
print(lista)
