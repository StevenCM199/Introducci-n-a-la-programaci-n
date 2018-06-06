
def listaMM(lista):
    if isinstance (lista, list):
        return Mayor_aux(lista, lista[0]), Menor_aux(lista, lista[0])
    else:
        return "Error"

def Mayor_aux(lista, mayor):
    if lista == []:
        return mayor
    elif lista[0] > mayor:
        return Mayor_aux(lista[1:], lista[0])
    else:
        return Mayor_aux(lista[1:], mayor)

def Menor_aux(lista, menor):
    if lista == []:
        return menor
    elif lista[0] < menor:
        return Menor_aux(lista[1:], lista[0])
    else:
        return Menor_aux(lista[1:], menor)

