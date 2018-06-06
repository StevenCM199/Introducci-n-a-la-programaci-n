def busqueda(num, lista):
    if isinstance (num,int) and (lista,list):
        return busqueda_aux(num, lista, len(lista)//2)
    else:
        return "Error" 


def busqueda_aux(num, lista, indice):
    if indice == -1 or indice == len(lista):
        return False
    
    elif num == lista[indice]:
        return True

    elif num > lista[indice]:
        return busqueda_aux(num, lista, indice + 1)
    
    elif num < lista[indice]:
        return busqueda_aux(num, lista, indice - 1)

