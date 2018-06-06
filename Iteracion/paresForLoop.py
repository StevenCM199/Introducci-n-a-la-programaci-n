#Agrupar numeros entre listas de pares e impares
#Usando For Loop 

def pares(lista):
    if isinstance(lista, list) and lista != []:
        return pares_impares_aux(lista)

def pares_impares_aux(lista):
    listaPares = []
    listaImpares = []
    for valor in lista: #establece un loop entre las lineas de codigo identadas
        if (valor % 2 == 0): 
            listaPares += [valor]
        else: listaImpares += [valor]
    return listaPares, listaImpares #cuando llega al final de la lista, devuelve las variables
