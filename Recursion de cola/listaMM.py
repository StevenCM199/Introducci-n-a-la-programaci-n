#Recibe una lista y devuelve el numero mayor y el numero menor de la lista
#con indices

def listaMM(lista):
    if isinstance (lista, list):
        return Mayor_aux(lista, 1, lista[0]), Menor_aux(lista, 1, lista[0])
    else:
        return "Error"


def Mayor_aux(lista, indice, mayor):
    if indice == len(lista):
        return mayor
    elif lista[indice] >= mayor:
        return Mayor_aux(lista, indice + 1, lista[indice])
    else:
        return Mayor_aux(lista, indice + 1, mayor)


def Menor_aux(lista, indice, menor):
    if indice == len(lista):
        return menor
    elif lista[indice] <= menor:
        return Menor_aux(lista, indice + 1, lista[indice])
    else:
        return Menor_aux(lista, indice + 1, menor)

