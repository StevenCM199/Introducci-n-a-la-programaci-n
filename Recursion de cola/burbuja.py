#Ordenar una lista de mayor a menor(algoritmo burbuja)

#Si lista[0] > lista[1], se reasignan los valores de lista[0] a lista[1] y viceversa
#y asi sucesivamente con el resto de posiciones

def orden(lista):
    if isinstance (lista, list):
        return orden_aux(lista, 0, 0)
    else:
        return "Error"

def orden_aux(lista,indice1, indice2):
    if indice2 == len(lista) - 1:
        return lista
    elif indice1 == len(lista) - 1:
        return orden_aux(lista, 0, indice2 + 1)
    elif lista[indice1] > lista[indice1 + 1]:
        aux = lista[indice1]
        lista [indice1] = lista [indice1 + 1]
        lista [indice1 + 1] = aux

    return orden_aux(lista, indice1 + 1, indice2)
