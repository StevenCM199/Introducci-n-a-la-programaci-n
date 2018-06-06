def listapar (lista):
    if isinstance (lista, list) and lista != []:
        return listapar_aux(lista, len(lista) ,0 ,[])  
    else:
        return "Error: el valor ingresado no es una lista"
    
def listapar_aux(lista, largo, indice, resultado):
    if indice == largo:
        return resultado
    elif lista[indice] % 2 == 0:
        return listapar_aux(lista, largo, indice + 1, resultado+[lista[indice]])
    else:
        return listapar_aux(lista, largo, indice + 1, resultado) 
