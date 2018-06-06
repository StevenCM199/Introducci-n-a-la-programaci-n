def lista2(lista):
    if isinstance (lista,list) and lista!= []:
        return lista2_aux (lista, len(lista), 1, 0)
    else:
        return "Error"

def lista2_aux (lista, largo, resultado, indice):
    if indice == largo:
        return resultado
    else:
        return lista2_aux(lista, largo, resultado * lista[indice], indice + 1)
